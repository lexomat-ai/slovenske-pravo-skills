---
name: overenie-citacii
description: Pred odoslaním odpovede overí každú právnu citáciu v nej, teda paragrafy a články slovenských právnych predpisov, súdne rozhodnutia a judikatúru. S pripojeným konektorom LEXOMA (lexoma.sk) skontroluje citácie nástrojom verify_citations, načíta znenie ustanovení cez get_provision v znení účinnom k rozhodujúcemu dňu a rozhodnutia cez get_decision, porovná ich s tvrdeniami v odpovedi a označí zrušené, zmenené alebo neexistujúce ustanovenia a nenájdené rozhodnutia. Bez konektora používateľovi presne vymenuje, ktoré citácie overené neboli, a odkáže ho na slov-lex.sk. Použi vždy, keď odpoveď obsahuje odkaz na § alebo článok predpisu, číslo zákona, spisovú značku alebo iné označenie súdneho rozhodnutia, aj keď sa používateľ na overenie výslovne nepýta, a tiež keď používateľ chce skontrolovať citácie v cudzom texte (podanie, zmluva, posudok).
license: MIT
metadata:
  provenance: ai-generated
  generated_by: claude-fable-5-2
  authors: ""
  reviewed_by: ""
  review_status: unreviewed
  tags: "vseobecne,citacie,overovanie"
  requires: "lexoma"
---

# Overenie právnych citácií

## Kedy skill použiť

- Tvoja odpoveď obsahuje citáciu predpisu (napr. „§ 100 ods. 1 zákona č. 40/1964 Zb.“) alebo súdneho rozhodnutia (spisová značka „sp. zn. …“, ECLI, číslo publikovaného rozhodnutia).
- Používateľ ťa žiada skontrolovať citácie v texte, ktorý ti dal.
- Iný skill v postupe vyžaduje krok „Overenie“.

Skill je procedurálny: neurčuje, čo je obsahom práva, iba overuje, že to, čo citovaná pasáž tvrdí, sedí so zdrojom.

## Fakty, ktoré si vyžiadaj

1. **Rozhodujúci deň**: ku ktorému dňu sa vec posudzuje (deň právneho úkonu, udalosti, podania, rozhodnutia). Ak ho používateľ neuvedie, overuj k dnešnému dňu a výslovne to napíš.
2. Pri kontrole cudzieho textu: celý text alebo zoznam citácií. Osobné údaje strán nepotrebuješ; do nástrojov ich neposielaj, odstráň ich alebo nahraď zástupným textom.

## Postup

### 1. Vypíš všetky citácie

Prejdi celý návrh odpovede (alebo text používateľa) a vytvor zoznam. Každú citáciu zapíš v úplnom tvare:

- predpis: § / článok, odsek, písmeno, číslo a rok predpisu, zbierka (napr. „§ 100 ods. 1 zákona č. 40/1964 Zb.“);
- rozhodnutie: súd, spisová značka („sp. zn.“), dátum, prípadne ECLI.

Skratky („OZ“, „CSP“) rozviň na číslo predpisu. Citáciu, ktorú nevieš jednoznačne priradiť k predpisu alebo rozhodnutiu, označ ako **neurčitú** a nezahŕňaj ju do odpovede ako fakt.

### 2. Over citácie cez LEXOMA (ak je pripojená)

1. Celý zoznam pošli do `verify_citations`. Zaznamenaj, ktoré citácie nástroj potvrdil, ktoré nenašiel a ktoré označil ako problematické.
2. Pre každé ustanovenie, na ktorom odpoveď stojí, načítaj text cez `get_provision` v znení účinnom k rozhodujúcemu dňu. Ak sa rozhodujúci deň líši od dnešného, načítaj aj aktuálne znenie a porovnaj ich.
3. Porovnaj tvrdenie v odpovedi s načítaným textom: sedí číslo odseku a písmena, sedí obsah (lehota, suma, podmienka, výnimka)?
4. Pri rozhodnutiach načítaj text cez `get_decision` a over, že súd, spisová značka a dátum sedia a že rozhodnutie naozaj obsahuje citovaný právny názor. Ak rozhodnutie nevieš nájsť, skús `search_case_law`; ak ani tak, citáciu z odpovede vyraď.
5. Ak potrebuješ súvislosti predpisu (úvodné, prechodné alebo zrušovacie ustanovenia), použi `get_act`; ak potrebuješ nájsť správny predpis k téme, použi `search_legislation`.

