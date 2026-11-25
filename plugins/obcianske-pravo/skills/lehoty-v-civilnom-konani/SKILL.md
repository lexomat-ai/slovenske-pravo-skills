---
name: lehoty-v-civilnom-konani
description: Určí a vypočíta procesné lehoty v civilnom sporovom konaní podľa Civilného sporového poriadku (zákon č. 160/2015 Z. z.). Pokrýva lehotu na odvolanie (15 dní), dovolanie (2 mesiace), odpor proti platobnému rozkazu (15 dní) a vyjadrenie k žalobe (lehota určená súdom), začiatok plynutia od doručenia vrátane fikcie doručenia, počítanie lehôt podľa dní a mesiacov, posun konca lehoty zo soboty alebo dňa pracovného pokoja, zachovanie lehoty odovzdaním podania pošte a odpustenie zmeškania lehoty. Na žalobu na obnovu konania a dovolanie generálneho prokurátora iba odkáže. Použi, keď sa používateľ pýta, dokedy môže podať odvolanie, dovolanie alebo odpor, dokedy sa má vyjadriť k žalobe, či stihne lehotu, ak podanie odošle poštou v posledný deň, odkedy plynie lehota pri nevyzdvihnutej zásielke, alebo čo robiť po zmeškaní lehoty. Nerieši trestné, správne ani mimosporové konanie a hmotnoprávne lehoty (premlčanie, preklúziu).
license: MIT
metadata:
  provenance: ai-generated
  generated_by: claude-fable-5-2
  authors: ""
  reviewed_by: ""
  review_status: unreviewed
  tags: "civilne-konanie,lehoty,odvolanie,dovolanie,platobny-rozkaz,csp"
  requires: "lexoma"
---

# Lehoty v civilnom sporovom konaní (CSP)

## Kedy skill použiť

- Používateľ potrebuje určiť posledný deň lehoty na odvolanie, dovolanie, odpor proti platobnému rozkazu alebo vyjadrenie k žalobe v spore podľa Civilného sporového poriadku (zákon č. 160/2015 Z. z., ďalej „CSP“).
- Používateľ sa pýta, odkedy lehota plynie, či ju zachová podaním na pošte alebo čo robiť po jej zmeškaní.

Nepoužívaj ho na mimosporové a správne súdne konanie, trestné konanie ani na hmotnoprávne lehoty (premlčanie, preklúzia).

## Fakty, ktoré si vyžiadaj

Pýtaj sa len na to, čo chýba. Do nástrojov neposielaj mená, spisové značky ani iné údaje o veci; stačia dátumy a druh rozhodnutia.

1. **Druh písomnosti**: rozsudok alebo uznesenie súdu prvej inštancie, rozhodnutie odvolacieho súdu, platobný rozkaz, výzva súdu na vyjadrenie k žalobe (a lehota v nej uvedená).
2. **Deň doručenia** a spôsob: prevzatie zásielky, nevyzdvihnutá zásielka vrátená súdu, odopretie prijatia, elektronická schránka, elektronická adresa.
3. **Zastúpenie**: či má strana zástupcu so splnomocnením na celé konanie (vtedy sa doručuje jemu, § 110 ods. 1 CSP).
4. **Poučenie v rozhodnutí**: aká lehota a aký súd sú v ňom uvedené, či poučenie chýba.
5. **Opravné uznesenie**: či bolo vydané a kedy doručené.
6. Pri zmeškanej lehote: **dôvod zmeškania** a deň, keď prekážka odpadla.

Ak deň doručenia nie je istý, počítaj od najskoršieho možného dňa a uveď to.

## Postup

### 1. Urči lehotu

| Úkon | Lehota | Začiatok | Ustanovenie CSP |
|---|---|---|---|
| Odvolanie proti rozhodnutiu súdu prvej inštancie | 15 dní | doručenie rozhodnutia | § 362 ods. 1 |
| Dovolanie proti rozhodnutiu odvolacieho súdu | 2 mesiace | doručenie rozhodnutia odvolacieho súdu oprávnenému subjektu | § 427 ods. 1 |
| Odpor proti platobnému rozkazu | 15 dní | doručenie platobného rozkazu | § 265 ods. 1 |
| Vyjadrenie k žalobe | lehota určená súdom, najmenej 15 dní, ak zákon neustanovuje inak; súd ju môže primerane predĺžiť | doručenie výzvy so žalobou | § 167 ods. 2, § 118 |

