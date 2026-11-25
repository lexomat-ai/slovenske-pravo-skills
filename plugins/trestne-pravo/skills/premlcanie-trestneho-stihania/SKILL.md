---
name: premlcanie-trestneho-stihania
description: Posúdi, či zanikla trestnosť činu premlčaním trestného stíhania podľa Trestného zákona (zákon č. 300/2005 Z. z., § 87 a 88, pri mladistvých § 96). Určí premlčaciu dobu podľa toho, či ide o prečin alebo zločin, a podľa hornej hranice trestnej sadzby, vrátane osobitných dôb pre trestné činy proti životu a zdraviu, slobode a ľudskej dôstojnosti, rodine a mládeži a iným právam a slobodám, pre trestné činy poškodzujúce finančné záujmy EÚ a pre činy spáchané na osobách mladších ako 18 rokov. Upozorní na nepremlčateľné trestné činy, na doby, ktoré sa do premlčacej doby nezapočítavajú, na prerušenie premlčania a na časovú pôsobnosť zákona. Premlčanie výkonu trestu len odlíši a odkáže na § 90 a 91. Použi, keď sa používateľ pýta, či sa skutok premlčal, dokedy ho možno stíhať, či vznesenie obvinenia alebo nový trestný čin premlčanie prerušili, alebo či je trestný čin nepremlčateľný.
license: MIT
metadata:
  provenance: ai-generated
  generated_by: claude-fable-5-2
  authors: ""
  reviewed_by: ""
  review_status: unreviewed
  tags: "trestne-pravo,trestny-zakon,premlcanie,zanik-trestnosti"
  requires: "lexoma"
---

# Premlčanie trestného stíhania (Trestný zákon)

Skill vychádza zo znenia zákona č. 300/2005 Z. z. (ďalej „TZ“) účinného od 18. 8. 2026. Trestný zákon sa od roku 2024 viackrát menil vrátane trestných sadzieb, preto vždy over znenie (krok Overenie).

## Kedy skill použiť

- Používateľ sa pýta, či sa skutok už premlčal alebo dokedy ho možno stíhať.
- Rieši, či vznesenie obvinenia, ďalšie úkony alebo nový trestný čin premlčanie prerušili.
- Pýta sa, či je trestný čin nepremlčateľný.

Nepoužívaj ho na procesné lehoty (skill `lehoty-v-trestnom-konani`) ani na premlčanie výkonu už uloženého trestu (len odkaz v kroku 7).

## Fakty, ktoré si vyžiadaj

Neposielaj do nástrojov mená ani iné osobné údaje; stačí právna kvalifikácia a dátumy.

1. **Právna kvalifikácia**: § a odsek TZ (základná alebo kvalifikovaná skutková podstata) a či ide o úmyselný čin alebo čin z nedbanlivosti.
2. **Dátum spáchania** (pri pokračovacom, trvácom alebo hromadnom čine dátum posledného útoku či skončenia protiprávneho stavu, § 122 ods. 10 až 12).
3. **Vek páchateľa** v čase činu (mladistvý?) a **vek obete**, ak ide o čin uvedený v § 87 ods. 5.
4. **Procesné udalosti**: vznesenie obvinenia a ďalšie úkony (dátumy), zrušenie obvinenia, prerušenie trestného stíhania, podmienečné zastavenie, dočasné odloženie vznesenia obvinenia, pobyt páchateľa v cudzine.
5. **Nové trestné činy** páchateľa počas premlčacej doby a ich kvalifikácia.
6. Deň, ku ktorému sa premlčanie posudzuje.

## Postup

### 1. Over, či nejde o nepremlčateľný čin (§ 88)

Nepremlčujú sa trestné činy z dvanástej hlavy osobitnej časti (trestné činy proti mieru, proti ľudskosti, trestné činy terorizmu, extrémizmu a vojnové) **okrem** § 417a až 417d, § 421, 422, 422a, 422b, 422c, 422d, 423 a 424. Ak je čin nepremlčateľný, skonči s týmto záverom.

### 2. Zaraď čin: prečin alebo zločin

