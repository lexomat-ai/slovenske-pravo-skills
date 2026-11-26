---
name: kontrola-premlcania
description: Skontroluje, či je občianskoprávny nárok premlčaný podľa Občianskeho zákonníka (zákon č. 40/1964 Zb., § 100 až 114). Určí použiteľnú premlčaciu dobu (všeobecnú trojročnú alebo osobitnú, napr. pri náhrade škody, bezdôvodnom obohatení, preprave, vecnom bremene, práve priznanom rozhodnutím alebo písomne uznanom), deň, od ktorého doba plynie, vplyv podania žaloby a uznania dlhu, a vypočíta posledný deň doby. Odlíši premlčanie od preklúzie a pripomenie, že súd na premlčanie prihliadne len na námietku dlžníka. Použi, keď sa používateľ pýta, či je pohľadávka, dlh, pôžička, faktúra, nárok na náhradu škody alebo iné majetkové právo premlčané, dokedy možno podať žalobu, či sa oplatí vzniesť námietku premlčania, alebo čo spôsobí uznanie dlhu. Pri vzťahoch medzi podnikateľmi skill iba odkáže na Obchodný zákonník (513/1991 Zb.) a ďalej ho nerieši.
license: MIT
metadata:
  provenance: ai-generated
  generated_by: claude-fable-5-2
  authors: ""
  reviewed_by: ""
  review_status: unreviewed
  tags: "obcianske-pravo,premlcanie,lehoty"
  requires: "lexoma"
---

# Kontrola premlčania (Občiansky zákonník)

## Kedy skill použiť

- Používateľ chce vedieť, či je jeho nárok (alebo nárok proti nemu) premlčaný, alebo dokedy ho treba uplatniť na súde.
- Používateľ zvažuje námietku premlčania, uznanie dlhu alebo dohodu o splátkach.
- Nárok sa spravuje Občianskym zákonníkom (zákon č. 40/1964 Zb., ďalej „OZ“).

Nepoužívaj ho na obchodné záväzkové vzťahy (pozri krok 1), na pracovnoprávne, daňové ani trestné lehoty a na procesné lehoty.

## Fakty, ktoré si vyžiadaj

Pýtaj sa len na to, čo chýba. Do nástrojov neposielaj mená ani iné osobné údaje; stačia dátumy a druh nároku.

1. **Druh nároku**: zmluva (aká), náhrada škody, bezdôvodné obohatenie, preprava, poistné plnenie, vecné bremeno, dedičstvo, úroky alebo opakujúce sa plnenie, iné.
2. **Strany**: fyzické osoby, podnikatelia, spotrebiteľ voči dodávateľovi; či ide o manželov alebo o zákonného zástupcu a zastúpeného.
3. **Rozhodujúci deň**: deň splatnosti (zročnosti); pri splátkach splatnosť každej splátky a či sa stal zročným celý dlh; pri škode a obohatení deň udalosti a deň, keď sa oprávnený dozvedel o škode či obohatení a o povinnej osobe.
4. **Uznanie**: či dlžník právo uznal, kedy, či písomne a či čo do dôvodu aj výšky; či bola v uznaní lehota na plnenie.
5. **Súdne alebo iné konanie**: či a kedy bolo právo uplatnené na súde alebo u iného príslušného orgánu, ako konanie skončilo, či existuje právoplatné rozhodnutie a odkedy sa podľa neho malo plniť, či bol navrhnutý výkon rozhodnutia.
6. **Dnešný dátum** alebo deň, ku ktorému sa má premlčanie posúdiť.

Ak rozhodujúci údaj chýba, výsledok podaj podmienene („ak bola splatnosť …, potom …“) a nehádaj.

## Postup

### 1. Over, že sa použije OZ

