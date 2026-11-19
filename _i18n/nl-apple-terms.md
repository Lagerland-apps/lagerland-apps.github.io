# Apple's Dutch (Netherlands) terms

Part of the Dutch language sheet. Checked 2026-11-19 against Apple's live Netherlands pages, fetched with curl (`Accept-Language: nl-NL`, Safari User-Agent) and read as raw HTML. Sources used: `support.apple.com/nl-nl/...` (page footer "Nederland", title suffix "Apple Support (NL)", `<html lang="nl">`), `www.apple.com/nl/...` (title suffix "Apple (NL)", `lang="nl-NL"`) and `apps.apple.com/nl/...` (`lang="nl"`). No Flemish (`nl-be`, `/be-nl/`) page is a source for any row. Use these names exactly; never invent an Apple name. Rows marked "not verified" have no Apple Netherlands page that names them.

The user guides on support.apple.com/nl-nl are the iOS 27, watchOS 27 and macOS 27 editions (version selector "iOS 27 ... iOS 12", "macOS 27 Golden Gate"). 97 guide pages, 15 support articles and 8 apple.com/nl pages were fetched and counted.

Five things to know before reading the rows:

1. **Apple Netherlands writes "je / jij / jouw", never "u".** Across 61 iPhone-guide pages, 24 Apple Watch pages, 5 Mac pages, 15 support articles and 8 marketing pages: 5139 "je", 32 "jij", 28 "jouw", 64 "jou", 9 "jezelf", 2 "jullie", 0 "gij", and 3 "u". Those 3 "u" are one string in the page chrome ("Als u deze regelaar wijzigt, wordt deze pagina automatisch bijgewerkt", the version selector) plus the feedback box at the foot of every page ("Neem geen persoonlijke informatie op in uw opmerking", "Hartelijk dank voor uw feedback"). The body text of every page is "je". This decides the formality: informal "je" (TRANSLATION.md 13 default confirmed). See "Register" below.
2. **Settings and UI wording is Dutch, not Flemish.** "Instellingen" (iPhone), "Systeeminstellingen" (Mac), "inloggen" (36 hits; "aanmelden" only 3), "Schermtijd", "beginscherm", "toegangsscherm", "bedieningspaneel", "Delen met gezin", "Opdrachten", "Zoek mijn".
3. **Apple writes the account as "Apple Account"** (35 hits; 0 "Apple ID", 0 "Apple-account"), capital A on both words, with the English name kept, and compounds it with a hyphen: "Apple Account-wachtwoord", "Apple Account-knop", "Apple Account-saldo".
4. **Apps get a hyphenated compound**: "de Gezondheid-app", "de Instellingen-app", "de Conditie-app", "de Work-out-app", "de Slaap-app", "de Camera-app", "de Bestanden-app", "de Opdrachten-app", "de Weer-app", "de App Store-app". The Apple Watch guide also has the open form "de app Vitale functies" (iPhone guide 11 hits). Both are Apple's.
5. **Gender: "de app" (86 hits, 0 "het app"), "de App Store" (50, 0 "het"), "de iPhone" (311), "de Apple Watch" (13, 0 "het"), "de Mac" (34), "de iPad" (8), "het Dynamic Island" (5, 0 "de"), "het bedieningspaneel", "het beginscherm", "het toegangsscherm", "de widget" (28), "de slimme stapel".** "het iPhone" (4 hits) is not a gender error: it is "het iPhone-scherm" (the screen is neuter).

Abbreviations: ig = iPhone user guide https://support.apple.com/nl-nl/guide/iphone/welcome/ios (table of contents), wg = Apple Watch user guide https://support.apple.com/nl-nl/guide/watch/welcome/watchos, mg = Mac user guide https://support.apple.com/nl-nl/guide/mac-help/welcome/mac, am = apple.com/nl marketing pages (https://www.apple.com/nl/iphone/, /nl/app-store/, /nl/icloud/, /nl/apple-fitness-plus/, /nl/apple-intelligence/, /nl/apple-pay/, /nl/privacy/), ap = apps.apple.com/nl. Article URLs are https://support.apple.com/nl-nl/NNNNNN. Guide pages are https://support.apple.com/nl-nl/guide/iphone/<id>/ios (or /watch/<id>/watchos). **There is no `www.apple.com/nl/health/` page (HTTP 404) and no `www.apple.com/nl/family-sharing/` page (404).** `developer.apple.com/nl/...` (Xcode, TestFlight, App Store Connect, marketing guidelines) and the Dutch App Store Connect / TestFlight user guides all return 404: those products are not localised on Apple's Dutch pages.

How Apple writes them in running text:
- **App names**: capitalised name + hyphen + "app" ("de Gezondheid-app", "de Wallet-app", "de Foto’s-app"), no italics, no quotes. The three-word guide titles use "in Gezondheid" without "app" ("Je slaapgeschiedenis bekijken in Gezondheid op de iPhone"). Common names without "app": Siri, Spotlight, iCloud, Wallet, Safari.
- **Features and setting labels** go in **straight single quotes** in the guides: 'Schermtijd', 'Privacy en beveiliging' > 'Tracking', 'Delen met gezin', 'Voeg schema toe'. The articles mix straight ' (820) and curly ‘ ’ (82 and 119). Double quotes are used for spoken text only ("Hé, Siri"). See "Typography".
- **Menu paths** use ">" with a NO-BREAK SPACE before it and a plain space after ("Tik in Instellingen op 'Privacy en beveiliging' > 'Tracking'"; 54 NBSP-before-">" on the guide pages). The Mac pages use the plain verb chain ("Ga naar Systeeminstellingen op de Mac. Klik op een optie in de navigatiekolom").
- **Capitalisation**: sentence style. Feature nouns are lowercase in running text: "een focus", "de slaapfocus", "het bedieningspaneel", "de slimme stapel", "live activiteiten", "de donkere modus", "het universele klembord". "Apple Account" and "Apple Intelligence" stay capitalised. "Schermtijd" is capitalised as the feature/app name ("Schermtijd voor jezelf instellen") but "tijdslimieten" and "schema's" are lowercase.
- Other Apple spellings: "wifi" lowercase (25 hits, 0 "Wi-Fi"); "e‑mail" with a non-breaking hyphen (84); "work‑out"/"work-out" (129 hits, 0 "workout"); "in-app aankopen" (in-app lowercase, two words); "Apple apparaat" open compound (26 vs 2 "Apple-apparaat"); "back‑up"; "gezinshoofd"; "ontvangstbewijs"; "koptelefoon" (not "hoofdtelefoon"); "ov-kaarten"; "ontwikkelaar"; "wachtwoord"; "scherm"; "tikken" (1136 "tik") on iPhone vs "klikken" (143) on Mac.
- Apple's inclusive wording: "gezinsleden", "vriend(in)" with the bracket "(in)" (ig), "gezinshoofd", "ouderlijk toezicht".

## Health and fitness