### 3. Vyhodnoť stav každej citácie

| Stav | Kedy | Čo urobiť v odpovedi |
|---|---|---|
| Overená | text k rozhodujúcemu dňu potvrdzuje tvrdenie | ponechaj, uveď deň znenia |
| Zmenená | ustanovenie bolo novelizované; znenie k rozhodujúcemu dňu sa líši od aktuálneho | uveď obe znenia, novelu a dátum účinnosti; upozorni na prechodné ustanovenia |
| Zrušená | ustanovenie alebo predpis už neplatí | označ výslovne; ak sa vec posudzuje k dňu, keď platilo, vysvetli to |
| Ešte neúčinná | ustanovenie je vyhlásené, ale účinnosť nastane neskôr | označ dátum účinnosti |
| Nesedí obsah | ustanovenie existuje, ale hovorí niečo iné | oprav tvrdenie alebo citáciu, nie text zdroja |
| Nenájdená | nástroj ani vyhľadávanie ju nenašli | vyraď z odpovede alebo ju výslovne označ ako neoverenú |

Neopravuj citáciu „odhadom“ na iný paragraf. Ak správne ustanovenie nevieš nájsť a načítať, citáciu vyraď.

### 4. Bez LEXOMA

Ak konektor LEXOMA nie je pripojený alebo zlyhal:

- Citácie nevymýšľaj a neopravuj z pamäti; pamäť môže obsahovať staré znenie.
- V odpovedi uveď vetu: „Citované ustanovenia neboli overené voči aktuálnemu zneniu zákona.“
- Pod odpoveď daj zoznam **všetkých** citácií s označením „neoverené“ a pri každej, čo treba skontrolovať (číslo odseku, lehotu, účinnosť).
- Odkáž na slov-lex.sk (aktuálne a historické znenia predpisov) a pri rozhodnutiach na zdroj, ktorý ich zverejňuje (webové sídlo príslušného súdu).
- Spisové značky, ktoré si nevidel v zdroji, do odpovede nedávaj.

## Overenie

Pred odoslaním odpovede skontroluj:

- Každá citácia z kroku 1 má stav z kroku 3 (alebo „neoverené“ podľa kroku 4).
- Žiadna citácia so stavom „Nenájdená“ alebo „Nesedí obsah“ nezostala v odpovedi bez opravy alebo upozornenia.
- Pri každej overenej citácii je uvedený deň, ku ktorému bolo znenie načítané.
- Po úpravách odpovede si ešte raz spusti `verify_citations` na finálny text (ak je LEXOMA pripojená).

## Formát výstupu

Na koniec odpovede pridaj sekciu **Stav overenia citácií**:

```
Stav overenia citácií (znenie k DD.MM.RRRR, zdroj: LEXOMA | neoverené)
- § 100 ods. 1 zákona č. 40/1964 Zb.: overená
- § X ods. Y zákona č. N/RRRR Z. z.: zmenená novelou č. …, účinnou od …; použité znenie k …
- sp. zn. …: nenájdená, z odpovede vyradená
```

Ak overenie neprebehlo, sekcia obsahuje vetu „Citované ustanovenia neboli overené voči aktuálnemu zneniu zákona.“ a odkaz na slov-lex.sk. Záver odpovede: „Tento výstup nie je právna rada.“

## Časté chyby

- Overenie iba aktuálneho znenia, hoci sa vec posudzuje k skoršiemu dňu.
- Overenie, že § existuje, bez kontroly, či hovorí to, čo odpoveď tvrdí.
- Zámena „Zb.“ a „Z. z.“ alebo roku predpisu; zámena ods. a písm.
- Citovanie rozhodnutia podľa sekundárneho zdroja bez načítania jeho textu.
- Prehliadnutie, že ustanovenie je vyhlásené, ale ešte neúčinné.
- Tiché vynechanie neoverených citácií namiesto ich výslovného označenia.
- Posielanie mien alebo iných osobných údajov z textu používateľa do nástrojov.

Tento výstup nie je právna rada; overenie citácií nenahrádza posúdenie veci advokátom.
