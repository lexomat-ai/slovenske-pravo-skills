---
name: ustavna-staznost
description: Pomôže pripraviť alebo posúdiť individuálnu ústavnú sťažnosť fyzickej alebo právnickej osoby na Ústavný súd SR podľa čl. 127 Ústavy SR a zákona č. 314/2018 Z. z. o Ústavnom súde (§ 122 až 135). Skontroluje dvojmesačnú lehotu a deň, od ktorého plynie (právoplatnosť, doručenie písomného vyhotovenia, mimoriadny opravný prostriedok), subsidiaritu a vyčerpanie právnych prostriedkov, povinné zastúpenie advokátom a plnomocenstvo, povinné náležitosti a prílohy, dôvody odmietnutia pri predbežnom prerokovaní a návrh na primerané finančné zadosťučinenie. Použi, keď sa používateľ pýta, či a dokedy môže podať ústavnú sťažnosť, čo musí obsahovať, prečo môže byť odmietnutá, alebo ako žiadať finančné zadosťučinenie za porušenie základných práv (napr. pri prieťahoch v konaní). Nepokrýva sťažnosť orgánu územnej samosprávy (čl. 127a) ani konanie pred ESĽP.
license: MIT
metadata:
  provenance: ai-generated
  generated_by: claude-fable-5-2
  authors: ""
  reviewed_by: ""
  review_status: unreviewed
  tags: "ustavne-pravo,ustavna-staznost,ustavny-sud"
  requires: "lexoma"
---

# Ústavná sťažnosť (čl. 127 Ústavy SR)

## Kedy skill použiť

- Fyzická alebo právnická osoba tvrdí, že právoplatným rozhodnutím, opatrením alebo iným zásahom orgánu verejnej moci boli porušené jej základné práva a slobody (§ 122 zákona č. 314/2018 Z. z., ďalej „ZÚS“; čl. 127 ods. 1 Ústavy SR, zákon č. 460/1992 Zb.).
- Používateľ potrebuje overiť lehotu, prípustnosť, náležitosti alebo návrh na primerané finančné zadosťučinenie.

Nepoužívaj ho na sťažnosť orgánu územnej samosprávy (čl. 127a Ústavy), na iné konania pred Ústavným súdom ani na sťažnosť na ESĽP.

## Fakty, ktoré si vyžiadaj

Do nástrojov ani do textu neposielaj mená, rodné čísla, adresy ani iné osobné údaje; stačí druh konania, orgán a dátumy.

1. **Čo porušenie spôsobilo**: právoplatné rozhodnutie (ktorého orgánu), opatrenie, iný zásah, alebo nečinnosť (napr. prieťahy).
2. **Dátumy**: právoplatnosť rozhodnutia; či nadobudlo právoplatnosť vyhlásením alebo oznámením a kedy bolo doručené písomné vyhotovenie (sťažovateľovi alebo jeho zástupcovi); pri opatrení alebo inom zásahu deň, keď sa o ňom sťažovateľ mohol dozvedieť.
3. **Opravné prostriedky**: ktoré riadne a mimoriadne opravné prostriedky (napr. dovolanie, kasačná sťažnosť) boli podané, s akým výsledkom a kedy bolo doručené rozhodnutie o nich; či vec môže ešte preskúmať iný súd.
4. **Ktoré základné práva** sa podľa používateľa porušili (článok Ústavy alebo medzinárodnej zmluvy).
5. **Zastúpenie**: či má sťažovateľ advokáta, alebo či je sám advokát; či žiada o ustanovenie právneho zástupcu.
6. **Zadosťučinenie**: či žiada primerané finančné zadosťučinenie, v akej výške a prečo.

## Postup

### 1. Over právomoc a subsidiaritu

- Ústavný súd o sťažnosti rozhoduje, len ak o ochrane týchto práv a slobôd nerozhoduje iný súd (čl. 127 ods. 1 Ústavy).
- Ústavná sťažnosť je neprípustná, ak je na ochranu práv sťažovateľa vo veci príslušný iný súd alebo ak sťažovateľ nevyčerpal právne prostriedky, ktoré mu zákon na ochranu jeho základných práv a slobôd priznáva (§ 132 ods. 1 ZÚS). Z dôvodov hodných osobitného zreteľa ju možno neodmietnuť (§ 132 ods. 2 ZÚS); na túto výnimku sa nespoliehaj.
- Ak existuje nevyčerpaný opravný prostriedok alebo iná cesta na súd, povedz to ako hlavné riziko a odporuč ju posúdiť s advokátom ako prvú.

