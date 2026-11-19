---
layout: journal
slug: apple-watch-hrv-without-a-baseline
ref: /journal/apple-watch-hrv-without-a-baseline/
permalink: /nl/journal/apple-watch-hrv-without-a-baseline/
translated_from: 2026-11-08
last_updated: 2026-11-19
date: 2026-11-19
title: "HRV-waarde: waarom het cijfer op je Apple Watch zonder basislijn bijna niets zegt"
seo:
  title: "HRV-waarde: wat zegt je cijfer zonder basislijn?"
  description: "HRV-waarde: 42 ms kan prima of zorgelijk zijn, en alleen je eigen basislijn zegt welke van de twee. Wat HRV meet, wat het mist en hoe je je waarde leest."
  keywords:
    - "hrv waarde"
    - "hrv waarden betekenis"
    - "hrv waarden te laag"
    - "hrv waarden slaap"
    - "hrv waarden leeftijd"
    - "lage hrv"
    - "lage hrv betekenis"
    - "hrv betekenis"
lede: "Een HRV van 42 ms op je Apple Watch kan uitstekend, gemiddeld of zorgelijk zijn, en zonder context weet je niet welke van de drie. Op zichzelf is het cijfer een van de vaakst verkeerd gelezen waarden in de gezondheidstechnologie voor consumenten. Dit artikel legt uit wat HRV je wel en niet vertelt, en waarom een persoonlijke basislijn het enige kader is waarmee je de meting kunt gebruiken."
quick_answer: "Een HRV-waarde zegt pas iets als je die afzet tegen je eigen voortschrijdende basislijn. HRV (hartritmevariabiliteit, op de Apple Watch weergegeven als SDNN) verschilt in absolute waarde 3 tot 10 keer tussen mensen, afhankelijk van leeftijd, geslacht, conditie, lichaamshouding, het moment van meten en de pols waaraan je het horloge draagt. Lees je HRV als een procentuele afwijking van je eigen gemiddelde over de afgelopen weken; 60 dagen is een goed venster. Je cijfer vergelijken met dat van een vriend, met een bevolkingsgemiddelde of met een tabel met “normale waarden” van internet misleidt je bijna altijd."
excerpt: "Een HRV van 42 ms op de Apple Watch is voor de een uitstekend en voor de ander zorgelijk. Dit artikel legt uit waarom absolute HRV-waarden 3 tot 10 keer verschillen tussen mensen, waarom alleen je persoonlijke basislijn de HRV van je Apple Watch bruikbaar maakt en hoe je trends leest zoals een sportwetenschapper dat doet."
faq:
  - q: "Is een HRV van 42 ms goed of slecht?"
    a: "Dat hangt helemaal af van wiens 42 ms het is. Bij iemand met een basislijn van 38 ms over de afgelopen 60 dagen ligt 42 ms boven het gemiddelde en is het een goed herstelsignaal. Bij iemand met een basislijn van 80 ms is 42 ms de helft van wat normaal is en wijst het waarschijnlijk op flinke stress, ziekte of opgebouwde trainingsbelasting. Dezelfde absolute waarde is in het ene lichaam goed nieuws en in het andere slecht nieuws. Daarom vergelijkt elke HRV-app die het gebruiken waard is je met jezelf."
  - q: "Waarom wijkt de HRV van de Apple Watch zo af van die van een borstband?"
    a: "De Apple Watch meet HRV (SDNN) op wisselende momenten overdag en ’s nachts als je stil bent, met optische fotoplethysmografie. Een borstband meet continu, op basis van de elektrische activiteit van het hart. Dat zijn twee verschillende metingen onder verschillende omstandigheden, dus de absolute waarden komen niet met elkaar overeen. De metingen die je horloge in de loop van de tijd van jou doet, zijn wel onderling te vergelijken. Je trend is betrouwbaar; je absolute waarde naast een tabel voor borstbanden is dat niet."
  - q: "Hoeveel schommelt je HRV van dag tot dag?"
    a: "Veel. Schommelingen van 10 tot 25% van dag tot dag zijn normaal bij een gezonde volwassene, dus één lage meting zegt bijna nooit iets. Kijk naar het voortschrijdende gemiddelde over 7 dagen ten opzichte van je basislijn over 60 dagen. De HRV van één dag is vooral ruis."
  - q: "Waarom daalt je HRV in de winter?"
    a: "Door seizoensgebonden aanpassing van hart en bloedvaten. Kou, minder daglicht, minder aerobe activiteit en een veranderd slaappatroon verschuiven het evenwicht van het autonome zenuwstelsel naar een overwicht van de sympathische kant. Een winterdip van 10 tot 20% komt vaak voor en is geen teken van ziekte. Een van de meest gemaakte leesfouten is die dip opvatten als “er is iets mis met me”, terwijl hij betekent: “in de winter ligt mijn HRV lager”."
  - q: "Geeft de Apple Watch RMSSD, SDNN of lnRMSSD?"
    a: "SDNN. De Gezondheid-app slaat de HRV van de Apple Watch op als SDNN, de standaarddeviatie van de intervallen tussen opeenvolgende hartslagen, in milliseconden, en het is de enige HRV-maat die HealthKit beschikbaar stelt. In de sportwetenschap gebruikt men vaak RMSSD en de natuurlijke logaritme daarvan, lnRMSSD. Dat zijn andere berekeningen dan SDNN, dus een meting van de Apple Watch laat zich niet zomaar omrekenen naar een van beide. Observa toont de SDNN die de Gezondheid-app vastlegt en vergelijkt die met je eigen basislijn."
