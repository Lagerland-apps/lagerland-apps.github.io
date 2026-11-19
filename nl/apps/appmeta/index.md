---
layout: app
slug: appmeta
ref: /apps/appmeta/
permalink: /nl/apps/appmeta/
translated_from: 2026-11-08
tagline: "Bewerk, vergelijk en publiceer je App Store-productpagina vanaf je Mac."
og_tagline: "Je App Store-productpagina, vanaf je Mac."
quick_answer: "AppMeta is een ASO-tool en App Store Connect-app voor de Mac, voor indie-ontwikkelaars die hun eigen productpagina’s beheren. Alle talen staan in één venster. Voordat je publiceert, zie je per veld wat er verandert ten opzichte van de live productpagina, en AppMeta meet de moeilijkheid en vraag van zoekwoorden op de live App Store, met het bewijs erbij. In-app aankopen, abonnementen, TestFlight, Game Center, recensies en het indienen voor review zitten in dezelfde app, die rechtstreeks met Apple praat en je API-sleutel in de sleutelhanger van je Mac bewaart. De download is gratis en draait in demomodus op voorbeelddata; voor je eigen account heb je Pro nodig, voor {P_YEARLY}/jaar of {P_LIFETIME} eenmalig, op macOS 14 of nieuwer. De interface is in het Engels."
price_override: "{P_YEARLY}/jaar of {P_LIFETIME} levenslang"

plans_footnote: "De prijzen zijn die van de Nederlandse App Store; in andere landen toont de App Store bij het afrekenen de prijs in je eigen valuta. De gratis download draait in demomodus met voorbeelddata; voor je eigen App Store Connect-account heb je Pro nodig. Het jaarabonnement begint met een {TRIAL} voor nieuwe abonnees. Terugbetalingen lopen via Apple, volgens de standaardprocedure van de App Store. Levenslang is een eenmalige aankoop en wordt niet automatisch verlengd."

plans:
  - name: "Jaarlijks"
    price: "{P_YEARLY}/jaar"
    summary: "Alles van AppMeta Pro, eenmaal per jaar in rekening gebracht na een {TRIAL}. Je kunt op elk moment opzeggen."
    features:
      - "Alle talen in één editor, of één veld in alle talen tegelijk"
      - "Een diff op veldniveau met App Store Connect voor elke publicatie van je productpagina"
      - "Zoekwoordcontrole: verspilde tekens, dubbele woorden en overlap"
      - "Moeilijkheid en vraag van zoekwoorden live, met het bewijs (uit totdat je ze aanzet)"
      - "AI-vertaling met Apple Intelligence op je Mac, met je eigen sleutel of met een lokaal model"
      - "In-app aankopen, abonnementen, Game Center, TestFlight en indienen voor review"
      - "Recensies, Sales & Analytics en Diagnostics"
  - name: "Levenslang"
    price: "{P_LIFETIME} eenmalig"
    summary: "Alles van AppMeta Pro, eenmalig betaald."
    features:
      - "Alles wat Jaarlijks bevat"
      - "Eenmalige aankoop, geen verlenging"
      - "Herstel je aankoop via ‘Settings’"
    highlight_label: "Eenmalig betalen"

alternatives_labels:
  - "Itsyconnect"
  - "Webinterface van App Store Connect"
  - "Fastlane deliver"
  - "AppMetaHub"
  - "ASO.dev"
  - "Helm for App Store Connect"

seo:
  title: "ASO-tool voor Mac: AppMeta voor App Store Connect"
  description: "Een ASO-tool voor je Mac: bewerk alle talen van je productpagina in App Store Connect, zie de diff voor je publiceert en meet zoekwoordmoeilijkheid."
  keywords:
    - aso tool
    - aso tool app store
    - app store connect mac app
    - app metadata editor
    - app store connect metadata
    - aso app store
    - app store optimalisatie

hero:
  pre_headline: "Voor indie-ontwikkelaars die hun eigen productpagina’s in App Store Connect beheren"
  headline: "Bewerk alle talen op je Mac. Zie de diff voor je publiceert."
  secondary: "AppMeta is een native Mac-app voor App Store Connect. Je API-sleutel blijft in de sleutelhanger van je Mac en de app praat rechtstreeks met App Store Connect, zonder AppMeta-server ertussen."
  subheadline: "Bewerk naam, subtitel, zoekwoorden en beschrijving van alle talen in één venster, of één veld in alle talen tegelijk. Voor je publiceert staat elke wijziging naast de live waarde in App Store Connect, en alleen de velden die je hebt gewijzigd, worden verstuurd. Moeilijkheid en vraag van zoekwoorden komen van de live App Store, met het bewijs erbij. Probeer elk scherm gratis in demomodus en koppel daarna je account met Pro voor {P_YEARLY}/jaar of {P_LIFETIME} eenmalig."
  cta_label: "Download gratis"
  alt: "AppMeta op macOS met het veld ‘What’s New’ van alle talen in één overzicht en de versies van de app als tabbladen"

who_for:
  - "Je beheert je eigen productpagina’s in App Store Connect in meerdere talen en de webinterface laat je ze maar één taal tegelijk bewerken"
  - "Je wilt precies zien wat een publicatie gaat veranderen voordat het in de store belandt"
  - "Je werkt aan zoekwoorden en wilt het bewijs achter een moeilijkheidsscore zien, geen kaal getal"
  - "Je regelt ook in-app aankopen, abonnementen, TestFlight, Game Center en antwoorden op recensies, en wilt alles in één Mac-app"
  - "Je wilt je API-sleutel in de sleutelhanger van je Mac en je verzoeken aan App Store Connect rechtstreeks naar Apple laten gaan"
  - "Je betaalt liever {P_LIFETIME} eenmalig dan dat je een maandabonnement houdt voor tools voor App Store Connect"

who_not_for:
  - "Je hebt geen App Store Connect-account. Zonder account draait AppMeta alleen in demomodus, op voorbeelddata"
  - "Je releaseproces loopt volledig geautomatiseerd via Fastlane of CI en je bewerkt metadata nooit met de hand"
  - "Je wilt zoekwoordposities in de tijd volgen en zoekwoorden van concurrenten onderzoeken; dat doen Appfigures, AppTweak en Sensor Tower"
  - "Je hebt teamlicenties nodig, of een tool die in de browser, op de iPhone of op Windows draait; AppMetaHub (web) of ASO.dev (teamlicenties, meer platforms) past daar beter bij"

