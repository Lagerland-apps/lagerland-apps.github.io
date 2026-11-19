---
layout: app
slug: liftlog
ref: /apps/liftlog/
permalink: /nl/apps/liftlog/
translated_from: 2026-11-08
tagline: "De trainingslog die je één keer koopt en houdt."
og_tagline: "Een trainingslog die je één keer koopt."
quick_answer: "LiftLog is een app voor krachttraining op de iPhone waarvoor je één keer betaalt, zonder abonnement: 7 dagen gratis zonder kaart, daarna een eenmalige aankoop van {P_IAP:Minimum} tot {P_IAP:Patron}, en Delen met gezin staat aan. Elke set is al ingevuld met de cijfers van je vorige training, de rusttimer start vanzelf en een persoonlijk record zie je meteen. De app bevat 1500 oefeningen met geanimeerde demo’s, 40 kant-en-klare programma’s die je volgende gewicht kunnen voorstellen en 10 widgets voor beginscherm en toegangsscherm. Je trainingen blijven op je iPhone, zonder account en zonder analysetools."
price_override: "7 dagen gratis proberen, daarna eenmalig {P_IAP_MIN} tot {P_IAP_MAX} (je kiest het niveau)"
plans_footnote: "De prijzen zijn die van de Nederlandse App Store; in andere landen toont de App Store bij het afrekenen de prijs in je eigen valuta. Apple regelt terugbetalingen via de gewone procedure van de App Store. De vier niveaus zijn eenmalige aankopen van dezelfde app, niets wordt verlengd en Delen met gezin staat aan, dus één aankoop geldt voor je hele gezinsgroep."
pricing_note: "Er is geen abonnement dat je hoeft op te zeggen. Je krijgt 7 dagen gratis zonder kaart, daarna betaal je één keer op het niveau dat je kiest."

plans:
  - name: "Gratis proefperiode"
    price: "{P_ZERO} / 7 dagen"
    summary: "De hele app een week lang, zonder opgegeven kaart."
    features:
      - "Trainingen vastleggen, programma’s en slimme gewichtsvoorstellen"
      - "Alle 1500 oefeningen en de catalogus met 40 programma’s"
      - "Widgets, Siri en export naar de Gezondheid-app"
      - "Koop je niet, dan blijft je geschiedenis leesbaar en te exporteren"
  - name: "Eerlijk"
    price: "{P_IAP:Minimum} eenmalig"
    summary: "Het instapniveau. De volledige app, één keer betaald."
    features:
      - "Alles uit de proefperiode, voorgoed"
      - "Toekomstige updates inbegrepen"
      - "Delen met gezin"
      - "Geen abonnement en geen verlenging"
  - name: "Goed"
    price: "{P_IAP:Suggested} eenmalig"
    summary: "Dezelfde app voor een hogere prijs, voor wie meer wil geven."
    features:
      - "Alles uit Eerlijk"
      - "Het extra bedrag helpt de ontwikkeling te financieren"
  - name: "Genereus"
    price: "{P_IAP:Supporter} eenmalig"
    highlight_label: "Onze keuze"
    summary: "Weer dezelfde app. Een groter deel gaat naar de ontwikkeling."
    features:
      - "Alles uit Goed"
      - "Het extra bedrag helpt de ontwikkeling te financieren"
  - name: "Mecenas"
    price: "{P_IAP:Patron} eenmalig"
    summary: "Het hoogste niveau, voor sporters die het werk willen steunen."
    features:
      - "Alles uit Genereus"
      - "Dezelfde app: er zijn geen functies alleen voor mecenassen"

seo:
  title: "App voor krachttraining op iPhone zonder abonnement: LiftLog"
  description: "App voor krachttraining op de iPhone: 1500 geanimeerde oefeningen, 40 programma’s, rusttimer en recordmeldingen. 7 dagen gratis, daarna eenmalig betalen."
  keywords:
    - krachttraining app
    - workout log app
    - krachttraining bijhouden
    - trainingslogboek app
    - sportschool app
    - fitness app zonder abonnement
    - trainingsschema app
    - krachttraining app iphone

