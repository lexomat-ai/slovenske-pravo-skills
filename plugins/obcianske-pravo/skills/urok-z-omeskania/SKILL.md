---
name: urok-z-omeskania
description: Vypočíta úroky z omeškania pri peňažnom dlhu v občianskoprávnom vzťahu podľa § 517 ods. 2 Občianskeho zákonníka (zákon č. 40/1964 Zb.) a § 3 nariadenia vlády č. 87/1995 Z. z. Určí prvý deň omeškania, sadzbu (základná úroková sadzba ECB platná k prvému dňu omeškania + 5 percentuálnych bodov), rozdelí omeškanie na obdobia podľa splatnosti jednotlivých súm a čiastočných platieb a vypočíta úroky za každé obdobie. Upozorní na prechodné pravidlá pre vzťahy vzniknuté pred 1. 2. 2013, na poplatok z omeškania pri nájme bytu, na strop sankcií pri spotrebiteľskom úvere a na zrušenie oboch predpisov novým Občianskym zákonníkom od 1. 7. 2027. Použi, keď sa používateľ pýta, koľko úrokov z omeškania môže žiadať alebo musí zaplatiť z nezaplatenej faktúry, pôžičky, nájomného alebo iného peňažného dlhu medzi občanmi alebo voči spotrebiteľovi, alebo chce skontrolovať výpočet úrokov v upomienke či žalobe. Pri vzťahoch medzi podnikateľmi iba odkáže na § 369 Obchodného zákonníka a ďalej ich nerieši.
license: MIT
metadata:
  provenance: ai-generated
  generated_by: claude-fable-5-2
  authors: ""
  reviewed_by: ""
  review_status: unreviewed
  tags: "obcianske-pravo,urok-z-omeskania,omeskanie,penazny-dlh,vypocet"
  requires: "lexoma"
---

# Úrok z omeškania (Občiansky zákonník)

## Kedy skill použiť

- Dlžník nezaplatil peňažný dlh riadne a včas a používateľ chce vypočítať úroky z omeškania, ktoré môže žiadať alebo ktoré dlhuje.
- Používateľ kontroluje sumu úrokov v upomienke, výzve alebo žalobe.
- Vzťah sa spravuje Občianskym zákonníkom (zákon č. 40/1964 Zb., ďalej „OZ“).

Nepoužívaj ho na zmluvné úroky (odplatu za úver), zmluvné pokuty ani na obchodné záväzkové vzťahy.

## Fakty, ktoré si vyžiadaj

Pýtaj sa len na to, čo chýba. Do nástrojov neposielaj mená ani iné osobné údaje; stačia sumy a dátumy.

1. **Strany**: fyzické osoby, podnikateľ voči spotrebiteľovi, podnikatelia medzi sebou; či ide o spotrebiteľský úver.
2. **Druh dlhu**: kúpna cena, pôžička, nájomné za byt alebo úhrada za plnenia spojené s užívaním bytu, iné.
3. **Istina a splatnosť**: každá dlžná suma a jej deň splatnosti; ak splatnosť nebola dohodnutá, kedy veriteľ o plnenie požiadal.
4. **Platby**: dátum a suma každej čiastočnej platby; či dlžník určil, na čo platí.
5. **Deň vzniku záväzku** (uzavretia zmluvy), kvôli prechodným ustanoveniam.
6. **Deň, ku ktorému sa úroky počítajú** (dnešok, deň zaplatenia, deň podania žaloby).
7. Či veriteľ niekedy odmietol riadne ponúknuté plnenie alebo neposkytol súčinnosť.

## Postup

### 1. Over, že sa použije OZ

- Záväzkové vzťahy medzi podnikateľmi týkajúce sa ich podnikateľskej činnosti (§ 261 ods. 1 Obchodného zákonníka, zákon č. 513/1991 Zb.), vzťahy podľa § 261 ods. 2 a vzťahy, pri ktorých si strany písomne dohodli jeho použitie (§ 262), sa spravujú Obchodným zákonníkom.
- Úroky z omeškania tam upravuje § 369 Obchodného zákonníka: v dohodnutej výške, a ak nebola dohodnutá, v sadzbe podľa nariadenia vlády vydaného k tomuto ustanoveniu. Nariadenie č. 87/1995 Z. z. vykonáva OZ, nie § 369. Povedz používateľovi, že tento skill sa na jeho vec nevzťahuje, odkáž ho na § 369 až 369d Obchodného zákonníka a ďalej nepočítaj.

