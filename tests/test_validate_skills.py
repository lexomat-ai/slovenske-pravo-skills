import json
from pathlib import Path

from validate_skills import check_pr_labels, validate_marketplace, validate_skill

GOOD_META = """  provenance: ai-generated
  generated_by: claude-fable-5-2
  authors: ""
  reviewed_by: ""
  review_status: unreviewed
"""
BODY = "\n# Skill\n\nPostup...\n\nTento výstup nie je právna rada.\n"


def make_skill(root: Path, plugin: str, name: str, meta: str = GOOD_META, *,
               folder: str | None = None, body: str = BODY, raw: str | None = None) -> Path:
    d = root / "plugins" / plugin / "skills" / (folder or name)
    d.mkdir(parents=True, exist_ok=True)
    text = raw if raw is not None else (
        f"---\nname: {name}\ndescription: Kontrola niečoho.\nmetadata:\n{meta}---\n{body}"
    )
    (d / "SKILL.md").write_text(text, encoding="utf-8")
    return d / "SKILL.md"


def make_marketplace(root: Path, plugins: list[str]) -> None:
    (root / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    data = {"name": "x", "owner": {"name": "x"},
            "plugins": [{"name": p, "source": f"./plugins/{p}"} for p in plugins]}
    (root / ".claude-plugin" / "marketplace.json").write_text(json.dumps(data))


def test_valid_skill_passes(tmp_path: Path) -> None:
    assert validate_skill(make_skill(tmp_path, "p", "dobry-skill")) == []


def test_name_must_match_folder(tmp_path: Path) -> None:
    errs = validate_skill(make_skill(tmp_path, "p", "iny-nazov", folder="priecinok"))
    assert any("folder" in e for e in errs)


def test_name_rejects_diacritics(tmp_path: Path) -> None:
    errs = validate_skill(make_skill(tmp_path, "p", "lehoty-v-konaní"))
    assert any("[a-z0-9-]" in e for e in errs)


def test_missing_closing_fence(tmp_path: Path) -> None:
    errs = validate_skill(make_skill(tmp_path, "p", "x", raw="---\nname: x\ndescription: y\n"))
    assert len(errs) == 1 and "frontmatter" in errs[0]


def test_non_mapping_frontmatter(tmp_path: Path) -> None:
    errs = validate_skill(make_skill(tmp_path, "p", "x", raw="---\n- a\n- b\n---\nbody nie je právna rada\n"))
    assert len(errs) == 1 and "mapping" in errs[0]


def test_invalid_yaml(tmp_path: Path) -> None:
    errs = validate_skill(make_skill(tmp_path, "p", "x", raw="---\nname: [unclosed\n---\nbody\n"))
    assert len(errs) == 1 and "YAML" in errs[0]


def test_metadata_list_rejected(tmp_path: Path) -> None:
    meta = GOOD_META.replace('authors: ""', "authors: [a, b]")
    errs = validate_skill(make_skill(tmp_path, "p", "x", meta))
    assert any("comma-separated string" in e for e in errs)


def test_bad_provenance(tmp_path: Path) -> None:
    errs = validate_skill(make_skill(tmp_path, "p", "x", GOOD_META.replace("ai-generated", "robot")))
    assert any("provenance" in e for e in errs)


def test_ai_requires_generated_by(tmp_path: Path) -> None:
    meta = GOOD_META.replace("generated_by: claude-fable-5-2", 'generated_by: ""')
    errs = validate_skill(make_skill(tmp_path, "p", "x", meta))
    assert any("generated_by" in e for e in errs)


def test_reviewed_requires_reviewed_by(tmp_path: Path) -> None:
    meta = GOOD_META.replace("review_status: unreviewed", "review_status: reviewed")
    errs = validate_skill(make_skill(tmp_path, "p", "x", meta))
    assert any("reviewed_by" in e for e in errs)


def test_missing_disclaimer(tmp_path: Path) -> None:
    errs = validate_skill(make_skill(tmp_path, "p", "x", body="\nBez upozornenia.\n"))
    assert any("nie je právna rada" in e for e in errs)


def test_plugin_not_in_marketplace(tmp_path: Path) -> None:
    make_skill(tmp_path, "a", "x")
    make_skill(tmp_path, "b", "y")
    make_marketplace(tmp_path, ["a"])
    errs = validate_marketplace(tmp_path)
    assert any("'b'" in e and "not listed" in e for e in errs)


def test_marketplace_entry_without_folder(tmp_path: Path) -> None:
    make_skill(tmp_path, "a", "x")
    make_marketplace(tmp_path, ["a", "ghost"])
    errs = validate_marketplace(tmp_path)
    assert any("ghost" in e and "no folder" in e for e in errs)


def test_ai_label_with_human_skill_fails(tmp_path: Path) -> None:
    make_skill(tmp_path, "p", "ai", GOOD_META)
    make_skill(tmp_path, "p", "clovek", GOOD_META.replace("ai-generated", "human"))
    changed = ["plugins/p/skills/ai/SKILL.md", "plugins/p/skills/clovek/SKILL.md"]
    errs = check_pr_labels(changed, ["ai-generated"], tmp_path)
    assert any("clovek" in e for e in errs)


def test_ai_skill_without_label_fails(tmp_path: Path) -> None:
    make_skill(tmp_path, "p", "ai", GOOD_META)
    errs = check_pr_labels(["plugins/p/skills/ai/SKILL.md"], [], tmp_path)
    assert any("ai-generated" in e for e in errs)


def test_matching_ai_label_passes(tmp_path: Path) -> None:
    make_skill(tmp_path, "p", "ai", GOOD_META)
    assert check_pr_labels(["plugins/p/skills/ai/SKILL.md"], ["ai-generated"], tmp_path) == []


def test_no_skill_changes_ignores_labels(tmp_path: Path) -> None:
    assert check_pr_labels(["README.md"], ["ai-generated"], tmp_path) == []


def test_deleted_skill_is_ignored(tmp_path: Path) -> None:
    assert check_pr_labels(["plugins/p/skills/zmazany/SKILL.md"], [], tmp_path) == []


def _plugin_json(root: Path, plugin: str, name: str | None = None) -> None:
    d = root / "plugins" / plugin / ".claude-plugin"
    d.mkdir(parents=True, exist_ok=True)
    (d / "plugin.json").write_text(json.dumps({"name": name or plugin}))


def test_skill_folder_without_skill_md(tmp_path: Path) -> None:
    from validate_skills import validate_layout
    d = tmp_path / "plugins" / "p" / "skills" / "bez"
    d.mkdir(parents=True)
    (d / "skill.md").write_text("x")
    _plugin_json(tmp_path, "p")
    errs = validate_layout(tmp_path)
    assert any("bez" in e and "SKILL.md" in e for e in errs)


def test_label_check_flags_folder_without_skill_md(tmp_path: Path) -> None:
    d = tmp_path / "plugins" / "p" / "skills" / "bez"
    d.mkdir(parents=True)
    (d / "skill.md").write_text("x")
    errs = check_pr_labels(["plugins/p/skills/bez/skill.md"], [], tmp_path)
    assert any("SKILL.md" in e for e in errs)


def test_plugin_without_manifest(tmp_path: Path) -> None:
    from validate_skills import validate_layout
    make_skill(tmp_path, "p", "x")
    errs = validate_layout(tmp_path)
    assert any("plugin.json" in e for e in errs)


def test_marketplace_name_must_match_manifest(tmp_path: Path) -> None:
    make_skill(tmp_path, "p", "x")
    _plugin_json(tmp_path, "p", name="iny")
    make_marketplace(tmp_path, ["p"])
    errs = validate_marketplace(tmp_path)
    assert any("'iny'" in e for e in errs)


def test_marketplace_malformed_shapes(tmp_path: Path) -> None:
    (tmp_path / ".claude-plugin").mkdir()
    mp = tmp_path / ".claude-plugin" / "marketplace.json"
    for bad in ("[]", '{"plugins": ["x"]}', '{"plugins": {}}'):
        mp.write_text(bad)
        errs = validate_marketplace(tmp_path)
        assert errs and all(e.startswith(str(mp)) for e in errs), bad


# --- robustness (review follow-ups) ---

def test_bom_prefixed_file_passes(tmp_path: Path) -> None:
    p = make_skill(tmp_path, "p", "s-bom")
    p.write_bytes(b"\xef\xbb\xbf" + p.read_bytes())
    assert validate_skill(p) == []


def test_crlf_line_endings_pass(tmp_path: Path) -> None:
    p = make_skill(tmp_path, "p", "s-crlf")
    p.write_bytes(p.read_bytes().replace(b"\n", b"\r\n"))
    assert validate_skill(p) == []


def test_decomposed_unicode_disclaimer_passes(tmp_path: Path) -> None:
    import unicodedata
    body = unicodedata.normalize("NFD", "\nTento výstup nie je právna rada.\n")
    assert validate_skill(make_skill(tmp_path, "p", "s-nfd", body=body)) == []


def test_disclaimer_variants_pass(tmp_path: Path) -> None:
    for i, body in enumerate([
        "\nVýstupy nie sú právna rada.\n",
        "\nTento výstup nie je právnou radou.\n",
        "\nTento výstup nie je\nprávna rada.\n",
    ]):
        assert validate_skill(make_skill(tmp_path, "p", f"s-var{i}", body=body)) == [], body


def test_negated_disclaimer_still_required(tmp_path: Path) -> None:
    errs = validate_skill(make_skill(tmp_path, "p", "s-none", body="\nToto je právna rada.\n"))
    assert any("nie je právna rada" in e for e in errs)


def test_missing_metadata_has_clear_message(tmp_path: Path) -> None:
    raw = "---\nname: s-nometa\ndescription: d\n---\nnie je právna rada\n"
    errs = validate_skill(make_skill(tmp_path, "p", "s-nometa", raw=raw))
    assert any("metadata is missing" in e for e in errs)


def test_label_match_ignores_case(tmp_path: Path) -> None:
    make_skill(tmp_path, "p", "s-ai")
    assert check_pr_labels(["plugins/p/skills/s-ai/SKILL.md"], ["AI-Generated"], tmp_path) == []


def test_workflow_diff_keeps_non_ascii_paths_unquoted() -> None:
    wf = (Path(__file__).parents[1] / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")
    assert "core.quotepath=false" in wf