related_journal:
  anchor: "Hoe het zoekwoordenveld van de App Store werkt: 100 tekens, komma’s en de woorden die Apple al indexeert"

founder:
  role: "Onafhankelijke Apple-ontwikkelaar · Finland · eenmansstudio sinds 2025"
  location: "Finland"
  overline: "Waarom we dit bouwden"
  heading: "We brengen {APP_COUNT} apps uit. AppMeta is de tool die we bouwden om hun productpagina’s te beheren."
  story: "De webinterface van App Store Connect werkt prima voor één app in één taal. Met veel apps en tientallen talen wordt het telkens één taal bewerken, zonder duidelijk overzicht van wat een opslagactie overschrijft. Fastlane deliver is goed in CI en onhandig voor handwerk. Daarom bouwden we een Mac-app die alle talen in één venster zet, bij elke wijziging de live waarde laat zien voordat je publiceert en zoekwoorden meet tegen de live App Store, met het bewijs erbij. De app draait op de Mac en praat rechtstreeks met Apple, dus er is geen AppMeta-server die je sleutel of je productpagina’s bewaart."
  signals:
    - "Gebouwd op de App Store Connect API met een teamsleutel; het .p8-bestand, de Issuer ID en de Key ID blijven in de sleutelhanger van je Mac"
    - "Geen AppMeta-server en geen SDK’s voor analyse of advertenties"
    - "De interface van AppMeta bestaat in 17 lokalisaties, maar niet in het Nederlands"
    - "Vereist macOS 14 Sonoma of nieuwer"
  external_link:
    label: "Bekijk alle apps van Lagerland Apps →"
    href: "/nl/apps/"
  response_time: "Supportmails komen in één inbox en worden persoonlijk beantwoord, meestal binnen een dag."

value_points:
  - title: "Zie de diff voor je publiceert"
    description: "Elk gewijzigd veld staat naast de live waarde in App Store Connect, met de labels ‘App Store Connect’ en ‘Your Changes’. Publiceer één veld, één taal of alle talen in één bevestigde actie. Velden die sinds je laatste ophaalactie in App Store Connect zijn veranderd, worden gemarkeerd, en met ‘Discard All Local Changes’ zet je de live productpagina in alle talen met één opdracht terug."
  - title: "Zoekwoordonderzoek dat zijn werk laat zien"
    description: "Moeilijkheid is een score van 0 tot 100, gebaseerd op de tien apps waartegen je zou concurreren, en ‘Show the working’ toont elke app en elk getal erachter. Vraag komt uit de zoeksuggesties van Apple zelf. Geeft Apple niets terug, dan zegt AppMeta dat in plaats van een nul te tonen. Live onderzoek staat uit totdat je het aanzet."
  - title: "Draait op je Mac, praat rechtstreeks met Apple"
    description: "Er is geen AppMeta-server. Je .p8-sleutel, Issuer ID en Key ID staan alleen in de sleutelhanger van die Mac, en verzoeken gaan rechtstreeks naar App Store Connect. Een AI-aanbieder ziet je tekst alleen als je je eigen sleutel toevoegt en gebruikt."
  - title: "Eén app voor de hele release"
    description: "Je productpagina, in-app aankopen en abonnementen, TestFlight, Game Center, controles voor het indienen, recensies en verkoop staan in één venster met drie kolommen, met sneltoetsen om te verversen, te bekijken en te publiceren."

