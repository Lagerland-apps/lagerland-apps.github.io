# Language sheet: Dutch (nl), Netherlands

Never published (`_i18n` is excluded from the build). Rulebook: TRANSLATION.md. Read this sheet before writing or
reviewing any Dutch page. Every decision a translator would otherwise make differently per page lives here.

## Status

| Item | Status |
|---|---|
| Setup (config default, locales.yml block, `_data/i18n/nl.yml`, sitemap and feed stubs) | done 2026-11-19 (nl.yml written by one agent, reviewed and copy-edited by another: 63 values changed) |
| Keyword research (Tier 1) | done 2026-11-19 from Google suggest (hl=nl, gl=nl), Bing (mkt=nl-NL), App Store search hints for the Dutch storefront (143452) and the iTunes Search API (country=nl); Search Console for the Netherlands not read (Claude in Chrome not connected, built-in browser not signed in; the only export on disk, July 2026, shows 1647 impressions and 11 clicks from the Netherlands over three months, with no per-country queries) |
| Tier 1 pages | not started |
| Live | no (`live: false`) |
| Native review | none (NATIVE REVIEWER: none). Every page is logged as "no native review yet" |
| Build time | to be measured |

## Market and register

- Market: the Netherlands. Folder `/nl/`, `<html lang="nl">`, hreflang `nl`, og:locale `nl_NL`, territory NLD,
  currency EUR. Belgian (Flemish) readers share the bare `nl` tag and see Dutch EUR prices; the App Store link opens
  their own storefront.
- Engines (TRANSLATION.md 7.4): Google first, then Bing (also feeds DuckDuckGo, Ecosia, Copilot). Tools: Search
  Console, Bing Webmaster Tools. IndexNow covers Bing and the engines that use it.
