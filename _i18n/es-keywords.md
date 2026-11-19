# Keyword research, Spanish (Spain)

Part of the language sheet `_i18n/es.md`. Two research passes on 2026-11-19 (part 1: studio pages and ten apps; part 2: the other eleven apps). Sources: **G** = Google suggest (hl=es, gl=es), **B** = Bing autosuggest (qsonhs, mkt=es-ES; the osjson endpoint returned HTTP 204), **A** = App Store search hints (storefront 143454-8,29, Spain/Spanish), **S** = iTunes Search API (country=es). Every query was returned by one of them. People also ask was not collected (it needs a live results page). Search Console for Spain was not read this session.

Owner-facing decision recorded in the sheet: Tare and Millrace both drew the «juegos de lógica iphone» family. Millrace keeps `juegos de lógica iphone`; Tare takes `juegos de ingenio iphone` (closer to its store name «Rompecabezas de lógica»), so the two pages do not compete.

## Part 1: studio pages, aftershift to millrace

Pages: Home, Apps hub, About, Support hub, Transparency, and the app pages aftershift, allpaid, appmeta,
appmeta-pulse, chessful, earnlock, gymlogger-x, liftlog, mediakit, millrace. Format follows `_i18n/fr-keywords.md`.

Collected 2026-11-19. Source marks: **G** = Google suggest (hl=es, gl=es), **B** = Bing autosuggest (mkt=es-ES),
**A** = App Store search hints (storefront 143454, Spain), **S** = iTunes Search API (country=es, lang=es_es),
used only for competitor names and the vocabulary in Spanish app titles. Every query below was returned by one of
these sources; nothing was invented. Accents: Google nearly always returns the unaccented form ("dormir despues de
trabajar de noche", "aplicacion ajedrez"), also when the seed had accents; I write the accented form where the
difference is only the accent and mark the source anyway. Search Console data is not included.

## Method note

- **Requests: about 660**, 0.8 s apart. Main run 395 (G 211, B 131, A 37, S 16), a Bing re-run 131, an extra
  round of 63 seeds on G and B (126), plus a few probes (A storefront suffixes, endpoint tests).
  118 seeds on G and B, alphabet suffixes (a b c d e f g h i l m o p r s t) on 5 seeds on G only: aplicación
  ajedrez, app gimnasio, sueño turnos, app recordatorio pagos, aplicaciones sin anuncios. 37 single-word or
  two-word seeds on A.
- **Google suggest: worked.** It needs a browser User-Agent. Alphabet suffixes were very productive for
  "aplicación ajedrez" (47 distinct suggestions) and "app gimnasio" (93, many local gym brands); they gave
  almost nothing for "sueño turnos" and "app recordatorio pagos". G mixes Latin American results into hl=es gl=es
  (colombia, mexico, peru, "celular"), so each pick below is a phrase that is also natural in Spain.
- **Bing osjson (`api.bing.com/osjson.aspx?query=&mkt=es-ES`): failed after the first probe.** One probe returned
  data; the 131 queries of the main run came back empty (HTTP 204), probably throttled, so I re-ran every seed on
  the sibling endpoint **`api.bing.com/qsonhs.aspx?mkt=es-ES&q=`** (the same Bing autosuggest), which worked. All B
  marks come from that endpoint. Bing is noisy: loosely related queries, Latin American phrasing ("celular",
  "computadora") and many generic "cómo ..." questions.
- **App Store hints (MZSearchHints, header `X-Apple-Store-Front: 143454-8,29`, `Accept-Language: es-ES`):**
  worked for single words and short seeds, empty for 3+ word seeds and for "mejores aplicaciones",
  "trabajo nocturno", "límite de apps", "registro entrenamiento", "sin suscripción". Suffix `-1` returned identical
  Spanish hints to `-8`; I used `-8`. Hints are Spanish.
- **iTunes Search API (country=es): worked** for competitor names (16 searches). Spanish title style:
  "Nombre: Palabra clave" or "Nombre - Palabra clave", English tails common.
- **People also ask: not collected.** It needs a live Google results page and a plain fetch would hit the consent
  wall; I did not try. FAQ items come from question-style suggest ("cómo", "mejor", "qué es") on G and B.
- **Weak spots:** Spanish suggest returns nothing, or only noise, for the privacy and studio themes (Home, About,
  Transparency): "aplicaciones sin rastreadores", "aplicaciones sin seguimiento", "aplicaciones que respetan la
  privacidad", "estudio de aplicaciones independiente", "seguimiento de apps iphone", "etiquetas de privacidad app
  store", "desarrollador de apps finlandia". It also returns nothing for every "sin suscripción" gym seed ("app
  gimnasio sin suscripción", "app entrenamiento sin suscripción", "app musculación sin suscripción", "app fitness sin
  suscripción", "app gimnasio pago único"), for "app recordatorio facturas", "app sueño trabajo por turnos",
  "informes de ventas app store", "metadatos app store", "palabras clave app store", and for the earn-by-moving
  mechanic ("app caminar para desbloquear", "app pasos desbloquear apps", "bloquear apps hasta hacer ejercicio").
  For those pages the pick is the closest real phrase and it is said so.
- **Aplicación vs app vs appli:** both "aplicación" and "app" are typed. Casual and long-tail queries lean on
  "app" ("app ajedrez" returned 10 suggestions, "app gimnasio" 93 with suffixes, "app para recordar pagos"),
  while head phrases often use "aplicaciones" ("mejores aplicaciones iphone", "aplicaciones sin anuncios",
  "bloqueador de aplicaciones"). Apple's own Spanish UI says "aplicación". "Appli" is a French form and never
  appeared. Recommend "aplicación" in titles and H1 where the primary uses it, "app" in body copy and FAQ.
  "Móvil" (Spain) and "celular" (Latin America) both appear; use "móvil". "Ordenador" (Spain) vs "computadora"
  and "pc": Bing returns "computadora" and "pc", Google "pc"; for the Mac pages write "Mac" and avoid both.
- **Good sign:** our own Spanish App Store listing already shows in S: "AfterShift: Sueño y Turnos".
- **Spain-specific:** Apple's Spanish (Spain) name for Screen Time is "Tiempo de uso" (G: "tiempo de uso iphone"
  with many suggestions); Latin American iOS says "Tiempo en pantalla", and App Store titles use "Tiempo de pantalla"
  (A, S). EarnLock copy should use all three words once.

---

## Home (/es/): studio of privacy-first Apple apps

- **Primary:** `aplicaciones sin anuncios` (G). Caution: the demand is dominated by music, YouTube and films
  ("aplicaciones sin anuncios para escuchar música", "para ver películas", G; B the same). It is still the real
  Spanish phrase for "no ads", and the tail "aplicaciones sin anuncios gratis" (G) is generic.
- **Secondary:** `aplicaciones sin publicidad` (G); `aplicaciones sin anuncios gratis` (G); `apps privadas iphone`
  (G; weak, the only privacy-flavoured phrase returned and it is a different audience: hiding apps).
- **Not usable as primary:** `aplicaciones sin suscripción` (G): suggest returned only IPTV, dating and Adobe
  ("aplicaciones iptv sin suscripción", "de citas", "de adobe"), and the house rule limits "sin suscripción" to
  LiftLog, Millrace, Mockly and Tare anyway.
- **FAQ-style (from suggest):** none on-topic. Nearest: `como jugar juegos sin anuncios en iphone` (G) and, on B,
  `app para quitar anuncios`.