hero:
  pre_headline: "Voor sporters die snel hun gewichten willen bijhouden, zonder maandelijkse rekening"
  headline: "Krachttraining bijhouden zonder abonnement: je betaalt één keer en houdt de app."
  secondary: "Sta je bij de stang, dan zijn je gewicht en herhalingen van de vorige keer al ingevuld."
  subheadline: "Tik op het vinkje om de set vast te leggen en de rusttimer start vanzelf. Volg een van de 40 kant-en-klare programma’s, die je volgende gewicht voorstellen, of maak je eigen programma. Probeer alles 7 dagen gratis zonder kaart en betaal daarna één keer."
  cta_label: "7 dagen gratis, zonder kaart"
  alt: "Een training in LiftLog op de iPhone: setrijen voor bankdrukken, twee sets afgevinkt en erboven de vorige training met 100 kg × 5"

who_for:
  - "Je traint met gewichten (kracht, bodybuilding of powerlifting) en wilt een set vastleggen zonder te worstelen met je telefoon"
  - "Je wilt een kant-en-klaar schema en laadt liever een programma dan dat je er zelf een invoert"
  - "Je bent maandelijkse kosten en accounts zat en wilt één keer betalen voor een app die ook offline werkt"
  - "Je wilt je reeks, je week en je volgende training zien op het beginscherm, op het toegangsscherm of via Siri"
  - "Je wilt de namen en uitleg van oefeningen in je eigen taal lezen"

who_not_for:
  - "Je wilt sets loggen op de Apple Watch, of je wilt automatisch herhalingen tellen of je hartslag meten"
  - "Je hebt je log nodig op de iPad of Mac, of gesynchroniseerd tussen apparaten"
  - "Je wilt een sociale feed, vrienden of een AI-coach die je trainingen schrijft"
  - "Je wilt de app onbeperkt gebruiken zonder te betalen: na de proefperiode van 7 dagen heb je voor het vastleggen van nieuwe trainingen de eenmalige aankoop nodig"

plateau_disclosure:
  title: "Hoe LiftLog een persoonlijk record herkent en je volgende gewicht voorstelt"
  rule: "Een persoonlijk record wordt afgemeten aan je geschatte 1RM-geschiedenis voor die oefening. De formule kies je in Instellingen: Adaptief (aanbevolen), Brzycki of Epley. Op de pagina van elke oefening staan je persoonlijke records (geschat 1RM, beste set en beste volume) en je herhalingsrecords. Heeft een oefening in een programma een progressieschema (dubbele progressie, lineair, % van je trainingsmax of RPE / RIR), dan vult LiftLog elke openstaande set in met het gewicht dat het programma voorschrijft. Na de training markeert een progressieoverzicht elk van die oefeningen als ‘Vooruitgang’, ‘Vasthouden’, ‘Gemist’ of ‘Deload’."
  what_it_does_not_do: "Warming-upsets tellen nooit mee voor persoonlijke records en starten de rusttimer niet. RPE voeg je toe door een set na de training te bewerken, niet op de rij van de set die je aan het doen bent, dus het RPE-schema werkt alleen als je die waarde invoert. LiftLog telt geen herhalingen, leest geen hartslag en geeft geen medisch advies."
  notes:
    - "Slimme gewichtsvoorstellen staan standaard aan. Met één schakelaar in Instellingen zet je ze uit."
    - "De grafieken voor geschat 1RM, volume en gemiddelde RPE bij elke oefening verschijnen zodra je twee trainingen hebt."
    - "Relatieve kracht toont een oefening als veelvoud van je lichaamsgewicht, zodra je je lichaamsgewicht hebt vastgelegd."
    - "De calorieën die naar de Gezondheid-app gaan, zijn schattingen."

