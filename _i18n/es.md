# Language sheet: Spanish (es), Spain

Never published (`_i18n` is excluded from the build). Rulebook: TRANSLATION.md. Read this sheet before writing or
reviewing any Spanish page. Every decision a translator would otherwise make differently per page lives here.

## Status

| Item | Status |
|---|---|
| Setup (config default, locales.yml block, `_data/i18n/es.yml`, sitemap and feed stubs) | done 2026-11-19 (es.yml written by one agent, reviewed and copy-edited by another: 42 values changed) |
| Keyword research (Tier 1) | done 2026-11-19 from Google suggest, Bing, App Store hints and the iTunes Search API; Search Console for Spain not read yet (no access this session) |
| Tier 1 pages | done 2026-11-19, no native review yet: home, apps hub, 21 app pages (Clippet unlisted), 21 support pages, 21 privacy policies + Clippet terms, about, support hub, transparency (+ `_data/i18n_transparency/es.yml`), /es/llms.txt, /es/llms-full.txt, 21 OG cards. Commits 6a83675 (batch 1), ac4a1a3, e6e2231, 3857ea6, cfaed65 (batches 2 to 5), then AI files and go-live |
| Live | no, `live: false` |
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
| AllPaid | `app recordatorio de pagos` | `app para recordar pagos`, `app control suscripciones` |
| AppMeta | `app store connect mac app` (developers search in English) | `app store connect for mac`, `aso app store` |
| AppMeta Pulse | `app store connect iphone` | `app store connect ios`, `app store connect api` |
| Chessful | `aplicación ajedrez` | `aprender ajedrez app`, `análisis de partidas de ajedrez` |
| EarnLock | `bloquear apps iphone` | `bloqueador de aplicaciones`, `limitar tiempo de pantalla` |
| GymLogger X | `app gimnasio apple watch` | `app para registrar entrenamientos gimnasio`, `app de entrenamiento apple watch` |
| LiftLog | `app registro gimnasio` («sin suscripción» has no demand; kept in the title as the differentiator) | `app seguimiento gimnasio`, `app de pesas` |
| MediaKit | `comprimir video iphone` | `comprimir pdf iphone`, `convertir video a mp4 iphone` |
| Millrace (never write the number title) | `juegos de lógica iphone` | `juegos de lógica sin anuncios`, `mejores juegos de puzzle iphone` (`juegos de ingenio iphone` goes to Tare) |
| Mockly | `screenshots app store` (developers type the English; «capturas app store» has no demand) | `app store screenshot generator`, `mockup app store`, `app store screenshot maker` |
| Observa | `hrv apple watch` («hrv» alone is Honda HR-V noise) | `variabilidad frecuencia cardiaca`, `app sueño apple watch`, `app hrv apple watch` |
| Pawza | `cartilla veterinaria digital` («cartilla» is the Spain word; «carnet de vacunación» is Latin-American) | `app cartilla de vacunación perros`, `app salud mascotas`, `calendario vacunación perros` |
| RightSplit | `app para dividir cuenta restaurante` (bare «dividir cuenta» is arithmetic noise; «pagar a escote» is the Spain idiom) | `app dividir gastos`, `dividir cuentas entre amigos`, `calculadora dividir cuentas` |
| Shogiful | `shogi` | `ajedrez japonés`, `como se juega al shogi`, `aprender shogi` |
| Soon. | `cuenta atrás iphone` | `widget cuenta atrás`, `app cuenta atrás`, `contador de días app` |
| Tare | `juegos de ingenio iphone` (moved from Millrace to avoid two pages on one query; «juego de balanza» is a kids' maths audience) | `mejores juegos logica iphone`, `juegos de logica sin anuncios`, `mejores juegos de puzzle iphone` |
| Taskful Day | `app lista de tareas` | `app planificador diario`, `app to do list`, `app para organizar el dia` |
| WanderWiki | `wikipedia aleatoria` (tiny demand; intent is Wikipedia's own random page) | `wikipedia aleatorio`, `wikipedia al azar`, `app wikipedia` |
| Xiangqiful | `ajedrez chino` (title carries both «ajedrez chino» and «xiangqi») | `xiangqi`, `ajedrez chino como se juega`, `ajedrez chino reglas` |
| Clippet (unreleased, unlisted) | `historial portapapeles iphone` | `historial portapapeles mac`, `gestor de portapapeles mac`, `app portapapeles iphone` |

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

Not researched yet. Candidates seen in the iTunes Search API results during keyword research are listed in
es-keywords.md per page.

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

## Apps still on English screenshots

MediaKit and Mockly (2026-11-19). The other 19 apps already had complete Spanish sets in `assets/screenshots/<slug>/es/`
from commit 763463c («localized sets for 16 languages»), so their pages and OG cards show Spanish screenshots.
