# Apple's own Spanish names (es, Spain)

Part of the language sheet `_i18n/es.md`. Verified 2026-11-19 on Apple's Spain pages (source per row). Use these exactly; never invent an Apple name. Rows marked "not verified" have no Apple Spain page that names them.

Checked 2026-11-19 against Apple's live Spain pages: fetched directly with curl and `Accept-Language: es-ES`, raw HTML read for characters. Only `support.apple.com/es-es/...`, `www.apple.com/es/...` and `apps.apple.com/es/...` (page `lang="es-ES"`, footer "España" on support pages) were used; no Latin American (`es-mx`, `es-la`, `/la/`) page is a source for any row. The iPhone and Apple Watch user guides on support.apple.com/es-es are for iOS 27 and watchOS 27. **Apple Spain writes "tú" throughout** (imperatives "Toca", "Abre", "Ve a", "Pulsa", "Haz clic"; possessive "tu"; zero occurrences of "usted" in the guides, support articles, apple.com/es health and privacy pages and App Store pages checked). This is the register for the site. Apple Spain also writes "las amistades", "la persona organizadora", "tu hijo o hija" (inclusive wording) in the iOS 27 guide.

Two Latin American things Apple Spain does NOT use, useful as a check: "Tiempo en pantalla" (Spain: "Tiempo de uso"), "Descárgalo en el App Store" (Spain badge: "Consíguelo en el App Store"). Also Spain: "ordenador" (73 hits in the guides; "computadora" not used), "móvil" (201), "vídeo" with accent (3094 vs 214 "video"), "Ajustes" (not "Configuración" for the app), "cuenta de Apple", "Cartera" (not "Wallet"), "Atajos" (not "Accesos directos").

How Apple writes them in running text:
- **App names**: Apple writes "la app" + capitalised name, no quotes, no italics: la app Salud, la app Fitness, la app Archivos, la app Recordatorios, la app Ajustes, la app Reloj, la app Diario, la app Fotos, la app Atajos, la app Cartera, la app Mapas, la app Contraseñas, la app Apple Games, la app ECG, la app Constantes Vitales, la app Disposición, la app Entreno, la app Actividad, la app Sueño, la app Mindfulness, la app Ruido (Apple Watch). In the iPhone guide's table of contents and steps it is "app" everywhere (5569 "app", 0 "aplicación" in the guides; the old support articles have a handful of "aplicación": article 102638 "En la aplicación Ajustes", article 118408 "Alternar las aplicaciones"). So the word is **app**, never "aplicación" in current copy. Apple also writes "la app App Store" and "el App Store" (masculine). Marketing pages write the same: "la app Salud del iPhone", "la app ECG", "la app Constantes Vitales".
- **Features and multi-word setting labels** go in English-style curly double quotes “ ” (U+201C, U+201D), with no space inside: “Tiempo de uso”, “En familia”, “En reposo”, “No molestar”, “Reducir interrupciones”, “Iniciar sesión con Apple”, “Fotos en iCloud”, “Sincronizar este iPhone”, “Cancelar suscripción”, “Privacidad y seguridad” (sometimes bare, see next bullet). 2333 “ ” pairs counted across the iPhone and Apple Watch guide pages fetched, 0 « ». **Single-word labels are written bare**: Suscripciones, Concentración, Notificaciones, Resumen, Explorar, Sueño, Medicación (only 33 of 2337 quoted labels are one word, mostly Siri, Explorar, Notificaciones). Support articles (support.apple.com/es-es/NNNNNN) and apple.com marketing use « » instead (no space inside): «recibo de Apple», «Pedir a la app que no rastree», «cualquiera con el enlace»; in articles many button labels are written bare and capitalised: Cancelar Suscripción, Solicitar un reembolso, Permitir, Pedir a la app que no rastree.
- Menu paths use ">" with a no-break space before it and a normal space after: "Ve a Ajustes&nbsp;> Privacidad y seguridad&nbsp;> Rastreo." (the iPhone guide puts a tiny Settings icon image between the app name and the first ">"). Articles on the older pattern use spaces: "Ve a Ajustes > Accesibilidad." For steps Apple prefers the verb chain: "Abre la app Ajustes del iPhone. Toca “Tiempo de uso”."
- **Capitalisation**: sentence style in the iPhone guide (“Tiempo de uso”, “En familia”, “No molestar”, “Compartir entre dispositivos”). The Apple Watch guide, apple.com marketing and some articles use Title Case on feature/app names: Frecuencia Cardiaca, Constantes Vitales, Control del Ciclo, Oxígeno en Sangre, Calidad del Sueño, Historial de Fibrilación Auricular, Compartir Datos de Salud, Notas de Voz, Distancia de la Pantalla. Common nouns for features stay lowercase in running text: las notificaciones, el centro de control, el centro de notificaciones, un modo de concentración, el modo de concentración de descanso, la pantalla de inicio, la pantalla de bloqueo, el modo oscuro, el modo Avión (capital A), el modo de bajo consumo, la cuenta de Apple (lowercase "cuenta" in running text; "Cuenta de Apple" capitalised when it is a button or account label, e.g. toca “Cuenta de Apple”, and in articles 118428/118223: "tu Cuenta de Apple"). The site should use "cuenta de Apple" lowercase in prose.
- Gender and elision: el iPhone, el iPad, el Mac, **el Apple Watch** (masculine: "en el Apple Watch"), el Apple TV, la Dynamic Island, el App Store, el Mac App Store, la app Salud, "las Apple Vision Pro" (article 118428 plural) / "el Apple Vision Pro" (not checked elsewhere; use "Apple Vision Pro" without article if needed). iCloud: no article ("en iCloud"). Apple writes "iCloud Drive", "Face ID", "Touch ID", "Apple Pay", "Apple Intelligence", "AirDrop", "Siri" in English.
- Other Apple spellings: "Wi-Fi" appears as "Wi‑Fi" with U+2011 NON-BREAKING HYPHEN in the Mac guide and iPhone guide (159 U+2011 on the pages fetched) and as plain "Wi-Fi" elsewhere; "cardiaca" without accent in Spain ("frecuencia cardiaca", "salud cardiaca"; Apple does not write "cardíaca"); "vídeo" with accent; "ítems" (Apple uses it: "Restaurar en el iPhone ítems comprados"); "por omisión" for "default" (also "por defecto" on apple.com/es privacy); "eventos" in the Calendar guide; "toca" for tap, "mantén pulsado" for press and hold, "desliza" for swipe, "haz clic" on Mac, "selecciona"/"elige", "pulsa" for physical buttons, "inicia sesión", "ajustes" (lowercase noun "ajustes de privacidad"); "app" plural "apps" (no -s accent). Percentages and units with NBSP: "30 %", "5 GB", "iOS 27", "Apple Watch Series 12".
- Apple's inclusive wording in iOS 27 copy: "tus amistades y familiares", "la persona que organiza la familia", "peques" (Apple Spain's word for little kids: "Dispositivos Apple para peques y familias", "Apple Watch para tus Peques").

