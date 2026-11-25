---
name: lehoty-v-trestnom-konani
description: Určí a vypočíta lehoty na opravné prostriedky a súvisiace návrhy podľa Trestného poriadku (zákon č. 301/2005 Z. z.) - sťažnosť proti uzneseniu (§ 187), odvolanie proti rozsudku (§ 309), dovolanie (§ 370) a návrh na povolenie obnovy konania (§ 393 až 402, len pokiaľ ide o lehoty). Vysvetlí počítanie lehôt (§ 63), kedy je lehota zachovaná podaním na pošte alebo inde, navrátenie lehoty (§ 64) a rozdiely v plynutí lehoty pre obvineného, jeho obhajcu a zákonného zástupcu, poškodeného, prokurátora a ďalšie oprávnené osoby. Použi, keď sa používateľ pýta, dokedy môže podať sťažnosť, odvolanie alebo dovolanie v trestnej veci, od ktorého dňa lehota plynie, či stačí podať na pošte v posledný deň, čo robiť pri zmeškaní lehoty alebo či je obnova konania časovo obmedzená. Nerieši premlčanie trestného stíhania ani lehoty väzby.
license: MIT
metadata:
  provenance: ai-generated
  generated_by: claude-fable-5-2
  authors: ""
  reviewed_by: ""
  review_status: unreviewed
  tags: "trestne-pravo,trestny-poriadok,lehoty,opravne-prostriedky"
  requires: "lexoma"
---

# Lehoty v trestnom konaní (Trestný poriadok)

Skill vychádza zo znenia zákona č. 301/2005 Z. z. (ďalej „TP“) účinného od 18. 8. 2026. Ak riešiš úkon, ktorý sa stal skôr, alebo dnešný dátum je po zmene zákona, over použiteľné znenie (krok Overenie).

## Kedy skill použiť

- Používateľ chce vedieť, dokedy môže podať sťažnosť proti uzneseniu, odvolanie proti rozsudku alebo dovolanie.
- Pýta sa, od ktorého dňa lehota plynie, či stačí podať na pošte, čo ak lehota pripadne na víkend.
- Lehotu zmeškal a zvažuje navrátenie lehoty.
- Zvažuje návrh na povolenie obnovy konania a pýta sa, či je časovo obmedzený.

Nepoužívaj ho na lehoty väzby, premlčanie trestného stíhania (na to je skill `premlcanie-trestneho-stihania`) ani na civilné či správne konanie.

## Fakty, ktoré si vyžiadaj

Do nástrojov ani do výstupu nedávaj mená, čísla konaní ani iné osobné údaje; stačí druh rozhodnutia, procesné postavenie a dátumy.

1. **Druh rozhodnutia**: uznesenie (koho: policajt, prokurátor, súd), rozsudok, trestný rozkaz, iné; či ide o rozhodnutie o väzbe.
2. **Kto chce podať**: obvinený/obžalovaný, obhajca, zákonný zástupca, poškodený, zúčastnená osoba, prokurátor, príbuzný (§ 308 ods. 2), orgán sociálnoprávnej ochrany detí a sociálnej kurately; či ide o mladistvého.
3. **Ako a kedy bolo rozhodnutie oznámené**: vyhlásené v prítomnosti tejto osoby (dátum), alebo doručené (dátum doručenia, prípadne uloženia na pošte). Či má osoba obhajcu alebo splnomocnenca a kedy bolo doručené jemu.
4. **Ako sa podanie urobí**: na pošte, osobne, elektronicky (s kvalifikovaným elektronickým podpisom alebo bez neho), z väzby alebo z výkonu trestu.
5. **Pri zmeškaní**: aká prekážka bránila podaniu a kedy odpadla.

## Postup

### 1. Urči druh podania a lehotu

| Podanie | Lehota a začiatok | Kde sa podáva | § TP |
|---|---|---|---|
| Sťažnosť proti uzneseniu | 3 pracovné dni od oznámenia uznesenia | orgánu, proti ktorého uzneseniu smeruje | § 187 ods. 1 |
| Sťažnosť pri skrátenom vyšetrovaní (§ 204 ods. 1) | do skončenia skráteného vyšetrovania | tamže | § 187 ods. 1 |
| Sťažnosť podľa § 83 ods. 2 (nevzatie do väzby, prepustenie zatknutého; rozhodovanie podľa § 76 ods. 3, 4 alebo 10) | len ihneď po vyhlásení uznesenia | tamže | § 83 ods. 2 |
| Odvolanie proti rozsudku | 15 dní od oznámenia rozsudku | na súde, proti ktorého rozsudku smeruje | § 309 ods. 1 |
| Dovolanie v neprospech obvineného | 3 roky od doručenia rozhodnutia prokurátorovi | na súde, ktorý rozhodol v prvom stupni | § 370 ods. 1 a 3 |
| Dovolanie v prospech obvineného | 3 roky od doručenia rozhodnutia obvinenému (pri viacerých doručeniach od najneskoršieho) | tamže | § 370 ods. 1 a 3 |
| Dovolanie ministra spravodlivosti | 3 roky od doručenia vykonaného najneskôr | tamže | § 370 ods. 2 |
| Návrh na povolenie obnovy konania | v § 393 až 402 lehota ustanovená nie je; obnova v neprospech obvineného je vylúčená, ak trestnosť činu zanikla, na trest sa vzťahuje amnestia alebo obvinený zomrel | súd podľa § 397 | § 395, § 396 |
| Sťažnosť proti uzneseniu o návrhu na povolenie obnovy | ako pri sťažnosti (§ 187); má odkladný účinok | - | § 402 ods. 3 |

