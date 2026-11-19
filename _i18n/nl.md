# Language sheet: Dutch (nl), Netherlands

Never published (`_i18n` is excluded from the build). Rulebook: TRANSLATION.md. Read this sheet before writing or
reviewing any Dutch page. Every decision a translator would otherwise make differently per page lives here.

## Status

| Item | Status |
|---|---|
| Setup (config default, locales.yml block, `_data/i18n/nl.yml`, sitemap and feed stubs) | done 2026-11-19 (nl.yml written by one agent, reviewed and copy-edited by another: 63 values changed) |
| Keyword research (Tier 1) | done 2026-11-19 from Google suggest (hl=nl, gl=nl), Bing (mkt=nl-NL), App Store search hints for the Dutch storefront (143452) and the iTunes Search API (country=nl); Search Console for the Netherlands not read (Claude in Chrome not connected, built-in browser not signed in; the only export on disk, July 2026, shows 1647 impressions and 11 clicks from the Netherlands over three months, with no per-country queries) |
| Tier 1 pages | written and reviewed 2026-11-19, no native review yet: home, apps hub, 21 app pages (Clippet unlisted), 21 support pages, 21 privacy policies + Clippet terms, about, support hub, transparency (+ `_data/i18n_transparency/nl.yml`), /nl/llms.txt, /nl/llms-full.txt, 21 OG cards |
| Live | yes, `live: true` since 2026-11-19 (Tier 1; go-live commit not yet pushed) |
| Tier 2 | done 2026-11-19 (not pushed). Batch 1 (b2a28be): both hubs, chess, logic puzzles, workout without subscription, xiangqi guides, 3 audience pages, local-only /nl/guides/schermtijd-beperken-iphone/. Batch 2: shogi, bill tracker rewritten around Dyme, Wallet and Spendee (Rocket Money, Monarch, Copilot not sold in NL), local-only /nl/guides/aftellen-op-iphone/. for/indie-ios-developers stays English-only. `i18n.py stale` was 0 on 2026-11-19. Research: ~/Downloads/githubcode/nl-tier2-research-2026-11-19.md; briefs `_i18n/nl-tier2-brief.md`, `_i18n/nl-tier2-review-brief.md`. Next: Tier 3 (local-only «Dyme alternatief» is a candidate; `dyme app alternatief` is reserved for it) |
| Tier 4 | batch 1 done 2026-11-19 (not pushed): hub /nl/journal/ («Blog») + 9 translated posts (steps per day, rest between sets, push pull legs / upper/lower / 5/3/1, deloadweek, 1RM, HRV-waarde, puppy and kitten vaccinations with the NVWA / Rijksoverheid / Your Europe travel rules for rabies, US tipping, puzzle games without ads or lives) and the local-only /nl/journal/mkv-naar-mp4/. Research and queue: ~/Downloads/githubcode/nl-tier4-research-2026-11-19.md; briefs `_i18n/nl-tier4-brief.md`, `_i18n/nl-tier4-review-brief.md`. Inbound links: workout guide (4 posts), Apple Health audience page (2), logic guide, FAQ answers on Pawza, RightSplit and MediaKit; GymLogger X's related post now resolves to the Dutch strength-program post |
| Tier 3 | batch 1 done 2026-11-19 (not pushed): hub /nl/alternatives/ + tricount, splitwise, whoop, oura, chess-com, forest, hevy, pdf-expert and the local-only wiebetaaltwat-alternatief (RightSplit; WieBetaaltWat ★62.348 is the Dutch default for group expenses) and dyme-alternatief (AllPaid). Research ~/Downloads/githubcode/nl-tier3-research-2026-11-19.md (Google suggest hl=nl gl=nl over all 123 English comparisons + Dutch lookup); store data nl-tier3-store-2026-11-19.md (Dutch in-app rows; Oura EU web price; WHOOP has no Dutch price); briefs `_i18n/nl-tier3-brief.md`, `_i18n/nl-tier3-review-brief.md`. The AllPaid page now compares with Dyme instead of Rocket Money (not sold in NL). Next candidates: Opal, Bevel, Lichess, Welltory, one sec, HandBrake, local-only Tikkie and Sleep Cycle (research file) |
| Native review | none (NATIVE REVIEWER: none). Every page is logged as "no native review yet" |
| Build time | 139 s at the setup (main with es, it, pt Tier 2 and 3, other sessions running); 160 s with Dutch Tier 1 (990 audited pages) |

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
English statistics labels). Gaps to keep off the pages: AfterShift's calendar permission prompt and Pawza's camera and photo-library prompts are
English only. AllPaid's and RightSplit's Siri phrases are English only: where a page quotes a Siri phrase (as the English
pages do), say so in brackets («de Siri-zinnen zijn er alleen in het Engels»), as the Tier 1 app pages do.

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
| Support hub (/nl/support/) | `abonnement opzeggen iphone` | `abonnement opzeggen app store`, `geld terug app store`, `terugbetaling app store` |
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
| Shogiful | `shogi app` | `japans schaken`, `shogi regels` (no `shogi online`: the app has no online play) |
| Soon. | `aftel app` | `countdown app`, `countdown widget iphone`, `aftellen naar vakantie` |
| Tare | `beste puzzelgames iphone` (Millrace keeps the logic side; `balans puzzel` is crossword noise) | `denkspelletjes app`, `breinbreker` |
| Taskful Day | `to do lijst app` | `dagplanner app`, `takenlijst app`, `to do lijst iphone` |
| WanderWiki | `willekeurige wikipedia pagina` | `random wikipedia`, `wikipedia app`, `leuke weetjes app` |
| Xiangqiful | `chinees schaken` | `xiangqi`, `chinees schaken spelregels`, `xiangqi app` |
| Clippet (unreleased, unlisted) | `klembord geschiedenis` | `klembord iphone`, `clipboard manager mac`, `kopieer geschiedenis` |