Kde sa podáva:
- Odvolanie: na súde, proti ktorého rozhodnutiu smeruje; včas je podané aj vtedy, ak bolo v lehote podané na príslušnom odvolacom súde (§ 362 ods. 1 a 2).
- Dovolanie: na súde, ktorý rozhodoval v prvej inštancii; včas je podané aj na príslušnom odvolacom alebo dovolacom súde (§ 427 ods. 1 a 2). Dovolateľ musí byť zastúpený advokátom a dovolanie musí spísať advokát, okrem výnimiek v § 429 ods. 2.

Ďalšie pravidlá:
- Opravné uznesenie: lehota na odvolanie aj dovolanie plynie znovu od jeho doručenia, ale len v rozsahu vykonanej opravy (§ 362 ods. 1, § 427 ods. 1).
- Nesprávne alebo chýbajúce poučenie o odvolaní: odvolanie je včas, ak sa odvolateľ spravoval nesprávnym poučením o lehote; ak poučenie o lehote chýba alebo nesprávne uvádza, že odvolanie nie je prípustné, možno ho podať do troch mesiacov od doručenia (§ 362 ods. 3). Podanie na nepríslušnom súde podľa nesprávneho alebo chýbajúceho poučenia o súde je tiež včas (§ 362 ods. 4).
- Rozsah napadnutia, odvolacie dôvody a dôkazy možno meniť a dopĺňať len do uplynutia lehoty na odvolanie (§ 364, § 365 ods. 3); rozsah dovolania len do uplynutia lehoty na dovolanie (§ 430).
- Intervenientovi plynie lehota na odvolanie od doručenia rozhodnutia jemu (§ 360 ods. 3).

### 2. Urči deň doručenia

- Doručenie do vlastných rúk potvrdzuje doručenka; jej údaje sa považujú za pravdivé, kým sa nedokáže opak (§ 111 ods. 1).
- Ak má strana zástupcu so splnomocnením na celé konanie, doručuje sa len jemu (§ 110 ods. 1); lehota sa počíta od doručenia zástupcovi.
- Ak písomnosť nemožno doručiť na adresu podľa § 106, považuje sa za doručenú dňom vrátenia nedoručenej zásielky súdu, aj keď sa o nej adresát nedozvie (§ 111 ods. 3, § 112).
- Pri bezdôvodnom odopretí prijatia je písomnosť doručená dňom odopretia (§ 113).
- Doručenie na elektronickú adresu na žiadosť strany: písomnosť sa považuje za doručenú po troch dňoch od odoslania (§ 105 ods. 2).
- Doručenie do elektronickej schránky upravuje osobitný predpis (§ 105 ods. 1). Deň doručenia v takom prípade over v ňom; tento skill ho nepočíta.
- **Platobný rozkaz** sa doručuje do vlastných rúk spolu so žalobou a fikcia podľa § 111 ods. 3 sa naň nepoužije (§ 266 ods. 1 a 2). Odpor teda plynie len od skutočného doručenia.

### 3. Vypočítaj posledný deň

- Lehota podľa dní: deň doručenia sa nezapočítava (§ 121 ods. 2). Prvým dňom je nasledujúci deň.
- Lehota podľa mesiacov: končí uplynutím dňa, ktorý sa označením zhoduje s dňom doručenia; ak ho v mesiaci niet, posledným dňom mesiaca (§ 121 ods. 3).
- Ak koniec pripadne na sobotu alebo deň pracovného pokoja, posledným dňom je najbližší nasledujúci pracovný deň (§ 121 ods. 4).
- Príklady: doručenie v pondelok 9. 3. 2026, odvolanie 15 dní → posledný deň utorok 24. 3. 2026. Doručenie 31. 12. 2025, dovolanie 2 mesiace → február nemá 31. deň, teda 28. 2. 2026, čo je sobota → posledný deň pondelok 2. 3. 2026.
- Lehota neplynie tomu, kto stratil procesnú subjektivitu alebo spôsobilosť samostatne konať (§ 119). Ak počas lehoty vstúpi do konania zákonný zástupca alebo procesný opatrovník, lehota plynie od jeho vstupu (§ 120).

### 4. Zachovanie lehoty

Lehota je zachovaná, ak sa v posledný deň urobí úkon na súde alebo sa podanie odovzdá orgánu, ktorý má povinnosť ho doručiť; platí to aj pre elektronické podanie doručené súdu mimo pracovného času (§ 121 ods. 5). Rozhoduje deň odovzdania, nie deň, keď zásielka príde na súd.

Elektronické podanie vo veci samej (napr. odvolanie, odpor, dovolanie) bez autorizácie treba do desiatich dní doručiť v listinnej podobe alebo autorizované; inak sa naň neprihliada a súd na to nevyzýva (§ 123 ods. 2, § 125 ods. 2).

### 5. Zmeškaná lehota