### 2. Vypočítaj lehotu

Ústavnú sťažnosť možno podať **do dvoch mesiacov** (§ 124 ZÚS):

| Situácia | Lehota plynie od |
|---|---|
| Rozhodnutie | nadobudnutia právoplatnosti |
| Rozhodnutie právoplatné vyhlásením alebo oznámením, ak sa zároveň doručuje písomné vyhotovenie | doručenia písomného vyhotovenia sťažovateľovi; ak sa doručuje len zástupcovi, doručenia zástupcovi |
| Opatrenie alebo iný zásah | dňa, keď sa sťažovateľ mohol o opatrení alebo zásahu dozvedieť |
| Bol podaný mimoriadny opravný prostriedok | vo vzťahu k ním napadnutému rozhodnutiu od doručenia rozhodnutia o mimoriadnom opravnom prostriedku |

- Konanie sa začína dňom doručenia návrhu Ústavnému súdu (§ 41 ods. 2 ZÚS); počítaj teda s doručením, nie s odoslaním, ak si spôsob počítania lehoty neoveril.
- Na otázky, ktoré ZÚS v piatej alebo šiestej časti neupravuje, sa primerane použije Civilný sporový poriadok alebo Správny súdny poriadok (§ 62 ZÚS). Pravidlá počítania lehôt z týchto predpisov over (s LEXOMA nástrojom `compute_deadline`) a necituj ich naslepo.
- Oneskorene podaný návrh Ústavný súd odmietne (§ 56 ods. 2 písm. f) ZÚS).

### 3. Over zastúpenie

- Navrhovateľ musí byť v celom konaní zastúpený advokátom; ak je sám advokátom, nemusí (§ 34 ZÚS). Advokát sa nemôže dať zastúpiť advokátskym koncipientom (§ 36 ZÚS).
- K návrhu sa pripája plnomocenstvo, v ktorom sa výslovne uvedie, že sťažovateľ advokáta splnomocňuje na zastupovanie pred Ústavným súdom (§ 43 ods. 3 ZÚS).
- Na žiadosť môže Ústavný súd ustanoviť právneho zástupcu, ak to odôvodňujú majetkové pomery a nejde o zrejme bezúspešné uplatňovanie nároku; neplatí to, ak ho možno ustanoviť podľa osobitného predpisu (§ 37 ods. 1 ZÚS).

### 4. Skontroluj náležitosti a prílohy

- **Všeobecné** (§ 39 ods. 3 a § 43 ods. 1 a 2 ZÚS): kto podanie robí, ktorej veci sa týka, čo sa ním sleduje; dátum narodenia (fyzická osoba) alebo IČO (právnická osoba); bydlisko alebo sídlo; proti komu návrh smeruje; akého rozhodnutia sa sťažovateľ domáha (petit); odôvodnenie; navrhované dôkazy; dátum a podpis.
- **Osobitné** (§ 123 ods. 1 ZÚS): kto podľa sťažovateľa porušil jeho práva; označenie právoplatného rozhodnutia, opatrenia alebo iného zásahu; označenie porušených základných práv a slobôd; konkrétne skutkové a právne dôvody porušenia.
- **Príloha** (§ 123 ods. 3 ZÚS): kópia právoplatného rozhodnutia alebo opatrenia, alebo dôkaz o inom zásahu.
- **Forma** (§ 40 ZÚS): písomne, listinne alebo elektronicky. Neautorizované elektronické podanie treba do 10 dní doplniť; Ústavný súd na to nevyzýva.
- Ústavný súd je viazaný rozsahom a dôvodmi návrhu (§ 45 ZÚS), preto petit a dôvody musia pokryť všetko, čo sťažovateľ chce.
- Voliteľne: návrh, aby senát podal návrh na konanie o súlade právneho predpisu (čl. 127 ods. 5 Ústavy, § 123 ods. 4 ZÚS) s náležitosťami podľa § 123 ods. 4 písm. a) až d).

### 5. Primerané finančné zadosťučinenie

- Ústavný súd ho môže priznať, ak sťažnosti vyhovie a sťažovateľ o to požiadal (čl. 127 ods. 3 Ústavy, § 133 ods. 3 písm. e) ZÚS).
- V sťažnosti treba uviesť požadovaný rozsah a dôvody (§ 123 ods. 2 ZÚS).
- Orgán ho zaplatí do dvoch mesiacov od právoplatnosti nálezu; pri omeškaní sa zvyšuje o 5 % za každý aj začatý rok (§ 135 ZÚS).
- Zodpovednosť za škodu alebo inú ujmu tým nie je dotknutá (čl. 127 ods. 4 Ústavy).

