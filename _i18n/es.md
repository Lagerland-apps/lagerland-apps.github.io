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
| Pawza | `cartilla veterinaria digital` («cartilla» is the Spain word; «carnet de vacunación» is Latin-American) | `app cartilla de vacunación perros`, `app salud mascotas`, `calendario vacunación perros` |
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

## Apps still on English screenshots

MediaKit and Mockly (2026-11-19). The other 19 apps already had complete Spanish sets in `assets/screenshots/<slug>/es/`
from commit 763463c («localized sets for 16 languages»), so their pages and OG cards show Spanish screenshots.