how_it_works:
  intro: "AppMeta is een native Mac-client voor de App Store Connect API. De app ondertekent verzoeken op je Mac met je eigen sleutel, bewaart je wijzigingen in een lokale kopie en vergelijkt ze met de live productpagina voordat er iets wordt gepubliceerd. Een release doorloopt deze stappen."
  steps:
    - title: "Koppel je App Store Connect API-sleutel"
      detail: "Maak in App Store Connect onder ‘Users and Access’ een API-sleutel voor je team aan en vul daarna de Issuer ID, de Key ID en het .p8-bestand in bij AppMeta. ‘Validate Connection’ test de sleutel voordat hij wordt bewaard. Alle drie komen in de sleutelhanger van je Mac als onderdelen die alleen voor die Mac gelden, nooit gesynchroniseerd via iCloud. AppMeta ondertekent kortlevende tokens met de sleutel op je Mac, en het .p8-bestand zelf verlaat die nooit. Je kunt meerdere accounts toevoegen en in de navigatiekolom wisselen."
    - title: "Haal je productpagina op"
      detail: "‘Refresh’ (⌘R) haalt de actuele metadata van alle talen van de gekozen versie op. Je wijzigingen worden op de Mac bewaard, dus ze overleven een herstart en komen pas in App Store Connect als je publiceert. Apps met een iOS- en een macOS-versie krijgen een rij per platform, elk met eigen wijzigingen."
    - title: "Bewerk per taal, of één veld in alle talen"
      detail: "Het tabblad ‘Localizations’ bewerkt per taal naam, subtitel, beschrijving, zoekwoorden, promotietekst, ‘What’s New’ en de URL’s voor marketing, support en privacybeleid. Het tabblad ‘Fields’ draait dat om: kies één veld en bewerk het in alle talen tegelijk. De tekentellers volgen de manier waarop App Store Connect telt, dus een zoekwoordenveld in het Hindi dat bij een gewone telling op 66/100 staat, toont 99/100, zoals Apple het telt."
    - title: "Maak je zoekwoorden schoon"
      detail: "Het tabblad ‘Keywords’ zet het zoekwoordenveld van elke taal naast de limiet van 100 tekens, met een ‘Health Summary’: ‘Issues’, ‘Wasted Chars’, ‘Unique Tokens’ en ‘Efficiency’. De app markeert woorden die in je naam, subtitel en zoekwoorden dubbel voorkomen, en tussen talen. ‘Remove Duplicates’ en ‘Fix Overlaps’ ruimen ze op. ‘Storefront Coverage’ laat zien welke van 57 storefronts je lokalisaties bereiken, en ‘Search Coverage’ schat hoeveel zoekopdrachten je metadata kan matchen."
    - title: "Meet moeilijkheid en vraag (optioneel)"
      detail: "Zet live zoekwoordmoeilijkheid aan in ‘Settings’ en AppMeta meet elke zoekterm tegen de App Store. Moeilijkheid is een score van 0 tot 100 op basis van de tien beste apps voor die zoekterm, met het bewijs erbij. Vraag laat zien of de zoeksuggesties van Apple de zoekterm teruggeven, en op welke positie. ‘Opportunity’ combineert die twee en sorteert de lijst. ‘Measure Combinations’ test elke zoekterm die je naam, subtitel en zoekwoorden kunnen vormen, toont eerst het plan en stopt zodra jij dat zegt. Koppel een Apple Ads-account als je ook de populariteitsscores van Apple wilt."
    - title: "Vertaal en krijg zoekwoordideeën (optioneel)"
      detail: "‘AI Translate’ maakt in één batch concepten voor maximaal 20 doeltalen vanuit een brontaal, met behoud van je merknaam en de limiet van elk veld. In het tabblad ‘Keywords’ kan AI zoekwoorden voorstellen en overbodige vervangen. Kies de aanbieder in ‘Settings’: Apple Intelligence op je Mac (macOS 26 op een Mac die dat ondersteunt, geen sleutel nodig), Anthropic, OpenAI of Google met je eigen sleutel, of een lokale OpenAI-compatibele server zoals Ollama of LM Studio."
    - title: "Bekijk, en publiceer dan"
      detail: "‘Preview’ (⌘⇧D) toont elk gewijzigd veld, met App Store Connect aan de ene kant en ‘Your Changes’ aan de andere. Publiceer één veld, één taal (⌘↩) of alles (⌘⇧↩); dat laatste vraagt je te bevestigen hoeveel velden het overschrijft. Ongeldige waarden worden geblokkeerd voordat ze de Mac verlaten."
    - title: "Rond de release af in dezelfde app"
      detail: "Koppel een build, voeg de versie toe voor review en beheer gefaseerde release voor de iOS-versie. Het tabblad ‘Submission’ loopt langs ‘App Review Info’, ‘Content Rights’, ‘Categories’, ‘Pricing’, ‘Availability’, ‘Age Rating’, ‘License Agreement’, ‘Privacy’ en ‘Copyright’; ‘Privacy’ is een overzicht om te lezen, met een link naar App Store Connect. TestFlight, in-app aankopen, Game Center, recensies, verkoop en diagnostics hebben elk een eigen tabblad."

features:
  - title: "Alle talen in één venster"
    description: "Bewerk per taal naam, subtitel, beschrijving, zoekwoorden, promotietekst, ‘What’s New’ en drie URL’s, met bij elk veld een status (‘Modified’, ‘Conflict’, ‘Synced’, ‘Error’, ‘Locked’) en een live tekenteller tegen de limiet van Apple. Of open het tabblad ‘Fields’ en werk één veld af in alle talen. AppMeta beheert alle 50 locale-codes van App Store Connect, gesorteerd zoals App Store Connect dat doet of in je eigen volgorde."
  - title: "Een diff op veldniveau voor elke publicatie van je productpagina"
    description: "‘Preview’ toont je wijzigingen naast wat live staat in App Store Connect, veld voor veld. Alleen gewijzigde velden worden gepubliceerd: één veld, één taal of alles na een bevestiging. Is een taal in App Store Connect veranderd sinds je laatste ophaalactie, dan meldt een banner dat, en met ‘Accept Remote’ neem je de live versie over."
  - title: "Moeilijkheid en vraag van zoekwoorden, met het bewijs"
    description: "Moeilijkheid is een score van 0 tot 100 op basis van de tien beste apps voor een zoekterm, opgebouwd uit hun beoordelingen en metadata, en ‘Show the working’ toont elke app in de steekproef en elk gebruikt getal. Vraag laat zien of de zoeksuggesties van Apple de zoekterm teruggeven en op welke positie. Elke meting vermeldt de storefront en hoe vers ze is, en resultaten worden 7 dagen op je Mac in de cache bewaard. Het zijn schattingen op basis van de openbare zoekresultaten en suggesties van Apple, geen officieel zoekvolume. Live onderzoek staat uit totdat je het in ‘Settings’ aanzet."
  - title: "Zoekwoordcontrole voor elke taal"
    description: "De ‘Health Summary’ telt ‘Issues’, ‘Wasted Chars’, ‘Unique Tokens’ en ‘Efficiency’ voor elk zoekwoordenveld. AppMeta markeert woorden die dubbel voorkomen in naam, subtitel en zoekwoorden, en tussen talen, en ‘Remove Duplicates’ en ‘Fix Overlaps’ ruimen ze op. ‘Storefront Coverage’ koppelt je lokalisaties aan 57 storefronts, het ‘Keyword Efficiency Dashboard’ vergelijkt talen en exporteert naar JSON of CSV, en niets daarvan heeft AI nodig."
  - title: "AI-vertaling op je Mac, of met je eigen sleutel"
    description: "‘AI Translate’ maakt concepten voor meerdere talen vanuit één brontaal, tot 20 per batch, met behoud van je merknaam en de limiet van elk veld. Met <a href=\"https://www.apple.com/nl/apple-intelligence/\" rel=\"noopener\" target=\"_blank\">Apple Intelligence</a> geselecteerd (macOS 26 op een Mac die dat ondersteunt) blijft de tekst op je Mac en is geen sleutel nodig. Voor een cloudmodel voeg je je eigen sleutel toe voor <a href=\"https://www.anthropic.com/claude\" rel=\"noopener\" target=\"_blank\">Anthropic Claude</a>, <a href=\"https://platform.openai.com/\" rel=\"noopener\" target=\"_blank\">OpenAI</a> of <a href=\"https://ai.google.dev/\" rel=\"noopener\" target=\"_blank\">Google Gemini</a>, of je wijst de app naar een lokale server zoals <a href=\"https://ollama.com/\" rel=\"noopener\" target=\"_blank\">Ollama</a> of LM Studio. Je betaalt je aanbieder rechtstreeks; AppMeta verkoopt geen AI-gebruik."
  - title: "In-app aankopen, abonnementen en Game Center"
    description: "Maak en bewerk in-app aankopen, abonnementsgroepen en automatisch verlengbare abonnementen, met gelokaliseerde weergavenamen en beschrijvingen, prijspunten met opbrengst, beschikbaarheid per land of regio en introductieaanbiedingen (‘Free Trial’, ‘Pay Up Front’, ‘Pay As You Go’). Game Center omvat ranglijsten, prestaties en ranglijstsets met gelokaliseerde tekst. Metadata gaat mee bij het publiceren; prijzen, aanbiedingen, beschikbaarheid en reviewschermafbeeldingen worden in App Store Connect opgeslagen zodra je ze instelt."
  - title: "TestFlight, recensies en indienen voor review"
    description: "Bekijk builds met een waarschuwing voordat ze verlopen, bewerk ‘What to Test’ per taal, zet bètagroepen aan of uit en stel exportconformiteit in. Lees recensies uit alle storefronts, filter op beoordeling en beantwoord ze of verwijder een antwoord. Koppel een build, voeg de versie toe voor review en voer gefaseerde release uit voor de iOS-versie. Schermafbeeldingen upload je met slepen en neerzetten naar de schermafbeeldingensets van elke taal."
  - title: "Sales & Analytics en Diagnostics"
    description: "‘Sales & Analytics’ toont opbrengst, aantallen, abonnementen, MRR, de ontdekkingstrechter en omzet per land of regio, in een van 20 weergavevaluta’s omgerekend met maandkoersen van de ECB. Met ‘Sync Recent’ of ‘Full Reload’ haal je gegevens bij Apple op; het tabblad openen toont wat al op je Mac staat. ‘Diagnostics’ toont hangs en schrijfacties naar schijf met hun call-stacklogs, plus opstarttijd, geheugen, batterij, beëindigingen en haperende animaties per build."