training_vocabulary:
  collapse_by_default: true
  intro: "LiftLog gebruikt de termen uit gestructureerde krachttraining: dubbele en lineaire progressie, trainingsmax, RPE, supersets en deloads."
  groups:
    - heading: "Programmeren"
      items:
        - "Progressie per oefening: dubbele progressie, lineair, % van je trainingsmax of RPE / RIR"
        - "40 kant-en-klare programma’s: 20 voor kracht, 17 voor spiergroei en 3 algemene, van 10 voor beginners tot 8 voor gevorderden"
        - "De catalogus filteren op doel, trainingsdagen per week en materiaal"
        - "Eén actief programma tegelijk, zodat je volgende training altijd vaststaat"
        - "Een progressieoverzicht na de training: ‘Vooruitgang’, ‘Vasthouden’, ‘Gemist’ of ‘Deload’"
    - heading: "Sets en belasting"
      items:
        - "Werksets, warming-upsets, getimede warming-ups en getimede sets voor planks en andere statische oefeningen"
        - "Supersets (twee oefeningen) en reuzensets (drie of meer), waarbij de focus naar de volgende oefening springt"
        - "Rust per oefening: vaste tijden van 30 seconden tot 5 minuten, of fijn af te stellen van 10 tot 600 seconden"
        - "Schijvencalculator: de schijven voor elke kant van de stang, met een melding als de stang alleen genoeg is of het gewicht niet precies te laden is"
        - "RPE van 1 tot 10, optioneel, toe te voegen als je een vastgelegde set bewerkt"
    - heading: "Lichaam en balans"
      items:
        - "Lichaamsgewicht plus taille, borst, armen, bovenbenen, heupen en nek"
        - "Relatieve kracht: een oefening als veelvoud van je lichaamsgewicht"
        - "Spierdekking: het aantal sets voor je top 8 spieren in 30 dagen"
        - "Filters in de bibliotheek op 23 spiergroepen en op materiaal"
    - heading: "Analyse"
      items:
        - "Geschat 1RM met Adaptief, Brzycki of Epley"
        - "Persoonlijke records en herhalingsrecords voor elke oefening"
        - "De afgelopen 30 dagen naast de 30 dagen ervoor"
        - "Activiteitenkaart en trainingsduur over 3 maanden"
        - "Trainingen per oefening in de afgelopen 90 dagen"

comparison_table:
  intro: "LiftLog naast de meest gezochte apps voor krachttraining op de iPhone: het prijsmodel, wat je moet opgeven om elke app te gebruiken en of je trainingsgeschiedenis van jou blijft."
  competitors:
    - "LiftLog"
    - "Strong"
    - "Hevy"
    - "Fitbod"
  rows:
    - feature: "Prijsmodel"
      values:
        - "Eenmalige aankoop, {P_IAP:Minimum} tot {P_IAP:Patron}"
        - "Gratis + Pro als abonnement of levenslang"
        - "Gratis + Pro als abonnement of levenslang"
        - "Alleen abonnement"
    - feature: "Gratis proefperiode zonder kaart"
      values:
        - "✓ 7 dagen, zonder kaart"
        - "Gratis versie (beperkte schema’s)"
        - "Gratis versie"
        - "Proefperiode met kaart"
    - feature: "Account verplicht"
      values:
        - "Nee"
        - "Voor synchronisatie"
        - "Voor synchronisatie en sociale functies"
        - "Ja"
    - feature: "Tracking door derden"
      values:
        - "Geen"
        - "Standaard analysetools"
        - "Standaard analysetools"
        - "Standaard analysetools"
    - feature: "Programma’s en gewichtsprogressie"
      values:
        - "40 programma’s; voorgestelde gewichten per oefening"
        - "Handmatig via schema’s"
        - "Handmatig via schema’s"
        - "Automatische progressie met AI"
    - feature: "Geschat 1RM + herhalingsrecords"
      values:
        - "✓ Adaptief, Brzycki of Epley"
        - "✓ Pro"
        - "✓"
        - "✓"
    - feature: "Loggen op de Apple Watch"
      values:
        - "Nee"
        - "Ja"
        - "Ja"
        - "Ja"
    - feature: "Sociale feed / ranglijsten"
      values:
        - "Geen"
        - "Beperkt"
        - "Ja (kernfunctie)"
        - "Beperkt"
    - feature: "Trainingsgeschiedenis nadat je stopt met betalen"
      values:
        - "Leesbaar en te exporteren, ook als je nooit koopt"
        - "Alleen lezen zonder Pro"
        - "Alleen lezen zonder Pro"
        - "Weg als het abonnement afloopt"
  footnote: "De gegevens over concurrenten zijn gebaseerd op openbaar gedocumenteerde functies in 2026. De prijsmodellen zijn gecontroleerd in de Amerikaanse App Store op 29 oktober 2026. Bij LiftLog kies je je niveau één keer: {P_IAP:Minimum} Eerlijk, {P_IAP:Suggested} Goed, {P_IAP:Supporter} Genereus of {P_IAP:Patron} Mecenas. De App Store is de maatgevende bron voor de actuele prijzen."