- Súd zmeškanie odpustí, ak ho strana, zástupca alebo procesný opatrovník zmeškal z ospravedlniteľného dôvodu a bol preto vylúčený z úkonu. Návrh treba podať do 15 dní po odpadnutí prekážky a spojiť s ním zmeškaný úkon (§ 122).
- Pri fikcii doručenia (§ 111 ods. 3, § 112) súd zmeškanie odpustí, len ak sa adresát z ospravedlniteľného dôvodu na adrese nezdržiaval a neporušil tým žiadnu právnu povinnosť (§ 114).
- Oneskorený odpor súd odmietne (§ 267 ods. 2 písm. a); platobný rozkaz nadobúda právoplatnosť márnym uplynutím lehoty na odpor (§ 268 písm. a).
- Nesplnenie povinnosti vyjadriť sa k žalobe môže viesť k rozsudku pre zmeškanie, ak súd túto povinnosť uložil uznesením doručeným do vlastných rúk s poučením o následkoch (§ 273). Ak žalovaný zmeškal lehotu z ospravedlniteľných dôvodov, môže do 15 dní odkedy sa o rozsudku dozvedel navrhnúť jeho zrušenie spolu s vyjadrením (§ 277 ods. 1 a 3).

### 6. Mimoriadne prostriedky (len odkaz)

Ak lehoty uplynuli, používateľa iba odkáž, nepočítaj:
- **Žaloba na obnovu konania**: § 397 a nasl. CSP, lehoty v § 403 a 404; zmeškanie lehoty na jej podanie nemožno odpustiť (§ 405).
- **Dovolanie generálneho prokurátora**: § 458 a nasl. CSP; generálny prokurátor ho podáva len na podnet strany (§ 458 ods. 3).

## Overenie

- **Konektor LEXOMA (lexoma.sk) je pripojený**: každý citovaný § načítaj nástrojom `get_provision` (zákon „160/2015 Z. z.“) a porovnaj s tým, čo tvrdíš; posledný deň lehoty prepočítaj nástrojom `compute_deadline`. Ak sa konanie začalo dávnejšie, upozorni, že rozhodujúce môžu byť prechodné ustanovenia. Ak sa znenie líši od tohto skillu, riaď sa aktuálnym znením a rozdiel uveď.
- **Konektor nie je pripojený alebo zlyhal**: do odpovede napíš vetu „Citované ustanovenia neboli overené voči aktuálnemu zneniu zákona.“ a odporuč overenie na slov-lex.sk.
- Dni pracovného pokoja (sviatky) over v aktuálnom predpise; nepočítaj s nimi spamäti.
- Necituj § ani súdne rozhodnutie, ktoré nie je v tomto skille a ktoré si si neoveril.

## Formát výstupu

1. **Záver**: posledný deň lehoty (dátum a deň v týždni), alebo „nedá sa určiť bez údaja X“.
2. **Úkon a lehota** s § CSP.
3. **Deň doručenia** a spôsob, ako bol určený (§).
4. **Výpočet** krok po kroku vrátane posunu zo soboty alebo dňa pracovného pokoja.
5. **Kde a ako podať**, vrátane zachovania lehoty na pošte a autorizácie elektronického podania.
6. **Riziká**: fikcia doručenia, zmeškanie a možnosť odpustenia.
7. **Predpoklady a chýbajúce údaje**.
8. **Stav overenia**: ktoré §§ boli overené cez LEXOMA, alebo že overené neboli.
9. Záverečná veta: „Tento výstup nie je právna rada; lehotu si overte v poučení rozhodnutia a s advokátom.“

## Časté chyby

- Započítanie dňa doručenia do lehoty podľa dní (§ 121 ods. 2).
- Počítanie od dňa, keď si strana písomnosť prečítala, hoci nastala fikcia doručenia dňom vrátenia zásielky súdu (§ 111 ods. 3, § 112).
- Použitie fikcie doručenia na platobný rozkaz (§ 266 ods. 2 ju vylučuje).
- Počítanie od doručenia strane, hoci má zástupcu na celé konanie (§ 110 ods. 1).
- Predpoklad, že zásielka musí prísť na súd do konca lehoty; stačí ju v posledný deň odovzdať doručujúcemu orgánu (§ 121 ods. 5).
- Zabudnutie na dodatočnú autorizáciu elektronického podania do desiatich dní (§ 125 ods. 2).
- Odpor bez vecného odôvodnenia: súd ho odmietne (§ 267 ods. 1 a 2 písm. c).
- Dovolanie podané bez advokáta, hoci dovolateľ nespadá pod výnimky § 429 ods. 2.
- Doplnenie odvolacích dôvodov po uplynutí lehoty na odvolanie (§ 365 ods. 3).

Tento výstup nie je právna rada; skill je pomôcka na orientáciu a nenahrádza posúdenie veci advokátom.