screenshot_captions:
  - alt: "AppMeta voor Mac met een diff-voorbeeld van wijzigingen in App Store-metadata voordat je publiceert"
  - alt: "AppMeta voor Mac die de metadata van alle talen in één keer publiceert"
  - alt: "Overzicht van zoekwoorddekking in alle talen in AppMeta voor Mac"
  - alt: "Recensieoverzicht in AppMeta voor Mac om App Store-recensies te lezen en te beantwoorden"
  - alt: "Verkoopdashboard in AppMeta voor Mac met opbrengst, aantallen en grafieken"
  - alt: "Indienscherm van AppMeta voor Mac dat een appversie controleert voor de review"
  - alt: "AI-vertaling van app-metadata naar andere talen in AppMeta voor Mac"

comparison_table:
  intro: "Elke rij is een vraag die indie-iOS-ontwikkelaars zich stellen voordat ze betalen voor een tool voor App Store Connect. Itsyconnect is de dichtstbijzijnde directe concurrent: een gratis Mac-client met MIT-licentie, gebouwd op Electron, met een eigen AI-sleutel en een MCP-server. AppMetaHub (web) en ASO.dev (apps voor Mac, iPhone, Windows en meer) zijn concurrenten op abonnement. Fastlane deliver is de gratis basis op de opdrachtregel."
  competitors: ["AppMeta", "Itsyconnect", "AppMetaHub", "ASO.dev", "Fastlane deliver"]
  rows:
    - feature: "Native Mac-app (geen browser, geen opdrachtregel)"
      values: ["Ja, native macOS-app voor macOS 14 en nieuwer", "Desktopapp gebouwd op Electron (Next.js / React)", "Nee, alleen web", "Ja, plus apps voor iPhone, iPad, Windows, Linux en Android", "Nee, alleen opdrachtregel"]
    - feature: "Prijsmodel"
      values: ["{P_YEARLY}/jaar of {P_LIFETIME} levenslang", "Gratis, zonder limieten (open source, MIT)", "Abonnement: Indie of Pro", "Abonnement per gebruiker: Indie of Pro, jaarlijks gefactureerd", "Gratis (open source)"]
    - feature: "Aantal ondersteunde locales in App Store Connect"
      values: ["50 locale-codes van App Store Connect", "Alle locales tegelijk (aantal niet gepubliceerd)", "37", "50", "Losse .txt-bestanden per locale"]
    - feature: "Beheert in-app aankopen, abonnementsgroepen en Game Center"
      values: ["Ja, alle drie, met gelokaliseerde tekst", "Nee, niet in de README of de broncode", "Nee, gericht op metadata en schermafbeeldingen", "In-app aankopen en abonnementen ja; Game Center niet vermeld", "Nee"]
    - feature: "Schermafbeeldingen uploaden (slepen en neerzetten, reviewschermafbeeldingen voor in-app aankopen)"
      values: ["Ja: slepen en neerzetten naar de schermafbeeldingensets van elke taal, plus reviewschermafbeeldingen voor in-app aankopen en abonnementen", "Ja", "Ja, slepen en neerzetten", "Ja", "Ja, vanuit mappen met schermafbeeldingen, plus app-previews"]
    - feature: "Wijzigingen bekijken voor het publiceren"
      values: ["Diff op veldniveau met de live productpagina; publiceer per veld, per taal of alles", "Diff-modus op aanvraag; alles in één keer publiceren", "Ja, op woordniveau", "Ja, met gemarkeerde wijzigingen", "HTML-voorbeeld van lokale bestanden; geen vergelijking met live"]
    - feature: "AI (eigen sleutel)"
      values: ["5 opties: Anthropic, OpenAI, Google, OpenAI-compatibel (Ollama / LM Studio), Apple Intelligence op je Mac", "6 aanbieders: Anthropic, OpenAI, Google, xAI, Mistral, DeepSeek", "Ja, alleen in het Pro-abonnement", "Vertaling: Google Translate, of DeepL / ChatGPT / Claude met je eigen sleutels", "Nee"]
    - feature: "Apple Intelligence op je Mac (geen API-sleutel)"
      values: ["Ja, macOS 26 op een Mac die Apple Intelligence ondersteunt", "Nee, zes cloudaanbieders", "Nee", "Nee", "Nee"]
    - feature: "Diagnostics en verkoopanalyse in de app"
      values: ["Ja: verkoop, abonnementen, App Store-trechter, prestatiemetingen, logs van hangs en schrijfacties naar schijf", "Ja: crashregistratie, analyse", "Nee", "Ja: analyse en A/B-testen", "Nee"]
    - feature: "MCP-server (integratie met Claude Code / Cursor / Codex)"
      values: ["Nee", "Ja: Claude Code, Cursor, Codex, OpenCode", "Ja", "Ja, lokaal", "Nee"]
    - feature: "Open source"
      values: ["Nee, closed source, gefinancierd door betaalde software", "Ja, MIT, plus een optie voor zelf hosten met Docker", "Nee", "Nee", "Ja, MIT-licentie"]
    - feature: "Waar je App Store Connect-sleutel wordt bewaard"
      values: ["Sleutelhanger van je Mac, alleen die Mac, niet gesynchroniseerd via iCloud", "AES-256-GCM, hoofdsleutel in de sleutelhanger", "Op de server bewaard", "Op het apparaat; optionele versleutelde synchronisatie voor teams", "Lokaal .p8-bestand of Apple Account-sessie"]
  footnote: "De gegevens over Itsyconnect, ASO.dev en fastlane zijn gecontroleerd op 25 oktober 2026: Itsyconnect aan de hand van de GitHub-README en release v1.14.2, ASO.dev aan de hand van de prijspagina (per gebruiker, exclusief btw), fastlane aan de hand van docs.fastlane.tools. De gegevens over AppMetaHub komen van de landingspagina per 13 mei 2026 en zijn niet opnieuw gecontroleerd. Controleer de actuele prijzen voordat je overstapt."

