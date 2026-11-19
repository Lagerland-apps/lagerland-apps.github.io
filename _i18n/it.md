# Language sheet: Italian (it), Italy

Never published (`_i18n` is excluded from the build). Rulebook: TRANSLATION.md. Read this sheet before writing or
reviewing any Italian page. Every decision a translator would otherwise make differently per page lives here.

## Status

| Item | Status |
|---|---|
| Setup (config default, locales.yml block, `_data/i18n/it.yml`, sitemap and feed stubs) | done 2026-11-19, commit 16a4f41 (it.yml written by one agent, reviewed and copy-edited by another: 59 values changed) |
| Keyword research (Tier 1) | done 2026-11-19 from Google suggest, Bing, App Store hints and the iTunes Search API; Search Console has no Italy query data (see Keyword research) |
| Tier 1 pages | done 2026-11-19, no native review yet: home, apps hub, 21 app pages (Clippet unlisted), 21 support pages, 21 privacy policies + Clippet terms, about, support hub, transparency (+ `_data/i18n_transparency/it.yml`), /it/llms.txt, /it/llms-full.txt, 21 OG cards. Six batch commits, then go-live |
| Live | yes, `live: true` since 2026-11-19 (Tier 1; go-live commit not pushed) |
| Tier 2 | done 2026-11-19 (not pushed). Batch 1 (8cf9a81): both hubs, chess, logic puzzles, workout without subscription, 3 audience pages, local-only /it/guides/limitare-tempo-di-utilizzo-iphone/ and /it/guides/come-mettere-conto-alla-rovescia-iphone/. Batch 2: shogi, xiangqi, bill tracker rewritten around Wallet by BudgetBakers, Spendee and Toshl Finanze (Rocket Money, Monarch, Copilot not sold in Italy). for/indie-ios-developers stays English-only (developers search in English). Research: ~/Downloads/githubcode/it-tier2-research-2026-11-19.md; brief: `_i18n/it-tier2-brief.md` |
| Tier 3 | batch 4 done 2026-11-19 (not pushed): the must-have comparisons left after an Italian demand scan of the 103 untranslated English pages: jefit, strong-workout-app (GymLogger X); hrv4training (Observa); one-sec (EarnLock); documents-by-readdle, xnconvert (MediaKit; XnConvert is a desktop tool, like HandBrake); flow-free, two-dots (Millrace, its first Italian comparisons); rise-sleep-tracker (AfterShift, its first); wikipedia-app, kiwix, wikiwand (WanderWiki, its first; wikiwand.com returned 403, so its plans stay qualitative). Hub 37 with new sections «Giochi di logica», «Lavoro a turni e sonno» and «Wikipedia». No local-only gap (pet-record apps: MyVet is a vet-clinic app, the rest under ten ratings). Research: it-tier3-research-2026-11-19.md § Batch 4 shortlist; store data it-tier3-store-batch4-2026-11-19.md. Remaining English comparisons have weak Italian demand (optional: Countdown Star, AutoSleep, KAMI 2, Gentler Streak, Nonogram Katana). Batch 3 done 2026-11-19 (short batch of five, pushed as 2091b6a): local-only alternativa-a-monefy and alternativa-a-sleep-cycle, wondershare-uniconverter, habitica, alpha-progression; hub 25; store data it-tier3-store-batch3-2026-11-19.md (with Italian App Privacy labels). Batch 2 done 2026-11-19, pushed as 4b80642: handbrake, convertio, cloudconvert (web/desktop tools, owner approved despite 6.4), opal, bevel, welltory, fitbod, settle-up and local-only /it/alternatives/alternativa-a-splid/ and /it/alternatives/alternativa-a-appblock/; hub 20 cards; store data it-tier3-store-batch2-2026-11-19.md. Batch 1 done 2026-11-19, pushed as 94ecf4d: /it/alternatives/ hub + tricount, splitwise, chess-com, lichess, whoop, oura, hevy, forest, pdf-expert and local-only /it/alternatives/alternativa-a-wallet-budgetbakers/ (also closes the Rocket Money part of I-0376 on the AllPaid page). Research: ~/Downloads/githubcode/it-tier3-research-2026-11-19.md (batch 2 queue inside: HandBrake, Convertio, CloudConvert, UniConverter, Splid local-only, Fitbod, Bevel, Opal, Jefit, Welltory, Settle Up, AppBlock local-only); store data: it-tier3-store-2026-11-19.md; briefs `_i18n/it-tier3-brief.md`, `_i18n/it-tier3-review-brief.md` |
| Tier 4 | batch 1 done 2026-11-19 (not pushed): /it/journal/ hub («Blog») + how-many-steps-a-day-to-aim-for, how-long-to-rest-between-sets, how-to-estimate-your-one-rep-max, rpe-and-rir-explained, choosing-a-strength-program-you-will-finish, when-to-deload, how-much-to-tip-in-the-us, apple-watch-hrv-without-a-baseline, puppy-and-kitten-vaccination-schedule (Italy rabies rules from salute.gov.it) and local-only /it/journal/festivita-2027/ (L. 260/1949 as amended, L. 151/2025). Research: ~/Downloads/githubcode/it-tier4-research-2026-11-19.md (next-batch queue inside); briefs `_i18n/it-tier4-brief.md`, `_i18n/it-tier4-review-brief.md` |
| Stale pages | 0 (2026-11-19, `i18n.py stale`); no wording-only changes waiting |
| Native review | none (NATIVE REVIEWER: none). Every page is logged as "no native review yet" |
| Build time | 69.5 s wall before Italian pages; 78 to 81 s with all 69 Italian Tier 1 pages (2026-11-19, clean worktree, other sessions' agents running) |

## Market and register

- Market: Italy. Folder `/it/`, `<html lang="it">`, hreflang `it` (also covers Italian readers in Switzerland and
  San Marino), og:locale `it_IT`, territory ITA, currency EUR.
- Engines (TRANSLATION.md 7.4): Google first, then Bing (also feeds DuckDuckGo, Ecosia, Copilot). Tools: Search
  Console, Bing Webmaster Tools. IndexNow covers Bing and the engines that use it. No market-specific engine.
- **Formality: tu** for one reader; avoid voi (a plural "you") except where the text really speaks to a group, and
  never Lei. Reasons:
  1. TRANSLATION.md 13 default for Italy.
  2. Apple Italy writes tu on every page checked (support.apple.com/it-it guides and articles, apple.com/it,
     apps.apple.com/it: "Tocca" 357 times, "Tocchi" 0, zero Lei imperatives; it-apple-terms.md).
  3. All 20 apps with an Italian interface write tu (it-glossary.md). The one exception is about 60 Observa coaching
     strings in voi (an app-side defect, not a model). So app strings can be quoted as they are.
  Never mix: no Lei/Suo/La addressing the reader, no voi to one reader.
- Gender-inclusive where it costs nothing, as Apple Italy does ("chi usa l’app", "la persona"); never «utente/i» for
  the reader when tu works.

## Typography and punctuation

House rules (TRANSLATION.md 8.3), with the characters to type:

- Quotes: “…” (U+201C/U+201D), as Apple Italy writes UI labels in guides and articles (961 “ ” and 0 « » on 111
  Apple pages). No space inside, punctuation after the closing mark: Tocca “Tempo di utilizzo”. Inner quotes ‘…’.
  TRANSLATION.md 13 says pick « » or “ ” and keep it: the site picks “ ”. A one-word UI label is written bare and
  capitalised (Tocca Abbonamenti); a multi-word label goes in “…”.
- Apostrophe: typographic ’ (U+2019) everywhere in Italian prose: l’app, un’app, dell’App Store, c’è. Never a straight
  '. (YAML: inside double-quoted strings ’ needs no escape.)
- Accents: è (is), é in perché, poiché, né, affinché; più, già, così, può, cioè. Never e', piu', perche'. Capital È
  (never E').
- Menu paths: Impostazioni > [il tuo nome] > Abbonamenti (spaces around >; no arrows →).
- Headings and labels in sentence case: only the first word and proper names take a capital. Store titles in Title
  Case («Puzzle Logico Rilassante») are the store's, not a model.
- No em or en dashes (Apple Italy uses almost none). A range is «da 3 a 5 kg». Lists: «A, B e C» (no comma before
  e/o). Ordinal day: no.
- Numbers: decimal comma (4,8); thousands with a period (100.000; four-digit numbers may stay unseparated: 6005).
  No-break space U+00A0 between a number and €, units: `3,99 €`, `35 °C`, `8 h`, `5 GB`. **Percent takes no space:
  `30%`** (Apple Italy writes «al 30%»). Metric units only.
- Times: 24-hour, «22:30» or «alle 7». Dates in prose: «26 ottobre 2026», months lowercase, «1 novembre» (cardinal,
  as Apple Italy writes «1 ottobre 2026»). Templates use date.html.
- «app» is feminine and invariable: «l’app», «un’app», «le app» (never «apps», never «la app»). «applicazione» once in a
  description or FAQ where the search phrase uses it, never in body copy as a habit.
- App Store after prepositions: Apple Italy's guides write it bare («su App Store», «da App Store», «di App Store»),
  its store pages write «dall’App Store». The site writes it bare: «su App Store», «Scarica su App Store»,
  «disponibile su App Store». l’iPhone/su iPhone, il Mac/sul Mac, l’Apple Watch (masculine), la Dynamic Island
  (feminine), iCloud without article.
- Anglicisms: Italian keeps far more English than French. Keep what Apple Italy and Italian searchers keep: app,
  widget, backup, feedback, privacy, link, online/offline, screenshot (the picture; «schermata» is a screen of an app),
  smart, full immersion (Apple's Italian name for Focus), StandBy, Dynamic Island, Wallet, Apple Account, Game Center,
  App Store Connect, ASO, privacy manifest, App Tracking Transparency, to do list. Use Italian where Italian is normal:
  abbonamento (not subscription), impostazioni, promemoria, allenamento, scheda (gym programme card), conto alla
  rovescia (countdown), appunti (clipboard), sonno.

## Formats (checked 2026-11-19 against the Italian App Store)

Source: the iTunes lookup API (`itunes.apple.com/lookup?country=it&lang=it_it`) for Things 3 (id904237743), Mockly,
LiftLog and Observa, plus the apps.apple.com/it pages and Apple Italy pages read by the glossary and Apple-terms agents.

| What | Format seen | Where | In the site |
|---|---|---|---|
| Price | `9,99 €` (U+00A0 before €), `14,99 €`, raw `2,99&nbsp;€` | Things 3; Mockly; Italian App Store pages | locales.yml `EUR: position after, space U+00A0, decimal ",", group "."` |
| Free app | `Gratis` (and «Acquisti in-app») | LiftLog, Observa and all our free apps | `strings.free: "Gratis"` |
| Thousands | `100.000` | apple.com/it/health | `group: "."` |
| Percent | `30%` (no space) | Apple Italy guides | prose rule above |
| Dates | «1 ottobre 2026», «18 settembre 2026» in running text | support.apple.com/it-it | `date_long "{d} {month} {Y}"`, `day_one "1"` |
| Rating value | decimal comma | App Store | `strings.decimal: ","` |

Price line pattern: `Gratis, Premium da 3,99 €/mese, 24,99 €/anno o 59,99 € a vita` (strings.from «da», per_month
«/mese», per_year «/anno», lifetime «a vita», or «o»). Trial label: `7 giorni di prova gratuita` (AfterShift's paywall:
«7 giorni di prova gratuita»). Zero price on plan cards: `{P_ZERO}` → `0 €`. One-time purchase in prose: «acquisto
unico» (the store and apps also say «una tantum», «acquisto singolo»; the site uses «acquisto unico» and «a vita»).

Note: the Italian App Store shows the developer's personal name and address (seller line). That name never goes on
the site; attribute to "Lagerland Apps".

## Glossary

Companion files: `_i18n/it-glossary.md` (per app: Italian coverage, register, feature names verbatim from the string
catalogs, Italian App Store name and subtitle, tier names, flags) and `_i18n/it-apple-terms.md` (Apple Italy's own
names, each with its Apple source URL). Rule: a feature name is written exactly as the app's Italian interface shows
it; an Apple product or feature name exactly as Apple Italy writes it.

**Italian interface: 20 of 21 apps.** Every app except **Mockly** has an Italian interface (99 to 100 % of each
catalog, checked 2026-11-19). **Mockly has no Italian localization** (its catalog has de, en, es-ES, es-MX, fr, ja,
ko, pt-BR, tr, zh-Hans; its Italian store page is in English): the Mockly page says plainly that the app's interface
is not in Italian, and no page claims all our apps are in Italian. Gaps to keep off the pages: AfterShift's calendar
permission prompt and Pawza's camera and photo prompts are English only; AllPaid's Siri phrases are English only;
LiftLog has 8 untranslated statistics labels and an English Siri hint; Taskful Day's «End/Extend focus session»
Watch shortcuts fall back to English; about 18 Observa strings are English or half-English.

The terms that matter most across the site:

| English | Italian on the site | Source |
|---|---|---|
| (address) you | tu; never Lei, never voi to one reader | this sheet |
| Download on the App Store (badge) | Scarica su / App Store (Mac: Scarica su / Mac App Store) | Apple badge artwork it-it (tools.applemediaservices.com) |
| Get (App Store button) | Ottieni | Italian App Store |
| Free (price) | Gratis | Italian App Store |
| In-App Purchases | Acquisti in-app | Italian App Store |
| subscription / cancel | abbonamento; Impostazioni > [il tuo nome] > Abbonamenti > “Annulla abbonamento”. Italians search «cancellare», «annullare» and «disdire»: prose may use all three, the button is “Annulla abbonamento” | support.apple.com/it-it/118428, it-keywords.md |
| Request a refund | “Richiedere un rimborso” (reportaproblem.apple.com) | support.apple.com/it-it/118223 |
| Restore purchases | Ripristina acquisti | every app catalog |
| lifetime (purchase) | «a vita» (price line, plan cards: the apps' paywalls say «A vita»); «acquisto unico» in prose | app catalogs |
| Family Sharing | In famiglia (Apple's name, also in every app; the store's «Condivisione in famiglia» is not used) | Apple support, app catalogs |
| Data Not Collected | Dati non raccolti (section «Privacy dell’app») | Italian App Store |
| Health app / Apple Health | l’app Salute / Salute (never «Apple Salute», never «Apple Health» in Italian prose) | apple.com/it/health |
| Heart Rate Variability (HRV) | variabilità della frequenza cardiaca (HRV); Apple Italy keeps «HRV», and so does Observa's Italian UI. Observa: «HRV (SDNN)»; never «VFC» on the site (only Observa's store title says it) | Apple IT, Observa catalog |
| Resting heart rate | frequenza cardiaca a riposo (Watch label “Battito cardiaco a riposo”) | Apple IT |
| Sleep stages | Veglia, REM, Principale, Profondo (Apple). Apps may differ: quote an app's own labels only where the page describes the app | support.apple.com/it-it/108906 |
| VO2 max / Cardio Fitness | VO2 max / tono cardiovascolare | Apple IT |
| Workouts (Apple) | allenamenti (the Watch app is Allenamento) | Apple IT |
| Screen Time | Tempo di utilizzo (Apple; «tempo di schermo» only as the searched common noun) | Apple support, keyword research |
| Focus / Sleep Focus | full immersion / full immersion Sonno | Apple support |
| Home Screen / Lock Screen / widgets | schermata Home / schermata di blocco / widget (invariable) | Apple support |
| Live Activities / Smart Stack / StandBy | attività in tempo reale / raccolta smart / StandBy | Apple support |
| Shortcuts / Wallet | Comandi Rapidi / Wallet | Apple support |
| Settings (iOS / Mac) | Impostazioni / Impostazioni di Sistema | Apple support |
| Apple Account | Apple Account (kept in English, as Apple Italy writes it; never «ID Apple») | Apple support |
| Sign in with Apple | Accedi con Apple | Apple IT |
| App Tracking Transparency | tracciamento; “Richiesta tracciamento attività”; Impostazioni > Privacy e sicurezza > Tracciamento; IDFA = identificativo per gli inserzionisti (IDFA) | Apple IT |
| iCloud sync / backup | sincronizzazione con iCloud / backup su iCloud (switch “Backup iCloud”) | Apple support, app catalogs |
| countdown | conto alla rovescia (Soon.'s word, 65 strings) | Soon. catalog, keyword research |
| clipboard | appunti; «cronologia appunti» (never «appunti» alone in titles: it also means lecture notes) | Clippet catalog, keywords |
| Journal (section) | Blog (hub title, nav, feed); URLs stay `/it/journal/`. «Diario» reads as a personal diary | it.yml 2026-11-19 |
| stamp sheet (design metaphor) | foglio (di francobolli): «Foglio 2025-{year} · Emesso in Finlandia» | it.yml 2026-11-19 |
| privacy manifest | «privacy manifest» (Italians search the English; Apple Italy has no consumer term) | it-keywords.md |
| support (help) | assistenza («Assistenza» in nav; support pages «X: assistenza e contatti») | it.yml |

Per-app tier names follow each app's Italian UI (it-glossary.md): Premium for AfterShift, Observa (the English site
says Pro), Soon., Shogiful, Xiangqiful, WanderWiki, EarnLock; Pro+ for RightSplit; Pro for AllPaid, AppMeta,
MediaKit, Pawza («Pawza Pro»), Taskful Day, GymLogger X; Clippet Pro. Exception carried over from the owner decision
of 2026-11-08: **Chessful's tier is Pro** on every language page (as in the store IAP names), although the app UI
still says Premium. AppMeta Pulse has no tier name (the whole app unlocks). LiftLog's one-time tiers: **Equo,
Buono, Generoso, Mecenate** (store IAP names; the app says «Bene» and «Sostenitore» for the second and fourth, an
app-side mismatch). Tare's unlock: «Capitoli II–X» (settled, never flagged). Millrace: free, with one-time packs.

Italian App Store names (they differ from English except AppMeta and Mockly):

| App | Italian store name | Italian subtitle |
|---|---|---|
| AfterShift | AfterShift: Sonno & Turni | Recupero, riposo e fatica |
| AllPaid | AllPaid – Gestione Bollette | Paga in tempo, senza stress |
| AppMeta | AppMeta for App Store Connect | ASO, metadati e recensioni |
| AppMeta Pulse | AppMeta Pulse: Vendite di app | Risposte IA alle recensioni |
| Chessful | Chessful: Allena & Analizza | Coach scacchi: tattica, puzzle |
| EarnLock | EarnLock: Blocca App e Focus | Benessere digitale e passi |
| GymLogger X | GymLogger X: Tracker Palestra | Allenamento Forza & Palestra |
| LiftLog | LiftLog: Scheda Palestra | Serie, ripetizioni & forza |
| MediaKit | MediaKit: Comprimi e Converti | Video, Audio, Immagini e PDF |
| Millrace | Millrace: rompicapo di numeri (owner check: the English is "Tile Delivery Puzzle") | 64 livelli, un solo ingresso |
| Mockly | Mockly: Screenshot Maker (listing in English) | none |
| Observa | Observa: VFC, Recupero & Score | Sonno, Ciclo, Coach Prontezza |
| Pawza | Pawza: Salute del Cane e Gatto | Libretto, vaccini e promemoria |
| RightSplit | RightSplit: Dividi Conto Spese | Scansiona scontrino con amici |
| Shogiful | Shogiful: Scacchi giapponesi | Shogi: tattica e analisi IA |
| Soon. | Soon. Giorni ai Grandi Eventi | Matrimonio, Viaggio & Bebè |
| Tare | Tare: Puzzle Logico Rilassante | Rompicapo con Pesi Nascosti |
| Taskful Day | Taskful Day: Pianificatore | Lista Attività & Focus |
| WanderWiki | WanderWiki: scopri e impara | Fatti, storia e curiosità |
| Xiangqiful | Xiangqiful: Scacchi Cinesi | Impara lo xiangqi: tattica, IA |
| Clippet (unreleased) | Clippet: Gestore Appunti (prepared listing) | Copia e incolla con cronologia |

The site writes the app name alone (`name` is never translated); the store name and subtitle are vocabulary hints.
Store wording that the site does not copy: «VFC» (Observa), «Cane e Gatto» as the whole scope (Pawza covers more
animals), «numeri» (Millrace).

## Keyword research

Full notes, sources and FAQ-style questions per page: `_i18n/it-keywords.md` (Google suggest hl=it gl=it, Bing
qsonhs mkt=it-IT, App Store search hints for the Italian storefront 143450-7,29, iTunes Search API country=it,
2026-11-19, about 1,700 requests). Every query below came from one of those sources.

Search Console for Italy: Claude in Chrome was not connected this session and the only export on disk is from
July 2026 (country totals only: Italy 9 clicks, 1,432 impressions in three months, no Italy query list). Revisit 4 to
6 weeks after go-live with the page filter `/it/` and the country filter Italy.

`seo.title`, the H1 and `quick_answer` of each page are written for its primary query.

| Page | Primary query | Secondary queries |
|---|---|---|
| Home (/it/) | `app senza pubblicità` (privacy angle has little demand) | `applicazioni senza pubblicità`, `app privacy iphone` |
| Apps hub (/it/apps/) | `migliori app iphone` | `app utili iphone`, `app indispensabili iphone`, `migliori app mac` |
| About (/it/lagerland-apps/) | none with demand: brand-led («Lagerland Apps» + «sviluppatore indipendente») | `sviluppatore app ios` |
| Support hub (/it/support/) | `cancellare abbonamento iphone` (twins «annullare», «disdire») | `ripristina acquisti`, `rimborso app store`, `richiedere rimborso apple` |
| Transparency (/it/transparency/) | `app tracking transparency` (Italians type the English) | `privacy manifest`, `tracciamento app iphone` |
| AfterShift | `dormire dopo il turno di notte` | `non riesco a dormire dopo il turno di notte`, `come recuperare debito di sonno` (never bare «debito di sonno»: a song) |
| AllPaid | `app promemoria pagamenti` | `app scadenze bollette`, `app per ricordare scadenze bollette` |
| AppMeta | `app store connect mac app` (developers search in English) | `aso app store`, `app store connect app` |
| AppMeta Pulse | `app store connect iphone` | `app store connect api`, `app analytics app store connect` |
| Chessful | `app scacchi` (owns the bare word «scacchi») | `analisi partite scacchi`, `imparare scacchi app` |
| EarnLock | `bloccare app iphone` | `tempo di utilizzo iphone`, `app per limitare l’uso del telefono` |
| GymLogger X | `app scheda palestra apple watch` | `app allenamento palestra apple watch`, `app creare scheda palestra` |
| LiftLog | `app diario allenamento palestra` | `app palestra senza abbonamento` (only LiftLog may say it), `app per segnare pesi palestra` |
| MediaKit | `comprimere video iphone` | `comprimere pdf iphone`, `convertire video in mp4 iphone` |
| Millrace (never write the number title) | `giochi di logica iphone` | `giochi di logica senza pubblicità`, `giochi puzzle iphone` |
| Mockly | `screenshot app store` (developers type the English) | `app store screenshot generator`, `mockup app store`, `app store screenshot maker` |
| Observa | `hrv apple watch` | `variabilità della frequenza cardiaca`, `app sonno apple watch`, `hrv valori normali` |
| Pawza | `libretto sanitario cane` (the page must not suggest Pawza replaces the official booklet; say only what the English page says) | `libretto sanitario cane digitale`, `libretto sanitario gatto`, `app libretto sanitario cane` |
| RightSplit | `app per dividere il conto` | `app per dividere il conto al ristorante`, `dividere il conto alla romana`, `app per dividere le spese` |
| Shogiful | `shogi` | `scacchi giapponesi`, `shogi regole`, `come si gioca a shogi` |
| Soon. | `conto alla rovescia iphone` | `widget conto alla rovescia`, `app conto alla rovescia`, `countdown iphone` |
| Tare | `giochi rompicapo iphone` (the logic-puzzle head terms go to Millrace) | `giochi offline iphone`, `giochi rilassanti iphone`, `giochi senza pubblicità iphone` |
| Taskful Day | `app to do list` (Italian «lista attività» has no demand) | `app per organizzare la giornata`, `app per pianificare la giornata`, `agenda giornaliera app` |
| WanderWiki | `wikipedia casuale` | `wikipedia pagina casuale`, `wikipedia a caso`, `app wikipedia` |
| Xiangqiful | `scacchi cinesi` | `xiangqi`, `scacchi cinesi regole`, `come si gioca a scacchi cinesi` |
| Clippet (unreleased, unlisted) | `cronologia appunti iphone` | `cronologia appunti mac`, `clipboard manager mac`, `gestore appunti` |

Tier 2 (2026-11-19, from it-tier2-research-2026-11-19.md). Guides own the «migliore/migliori» list and how-to queries;
app pages keep the app queries (Tare gave up `migliori giochi rompicapo iphone`, GymLogger X `app scheda palestra gratis`,
EarnLock `tempo di utilizzo iphone`).

| Page | Primary query | Secondary queries |
|---|---|---|
| /it/guides/ | `guide app iphone` (brand-led hub) | the five guides' primaries |
| /it/for/ | none (hub) | `lavoro a turni e salute`, `migliore app salute apple watch`, `migliori app produttività iphone` |
| best-chess-apps-iphone | `migliore app scacchi iphone` | `migliori app scacchi gratis`, `migliore app per imparare scacchi`, `migliore app scacchi offline` |
| best-logic-puzzle-games-iphone | `migliori giochi di logica iphone` | `giochi di logica iphone gratis`, `migliori giochi rompicapo iphone gratis`, `giochi di logica adulti app` |
| workout-app-without-subscription | `app palestra gratis senza abbonamento` | `app scheda palestra gratis`, `migliore app scheda palestra gratis`, `app allenamento palestra gratis` |
| for/shift-workers | `lavoro a turni e salute` | `lavoro su turni e sonno` (the page does not answer night-work health risks, so `lavoro notturno fa male alla salute` is not targeted) |
| for/apple-health-power-users | `migliore app salute apple watch` | `app monitoraggio salute apple watch`, `app sonno apple watch gratis` |
| for/calm-productivity | `migliori app produttività iphone` | `app per organizzarsi la vita`, `app per combattere la procrastinazione` |
| local-only limitare-tempo-di-utilizzo-iphone | `come limitare il tempo di utilizzo di un app su iphone` | `tempo di utilizzo iphone`, `come ridurre il tempo di utilizzo del telefono iphone`, `app per smettere di guardare il telefono` |
| local-only come-mettere-conto-alla-rovescia-iphone | `come mettere un conto alla rovescia su iphone` | `come aggiungere un conto alla rovescia su iphone`, `conto alla rovescia widget iphone` |
| best-shogi-apps-iphone (batch 2) | `shogi online` (bare `shogi` stays Shogiful's) | `shogi online gratis`, `shogi gioco`, `shogi giapponese`, `shogi app iphone` |
| best-xiangqi-apps-iphone (batch 2) | `xiangqi online` (`scacchi cinesi`, `xiangqi` stay Xiangqiful's) | `xiangqi app`, `xiangqi gioco`, `xiangqi regole`, `xiangqi play ok` |
| bill-tracker-without-bank-connection (batch 2) | `migliore app per scadenze pagamenti` (AllPaid keeps `app promemoria pagamenti`, `app scadenze bollette`) | `app scadenze pagamenti`, `app promemoria scadenze pagamenti`, `gestione abbonamenti app iphone`, `app per spese fisse` |

Tier 3 batch 1 (2026-11-19). Comparison pages own the competitor-name queries; app pages keep the app queries.

| Page | Primary query | Secondary queries |
|---|---|---|
| /it/alternatives/ | brand-led hub | the pages' primaries |
| tricount | `alternativa a tricount` | `tricount come funziona`, `tricount gratis`, `meglio splitwise o tricount` |
| splitwise | `alternativa a splitwise` | `alternativa a splitwise gratis`, `app alternativa a splitwise` |
| chess-com | `alternativa a chess com` | `chess com come funziona`, `chess com app gratis` |
| lichess | `meglio lichess o chess com` | `lichess come funziona`, `lichess o chess com` |
| whoop | `alternativa a whoop senza abbonamento` | `alternativa a whoop`, `whoop senza abbonamento`, `whoop o apple watch` |
| oura | `oura ring senza abbonamento` | `oura ring abbonamento costo`, `oura ring alternativa`, `meglio oura o whoop` |
| hevy | `hevy app come funziona` | `hevy app gratis`, `hevy app recensioni` |
| forest | `forest app come funziona` | `forest app per studiare`, `forest app è gratis` |
| pdf-expert | `pdf expert gratis` | `pdf expert è gratis`, `pdf expert per mac` |
| local-only alternativa-a-wallet-budgetbakers | `wallet budgetbakers recensioni` | `wallet budgetbakers è sicuro`, `wallet budgetbakers costo`, `spendee o wallet` |
| handbrake (batch 2) | `handbrake come funziona` | `handbrake cos'è`, `alternativa a handbrake`, `handbrake gratis` |
| convertio (batch 2) | `convertio opinioni` | `alternativa a convertio`, `convertio gratis`, `convertio online gratis` |
| cloudconvert (batch 2) | `cloudconvert è gratis` | `cloudconvert italiano gratis`, `cloudconvert gratis online` |
| local-only alternativa-a-splid (batch 2) | `splid come funziona` | `splid app`, `splid online` |
| opal (batch 2) | `come funziona opal app` | `opal app è gratis`, `opal app gratis` |
| bevel (batch 2) | `bevel app costo` | `bevel app recensioni`, `bevel app è gratis`, `bevel app come funziona` |
| welltory (batch 2) | `welltory recensioni` | `welltory italiano`, `welltory gratis` |
| fitbod (batch 2) | `fitbod costo` | `fitbod italiano`, `fitbod opinioni`, `fitbod app gratis` |
| settle-up (batch 2) | `settle up come funziona` | `settle up in italiano`, `settle up gratis` |
| local-only alternativa-a-appblock (batch 2) | `appblock recensioni` | `appblock è sicuro`, `appblock gratis`, `appblock è a pagamento` |
| local-only alternativa-a-monefy (batch 3) | `monefy come funziona` | `monefy è gratis`, `monefy recensioni`, `monefy costo` |
| local-only alternativa-a-sleep-cycle (batch 3) | `sleep cycle app come funziona` | `sleep cycle gratis`, `sleep cycle app gratis`, `sleep cycle premium` |
| wondershare-uniconverter (batch 3) | `uniconverter è gratis` | `uniconverter gratis italiano`, `wondershare uniconverter italiano` |
| habitica (batch 3) | `habitica come funziona` | `habitica italiano` |
| alpha-progression (batch 3) | `alpha progression recensioni` | `alpha progression gratis`; English-form suggests typed in Italy: `alpha progression app`, `alpha progression vs fitbod` |
| jefit (batch 4) | `jefit italiano` | `jefit opinioni`, `jefit recensioni`, `jefit costo`, `jefit gratis`, `jefit app italiano` |
| strong-workout-app (batch 4) | `strong app palestra` | English-form suggests: `strong app apple watch`, `strong app` |
| hrv4training (batch 4) | `hrv4training costo` | `hrv4training gratis`, `hrv4training recensioni`, `hrv4training pro`, `hrv4training apple watch` |
| one-sec (batch 4) | `one sec app gratis` | `one sec app alternative`, `one sec app`, `one sec pro` |
| rise-sleep-tracker (batch 4) | `rise sonno e sveglia` | `rise sleep gratis`, `rise sleep alternative`, `rise sonno`, `rise sleep app` |
| documents-by-readdle (batch 4) | `documents readdle gratis` | `documents di readdle gratis`, `documents readdle`, `documents readdle app`, `documents readdle mac` |
| xnconvert (batch 4) | `xnconvert come funziona` | `xnconvert cos è`, `xnconvert recensioni`, `xnconvert download gratis`, `xnconvert sito ufficiale` |
| flow-free (batch 4) | `flow free gioco` | `flow free gratis`, `flow free online gratis` (the «free flow» hits are motorway tolls) |
| two-dots (batch 4) | `two dots gioco` | `two dots gratis` |
| wikipedia-app (batch 4) | `app wikipedia italiano` | `wikipedia app gratis` (`wikipedia casuale` stays with WanderWiki's app page) |
| kiwix (batch 4) | `wikipedia offline iphone` | `kiwix cos’è`, `download wikipedia offline iphone`, `wikipedia offline kiwix` |
| wikiwand (batch 4) | `wikiwand cos è` | none with Italian phrasing besides `wikiwand italiano`, which the page can’t answer (site returned 403) |

Tier 4 batch 1 (2026-11-19). Journal posts own the informational queries; app pages, guides and comparisons keep theirs.

| Page | Primary query | Secondary queries |
|---|---|---|
| /it/journal/ | brand-led hub («Blog di Lagerland Apps») | the posts' primaries |
| how-many-steps-a-day-to-aim-for | `quanti passi al giorno` | `quanti passi al giorno bisogna fare`, `quanti passi al giorno per stare bene`, `10000 passi al giorno`, `quanti passi al giorno in base all’età` |
| how-long-to-rest-between-sets | `recupero tra le serie` | `tempo di recupero tra le serie`, `recupero tra le serie ipertrofia`, `quanto riposare tra una serie e l’altra` |
| how-to-estimate-your-one-rep-max | `calcolo massimale` | `calcolare massimale`, `formula brzycki`, `formula epley`, `calcolo massimale panca`, `tabella massimale` |
| rpe-and-rir-explained | `rpe e rir` | `rir palestra`, `rpe palestra`, `scala rpe palestra`, `buffer palestra` |
| choosing-a-strength-program-you-will-finish | `push pull legs` | `scheda push pull legs`, `scheda upper lower`, `meglio full body o split` |
| when-to-deload | `settimana di scarico` | `settimana di scarico ogni quanto`, `scarico palestra`, `deload palestra` |
| how-much-to-tip-in-the-us | `mancia in america` | `mancia in america obbligatoria`, `mancia in america quanto`, `mancia negli stati uniti` |
| apple-watch-hrv-without-a-baseline | `hrv bassa` | `hrv bassa cosa significa`, `hrv bassa cause`, `hrv valori normali` |
| puppy-and-kitten-vaccination-schedule | `vaccinazioni cane` | `vaccini cucciolo cane`, `vaccinazioni cane obbligatorie`, `vaccini gattino` (Pawza keeps `calendario vaccinazioni cane`) |
| local-only festivita-2027 | `festività 2027` | `festività 2027 italia`, `ponti 2027`, `festività 2027 san francesco`, `festività 2027 4 ottobre` |

## Decisions from the Tier 4 reviews (2026-11-19)

- Gym words: «massimale (1RM)» once, then either; «recupero» between sets (LiftLog's own label stays “Timer di riposo”); «scheda» for a
  programme card; «settimana di scarico» («deload» once); RPE and RIR kept, «ripetizioni in riserva» once and «buffer» once, only in
  the RPE post; push pull legs, upper/lower, full body, 5/3/1 in English; «atleti di forza e di bodybuilding» for strength and physique
  athletes; «età allenante» for training age; pounds dropped where the English pairs kg and lb.
- Ranges in prose and tables «da 4 a 6», «tra 6 e 8», never «4-6» or «4 o 8» for a range. U+00A0 between a number and passi, kg, kcal,
  min, ripetizioni, settimane, giorni, $.
- Dollars in the US tipping post: «20 $», decimal comma; «imposta» for sales tax (Italians search «tasse»: kept in seo only).
- Vaccines: disease names from the official Italian WSAVA 2015 translation (cimurro, adenovirus canino, parvovirosi, panleucopenia felina,
  herpesvirus felino tipo 1, calicivirus felino, leucemia felina, “tosse dei canili”); never «adenovirosi», «calicivirosi». Rabies: only
  what salute.gov.it says (compulsory for international movement; Reg. (UE) 576/2013).
- Holidays: 12 national holidays besides Sundays (L. 260/1949 as amended, L. 54/1977, DPR 792/1985, L. 336/2000, L. 27/2024, L. 151/2025);
  ponti only as «guarda il tuo contratto o chiedi al datore di lavoro»; patron days only as the Camera page says; no pay rules.
- Soon.: never say an Italian holiday gets the “Festività” event type (the type is inferred from English title words, I-0295).
- Link sentences from app pages to posts: «l’articolo del blog <link>su …</link>», not «il nostro articolo».

## Decisions from the Tier 1 reviews (2026-11-19)

- Price footnote, one sentence on every page: «I prezzi indicati sono quelli di App Store in Italia; negli altri paesi App
  Store mostra il prezzo nella tua valuta al momento dell’acquisto.» («di App Store italiano» is ungrammatical without
  the article; «in Italia» keeps App Store bare.) «paesi» lowercase.
- Lifetime: plan-card price «{P_LIFETIME} una tantum» (= `strings.once`); in prose «{P_LIFETIME} a vita» or «acquisto
  unico»; plan name «A vita».
- "Cancel anytime" is «Puoi annullare quando vuoi» / «Annulla quando vuoi», never «Annulli» (reads as a Lei imperative);
  same for «Paghi una volta» → «Un solo pagamento». Never «cancella» (= delete).
- «a partire da {TRIAL}» reads as "from at least 7 days": write «che parte con {TRIAL}» / «con {TRIAL} per iniziare».
- «In famiglia» with «funziona con» / «è compatibile con», never «supporta».
- `privacy.data_collection` is «nessuna» (it follows the feminine label «Raccolta dei dati»).
- App Store privacy labels exactly as Apple Italy writes them (it-apple-terms.md, verified section): «Dati non collegati
  a te», «Dati collegati a te», «Dati utilizzati per monitorarti», «Funzionalità delle app»; section «Privacy dell’app».
- One-word UI labels bare and capitalised (Annulla, Sorprendimi); multi-word labels in “ ”; feature or module names
  that read as proper nouns (Blocco app, Incolla rapido) may stay bare.
- «X è in italiano?» FAQs answer from the coverage line only: no store name, no list of English-only gaps.
- Founder lines: «Sviluppatore Apple indipendente · Finlandia · studio di una sola persona dal 2025» / «Studio
  indipendente di app Apple · Finlandia». Never «studio Apple». A one-person studio speaks as «lo studio» or in the
  passive; «noi» only where the English says "we".
- Support pages: «<App>: assistenza e contatti». The support hub H1 is «Assistenza, abbonamenti e rimborsi» (the
  keyword stays in seo.title).
- Observa: «Prontezza» capitalised as the app's feature name; HRV feminine («HRV avanzata»); «tono cardiovascolare»;
  Apple's sleep stages where the page describes Salute, AfterShift's own (Leggero, Profondo) where it describes the app.
- Shogiful: drops follow the app: «paracadute», «Esercizi di paracadute», «Errore di paracadute», explained once per page.
- Taskful Day: carry-forward is «Sposta a oggi» (app string) or described; Inbox described as «la lista per le
  attività senza giorno»; check-ins are «verifiche» (app string).
- Pulse: Proceeds «Ricavi», Revenue «Fatturato». AppMeta: the App Store Connect key path as AppMeta's Italian onboarding
  writes it, «Utenti e accesso > Integrazioni > App Store Connect API» (Apple's Italian Help is not available).
- Soon.: «Apple Weather», as the app's Italian string says (Apple's own app is «Meteo»; the privacy page says «Meteo di
  Apple (WeatherKit)»).
- Mockly: its English UI labels are quoted in English; the page says once, plainly, that the interface is not in Italian.
- Privacy pages: «Informativa sulla privacy di <App>»; «trattare / trattamento», «raccogliere», «consapevolmente»,
  «terze parti», «dati personali» (for "personal data" and "personal information"), «sincronizzazione con iCloud», «in
  locale», «una quantità limitata di dati», «Per impostazione predefinita», «Possiamo aggiornare…», «Ogni modifica
  sarà riportata in questa pagina», refund clause «Effettuando un acquisto, accetti che possiamo…» and «se preferiremmo
  che Apple approvasse o rifiutasse il rimborso»; Finland's authority «l’Ufficio del Garante per la protezione dei dati
  della Finlandia (Tietosuojavaltuutetun toimisto)»; Apple's EULA «Contratto di Licenza per utenti finali per le
  Applicazioni concesse in licenza (“Contratto EULA Standard”)».
- Legal terms to show an Italian lawyer when one is available: consent bundled with a purchase (refund clause, GDPR art.
  7(4)); «minori di 13 anni» kept from English although Italy's age of digital consent is 14 (art. 2-quinquies Codice
  privacy); no «titolare del trattamento», legal bases, retention, rights under artt. 15–22 or Garante complaint in the
  English policies, so none in Italian; Pulse «è responsabile dei dati personali» (could read as «responsabile del
  trattamento»); AppMeta's transfers to AI providers outside the EU; Clippet terms: «così com’è», «secondo
  disponibilità», «commerciabilità», «idoneità a uno scopo particolare», punitive damages, art. 1229 c.c.

## Local competitors (for Tier 3)

Not researched yet. Candidates seen in the iTunes Search API results during keyword research are listed in
it-keywords.md per page (for example Blocus for EarnLock, Billo for AllPaid).
Tier 2 research (2026-11-19) adds: Italian roster apps Supershift (★10 768), Calendario di Lavoro per turni (★9482) and
Tabella Turni Facile (★7008) for AfterShift; Italian budget apps for the bill-tracker rewrite: Gestione delle spese by Orange
Dog (★18 135), Monefy (★7028), Spendee (★4167), Wallet by BudgetBakers (★2883; its Italian listing names «Aggiornamenti automatici dalla banca» as a Premium feature, checked 2026-11-19).

## Tells to cut in Italian (TRANSLATION.md 8.2, plus what reviews find)

Stock phrasing: «Nel mondo frenetico di oggi», «Nell’era digitale», «Immergiamoci», «Scopriamo insieme», «È importante
notare che», «Vale la pena sottolineare», «fondamentale» and «cruciale» everywhere, «un vero e proprio», «In
conclusione», «In definitiva», «non solo … ma anche», «Che tu sia … o …», «porta il tuo … al livello successivo»,
«potenziare», «ottimizzare» everywhere, «un’esperienza fluida», «senza soluzione di continuità», «rivoluzionario»,
«in modo efficiente», «a 360 gradi», «game changer», «perfetto per chi».

Translationese: title case headings; English word order (adjective before noun where Italian puts it after);
needless anglicisms where Italian has the normal word («subscription», «setting», «task» in prose); possessives on
devices and body parts copied from English («alza la tua mano»: «alza la mano»); «supportare» for "support a feature"
(«funziona con», «è compatibile con»); «fare senso»; «giocare un ruolo»; «a livello di»; «andare a + infinitive»
filler («andrai a registrare»); «utente» everywhere where Italian says tu or «chi»; chains of gerunds copied from
English -ing; «Lei» forms or voi to one reader; straight apostrophes; « » quotes against the sheet's “ ”.

Found in the Tier 1 reviews (2026-11-19): tu indicatives that read as Lei imperatives («Annulli quando vuoi», «Paghi una
volta»); keyword nouns in apposition («un’app scacchi», «App HRV per Salute», «un’app to do list»); keyword-then-colon
H1s; gendered address («Sei uno sviluppatore?», «Bloccato?», «ti sei svegliato», «Sei stanco», «crei da solo»); team
«noi» on a one-person studio («Scrivici», «ci aiutano»); «per costruzione» ("by construction": «fin dal progetto»);
«provata» for "proven" («dimostrata»); «registrazione» for logging next to «nessuna registrazione» (sign-up);
«analisi» for analytics where Analisi is an app feature («strumenti di analisi d’uso»); «mobile» for "rolling"
(«media mobile»); «schermata di blocco» for an app's own block screen (it means Lock Screen); «a livello di sistema»;
«spezzare il legame» (unlink: «scollegare»); days as a subject («i tuoi primi 3 giorni sbloccano»); «da condividere» for
"shared"; «vuole essere» for "is meant to"; «Il lavoro copre»; «registri» for logs; «segue l’assistenza»; «subito» for
"up front"; «anche dove» for "including where"; a bare «Nessuno» after a list of things; «ti legge»; «più la sua…»;
«pagare per le app»; added «solo» or «cioè …» definitions; «Privato per costruzione»; «contamosse»; «serotino»;
«nell’ospitalità»; «quasi sempre» for "usually"; «non vanno da nessuna parte» for "fit nowhere"; «le partite dal vivo»;
«problemi di scacchi consecutivi» («a scacco continuo»); «scambio» for a move-order slip; «centipedoni»; ranges as «7-9
ore» («da 7 a 9 ore»); over-quoting one-word labels; a meta description opening with «Cerchi…?»; slogan add-ons after a
colon in privacy titles («: senza tracciamento»); dropping the defining noun (Tare is a balance game).

Found in the Tier 2 reviews (2026-11-19): «lavorare insieme» for apps that work together («funzionare insieme»); «dormire a
pezzi» («a più riprese»); «un solo buon sonno» («una buona dormita»); «come ti sta trattando»; «fare chiamate di rete»
(«effettuare connessioni di rete»); «l’analisi si fa» («avviene»); «la scadenza» for a countdown; «non facciamo promesse»
for "make no claims"; quoting one-word tab names (“Oggi”); «paramedici» («soccorritori»); bare «serie» for a streak
before «serie di giorni consecutivi» has been said once; raw-keyword seo.titles («Migliore app salute Apple Watch:»);
«per uso» in titles; «port» for an app version; «bolletta del server»; «non ti sono rimasti addosso» ("didn't stick");
«e basta» for "only"; a meta description opening with a keyword question; «quasi tutto» / «chi migliora … di solito» for
"most"; an Italian store title used as the product name (write the English name, the store title once); «cambia quello
che costa aprire» («rende più faticoso aprire»); «saltare i limiti»; «usare “Usa …”» (Apple's verb «attiva»); «non lo
supponiamo»; «Apple propone» for Apple's «ad esempio, puoi…»; added softeners on competitor claims («con facilità»);
«una app»; «del gruppo» for a set that includes our own app; one-line closers after a card; «portare avanti» for
carry-forward («sposta a oggi»); «a vita a {price}» («a vita per»); «per ora» / «non ancora in italiano» (an implied
translation promise); masculine plural job nouns as an audience («Infermieri, soccorritori»: «chi lavora in corsia o in
ambulanza»). Writers also missed U+00A0 before € and saved empty 301 stubs from apps.apple.com (use `curl -sL` with a
full Safari UA). Batch 2 reviews: «casuale» for "casual" («informali»); «nata attorno a» ("designed around"); «molto
graduati» («graduati con precisione»); «quasi gli stessi pezzi» for "most of the same pieces"; «il tuffo in acque
profonde»; «mettiti in conto» («metti in conto»); indicative after «qualunque» («qualunque app tu scelga»); an acronym used
before it is defined; «Per un’app che …, c’è X» as an opener; a subject switch inside one sentence; «bollette» for both
bills and utilities («utenze» for utilities); «13 000» copied from a listing («13.000»); «a un terzo» («a terzi»); «(nostra)»

Found in the Tier 3 reviews (2026-11-19): «un solo conto non vale la pena di…» (wrong subject); «lingue di scontrino»; «si fa
valere» («dà il meglio»); «di default» («per impostazione predefinita»); «fanno lavori diversi» («servono a cose diverse»);
«vive solo sul telefono» («resta»); «alternativa privata» (reads as privately owned); «manifesto della privacy» or
«Privacy Manifest» («privacy manifest»); Spanish spelling leaks («calcula»); «una tantum» in prose («a vita per»); «da
{P_LIFETIME}» for a single price (reads as "from": «di»); adjective agreement after a plural subject; «Contro X» on related
cards («Confronto con X»); ambiguous pronouns («darle accesso»); «valutazione Elo» for a platform's own rating; a
quick_answer opening with a self-answered keyword question; «Pronto?» / «Provalo» as CTAs («Si parte?», «Provala»: l’app is
feminine); «Su <App>» as a heading («Informazioni su <App>»); «alternativa vicina» («simile»); «con i motivi in vista»; «Può
farlo se…» («Sì, se…»); «sta dietro un abbonamento»; «operazioni di tutti i giorni» for "utility jobs" («operazioni
pratiche»); «ti basta» for "suits you"; «ti conviene di più» for "the better fit" (implies price); «costruito intorno»;
added «sempre»; «per conto suo» («proprie»); «analytics» left in English; «per i membri residenti nell’UE» («per chi
risiede nell’UE»); body lines citing «il confronto in inglese» as a source; pointer sentences in FAQ answers; «noi» on
comparison pages («non li riportiamo», «non abbiamo provato»: impersonal or «Lagerland Apps»); «alternativa a X» keywords
with no suggest evidence.
Batch 2 reviews (2026-11-19): «schermata di blocco» for an app's own block screen (again: «schermata che invita alla
consapevolezza», «schermate per le app bloccate»); «Opal app» / «la Bevel app» («l’app X»); «orari legati all’ora»; gendered
«ti sei mosso», «quanto sei recuperato»; «copre più/meno terreno» («fa più/meno cose»); «gira intorno a»; a price tacked on
after a comma; «Registrazione gratis»; «Oltre 1000» («1.000»); «settimana di prova» for EarnLock's no-block week; «Nessun
abbonamento obbligatorio» on a subscription app's overline; raw «X recensioni, costo e…», «X come funziona?», «X opinioni:»
titles, H2s and FAQ questions; «approfondisce un solo lavoro»; «più privato di X» («protegge la privacy più di»); «batch»
(MediaKit says «in blocco»); a capital after a colon in card labels; scraping artifacts written as facts («non sono visibili
nella pagina»); a trailing «dice la sua scheda»; «Niente X e niente Y»; a comma before «e» in titles; inferred «resta sul
dispositivo» on a competitor; «Cosa fa X che Y non fa» listing features Y also has; app-page queries copied into a
comparison's seo.keywords.
Batch 3 reviews (2026-11-19): «X ti conviene se…» / «quale ti conviene?» on decision cards («Scegli X se…», «quale
scegliere?»); «da 39,99 €» for a listed price (reads as "from"); «cioè …» glosses; «lo trasforma in … HRV» (HRV is read, not
derived); «più conti» where the listing says «più account»; «vivono sui suoi server» («restano»); double-brace tokens
`{{P_…}}` in tables (print blank); added glosses («(la fonte consigliata)»); pointer advice («guarda la schermata di
acquisto»); «Sostituisce, in parte,»; «una alternativa» without elision; two «Come funziona X e un’alternativa…» titles in
one batch.
after an app name («AllPaid, la nostra app,»); «ti legge» for Siri reading items («Siri ti dice …»).


Found in the Tier 4 reviews (2026-11-19): hyphen ranges («6000-8000», «2-4 settimane») and «ogni 4 o 8 settimane» for a range; «di da» before a
range; «confusione residua» («confondimento residuo»); «analisi riunite» for pooled («aggregate»); «di decine di chili» for "double-digit
kilos"; «camminata voluta» («fatta apposta»); «tenere onesto il numero»; «strappare un massimale»; «eri sul telefono»; «atleti di fisico»;
«valuta la fatica» for "how hard it was"; «nel mezzo» for "between them" («tra l’uno e l’altro»); «schede scritte da sé» («fai da te»);
«servizi tipo Uber» (a brand the English doesn't name); «una HRV» (elide: «un’HRV»); «È come…» for "about as useful as"; «servono tutti un
diario» (agreement); gendered «saresti stato bloccato», «parti più leggero», «sei capitato», «stai fermo», «sono un principiante?»; «Quanti
passi al giorno fare?» («Quanti passi fare al giorno?»); «full immersione» («full immersion»); reviewer-facing meta left in copy («non
presa da una fonte consultata», «non le abbiamo verificate»); claims stronger than the source on patron days; bold-label bullet lists; a
keyword-then-colon H1 or a raw keyword-question seo.title; writer-added definitions («Il massimale è…» as its own line); keywords with no
suggest evidence; dropped hedges («circa», «tutto», «all’incirca», «probabilmente»).

Found in the Tier 3 batch 4 reviews (2026-11-19): «dal vivo» for live data or a game's live events («online», «eventi a tempo»);
«fa un altro lavoro» («serve ad altro»); «il lavoro è diverso», «la domanda è dove…» («ti chiedono cose diverse», «devi capire…»);
gendered participles in reader features and competitor facts («ti eri fermato», «ci sei andato vicino», «appena sveglio»:
«riprende dal punto in cui hai interrotto», «subito dopo il risveglio»); «Dove …» as a contrastive opener («Mentre»); «licenza da
15,00 €» when one list price applies; «un’app ricca» («completa»); «un’app curata di debito di sonno» (app + di + noun);
«gestore di file e lettore» («gestore e lettore di file»); «misurazione deliberata» («fatta di proposito»); «tienila» pointing at a
feature instead of the app; «farti ripensarci»; «ti funziona». Process tells: the store's «Compatibilità» line (Mac with Apple chip,
Apple Vision) reported as a competitor's platforms; «la scheda non elenca / non indica …» used to replace an English claim (absence
from a listing is not a contradiction: keep the English claim); «elenca 10 acquisti in-app» (the product page shows at most 10 rows);
listing-internal comparisons narrated in footnotes; invented UI steps for a competitor; a listing sentence copied almost verbatim as
a claim (paraphrase and attribute it); competitor prices in seo.title; a store title used as a seo.keyword; an added verdict with a
dangling pronoun; `&nbsp;` instead of the U+00A0 character (scan JSON-LD too).

## House rules carried over

- No public roadmaps or dated promises. Describe what an app does today.
- Prices only through tokens. No arithmetic on our prices.
- «Senza abbonamento» only for LiftLog, Millrace, Mockly and Tare. For the others «nessun abbonamento obbligatorio»
  or «opzione a vita», where true.
- «Tranquilla» / «calma» and «attenta alla privacy» once, where they state positioning.
- Never the owner's personal name. Attribute to "Lagerland Apps".
- Millrace's copy never mentions the number title it replaced; Observa's HRV is SDNN, never RMSSD.
- App names, competitor names and "Lagerland Apps" as written in English.

## Review log

All Tier 1 pages, 2026-11-19. Writers: Sonnet agents (owner's request), one per page (support pages seven per writer,
privacy policies three or four per writer). Reviewers: separate Opus agents that did not write the pages, running the
full copy-editing skill, a fact diff against the English page, a glossary check against each app's Italian string
catalog and SEO limits. Back-translation by fresh agents that never saw the English, compared claim by claim by the
reviewers: home, all 21 app pages, about. Native review: none yet, for every page (NATIVE REVIEWER: none).

| Pages | Writer | Reviewer | Back-translation | Native |
|---|---|---|---|---|
| interface strings (it.yml) | 1 writer | 1 reviewer, 59 values changed | n/a | no native review yet |
| /it/, /it/apps/ | 2 writers | 1 reviewer | home: 14 shifts fixed | no native review yet |
| 21 app pages | 21 writers | 5 reviewers (4 to 5 pages each) | all 21: about 120 shifts fixed | no native review yet |
| 21 support pages | 3 writers | checked in the gate | n/a | no native review yet |
| 21 privacy policies + Clippet terms | 7 writers | 4 reviewers, sentence by sentence, then one term set applied to all | n/a | no native review yet |
| about, support hub, transparency | 3 writers | 1 reviewer | about: 1 shift fixed | no native review yet |
| /it/llms.txt, /it/llms-full.txt | 1 writer | 1 reviewer | n/a | no native review yet |
| Tier 2 batch 1: 3 guides (chess, logic, workout) | 3 writers (Sonnet) | 1 reviewer; Strong, Hevy, Fitbod euro prices re-fetched and restored | n/a | no native review yet |
| Tier 2 batch 1: 3 audience pages | 3 writers (Sonnet) | 1 reviewer | n/a | no native review yet |
| Tier 2 batch 1: 2 local-only guides (screen time, countdown) | 2 writers (Sonnet), sources saved | 1 reviewer, every Apple page and listing re-fetched, claim by claim | n/a | no native review yet |
| Tier 2 batch 1: both hubs, llms.txt lines, inbound-link sentences | 1 writer (Sonnet) + main session | 1 wiring reviewer | n/a | no native review yet |
| Tier 2 batch 2: shogi, xiangqi guides | 2 writers (Sonnet) | 1 reviewer; Best XiangQi listing re-fetched | n/a | no native review yet |
| Tier 2 batch 2: bill tracker (Wallet, Spendee, Toshl Finanze) | 1 writer (Sonnet), listings saved | 1 reviewer, every listing re-fetched, claim by claim | n/a | no native review yet |
| Tier 2 batch 2: hub cards, llms.txt lines, AllPaid and Xiangqiful link sentences | main session | same reviewer as the bill tracker | n/a | no native review yet |
| Tier 3 batch 1: 9 comparisons + local-only Wallet page | 10 writers (Sonnet), Italian store data from one store-check agent | 2 reviewers (Opus), full copy-editing skill, fact diff against English + Italian store file; every US price and US date removed | n/a | no native review yet |
| Tier 3 batch 1: hub, llms.txt lines, AllPaid / RightSplit / Observa / AppMeta Pulse / bill-tracker link edits | main session | reviewer of group A | n/a | no native review yet |
| Tier 3 batch 2: 8 comparisons + local-only Splid and AppBlock | 10 writers (Sonnet), one store/web-check agent | 2 reviewers (Opus), full copy-editing skill, fact diff vs English + Italian store/web file; App Privacy claims re-checked on the raw Italian product pages | n/a | no native review yet |
| Tier 3 batch 2: hub (20 cards), llms.txt lines, RightSplit / Observa / GymLogger X / screen-time guide links; batch 1 «una tantum» and Forest description fixes | main session | reviewer of group A (batch 2) | n/a | no native review yet |
| Tier 3 batch 3: local-only Monefy and Sleep Cycle, UniConverter, Habitica, Alpha Progression; hub 25, llms.txt lines, Observa and AllPaid links | 5 writers (Sonnet), one store/web-check agent | 1 reviewer (Opus), full copy-editing pass, fact diff vs English + Italian store/web file | n/a | no native review yet |
| Tier 3 batch 4: jefit, strong-workout-app, hrv4training, one-sec, rise-sleep-tracker, documents-by-readdle, xnconvert, flow-free, two-dots, wikipedia-app, kiwix, wikiwand | 12 writers (Sonnet), one store/web-check agent (Sonnet) | 2 reviewers (Opus), full copy-editing skill, fact diff vs English + Italian store/web file, title-pattern check against all 37 comparisons | n/a | no native review yet |
| Tier 3 batch 4: hub (37 cards, 3 new sections), 12 llms.txt lines, Observa / GymLogger X links | main session | 1 wiring reviewer (Opus) | n/a | no native review yet |
| Tier 4 batch 1: 9 journal posts + local-only festivita-2027 | 10 writers (Sonnet), Italian sources saved per post (salute.gov.it, Your Europe, Normattiva, Camera, EpiCentro, Apple Italy) | 3 reviewers (Opus): full copy-editing skill, sentence-by-sentence fact diff, every worked example recomputed, every source re-fetched live, UI labels against the .xcstrings | n/a | no native review yet |
| Tier 4 batch 1: /it/journal/ hub, 10 llms.txt routing lines + Blog lines, link sentences on 7 app pages, GymLogger X anchor | main session | 1 wiring reviewer (Opus) | n/a | no native review yet |

## Screenshots

`assets/screenshots/<slug>/it/` already holds complete Italian sets for 19 apps (from commit 763463c, «localized sets
for 16 languages»), so their pages and OG cards show Italian screenshots. Apps still on English screenshots:
**MediaKit and Mockly** (no `it/` folder). Mockly has no Italian interface, so an Italian set cannot exist for it.