- **Prečin**: čin z nedbanlivosti, alebo úmyselný čin s hornou hranicou sadzby trestu odňatia slobody neprevyšujúcou päť rokov (§ 10 ods. 1).
- **Zločin**: úmyselný čin s hornou hranicou prevyšujúcou päť rokov; aj ak ide o prísnejšiu skutkovú podstatu úmyselného prečinu s hornou hranicou nad päť rokov (§ 11 ods. 1 a 2).
- Rozhoduje sadzba v osobitnej časti TZ pre konkrétnu skutkovú podstatu. Sadzbu načítaj z aktuálneho znenia; nespoliehaj sa na pamäť.

### 3. Urči premlčaciu dobu

Všeobecné doby (§ 87 ods. 1):

| Čin | Doba |
|---|---|
| Zločin, za ktorý TZ dovoľuje uložiť doživotie | 30 rokov |
| Zločin s hornou hranicou sadzby **prevyšujúcou** 10 rokov | 15 rokov |
| Ostatné zločiny | 10 rokov |
| Prečin s hornou hranicou sadzby **prevyšujúcou** 3 roky | 5 rokov |
| Ostatné prečiny | 3 roky |

Osobitné pravidlá:
- **Prvá, druhá, tretia a deviata hlava osobitnej časti** (trestné činy proti životu a zdraviu, proti slobode a ľudskej dôstojnosti, proti rodine a mládeži, proti iným právam a slobodám): zločin s hornou hranicou **najmenej** 10 rokov sa premlčí za 20 rokov (namiesto § 87 ods. 1 písm. b)); prečin s hornou hranicou **najmenej** 3 roky za 5 rokov (namiesto písm. d)) (§ 87 ods. 6).
- **Finančné záujmy EÚ** (§ 213, 233, 237, 254, 261, 262, 266, § 276 ods. 4, § 277 ods. 4, § 277a ods. 3, § 326, 330 a 334, ak ich spáchaním dochádza k poškodzovaniu finančných záujmov EÚ): 20 rokov pri zločine s hornou hranicou najmenej 10 rokov, 10 rokov pri ostatných zločinoch, 5 rokov pri prečine s hornou hranicou najmenej 3 roky, 3 roky pri ostatných prečinoch (§ 87 ods. 7). Účinky prerušenia sa zachovajú aj pri neskoršom skrátení doby zákonom (§ 87 ods. 8).
- **Obete mladšie ako 18 rokov** pri činoch podľa § 159 ods. 2, § 179, 199, 200, 201 až 202, 208 a 368: trestné stíhanie sa premlčí najskôr 15 rokov po tom, čo obeť dovŕšila 18 rokov (§ 87 ods. 5). Vypočítaj obe doby a použi neskoršiu.
- **Mladistvý páchateľ**: 10 rokov pri čine, za ktorý TZ ustanovuje doživotie; 5 rokov, ak je horná hranica sadzby najmenej 10 rokov; 3 roky pri ostatných (§ 96 ods. 1); nepremlčateľnosť platí, kde to zákon ustanovuje (§ 96 ods. 2).

### 4. Začiatok plynutia

§ 87 TZ deň začiatku premlčacej doby výslovne neurčuje (okrem § 87 ods. 5). Deň začiatku pri jednotlivých formách činu (dokonanie, posledný čiastkový útok, skončenie trváceho stavu) over v judikatúre (`search_case_law`) a vo výstupe ho uveď ako predpoklad s odkazom na zdroj.

### 5. Odpočítaj doby, ktoré sa nezapočítavajú (§ 87 ods. 2)

- doba, po ktorú páchateľa nebolo možné postaviť pred súd pre zákonnú prekážku,
- doba, po ktorú sa páchateľ zdržiaval v cudzine s úmyslom vyhnúť sa trestnému stíhaniu,
- skúšobná doba podmienečného zastavenia trestného stíhania,
- doba dočasného odloženia vznesenia obvinenia,
- doba, po ktorú bolo trestné stíhanie prerušené.

Tieto doby premlčaciu dobu predlžujú; nezačína sa nová doba.

### 6. Zisti prerušenie (§ 87 ods. 3 a 4)

Premlčanie sa prerušuje:
- vznesením obvinenia pre daný trestný čin a po ňom nasledujúcimi riadnymi úkonmi orgánu činného v trestnom konaní, sudcu pre prípravné konanie alebo súdu smerujúcimi k trestnému stíhaniu obvineného, **okrem** prípadu, ak bolo obvinenie následne zrušené,
- spáchaním nového trestného činu v premlčacej dobe, za ktorý TZ ustanovuje trest rovnaký alebo prísnejší.