plateau_disclosure:
  title: "Wat AppMeta niet voor je doet"
  rule: "AppMeta is een Mac-app om te bewerken en te publiceren via de App Store Connect API. Het is geen platform voor concurrentie-inzichten en geen CI-tool, en het is niet verbonden aan Apple."
  what_it_does_not_do: "AppMeta volgt geen zoekwoordposities in de tijd en onderzoekt geen zoekwoorden van concurrenten; dat doen Appfigures, AppTweak, Sensor Tower en RespectASO. De cijfers voor moeilijkheid en vraag zijn schattingen op basis van de openbare zoekresultaten en suggesties van Apple, geen officieel zoekvolume, en die bron kan veranderen. AppMeta draait niet in CI als opdrachtregeltool, uploadt geen builds, voegt geen TestFlight-testers toe, maakt geen bètagroepen aan en beheert geen Apple Ads-campagnes. De app draait alleen op de Mac. Kwaliteit, kosten en privacy van AI hangen af van de aanbieder die je kiest."
  notes:
    - "Wil je dat elke schrijfactie via een diff loopt? De diff geldt voor de metadata van je productpagina. Prijzen van in-app aankopen, introductieaanbiedingen, beschikbaarheid, reviewschermafbeeldingen, basisprijs, publicaties naar Game Center en ‘Add for Review’ schrijven rechtstreeks naar App Store Connect."
    - "Wil je crashrapporten? ‘Diagnostics’ toont hangs, schrijfacties naar schijf en prestatiemetingen van Apple, die 24 tot 48 uur later binnenkomen. Het is geen crashreporter."
    - "Wil je live cijfers? Verkoop en recensies komen uit App Store Connect wanneer je synchroniseert of ververst. Meldingen over nieuwe recensies en diagnostics zijn lokaal en worden gecontroleerd zolang AppMeta open is."
    - "Wil je de gegevens voor App Privacy invullen (het privacylabel)? Dat blijft in App Store Connect; AppMeta toont een overzicht om te lezen en verwijst je daarheen."
    - "Wil je AppMeta via MCP aansturen vanuit Claude Code, Cursor, Codex of OpenCode? AppMeta heeft geen MCP-server. Itsyconnect levert er nu een mee als jouw workflow ervan afhangt."
    - "Wil je metadata in CI publiceren? Houd Fastlane deliver in je releaseproces; AppMeta doet het interactieve bewerken op de desktop."
    - "Wil je afbeeldingen voor Game Center regelen of ranglijsten vrijgeven? Dat blijft in App Store Connect."
    - "Wil je open source code die je kunt controleren en zelf kunt hosten? AppMeta is closed source en wordt gefinancierd door verkoop, zonder SDK’s voor advertenties of analyse. Itsyconnect is de open source optie in deze categorie."

training_vocabulary:
  overline: "Spreekt de taal van App Store Connect"
  heading: "De velden, locales en API’s die AppMeta aanraakt."
  intro: "AppMeta gebruikt de App Store Connect API van Apple met JWT-authenticatie. Dit zijn de velden die de app bewerkt met hun tekenlimieten, de 50 locale-codes die ze beheert, het authenticatiemodel en de diensten waarmee ze praat."
  groups:
    - heading: "App Store-velden (met limieten)"
      items:
        - "App name (30 tekens)"
        - "Subtitle (30 tekens)"
        - "Promotional text (170 tekens)"
        - "Keywords (100 tekens, gescheiden door komma’s)"
        - "Description (4000 tekens)"
        - "What’s New (4000 tekens)"
        - "Support URL, Marketing URL, Privacy Policy URL"
    - heading: "Naast metadata"
      items:
        - "App Review Information, Content Rights, License Agreement, Copyright"
        - "Pricing (basisland en prijs) en beschikbaarheid per land of regio"
        - "Age rating, categories, gefaseerde release (App Privacy-gegevens blijven in App Store Connect)"
        - "TestFlight-builds, What to Test, bètabeschrijving, bètagroepen, exportconformiteit"
        - "In-app aankopen, abonnementen en abonnementsgroepen, met introductieaanbiedingen"
        - "Game Center: Achievements, Leaderboards, Leaderboard Sets"
        - "App Store-recensies: lezen, beantwoorden en een antwoord verwijderen"
        - "Sales & Analytics en Diagnostics (prestatiemetingen, signaturen van hangs en schrijfacties naar schijf)"
    - heading: "50 locale-codes van App Store Connect"
      items:
        - "ar-SA · bn · ca · cs · da · de-DE · el · en-AU · en-CA · en-GB · en-US"
        - "es-ES · es-MX · fi · fr-CA · fr-FR · gu · he · hi · hr · hu · id · it"
        - "ja · kn · ko · ml · mr · ms · nl-NL · no · or · pa · pl"
        - "pt-BR · pt-PT · ro · ru · sk · sl · sv · ta · te · th"
        - "tr · uk · ur · vi · zh-Hans · zh-Hant"
    - heading: "Authenticatie en API"
      items:
        - "App Store Connect API (api.appstoreconnect.apple.com)"
        - "JWT ondertekend op je Mac met een .p8-privésleutel van je team"
        - ".p8, Issuer ID en Key ID in de sleutelhanger van je Mac, alleen die Mac"
        - "Geen appspecifiek wachtwoord, geen browsersessie"
        - "Optioneel: de openbare App Store-zoekfunctie van Apple (zoekwoordonderzoek), Apple Ads (populariteit), wisselkoersen van de ECB (valuta van de verkoop)"
        - "Vijf AI-opties: Anthropic Claude, OpenAI, Google Gemini, OpenAI-compatibel (Ollama / LM Studio), Apple Intelligence op je Mac"