### 2. Over, či je dlžník v omeškaní a či nejde o poplatok z omeškania

- Dlžník, ktorý dlh riadne a včas nesplní, je v omeškaní (§ 517 ods. 1 OZ). Pri peňažnom dlhu má veriteľ právo popri plnení na úroky z omeškania, ak dlžník nie je povinný platiť poplatok z omeškania (§ 517 ods. 2 OZ).
- Ak čas plnenia nie je dohodnutý, ustanovený predpisom ani určený rozhodnutím, dlžník má plniť prvý deň po tom, čo ho veriteľ o plnenie požiadal (§ 563 OZ).
- K omeškaniu dlžníka nedôjde, ak veriteľ riadne a včas ponúknuté plnenie neprijal alebo neposkytol potrebnú súčinnosť (§ 520 OZ). Za čas veriteľovho omeškania dlžník úroky platiť nemusí (§ 523 OZ).
- **Nájom bytu**: ak nájomca nezaplatí nájomné alebo úhradu za plnenia spojené s užívaním bytu do piatich dní po splatnosti, platí poplatok z omeškania (§ 697 OZ), nie úroky z omeškania. Poplatok je 0,5 promile dlžnej sumy za každý deň omeškania, najmenej 0,83 eura za každý aj začatý mesiac omeškania (§ 4 nariadenia č. 87/1995 Z. z.).

### 3. Urči sadzbu

- **Omeškanie zo záväzku vzniknutého od 1. 2. 2013**: sadzba je o 5 percentuálnych bodov vyššia ako základná úroková sadzba Európskej centrálnej banky platná k prvému dňu omeškania (§ 3 nariadenia č. 87/1995 Z. z.). Sadzba sa určí raz, k prvému dňu omeškania, a počas omeškania sa nemení.
- Základnou úrokovou sadzbou ECB sa rozumie sadzba, ktorú ECB stanovuje a zverejňuje pre hlavné refinančné obchody Eurosystému (§ 17 ods. 1 zákona č. 659/2007 Z. z.). Hodnotu platnú k prvému dňu omeškania zisti z webu ECB alebo NBS; neuvádzaj ju spamäti.
- **Záväzok vzniknutý pred 1. 2. 2013**: výška úrokov sa riadi predpismi účinnými k 31. 1. 2013 aj za omeškanie po tomto dni (§ 10c nariadenia). Podľa znenia účinného od 1. 7. 2010 do 31. 1. 2013 bola sadzba o 8 percentuálnych bodov vyššia ako základná sadzba ECB k prvému dňu omeškania; ak sa sadzba ECB počas omeškania zmenila a je to pre veriteľa výhodnejšie, za každý kalendárny polrok o 7 percentuálnych bodov vyššia ako sadzba ECB platná k jeho prvému dňu (§ 3 ods. 1 a 2 v tom znení). Vtedy počítaj po polrokoch.
- **Omeškanie, ktoré vzniklo pred 1. 1. 2009**: riadi sa predpismi účinnými do 31. 12. 2008 (§ 10a nariadenia). Tento skill ich nepokrýva; načítaj znenie k danému dňu.
- **Spotrebiteľský úver**: sankcie za omeškanie spotrebiteľa (úroky z omeškania, zmluvné pokuty a iné plnenia) spolu nesmú prekročiť strop podľa § 3a nariadenia (vychádza z priemernej ročnej percentuálnej miery nákladov a z trojnásobku úrokov z omeškania); východisko je § 53b ods. 1 OZ. Ak ide o taký prípad, na strop upozorni a výpočet stropu over.

### 4. Rozdeľ omeškanie na obdobia

- Každá suma s vlastnou splatnosťou má vlastný prvý deň omeškania, a teda aj vlastnú sadzbu. Počítaj ju samostatne.
- Každá čiastočná platba mení dlžnú sumu: obdobie končí dňom platby a ďalšie obdobie sa počíta z novej sumy.
- Čiastočné plnenie peňažného dlhu sa započítava najprv na istinu a potom na úroky, ak dlžník neurčí inak (§ 566 ods. 2 OZ).
- Ak sa strany dohodli, že sa už splatný dlh bude plniť v splátkach, úroky z omeškania v splátkach dlžník platí len vtedy, ak sa to výslovne dohodlo (§ 521 OZ).
- Pri záväzku spred 1. 2. 2013 s polročnou sadzbou rozdeľ omeškanie aj na kalendárne polroky (krok 3).

### 5. Vypočítaj