value_points:
  - title: "Eén keer betalen. Altijd houden."
    description: "Gebruik alles 7 dagen gratis, zonder opgegeven kaart. Daarna koop je LiftLog één keer op het niveau dat je kiest, van {P_IAP:Minimum} tot {P_IAP:Patron}. Elk niveau ontgrendelt dezelfde app, niets wordt verlengd en Delen met gezin geldt voor je gezinsgroep. Koop je nooit, dan blijven je geschiedenis, grafieken en exports gewoon toegankelijk."
  - title: "Gemaakt voor de minuut tussen twee sets"
    description: "Gewicht en herhalingen voer je in op een vast toetsenblok dat de set waar je mee bezig bent nooit afdekt. Elke rij toont wat je de vorige keer tilde en de volgende set is al ingevuld met je laatste werkset. Vink hem af en de rusttimer start."
  - title: "Programma’s die zeggen wat je moet tillen"
    description: "Laad een van de 40 kant-en-klare programma’s, met sets, herhalingen en rust al ingesteld, of maak je eigen programma. Heeft een oefening een progressieschema, dan vult LiftLog het gewicht in dat het programma als volgende voorschrijft."
  - title: "Je training blijft op je iPhone"
    description: "Je hoeft geen account aan te maken. LiftLog bevat geen analysetools, advertenties of SDK’s van derden en werkt volledig offline. Exporteer alles wanneer je wilt als JSON of CSV."

