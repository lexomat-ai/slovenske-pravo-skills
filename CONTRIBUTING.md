# Ako prispieť

Vítame skills od advokátov, koncipientov, právnikov aj vývojárov.

## Nový skill

1. Vyberte odvetvie v `plugins/<odvetvie>/` (napr. `trestne-pravo`). Nové odvetvie pridajte aj do
   `.claude-plugin/marketplace.json` a vytvorte `plugins/<odvetvie>/.claude-plugin/plugin.json`.
   Inštitúcie (napr. verejný ochranca práv) nie sú odvetvie, uveďte ich v `tags`.
2. Vytvorte `plugins/<odvetvie>/skills/<nazov-skillu>/SKILL.md`. Názov: malé písmená bez diakritiky, číslice a
   pomlčky, rovnaký ako názov priečinka.
3. Hlavička (hodnoty v `metadata` sú vždy reťazce; zoznamy oddeľujte čiarkou):

   ```yaml
   ---
   name: nazov-skillu
   description: Čo skill robí a kedy ho použiť (max. 1024 znakov).
   license: MIT
   metadata:
     provenance: human            # ai-generated | ai-assisted | human
     generated_by: ""             # model, ak provenance je ai-*
     authors: "vas-github-login"
     reviewed_by: ""              # kto skill odborne skontroloval
     review_status: unreviewed    # unreviewed | reviewed
     tags: "odvetvie,tema"
     requires: "lexoma"           # voliteľné
   ---
   ```
4. Telo musí obsahovať vetu „nie je právna rada“.
5. Overte lokálne: `uv run --with pyyaml --with pytest pytest -q && uv run --with pyyaml python scripts/validate_skills.py`

## Pôvod (AI vs. človek)

Pôvod každého skillu je v jeho súbore (`provenance`), lebo súbor putuje so skillom aj po inštalácii. PR so
skillmi vytvorenými s pomocou AI musí mať label `ai-generated`. CI skontroluje, že label a súbory súhlasia.
Skills generované AI commituje účet `lexomat-ai`; ľudia commitujú zo svojich účtov.

## Odborná kontrola

`review_status: reviewed` znamená, že skill skontroloval advokát alebo právnik uvedený v `reviewed_by`. Kým
sa tak nestane, skill je označený ako neskontrolovaný.

## Čo nikdy

Žiadne údaje o klientoch, spisoch ani osobné údaje, ani v príkladoch.

Príspevkom súhlasíte, že ho poskytujete pod licenciou MIT tohto repozitára.