- Záväzkové vzťahy medzi podnikateľmi, ktoré sa týkajú ich podnikateľskej činnosti, vzťahy vymenované v § 261 Obchodného zákonníka (zákon č. 513/1991 Zb.) a vzťahy, pre ktoré si strany písomne dohodli jeho použitie (§ 262), sa spravujú Obchodným zákonníkom. Ten má vlastnú úpravu premlčania v § 387 až 408 a inú všeobecnú premlčaciu dobu (štyri roky, § 397).
- V takom prípade používateľovi povedz, že tento skill sa na jeho vec nevzťahuje, odkáž ho na § 387 a nasl. Obchodného zákonníka a ďalej nepočítaj.

### 2. Over, či sa právo vôbec premlčuje a či nejde o preklúziu

- Premlčujú sa všetky majetkové práva okrem vlastníckeho práva. Záložné práva sa nepremlčujú skôr než zabezpečená pohľadávka. Nepremlčujú sa práva z vkladov a bežných účtov, kým vkladový vzťah trvá (§ 100 ods. 2 a 3 OZ).
- **Premlčanie**: právo nezaniká, ale ak sa dlžník premlčania dovolá, súd ho veriteľovi neprizná (§ 100 ods. 1 OZ).
- **Preklúzia**: právo zaniká, lebo nebolo uplatnené v určenom čase. Nastáva len v prípadoch uvedených v zákone a súd na ňu prihliadne, aj keď to dlžník nenamietne (§ 583 OZ).
- Ak zákon s uplynutím lehoty spája zánik práva, ide o preklúziu a pravidlá o premlčaní z tohto skillu sa nepoužijú. Upozorni na to a lehotu over v príslušnom ustanovení.

### 3. Urči premlčaciu dobu

| Nárok | Doba | Ustanovenie OZ |
|---|---|---|
| Všeobecne, ak nie je uvedené inak | 3 roky | § 101 |
| Náhrada škody | 2 roky odo dňa, keď sa poškodený dozvie o škode a o zodpovednej osobe; najneskôr 3 roky, pri úmyselnej škode 10 rokov od udalosti, z ktorej škoda vznikla; horná hranica neplatí pri škode na zdraví | § 106 ods. 1 a 2 |
| Škoda spôsobená trestným činom korupcie | 3 roky od právoplatnosti odsudzujúceho rozhodnutia, najneskôr 10 rokov od spáchania | § 106 ods. 3 |
| Bezdôvodné obohatenie | 2 roky odo dňa, keď sa oprávnený dozvie o obohatení a o obohatenom; najneskôr 3 roky, pri úmyselnom obohatení 10 rokov odo dňa, keď k nemu došlo | § 107 ods. 1 a 2 |
| Práva z prepravy (okrem náhrady škody pri preprave osôb) | 1 rok | § 108 |
| Právo zodpovedajúce vecnému bremenu | premlčí sa, ak sa 10 rokov nevykonávalo | § 109 |
| Právo priznané právoplatným rozhodnutím súdu alebo iného orgánu | 10 rokov odo dňa, keď sa malo podľa rozhodnutia plniť | § 110 ods. 1 |
| Právo písomne uznané čo do dôvodu i výšky | 10 rokov od uznania, resp. od uplynutia lehoty na plnenie uvedenej v uznaní | § 110 ods. 1 |
| Úroky a opakujúce sa plnenia | 3 roky; pri priznaných alebo uznaných právach to platí len pre tie, ktoré sa stali zročnými po právoplatnosti rozhodnutia alebo po uznaní | § 110 ods. 3 |

Pri škode a bezdôvodnom obohatení plynú dve doby súbežne (subjektívna a objektívna). Právo je premlčané, len čo uplynie ktorákoľvek z nich.

### 4. Urči deň, od ktorého doba plynie