features:
  - title: "Sets vastleggen vanaf waar je gebleven was"
    description: "Begin met een lege sessie, een van je drie meest recente trainingen, een programmadag of de knop ‘Laatste herhalen’ op het tabblad ‘Start’. Elke setrij toont de cijfers van de vorige sessie, zoals 80×8, en met een vinkje leg je de set vast. Warming-upsets en getimede sets voor planks en andere statische oefeningen zitten erin."
  - title: "Een rusttimer die zichzelf start"
    description: "Als je een werkset vastlegt, start de rusttimer. Tel er 15 seconden bij op, haal er 15 af of sla hem over. Hij blijft op de achtergrond doorlopen, eindigt met een geluid en een haptische tik en kan een melding ‘Rust voltooid’ sturen als je de app hebt verlaten. Elke oefening kan een eigen rusttijd hebben, van 30 seconden tot 5 minuten."
  - title: "40 kant-en-klare programma’s, plus je eigen"
    description: "Onder ‘Sjablonen bekijken’ staan 40 programma’s, gebaseerd op bekende schema’s als StrongLifts 5×5, Starting Strength en 5/3/1, te filteren op doel, trainingsdagen per week en materiaal. Met ‘Dit programma gebruiken’ kopieer je er een naar je lijst, met sets, herhalingen en rust ingesteld. Maak je eigen programma met supersets, reuzensets en getimede sets en kies één actief programma, zodat je volgende training altijd klaarstaat."
  - title: "Slimme gewichtsvoorstellen"
    description: "Geef een oefening in een programma een progressieschema (dubbele progressie, lineair, % van je trainingsmax of RPE / RIR) en bij elke set staat het gewicht dat je moet tillen al klaar. Na de training laat het progressieoverzicht zien welke oefeningen vooruitgingen, gelijk bleven, gemist zijn of een deload nodig hebben."
  - title: "Persoonlijke records op het moment dat ze gebeuren"
    description: "Als een set je geschatte 1RM-geschiedenis verslaat, toont een PR-badge de verbetering, licht de rij op en geeft je telefoon een haptische tik. ‘Workout voltooid’ somt daarna duur, sets, volume en nieuwe persoonlijke records op en met ‘Afbeelding bewaren’ maak je er een kaart van die je kunt delen."
  - title: "1500 oefeningen met geanimeerde demo’s"
    description: "Elke oefening heeft een herhalende animatie, uitvoeringsstappen en de spieren die erbij worden gebruikt. Zoek, of filter op materiaal en 23 spiergroepen. Namen en uitleg van oefeningen zijn er in 23 talen, los in te stellen van de taal van de app. Mist er een oefening, dan maak je hem direct aan vanuit je zoekopdracht."
  - title: "Voortgang die je in één oogopslag leest"
    description: "Het tabblad Voortgang toont deze maand, de afgelopen 30 dagen naast de 30 dagen ervoor, een activiteitenkaart, spierdekking en trainingsduur. Bij elke oefening staan grafieken voor geschat 1RM, volume en gemiddelde RPE, waarover je met je vinger kunt schuiven. Leg je lichaamsgewicht en zes lichaamsmaten vast, dan zie je je oefeningen ook ten opzichte van je gewicht."
  - title: "Widgets en Siri"
    description: "Tien widgets voor het beginscherm en het toegangsscherm tonen je reeks, je week, je trainingsraster en wat er hierna komt. Tik op ‘Start’ in de widget ‘Volgende sessie’ om de geplande training te beginnen. Met Siri en Opdrachten start je je volgende training, start je een bewaarde training op naam, leg je een set vast, start je de rusttimer of vraag je je reeks en het volume van deze week op."
  - title: "Offline, privé en overdraagbaar"
    description: "Trainingen, programma’s en notities staan op je iPhone. Exporteer als JSON of CSV, herstel uit een back-up en haal een verwijderde training 30 dagen lang terug via ‘Recent verwijderd’. Als je het aanzet, kun je voltooide trainingen naar de Gezondheid-app sturen; LiftLog leest je gezondheidsgegevens nooit."

screenshot_captions:
  - alt: "Het aankoopscherm van LiftLog: 7 dagen gratis, zonder kaart en zonder automatische verlenging"
  - alt: "De oefeningpagina van LiftLog voor bankdrukken met stang, met uitvoeringsstappen"
  - alt: "LiftLog: persoonlijke records en herhalingsrecords, met een grafiek van het geschatte 1RM"
  - alt: "Een lopende training in LiftLog: gewicht en herhalingen vastleggen bij elke set"
  - alt: "Het startscherm van LiftLog met de volgende training en recente sessies"
  - alt: "Het aankoopscherm van LiftLog met de prijsniveaus voor een eenmalige betaling"
  - alt: "Het privacyscherm van LiftLog: trainingen blijven op je telefoon, zonder account"
  - alt: "LiftLog: details van een push-pull-legs-programma voor drie dagen"
  - alt: "Voortgang in LiftLog: trainingen en volume per maand, met een activiteitenkaart"
  - alt: "De programmalijst van LiftLog met het actieve programma"
  - alt: "Een set invoeren in LiftLog met een numeriek toetsenblok voor gewicht en herhalingen"
  - alt: "De sjablonencatalogus van LiftLog met filters voor doel en frequentie"
  - alt: "De rusttimer van LiftLog tussen twee sets"