Sťažnosťou nemožno napadnúť uznesenie policajta o začatí trestného stíhania; uznesenie súdu alebo prokurátora len tam, kde to zákon výslovne pripúšťa (§ 185 ods. 2). Dovolanie môžu podať len osoby podľa § 369 a spravidla len ak využili riadny opravný prostriedok (§ 372 ods. 1). Poškodený medzi oprávnenými na dovolanie nie je; môže podať podnet ministrovi spravodlivosti (§ 369 ods. 1).

### 2. Urči deň, od ktorého lehota plynie

- **Oznámenie uznesenia**: vyhlásením v prítomnosti osoby alebo doručením rovnopisu (§ 179 ods. 1). Ak má osoba obhajcu alebo splnomocnenca a uznesenie sa doručuje, doručí sa len jemu (§ 179 ods. 2).
- **Oznámenie rozsudku**: vyhlásenie v prítomnosti toho, komu treba rozsudok doručiť; ak bol vyhlásený v jeho neprítomnosti, až doručenie (§ 309 ods. 1).
- **Uloženie zásielky**: písomnosť sa považuje za doručenú dňom uloženia, aj keď sa adresát o uložení nedozvedel (§ 65 ods. 3); pri poštovom priečinku platia pravidlá § 65 ods. 5.

### 3. Rozlíš lehotu podľa osoby

- **Obvinený s obhajcom alebo zákonným zástupcom**: ak sa oznamuje viacerým z nich, lehota plynie od oznámenia vykonaného najneskôr (sťažnosť § 187 ods. 1, odvolanie § 309 ods. 2, dovolanie § 370 ods. 1).
- **Osoby podávajúce v prospech obvineného** (napr. príbuzní podľa § 308 ods. 2): lehota im končí tým istým dňom ako obvinenému (§ 187 ods. 2, § 309 ods. 4).
- **Prokurátor**: pri sťažnosti mu lehota plynie vždy samostatne (§ 187 ods. 2); pri odvolaní sa naňho pravidlo o konci lehoty v ten istý deň ako obžalovanému nevzťahuje (§ 309 ods. 4).
- **Mladistvý obvinený**: zákonnému zástupcovi, obhajcovi a orgánu sociálnoprávnej ochrany detí a sociálnej kurately plynie lehota na sťažnosť samostatne (§ 186 ods. 1); orgánu pri odvolaní tiež (§ 309 ods. 3).
- **Poškodený**: odvolanie len proti výroku o náhrade škody (§ 307 ods. 1 písm. c), § 308 ods. 1); lehota 15 dní od oznámenia jemu (§ 309 ods. 1).
- **Späťvzatie prokurátorom**: ak prokurátor vezme späť sťažnosť alebo odvolanie podané v prospech obvineného, obvinenému plynie nová lehota od upovedomenia (§ 188 ods. 3, § 312 ods. 3, pri mladistvom § 313).

### 4. Vypočítaj koniec lehoty (§ 63)

- Do lehoty určenej podľa dní sa nezapočítava deň udalosti, ktorá určuje jej začiatok (§ 63 ods. 3).
- Lehota podľa týždňov, mesiacov alebo rokov sa skončí dňom, ktorý pomenovaním alebo číslom zodpovedá dňu udalosti; ak taký deň v mesiaci chýba, posledným dňom mesiaca (§ 63 ods. 4).
- Ak koniec pripadne na deň pracovného pokoja alebo pracovného voľna, posledným dňom je najbližší pracovný deň; neplatí to pre lehotu väzby (§ 63 ods. 5).
- Pri sťažnosti počítaj tri **pracovné** dni (§ 187 ods. 1).
- Ak je k dispozícii `compute_deadline`, použi ho, ale výsledok skontroluj ručným výpočtom podľa § 63.

### 5. Over, či podanie lehotu zachová (§ 63 ods. 6, § 62 ods. 1)