**Search forms vs spelling (decision 2026-11-19).** Dutch searchers often type split forms («aftel app», «schaak app»,
«to do lijst app», «krachttraining app», «rekening splitsen app»). Visible text (seo.title, H1, seo.description,
quick_answer, body, FAQ) uses correct Dutch spelling: closed or hyphenated compounds («aftelapp», «schaakapp»,
«to-dolijst», «takenlijst-app») or a phrase that keeps both words apart naturally («app voor krachttraining», «app om
een rekening te splitsen»). The split search forms go only into `seo.keywords`. Google matches the forms.

Tier 2 (2026-11-19): the chess guide owns `beste schaak app` (moved off Chessful, which took `schaak app iphone`); the local-only
screen-time guide owns `schermtijd beperken iphone` (EarnLock gave up `schermtijd beperken` for `apps blokkeren voor bepaalde tijd`).
Guide primaries: shogi `shogi online`, bill tracker `huishoudboekje app zonder bankrekening`, local countdown guide `aftellen op iphone`, logic `puzzelspellen voor volwassenen`, workout `gratis gym app`, xiangqi `chinees schaken online`, shift workers
`ploegendienst gezondheid`, Apple Health `beste apple watch apps`, calm productivity `productiviteit app iphone` (low demand).

Tier 3 batch 1 (2026-11-19) comparison primaries: WieBetaaltWat `wie betaalt wat alternatief`, Tricount `alternatief voor tricount`, Splitwise `gratis alternatief voor splitwise`, Dyme `dyme app alternatief`, WHOOP `whoop alternatief zonder abonnement`, Oura `oura ring alternatief zonder abonnement`, Chess.com `chess.com abonnement`, Forest `forest app gratis`, Hevy `hevy app gratis`, PDF Expert `pdf expert kosten`. Visible text: «Forest-app», «Hevy-app», «Chess.com-abonnement», «Oura Ring-alternatief», «Whoop-alternatief»; the «zonder abonnement» queries are answered with «zonder verplicht abonnement» / «abonnement optioneel» (Observa sells Premium).

Tier 4 batch 1 (2026-11-19) journal primaries: steps `hoeveel stappen per dag`, rest `rust tussen sets`, strength program
`push pull legs schema` (visible text «push pull legs» + «schema», «upper/lower»), deload `deload week` (visible «deloadweek»), 1RM
`1rm berekenen`, HRV post `hrv waarde` + `lage hrv` (Observa keeps `hrv apple watch`), vaccinations `vaccinaties puppy` + `kitten
vaccinaties` (Pawza keeps `vaccinaties kat`, `dierenpaspoort`), tipping `fooi amerika`, puzzle post `spelletjes zonder reclame` (home
keeps `apps zonder reclame` and `spelletjes apps zonder reclame`), local-only MKV post `mkv naar mp4`.