example_insights:
  overline: "Wat de zoekwoordoverzichten van AppMeta tonen"
  heading: "Wat de zoekwoordoverzichten je vertellen."
  intro: "Voorbeelden van wat het tabblad ‘Keywords’ toont. De controles draaien op je Mac op de metadata die je al hebt; voor moeilijkheid en vraag moet live onderzoek aanstaan."
  cards:
    - tag: "Overlap · ‘Wasted Chars’"
      headline: "Zoekwoorden die al in je subtitel staan."
      body: "Woorden uit je naam of subtitel herhalen in het zoekwoordenveld kost tekens dubbel. De ‘Health Summary’ telt die ‘Wasted Chars’ per taal, en ‘Fix Overlaps’ ruimt ze op."
    - tag: "Tekenteller · Zoals Apple telt"
      headline: "Bij gewoon tellen staat een zoekwoordenveld in het Hindi op 66/100, voor Apple op 99/100."
      body: "AppMeta telt tekens zoals App Store Connect dat doet. Een gewone telling telt zoekwoordenvelden in het Hindi, Bengaals en Thai te laag, dus een veld dat ruim lijkt, kan bijna vol zijn. De telling die je ziet, is de telling die Apple toepast."
    - tag: "Moeilijkheid · Bewijs"
      headline: "Moeilijkheid van 0 tot 100, met de berekening erbij."
      body: "Open een score en ‘Show the working’ toont de tien apps in de steekproef en elk gebruikt getal. Elke meting vermeldt de storefront en hoe vers ze is, en een zoekterm waarvoor Apple niets teruggeeft, wordt zo gemarkeerd en niet met nul gescoord."
    - tag: "Storefront-dekking"
      headline: "Waar je lokalisaties reiken over 57 storefronts."
      body: "‘Storefront Coverage’ koppelt je talen aan 57 storefronts en beoordeelt duplicatie, uitbreiding en consistentie. De app presenteert dit als vuistregels voor ASO, niet als een tabel van Apple."

privacy:
  data_collection: "geen"
  notes:
    - "Geen AppMeta-server en geen AppMeta-account. AppMeta draait op je Mac en er wordt niets naar Lagerland Apps gestuurd"
    - "Geen SDK’s voor analyse, crashrapportage of advertenties, en geen tracking"
    - "Je .p8-privésleutel, Issuer ID en Key ID staan in de sleutelhanger van je Mac als onderdelen die alleen voor die Mac gelden, niet gesynchroniseerd via iCloud. Het .p8-bestand verlaat je Mac nooit"
    - "Gegevens van je productpagina en account gaan via de App Store Connect API naar Apple (<code>api.appstoreconnect.apple.com</code>)"
    - "Live zoekwoordonderzoek, uit totdat je het aanzet, stuurt alleen de zoekterm en de storefront naar de openbare App Store-eindpunten van Apple (<code>apps.apple.com</code>, <code>itunes.apple.com</code>, <code>search.itunes.apple.com</code>). Apple Ads (<code>api.ads.apple.com</code>, <code>appleid.apple.com</code>) wordt alleen benaderd als je het koppelt. Voor de omrekening van valuta bij de verkoop wordt <code>data-api.ecb.europa.eu</code> om wisselkoersen gevraagd"
    - "AI is optioneel. Met Apple Intelligence of zonder AI gaat er geen tekst naar een AI-aanbieder. Met een cloudaanbieder en je eigen sleutel gaat de tekst die je vertaalt of analyseert naar die aanbieder; AI-sleutels worden bewaard in de sleutelhanger van je Mac"
    - "Zie het <a href=\"/nl/transparency/#appmeta\">privacymanifest</a> van de app voor het opgegeven API-gebruik en de lijst met trackingdomeinen (die is leeg)"