Pre každé obdobie: úrok = dlžná suma × ročná sadzba (%) / 100 × počet dní omeškania v období / počet dní v roku.

- Nariadenie neurčuje, ako prepočítať ročnú sadzbu na dni, ani ktoré dni sa započítajú. Použitú konvenciu (prvý a posledný započítaný deň, 365 alebo skutočný počet dní v roku) výslovne uveď ako predpoklad.
- Výsledky za obdobia sčítaj a zaokrúhli na centy až na konci.
- Úroky z omeškania sú príslušenstvom pohľadávky (§ 121 ods. 3 OZ). Náhradu škody spôsobenej omeškaním možno pri peňažnom dlhu žiadať len v rozsahu, ktorý úroky z omeškania alebo poplatok z omeškania nepokrývajú (§ 519 OZ).

### 6. Zmena právnej úpravy od 1. 7. 2027

OZ aj nariadenie č. 87/1995 Z. z. sú zrušené novým Občianskym zákonníkom (zákon č. 260/2026 Z. z.) s účinnosťou od 1. 7. 2027. Ak omeškanie trvá k tomuto dňu alebo vzniklo neskôr, upozorni, že výpočet za obdobie od 1. 7. 2027 treba overiť podľa nového zákonníka a jeho prechodných ustanovení; tento skill ich nepokrýva.

## Overenie

- **Konektor LEXOMA (lexoma.sk) je pripojený**: každý citovaný § načítaj nástrojom `get_provision` („40/1964 Zb.“, „87/1995 Z. z.“, pri odkaze aj „513/1991 Zb.“) a porovnaj s tým, čo tvrdíš. Pri starších záväzkoch načítaj znenie nariadenia účinné k rozhodujúcemu dňu. Ak sa znenie líši od tohto skillu, riaď sa aktuálnym znením a rozdiel uveď.
- **Konektor nie je pripojený alebo zlyhal**: do odpovede napíš vetu „Citované ustanovenia neboli overené voči aktuálnemu zneniu zákona.“ a odporuč overenie na slov-lex.sk.
- Sadzbu ECB vždy over z primárneho zdroja (ECB alebo NBS) a uveď zdroj aj dátum, ku ktorému platí.
- Necituj § ani súdne rozhodnutie, ktoré nie je v tomto skille a ktoré si si neoveril.

## Formát výstupu

1. **Záver**: suma úrokov z omeškania k zadanému dňu, alebo „nedá sa určiť bez údaja X“.
2. **Použitý predpis**: OZ a nariadenie č. 87/1995 Z. z. (s §), alebo odkaz na § 369 Obchodného zákonníka a koniec.
3. **Sadzba**: sadzba ECB k prvému dňu omeškania + 5 p. b. = výsledná ročná sadzba, so zdrojom sadzby ECB.
4. **Tabuľka období**: dlžná suma | od | do | počet dní | sadzba | úrok.
5. **Súčet** a započítanie platieb (§ 566 ods. 2 OZ).
6. **Upozornenia**: poplatok z omeškania, spotrebiteľský strop, prechodné pravidlá, zmena od 1. 7. 2027.
7. **Predpoklady**: konvencia počítania dní, neisté dátumy.
8. **Stav overenia**: ktoré §§ boli overené cez LEXOMA, alebo že overené neboli.
9. Záverečná veta: „Tento výstup nie je právna rada; pred uplatnením nároku si výpočet overte s advokátom.“

## Časté chyby

- Použitie dnešnej sadzby ECB namiesto sadzby platnej k prvému dňu omeškania.
- Prepočítavanie sadzby pri každej zmene sadzby ECB pri záväzku od 1. 2. 2013; polročná zmena platí len pre záväzky spred tohto dňa (§ 10c nariadenia).
- Jedna sadzba pre viac faktúr či splátok s rôznou splatnosťou.
- Započítanie čiastočnej platby najprv na úroky, hoci OZ určuje opak, ak dlžník neurčí inak (§ 566 ods. 2 OZ).
- Úroky z omeškania pri nájomnom za byt namiesto poplatku z omeškania (§ 697 OZ).
- Použitie nariadenia č. 87/1995 Z. z. na obchodný záväzkový vzťah.
- Úroky za čas, keď bol v omeškaní veriteľ (§ 523 OZ).
- Neuvedenie konvencie počítania dní, takže výpočet nemožno skontrolovať.

Tento výstup nie je právna rada; skill je pomôcka na orientáciu a nenahrádza posúdenie veci advokátom.