Prerušením sa začína **nová** premlčacia doba (§ 87 ods. 4).

### 7. Časová pôsobnosť a odlíšenie od premlčania výkonu trestu

- Trestnosť sa posudzuje podľa zákona účinného v čase činu; ak sa zákon do rozsudku zmenil, použije sa zákon pre páchateľa priaznivejší (§ 2 ods. 1). Pri čine spáchanom pred 15. 3. 2024 alebo pred inou zmenou TZ porovnaj znenia a prečítaj prechodné ustanovenia (§ 438k a ďalšie). Ak premlčanie nastalo pred účinnosťou TZ podľa doterajších predpisov, ustanovenia TZ o premlčaní sa nepoužijú (§ 437 ods. 4).
- **Premlčanie výkonu trestu** je iný inštitút: týka sa už uloženého trestu a má vlastné doby, začiatok aj prerušenie (§ 90, nepremlčateľnosť § 91, mladiství § 120). Ak sa používateľ pýta na výkon trestu, len naň odkáž; tento skill ho nepočíta.

## Overenie

- **Konektor LEXOMA (lexoma.sk) je pripojený**: cez `get_provision` (zákon „300/2005 Z. z.“) načítaj § 87, 88, prípadne § 96, a skutkovú podstatu s jej sadzbou, a to v znení účinnom ku dňu činu aj dnes. Pri zmene zákona použi `get_act` na prechodné ustanovenia. Začiatok plynutia a výklad „riadneho úkonu“ hľadaj cez `search_case_law`, rozhodnutia čítaj cez `get_decision` a citácie over cez `verify_citations`. Ak sa znenie líši od skillu, riaď sa aktuálnym znením a rozdiel uveď.
- **Konektor nie je pripojený alebo zlyhal**: do odpovede napíš „Citované ustanovenia neboli overené voči aktuálnemu zneniu Trestného zákona.“ a odporuč overenie na slov-lex.sk.
- Necituj § ani rozhodnutie, ktoré si neprečítal.

## Formát výstupu

1. **Záver**: trestné stíhanie je pravdepodobne premlčané / nepremlčané / čin je nepremlčateľný / nedá sa určiť bez údaja X.
2. **Kvalifikácia a sadzba**: § TZ, horná hranica, prečin či zločin (§ 10, § 11).
3. **Premlčacia doba** a ustanovenie, podľa ktorého sa určila.
4. **Začiatok plynutia** (s označením, že ide o predpoklad, ak nie je overený).
5. **Nezapočítané doby a prerušenia** s dátumami.
6. **Výpočet**: posledný deň premlčacej doby.
7. **Časová pôsobnosť**: ktoré znenie TZ sa použilo a prečo.
8. **Stav overenia**: overené cez LEXOMA k dátumu, alebo neoverené.
9. „Tento výstup nie je právna rada; posúdenie premlčania konzultujte s advokátom.“

## Časté chyby

- Použitie § 87 ods. 1 písm. b) alebo d) na čin z prvej, druhej, tretej alebo deviatej hlavy, kde platí § 87 ods. 6.
- Zámena „prevyšujúcou“ (§ 87 ods. 1) a „najmenej“ (§ 87 ods. 6 a 7): sadzba s hornou hranicou presne 10 rokov nespadá pod § 87 ods. 1 písm. b), ale spadá pod ods. 6.
- Prehliadnutie § 87 ods. 5 pri obetiach mladších ako 18 rokov.
- Pokračovanie v plynutí doby po prerušení namiesto začatia novej doby, alebo naopak pripočítanie nezapočítanej doby ako nového začiatku.
- Považovanie zrušeného obvinenia za prerušenie.
- Použitie doby podľa dnešného znenia na starší skutok bez porovnania znení (§ 2 ods. 1).
- Zámena premlčania trestného stíhania s premlčaním výkonu trestu (§ 90).
- Určenie sadzby z pamäti; sadzby sa od roku 2024 menili.

Tento výstup nie je právna rada; skill je pomôcka na orientáciu a nenahrádza posúdenie veci advokátom.