Punctuation and spacing (checked in raw bytes on the iPhone guide, Apple Watch guide, Mac guide, support articles 118428, 118223, 108906, 102420, 105055, 108756, apple.com/es/health, apple.com/es/privacy, apps.apple.com/es):
- UI quotes in guides: “ ” (U+201C/U+201D) **without spaces inside** and **punctuation after the closing quote** ("Toca “Explorar”." 247 times `”.`; 78 `”,`; 0 `.”`). Support articles and marketing: « » (U+00AB/U+00BB) **with no space inside** (`«recibo de Apple»`). No spaces inside either pair. This differs from French (NBSP inside « »).
- `¿ ?` and `¡ !` used normally (`¿Necesitas más ayuda?`, `¿Te ha resultado útil?`, `¿Quieres saber más?`).
- Colon, semicolon: no space before (`Nota: ...`, `Siri: Pide a Siri algo como: “Activa el modo de concentración Trabajo”.`). 0 NBSP before ":" in 6 pages checked.
- Apostrophe: Spanish rarely needs one; Apple's pages use U+2019 where present (2 hits on all guide pages). Never a straight '.
- Dashes: Apple uses the spaceless raya for asides: "registrar síntomas —como dolores menstruales— y controlar" (raya attached to the text on the inside, space outside). En dash not used.
- Numbers: **decimal comma** (`12,9 pulgadas`, `92,7 MB`, `11,3 MB`, `5,0` rating); **thousands separator is a period**: `100.000 veces al día`, `1.500 millones`, `5.000 millones` (apple.com/es/health); space between value and unit is **U+00A0** (`5 GB`, `92,7 MB`, `50 puntos`, `24 a 48 horas`, `7 días`, `13 noches`); same before `%`: `30 %`, `200 %`, `80 %` (4 NBSP + 0 plain on guide pages; the App Store page of one developer shows plain-space `50 %` inside the developer's own text, not Apple's); `°C` with NBSP (`35 °C`, from one page, not re-checked).
- Currency: `2,99 €` = comma decimal, **U+00A0**, then € (checked raw: `<span>2,99&nbsp;€</span>` on the App Store page; `1,99 €`, `9,99 €`, `22,99 €`, `39,99 €`, `44,99 €` all NBSP). Euro sign is after the number.
- Dates in running text and articles: **"18 de septiembre de 2026"** (day without leading zero for 18; article footers show a leading zero: "Fecha de publicación: 01 de octubre de 2026", with NBSP after the colon). Lowercase month, "de" before month and before year. App Store version dates: "27 oct", "5 nov" (short month, lowercase, no period); "hace 6 d".
- Times: 24-hour clock with a colon: "de 11:00 a 13:00" (Calendar guide example). No "a. m." or "p. m." on the pages checked. Apple writes time-of-day in words as "las cuatro de la tarde" only in a developer's App Store text. Durations: "Durante 1 hora", "Hasta que me vaya de aquí" (Focus options, with NBSP after the number: `1 hora`).
- Product names: Apple's HTML puts **U+00A0 inside "Apple Watch", "App Store", "iCloud Drive", "Face ID", "Touch ID", "Apple Pay", "Apple Intelligence", "iPhone 15 Pro", "iOS 27", "Apple Fitness+", "Game Center", "Apple Games", "Liquid Glass"** throughout the guides (`Apple&nbsp;Watch`, `App&nbsp;Store`) and the App Store page title (`App&nbsp;Store` in `<title>`). Support articles 118428 and others use plain spaces in some places, so both occur. Also "Constantes&nbsp;Vitales", "Frecuencia&nbsp;cardiaca", "Frecuencia&nbsp;Cardiaca".
- Ordinals: `2.ª generación`, `3.ª generación` with NBSP after the ordinal (146 hits). "EE. UU." with NBSP (`EE.&nbsp;UU.`).
- apple.com marketing text puts NBSP before short words at line ends ("A⍽ciencia⍽cierta", "en⍽tu"); do not copy these typesetting NBSPs.
- Title, spelling and spacing in one case: Observa's own App Store title in Spain is "Observa: VFC y Recuperación" (developer text).

Abbreviations: ig = iPhone user guide https://support.apple.com/es-es/guide/iphone/welcome/ios (table of contents), wg = Apple Watch user guide https://support.apple.com/es-es/guide/watch/welcome/watchos, mg = Mac user guide https://support.apple.com/es-es/guide/mac-help/welcome/mac, ah = https://www.apple.com/es/health/ (page title "Salud de Apple - Apple (ES)"), apv = https://www.apple.com/es/privacy/, ap = apps.apple.com/es, sg = https://support.apple.com/es-es/guide/security/welcome/web. Article URLs are https://support.apple.com/es-es/NNNNNN.

## Health and fitness