Lehota je zachovaná, ak bolo podanie v lehote:
- podané na pošte a adresované súdu, prokurátorovi alebo policajtovi, u ktorého sa má podať alebo ktorý má vo veci rozhodnúť,
- urobené na súde alebo u prokurátora, ktorý má vo veci rozhodnúť,
- urobené príslušníkom ozbrojených síl, ozbrojeného zboru alebo v služobnom pomere u nadriadeného alebo služobného orgánu,
- urobené u riaditeľa ústavu, v ktorom je podávajúci vo väzbe alebo vo výkone trestu,
- urobené ústne do zápisnice na ktoromkoľvek okresnom súde alebo u okresného prokurátora.

Podanie telegraficky, telefaxom alebo elektronicky bez kvalifikovaného elektronického podpisu treba do troch pracovných dní potvrdiť písomne alebo ústne do zápisnice, inak sa o ňom nekoná (§ 62 ods. 1).

### 6. Zmeškaná lehota

- **Navrátenie lehoty (§ 64)**: obvinenému, obhajcovi, poškodenému alebo zúčastnenej osobe, ktorí z dôležitých dôvodov zmeškali lehotu na opravný prostriedok. Žiadosť do troch dní od odpadnutia prekážky; ak opravný prostriedok ešte nebol podaný, spojiť ho so žiadosťou. Pri odvolaní proti rozsudku ho možno odôvodniť do ôsmich dní od doručenia uznesenia o povolení navrátenia. Rozhoduje orgán, ktorý rozhoduje o opravnom prostriedku. Prokurátor v § 64 ods. 1 uvedený nie je.
- **Nesprávne poučenie**: sťažnosť ani odvolanie nemožno zamietnuť ako oneskorené, ak bolo podané oneskorene len preto, že sa oprávnená osoba riadila nesprávnym poučením (§ 193 ods. 2, § 316 ods. 2).
- Inak sa oneskorená sťažnosť zamietne (§ 193 ods. 1 písm. b)), oneskorené odvolanie zamietne (§ 316 ods. 1) a oneskorené dovolanie odmietne (§ 382 písm. a)).

## Overenie

- **Konektor LEXOMA (lexoma.sk) je pripojený**: každé citované ustanovenie načítaj cez `get_provision` (zákon „301/2005 Z. z.“, číslo §) a porovnaj s týmto skillom; pri staršom úkone over znenie účinné v deň úkonu. Výpočet over cez `compute_deadline`. Otázky, ktoré zákon výslovne nerieši (napr. či sa § 64 vzťahuje aj na dovolanie), hľadaj cez `search_case_law` a citácie skontroluj cez `verify_citations`. Ak sa znenie líši od skillu, riaď sa aktuálnym znením a rozdiel uveď.
- **Konektor nie je pripojený alebo zlyhal**: do odpovede napíš „Citované ustanovenia neboli overené voči aktuálnemu zneniu Trestného poriadku.“ a odporuč overenie na slov-lex.sk.
- Necituj § ani rozhodnutie, ktoré si neprečítal.

## Formát výstupu

1. **Záver**: posledný deň lehoty (dátum) alebo „nedá sa určiť bez údaja X“.
2. **Podanie a lehota**: druh podania, dĺžka lehoty, kam sa podáva, § TP.
3. **Začiatok lehoty**: rozhodujúce oznámenie/doručenie a prečo, § TP.
4. **Výpočet** krok po kroku vrátane presunu z dňa pracovného pokoja.
5. **Ako lehotu zachovať**: spôsob podania podľa § 63 ods. 6, prípadne potvrdenie podľa § 62 ods. 1.
6. **Pri zmeškaní**: navrátenie lehoty a jeho lehota.
7. **Predpoklady a chýbajúce údaje**.
8. **Stav overenia**: overené cez LEXOMA k dátumu, alebo neoverené.
9. „Tento výstup nie je právna rada; lehotu si overte u advokáta, jej zmeškanie môže mať nezvratné následky.“

## Časté chyby

- Počítanie lehoty na sťažnosť v kalendárnych dňoch namiesto pracovných.
- Započítanie dňa oznámenia alebo doručenia do lehoty (§ 63 ods. 3).
- Počítanie od doručenia obvinenému, hoci sa doručovalo aj obhajcovi neskôr, alebo naopak.
- Predpoklad, že príbuzným obvineného plynie vlastná lehota; končí sa im v ten istý deň ako obvinenému.
- Prehliadnutie, že pri doručení uložením sa za deň doručenia považuje deň uloženia (§ 65 ods. 3).
- Odoslanie e-mailom bez kvalifikovaného podpisu a bez potvrdenia do troch pracovných dní.
- Tvrdenie, že poškodený môže podať dovolanie alebo odvolanie proti výroku o vine či treste.
- Uvádzanie lehoty na obnovu konania, ktorú v § 393 až 402 TP nenájdeš.

Tento výstup nie je právna rada; skill je pomôcka na orientáciu a nenahrádza posúdenie veci advokátom.