| English | Dutch (Netherlands) as Apple writes it | Source | Note |
|---|---|---|---|
| Health (app) | **Gezondheid**; "de Gezondheid-app"; guide titles "in Gezondheid" | https://support.apple.com/nl-nl/guide/iphone/iphcae7451f3/ios ; https://www.apple.com/nl/privacy/ ("In de Gezondheid-app hou je zelf de controle") | Translated, never "Health". Tabs: 'Overzicht' (Summary), 'Gegevens' (Data in iOS 27: "Tik op 'Gegevens', tik op 'Slaap'"), 'Delen' |
| Apple Health | not verified | Apple's guides and marketing say only "Gezondheid" / "de Gezondheid-app"; no Apple page says "Apple Health" | Developers' nl store text writes "Apple Health" (the Observa nl listing) and "Apple Gezondheid-gegevens"; Apple does not. Use "de Gezondheid-app" / "Gezondheid" |
| Health data | gezondheidsgegevens; "Introductie tot gezondheidsgegevens op de iPhone" | https://support.apple.com/nl-nl/guide/iphone/iphbb8259c61/ios | |
| Health details | 'Gezondheidsdetails' (tab > photo > 'Gezondheidsgegevens' in the same page) | https://support.apple.com/nl-nl/guide/iphone/iphcae7451f3/ios | Apple uses both labels on one page |
| Health records | medische dossiers ("Medische dossiers downloaden op de iPhone") | https://support.apple.com/nl-nl/guide/iphone/iphc30019594/ios | |
| Medical ID | **medische ID** ("Je medische ID instellen en bekijken op de Apple Watch") | https://support.apple.com/nl-nl/guide/watch/apd58cd0b3f4/watchos | |
| Sleep (feature, Health) | **Slaap**; "de Slaap-app" (Apple Watch); Gezondheid > 'Gegevens' > 'Slaap' | https://support.apple.com/nl-nl/guide/iphone/iph72b370881/ios ; https://support.apple.com/nl-nl/108906 | Schedule: "slaapschema"; "bedtijd"; "wekker voor opstaan" |
| Sleep Focus | **slaapfocus** (one word, lowercase; focus name 'Slaap'): "De slaapfocus in- of uitschakelen op de iPhone"; Control Center path 'Focus' > 'Slaap' | https://support.apple.com/nl-nl/guide/iphone/iph7cdb86325/ios ; https://support.apple.com/nl-nl/108906 | Not "slaapmodus" |
| Focus (feature) | **focus** (common noun, "een focus", "Een focus instellen op de iPhone"); control 'Focus'; presets 'Niet storen', 'Werk', 'Persoonlijk', 'Slaap' | https://support.apple.com/nl-nl/guide/iphone/iphd6288a67f/ios ; https://support.apple.com/nl-nl/guide/iphone/iph5c3f5b77b/ios | Do Not Disturb = 'Niet storen' |
| Sleep Score | **slaapscore** ("Je slaapscore bekijken op de Apple Watch"); scale: Erg laag 0-40, Laag 41-60, OK 61-80, Hoog 81-95, Zeer hoog 96+ | https://support.apple.com/nl-nl/guide/watch/apded441a669/watchos | Lowercase one word; middle band is "OK" |
| Sleep stages Awake / REM / Core / Deep | **'Wakker', 'Remslaap', 'Kernslaap' en 'Diepe slaap'** (article, quoted, capitalised); Watch guide lowercase: "remslaap, kernslaap en diepe slaap"; "slaapfases" | https://support.apple.com/nl-nl/108906 ; https://support.apple.com/nl-nl/guide/watch/crpxel1lvun9/watchos | REM is "Remslaap" (one word, lowercase "rem"). Core = "Kernslaap" |
| Heart Rate Variability (HRV) | **hartritmevariabiliteit (HRV)** ("hartritmevariabiliteit (HRV) bij herstel", Digital Crown label 'Hartritmevariabiliteit') | https://support.apple.com/nl-nl/guide/watch/apda88aefe4c/watchos ; https://support.apple.com/nl-nl/guide/watch/flx4gnzby346/watchos | Apple keeps the English abbreviation "HRV". Not "hartslagvariabiliteit" (that is the developer's, Observa). Series 12 / Ultra 4 only |
| Resting heart rate | **hartslag in rust** ("je hartslag in rust"); Watch labels 'Bereik', 'In rust' | https://support.apple.com/nl-nl/guide/iphone/iphe3d379c32/ios ; https://support.apple.com/nl-nl/guide/watch/apda88aefe4c/watchos | Apple does not write "rusthartslag" |
| Heart rate | **hartslag**; "Je hartslag bekijken op je Apple Watch" | https://support.apple.com/nl-nl/guide/watch/apda88aefe4c/watchos | |
| Respiratory rate | **ademfrequentie** | https://support.apple.com/nl-nl/guide/watch/apd15aa7ed96/watchos | |
| Heart rate zones | **hartslagzones** ("Hartslagzones op de Apple Watch weergeven") | https://support.apple.com/nl-nl/guide/watch/apd897dccddf/watchos | |
| ECG app | **de Ecg-app** ("Een elektrocardiogram vastleggen met de Ecg-app") | https://support.apple.com/nl-nl/guide/watch/apdea4c50a57/watchos | "Ecg" with lowercase cg |
| Vitals app | **de app Vitale functies**; "nachtmetingen" | https://support.apple.com/nl-nl/guide/watch/apd15aa7ed96/watchos ; https://support.apple.com/nl-nl/guide/iphone/iphbb8259c61/ios | Open form "app Vitale functies", not "Vitale functies-app" |
| Readiness app (watchOS 27) | **de Gereedheid-app**; "gereedheidsscore" (0 tot en met 10) | https://support.apple.com/nl-nl/guide/watch/flx4gnzby346/watchos | Series 12 and Ultra 4 only. Observa's own nl store text uses "Gereedheid" the same way |
| Training Load | **trainingsbelasting** ("Je trainingsbelasting bijhouden op de Apple Watch") | https://support.apple.com/nl-nl/guide/watch/apde4c07a6cf/watchos | |
| Cardio Fitness | **cardioconditie** / "Cardiofitness of cardioconditie"; title "Je cardioconditieniveaus bijhouden"; "cardioconditieniveau" | https://support.apple.com/nl-nl/108790 | Apple's own title uses "cardioconditie" |
| VO2 max | **VO 2 max** (the 2 is a subscript in the HTML, written "VO 2 max" in text; "VO 2 max-bereik van 14-65 mL/kg/min") | https://support.apple.com/nl-nl/108790 | A developer writes "VO₂ max" (Observa nl store text); both read the same |
| Cycle Tracking | **Cyclus bijhouden** (feature label, quoted 'Cyclus bijhouden'); "Je menstruatiecyclus bijhouden"; "Cyclus bijhouden gebruiken op je Apple Watch" | https://support.apple.com/nl-nl/guide/watch/apd26429adf0/watchos ; https://support.apple.com/nl-nl/guide/iphone/iph51a822b18/ios | |
| Mindfulness app | **de Mindfulness-app**; sessions 'Reflectie' and ademsessie; "reflectie- of ademsessie" | https://support.apple.com/nl-nl/guide/watch/apd371dfe3d7/watchos | English name kept |
| State of Mind | **gemoedstoestand** ("Je gemoedstoestand vastleggen in Gezondheid op de iPhone"; "Je geestelijk welzijn bijhouden") | https://support.apple.com/nl-nl/guide/iphone/iph6a6decb13/ios | |
| Medications | **medicijnen** ("Je medicijnen bijhouden in Gezondheid op de iPhone"; button 'Medicijnen', 'Voeg een medicijn toe') | https://support.apple.com/nl-nl/guide/iphone/iph811670c81/ios | iPhone text says "medicatie" once (pinned category example) |
| Walking Steadiness | **wandelstabiliteit** ("Je wandelstabiliteit in de gaten houden") | https://support.apple.com/nl-nl/guide/iphone/iphff1bf03ed/ios | |
| Activity rings | **activiteitsringen** ("De doelen van je activiteitsringen aanpassen") | https://support.apple.com/nl-nl/guide/iphone/ipha5dddb411/ios ; ig | Apple writes "activiteitsringen" (not "activiteitenringen") |
| Move / Exercise / Stand rings | de rode **bewegingsring** / de groene **trainingsring** / de blauwe **staanring** (wheelchair: **rolring**) | https://support.apple.com/nl-nl/guide/watch/apd3bf6d85a6/watchos | Metrics: "actieve calorieën", "trainingsminuten", "sta-uren" |
| Fitness app | **de Conditie-app** (iPhone, iPad); "Aan de slag met Conditie op de iPhone" | https://support.apple.com/nl-nl/guide/iphone/ipha5dddb411/ios ; https://www.apple.com/nl/apple-fitness-plus/ | Translated: "Conditie", not "Fitness" |
| Activity app (Apple Watch) | **de Activiteit-app** | https://support.apple.com/nl-nl/guide/watch/apd3bf6d85a6/watchos | |
| Workout app | **de Work-out-app** ("Een work-out starten op je Apple Watch"); noun **work-out** / **work-outs** | https://support.apple.com/nl-nl/guide/watch/apdd16e8761a/watchos ; https://support.apple.com/nl-nl/108790 | Always hyphenated by Apple (129 hits, 0 "workout"); non-breaking hyphen on apple.com ("work‑out") |
| Heart / Fitness+ | **Apple Fitness+** ("Fitness+-trainers", "Probeer gratis uit") | https://www.apple.com/nl/apple-fitness-plus/ | English name kept |
| Wrist temperature | **polstemperatuur** ("Je nachtelijke polstemperatuur bijhouden met de Apple Watch") | https://support.apple.com/nl-nl/guide/watch/apd526d20feb/watchos ; https://support.apple.com/nl-nl/102674 | |
| Blood Oxygen | **de Saturatie-app**; "saturatie", "zuurstofgehalte in je bloed" | https://support.apple.com/nl-nl/guide/watch/apdaf17aa5ef/watchos | Not "Zuurstofsaturatie-app" |
| Noise | **de Geluid-app**; "geluidsniveau" | https://support.apple.com/nl-nl/guide/watch/apd00a43a9cb/watchos | |
| Headphone audio levels | "het geluidsniveau van je koptelefoon"; "Gehoorbescherming voor koptelefoons" | https://support.apple.com/nl-nl/guide/iphone/iph0596a9152/ios | |
| Sleep apnea notifications | **slaapapneumeldingen** ("Slaapapneumeldingen ontvangen op de Apple Watch") | https://support.apple.com/nl-nl/guide/watch/apd4e7713562/watchos | |
| Journal app | **het Dagboek** / "de Dagboek-app"; "In je dagboek schrijven op de iPhone" | https://support.apple.com/nl-nl/guide/iphone/iph9824e83ce/ios | |
| Steps | stappen | https://support.apple.com/nl-nl/guide/watch/apd3bf6d85a6/watchos | "het totale aantal stappen" |
| Flights climbed | **gelopen trappen** ("de gelopen trappen") | https://support.apple.com/nl-nl/guide/watch/apd3bf6d85a6/watchos | |

