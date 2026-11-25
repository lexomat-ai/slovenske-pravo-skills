"""Validate SKILL.md files, marketplace.json and the PR provenance label.

Usage:
    python scripts/validate_skills.py [--labels L1,L2 --changed-files F1 F2 ...]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PROVENANCE = {"ai-generated", "ai-assisted", "human"}
REVIEW_STATUS = {"unreviewed", "reviewed"}
DISCLAIMER = "nie je právna rada"
AI_LABEL = "ai-generated"
SKILL_PATH_RE = re.compile(r"^plugins/([^/]+)/skills/([^/]+)/")


def _parse(skill_md: Path) -> tuple[dict[str, object] | None, str, str | None]:
    """Return (frontmatter, body, error)."""
    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "", "frontmatter must start with '---' on the first line"
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None, "", "frontmatter has no closing '---'"
    try:
        data = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError as exc:
        return None, "", f"frontmatter is not valid YAML: {exc}"
    if not isinstance(data, dict):
        return None, "", "frontmatter must be a YAML mapping"
    return data, "\n".join(lines[end + 1 :]), None


def validate_skill(skill_md: Path) -> list[str]:
    data, body, err = _parse(skill_md)
    if err is not None or data is None:
        return [f"{skill_md}: {err}"]
    errors: list[str] = []

    name = data.get("name")
    if not isinstance(name, str) or not NAME_RE.match(name) or len(name) > 64:
        errors.append("name must be [a-z0-9-], at most 64 characters")
    elif name != skill_md.parent.name:
        errors.append(f"name '{name}' must equal its folder '{skill_md.parent.name}'")

    desc = data.get("description")
    if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024:
        errors.append("description must be a non-empty string of at most 1024 characters")

    meta = data.get("metadata")
    if not isinstance(meta, dict):
        errors.append("metadata must be a mapping")
        meta = {}
    for key, value in meta.items():
        if not isinstance(value, str):
            errors.append(f"metadata.{key} must be a string (use a comma-separated string for lists)")
    meta_s = {k: v for k, v in meta.items() if isinstance(v, str)}

    provenance = meta_s.get("provenance")
    if provenance not in PROVENANCE:
        errors.append(f"metadata.provenance must be one of {sorted(PROVENANCE)}")
    elif provenance.startswith("ai-") and not meta_s.get("generated_by", "").strip():
        errors.append("metadata.generated_by is required when provenance is ai-*")

    status = meta_s.get("review_status")
    if status not in REVIEW_STATUS:
        errors.append(f"metadata.review_status must be one of {sorted(REVIEW_STATUS)}")
    elif status == "reviewed" and not meta_s.get("reviewed_by", "").strip():
        errors.append("metadata.reviewed_by is required when review_status is reviewed")

    if DISCLAIMER not in body.lower():
        errors.append(f"body must contain '{DISCLAIMER}'")

    return [f"{skill_md}: {e}" for e in errors]


def _has_exact(folder: Path, filename: str) -> bool:
    """Case-exact presence check (macOS/Windows filesystems ignore case)."""
    return folder.is_dir() and filename in {p.name for p in folder.iterdir()}


def _manifest_name(root: Path, folder: str) -> str | None:
    path = root / "plugins" / folder / ".claude-plugin" / "plugin.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    name = data.get("name") if isinstance(data, dict) else None
    return name if isinstance(name, str) else None


def validate_marketplace(root: Path) -> list[str]:
    path = root / ".claude-plugin" / "marketplace.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [f"{path}: missing"]
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON: {exc}"]
    if not isinstance(data, dict) or not isinstance(data.get("plugins"), list):
        return [f"{path}: must be an object with a 'plugins' list"]
    listed: set[str] = set()
    errors: list[str] = []
    for entry in data["plugins"]:
        if not isinstance(entry, dict) or not isinstance(entry.get("source"), str):
            errors.append(f"{path}: each plugin must be an object with a string 'source' (got {entry!r})")
            continue
        source = entry["source"]
        folder = source.removeprefix("./plugins/").strip("/")
        listed.add(folder)
        if not (root / "plugins" / folder).is_dir():
            errors.append(f"{path}: plugin '{entry.get('name')}' has no folder at {source}")
            continue
        manifest = _manifest_name(root, folder)
        if manifest is not None and manifest != entry.get("name"):
            errors.append(
                f"{path}: entry name '{entry.get('name')}' differs from plugin.json name '{manifest}'"
            )
    plugins_dir = root / "plugins"
    present = {p.name for p in plugins_dir.iterdir() if p.is_dir()} if plugins_dir.is_dir() else set()
    for folder in sorted(present - listed):
        errors.append(f"{path}: plugin folder '{folder}' is not listed")
    return errors


def validate_layout(root: Path) -> list[str]:
    """Every plugin folder has a plugin.json; every skill folder has a SKILL.md."""
    errors: list[str] = []
    for plugin in sorted(p for p in (root / "plugins").glob("*") if p.is_dir()):
        manifest = plugin / ".claude-plugin" / "plugin.json"
        if not manifest.is_file():
            errors.append(f"{manifest}: missing")
        elif _manifest_name(root, plugin.name) is None:
            errors.append(f"{manifest}: must be JSON with a string 'name'")
        for skill in sorted(s for s in (plugin / "skills").glob("*") if s.is_dir()):
            if not _has_exact(skill, "SKILL.md"):
                errors.append(f"{skill}: skill folder has no SKILL.md")
    return errors


def check_pr_labels(changed_files: list[str], labels: list[str], root: Path) -> list[str]:
    skills = sorted({m.group(0) for f in changed_files if (m := SKILL_PATH_RE.match(f))})
    has_label = AI_LABEL in labels
    errors: list[str] = []
    for skill_dir in skills:
        skill_md = root / skill_dir / "SKILL.md"
        if not (root / skill_dir).is_dir():
            continue  # deleted skill
        if not _has_exact(root / skill_dir, "SKILL.md"):
            errors.append(f"{skill_dir}: skill folder has no SKILL.md")
            continue
        data, _, err = _parse(skill_md)
        meta = data.get("metadata") if data else None
        provenance = meta.get("provenance") if isinstance(meta, dict) else None
        is_ai = isinstance(provenance, str) and provenance.startswith("ai-")
        if is_ai and not has_label:
            errors.append(f"{skill_dir}: provenance '{provenance}' requires the '{AI_LABEL}' PR label")
        if has_label and not is_ai:
            errors.append(f"{skill_dir}: PR has the '{AI_LABEL}' label but this skill's provenance is '{provenance}'")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--labels", default=None, help="comma-separated PR labels; enables the label check")
    parser.add_argument("--changed-files", nargs="*", default=[])
    args = parser.parse_args(argv)
    root: Path = args.root

    errors = validate_marketplace(root) + validate_layout(root)
    for skill_md in sorted(root.glob("plugins/*/skills/*/SKILL.md")):
        errors += validate_skill(skill_md)
    if args.labels is not None:
        labels = [x.strip() for x in args.labels.split(",") if x.strip()]
        errors += check_pr_labels(args.changed_files, labels, root)

    for e in errors:
        print(f"ERROR {e}")
    print(f"{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
