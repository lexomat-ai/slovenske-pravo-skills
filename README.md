# Slovenské právo — skills

Otvorená knižnica **Agent Skills** pre slovenské právo: postupy, ktoré AI asistentovi (Claude a ďalším
agentom podporujúcim formát `SKILL.md`) povedia, ako pracovať na konkrétnej právnej úlohe, napr. ako
skontrolovať premlčanie nároku.

> Výstupy agenta podľa týchto skills **nie sú právna rada**. Každý skill má vyznačený pôvod (AI / človek) a
> stav odbornej kontroly.

## Odporúčaný zdroj dát: LEXOMA

Skills fungujú aj samostatne, najlepšie však s konektorom **[LEXOMA](https://lexoma.sk)**. Ten agentovi
poskytuje aktuálne znenia slovenských predpisov a judikatúru, aby mohol overiť každý citovaný paragraf.
Bez konektora skill na neoverené citácie upozorní.

Za knižnicou stojí tím **[Lexomat](https://lexomat.sk)**. Na lexomat.sk pripravujeme zobrazenie skills
v profiloch ich autorov a recenzentov.

## Štruktúra

```
plugins/<odvetvie>/skills/<skill>/SKILL.md
```

Každé odvetvie (napr. `obcianske-pravo`, `trestne-pravo`) je samostatný plugin, takže si môžete nainštalovať
len to, čo potrebujete. Zoznam je v `.claude-plugin/marketplace.json`.

| Odvetvie | Skills |
|---|---|
| obcianske-pravo | `kontrola-premlcania` |

## Inštalácia

**Všetci kódovací agenti naraz** (Claude Code, GitHub Copilot, Codex, Cursor, Gemini CLI a ďalší, cez
[skills CLI](https://github.com/vercel-labs/skills)):

```
npx skills add lexomat-ai/slovenske-pravo-skills        # nainštaluje skills do zistených agentov
npx skills add lexomat-ai/slovenske-pravo-skills --list # len vypíše dostupné skills
npx skills update                                        # aktualizácia na najnovšiu verziu
```

**Claude Code** (ako plugin):

```
/plugin marketplace add lexomat-ai/slovenske-pravo-skills
/plugin install obcianske-pravo@slovenske-pravo-skills
```

Automatická aktualizácia je pri marketplaces tretích strán predvolene vypnutá. Zapnite ju v `/plugin` →
Marketplaces, alebo aktualizujte ručne: `/plugin marketplace update slovenske-pravo-skills`.

**Iní agenti:** priečinok skillu (`SKILL.md`) skopírujte do priečinka skills vášho agenta.

Návody pre claude.ai, Cowork, ChatGPT, Microsoft Copilot a Perplexity (nahranie skillu ako .zip) pripravujeme.
Nahraný skill sa v týchto aplikáciách sám neaktualizuje; sledujte **Watch → Releases**.

## Pôvod a kontrola

V hlavičke každého `SKILL.md` je `provenance` (`ai-generated`, `ai-assisted`, `human`) a `review_status`.
Skills generované AI commituje účet `lexomat-ai`, takže pôvod je viditeľný aj v histórii. Ako prispieť:
[CONTRIBUTING.md](CONTRIBUTING.md).

## Správcovia

- [@marosjanco](https://github.com/marosjanco)
- [@citbaj](https://github.com/citbaj)

## Licencia

[MIT](LICENSE). Licencia neudeľuje právo používať názvy ani logá LEXOMA a Lexomat.

---

## English

An open library of **Agent Skills** for Slovak law: procedures that tell an AI assistant how to handle a
specific legal task. The outputs are **not legal advice**; each skill records its provenance (AI or human) and
its review status. The skills work standalone and work best with the **[LEXOMA](https://lexoma.sk)** connector,
which gives the agent current Slovak legislation and case law for verifying citations. Maintained by the
**[Lexomat](https://lexomat.sk)** team. Install in Claude Code with
`/plugin marketplace add lexomat-ai/slovenske-pravo-skills`, or in any coding agent with
`npx skills add lexomat-ai/slovenske-pravo-skills`. Licence: MIT; it grants no rights to the
LEXOMA or Lexomat names or logos.