- Všeobecne odo dňa, keď sa právo mohlo vykonať po prvý raz (§ 101 OZ).
- Právo, ktoré sa musí najprv uplatniť u fyzickej alebo právnickej osoby: odo dňa, keď sa takto uplatnilo (§ 102 OZ).
- Splátky: pri každej splátke odo dňa jej zročnosti. Ak sa pre nesplnenie splátky stal zročným celý dlh (§ 565 OZ), odo dňa zročnosti nesplnenej splátky (§ 103 OZ).
- Plnenie z poistenia: doba začína plynúť za rok po poistnej udalosti (§ 104 OZ).
- Právo oprávneného dediča na vydanie dedičstva: od právoplatnosti rozhodnutia, ktorým sa dedičské konanie skončilo (§ 105 OZ).
- Splátky určené rozhodnutím alebo uznaním: desaťročná doba pri každej splátke od jej zročnosti (§ 110 ods. 2 OZ).

### 5. Zisti, či doba neprestala plynúť alebo nezačala plynúť nová

OZ nepoužíva pojem „prerušenie“. Rozlišuj tieto situácie:

- **Uplatnenie na súde alebo u iného príslušného orgánu** v premlčacej dobe: ak veriteľ v konaní riadne pokračuje, doba od uplatnenia počas konania neplynie. To isté platí pri návrhu na výkon rozhodnutia pre právoplatne priznané právo (§ 112 OZ). Po skončení konania plynie zvyšok doby ďalej; nezačína sa odznova. Mimosúdna výzva ani upomienka tento účinok nemajú, § 112 OZ ho spája len s uplatnením na súde alebo u iného príslušného orgánu.
- **Právoplatné priznanie práva**: začína plynúť nová desaťročná doba odo dňa, keď sa malo podľa rozhodnutia plniť (§ 110 ods. 1 OZ).
- **Písomné uznanie čo do dôvodu i výšky**: nová desaťročná doba od uznania, resp. od uplynutia lehoty na plnenie uvedenej v uznaní (§ 110 ods. 1 OZ). Písomné uznanie zároveň zakladá domnienku, že dlh v čase uznania trval; pri premlčanom dlhu len vtedy, ak ten, kto dlh uznal, o premlčaní vedel (§ 558 OZ). Ústne uznanie ani čiastočná platba sa v § 110 OZ neuvádzajú.
- **Osoby, ktoré musia mať zákonného zástupcu**: premlčanie nezačne, kým im nie je ustanovený zástupca. Začaté premlčanie sa neskončí skôr než rok po ustanovení zástupcu alebo po odpadnutí prekážky (§ 113 OZ).
- **Zákonný zástupca a zastúpený, manželia navzájom**: premlčanie nezačína ani neplynie, okrem úrokov a opakujúcich sa plnení (§ 114 OZ).
- **Zmena veriteľa alebo dlžníka** (postúpenie, dedenie, prevzatie dlhu) na plynutie doby nemá vplyv (§ 111 OZ).

### 6. Vypočítaj posledný deň doby

- Koniec doby určenej podľa rokov pripadá na deň, ktorý sa číslom zhoduje s dňom udalosti, od ktorej sa doba začína (§ 122 ods. 2 OZ).
- Dobu, počas ktorej premlčanie neplynulo (krok 5), pripočítaj.
- Uveď výpočet krok po kroku s dátumami, aby ho používateľ vedel skontrolovať.

### 7. Posúď námietku premlčania

- Súd na premlčanie prihliadne len na námietku dlžníka; bez nej premlčané právo prizná (§ 100 ods. 1 OZ). Veriteľovi teda povedz, že žalobu podať môže, ale s rizikom neúspechu. Dlžníkovi povedz, že námietku musí v konaní sám vzniesť.
- Pri vzájomnom vrátení plnení z neplatnej alebo zrušenej zmluvy súd na námietku prihliadne len vtedy, ak by premlčanie mohol namietať aj druhý účastník (§ 107 ods. 3 OZ).
- Spotrebiteľská zmluva: premlčané právo nemožno vymáhať ani platne zabezpečiť. Zmeniť jeho obsah, nahradiť ho novým právom alebo obnoviť jeho vymáhateľnosť možno len právnym úkonom dlžníka, ktorý o premlčaní vedel (§ 54a OZ). Ak je dlžníkom spotrebiteľ, výslovne na to upozorni a odporuč overiť aj predpisy o ochrane spotrebiteľa, ktoré tento skill nepokrýva.