### 6. Upozorni na dôvody odmietnutia

Pri predbežnom prerokovaní môže Ústavný súd návrh uznesením odmietnuť (§ 56 ods. 2 ZÚS), ak: nemá právomoc; navrhovateľ nie je zastúpený a žiadosti o ustanovenie zástupcu nevyhovel; nemá zákonné náležitosti; je neprípustný (§ 55, § 132 ods. 1); je podaný zjavne neoprávnenou osobou; je oneskorený; je zjavne neopodstatnený. Pri ústavnej sťažnosti môže súd vyzvať na odstránenie odstrániteľných nedostatkov v určenej lehote (§ 56 ods. 3 ZÚS); na to sa nespoliehaj.

Ďalej: podanie sťažnosti nemá odkladný účinok (§ 128 ZÚS); o odklad vykonateľnosti alebo dočasné opatrenie treba výslovne navrhnúť (§ 129 a 130 ZÚS). Konanie je spravidla bez poplatku; pri opakovaných skutkovo a právne obdobných neúspešných sťažnostiach sa za jedenástu a ďalšiu v kalendárnom roku ukladá súdny poplatok (§ 71 a 72 ZÚS).

## Overenie

- **LEXOMA (lexoma.sk) je pripojená**: každý citovaný § ZÚS a článok Ústavy načítaj cez `get_provision` (alebo `get_act`) v znení účinnom ku dňu podania; výsledok porovnaj s týmto skillom a pri rozdiele sa riaď aktuálnym znením a rozdiel uveď. Lehotu prepočítaj cez `compute_deadline`. Judikatúru Ústavného súdu (napr. k subsidiarite alebo výške zadosťučinenia) cituj len vtedy, ak si ju našiel cez `search_case_law` a prečítal cez `get_decision`; celú odpoveď na záver skontroluj cez `verify_citations`.
- **LEXOMA nie je pripojená alebo zlyhala**: do odpovede napíš „Citované ustanovenia neboli overené voči aktuálnemu zneniu zákona.“ a odporuč overenie na slov-lex.sk. Necituj nijaký § ani rozhodnutie, ktoré nie je v tomto skille.

## Formát výstupu

1. **Záver**: sťažnosť je pravdepodobne včasná a prípustná / hrozí odmietnutie z dôvodu X / nedá sa určiť bez údaja Y.
2. **Lehota**: rozhodujúci deň, posledný deň lehoty, výpočet a § 124 ZÚS.
3. **Subsidiarita**: vyčerpané a nevyčerpané prostriedky.
4. **Zastúpenie a plnomocenstvo**.
5. **Kontrolný zoznam náležitostí a príloh** (§ 39, 43, 123 ZÚS) s označením, čo chýba.
6. **Zadosťučinenie**: či sa žiada, rozsah a dôvody.
7. **Riziká odmietnutia** podľa § 56 ods. 2 ZÚS.
8. **Stav overenia**: čo bolo overené cez LEXOMA a k akému dňu, alebo že overené nebolo.
9. Záver: „Tento výstup nie je právna rada; ústavnú sťažnosť podáva advokát, s ktorým vec posúďte.“

## Časté chyby

- Počítanie lehoty od vyhlásenia rozhodnutia, hoci sa doručuje písomné vyhotovenie, alebo prehliadnutie, že pri zastúpení rozhoduje doručenie zástupcovi.
- Podanie sťažnosti popri ešte otvorenom opravnom prostriedku alebo inej ceste na súd (§ 132 ods. 1 ZÚS).
- Podanie bez advokáta alebo s plnomocenstvom, ktoré výslovne neuvádza zastupovanie pred Ústavným súdom.
- Chýbajúca kópia napadnutého rozhodnutia alebo neoznačenie konkrétnych porušených práv.
- Žiadosť o zadosťučinenie bez sumy a dôvodov, alebo dodatočná žiadosť mimo rozsahu návrhu (§ 45 ZÚS).
- Predpoklad, že podanie sťažnosti odkladá výkon napadnutého rozhodnutia (§ 128 ZÚS).

Tento výstup nie je právna rada; slúži na orientáciu a nenahrádza posúdenie veci advokátom.