- **Formality: je / jij / jouw, lowercase (proposed 2026-11-19, to confirm with the owner).** Reasons:
  1. TRANSLATION.md 13 for nl: «je and jij».
  2. Apple Netherlands writes je: 5139 je, 32 jij, 28 jouw, 64 jou in 97 guide pages, 15 support articles and 8
     marketing pages; the only three «u» are widget chrome (nl-apple-terms.md, Register).
  3. All our apps with a Dutch UI write je (19 apps; the only u strings are Observa's onboarding, about 490 of 1450
     register-marked strings, Taskful Day's one «Uw apparaat», Pawza's vet e-mail template where u is right, and
     Chessful's proverb «Ken uzelf»). The Dutch store descriptions are je as well.
  Consequence: quote Observa only in its je strings. Never u/uw on the site, not even on privacy pages: Apple's own
  Dutch privacy and legal pages address the reader with je.
- Netherlands Dutch, not Flemish: telefoon or iPhone (never gsm), downloaden, e-mail, back-up, instellingen,
  sportschool (not fitnesscentrum in Flemish sense), «abonnement opzeggen» (the searched form; not «annuleren»),
  «geld terug» / «terugbetaling» in prose and Apple's «restitutie» only in its own label. No «gij», no «ge».

## Typography and punctuation

- Quotes: “…” for quotations, ‘…’ for an inner quote. UI labels and menu items go in single curly quotes ‘…’, as
  Apple Netherlands sets them in straight single quotes in its guides: ‘Zeg abonnement op’. A one-word label may stay
  bare when it is clearly a name (Instellingen). No « » on the Dutch site.
- Menu paths: Instellingen > [je naam] > ‘Abonnementen’ (spaces around >, Apple's labels).
- Headings and labels in sentence case: only the first word and proper names take a capital.
- No em or en dashes (8.3). Ranges «3 tot 5 kg» or «tussen 3 en 5». Lists «A, B en C» (no comma before en/of).
- Compounds closed («slaaptracker», «appontwikkelaar», «schermtijdlimiet»); a hyphen where vowels clash or a
  name or abbreviation is part of it (Apple style: «de Gezondheid-app», «de Instellingen-app», «iCloud-synchronisatie»,
  «HRV-meting», «Pro-versie», «AI-analyse»). Never split («slaap score», «app ontwikkelaar»).
- Numbers: decimal comma (4,8); thousands with a dot from five digits on (40.000), four digits without one (1000),
  as Apple Netherlands writes them. Percent with no space («30%»). A space between number and unit: «35 °C», «8 uur»,
  «5 GB», «10 km». Metric units only.
- Times: 24-hour, «22:30 uur» or «22:30». Dates in prose «26 oktober 2026», months lowercase, no article. Templates
  use date.html.
- «app» in body copy, «de app» (common gender, Apple 0 «het app»), «apps». «de App Store», «de Mac App Store»,
  «de Apple Watch», «de iPhone», «de iPad», «de Mac», «het Dynamic Island», «iCloud» without article.
- App names without an article («Observa leest…», «met Soon.»); the common noun is «de app».
- Anglicisms: Dutch where Apple Netherlands or common use has one (Instellingen, abonnement, back-up, beginscherm,
  toegangsscherm, schermtijd, deelmenu, downloaden). English where Dutch searchers and Apple keep it: App Store, App
  Store Connect, widget, Dynamic Island, Apple Watch, iCloud, Siri, ASO, privacy manifest, puzzel/puzzle → «puzzel».
- «work-out» (Apple's spelling) for an Apple Workout session; «training» in general prose.

## Formats (checked 2026-11-19 against the Dutch App Store)

Source: the iTunes lookup API (`country=nl&lang=nl_nl`) for Mockly (paid), Things 3, Observa and LiftLog, and the
apps.apple.com/nl product page of Observa read in the built-in browser (raw characters checked).

| What | Format seen | Where | In the site |
|---|---|---|---|
| Price | `€ 14,99` (Mockly), `€ 9,99` (Things 3): U+00A0 after € | lookup API | locales.yml `EUR: position before_space, space U+00A0, decimal ",", group "."` |
| IAP rows | «Premium maandabonnement € 3,99», «Premium jaarabonnement € 24,99», «Premium eenmalige aankoop € 59,99» (U+00A0) | Observa page | same |
| Free app | `Gratis`; «In-app aankopen» | lookup API, Observa page | `strings.free: "Gratis"` |
| Get button | Download | Apple NL (badge note) | badge text is Apple's artwork wording |
| Thousands | «40.000», «130.000»; «1000 nits» | Apple NL | `group: "."` |
| Rating | «4,7 van de 5», «1,7K beoordelingen» | App Store | `strings.decimal: ","` |
| Dates | «26 december 2025» in running text; Observa page «5 nov» (short) | support.apple.com/nl-nl | `date_long "{d} {month} {Y}"` |
| Privacy label | «Privacy van app», «Er worden geen gegevens verzameld» | Observa page | quoted exactly |
| File size | «92,7 MB» | Observa page | |

Price line pattern: `Gratis, Premium vanaf € 3,99/maand, € 24,99/jaar of € 59,99 eenmalig` (strings.from «vanaf»,
per_month «/maand», per_year «/jaar», lifetime «eenmalig», or «of»). Zero price on plan cards: `{P_ZERO}` → `€ 0`.

Note: the Dutch App Store shows the developer's personal name in the privacy section and seller line. That name never
goes on the site; attribute to "Lagerland Apps".

## Glossary

Companion files: `_i18n/nl-glossary.md` (per app: Dutch coverage, register, feature names verbatim from the string
catalogs, Dutch App Store name and subtitle, tier names, flags) and `_i18n/nl-apple-terms.md` (Apple Netherlands'
own names, each with its Apple source URL). Rule: a feature name is written exactly as the app's Dutch interface shows
it, unless the glossary flags it as defective; an Apple product or feature name exactly as Apple Netherlands writes it.

**Language claims.** Never say **AppMeta** or **Mockly** is in Dutch: neither has an `nl` localization (AppMeta 0 of
2300 keys, Mockly 0 of 333) and neither has a Dutch App Store listing; their Dutch pages say plainly that the app's
interface is in English. The other 19 (18 live plus Clippet) have a complete Dutch catalog (LiftLog 99 %, with 8
English statistics labels). Gaps to keep off the pages: AfterShift's calendar permission prompt, AllPaid's and
RightSplit's Siri phrases and Pawza's camera and photo-library prompts are English only.

The terms that matter most across the site:

| English | Dutch on the site | Source |
|---|---|---|
| (address) you | je / jij / jouw, lowercase; never u / uw | this sheet |
| Download on the App Store (badge) | Download in de / App Store (Mac: Download in de / Mac App Store) | Apple badge artwork nl-nl |
| Free (price) | Gratis | Dutch App Store |
| In-App Purchases | In-app aankopen | Dutch App Store |
| subscription / cancel | «abonnement» / «opzeggen» in prose (the searched form: «abonnement opzeggen iphone»); Apple's labels quoted exactly: Instellingen > [je naam] > ‘Abonnementen’ > ‘Zeg abonnement op’ | keyword research; support.apple.com/nl-nl |
| request a refund | via reportaproblem.apple.com: ‘Ik wil graag’ > ‘Om restitutie verzoeken’; «geld terug» / «terugbetaling» in prose | support.apple.com/nl-nl |
| Restore Purchases | «aankopen herstellen» (the apps' and searchers' form; Apple has no button label) | app catalogs, keyword research |
| lifetime (purchase) | «levenslang» as the tier label where the app says so; «eenmalige aankoop» / «eenmalig» for the price | app catalogs, Dutch App Store IAP rows |
| free trial | gratis proefperiode | Apple NL, app catalogs |
| Family Sharing | Delen met gezin | Apple NL |
| Data Not Collected | Er worden geen gegevens verzameld (section «Privacy van app») | Dutch App Store |
| Health app / Apple Health | de Gezondheid-app (Apple NL has no «Apple Health»; never «Apple Gezondheid») | Apple NL |
| Heart Rate Variability (HRV) | hartritmevariabiliteit (HRV); always SDNN for Apple Health; «HRV (SDNN)» on Observa | Apple NL |
| Resting heart rate | hartslag in rust | Apple NL |
| Sleep stages | Apple: Wakker, Remslaap, Kernslaap, Diepe slaap; Observa's own labels: Wakker / Kern / Diep / REM | Apple NL, Observa catalog |
| Cardio Fitness / VO2 max | cardioconditie / VO2 max | Apple NL |
| Screen Time / App Limits | Schermtijd / tijdslimieten | Apple NL |
| Focus / Sleep Focus | focus / slaapfocus | Apple NL |
| Home Screen / Lock Screen / widgets | beginscherm / toegangsscherm / widgets | Apple NL |
| Live Activities / Smart Stack / StandBy | live activiteiten / slimme stapel / Stand-by | Apple NL |
| Control Center | bedieningspaneel | Apple NL |
| iCloud sync | synchronisatie via iCloud, iCloud-synchronisatie | Apple NL, app catalogs |
| Settings (iOS) | Instellingen (Mac: Systeeminstellingen) | Apple NL |
| Shortcuts / Calendar / Reminders / Files / Weather | Opdrachten / Agenda / Herinneringen / Bestanden / Weer | Apple NL |
| Workout (Apple) | work-out | Apple NL |
| Sign in with Apple | Log in met Apple | Apple NL |
| Apple Account | Apple Account | Apple NL |
| App Tracking Transparency / tracking | ‘Sta trackingverzoeken van apps toe’; tracking = «volgen» («volgt je niet», Apple's privacy label «Gegevens die worden gebruikt om je te volgen») | Apple NL |
| Universal Clipboard | universeel klembord; clipboard in general «klembord» (Clippet's word) | Apple NL, Clippet catalog |
| Share sheet | deelmenu | Apple NL |
| countdown | aftellen / aftelling (Soon.'s words; check the glossary per sentence) | Soon. catalog |
| Journal (section) | Blog (hub title, nav, feed); URLs stay `/nl/journal/` | as decided for es, it, pt |
| stamp sheet (design metaphor) | vel (postzegelvel), «Vel 2025-{year} · Uitgegeven in Finland» | proposed |
| privacy manifest | «privacymanifest» in prose, «privacymanifest (privacy manifest)» at the first mention on home and transparency | as for other languages |
| reviews / ratings (App Store) | recensies / beoordelingen | Dutch App Store |

## Dutch App Store names and subtitles (App Store Connect nl-NL, 2026-11-19)

| App | Dutch name | Dutch subtitle |
|---|---|---|
| AfterShift | AfterShift: Slaap & Ploegen | Herstel, dutjes & vermoeidheid |
| AllPaid | AllPaid – Rekeningen bijhouden | Op tijd betalen, zonder stress |
| AppMeta | (no nl-NL localization) | |
| AppMeta Pulse | AppMeta Pulse: Verkoop & omzet | Recensies beantwoorden met AI |
| Chessful | Chessful: Train & Analyseer | Tactiek, Puzzels & Coach |
| EarnLock | EarnLock: App Blokker & Focus | Minder schermtijd via beweging |
| GymLogger X | GymLogger X: Training Tracker | Krachttraining & Sportschool |
| LiftLog | LiftLog: Kracht & Gym Log | Sets, reps & krachtschema |
| MediaKit | MediaKit Comprimeer Converteer | Video, Audio, Afbeelding & ZIP |
| Millrace | Millrace: Getallenpuzzel | 64 levels, niets is toeval |
| Mockly | (no nl-NL localization; store shows the English «Mockly: Screenshot Maker») | |
| Observa | Observa: HRV & Herstelscore | Paraatheid, Slaap-Cyclus-Coach |
| Pawza | Pawza: Hond & Kat Gezondheid | Enting, gewicht & herinnering |
| RightSplit | RightSplit: Delen & Groep | Rekening & uitgaven scannen |
| Shogiful | Shogiful: Japans schaken | Shogi: tactiek & AI-analyse |
| Soon. | Soon. - Dagen Tot Grote Events | Bruiloft, Reis & Baby Aftellen |
| Tare | Tare: Balans & Logica Puzzel | Denkspel & geheime gewichten |
| Taskful Day | Taskful Day: Dagplanner | Takenlijst & Focus |
| WanderWiki | WanderWiki: ontdek en leer | Feiten, geschiedenis & trivia |
| Xiangqiful | Xiangqiful: Chinees Schaken | Leer xiangqi: tactiek en AI |
| Clippet | Clippet: Klembord Manager (not on the store yet) | Kopiëren & plakken, historie |

The site uses the app's English name (`name` is a fact field); the Dutch store subtitles are a vocabulary source,
not copy to paste (several split compounds and title case: «Logica Puzzel», «Klembord Manager»).

## Keyword research

Full notes, sources and FAQ-style questions per page: `_i18n/nl-keywords.md` (part A: home, hubs, about, support,
transparency, first nine apps; part B: the other apps). Every query below came from one of
those sources. `seo.title`, the H1 and `quick_answer` of each page are written for its primary query.

Search Console for the Netherlands: not read in this session. Revisit 4 to 6 weeks after go-live with the page
filter `/nl/` and the country filter Netherlands.

| Page | Primary query | Secondary queries |
|---|---|---|
| Home (/nl/) | `apps zonder reclame` (the privacy angle has no Dutch demand: «zonder tracking», «privacyvriendelijke apps» empty) | `apps zonder reclame iphone`, `spelletjes apps zonder reclame` |
| Apps hub (/nl/apps/) | `beste apps iphone` | `beste apps ipad`, `beste apps apple watch`, `apps voor mac` |
| About (/nl/lagerland-apps/) | none with demand: brand-led («Lagerland Apps» + «indie appontwikkelaar»); weak `indie apps iphone` | `indie ontwikkelaar apps` |
| Support hub (/nl/support/) | `abonnement opzeggen iphone` | `abonnement opzeggen app store`, `geld terug app store`, `terugbetaling app store`, `aankopen herstellen` |
| Transparency (/nl/transparency/) | `app tracking transparency` (Dutch searchers type the English) | `privacy app store`, `app privacy iphone`, `app privacy labels` |
| AfterShift | `slapen na nachtdienst` | `ploegendienst slaap`, `slaapschuld`, `ploegendienst app` |
| AllPaid | `rekeningen bijhouden app` | `vaste lasten app`, `betalingsherinnering iphone` |
| AppMeta | `aso tool` (developers type English) | `app store connect mac app`, `app metadata editor`, `aso app store` |
| AppMeta Pulse | `app store connect analytics` | `app store connect iphone`, `app store sales report` |
| Chessful | `schaak app` | `beste schaak app`, `schaken leren app`, `schaakpartij analyseren`, `schaakpuzzels app` |
| EarnLock | `apps blokkeren iphone` | `schermtijd beperken`, `app limiet iphone`, `schermtijd verdienen` |
| GymLogger X | `gym app apple watch` | `apple watch krachttraining`, `workout app apple watch` |
| LiftLog | `krachttraining app` («geen abonnement» has no demand; kept in the copy as the differentiator) | `workout log app`, `krachttraining bijhouden`, `trainingslogboek app` |
| MediaKit | `video comprimeren iphone` (H1 or description also `video verkleinen iphone`) | `heic naar jpg`, `pdf comprimeren`, `pdf verkleinen`, `foto verkleinen iphone` |
| Millrace (never write the number title) | `logische puzzel app` | `getallenspel`, `rekenpuzzel`, `puzzel app zonder reclame` |
| Mockly | `app store screenshots` (developers type English) | `app store screenshot generator`, `app store screenshot sizes`, `mockup app store` |
| Observa | `hrv apple watch` | `hartslagvariabiliteit apple watch` (searchers' form; Apple writes hartritmevariabiliteit), `slaapscore apple watch`, `readiness score apple watch` |
| Pawza | `vaccinatieboekje hond` (position as a place to keep and scan records, never as the official passport) | `vaccinaties kat`, `dierenpaspoort`, `huisdieren app` |
| RightSplit | `rekening splitsen app` | `kosten delen app`, `bonnetje splitsen` (`tikkie alternatief` reserved for a Tier 3 page) |
| Shogiful | `shogi app` | `japans schaken`, `shogi regels`, `shogi online` |
| Soon. | `aftel app` | `countdown app`, `countdown widget iphone`, `aftellen naar vakantie` |
| Tare | `beste puzzelgames iphone` (Millrace keeps the logic side; `balans puzzel` is crossword noise) | `denkspelletjes app`, `breinbreker` |
| Taskful Day | `to do lijst app` | `dagplanner app`, `takenlijst app`, `to do lijst iphone` |
| WanderWiki | `willekeurige wikipedia pagina` | `random wikipedia`, `wikipedia app`, `leuke weetjes app` |
| Xiangqiful | `chinees schaken` | `xiangqi`, `chinees schaken spelregels`, `xiangqi app` |
| Clippet (unreleased, unlisted) | `klembord geschiedenis` | `klembord iphone`, `clipboard manager mac`, `kopieer geschiedenis` |

Splits: Chessful owns `schaak`/`schaken`; Shogiful and Xiangqiful never target `schaak app`. AfterShift owns `slaap` and
`nachtdienst`; EarnLock owns `schermtijd` and `apps blokkeren`. GymLogger X and LiftLog are split by «apple watch».
AppMeta takes ASO and metadata, Pulse analytics and sales. Home keeps `apps zonder reclame`; puzzle pages use it only
as a secondary.

## Tells to cut in Dutch (TRANSLATION.md 8.2, plus what reviews find)

Stock phrasing: «In de snel veranderende wereld van vandaag», «In het digitale tijdperk», «Laten we erin duiken»,
«Het is belangrijk om op te merken dat», «Het is vermeldenswaard», «speelt een cruciale rol», «naadloos», «cruciaal»,
«niet alleen … maar ook», «Kortom» as a closer, «Of je nu … of …», «ontdek hoe», «til je … naar een hoger niveau»,
«moeiteloos», «revolutionair», «oplossing» for a product, «op een efficiënte manier», «een wereld van verschil».

From the interface-strings review (2026-11-19): «prijzen» as a verb for "to price" (reads as "praise": «de prijs
bepalen»); «Haal {app}» for "Get" (Apple NL's button: «Download»); «wat je verwachtte dat er zou gebeuren» (cut to «wat je
verwachtte»); «uit {count} beoordelingen» for "from" («op basis van»); «probeer de gidsen» for "try" («bekijk»); noun
calques «na het bekijken van» («nadat je … hebt bekeken»); imperative «Scroll» (Dutch «scrol»); «omrekenen» for media
conversion («converteren», «conversie»); «dataeconomie» (vowel clash: «data-economie»); «privacyvriendelijk» repeated
(vary: «die je privacy respecteren», «zonder tracking», «privacy voorop»). In "{category} category" strings use Apple NL's
App Store category names (Diensten, Onderwijs, Grafisch en ontwerp, Gezondheid en fitness, Financiën). Rating line
«{value} van de 5» (Apple NL).

Translationese: split compounds, title case headings, u and je mixed, English word order with the verb not at the end
of a subordinate clause, «maken» calques («een verschil maken», «zin maken»: write «zinvol zijn»), «dat gezegd
hebbende», «aan het einde van de dag», gerund chains («biedend», «makend»), «gebruiker» everywhere where Dutch says
«je» or «wie», «de» before app names, Flemish vocabulary (gsm, plezant, efkes, «ge»).

## House rules carried over

- No public roadmaps or dated promises. Describe what an app does today.
- Prices only through tokens. No arithmetic on our prices.
- «Geen abonnement» (no subscription) only for LiftLog, Millrace, Mockly and Tare. For the others «geen abonnement
  nodig» or «levenslange optie / eenmalige aankoop», where true.
- «rustig» and «privacy voorop» (calm, privacy-first) once, where they state positioning.
- Never the owner's personal name. Attribute to "Lagerland Apps".
- Millrace's copy never mentions the number title it replaced; Observa's HRV is SDNN, never RMSSD (RMSSD only for
  Observa's ECG-based Premium feature, as on the English page).
- App names, competitor names and "Lagerland Apps" as written in English.

## Review log

| Pages | Writer | Reviewer | Back-translation | Native |
|---|---|---|---|---|
| `_data/i18n/nl.yml` (323 keys) | 1 Sonnet writer | 1 reviewer (copy-editing skill, fact diff, glossary): 63 values changed | n/a | no native review yet |

## Apps still on English screenshots

AppMeta, MediaKit and Mockly (2026-11-19: no `nl` folder in `assets/screenshots/<slug>/`). The other 18 apps already
have `nl` sets from commit 763463c («localized sets for 16 languages»), although the owner's brief said "none yet".