- **Notes:** "aplicaciones sin anuncios iphone" returned only music/YouTube tails (G: "aplicaciones para ver youtube
  sin anuncios en iphone"), "app sin publicidad iphone" returned nothing on G and ad-making tools on B ("app para
  hacer publicidad"). "Anuncios" is the Spanish word for ads in suggest, "publicidad" second. "Sin anuncios" also
  appears in A hints: "juegos sin anuncios", "ajedrez sin publicidad", "navegador sin anuncios", "hushclock: reloj sin
  anuncios". Privacy and tracking: "aplicaciones sin rastreo", "apps sin tracking" and "app que no recopila datos"
  returned only phone-tracking and data-collection noise ("aplicaciones de rastreo de celular"). Consumers do not
  type "privacidad" for apps; App Store titles do ("NordVPN - privacidad online", "AVG seguridad y privacidad", A).

## Apps hub (/es/apps/): all apps

- **Primary:** `mejores aplicaciones iphone` (G; B `mejores aplicaciones para iphone`, `las mejores aplicaciones para
  iphone`). Generic but it is the real phrase; pair it with the studio angle in the title.
- **Secondary:** `mejores apps iphone` (G; B `mejores apps para iphone`); `aplicaciones útiles para iphone` (G
  `aplicaciones utiles para iphone`, `aplicaciones mas utiles para iphone`; B `iphone 13 pro aplicaciones útiles`);
  `mejores aplicaciones mac` (G; also `mejores apps para mac` G).
- **FAQ-style (from suggest):**
  - mejores aplicaciones iphone gratis (G)
  - mejores apps apple watch gratis (G)
  - mejores aplicaciones ipad gratis (G)
  - aplicaciones imprescindibles iphone (G)
  - apps utiles para iphone (G)
  - cómo saber si una app es segura (B)
- **Notes:** G mixes in model names and years ("mejores aplicaciones iphone 17 pro max", "2026", "2025"); avoid
  dated titles. "Aplicaciones" and "apps" both sit at the head. Per-device versions exist for iPad
  (`mejores aplicaciones ipad`, G, mostly notes/study), Apple Watch (`mejores apps apple watch`, G, Ultra/SE models) and
  Mac (`mejores aplicaciones mac`, `mejores aplicaciones macbook`, G).

## About (/es/lagerland-apps/): one-person studio, Finland

- **Primary:** no real query found. Closest real phrases: `desarrollador de aplicaciones` (G, B; job-search intent:
  empleo, sueldo, trabajo, multiplataforma) and `desarrollador independiente` (B; G adds "en ingles", "web
  independiente", "de software independiente"). Recommendation: title on the brand ("Lagerland Apps") plus
  "desarrollador independiente" / "estudio independiente" in the description; this page ranks on brand, not on
  generic demand.
- **Secondary:** `desarrollador de aplicaciones` (G, B); `desarrollador de aplicaciones móviles` (G, B);
  `desarrollador independiente` (B).
- **FAQ-style:** none on-topic. G/B for "desarrollador de aplicaciones" are salary, jobs and tech-stack queries.
- **Not usable:** `desarrollador de apps ios` (G empty; B returned `programa para desarrolladores de apple`,
  `activar modo desarrollador ios`: wrong intent); `desarrollador de apps finlandia` (B: agencies in Seville and
  Mexico); `programador de apps independiente` (B: learn-to-code apps).
- **Notes:** "indie" is a game-developer word in Spanish ("desarrollador de videojuegos indie", G; `desarrollador
  indie` returned `desarrollador independiente`, B), so "independiente" is the safe word. Avoid "freelance" in copy
  (contractor intent, not tested but implied by the jobs results). Spain says "desarrollador" (also "programador").

## Support hub (/es/support/)

- **Primary:** `cancelar suscripción iphone` (G, B `cancelar suscripción en iphone`). Strongest support-type
  demand; fits the hub.
- **Secondary:** `restaurar compras app store` (G) / `restaurar compras apple` (G); `reembolso app store` (G, B
  `solicitar reembolso app store`); `cancelar suscripción app store` (G).
- **FAQ-style:**
  - cómo cancelar una suscripción en iphone (G, B)
  - cómo cancelar una suscripción de una app (B)
  - como cancelar una suscripcion en iphone y pedir reembolso (G)
  - como cancelar una suscripcion en iphone si no aparece la opción (G)
  - cómo eliminar suscripciones en iphone (B)
  - como dar de baja suscripciones de apple (B)
  - donde ver suscripciones activas en iphone (G)
  - como ver suscripciones apple (G; B `cómo ver mis suscripciones en apple`)
  - como restaurar compras iphone (G)
  - como pedir reembolso app store (G, B)
  - reembolso app store cuanto tarda (G)
  - historial de compras app store (B)
- **Notes:** Spanish uses "cancelar" (G, B), "dar de baja" and "eliminar" (B) for subscriptions, "reembolso" for
  refunds (also "devolución", not returned), "restaurar compras" (G) for restore. Everything returned is generic
  Apple, not per app: G shows `cancelar suscripción duolingo iphone`, `chatgpt`, `spotify`, so a per-app angle is
  not our page. "cancelar compra app store" (B) is a refund intent. The question seeds "cómo restaurar compras en app
  store" returned only Microsoft Store and password noise on B and the unaccented G echo; "contactar soporte app"
  returned only "contactar soporte apple" (G, B), for Apple itself. "recuperar compra integrada app" returned only
  deleted-app recovery (B).

## Transparency (/es/transparency/): tracking, SDKs, privacy manifests

- **Primary:** `app tracking transparency` (G, B `app tracking transparency att`). Spanish searchers type the
  English Apple term (and the developer ones: admob, xcode, flutter). No Spanish consumer phrasing has demand.
- **Secondary:** `app tracking transparency que es` (G); `privacy manifest` (G, B, English, developer
  audience); `aplicaciones que te rastrean` (G; the one consumer phrase returned, but the intent is mostly phone
  tracking).
- **FAQ-style:**
  - app tracking transparency que es (G)
  - what is app tracking transparency (B; English even with a Spanish seed)
  - que datos recopilan las apps (G, B)
  - cómo saber si una app es segura (B)
  - app tracking transparency iphone (G)
- **Not usable:** `seguimiento de apps iphone` (G empty; B: how to group apps); `permitir que las apps rastreen`
  (G empty; B: phone-tracking apps); `etiquetas de privacidad app store` (G empty; B: label-making apps);
  `cómo desactivar el seguimiento de apps iphone` (G empty; B: uninstalling apps); `apps que no recopilan datos`
  (G: `apps que recopilan datos`, the opposite; `app que no recopila datos` returned only definitions on B);
  `pedir a la app que no me rastree`, `qué es el seguimiento de apps` (noise); `aplicaciones sin seguimiento`,
  `aplicaciones sin rastreadores` (nothing).
- **Notes:** developer terms stay English: "privacy manifest" (B `itms-91061 missing privacy manifest` shows the
  upload error), "SDK", "App Tracking Transparency". Apple's Spanish UI says "Seguimiento" and "Permitir que las apps
  soliciten rastrear tu actividad" (from the OS UI, not a returned query); use that for the consumer-facing text.
  Demand for the topic itself is thin, so the page is a trust page, not a keyword page.

---

## AfterShift (shift-work sleep)

- **Primary:** `dormir después de trabajar de noche` (G `dormir despues de trabajar de noche`). The "turno de
  noche" form is a close twin: `como dormir si tengo turno de noche` (G). Write "trabajo a turnos y de noche" in
  the title area ("turnos" is the Spanish word in app titles: "Sueño y Turnos", S).
- **Secondary:** `trastorno del sueño por turnos de trabajo` (G, B; health intent, a related audience);
  `como dormir despues de un turno de noche` (G); `deuda de sueño` (G; also `deuda de sueño app`, `deuda de sueño
  calculadora`, `deuda de sueño sintomas`, G).
- **FAQ-style:**
  - porque no puedo dormir despues de trabajar de noche (G)
  - como dormir bien despues de trabajar de noche (G)
  - como dormir despues de un turno de noche (G)
  - como dormir si tengo turno de noche (G)
  - turno de noche no puedo dormir (G)
  - turno de noche cuando dormir (G)
  - se puede dormir en turno de noche (G)
  - como recuperar deuda de sueño (G)
  - se puede recuperar el sueño perdido (B)
  - que es el trabajo a turnos (B)
- **Competitors (S/A):** Sueño Trabajos por Turnos, ShiftNight: Monitor de sueño, ShiftRest: Plan Sueño y Turnos,
  Shiftrest: Sueno por Turnos, Peaks: Sueño y Energía, Diario de sueño y descanso. Roster apps (different intent):
  Shift Note: Cuadrante Turnos, ShiftKal: Agenda de turnos, Owlday: Calendario de Turnos, ShiftBell: alarma de
  turnos, Beepo: Despertador y Turnos. A hints for "turnos": turnos de trabajo, turnos enfermeria, turnos policía,
  calendario turnos, "crewshift: turnos y quedadas". Our listing: "AfterShift: Sueño y Turnos".
- **Notes:** "app sueño trabajo por turnos" (G empty; B: roster apps "aplicaciones para turnos de trabajo",
  "calendario de turnos app", "mejor app para turnos de trabajo gratis") and "app turno de noche" (B: roster) show
  the roster intent wins on "app" + "turnos". "trabajo nocturno sueño" (G empty), "trabajo a turnos sueño
  consejos" (G empty) and "app dormir turnos" (nothing) returned nothing. Spanish words: "trabajo a turnos",
  "turno de noche", "trabajo nocturno", "sueño", "deuda de sueño", "dormir", "descanso"; the roster word is
  "cuadrante" (S title). Caution: "sueño en el trabajo" (B) means sleepiness at work, not our topic.

## AllPaid (bill reminders, no bank login)

- **Primary:** `app recordatorio de pagos` (G; also `app para recordatorio de pagos`, G). Thin: G returns only
  these two for the seed and nothing for the alphabet pass.
- **Secondary:** `app para recordar pagos` (G; also `app para recordar pagos mensuales`, `app para recordar fechas
  de pagos`, G); `app control suscripciones` (G); `recordatorio de pago de facturas` (G).
- **FAQ-style:** none for reminders. Closest real phrases: `app para recordar fechas de pagos` (G), `calendario de
  pagos app` (G; but B shows pension-fund payment calendars, so weak).
- **Competitors (S/A):** Recordatorio de Pagos Facturas, Recordatorio Cuentas por Pagar, Bill Check: pagos y
  facturas, Recordatorio - BillSnap, Recuerda Pagar: Recordatorio, Billio: Recordatorios de pago, Facturas:
  recordatorio pagos, NoSeMePasa: Control de Pagos, Organizador de las Facturas, OnDue: Recordatorio Pagos,
  BillWell: Recordatorio Pagos (S, A "recordatorio pagos"); A "suscripciones": Renewio, Subtown, Subtrack, Subly,
  "suscripciones bajo control", "gestor de suscripción", "subpilot: cancelar suscripción".
- **Not usable:** `app gestión de facturas` (G `app gestion de facturas`; B `app para hacer facturas`: invoicing);
  `app recordatorio facturas` (G, B empty; B on "app para no olvidar pagar facturas" returned invoicing apps);
  `recordatorio de facturas` (G: overdue invoices for businesses, "vencidas"); `app presupuesto sin conectar
  banco` (G empty; B: quote-making apps); `app finanzas personales sin conexión bancaria` (B: generic finance
  apps); `app control de gastos fijos` (B: expense trackers).
- **Notes:** "factura" is double (a bill you pay vs an invoice you issue), as in French; in Spain a household bill
  is also a "recibo", but "recibo" in B means receipt-making apps ("app para hacer recibos"). Use "recordatorio de
  pagos", "vencimientos" (not returned, but competitor-like), "suscripciones", "contratos". "Sin conexión
  bancaria" has no echo. Both "pagos" and "facturas" appear in S titles.

## AppMeta (App Store Connect for Mac)

- **Primary:** `app store connect mac app` (G). Also `app store connect for mac` (G).
- **Secondary:** `app store connect for mac` (G); `aso app store` (G; also `aso app store keywords`, `aso app
  store tool`, `aso app store optimization`); `app store connect mcp` (B; a developer hook, a minor tie to the
  Pulse MCP angle, not for this page).
- **FAQ-style:** `que es app store connect` (G); `what is app store connect` (B); `app store connect crear
  cuenta` (G); `app store connect login` (G, B).
- **Competitors (S/A):** Lumetric for App Store Connect, AppDab for App Store Connect, Appdesk para App Store
  Connect, Appsales for App Store Connect, Big Bucks for App Store Connect, Helm for App Store Connect, MRRingo
  for App Store Connect, Peek for App Store Connect (A); ASO.dev: Copilot para Connect, KWRDS ASO Rank Keyword
  Tracker, Store Redirect, ASO View: App Rank Tracker, Review Buddy for App Store ASO, Picasso App Screenshot Studio
  (S), plus Apple's own App Store Connect, Apple Developer and TestFlight.
- **Not usable:** `palabras clave app store` (G empty; B: "app para poner clave", keyword-research definitions);
  `metadatos app store`, `optimización app store` (nothing); `app store connect aplicación` (B: "no se puede conectar
  a app store"). Caution: "app store connect mac" and "app store connect iphone" collide on G with the consumer
  error "app store cannot connect mac" / "cannot connect to the app store macbook".
- **Notes:** Spanish developers search in English ("app store connect", "aso", "app store optimization keywords").
  "ASO" in A alone is noise ("asos", "asobal"). Keep "App Store Connect", "ASO" and "metadata" in English in the
  title; the Spanish body can say "palabras clave" and "metadatos" without keyword evidence.

## AppMeta Pulse (App Store Connect dashboard on iPhone)

- **Primary:** `app store connect iphone` (G; also `app store connect app only for iphone`, G).
- **Secondary:** `app store connect ios` (G); `app store connect api` (G, B; also `app store connect api key`,
  G, B); `app store connect status` (G).
- **FAQ-style:** `que es app store connect` (G); `what is app store connect` (B); `app store connect login`
  (G, B); `app store connect crear cuenta` (G).
- **Competitors (S/A):** AppDab, Helm, Appdesk, Peek, Appsales, Lumetric, MRRingo, Big Bucks (all "for App Store
  Connect", A); Appboard: Ranking de App Store (S).
- **Not usable:** `app store connect ventas` (G empty; B: "app de ventas online"); `informes de ventas app store`
  (G empty; B: sales-report apps for shops); `ingresos app store desarrollador` (G empty; B: "cuánto cuesta
  desarrollar una app"). The Spanish money words returned nothing for developers.
- **Notes:** "MRR", "App Store Connect", "proceeds" stay English; the audience is developers. Same collision
  with the consumer error ("app store cannot connect iphone 17", G); keep "dashboard"/"ventas" in the title to
  separate it. Spanish title vocabulary for sales: "ventas", "ingresos", "informes" (none with suggest demand).

## Chessful (chess learning and analysis)

- **Primary:** `aplicación ajedrez` (G; B `aplicación de ajedrez`). Casual twin `app ajedrez` (G; also `app
  ajedrez sin anuncios`, `app ajedrez offline`, `app ajedrez iphone`, G).
- **Secondary:** `aprender ajedrez app` (G; B `app para aprender ajedrez`); `análisis de partidas de ajedrez` (G, B;
  B also `analizador de partidas de ajedrez`); `mejor app de ajedrez` (G; also `mejor app de ajedrez para iphone`,
  `para principiantes`, `sin anuncios`, `para ipad`, G).
- **FAQ-style:**
  - cómo mejorar en ajedrez (G)
  - como mejorar en ajedrez principiantes (G)
  - como aprender ajedrez desde cero (G)
  - como aprender ajedrez paso a paso (G)
  - qué aplicación de ajedrez es mejor (G)
  - cuales son las mejores aplicaciones de ajedrez (G)
  - mejor app de ajedrez para iphone (G)
  - mejor app de ajedrez para principiantes (G)
  - mejor app de ajedrez sin anuncios (G)
  - aplicación para entrenar ajedrez (G)
  - aplicacion para ganar en ajedrez (G)
  - aplicación de ajedrez sin anuncios (G)
  - app ajedrez offline (G)
  - stockfish que es (G); stockfish en español (G)
- **Competitors (S/A):** Ajedrez: Aprende,Juega&Entrena, Entrenador de ajedrez Lite, Lotus Chess – Entrenador,
  Táctica Ajedrez Gym: Entrenar, Chessy: Entrenador de Ajedrez, Chessable - Aprende ajedrez, Chessigma: Aprender
  ajedrez, Magnus Trainer: Curso Ajedrez, Play Magnus, Análisis Ajedrez: Chess AI, jquads: análisis ajedrez y PGN,
  Análisis Ajedrez - Chesslume, Take Take Take, Ajedrez: Análisis Stockfish, Gambit - Análisis de Ajedrez,
  MoveSense: Análisis Ajedrez, Lina Chess: Ajedrez y análisis, Ajedrez – Tablero de Análisis, Analizador de Ajedrez
  ChessFox, Ajedrez sin publicidad. A hints for "ajedrez": ajedrez gratis, online, para 2, "ajedrez: jugar y aprender",
  ajedrez niños gratis, ajedrez offline, "ajedrez: análisis stockfish". Our listing in Spanish: not seen in S.
- **Notes:** "ajedrez" is the word; "partidas" for games; "análisis" and "analizador". "Stockfish" typed as-is
  (`stockfish`, `stockfish en español`, `stockfish elo`, G). English leaks: "ajedrez online application", "app
  ajedrez chess". Big audiences: "niños", "gratis", "principiantes", "para jugar con amigos", "sin anuncios",
  "offline"/"sin internet". `mejor aplicación ajedrez iphone` returned only PC/Android noise on B and nothing on G,
  and `aplicación ajedrez sin conexión` likewise (G empty), so use the "app ajedrez offline" and "mejor app de
  ajedrez para iphone" forms. B and G also show "pc" and "android" as the dominant device words; the iPhone
  intent has to be stated on the page.

## EarnLock (earn screen time by moving: app blocker)

- **Primary:** `bloquear apps iphone` (G; A hint `bloquear apps` returns many app-title phrases:
  "train2scroll: bloquear apps", "app locker: bloquear apps", "bloquear apps y limitar tiempo"). The head
  term `bloqueador de aplicaciones` (G, A) is dominated by Android, PC and Windows, so the iPhone form isolates the
  intent.
- **Secondary:** `bloqueador de aplicaciones` (G, A `bloqueador de aplicaciones`); `limitar tiempo de pantalla`
  (G; A "tiempo de pantalla"); `bloquear instagram iphone` (G; also `app para bloquear instagram iphone`, G).
- **FAQ-style:**
  - cómo bloquear apps en iphone (B)
  - como bloquear apps en iphone con codigo (G)
  - app bloquear apps iphone (G)
  - como reducir el tiempo de pantalla en iphone (G)
  - como limitar el tiempo de pantalla (B)
  - aplicaciones para limitar el tiempo de pantalla (G)
  - estrategias para limitar el tiempo de pantalla (G)
  - tiempo de uso iphone no funciona (G)
  - app para usar menos el movil (G)
  - app para dejar el móvil (G)
  - cómo se llama la adicción al móvil (B)
  - aplicaciones para controlar el uso del móvil (B)
- **Competitors (S/A):** Opal: Tiempo de Pantalla Focus, one sec—tiempo pantalla y foco, Jomo - Reducir Tiempo
  Pantalla, Refocus: Bloquear Aplicaciones, AppBlock Bloquear Aplicaciones, Tiempo de Pantalla: Unplugged, Tiempo de
  Pantalla: Mi Diario, Freedom: Tiempo de Pantalla, Roots: Tiempo en Pantalla, Clarymind: Tiempo en pantalla, Seren:
  Tiempo de pantalla, Bloqueo De Aplicaciones Lock; A: Reptoll: bloqueador de apps, Train2scroll: bloquear apps,
  Mindgate, Screenpup, Acornlock, Palier, Wickstart, Pausi.
- **Not usable:** `app contra adicción al móvil` (G empty; B related definitions); the mechanic phrases
  `bloquear apps hasta hacer ejercicio`, `app caminar para desbloquear`, `app pasos desbloquear apps` (G empty; B:
  generic unlock and "desbloquear celulares" noise): the earn-by-moving idea has no Spanish query demand.
- **Notes:** "Tiempo de uso" is Apple's name for Screen Time on iOS in Spain (G: "tiempo de uso iphone" with 10
  suggestions: no funciona, código, contraseña, familia), "Tiempo en pantalla" is Latin American, and App Store
  titles say "Tiempo de pantalla" (A, S) and "límite de apps" got no A hints. Most G suggests for the screen-time words
  are about removing the code or the limit. "Bloquear" is the verb (also "bloqueo de aplicaciones" in titles). "Control
  parental" (S title) is another audience; children and parents are out of scope for the page.

## GymLogger X (strength workout tracker with Apple Watch)

- **Primary:** `app gimnasio apple watch` (G; also `app para gimnasio apple watch`, `mejor app gimnasio apple
  watch`, G).
- **Secondary:** `app para registrar entrenamientos gimnasio` (G; B shows `app para entrenar en el gym`); `app de
  entrenamiento apple watch` (G; B `app entrenamiento apple watch`, `app entreno apple watch`); `mejor app
  entrenamiento fuerza` (G; also `app entrenamiento fuerza gratis`, G).
- **FAQ-style:**
  - mejor app gimnasio apple watch (G)
  - mejor app entrenamiento apple watch (G)
  - como registrar entrenamientos en apple watch (G)
  - como registrar entrenamientos en iphone (G)
  - cual es la app de entrenamiento en apple watch (G)
  - como usar la app de entrenamiento en apple watch (G)
  - mejor app gimnasio iphone (G)
  - mejor app para rutinas de gimnasio (G)
  - mejor app para gimnasio gratis (G)
  - app para crear rutinas de gimnasio (G)
- **Competitors (S/A):** Hevy Rutinas Gym Entrenamiento, FitTracker - Diario de Gym, Gyminute: Registro de entreno,
  Gym Workout Tracker: RepCount, GymDone: Plan Entrenamiento, Fitwill: Registro de Entrenos, Diario de entrenamiento,
  Progression: Entrenamiento, BTB Diario de Gimnasio y Pesas, Plates: Diario de Gimnasio, VibeRep: Registro de
  Gimnasio, Gym Jotter - Diario de Entreno, Alpha Progression Musculación; A for "musculación": Gymaholic,
  AivancePro, Fitbrothers, Fitsse; A for "fuerza": Hitpr: rutinas gym y fuerza, Gravis: fuerza al fallo, "fuerza fit";
  G: "hevy app gimnasio".
- **Notes:** Spain says "gimnasio" and "gym" for the place, "entrenamiento" and "entreno" for the session, "rutina"
  for the programme, "fuerza" for strength, "diario" and "registro" for the log; "musculación" is typed
  (`app musculacion`, `app musculacion gratis`, G; `app musculation`, B returns the French form) but much less than
  "gimnasio". "Apple Watch" stays English. B for "app gimnasio apple watch" returned English and German
  ("best fitness app for apple watch", "fitness app für apple watch"), so little Spanish Bing demand. "Cuaderno" in
  A/S titles only ("Diario de Gimnasio" is the usual title form). Caution: "app gimnasio" alone is dominated by
  gym-chain apps and booking ("app reservas gimnasio", "app gimnasio smart fit", "app citas gimnasio"); keep "registro" or
  "entrenamiento" in the title.

## LiftLog (lifting log, one purchase, no subscription)

- **Primary:** `app registro gimnasio` (G alphabet pass), because the "sin suscripción" phrase has no suggest evidence:
  the strict primary would be `app gimnasio sin suscripción` and it returned nothing on G. "Sin suscripción" is
  allowed for LiftLog and should still lead the title as the differentiator, with the primary as the keyword.
- **Secondary:** `app seguimiento gimnasio` (G); `app de pesas` (G; also `app de pesas gratis`, `mejor app de
  pesas`, `app rutina de pesas`, G); `app para apuntar entrenamientos gym` (G).
- **FAQ-style:**
  - mejor app de gimnasio gratis (G)
  - mejor app gimnasio iphone (G)
  - mejor app de pesas (G)
  - app rutina gimnasio gratis iphone (G)
  - app musculacion gratis (G); mejor app musculación gratis (G)
  - mejores app de entrenamiento (B); mejores app entrenamiento gratis (B)
  - app para registrar entrenamientos gimnasio (G; shared with GymLogger X)
- **Competitors (S/A):** same pool as GymLogger X: Hevy Rutinas Gym Entrenamiento, FitTracker - Diario de Gym,
  Gyminute: Registro de entreno, Gym Workout Tracker: RepCount, Gym Jotter - Diario de Entreno, Plates: Diario de
  Gimnasio, BTB Diario de Gimnasio y Pesas, Progression: Entrenamiento.
- **Not usable (with note of demand):** all "sin suscripción" and "pago único" gym seeds returned nothing on G:
  `app gimnasio sin suscripción`, `app entrenamiento sin suscripción`, `app musculación sin suscripción`, `app
  fitness sin suscripción`, `apps de entrenamiento sin suscripción`, `app gimnasio pago único`. B returned
  gym-membership noise ("suscripción de gimnasio cerca de mí", "cómo cancelar suscripción en smart fit"). Generic
  `aplicaciones sin suscripción` (G) returned only IPTV, dating and Adobe. So the Spanish differentiator has no
  keyword demand; "gratis" has a lot ("mejor app de gimnasio gratis", "app rutina gimnasio gratis", G; "aplicaciones
  de entrenamiento gratis", B), which contradicts a paid-once offer: say the 7-day free trial only as far as the
  master file allows. `app para gimnasio gratis` (G) is the head of that "gratis" demand.
- **Notes:** the two gym pages share the head vocabulary; GymLogger X leads on "apple watch", LiftLog on "registro" /
  "pesas" and the pay-once angle. "Sin anuncios" and "sin cuenta" variants were not tested here.

## MediaKit (compress/convert video, images, PDF on device)

- **Primary:** `comprimir video iphone` (G, B `comprimir video en iphone`). Variants: `comprimir video desde iphone`,
  `comprimir video en iphone sin perder calidad` (G). G normalizes "vídeo" to "video".
- **Secondary:** `comprimir pdf iphone` (G, B `comprimir pdf en iphone`); `convertir video a mp4 iphone` (G, B
  `convertir video iphone a mp4`); `convertir heic a jpg` (G; also `convertir heic a jpg en iphone`, `en mac`, G);
  `compresor de videos` (G; for the generic head term).
- **FAQ-style:**
  - cómo comprimir un video en iphone (G, B)
  - como comprimir un video en iphone sin perder calidad (G)
  - como comprimir un video en iphone para enviarlo por whatsapp (G)
  - como comprimir un video en iphone para enviar por correo (G)
  - reducir tamaño video para enviar por whatsapp (G)
  - comprimir video iphone para enviar por email (G)
  - como comprimir pdf no iphone (B)
  - atajo comprimir video iphone (G)
  - como convertir un video mov a mp4 en iphone (G)
  - convertir heic a jpg sin perder calidad (G)
- **Competitors (S):** Compresor de Video Fácil, Compresor vídeo - encoger, Compress Videos & Resize Video, Video
  Compressor & Converter, Panda Video Compress & Convert, Compresor vídeos, Comprimir Vídeos y Reducir, Video
  Compress - Shrink Videos, Comprimir Video y Fotos Master, Comprimir Video 2026 Lite; PDF: Comprimir Archivo PDF,
  PDF Compressor : Compress PDF, iLovePDF- Editor PDF y Escáner, Comprímelo! Compresor de PDF, Adobe Scan; A for
  "comprimir pdf": "comprimir pdf & reducir pdf", "comprimir pdf: archivo ligero", "reducir peso"; A for "convertir
  video": a mp3, a audio, a mp4, en live photo.
- **Notes:** most G suggests are web tools (online, gratis, i love pdf, canva, adobe, windows); app intent needs
  "iphone". "Comprimir" is the verb, "reducir tamaño" (G) second, "compresor" the tool; "convertir" for formats.
  `comprimir imagen iphone` returned only itself (G). The WhatsApp and email destinations are the common reasons.
  The MediaKit page covers the Mac too; there is no Spanish demand for "mac" here (`logiciel` equivalents not
  returned).

## Millrace (tile-delivery logic puzzle; house rule applies)

- **Primary:** `juegos de lógica iphone` (G `juegos de logica iphone`; B `juegos de lógica gratis`). The head
  term `juegos de lógica` is huge but dominated by kids, printables and web games ("para niños", "online", "para
  imprimir", B); the iPhone form isolates app intent.
- **Secondary:** `juegos de lógica sin anuncios` (G `juegos de logica sin anuncios`); `juegos de ingenio iphone`
  (G; also `mejores juegos de ingenio iphone`, G); `juegos de lógica ipad` (G `juegos de logica ipad`).
- **FAQ-style:**
  - mejores juegos de lógica iphone (G `mejores juegos logica iphone`)
  - mejores juegos de ingenio iphone (G)
  - mejores juegos de pensar iphone (G)
  - mejores juegos sin anuncios iphone (G)
  - juegos sin internet iphone (G); mejores juegos sin internet iphone (G)
  - como jugar juegos sin anuncios en iphone (G)
  - juegos gratis sin anuncios ipad (G)
  - qué son los juegos de lógica (B)
  - juegos de lógica y estrategia (B)
- **Competitors (S/A):** Juegos de pensar: Brain Test!, Brain Test: Acertijos Engañosos, Sudoku.com - Juegos mentales,
  Logic Puzzles - Acertijos, Cross Logic - Juegos de logica, Easy Game - Juegos mentales, Brainilis - Juegos
  mentales, Blockudoku - Juego de bloques, Dot Knot - Line & Color Puzzle, Paper Fold: juego de lógica, Escape Time:
  Juegos de Pensar, Pawdoku – Puzle de lógica, Polygrams - Tangram Puzzles; A hints: "postmark: juegos de lógica",
  "wickhollow: juegos de lógica", "duskwick: juegos de lógica", "sparestep: puzle de lógica", "capynap: puzle de
  lógica", "desluma: puzle de lógica", "catpurrdoku: lógica gatuna"; G: "puzzle sin anuncios", "block puzzle sin
  anuncios".
- **Notes:** Spanish title patterns: "Nombre: juegos de lógica", "Nombre: puzle de lógica", "Nombre - Juegos
  mentales". Both "puzle" (RAE) and "puzzle" appear; "rompecabezas" (G, A) is the physical-jigsaw form and
  "juegos de ingenio" and "juegos de pensar" are the ES-ES casual forms. "Sin anuncios" is the strongest
  differentiator on the A side ("juegos sin anuncios", A); "sin internet" has large demand and the page can say
  offline. `juegos de puzzle ipad` (G `juegos puzzle ipad`), `juegos de rompecabezas iphone` (G empty) were weaker.
  Avoid the head phrase "juegos de lógica" alone (kids and printables). Number-title competitors exist in S; the
  house rule keeps that number out of every Millrace page.

---

## Summary table

| Page | Primary | Secondary 1 | Secondary 2 |
|---|---|---|---|
| Home | aplicaciones sin anuncios (G) | aplicaciones sin publicidad (G) | aplicaciones sin anuncios gratis (G) |
| Apps hub | mejores aplicaciones iphone (G, B) | mejores apps iphone (G, B) | aplicaciones útiles para iphone (G) |
| About | brand "Lagerland Apps" (no real query; closest: desarrollador de aplicaciones, G, B) | desarrollador de aplicaciones (G, B) | desarrollador independiente (B) |
| Support hub | cancelar suscripción iphone (G, B) | restaurar compras app store (G) | reembolso app store (G, B) |
| Transparency | app tracking transparency (G, B) | app tracking transparency que es (G) | privacy manifest (G, B) |
| aftershift | dormir después de trabajar de noche (G) | trastorno del sueño por turnos de trabajo (G, B) | deuda de sueño (G) |
| allpaid | app recordatorio de pagos (G) | app para recordar pagos (G) | app control suscripciones (G) |
| appmeta | app store connect mac app (G) | app store connect for mac (G) | aso app store (G) |
| appmeta-pulse | app store connect iphone (G) | app store connect ios (G) | app store connect api (G, B) |
| chessful | aplicación ajedrez (G, B) | aprender ajedrez app (G, B) | análisis de partidas de ajedrez (G, B) |
| earnlock | bloquear apps iphone (G, A) | bloqueador de aplicaciones (G, A) | limitar tiempo de pantalla (G, A) |
| gymlogger-x | app gimnasio apple watch (G) | app para registrar entrenamientos gimnasio (G) | app de entrenamiento apple watch (G, B) |
| liftlog | app registro gimnasio (G); "sin suscripción" as title differentiator (no suggest demand) | app seguimiento gimnasio (G) | app de pesas (G) |
| mediakit | comprimir video iphone (G, B) | comprimir pdf iphone (G, B) | convertir video a mp4 iphone (G, B) |
| millrace | juegos de lógica iphone (G) | juegos de lógica sin anuncios (G) | juegos de ingenio iphone (G) |


---

## Part 2: mockly to clippet

Tier 1 app pages: Mockly, Observa, Pawza, RightSplit, Shogiful, Soon., Tare, Taskful Day, WanderWiki, Xiangqiful,
Clippet. Format follows `_i18n/fr-keywords.md` Part 2.

Collected 2026-11-19. Source marks: **G** = Google suggest (hl=es, gl=es), **B** = Bing autosuggest (mkt=es-ES),
**A** = App Store search hints (Spain storefront 143454), **S** = iTunes Search API (country=es, lang=es_es), used only
for competitor names and the vocabulary in Spanish app titles. Every query below was returned by one of these
sources; nothing was invented. Accents are kept as the source returned them: Google mostly returns the unaccented form
(`cuenta atras iphone`) and sometimes the accented one (`widget cuenta atrás iphone gratis`); Bing and the App Store
mostly accent. Search Console data is not included.

## Method note

- **Requests: about 840.** Pass 1: 486 (G 223, B 115, A 115, S 33), seeds per app plus alphabet suffixes (a b c d e f
  g h i l m n o p r s t v) on 6 seeds only: `ajedrez chino`, `cuenta atras iphone`, `app lista de tareas`,
  `dividir cuenta`, `wikipedia aleatoria`, `portapapeles iphone`. Bing re-run: 115. Pass 2 (question-form and gap
  seeds): 240 (G 80, B 80, A 80). About 0.8 s between requests. Plus a handful of probes.
- **Google suggest: worked.** Best source. Alphabet suffixes were useful on `dividir cuenta`, `portapapeles iphone` and
  `ajedrez chino`, nearly empty on `wikipedia aleatoria` (the head term has only 5 suggestions) and thin on
  `cuenta atras iphone`.
- **Bing `osjson.aspx` (mkt=es-ES): did not work.** It answered HTTP 204 (empty body) to every request, with and without
  a browser User-Agent. The same Bing autosuggest service via `https://api.bing.com/qsonhs.aspx?mkt=es-ES&q=<q>`
  worked, so all **B** marks below come from that endpoint (115 + 80 requests). Bing is noisy: it drifts to
  Portuguese, French, English, Windows and unrelated phrases ("app hrvaška", "pasta alternativas"), and returns nothing
  for many long seeds. Used mainly to confirm Google.
- **App Store hints (Spain): worked only for short seeds.** Storefront `143454-8,29` and `143454-1,29` gave identical
  results for `shogi` (both return Spanish listing text, e.g. "shogiful: ajedrez japonés"), so the language suffix made no
  difference; `-8` was used throughout. Empty for almost every 3+ word seed and every question. Useful hits:
  `dividir cuenta`, `tricount`, `shogi`, `ajedrez japones`, `ajedrez chino`, `xiangqi`, `widget cuenta atras`,
  `cuenta atras boda`, `juegos de logica`, `juegos de ingenio`, `app to do list`, `planificador diario`,
  `gestor de portapapeles`, `mockup`, `variabilidad cardiaca`, `puntuacion de recuperacion`. Parsed the `<string>`
  entries of the plist and dropped the URLs and the "Suggestions" label.
- **iTunes Search API (country=es): worked** (33 searches, 3 per app) for competitor names and title vocabulary.
  Seller names are left out. Empty for the three WanderWiki queries.
- **People also ask: not collected.** It needs a live Google results page, which scripted fetches cannot get past
  (consent wall). I did not try to get around it. FAQ lines come from question-form autocomplete (`como`, `que es`,
  `cual es la mejor`, `donde esta`) on G and B.
- **"aplicación" vs "app":** `app` is what people type on Google for utility apps: `app lista de tareas` (G, B),
  `app dividir gastos` (G, B), `app cuenta atras` (G, A), `app sueño apple watch` (G), `app portapapeles` (G, B),
  `app wikipedia` (G, B), `app to do list` (G). `aplicación` appears second: `aplicacion dividir cuenta` (G),
  `aplicación para dividir gastos` (B), `aplicacion portapapeles para iphone` (G), `aplicación para organizar tu día`
  (B), `aplicación para hacer capturas` (B). App Store titles use both ("Dividir Cuenta - Propina", "Paste – Gestor
  de Portapapeles", "Shogiful: Ajedrez japonés"). Use "app" in titles and H1 where the suggest term has it, and
  "aplicación" in body text. `móvil` shows up as `portapapeles movil iphone` (G) and `dónde está el portapapeles en el móvil`
  (B); `ordenador` as `dónde está el portapapeles en mi ordenador` (B). Both are used in questions, almost never in
  head terms. **Spain vs Latin America:** many suggestions are Latin American (`cuenta regresiva`, `celular`,
  `carnet de vacunación`, `propina chile`); Spain says `cuenta atrás`. Both appear in G (`cuenta regresiva iphone`
  G), so `cuenta atrás` is chosen for Spain and `cuenta regresiva` is a body-copy variant.
- **Year/model variants** (`iphone 17`, `iphone 18`, `cartilla de vacunacion perros 2026`) avoided per house style.
  "gratis" variants exist almost everywhere; they are noted only where a free tier is real.
- **Nothing found at all** (empty on G, B and A): `capturas app store`, `crear capturas app store`,
  `generador capturas app store`, `tamaño capturas app store`, `app store connect capturas`, `app recuperacion deportiva`,
  `cartilla veterinaria app`, `app vacunas gato`, `app cartilla gato`, `pasaporte mascota digital`,
  `recordatorio medicacion mascota app`, `app para guardar documentos del veterinario`, `app dividir ticket`,
  `app dividir cuenta restaurante` (only the reworded form `app para dividir cuenta restaurante` G), `shogi iphone`,
  `ajedrez japones app`, `aprender xiangqi`, `ajedrez chino app`, `ajedrez chino iphone`, `cual es la mejor app de shogi`,
  `app cuenta atras boda`, `app cuenta atras nacimiento bebe`, `app cuenta atras examen`, `juego de logica iphone`,
  `juego de balanzas logica`, `puzzle sin palabras`, `mejor app to do iphone`, `app tareas apple watch`,
  `app lista de tareas apple watch`, `app tareas sin cuenta`, `lista de tareas mac` (only itself), `wikipedia aleatorio app`,
  `app articulos aleatorios`, `como ver articulos aleatorios de wikipedia`, `cual es el mejor gestor de portapapeles mac`,
  `que es un gestor de portapapeles` (G), `paste alternativa`.
- **Misleading seeds to avoid:** `dividir cuenta` alone (arithmetic homework "cuentas de dividir por dos cifras", bank
  accounts, "dividir estado de cuenta"), `app dias para` (fertile days), `app hrv` on Bing (Croatian, Harvest, Harvey),
  `hrv` alone (Honda HR-V: `hrv que es` G also gives "honda hrv que es", "hrv que pais es"), `puzzle de pesas`
  (Silent Hill), `cuenta atras iphone` + camera words (timer for photos), `variable aleatoria wikipedia` (statistics),
  `paste alternativa` (pasta), `recuperacion apple watch` (device "modo recuperación"), `app readiness` (Windows service),
  `cartilla de vacunación` alone (human vaccination card).

---

## Mockly (App Store screenshots on Mac)

- **Primary:** `screenshots app store` (G, B). Spanish developers keep the English "screenshots" for this topic; Google
  also returns `screenshots para app store` (G). The Spanish `capturas app store` returned nothing on G and A, and on B
  only generic "app para hacer capturas" (phone screenshot apps).
- **Secondary:** `app store screenshot generator` (G, B); `app store screenshot maker` (G); `mockup app store` (G, B).
  Optional: `app store screenshot template` (G), `app store connect screenshots` (G, B).
- **Not usable:**
  - `capturas app store`, `crear capturas app store`, `generador capturas app store`, `tamaño capturas app store`,
    `app store connect capturas`: G and A empty; B drifts to phone-screenshot apps (`app para hacer capturas`).
  - `mockup iphone gratis` (G) and `mockup iphone` (G, B): free-leaning, PSD/Figma/PNG template intent, and year
    variants (`mockup iphone 17`, `18`); Mockly is a paid Mac app.
  - `mockup` alone (G, B, A): T-shirt and generic mockup noise (`mockup camiseta`, "3d t-shirt mockup designer").
  - `app store screenshots skill`, `... figma`, `... free` (G): AI-skill, Figma and free intent.
  - "sin suscripción": allowed for Mockly (one-time purchase) but no returned query contains it.
- **FAQ-style (from suggest).** No Spanish question forms came back; the queries are English/developer ones:
  - app store connect screenshots sizes (G, B)
  - app store screenshot sizes (G)
  - screenshots app store size (G)
  - screenshots app store guidelines (G, B)
  - app store connect screenshots not uploading (G)
  - app store connect screenshots requirements (G)
  - app to make app store screenshots (B)
  - screenshots for app store connect (G)
- **Competitors (S):** StoreView: App Screenshot Tool, Screenshot Studio - Capturas, Picasso App Screenshot Studio,
  SMPRO: Mockup & Screenshot, Mockup Screenshot, Screenshots Pro, StoreShot - App Screenshots, Mockup y Demos: Screeny,
  Screenshot (App) Maker, App ShotCraft. A hints for `mockup`: "mockups: capturas y vídeos", "mockup generator - mocksy ai".
- **Notes:** Same pattern as French: keep "screenshots" and "mockup" in the title, use "capturas de pantalla" in the
  body. Hardly any query names Mac. Demand is small and English; this page cannot expect Spanish-language volume.

## Observa (sleep, HRV, recovery from Apple Health; HRV is SDNN)

- **Primary:** `hrv apple watch` (G, B). Spanish writers keep "HRV" in Latin letters.
- **Secondary:** `variabilidad frecuencia cardiaca` (G, B; also `variabilidad de la frecuencia cardiaca` B and
  `variabilidad cardiaca` G, B); `app sueño apple watch` (G; `mejor app sueño apple watch` G); `app hrv apple watch` (G).
  Optional: `app estres apple watch` (G).
- **Not usable:**
  - `app hrv` (G is fine, B is noise: "app hrvaška", "app harvest"): use `app hrv apple watch` instead.
  - `hrv que es` (G, B): mixes Honda HR-V ("honda hrv que es", "hrv que pais es"); fine only as an FAQ line with the
    health wording `hrv que es en salud` (G, B).
  - `readiness apple watch` (G, B): English, and the suggestions are device compatibility ("ultra 3", "compatibility");
    no Spanish "readiness" demand. Same for `sdnn hrv` (G; English only, "meaning", "formula").
  - `recuperacion apple watch` (G): "modo recuperación" is the device recovery mode; `app recuperacion deportiva` empty.
  - `puntuacion sueño apple watch` (G): only a long rating-scale phrase.
  - `app readiness` (G, B): Windows service.
  - `app apple salud` (G): about the Salud app being broken/missing, not about insights.
  - "sin suscripción" does not apply to Observa (Premium); at most "sin suscripción obligatoria" in the title; no
    returned query contains it.
- **FAQ-style (from suggest):**
  - que es la hrv (G, B) / hrv que es en salud (G, B) / hrv que significa (B)
  - hrv corazon que es (G)
  - como mejorar la hrv (G) / como mejorar mi hrv (G)
  - variabilidad frecuencia cardiaca normal (G, B) / variabilidad de la frecuencia cardiaca normal (B)
  - variabilidad cardíaca valores normales (G, B)
  - variabilidad frecuencia cardiaca durante el sueño (G)
  - variabilidad frecuencia cardiaca apple watch (G)
  - valores normales de hrv (B)
  - mejor app sueño apple watch (G) / app medir sueño apple watch (G) / app calidad sueño apple watch (G)
  - app medir estres apple watch (G)
  - recuperación frecuencia cardíaca apple watch (G)
- **Competitors (S):** Welltory: Mi Salud, StressWatch: Rastreo de Estrés, HRV-Tracker, HeartWatch, Athlytic:
  Fitness & Recovery, Narelia: HRV y readiness, Stressi: Monitor de Estrés HRV, Welldo: HRV Tracker para Watch,
  Stress HRV: monitor de estrés, VFC y Frecuencia Cardiaca, Cardia AI: Coach de salud, Variabilidad Cardíaca.
- **Notes:** Spanish app titles use both "HRV" and "VFC" (A hint `puntuación de recuperación vfc`, S "VFC y Frecuencia
  Cardiaca"); the search queries use "HRV" or the full "variabilidad (de la) frecuencia cardiaca". "frecuencia cardiaca"
  (no accent) is the Google form, "cardíaca" the Bing/App Store form. Never write RMSSD: Observa's HRV is SDNN, so
  "variabilidad de la frecuencia cardiaca (SDNN)" is the accurate wording. "Readiness" and "recovery" have no Spanish
  query equivalent; `puntuación de recuperación` is the closest (A, single hint).

## Pawza (pet health records, vaccines, vet documents)

- **Primary:** `cartilla veterinaria digital` (G). S shows the Spanish app vocabulary: "Mascotos: Cartilla Digital",
  "Vaccy: Cartilla de Vacunación", "Pidoy: Cartilla de Mascotas", and our own "Pawza: Salud y Cartilla Animal".
- **Secondary:** `app cartilla de vacunación perros` (G, as `app cartilla de vacunación perros`; B `cartilla de
  vacunación perro`); `app salud mascotas` (G); `calendario vacunación perros` (G, B as `calendario de vacunacion
  perros y gatos`).
- **Not usable:**
  - `cartilla de vacunación perros pdf`, `para imprimir`, `formato de cartilla de vacunación para perros` (G, B):
    printable-template intent. Year variants (`2025`, `2026`).
  - `carnet de vacunacion mascotas` (B only): Latin American term; Spain says "cartilla".
  - `calendario vacunacion perros madrid/españa/andalucia/chile/argentina/colmevet` (G): regional schedule intent.
  - `app para mascotas` (G, B): lost pets, virtual pets, adoption, Colombia/Argentina; `app para mascotas iphone`
    (B): nothing about health.
  - `app vacunas gato`, `app cartilla gato`, `cartilla veterinaria app`, `pasaporte mascota digital`,
    `recordatorio medicacion mascota app`, `app para guardar documentos del veterinario`: empty on G/A, noise on B.
  - `app salud perro` (G: `app salud perros`): thin.
  - "gratis": Pawza is free for one pet, so it is allowed in principle, but `app salud mascotas gratis` was not
    returned.
- **FAQ-style (from suggest).** Few question forms; these are the closest:
  - calendario de vacunacion perros y gatos (B)
  - cartilla de vacunación para mascotas (B)
  - cartilla de vacunación animal (B)
  - app cartilla de vacunación perros (G)
  - cartilla de vacunacion perros completa (G)
  - app salud mascotas (G)
  - Note: `como acceder a mi cartilla de vacunación` (B) is the human service, not pets.
- **Competitors (S):** Mascotos: Cartilla Digital, PetPaw AI – Salud de Mascotas, PawPass, Vaccy: Cartilla de
  Vacunación, Mascotas: Salud, Perro y Gato, Pet Health & Vaccine Tracker, Notes4Pets, NotePet: Recordatorio
  Mascotas, Pidoy: Cartilla de Mascotas, Petify: Salud Mascotas con IA, Salud Mascotas: PetnotePlus, Barkibu.
  A: `ruffo! app para mascotas`.
- **Notes:** "cartilla" (veterinaria / de vacunación) is the Spain word for the pet health booklet and the title word
  to use; "mascota" is the general noun, "perro/gato" in the long forms. The English page also covers rabbits,
  birds, reptiles and horses, but no Spanish query names them. On-device document scanning has no Spanish query
  demand; use it in the body only.

## RightSplit (split the bill from a receipt, tips)

- **Primary:** `app para dividir cuenta restaurante` (G; also `app para dividir cuentas en restaurantes` G,
  `dividir cuenta de restaurante` G, `dividir la cuenta del restaurante` G). A hint `dividir cuenta` offers
  "dividir cuenta propina grupo" and "dividir cuenta: pagar a escote".
- **Secondary:** `app dividir gastos` (G, B); `dividir cuentas entre amigos` (G, B); `calculadora dividir cuentas`
  (G, as `calculadora dividir cuentas` and `calculadora para dividir cuentas entre amigos`). Optional: `calcular propina`
  (G, B; `calcular propina iphone` G); `app para pagar a escote` (G).
- **Not usable:**
  - `dividir cuenta` alone: arithmetic, bank and utility-bill noise (`dividir cuenta bancaria`, `cuentas de dividir por
    dos cifras`, `dividir numero de cuenta`, `dividir estado de cuenta`, `dividir una cuenta de agua`).
  - `dividir cuenta uber / uber eats / rappi / mercado pago / revolut / bbva / netflix` (G): other products.
  - `tricount` (G, A, B) and `splitwise alternativa` (G, B): competitor brand queries; useful only for an
    alternatives page, not as the app page primary.
  - `app dividir ticket`, `como dividir la cuenta en un restaurante` on B: empty or noise.
  - `calcular propina chile / excel / por horas / 10` (G): Latin America and spreadsheet; tipping is also marginal in
    Spain, so tips are a secondary angle there.
  - `dividir la cuenta a la romana` (G): returned, but a regional idiom; "a escote" is the Spain idiom (A, G, B).
  - "gratis" variants (`app dividir gastos gratis` G): RightSplit is "free to start", so allowed in body copy, but not a
    primary.
- **FAQ-style (from suggest):**
  - como dividir la cuenta en un restaurante (G)
  - cual es la mejor app para dividir gastos (G) / cual es la mejor app para dividir gastos entre amigos (G)
  - como calcular la propina en un restaurante (G)
  - como calcular propina en iphone (G)
  - como calcular propina (G)
  - que es pagar a escote (B) / pagar a escote significado (B)
  - dividir cuenta iphone (G) / dividir cuenta en iphone (G)
  - app para dividir gastos entre amigos (G, B)
  - app para dividir gastos en pareja (G)
- **Competitors (S):** Splitwise, tricount - Gastos compartidos, Banana Split - Dividir gastos, Dividir Cuenta - Propina,
  Calculadora: Propinas y Cuenta, Dividir cuenta y gastos - dvup, Dividir cuenta: Pezzo, Dividir cuenta - Spliteasy,
  Apachas: Dividir gastos, SplitSlip: dividir la cuenta, Blito: Repartir la cuenta, SplitBill: Cuentas con amigos,
  Billy - Divide la cuenta, Splid, Settle Up, Quién me debe, Couple Count, Compartir Gastos. A: splitea, spliteroo,
  spliteasy.
- **Notes:** The verb is "dividir"; "repartir" is the second verb (`app repartir gastos` G, B). "cuenta" = the bill at a
  restaurant but also an account, hence the noise; "gastos" shifts intent to ongoing shared expenses (trips,
  flatmates), which RightSplit does not target. Qualify with "restaurante" or "ticket". Receipt scanning has no
  returned query; use "escanear el ticket" in the body only.

## Shogiful (shogi / Japanese chess, learn and analyze)

- **Primary:** `shogi` (G, B, A, S). Spanish title form: "Shogi (ajedrez japonés)". Our own listing shows up in A and S
  as "Shogiful: ajedrez japonés".
- **Secondary:** `ajedrez japonés` (G, A, S; Google form `ajedrez japones`); `como se juega al shogi` (G, B); `aprender
  shogi` (G).
- **Not usable:**
  - `shogi mod`, `shogi fabric`, `shogi minecraft`, `shogitai` (G, B): other things.
  - `shogi app yakuza`, `shogi online yakuza` (G): the shogi minigame of a video game.
  - `ajedrez japones de 372 piezas` (G): Dai dai shogi, a giant variant; `ajedrez japones go` (G): confusion with Go.
  - `shogi iphone`, `ajedrez japones app`, `cual es la mejor app de shogi`: empty on G/A, French/English noise on B.
  - `aprender a jogar shogi` (G): Portuguese.
  - `shogi online gratis` (G, B): fits only if the free tier is stated; leave as a body variant.
- **FAQ-style (from suggest):**
  - como se juega al shogi (G, B) / como jugar al shogi (G) / como se juega el shogi japones (G)
  - que es el shogi (G, B) / que es el shogi y como se juega (G)
  - que es el tsume shogi (G)
  - que tan dificil es el shogi (G)
  - que es mas dificil el ajedrez o el shogi (G) / diferencia entre ajedrez y shogi (G)
  - shogi reglas (G, B) / reglas del shogi en español (G) / shogi reglas pdf (G, avoid pdf intent)
  - movimientos piezas shogi (G)
  - shogi para principiantes (G) / shogi online para principiantes (B)
  - ajedrez japones como jugar (G)
  - shogi app (G, B) / shogi app store (G)
- **Competitors (S):** Shogi ™, Shogi Wars, PiyoShogi, 81Dojo, Dr. Shogi, Sr.SHOGI, Kanji Battle: Ajedrez Japonés, Everybody
  Shogi, Shogi Master, Shogi365: Tsume Shogi diario, Ajedrez Oscuro de Oriente. A: shogi quest online, shogi live,
  shogi lite, bushogi.
- **Notes:** Spanish searchers use "shogi" and "ajedrez japonés" about equally; the second is the descriptive phrase.
  "Tsume" appears in a question (G), so the 501 tsume problems can be named. "Kanji" and "sin kanji" have no returned
  query.

## Soon. (countdown app and widgets)

- **Primary:** `cuenta atrás iphone` (G; unaccented `cuenta atras iphone` G; also `app cuenta atrás iphone` G,
  `widget cuenta atrás iphone gratis` G).
- **Secondary:** `widget cuenta atrás` (G, A, B; `widget cuenta atrás iphone` G); `app cuenta atrás` (G, A, S);
  `contador de días app` (G, B); `cuenta atrás boda` (G, A).
- **Not usable:**
  - `cuenta atras camara iphone`, `cuenta atras foto iphone`, `cuenta atras alarma iphone`, `cuenta atras video iphone`
    (G): camera and alarm timers.
  - `cuenta atras bomba` (B), `cuenta atras vacaciones gif / meme / frases`, `cuenta atrás boda frases / video /
    instagram / amigos` (G): content, not app intent.
  - `widget cuenta atras notion / android / windows / samsung / mac` (G): other platforms (only `iphone` fits).
  - `app dias para` (G): fertile days and period apps; `app cuenta atras eclipse` (G); `app cuenta atras nacimiento bebe`,
    `app cuenta atras examen`, `app cuenta atras boda` (G, B empty or noise).
  - `cuenta atras iphone 18`, `cuenta regresiva iphone 18` (G): model variants.
  - "gratis": Soon. is free with Premium, so `widget cuenta atrás iphone gratis` (G) may appear once in the body; not
    the primary. Not a free-only claim.
- **FAQ-style (from suggest):**
  - como hacer una cuenta atras en iphone (G) / como hacer una cuenta atras de dias en iphone (G)
  - como poner una cuenta atras en iphone de dias (G)
  - se puede poner una cuenta atras en iphone (G)
  - como poner una cuenta regresiva en iphone (B)
  - poner cuenta atras en iphone (G) / hacer cuenta atras en iphone (G)
  - cuenta atrás dias iphone (G)
  - contador de dias para evento (G, B) / contador de dias para viaje (B) / contador de dias para vacaciones (B) /
    contador de dias para cumpleaños (B) / contador de dias para aniversario (B)
  - app cuenta atras viajes (G) / app cuenta atras compartida (G)
  - widget cuenta atrás iphone gratis (G)
- **Competitors (S):** Cuenta Atras ◎, Countdown Star, Cuenta atrás ‎, Days • Cuenta atrás de eventos, Cuenta Atrás
  Contador de Dias, Calendario de Cuenta Regresiva, Cuentas Atrás - Tu contador, Temporizador de Cuenta Atrás, Cuenta
  atrás: Pretty Progress, Countdown Buddy, Cuenta atrás - Widget, Widgetsmith, Countdown App & Widget, Reach: Cuenta
  Atras Widget. A: daymark, días: widget cuenta atrás, our day: cuenta atrás boda.
- **Notes:** Spain says "cuenta atrás"; Latin American "cuenta regresiva" is also suggested (G `cuenta regresiva iphone`,
  `widget cuenta regresiva`) and can appear once in the body. "contador de días" is the second noun phrase for
  days-until apps. Event types (boda, vacaciones, cumpleaños) have demand but mostly as content and gif queries.

## Tare (balance logic puzzle game)

- **Primary:** `mejores juegos logica iphone` (G; Spanish form `mejores juegos de lógica iphone`). Head term
  `juegos de lógica` (G, B, A) is huge but dominated by kids, online and printables, so the iPhone form isolates app
  intent. Suggested title form: "Juego de lógica sin palabras para iPhone y iPad".
- **Secondary:** `juegos de ingenio iphone` (G; `mejores juegos de ingenio iphone` G); `juegos de logica sin anuncios`
  (G); `mejores juegos de puzzle iphone` (G). Optional: `juegos de pensar iphone` (G), `juegos sin anuncios iphone` (G).
- **Not usable:**
  - `juego de balanza` (G, B) and `juego de balanzas` (B): kids' maths and school games, "Alice in Borderland", weighing
    equations (`juego de la balanza para resolver ecuaciones`), `juego de balanzas wordwall`. The closest intent match,
    but wrong audience; keep "balanza" in the body.
  - `acertijos de balanza` (G: `acertijos de balanzas`): classic weighing riddles, not a game app.
  - `puzzle de pesas` (G): Silent Hill 2 and Crisol puzzles.
  - `juego de equilibrio` (G, B): physical and children's balance games.
  - `juegos de razonar` (G): board games and kids.
  - `juegos de lógica niños / pdf / para imprimir / matemática` (G, B): wrong audience.
  - `juego de logica iphone`, `juego de logica para iphone`, `juego de puzzles iphone`, `puzzle sin palabras`:
    empty on G, noise on B.
  - "sin suscripción": allowed for Tare (free plus one unlock), but no returned query contains it; "sin anuncios" is
    returned instead (`juegos sin anuncios iphone` G, `juegos de logica sin anuncios` G) and is allowed because the
    page says no ads.
  - `juegos de logica gratis` (G, B, A): generic head term; Tare is free to start (20 levels), so allowed in the body,
    but not the primary.
- **FAQ-style (from suggest):**
  - mejores juegos de pensar iphone (G)
  - los mejores juegos de puzzle para iphone (G) / mejores juegos puzzle iphone (G)
  - mejores juegos sin anuncios iphone (G)
  - como jugar juegos sin anuncios en iphone (G)
  - juegos sin anuncios y sin internet para iphone (G)
  - juegos movil sin anuncios iphone (G)
  - qué son los juegos de lógica (B)
  - mejores juegos de ingenio iphone (G)
- **Competitors (S):** Impulse - Juegos Mentales, Brain Test: Acertijos Engañosos, Easy Game - Juegos mentales, Paper
  Fold: juego de lógica, Playdoku: Juego de Bloques, Logic Puzzles - Acertijos, Sudoku.com - Juegos mentales, Escape
  Time: Juegos de Pensar, Relojero: Juegos de Puzzles, Number Match, Test CI & Entrenamiento LEVO. A: "juegos de lógica
  blockmind", "juegos de lógica - rana".
- **Notes:** Spanish titles use "Juegos de lógica", "Juegos mentales", "Juegos de pensar", "Acertijos" and
  "Rompecabezas"/"Puzles". "Puzzle" is also used for jigsaws ("puzzles gratis", B), so prefer "lógica" and "ingenio".
  "Ingenio" has the iPhone form in Google; "lógica" has the volume.

## Taskful Day (day planner / to-do list, iPhone + Mac)

- **Primary:** `app lista de tareas` (G, B; `app lista de tareas iphone` G).
- **Secondary:** `app planificador diario` (G; the head `planificador diario` is G, B, A but printable-dominated);
  `app to do list` (G, A; `app to do list iphone` G); `app para organizar el dia` (G; `app organizar tareas diarias` G).
  Optional: `app lista de tareas diarias` (G), `app para planificar el dia` (G), `app agenda diaria` (G).
- **Not usable:**
  - `planificador diario para imprimir / pdf / excel / editable / niños` (G, B): printable-template intent.
  - `app lista de tareas compartida / android / windows / microsoft / google` (G): other platforms or team use.
  - `app de tareas del hogar / escolares / para niños / para ganar dinero` (G): other audiences.
  - `cual es la mejor app para hacer tareas de matematicas / de ia / resolver tareas` (G): homework help.
  - `lista de tareas mac`, `app tareas mac` (G: `app para organizar tareas mac`): thin (only itself).
  - `mejor app to do iphone`, `app tareas apple watch`, `app lista de tareas apple watch`, `app tareas sin cuenta`,
    `app planificador diario` on B: empty or noise.
  - `app to do list` on B: English "shared with friends". `app to do iphone` G: Portuguese and unrelated.
  - "gratis" variants are everywhere (`app lista de tareas gratis` G): the page offers Pro with a 7-day trial; mention
    "gratis" only if the free tier is confirmed against MASTER.md. "sin cuenta" (no account) has no returned query.
- **FAQ-style (from suggest):**
  - como organizar mi dia (G, B) / como organizar mi dia para ser mas productivo (G, B) / como organizar mi dia a dia (G)
  - como organizar mi rutina diaria (B)
  - cual es la mejor app para organizar tareas (G)
  - mejor app lista de tareas (G) / mejores app para organizar el dia (G)
  - app para planificar el dia (G) / app para planificar tu dia (G)
  - app para organizar el dia por horas (G)
  - app tareas pendientes iphone (G) / lista de tareas pendientes app (G)
  - aplicación para organizar tu día (B)
- **Competitors (S):** To Do List: Recordatorios, TickTick: Listas de tareas, Todoist: To do list–Calendario, Any.do,
  Microsoft To Do, Notion, Focus To-Do: Pomodoro & Tareas, Structured – Agenda del día, Me+ Planificador Diario,
  Planificador semanal - agenda, Planificador & Agenda - Floret, TodoLing: Tareas y Agenda, Planmore, Calendars: Agenda
  y Calendario, Eden - Organizador de tareas. A: planificador diario - planwoo, couchday.
- **Notes:** "Lista de tareas" is the main phrase; "to do list" in English is the second (G, A). "Tareas pendientes" is a
  separate cluster. "Planificador (diario)" is the title word that fits a day planner and is also the printable
  keyword; the "app" prefix isolates app intent. Carry-forward and "no red overdue pile" have no query demand; the
  title should say "lista de tareas" first.

## WanderWiki (swipe random Wikipedia articles)

- **Primary:** `wikipedia aleatoria` (G, B). Spanish Wikipedia calls the feature "Página aleatoria"; Google offers
  `wikipedia pagina aleatoria` and `pagina aleatoria wikipedia` (G).
- **Secondary:** `wikipedia aleatorio` (G, B; `wikipedia articulo aleatorio` G, `wikipedia artículo aleatorio` B);
  `wikipedia al azar` (G; `wikipedia articulo al azar` G); `app wikipedia` (G, B). Optional: `wikipedia random` (G, B),
  English form used in Spain.
- **Not usable:**
  - `variable aleatoria wikipedia`, `numeros aleatorios wikipedia`, `wikipedia busqueda aleatoria`: statistics and
    search noise (G returns these for the head term).
  - `wikipedia azar azmi` (G).
  - `curiosidades wikipedia`, `curiosidades con mike wikipedia` (G): trivia content, not an app.
  - `app datos curiosos` (G): "impostor" game; `app para aprender datos curiosos`: thin.
  - `app wikipedia sin internet`, `wikipedia offline app` (G): official or offline-copy intent. WanderWiki saves
    articles offline but is not an offline copy of Wikipedia, so do not claim it.
  - `wikipedia aleatorio app`, `app articulos aleatorios`, `como ver articulos aleatorios de wikipedia`,
    `app wikipedia iphone` (only an English "wikipedia app for iphone" on G): nothing or noise.
- **FAQ-style (from suggest).** No question forms came back; the nearest:
  - wikipedia articulo aleatorio (G) / wikipedia artículo aleatorio (B)
  - boton aleatorio wikipedia (G)
  - wikipedia modo aleatorio (G)
  - wikipedia tema aleatorio (G)
  - app wikipedia español (G)
  - wikipedia pagina aleatoria (G)
- **Competitors (S):** none returned (empty on all three searches). A hints: none.
- **Notes:** Demand is a small head term (G gives only about five suggestions for it) and it is the website feature
  people look for, not an app. Title should carry "Wikipedia aleatoria" and "iPhone". 32 Wikipedia language editions
  includes Spanish; check the page before claiming it.

## Xiangqiful (xiangqi / Chinese chess)

- **Primary:** `ajedrez chino` (G, B, A, S).
- **Secondary:** `xiangqi` (G, B, A, S); `ajedrez chino como se juega` (G, also `como jugar al ajedrez chino` G, `como
  se juega el ajedrez chino` B); `ajedrez chino reglas` (G; `xiangqi reglas` G). Optional: `ajedrez chino online`
  (G, B), `aprender ajedrez chino` (G).
- **Not usable:**
  - `ajedrez chino go` (G, B): confusion with Go (weiqi); `ajedrez chino shogi` (G), `ajedrez chino triangulo` (G).
  - `ajedrez chino de marfil / de madera / precio / comprar / mercado libre / amazon / imanes / tablero` (G): physical
    sets.
  - `ajedrez chino pvz`, `pvz fusion`, `where winds meet`, `ajedrez drama chino`, `ezhenatos ajedrez chino` (G): games
    and dramas.
  - `ajedrez chino crucigrama`, `ajedrez de origen chino crucigrama` (G): crossword clues.
  - `ajedrez en chino traductor`, `jugar ajedrez en chino` (G): language-learning intent.
  - `ajedrez chino app`, `ajedrez chino iphone`, `aprender xiangqi`, `cual es la mejor app de ajedrez chino`:
    empty on G and A; B returns generic chess apps.
  - `xiangqimei`, `xiangqi sg`, `xiangqi ok`, `xiangqian lao` (G, B): unrelated.
- **FAQ-style (from suggest):**
  - ajedrez chino como se juega (G) / como jugar al ajedrez chino (G) / xiangqi como se juega (G)
  - como se juega el ajedrez chino (B)
  - que es el xiangqi (G)
  - ajedrez chino reglas (G) / xiangqi reglas (G) / instrucciones ajedrez chino (G)
  - ajedrez chino movimientos (G)
  - ajedrez chino como se llama (G) / ajedrez chino nombre (G)
  - ajedrez chino origen (G) / ajedrez chino antiguo (G)
  - ajedrez chino piezas (G) / ajedrez chino figuras (G)
  - aprender ajedrez chino (G)
- **Competitors (S):** Xiangqi One - Ajedrez Chino, PVXiangqi: Ajedrez chino, Ajedrez chino V+, Xiangqi, Xiangqi Chinese Chess
  Online, Chinese Chess - Best XiangQi, Chinese Chess / Xiangqi, Co Tuong Viet Nam, 象棋 : 中国象棋. A: ajedrez chino
  offline, ajedrez chino - xiangqi ia, jardín xiangqi: ajedrez chino, xiangqi: ajedrez chino juego, xiangqi classic,
  xiangqi online - zyga chess, xiangqi 3d. Our own "Xiangqiful: Ajedrez Chino" is already in S.
- **Notes:** Spanish titles put "Ajedrez chino" first and "Xiangqi" second ("Xiangqi: ajedrez chino juego", "Xiangqi
  One - Ajedrez Chino"); both can sit in one title. "Pikafish" and "problemas de mate" have no returned query.

## Clippet (clipboard manager for iPhone and Mac, unreleased)

Unreleased and unlisted: these keywords are for when it goes live.

- **Primary:** `historial portapapeles iphone` (G, B; `ver historial portapapeles iphone` G).
- **Secondary:** `historial portapapeles mac` (G, B); `gestor de portapapeles mac` (G; `gestor portapapeles mac` G);
  `app portapapeles iphone` (G; `portapapeles iphone app` G, `aplicacion portapapeles para iphone` G).
- **Not usable:**
  - `portapapeles iphone no funciona`, `limpiar / borrar / vaciar portapapeles iphone` (G): fix and delete intent.
  - `portapapeles iphone 11 / 13 / 14 / 17`, `portapapeles en iphone 15 pro max` (G): model variants.
  - `portapapeles gboard iphone`, `teclado con portapapeles para iphone`, `portapapeles iphone teclado` (G): keyboard
    apps.
  - `gestor de portapapeles windows / linux / ubuntu`, `ditto gestor de portapapeles`, `historial portapapeles windows
    10 / 11`, `app portapapeles android / windows` (G, B): other platforms.
  - `paste alternativa`, `alternativa paste portapapeles` (G, B): empty or pasta noise; competitor brand names
    ("Paste") are not queries here.
  - `portapapeles madera`, `portapapeles marca maximo para baños` (B): physical clipboards.
  - `portapapeles iphone` alone (G): "donde esta", "no funciona" intents, model variants.
- **FAQ-style (from suggest):**
  - donde esta el portapapeles iphone (G; `donde esta el portapapeles en iphone 13` etc. is model-specific)
  - como ver el historial del portapapeles en iphone (G)
  - se puede ver el historial del portapapeles en iphone (G)
  - iphone tiene portapapeles (G) / iphone tiene historial de copiar y pegar (G)
  - como ver el portapapeles en mac (G, B as `cómo ver el portapapeles en mac`)
  - como ver mi historial de portapapeles en mac (G)
  - historial portapapeles mac atajo (G, as `portapapeles mac atajo`)
  - compartir portapapeles iphone mac (G)
  - qué es un portapapeles (B) / portapapeles qué es y para qué sirve (B)
  - dónde está el portapapeles en el móvil (B) / dónde está el portapapeles en mi ordenador (B)
- **Competitors (S):** Paste – Gestor de Portapapeles, Pop: Gestor de Portapapeles, Clippo - Gestor portapapeles, ClipBox:
  Portapapeles, Pasted - Portapapeles, Portapapeles: OnePaste, Copiar Mejor, +Portapapeles - copiar y pegar, Portapapeles
  Teclado Pegar. A: copyo – gestor de portapapeles, pastin, pip.
- **Notes:** "Portapapeles" is the only noun; "gestor de portapapeles" is how Spanish app titles label the category.
  Searchers mostly want to find or see the iPhone clipboard (built-in feature), so the page must say that iOS has no
  history and that Clippet adds one. Intent for "historial" is the strongest: both a G suggestion and a B suggestion
  on iPhone and Mac.

---

## Summary table

| Page | Primary | Secondaries |
|---|---|---|
| mockly | screenshots app store | app store screenshot generator; mockup app store; app store screenshot maker |
| observa | hrv apple watch | variabilidad frecuencia cardiaca; app sueño apple watch; app hrv apple watch |
| pawza | cartilla veterinaria digital | app cartilla de vacunación perros; app salud mascotas; calendario vacunación perros |
| rightsplit | app para dividir cuenta restaurante | app dividir gastos; dividir cuentas entre amigos; calculadora dividir cuentas |
| shogiful | shogi | ajedrez japonés; como se juega al shogi; aprender shogi |
| soon | cuenta atrás iphone | widget cuenta atrás; app cuenta atrás; contador de días app |
| tare | mejores juegos logica iphone | juegos de ingenio iphone; juegos de logica sin anuncios; mejores juegos de puzzle iphone |
| taskful-day | app lista de tareas | app planificador diario; app to do list; app para organizar el dia |
| wanderwiki | wikipedia aleatoria | wikipedia aleatorio; wikipedia al azar; app wikipedia |
| xiangqiful | ajedrez chino | xiangqi; ajedrez chino como se juega; ajedrez chino reglas |
| clippet | historial portapapeles iphone | historial portapapeles mac; gestor de portapapeles mac; app portapapeles iphone |
