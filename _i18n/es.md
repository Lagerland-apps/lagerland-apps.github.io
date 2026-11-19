# Language sheet: Spanish (es), Spain

Never published (`_i18n` is excluded from the build). Rulebook: TRANSLATION.md. Read this sheet before writing or
reviewing any Spanish page. Every decision a translator would otherwise make differently per page lives here.

## Status

| Item | Status |
|---|---|
| Setup (config default, locales.yml block, `_data/i18n/es.yml`, sitemap and feed stubs) | done 2026-11-19 (es.yml written by one agent, reviewed and copy-edited by another: 42 values changed) |
| Keyword research (Tier 1) | done 2026-11-19 from Google suggest, Bing, App Store hints and the iTunes Search API; Search Console for Spain not read yet (no access this session) |
| Tier 1 pages | done 2026-11-19, no native review yet: home, apps hub, 21 app pages (Clippet unlisted), 21 support pages, 21 privacy policies + Clippet terms, about, support hub, transparency (+ `_data/i18n_transparency/es.yml`), /es/llms.txt, /es/llms-full.txt, 21 OG cards. Commits 6a83675 (batch 1), ac4a1a3, e6e2231, 3857ea6, cfaed65 (batches 2 to 5), then AI files and go-live |
| Live | yes, `live: true` since 2026-11-19 (Tier 1; go-live commit not yet pushed) |
| Tier 2 | done 2026-11-19 (not pushed). Batch 1 (0cf087a): both hubs, chess, logic puzzles, xiangqi, workout without subscription, 3 audience pages, local-only /es/guides/limitar-tiempo-de-pantalla-iphone/. Batch 2: shogi, bill tracker rewritten around Fintonic, local-only /es/guides/como-poner-cuenta-atras-iphone/. Research: ~/Downloads/githubcode/es-tier2-research-2026-11-19.md. for/indie-ios-developers stays English-only (developers search in English) |
| Tier 3, batch 1 | written and integrated 2026-11-19, no native review yet (not pushed): hub /es/alternatives/ and nine comparisons tricount, splitwise (RightSplit); chess-com, lichess (Chessful); whoop (Observa); hevy (LiftLog); opal, forest (EarnLock); pdf-expert (MediaKit); plus the local-only /es/alternatives/alternativa-a-fintonic/ (AllPaid vs Fintonic). Demand research over all 123 English comparisons: ~/Downloads/githubcode/es-tier3-research-2026-11-19.md (next batch listed there); Spanish store check: ~/Downloads/githubcode/es-tier3-store-2026-11-19.md. Stale check before the batch: 0 pages stale in any language |
| Tier 3, batch 2 | written and integrated 2026-11-19, no native review yet (not pushed): oura, bevel, autosleep (Observa); fitbod, jefit (GymLogger X); settle-up (RightSplit); one-sec, screenzen (EarnLock); habitica (Taskful Day, its first Spanish comparison); plus the local-only /es/alternatives/alternativa-a-appblock/ (EarnLock vs AppBlock). Hub now 20 cards. Research: es-tier3-research-2026-11-19.md § Batch 2 shortlist (next: Welltory, Athlytic, Gentler Streak, Alpha Progression, StrongLifts, Strong, Streaks, Documents, CloudConvert, Wikipedia app); store check: ~/Downloads/githubcode/es-tier3-store-batch2-2026-11-19.md. Stale check before the batch: 0 |
| Tier 3, batch 3 | written and integrated 2026-11-19, no native review yet (not pushed): welltory, athlytic, gentler-streak (Observa); chessable (Chessful); strong-workout-app, alpha-progression, stronglifts-5x5 (GymLogger X); wikipedia-app (WanderWiki, its first Spanish comparison); documents-by-readdle, cloudconvert (MediaKit); plus I-0372 fixed on the chess guide. Hub now 30 cards. Store check: ~/Downloads/githubcode/es-tier3-store-batch3-2026-11-19.md. Next: es-tier3-research-2026-11-19.md § Batch 3 shortlist «Next after batch 3». Stale check before the batch: 0 |
| Tier 3, batch 4 | written and integrated 2026-11-19, no native review yet (not pushed): the must-have comparisons left after batch 3, by Spanish demand: handbrake, convertio, wondershare-uniconverter, izip (MediaKit); kiwix (WanderWiki); flow-free, two-dots (Millrace, its first Spanish comparisons); baba-is-you (Tare, its first); habitnow (Taskful Day); hrv4training (Observa); rise-sleep-tracker (AfterShift, its first); magnus-trainer (Chessful). Hub now 42 cards with a new «Juegos de lógica» section. Research: es-tier3-research-2026-11-19.md § Batch 4 shortlist; store check: ~/Downloads/githubcode/es-tier3-store-batch4-2026-11-19.md. Stale check before the batch: 0. Remaining English comparisons have weak or no Spanish demand (optional: Countdown Star, KAMI 2, DragonBox) |
| Tier 4, batch 1 | written and integrated 2026-11-19, no native review yet (not pushed): hub /es/journal/ («Blog») and nine posts how-many-steps-a-day-to-aim-for (EarnLock), how-long-to-rest-between-sets, choosing-a-strength-program-you-will-finish (LiftLog), how-to-estimate-your-one-rep-max, rpe-and-rir-explained (GymLogger X), how-much-to-tip-in-the-us (RightSplit), compress-a-video-for-email (MediaKit), apple-watch-hrv-without-a-baseline (Observa), puppy-and-kitten-vaccination-schedule (Pawza; Spain rabies rules from the MAPA note of June 2026 and the MAPA travel page), plus the local-only /es/journal/turnos-rotativos/ (AfterShift; BOE Estatuto de los Trabajadores arts. 34 and 36, Ley 31/1995 art. 22, INSST NTP 455). Sonnet writers, one per post; four separate reviewers plus a wiring reviewer. Research: ~/Downloads/githubcode/es-tier4-research-2026-11-19.md (next candidates listed there); briefs `_i18n/es-tier4-brief.md`, `_i18n/es-tier4-review-brief.md`. Stale check before the batch: 0 |
| Tier 4, batch 2 | written and integrated 2026-11-19, no native review yet (not pushed): five translations when-to-deload (GymLogger X), puzzle-games-without-ads-or-lives (Millrace), what-an-iphone-app-can-actually-block (EarnLock), how-plan-mode-builds-a-checklist (Soon.), find-every-recurring-charge (AllPaid; Rocket Money replaced by Fintonic from its Spanish listing) and five local-only posts: /es/journal/frecuencia-cardiaca-en-reposo/ (Observa; MedlinePlus en español, Fundación Española del Corazón, Apple es-es), /es/journal/cuantas-horas-de-sueno-profundo/ (Observa; Sociedad Española de Sueño, NHLBI, MedlinePlus, Apple es-es), /es/journal/sobrecarga-progresiva/ (LiftLog, GymLogger X; ACSM 2009 and 2026, Plotkin 2022, Schoenfeld 2017), /es/journal/pasaporte-para-perros/ (Pawza; MAPA, Your Europe, Implementing Regulation (EU) 2026/705), /es/journal/convertir-mkv-a-mp4/ (MediaKit; matroska.org, Apple es-es, VideoLAN). Hub 20 posts. Research: es-tier4-research-2026-11-19.md § Batch 2 shortlist. Stale check before the batch: 0 |
| Tier 4, batch 3 | written and integrated 2026-11-19, no native review yet (not pushed): one translation your-photos-shouldnt-ride-the-elevator (MediaKit, for «convertir heic a jpg») and nine local-only posts: festivos-2027 and cuantos-dias-faltan-para-navidad (Soon.; BOE resolution of 8 October 2026, ET art. 37, RD 2001/1983, Apple es-es), comprimir-pdf-mac and extraer-audio-de-video-iphone (MediaKit; Apple es-es), series-de-aproximacion (GymLogger X, LiftLog; Fradkin 2010, McCrary 2015, Ribeiro 2014), deuda-de-sueno (AfterShift; SES, NHLBI, MedlinePlus, NIH), sueno-rem and vo2-max (Observa; NICHD, NHLBI, SES, Apple whitepaper, CUN, Mandsager 2018), desparasitar-perro (Pawza; ESCCAP España guides). Hub 30 posts. Research: es-tier4-research-2026-11-19.md § Batch 3 shortlist. Stale check before the batch: 0 |
| Stale pages | 0 (2026-11-19, `i18n.py stale`) |
| Native review | none (NATIVE REVIEWER: none). Every page is logged as "no native review yet" |
| Build time | 270 s wall, 137 s CPU before Spanish (2026-11-19, seven research agents running in parallel, so the wall time is inflated); French sheet had 80 s after French Tier 1. Idle machine 2026-11-19: 157 s before the tx-app fix, 52 s after (617 pages, `--profile`; tx-app 99.6 s to 4.9 s, I-0258) |

## Market and register

- Market: Spain. Folder `/es/`, `<html lang="es-ES">`, hreflang `es-ES` plus the bare `es` until `/es-mx/` exists
  (TRANSLATION.md 2: moving the bare tag later changes only hreflang, never a URL), og:locale `es_ES`, territory
  ESP, currency EUR. Readers in Latin America who land here see EUR prices; the App Store link opens their own
  storefront.
- Engines (TRANSLATION.md 7.4): Google first, then Bing (also feeds DuckDuckGo, Ecosia, Copilot). Tools: Search
  Console, Bing Webmaster Tools. IndexNow covers Bing and the engines that use it.
- **Formality: tú** for one reader, **vosotros** for more than one (rare on this site; prefer singular). Reasons:
  1. TRANSLATION.md 13 default for Spain.
  2. Apple Spain writes tú on every page checked (support.apple.com/es-es guides, apple.com/es, apps.apple.com/es;
     zero usted, es-apple-terms.md).
  3. Every one of our apps' Spanish interfaces writes tú, with no usted or vos (es-glossary.md, counted 2026-11-19;
     the only usted strings are two GymLogger X validation messages), and our own Spanish App Store descriptions
     write tú (Observa: «Toca «¿Por qué?»…»). So app strings can be quoted as they are.
  Never mix: no usted, su/sus addressing the reader, vos or ustedes.
- Spain vocabulary only: móvil, ordenador, vídeo, añadir, informe, introducir, «cuenta atrás». Never celular,
  computadora, video (without accent), agregar, reporte, ingresar (for "enter"), «cuenta regresiva», puntaje. Some apps
  use Latin-American words in their `es` locale (AfterShift «Agregar», Soon. «cuenta regresiva», Observa's store
  subtitle «Puntaje», RightSplit «ingresa»); the site does not copy them.

## Typography and punctuation

House rules (TRANSLATION.md 8.3), with the characters to type:

- ¿…? and ¡…! always, also in headings, FAQ questions and short labels.
- Quotes: «…» with no inner spaces (Apple Spain's support and marketing style); inner quotes “…”. A UI label that
  is one word is written bare; a multi-word label goes in «…». Full stop after the closing quote: «Tiempo de uso».
- Menu paths: Ajustes > [tu nombre] > Suscripciones (spaces around >).
- Headings and labels in sentence case: only the first word and proper names take a capital. No English title case
  (store subtitles such as «Lista Tareas & Agenda» are the store's, not a model).
- No em or en dashes. A range is «de 3 a 5 kg» or «entre 3 y 5». Lists: «A, B y C» (no comma before y/o).
- Numbers: decimal comma (4,8); thousands with a period from five digits on (12.500, Apple Spain writes 100.000);
  four-digit numbers without separator (6005). No-break space U+00A0 between a number and %, €, units: `3,99 €`,
  `80 %`, `35 °C`, `8 h`. Metric units only.
- Times: 24-hour, «22:30» (Apple Spain «11:00 a 13:00»). Dates in prose: «26 de octubre de 2026», months lowercase,
  «1 de noviembre» (no ordinal), as Apple Spain writes them. Templates use date.html.
- Apostrophes do not occur in Spanish; never use a typographic one inside a Spanish word.
- «app» in body copy (feminine: «la app», «una app», as Apple Spain writes «la app Salud»); «aplicación» in titles
  and H1 where the search phrase uses it. Never «appli».
- Anglicisms: Spanish word where one is in common use (suscripción, ajustes, copia de seguridad, captura de pantalla).
  Keep English where Spanish searchers and Apple keep it: App Store, App Store Connect, widget, Dynamic Island
  (feminine: «la Dynamic Island»), Apple Watch (masculine: «el Apple Watch»), iCloud, Siri, ASO, privacy manifest.

## Formats (checked 2026-11-19 against the Spanish App Store)

Source: the iTunes lookup API (`itunes.apple.com/lookup?country=es&lang=es_es`) for all 20 live apps plus Things 3
(id904237743), and the apps.apple.com/es product pages read by the glossary agents (the web storefront rate-limited
with HTTP 429 at first; the retries came through).

| What | Format seen | Where | In the site |
|---|---|---|---|
| Price | `9,99 €` (U+00A0 before €), `14,99 €` | Things 3; Mockly id6756589122 | locales.yml `EUR: position after, space U+00A0, decimal ",", group "."` |
| Free app | `Gratis` (and «Compras dentro de la app») | all our free apps | `strings.free: "Gratis"` |
| Thousands | `100.000` | Apple Spain (es-apple-terms.md) | `group: "."` |
| Dates | «18 de septiembre de 2026» in running text | support.apple.com/es-es | `date_long "{d} de {month} de {Y}"` |
| Rating value | decimal comma | App Store | `strings.decimal: ","` |

Price line pattern: `Gratis, Premium desde 3,99 €/mes, 24,99 €/año o 59,99 € de por vida` (strings.from «desde»,
per_month «/mes», per_year «/año», lifetime «de por vida», or «o»). Trial label: `7 días de prueba gratis`
(the apps' paywalls say «Prueba gratuita de 7 días»; the number-first form keeps the label lowercase inside a line).
Zero price on plan cards: `{P_ZERO}` → `0 €`.

Note: the Spanish App Store shows the developer's personal name and address (seller line). That name never goes on
the site; attribute to "Lagerland Apps".

## Glossary

Companion files: `_i18n/es-glossary.md` (per app: Spanish coverage, feature names verbatim from the string
catalogs, Spanish App Store name and subtitle, tier names, flags) and `_i18n/es-apple-terms.md` (Apple's own Spain
Spanish names, each with its Apple source URL). Rule: a feature name is written exactly as the app's Spanish
interface shows it; an Apple product or feature name exactly as Apple Spain writes it.

All 21 apps (20 live plus Clippet) have a Spanish interface (99 to 100 % of each catalog, checked 2026-11-19), so
every app page may say the app is available in Spanish. Gaps to keep off the pages: AfterShift's calendar
permission prompt and Pawza's camera and photo permission prompts are English only; AllPaid's Siri phrases are
English only; LiftLog has 8 untranslated statistics labels and an English Siri hint; Taskful Day's «End/Extend
focus session» shortcuts fall back to English; GymLogger X's program creator has 99 unaccented strings (app bug:
never copy those spellings). Mockly and Millrace use the locale code `es-ES` instead of `es` in their catalogs.

The terms that matter most across the site:

| English | Spanish on the site | Source |
|---|---|---|
| (address) you | tú; vosotros for a plural; never usted | this sheet |
| Download on the App Store (badge) | Consíguelo en el / App Store (Mac: Consíguelo en el / Mac App Store). Not «Descárgalo», which is the Mexican badge | Apple badge artwork es-es (tools.applemediaservices.com) |
| Free (price) | Gratis | Spanish App Store |
| In-App Purchases | Compras dentro de la app | Spanish App Store |
| subscription / cancel | suscripción; Ajustes > [tu nombre] > Suscripciones > «Cancelar suscripción» | support.apple.com/es-es/118428 |
| lifetime (purchase) | «de por vida» (price line, plan cards, as most apps' paywalls and store products say); «compra única» in prose | app catalogs, store IAP names |
| Family Sharing | En familia (Apple's name; MediaKit's «Compartir en Familia» is an app-side variant) | Apple support, app catalogs |
| Data Not Collected | No se recopilan datos (section «Privacidad de la app») | Spanish App Store |
| Health app / Apple Health | la app Salud / Salud de Apple | support.apple.com/es-es, apple.com/es |
| Heart Rate Variability (HRV) | variabilidad de la frecuencia cardiaca (VFC); always SDNN for Apple Health; «VFC (SDNN)» on Observa. Apple Spain writes «cardiaca» without accent | Apple ES, Observa catalog |
| Resting heart rate | frecuencia cardiaca en reposo | Apple ES |
| Sleep stages | Despierto, REM, Esencial, Sueño profundo | Apple ES |
| Screen Time | Tiempo de uso (Apple's iOS name in Spain; «tiempo de pantalla» only where it is the searched phrase, as a common noun) | Apple support, keyword research |
| Focus / Sleep Focus | modo de concentración / modo de concentración Descanso | Apple support |
| Home Screen / Lock Screen / widgets | pantalla de inicio / pantalla de bloqueo / widgets | Apple support |
| Live Activities / Smart Stack / StandBy | actividades en directo / grupo inteligente / En reposo | Apple support |
| iCloud sync | sincronización con iCloud | Apple support, app catalogs |
| Settings (iOS) | Ajustes | Apple support |
| Shortcuts / Wallet | Atajos / Cartera | Apple support |
| Workouts (Apple) | entrenos (the Watch app is Entreno) | Apple ES |
| VO2 max | VO2 máximo | Apple ES |
| Sign in with Apple | Iniciar sesión con Apple | Apple ES |
| App Tracking Transparency | «Permitir que las apps soliciten rastrearte»; tracking = rastreo | Apple ES |
| countdown | cuenta atrás (Spain), never cuenta regresiva | Soon. store listing, Spain usage |
| Journal (section) | Blog (hub title, nav, feed); URLs stay `/es/journal/`. «Diario» reads as a newspaper or a personal diary in Spain | es.yml review 2026-11-19 |
| stamp sheet (design metaphor) | pliego (Correos sells «pliegos»), «Pliego 2025-{year} · Emitido en Finlandia» | es.yml review 2026-11-19 |
| Insights (section) | Análisis (as the apps' Spanish UIs say) | es-glossary.md |
| privacy manifest | «manifiesto de privacidad» in prose; «manifiesto de privacidad (privacy manifest)» at the first mention on the home and transparency pages. Apple Spain has no consumer term for it | decision 2026-11-19 (batch 1 review) |
| Get (App Store button) | Obtener (Spain iOS); «Consíguelo» only on the badge | es-apple-terms.md, batch 1 review |

Per-app tier names follow each app's Spanish UI (es-glossary.md): Premium for AfterShift, Observa (the English site
says Pro), Soon., Shogiful, Xiangqiful, WanderWiki, EarnLock; Pro+ for RightSplit; Pro for AllPaid, AppMeta,
MediaKit, Pawza, Taskful Day, GymLogger X; Clippet Pro. Exception carried over from the owner decision of 2026-11-08:
Chessful's tier is **Pro** on every language page (as in the store IAP names), although the app UI still says Premium.
LiftLog's one-time tiers: Justo, Bueno, Generoso, Mecenas (store IAP names; the app says «Bien» for the second, an
app-side mismatch).

Spanish App Store names (they differ from English except AppMeta and Mockly):

| App | Spanish store name | Spanish subtitle |
|---|---|---|
| AfterShift | AfterShift: Sueño y Turnos | Recuperación, siestas y fatiga |
| AllPaid | AllPaid – Gestión de Facturas | Paga a tiempo, sin estrés |
| AppMeta | AppMeta for App Store Connect | ASO, metadatos y reseñas |
| AppMeta Pulse | AppMeta Pulse: Ventas de apps | Ingresos y reseñas con IA |
| Chessful | Chessful: Entrena y Analiza | Ajedrez, táctica, puzzles, Elo |
| EarnLock | EarnLock: Bloquea Apps y Foco | Gana tu tiempo de pantalla |
| GymLogger X | GymLogger X: Entrena Gym | Entrenamiento y Registro Gym |
| LiftLog | LiftLog: Gimnasio Diario | Series, reps y fuerza |
| MediaKit | MediaKit Comprimir y Convertir | Vídeo, Audio, Imagen, PDF, ZIP |
| Millrace | Millrace: Entrega de fichas | 64 niveles, una sola entrada |
| Mockly | Mockly: Screenshot Maker | 50 idiomas, un clic |
| Observa | Observa: VFC y Recuperación | Sueño, Ciclo, Coach & Puntaje |
| Pawza | Pawza: Salud y Cartilla Animal | Vacunas, peso y recordatorios |
| RightSplit | RightSplit: Dividir y Propina | Escanea ticket, gastos grupo |
| Shogiful | Shogiful: Ajedrez japonés | Shogi: táctica y análisis IA |
| Soon. | Soon. Días Hasta Eventos | Boda Viaje y Bebé Cuenta Atrás |
| Tare | Tare: Rompecabezas de lógica | Equilibrio y pesos misteriosos |
| Taskful Day | Taskful Day: Planificador | Lista Tareas & Agenda |
| WanderWiki | WanderWiki: descubre y aprende | Datos, historia y curiosidades |
| Xiangqiful | Xiangqiful: Ajedrez Chino | Aprende xiangqi: táctica e IA |
| Clippet (unreleased) | Clippet: Portapapeles (prepared listing) | Copiar y pegar con historial |

The site writes the app name alone (`name` is never translated); the store name and subtitle are vocabulary hints.

## Keyword research

Full notes, sources and FAQ-style questions per page: `_i18n/es-keywords.md` (Google suggest hl=es gl=es, Bing
qsonhs mkt=es-ES, App Store search hints for the Spanish storefront 143454-8, iTunes Search API country=es,
2026-11-19). Every query below came from one of those sources.

Search Console for Spain: not read in this session (Claude in Chrome not connected, the built-in browser not signed
in, no export on disk). The French property showed almost no French queries; expect the same for Spain. Revisit
4 to 6 weeks after go-live with the page filter `/es/` and the country filter Spain.

`seo.title`, the H1 and `quick_answer` of each page are written for its primary query.

| Page | Primary query | Secondary queries |
|---|---|---|
| Home (/es/): studio of privacy-first Apple apps | `aplicaciones sin anuncios` (privacy angle has no demand) | `aplicaciones sin publicidad`, `aplicaciones sin anuncios gratis` |
| Apps hub (/es/apps/) | `mejores aplicaciones iphone` | `mejores apps iphone`, `aplicaciones útiles para iphone` |
| About (/es/lagerland-apps/) | none with demand: brand-led («Lagerland Apps» + «desarrollador independiente») | `desarrollador de aplicaciones`, `desarrollador independiente` |
| Support hub (/es/support/) | `cancelar suscripción iphone` | `restaurar compras app store`, `reembolso app store` |
| Transparency (/es/transparency/) | `app tracking transparency` (Spanish searchers type the English) | `app tracking transparency que es`, `privacy manifest` |
| AfterShift | `dormir después de trabajar de noche` | `trastorno del sueño por turnos de trabajo`, `deuda de sueño` |
| AllPaid | `app recordatorio de pagos` | `app para recordar pagos`, `recordatorio de pago de facturas` (`app control suscripciones` moved to the bill-tracker guide, Tier 2) |
| AppMeta | `app store connect mac app` (developers search in English) | `app store connect for mac`, `aso app store` |
| AppMeta Pulse | `app store connect iphone` | `app store connect ios`, `app store connect api` |
| Chessful | `aplicación ajedrez` | `aprender ajedrez app`, `análisis de partidas de ajedrez` |
| EarnLock | `bloquear apps iphone` | `bloqueador de aplicaciones`, `app bloquear apps iphone` (`limitar tiempo de pantalla` and `como reducir el tiempo de pantalla en iphone` moved to the screen-time guide, Tier 2) |
| GymLogger X | `app gimnasio apple watch` | `app para registrar entrenamientos gimnasio`, `app de entrenamiento apple watch` |
| LiftLog | `app registro gimnasio` («sin suscripción» has no demand; kept in the title as the differentiator) | `app seguimiento gimnasio`, `app de pesas` |
| MediaKit | `comprimir video iphone` | `comprimir pdf iphone`, `convertir video a mp4 iphone` |
| Millrace (never write the number title) | `juegos de lógica iphone` | `juegos de lógica sin anuncios`, `juegos de lógica ipad` (`juegos de ingenio iphone` goes to Tare; `mejores juegos de lógica / puzzle iphone` to the logic guide, Tier 2) |
| Mockly | `screenshots app store` (developers type the English; «capturas app store» has no demand) | `app store screenshot generator`, `mockup app store`, `app store screenshot maker` |
| Observa | `hrv apple watch` («hrv» alone is Honda HR-V noise) | `variabilidad frecuencia cardiaca`, `app sueño apple watch`, `app hrv apple watch` |
| Pawza | `cartilla veterinaria digital` («cartilla» is the Spain word; «carnet de vacunación» is Latin-American) | `app cartilla de vacunación perros`, `app salud mascotas` (`calendario vacunación perros` moved to the vaccination post, Tier 4) |
| RightSplit | `app para dividir cuenta restaurante` (bare «dividir cuenta» is arithmetic noise; «pagar a escote» is the Spain idiom) | `app dividir gastos`, `dividir cuentas entre amigos`, `calculadora dividir cuentas` |
| Shogiful | `shogi` | `ajedrez japonés`, `como se juega al shogi`, `aprender shogi` |
| Soon. | `cuenta atrás iphone` | `widget cuenta atrás`, `app cuenta atrás`, `contador de días app` |
| Tare | `juegos de ingenio iphone` (moved from Millrace to avoid two pages on one query; «juego de balanza» is a kids' maths audience) | `mejores juegos de ingenio iphone`, `juegos de logica sin anuncios` (`mejores juegos de lógica / puzzle iphone` moved to the logic guide, Tier 2) |
| Taskful Day | `app lista de tareas` | `app planificador diario`, `app to do list`, `app para organizar el dia` |
| WanderWiki | `wikipedia aleatoria` (tiny demand; intent is Wikipedia's own random page) | `wikipedia aleatorio`, `wikipedia al azar`, `app wikipedia` |
| Xiangqiful | `ajedrez chino` (title carries both «ajedrez chino» and «xiangqi») | `xiangqi`, `ajedrez chino como se juega`, `ajedrez chino reglas` |
| Clippet (unreleased, unlisted) | `historial portapapeles iphone` | `historial portapapeles mac`, `gestor de portapapeles mac`, `app portapapeles iphone` |

Tier 2 (2026-11-19, from es-tier2-research-2026-11-19.md). Guides own the «mejor/mejores» list queries; app pages keep the
app queries (Chessful lost `mejor app de ajedrez`, GymLogger X `mejor app para gimnasio gratis`).

| Page | Primary query | Secondary queries |
|---|---|---|
| /es/guides/best-chess-apps-iphone/ | `mejor app de ajedrez` | `mejor app de ajedrez para iphone`, `mejor app para aprender ajedrez`, `mejor app de ajedrez sin anuncios` |
| /es/guides/best-logic-puzzle-games-iphone/ | `mejores juegos de lógica iphone` | `mejores juegos de puzzle iphone`, `juegos de puzzle para iphone` |
| /es/guides/best-xiangqi-apps-iphone/ | `ajedrez chino online` (`ajedrez chino` and `xiangqi` are Xiangqiful's) | `jugar ajedrez chino online`, `xiangqi online` |
| /es/guides/workout-app-without-subscription/ | `mejor app gimnasio gratis` | `app gimnasio sin suscripción`, `app rutina gimnasio gratis iphone` |
| /es/guides/limitar-tiempo-de-pantalla-iphone/ (local-only) | `como limitar el tiempo de pantalla en iphone` | `limitar tiempo de pantalla`, `bloquear apps iphone por tiempo`, `app para dejar de usar el movil` |
| /es/for/shift-workers/ | `trabajo a turnos y salud` | `trabajo a turnos salud`, `trabajo de noche afecta la salud` |
| /es/for/apple-health-power-users/ | `mejores apps salud apple watch` | `mejor app salud apple watch`, `app salud apple watch gratis` |
| /es/for/calm-productivity/ | `mejores apps de productividad iphone` | `app minimalista para iphone`, `apps procrastinación` |
| /es/guides/best-shogi-apps-iphone/ | `shogi online` (`shogi`, `shogi app`, `aprender shogi` are Shogiful's) | `jugar shogi online`, `shogi online español`, `shogi online gratis` |
| /es/guides/bill-tracker-without-bank-connection/ | `app para controlar suscripciones` (AllPaid gave up `app control suscripciones`) | `app gastos fijos y variables`, `gestionar suscripciones apple`; `fintonic alternativas` moves to the Tier 3 «alternativa a Fintonic» page when it exists |
| /es/guides/como-poner-cuenta-atras-iphone/ (local-only) | `como poner una cuenta atrás en el iphone` (Soon. gave up `widget cuenta atrás iphone`) | `como poner un widget de cuenta atrás en iphone`, `widget contador de días iphone`, `widget cuenta atrás iphone gratis` |

Tier 3 batch 1 (2026-11-19, from es-tier3-research-2026-11-19.md). Comparisons own the brand queries; app pages and guides keep
the generic ones (`app dividir gastos` stays on RightSplit, `app para controlar suscripciones` on the bill-tracker guide, which gave
`fintonic alternativas` to the Fintonic page).

| Page | Primary query | Secondary queries |
|---|---|---|
| /es/alternatives/ (hub) | `alternativa a tricount` … (brand list) | `comparativa apps iphone`, `apps alternativas iphone` |
| /es/alternatives/tricount/ | `alternativa a tricount` | `tricount alternativa`, `tricount opiniones`, `tricount gratis` |
| /es/alternatives/splitwise/ | `splitwise o tricount` | `splitwise o tricount cual es mejor`, `alternativas splitwise gratis`, `splitwise como funciona` |
| /es/alternatives/alternativa-a-fintonic/ (local-only) | `alternativas a fintonic` | `fintonic alternativas`, `app como fintonic`, `fintonic es seguro` |
| /es/alternatives/chess-com/ | `alternativa a chess.com` | `análisis de partidas chess.com gratis`, `chess.com gratis` |
| /es/alternatives/lichess/ | `chess.com o lichess` | `es mejor chess com o lichess`, `alternativa a lichess` |
| /es/alternatives/whoop/ | `whoop sin suscripción` (title: «Alternativa a Whoop sin suscripción obligatoria»; Observa is never «sin suscripción») | `whoop alternativas`, `alternativa whoop apple watch`, `alternativa a whoop sin pulsera` |
| /es/alternatives/hevy/ | `alternativa a hevy` / `hevy app opiniones` | `hevy app precio`, `hevy app es gratis`, `hevy o strong` |
| /es/alternatives/opal/ | `alternativa a opal` / `opal app para qué sirve` | `opal app es gratis`, `app como opal` |
| /es/alternatives/forest/ | `forest app` / `alternativa a forest` | `forest app estudio`, `forest app gratis`, `forest app cómo funciona` |
| /es/alternatives/pdf-expert/ | `alternativa a pdf expert` | `pdf expert gratis`, `pdf expert gratis mac` |

Tier 3 batch 2 (2026-11-19).

| Page | Primary query | Secondary queries |
|---|---|---|
| /es/alternatives/oura/ | `oura ring o apple watch` | `alternativa a oura`, `oura ring alternativas`, `oura ring sin suscripción` |
| /es/alternatives/bevel/ | `alternativa a bevel` / `bevel app opiniones` | `bevel app es gratis`, `bevel app precio`, `bevel o whoop` |
| /es/alternatives/autosleep/ | `alternativa a autosleep` / `autosleep apple watch` | `autosleep app`, `autosleep opiniones` |
| /es/alternatives/fitbod/ | `alternativa a fitbod` / `fitbod opiniones` | `fitbod es gratis`, `fitbod precio` |
| /es/alternatives/jefit/ | `jefit en español` / `alternativa a jefit` | `jefit opiniones`, `jefit es gratis` |
| /es/alternatives/settle-up/ | `settle up o tricount` | `settle up cómo funciona`, `settle up app vs splitwise`, `settle up español` |
| /es/alternatives/one-sec/ | `alternativa a one sec` / `one sec app` | `one sec es gratis`, `one sec español` |
| /es/alternatives/screenzen/ | `alternativa a screenzen` (no reviews on the page, so not `screenzen opiniones` in the title) | `screenzen es gratis`, `screenzen es seguro` |
| /es/alternatives/habitica/ | `habitica en español` | `alternativa a habitica`, `habitica es gratis`, `habitica qué es` |
| /es/alternatives/alternativa-a-appblock/ (local-only) | `appblock iphone` | `alternativa a appblock`, `appblock es gratis`, `appblock es seguro` |

Tier 3 batch 3 (2026-11-19).

| Page | Primary query | Secondary queries |
|---|---|---|
| /es/alternatives/welltory/ | `welltory en español` | `welltory opiniones`, `welltory es gratis`, `alternativa a welltory` |
| /es/alternatives/athlytic/ | `athlytic en español` | `athlytic opiniones`, `athlytic es gratis`, `alternativa a athlytic` |
| /es/alternatives/gentler-streak/ | `alternativa a gentler streak` | `gentler streak opiniones`, `gentler streak vs bevel` |
| /es/alternatives/chessable/ | `chessable en español` | `chessable cursos en español`, `chessable es gratis`, `alternativa a chessable` |
| /es/alternatives/strong-workout-app/ | `alternativa a strong` / `strong o hevy` | `strong hevy app` |
| /es/alternatives/alpha-progression/ | `alternativa a alpha progression` | `alpha progression opiniones`, `alpha progression gratis` |
| /es/alternatives/stronglifts-5x5/ | `stronglifts 5x5 español` | `alternativa a stronglifts`, `stronglifts 5x5 app` |
| /es/alternatives/wikipedia-app/ | `app wikipedia español` | `app wikipedia sin internet`, `wikipedia app gratis` |
| /es/alternatives/documents-by-readdle/ | `alternativa a documents de readdle` | `documents by readdle gratis` |
| /es/alternatives/cloudconvert/ | `cloudconvert gratis` / `cloudconvert en español` | `cloudconvert es gratis`, `alternativa a cloudconvert` |

Tier 3 batch 4 (2026-11-19). The Millrace app page keeps `juegos de lógica sin anuncios` and `juegos sin internet iphone`; Tare keeps
`juegos de ingenio iphone`; Observa keeps `hrv apple watch`: the comparisons dropped those keywords.

| Page | Primary query | Secondary queries |
|---|---|---|
| /es/alternatives/handbrake/ | `alternativa a handbrake` | `handbrake gratis`, `handbrake para qué sirve`, `handbrake mac` (`handbrake en español` dropped: no source says whether HandBrake has a Spanish UI) |
| /es/alternatives/convertio/ | `convertio gratis` | `alternativa a convertio`, `convertio precio` |
| /es/alternatives/wondershare-uniconverter/ | `uniconverter es gratis` | `uniconverter precio`, `alternativa a wondershare uniconverter` |
| /es/alternatives/izip/ | `izip gratis` | `alternativa a izip`, `descomprimir rar iphone` |
| /es/alternatives/kiwix/ | `kiwix wikipedia offline español` | `kiwix para qué sirve`, `wikipedia sin conexión iphone` |
| /es/alternatives/flow-free/ | `flow free juego` | `juegos como flow free`, `alternativa a flow free` |
| /es/alternatives/two-dots/ | `two dots juego` | `alternativa a two dots`, `juegos como two dots` |
| /es/alternatives/baba-is-you/ | `juegos parecidos a baba is you` | `baba is you español`, `baba is you precio`, `tare o baba is you` |
| /es/alternatives/habitnow/ | `habitnow iphone` / `habitnow es gratis` | `alternativa a habitnow` |
| /es/alternatives/hrv4training/ | `hrv4training que es` | `hrv4training como funciona`, `alternativa a hrv4training` |
| /es/alternatives/rise-sleep-tracker/ | `rise sleep gratis` | `alternativa a rise sleep tracker`, `rise sleep funciona`, `app sueño trabajo a turnos` |
| /es/alternatives/magnus-trainer/ | `magnus trainer` | `alternativa a magnus trainer`, `magnus trainer descargar` |

Tier 4 batch 1 (2026-11-19). Journal posts never take an app page's, guide's or comparison's primary (Observa keeps `hrv apple watch` and
`variabilidad frecuencia cardiaca`, MediaKit `comprimir video iphone`, AfterShift `dormir después de trabajar de noche`); the Pawza app page gave
`calendario vacunación perros` to the vaccination post. The hub is brand-led («blog lagerland apps», «blog de gimnasio» …).

| Page | Primary query | Secondary queries |
|---|---|---|
| /es/journal/how-many-steps-a-day-to-aim-for/ | `cuántos pasos al día` | `cuántos pasos hay que dar al día`, `cuántos pasos al día es saludable` |
| /es/journal/how-long-to-rest-between-sets/ | `cuánto descansar entre series` | `descanso entre series hipertrofia`, `descanso entre series de fuerza` |
| /es/journal/how-to-estimate-your-one-rep-max/ | `calcular 1rm` | `fórmula 1rm`, `fórmula brzycki`, `fórmula epley`, `calculadora rm` |
| /es/journal/rpe-and-rir-explained/ | `rpe y rir` | `diferencia rpe y rir`, `rpe y rir tabla`, `rir gimnasio significado` |
| /es/journal/choosing-a-strength-program-you-will-finish/ | `rutina ppl` | `rutina torso pierna`, `full body o rutina dividida`, `rutina 5/3/1` |
| /es/journal/how-much-to-tip-in-the-us/ | `propina en estados unidos` | `propina en estados unidos es obligatoria`, `propina en estados unidos porcentaje`, `propina usa` |
| /es/journal/compress-a-video-for-email/ | `comprimir vídeo para enviar por correo` | `enviar vídeo pesado por correo`, `tamaño maximo archivos adjuntos gmail`, `mail drop icloud` |
| /es/journal/apple-watch-hrv-without-a-baseline/ | `vfc baja` | `vfc baja qué significa`, `variabilidad de la frecuencia cardiaca valores normales`, `valores de referencia vfc` |
| /es/journal/puppy-and-kitten-vaccination-schedule/ | `vacunas cachorro` | `calendario vacunas perros españa`, `vacunas gatos calendario`, `vacuna rabia perro obligatoria` |
| /es/journal/turnos-rotativos/ (local-only) | `turnos rotativos` | `turnos rotativos qué significa`, `turnos rotativos mañana, tarde y noche`, `cuadrante de turnos rotativos` |

Tier 4 batch 2 (2026-11-19). The Spanish home gave up `juegos sin anuncios iphone` and `mejores juegos sin anuncios iphone` to the games post.

| Page | Primary query | Secondary queries |
|---|---|---|
| /es/journal/when-to-deload/ | `semana de descarga gym` | `semana de descarga gym cada cuanto`, `semana de descarga gym como se hace`, `deload que es` |
| /es/journal/puzzle-games-without-ads-or-lives/ | `juegos sin anuncios iphone` | `juegos gratis sin anuncios iphone`, `juegos sin vidas`, `como ganan dinero los juegos gratis` |
| /es/journal/what-an-iphone-app-can-actually-block/ | `como bloquear una app en iphone` | `puedo bloquear una aplicacion en iphone`, `se puede bloquear instagram en iphone`, `family controls` |
| /es/journal/how-plan-mode-builds-a-checklist/ | `lista para organizar una boda` | `checklist boda`, `cronograma boda`, `app para organizar una boda` |
| /es/journal/find-every-recurring-charge/ | `como ver mis suscripciones en iphone` | `ver suscripciones activas iphone`, `como saber cuantas suscripciones tengo` |
| /es/journal/frecuencia-cardiaca-en-reposo/ (local-only) | `frecuencia cardiaca en reposo normal` | `pulsaciones en reposo`, `pulsaciones normales en reposo por edad` |
| /es/journal/cuantas-horas-de-sueno-profundo/ (local-only) | `cuantas horas de sueño profundo` | `sueño profundo cuanto tiempo es normal`, `porcentaje sueño profundo` |
| /es/journal/sobrecarga-progresiva/ (local-only) | `sobrecarga progresiva` | `sobrecarga progresiva ejemplos`, `sobrecarga progresiva gym`, `sobrecarga progresiva hipertrofia` |
| /es/journal/pasaporte-para-perros/ (local-only) | `pasaporte para perros` | `pasaporte para perros en españa`, `pasaporte para perros es obligatorio`, `sacar pasaporte perro` |
| /es/journal/convertir-mkv-a-mp4/ (local-only) | `convertir mkv a mp4` | `convertir mkv a mp4 con vlc`, `convertir mkv a mp4 sin perder calidad`, `convertir mkv a mp4 iphone` |

Tier 4 batch 3 (2026-11-19). The AfterShift page gave `deuda de sueño` and `cómo recuperar deuda de sueño` to the sleep-debt post; the MediaKit
page gave `convertir heic a jpg` and `convertir heic a jpg iphone` to the HEIC post.

| Page | Primary query | Secondary queries |
|---|---|---|
| /es/journal/your-photos-shouldnt-ride-the-elevator/ | `convertir heic a jpg` | `heic a jpg`, `convertir heic a jpg en mac`, `convertir heic a jpg en iphone` |
| /es/journal/festivos-2027/ (local-only) | `festivos 2027 españa` | `festivos nacionales 2027`, `calendario laboral 2027`, `festivos 2027 españa boe` |
| /es/journal/cuantos-dias-faltan-para-navidad/ (local-only) | `cuantos dias faltan para navidad` | `cuenta atras navidad`, `cuantos dias faltan para navidad desde hoy` |
| /es/journal/comprimir-pdf-mac/ (local-only) | `comprimir pdf mac` | `comprimir pdf vista previa mac`, `reducir tamaño pdf mac` |
| /es/journal/extraer-audio-de-video-iphone/ (local-only) | `extraer audio de video iphone` | `extraer audio de video iphone gratis`, `convertir video a mp3 iphone` |
| /es/journal/series-de-aproximacion/ (local-only) | `series de aproximacion` | `series de aproximacion y efectivas`, `cuantas series de calentamiento hacer` |
| /es/journal/deuda-de-sueno/ (local-only) | `deuda de sueño` | `deuda de sueño acumulada`, `deuda de sueño sintomas`, `como recuperar sueño perdido` |
| /es/journal/sueno-rem/ (local-only) | `sueño rem` | `sueño rem que significa`, `sueño rem y sueño profundo`, `sueño rem bajo` |
| /es/journal/vo2-max/ (local-only) | `vo2 max que es` | `vo2 max que es y como se mide`, `vo2 max apple watch`, `vo2 max apple watch fiable` |
| /es/journal/desparasitar-perro/ (local-only) | `desparasitar perro` | `cada cuanto desparasitar perro`, `desparasitar perro cachorro`, `desparasitar perros interno y externo` |

## Decisions from the Tier 1 reviews (2026-11-19)

- Founder lines mirror the two English forms: «Desarrollador Apple independiente · Finlandia · estudio de una sola
  persona desde 2025» and «Estudio Apple independiente · Finlandia». Never «desarrollador independiente de Apple»
  (reads as Apple's own developer, or "independent from Apple").
- `privacy.data_collection` is «ninguna» (it follows the feminine label «Recopilación de datos»).
- «el App Store» (masculine), as Apple Spain and es.yml write it; «la App Store» only inside a quoted app label.
- Apple feature names that are proper names are written bare in running text (En familia, Tiempo de uso, Salud de
  Apple); «» only around quoted UI labels and buttons. «Admite En familia» for Family Sharing support.
- "N localizations" is «N localizaciones», never «N idiomas» (the counts include regional variants); "N languages"
  stays «N idiomas».
- Privacy pages: «tratar/tratamiento», «recopilar», «a sabiendas», «no gestiona servidores propios», «copia de
  seguridad en iCloud», «No se recopilan datos», «identificador de publicidad (IDFA)»; the advertising clause mirrors
  the English ambiguity: «no vende, comparte ni utiliza … con fines publicitarios». Clippet's own terms page is
  «Términos del servicio» (the app's Spanish label); Apple's EULA is «Contrato de Licencia de Usuario Final de la
  Aplicación con Licencia («EULA Estándar»)», as Apple Spain names it.
- AppMeta and Pulse: Proceeds is «ingresos netos», Revenue/Sales «ventas»/«ingresos». Pulse's first tab is «Panel».
- Soon.: «evento» on the site (the searched word), «momento» is the app's word; Apple's Weather app is «Tiempo», so
  the site says «la previsión del tiempo de Apple», never «Apple Clima» (the app's Latin-American string).
- Tare: «cronómetro» for the game timer (never «cuenta atrás»); «móvil colgante» for the mobile.
- AfterShift: sleep stages as AfterShift's own screens show them (Ligero, Profundo) where the page describes the app,
  Apple's names (Esencial, Sueño profundo) where it describes Salud de Apple.
- Chessful: tier Pro; mistake labels as the app shows them («Tenedor perdido», «Clavada perdida», «Mala seguridad
  del rey»); «error grave» for blunder (not the app's «Pifia»), «Elo» (not «Rating»); move examples in Spanish piece
  letters (D, T, A, C, R).
- Observa: training call «Intenso, Mantener, Recupérate o Descanso» (app strings), readiness bands «Listo, Moderado,
  Bajo», «Estableciendo tu referencia», «Ajustar sueño», «Fuente de sueño», widgets «Foco»…«Observación».
- Support pages: one title pattern «X: soporte y contacto».
- Legal terms to show a Spanish lawyer when one is available: «a sabiendas», «tratar/tratamiento», «responsable de
  los datos personales» (not the formal «responsable del tratamiento»), «fecha de entrada en vigor», refund consent
  «Al hacer una compra, aceptas que podamos responder…», «cambios sustanciales», «menores de 13 años» (Spain's age of
  digital consent is 14), Finland's «Defensor de la Protección de Datos» (working name), and in Clippet's terms
  «lucro cesante», «daños indirectos, incidentales, especiales, consecuentes o punitivos», «comerciabilidad»,
  «tal cual», «idoneidad para un fin determinado», «leyes imperativas de protección de los consumidores».

## Local competitors (for Tier 3)

Candidates from the Tier 2 research (2026-11-19): a local-only «alternativa a Fintonic» for AllPaid (G `fintonic
alternativas`, Fintonic ★25 898 in Spain); Spain-specific shift calendars Shifter (★33 072) and Supershift (★8621) for
AfterShift; AppBlock (★974) for EarnLock. Not researched further yet. Candidates seen in the iTunes Search API results during keyword research are listed in
es-keywords.md per page.

## Decisions from Tier 3 batch 1 (2026-11-19)

- JSON-LD `inLanguage` on Spanish pages is `"es-ES"` (the `html_lang`), never `"es"`.
- Competitor facts: Spanish App Store rows only, in EUR, with «(App Store de España, consultado el 19 de noviembre de 2026)» once per
  page (the small note); facts the Spanish store doesn't show stay as the English page's check says, and the note says which is which.
  No price range built from mixed or truncated IAP rows (PDF Expert, Opal): state the billing model without amounts, or «entre los
  planes de la ficha de España figuran…» when the rows are clear.
- A listing that shows no Watch device: «No consta: la ficha de España no muestra ninguna app para el Apple Watch», never a flat «no tiene».
- Apple's App Privacy headings in Spanish: sección «Privacidad de la app», «Datos usados para rastrearte», «Datos vinculados contigo»;
  never «etiqueta de privacidad».
- Chessful's PGN import takes up to 2.000 games since 2.1.1 (the English chess-com, lichess and chessis pages said 500; fixed in EN,
  DE and FR in the same change).
- Verdict wording: «encaja mejor», «conviene más», «es la opción», «sirve mejor», «es preferible»; vary them across a hub or llms block.
- RightSplit: «la cuenta» or «el ticket» for the bill, «sin registro» or «cuenta de usuario» for accounts.
- Fintonic page: AllPaid «no ofrece perfil crediticio ni préstamos» (AllPaid has a «Préstamos» bill category, so never «no tiene préstamos»);
  «tus cuentas conectadas», never «todas tus cuentas»; the safety FAQ reports the listing only, with «no damos una opinión».

## Decisions from Tier 3 batch 2 (2026-11-19)

- Observa's «Estableciendo tu referencia» shows for about the first five nights (blueprint: until about 5 baseline nights; high
  confidence needs 7). The English oura, hrv4training and what-14-days pages said 7; fixed in EN, DE and ES in the same change.
- A competitor price only where the English page states one, even when the Spanish store shows it (AutoSleep 9,99 € left out:
  «es de pago, sin compras dentro de la app»).
- Before writing «No se indica» for a competitor, check the store page's «En familia» and «Requiere … watchOS» fields (AppBlock
  shows both); the footnote says «No se indica» means the listing doesn't mention it.
- seo.title patterns: one pattern per app at most (Opal «… apps bloqueadas hasta que camines», one sec «… un bloqueo en lugar de
  una pausa», ScreenZen «… bloqueo que se gana con actividad»; Whoop «Alternativa a X sin Y: Observa» is taken).
- EarnLock: «objetivo diario de actividad» for what unlocks apps; «objetivo de pasos» only for the free tier's step goal.

## Decisions from Tier 3 batch 3 (2026-11-19)

- A store line «Requiere macOS … y un Mac con el chip M1» on a listing «Diseñada para iPad» is the iPad app running on Apple-silicon
  Macs, not a Mac app: never add Mac to a competitor's platforms from it (Documents, CloudConvert, StrongLifts, Chessable).
- Apple's App Privacy headings stay exactly as es-apple-terms.md sources them: «Datos usados para rastrearte» (not «utilizados»),
  «Datos vinculados contigo», «Datos no vinculados contigo», «No se recopilan datos».
- A competitor fact on the English page that the Spanish store doesn't show (Chessable Pro's 7-day trial) stays, attributed to the
  English page's check; it is never dropped for lack of a Spanish source.
- «… en español» pages: keyword-first «X en español: …» titles are fine for two apps (Welltory, Athlytic) as long as the tails differ.
- GymLogger X program names and plateau statuses: es-glossary.md, GymLogger X section.

## Decisions from Tier 3 batch 4 (2026-11-19)

- Competitors not in the App Store de España (HandBrake; Convertio, whose only store hit is another seller's app; UniConverter, sold
  there only as four Mac App Store listings): their facts stay as the English page states them, attributed to «la versión en inglés de
  esta página, actualizada el …» when the English page has no dated check, or to its own check date when it has one. USD amounts are
  dropped, never converted; the billing model stays.
- A third-party app that uses a competitor's name lends it no fact (Convertio, HabitNow); the note only says another seller publishes it.
- A rating is given only where the English page states one; then the Spanish store figure replaces the US one, written «4,5 sobre 5 en
  5167 valoraciones».
- Two counts from two sources (Two Dots: «más de 5000 niveles» in the Spanish listing, 7600 in its help centre per the English check):
  both stay, each attributed.
- Apple's «Editors' Choice» has no sourced Apple Spain label in es-apple-terms.md: describe it («elegido por los editores del App Store»).
- AfterShift has no Apple Watch app: a verdict may name the competitor's Watch app as a reason to pick it.
- Comparison pages never take an app page's own keyword (Millrace `juegos de lógica sin anuncios`, `juegos sin internet iphone`; Tare
  `juegos de ingenio iphone`; Observa `hrv apple watch`).
- Taskful Day's Spanish parser knows «mañana» and «a las» (TaskfulDayKit/Parsing/KeywordPacks.swift): «Estirar mañana a las 7:00».

## Decisions from Tier 4 batch 1 (2026-11-19)

- Journal front matter: `date` and `last_updated` are the Spanish publication day; `translated_from` is the English `last_updated`; `read_time`
  «N min de lectura» (U+00A0) from body words only, without URLs and Markdown table syntax, ÷ 200.
- English-language sources keep their links with `{: hreflang="en"}` and « (en inglés)»; where the same help page exists in Spain Spanish
  (Gmail, Microsoft, Apple es-es, YouTube) the Spanish version may replace it when it states the same figure (checked live).
- Spain YMYL additions only from pages fetched that day and saved for the reviewer. Rabies in Spain: competence of each comunidad and ciudad
  autónoma; the post reports the MAPA note (June 2026, figures «a 1 de mayo de 2023» from annex IV of the Plan de Contingencia) and names no
  comunidad. «información general, no un consejo veterinario» is added where the English has only an implicit caveat.
- Apple's Exercise ring is «actividad moderada» (Apple Spain), where the English says "brisk activity"; «anillo Ejercicio verde».
- Observa "baseline" in prose is «referencia» (the app's «Estableciendo tu referencia», the searched «valores de referencia vfc»); I-0414
  tracks the pages that still say «línea base». «Tu rango habitual» for "your usual range"; Apple Health chart label «Intervalo».
- Gym vocabulary: «torso/pierna» (Upper/Lower), «empuje, tirón y pierna» once for PPL, «serie principal (top set)», «series de back-off»,
  «barras de seguridad», «reinicio» or «bajar la carga» for a load reset (never «bajada de peso»), «personas sin experiencia» for untrained
  subjects, «repetición máxima (RM)» once.
- GymLogger X plateau states on the site are the analytics strings «Estancamiento», «En observación», «Estancamiento previsto» (I-0190 lists
  the app's other forms); «Progreso de fuerza», «Tabla de máximos». LiftLog review labels Progresaste, Mantén, Fallado, Descarga (catalog).
- MediaKit labels (catalog `es`): «Comprimir vídeo», Modo, «Tamaño objetivo», Avanzado, «Resolución máx.», Códec, «Tasa de bits de audio»,
  «64 kbps (voz)». AfterShift «Línea de recuperación» (Recovery Timeline). Pawza reminders: Repetición, Nunca, Urgente, Atrasado, Hoy,
  «Esta semana», «Más tarde», «Supera los modos de concentración».
- US tipping post: US rules and dollar amounts stay, written `20 $` with U+00A0 and decimal comma; agencies in Spanish with the English name once.
- Turnos rotativos: the ET defines «trabajo a turnos» (art. 36.3), not the phrase; the 12-hour rest is «con carácter general» (art. 34.3, with
  34.7 exceptions); NTP 455 hedges kept («no parece haber acuerdo», «se recomienda», «podría situarse»); NTPs are non-binding good practice.
- Hub keywords are brand-led and never a post's primary query.

## Decisions from Tier 4 batch 2 (2026-11-19)

- Spanish health pages: authoritative sources (MedlinePlus en español, Sociedad Española de Sueño, NHLBI en español, Fundación Española del
  Corazón, Apple es-es) carry the facts. Commercial health blogs (canalSALUD/Mapfre, OXIGEN salud, Acofarma) may appear only attributed by name
  and date as information pages that disagree, never as a norm, never in the quick_answer, and never as the base of a derived calculation.
  MedlinePlus is named once as a US government site in Spanish; «911» becomes «el número de emergencias» (no 112 unless a source says it).
- A range from a page that doesn't say «en reposo» is not presented as a resting range (Fundación Española del Corazón: «frecuencia cardiaca
  normal»). Apple writes «app Frecuencia cardiaca» on support 120277 and «Frecuencia Cardiaca» in title case on 120276 and the Watch guide.
- EU pet travel: since 22 April 2026 Implementing Regulation (EU) 2026/705 sets the passport model; older models stay valid by issue date
  (MAPA entry note). Serology on return depends on Annex I and II of Regulation (EU) 2026/636, not only the «equivalent countries» list.
  EUR-Lex returns nothing to curl: cite the DOUE text through the BOE mirror and the MAPA pages.
- Competitor USD amounts on journal posts follow the Tier 3 batch 4 rule (Brick's one-time price dropped, the billing model kept).
- Pretérito perfecto for recent or undefined past in Spain («las apps que has bloqueado»), not the indefinido.
- An app blocker's screen is «escudo» (defined once), never «pantalla de bloqueo» (Apple Spain's Lock Screen).
- MediaKit remux label «Mantener el original (remux)»; GymLogger X «Insertar semana de descarga», «Marcar como descarga»; «semana de descarga»
  with «deload» once; Soon. «Restaurar sugerencias», «modo plan», tab Plan.
- AllPaid's Fintonic paragraph on journal posts: only what the Spanish listing says (credit profile, loans, FinScore through openbanking,
  CreditBuilder «para darte recomendaciones»); never «de forma segura».

## Decisions from Tier 4 batch 3 (2026-11-19)

- Soon. has no event-type picker: it infers the type from English words in the title (blueprint §4.3), so a Spanish title gets the generic plan.
  Never write «elige el tipo Festivo/Boda»; say the type is deduced from English title words where a page lists the typed plans (I-0445).
- Apple iOS 27 (es-es iphb8f1bf206): Home Screen widgets via long-press, then the Editar button, then «Añadir widget» (not «+»). Apple Spain's Cardio
  Fitness is «Capacidad Aeróbica» and the Workout app «Entreno»; Preview's Quartz filter is «Reducción del tamaño de archivo».
- 2027 holidays: only the BOE resolution of 8 October 2026 (BOE núm. 254, 13 October 2026); regional days only as its annex lists them; weekdays
  computed and labelled as such.
- A derived minutes table is dropped when the authoritative figure's scope is unclear (NICHD «25 % del ciclo de sueño»): keep the attributed figure.
- Warm-up sets: GymLogger X counts them in tonnage but not in weekly set volume; LiftLog keeps them out of records and doesn't start the rest timer.
- ESCCAP España: frequencies only with their risk group and conditions; the 2017 modular guide's «al menos cuatro veces al año» and the 2021
  guide's group-A «1 a 2 veces» both dated and attributed; no product, ingredient, dose or price.
- salud.nih.gov blocks curl: cite through a dated Wayback snapshot and say so in the saved source.

## Tells to cut in Spanish (TRANSLATION.md 8.2, plus what reviews find)

Stock phrasing: «En el mundo actual», «En la era digital», «Sumerjámonos», «Adentrémonos», «Es importante destacar
que», «Cabe destacar que», «juega un papel fundamental», «sin lugar a dudas», «En resumen», «En definitiva»,
«no solo … sino también», «Ya sea que … o …», «descubre cómo», «lleva tu … al siguiente nivel», «potenciar»,
«optimizar» everywhere, «una experiencia fluida», «sin fisuras», «revolucionario», «de forma eficiente».

Found in Tier 1 reviews (2026-11-19): «estudio Apple» (reads as Apple's own studio: «estudio de apps para Apple»);
«desarrollador independiente de Apple» (reads as "independent from Apple"); «pensada para sentirse tranquila» (an app
doesn't feel: «hecha para usarse con calma»); «hablar con» a service ("talk to App Store Connect": «usar», «conectarse
con»); «¿Cómo ganáis…?» (vosotros to a one-person studio: impersonal); «cuentas» for restaurant bills next to «sin
cuentas» (accounts): «la cuenta del restaurante», «tickets»; «traslada solo…» / «pasan solas al siguiente» for
carry-forward (ambiguous or adds "next day": «avanzan solas»); «Conseguir» for the Get button («Obtener»); slogan
fragments such as «cero rastreo»; French typography (U+202F) left in a Spanish file. From the app-page and privacy
reviews: «la App Store» (feminine); «ID de Apple» (now «cuenta de Apple»); «Apple Salud» (Apple Spain: «Salud de
Apple»); «con una pulsación larga» («mantén pulsado»); «armar» («montar»); «directo» as an adverb; «recoge datos»
(«recopila»); «seguimiento» for tracking («rastreo»); «juego» for a "set" (reads as "game": «serie»); «N idiomas» for
"N localizations"; «aprender» standing in for "training"; «una solución más corta» for "the shortest solution";
«cuenta atrás» for a game timer; «Incluido en En familia»; «tiene que no encajar» (double negation); English
third-person headings turned into imperatives («Reclama el dinero…»); «El usuario…» in summaries («Alguien…»);
gendered «Eres desarrollador», «¿Atascado?»; a keyword noun in apposition in prose («una app recordatorio de
pagos»); «a nivel de palabra»; absolute gerunds («con iOS decidiendo»); periods at the end of who_for bullets;
multi-word UI labels left unquoted; merged FAQ questions that add a framing sentence; «te lee» (French calque);
«Sobre nosotros» for a one-person studio; raw keyword-style H1s («Cancelar suscripción iPhone: …»).

Found in the Tier 2 reviews (2026-11-19): «queda de tu mano» for "is left to you" («corre de tu cuenta»); «adelantar» for
carry-forward (reads as "move earlier": «pasa a hoy»); «una buena dormida» («un buen descanso»); «ibas tarde» for "feel behind"
(«ibas con retraso»); «la vida se interpone»; indicative where Spanish needs the subjunctive («donde no te cuesta», «la próxima
vez que la abres»); gendered audience words («harto», «despierto», «atrapado»); raw keyword seo.titles without «de/para»
(«Mejores apps salud Apple Watch»); «sin rachas» for Taskful Day (fact trap: Análisis shows streaks); «dejan con ganas de más»
for "unsatisfying" (means the opposite); «la parte honda de la piscina»; «escrito por autores» ("authored"); «estancamiento» for
stalemate («ahogado»); «la jugada mejor»; a keyword prefixed onto an H2; a capitalised tab name used as a common noun
(«y Análisis que…»); an unconditional `{{ t.english_marker }}` inside JSON-LD text; «hacer ganar la apertura» ("earn the open");
a heading promising something about every app when only some were checked («Lo que ninguna app … puede hacer»); «pase lo que
pase» on a system setting; «guía honesta» / «(2026)» sales padding in seo.titles; «seguimiento» for tracking (Spain: «rastreo»);
missing U+00A0 before % and € (none of the Tier 2 writers typed it). Batch 2 reviews: «ránking» («partidas clasificatorias», «rango»); «X es
la otra dirección» (French calque); «Es otro trabajo» ("a different job"); «pierde con convicción» ("loses convincingly");
«dejes de dejar»; «la editora de esta guía» (reads as a woman editor: «quien publica esta guía»); a blanket «ninguna app está
en español» when our own app in the table is; «para iPhone para quien…»; «quedarse con las claves» (can mean "steal": «no
compartir»); «sostenible» for a habit («funciona a la larga»); «para funcionar» on a competitor whose
listing gives a narrower purpose; a competitor's business model under a "costs" heading; «es un punto… Además». Countdown review: «suman entre X y Y valoraciones» for a per-app
range («tienen entre X y Y… cada una»); «cronología de salida» (French calque: «iniciales»); «y por cuánto tiempo» in a heading;
«Lo recordamos cada vez que aparece» (a promise the page must keep); three «mientras que» in one card; mixed list items
(«…, y exportar…»). Competitor Apple Watch support: the listing's device list counts (Countdown Buddy names watchOS 11 although its
description doesn't mention the Watch). Competitor prices: Spanish App Store euro rows only,
«(App Store de España, consultado el …)» once per page; never US figures converted.

Found in the Tier 3 batch 1 reviews (2026-11-19): «compra integrada» («compra dentro de la app»); «Tú y tu grupo dependéis» (mixed register); «hace mucho más» about a competitor; «ver todas tus cuentas» when the listing gives no count; «no tiene préstamos» when the app has a Loans category; «es la mejor opción» for "the better pick" («encaja mejor»); «no indica ninguna app» about a listing («no muestra», «no consta»); «etiqueta de privacidad»; a FAQ question that raises the English claim («protege mejor tus datos» for "more private"); «la mayor comunidad» (unsourced superlative); «de X a Y €» built from mixed IAP rows; «compra única» for "a one-time option" («opción de compra única»); «sin suscripción obligatoria» placed so it attaches to the competitor («Whoop sin suscripción obligatoria: Observa»); «sin X, sin Y y sin Z» lists; the dated store line repeated in card, FAQ and note; «{P_LIFETIME} una vez» («de por vida»); `{{P_…}}` double-brace tokens (Liquid error: single braces only). Hub and llms tells (R-wiring): «encaja mejor» on every line; «solo en inglés» next to the «(en inglés)» marker; a card that opens on a noun phrase with no subject; a card naming the page's metric differently («recuperación» vs «preparación»); «las comparamos» after a singular; «jugar en directo» when the page doesn't say live; a hub keyword that a comparison page owns.

Found in the Tier 3 batch 2 reviews (2026-11-19): «Datos no recopilados» (Apple: «No se recopilan datos»); a literal «el sensor … que lleva el anillo» for "finger-based sensing"; «sin X, sin Y y sin Z» in a seo.description or CTA; «Si no quieres A, B ni C» opening a quick_answer; «encaja mejor» for both sides of one verdict; sibling pages (Splitwise, Settle Up) with the same seo.title or description skeleton; «Taskful Day: Habitica convierte…» (a colon that fuses two product names); «le va a quien» («es para quien»); «lo que lo motiva» (gendered «lo»: «lo que motiva»); «cubre más terreno»; a table row header that doesn't fit the competitor's cell; «1.131» (four digits take no separator); a title promising «opiniones» on a page with no reviews.

Found in the Tier 3 batch 3 reviews (2026-11-19): two colons in one sentence («… al lado: toca X para ver cuál …: lista»); a seo.description repeating a language fact already in the title and quick_answer; a bare «No:» opening a quick_answer; «X y una alternativa con…» as a description opener; «Apple Watch gratis» in a title (reads as a free watch); «sí está en español, y …» fusing two ideas; «equipamiento» where the app says «material»; «en su lugar» calquing "instead"; «merece una mirada» repeated; «arma» («monta»); «membresía» (Latin-American: «suscripción»); a reviewer «correcting» a sourced Apple label (check es-apple-terms first).

Found in the Tier 3 batch 4 reviews (2026-11-19): «X en español» in a seo.title when the page never says whether X has a Spanish UI; a seo.title that reads as if the competitor were free or lifetime («UniConverter gratis: alternativa de por vida»); title and description shapes reused across pages of one app («X gratis: alternativa…», «¿X gratis? …»); an unsourced «no es gratis del todo» reshaping the English billing fact; explaining the method in copy («figuraba en dólares… aquí no lo convertimos»); «se comprobaron… según la comprobación»; «comprobada el …» for an English page with no dated check («actualizada el …»); «un par de formatos» for "a format pair" («una combinación de formatos»); «una exportación por ejecución» for "single-file runs"; «enlaces a nubes» («conexión con servicios en la nube»); «tu dispositivo» inside a FAQ question the reader asks; «sin cuenta y sin conexión» as a feature line (reads as a lack: «no pide cuenta y funciona sin conexión»); «no registra solo» (reads "doesn't only": «automáticamente», «por sí solo»); «por su cuenta» next to «sin cuenta» («propias»); «construida en torno a» («gira en torno a»); «herramienta estrecha» («específica»); «lecciones con juegos de X» for "lessons by X"; «(compra universal)»; «te mantenga motivado», «tú mismo» (gendered); «4,5 sobre 5167 valoraciones» («4,5 sobre 5 en 5167 valoraciones»); «recibes uno gratis» where «uno» refers to the wrong noun; «No tiene X ni Y, tampoco Z» dodging a triad («No tiene X, Y ni Z»); «Wikipedia de verdad sin conexión» («totalmente sin conexión»); «en vivo» for a live API («en línea»); «doblan las reglas» («retuercen»); «con En familia» («admite En familia»); «y subiendo» for "and counting"; the page's query turned into a claim («Tare es un juego parecido a…»); writer-made groupings of store rows («packs de colores y de tableros»); capitalised writer-made names for competitor features that read as UI labels («Pase de temporada»); a footnote that contradicts the page's framing («antes de cambiar de app» on a companion page). Hub and llms tells (R-wiring-4): one card skeleton («X …; MediaKit …, y X conviene más …») reused across sibling cards; «es la opción» on neighbouring cards and lines; an llms verb whose subject slides to the engine («Stockfish … explica cada error»); an adjective on the wrong noun («un archivo ZIM gratuito» when only the app is free); «para jugar después de X» softening the verdict «empieza por X»; «limita el nivel gratuito a 1 GB» for a per-file limit; «, todas en español» on a Spanish page; a verdict justified by a fact that is no reason.

Found in the Tier 4 batch 1 reviews (2026-11-19): «cuentas» for arithmetic next to «cuenta» for the bill («cálculos»); «estás en buena compañía» for "you are in the majority" (drops the claim); «quedarse corto» for "missed" (one direction only); «unos puntos porcentuales» for "a few percent"; «la mitad más altas» for "half as high again" («un 50 % más»); «la horquilla de la etiqueta»; «bajada de peso» for a load reset; «quienes no entrenan» for untrained subjects; «sentadilleros»; «se movieron con fuerza en sentidos opuestos» for a strong inverse correlation; «X es honesta» for numbers («no engaña», «realistas»); «¿qué tal de dura?» («¿cómo de dura?»); «réstalo de 10» («réstaselo a 10»); «la constancia» for both adherence and accountability; «a las 6 u 8 semanas» for a range («entre las 6 y las 8»); indicative after «hasta que» / «cuando» about the future; «se siente como» ("feels like"); «en los altos miles»; «fisiología de consumo»; «tendencia sostenida al alza» for "consistently higher"; «espera que» for "expect" («cuenta con que»); «logarítmico-normal» («lognormal»); «el estrés vital», «un bebé nuevo»; «1,95 veces las odds» («una odds ratio de 1,95»); «donde no veas tu mano» («no te veas la mano»); «con holgura» for "loosely"; a legal «se tendrá en cuenta» hardened into «nadie debe»; «quien trabaja de noche» where the law says «trabajador nocturno»; «tu convenio puede…» added to a legal rule without a source; an Oxford comma in a lede. Process tells: writer keywords that Google suggest doesn't return (check before shipping); a hedge dropped from the quick_answer but kept in the FAQ; a writer-added hedge that contradicts the source («puede haber cambiado» when the source says «Actualmente»); a study's finding fused by a colon with the writer's own reasoning; read_time counted with Markdown and URLs; quoted labels capitalised unevenly; the hub's keywords taking the posts' primary queries. Wiring (R-wiring-t4): the «X lo explica / cuenta / resume nuestro artículo…» shape with the object fronted, repeated across sibling FAQ link sentences (five in one batch); a link sentence repeating its own anchor topic («Si viajas a Estados Unidos… sobre la propina en Estados Unidos»); «cuántos pasos al día dar» («cuántos pasos dar al día»); «porque» in an llms Razón that makes a cited study the reason for a recommendation; a routed query with no fact for it in the Razón; «Epley calcula» (a formula is, it doesn't calculate); «dice con claridad» padding; a hub lead repeating the quick_answer below it; U+00A0 missing before kg, %, $, MB, GB in new llms lines; an llms line still routing a keyword its page gave away.

Found in the Tier 4 batch 2 reviews (2026-11-19): «pantalla de bloqueo» for a blocker's shield; pretérito indefinido for recent past («bloqueaste», «te fuiste»); «limitarse a uno mismo»; «X es incoherente» for "inconsistent"; «comparar notas»; «reponderar»; «en su lugar» in an H1; «los deshacer»; a writer-added link sentence claiming what the linked page does; «de [el artículo…]» before a link («del»); «El contexto del artículo» for "background" («la introducción»); «planas» for flat reps; «llegar a un pico en un básico»; «empujar con honestidad»; «Esta página da…» meta openers; a source sentence translated near-verbatim in both body and FAQ of a local-only page; unsourced boilerplate («la técnica va antes que el peso»); a levers table listing something the source doesn't count; «tu propia costumbre» for "baseline"; a non-resting range presented as resting; a «cálculo orientativo» on non-authoritative percentages promoted into the quick_answer; «Por el nombre, X es…» inferences; «no solo el profundo» tacked onto a source sentence; «hablar con» between systems; trailing «, buscando…» in FAQ answers; «la ficha de la app» for our own app page; «Guarda la lista» reading as an imperative; «o sea»; «basta o casi»; «X lo dice así:» + a near-verbatim official sentence; «de pago único» for lifetime («de por vida»); an unsourced timing for an app notice; circular definitions («sin fines comerciales: … sin finalidad comercial»); scope drift («fuera de esa lista» when the rule's list is wider). Wiring (R-wiring-t4b2): a Razón announcing «ocho registros (…)» and listing seven; a pronoun carrying a stronger claim than the post («VLC lo hace» = a lossless remux the source doesn't confirm); comma-joined Razón clauses that rebind a noun; hub or Blog summaries promising more than the post («cuáles no tienen anuncios»); a scoped, hedged finding made general; a link sentence restating the table above it; «descargar» alone for a deload (reads as download); a document as the subject of «pedir»; «válidos» for what a source only calls «se aceptan en los controles»; a hub list mixing a field with single metrics; an app page keeping keywords that a post or another app page now owns (Tare had two).

Found in the Tier 4 batch 3 reviews (2026-11-19): «gesto» for a task; «tocar internet»; «la larga cola de herramientas»; «gratis sin pagar»; generic «uno» («se puede quedar uno solo con…»); «pulsa Guardar» for a Mac button (Apple: «haz clic en»); an H1 offering Apple apps as «o» options for a task the post says they don't document; a heading promising «por qué» that the body never answers; a «gratis» keyword on a page whose tool needs Pro after 3 days; a «cálculo orientativo» on a figure of unclear scope; writer-added «consulta con tu médico si…» lines; «X lo dice casi igual:» + verbatim; «Solo cuentan A, B y C» for Apple's «como A, B, C»; a dropped hedge in a symptom list; one disclaimer sentence repeated in every section; 12-hour times («las 3 de la tarde»: «15:00»); gender agreement after a feminine noun («no apuntan todos»); «se establecen / se controlan» for a source's «deben / deberían»; an ambiguous object clitic; «del año que viene» in an evergreen post; «de la UE» for a list with non-EU countries; an H1 used as anchor text; a type picker or UI step described from a writer's assumption (check the app code or blueprint §4). Wiring (R-wiring-t4b3): a regional count stated as universal, dropping the post's exception (Canarias); the 3rd or 4th routed query with no fact in the Razón (check the last queries first); «ni A, ni B ni C» with a comma; singular «Ninguna fuente…» followed by plural «recomiendan»; a relative «que» after a list attaching to the last item; «deduce el tipo de las palabras» («a partir de»); unsourced demand claims in link sentences («fechas muy buscadas»); hub lists mixing noun phrases with clauses; a hub seo.description not updated when topics grow.

Translationese: title case headings; missing ¿ and ¡; chains of gerunds copied from English -ing («ofreciendo»,
«permitiendo», «haciendo» trailing a sentence); passive «es … por» where Spanish uses «se»; possessives on body
parts and devices copied from English («tu teléfono» is fine, «levanta tu mano» is not: «levanta la mano»);
«usuario» everywhere where Spanish says «tú» or «quien»; «aplicar» for "apply for"; «en orden a»; «a nivel de».
Latin-American vocabulary on this Spain site (celular, computadora, agregar, reporte, ingresar, cuenta regresiva,
puntaje) and vosotros forms on the future Mexican site.

## House rules carried over

- No public roadmaps or dated promises. Describe what an app does today.
- Prices only through tokens. No arithmetic on our prices.
- «Sin suscripción» only for LiftLog, Millrace, Mockly and Tare. For the others «sin suscripción obligatoria» or
  «opción de por vida», where true.
- «Tranquila» / «calmada» and «respetuosa con la privacidad» once, where they state positioning.
- Never the owner's personal name. Attribute to "Lagerland Apps".
- Millrace's copy never mentions the number title it replaced; Observa's HRV is SDNN, never RMSSD.
- App names, competitor names and "Lagerland Apps" as written in English.

## Review log

All Tier 1 pages, 2026-11-19. Writers: Sonnet agents, one per page (support stubs three per writer, privacy policies
three or four per writer). Reviewers: separate agents that did not write the pages, running the full copy-editing
skill, a fact diff against the English page, a glossary check against each app's Spanish string catalog and SEO
limits. Back-translation by fresh agents that never saw the English, compared claim by claim with the English page:
home, all 21 app pages, about. Native review: none yet, for every page (NATIVE REVIEWER: none).

| Pages | Writer | Reviewer | Back-translation | Native |
|---|---|---|---|---|
| /es/, /es/apps/ | 2 writers | 1 reviewer | home: 4 meaning shifts fixed | no native review yet |
| 21 app pages | 21 writers | 4 reviewers (5 to 6 pages each) | all 21: about 45 meaning shifts fixed | no native review yet |
| 21 support pages | 7 writers | 1 reviewer | n/a | no native review yet |
| 21 privacy policies + Clippet terms | 7 writers | 4 reviewers, sentence by sentence | n/a | no native review yet |
| about, support hub, transparency | 3 writers | 1 reviewer | about: 1 fix | no native review yet |
| /es/llms.txt, /es/llms-full.txt | 1 writer | 1 reviewer | n/a | no native review yet |
| Tier 2 batch 1: 4 guides | 4 writers (Sonnet) | 1 reviewer | n/a | no native review yet |
| Tier 2 batch 1: 3 audience pages | 3 writers (Sonnet) | 1 reviewer | n/a | no native review yet |
| Tier 2 batch 1: local-only screen-time guide | 1 writer (Sonnet), sources saved | 1 reviewer, every source re-fetched, claim by claim | n/a | no native review yet |
| Tier 2 batch 1: both hubs, llms.txt lines, inbound-link sentences | 1 writer (Sonnet) + main session | 1 wiring reviewer | n/a | no native review yet |
| Tier 2 batch 2: shogi guide, bill tracker (Fintonic) | 2 writers (Sonnet) | 1 reviewer each; Fintonic listing re-fetched | n/a | no native review yet |
| Tier 2 batch 2: local-only countdown guide | 1 writer (Sonnet), sources saved | 1 reviewer, sources re-fetched, claim by claim | n/a | no native review yet |
| Tier 2 batch 2: hub cards, llms.txt lines, AllPaid and Soon. link sentences | main session | 1 wiring reviewer | n/a | no native review yet |
| Tier 3 batch 1: 9 comparisons + local-only Fintonic page | one writer agent (Sonnet) each | reviewers R-money (14 must-fix), R-chess-pdf (6), R-health-screen (23), 2026-11-19 (copy-editing, fact diff against English and the Spanish store check, glossary, SEO/schema): e.g. Fintonic «no tiene préstamos» and «todas tus cuentas» fixed, Lichess unsupported «mayor comunidad» cut, PDF Expert price range removed, Whoop title moved off «Whoop sin suscripción obligatoria», Hevy Ladder card restored, Opal Watch claim softened to «No consta» | n/a (Tier 3) | no native review yet |
| Tier 3 batch 1: hub, 10 llms.txt lines, bill-tracker guide link | one writer (Sonnet) + main session | R-wiring (about 12 must-fix: hub verdicts added, Whoop card metric, llms verdict variety, Lichess line answers the «o» query) | n/a | no native review yet |
| Tier 3 batch 2: 9 comparisons + local-only AppBlock page | one writer agent (Sonnet) each | reviewers R-health-2 (9 must-fix), R-gym-split-2 (11), R-screen-habit-2 (16), 2026-11-19: e.g. Bevel FAQ «¿Observa es más barata que Bevel?» restored, AutoSleep price removed, Oura «Estableciendo tu referencia» quoted and the five-night fact corrected, AppBlock En familia and Watch rows fixed from the store page, Jefit «sin X, sin Y» lists rewritten, Settle Up title moved off the Splitwise pattern | n/a (Tier 3) | no native review yet |
| Tier 3 batch 2: hub (20 cards), 10 llms.txt lines, screen-time guide links | one hub writer (Sonnet) + main session | R-wiring-2 | n/a | no native review yet |
| Tier 3 batch 3: 10 comparisons + I-0372 chess-guide fix | one writer agent (Sonnet) each | reviewers R-health-3 (8 must-fix), R-gym-3 (21), R-misc-3 (15), 2026-11-19: e.g. Documents Mac platform removed (iPad app on M1), Chessable Pro trial restored, Strong «Strong o Hevy» section trimmed to sourced facts, StrongLifts program names from the app catalog, Wikipedia app UI names described plainly, Athlytic double «en español» removed | n/a (Tier 3) | no native review yet |
| Tier 3 batch 3: hub (30 cards), 10 llms.txt lines | one hub writer (Sonnet) + main session | R-wiring-3 | n/a | no native review yet |
| Tier 3 batch 4: 12 comparisons | one writer agent (Sonnet) each | reviewers R-files-4 (21 must-fix), R-health-plan-chess-4 (44), R-games-read-4 (37), 2026-11-19: e.g. a `{{P_LIFETIME@mediakit}}` double-brace token, HandBrake and UniConverter titles that promised false or unanswered facts, iZip card claiming MediaKit extracts more formats, RISE «no registra solo» ambiguity and US-store attribution restored, HRV4Training dropped check date restored, Two Dots 5000 vs 7600 levels attributed, Kiwix rating removed (not on the English page), app-page keywords removed from comparisons | n/a (Tier 3) | no native review yet |
| Tier 3 batch 4: hub (42 cards, new «Juegos de lógica» section), 12 llms.txt lines, logic-guide markers, Observa FAQ link | main session | R-wiring-4 (19 must-fix: all 12 cards rewritten for verdict variety and page metrics, 4 llms lines, hub quick_answer, Observa FAQ) | n/a | no native review yet |
| Tier 4 batch 1: 9 journal posts + local-only turnos-rotativos | one writer agent (Sonnet) each | reviewers R-gym (4 posts, ~45 fixes), R-money-media (2, ~25), R-health-pet (3, ~55), R-turnos (1, ~35), 2026-11-19 (copy-editing skill, sentence-by-sentence fact diff, every Spain source re-fetched live, UI strings from the GymLogger X, LiftLog, MediaKit, Observa, Pawza and AfterShift catalogs, SEO): e.g. two dropped hedges restored (RPE quick_answer, «Gains start low»), «6 u 8 semanas» range fixed, rabies section cut to what the MAPA note says, NTP 455 hedges restored and checked against the verbatim INSST text, MediaKit labels from the catalog, keywords without suggest replaced | n/a (Tier 4) | no native review yet |
| Tier 4 batch 1: hub, 10 llms.txt lines, Blog lines, 11 inbound-link sentences on 8 app pages, GymLogger X related_journal anchor | main session | R-wiring-t4 | n/a | no native review yet |
| Tier 4 batch 2: 5 translations + 5 local-only posts | one writer agent (Sonnet) each | reviewers R-plan-screen (3 posts, ~50 fixes), R-gym-2 (2, ~45), R-health-2 (2, ~40), R-money-pet-media (3, ~45), 2026-11-19 (copy-editing skill, fact diff, every source re-fetched live incl. PDFs via PDFKit, UI strings from the GymLogger X, Soon., Millrace, EarnLock, MediaKit, Pawza and Observa catalogs, keywords checked in suggest): e.g. a wrong serology scope on the passport page fixed, the deep-sleep minutes table built on commercial percentages removed, a Fundación del Corazón range no longer called «en reposo», two unsourced claims and a near-verbatim ACSM passage cut from the overload post, the Brick USD price dropped | n/a | no native review yet |
| Tier 4 batch 2: hub text, 10 llms.txt lines, Blog line, link sentences on 7 app pages, 2 related_journal anchors, home keywords, 2 batch-1 post sentences | main session | R-wiring-t4b2 | n/a | no native review yet |
| Tier 4 batch 3: 1 translation + 9 local-only posts | one writer agent (Sonnet) each | reviewers R-health-3 (3 posts, ~50 fixes), R-media-3 (3, ~45), R-soon-gym-pet (4, ~55), 2026-11-19 (copy-editing skill, fact diff, every source re-fetched live incl. the BOE annex parsed row by row and the ESCCAP and Apple whitepaper PDFs, UI strings from the Soon., MediaKit, GymLogger X, LiftLog, Observa, AfterShift and Pawza catalogs and code): e.g. Soon.'s non-existent type picker removed, the REM minutes table dropped, Apple's Editar step, near-verbatim passages paraphrased, three unsourced see-a-doctor lines cut | n/a | no native review yet |
| Tier 4 batch 3: hub text, 10 llms.txt lines, Blog line, link sentences on 6 app pages, MediaKit and AfterShift keywords, countdown-guide Editar fix, plan-mode caveat, 3 back-links | main session | R-wiring-t4b3 | n/a | no native review yet |

## Apps still on English screenshots

MediaKit and Mockly (2026-11-19). The other 19 apps already had complete Spanish sets in `assets/screenshots/<slug>/es/`
from commit 763463c («localized sets for 16 languages»), so their pages and OG cards show Spanish screenshots.