mentioned_apps:
  - observa
read_time: "7 min lezen"
---

De Apple Watch meet een van de meest informatieve lichaamswaarden die je als consument kunt bijhouden, en bijna niemand gebruikt die goed.

Open de Gezondheid-app en tik op Hartritmevariabiliteit. Je ziet een rij getallen van de afgelopen weken, misschien een paar van 25, een paar van 45 en een paar van 80, en een grafiek van het bereik die er vaag informatief uitziet. Als je in de verkeerde hoek van internet bent beland, heb je misschien gelezen dat je HRV-waarde boven 50 ms “hoort” te liggen, of dat alles onder 30 “zorgelijk” is. Dat is ongeveer even nuttig als de bewering dat je “normale” lichaamstemperatuur 37,2 °C moet zijn, wie je ook bent. Het getal is echt. Het kader klopt niet.

## Wat HRV eigenlijk meet

HRV, of hartritmevariabiliteit, is de variatie in tijd tussen opeenvolgende hartslagen. De Apple Watch rapporteert SDNN, de standaarddeviatie van de intervallen tussen opeenvolgende normale hartslagen (de NN- of RR-intervallen), in milliseconden. Hoger betekent over het algemeen meer parasympathische activiteit van het zenuwstelsel (“rust en vertering”) en lager betekent over het algemeen meer sympathische activiteit (“vechten of vluchten”). Een structureel hogere trend hangt samen met cardiovasculaire conditie, herstelkwaliteit en een overwegend parasympathische toestand.

Tot zover niets aan de hand. De problemen beginnen als dezelfde woorden gelden voor twee mensen van wie de absolute waarden een factor drie uit elkaar liggen.

## De variatie tussen mensen is enorm

De absolute HRV van gezonde volwassenen loopt grofweg van 15 ms tot 150 ms in SDNN, een spreiding van een factor 10. Deze factoren verschuiven iemands persoonlijke basislijn:

- **Leeftijd.** De meeste longitudinale studies vinden dat HRV na je dertigste ruwweg 0,5 tot 1 ms per jaar daalt. Een 45-jarige met een HRV van 35 ms en een 25-jarige met 70 ms kunnen voor hun leeftijd allebei een perfecte parasympathische gezondheid hebben.
- **Geslacht.** De gemiddelde HRV is bij volwassen vrouwen iets lager dan bij mannen, al is de variatie binnen elk geslacht veel groter dan het verschil tussen beide.
- **Conditie.** Duurgetrainde mensen hebben in rust geregeld een 50 tot 100% hogere HRV dan ongetrainde mensen. Ook dat zegt niet evenredig veel: goed getrainde atleten zitten vaak in bereiken die een algemene tabel “verhoogd” zou noemen.
- **Lichaamshouding.** HRV is liggend hoger dan zittend, en zittend hoger dan staand.
- **Tijdstip.** Hoger ’s nachts, lager tijdens de actieve uren.
- **Meetmethode.** De optische PPG van de Apple Watch, op wisselende momenten, geeft andere waarden dan een borstband of een ECG van onderzoekskwaliteit, zelfs bij dezelfde persoon op hetzelfde moment.

HRV is een van die biologische waarden waarbij alleen *die van jou* iets betekent. Je 42 ms vergelijken met de 65 ms van een vriend zegt niets.

## Het juiste kader: je eigen basislijn over 60 dagen

De enige HRV-metingen die je betrouwbaar kunt duiden, zien er zo uit:

- **“De HRV (SDNN) van vandaag ligt X% boven of onder mijn eigen voortschrijdende gemiddelde over 7 dagen.”**
- **“Het gemiddelde van deze week ligt X% boven of onder mijn eigen voortschrijdende gemiddelde over 60 dagen.”**

Beide vergelijken je met jezelf, en dat neemt vrijwel alle verstorende factoren hierboven weg. Je leeftijd en geslacht veranderen niet in 60 dagen, je conditie verandert niet drastisch en je horloge is hetzelfde horloge. Wat wel verandert, is *wat je fysiologie deze week heeft verschoven ten opzichte van het afgelopen kwartaal*, en dat is de vraag die ertoe doet.

Zestig dagen werkt als venster voor je basislijn om drie redenen. Het zijn ongeveer twee menstruatiecycli, dus cyclische schommelingen middelen uit. Het beslaat twee gangbare trainingsmesocycli, dus aanpassing op korte termijn overheerst niet. En je krijgt genoeg niet-overlappende wekelijkse metingen om een standaarddeviatie iets te laten betekenen; met minder schommelt de SD zelf te sterk.