OZ (zákon č. 40/1964 Zb.) je zrušený novým Občianskym zákonníkom (zákon č. 260/2026 Z. z.) s účinnosťou od 1. 7. 2027. Ak premlčacia doba plynie k tomuto dňu alebo začne plynúť neskôr, upozorni, že premlčanie treba overiť podľa nového zákonníka a jeho prechodných ustanovení; tento skill ich nepokrýva.

## Overenie

Pred odoslaním odpovede over aktuálne znenie každého ustanovenia, ktoré cituješ.

- **Konektor LEXOMA (lexoma.sk) je pripojený**: každý citovaný § načítaj nástrojom na získanie znenia ustanovenia (zákon „40/1964 Zb.“ a číslo paragrafu) a porovnaj ho s tým, čo tvrdíš. Ak rozhodujúce skutočnosti nastali dávnejšie, načítaj aj znenie účinné k danému dňu a upozorni, že o tom, ktoré znenie sa na vec použije, rozhodujú prechodné ustanovenia. Ak sa znenie líši od tohto skillu, riaď sa aktuálnym znením a rozdiel uveď.
- **Konektor nie je pripojený alebo zlyhal**: do odpovede napíš vetu „Citované ustanovenia neboli overené voči aktuálnemu zneniu zákona.“ a odporuč overenie na slov-lex.sk.
- Necituj žiadny §, ktorý nie je v tomto skille a ktorý si si neoveril. Súdne rozhodnutia cituj len vtedy, ak si ich vyhľadal a prečítal.

## Formát výstupu

1. **Záver** jednou vetou: nárok je pravdepodobne premlčaný / pravdepodobne nie je premlčaný / nedá sa určiť bez údaja X.
2. **Použitý predpis a doba**: OZ, dĺžka doby a § (alebo odkaz na Obchodný zákonník a koniec).
3. **Začiatok plynutia**: dátum a dôvod s §.
4. **Udalosti s vplyvom na plynutie**: konanie, rozhodnutie, uznanie, s dátumami a §.
5. **Výpočet**: posledný deň premlčacej doby.
6. **Čo z toho vyplýva**: námietka dlžníka, riziko pre veriteľa, prípadná preklúzia alebo spotrebiteľský režim.
7. **Predpoklady a chýbajúce údaje**.
8. **Stav overenia**: ktoré §§ boli overené cez LEXOMA a k akému dňu, alebo že overené neboli.
9. Záverečná veta: „Tento výstup nie je právna rada; pred podaním žaloby alebo vznesením námietky sa poraďte s advokátom.“

## Časté chyby

- Tvrdenie, že premlčané právo zaniklo. Nezaniká; zaniká právo pri preklúzii (§ 583 OZ).
- Predpoklad, že súd premlčanie zohľadní sám. Prihliadne naň len na námietku (§ 100 ods. 1 OZ).
- Predpoklad, že po skončení súdneho konania plynie celá doba odznova. Podľa § 112 OZ doba počas konania iba neplynie.
- Považovanie upomienky, výzvy alebo ústneho prísľubu za uznanie podľa § 110 ods. 1 OZ, ktoré vyžaduje písomnú formu a určenie dôvodu aj výšky.
- Počítanie len subjektívnej dvojročnej doby pri škode a obohatení a prehliadnutie objektívnej doby, alebo naopak.
- Počítanie jednej doby pre celý dlh pri splátkach bez toho, aby sa stal zročným celý dlh (§ 103 OZ).
- Použitie trojročnej doby OZ na obchodný záväzkový vzťah.
- Použitie dnešného znenia na staré skutočnosti bez upozornenia na prechodné ustanovenia.
- Vydávanie výsledku za istý, hoci deň splatnosti alebo deň, keď sa oprávnený dozvedel o škode, používateľ len odhaduje.

Tento výstup nie je právna rada; skill je pomôcka na orientáciu a nenahrádza posúdenie veci advokátom.