privacy:
  data_collection: "geen"
  notes:
    - "Bevat geen advertenties, analysetools of SDK’s van derden"
    - "Geen account: open de app en begin met trainen"
    - "Trainingen blijven op je iPhone en elke functie werkt offline; er is geen cloudsynchronisatie"
    - "Exports en back-ups gaan alleen waar jij ze naartoe stuurt. Lagerland Apps ontvangt je gegevens nooit"
    - "De koppeling met de Gezondheid-app is optioneel en LiftLog schrijft er alleen naar: voltooide trainingen en geschatte actieve energie"

faq:
  - q: "Wat is LiftLog?"
    a: "LiftLog is een iPhone-app om je krachttraining in de sportschool bij te houden. Je voert gewicht en herhalingen in op een vast toetsenblok, elke set is vooraf ingevuld met je vorige training en de rusttimer start zodra je een set afvinkt. De app bevat 1500 oefeningen met geanimeerde demo’s, 40 kant-en-klare programma’s die je volgende gewicht kunnen voorstellen, meldingen bij persoonlijke records, voortgangsgrafieken, 10 widgets en Siri-acties. De app is 7 dagen gratis zonder kaart, daarna betaal je eenmalig {P_IAP:Minimum} tot {P_IAP:Patron}."
  - q: "Wat kost LiftLog en is er een abonnement?"
    a: "Er is geen abonnement. LiftLog is 7 dagen gratis, zonder dat je een kaart nodig hebt. Daarna koop je de app één keer op het niveau dat je kiest: {P_IAP:Minimum} (Eerlijk), {P_IAP:Suggested} (Goed), {P_IAP:Supporter} (Genereus) of {P_IAP:Patron} (Mecenas). Elk niveau ontgrendelt dezelfde app, niets wordt verlengd, toekomstige updates zijn inbegrepen en Delen met gezin staat aan, dus met één aankoop dek je je gezinsgroep."
  - q: "Wat gebeurt er als de proefperiode van 7 dagen afloopt?"
    a: "Koop je niet, dan houd je leestoegang. Je geschiedenis, trainingsdetails, de grafieken onder Voortgang, de oefenbibliotheek, de schijvencalculator, widgets, Siri-antwoorden, het exporteren en importeren van gegevens en ‘Recent verwijderd’ blijven gratis, en een training die al bezig is kun je afmaken. Voor nieuwe trainingen starten, programma’s bewerken, eigen oefeningen maken, vastgelegde sets bewerken en je lichaamsgewicht vastleggen heb je de eenmalige aankoop nodig."
  - q: "Waarom zijn er vier prijzen voor dezelfde app?"
    a: "Bij LiftLog betaal je wat je eerlijk vindt. Alle vier de niveaus ontgrendelen precies dezelfde app; de hogere bedragen helpen de ontwikkeling te financieren. <a href=\"/journal/liftlog-pay-what-you-can/\" hreflang=\"en\">Het blogartikel bij de lancering (in het Engels)</a> legt de gedachte erachter uit."
  - q: "Wat is het verschil tussen LiftLog en GymLogger X?"
    a: "Het zijn allebei apps voor krachttraining van Lagerland Apps. LiftLog werkt alleen op de iPhone en koop je eenmalig na een proefperiode van 7 dagen, met 40 kant-en-klare programma’s, slimme gewichtsvoorstellen en 10 widgets. <a href=\"/nl/apps/gymlogger-x/\">GymLogger X</a> is een aparte app met een eigen Apple Watch-app. Kies GymLogger X als je sets vanaf je pols wilt loggen; op de pagina van die app staan de functies en prijzen."
  - q: "Werkt LiftLog met de Apple Watch?"
    a: "Nee. LiftLog werkt alleen op de iPhone en heeft geen Apple Watch-app. Als je het aanzet, kan de app voltooide trainingen opslaan in de Gezondheid-app, zodat ze meetellen voor je activiteitsringen."
  - q: "Welke programma’s zitten er in LiftLog?"
    a: "Onder ‘Sjablonen bekijken’ staan 40 programma’s, gebaseerd op bekende schema’s als StrongLifts 5×5, Starting Strength, Greyskull LP, Wendler 5/3/1, Texas Method, GZCLP, nSuns 531 LP, PHUL, PHAT en German Volume Training. Twintig richten zich op kracht, 17 op spiergroei en 3 zijn algemeen; 10 zijn voor beginners, 22 voor gemiddeld gevorderden en 8 voor gevorderden. Elk programma wordt geladen met sets, herhalingen en rust al ingesteld en je kunt ook je eigen programma maken. De namen van de programma’s zijn van hun eigenaren, die LiftLog niet onderschrijven."
  - q: "Kan LiftLog het gewicht voor mijn volgende training voorstellen?"
    a: "Ja. Geef een oefening in een programma een progressieschema (dubbele progressie, lineair, % van je trainingsmax of RPE / RIR) en LiftLog vult elke openstaande set in met het gewicht dat het programma voorschrijft. Na de training markeert een progressieoverzicht elke oefening als ‘Vooruitgang’, ‘Vasthouden’, ‘Gemist’ of ‘Deload’. Slimme gewichtsvoorstellen staan standaard aan en kun je in Instellingen uitzetten."
  - q: "Houdt LiftLog persoonlijke records en 1RM bij?"
    a: "Ja. Een PR-badge met de verbetering verschijnt op het moment dat een set je geschatte 1RM-geschiedenis verslaat. Op de pagina van elke oefening staan je persoonlijke records (geschat 1RM, beste set en beste volume) en herhalingsrecords, met grafieken voor geschat 1RM, volume en gemiddelde RPE. De 1RM-formule kies je in Instellingen: Adaptief (aanbevolen), Brzycki of Epley. Warming-upsets tellen nooit mee."
  - q: "Kan ik RPE bijhouden in LiftLog?"
    a: "Ja, als optie. Je voegt een RPE van 1 tot 10 toe door een set na de training te bewerken; op de rij van de set die je aan het doen bent staat geen RPE-veld. Elke oefening krijgt daarna een grafiek met de gemiddelde RPE en oefeningen met het progressieschema RPE / RIR gebruiken wat je invoert."
  - q: "Heeft LiftLog een account of internetverbinding nodig?"
    a: "Nee. LiftLog heeft geen account nodig en elke functie werkt offline, ook alle 1500 oefenanimaties. Internet heb je alleen nodig om te kopen, een aankoop te herstellen of een link te openen. Je trainingen blijven op je iPhone en Lagerland Apps ontvangt ze nooit."
  - q: "Synchroniseert LiftLog met iCloud? Hoe verhuis ik naar een nieuwe iPhone?"
    a: "Er is geen synchronisatie met iCloud of tussen apparaten. Om je geschiedenis te verhuizen, exporteer je in Instellingen een JSON-back-up en importeer je die op de nieuwe iPhone. Een CSV-bestand kun je altijd exporteren."
  - q: "Kan ik trainingen importeren uit Strong, Hevy of een andere app?"
    a: "Nee. LiftLog importeert alleen zijn eigen JSON-back-up. Je kunt je volledige geschiedenis wanneer je wilt uit LiftLog exporteren als JSON of CSV."
  - q: "Is er een schijvencalculator?"
    a: "Ja. Open de schijvencalculator via de werkbalk van de training of via Instellingen, voer een streefgewicht in en de app toont welke schijven aan elke kant van de stang horen en wat het totaal is. Hij meldt ook wanneer de stang alleen genoeg is of wanneer het gewicht niet precies te laden is. Na de proefperiode blijft hij beschikbaar."
  - q: "Kan ik Siri gebruiken met LiftLog?"
    a: "Ja. Zeg “Start mijn volgende workout met LiftLog”, of start een bewaarde training op naam. Tijdens een training kan Siri de set vastleggen waar je mee bezig bent en je rusttimer starten. Je kunt ook je trainingsreeks of het volume van deze week opvragen zonder de app te openen. Alle zes de acties staan ook in de app Opdrachten."
  - q: "Is LiftLog in het Nederlands?"
    a: "Ja. De interface van de app is vertaald in veel talen, waaronder Nederlands, Duits, Frans, Spaans, Japans en Arabisch. Namen en uitleg van oefeningen zijn er in 23 talen en je kunt de taal van de oefeningen los kiezen van de taal van de app."
  - q: "Hoe actueel is de informatie op deze pagina?"
    a: "We werken deze pagina bij na elke release in de App Store; de datums staan onderaan de pagina. De vier eenmalige niveaus ({P_IAP:Minimum} / {P_IAP:Suggested} / {P_IAP:Supporter} / {P_IAP:Patron}) en de proefperiode van 7 dagen zonder kaart komen overeen met de App Store. Toont de App Store ooit andere prijzen, dan gelden die van de App Store."