## Wat één lage meting wel en niet betekent

Een ochtend waarop je HRV 30% onder je gemiddelde van 7 dagen ligt, betekent dat *er iets is gebeurd*: laat eten, alcohol, slecht slapen, een stressvolle avond, het begin van een ziekte, zware training de dag ervoor of gewone biologische ruis van dag tot dag. Op zichzelf zegt het niet dat je moet rusten, hard moet trainen, in paniek moet raken of moet juichen.

Een *patroon* is wel diagnostisch. Drie dagen achter elkaar meer dan één standaarddeviatie onder je basislijn is een signaal. Een eenmalige daling van 25% na een bekende stressfactor vertelt je iets over die stressfactor, niet over je gezondheid. Een daling van 25% zonder aanwijsbare oorzaak die na 72 uur nog niet is verdwenen, verdient aandacht van een zorgverlener, niet van een consumentenapp.

Voor zelfexperimenten lijkt me deze drempel ongeveer goed: **minstens 10 metingen onder dezelfde omstandigheden binnen een venster van 60 dagen, en minstens één standaarddeviatie verschil tussen de omstandigheden**, voordat je een bevinding als iets anders behandelt dan ruis. Een “inzicht” met minder houvast is meestal een gok.

## Waarom HRV in de winter daalt (en andere seizoensruis)

Als je een Apple Watch draagt door een winter op het noordelijk halfrond, kun je verwachten dat je HRV-basislijn tussen oktober en februari 10 tot 20% zakt. De gebruikelijke oorzaken zijn kou, minder daglicht, minder aerobe activiteit, meer tijd binnen en een veranderd slaappatroon. Geen ervan wijst op ziekte, en ze trekken het getal allemaal omlaag.

Een winterdip lezen als “er is iets mis met me” is een van de meest gemaakte leesfouten. De juiste lezing is: “in de winter ligt mijn HRV lager, en dit is de nieuwe basislijn om afwijkingen aan te meten.” De basislijn hoort te verschuiven, want je fysiologie verschuift mee met de wereld om je heen.

## Wat dit in de praktijk betekent

Uit dit alles volgen een paar praktische regels:

1. **Vergelijk je cijfer nooit met dat van een ander.** Ook niet met dat van een vriend, een vreemde op Reddit of een infographic met een “normaal bereik”. Vergelijk jezelf met jezelf.

2. **Volg trends.** De HRV van één dag is vooral ruis. Het voortschrijdende gemiddelde over 7 dagen is het signaal, en de basislijn over 60 dagen is het kader waarmee je dat signaal kunt duiden.

3. **Lees het als een afwijking van je eigen basislijn.** HRV is bij benadering lognormaal verdeeld, dus hetzelfde verschil in milliseconden weegt zwaarder bij een lage basislijn dan bij een hoge. Pas als je de SDNN van vandaag uitdrukt als procentuele afwijking van je persoonlijke voortschrijdende gemiddelde, kun je de waarde duiden.

4. **Spoor je stressfactoren op.** Als je HRV steeds daalt na late trainingen, alcohol of lange schermtijd, kun je daar iets mee. Het probleem is een oorzaak die je niet kent, niet de daling zelf.

5. **Reken op seizoensverschuiving.** Lager in de winter en hoger in de zomer is normaal. Een pandemie, een ziekte, stress in je leven of een nieuwe baby verschuiven je basislijn ook. Zie het als een kader dat meebeweegt.

[Observa](/nl/apps/observa/) doet een groot deel hiervan voor je. De app zet je HRV (SDNN) af tegen je eigen gebruikelijke bereik, met een trend over 7 dagen gratis en over 30, 90 of 365 dagen met Premium. HRV weegt ook voor 25% mee in de dagelijkse gereedheidsscore, en ‘Waarom deze score?’ legt je in gewone taal uit wanneer je HRV buiten je gebruikelijke bereik valt en daardoor de score verandert. De analyse draait op je apparaat, en de app vergelijkt *jou, vandaag, met je eigen normaal*: de enige HRV-vergelijking die zin heeft.

## Kort samengevat

- **Absolute HRV verschilt 3 tot 10 keer tussen gezonde volwassenen.** Je cijfer vergelijken met dat van een ander zegt niets.
- **Je eigen basislijn, opgebouwd over weken, is het enige kader waarmee HRV bruikbaar wordt.** Schommelingen van 10 tot 25% van dag tot dag zijn normaal.
- **Trends tellen, losse metingen niet.** Drie dagen achter elkaar meer dan één SD onder je basislijn is een signaal. Eén dag is ruis.
- **HRV ligt in de winter lager dan in de zomer.** Een lagere waarde in de winter is normaal; die als ziekte opvatten is de bekende fout.
- **Lees SDNN als afwijking van je eigen basislijn.** HRV is bij benadering lognormaal verdeeld, dus vergelijk elke dag als percentage met je persoonlijke gemiddelde, niet met vaste drempels in milliseconden.

Het cijfer stond altijd al in je Gezondheid-app. Wat ontbrak, was een basislijn om het tegen af te zetten.