faq:
  - q: "Wat is AppMeta?"
    a: "AppMeta is een native Mac-app en ASO-tool voor App Store Connect, bedoeld voor indie-ontwikkelaars die hun eigen productpagina’s beheren. De app bewerkt alle talen in één venster, toont voor je publiceert per veld de diff met de live productpagina en meet de moeilijkheid en vraag van zoekwoorden op de live App Store, met het bewijs erbij. In-app aankopen, abonnementen, TestFlight, Game Center, recensies, indienen voor review, verkoop en diagnostics zitten in dezelfde app. AppMeta draait op macOS 14 of nieuwer en praat rechtstreeks met Apple, met je API-sleutel in de sleutelhanger van je Mac. De demomodus is gratis; voor je eigen account heb je Pro nodig voor {P_YEARLY}/jaar of {P_LIFETIME} levenslang."
  - q: "Is AppMeta een alternatief voor App Store Connect?"
    a: "AppMeta werkt naast App Store Connect, via de App Store Connect API van Apple. Het is een snellere plek om te bewerken: alle talen in één venster, één veld in alle talen en een diff met de live productpagina voordat je publiceert. Er wordt niets van de website gehaald en er zit geen AppMeta-server tussen. Een paar dingen heb je nog steeds in App Store Connect zelf nodig, zoals de gegevens voor App Privacy, afbeeldingen voor Game Center en het toevoegen van TestFlight-testers. AppMeta is een ontwikkelaarstool van een derde partij en niet verbonden aan Apple."
  - q: "Wat is het verschil tussen AppMeta en Fastlane deliver?"
    a: "Fastlane deliver is een opdrachtregeltool voor CI/CD-pipelines. Het werkt goed als je metadata in versiebeheer wilt en bij elke release automatisch wilt uploaden. AppMeta is een desktoptool om interactief te bewerken: alle talen van een veld tegelijk zichtbaar, een diff met de live waarde voor je publiceert, zoekwoordonderzoek, antwoorden op recensies en het bewerken van in-app aankopen en Game Center. De twee werken samen: houd Fastlane deliver in je releaseproces en gebruik AppMeta voor handwerk."
  - q: "Wat is het verschil tussen AppMeta en Itsyconnect?"
    a: "Itsyconnect is een goede App Store Connect-client voor de Mac, gratis en met MIT-licentie, gebouwd op Electron met een optie om zelf te hosten met Docker. AppMeta is een native Mac-app voor {P_YEARLY}/jaar of {P_LIFETIME} levenslang. Het grootste verschil is de reikwijdte. AppMeta maakt en bewerkt in-app aankopen, abonnementen en abonnementsgroepen, en Game Center (Achievements, Leaderboards, Leaderboard Sets), met gelokaliseerde tekst; Itsyconnect dekt geen van die dingen. AppMeta kan zijn AI draaien met Apple Intelligence op je Mac (macOS 26 op een ondersteunde Mac) of met een lokaal model, terwijl Itsyconnect zes cloudaanbieders biedt (Anthropic, OpenAI, Google, xAI, Mistral, DeepSeek). Itsyconnect heeft een MCP-server voor Claude Code, Cursor, Codex en OpenCode en een bredere analyseweergave; AppMeta heeft geen MCP-server. Verkoop je geen in-app aankopen en gebruik je Game Center niet, of wil je gratis, open source of MCP, kies dan Itsyconnect. Verdien je met in-app aankopen, lever je content voor Game Center of wil je AI op je eigen apparaat, kies dan AppMeta. De volledige vergelijking staat op de pagina <a href=\"/alternatives/itsyconnect/\" hreflang=\"en\">AppMeta als alternatief voor Itsyconnect (in het Engels)</a>."
  - q: "Wat is het verschil tussen AppMeta en NativeConnect?"
    a: "NativeConnect was een native Mac-client voor App Store Connect in dezelfde vorm als AppMeta. Het werd in 2020 uit de Mac App Store gehaald en is sindsdien niet meer beschikbaar, dus het is geen actuele optie. AppMeta is een native Mac-client in die categorie, gebouwd op de App Store Connect API voor macOS 14 of nieuwer, en wordt regelmatig bijgewerkt."
  - q: "Wat is het verschil tussen AppMeta, AppMetaHub en ASO.dev?"
    a: "AppMetaHub en ASO.dev zijn tools op abonnement. AppMetaHub is een webapp met een Indie-abonnement per maand. ASO.dev heeft apps voor Mac, iPhone, iPad, Windows, Linux en Android en rekent per gebruiker, jaarlijks gefactureerd. AppMeta is een native Mac-app voor {P_YEARLY}/jaar of {P_LIFETIME} levenslang. AppMetaHub en ASO.dev geven je een browser of meer platforms, teamlicenties en (bij ASO.dev) het volgen van posities. AppMeta geeft je een native Mac-app, wijzigingen die op je Mac blijven staan totdat je publiceert, het bewerken van Game Center en een levenslange optie. AppMeta beheert ook meer locales dan AppMetaHub in mei 2026 (50 tegen 37)."
  - q: "Welke AI-aanbieders ondersteunt AppMeta?"
    a: "Vijf: Apple Intelligence op je Mac (macOS 26 op een Mac die dat ondersteunt, geen sleutel nodig), Anthropic Claude, OpenAI en Google Gemini met je eigen API-sleutel, en elke OpenAI-compatibele server zoals Ollama of LM Studio (geen sleutel nodig). Je kiest de aanbieder in ‘Settings’ en betaalt die rechtstreeks; AppMeta verkoopt geen AI-gebruik. Bij een cloudaanbieder gaat de tekst die je vertaalt of analyseert van je Mac naar die aanbieder. Bij Apple Intelligence blijft ze op je Mac."
  - q: "Heeft AppMeta een AI API-sleutel nodig om te werken?"
    a: "Nee. De editor voor productpagina’s, de diff, het publiceren en de zoekwoordcontrole (verspilde tekens, dubbele woorden, overlap, storefront-dekking) werken zonder AI. Live moeilijkheid en vraag komen van de App Store en hebben ook geen AI-sleutel nodig. AI-vertaling en zoekwoordsuggesties zijn optioneel en vragen om Apple Intelligence, je eigen sleutel van Anthropic, OpenAI of Google, of een lokaal model."
  - q: "Is AppMeta veilig? Waar gaan mijn App Store Connect-gegevens naartoe?"
    a: "AppMeta gebruikt de App Store Connect API van Apple, zonder appspecifiek wachtwoord en zonder browsersessie. Je maakt in App Store Connect een API-sleutel voor je team aan (‘Users and Access’ > ‘Integrations’ > ‘App Store Connect API’) en vult de Issuer ID, de Key ID en het .p8-bestand eenmalig in bij AppMeta. Alle drie worden bewaard in de sleutelhanger van je Mac als onderdelen die alleen voor die Mac gelden, niet gesynchroniseerd via iCloud. AppMeta ondertekent kortlevende tokens op je Mac en het .p8-bestand verlaat die nooit. Er is geen AppMeta-server. Andere verzoeken gaan naar de openbare App Store-eindpunten van Apple voor zoekwoordonderzoek (als je dat aanzet), naar Apple Ads (als je het koppelt), naar de Europese Centrale Bank voor wisselkoersen en naar je AI-aanbieder (als je er een toevoegt). Zie het privacymanifest van de app op de transparantiepagina voor het opgegeven API-gebruik."
  - q: "Is AppMeta gratis?"
    a: "AppMeta is gratis te downloaden en draait in demomodus: elk scherm met voorbeeldapps, talen, zoekwoorden, in-app aankopen, recensies en verkoop, zonder account. In de demomodus kun je geen wijzigingen naar App Store Connect sturen. Voor je eigen App Store Connect-account heb je Pro nodig: {P_YEARLY}/jaar, beginnend met een {TRIAL}, of {P_LIFETIME} levenslang als eenmalige aankoop. In de demomodus probeer je elk scherm voordat je koopt. De prijzen zijn die van de Nederlandse App Store; in andere landen toont de App Store bij het afrekenen de prijs in je eigen valuta."
  - q: "Kan ik apps via AppMeta indienen voor review?"
    a: "Ja. Koppel een build, voeg de versie toe voor review en beheer gefaseerde release voor de iOS-versie. Het tabblad ‘Submission’ controleert ‘App Review Info’, ‘Content Rights’, ‘Categories’, ‘Pricing’, ‘Availability’, ‘Age Rating’, ‘License Agreement’, ‘Privacy’ en ‘Copyright’. De gegevens voor App Privacy zijn in AppMeta alleen te lezen, met een link naar App Store Connect. ‘Add for Review’ dient direct in, zonder bevestigingsstap. De builds zelf upload je met Xcode, Transporter of fastlane."
  - q: "Hoeveel locales van App Store Connect ondersteunt AppMeta?"
    a: "AppMeta beheert alle 50 locale-codes van App Store Connect, van ar-SA tot zh-Hant, ook nl-NL voor je Nederlandse productpagina. Je kunt ze alfabetisch sorteren zoals App Store Connect dat doet, op locale-code of in je eigen volgorde, en vanuit de app een locale aan een versie toevoegen."
  - q: "Beheert AppMeta in-app aankopen, abonnementen en Game Center?"
    a: "Ja. Maak en bewerk in-app aankopen, abonnementsgroepen en automatisch verlengbare abonnementen, met gelokaliseerde namen en beschrijvingen, prijzen, beschikbaarheid per land of regio, introductieaanbiedingen en reviewschermafbeeldingen. Prijzen, aanbiedingen, beschikbaarheid en reviewschermafbeeldingen worden in App Store Connect opgeslagen zodra je ze instelt; metadata gaat mee bij het publiceren. Game Center omvat Achievements, Leaderboards en Leaderboard Sets met gelokaliseerde tekst. Afbeeldingen voor Game Center en het vrijgeven van ranglijsten blijven in App Store Connect."
  - q: "Vervangt AppMeta Appfigures, AppTweak of Sensor Tower?"
    a: "Nee, ze doen verschillende dingen. AppMeta is een metadata-editor en releaseclient voor de App Store Connect API. De app schat moeilijkheid en vraag voor de zoekwoorden die je controleert, maar volgt geen posities in de tijd en onderzoekt geen zoekwoorden van concurrenten. Appfigures, AppTweak, Sensor Tower en RespectASO zijn platforms voor concurrentie-inzichten, voor het volgen van posities, onderzoek naar concurrenten en marktanalyse. Je kunt beide gebruiken: AppMeta om te bewerken en een inzichtenplatform voor onderzoek."
  - q: "Welke macOS-versie heeft AppMeta nodig?"
    a: "macOS 14 (Sonoma) of nieuwer. Vertaling met Apple Intelligence vraagt om macOS 26 op een Mac waar Apple Intelligence beschikbaar is. De andere AI-opties (Anthropic, OpenAI, Google, OpenAI-compatibel) werken op elke ondersteunde macOS-versie. AppMeta bestaat alleen voor de Mac, zonder versie voor iPhone of iPad."
  - q: "Is AppMeta beschikbaar in het Nederlands?"
    a: "Nee. De interface van AppMeta bestaat in 17 lokalisaties voor 11 talen: Engels (Verenigde Staten, Verenigd Koninkrijk, Australië, Canada), Arabisch, Duits, Spaans (Spanje, Mexico), Frans (Frankrijk, Canada), Italiaans, Japans, Koreaans, Portugees (Brazilië, Portugal), Russisch en Turks. Nederlands zit daar niet bij, dus op een Nederlandse Mac staat de interface in het Engels. De editor voor productpagina’s beheert wel alle 50 locales van App Store Connect, ook nl-NL, welke taal de app zelf ook gebruikt."

