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

## Screenshots

`assets/screenshots/<slug>/it/` already holds complete Italian sets for 19 apps (from commit 763463c, «localized sets
for 16 languages»), so their pages and OG cards show Italian screenshots. Apps still on English screenshots:
**MediaKit and Mockly** (no `it/` folder). Mockly has no Italian interface, so an Italian set cannot exist for it.