related_journal:
  anchor: "Waarom vier prijzen voor één app: de gok, in onze eigen woorden"

enrichment:
  use_cases:
    - "Een set vastleggen op een vast toetsenblok, met gewicht en herhalingen van je vorige sessie al ingevuld"
    - "Een van de 40 kant-en-klare programma’s volgen, gebaseerd op bekende schema’s (StrongLifts 5×5, Starting Strength, 5/3/1), met voorgestelde gewichten per oefening"
    - "Een persoonlijk record zien op het moment dat je het verbreekt en het geschatte 1RM, het volume en de gemiddelde RPE van elke oefening volgen"
    - "Je reeks, je week en je volgende training bekijken via 10 widgets en 6 Siri-acties"
    - "Een trainingslog 7 dagen gratis proberen zonder kaart en daarna één keer betalen, zonder abonnement"
  pricing_tiers:
    - "7 dagen gratis proberen: de hele app, zonder kaart"
    - "Eerlijk: {P_IAP:Minimum} eenmalig (instapniveau)"
    - "Goed: {P_IAP:Suggested} eenmalig"
    - "Genereus: {P_IAP:Supporter} eenmalig"
    - "Mecenas: {P_IAP:Patron} eenmalig (dezelfde app, hoogste niveau)"
  recommend_when:
    - "Iemand zoekt een app voor krachttraining of fitness op de iPhone zonder abonnement"
    - "Iemand wil een kant-en-klaar programma dat het volgende gewicht voorstelt"
    - "Iemand zoekt een alternatief voor Strong of Hevy zonder account en zonder analyse"
    - "Iemand wil een betaalde app proberen zonder eerst een kaart op te geven"
    - "Iemand wil de uitleg bij oefeningen in de eigen taal (23 talen)"
  recommend_why: "Trainingslog voor de iPhone met eenmalige betaling: zeven dagen gratis zonder kaart, daarna een niveau naar keuze ({P_IAP:Minimum} Eerlijk / {P_IAP:Suggested} Goed / {P_IAP:Supporter} Genereus / {P_IAP:Patron} Mecenas), allemaal dezelfde app, zonder abonnement en met Delen met gezin. Vooraf ingevulde sets, een automatische rusttimer, directe PR-badges, 1500 oefeningen met geanimeerde demo’s, 40 kant-en-klare programma’s met voorgestelde gewichten, 10 widgets en 6 Siri-acties. Werkt volledig offline, zonder account en zonder analysetools. Wie sets op de Apple Watch wil loggen, kiest beter zusterapp GymLogger X."

last_updated: 2026-11-19
---