| English | Spanish (Spain) as Apple writes it | Source | Note |
|---|---|---|---|
| Health (app) | Salud; la app Salud | https://support.apple.com/es-es/guide/iphone/iphcae7451f3/ios ; ah | Translated, never "Health". Tabs: Resumen, Compartir, Explorar (older text: Examinar) |
| Apple Health | Salud de Apple; la app Salud de Apple | ah (page title "Salud de Apple - Apple (ES)", sections "Salud de Apple" and "App Salud de Apple") | Translated on Apple's own pages. Developers' App Store text still says "Apple Health" (Observa's Spain listing); Apple's pages do not |
| Health data | datos de salud; datos de Salud (capital S when it is the app's data); "Introducción a los datos de Salud" | https://support.apple.com/es-es/guide/iphone/iphcae7451f3/ios ; https://support.apple.com/es-es/guide/iphone/iphbb8259c61/ios | |
| Health profile | perfil de salud (Resumen > tu foto > Perfil de salud) | https://support.apple.com/es-es/guide/iphone/iphcae7451f3/ios | |
| Health records | historial clínico ("Ver el historial clínico en la app Salud en el iPhone") | https://support.apple.com/es-es/guide/iphone/iphcae7451f3/ios (link text) | not re-opened; text from "¿Quieres saber más?" list |
| Medical ID | not verified | not fetched | Apple Watch guide TOC has "Configurar y consultar datos médicos" (https://support.apple.com/es-es/guide/watch/apd58cd0b3f4/watchos) ; the exact feature label "Ficha médica" is a guess, not seen |
| Health category (Summary pins) | categorías de salud; pantalla Resumen; lista “Datos fijados” (Fijadas); “Datos importantes”; “Categorías de Salud” (Examinar/Explorar screen); Tendencias | https://support.apple.com/es-es/guide/iphone/iphe3d379c32/ios | "Fijar en el resumen" |
| Sleep (in Health) | Sueño (app Sueño on Apple Watch; “Configurar Sueño”); on iPhone iOS 27 the Explorar category is also called **Descanso** ("Toca Explorar y toca Descanso dos veces seguidas") | https://support.apple.com/es-es/guide/iphone/iphaf56dceb4/ios ; https://support.apple.com/es-es/guide/iphone/iph72b370881/ios ; https://support.apple.com/es-es/108906 (article says "Toca Sueño") ; https://support.apple.com/es-es/guide/watch/crpxel1lvun9/watchos | Apple's pages disagree (Descanso in the iOS 27 iPhone guide, Sueño in the Watch guide and the article). Use "sueño" in prose; avoid quoting a tab name |
| Sleep Focus | modo de concentración de descanso (also "modo Descanso", "modo de descanso", "Modo de concentración de descanso" in the article); Focus mode name: Descanso | https://support.apple.com/es-es/guide/iphone/iphaf56dceb4/ios ; https://support.apple.com/es-es/guide/iphone/iph5c3f5b77b/ios ; ah ("activar automáticamente el modo Descanso") | Not "Sueño". Focus list: Trabajo, Personal, “Tiempo libre”, Descanso, “No molestar” |
| Sleep Score | puntuación de la calidad del sueño; “Calidad del sueño” (Salud); Calidad del Sueño (marketing prestación) | https://support.apple.com/es-es/guide/watch/apded441a669/watchos ; ah | Scale: Muy baja 0-40, Baja 41-60, Aceptable 61-80, Alta 81-95, Muy alta más de 96 |
| Sleep apnea notifications | Notificaciones de apnea del sueño | https://support.apple.com/es-es/guide/watch/apd4e7713562/watchos (page title "Recibir notificaciones de apnea del sueño en el Apple Watch") | |
| Sleep stages Awake / REM / Core / Deep | **Despierto / REM / Esencial / Sueño profundo** (article: "las fases Despierto, REM, Esencial o Sueño profundo"); Watch guide prose: "sueño REM, esencial y profundo" and "cuándo es posible que te hayas despertado" | https://support.apple.com/es-es/108906 ; https://support.apple.com/es-es/guide/watch/crpxel1lvun9/watchos | Word for stage: "fase del sueño" (not "etapa"; article intro also says "etapas del sueño" once: "Para ver el historial y las etapas del sueño"). Core = "Esencial" |
| Heart Rate Variability (HRV) | variabilidad de la frecuencia cardiaca; abbreviation **VFC**; "variabilidad de frecuencia cardiaca (VFC)" (marketing) | https://support.apple.com/es-es/guide/watch/apda88aefe4c/watchos ; ah ("la variabilidad de frecuencia cardiaca (VFC)") ; https://support.apple.com/es-es/guide/watch/flx4gnzby346/watchos ("la variabilidad de la frecuencia cardiaca (VFC)") | Apple Spain abbreviates VFC, never HRV. Watch label "Variabilidad de la frecuencia cardiaca"; "VFC en recuperación" on Series 12 / Ultra 4. Observa's own Spain store title uses "VFC" |
| Resting heart rate | frecuencia cardiaca en reposo (Watch labels: “Frec. en reposo”, “Media andando”, Intervalo) | https://support.apple.com/es-es/guide/watch/apda88aefe4c/watchos ; https://support.apple.com/es-es/guide/iphone/iphe3d379c32/ios ("la frecuencia cardiaca en reposo") | Not "frecuencia cardíaca" |
| Heart rate | frecuencia cardiaca; la app Frecuencia Cardiaca (Watch); "pulsaciones" (marketing, colloquial) | same | |
| Respiratory rate | frecuencia respiratoria | https://support.apple.com/es-es/guide/watch/crpxel1lvun9/watchos | |
| Heart rate zones | zonas de frecuencia cardiaca | https://support.apple.com/es-es/guide/watch/apd897dccddf/watchos ; ah | |
| ECG app | la app ECG; electrocardiograma | https://support.apple.com/es-es/guide/watch/apdea4c50a57/watchos ; ah | |
| AFib History | Historial de Fibrilación Auricular | ah | |
| Irregular rhythm notifications | notificaciones/avisos de ritmo irregular | ah | |
| Vitals app | la app Constantes Vitales; constantes vitales nocturnas / diurnas ("Constantes vitales nocturnas") | https://support.apple.com/es-es/guide/watch/apd15aa7ed96/watchos ; ah | "constantes vitales", not "signos vitales". Also "métricas de salud nocturnas" |
| Readiness app (watchOS 27) | la app **Disposición**; puntuación de disposición (0 a 10) | https://support.apple.com/es-es/guide/watch/flx4gnzby346/watchos ; ah ("Disposición te dice cuándo toca descansar") | The Watch guide TOC calls the page "Disposición". Apple Watch Series 12 and Ultra 4 only |
| Training Load | **carga de ejercicio** (scale "Muy inferior" a "Muy superior") | https://support.apple.com/es-es/guide/watch/apde4c07a6cf/watchos ; ah | Not "carga de entrenamiento" (Apple's article title: "Seguimiento de la carga de ejercicio"). Observa's own store text says "carga de entrenamiento" (developer's wording) |
| Cardio Fitness | **capacidad aeróbica** ("Haz un seguimiento de tus niveles de capacidad aeróbica"; Salud > Corazón > Capacidad Aeróbica) | https://support.apple.com/es-es/108790 ; https://support.apple.com/es-es/guide/iphone/ipha5dddb411/ios ; ah | |
| VO2 max | VO2 máximo (VO<sub>2</sub> máximo, subscript 2 in the HTML); abbreviation "VO2 máx." | https://support.apple.com/es-es/108790 (raw `VO<sub>2</sub> m&aacute;ximo`) ; ah ("el VO2 máximo") ; Fitness guide ("VO2 máx.") | "la cantidad máxima de oxígeno que el organismo puede consumir durante el ejercicio" |
| Cycle Tracking | Control del Ciclo (title case on the Watch and in "Configurar Control del Ciclo"); control del ciclo / seguimiento del ciclo menstrual in prose | https://support.apple.com/es-es/guide/watch/apd26429adf0/watchos ; https://support.apple.com/es-es/guide/iphone/iphcae7451f3/ios | |
| Mindfulness app | la app Mindfulness; sesiones Reflexionar y Respirar; "atención plena" in prose | https://support.apple.com/es-es/guide/watch/apd371dfe3d7/watchos ; ah | |
| State of Mind | Estado de ánimo (Salud mental > Estado de ánimo) | https://support.apple.com/es-es/guide/iphone/iph6a6decb13/ios ; ah | "Registrar tu estado de ánimo" |
| Medications | **Medicación** (Explorar > Medicación; page title "Llevar un control de los medicamentos"); "Añadir medicamento"; "Programar la medicación" | https://support.apple.com/es-es/guide/iphone/iph811670c81/ios ; https://support.apple.com/es-es/guide/iphone/iphcae7451f3/ios | Feature = Medicación; the thing = medicamentos |
| Walking Steadiness | estabilidad al andar (“Notificaciones de estabilidad al andar”) | https://support.apple.com/es-es/guide/iphone/iphff1bf03ed/ios | Not "estabilidad al caminar" |
| Mobility | Movilidad (Explorar > Movilidad) | same | |
| Activity rings | anillos de actividad; “anillos de Actividad” (capital A when naming the app's rings) | https://support.apple.com/es-es/guide/iphone/ipha5dddb411/ios ; https://support.apple.com/es-es/guide/watch/apd3bf6d85a6/watchos ; ah | |
| Move / Exercise / Stand rings | anillo **Movimiento** (red, calorías activas) / anillo **Ejercicio** (green, minutos de ejercicio) / anillo “**De pie**” (blue, quoted; "De Pie" in marketing); wheelchair ring: **Impulsos** | https://support.apple.com/es-es/guide/watch/apd3bf6d85a6/watchos ; ah ("Movimiento, Ejercicio y De Pie") | Not "Mover" / "Pararse". Apple writes "Movimiento, Ejercicio y “De pie”" in the guide |
| Fitness app | la app Fitness (iPhone and iPad; tab Resumen, Entreno, Compartir) | https://support.apple.com/es-es/guide/iphone/ipha5dddb411/ios ; ah | English kept |
| Activity app (Apple Watch) | la app Actividad | https://support.apple.com/es-es/guide/watch/apd3bf6d85a6/watchos | |
| Workout app | **la app Entreno**; "entreno" (a workout); “Iniciar entreno”; "entrenos de fuerza"; "entrenamientos" appears once in an article | https://support.apple.com/es-es/guide/watch/apdd16e8761a/watchos ; https://support.apple.com/es-es/guide/iphone/ipha5dddb411/ios ; https://support.apple.com/es-es/108790 ("entrenamientos en interiores") | Apple's guides: entreno / Entreno. Not "ejercicio" for the workout |
| Workouts (the plural) | entrenos | same | |
| Stand hours | horas de pie | https://support.apple.com/es-es/guide/watch/apd3bf6d85a6/watchos | |
| Exercise minutes | minutos de ejercicio | same | |
| Active energy / calories | calorías activas | same | |
| Flights climbed | pisos subidos | https://support.apple.com/es-es/guide/iphone/iphbb8259c61/ios | |
| Steps | pasos | same | |
| Headphone audio levels | niveles de audio de los auriculares; “Notificaciones de los auriculares” | https://support.apple.com/es-es/guide/iphone/iph0596a9152/ios | |
| Noise / environmental sound | la app Ruido; niveles de ruido | https://support.apple.com/es-es/guide/watch/apd00a43a9cb/watchos (title "Medir los niveles de ruido con el Apple Watch") ; ah | |
| Wrist temperature | temperatura de la muñeca | https://support.apple.com/es-es/102674 ; https://support.apple.com/es-es/guide/watch/apd526d20feb/watchos | |
| Blood Oxygen | Oxígeno en Sangre (app, title case); oxígeno en sangre (prose) | https://support.apple.com/es-es/guide/watch/apd15aa7ed96/watchos ; ah | |
| Apple Watch | el Apple Watch (masculine: "en el Apple Watch") | https://www.apple.com/es/watch/ not fetched; ah ; wg | English kept |
| Apple Fitness+ | Apple Fitness+ | https://support.apple.com/es-es/guide/iphone/iph6e7917d3f/ios ; ah | English kept |
| Journal app | la app Diario ("Escribir en el diario") | https://support.apple.com/es-es/guide/iphone/iph9824e83ce/ios ; ah | |

## System features

| English | Spanish (Spain) as Apple writes it | Source | Note |
|---|---|---|---|
| Settings | la app **Ajustes**; Ajustes del Sistema (Mac) | https://support.apple.com/es-es/guide/iphone/iphd6804774e/ios ; https://support.apple.com/es-es/guide/mac-help/mchlc9d0e1f2/mac | Not "Configuración" (that word is used only for "configurar" the verb and "configuración" as the setup process) |
| Screen Time | “**Tiempo de uso**” | https://support.apple.com/es-es/guide/iphone/iphbfa595995/ios | Quoted in the iOS 27 guide (61 pairs). **Not "Tiempo en pantalla"** (Latin America) |
| Screen Time Schedules (iOS 27) | “Horario de tiempo de uso”; horarios de tiempo de uso | same | "Horario" is the switch |
| Screen Time Limits | “Límites de tiempo” (iOS 27) | same | Also "Gestionar tiempo de uso", “Compartir entre dispositivos”, “Activar actividad de apps y sitios web” |
| Downtime / App Limits (iOS 26 and earlier) | not verified | not fetched (the iOS 27 guide replaced them; the ig version switch lists iOS 26, 18, 17, 16 but those pages were not opened) | |
| Screen Time, more iOS 27 labels (verified 2026-11-19, Tier 2 screen-time guide review) | “Siempre permitidas” (Apple also writes «Siempre permitidos/permitido»; use the path form), “Ajustar al horario de tiempo de uso”, “Gestionar categorías”, “Añadir horario”, “Eliminar esta franja horaria”, “Desactivar actividad en apps y sitios web”, the switch Horario | https://support.apple.com/es-es/guide/iphone/iphb0c7313c9/ios | Schedules and limits need iOS 27 or later on every device, signed in with the same cuenta de Apple, to be shared |
| Screen Time weekly report | informe semanal de tiempo de uso; “Promedio diario”; “Consultas del dispositivo”; “Notificaciones” | https://support.apple.com/es-es/guide/iphone/iphbfa595995/ios | |
| Screen Distance | Distancia de la Pantalla | ah | Marketing page only |
| Focus | **Concentración**; modo de concentración (lowercase, plural "modos de concentración") | https://support.apple.com/es-es/guide/iphone/iphd6288a67f/ios ; https://support.apple.com/es-es/guide/iphone/iph5c3f5b77b/ios | Settings label: Concentración (bare); control center tile: Modos. Modes: Trabajo, Personal, “Tiempo libre”, Descanso |
| Do Not Disturb | “No molestar” | same | |
| Reduce Interruptions (Focus) | “Reducir interrupciones” (uses Apple Intelligence) | https://support.apple.com/es-es/guide/iphone/iphd6288a67f/ios | |
| Focus Filter / link Focus to Lock Screen | "Vincular un modo de concentración a la pantalla de bloqueo" | same | |
| Family Sharing | **“En familia”**; "un grupo de “En familia”"; Ajustes > Familia; menu words "Configurar “En familia”", "Compartir con la familia" | https://support.apple.com/es-es/guide/iphone/iph4e3e7324f/ios ; https://support.apple.com/es-es/guide/iphone/iph6e7917d3f/ios ; https://support.apple.com/es-es/guide/iphone/iph4cd8953e2/ios ; ap ("Si está activada la función “En familia”...") | Capitalised "En Familia" in article 105055 and in the Tare Spain product page ("compatible con En Familia", developer text). Apple's guide: sentence case “En familia”. Never "Compartir en familia" as the name |
| Family sharing label on the product page | Compatibilidad > **En familia**: "Si está activada la función “En familia”, es posible que se puedan compartir con el grupo familiar algunas suscripciones y compras dentro de la app." | https://apps.apple.com/es/app/id6806255929 | Exact store text |
| Ask to Buy | **Solicitar la compra**; “Solicitar la compra” (guide, quoted) | https://support.apple.com/es-es/105055 ; https://support.apple.com/es-es/guide/iphone/iph6e7917d3f/ios | Article title: "Aprobar lo que tu hijo o hija puede comprar y descargar con Solicitar la compra" |
| Parental controls | control parental ("funciones de control parental") | https://support.apple.com/es-es/guide/iphone/iphbfa595995/ios | |
| Family Controls (framework) | not verified (developer docs are English; the user-facing feature is “Tiempo de uso” and control parental) | developer.apple.com/es redirects to the Latin American /la/ site or English; no Spain page | |
| In-App Purchases | **compras dentro de la app** (store label "Compras dentro de la app"); "compras dentro de una app" | https://apps.apple.com/es/app/id6806255929 ; https://support.apple.com/es-es/guide/iphone/iph4e3e7324f/ios | Not "compras integradas", not "compras en la app" |
| Subscriptions (manage) | "En Ajustes, toca tu nombre. Toca Suscripciones. Toca la suscripción. Toca Cancelar Suscripción." (Mac: "En el App Store, haz clic en tu nombre... Haz clic en Suscripciones... Haz clic en Cancelar Suscripción.") | https://support.apple.com/es-es/118428 | Article title: "Cancelar una suscripción de Apple". iPhone guide: "Abre la app Ajustes del iPhone. Toca tu nombre y, a continuación, toca Suscripciones. ... toca “Cancelar suscripción”" |
| Cancel subscription (button) | **Cancelar Suscripción** (article, title case); “Cancelar suscripción” (iPhone guide); “Cancelar todos los servicios” | https://support.apple.com/es-es/118428 ; https://support.apple.com/es-es/guide/iphone/iph4e3e7324f/ios | Expired: "ves un mensaje de caducidad en texto rojo" |
| Apple Account (ex Apple ID) | **cuenta de Apple** (lowercase in prose); “Cuenta de Apple” (button/label) | https://support.apple.com/es-es/guide/iphone/iph76e54c61e/ios ; https://support.apple.com/es-es/118223 | Apple Spain does not write "ID de Apple" in the iOS 27 guide (one article still has "cuenta ID de Apple"). |
| iCloud | iCloud | https://support.apple.com/es-es/guide/iphone/iphde0f868fd/ios | English kept |
| iCloud+ | iCloud+ | same ("cómo suscribirse a iCloud+") | |
| iCloud Drive | iCloud Drive | https://support.apple.com/es-es/guide/iphone/iphbbcf8827d/ios | |
| iCloud Photos | **Fotos en iCloud** (quoted: “Fotos en iCloud”); "Fotos de iCloud" appears once in article 108922 | https://support.apple.com/es-es/guide/iphone/iph11f1eb698/ios ; https://support.apple.com/es-es/108922 | Page title: "Realizar una copia de seguridad en iCloud de los datos de la app Salud..." for Health; Photos page TOC "Realizar una copia de seguridad de las fotos y vídeos sincronizarlas con iCloud" |
| Sync this iPhone (iCloud Drive toggle) | “Sincronizar este iPhone” (Ajustes > [tu nombre] > iCloud > Drive) | https://support.apple.com/es-es/guide/iphone/iphbbcf8827d/ios | |
| iCloud sync | "mantener sincronizado/a"; "sincronizar con iCloud" | https://support.apple.com/es-es/guide/iphone/iphde0f868fd/ios | No fixed noun phrase |
| iCloud backup | copia de seguridad en iCloud | https://support.apple.com/es-es/guide/iphone/iphde0f868fd/ios | |
| Advanced Data Protection | **protección de datos avanzada** (lowercase; "Cómo activar la protección de datos avanzada para iCloud"); security guide: "Protección de datos avanzada para iCloud" | https://support.apple.com/es-es/108756 ; https://support.apple.com/es-es/102651 ; sg | Spain order: "datos avanzada" (not "avanzada de datos") |
| Standard data protection | "protección de datos estándar" | https://support.apple.com/es-es/102651 | |
| Data Protection (iOS file encryption) | **Protección de datos** ("Descripción general de Protección de datos", "Clases de Protección de datos") | https://support.apple.com/es-es/guide/security/secf6276da8a/web | Resolved here: the Spain security guide IS translated |
| Apple Push Notification service (APNs) | servicio de notificaciones push de Apple (APNs) | https://support.apple.com/es-es/guide/security/aside/sec19eabb530/web (page title "servicio de notificaciones push de Apple (APNs):") | For users: "notificaciones" |
| Home Screen | **pantalla de inicio** | https://support.apple.com/es-es/guide/iphone/iphb8f1bf206/ios ; https://support.apple.com/es-es/102638 | |
| Lock Screen | **pantalla de bloqueo** (also "pantalla bloqueada" once in a developer's text) | https://support.apple.com/es-es/guide/iphone/iph4d0e6c351/ios ; https://support.apple.com/es-es/102638 | |
| Widgets | widgets; galería de widgets; "Editar widgets" | https://support.apple.com/es-es/guide/iphone/iphb8f1bf206/ios ; https://support.apple.com/es-es/guide/mac-help/mchl52be5da5/mac | English kept |
| Smart Stack | **grupo inteligente** ("Un grupo inteligente (un widget con puntos junto a él)"; Watch: "Ver widgets según la hora en el grupo inteligente") | https://support.apple.com/es-es/guide/iphone/iphb8f1bf206/ios ; https://support.apple.com/es-es/guide/watch/apdecf142fb9/watchos | Not "Smart Stack"; not "pila inteligente" (Observa's store text says "Pila" for its own widget) |
| Live Activities | **actividades en directo**; “Actividades en directo” (setting: Ajustes > Apps > [app] > “Actividades en directo”) | https://support.apple.com/es-es/guide/iphone/iph28f50d10d/ios ; https://support.apple.com/es-es/guide/iphone/iph3d92302ee/ios ; https://support.apple.com/es-es/guide/watch/bz1vx4mwqbw9/watchos | Not "Live Activities" |
| Dynamic Island | Dynamic Island (feminine: "la Dynamic Island", "en la Dynamic Island") | https://support.apple.com/es-es/guide/iphone/iph28f50d10d/ios | English kept |
| StandBy | **“En reposo”** (modo “En reposo”; "esferas de “En reposo”") | https://support.apple.com/es-es/guide/iphone/iph878d77632/ios | Not "StandBy", not "En espera". Settings: Ajustes > “En reposo” |
| Control Center | **centro de control** (lowercase) | https://support.apple.com/es-es/guide/iphone/iph59095ec58/ios ; https://support.apple.com/es-es/guide/mac-help/mchlc9d0e1f2/mac | Article 108350 writes "Centro de control" capitalised once; guides lowercase |
| Notification Center | centro de notificaciones | https://support.apple.com/es-es/guide/iphone/iph6534c01bc/ios | |
| Notifications | notificaciones (“Permitir notificaciones”, “Notificaciones importantes”, “Resumir notificaciones”) | https://support.apple.com/es-es/guide/iphone/iph7c3d96bab/ios | Time Sensitive = “Notificaciones importantes” |
| Share Sheet / Share button | botón Compartir; menú Compartir | https://support.apple.com/es-es/guide/iphone/iphc572ca489/ios | |
| AirDrop | AirDrop | https://support.apple.com/es-es/guide/iphone/iphcd8b9f0af/ios | English kept |
| Spotlight | Spotlight | https://support.apple.com/es-es/guide/iphone/iph3c511548/ios | English kept |
| Siri | Siri; "Di “Siri” u “Oye Siri”"; ajustes: Ajustes > Siri | https://support.apple.com/es-es/guide/iphone/iph83aad8922/ios ; https://support.apple.com/es-es/105020 (Siri en todos tus dispositivos Apple) | |
| Apple Intelligence | Apple Intelligence | https://support.apple.com/es-es/guide/iphone/iph1fbe7d2b9/ios ; apv | English kept |
| Shortcuts (app) | **la app Atajos**; atajos (user shortcuts); "Usar la app Atajos para automatizar tareas" | https://support.apple.com/es-es/guide/iphone/iph47e1c9d7d/ios ; https://support.apple.com/es-es/guide/shortcuts/welcome/ios (title "Manual de uso de Atajos") | Not "Accesos directos". Keyboard shortcuts are "atajos de teclado" too |
| Universal Clipboard | **Portapapeles Universal** (capitals in the guide's first mention); "portapapeles universal" later | https://support.apple.com/es-es/guide/iphone/iph220ea8dca/ios | |
| Handoff | Handoff | same | English kept |
| Picture in Picture | **imagen dentro de imagen** (“Imagen dentro de imagen” as window name) | https://support.apple.com/es-es/guide/iphone/iphcc3587b5d/ios | |
| Airplane Mode | **modo Avión** (capital A) | https://support.apple.com/es-es/guide/iphone/iph59095ec58/ios ; https://support.apple.com/es-es/guide/watch/apdc22c9d320/watchos ("Usar el modo Avión") | |
| Low Power Mode | **modo de bajo consumo**; iOS 27: “Modo de consumo” (Ajustes > Batería) and “Consumo adaptativo” | https://support.apple.com/es-es/guide/iphone/iphcab9aecd1/ios | Page title "Ahorrar batería con los modos de consumo del iPhone" |
| Dark Mode | **modo oscuro** (lowercase; “Modo Oscuro” as the control center tile; setting Ajustes > Pantalla y brillo > Oscuro) | https://support.apple.com/es-es/108350 | |
| Appearance (iOS 27) | “Aspecto” (Ajustes > Aspecto > “Tamaño del texto”, “Texto en negrita”, Liquid Glass, “Zoom de pantalla”) | https://support.apple.com/es-es/guide/iphone/iphd6804774e/ios | |
| Accessibility | Accesibilidad | https://support.apple.com/es-es/guide/iphone/iph3e2e4367/ios | |
| VoiceOver | VoiceOver | wg ; ig TOC | English kept |
| Larger Text (Dynamic Type setting) | “**Tamaño del texto**” (iOS 27, Ajustes > Aspecto); “Texto más grande” (under Zoom de pantalla); “Pantalla y tamaño del texto” (Accesibilidad) | https://support.apple.com/es-es/guide/iphone/iphd6804774e/ios | The Accessibility "Texto más grande" slider page itself was not opened |
| Reduce Motion | **Reducir movimiento** (Ajustes > Accesibilidad > Movimiento > Reducir movimiento) | https://support.apple.com/es-es/111781 | Not "Reducir animaciones" |
| Offline | sin conexión ("Descargar mapas sin conexión", "modo sin conexión") | ig TOC | |
| Privacy & Security | **Privacidad y seguridad** (bare in paths: "Ajustes > Privacidad y seguridad") | https://support.apple.com/es-es/guide/iphone/iph4f4cbd242/ios ; https://support.apple.com/es-es/guide/iphone/iph251e92810/ios | |
| App Tracking | **Rastreo** (Ajustes > Privacidad y seguridad > Rastreo); toggle “Permitir que las apps soliciten rastrearte” | https://support.apple.com/es-es/guide/iphone/iph4f4cbd242/ios ; https://support.apple.com/es-es/102420 | See App Tracking Transparency in the store section. Not "Seguimiento" (Spain uses "rastreo/rastrear"; "Seguimiento" in Spain Apple copy means "tracking progress of health") |
| Analytics share with developers | Ajustes > Privacidad y seguridad > **Análisis y mejoras**; “Compartir con desarrolladores” (older) | https://support.apple.com/es-es/108971 | Newer label not verified beyond "Compartir análisis del iPhone y el Apple Watch" |
| Background App Refresh | not verified | no es-es page found with the label (es-es article 118408 is the app switcher, not Background App Refresh) | |
| Restore purchases | Apple's phrases: "Restaurar en el iPhone ítems comprados y eliminados"; "Volver a descargar apps desde Apple" | https://support.apple.com/es-es/guide/iphone/iphfe205f2e5/ios | In-app StoreKit button label not documented on a Spain page |

## Built-in apps

| English | Spanish (Spain) as Apple writes it | Source | Note |
|---|---|---|---|
| Reminders | Recordatorios (la app Recordatorios) | ig TOC; https://support.apple.com/es-es/guide/iphone/iphd6804774e/ios (ajustes) | |
| Calendar | Calendario (la app Calendario) | https://support.apple.com/es-es/guide/iphone/iph3d110f84/ios | Event = "evento" |
| Files | Archivos (la app Archivos) | https://support.apple.com/es-es/guide/iphone/iphbbcf8827d/ios | |
| Photos | Fotos (la app Fotos) | ig TOC | |
| Camera | **Cámara** (la app Cámara; “Control de la cámara”) | ig TOC (section "Cámara") | |
| Notes | Notas | ig TOC | |
| Clock / Alarm | Reloj (la app Reloj); despertador; alarma | https://support.apple.com/es-es/guide/iphone/iphaf56dceb4/ios ("desde la app Reloj") | |
| Games app | la app Apple Games; Game Center | https://support.apple.com/es-es/guide/iphone/iph3aed54d2e/ios | English kept |
| Wallet | **Cartera** (la app Cartera); marketing "Cartera de Apple" | https://support.apple.com/es-es/guide/iphone/iph9b7f53382/ios ; https://support.apple.com/es-es/guide/watch/apd16914b6d1/watchos ; apv footer ("Cartera de Apple") | Not "Wallet" |
| Apple Pay | Apple Pay | https://support.apple.com/es-es/guide/iphone/iphbd4cf42b4/ios | English kept |
| Sign in with Apple | **“Iniciar sesión con Apple”** | https://support.apple.com/es-es/guide/iphone/iph238921d37/ios | |
| Passwords | Contraseñas | ig TOC | |
| Maps | Mapas | ig TOC | |
| Weather | Tiempo | wg TOC | |
| Stocks | Bolsa | ig TOC | |
| Messages / Mail | Mensajes / Mail | ig TOC | |
| Voice Memos | Notas de Voz (Watch, title case) | wg TOC | |

## Devices and platforms

| English | Spanish (Spain) as Apple writes it | Source | Note |
|---|---|---|---|
| iPhone, iPad, Mac | iPhone, iPad, Mac (el iPhone, el iPad, el Mac) | ap ; ig | |
| Apple Watch | el Apple Watch | ap ; ah ; wg | |
| Apple Vision Pro | Apple Vision Pro (article 118428: "en las Apple Vision Pro") | https://support.apple.com/es-es/118428 ; ap (compat label "Apple Vision") | App Store compatibility label says "Apple Vision" |
| iOS, iPadOS, macOS, watchOS, visionOS | unchanged ("Requiere iOS 17.6 o posterior.") | ap | |
| Designed for iPad / iPhone (on Mac) | "Diseñado para iPad. No verificado para macOS." (Observa) ; "Diseñada para iPhone. No verificada para macOS." (EarnLock) | https://apps.apple.com/es/app/id6757438990 ; https://apps.apple.com/es/app/id6771099230 | Apple writes the participle in the gender of the app's title word: masculine for Observa, feminine for EarnLock (Spanish text agrees with "app" in EarnLock's case). Copy exactly per page |
| Mac chip wording | "Requiere macOS 14.6 o posterior y un Mac con el chip M1 de Apple o posterior." | https://apps.apple.com/es/app/id6757438990 | |

## App Store and developer

| English | Spanish (Spain) as Apple writes it | Source | Note |
|---|---|---|---|
| App Store | el App Store (la app App Store) | https://support.apple.com/es-es/guide/iphone/iphc90580097/ios | |
| "Download on the App Store" badge | **Line 1: Consíguelo en el / Line 2: App Store** | https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/es-es (SVG title "Download_on_the_App_Store_Badge_ES_RGB_blk_100217"; same file at https://toolbox.marketingtools.apple.com/api/v2/badges/download-on-the-app-store/black/es-es; rendered with rsvg-convert and read 2026-11-19) | Spain wording is "Consíguelo en el". The Mexican badge (`es-mx`, same API) reads "Descárgalo en el" and must NOT be used. The artwork is outlined paths, so there is no text node; read from the rendered image |
| "Download on the Mac App Store" badge | **Line 1: Consíguelo en el / Line 2: Mac App Store** | https://tools.applemediaservices.com/api/badges/download-on-the-mac-app-store/black/es-es (rendered and read) | |
| App Privacy (section) | **Privacidad de la app** (section heading); "Prácticas de privacidad" in the text | https://apps.apple.com/es/app/id6806255929 | |
| Data Not Collected | **No se recopilan datos**; sub-line: "El desarrollador no recopila ningún dato en esta app." | https://apps.apple.com/es/app/id6806255929 | |
| Data Used to Track You | "Datos usados para rastrearte" | https://apps.apple.com/es/app/id526641427 | |
| Data Linked to You | "Datos vinculados contigo" | https://apps.apple.com/es/app/id1550574178 ; id526641427 | |
| Data Not Linked to You | "Datos no vinculados contigo" | https://apps.apple.com/es/app/id1550574178 | |
| Purposes in the privacy label | "Publicidad de terceros", "Publicidad o marketing del desarrollador", "Análisis de datos", "Personalización del producto", "Funcionalidad de la app" | https://apps.apple.com/es/app/id526641427 ; id1550574178 | |
| Privacy nutrition label | not verified as a noun phrase; the store section is "Privacidad de la app" and the disclaimer is "Esta información no ha sido verificada por Apple." (Apple's help link: “Definiciones y ejemplos de privacidad”) | https://apps.apple.com/es/app/id6806255929 ; apv shows a "Fichas" nav tab (not about labels) | "etiqueta de privacidad" is NOT confirmed on any Apple Spain page I fetched |
| Privacy Manifest | not verified | developer.apple.com/es/... redirects to the Latin American /la/ site or English | |
| App Store Connect | App Store Connect (English kept) | https://support.apple.com/es-es/guide/app-store-connect/welcome/web → 404 on es-es (the French pattern was a French "page introuvable" page); no Spain page | not verified |
| TestFlight | TestFlight (English kept) | https://testflight.apple.com/ (English page); https://support.apple.com/es-es/guide/testflight/welcome/ios → 404 | not verified |
| Xcode, CloudKit, Feedback Assistant | English kept | developer.apple.com pages do not exist for Spain | not verified |
| Universal Purchase | not verified | no es-es page; developer.apple.com/es pages redirect to /la/ or 404 | Do not invent "compra universal" |
| App Tracking Transparency | name kept in English by developers; Apple Spain's article title: "Si una app pide rastrear tu actividad"; buttons «Permitir» and «Pedir a la app que no rastree»; toggle “Permitir que las apps soliciten rastrearte”; verb phrase "rastrear tu actividad" | https://support.apple.com/es-es/102420 ; https://support.apple.com/es-es/guide/iphone/iph4f4cbd242/ios | The ATT system prompt title is not on any Spain page fetched (not verified) |
| Report a Problem (reportaproblem.apple.com) | Apple's article names the site: "Inicia sesión en reportaproblem.apple.com." The menu entry is « Me gustaría » > « Solicitar un reembolso » (bare, capitalised: Me gustaría, Solicitar un reembolso). iPhone guide link: "Informar de un problema con un juego" | https://support.apple.com/es-es/118223 ; https://support.apple.com/es-es/guide/iphone/iph7b4e902b1/ios (title only) | "Informar de un problema" (not "Notificar") |
| Refund request | **Solicitar un reembolso**; article "Solicitar el reembolso de las compras de apps o contenido de Apple"; steps: Inicia sesión en reportaproblem.apple.com > toca o haz clic en Me gustaría > Solicitar un reembolso > elige el motivo > Siguiente > elige la app > Enviar; "Esperar de 24 a 48 horas" | https://support.apple.com/es-es/118223 | No refund promise |
| Purchase history | **Historial de compras** (App Store > tu foto > Apps e historial de compras > Historial de compras) | https://support.apple.com/es-es/guide/iphone/iph4e3e7324f/ios | |
| Re-download apps | "Ver y volver a descargar apps"; Apps e historial de compras > Tus apps | same | |
| Manage / cancel subscriptions (path) | Ajustes > tu nombre > Suscripciones > la suscripción > Cancelar Suscripción | https://support.apple.com/es-es/118428 | Trial note not on this page's fetched part |
| Price label | **Gratis** (price line "Gratis · Compras dentro de la app") | https://apps.apple.com/es/app/id6806255929 | |
| Get button | **Obtener** | same (raw `"title":"Obtener"`) | |

## Spanish App Store product page labels

Copied from https://apps.apple.com/es/app/id6806255929 (Tare), https://apps.apple.com/es/app/id6757438990 (Observa), https://apps.apple.com/es/app/id6771099230 (EarnLock), plus id1550574178 and id526641427 for the privacy-label rows.

| Label | Exact Spanish text |
|---|---|
| Price line (free app with IAP) | `Gratis · Compras dentro de la app` (Observa adds `· Diseñado para iPad. No verificado para macOS.`; EarnLock `· Diseñada para iPhone. No verificada para macOS.`). Separators are plain space, U+00B7 MIDDLE DOT, plain space |
| Free | Gratis |
| Get button | Obtener |
| Ratings section | Valoraciones y reseñas. Empty state: "Esta app no ha recibido suficientes valoraciones o reseñas como para mostrar una visión general." |
| Age rating | header chip: Clasificación por edades, value "4+" with caption "Años" (Observa "9+" "Años"); Information row: Edad "4+"; Observa adds Contiene: "Temas de salud o bienestar" |
| Category | header chip and row: Categoría (Tare: Puzle; Observa: Salud y forma física; Pawza: Estilo de vida) |
| Developer | header chip: **Desarrollador**; Information row: **Proveedor** |
| Language | header chip: Idioma ("ES y 43 más"); Information row: Idiomas ("Español y 43 más", then the full list; language names capitalised: Español, Alemán, Francés, Inglés) |
| Size | Tamaño: `11,3 MB`, `92,7 MB` (U+00A0 before MB) |
| Compatibility | Compatibilidad: "Requiere iOS 18.0 o posterior." / "Requiere iPadOS 18.0 o posterior." / Mac: "Requiere macOS 14.6 o posterior y un Mac con el chip M1 de Apple o posterior." / Apple Watch: "Requiere watchOS 10.0 o posterior." / Apple Vision: "Requiere visionOS 1.3 o posterior." (NBSP inside "iOS 18.0"; no ending "versión") |
| Info section heading | Ficha técnica |
| In-App Purchases | Compras dentro de la app: "Sí", then one row per item (`Capítulos II–X 2,99 €`) |
| Accessibility | Accesibilidad; "Prestaciones compatibles"; "El desarrollador no ha indicado todavía las prestaciones de accesibilidad que son compatibles con la app." |
| Family Sharing | Compatibilidad > En familia |
| Privacy section | Privacidad de la app; "No se recopilan datos"; link “Definiciones y ejemplos de privacidad”; disclaimer "Esta información no ha sido verificada por Apple." |
| Privacy policy link | Política de privacidad |
| Developer website | Sitio web del desarrollador |
| Other sections | Novedades (version "Versión 1.2 hace 6 d", "Historial de versiones", version dates "27 oct"); Más de <developer>; Quizá también te guste; Vistas previas de la app y capturas de pantalla; Compartir; Soporte (footer); "Términos del servicio de internet"; "App Store y la privacidad"; "Aviso sobre cookies" |
| Platform names in nav | iPhone, iPad, Mac, Watch, TV (nav tabs: Hoy, Juegos, Apps, Arcade, Buscar; "Plataforma" menu) |
| Meta title / description | `App <name> - App Store` (U+00A0 inside "App Store"); "Descarga <name> de <developer> en App Store. Mira capturas de pantalla, valoraciones y reseñas, consejos de usuarios y más apps como…" (og:description; note "en App Store" without "el") |

In-app purchase price format: `2,99 €`. Comma decimal, then a **NO-BREAK SPACE (U+00A0)**, then €. Checked in the raw HTML (Tare "Capítulos II–X 2,99 €").

## Spanish App Store category names

Read from the "Categoría" field of live apps.apple.com/es/app/id... pages on 2026-11-19 (sample app and ID in the last column). The `apps.apple.com/es/genre/...` pages were not tried. Apple answered HTTP 429 to part of a batch; retried with pauses; the one ID still blocked (Business) is listed as "not verified".

| English | Spanish as the App Store shows it | Sample page (https://apps.apple.com/es/app/id...) |
|---|---|---|
| Health & Fitness | Salud y forma física (NOT "Salud y bienestar") | id6757438990 (Observa) |
| Productivity | Productividad | id1232780281 |
| Finance | Finanzas (plural) | id283646709 |
| Business | not verified (HTTP 429 on retries) | id618783545 |
| Developer Tools | Para desarrolladores | id6756589122 (Mockly) |
| Games > Puzzle | Puzle | id6806255929 (Tare) |
| Games > Board | Juegos de mesa | id6761336870, id6761656926, id6794340136, id6759511759 |
| Games > Strategy | Estrategia | id529479190 |
| Games > Adventure | Aventura | id479516143 |
| Games (tab) | Juegos | nav tab on every page |
| Utilities | Utilidades | id6757253009 |
| Education | Educación | id570060128 |
| Books | Libros | id302584613 |
| Lifestyle | Estilo de vida | id429047995, id6773507068 (Pawza) |
| Graphics & Design | Diseño gráfico | id916366645 |
| Photo & Video | Foto y vídeo | id1500855883 |
| Reference | Referencia (singular) | id324715238 |
| Entertainment | Entretenimiento | id363590051 |
| Travel | Viajes | id401626263 |
| Music | Música | id324684580 |
| Navigation | Navegación | id585027354 |
| Food & Drink | Comida y bebida | id1058959277 |
| News | Noticias | id1064216828 |
| Sports | Deportes | id382002079 |
| Medical | Medicina | id321367289 |
| Weather | Tiempo | id295646461 |
| Shopping | Compras | id282614216 |
| Social Networking | Redes sociales | id310633997 |

Not checked: Magazines & Newspapers, Kids, other Games subcategories (Action, Card, Casino, Casual, Family, Music, Racing, Role Playing, Simulation, Sports, Trivia, Word).

## Unverified (best guesses, not confirmed on an Apple Spain page)

| English | Best guess | Why unverified |
|---|---|---|
| Medical ID (feature name) | no guess; use "datos médicos" only in the sense Apple writes ("Configurar y consultar datos médicos", Watch guide TOC) | The iPhone Health page that names the feature was not opened |
| Downtime / App Limits (iOS 26 and earlier) | none | Older iOS guide versions not opened; iOS 27 uses “Horario de tiempo de uso” and “Límites de tiempo” |
| Privacy nutrition label (noun) | none | Not on any Apple Spain page fetched; the store uses "Privacidad de la app" |
| Privacy manifest, Universal Purchase, App Store Connect, TestFlight, Xcode, CloudKit, Feedback Assistant, Family Controls, Dynamic Type (developer term), StoreKit "Restore Purchases" button | English kept | developer.apple.com/es/... redirects to the Latin American /la/ site or English; support.apple.com/es-es guides for App Store Connect and TestFlight return 404 |
| Background App Refresh | none | No Spain page with the label found |
| ATT system prompt title | none | Only the buttons and settings are documented |
| Analytics label (newest iOS) | "Análisis y mejoras" | Article 108971 names it in the iOS 10 steps; newest label not re-read |
| Business category | none | HTTP 429 |
| Sleep tab name on iPhone | "Descanso" (iOS 27 guide) or "Sueño" (article, Watch guide) | Apple's own pages disagree |
| Salud tab name Explorar / Examinar | "Explorar" (iOS 27 guide, new article 108790) | "Examinar" appears in article 108906 and one older block; the guide you should follow is "Explorar" |

## Added rows (same extra rows as the French and German files)

| English | Spanish as Apple writes it | Source | Note |
|---|---|---|---|
| Medications (inconsistency) | iPhone guide intro: "toca “Explorar” > Medicamentos > Añadir un medicamento"; medications page: "Toca Explorar y, a continuación, toca Medicación" | https://support.apple.com/es-es/guide/iphone/iphcae7451f3/ios ; https://support.apple.com/es-es/guide/iphone/iph811670c81/ios | Use "Medicación" for the feature |
| Share With App Developers (Analytics) | Ajustes > Privacidad y seguridad > Análisis y mejoras > Compartir análisis del iPhone y el Apple Watch | https://support.apple.com/es-es/108971 | |
| Delete data from iCloud (storage path) | Ajustes > tu nombre > iCloud > ... ("Gestionar el almacenamiento de iCloud en un dispositivo Apple") | https://support.apple.com/es-es/108922 | Exact tap-target not re-read |
| Cancel a subscription | iPhone: «Cancelar Suscripción»; Mac and Windows: "haz clic en Cancelar Suscripción" | https://support.apple.com/es-es/118428 | Expired: "mensaje de caducidad en texto rojo" |
| Request a refund | reportaproblem.apple.com > Me gustaría > Solicitar un reembolso | https://support.apple.com/es-es/118223 | |
| Camera app | **Cámara** (iOS 27 guide); no "Cámara fotográfica" | ig TOC | |
| Control Center on Mac | centro de control (Mac: "haz clic en su icono de la barra de menús") | https://support.apple.com/es-es/guide/mac-help/mchlc9d0e1f2/mac | |
| Stage Manager | **organizador visual** | https://support.apple.com/es-es/guide/mac-help/mchl534ba392/mac | |
| Desktop widgets (Mac) | widgets del escritorio; "centro de notificaciones" | https://support.apple.com/es-es/guide/mac-help/mchl52be5da5/mac | |
| System Settings | Ajustes del Sistema (capital S on "Sistema" in the Mac guide: "Cambiar los Ajustes del Sistema") | https://support.apple.com/es-es/guide/mac-help/mchlc9d0e1f2/mac ; mg TOC | |
| Calendar event / Reminders list | evento; recordatorio; "listas inteligentes" | ig TOC | |
| Smart folders | "carpetas inteligentes" | ig TOC | |

## Note from Tier 4 batch 2 (2026-11-19)

- Heart rate app: support.apple.com/es-es/120277 writes «app Frecuencia cardiaca» (sentence case); 120276 and the Watch guide write «Frecuencia
  Cardiaca». The site uses sentence case; don't «correct» it. Watch labels «Frec. en reposo», «Media andando», Intervalo (guide apda88aefe4c).
- Screen Time iOS 27: «Límites de tiempo», «Horario de tiempo de uso», «Compartir entre dispositivos»; iOS 26: «Límites de uso de apps»,
  «Tiempo de inactividad» (iphbfa595995, both versions). «Filtros de color» (iph3e2e1fb0).