## System features

| English | Dutch (Netherlands) as Apple writes it | Source | Note |
|---|---|---|---|
| Home Screen | **beginscherm** ("Je beginscherm aanpassen", "Apps en widgets in het beginscherm verplaatsen") | https://support.apple.com/nl-nl/guide/iphone/iphd2fc8ce30/ios | One word |
| Lock Screen | **toegangsscherm** ("Een aangepast iPhone-toegangsscherm aanmaken") | https://support.apple.com/nl-nl/guide/iphone/iph4d0e6c351/ios | Not "vergrendeld scherm" / "vergrendelscherm" |
| Widgets | **widgets** ("Widgets toevoegen, wijzigen en verwijderen op de iPhone"); 'Voeg widget toe'; widget 'Schermtijd' | https://support.apple.com/nl-nl/guide/iphone/iphb8f1bf206/ios | Today View = "Vandaag-weergave" |
| Smart Stack | **slimme stapel** ("de slimme stapel", lowercase; "Actuele widgets in de slimme stapel op de Apple Watch bekijken"); control 'Slimme stapel' > 'Live activiteiten' | https://support.apple.com/nl-nl/guide/watch/apdecf142fb9/watchos ; https://support.apple.com/nl-nl/guide/iphone/iphb8f1bf206/ios | |
| Live Activities | **live activiteiten** (lowercase, two words; "Live activiteiten bekijken in het Dynamic Island op de iPhone") | https://support.apple.com/nl-nl/guide/iphone/iph28f50d10d/ios ; https://support.apple.com/nl-nl/guide/watch/bz1vx4mwqbw9/watchos | |
| StandBy | **'Stand-by'** (with a hyphen, quoted: "'Stand-by' op de iPhone gebruiken om op afstand informatie te bekijken") | https://support.apple.com/nl-nl/guide/iphone/iph878d77632/ios | Apple also writes "Stand‑by-wijzerplaat" with a non-breaking hyphen |
| Dynamic Island | **het Dynamic Island** (neuter) | https://support.apple.com/nl-nl/guide/iphone/iph28f50d10d/ios | English name kept |
| Control Center | **bedieningspaneel** ("Het bedieningspaneel gebruiken en aanpassen op de iPhone"; Mac: "bedieningspaneel" too) | https://support.apple.com/nl-nl/guide/iphone/iph59095ec58/ios ; https://support.apple.com/nl-nl/guide/mac-help/mchlc9d0e1f2/mac | |
| Notification Center | not verified (iOS 16+ stacks notifications on the Lock Screen: "Meldingen bekijken en erop reageren") | https://support.apple.com/nl-nl/guide/iphone/iph6534c01bc/ios | "meldingen"; no "berichtencentrum" |
| Settings (iOS) | **Instellingen** ("de Instellingen-app", "Tik in Instellingen op ...") | https://support.apple.com/nl-nl/guide/iphone/iph76e54c61e/ios | |
| System Settings (Mac) | **Systeeminstellingen** ("Ga naar Systeeminstellingen op de Mac") | https://support.apple.com/nl-nl/guide/mac-help/mh15217/mac | |
| Shortcuts | **Opdrachten** ("de Opdrachten-app", "Gebruikershandleiding Opdrachten"); one shortcut = **opdracht** | https://support.apple.com/nl-nl/guide/iphone/iph47e1c9d7d/ios ; https://support.apple.com/nl-nl/guide/shortcuts/welcome/ios | Gallery = 'Galerie' |
| Siri | **Siri** (bare in the guides, 268 hits; "de Siri-app", "de Siri-instellingen" compounds); settings label 'Siri'; 'Zet Siri aan' | https://support.apple.com/nl-nl/guide/iphone/iph83aad8922/ios | Wake phrase: "Siri" or "Hé, Siri" |
| Wallet | **Wallet** ("de Wallet-app"); "Apple Wallet", "Apple Pay" | https://support.apple.com/nl-nl/guide/iphone/iph9b7f53382/ios ; https://www.apple.com/nl/apple-pay/ | |
| Weather | **Weer** ("de Weer-app", widget 'Weer') | https://support.apple.com/nl-nl/guide/iphone/iph1ac0b35f/ios | |
| Calendar | **Agenda** ("de Agenda-app") | https://support.apple.com/nl-nl/guide/iphone/iph3d110f84/ios | |
| Reminders | **Herinneringen** ("de Herinneringen-app") | https://support.apple.com/nl-nl/guide/iphone/iphc7880ecd6/ios | |
| Files | **Bestanden** ("de Bestanden-app") | https://support.apple.com/nl-nl/guide/iphone/iphbbcf8827d/ios | |
| Photos | **Foto’s** ("de Foto’s-app"; ig writes Foto's with a straight apostrophe) | https://www.apple.com/nl/apple-intelligence/ ; ig | |
| Camera | **Camera** ("de Camera-app") | https://www.apple.com/nl/apple-fitness-plus/ ; ig | |
| Clock / alarm | **Klok** ("een wekker zetten in Klok", "de Klok-app") | https://support.apple.com/nl-nl/guide/iphone/iph2909d3a74/ios | |
| Universal Clipboard | **universele klembord** ("Via het universele klembord kun je content op een van je Apple apparaten kopiëren"); title "Kopiëren en plakken tussen je iPhone en andere Apple apparaten" | https://support.apple.com/nl-nl/guide/iphone/iph220ea8dca/ios | Lowercase, neuter: "het universele klembord" |
| Handoff | **Handoff** ("Taken verplaatsen tussen je iPhone en je andere apparaten") | https://support.apple.com/nl-nl/guide/iphone/iphcec5d0a9d/ios | English name kept |
| AirDrop | **AirDrop** ("Met AirDrop onderdelen naar Apple apparaten in de buurt versturen") | https://support.apple.com/nl-nl/guide/iphone/iphcd8b9f0af/ios | |
| Continuity | **Continuïteit** ("Introductie tot Continuïteit"; "continuïteitsfuncties") | ig ; mg | |
| Share sheet | **deelmenu** ("om het deelmenu in te stellen"); the button is the **deelknop** ("op de deelknop tikt"); title "Deelopties aanpassen in een iPhone-app" | https://support.apple.com/nl-nl/guide/iphone/iphc572ca489/ios | Not "deelblad" |
| Screen Time | **Schermtijd** (capitalised, "Schermtijd voor jezelf instellen op de iPhone") | https://support.apple.com/nl-nl/guide/iphone/iphbfa595995/ios | |
| App Limits | **tijdslimieten** (the label is 'Tijdslimieten'; "tijdslimieten voor apps"); in the Ask to Buy article "appbeperkingen" | https://support.apple.com/nl-nl/guide/iphone/iphbfa595995/ios ; https://support.apple.com/nl-nl/105055 | |
| Downtime | 'Schema voor schermtijd' (verified iOS 27, 2026-11-19, on both Screen Time pages; iphb0c7313c9 also writes 'Schermtijdschema' once); steps 'Schema' (switch), 'Voeg schema toe', 'Verwijder dit tijdvenster'; in 'Tijdslimieten' the switch 'Match schema voor schermtijd'; older "Rusttijd" not on any page fetched | https://support.apple.com/nl-nl/guide/iphone/iphbfa595995/ios, https://support.apple.com/nl-nl/guide/iphone/iphb0c7313c9/ios | Do not use "Rusttijd" |
| Always Allowed | 'Altijd toegestaan' (verified 2026-11-19), with 'Voeg personen toe', 'Voeg apps toe', 'Wijzig'; also 'Beheer categorieën', 'Verwijder categorie (naam van de categorie)', 'Beheer schermtijd', 'Deel op alle apparaten' (needs iOS 27 on every device), 'Schakel 'App- en websiteactiviteit' in' / '… uit', reports 'Gemiddelde per dag', 'Week', 'Dag' | https://support.apple.com/nl-nl/guide/iphone/iphb0c7313c9/ios | |
| Editors' Choice (App Store badge) | 'Keuze van de redactie'; editorial notes «App Store - aantekeningen van de redactie» | Dutch App Store product pages (apps.apple.com/nl, saved 2026-11-19) | never «uitgelicht door de redactie» |
| Family Sharing | **Delen met gezin** (quoted 'Delen met gezin'; "een 'Delen met gezin'-groep"; "'Delen met gezin'-leden") | https://support.apple.com/nl-nl/guide/iphone/iph223f61318/ios | Organiser = **gezinshoofd**; members = **gezinsleden**; "Aankopen delen", "Abonnementen delen" |
| Ask to Buy | **Vraag om te kopen** | https://support.apple.com/nl-nl/105055 | |
| Apple Account | **Apple Account** ("je Apple Account", "bij je Apple Account inloggen"); title "Inloggen bij je Apple Account en je Apple Account beheren op de iPhone"; Settings row 'Apple Account' | https://support.apple.com/nl-nl/guide/iphone/iph76e54c61e/ios | 0 "Apple ID". "Apple Account-saldo" |
| Sign in with Apple | **'Log in met Apple'** (button and feature; "Met 'Log in met Apple' kun je met je Apple Account inloggen bij deelnemende websites en apps") | https://support.apple.com/nl-nl/guide/iphone/iph238921d37/ios | Capital L as a label; "inloggen bij" in running text |
| Two-factor authentication | twee-factor-authenticatie | https://support.apple.com/nl-nl/guide/iphone/iph76e54c61e/ios | |
| iCloud | **iCloud** (no article in headings; "in iCloud" 83 hits, "de iCloud" 12 in "de iCloud-gebruikershandleiding"); iCloud+ ("Een abonnement nemen op iCloud+") | https://support.apple.com/nl-nl/guide/iphone/iphde0f868fd/ios ; https://www.apple.com/nl/icloud/ | |
| iCloud Drive | **iCloud Drive** (label 'iCloud Drive'; "iCloud Drive configureren op de iPhone") | https://support.apple.com/nl-nl/guide/iphone/iphbbcf8827d/ios | |
| iCloud sync wording | 'Synchroniseer deze iPhone' (the Drive toggle); "synchroniseren met iCloud"; "up-to-date gehouden op al je apparaten"; "Back‑up in iCloud" | https://support.apple.com/nl-nl/guide/iphone/iphbbcf8827d/ios ; https://support.apple.com/nl-nl/guide/iphone/iphde0f868fd/ios | Path: Instellingen > '[ je naam ]' > 'iCloud' > 'Toon alles' |
| Back up | **back‑up** ("Een back‑up van je gezondheidsgegevens in iCloud maken") | https://support.apple.com/nl-nl/guide/iphone/iph11f1eb698/ios | |
| Apple Intelligence | **Apple Intelligence** (English kept); "Schrijfhulp", "Image Playground", "Genmoji", "visuele intelligentie", "de Siri-app" | https://support.apple.com/nl-nl/guide/iphone/iphc28624b81/ios ; https://www.apple.com/nl/apple-intelligence/ | |
| Face ID / Touch ID | Face ID, Touch ID | https://support.apple.com/nl-nl/105055 | |
| Dark Mode | **donkere modus** (lowercase; title "Donkere modus gebruiken op een iPhone en iPad") | https://support.apple.com/nl-nl/108350 | Accessibility: 'Donkere interface' (store) |
| Reduce Motion | **verminderde beweging** / "De beweging van het scherm ... verminderen" | https://support.apple.com/nl-nl/111781 | Store accessibility label 'Verminderde beweging' |
| Airplane mode | **vliegtuigmodus** (iPhone: "vliegtuigmodus"; Watch title "De vliegtuigmodus op de Apple Watch gebruiken") | https://support.apple.com/nl-nl/guide/watch/apdc22c9d320/watchos | |
| Low Power Mode | **energiebesparingsmodi** (plural title "De batterijduur verlengen met energiebesparingsmodi op de iPhone") | https://support.apple.com/nl-nl/guide/iphone/iphcab9aecd1/ios | |
| Find My | **Zoek mijn** | ig | |
| Spotlight | **Spotlight** | https://support.apple.com/nl-nl/guide/iphone/iph3c511548/ios | |
| Picture in Picture | **Beeld in beeld** | ig | |
| Always-On Display | 'Altijd aan' (display option) | https://support.apple.com/nl-nl/guide/iphone/iph878d77632/ios | |

## Privacy, tracking and purchases

| English | Dutch (Netherlands) as Apple writes it | Source | Note |
|---|---|---|---|
| App Tracking Transparency | **transparante apptracking** ("de functie voor transparante apptracking"); "Toestemming voor apptracking instellen op de iPhone" | https://support.apple.com/nl-nl/102420 ; https://support.apple.com/nl-nl/guide/iphone/iph4f4cbd242/ios | "apptracking" one word |
| Settings toggle "Allow Apps to Request to Track" | **'Sta trackingverzoeken van apps toe'** (Settings > 'Privacy en beveiliging' > 'Tracking') | https://support.apple.com/nl-nl/102420 ; https://support.apple.com/nl-nl/guide/iphone/iph4f4cbd242/ios | |
| ATT prompt buttons | **'Sta toe'** and **'Vraag app om niet te tracken'** ("Als een app vraagt om je activiteit te volgen") | https://support.apple.com/nl-nl/102420 | Prompt title: "Als een app vraagt om je activiteit te volgen" |
| tracking (noun) | **tracking** (English kept: "Bij tracking worden uit een app verzamelde gegevens ... gekoppeld") | https://support.apple.com/nl-nl/102420 | |
| to track (verb) | **volgen** ("je activiteit ... volgen") and "tracken" only in the button 'Vraag app om niet te tracken' | https://support.apple.com/nl-nl/102420 | "je activiteit in apps en op websites van andere bedrijven volgen" |
| Privacy label / nutrition label | **privacylabel** ("Aan de hand van het privacylabel bepaal je of de app voor jou geschikt is") | https://www.apple.com/nl/privacy/ | |
| App Privacy (section) | **Privacy van app** (store section heading) | https://apps.apple.com/nl/app/id904237743 (Things 3) | |
| Data Not Collected | **Er worden geen gegevens verzameld**; sentence "De ontwikkelaar verzamelt geen gegevens van deze app." | https://apps.apple.com/nl/app/id6760043411 (LiftLog) | |
| Data Not Linked to You | **Niet aan jou gekoppelde gegevens** ("De volgende gegevens worden mogelijk verzameld, maar zijn niet gekoppeld aan je identiteit") | https://apps.apple.com/nl/app/id904237743 | |
| Data Linked to You | **Aan jou gekoppelde gegevens** | https://apps.apple.com/nl/app/id904237743 | |
| Data Used to Track You | **Gegevens die worden gebruikt om je te volgen** ("De volgende gegevens worden mogelijk gebruikt om je te volgen op apps en websites van andere bedrijven") | https://apps.apple.com/nl/app/id835599320 (TikTok) | |
| Privacy section help line | "Privacy: definities en voorbeelden"; "Deze informatie is niet door Apple geverifieerd" | https://apps.apple.com/nl/app/id904237743 | |
| Subscriptions management path | **Instellingen > [je naam] > 'Abonnementen'** ("Tik in Instellingen op je naam. Tik op ‘Abonnementen’. Tik op het abonnement.") | https://support.apple.com/nl-nl/118428 ; https://support.apple.com/nl-nl/guide/iphone/iph4e3e7324f/ios | Mac: App Store > naam > 'Abonnementen' |
| Cancel Subscription | **'Zeg abonnement op'** (the iPhone guide: "tik vervolgens op 'Zeg abonnement op' of 'Annuleer alle diensten'"). The article names both: "Tik op 'Annuleer abonnement'. Mogelijk moet je omlaag scrollen om de knop 'Zeg abonnement op' te vinden." | https://support.apple.com/nl-nl/guide/iphone/iph4e3e7324f/ios ; https://support.apple.com/nl-nl/118428 | Apple's own article is inconsistent. Verb: "een abonnement opzeggen" (article title "Een abonnement van Apple opzeggen") |
| Subscription | **abonnement** (170 hits) | https://support.apple.com/nl-nl/118428 | "gezinsabonnement", "proefabonnement" |
| Request a refund (reportaproblem) | "Een terugbetaling aanvragen voor apps of materiaal die je van Apple hebt gekocht"; "Log in bij reportaproblem.apple.com. Tik of klik op 'Ik wil graag' en kies vervolgens 'Om restitutie verzoeken'." | https://support.apple.com/nl-nl/118223 | "terugbetaling" (noun), "restitutie" only in the button |
| Restore Purchases | not verified as a button label. Apple's closest: "Aangeschafte en verwijderde onderdelen terugzetten op de iPhone" ("gekochte onderdelen opnieuw downloaden ... zonder dat je ze opnieuw hoeft te kopen") | https://support.apple.com/nl-nl/guide/iphone/iphfe205f2e5/ios | Use "terugzetten"/"opnieuw downloaden"; for the in-app button the developer chooses ("Aankopen herstellen" is not on any Apple page) |
| Purchase history | **'Apps en aankoopgeschiedenis'** > 'Aankoopgeschiedenis' | https://support.apple.com/nl-nl/guide/iphone/iph4e3e7324f/ios | |
| Receipt | **ontvangstbewijs** ("ontvangstbewijs van Apple") | https://support.apple.com/nl-nl/118223 | |
| In-App Purchases | **in-app aankopen** (store label "In-app aankopen"; article "een in-app aankoop doen") | https://apps.apple.com/nl/app/id6757438990 ; https://support.apple.com/nl-nl/105055 | |
| Free trial | **gratis proefperiode** ("Na afloop van de gratis proefperiode"); "gratis proefabonnement"; CTA "Probeer gratis uit" | https://www.apple.com/nl/apple-fitness-plus/ | "3 maanden gratis", "1 maand gratis" |
| Auto-renewal | "Het abonnement wordt automatisch verlengd totdat het wordt opgezegd." | https://www.apple.com/nl/apple-fitness-plus/ | |
| Premium wording on the store | "Er is een abonnement vereist" for Arcade: "(abonnement vereist)" | https://support.apple.com/nl-nl/guide/iphone/iphc90580097/ios | |

## App Store and developer

| English | Dutch (Netherlands) | Source | Note |
|---|---|---|---|
| App Store | **App Store** (English kept, "de App Store"; NBSP inside on apple.com) | https://www.apple.com/nl/app-store/ | |
| Mac App Store | **Mac App Store** (store name; Xcode's page title "Xcode-app - App Store") | badge SVG ; https://apps.apple.com/nl/app/xcode/id497799835 | |
| "Download on the App Store" badge | **"Download in de App Store"** (line 1 `Download in de`, line 2 `App Store`) | https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/nl-nl (SVG title `Download_on_the_App_Store_Badge_NL_RGB_blk_100317`) | See "Official badge wording" |
| Mac App Store badge | **"Download in de Mac App Store"** (line 1 `Download in de`, line 2 `Mac App Store`) | https://tools.applemediaservices.com/api/badges/download-on-the-mac-app-store/black/nl-nl (SVG title `Download_on_the_Mac_App_Store_Badge_NL_RGB_blk_100317`) | |
| Get button | **Download** (button title in the page JSON, 26 to 36 hits per page; 0 "Verkrijg", 0 "Haal") | https://apps.apple.com/nl/app/id6760043411 | Paid apps show the price in the button position |
| Free (price) | **Gratis** (hero line "Gratis · In-app aankopen"; iTunes lookup `formattedPrice` "Gratis") | https://apps.apple.com/nl/app/id835599320 ; https://itunes.apple.com/lookup?id=6760043411&country=nl&lang=nl_nl | Capital G |
| Price | **€ 9,99** (U+00A0 between € and the number) | https://apps.apple.com/nl/app/id904237743 ; iTunes lookup `formattedPrice` "€\xa09,99" | In-app rows: "€ 0,39", "€ 16,49" |
| Hero line, free app with in-app purchases | "Gratis · In-app aankopen · Ontworpen voor iPad. Niet geverifieerd voor macOS." / "Gratis · In-app aankopen" | https://apps.apple.com/nl/app/id6757438990 (Observa) ; https://apps.apple.com/nl/app/id835599320 | Separator is " · " (space, U+00B7, space) |
| Ratings and reviews | **Beoordelingen en recensies**; "4,7 van de 5"; "1,7K beoordelingen"; header chip "1,7K beoor­delingen" | https://apps.apple.com/nl/app/id904237743 (Things 3) | Comma decimal; **K** (not "k", no space): "1,7K", "416K beoordelingen" (TikTok) |
| No ratings yet | "Deze app heeft niet genoeg beoordelingen of recensies ontvangen voor een overzicht." | https://apps.apple.com/nl/app/id6757438990 | |
| Star count in a sentence | "beoordelingen", "recensies" (9 and 2 hits on the guide and marketing pages) | https://support.apple.com/nl-nl/guide/iphone/iphc90580097/ios | "Beoordelingen en recensies" in the App Store info list |
| Version history | **Versiegeschiedenis**; "Nieuw"; "Versie 3.25.3"; "3 uur geleden", "2 dgn geleden", "5 nov", "25-10-2017" (review date) | https://apps.apple.com/nl/app/id904237743 ; https://apps.apple.com/nl/app/id835599320 | |
| Information list | **Informatie**: "Grootte", "Categorie", "Compatibiliteit", "Talen", "Leeftijd", "Provider", "Copyright", "Ondersteunt" | https://apps.apple.com/nl/app/id904237743 | "Vereist iOS 16.4 of nieuwer." |
| Family Sharing row (store) | "Delen met gezin: Maximaal zes gezinsleden kunnen deze app gebruiken wanneer 'Delen met gezin' is ingeschakeld." | https://apps.apple.com/nl/app/id904237743 | |
| Age rating | **Leeftijdsclassificatie** (4+, 13+) | https://apps.apple.com/nl/app/id904237743 | |
| Developer | **Ontwikkelaar**; "appontwikkelaar" | https://apps.apple.com/nl/app/id904237743 | |
| Accessibility (store) | **Toegankelijkheid**; "Ondersteunde functies": VoiceOver, Stembediening, Grotere tekst, Donkere interface, Voldoende contrast, Verminderde beweging | https://apps.apple.com/nl/app/id904237743 | |
| Platform tabs | Zoek, Vandaag, Games, Apps, Arcade; platform: iPhone, iPad, Mac, Watch, TV | https://apps.apple.com/nl/app/id6757438990 | |
| Mac-only note | "Alleen voor Mac"; for an iPad-only app on a Mac "Niet geverifieerd voor macOS" | https://apps.apple.com/nl/app/xcode/id497799835 ; https://apps.apple.com/nl/app/id6757438990 | |
| Store page title | "<naam>-app - App Store" (e.g. "Things 3-app - App Store", "Xcode-app - App Store"; leading U+200E) | https://apps.apple.com/nl/app/id904237743 | |
| App Store Connect | not verified: no Dutch page (developer.apple.com/nl 404, support guide 404); keep "App Store Connect" | https://developer.apple.com/app-store-connect/ | English only |
| TestFlight | not verified: no Dutch page (testflight guide on support.apple.com/nl-nl is the English "Page Not Found - Apple Support (GW)"; the Dutch App Store page for id899247664 returned HTTP 429, not read) | https://support.apple.com/nl-nl/guide/testflight/welcome/ios | Keep "TestFlight" |
| Xcode | **Xcode** (English; store page text is English too, title "Xcode-app", category "Ontwikkelaarstools") | https://apps.apple.com/nl/app/xcode/id497799835 | |

## Devices and platforms

| English | Dutch (Netherlands) | Source | Note |
|---|---|---|---|
| iPhone, iPad, Mac | iPhone, iPad, Mac; "de iPhone" (311), "de iPad" (8), "de Mac" (34) | ig ; mg | |
| Apple Watch | **de Apple Watch** (13 hits "de", 0 "het") | wg | "je Apple Watch" |
| Apple Pencil | Apple Pencil (English; apple.com page title "Apple Pencil - Apple (NL)") | https://www.apple.com/nl/apple-pencil/ | |
| Apple Vision Pro | Apple Vision Pro | https://support.apple.com/nl-nl/118428 | |
| iOS / iPadOS / macOS / watchOS | iOS 27, iPadOS 27, macOS 27, watchOS 27, visionOS 27 ("iOS 27 of nieuwer") | https://support.apple.com/nl-nl/guide/iphone/iphbfa595995/ios | "of nieuwer" for "or later" |
| Apple devices | **Apple apparaten** (open compound, 26 hits; "Apple-apparaten" 2) | https://support.apple.com/nl-nl/guide/iphone/iph220ea8dca/ios | |
| Digital Crown | de Digital Crown | https://support.apple.com/nl-nl/guide/watch/bz1vx4mwqbw9/watchos | |
| Watch face | **wijzerplaat** | https://support.apple.com/nl-nl/guide/watch/bz1vx4mwqbw9/watchos | |
| Side button / Home button | zijknop / thuisknop | https://support.apple.com/nl-nl/guide/iphone/iph83aad8922/ios | |
| Action button | actieknop | ig | |

## Dutch App Store category names (lookup `lang=nl_nl`, genres array, checked 2026-11-19)

Source: https://itunes.apple.com/lookup?id=6755734580,6756589122,6757163182,6757253009,6757268612,6757280643,6757345400,6757438990,6758459119,6758547802,6758788164,6759511759,6760043411,6761336870,6761451361,6761656926,6771099230,6773507068,6794340136,6806255929&country=nl&lang=nl_nl

| English | Dutch |
|---|---|
| Health & Fitness | Gezondheid en fitness |
| Utilities | Diensten |
| Productivity | Productiviteit |
| Lifestyle | Lifestyle |
| Developer Tools | Ontwikkelaarstools |
| Education | Onderwijs |
| Reference | Naslagwerken |
| Business | Zakelijk |
| Games | Games |
| Puzzle (game) | Puzzel |
| Board (game) | Bordspel |
| Casual (game) | Casual |
| Graphics & Design | Grafisch en ontwerp |
| Food & Drink | Eten en drinken |
| Finance | Financiën |
| Medical | Geneeskunde |
| Entertainment | Amusement (TikTok page) |

## Register: je, jij or u?

**Apple Netherlands uses "je / jij" throughout.** Counts (body text only, feedback-box and version-selector chrome excluded):

| Page set | Files | je / jij / jouw / jou / jezelf | u / uw |
|---|---|---|---|
| iPhone user guide pages | 61 | 2022 | 0 |
| Apple Watch user guide pages | 24 | 895 | 0 |
| Mac user guide pages | 5 | 128 | 0 |
| Support articles (15 numbered articles) | 15 | 931 | 0 |
| apple.com/nl marketing (iPhone, App Store, iCloud, Apple Fitness+, Apple Intelligence, Apple Pay, privacy, iPhone compare excluded) | 8 | 959 | 0 |
| Other guides (Opdrachten, Platform Security, Sleutelhangertoegang) | 7 | 13 | 0 |

Chrome outside the body: the guide header "Als u deze regelaar wijzigt, wordt deze pagina automatisch bijgewerkt" (88 guide pages) and the feedback widget ("Neem geen persoonlijke informatie op in uw opmerking", "Hartelijk dank voor uw feedback") carry "u / uw". The text above the line is "je"; those two widgets are the only exceptions.

Examples, all Apple Netherlands:
- "Tik in Instellingen op je naam. Tik op ‘Abonnementen’. Tik op het abonnement." (article 118428)
- "Je kunt abonnementen van Apple of abonnementen die je hebt gekocht met een app uit de App Store opzeggen via internet of op je apparaat." (article 118428)
- "Jij en je gezinsleden kunnen via 'Delen met gezin' in aanmerking komende appaankopen, jullie locatie en zelfs gezondheidsgegevens met elkaar uitwisselen." (iPhone guide welcome page)
- "Gebruik de Camera-app om je gratis proefabonnement te activeren." (apple.com/nl/apple-fitness-plus/)
- "Je kunt op elk moment toestemming geven aan een app om je activiteit te volgen of de toestemming hiervoor intrekken." (article 102420)
- "Probeer gratis uit" (button), "Ontdek work‑outs ontworpen voor jou. En met jou." (marketing)

Imperative: "Tik", "Ga naar", "Open", "Kies", "Voer in", "Scrol", "Veeg", "Klik" (Mac). On the Dutch store the developer line is "Ga voor meer informatie naar het privacybeleid van de ontwikkelaar" and "ga je naar Privacy: definities en voorbeelden". Plural "jullie" (2 hits) only for the family group. No "gij", no Flemish forms.

What this means for the site: informal "je" with "jouw/je" possessives and imperatives ("Tik", "Open"), exactly TRANSLATION.md 13's default. Never "u".

## Typography

All measured on the raw HTML of the pages listed above.

- **Quotes for UI labels**: straight single quotes ' in the guide pages (2637 straight, 9 curly ’; 0 “ ” and 0 « »). Example: "Tik op 'Schermtijd' en tik vervolgens op 'Schema voor schermtijd'." Apostrophes inside words are straight too ("foto's", "schema's"), so "Tik op 'Foto's'" has an inner apostrophe. The support articles mix straight ' (820), curly ‘ (82) and curly ’ (119). apple.com/nl marketing uses the curly apostrophe ’ (132) and curly ‘ (10) and no straight single quote. Double quotes (straight " 36 in guides, 6 in articles) are for spoken or typed examples: Zeg "Siri" of "Hé, Siri"; "Plan een vergadering met Jeroen om 9 uur". The site can use one consistent pair: curly single quotes ‘ ’ for UI labels is Apple's article style; straight ' is Apple's guide style.
- **Inner spacing**: no space inside the quotes. No space before `:`, `;`, `?`, `!`. Closing quote before the full stop or comma.
- **Menu path separator**: `>` with a NBSP before and a plain space after in the iPhone guide (54 NBSP-before-">" occurrences, 0 plain-space-before in the guide pages; articles write plain spaces: "Instellingen > Privacy en beveiliging"). Steps are usually a chain of verbs.
- **Decimal comma**: `1,7K`, `4,7 van de 5`, `1,8 miljoen`, `127,9 MB`, `€ 9,99`, `3,1 GB`. The only decimal point is a lens aperture (`ƒ/1.8`) and version numbers.
- **Thousands**: four digits with no separator (`1000 nits`, `2030`, `1050` in store text); five or more digits with a **dot**: `40.000 verhalen`, `130.000 apps`, `2.000.000:1`, `270.000 apps`. 0 NBSP or space thousands separators in these pages. "miljoen" / "miljard" spelled out, with the number and word joined by NBSP: `1,9 miljoen`. Store counts: `1,7K`, `416K`.
- **Units and %**: NBSP between number and unit (`256 GB`, 133 NBSP hits; `127,9 MB`). **Percent glued, no space**: `100%`, `50%`, `30%` (57 hits, 0 with a space). Degrees `°C` with a space.
- **Currency**: `€ 9,99`, `€ 79,99 per jaar`, `€ 0,99/maand` with **U+00A0** between € and the amount; € before the number. "per maand", "per jaar", "/maand", "9,99/maand". Free is "Gratis".
- **Dates in running text**: `26 december 2025`, `18 september 2026`, `1 oktober 2026`: day without leading zero, lowercase month name, no "de" and no comma. Article footers: `Publicatiedatum:\xa026 december 2025` (NBSP after the colon). Store: version dates `5 nov`, `3 uur geleden`, `2 dgn geleden`; review dates `25-10-2017` (dd-mm-yyyy with hyphens).
- **Times**: 24-hour clock with a colon and the word "uur": "van 11:00 uur tot 13:00 uur", "om 9 uur"; no "a.m."/"p.m." anywhere. "1 uur", "4 uur per nacht", "24 tot 48 uur".
- **Ordinals**: "2e generatie" (`iPhone SE (2e generatie)`), "3e generatie".
- **Dashes**: the guides use en/em dashes very rarely (4 em dashes in guides, 0 en dashes); marketing uses en dashes with spaces (` – `, 7 hits); the store title uses ` - ` (hyphen). Compound hyphens are often U+2011 non-breaking hyphens: `e‑mail`, `back‑up`, `work‑out`, `Camera‑app`, `Stand‑by-wijzerplaat` (108 in the guides, 115 in marketing). Do not replace them with U+2010.
- **Apostrophe**: straight ' in the guide pages ("foto's", "schema's"), curly ’ on apple.com and the store ("Foto’s-app", "Gerelateerd: apple’s").
- **Ellipsis**: `…` appears in the store ("… meer").
- **NBSP in product names**: apple.com puts U+00A0 inside "App Store", "Apple Watch", "Apple Account" and before "GB", "MB", "nits".
- **Bullet separators on the store hero line**: " · " (U+00B7 with plain spaces).

## Notes for the writer

- **Never "u"**; always "je/jouw". Never Flemish ("gij", "ge", "u" forms, "app-store", "uw").
- "Delen met gezin" (not "Gezinsdeling", "Family Sharing"). "Apple Account" (not "Apple ID", not "Apple-account"). "Schermtijd" (not "Schermtijd" lower case). "Instellingen" / "Systeeminstellingen". "beginscherm", "toegangsscherm", "bedieningspaneel". "Gezondheid" for Health, never "Apple Health" in the site's own words.
- Brand names Apple keeps in English: App Store, Mac App Store, iCloud, iCloud Drive, Apple Account, Apple Intelligence, Apple Pay, Apple Watch, Apple Fitness+, Face ID, Touch ID, AirDrop, Handoff, Spotlight, Siri, Dynamic Island, Digital Crown, Wallet, Xcode, TestFlight, App Store Connect.
- Hyphen vs open compound: "de Gezondheid-app" (hyphen), "de app Vitale functies" (open, Watch guide only). "Apple apparaat" is open, "iPhone-scherm", "iPhone-gebruikershandleiding", "iPad-app" are hyphenated.
- Developers' own Dutch store text (Observa: "hartslagvariabiliteit", "Rusthartslag", "Apple Health", "VO₂ max", "Gereedheid", "work-out"/"workout", "complicaties") differs from Apple's ("hartritmevariabiliteit (HRV)", "hartslag in rust", "Gezondheid", "VO 2 max", "Gereedheid-app", "work-out", "widgets"/"wijzerplaat"). Where a term names an Apple feature, use Apple's form from this file.

## Added from the Tier 1 reviews (2026-11-19, each fetched from the Apple NL page named)

| English | Apple NL | Source |
|---|---|---|
| Advertising identifier (IDFA) | **de reclame-ID (IDFA)** | https://support.apple.com/nl-nl/102420 |
| Privacy label data types | «Foto’s of video’s», **«Overige gebruikerscontent»**, «Aankoopgeschiedenis», **«Ruwe locatie»**, «Gezondheid»; purpose **«App-functionaliteit»** | https://apps.apple.com/nl/app/id284882215 (privacy section) |
| iCloud Backup | toggle **'Back-up in iCloud'**; prose **«iCloud-back-up»**, «back-up» | https://support.apple.com/nl-nl/108922 ; https://support.apple.com/nl-nl/108770 |
| Manage Storage | ‘Opslag’ / **‘Beheer accountopslag’** / ‘Verwijder gegevens uit iCloud’ (Mac: 'Verwijder uit iCloud') | https://support.apple.com/nl-nl/108922 |
| Advanced Data Protection | **«geavanceerde gegevensbescherming»** (heading «Geavanceerde gegevensbescherming voor iCloud»); «Standaard gegevensbescherming»; «encryptiesleutels»; «tijdens de overdracht» | https://support.apple.com/nl-nl/102651 |
| Share With App Developers | **‘Deel met appontwikkelaars’**; 'Analyse en verbeteringen' | https://support.apple.com/nl-nl/guide/mac-help/mh27990/mac |
| iCloud Keychain / Keychain | **«iCloud-sleutelhanger»**; Mac app «Sleutelhangertoegang»; current label ‘Wachtwoorden’ | https://support.apple.com/nl-nl/109016 |
| Apple Account (grammar) | «dezelfde Apple Account», «dezelfde iCloud-account» | https://support.apple.com/nl-nl/102430 |
| Apple's standard EULA | «Licentieovereenkomst voor eindgebruikers van de Gelicentieerde app (‘Standaard licentieovereenkomst voor eindgebruikers’)» | https://www.apple.com/nl/legal/internet-services/itunes/nl/terms.html |
| receipt (App Store) | «ontvangstbewijs» | https://support.apple.com/nl-nl/118223 |
| Version History (store) | «Versiegeschiedenis» | apps.apple.com/nl |