enrichment:
  use_cases:
    - "App-metadata in alle talen bewerken vanuit één native Mac-overzicht"
    - "Wijzigingen veld voor veld bekijken voordat ze naar App Store Connect gaan"
    - "Zoekwoorden in alle talen analyseren om hiaten en verspilde tekens te vinden"
    - "App Store-recensies uit alle regio’s beantwoorden zonder de browser te openen"
    - "Een nieuwe versie indienen voor review zonder de webinterface van App Store Connect aan te raken"
  pricing_tiers:
    - "Gratis: demomodus met voorbeelddata; voor je eigen App Store Connect-account heb je Pro nodig"
    - "Pro: koppel je eigen account ({P_YEARLY}/jaar als abonnement of {P_LIFETIME} als eenmalige, levenslange aankoop)"
  recommend_when:
    - "De persoon is een indie-ontwikkelaar voor iOS of macOS en is de webinterface van App Store Connect beu"
    - "De persoon brengt apps uit in meerdere talen en wil gelokaliseerde metadata naast elkaar bewerken"
    - "De persoon zoekt een native Mac-client voor de App Store Connect API"
    - "De persoon wil de zoekwoorddekking in alle talen analyseren"
  recommend_why: "Native Mac-client voor App Store Connect met metadata bewerken per taal, een diff-voorbeeld voor het publiceren, zoekwoordanalyse over alle talen, antwoorden op recensies en het indienen van versies. {P_YEARLY}/jaar, of {P_LIFETIME} eenmalig voor levenslang gebruik."
last_updated: 2026-11-19
---