Splits: Chessful owns `schaak`/`schaken`; Shogiful and Xiangqiful never target `schaak app`. AfterShift owns `slaap` and
`nachtdienst`; EarnLock owns `schermtijd` and `apps blokkeren`. GymLogger X and LiftLog are split by «apple watch».
AppMeta takes ASO and metadata, Pulse analytics and sales. Home keeps `apps zonder reclame`; puzzle pages use it only
as a secondary.

## Decisions from the Tier 1 writing (2026-11-19)

- Readiness follows each app's own Dutch UI: Observa «Gereedheid» (gereedheidsscore), AfterShift «Paraatheid». The store
  subtitles are not a model.
- LiftLog tiers: Eerlijk, Goed, Genereus, Mecenas (the Dutch store names; the app's «Gul» and «Beschermheer» are flagged in I-0382).
- `{TRIAL}` expands to «gratis proefperiode van 7 dagen» (noun phrase): «met een {TRIAL}».
- «Prices in USD» becomes «De prijzen zijn die van de Nederlandse App Store; in andere landen toont de App Store bij het
  afrekenen de prijs in je eigen valuta.»
- Memories vs Reminders in Soon.: «Herinneringen» (Memories, with a clarifying phrase) vs «meldingen» (reminders).
- Shogiful: drop «inzet», castle «burcht» in prose, handicap «voorgift»; MediaKit Redact «zwartmaken».
- Taskful Day check-ins described as «opvolgherinnering», never quoted from the app.

- Abbreviations: PNG, JPG, HEIC, CSV, OCR, SDK’s, QR-code uppercase; «pdf» lowercase as a common noun in prose
  (Woordenlijst; MediaKit's Dutch store text), «PDF» only inside UI names («PDF dierenartsbezoek», MediaKit's category
  «PDF»). Apostrophes curly: foto’s, SDK’s, pdf’s.
- Place adjectives capitalised in visible text («Chinees schaken», «Japans schaken»); lowercase only in seo.keywords.
- App Store "listing" = «productpagina» (App Store Connect's Dutch word), never «listing» or «vermelding».
- Sign-up = «account aanmaken» / «registreren»; sign-in = «inloggen» (Apple NL); never «aanmelden» for either.
- The free tier is «de gratis versie», never «gratis abonnement»; Lifetime is an «optie», never an «abonnement»;
  "every paid plan" = «elke betaalde optie».
- "Cancel anytime" = «Op elk moment opzegbaar» / «Altijd opzegbaar».
- Times «22:00 uur», never 12-hour forms.
- Privacy pages: consent sentence «Door een aankoop te doen, ga je ermee akkoord dat wij met de volgende informatie over die
  aankoop mogen antwoorden:»; "to help it decide" «die helpt bij die beslissing»; "under 13" «jonger dan 13 jaar»;
  "not directed at" «niet gericht op», "not intended for" «niet bedoeld voor» (follow each English page); «reclame-ID (IDFA)»;
  «iCloud-back-up»; «ingangsdatum» where the English says "effective date", ‘Laatst bijgewerkt’ where it says "Last updated".
- Apps whose Dutch UI quotes were corrected against the catalogs in review (use these): Shogiful ‘Train deze zwaktes’,
  ‘Oefenen beginnen’, Nieuweling, Positiespel, Clubplastic, Ebbenhout & goud, Zwevende toren; MediaKit ‘Comprimeer’ /
  ‘Converteer’ per category, ‘Wijzig grootte’; LiftLog ‘Afbeelding bewaren’; Clippet ‘Sta toe’, ‘Voeg knipsel toe’,
  ‘Haal linkvoorbeelden op’; GymLogger X ‘Krachtvoortgang’, ‘Wordt bewaakt’, ‘Plateau voorspeld’; RightSplit ‘Toon in widgets’,
  ‘Verdelen per artikel’; Soon. ‘Op vergrendelscherm houden’ (the app's own string, although Apple says toegangsscherm);
  AfterShift ‘Hersteldetails’; Pulse ‘Toon bedrag’, ‘Per land of regio’; AllPaid ‘App-vergrendeling’, Totaal verschuldigd /
  Betaald / Resterend.
- Taskful Day's sentence parser has no Dutch keywords: the Dutch page gives its example in English (I-0391).

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

From the Tier 1 reviews (2026-11-19): «prijzen» for "to price"; «Haal {app}»; outcome claims («lukt beter met X»);
staged self-answered openers in quick_answer and descriptions («Zoek je …?»); «De vrager» / «De gebruiker» in enrichment
(«Iemand die …»); «hij»/«het»/«haar» for a named app or a de-word («die», or the name); «past zich aan aan»; «meten je aan»;
«herstelt op elke iPhone» (intransitive calque); «op tijd» for "timed" (means punctual); «planken» for planks; «X komt met Y»;
«dek je je gezinsgroep»; «afgewerkt» (Flemish: «kant-en-klaar»); «naast … naast elkaar»; «iets voor inleveren»; «stijlen»,
«de look», «fixes»; «score op 100» (Belgian: «van 0 tot 100»); «X door ontwerp» («van opzet»); two verbs for one meaning;
«kaart» for card («creditcard»); «stuk voor stuk» on chess pages; a bare tier name as subject («Gratis staat … toe»);
«naar beneden onderhandelen»; «doet geen X»; «over het waarom»; «nieuw met schaken»; lowercase place adjectives;
«open-sourceengine»; dangling «Door X te doen, …» clauses with another subject; «één stuk per keer»; «voeden» («tellen mee
voor»); «X naast Y» for comparisons («vergeleken met»); «ontmantelen»; «in uitvoering»; «Thai» («Thais»); «Gratis spelers»;
«geen X en geen Y» for "no X or Y"; language names as adjectives («een Hindi zoekwoordenveld»); English compounds
(«rankedpartijen»); «wegschrijven», «gaan de deur uit»; «vertalingen» for localizations («lokalisaties»); «toestel»
(«apparaat»); «portretstand» («staande stand»); «beginscherm» for an app's own main screen; «laat je een account
aanmaken»; «meteen betalen» («vooraf»); «verbinden met» («verbinding maken met»); «vraagt Apple aan apps om»; «kiezen te +
infinitive» («diensten waarvoor je zelf kiest»); «optellen tot»; «leven op je telefoon»; «razendsnel» overstatement;
«draait op advertenties» («leeft van»); «na een dag dat» («waarop»); «rekensom met twee cijfers» («getallen van twee
cijfers»); gerund subjects («Een artikel bewaren downloadt…»); «verjaardag» for a non-birthday anniversary; «plant op
tijd»; «beste N landen» («top N»); «terugzetten» for restoring purchases («herstellen»); «tussendienst» for swing shift
(«late dienst»); «platformdienst» («grondafhandeling»); invented «-stoornis» compounds; «melatonine dat»; «data» as the plural
of datum («datums»); «Geen enkele» repeated; «als uitgangspunt» for "by default" («als standaard»); fragments («Geen eigen.»).

From the Tier 2 reviews (2026-11-19): invented conditions on Apple steps («alleen», «de eerste keer»); «de app vraagt iOS X»
(«vereist»); «X wisselen de regels met» («veranderen»); «je opening verdienen»; «een voor een» («één voor één»); «dezelfde instellingen
als waarmee»; an ambiguous «Die» opening a sentence; «zijn eigen» for a named app; relative clauses inside list items; «geeft elke fout
een naam uit het xiangqi» («benoemt in xiangqi-termen»); «wat de score heeft verschoven» («waardoor de score is veranderd»); topicalised
«X hebben we daarvoor gemaakt»; «als ik als»; «app voor alles» («allrounder»); «sets aan tafel» («fysieke sets»); coinages («reeksendruk»);
«noemt zijn prijs duidelijk» («is open over zijn prijs»); English if-clauses turned into staged questions; «Apple Watch apps» split
(«Apple Watch-apps»), and that plural for a set that includes an app without a Watch app; «rusthartslag» («hartslag in rust»);
«uitgelicht door de App Store-redactie» (Apple NL badge: ‘Keuze van de redactie’); «gokspel» for a guessing game («raadspel»);
«veel anderen» for "many also"; «laat X oefenen» without an object; «pakken het op» for "reach for it"; «een verstandig pad»; «mobiel»
for a hanging mobile («hangmobiel»); «5.000» (four digits take no dot); «Let op:» as a disclosure («Transparantie:»); Dutch store
titles replacing competitor names (English name, store title once); keywords not from the research file; «geen enkel antwoord» for "no
single answer"; a maker's name dropped as if the no-name rule covered everyone (it covers only the site owner). Hubs and llms lines: «reeksendruk» and other «-druk» coinages; «zet X naast Y» for “compares” («vergelijkt X met Y»); «zet … bij elkaar» («combineert»); «registreert al je …» («al» reads as “all”); «aftellers» («aftelling»); «voorlopig» or «nog alleen in het Engels» on hubs (a roadmap hint); «In het Nederlands staan …» with no location («zijn er»); one verb three times in a sentence; hub cards ending in «, met bij elke app …». Batch 2: «het diepe einde» («in het diepe springen»); «en die verdient de app» («en terecht»); «matchmaking in real time» («live matchmaking»); «snelle bedenktijden» («korte bedenktijden»); «wedlopen om aan te vallen»; bare «rekening(en)» for bank accounts on a bills page («bankrekening»); heading fragments; «in privé»; an added definition in brackets in a hero lead; «de app van wie deze gids publiceert»; «startscherm» copied from a listing («beginscherm»); «volledig gericht op» overstating a listing; the check date repeated in every section lead. Compound with -je + app: «huishoudboekje-app» (hyphen for readability, as «takenlijst-app»).

From the Tier 4 reviews (2026-11-19): «databrokers» (Apple NL «datahandelaars»); «advertentiemeting» («het effect van reclame meten»);
intransitive «levens vullen aan»; «inruilen» for watching an ad; «blijft plakken»; «beveiliging» for a guard («waarborg»); «meetellen»
for "fit"; «Of je nu koopt of niet»; meta sentences about what a source does not say, or phrased so they read like a rule; «Themaankopen»
(«thema-aankopen»); mixed «hrv»/«HRV» (always «HRV», «HRV-…»); «ziekelijk» for pathological («geen teken van ziekte»); «resterende
verstoring» («residuele confounding»); «banden» for categories («indeling»); «nog steeds» for "still" where Dutch says «al»; «Geen van
allen» for things («Geen ervan»); «de enige die» for "the one that"; near-verbatim copies of Apple or government sentences; «maximaal
maakt»; «schrappen» for cutting sets («minder», «verminderen»); «klopte» for "beat"; «fysiek» / «fysiekatleten» for physique sports
(«bodybuilding»); «triggers» («aanleidingen»); «spreiding» for a range («bereik», «uiteenlopend van»); «één-herhalingsmaximum» and
«X-herhalingenmaximum» (1RM, 5RM after one gloss); a decimal comma inside a comma list («1, 1,5, 2»: «anderhalve minuut»); «Deload week»
split in visible text («deloadweek»); «lifters» («krachtsporters»); straight apostrophes; «data» for datums (again); bare «afhaal»
(«afhalen»); «uit reflex» («uit gewoonte»); «is waar X»; «niet-kern» as a noun («niet-kernvaccin»); «verzwakt levend» («levend
verzwakt»); a currency note repeated; «vast bedrag» for a load step («vaste stap»); «terugschakelen» for a weight reset («teruggaan in
gewicht»); «afdrijven» for drifting estimates («uit elkaar lopen»); «Welke je ook …» for "whichever"; «vastpinnen» («klem komen te
zitten»); «rond een blessure trainen» («om een blessure heen»); «uitlopen» for "finish" («afmaken»); «verantwoording» for gym
accountability («stok achter de deur»); visible «push pull legs schema» and «upper lower» («push pull legs», «upper/lower»); «haar» for
a formula. Wiring (hub, llms lines, links): hanging-hyphen compounds for English names («een push pull legs- of upper/lower-schema»: «een schema als push pull legs of upper/lower»); hub fragments («Verder over X»); «vragen» for a legal requirement («nodig hebben», «vereisen»); «tot 3 à 5»; an imperative opening an llms reason («het artikel adviseert …»); «grote studies» for one named meta-analysis; a link sentence tacked on with a semicolon. Quoted UI text keeps iOS's grouping («nog 2.026 stappen tot ontgrendeling»); the «8000» rule is for our own prose.

From the Tier 3 reviews (2026-11-19): a raw search form as an FAQ question («Tricount hoe werkt het»: «Hoe werkt Tricount»); «liever X dan … te + infinitive» (parallel verbs: «dan bonnen scant»); «hen» as indirect object («hun»); «Één» at the start of a line («Eén»); «scannen tot artikelen» («scannen en in artikelen opdelen»); «met Apple Intelligence aan» («waarop Apple Intelligence aanstaat»); «een Nederlandse variant» for a competitor (a nationality claim no listing makes); cross-references inside FAQ answers (schema answers stand alone); hedged links («zoek je misschien liever bij»); «we» on a page whose English has none («Dyme hebben we niet getest»: «… heeft Dyme niet getest»); a price range that skips rows; «ze»/«Ze» for an app in store lines («de app», «de productpagina»); «er wordt niets naartoe gestuurd» for "never sent anywhere" (reverses it: «stuurt … nergens heen»); «in groep» (Flemish: «samen met»); «Geen vermeld» («Niet vermeld»); main-clause order in bullets that continue an «als je…» lead (verb last); «de eigen servers» with an unclear owner («de servers van X»); «X betaal je … levenslang» («als levenslange aankoop»); «afhankelijk van de periode» for in-app rows without a period («Voor welke periode elk bedrag geldt, staat er niet bij»); «het alternatief» for "an alternative"; two pages in one batch with the same description opening; staged questions in H1 or seo.title («Op zoek naar …?», «Forest-app gratis? …»). Wiring (hub, llms lines, app-page links): «zet/staat X tegenover Y» for "compares" («vergelijkt X met Y»); «bewegingsdoel» for EarnLock’s goal (Apple’s Move ring: «activiteitsdoel»); «splitst één bon» (you split a «rekening» and read a «bon»); «X is logischer als» («past beter als»); card reasons not on the page («een timer om te studeren»); «loopt het punt voor punt door» («staan de verschillen punt voor punt»); «bankgegevens aan een app van een derde geven» where the page only says the app links bank accounts; llms queries not in the research evidence column.

Translationese: split compounds, title case headings, u and je mixed, English word order with the verb not at the end
of a subordinate clause, «maken» calques («een verschil maken», «zin maken»: write «zinvol zijn»), «dat gezegd
hebbende», «aan het einde van de dag», gerund chains («biedend», «makend»), «gebruiker» everywhere where Dutch says
«je» or «wie», «de» before app names, Flemish vocabulary (gsm, plezant, efkes, «ge»).

## Legal terms for a Dutch lawyer (from the privacy reviews)

Consent formed by purchase («Door een aankoop te doen, ga je ermee akkoord dat wij … mogen antwoorden»); «verwerken»,
«persoonsgegevens», plain «wij» instead of «verwerkingsverantwoordelijke»; «niet bewust verzamelen»; «niet gericht op
kinderen jonger dan 13 jaar» (the Dutch digital-consent age is 16, UAVG art. 5); «ingangsdatum»; «wezenlijke wijzigingen»;
Pulse's rights list («inzage, correctie of verwijdering», GDPR Dutch: rectificatie, wissing, beperking, bezwaar) and
«gegevensbeschermingsautoriteit waar je woont» (GDPR: toezichthoudende autoriteit; NL: Autoriteit Persoonsgegevens);
«Apple treedt op als opslagaanbieder» (verwerker?); Clippet terms: «zoals het is» / «zoals beschikbaar», «verhandelbaarheid»,
«geschiktheid voor een bepaald doel», «indirecte, incidentele, bijzondere, gevolg- of punitieve schade», the 12-month cap,
«met uitsluiting van de Finse regels van internationaal privaatrecht (conflictregels)», «dwingend consumentenrecht»,
«ter beoordeling van Apple», «niet-verbruikbare aankoop».

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
| /nl/, /nl/apps/, `_data/i18n_transparency/nl.yml` | 2 Sonnet writers | 1 reviewer (about 45 fixes; Apple NL privacy-label and IDFA terms verified) | home: 4 meaning shifts fixed | no native review yet |
| 21 app pages (Clippet unlisted) | 21 Sonnet writers | 10 reviewers (1 to 4 pages each), catalog checks of every quoted label | all 21: meaning shifts fixed on 19 pages (dropped hedges and qualifiers, Family Sharing scope, outcome claims, Memories vs Reminders on Soon., the HEIC claim on MediaKit, an unsupported "best" title on Tare, added keyword sentences); none on Mockly and AppMeta Pulse beyond wording | no native review yet |
| 21 support pages | 2 Sonnet writers | 1 reviewer (descriptions rewritten to match the questions the layout picks, simulated in Ruby) | n/a | no native review yet |
| 21 privacy policies + Clippet terms | 6 Sonnet writers | 6 reviewers, sentence by sentence, then a main-session sweep for one consent sentence, «jonger dan 13 jaar», «niet gericht op» | n/a | no native review yet |
| about, support hub, transparency | 3 Sonnet writers | 1 reviewer (an added Settings sentence removed from transparency) | about: 3 meaning shifts fixed | no native review yet |
| /nl/llms.txt, /nl/llms-full.txt | 1 Sonnet writer | 1 reviewer (every reason checked against the reviewed Dutch page) | n/a | no native review yet |
| Tier 2 batch 1: chess, logic, workout, xiangqi guides, 3 audience pages | 7 Sonnet writers | 2 reviewers (all Dutch competitor prices checked against the saved Dutch store pages; Taskful Day «in totaal maximaal 50 taken»; maker name and US-listing caveat restored) | n/a | no native review yet |
| Tier 2 batch 1: local-only screen-time guide | 1 Sonnet writer, sources saved | 1 reviewer, both Apple NL iOS 27 pages re-fetched, claim by claim (invented «alleen» condition and a dropped iOS 27 sharing condition fixed) | n/a | no native review yet |
| Tier 2 batch 1: both hubs, llms lines, EarnLock FAQ link | 1 Sonnet writer + main session | 1 wiring reviewer | n/a | no native review yet |
| Tier 2 batch 2: shogi, bill-tracker guides | 2 Sonnet writers | 1 reviewer (every Dyme, Wallet and Spendee sentence checked against its Dutch listing; Wallet price without period removed; shogi language column and Shogi Wars offline from the listings) | n/a | no native review yet |
| Tier 2 batch 2: local-only countdown guide | 1 Sonnet writer, sources saved | 1 reviewer, three Apple NL iOS 27 pages re-fetched (two dropped Stand-by conditions restored) | n/a | no native review yet |
| Tier 4 batch 1: 9 journal posts | 9 Sonnet writers (Dutch sources saved for steps, strength program and vaccinations) | 5 reviewers, two posts each (copy-editing, fact diff, every converted or recomputed number, live re-fetch of every Dutch source, UI strings from the catalogs) | n/a | no native review yet |
| Tier 4 batch 1: local-only mkv-naar-mp4 | 1 Sonnet writer, sources saved | 1 reviewer (four sources re-fetched; an unsupported subtitles sentence removed; MediaKit strings from the catalog) | n/a | no native review yet |
| Tier 4 batch 1: hub, llms lines, inbound links | main session | 1 wiring reviewer | n/a | no native review yet |
| Tier 3 batch 1: tricount, splitwise, whoop, oura, chess-com, forest, hevy, pdf-expert | 8 Sonnet writers | 2 reviewers (full copy-editing skill; every competitor price, rating and date checked against the Dutch store file; titles made distinct; Premium price range on PDF Expert corrected; a reversed privacy sentence on Forest fixed) | n/a | no native review yet |
| Tier 3 batch 1: local-only wiebetaaltwat-alternatief, dyme-alternatief | 2 Sonnet writers (listings only) | reviewed with the batch (every WieBetaaltWat, Tikkie and Dyme fact against the Dutch listing; user count attributed; no safety judgement on Dyme) | n/a | no native review yet |
| Tier 3 batch 1: hub, llms lines, app-page and guide links | main session | 1 wiring reviewer | n/a | no native review yet |

## Apps still on English screenshots

AppMeta, MediaKit and Mockly (2026-11-19: no `nl` folder in `assets/screenshots/<slug>/`). The other 18 apps already
have `nl` sets from commit 763463c («localized sets for 16 languages»), although the owner's brief said "none yet".
