# Spanish glossary per app (es, Spain)

Part of the language sheet `_i18n/es.md`. Extracted 2026-11-19 from each app's string catalog (read-only, locale `es`; Mockly and Millrace use `es-ES`) and its Spanish App Store listing (apps.apple.com/es and the iTunes lookup API, country=es). Spanish UI strings are verbatim from the catalogs: use them exactly on the site, except where a note says the app string is defective (missing accents, English left in, Latin-American vocabulary). Every app writes tú, like the site. Store prices here are reference only: the site prints prices from the catalog.

## Spanish glossary, batch 1: aftershift, allpaid, appmeta, appmeta-pulse, chessful

Method (checked 2026-11-19). Read-only extraction from each app's source catalogs under `~/Downloads/` (xcstrings parsed as JSON with `python3 -I`; AfterShift's legacy `.lproj/*.strings` and `.stringsdict` converted with `plutil`). "total" = translatable keys (`shouldTranslate: false` and blank keys excluded; stale keys are counted, the non-stale figure is given in brackets where it differs); "es" = keys whose `es` value has state `translated` (or plural/substitution variations, or a translated stringSet). Locale `es` is Spain Spanish; every catalog also carries `es-MX` values (no `es-419` anywhere), ignored here, and no key lacks an `es` value except the format-only ones named below. Spanish values are copied verbatim from the catalogs (apostrophes, `«»` quotes, `—` and capitalization as in source). Counts differ from the French sheet for the same catalogs (for example Pulse 1418 here vs 999 there) because the catalogs have grown and this run also counts every non-blank, non-`shouldTranslate:false` key. App Store data: iTunes lookup API (`country=es&lang=es_es`, `country=us&lang=en_us`) plus the raw `serialized-server-data` JSON of `apps.apple.com/es/app/id<ID>` (Safari UA, `Accept-Language: es-ES`; two or three 429 retries with 25–30 s pauses were enough, all five Spanish pages and all five US pages were read). Prices keep the NBSP (U+00A0) before `€` and are reference only. Register counts are rough regexes on Spanish values (tú = tu/tus/te/ti/contigo, eres/tienes/puedes/quieres/necesitas/estás and common tú imperatives such as "toca", "añade", "desbloquea"; usted = "usted/ustedes" plus common usted imperatives such as "toque", "seleccione", "añada"). Usted/vos hits were hand-checked: there are none (see Formality). The listing page also prints the seller's personal name and address; deliberately not copied.

Formality across catalogs (rough): **all five apps write tú (informal singular)**, with no usted and no vos anywhere. Tú-marked values: AfterShift ~250–270 of 1484 (widget 5 of 15), AllPaid ~75–85 of 653, AppMeta ~255–305 of 2282, AppMeta Pulse ~235–270 of 1612, Chessful Localizable ~325–390 of 2146 and Lessons ~1160–1310 of 3649 (lesson text is also tú: "Cuando estás peor, juega activamente…"). Zero values contain "usted", "ustedes", "vos" or voseo forms; the regex "usted" hits in a looser pass were false positives ("puede", "tiene", "su" referring to a third party, "Pulse" the app name). Impersonal infinitives are used for some buttons ("Suscribirse", "Desbloquear", "Restaurar compras"), which is neutral. The site writes tú, so every Spanish term can be quoted as is; the only care points are the two store-listing names that carry a tú imperative (AllPaid subtitle, Chessful name) and the LatAm-leaning words listed under Flags.

---

### 1. AfterShift (`aftershift`, source `shiftworkersleep/`, ID 6757163182)

### Spanish coverage
- Main app, legacy `.lproj` (no xcstrings): `en.lproj/Localizable.strings` 1484 keys, `es.lproj/Localizable.strings` 1484 keys, 0 missing, 0 extra, 23 values identical to English ("Premium", "REM", "AfterShift"-style names). `Localizable.stringsdict` en and es both present (4 plural keys: `plural.naps`, `plural.days`, `plural.hours`, `plural.daysRemaining`; es forms "%d siesta/siestas", "%d día/días", "%d hora/horas", "%d día restante/días restantes"). → **100 %**
- `es.lproj/AppShortcuts.strings`: 16 Siri/Shortcuts phrases in Spanish, all in tú or neutral (e.g. "Registrar sueño en ${applicationName}", "Cuándo es mi próximo turno en ${applicationName}", "Próximo turno en ${applicationName}", "Pregúntale a ${applicationName} cuándo debo dormir", "Próxima ventana de sueño en ${applicationName}", "Cómo llego al turno en ${applicationName}", "Apunta mis horas de sueño en ${applicationName}", "Registra mi sueño en ${applicationName}", "Cuál es mi ventana de sueño en ${applicationName}", "Preparación para el turno en ${applicationName}", "Comprueba mi preparación en ${applicationName}", "Dile a ${applicationName} que he dormido", "Cuál es mi próximo turno en ${applicationName}", "Pregúntale a ${applicationName} si llego bien al turno", "Pregúntale a ${applicationName} cuándo me toca trabajar", "Cuándo debería dormir en ${applicationName}"). Siri phrases ARE in Spanish (Spain forms: "he dormido", "me toca").
- Widget `shiftworkersleepWidget/Localizable.xcstrings`: 15 / 15 → 100 % (the widget gallery names and descriptions live under `widget.gallery.*` in this catalog).
- InfoPlist: `es.lproj/InfoPlist.strings` has 2 keys: `CFBundleDisplayName` ("AfterShift") and `NSHealthShareUsageDescription` ("AfterShift lee tus datos de sueño de Apple Salud para calcular la deuda de sueño y la recuperación entre turnos."). **English-only:** `NSCalendarsUsageDescription` / `NSCalendarsFullAccessUsageDescription` are build settings with no localization ("AfterShift reads your calendar events to automatically detect work shifts. No data is uploaded — everything stays on your device."), so the calendar permission prompt is English on a Spanish device. `NSHealthUpdateUsageDescription` is debug-only.
- Paywall (`paywall.*`) translated.
- **Verdict: app is in Spanish (Spain): yes**, with one English permission prompt (calendar access).

### Glossary
| English term on site | English UI string (key) | Spanish UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Today (screen / tab) | Today (`tab.today`) | Hoy | |
| Coach (screen) | Coach (`tab.coach`, `coach.title`) | Guía | Not "Coach": the tab is "Guía" |
| Roster (shift calendar) | Roster (`tab.roster`) | Turnos | widget `widget.gallery.roster.name` also "Turnos"; the store text and one in-app string use "cuadrante" (`settings.shiftTypes.hint`: "…tantos como necesite tu cuadrante") |
| Settings | Settings (`tab.settings`) | Ajustes | |
| Shift Recovery Score | Shift Recovery Score (`recovery.shiftRecoveryScore`) | Puntuación de recuperación por turnos | distinct from Sleep Score (unlike French) |
| Sleep Score | Sleep Score (`sleepScore.title`) | Puntuación de sueño | `sleepScore.unlock` = "Desbloquear puntuación de sueño" |
| Readiness | Readiness (`readiness.title`; widget `widget.gallery.readiness.name`) | Estado de preparación | **Flag:** `shiftChange.readiness` "Readiness" = "Nivel de recuperación"; `readiness.locked` = "Recuperación bloqueada"; `intent.readiness.title` "Shift Readiness" = "Preparación para el turno"; `swap.headline.improved` = "La preparación debería mejorar". The store text also says "Estado de preparación". Use "Estado de preparación" |
| On-call | On-call (`sleepScore.onCall`) | De guardia | `schedule.irregular` "Irregular/On-Call" = "Irregular/De guardia"; `coach.onCall.title` = "Modo de recuperación de guardia"; "guardia" is used consistently (33 values) |
| Naps | Naps (`naps.title`) / Nap (`nap.label`) | Siestas / Siesta | `today.logNap` "Log Nap" = "Registrar siesta"; stringsdict "%d siesta/siestas" |
| Nap window | Optional nap window (`notification.napWindow.title`) | Ventana de siesta opcional | `insight.notification.napWindow.title` "Nap window" = "Ventana de siesta" |
| Sleep window | Sleep window (`notification.sleepWindow.title`) | Ventana de sueño | `intent.sleepWindow.title` "Next Sleep Window" = "Próxima ventana de sueño" |
| Sleep Timing | Sleep Timing (`timing.title`) | Horario de sueño | `paywall.free.sleepTiming` = "Horarios de sueño entre turnos" |
| Sleep debt | Sleep debt trend (`debtTrend.title`); widget Sleep debt | Deuda de sueño | widget `widget.gallery.sleepDebt.name` "Deuda de sueño"; trend strings "Tendencia…" ("Aún no hay suficientes datos para mostrar la tendencia") |
| Sleep stages Awake / Core / Deep / REM | `stages.awake/core/deep/rem` | Despierto / Ligero / Profundo / REM | `stages.sleepStages` = "Fases del sueño"; Core → "Ligero" is the app's own choice, check it against Apple Salud's Spanish stage labels before the site relies on it |
| Time in bed | Time in bed (`timing.timeInBed`) | Tiempo en cama | |
| Fragmentation | Fragmentation (`continuity.fragmentation`) | Fragmentación | `paywall.premium.fragmentation` = "Análisis de fragmentación y continuidad" |
| Caffeine timing | Caffeine timing (`coach.caffeine.title`) | Tiempo de la cafeína | **Flag, three forms:** `technique.caffeineTiming.title` "Caffeine Timing" = "Timing de la cafeína" (anglicism), `caffeine.header` "Caffeine Timing" = "Consumo de cafeína" (means consumption), `caffeine.trend.excellent` = "Excelente horario de cafeína en las últimas 2 semanas" |
| Caffeine cut-off | Caffeine cutoff (`notification.caffeineCutoff.title`) | Límite de cafeína | consistent ("tu límite de cafeína", "límite 8h") |
| Wind-down reminder | Wind down (`notification.windDown.title`) | Relajación | **Flag, three forms:** `insight.notification.windDown.title` "Wind-down time" = "Hora de relajarse"; `playbook.step.windDown.title` "Wind down" = "Desacelera"; "tiempo de relajación" in insights |
| Calendar shift import | Import from calendar (`roster.calendarImport`) | Importar del calendario | `onboarding.calendar.title` = "Importa tu horario" |
| Calendar sync (Premium) | Calendar Sync (`calendar.sectionTitle`) | Sincronización del calendario | `calendar.upgradeAutoSync` = "Mejora: sincronización automática, varios calendarios y horas extra"; `paywall.premium.calendarSync` = "Sincronización automática del calendario y registro de horas extra" |
| Overtime | Overtime: (`nextShift.overtime`) | Horas extra: | `nextShift.overtime.addOneHour` = "Añadir 1 hora extra" |
| Add a shift | Add shift (`roster.addShift`, `today.addShift`) | Agregar turno | **Flag:** "Agregar" 20 values vs "Añadir" 12 values inside the same catalog (`nextShift.overtime.addOneHour` "Añadir 1 hora extra", but `roster.addShift` "Agregar turno"); "agregar" is the Latin-American form, Spain says "añadir" |
| Shift types | Day / Evening / Night / Off (`shift.day/evening/night/off`) | Día / Tarde / Noche / Libre | |
| Shift change | Shift change impact (`shiftChange.title`) | Impacto del cambio de turno | `insight.shiftChange.title` = "Cambio de turno"; `overtime.extended` = "Turno cambiado de %@ a %@ (+%d min)." |
| Repeating rotation | Repeating rotation (`roster.rotation`) | Ciclo de turnos recurrente | `rotation.presets` "Common rotations" = "Ciclos habituales". **Flag:** `roster.tapToAdd` = "Toca + para agregar un turno" (drops "or set up a repeating rotation") |
| Three-shift (day → evening → night) | `rotation.preset.threeShift` (+ `.sub`) | Tres turnos (sub: Día → tarde → noche, 2 de cada) | |
| 4-on-4-off | `rotation.preset.fourOnFourOff` | 4 y 4 | sub: "Cuatro noches y cuatro días libres" |
| 4-on-3-off | `rotation.preset.fourOnThreeOff` | 4 y 3 | sub: "Cuatro días y tres libres" |
| 2 days / 2 nights | `rotation.preset.ddnn` | 2 días / 2 noches | sub: "Dos días, dos noches y cuatro libres" |
| Panama/Pitman (2-2-3) | `rotation.preset.panama` | Panamá (2-2-3) | sub: "2-2-3 rotativo, un fin de semana libre de cada dos" |
| Fixed nights | `rotation.preset.fixedNights` | Noches fijas | sub: "Cinco noches, fines de semana libres" |
| Fixed days | `rotation.preset.fixedDays` | Días fijos | sub: "Cinco días, fines de semana libres" |
| Trends | Trends (`trends.title`) | Tendencias | `today.section.trends` "Trends & Insights" = "Tendencias e ideas" |
| Do this now (playbook) | Do this now (`playbook.cardKicker`) | Haz esto ahora | tú imperative; widget `widget.label.doThisNow` = "Hazlo ahora" |
| Techniques | Techniques (`library.title`) | Técnicas | |
| Export / PDF report | Export Sleep Report (`settings.exportReport`) | Exportar reporte de sueño | **Flag:** "reporte" (7 values, LatAm) vs "informe" (3 values: `export.title` "INFORME DE SUEÑO AFTERSHIFT", `export.pdf.filename` "AfterShift-Informe-%@.pdf", `export.dataLoadError`); `premium.export.title` = "Exportar reporte". Spain: "informe" |
| Live Activity / Lock Screen | Shift countdown on Lock Screen (`liveactivity.settings.title`) | Cuenta atrás del turno en la pantalla bloqueada | "cuenta atrás" is the Spain form |
| Widgets: Next Shift, Shift Plan, Rhythm, Sleep Debt, Roster, Readiness (+ Sleep Graph) | `widget.gallery.*.name` | Próximo turno, Plan del turno, Ritmo, Deuda de sueño, Turnos, Estado de preparación, Gráfico de sueño | the widget catalog carries seven names including `sleepGraph` = "Gráfico de sueño"; descriptions e.g. "Cuenta atrás en directo hasta tu próximo turno." |
| Family Sharing | Share with your family — up to 5 members (`paywall.premium.familySharing`) | Compártelo con tu familia — hasta 5 miembros | |
| Siri / Shortcuts | AppShortcuts phrases | see coverage section | |

### Paid tier names in the Spanish UI (AfterShift)
- Title: **AfterShift Premium** (`paywall.premiumTitle`, `pro.chipLabel` "Premium"); `paywall.continuePremium` "Continuar Premium"; `paywall.tryPremium` "Prueba AfterShift Premium"; `paywall.unlockForever` "Desbloquear Premium para siempre". The word "Pro" never appears in the Spanish UI (0 values), unlike the French catalog; the site term is Premium.
- Periods: Mensual / Anual / De por vida (`paywall.monthly/yearly/lifetime`); `paywall.month` mes, `paywall.year` año; `settings.lifetimeActive` "Premium de por vida"; `paywall.payOnce` "Pago único"; `paywall.lifetimeDisclosure` "Compra única. Sin suscripción. Todas las funciones Premium, para siempre." **Flag:** `paywall.bestValue` "Mejor valor" is a calque of "Best value" ("Mejor opción" is what AppMeta uses).
- Trial: `paywall.startTrial` "Comenzar prueba gratuita de 7 días"; `paywall.7dayTrial` "Prueba gratuita de 7 días"; `paywall.freeFor7Days` "gratis durante 7 días"; `paywall.noChargeToday` "No se cobrará hoy. No se te cobrará si cancelas antes de que termine la prueba."
- Restore: `paywall.restorePurchases` "Restaurar compras".

### Spanish App Store listing (checked 2026-11-19)
- Name: **AfterShift: Sueño y Turnos** (differs from English "AfterShift: Sleep & Shift Work"); colon is U+003A without a space before it, as in Spanish convention.
- Subtitle: **Recuperación, siestas y fatiga** (a direct translation of the English "Recovery, naps & fatigue").
- Category: **Salud y forma física** (English: Health & Fitness). Price: "Gratis" with "Compras dentro de la app". Compatible: iPhone (iOS 17.6+), Mac (macOS 14.6+, Apple silicon), Apple Vision (visionOS 1.3+); the lookup lists iPhone, iPad and others in `supportedDevices` (132 entries) but the page's platform tabs are iPhone / iPad / Mac / Watch.
- IAPs (page): `Premium compra única 44,99 €` · `Apoyar al desarrollador 1,00 €` · `Premium anual 29,99 €` · `Premium mensual 3,99 €` (US: AfterShift Premium Lifetime $39.99 / Support the Developer $1.00 / Premium Yearly $24.99 / Premium Monthly $3.99). Store IAP names are Premium (same word as the app).
- Idiomas: "Español y 33 más" (34 languages: Español, Alemán, Catalán, Checo, Chino simplificado, Chino tradicional, Coreano, Croata, Danés, Eslovaco, Esloveno, Finés, Francés, Griego, Hebreo, Hindi, Húngaro, Indonesio, Inglés, Italiano, Japonés, Malayo, Neerlandés, Noruego bokmål, Polaco, Portugués, Rumano, Ruso, Sueco, Tailandés, Turco, Ucraniano, Vietnamita, Árabe).
- Description (store, tú): "Tu día empieza cuando acaba tu turno." Uses "cuadrante" for the roster ("Tu cuadrante, ya relleno") and "Estado de preparación" for Readiness; in-app uses "Turnos" for Roster. Site should pick one and note the store's "cuadrante".

---

### 2. AllPaid (`allpaid`, source `billreminder/`, ID 6757253009)

### Spanish coverage
- Main `Localizable.xcstrings`: 494 / 494 → **100 %** (non-stale 464 / 464; 20 values identical to English: "Pro", "Streaming", brand names).
- `InfoPlist.xcstrings`: 3 / 3 → 100 % (display name "AllPaid"; `NSFaceIDUsageDescription` "Requiere Face ID o Touch ID para abrir la app.").
- Widget `billreminderWidget/Localizable.xcstrings`: 57 / 58 → 98.3 % (only `%lld` untranslated, format-only). `billreminderWidgetShared/Widget.xcstrings`: 130 / 130 → 100 %.
- **Not localized:** Siri App Shortcut phrases (`Services/AppIntents/BillsDueIntent.swift`: "What bills are due in \(.applicationName)", "Show my bills in \(.applicationName)", "Bills due this week in \(.applicationName)"): no `AppShortcuts.xcstrings`/`.strings` exists, so the spoken phrases are English only. The intent title ("Bills Due This Week" → "Facturas esta semana") and description are translated; the phrases are not. Do not promise Spanish Siri phrases on the page.
- **Verdict: app is in Spanish: yes** (Siri phrases English only).

### Glossary
| English term on site | English UI string (key) | Spanish UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Bills | Bills | Facturas | "factura" used throughout (72 values) |
| Add a bill | Add Bill | Añadir factura | "Añadir" (6 values); no "Agregar" in AllPaid |
| Mark paid | Mark as paid / Mark paid | Marcar como pagado / Marcar como pagada | **Flag:** masculine vs feminine for the same action (also "No se pudo marcar como pagada. Inténtalo de nuevo.") |
| Paid | Paid | Pagada | feminine; plural "pagadas"; `Mark as renewed` = "Marcar como renovado" (masc.) |
| Undo | Undo | Deshacer | distinct from Cancel = "Cancelar" (better than French) |
| Snooze (notification) | Remind in 2 hours / Remind tomorrow | Recordar en 2 horas / Recordar mañana | no single "Snooze" string |
| Monthly calendar | Monthly Calendar | Calendario mensual | |
| Total due | Total due | Total por vencer | |
| Upcoming | Upcoming / Coming Up | Próximas / Próximas facturas | |
| Reminders | Reminders | Recordatorios | |
| Multiple reminders per bill (Pro) | Multiple reminders per bill | Varios recordatorios por factura | other string: "Múltiples recordatorios — no pierdas ningún vencimiento" |
| Due-day reminder | Due-day reminders | Recordatorios el día del vencimiento | "vence hoy", "vence mañana", "vence en N días" (consistent, no English left) |
| Spending analytics (Pro) | Spending Analytics | Análisis de gastos | "Analytics" alone = "Análisis" |
| Category breakdown | By category | Por categoría | |
| Monthly trends | Monthly trend | Tendencia mensual | |
| Full payment history | Full payment history / Payment History | Historial completo de pagos / Historial de pagos | |
| Unlimited bills | Unlimited bills | Facturas ilimitadas | |
| iCloud Sync | iCloud Sync | Sincronización con iCloud | |
| Search / Sort / Notes / Share | Search bills / Sort by / Notes / Share bill | Buscar facturas / Ordenar por / Notas / Compartir factura | |
| Billing cycles | Weekly / Bi-weekly / Quarterly / Semi-annual / Custom | Semanal / Quincenal / Trimestral / Semestral / Personalizado | "Quincenal" (Bi-weekly) in Spain means roughly every 15 days; fine for "every two weeks" but note |
| Categories (examples) | Streaming / Subscriptions / Utilities / Housing / Insurance | Streaming / Suscripciones / Suministros / Vivienda / Seguros | "Suministros" for Utilities is correct Spain wording |
| Contracts | Contract / Contracts / Contract ends | Contrato / Contratos / Fin del contrato | `Contract ending soon` = "Contrato por terminar"; `%@ contract ends in %lld days.` plural = "El contrato de %1$@ termina en %2$lld día." |
| Auto-pay | Auto-pay | Pago automático | |
| Documents attached to the bill | Attachment… / DataVault | adjuntos / DataVault | `Manage attachments` = "Gestionar adjuntos"; `DataVault` left as product name |
| App lock (Face ID) | App Lock | Bloqueo de app | |
| Family Sharing | Share with up to 5 family members | Compártelo con hasta 5 miembros de la familia | |
| Widgets: Next Bill, Horizon, Paid Rhythm (+ Recurring Bills, Week Ahead, Month Progress, Monthly Calendar) | widget names | Próxima factura, Horizonte, Ritmo de pagos (+ Facturas recurrentes, Semana a la vista, Progreso del mes, Calendario mensual) | |
| Free tier | Free plan | Plan gratuito | `Free plan allows up to 3 bills…` = "El plan gratuito permite hasta 3 facturas. Actualiza a Pro para facturas ilimitadas."; `Free: 1` = "Gratis: 1" (contract reminders, not bills) |
| Pro | Pro / AllPaid Pro / Upgrade to Pro | Pro / AllPaid Pro / Actualizar a Pro | `Unlock AllPaid Pro` = "Desbloquear AllPaid Pro"; `Start Pro` = "Activar Pro" |
| Lifetime | Lifetime / Buy Lifetime Access | De por vida / Comprar acceso de por vida | store IAP says "compra única" |
| 7-day free trial | Try Pro free for 7 days | Prueba Pro gratis durante 7 días | `Start free trial` = "Iniciar prueba gratuita"; `Try Pro free for %@` = "Prueba Pro gratis durante %@" |
| Restore Purchases | Restore Purchases | Restaurar compras | |

### Paid tier names in the Spanish UI (AllPaid)
Pro (`Pro`, `AllPaid Pro`); Mensual / Anual / De por vida (`Lifetime`); `Upgrade to Pro` = "Actualizar a Pro"; `Unlock` = "Desbloquear" and `Unlock AllPaid` = "Desbloquear AllPaid" (one verb, unlike French); trial "Prueba Pro gratis durante 7 días"; "Cancela cuando quieras" / "Cancela en cualquier momento. Sin cargos hasta que termine la prueba."; purchase pending "Compra pendiente de aprobación. Tendrás acceso una vez aprobada."; lifetime disclosure "El pago se cargará a tu ID de Apple como compra única. Sin suscripción, sin cargos recurrentes."; restore "Restaurar compras".

### Spanish App Store listing (checked 2026-11-19)
- Name: **AllPaid – Gestión de Facturas** (en dash, differs from English "AllPaid – Bill Tracker"; the French store name was "Suivi de factures").
- Subtitle: **Paga a tiempo, sin estrés** (differs from English "Pay on time, stress-free"); tú imperative.
- Category: **Utilidades** (primary; secondary shown by the lookup: "Comida y bebida"). Price "Gratis" with "Compras dentro de la app". Compatible: iPhone (iOS 17.0+), iPad (iPadOS 17.0+), Mac (macOS 14.0+), Apple Vision (visionOS 1.0+); the store text says "AHORA EN IPHONE, IPAD Y MAC". (The French sheet recorded "iPhone only"; the store has moved on.)
- IAPs: `AllPaid Pro compra única 29,99 €` · `AllPaid Pro anual 14,99 €` · `AllPaid Pro mensual 1,99 €` (US: AllPaid Pro Lifetime $24.99 / Yearly $12.99 / Monthly $1.99).
- Idiomas: "Español y 33 más" (same 34-language list as AfterShift).
- Description (store, tú): "No vuelvas a olvidar ninguna factura." The description says "Añade una factura" and "móvil" ("el móvil que llevas en el bolsillo") while the UI says "app" and "factura".

---

### 3. AppMeta (`appmeta`, source `metabuilder/`, ID 6758547802, macOS)

### Spanish coverage
- `metabuilder/Localizable.xcstrings`: 2282 / 2300 translatable keys → **99.2 %** (non-stale 2247 / 2265, also 99.2 %). The 18 keys without `es` are all format-only or symbol strings (` "%@"`, `(%lld %@)`, `%`, `%@ — %@`, `%@ — %@ (%@)`, `%@ %@ %@`, `%lld %@`, `$`, `$0`, `0%`, `1D`, `7D`, `30D`, `60D`, `90D`, `P50`, `P95`, `s`). 72 values identical to English (product names, "Pro", "TestFlight", "Issuer ID", "Key ID").
- No InfoPlist.xcstrings, no widgets, no extensions, no permission prompts; display name "AppMeta" is a brand name.
- **Verdict: app is in Spanish: yes** (only format-only keys lack Spanish).

### Glossary
| English term on site | English UI string | Spanish UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Locales | Locales | Idiomas | lowercase `locales` = "idiomas" ("idioma" 118 values); consistent |
| Metadata | Metadata | Metadatos | lowercase form "los metadatos" |
| Name / Subtitle / Promotional Text / Description / What's New | same | Nombre / Subtítulo / Texto promocional / Descripción / Novedades | |
| Keywords | Keywords | Palabras clave | consistent |
| Keyword Optimizer | Keyword Optimizer | Optimizador de palabras clave | also "Keyword Opportunities" = "Oportunidades de palabras clave", "Keyword Efficiency Dashboard" = "Panel de eficiencia de palabras clave" |
| Difficulty / Demand / Opportunity | same | Dificultad / Demanda / Oportunidad | |
| Search coverage | App Store Search Coverage / Coverage | Cobertura de búsqueda en la App Store / Cobertura | |
| Preview changes (diff) | Preview Changes | Previsualizar cambios | `Diff previews and sync simulation` = "Vista previa de diferencias y simulación de sincronización"; `Diff-first safety` = "Seguridad: primero las diferencias"; the store text keeps "diff" ("hasta que hayas visto el diff") |
| Push | Push / Push All / Push Changes | Publicar / Publicar todo / Publicar cambios | ("Publicar" 33 values vs "Enviar" 21: `Submit` = "Enviar"); the store text says "envío" ("PRIMERO EL DIFF, LUEGO EL ENVÍO") |
| Refresh | Refresh | Actualizar | |
| Bulk actions | Bulk Actions / Bulk Copy | Acciones masivas / Copia masiva | |
| AI translation | AI Translation / Translate | Traducción con IA / Traducir | |
| AI provider | Provider / Default Provider | Proveedor / Proveedor predeterminado | `Use your own API key` = "Usa tu propia clave de API" |
| AI credits | AI Credits / Buy Credits / Starter Pack / Pro Pack | Créditos de IA / Comprar créditos / Paquete Starter / Paquete Pro | `AppMeta AI Credits` = "Créditos de AppMeta AI" |
| Apple Intelligence | Apple Intelligence | Apple Intelligence | |
| Submit for review | Submit for Review | Enviar a revisión | |
| App Review Information | App Review Information | Información de revisión de la App Store | |
| Phased release / Age rating / Availability / Pricing | same | Lanzamiento por fases / Clasificación por edad / Disponibilidad / Precios | `Release to All` = "Lanzar a todos" |
| Reviews / Ratings | Reviews / Ratings / Rating | Reseñas / Valoraciones / Valoración | clean distinction (French merged Reviews and Ratings) |
| TestFlight / What to Test | same | TestFlight / Qué probar | |
| In-App Purchases / Subscription Groups | same | Compras dentro de la app / Grupos de suscripciones | "Compras dentro de la app" 12 values, never "compras integradas" |
| Game Center Achievements / Leaderboards | Achievements / Leaderboards | Logros / Clasificaciones | lowercase "clasificaciones" also appears; `Game Center` has no standalone key |
| Sales and Analytics | Sales / Analytics | Ventas / Analíticas | **Flag:** "Analíticas" (3) vs "Analítica" (6) vs "Análisis" (2) for Analytics; `Sales & Trends` = "Ventas y Tendencias" (capital T in 2 values) vs "Ventas y tendencias" (1) vs untranslated "Haz clic en Sales and Trends" (`Click Sales and Trends`) |
| Diagnostics | Diagnostics | Diagnósticos | |
| Screenshots | Screenshots | Capturas | "Capturas de pantalla" in 1 value, "Capturas" in 3 |
| Issuer ID / Key ID | same | Issuer ID / Key ID | both left English (French translated Key ID); `Different from the Issuer ID` = "Distinto del Issuer ID."; but one string uses "ID de emisor" ("Este parece un ID de emisor de App Store Connect") |
| Territories | Territories | Territorios | |
| Dashboard | Dashboard | Panel | "Panel de eficiencia…" |
| Demo mode | Demo Mode | Modo de demostración | `Demo (Free)` = "Demo (gratis)"; `Explore Demo Mode` = "Explorar el Modo de demostración"; capitalised "Modo" in the middle of a sentence |
| Pro | Pro / AppMeta Pro / Unlock Pro | Pro / AppMeta Pro / Desbloquear Pro | `Upgrade to Pro` = "Hazte Pro"; `Unlock AppMeta Pro` = "Desbloquear AppMeta Pro" |
| Yearly / Lifetime | Yearly / Lifetime | Anual / De por vida | `Auto-renews yearly` = "Se renueva cada año"; `Most popular` = "Más popular"; `Best Value` = "Mejor opción"; `Pays off after ~%lld years` = "Se amortiza en ~%lld años"; `Unlock Lifetime` = "Comprar de por vida: %@" |
| Restore Purchases | Restore Purchases | Restaurar compras | `Manage Subscription` = "Gestionar suscripción" |
| Add | add | Añadir ("Añad" 25 values; 0 "Agregar") | consistent Spain form |

### Paid tier names in the Spanish UI (AppMeta)
**AppMeta Pro** (`Pro`, `AppMeta Pro`); periods "Anual" (`Yearly`) and "De por vida" (`Lifetime`); no monthly plan; no free trial in the app (the `Free Trial` string is an analytics label = "Prueba gratuita"). Paywall verbs: "Desbloquear AppMeta Pro", "Hazte Pro", "Comprar de por vida: %@". Demo mode is free: "Demo (gratis)". `Pay once, own forever` = "Paga una vez, tuyo para siempre".

### Spanish App Store listing (checked 2026-11-19)
- Name: **AppMeta for App Store Connect** (identical to English, not translated).
- Subtitle: **ASO, metadatos y reseñas** (differs from English "Metadata & ASO Tools").
- Category: **Utilidades** (English: Utilities). Mac only (macOS 14.0+); lookup `kind` = `mac-software`.
- IAPs: `AppMeta Yearly 19,99 €` · `AppMeta Compra única 34,99 €` (flag: "Yearly" display name not localized in the Spanish store; "Compra única" has a capital C). US: AppMeta Lifetime $29.99 / AppMeta Yearly $17.99.
- Idiomas: "Español y 10 más" (Español, Alemán, Coreano, Francés, Inglés, Italiano, Japonés, Portugués, Ruso, Turco, Árabe). Fewer languages than the iPhone apps.
- Description (store, tú): "Un pegado erróneo puede publicar un campo de palabras clave roto en un idioma que no sabes leer."

---

### 4. AppMeta Pulse (`appmeta-pulse`, source `metabuilder_phone/`, ID 6758788164)

### Spanish coverage
- Main `metabuilder_phone/Localizable.xcstrings`: 1418 / 1418 → **100 %** (non-stale 1415 / 1415; 34 values identical to English).
- `AppShortcuts.xcstrings` (Siri phrases): 3 / 3 keys carry a translated stringSet in `es`: "Abre ${applicationName} | Muestra los ingresos de hoy en ${applicationName} | Ventas de hoy en ${applicationName}"; "Muestra el análisis en ${applicationName} | Conversión de App Store en ${applicationName}"; "Muestra los suscriptores en ${applicationName} | Suscripciones activas en ${applicationName}". Siri phrases ARE in Spanish.
- Widget `AppMetaPulseWidget/Localizable.xcstrings`: 256 / 256 → **100 %**.
- No InfoPlist.xcstrings; display names "AppMeta Pulse" / "AppMeta Pulse Widget" are brand names; no permission prompts.
- **Verdict: app is in Spanish: yes.**

### Glossary
| English term on site | English UI string | Spanish UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Dashboard | Dashboard | Panel | `7-Day Dashboard` = "Panel de 7 días"; `Start` = "Inicio" is the date-range picker label, not a tab; the first tab is `Dashboard` = "Panel" (corrected 2026-11-19, privacy review) |
| Apps | Apps | Apps | |
| Analytics | Analytics | Análisis | AppMeta uses "Analíticas"/"Analítica", see Cross-app |
| Reviews | Reviews | Reseñas | `Reply` = "Respuesta"; `Reply to this review` = "Responder a esta reseña" |
| Settings | Settings | Ajustes | |
| Proceeds | Proceeds | Ingresos | **Flag:** `Revenue` = "Ingresos" too, so Proceeds and Revenue collide; the explanatory strings tell them apart ("Lo que ganas tras la comisión de Apple" = proceeds; "Lo que pagaron los clientes" = customer price; `Gross` = "Importe bruto que pagan los clientes"; `Net` = "Neto") |
| Sales | Sales | Ventas | |
| Units | Units | Unidades | widget short form "UNID." |
| Revenue | Revenue | Ingresos | see Proceeds |
| MRR | MRR | MRR | |
| Active subscriptions | Active Subscriptions / Active Subs | Suscripciones activas / Susc. activas | `Subscription Status` = "Estado de las suscripciones" |
| Trials | Trials / Active Trials | Pruebas / Pruebas activas | |
| Trial-to-paid conversion | Trial → Paid / Conversion | Prueba → pago / Conversión | |
| Churn | Monthly Churn / Churn /mo | Bajas mensuales / Bajas/mes | also "Tasa mensual de bajas" |
| Cancellations | Cancels / Cancelled | Cancelac. / Canceladas | |
| New subscriptions | New Subs | Susc. nuevas / Nuevas suscr. | long form "Suscripciones nuevas" |
| Downloads / Impressions / Product page views | Downloads / Impressions / Product Page Views | Descargas / Impresiones / Vistas de página | `Page views` short form; "vistas de la página del producto" in long chart text |
| Top territories | Top Territories | Principales países y regiones | |
| Trend comparison | Compare / Previous period / Last year / Custom Range | Comparar / Periodo anterior / Año anterior / Intervalo personalizado | |
| Goals | Goals / Monthly Goal | Objetivos / Objetivo mensual | |
| iCloud sync | iCloud Sync | Sincronización con iCloud | same wording as AllPaid |
| AI review reply drafts | Draft suggestions / AI draft per review | Borradores sugeridos / Borrador de IA por reseña | "Borradores de respuesta con IA, escritos en tu dispositivo por Apple Intelligence." |
| Reply templates | Templates | Plantillas | `Reply Templates` = "Plantillas de respuesta" in Ajustes → Objetivos |
| Display currency | Convert to your preferred currency | Convierte los importes a tu moneda preferida | `Currency` = "Moneda" |
| Funnel | Funnel | Embudo | |
| Demo mode | Try with sample data | Probar con datos de ejemplo | `Demo Mode` = "Modo demo" (not "Modo de demostración" as AppMeta says) |
| Widgets | Home Screen widgets | Widgets en la pantalla de inicio | |
| AI assistant (MCP) | Ask your AI assistant | Pregunta a tu asistente de IA | "Un servidor MCP para Claude, Cursor y otras apps de IA" |
| Year over year | Year-over-year | Comparación interanual | |
| Paywall bullets | Full access to revenue & subscription metrics / Per-app performance breakdowns / Trends and historical insights / All future updates included | Acceso completo a las métricas de ingresos y suscripciones / Desglose del rendimiento por app / Tendencias e información histórica / Todas las actualizaciones futuras incluidas | |
| Pro (site plan name) | no UI string | n/a | the app never says "Pro" in its paywall; gating is "Desbloquea AppMeta Pulse" |
| Monthly / Yearly / Lifetime | Monthly / Yearly / Lifetime | Mensual / Anual / De por vida | `One-time purchase · Use forever` = "Compra única · Úsala para siempre"; `Best Value` = "Mejor oferta"; `Billed monthly` = "Facturación mensual" |
| Free trial | Start Free Trial | Empezar prueba gratuita | `Billed yearly · Free trial included` = "Facturación anual · Prueba gratuita incluida" |
| Restore Purchases | Restore Purchase / Restore Purchases | Restaurar compra / Restaurar compras | **Flag:** paywall says "Restaurar compra" (singular, mirrors English) vs Ajustes "Restaurar compras" |

### Paid tier names in the Spanish UI (Pulse)
No tier name: the whole app is gated. Strings: "Desbloquea AppMeta Pulse" (23 values), "Desbloquear acceso de por vida" (`Unlock Lifetime Access`), `Subscribe` = "Suscribirse"; periods Mensual / Anual / De por vida; trial "Empezar prueba gratuita"; restore "Restaurar compra" (paywall) and "Restaurar compras" (settings). The store IAP names use "Acceso vitalicio / anual / mensual" while the app says "De por vida".

### Spanish App Store listing (checked 2026-11-19)
- Name: **AppMeta Pulse: Ventas de apps** (differs from English "AppMeta Pulse: App Sales & MRR").
- Subtitle: **Ingresos y reseñas con IA** (differs from English "Revenue & AI Review Replies").
- Category: **Economía y empresa** (English: Business). Compatible: iPhone (iOS 17.0+), Mac (macOS 14.0+), Apple Vision; the description says "ahora también en el Mac" ("NOVEDAD: PULSE PARA MAC").
- IAPs: `AppMeta Pulse Acceso vitalicio 14,99 €` · `AppMeta Pulse Acceso anual 6,99 €` · `AppMeta Pulse Acceso mensual 0,99 €` (US: Access Lifetime $12.99 / Yearly $5.99 / Monthly $0.99). Prices differ from the French sheet (2026-11-07) so reference prices change; always use the master file.
- Idiomas: "Español y 14 más" (Español, Alemán, Chino simplificado, Chino tradicional, Coreano, Francés, Inglés, Italiano, Japonés, Neerlandés, Portugués, Ruso, Sueco, Turco, Ucraniano).
- Description (store, tú): "Tus ventas en el App Store, el MRR y las reseñas en el iPhone, y ahora también en el Mac."

---

### 5. Chessful (`chessful`, source `Chessful/`, ID 6761336870)

### Spanish coverage
- `Localizable.xcstrings`: 2146 / 2146 → **100 %** (non-stale 2113 / 2113; 74 values identical to English: "Stockfish", "Expert", notation).
- `Lessons.xcstrings`: 3649 / 3649 → 100 % (14 identical).
- `InfoPlist.xcstrings`: 2 / 2 → 100 % (`CFBundleDisplayName`/`CFBundleName` "Chessful", no permission prompts).
- No widget, watch, App Intents or AppShortcuts catalogs.
- **Verdict: app is in Spanish: yes.**

### Glossary
| English term on site | English UI string | Spanish UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Dashboard (tab) | Dashboard | Inicio | not "Panel" (AppMeta/Pulse use "Panel") |
| Play (tab) | Play | Jugar | |
| Analysis (tab) | Analysis | Análisis | |
| Training (tab) | Training | Entrenamiento | |
| Learn (tab) | Learn | Aprender | |
| Progress | Progress | Progreso | |
| Game review | Game Review | Revisión | `Review Game` = "Revisar partida"; `Game Analysis…` = "Análisis de la partida…"; `Analyze Game` = "Analizar partida" |
| Accuracy | Accuracy | Precisión | |
| Key moments | Key Moments | Momentos clave | |
| Blunder / Mistake / Inaccuracy | same | Pifia / Error / Imprecisión | **Flag:** "Pifia" for Blunder (colloquial, not the usual chess term; "error grave" is 0 values); `Mistake Detail` = "Detalle"; `Mistake Hunter` = "Cazador de errores" |
| Better move | See the better move / Best move | Ver la mejor jugada / Mejor jugada | "jugada" (160 + 275 in lessons) vs "movimiento" (67 + 3): mixed but "jugada" dominant |
| Today's training | Today's Training | Entrenamiento de hoy | |
| Train your weaknesses | Train Your Weaknesses | Entrena tus debilidades | tú; `Train Your Weaknesses Daily` = "Entrena tus debilidades a diario" |
| Skills (5 dimensions) | Skills | Habilidades | |
| Tactics / Defense / Positional / Openings / Endgames | same | Táctica / Defensa / Posicional / Aperturas / Finales | |
| Opening repertoire | Opening Repertoire | Repertorio de aperturas | |
| 40 AI opponents | 40 Unique Opponents | 40 oponentes únicos | levels Beginner / Intermediate / Advanced / Master = Principiante / Intermedio / Avanzado / Maestro; "rival" also used in text ("Tu rival solo puede salvar una") |
| Import games | Import Games / Import from PGN | Importar partidas / Importar desde PGN | `Analyze All` = "Analizar todo" |
| Weekly comparison / Weakness trends | same | Comparación semanal / Tendencias de debilidades | |
| Rating / Elo | Rating | Rating | **Flag:** left in English ("Rating", "Rating de problemas", "Tu rating") but `Rating Over Time` = "Valoración en el tiempo"; Elo shown as "%lld ELO" (all caps) while the store subtitle says "Elo" |
| Achievements | Achievements | Logros | |
| 3D board | 3D Board / Board style | Tablero 3D / Estilo del tablero | `Classic 2D` = "Clásico 2D" |
| Puzzles | puzzle(s) | Puzzles / problemas | **Flag:** "Puzzles de tus errores reales" (14 values with "puzzle") vs "Problema %@ · Tu rating", "Rating de problemas", "temas de problemas" (21 values); Lessons use "problema" only (21) |
| Back-rank | Back-Rank Weakness | Mate de última fila no visto | **Flag:** "mate de última fila" (27 + 78 values) vs "Mate del pasillo" (2 + 10) vs "Defensa desde la primera fila"; the store text uses «Mate de última fila no visto» |
| Fork | A fork | Un tenedor / La horquilla | **Flag:** two words for the same tactic: "Un tenedor: … ataca …" and "La horquilla ataca dos piezas" |
| Free | Free Plan | Plan gratuito | |
| Pro (site) | Chessful Premium / Upgrade to Premium | app: Premium ("Chessful Premium", "Actualizar a Premium"); store: **Pro** ("Chessful Pro anual") | owner decision 2026-11-08: the site says **Pro**; the app UI still says Premium (8 values; "Forzar Pro (depuración)" is a debug string) until the app fix (Kanban) |
| Monthly / Yearly / Lifetime | same | Mensual / Anual / De por vida | `Purchase Lifetime` = "Comprar de por vida" |
| Free trial | Start Free Trial | Prueba gratuita | `%@ free trial` = "%@ de prueba gratis"; stale 3-day strings ("Prueba gratuita de 3 días, luego se renueva automáticamente", "3,33 $/mes · 3 días de prueba") remain in the catalog but are unused; the trial is 1 week (master), so the site uses the {TRIAL} token |
| Restore Purchases | Restore Purchases | Restaurar compras | `Already subscribed? Restore Purchases` = "¿Ya tienes suscripción? Restaurar compras" |
| Hint / Resign / New game | Hint / Resign / New Game | Pista / Rendirse / Nueva partida | |
| Stockfish | Stockfish | Stockfish | "Analizar con Stockfish", "Stockfish (profundidad 12)" |

### Paid tier names in the Spanish UI (Chessful)
App: **Premium** ("Chessful Premium", "Actualizar a Premium", "Premium. Abre la pantalla de mejora."); periods Mensual / Anual / De por vida; "Prueba gratuita" (trial length via StoreKit at runtime). Store IAP names: **Chessful Pro mensual / anual / compra única** plus tips "Invitar a un café" / "Apoyo" / "Gran apoyo". Owner decision 2026-11-08: the paid tier is **Pro** on the site.

### Spanish App Store listing (checked 2026-11-19)
- Name: **Chessful: Entrena y Analiza** (differs from English "Chessful: Train & Analyze"). **Flag:** "Entrena" is a tú imperative and "Analiza" is capitalised mid-title; colon is U+003A.
- Subtitle: **Ajedrez, táctica, puzzles, Elo** (differs from English "Chess tactics, puzzles, coach").
- Category: **Juegos de mesa** (lookup genres "Juegos", "Juegos de mesa"; English: Board). Price "Gratis" with "Compras dentro de la app". Compatible: iPhone (iOS 18.0+), iPad (iPadOS 18.0+), Mac (macOS 15.0+, Apple silicon), Apple Vision (visionOS 2.0+).
- IAPs: `Chessful Pro anual 17,99 €` · `Chessful Pro mensual 2,99 €` · `Gran apoyo 9,99 €` · `Apoyo 5,99 €` · `Invitar a un café 1,99 €` · `Chessful Pro compra única 29,99 €` (US: Chessful Pro Monthly/Yearly/Lifetime, Support the Developer Huge Support $9.99 / Supporter $4.99 / Coffee $1.99; the Spanish store's "Apoyo" is $4.99 in US, shown 5,99 € here).
- Idiomas: "Español y 32 más" (Español, Alemán, Catalán, Checo, Chino simplificado, Chino tradicional, Coreano, Croata, Danés, Eslovaco, Finés, Francés, Griego, Hebreo, Hindi, Húngaro, Indonesio, Inglés, Italiano, Japonés, Malayo, Neerlandés, Noruego bokmål, Polaco, Portugués, Rumano, Ruso, Sueco, Tailandés, Turco, Ucraniano, Vietnamita, Árabe; no Esloveno).
- Description (store, tú): "Has perdido la partida y no sabes qué jugada lo decidió. Chessful sí." and «Mate de última fila no visto».

---

### Cross-app terms (this batch)
| Concept | Values seen | Recommendation |
|---|---|---|
| Restore Purchases | Restaurar compras (AfterShift, AllPaid, AppMeta, Chessful, Pulse settings); Pulse paywall "Restaurar compra" | consistent except Pulse paywall |
| Lifetime | De por vida (all five); store IAPs: "compra única" (AfterShift, AllPaid, AppMeta, Chessful), "Acceso vitalicio" (Pulse) | consistent in app; store differs |
| Monthly / Yearly | Mensual / Anual (all) | consistent |
| Unlock | Desbloquear (all five) | consistent (French mixed two verbs) |
| Free trial | Prueba gratuita (all); AllPaid "Prueba Pro gratis durante 7 días"; Chessful "%@ de prueba gratis" | consistent |
| Reviews | Reseñas (AppMeta, Pulse) | consistent |
| Ratings | Valoraciones (AppMeta); Chessful keeps "Rating" | note |
| Analytics | Análisis (Pulse, AllPaid "Análisis de gastos", Chessful tab); Analíticas/Analítica (AppMeta, mixed with "Análisis") | choose per app |
| Dashboard | Panel (AppMeta, Pulse); Inicio (Chessful tab) | choose per app |
| iCloud Sync | Sincronización con iCloud (AllPaid, Pulse) | consistent |
| Free tier | Plan gratuito (AllPaid, Chessful) | consistent |
| Add | Añadir (AllPaid, AppMeta, Pulse "Añade"); Agregar (AfterShift) | Spain form is "añadir"; flag AfterShift |
| Report | reporte (AfterShift) vs informe (AfterShift, Pulse "informes de App Store Connect") | Spain form is "informe" |
| In-app purchases | Compras dentro de la app (AppMeta, store listings) | consistent |
| Settings | Ajustes (all five) | consistent |
| Apple ID | "Apple ID" (AllPaid 1 value, AfterShift) vs "ID de Apple" (AllPaid 3 values) | pick "Apple ID" for the site (Spain Apple uses "ID de Apple" in iOS; keep and note) |
| Phone | teléfono / móvil (AfterShift, AllPaid store text); "dispositivo" in Pulse | Spain-compatible; no "celular" anywhere |
| Formality | tú in all five (no usted, no vos) | site writes tú; no register mix between apps |

### Flags
1. **AfterShift uses Latin-American vocabulary inside the `es` locale**: "Agregar" 20 values vs "Añadir" 12 (`roster.addShift`, `today.addShift`, `shift.addTitle`, `addShifts.*`, "Premium agrega…"), and "reporte" 7 vs "informe" 3 (`settings.exportReport`, `premium.export.title`, `export.disclaimer`). Spain Spanish: "añadir", "informe". App-side string fix (not on Kanban here; add to ISSUES.md if the owner agrees).
2. **AfterShift has three Spanish forms for the same concepts**: caffeine timing ("Tiempo de la cafeína", "Timing de la cafeína", "Consumo de cafeína", "Excelente horario de cafeína"), readiness ("Estado de preparación", "Nivel de recuperación", "Recuperación bloqueada", "La preparación"), wind-down ("Relajación", "Hora de relajarse", "Desacelera"). The site must pick one (suggest "Estado de preparación", "Límite de cafeína", "Relajación") and the store text says "cuadrante" for the roster where the app says "Turnos".
3. **AppMeta Pulse: Proceeds and Revenue are both "Ingresos"** (`Proceeds`, `Revenue`, widget "INGRESOS"); the paywall says "Restaurar compra" while Ajustes says "Restaurar compras"; "Panel" is the Dashboard but the first tab key `Start` = "Inicio"; demo mode is "Modo demo" here and "Modo de demostración" in AppMeta.
4. **Chessful term mixes**: "Rating" left English (and "ELO" vs "Elo"), "Pifia" for Blunder, "Un tenedor" vs "La horquilla" for fork, "mate de última fila" vs "mate del pasillo", "puzzles" vs "problemas"; the app still says Premium while the store and the site say Pro (Kanban item). Stale 3-day trial strings remain in the catalog. Store name "Chessful: Entrena y Analiza" uses a tú imperative.
5. **Missing Spanish**: AllPaid Siri phrases are English-only (no AppShortcuts localization; `BillsDueIntent.swift`), AfterShift's calendar permission prompts (`NSCalendarsUsageDescription`, `NSCalendarsFullAccessUsageDescription`) are English-only build settings, AppMeta has 18 untranslated format-only keys (no user impact), AllPaid widget has 1 (`%lld`).
6. **AppMeta left words in English**: `Issuer ID` / `Key ID` (but "ID de emisor" in one string), `Click Sales and Trends` → "Haz clic en Sales and Trends" (English product label) while the other strings translate it to "Ventas y Tendencias"; "Analíticas/Analítica/Análisis" are mixed for Analytics; store IAP name "AppMeta Yearly" is not localized (English "Yearly" in the Spanish store).
7. **Capitalisation/format oddities**: AppMeta store IAP "AppMeta Compra única" (capital C); `Reseñas`/`Valoraciones` are fine, but the AppMeta Pulse store IAPs say "Acceso vitalicio" whereas the app says "De por vida"; AfterShift "Mejor valor" and AllPaid "Marcar como pagado" vs "Marcar como pagada" (gender mismatch); AfterShift "Premium agrega análisis…" is LatAm-leaning ("añade").
8. **Store listings differ from the French sheet** (apps changed since 2026-11-07): AllPaid is now iPhone + iPad + Mac + Vision (French sheet said iPhone only), Pulse IAP prices changed (14,99 / 6,99 / 0,99 €), Pulse now lists Mac; the Spanish subtitles are real translations of the English ones except AppMeta Pulse ("Ingresos y reseñas con IA" vs "Revenue & AI Review Replies") and Chessful ("Ajedrez, táctica, puzzles, Elo" vs "Chess tactics, puzzles, coach"). Prices must still come from `MASTER-prices.csv`.


---

## Spanish glossary, batch 2: earnlock, gymlogger-x, liftlog, mediakit, millrace

Method (checked 2026-11-19, nothing modified outside this file): coverage was counted with `python3 -I` over each app's `.xcstrings` catalogs (`strings` → key → `localizations.es` → `stringUnit` / `variations` / `stringSet`, keys with `shouldTranslate: false` and blank keys excluded; a key counts as translated when every unit is in state `translated`). Worktrees, `.build`, DerivedData and Pods were ignored. For GymLogger X the app has no `.xcstrings`; its JSON files `GymLogger/GymLogger/Localizations/es.json`, `GymLoggerWidget/Localizations/es.json` and `GymLoggerWatch Watch App/Localizations/es.json` were compared key by key with their `en.json`, and `GymLogger/es.lproj/InfoPlist.strings` was read for the permission prompts. Locale code: `es` (Spain Spanish) for EarnLock, GymLogger X, LiftLog and MediaKit; **Millrace uses `es-ES`, not `es`** (333 of 333 translated; it also ships a separate `es-MX`), and that `es-ES` column is what is quoted below. `es-MX` / `es-419` were ignored. Spanish UI strings are copied verbatim from the catalogs (plural variations shown as `one:` / `other:`), keeping each catalog's own apostrophes, guillemets and capitalization. Register counts are rough regex counts of strings with tú markers (tu, tus, te, ti, contigo, tuteo verb forms such as toca, elige, selecciona, añade) versus usted markers (usted, ustedes, seleccione, ingrese and similar subjunctive imperatives); hits were checked by hand and the usted figures below are the real ones, not the regex hits (the regex also catches nouns like "Doble toque" and "Ajuste"). Latin-American vocabulary and vosotros forms were searched for as well. App Store data: iTunes lookup API (`country=es&lang=es_es` against `country=us&lang=en_us`) plus the raw `serialized-server-data` JSON of `https://apps.apple.com/es/app/id<ID>` and `/us/app/id<ID>` (Safari User-Agent, `Accept-Language: es-ES`); five of the pages answered 429 at first and were retried after 25 s pauses until 200, so every subtitle and in-app purchase name below is verified. The seller block of the store page was not copied. Prices are reference only (the store prints `22,99 €` with U+00A0 before the euro sign; `formattedPrice` for the free download is `Gratis`). The French glossary `_i18n/fr-glossary.md` (batch 2) was the row checklist; the master file was not consulted (out of scope).

Headline flags for the whole batch:
- **All five apps write tú (tuteo), none writes vosotros or "vos", and none uses usted** except two GymLogger X validation messages (`Por favor, ingrese un nombre de ejercicio`, `Por favor, seleccione al menos un músculo`). The site can write tú and quote the UI without a register clash. This is cleaner than French (every app mixed tu/vous there).
- **GymLogger X: 99 of the 195 `creator_*` strings (the whole Program Creator) have no accents, no ñ and no opening ¿ ¡** (`Rehabilitacion`, `Duracion de la Sesion`, `Menos de 1 ano`, `A que equipamiento tienes acceso?`, `Perfecto!`). App-side bug; don't copy those values. The same screens also use Latin-American `Jalon` and `Agregar`.
- **LiftLog's paid-tier label `Bien` in the app differs from the store IAP name `Bueno`** (the other three match: `Justo`, `Generoso`, `Mecenas`). The tier names need one decision for the site.
- **LiftLog has 8 user-visible English fallbacks** in the main app (`Average`, `Best`, `Best run`, `By month`, `By weekday`, `min`, `Sessions in run`, `Weekly avg`; the widget catalog does have Spanish for them) and its Siri hint tells Spanish users to say English phrases.
- **Millrace's undo noun is the bare verb `deshacer`** in every plural (`10 deshacer`, `50 deshacer`, the store IAPs `50 deshacer`, `200 deshacer`), and its Spanish catalog lives under `es-ES` while the other four use `es`.
- All five App Store names differ from the English ones, and EarnLock, GymLogger X, LiftLog and Millrace subtitles differ too (MediaKit's differs only in the accent and the ampersand).

---

### 1. EarnLock (earnlock, source `EarnScreen`, ID 6771099230, has an Apple Watch app)

#### Spanish coverage

| Catalog | Keys | `es` present | `es` translated | % |
|---|---|---|---|---|
| EarnScreen/EarnScreen/Localizable.xcstrings (main app) | 620 | 620 | 620 | 100% |
| EarnScreen/EarnScreen/AppShortcuts.xcstrings | 9 | 9 | 9 | 100% |
| EarnScreen/EarnScreen/InfoPlist.xcstrings | 5 | 3 | 0 (all 3 `needs_review`) | 0% translated, 60% present |
| EarnScreenLiveActivity/Localizable.xcstrings (widgets + Live Activity) | 148 | 148 | 148 | 100% |
| EarnScreenShield/Localizable.xcstrings | 6 | 6 | 6 | 100% |
| EarnScreenWatchComplications/Localizable.xcstrings | 13 | 13 | 13 | 100% |
| watchkitapp Watch App/Localizable.xcstrings | 28 | 28 | 28 | 100% |
| watchkitapp Watch App/InfoPlist.xcstrings | 4 | 2 | 0 (both `needs_review`) | 0% translated, 50% present |
| EarnScreenDeviceActivity, EarnScreenShieldAction | 0 | n/a | n/a | empty catalogs |

All Localizable catalogs together: 815 keys, 815 translated (100%). Every catalog also carries an `es-MX` column.

English-only or unreviewed: the three permission prompts (HealthKit read, HealthKit write, Photo Library add) have Spanish text but are `needs_review`: `EarnLock lee tus pasos, minutos de actividad y energía activa de la app Salud para seguir tu progreso hacia el objetivo que desbloquea tus apps bloqueadas. Estos datos nunca salen de tu dispositivo.` / `EarnLock solo lee tus datos de actividad: no escribe nada en la app Salud. Apple exige este permiso porque el framework HealthKit técnicamente puede escribir datos.` / `Te permite guardar una tarjeta de hito en tu fototeca. EarnLock nunca lee tus fotos.` `CFBundleDisplayName` has no `es` entry (the name stays "EarnLock"). Siri / App Shortcuts phrases are Spanish and `translated` (e.g. `Cuál es mi objetivo en ${applicationName}`, `Iniciar una sesión de concentración en ${applicationName}`, `Bloquear mis apps en ${applicationName}`).

**Verdict: app is in Spanish: yes** (100% of every Localizable catalog, widgets, Live Activity, shield, Watch and Siri phrases; only the permission prompts are `needs_review`).

Register: tú. About 190 of 818 strings carry tú markers (`Te quedan %@ %@: vas por el %@ del camino hacia el desbloqueo.`, `Toca para pasar a Premium.`, `Concede acceso a Tiempo de uso para continuar.`), 0 real usted strings, no vosotros, no vos. Spanish-Spain markers present: `móvil` (once), `apps`, `Tiempo de uso`, `fototeca`, `Atajos`.

Wording flags:
- Screen Time is `Tiempo de uso` (Apple's Spain term, 13 strings), but 6 marketing strings say `tiempo de pantalla` (`Tiempo de pantalla ahorrado`, `Gana tiempo de pantalla cumpliendo objetivos diarios de actividad.`). The first is the shared product concept ("screen time saved"), so decide whether the site follows `Tiempo de uso` (the Apple feature) or `tiempo de pantalla` (the concept).
- Family Sharing: `En familia` (Apple's Spain name) but written `En Familia` in the sign-in string: `Inicia sesión en iCloud para activar En Familia y sincronizar las compras entre dispositivos.`
- Lock Screen widget title is `EarnLock — Pantalla bloqueada`; Apple's iOS term in Spain is "pantalla de bloqueo" (`Pantalla bloqueada` is a literal calque).
- Shadow Mode: `modo sombra` / `semana sombra` in most strings, but one error string leaves it in English: `No se ha podido seguir Shadow Mode`.
- Siri phrase `Qué tan cerca estoy de desbloquear en ${applicationName}` is a Latin-American construction (`Qué tan cerca`); Spain says `A qué distancia` or `Cuánto me falta` (the neighbouring phrase already uses `Cuánto me falta para desbloquear`).
- Capitalization: `Comprar De por vida` / `Premium · De por vida` (capital D in a mid-sentence label).
- Free-trial wording mixes `Empezar prueba gratis`, `7 días de prueba gratis, luego %@/año`, `Prueba gratuita de 7 días; luego, %@/mes` (the last one uses a semicolon where the yearly one uses a comma).

#### Glossary

| English term on site | English UI string (key) | Spanish UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Free (tier) | `Free forever for one app. Go further with Premium.`; `Free plan locks 1 app. Tap to upgrade.`; `Free locks one app. Premium has no limit.` | `Gratis para siempre con una app. Más allá con Premium.`; `El plan gratis bloquea 1 app. Toca para pasar a Premium.`; `El gratis bloquea una app. Premium sin límite.` | No standalone "Free" string. `plan gratis` is the app's term. |
| Premium | `Premium` | `Premium` | |
| Monthly | `Monthly` | `Mensual` | `Premium · Monthly` → `Premium · Mensual` |
| Yearly | `Yearly` | `Anual` | `Premium · Yearly` → `Premium · Anual` |
| Lifetime | `Lifetime` | `De por vida` | `Premium · Lifetime` → `Premium · De por vida`; `Get Lifetime` → `Comprar De por vida`; the store IAP is `compra única`. |
| Get Premium (button) | `Get Premium` | `Consigue Premium` | tú imperative. |
| Start free trial (button) | `Start free trial` | `Empezar prueba gratis` | |
| 7-day free trial | `7-day free trial, then %@/year`; `7-day free trial, then %@/month` | `7 días de prueba gratis, luego %@/año`; `Prueba gratuita de 7 días; luego, %@/mes` | Two different patterns for the same offer (see flags). |
| Restore Purchases | `Restore Purchases` | `Restaurar compras` | |
| Today tab (site says "Home screen") | `Today`; `Go to Today` | `Hoy`; `Ir a Hoy` | The tab is Today → `Hoy`. |
| Insights tab | `Insights` | `Análisis` | |
| Insights Day / Week / Month | `Day` / `Week` / `Month` | `Día` / `Semana` / `Mes` | |
| Settings tab | `Settings` | `Ajustes` | Apple's iOS term in Spain. |
| Shadow Week | `Run another Shadow Week`; `No Shadow Weeks yet`; `Compared with your previous Shadow Week.` | `Hacer otra semana sombra`; `Aún no hay semanas sombra`; `En comparación con tu semana sombra anterior.` | Feature name = **semana sombra** (lowercase); `Shadow Mode` → `modo sombra` (`Finaliza el modo sombra y aplica el bloqueo de inmediato`). One string keeps `Shadow Mode`. |
| Enable real blocking | `Enable real blocking` | `Activar bloqueo real` | |
| Reflect (button) | `Reflect` | `Reflexionar` | |
| Reflection (noun) | `Reflection summary`; `Reflections this month` | `Resumen de reflexiones`; `Reflexiones este mes` | |
| Reflection prompt | `What were you hoping to find?` | `¿Qué esperabas encontrar?` | tú (imperfect, no pronoun). |
| Reflection answers | `Boredom` / `Anxiety` / `FOMO` / `Habit` / `Other` | `Aburrimiento` / `Ansiedad` / `FOMO` / `Hábito` / `Otro` | |
| Smart Schedules | `Smart Schedules` / `Smart schedules` | `Horarios inteligentes` / `Horarios inteligentes` | Consistent. `Smart Schedules + custom app icons` → `Horarios inteligentes + iconos personalizados`. Section `Schedules` → `Horarios`. |
| Goal tiers Light / Standard / Challenge | `Light` / `Standard` / `Challenge` | `Suave` / `Estándar` / `Reto` | |
| Default schedules | `Work hours` / `Evenings` / `Weekends` / `Sleep` | `Horario laboral` / `Tardes` / `Fines de semana` / `Sueño` | |
| Daily goal | `Daily goal` | `Objetivo diario` | `Progress to goal` → `Progreso al objetivo`. |
| Adaptive goal | `Adaptive` | `Adaptativo` | |
| Steps | `Steps` | `Pasos` | `%lld steps` → one:`%lld paso` / other:`%lld pasos` |
| Active minutes | `Active minutes` | `Minutos de actividad` | Consistent (`Minutos de actividad y calorías`). |
| Active energy / calories | `Active calories` | `Calorías activas` | Helper: `Energía activa que quemas al moverte — no la basal.` |
| "2,026 steps until unlock" (shield) | `%@ until unlock`; `1,247 steps until unlock` | `%@ para desbloquear`; `1.247 pasos para desbloquear` | Catalog example uses a point as thousands separator. Shield button `Earn it` → `Gánatelo`; shield title `Earn your way in` → `Gánate la entrada`. |
| Emergency unlock | `Emergency unlock` | `Desbloqueo de emergencia` | `Emergency unlock until %@` → `Desbloqueo de emergencia hasta las %@`. Math gate: `Solve to continue` → `Resuelve para continuar`. |
| Partial unlock | `Partial unlock` | `Desbloqueo parcial` | `Your partial unlock ends in 10 minutes.` → `Tu desbloqueo parcial termina en 10 minutos.` |
| Rest day | `Rest day` / `Weekly rest day` | `Día de descanso` / `Día de descanso semanal` | |
| Streak | `Streak`; `Current streak` | `Racha`; `Racha actual` | |
| Streak shields | `Streak shields`; `Shield saved your streak` | `Escudos de racha`; `El escudo salvó tu racha` | |
| Most-attempted blocked app | `Most attempted blocked app today` | `App bloqueada más intentada hoy` | |
| Screen time saved (estimate) | `Screen time saved (estimated)` | `Tiempo de pantalla ahorrado (estimación)` | Live Activity: `TIME SAVED` → `TIEMPO AHORRADO`. |
| Screen Time (Apple feature) | `Allow Screen Time access` | `Permitir acceso a Tiempo de uso` | Apple's Spain term: Tiempo de uso. |
| Apple Health | `Apple Health` | `Apple Salud` | The app also says `la app Salud` / `Salud` in permission texts. |
| Locked apps | `Locked apps` | `Apps bloqueadas` | `app`/`apps` throughout (about 87 strings); no `aplicación`. |
| Family Sharing | `Family Sharing supported — Premium unlocks for up to five family members in your Apple Family group.` | `Compatible con En familia: Premium se desbloquea para hasta cinco miembros de tu grupo familiar de Apple.` | Apple's Spain name is "En familia" (feature "Compartir en familia"); see flags for the capital F in one string. |
| Activity heatmap | `Activity heatmap` | `Mapa de calor de actividad` | |
| Best week / best month | `Best week` / `BEST MONTH` | `Mejor semana` / `MEJOR MES` | |
| Goal cooldown | `Premium can bypass the 24h cooldown on lowering once per week.` | `Premium puede saltar el enfriamiento de 24 h al bajar una vez por semana.` | Another string: `Saltar enfriamiento`. |
| App icons | `Midnight` / `Ember` / `Mono` | `Medianoche` / `Brasa` / `Mono` | |
| Focus session | `Focus session` | `Sesión de concentración` | `Focus sessions are a Premium feature.` → `Las sesiones de concentración son una función Premium.` |
| Milestone card | `Next milestone`; `A quiet milestone.` | `Próximo hito`; `Un hito discreto.` | |
| Widgets (Live Activity catalog) | `EarnLock — Contributions` / `— History` / `— Streak` / `— Summary` / `— Today & Month` / `— Lock Screen` | `EarnLock — Contribuciones` / `— Historial` / `— Racha` / `— Resumen` / `— Hoy y mes` / `— Pantalla bloqueada` | Widget gallery names; `Deep Focus`, `Dynamic Island` and `Live Activity` have no UI string. |
| Apple Watch app | `Apple Watch app` | `App para el Apple Watch` | |

#### Paid tier names in the Spanish UI

`Premium` (tier), `Mensual` / `Anual` / `De por vida`, combined labels `Premium · Mensual`, `Premium · Anual`, `Premium · De por vida`, `Premium · Compartido contigo`; buttons `Consigue Premium`, `Comprar De por vida`, `Empezar prueba gratis`; `Restaurar compras`; `Gestionar suscripción`; product name `EarnLock Premium`.

#### Spanish App Store listing (fetched 2026-11-19)

- Name: **EarnLock: Bloquea Apps y Foco** (English: "EarnLock: App Blocker & Focus"). Differs. Page title: "App EarnLock: Bloquea Apps y Foco - App Store".
- Subtitle: **Gana tu tiempo de pantalla** (English: "Your steps unlock screen time"). Differs.
- IAP as shown (reference): `EarnLock Premium compra única 22,99 €` · `EarnLock Premium anual 9,99 €` · `EarnLock Premium mensual 1,99 €` (US: Lifetime $19.99, Yearly $9.99, Monthly $1.99).
- Languages: "Español y 32 más"
- Category: **Productividad**
- Compatibility shown: iPhone (iOS 17.0+), Mac (macOS 14.0+, M1 or later), Apple Vision (visionOS 1.0+), Apple Watch (watchOS 10.0+). Age 9+. `formattedPrice`: `Gratis`.

---

### 2. GymLogger X (gymlogger-x, source `GymLogger`, ID 6755734580)

The app does not use `.xcstrings`. Text comes from JSON files (`GymLogger/GymLogger/Localizations/es.json`, `GymLoggerWidget/Localizations/es.json`, `GymLoggerWatch Watch App/Localizations/es.json`), plus `GymLogger/es.lproj/InfoPlist.strings`. `es-MX.json` files exist separately. There is no App Shortcuts / Siri phrase provider (no `AppShortcutsProvider` in the project). `ExerciseTranslations.es.json` and `RehabTranslations.es.json` hold exercise and rehab names (not audited here).

#### Spanish coverage

| Catalog | Keys (en) | `es` present | % | identical to English |
|---|---|---|---|---|
| Localizations/es.json (main app) | 2923 | 2923 | 100% | 82 (Pro, 1RM, units, brand and loanwords: RIR, RPE, MEV, MRV, Kettlebell, Bro Split) |
| GymLoggerWidget/Localizations/es.json | 115 | 115 | 100% | 3 |
| GymLoggerWatch Watch App/Localizations/es.json | 98 | 98 | 100% | 5 |
| GymLogger/es.lproj/InfoPlist.strings | 4 keys | 4 | yes | Display name "GymLogger X"; both Health permissions are Spanish (tú): `GymLogger lee tu frecuencia cardíaca y calorías para proporcionar análisis de entrenamiento y seguir tu progreso físico.` / `GymLogger guarda tus entrenamientos completados en Apple Salud para mantener tus anillos de actividad e historial completos.` |

No missing keys, no empty values. **Verdict: app is in Spanish: yes** (100% of keys in app, widget and Watch; permission prompts localized). Siri phrases: not applicable (none exist).

Register: tú. About 420 of 3136 strings carry tú markers (`Selecciona un entrenamiento para empezar`, `Tienes series incompletas. ¿Realmente quieres finalizar este entrenamiento?`, `Arrastra ejercicios para reordenar`). Two usted strings: `Por favor, ingrese un nombre de ejercicio` and `Por favor, seleccione al menos un músculo` (the neighbouring `Por favor, corrige los errores en las semanas` is tú). No vosotros.

Defects (app-side; do not copy these into the site):
- **Program Creator without accents, ñ, ¿ or ¡:** 99 of the 195 `creator_*` strings (values longer than 14 characters with no accented character at all) plus short ones: `creator_step_injury` = `Lesiones y Rehabilitacion`, `creator_session_duration` = `Duracion de la Sesion`, `creator_days_per_week` = `Dias por Semana`, `creator_goal_rehab` = `Rehabilitacion y Recuperacion`, `creator_goal_recomp` = `Recomposicion Corporal`, `creator_muscle_quads` = `Cuadriceps`, `creator_muscle_glutes` = `Gluteos`, `creator_location_minimal` = `Equipamiento Minimo`, `creator_level_beginner_desc` = `Menos de 1 ano de entrenamiento constante` (ñ lost), `creator_step_equipment_desc` = `A que equipamiento tienes acceso?` and `creator_step_goals_desc` = `Que quieres conseguir?` (no ¿), `creator_no_injuries_desc` = `Perfecto! Puedes saltarte este paso si no tienes lesiones.` (no ¡). Correct spellings would be Rehabilitación, Duración, Días, Cuádriceps, Glúteos, Mínimo, año.
- `share_just_finished` has a stray backslash: `Acabo de terminar %@\!` (the English has it too: `Just finished %@\!`).
- Mixed push/pull terms for the same pair: `Empuje / Jalon` (creator, unaccented, Latin-American `jalón`), `Empuje / Tirón` (`push_pull_balance`), `Empuje/Tirón` (`analytics_push_pull`). Spain's usual word is `tirón`.
- `añadir` (43 strings) against Latin-American `agregar` / `agrega` (25 strings: `Agregar ejercicios de rehabilitacion en los dias correspondientes`, `Agregar Lesion`, `plateau_suggestion_lower_weight` = `Bajar peso, agregar repeticiones`).
- `rastrear` / `Rastrea tus entrenamientos y preparación.` (`widget_description`, 4 strings) is Latin-American; Spain says `registrar` / `seguir`.
- `Deload` has two forms: `Descarga` / `Insertar semana de descarga` in the UI, but `coach_insight_next_block_deload` keeps `un deload`.
- Title Case in sentences (`Tipo de Rutina`, `Pro de por Vida`, `Variar Repeticiones Semanalmente`) is English capitalization and not Spanish style.
- "AI Coach": `ai_coach` = `Entrenador IA` (the English site page says there is no language model and no chat bot; check before using it as a feature name).
- `Apple Health` in-app against `Apple Salud` in the permission prompts: 22 strings say `Apple Health` (`Guardado en Apple Health`, `Gestionar en Apple Health`), the InfoPlist says `Apple Salud`.

#### Glossary

| English term on site | English UI string (key) | Spanish UI string (verbatim) | Note |
|---|---|---|---|
| Free | `free` = Free | `Gratis` | `paywall_continue_free` = `Continuar con versión gratuita`. |
| Pro | `widget_pro` = Pro; `gymlogger_pro` = GymLogger X Pro | `Pro`; `GymLogger X Pro` | |
| Pro Monthly | `paywall_plan_monthly` = Monthly | `Mensual` | |
| Pro Annual | `paywall_plan_yearly` = Yearly; `paywall_yearly_pro` = Yearly Pro | `Anual`; `Pro Anual` | The app says "Yearly" (`Anual`), not "Annual". |
| Lifetime | `paywall_plan_lifetime` = Lifetime; `paywall_lifetime_pro` = Lifetime Pro; `paywall_lifetime_access` | `De por vida`; `Pro de por Vida`; `ACCESO DE POR VIDA` | Capital V in `Pro de por Vida`. Store IAP is `compra única`. `paywall_lifetime_description` → `Paga una vez, tuyo para siempre. Sin renovación.` |
| Restore Purchases | `restore_purchases` | `Restaurar compras` | |
| Start free trial | `paywall_start_trial` = Start Free Trial; `paywall_trial_text` = 1-week free trial | `Iniciar prueba gratis`; `1 semana de prueba gratis` | The trial in the app is 1 week. `paywall_trial_best_value` → `1 semana gratis • MEJOR VALOR`. |
| Tabs: Home / Training / Progress / Settings | `home_title` / `training_title` / `progress` / `settings` | `Inicio` / `Entrenamiento` / `Progreso` / `Ajustes` | |
| Smart Program Creator | `paywall_tile_program_creator` = Smart Program Creator — built around you | `Smart Program Creator — hecho para ti` | English name kept; `creator_create_program` = `Crear programa inteligente`; `creator_title` = `Creador de Programas` (the screen title; correct, but most of the screen below it is unaccented). |
| Plateau detection | `plateau_detection` = Plateau Detection | `Detección de estancamiento` | Status labels: `plateau_confirmed` = `Meseta detectada`, `plateau_watch` (Monitoring) = `En observación`, `plateau_none` (Progressing) = `Progresando`. Flag: `estancamiento` (title) and `meseta` (status) for the same concept. |
| Estimated 1RM | `analytics_estimated_1rm` = Estimated 1RM | `1RM estimado` | `widget_e1rm_a11y` = `Máximo estimado de una repetición`. |
| Deload week | `insert_deload_week` = Insert Deload Week | `Insertar semana de descarga` | `load_deload` and `creator_deload` = `Descarga`; one coach insight keeps `deload`. |
| Periodization types: linear / DUP / block / wave | `creator_periodization_*` | `Lineal` / `Ondulante (DUP)` / `Bloques` / `Ondas` | `creator_periodization` = `Estilo de Periodizacion` (unaccented). |
| Splits: Full Body / Upper-Lower / PPL / Push-Pull / Arnold / Bro | `creator_split_*` | `Cuerpo Completo` / `Tren Superior / Tren Inferior` / `Empuje / Jalon / Piernas` / `Empuje / Jalon` / `Split Arnold` / `Bro Split` | See push/pull flag. |
| Balance cards | `muscle_balance`; `front_back_balance`; `upper_lower_balance` | `Balance muscular`; `Frontal / Posterior`; `Superior / Inferior` | |
| Program library | `programs` = Programs; `example_programs` = Example Programs | `Programas`; `Programas de ejemplo` | `program_workouts` (en "Programs") = `Entrenamientos del programa`. `paywall_tile_programs` = `Más de 35 programas probados`. `training_gymlogger_programs` = `Programas GymLogger`. |
| The Golden Six | `arnold_golden_six_name` | `The Golden Six` | Name left in English. |
| Rest timer | `watch_a11y_rest_timer` = Rest timer | `Temporizador de descanso` | `info.logging.bullet3` = `Los temporizadores de descanso se ejecutan automáticamente.` Heart Rate Rest Timer: `settings_watch_hr_timer_title` = `Temporizador de descanso por FC`. LiftLog says `Cronómetro de descanso` for the same thing. |
| Templates | `templates`; `workout_templates` | `Plantillas`; `Plantillas de entrenamiento` | `save_as_template` → `Guardar como plantilla`. |
| Superset / Giant set | `superset` / `giant_set` | `Superserie` / `Serie gigante` | `create_giant_set` = `Crear serie gigante`; `creator_include_supersets` = `Incluir Superseries`. Consistent here and in LiftLog. |
| Warm-up set | `warmup_set` / `mark_as_warmup` | `Serie de calentamiento` / `Marcar como calentamiento` | |
| Sets / Reps | `sets` / `reps` | `Series` / `Repeticiones` | `Reps` (key `reps`) is `Repeticiones`; LiftLog uses `Reps` as the label. |
| Personal records | `personal_records` = Personal Records; `prs` = PRs | `Récords personales`; `Récords` | Consistent. |
| Rep-max table | `analytics_rep_max_table` = Rep-Max Table | `Tabla de máximos` | |
| Strength progress | `analytics_strength_progress` | `Progreso de fuerza` | |
| Next Move card | `analytics_next_move_label` = Next Move | `Próximo paso` | |
| Training load ratio | `analytics_acwr_title` | `Ratio de carga de entrenamiento` | `training_load` = `Carga de entrenamiento`. |
| Set volume vs MEV / MAV / MRV | `analytics_set_volume` | `Volumen de series` | `set_volume_landmark_row` = `MEV %1$@ · MAV %2$@ · MRV %3$@`; `set_volume_band_below` = `Bajo el MEV`. |
| Muscle heatmap | `muscle_heatmap` | `Mapa de calor muscular` | |
| Readiness / fatigue / recovery | `readiness_*`; `home_fatigue`; `home_recovery` | `preparación`; `Nivel de fatiga`; `Recuperación` | `readiness_explanation_intro` = `Tu puntuación de preparación se calcula en base a:`; a coach string says `disposición` for readiness (`permitiendo que la disposición se estabilice`): two words for one concept. |
| Plate calculator | `plate_calculator` | `Calculadora de discos` | |
| Weekly summary | `weekly_summary_title` | `Resumen semanal` | |
| Custom exercises | `create_custom_exercise` | `Crear ejercicio personalizado` | |
| Import a coach's spreadsheet program | `import_program` = Import Program; `import_from_spreadsheets` = Spreadsheets (CSV) | `Importar programa`; `Hojas de cálculo (CSV)` | |
| Apple Health export | `health_saved_to_health` = Saved to Apple Health | `Guardado en Apple Health` | Flag: `Apple Health` in app, `Apple Salud` in permissions. |
| Start workout | `start_workout` = Start Workout | `Iniciar entrenamiento` | Also `sesión` for a logged workout: `entrenamiento` (372 strings) and `sesión/sesiones` (117) are both used. |
| Family Sharing | `paywall_family_sharing_title` | `Incluye En familia` | `paywall_family_sharing_subtitle` → `Una sola compra. Hasta 6 miembros de la familia. Sin coste extra.` (`coste`, Spain). |
| iCloud sync | `icloud_sync` | `Sincronización iCloud` | |

#### Paid tier names in the Spanish UI

`Gratis` / `GymLogger X Pro` / `Pro`; plan cards `Mensual`, `Anual` (`Pro Anual`), `De por vida` (`Pro de por Vida`, `ACCESO DE POR VIDA`); `Iniciar prueba gratis`, `1 semana de prueba gratis`; `Restaurar compras`; `Continuar con versión gratuita`; `Pago único`; `Sin suscripción`; `MEJOR VALOR`; `MÁS POPULAR`; `Incluye En familia`.

#### Spanish App Store listing (fetched 2026-11-19)

- Name: **GymLogger X: Entrena Gym** (English: "GymLogger X: Workout Tracker"). Differs.
- Subtitle: **Entrenamiento y Registro Gym** (English: "Strength Training & Gym Log"). Differs.
- IAP as shown (reference): `GymLogger X Pro compra única 44,99 €` · `GymLogger X Pro anual 19,99 €` · `GymLogger X Pro mensual 1,99 €` · `Support the developer 1,00 €` (name not translated). US: Lifetime $39.99, Yearly $17.99, Monthly $1.99, tip $1.00.
- Languages: "Español y 33 más"
- Category: **Salud y forma física**
- Compatibility shown: iPhone (iOS 17.6+) and Apple Watch (watchOS 10.0+). Age 9+. `formattedPrice`: `Gratis`.

---

### 3. LiftLog (liftlog, source `CoreLift`, ID 6760043411)

#### Spanish coverage

| Catalog | Keys | `es` present | `es` translated | % |
|---|---|---|---|---|
| CoreLift/CoreLift/Resources/Localizable.xcstrings (main app) | 990 | 980 | 980 | 99.0% |
| CoreLift/CoreLift/Resources/AppShortcuts.xcstrings | 6 | 6 | 6 (stringSet, 3-4 phrasings each) | 100% |
| CoreLift/CoreLift/Resources/InfoPlist.xcstrings | 4 | 2 | 2 | 50% (both Health permission texts are Spanish; `CFBundleDisplayName` / `CFBundleName` have no entry, so the name is "LiftLog") |
| LiftLogWidgets/Resources/WidgetLocalizable.xcstrings | 137 | 137 | 137 | 100% |

The 10 main-app keys without `es`: ` / %lld` and `%@` (symbols only) and eight real English words that are user-visible in the Spanish app: `Average`, `Best`, `Best run`, `By month`, `By weekday`, `min`, `Sessions in run`, `Weekly avg`. The widget catalog does translate them (`Media`, `Mejor`, `Mejor racha`, `Por mes`, `Por día de la semana`), so the main app could reuse them. The catalog has no `es-MX`.

Siri: the App Shortcuts phrases are Spanish (e.g. `Inicia mi próximo entrenamiento con ${applicationName}`, `Cuál es mi racha en ${applicationName}`, `Registra mi serie en ${applicationName}`), but the Siri hint in Localizable tells users to say the English phrases: `Di «Start my next workout with LiftLog» para empezar una sesión, o pregunta «What’s my streak in LiftLog?» y «How much did I lift this week in LiftLog?» para obtener una respuesta sin abrir la app.` App-side inconsistency.

Permission texts name the app **LiftLog**: `LiftLog nunca lee tus datos de salud de Apple Salud: solo guarda tus entrenamientos de fuerza completados para que cuenten para tus anillos de actividad.` / `LiftLog guarda tus entrenamientos de fuerza completados en Apple Salud para que cuenten para tus anillos de actividad. Nunca lee tus datos de salud.`

**Verdict: app is in Spanish: yes** (99% main app, 100% widgets and Shortcuts; 8 English fallbacks in the stats screens).

Register: tú. About 132 of 1119 strings carry tú markers (`Define el máximo de entrenamiento`, `Añade ejercicios personalizados o carga la biblioteca.`, `Llevas una racha de %lld semanas.`), 0 real usted strings, no vosotros. Widgets are tú too.

Wording flags:
- `Back` in the widget catalog is `Atrás` (the navigation word) where a body-part label is meant; the neighbouring `BACK` = `ESPALDA` and `Back` should be `Espalda`.
- `Rest Timer` = `Cronómetro de descanso` (cronómetro is a stopwatch; GymLogger X says `Temporizador de descanso`); the Siri phrase says `Inicia mi cronómetro de descanso`.
- `PR` badge = `RP` (an abbreviation nobody uses; Spanish lifters say `PR` or `récord`).
- `Sets` = `Series` and `Streak` = `Racha` (no collision, unlike French `série`); `Reps` stays `reps` in 30 strings while `repeticiones` is used in 11.
- `Tier: Good` is `Bien` in the app but `Bueno` in the store (see tiers below).
- No Latin-American vocabulary found (`peso muerto`, `mancuerna`, `jalón` are fine for Spain).

#### Glossary

| English term on site | English UI string (key) | Spanish UI string (verbatim) | Note |
|---|---|---|---|
| Free trial | `Free Trial`; `Free for 7 days.` | `Prueba gratuita`; `Gratis durante 7 días.` | `%d days left in trial` → `%d días restantes de la prueba`; `You won't be charged today. We'll remind you in 7 days.` → `Hoy no te cobramos. Te avisaremos en 7 días.` |
| Tier: Fair | `Fair` | `Justo` | Same as the store (`Acceso completo · Justo`). |
| Tier: Good | `Good` | `Bien` | **Store IAP is `Acceso completo · Bueno`.** |
| Tier: Generous | `Generous` | `Generoso` | Same as the store. |
| Tier: Patron | `Patron` | `Mecenas` | Same as the store. |
| Full access | `Full Access` | `Acceso completo` | |
| One-time purchase / no subscription | `One-time purchase`; `No subscription` | `Compra única`; `Sin suscripción` | `Pay what feels fair.` → `Paga lo que te parezca justo.`; `One payment. Yours forever. Free for the next 7 days.` → `Un solo pago. Tuyo para siempre. Gratis los próximos 7 días.` |
| Restore Purchases | `Restore Purchases` | `Restaurar compras` | |
| Tabs: Home / Exercises / Programs / Progress / Settings | same | `Inicio` / `Ejercicios` / `Programas` / `Progreso` / `Ajustes` | `History` → `Historial`. |
| Log set key | `Log set · start rest`; `Log Set` | `Registrar serie · iniciar descanso`; `Registrar serie` | Consistent verb `Registrar`. |
| Rest timer | `Rest Timer` / `Rest timer` | `Cronómetro de descanso` | Consistent inside the app. |
| Estimated 1RM | `Estimated 1RM`; `Est. 1RM` | `1RM estimado`; `1RM est.` | |
| Rep PRs | `Rep PRs`; `PR` | `Récords de repeticiones`; `RP` | See flag. |
| Personal bests | `Personal Bests`; `New Personal Bests`; `Personal record` | `Récords personales`; `Nuevos récords personales`; `Récord personal` | |
| Best set / Best volume | `Best Set` / `Best Volume` | `Mejor serie` / `Mejor volumen` | |
| Activity heatmap | `Complete workouts to see your progress and activity heatmap.` | `Completa entrenamientos para ver tu progreso y el mapa de actividad.` | Feature name = **mapa de actividad**. Widget: `Activity grid` → `Cuadrícula de actividad`. |
| Last 30 days | `Last 30 days` | `Últimos 30 días` | |
| Training Max | `Set a training max` | `Define el máximo de entrenamiento` | Noun: `máximo de entrenamiento`; `% of training max` → `% del máximo de entrenamiento`. |
| Double progression / Progression | `Double progression` / `Progression` | `Doble progresión` / `Progresión` | |
| Deload (trigger) | `Deload` | `Descarga` | `Deload after` → `Descarga tras`. |
| Adaptive 1RM formula | `Adaptive (recommended)`; `1RM Formula` | `Adaptable (recomendada)`; `Fórmula de 1RM` | |
| Superset / Giant set | `Superset` / `Giant Set` | `Superserie` / `Serie gigante` | `Create Superset` → `Crear superserie`. |
| How To (exercise detail) | `How To` | `Cómo hacerlo` | |
| Workout | `Workout` | `Entrenamiento` | `entrenamiento` (92 strings) is the app's word; `sesión` (42) is used for a logged session. |
| Sets / Reps | `Sets` / `Reps` | `Series` / `Reps` | See flags. |
| Streak | `Streak` | `Racha` | `%lld week streak` → `Racha de %lld semanas`. |
| Export (JSON / CSV) | `Export Data (CSV)` / `Export Data (JSON)` | `Exportar datos (CSV)` / `Exportar datos (JSON)` | |
| Apple Health | `Apple Health` | `Apple Salud` | |
| Family Sharing | `Family Sharing` | `En familia` | |
| Warm-up set | `Warm-up set %lld` | `Serie de calentamiento %lld` | |
| Siri & Shortcuts | `Siri & Shortcuts` | `Siri y Atajos` | Apple's Spain term: Atajos. |
| Support | `Support`; `Funds 3 months of dev` | `Apoyar`; `Financia 3 meses de desarrollo` | |

Program names (StrongLifts 5×5, 5/3/1, GZCLP, Greyskull LP, ...) stay in English; descriptions are Spanish. Exceptions where the app's Spanish program catalog (`~/Downloads/GymLogger/scripts/catalog_translations/es.json`) gives a Spanish name, used on the site: «Fundamento 5×5 lineal», «Método Texas», «Método conjugado», «Rampa 5×5 intermedia» (Intermediate 5×5 Ramp), «Pesado / Ligero / Medio 5×5» (Heavy / Light / Medium 5×5). Plateau statuses on the site follow the Spanish app page: «Estancamiento», «En observación», «Estancamiento previsto» (the UI also has «Meseta detectada»; checked 2026-11-19, Tier 3 batch 3).

#### Paid tier names in the Spanish UI

LiftLog has no Pro/Premium and no subscription: it is a one-time purchase with four tiers that all unlock the same app: `Justo` / `Bien` / `Generoso` / `Mecenas` (in-app) against `Justo` / `Bueno` / `Generoso` / `Mecenas` (App Store IAP names); buttons `Desbloquear`, `Desbloquear LiftLog`, `Prueba gratuita`, `Restaurar compras`; `Un solo pago. Tuyo para siempre. Gratis los próximos 7 días.` The only mismatch is Good: `Bien` (app) against `Bueno` (store).

#### Spanish App Store listing (fetched 2026-11-19)

- Name: **LiftLog: Gimnasio Diario** (English: "LiftLog: Workout Gym Tracker"). Differs. Page title: "App LiftLog: Gimnasio Diario - App Store".
- Subtitle: **Series, reps y fuerza** (English: "Sets, reps & strength programs"). Differs.
- IAP as shown (reference): `Acceso completo · Justo 9,99 €` · `Acceso completo · Bueno 22,99 €` · `Acceso completo · Generoso 39,99 €` · `Acceso completo · Mecenas 44,99 €` (US: Fair $9.99, Good $19.99, Generous $29.99, Patron $39.99).
- Languages: "Español y 43 más"
- Category: **Salud y forma física**
- Compatibility shown: iPhone (iOS 17.6+), Mac (macOS 14.6+, M1 or later), Apple Vision (visionOS 1.3+). Age 4+. `formattedPrice`: `Gratis`.

---

### 4. MediaKit (mediakit, source `ClearCut`, ID 6761451361)

#### Spanish coverage

| Catalog | Keys | `es` present | `es` translated | % |
|---|---|---|---|---|
| ClearCut/MediaKit/Localizable.xcstrings (main app) | 2583 | 2583 | 2583 | 100% |
| ClearCut/MediaKit/AppShortcuts.xcstrings | 6 | 6 | 6 | 100% |
| ClearCut/MediaKit/InfoPlist.xcstrings | 26 | 23 | 23 | 88.5% (Photo Library add permission, Speech Recognition permission and the file-type names are Spanish; missing: `CFBundleDisplayName`, `CFBundleName`, `NSHumanReadableCopyright`, so the name stays "MediaKit") |
| ClearCut/MediaKitShareExtension/Localizable.xcstrings | 13 | 13 | 13 | 100% |

Every catalog also has `es-MX`. Permission texts: `MediaKit guarda los vídeos e imágenes procesados en tu fototeca.` / `MediaKit usa el reconocimiento de voz para transcribir audio y vídeo a texto cuando ejecutas la herramienta Transcribir.` Siri phrases are Spanish: `Comprimir un vídeo con ${applicationName}`, `Combinar PDF con ${applicationName}`, `Crear un ZIP con ${applicationName}`.

**Verdict: app is in Spanish: yes** (100% of the main app, Shortcuts and share extension; permissions localized).

Register: tú. About 223 of 2619 strings carry tú markers (`Prueba con H.264 o define una tasa de bits...`, `Suelta un archivo para previsualizarlo`, `Permite que MediaKit guarde junto a tus archivos...`), 0 real usted strings, no vosotros. Spanish-Spain markers: `vídeo` with accent (72 strings), `fototeca`, `coste`.

Wording flags:
- `Redact` has three different Spanish verbs: `Censurar PDF` / `Censurar` (tool), `Tachar rectángulos` (a rectangle option) and `Redactar rectángulos` (another key for the same option), `Censurando %@…`. "Redactar" means "to write", so `Redactar rectángulos` is a false friend.
- `Archive` (category) = `Archivo`, which is also Spanish for "file" (`Archivo de audio`, `Archivo de subtítulos`); the InfoPlist file-type name is `Archivo comprimido`. A site term for the archive category should be `Archivos comprimidos`, not `Archivo`.
- `Trim` = `Recortar tiempo` and `Crop` = `Recortar`, so the pair is distinguished only by the added words.
- `Free` (key `Free`, tier label) = `Libre`, while `Free tier` = `Plan gratuito`; check where `Libre` shows.
- Family Sharing is `Compatible con Compartir en Familia` (capital F; Apple's Spain feature is "Compartir en familia").
- Ellipsis style: `Estabilizando %@...` (three dots) beside `Estabilizando…` elsewhere.
- Free-trial strings mix `Prueba gratuita de %@` and `%@ de prueba gratis · %@/mes`.
- Several keys identical to English that look like raw values (`bottom`, `bottomLeft`, `bottomRight`, `center`, `left`, `Horizontal`): possibly internal, worth checking in the app.

#### Glossary

| English term on site | English UI string (key) | Spanish UI string (verbatim) | Note |
|---|---|---|---|
| Pro | `Pro` | `Pro` | `Upgrade to Pro` → `Actualizar a Pro`; `Unlock Pro` → `Desbloquear Pro`. |
| Pro · Monthly | `Monthly` | `Mensual` | |
| Pro · Annual | `Annual` | `Anual` | The key here is "Annual" (GymLogger X and EarnLock use "Yearly"). |
| Lifetime | `Lifetime` | `De por vida` | Store IAP: `MediaKit Pro compra única`. |
| Free trial (3 days) | `Every tool, 3 days free`; `%@ free trial`; `%@ free trial · %@/mo` | `Todas las herramientas, 3 días gratis`; `Prueba gratuita de %@`; `%@ de prueba gratis · %@/mes` | |
| Free tier (five tools stay free) | `Free tier`; `Free` | `Plan gratuito`; `Libre` | `Free tier includes 5 unlimited tools forever.` → `El plan gratuito...`. |
| Tool (generic) | `Tool`; `Add a Tool to the Recipe` | `Herramienta`; `Añadir una herramienta a la receta` | |
| Recipes (chained tools) | `Recipes`; `Create a new multi-step recipe`; `Recipe Marketplace` | `Recetas`; `Crea una nueva receta de varios pasos`; `Mercado de recetas` | Feature name = **receta**; `Browse Recipe Marketplace` → `Explorar el mercado de recetas`. |
| Make It Fit | `Make It Fit` | `Hacer que encaje` | |
| Video / Image Compress | `Compress`; `Compress Video`; `Compress Image` | `Comprimir`; `Comprimir vídeo`; `Comprimir imagen` | |
| Image Resize | `Resize` | `Cambiar tamaño` | |
| Convert (audio, image...) | `Convert`; `Convert Image` | `Convertir`; `Convertir imagen` | |
| Categories: Video / Audio / Image / PDF / Archive / Ebook | same | `Vídeo` / `Audio` / `Imagen` / `PDF` / `Archivo` / `Libro electrónico` | See `Archivo` flag. |
| Batch processing | `Batch Processing` | `Procesamiento por lotes` | |
| Export presets | `Preset`; `Platform preset` | `Ajuste preestablecido`; `Ajuste de plataforma` | Spain's term for a preset in this app is `ajuste preestablecido` (not `preajuste`). |
| Shortcuts actions | `Shortcuts & Siri` | `Atajos y Siri` | Apple's Spain term: Atajos. |
| Merge | `Merge`; `Merge PDFs` | `Combinar`; `Combinar PDF` | `Merge` is `Combinar` (not `Fusionar`). |
| Extract text / OCR | `Extract Text from Image`; `OCR` | `Extraer texto de una imagen`; `OCR` | |
| Remove background | `Remove background` | `Quitar el fondo` | |
| AI upscale | `AI Upscale` | `Escalado con IA` | |
| Auto Subtitle | `Auto Subtitle`; `Auto Subtitle + Translate` | `Subtítulos automáticos`; `Subtítulos auto + traducción` | |
| Transcribe | `Transcribe` | `Transcribir` | |
| Strip EXIF metadata | `Strip Metadata` | `Eliminar metadatos` | |
| Reduce noise | `Noise Reduce` / `Denoise` | `Reducir ruido` / `Reducir ruido` | Same value for both keys. |
| Normalize (EBU R128 / LUFS) | `Normalize loudness`; `EBU R128 loudness normalization` | `Normalizar la sonoridad`; `Normalización de sonoridad EBU R128` | Consistent (`sonoridad`). |
| Redact | `Redact PDF`; `Redact`; `Redact rectangles` | `Censurar PDF`; `Censurar`; `Tachar rectángulos` | See flag. |
| Compare | `Compare`; `Compare Takes` | `Comparar`; `Comparar tomas` | |
| Smart Duplicate Finder | `Smart Duplicate Finder` | `Buscador inteligente de duplicados` | |
| Trim / Stabilize / Watermark / Crop / Rotate / Flip / Sign / Encrypt | same | `Recortar tiempo` / `Estabilizar` / `Marca de agua` / `Recortar` / `Girar` / `Voltear` / `Firmar` / `Cifrar` | |
| Drop a file in | `Drop a file to preview` | `Suelta un archivo para previsualizarlo` | The verb is `soltar`. |
| Watch folder / Folder Automation | `Watch folder`; `Folder Automation` | `Carpeta vigilada`; `Automatización de carpetas` | |
| Menu bar | no UI string | n/a | Apple's Spain term would be "barra de menús"; not in the catalog (count 0). |
| Settings | `Settings` | `Ajustes` | |
| Restore Purchases | `Restore Purchases` | `Restaurar compras` | |
| Share extension | `Open in MediaKit`; `Send to MediaKit` | `Abrir en MediaKit`; `Enviar a MediaKit` | |
| Family Sharing | no standalone string | `Compatible con Compartir en Familia` | |

#### Paid tier names in the Spanish UI

`Pro`; `Mensual` / `Anual` / `De por vida`; `Prueba gratuita de %@`; `Plan gratuito`; `Actualizar a Pro`; `Desbloquear Pro`; `Restaurar compras`. Store IAP names: `MediaKit Pro mensual`, `MediaKit Pro anual`, `MediaKit Pro compra única`.

#### Spanish App Store listing (fetched 2026-11-19)

- Name: **MediaKit Comprimir y Convertir** (English: "MediaKit: Compress & Convert"). Differs (no colon, no ampersand).
- Subtitle: **Vídeo, Audio, Imagen, PDF, ZIP** (English: "Video, Audio, Image, PDF & ZIP"). Differs (accent and no ampersand).
- IAP as shown (reference): `MediaKit Pro anual 24,99 €` · `MediaKit Pro compra única 44,99 €` · `MediaKit Pro mensual 4,99 €` (US: Yearly $22.99, Lifetime $39.99, Monthly $3.99).
- Languages: "Español y 11 más"
- Category: **Utilidades**
- Compatibility shown: iPhone (iOS 17.0+), Mac (macOS 14.6+), Apple Vision (visionOS 1.0+). Age 4+. `formattedPrice`: `Gratis`.

---

### 5. Millrace (millrace, source `thegame`, ID 6759511759)

The site never writes the number the old name contained. None of the Spanish strings below contain it, and the Spanish column has 0 strings with it.

#### Spanish coverage

| Catalog | Keys | `es-ES` present | `es-ES` translated | % |
|---|---|---|---|---|
| thegame/thegame/Localizable.xcstrings (only catalog) | 333 | 333 | 333 | 100% (locale code is `es-ES`; there is no plain `es` column; `es-MX` also 333) |
| InfoPlist | no InfoPlist.xcstrings | | | Display name "Millrace" comes from the build settings and is the same in every language; the app requests no permissions. |

Only two strings are identical to English: `Extras` and `Game Center`. **Verdict: app is in Spanish: yes (100%).** Siri: no App Shortcuts catalog. Register: tú (about 50 of 333 strings carry tú markers: `Mantén tus fichas grandes juntas en una misma fila, ordenadas por tamaño.`, `Toca dos veces para ver los detalles del tema`, `Gratis · siempre tuyo`), 0 usted, no vosotros.

Wording flags:
- **`Undo` as a noun is the bare infinitive** `deshacer` in every count: `%lld Undos` → `%lld deshacer` (both plural categories), `10 Undos` → `10 deshacer`, `Get Undos` → `Conseguir deshacer`, `Add 50 Undos` → `Añadir 50 deshacer`, `Racha de %lld días: %lld deshacer`, and the store IAPs `10 deshacer`, `50 deshacer`, `200 deshacer`. Natural Spanish would be `deshaceres` or `10 pasos atrás`; `Undo Tokens` = `Fichas de deshacer` also reads oddly.
- Daily: `Reto diario` (challenge) but `Diario` and `Mejor diario` for the bare label and the daily best.
- `Puzzles` = `Puzles` (RAE plural); the store name says `Entrega de fichas`, not "puzle".
- `Haptics` = `Respuesta táctil`.
- The locale code is `es-ES` while the sibling apps use `es`; check that Spanish-language devices in Latin America fall back to `es-MX`, which is fine, but a user set to plain Spanish resolves to `es-ES`.

#### Glossary

| English term on site | English UI string (key) | Spanish UI string (`es-ES`, verbatim) | Note |
|---|---|---|---|
| Chapter: Warm-up | `Warm-up` | `Calentamiento` | |
| Chapter: Tactics | `Tactics` | `Táctica` | |
| Chapter: Pressure | `Pressure` | `Presión` | |
| Chapter: Precision | `Precision` | `Precisión` | |
| Chapter: Deep Water | `Deep Water` | `Aguas profundas` | |
| Chapter: Mastery | `Mastery` | `Maestría` | |
| Level | `Level %lld` | `Nivel %lld` | No "Chapter" string (no `capítulo` in the catalog). |
| Puzzle | `Puzzles`; `Next puzzle`; `Puzzle not solved` | `Puzles`; `Siguiente puzle`; `No has resuelto el puzle` | Term = **puzle** (Spain). |
| Freeplay | `Freeplay` | `Juego libre` | `Merge as long as you can. No goal, no move limit.` → `Fusiona todo lo que puedas. Sin objetivo ni límite de movimientos.` (verb `fusionar` here, `Combina dos fichas %@` for the same action elsewhere: two verbs). |
| Hint | `Hint` | `Pista` | `Dismiss tip` → `Descartar consejo`. |
| The Coach | `Coach`; `Coaching notes` | `Entrenador`; `Notas del entrenador` | |
| Daily board / daily challenge | `Daily Challenge` / `Daily challenge` / `Daily` | `Reto diario` / `Reto diario` / `Diario` | `Daily Best` → `Mejor diario`. No "daily board" string. |
| Undo | `Undo` | `Deshacer` | See flag on the plural noun. |
| Daily streak | `Current Streak` / `Longest Streak` / `Streak Rewards` | `Racha actual` / `Racha más larga` / `Recompensas por racha` | `%lld-day streak: %lld undos` → `Racha de %lld días: %lld deshacer`. |
| Personal best | `Personal Best` / `Best` / `NEW BEST` | `Récord personal` / `Mejor` / `NUEVO RÉCORD` | `Best Score` → `Mejor puntuación`; `Best Tile` → `Mejor ficha`. |
| Move budget / moves left | `%lld moves left`; `No moves left` | one:`%lld movimiento restante` / other:`%lld movimientos restantes`; `No quedan movimientos` | The unit is **movimiento**. `Best possible is %lld moves` → `El mínimo posible son %lld movimientos`. No "move budget" string. |
| Target cell | `This is the target cell.` | `Esta es la celda objetivo.` | VoiceOver; the term is **celda objetivo** / **celda marcada** (`Forma exactamente %@ en la celda marcada`). The grid is `tablero`, and `de 16 celdas ocupadas`. |
| Inlet | no UI string | `Las fichas siguen llegando a la celda marcada. Si la bloqueas, pierdes.` | The app describes the inlet without naming it; the store subtitle says `una sola entrada`. The site needs its own Spanish term. |
| Tile | `%lld tiles arriving` | one:`%lld ficha por llegar` / many:`%lld fichas por llegar` / other:`%lld fichas por llegar` | Term = **ficha**; `Highest tile %lld` → `Ficha más alta %lld`. |
| Blocked | `Blocked` | `Bloqueado` | |
| Theme / themes | `Theme` / `Themes` | `Tema` / `Temas` | |
| Theme packs | `Designer Pack 1` / `Designer Pack 2` / `Summer Pack` / `Winter Pack` | `Pack de diseño 1` / `Pack de diseño 2` / `Pack de verano` / `Pack de invierno` | Matches the store IAP names exactly. |
| Complete Collection | `Complete collection` | `Colección completa` | `Unlock All Themes` → `Desbloquear todos los temas`; `Every theme. Forever.` → `Todos los temas. Para siempre.` |
| Classic (free theme) and theme names | no catalog entries | n/a | Theme names are not localized. |
| Support the Developer (tip) | `Support the Developer` | `Apoya al desarrollador` | |
| Game Center leaderboards / achievements | `Leaderboards` / `Achievements` | `Clasificaciones` / `Logros` | |
| Settings: Haptics / Sound Effects / Music | same | `Respuesta táctil` / `Efectos de sonido` / `Música` | |
| Settings | `Settings` | `Ajustes` | |
| No subscription | `One-time purchases. No subscription. No ads, ever.` | `Compras únicas. Sin suscripción. Sin anuncios, nunca.` | |
| Restore Purchases | `Restore Purchases` | `Restaurar compras` | |

#### Paid tier names in the Spanish UI

Millrace has no Premium/Pro tier. It is free with one-time purchases: `Colección completa`, `Pack de diseño 1`, `Pack de diseño 2`, `Pack de verano`, `Pack de invierno`, undo packs `10 deshacer` / `50 deshacer` / `200 deshacer`, tip `Apoya al desarrollador`; buttons `Desbloquear`, `Desbloquear %@`, `Desbloquear todo`, `Restaurar compras`; label `Pago único`. No free-trial string.

#### Spanish App Store listing (fetched 2026-11-19)

- Name: **Millrace: Entrega de fichas** (English: "Millrace: Tile Delivery Puzzle"). Differs. Page title: "App Millrace: Entrega de fichas - App Store".
- Subtitle: **64 niveles, una sola entrada** (English: "64 forged levels, one inlet"). Differs.
- IAP as shown (reference): `Colección completa 6,99 €` · `50 deshacer 2,99 €` · `Pack de invierno 1,99 €` · `Apoya al desarrollador 1,99 €` · `200 deshacer 6,99 €` · `10 deshacer 0,99 €` · `Pack de diseño 2 1,99 €` · `Pack de diseño 1 1,99 €` · `Pack de verano 1,99 €` (US: Complete Collection $5.99, 200 Undos $5.99).
- Languages: "Español y 33 más"
- Category: **Juegos de mesa** (English storefront: "Board")
- Compatibility shown: iPhone (iOS 18.0+), iPad (iPadOS 18.0+), Mac (macOS 15.0+, M1 or later), Apple Vision (visionOS 2.0+). Age 4+. `formattedPrice`: `Gratis`.

---

### Cross-app terms (as the five apps write them in Spanish)

| Concept | Spanish used | Where it varies |
|---|---|---|
| Restore Purchases | `Restaurar compras` | Identical in all five. |
| Settings | `Ajustes` | Identical in all five (Apple's Spain term). |
| Apple Health | `Apple Salud` (EarnLock, LiftLog, GymLogger X permissions), `Apple Health` (GymLogger X in-app, 22 strings) | GymLogger X only. |
| Screen Time (Apple feature) | `Tiempo de uso` | EarnLock only (6 marketing strings use `tiempo de pantalla`). |
| Family Sharing | `En familia` (EarnLock, GymLogger X, LiftLog), `Compartir en Familia` (MediaKit) | Capital F in three strings; no string in Millrace. |
| Monthly / Yearly or Annual | `Mensual` / `Anual` | Identical wording across apps. |
| Lifetime | `De por vida` | GymLogger X also `Pro de por Vida`, `ACCESO DE POR VIDA`. |
| One-time purchase | `compra única` (store IAPs, LiftLog `Compra única`, `pago único` in EarnLock), `Pago único` (GymLogger X, Millrace) | Two forms. |
| Free trial | `prueba gratuita` / `prueba gratis` | Mixed inside EarnLock, GymLogger X and MediaKit. |
| Streak | `Racha` | Identical in all (no collision with `serie`). |
| Personal best / PR | `Récord personal`, `Récords personales` | LiftLog badge `RP` is the exception. |
| Sets / Reps | `Series` / `Repeticiones` (GymLogger X), `Series` / `Reps` (LiftLog) | |
| Superset / giant set | `Superserie` / `Serie gigante` | Identical in GymLogger X and LiftLog. |
| Deload | `Descarga` | GymLogger X keeps `deload` in one coach string. |
| Rest timer | `Temporizador de descanso` (GymLogger X), `Cronómetro de descanso` (LiftLog) | |
| Workout | `Entrenamiento` (`sesión` for a logged session) | |
| Video | `vídeo` with accent (MediaKit 72 strings) | |
| App | `app` / `apps` (lowercase); `aplicación` only 12 times in GymLogger X and once in MediaKit | |
| Heatmap | `Mapa de calor` (EarnLock, GymLogger X), `mapa de actividad` (LiftLog) | |
| Unlock | `Desbloquear` / `Desbloqueo` | Identical across EarnLock, LiftLog, Millrace. |
| Premium / Pro | `Premium` (EarnLock), `Pro` (GymLogger X, MediaKit) | Not translated. |
| Lock Screen | `Pantalla bloqueada` (EarnLock widget title) | Apple's term would be `pantalla de bloqueo`. |
| Siri & Shortcuts | `Atajos y Siri` / `Siri y Atajos` | Word order differs between MediaKit and LiftLog. |
| Mac | `este Mac`, `tu Mac` (masculine) | Consistent in MediaKit. |

---

### Flags (app-side string bugs, register mixes, missing Spanish)

1. **GymLogger X, Program Creator unaccented (99 of 195 `creator_*` strings).** No accents, no ñ, no ¿ ¡, plus Latin-American `Jalon` and `Agregar`. Keys include `creator_step_injury`, `creator_goal_rehab`, `creator_session_duration`, `creator_level_beginner_desc`, `creator_step_equipment_desc`, `creator_no_injuries_desc`. App-side; same bug as French.
2. **LiftLog tier label mismatch:** in-app `Bien` against store IAP `Bueno` (the French equivalent mismatched two tiers; here one). The site needs a single choice.
3. **LiftLog English fallbacks:** `Average`, `Best`, `Best run`, `By month`, `By weekday`, `min`, `Sessions in run`, `Weekly avg` have no `es` in `Localizable.xcstrings` (the widget catalog has them). The Siri hint tells Spanish users to say English phrases; `Back` in the widget catalog is `Atrás` (should be `Espalda`).
4. **Millrace undo noun `deshacer`** in every count and in the store IAP names (`50 deshacer`, `200 deshacer`); also Spanish lives under `es-ES` rather than `es`.
5. **EarnLock permissions `needs_review`:** the three permission prompts (and the Watch's two) are Spanish but unreviewed; `CFBundleDisplayName` has no `es` entry.
6. **EarnLock vocabulary:** Siri phrase `Qué tan cerca estoy de desbloquear` (Latin-American), widget title `Pantalla bloqueada` (calque of "Lock Screen"), `Shadow Mode` left in English in one error string, `Tiempo de pantalla` against `Tiempo de uso`, `En Familia` capitalization, two free-trial patterns.
7. **MediaKit `Redact`** is three words (`Censurar`, `Tachar`, `Redactar`; the last is a false friend), `Archive` = `Archivo` collides with "file", `Trim` = `Recortar tiempo` vs `Crop` = `Recortar`, `Free` = `Libre`.
8. **Register is clean:** all five apps are tú. The only usted strings are two GymLogger X validation messages (`Por favor, ingrese...`, `Por favor, seleccione...`). No vosotros, no vos, no `celular` / `computadora`; `móvil` appears in EarnLock and GymLogger X (fine for Spain). The Latin-American markers found are `agregar` (GymLogger X), `rastrear` (GymLogger X widget text), `jalón` / `Jalon` (GymLogger X), `Qué tan` (EarnLock Siri).
9. **Missing Spanish:** no Spanish for the Dynamic Island, Live Activity or Deep Focus names in EarnLock (no UI string), no `capítulo` string in Millrace, no menu bar string in MediaKit, no Siri phrases in GymLogger X (none exist), and no Spanish name for Millrace's inlet (the store subtitle uses `entrada`).
10. **House rule for Millrace:** the old name's number appears nowhere in the Spanish `es-ES` column or the Spanish store text (checked by search: 0 hits), and this file doesn't write it.


---

## Spanish glossary, batch 3: mockly, observa, pawza, rightsplit, shogiful

Method (checked 2026-11-19). Read-only. Counts come from a `python3` script over every `.xcstrings` in each app's source folder (no worktree, `.build`, DerivedData or Pods copies exist in these five folders): `strings` → key → `localizations` → `es` → `stringUnit` (state, value), `variations` or `stringSet`. Blank keys and `shouldTranslate: false` keys are excluded from the totals. "Translated" = state `translated`, or a `variations` block (plural forms). `es-MX` and `es-419` were ignored except to note them. **Mockly is the exception: its catalog has `es-ES` and `es-MX` but no plain `es`, so the Mockly numbers are for `es-ES`.** Spanish values are copied verbatim from the catalogs. Register counts are rough regex counts over `es` values (tú: tu/tus/te/ti/contigo/eres/puedes/tienes/quieres/necesitas/sabes/estás, plus strings that start with a tú imperative such as Introduce, Pulsa, Toca, Añade; usted: usted/ustedes/suyo and usted imperatives such as Ingrese, Presione, Toque, Introduzca; vosotros/vos: vosotros, vuestro, -áis/-éis, vos, tenés). App Store data comes from the iTunes lookup API (`country=es&lang=es_es` and `country=us`) plus `curl` (Safari User-Agent, `Accept-Language: es-ES` / `en-US`) of `https://apps.apple.com/es/app/id<ID>` and `/us/app/id<ID>`, parsed from the raw `serialized-server-data` JSON, not a summarizer. The stores returned HTTP 429 on the first pass; the pages were read after retries with pauses. One page still returned 429 (Observa US), so its US subtitle is "not verified (429)". Prices use a NO-BREAK SPACE (U+00A0) before the euro sign. Prices are reference only. The seller line on the store pages carries the owner's personal name; it is deliberately not copied. The lookup API's `primaryGenreName` is always English, so the Spanish category names come from the store page. Shared note: es and es-MX are identical for 89% to 94% of strings in each catalog (Mockly 297/333, Observa 6149/6686, Pawza 1129/1322, RightSplit 432/499, Shogiful 3626/3751), so the `es` values are largely neutral Spanish; the vocabulary below is Spain-leaning ("añadir", "propina", "móvil", "recibo").

## Summary

| App | Main catalog `es` | Extensions / other catalogs | InfoPlist / permissions | Register | Verdict |
|---|---|---|---|---|---|
| Mockly | 333/333 (100%), code `es-ES` (no plain `es`) | none | InfoPlist 4/4 (`es-ES`) | tú | **yes** |
| Observa | 6672/6684 translated (99.8%); all 6684 have a value; 12 `needs_review` | Watch 477/477, Widgets 403/403, AppShortcuts 15/15 have a value (9 translated, 6 `needs_review`) | app 5/5, watch 5/5 (Health, Siri texts in Spanish) | tú | **yes** |
| Pawza | 1322/1323 (99.9%) | AppShortcuts 4/4; no widget catalog (widgets share the main one) | **none**: no InfoPlist catalog, camera and photo texts are English build settings | tú | **yes** (permission prompts in English) |
| RightSplit | 499/499 (100%) | Widgets 376/376, Share 3/3, SplititKit 65/65 | InfoPlist 5/5 | tú | **yes** |
| Shogiful | 3751/3751 (100%) | none | InfoPlist 0/2 (only display and bundle name, English-only catalog; the app requests no permissions) | tú | **yes** |

Keys without `es`: Pawza `%@` (format-only). Mockly has no key without `es-ES` except the blank key. Every app is tú. No usted, vosotros or vos form turned up in any catalog (the few regex hits are false positives, listed per app).

Cross-app flags for the whole batch are at the end ("Cross-app terms" and "Flags").

---

### 1. Mockly (`mockly`, source `AppScreenMaker/`, ID 6756589122, macOS)

### Spanish coverage

- `Resources/Localizable.xcstrings`: 333 keys, all 333 have an `es-ES` value in state translated (100%). **There is no `es` locale; the catalog holds `es-ES` and `es-MX`** (10 languages in all: de, en, es-ES, es-MX, fr, ja, ko, pt-BR, tr, zh-Hans). Xcode maps a Spain-Spanish device to `es-ES`, so the app is localized for Spain; but any tooling that reads only `es` will report Mockly as untranslated. `es-ES` and `es-MX` are identical for 297 of 333 strings.
- `InfoPlist.xcstrings`: 4/4 in `es-ES` (`CFBundleDisplayName` "Mockly", `CFBundleName` "Mockly", `Mockly Project` → "Proyecto de Mockly", `NSHumanReadableCopyright` → "Copyright © 2026. Todos los derechos reservados.").
- No extensions, no Siri phrases, no widgets, no permission prompts, no `.lproj` files.
- Register: **tú** (19 strings with tu/tus/te/ti, 11 that start with a tú imperative; 0 usted). One `su` hit is third person ("Describe qué hace tu app y su propuesta de valor principal."). No Latin-American vocabulary found.
- **Verdict: app is in Spanish: yes** (as `es-ES`).

Flags
- **M1 (locale code):** `es-ES` instead of `es` (see above).
- **M2 (translation packs):** the app sells translation credit packs ("Packs de traducción", "Créditos de traducción") next to bring-your-own-key. The Spanish store page lists no in-app purchases, so the packs may not be live. The site only says "your own key". Check before the Spanish page says anything about packs (same issue as the German and French glossaries).
- **M3 (language count):** the Spanish store subtitle is "50 idiomas, un clic" (the US subtitle is "50 Languages, One Workflow"; "un clic" is not a translation of "One Workflow"). The app itself ships in 10 languages. The site mixes "50 languages" (App Store locales Mockly can build) and "39". Pick one number.
- **M4 (upload verb):** `Upload` is "Subir" in buttons ("Subir a App Store Connect", "Subiendo capturas…") and the noun is "Subida completada". The count string reads `%lld uploaded` → "%lld subidas" and `%lld uploaded, %lld failed` → "%lld subida(s), %lld con error" (one gender-neutral workaround, one plain plural).
- **M5 (odd word):** `Preset` → "Ajuste" (artboard preset). "Ajuste" also means setting. A Spanish page should say "tamaño predefinido" or similar, but the app's own string is "Ajuste".
- Mixed words: "app" is used throughout ("tu app"), never "aplicación".
- The app has no strings for "Templates", "Bulk Import", "Panorama", "Realistic / Clay / UI Only" or "Metal". The site's "device models" has no UI string; the closest are `Devices` / `Device Style` / `Model`.

### Glossary

| English term on site | English UI string (key) | Spanish UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Upload to App Store Connect | `Upload to App Store Connect` | Subir a App Store Connect | button; M4 |
| App Store Connect credentials | `App Store Connect Credentials` | Credenciales de App Store Connect | settings section; `API Credentials` → "Credenciales de API"; `Delete Credentials` → "Eliminar credenciales" |
| Issuer ID / Key ID / .p8 key | `Issuer ID` / `Key ID` / `Import .p8 File` | ID del emisor / ID de la clave / Importar archivo .p8 | |
| API key (bring your own) | `API Key` / `Own API Key` | Clave API / Clave API propia | |
| AI translation | `AI Translation` | Traducción con IA | feature name |
| AI Translate (button) | `AI Translate` | Traducir con IA | |
| Translate All | `Translate All` | Traducir todo | |
| Bulk translations | `Bulk Translations` | Traducciones masivas | |
| AI integration | `AI Integration` | Integración de IA | |
| Provider | `Provider` / `Default Provider` | Proveedor / Proveedor predeterminado | OpenAI, Anthropic, Google are not in the catalog as strings |
| Localization panel | `Localizations` | Localizaciones | |
| Languages / locales | `Languages` / `Target Languages` / `Source Language` | Idiomas / Idiomas de destino / Idioma de origen | the app says "idiomas", not "locales" |
| Add language | `Add Language` / `Add All (%lld)` | Añadir idioma / Añadir todos (%lld) | |
| Linked to source | `Linked to source` / `Changes follow %@` | Vinculado al origen / Los cambios siguen a %@ | the site's "link-to-source switch" |
| Device models | `Devices` / `Device Style` / `Model` | Dispositivos / Estilo del dispositivo / Modelo | |
| Artboard | `Artboard` / `Artboards` | Mesa de trabajo / Mesas de trabajo | Adobe's Spanish term |
| Export | `Export` / `Export %lld Artboards` | Exportar / Exportar %lld mesas de trabajo | |
| Save images | `Save Images` | Guardar imágenes | |
| Text overlays / captions | `Text Block` / `Text Blocks` | Bloque de texto / Bloques de texto | the app's own word for captions; tab `Text Editing` → "Edición de texto" |
| Copy Style | `Copy Style` | Copiar estilo | |
| Auto-apply screenshots | `Auto-apply screenshots to devices across all pages and languages.` | Aplica automáticamente las capturas de pantalla a los dispositivos en todas las páginas e idiomas. | the app has no "Bulk Import" string; the folder link is `Link a folder of images` → "Vincular carpeta de imágenes" |
| CSV import/export | `Import CSV` / `Export CSV` | Importar CSV / Exportar CSV | |
| Do not translate | `Do not translate` | No traducir | per-block flag |
| Pages | `Pages` / `Page` | Páginas / Página | |
| Layers | `Layers` | Capas | |
| Background | `Background` | Fondo | |
| Gradient | `Gradient` | Degradado | |
| Shadow | `Shadow` | Sombra | |
| Border / Corner radius | `Border` / `Corner Radius` | Borde / Radio de las esquinas | |
| Camera / Lighting | `Camera` / `Lighting` | Cámara / Iluminación | |
| Perspective / Orthographic | `Perspective` / `Orthographic` | Perspectiva / Ortográfica | `Projection` → "Proyección" |
| Rotation / Scale / Offset | `Rotation` / `Scale` / `Offset` | Rotación / Escala / Desplazamiento | |
| Device overflow | `Device Overflow` | Desbordamiento de dispositivo | |
| New Project | `New Project` | Nuevo proyecto | |
| macOS Keychain | `Translation credits never expire. Your API key is stored in the macOS Keychain.` | Los créditos de traducción no caducan nunca. Tu clave API se guarda en el llavero de macOS. | Keychain = "llavero" |
| Translation packs (IAP) | `Translation Packs` / `Translation Credits` | Packs de traducción / Créditos de traducción | M2; `Buy More` → "Comprar más" |
| Restore Purchases | `Restore Purchases` | Restaurar compras | |
| Powered by Claude | `Powered by Claude for high-quality screenshot localization.` | Con tecnología Claude para una localización de capturas de alta calidad. | |
| Templates | no UI string | no UI string | |
| Render styles (Realistic, Clay, UI Only) | no UI string | no UI string | |
| Percentage-based layout | no UI string | no UI string | |

Paid tier names: Mockly is a paid app (one-time), with no tiers. The only purchase UI is the translation-pack sheet: "Packs de traducción", "Comprar más", "Restaurar compras", "Packs únicos. Sin suscripciones. Hecho para desarrolladores." Also: "Usa tu propia clave API o desbloquea traducción con IA al instante con un pack único. Sin suscripciones." No free trial.

### Spanish App Store listing (https://apps.apple.com/es/app/id6756589122, read 2026-11-19)

- Name: **Mockly: Screenshot Maker** (not localized; same as English; no space before the colon)
- Subtitle: **50 idiomas, un clic** (English "50 Languages, One Workflow"; M3)
- Category: **Para desarrolladores** (English "Developer Tools")
- Price: **14,99 €** (paid app; US $12.99). No in-app purchases listed.
- Idiomas: "Español y 8 más" (9 listed)
- Compatibility: "Requiere macOS 14.0 o posterior." (Mac only). Size 34,9 MB.
- Description register: tú (15 hits, 0 usted).

---

### 2. Observa (`observa`, source `HealthLogger/`, ID 6757438990)

### Spanish coverage

- Main `HealthLogger/Localizable.xcstrings`: 6684 keys, all 6684 with an `es` value, 6672 state translated or plural variations (99.8%). 12 are `needs_review` (all `insight_signal_*`, values present, e.g. `insight_signal_morning_hrv` → "VFC matutina"). 41 languages; `es`, `es-MX` and `es-419` all exist.
- Watch `ObservaWatch/Localizable.xcstrings`: 477/477. Widgets `ObservaWidgets/Localizable.xcstrings`: 403/403.
- `AppShortcuts.xcstrings`: 15 keys, all with an `es` value: 9 translated, 3 `needs_review` single strings ("Log my ${applicationName} morning check-in" → "Registrar mi control matinal en ${applicationName}", "What was my ${applicationName} sleep score?" → "¿Cuál fue mi puntuación de sueño en ${applicationName}?", "What's my ${applicationName} readiness?" → "¿Cuál es mi preparación en ${applicationName}?"), and 3 `stringSet` phrases with two spoken variants each (two of them `needs_review`: "Log water in ${applicationName}" → "Registrar agua en ${applicationName}" / "Anotar agua en ${applicationName}", "Should I train today in ${applicationName}?" → "¿Debería entrenar hoy según ${applicationName}?" / "¿Debo entrenar hoy en ${applicationName}?"). Spanish Siri works, partly unreviewed.
- `InfoPlist.xcstrings` app 5/5 and watch 5/5 in Spanish, including `NSHealthShareUsageDescription` ("Observa lee tus datos de salud para mostrar información sobre el sueño, el corazón, la actividad y la recuperación. Todos los datos se procesan en tu dispositivo y nunca se suben."), `NSHealthUpdateUsageDescription`, `NSSiriUsageDescription` ("…registrar la hidratación o tu registro matutino con la voz.").
- Register: **tú.** 1522 strings with tu/tus/te/ti/puedes/tienes…, 370 that start with a tú imperative, 0 usted. 26 `su/sus` hits are all third-person objects (the Apple Watch's sensor, "su ritmo"). No vosotros, no vos. Latin-American vocabulary: `agregar` 5 and `agrega` 1 against about 60 `añadir/añade/añaden` (Spain form); "manejar" 2, "celular" 1 (in "función celular", i.e. cellular, fine).
- **Verdict: app is in Spanish: yes** (all user-visible parts; 12 insight labels and 6 Siri phrases flagged needs_review).

**How the Spanish UI labels HRV:** **"VFC"** (keys `HRV`, `metric_label_hrv` → "VFC"; about 206 strings). The long form is **"Variabilidad de la frecuencia cardíaca"** (`Heart Rate Variability`). The English acronym **"HRV" survives in 18 strings** ("Sueño, frecuencia cardíaca y HRV", "Desbloquea HRV Trends", all five Home Screen widget labels `widget.title.hrv`, `widget.metric.hrv`, `widget.factor.hrv` → "HRV", and the "Tu HRV del sueño de %lld ms…" insight sentences). The App Store description also says "tu HRV". There is no short "VFC (SDNN)" label in the app. SDNN appears only in explanatory sentences: "La desviación estándar de los intervalos NN (SDNN) refleja tu variabilidad cardíaca general desde todas las fuentes: simpáticas y parasimpáticas." RMSSD and pNN50 stay as they are on the ECG path ("RMSSD y pNN50 derivados del ECG") and in the autonomic-balance sentence ("proporción RMSSD/SDNN"). House rule: Apple Health HRV is SDNN, never RMSSD. For the site: write "VFC (SDNN)" for the Apple Health value, and "HRV" only if the site decides to keep the English acronym (the store description and widgets do).

Flags
- **O1 (tier name):** the Spanish app says **Premium** everywhere (paywall, Watch "Observa Premium lo desbloquea. Abre Observa en tu iPhone.", widgets "Requiere Observa Premium", "Se requiere Premium"), and the store IAPs are "Premium anual/mensual/compra única". The English site says "Pro". The Spanish page needs "Premium". Only one string says "Pro" ("Modo Pro", unrelated).
- **O2 (readiness):** `Readiness` → "Preparación" (about 151 strings: tab, score, Siri, widgets), `Readiness Score` → "Puntuación de preparación". But `Moderate Readiness` → "Disposición moderada" (an inconsistent synonym) and "disponibilidad" in 4 strings. Use "preparación".
- **O3 (baseline):** `Baseline` → "Línea base" (149 strings), but "referencia" in about 55 (`Above Baseline` → "Por encima de la referencia", "Por encima de tu referencia para este período", "bandas de referencia"). Pick "línea base".
- **O4 (resting heart rate):** "Frecuencia cardíaca en reposo" (57), "FC en reposo" (52) and "FCR" (29, the `RHR` key). The English "bpm" is "lpm" in 42 strings, but one string says "brpm" → "rpm" for breaths per minute.
- **O5 (weekly reflection):** `Weekly Reflection` → "Reflexión semanal"; `Unlock Weekly Reflections` → "Desbloquea reflexiones semanales". Consistent.
- **O6 (check-in):** `Morning Check-In` → "Control matinal" (7 strings), but the Watch complication `watch.complication.checkIn.title` → "Registro" ("Tu registro matutino, a un toque.") and the Siri permission text says "tu registro matutino". Same thing, two words. Pick "control matinal".
- **O7 (patterns):** tab `Patterns` → "Patrones" (328 strings with "patrones"); "tendencias" is `Trends`.
- **O8 (English left in a button):** `Unlock Lifetime Access` → "Desbloquea Lifetime Access" and `Unlock HRV Trends` → "Desbloquea HRV Trends" (English product names kept). The onboarding paywall uses "Desbloquear acceso de por vida". Also the imperative form is mixed: "Desbloquear Premium" (infinitive) vs "Desbloquea Lifetime Access" (tú imperative).
- **O9 (best value):** `Best Value` and `Best value` → "Mejor valor"; `pricing_label_yearly` → "Anual (mejor valor)". Consistent here, but a calque ("mejor relación calidad-precio" is the idiomatic form).
- **O10 (missing accents, real defect):** the string `Your Sleep Quality score is built from four factors:…` has Spanish with no accents, no inverted question marks: "Tu puntuacion de Calidad del Sueno se basa en cuatro factores: Continuidad (35%) Que tan ininterrumpido fue tu sueno? Profundidad y eficiencia (25%) Realmente estabas durmiendo? Restauracion (30%) Se recupero tu cuerpo? Consistencia (10%) Dormiste a tu hora habitual?" (`es-MX` has the same text). Also `Your VO₂ Max indicates excellent aerobic fitness…` → "VO₂ Max indica excelente condicion aerobica con capacidad superior." (missing accent, shortened, drops "above-average cardiovascular capacity and strong heart health").
- **O11 (English left in):** four `VO₂ max …` explanation strings (keys that start `VO₂ max combines lung capacity…`, `VO₂ max is used in research…`, `VO₂ max naturally declines with age…`, `VO₂ max represents the maximum amount of oxygen…`) have an `es` value identical to the English.
- **O12 (store subtitle vs app):** the store subtitle says "Puntaje" (Latin-American); the app says "puntuación" everywhere (125 strings, 0 "puntaje").
- **O13 (add verb):** "agregar/agrega" (6 strings) next to "añadir/añade" (about 60). Spain form is "añadir".
- `ECG` → "ECG". `Cycle Context` → "Contexto del ciclo", `Menstrual Cycle` → "Ciclo menstrual". The Spanish store subtitle says "Ciclo". The English site page does not cover cycle tracking: fact gap to check (same as in the German and French glossaries).
- The ES storefront lists a tip IAP "Apoyar al desarrollador" (1,00 €).
- `Moderate Debt` → "Déficit moderado" while `Sleep Debt` → "Deuda de sueño" (same concept, two words).

### Glossary

| English term on site | English UI string (key) | Spanish UI string (verbatim) | Note |
|---|---|---|---|
| Tab: Sleep | `Sleep` | Sueño | tab bar: Sleep, Recovery, Heart, Patterns, More |
| Tab: Recovery | `Recovery` | Recuperación | |
| Tab: Heart | `Heart` | Corazón | |
| Tab: Patterns | `Patterns` | Patrones | O7 |
| Tab: More | `More` | Más | |
| HRV | `HRV` / `metric_label_hrv` | VFC | no "(SDNN)" label, see note above; "HRV" left in 18 strings |
| Heart rate variability | `Heart Rate Variability` | Variabilidad de la frecuencia cardíaca | |
| ECG-derived RMSSD & pNN50 | `ECG-derived RMSSD & pNN50` | RMSSD y pNN50 derivados del ECG | ECG path only |
| ECG | `ECG` / `ECG Recording` / `ECG Analysis` | ECG / Grabación de ECG / Análisis de ECG | |
| Autonomic balance | `Autonomic Balance` | Equilibrio autónomo | |
| Sinus rhythm | `Sinus Rhythm` | Ritmo sinusal | |
| Readiness | `Readiness` | Preparación | O2 |
| Readiness score | `Readiness Score` | Puntuación de preparación | |
| Sleep Score | `Sleep Score` | Puntuación de sueño | |
| Recovery score | `recovery score` | puntuación de recuperación | `insight_signal_recovery_score` → "Puntuación de recuperación" (needs_review) |
| Training call | `Should I train today?` | ¿Debería entrenar hoy? | `${applicationName} training call` (Siri) → "Recomendación de entrenamiento de ${applicationName}"; Siri phrase "¿Puedo entrenar hoy según ${applicationName}?" |
| Resting heart rate | `Resting Heart Rate` / `RHR` | Frecuencia cardíaca en reposo / FCR | O4 |
| Sleep efficiency | `Sleep Efficiency` | Eficiencia del sueño | |
| Sleep stages | `Sleep Stages` | Fases del sueño | |
| Deep sleep / REM | `Deep Sleep` / `REM Sleep` | Sueño profundo / Sueño REM | |
| Sleep debt | `Sleep Debt` | Deuda de sueño | |
| Heart-rate dip | `Nocturnal Dip` | Descenso nocturno | |
| Heart rate recovery | `Heart Rate Recovery` | Recuperación de frecuencia cardíaca | |
| Stress | `Stress` | Estrés | |
| Today's Plan | `Today's Plan` | Plan de hoy | |
| Functional Age | `Unlock Functional Age` | Desbloquear edad funcional | label "edad funcional" |
| Chronotype | `Chronotype Analysis` | Análisis de cronotipo | `chronotype_intermediate` → "Cronotipo intermedio" |
| Training load | `Training Load` | Carga de entrenamiento | |
| Strain | `Strain` | Esfuerzo | `insight_signal_strain` → "Esfuerzo de entrenamiento" (needs_review) |
| Workouts | `Workouts` | Entrenamientos | |
| Energy | `Energy` / `Active Energy` | Energía / Energía activa | |
| Personal baseline | `Baseline` / `Your baseline` | Línea base / Tu línea base | O3 |
| Confidence | `Confidence` | Confianza | |
| Patterns / correlations | `Correlation strength (r)` | Fuerza de correlación (r) | |
| Insight cards | `Daily insights` / `Insights` | Análisis diarios / Análisis | the app says "análisis", not "perspectivas" |
| Weekly reflection | `Weekly Reflection` | Reflexión semanal | O5 |
| Long-term trends | `Long-Term Trends` | Tendencias a largo plazo | |
| Morning check-in | `Morning Check-In` | Control matinal | O6 |
| Hydration | `Hydration` | Hidratación | |
| Apple Watch complications | `watch.complication.*.title` | Registro / Hidratación / Métrica / Hoy / ¿Entreno hoy? | descriptions: "Tu registro matutino, a un toque.", "El agua de hoy frente a tu objetivo.", "Entrenar hoy o no, de un vistazo." |
| Apple Health | `Apple Health` (in sentences) | Apple Health | the app keeps the English product name (72 strings), never "Salud" |
| Premium tier | `Premium` / `Upgrade to Premium` / `Unlock Premium` | Premium / Actualizar a Premium / Desbloquear Premium | O1 |
| Monthly / Yearly / Lifetime | `Monthly` / `Yearly` / `Lifetime` | Mensual / Anual / De por vida | |
| Unlock lifetime | `Unlock Lifetime Access` / `onboarding_paywall_lifetime_cta` | Desbloquea Lifetime Access / Desbloquear acceso de por vida | O8 |
| Start free trial | `Start Free Trial` / `Start %@ Free Trial` | Iniciar prueba gratuita / Iniciar %@ de prueba gratis | |
| Start plan | `Start Yearly Plan` | Iniciar plan anual | |
| Restore Purchases | `Restore Purchases` | Restaurar compras | |
| Free | `Free` | Gratis | free tier: "el nivel gratuito" |
| Best value | `Best Value` / `Best value` | Mejor valor | O9 |

Paid tier names as the Spanish UI shows them: **Premium** (Watch and widgets too), **Mensual / Anual / De por vida**, "Mejor valor", "Desbloquear Premium", "Actualizar a Premium", "Restaurar compras", "Iniciar prueba gratuita". Premium is unlocked for the first week ("Tu semana gratis de acceso completo ya se usó en este dispositivo. El nivel gratuito sigue incluyendo puntuaciones diarias y tendencias de 7 días.").

### Spanish App Store listing (https://apps.apple.com/es/app/id6757438990, read 2026-11-19)

- Name: **Observa: VFC y Recuperación** (English "Observa: HRV & Recovery Score"; no space before the colon)
- Subtitle: **Sueño, Ciclo, Coach & Puntaje** (US subtitle not verified (429); the French glossary read "Readiness, Sleep & Cycle Coach" on 2026-11-07)
- Category: **Salud y forma física** (English "Health & Fitness")
- Price: Gratis. In-app purchases as shown: Premium anual **24,99 €**, Premium mensual **3,99 €**, Premium compra única **59,99 €**, Apoyar al desarrollador **1,00 €**
- Idiomas: "Español y 33 más"
- Compatibility: iOS 17.6, iPadOS 17.6, macOS 14.6 (M1), visionOS 1.3, watchOS 10.0. Size 92,7 MB.
- Description register: tú (30 hits, 0 usted). It uses "HRV" and "Preparación".

---

### 3. Pawza (`pawza`, source `PetCare/`, ID 6773507068)

### Spanish coverage

- `PetCare/Localizable.xcstrings`: 1323 keys, 1322 with `es`, all translated (99.9%; 1317 plain, 5 plural variations). Missing: only the format-only key `%@`. 50 languages; `es` and `es-MX` exist. The widget target shares this catalog (no catalog of its own).
- `AppShortcuts.xcstrings`: 4/4, e.g. "Registrar cuidado de ${pet} en ${applicationName}", "Registrar el ánimo de ${pet} en ${applicationName}", "Registrar ${kind} en ${applicationName}", "Registrar cuidado en ${applicationName}".
- **No `InfoPlist.xcstrings`.** The camera and photo-library permission texts are `INFOPLIST_KEY_NSCameraUsageDescription` / `INFOPLIST_KEY_NSPhotoLibraryUsageDescription` build settings in English only ("Pawza uses your camera to scan vet documents and take photos of your pets.", "Pawza needs photo access to import pictures of your pets and their documents."). The project's known regions include `es` and `es-MX`, so Spanish users see the permission prompts in English.
- Register: **tú.** 97 strings with tu/tus/te/ti…, 84 that start with a tú imperative ("Añade tu primera mascota para empezar a seguir su salud.", "Importa tu primera foto…"). One `usted` regex hit ("Guarda cada foto suya") is third person. No vosotros, no vos. No Latin-American vocabulary ("móvil" 3, "teléfono" 10 are fine).
- **Verdict: app is in Spanish: yes** (permission prompts in English from build settings).

Flags
- **P1:** permission texts not localized (see above). Same defect as in German and French.
- **P2 (scan):** "escanear/escaneo" throughout (29 strings), no "digitalizar" anywhere. Consistent. `Scan` → "Escanear".
- **P3 (records vs sheet):** `Records` → "Registros" (91 strings with "registro"), but the sitter document is a "Ficha del cuidador" and the English "health record" is "registro de salud". "Cartilla" (the store name's "Cartilla Animal") appears in only one UI string ("cartilla de vacunación").
- **P4 (accounts):** "free accounts" wording from the French glossary does not occur in Spanish; the free tier is "Gratis" / "Pro". Check the site: the app has no accounts.
- **P5 (best value):** `Best value` → "Mejor opción" (Observa, RightSplit and Shogiful say "Mejor valor").
- **P6 (upgrade verb):** `Upgrade to Pawza Pro` → "Mejora a Pawza Pro" (tú imperative) next to `Unlock Pawza Pro` → "Desbloquear Pawza Pro" (infinitive).
- **P7 (mood):** `Mood` → "Ánimo" (short for "estado de ánimo"); 5 strings.
- **P8 (settings word):** "Ajustes" 13, "Configuración" 2 (both mean settings).
- `Start 7-day free trial` → "Comenzar prueba gratuita de 7 días" (Observa and Shogiful say "Iniciar prueba gratuita"); banner "7 DÍAS DE PRUEBA GRATIS".

### Glossary

| English term on site | English UI string (key) | Spanish UI string (verbatim) | Note |
|---|---|---|---|
| Tab: Pets | `Pets` | Mascotas | tabs: Pets, Reminders, Settings |
| Tab: Reminders | `Reminders` | Recordatorios | |
| Tab: Settings | `Settings` | Ajustes | P8 |
| Pet / Add pet | `Pet` / `Add Pet` | Mascota / Añadir mascota | |
| Health records | `Records` | Registros | P3 |
| Vaccinations | `Vaccinations` / `Vaccines` | Vacunas / Vacunas | both keys give "Vacunas" |
| Medications | `Medications` / `Medication` | Medicamentos / Medicamento | |
| Doses | `Doses` | Dosis | |
| Vet visits | `Vet visits` | Visitas al veterinario | |
| Vet | `Vet` | Veterinario | `Emergency vet` → "Veterinario de urgencias" |
| Weight / weight alerts | `Weight` / `Weight trend alerts` | Peso / Alertas de tendencia del peso | |
| Symptoms | `Symptoms` | Síntomas | `Log Symptom` → "Registrar síntoma" |
| Care log | `Care log` / `Log care` | Registro de cuidados / Registrar cuidado | |
| Walks | `Walks` | Paseos | |
| Mood | `Mood` | Ánimo | P7 |
| Feeding | `Feeding` / `Log food` | Comidas / Registrar comida | `Dry food` → "Pienso" |
| Document scanning | `Scan a vet document` / `Scan` | Escanear un documento del veterinario / Escanear | P2 |
| Import past records | `Import past records` | Importar registros anteriores | |
| AI auto-fill | `Unlock AI auto-fill` | Desbloquea el autorrelleno con IA | |
| AI summaries | `AI Summaries` / `AI summaries for every record` | Resúmenes con IA / Resúmenes con IA para cada registro | |
| Apple Intelligence | `Apple Intelligence summary` / `Fill with Apple Intelligence` | Resumen de Apple Intelligence / Rellenar con Apple Intelligence | |
| Vet-visit PDF | `Vet Visit PDF` / `Vet visit PDF generator` | PDF de visita al veterinario / Generador de PDF de visita al veterinario | |
| Since last vet visit | `Since last vet visit` | Desde la última visita al veterinario | |
| Emergency Card | `Emergency Card` | Tarjeta de emergencia | `Emergency Info` → "Información de emergencia" |
| Lost Pet Kit | `Lost Pet Kit` / `Lost Pet Poster` | Kit mascota perdida / Cartel de mascota perdida | |
| Sitter Pack | `Sitter Pack` | Ficha del cuidador | `Make a sitter pack` → "Crear la ficha del cuidador" |
| Photo gallery | `Unlimited photo gallery` | Galería de fotos ilimitada | |
| Unlimited pets and scans | `Unlimited pets and scans` | Mascotas y escaneos ilimitados | |
| Free / Pro | `Free` / `Pro` / `Pawza Pro` | Gratis / Pro / Pawza Pro | |
| Unlock Pro | `Unlock Pawza Pro` / `Upgrade to Pawza Pro` | Desbloquear Pawza Pro / Mejora a Pawza Pro | P6 |
| Monthly / Yearly / Lifetime | `Monthly` / `Yearly` / `Lifetime` | Mensual / Anual / De por vida | `Pro (Lifetime)` → "Pro (de por vida)", `Buy Lifetime — %@` → "Comprar de por vida — %@" |
| 7-day free trial | `Start 7-day free trial` | Comenzar prueba gratuita de 7 días | |
| Subscribe | `Subscribe` | Suscribirse | |
| Best value | `Best value` | Mejor opción | P5 |
| Due / Upcoming | `Due` / `Upcoming` | Vence / Próximos | |
| iCloud sync | `iCloud Sync: up to date.` | Sincronización de iCloud: al día. | |
| Syncing with iCloud | `Syncing with iCloud...` | Sincronizando con iCloud… | |
| Restore Purchases | `Restore Purchases` | Restaurar compras | |

Paid tier names as the Spanish UI shows them: **Pawza Pro** (also "Pro"), labels **Mensual / Anual / De por vida**, "Comenzar prueba gratuita de 7 días", "Restaurar compras", "Suscribirse", "Mejor opción". "«%@» es una función Pro" is the lock message.

### Spanish App Store listing (https://apps.apple.com/es/app/id6773507068, read 2026-11-19)

- Name: **Pawza: Salud y Cartilla Animal** (English "Pawza: Pet Health & Records"; no space before the colon)
- Subtitle: **Vacunas, peso y recordatorios** (English "Vaccine Tracker & Reminders")
- Category: **Estilo de vida** (English "Lifestyle")
- Price: Gratis. In-app purchases as shown: Pawza Pro mensual **2,99 €**, Pawza Pro anual **22,99 €**, Pawza Pro compra única **44,99 €** (US: $2.99, $19.99 yearly, $39.99 lifetime)
- Idiomas: "Español y 43 más"
- Compatibility: iOS 17.6 (iPhone), iPadOS 17.6, macOS 14.6 (M1), visionOS 1.3. Size 39,7 MB.
- Description register: tú (20 hits, 0 usted).

---

### 4. RightSplit (`rightsplit`, source `splitit/`, ID 6757268612)

### Spanish coverage

- Main `splitit/Localizable.xcstrings`: 499 keys, all 499 with `es` (491 plain, 8 plural variations; 100%). 40 languages; `es` and `es-MX` exist.
- Widgets `splititWidgets`: 376/376 (33 plural variations). Share extension `splititShare`: 3/3. SplititKit package (`Sources/SplititKit/Resources`): 65/65.
- `InfoPlist.xcstrings`: 5/5 in Spanish: `CFBundleDisplayName` "RightSplit", `CFBundleName` "splitit", camera "RightSplit usa la cámara para escanear recibos de restaurantes y dividir la cuenta.", contacts "RightSplit accede a los contactos para añadir personas al dividir una cuenta.", photo-library add "RightSplit guarda una imagen en la fototeca solo cuando lo elijas."
- Register: **tú.** 64 strings with tu/tus/te/ti…, 56 that start with a tú imperative ("Escanea o toca un método para pagarme.", "Prueba con una foto más clara…"). The 3 `usted` regex hits are the noun "Importe" (amount), not a verb. No vosotros, no vos. The only Latin-American form is "ingresa" (2 strings, see R3).
- **Verdict: app is in Spanish: yes.**

Flags
- **R1 (split verb):** "Dividir/división" is the word throughout (87 strings: `Split by items` → "Dividir por artículos", `Split Receipt` → "Dividir recibo", `Start splitting` → "Empezar a dividir", `Split Complete` → "División completa"). "Compartir" is only the share action (`Share` → "Compartir", `Share RightSplit` → "Compartir RightSplit", `Text / WhatsApp share` → "Compartir por SMS / WhatsApp"). No ambiguity here, unlike French. One string reads "Divide justamente." (`Split fairly.`).
- **R2 (receipt / bill):** `Receipt` → "Recibo" (57 strings), `Bill` → "Cuenta" (the restaurant bill; 22 "cuenta" strings also include the `Split a bill` → "Dividir una cuenta" family). **The store name and description say "ticket"** ("Escanea ticket, gastos grupo", "Escanea el ticket y toca quién tomó qué"), the app says "recibo". In Spain a restaurant "recibo" is unusual; "ticket" is the everyday word. Decide for the site; the app UI says "recibo".
- **R3 (enter verb, Latin-American):** `Try taking a clearer photo with good lighting, or enter items manually.` → "Intenta tomar una foto más clara con buena iluminación,\no ingresa los artículos manualmente." and the matching error text "Prueba con una foto más clara o ingresa los artículos manualmente." "Ingresar" is Latin-American; Spain uses "introduce". Also "Intenta tomar una foto" (calque; Spain "hacer una foto").
- **R4 (tax):** `Tax` → "Impuesto" (1 string). Spanish restaurant bills include IVA; "impuesto" reads generic. Check the Spanish site copy ("impuestos" vs "IVA").
- **R5 (best value):** `Best value` → "Mejor valor" (Pawza says "Mejor opción").
- **R6 (spaces):** `Spaces` → "Espacios" (`New space` → "Nuevo espacio"), consistent. `Trips` → "Viajes". `Pocket Split` → "División exprés".
- `Everyone's settled — no transfers needed.` → "Todos están saldados — no hacen falta transferencias." (em dash in UI; do not copy to the site).
- `Send feedback` and `Send Feedback` → both "Enviar comentarios" (consistent, unlike French).
- `Pro+ restored successfully!` → "¡Pro+ restaurado correctamente!"
- `paypal.me username` → "paypal.me username" and `revolut.me username` are English left in (placeholders; the second is identical to English).
- `owed` → "recibe", `Owed` → "Debe", `owes` → "paga": the labels are fine in context, but `Owed` → "Debe" is the opposite sense as a heading; check where it is shown.

### Glossary

| English term on site | English UI string (key) | Spanish UI string (verbatim) | Note |
|---|---|---|---|
| Scan receipt | `Scan Receipt` | Escanear recibo | R2 |
| Receipts | `Receipts` / `Receipt` | Recibos / Recibo | |
| Receipt language | `Receipt Language` | Idioma del recibo | |
| Item-level splits | `Split by items` | Dividir por artículos | R1 |
| Shared dishes | `Shared dishes` / `Add shared item` | Platos compartidos / Añadir artículo compartido | |
| Equal splitting | `Equal splits & tip` | División igual y propina | R1 |
| Per person | `Per person` / `Adjust per person` | Por persona / Ajustar por persona | |
| Tip | `Tip` / `Tip included` | Propina / Propina incluida | |
| Tax | `Tax` | Impuesto | R4 |
| Subtotal / Total | `Subtotal` / `Total` | Subtotal / Total | |
| Fair rounding | `Round fairly` | Redondear con justicia | |
| Send totals / payment requests | `Send Payment Requests` | Enviar solicitudes de pago | `Payment reminder` → "Recordatorio de pago" |
| Pay-Me card / payment link | `Pay Me` / `Pay-Me Card` | Págame / Tarjeta Pay-Me | |
| Text / WhatsApp share | `Text / WhatsApp share` | Compartir por SMS / WhatsApp | the site says iMessage/WhatsApp |
| Paid | `Paid` | Pagado | |
| Spaces | `Spaces` / `New space` | Espacios / Nuevo espacio | R6 |
| Trips | `Trips` / `Trips & shared expenses` | Viajes / Viajes y gastos compartidos | |
| Balances / settle-up | `Balance` / `Settlement` / `Settle in` | Saldo / Liquidación / Liquidar en | |
| Split history | `History` / `Unlimited split history` | Historial / Historial de divisiones ilimitado | |
| Templates | `Templates` / `Split template` | Plantillas / Plantilla de división | |
| People | `People` | Personas | |
| Currency | `Currency` | Moneda | `Language & Currency` → "Idioma y moneda" |
| Free | `Free` | Gratis | |
| Pro+ | `Pro+` / `Unlock Pro+` / `Upgrade to Pro+` | Pro+ / Desbloquear Pro+ / Mejorar a Pro+ | |
| Pro+ yearly | `Pro+ Yearly` | Pro+ Anual | |
| Pro+ lifetime | `Pro+ Lifetime` / `Unlock Pro+ Lifetime` | Pro+ de por vida / Desbloquear Pro+ de por vida | `Unlock Pro+ — Pay once` → "Desbloquear Pro+ — Pago único" |
| Free trial | `%lld-day free trial` | Prueba gratis de %lld días | |
| Best value | `Best value` | Mejor valor | R5 |
| Restore Purchases | `Restore Purchases` | Restaurar compras | |

Paid tier names as the Spanish UI shows them: **Pro+** (no plain "Pro"), **Pro+ Anual**, **Pro+ de por vida**, "Desbloquear Pro+", "Continuar con Pro+", "Restaurar compras". Auto-renew line: "Se renueva automáticamente cada año hasta que lo canceles." One-time line: "El pago se cargará a tu Apple ID. Esta es una compra única sin cargos recurrentes."

### Spanish App Store listing (https://apps.apple.com/es/app/id6757268612, read 2026-11-19)

- Name: **RightSplit: Dividir y Propina** (English "RightSplit: Bill Splitter Tip"; no space before the colon)
- Subtitle: **Escanea ticket, gastos grupo** (English "Scan & share group expenses"; note "ticket" vs the app's "recibo", R2)
- Category: **Utilidades** (English "Utilities")
- Price: Gratis. In-app purchases as shown: RightSplit Pro+ Compra única **8,99 €**, RightSplit Pro+ anual **4,99 €** (US: $7.99 lifetime, $3.99 yearly)
- Idiomas: "Español y 33 más"
- Compatibility: iOS 17.0, macOS 14.0 (M1), visionOS 1.0 (no iPad listed). Size 18,2 MB.
- Description register: tú (18 hits, 0 usted).

---

### 5. Shogiful (`shogiful`, source `shogi/`, ID 6761656926)

### Spanish coverage

- `Localization/Localizable.xcstrings`: 3751 keys, all 3751 with `es`, all translated (100%). 39 languages; `es` and `es-MX` exist (es and es-MX identical for 3626 of 3751). Most keys are semantic (`tab.play`, `paywall.plan.monthly`), so look up by key, not English text.
- `InfoPlist.xcstrings`: 0/2 (only `CFBundleDisplayName` "Shogiful" and `CFBundleName` "shogi", one language only, no translation needed). The app requests no permissions.
- No extensions or Siri phrases.
- Register: **tú.** 593 strings with tu/tus/te/ti/puedes…, 109 that start with a tú imperative ("Haz un test breve para fijar tu rango kyu/dan y ajustar tu plan diario.", "Sigue jugando para revelar este logro.", "Mantén cada pieza defendida"). The 25 `usted` regex hits are all "suyo/suya" meaning "the opponent's" ("Si el suyo es más corto…"). No vosotros, no vos. No real Latin-American vocabulary: "colocar" (38) is fine in Spain; "presionar/presiona" (6) is used in the sense of applying pressure on a pawn; "descargar" 1 (NNUE file) is correct.
- **Verdict: app is in Spanish: yes.**

**Spanish shogi terms the app uses**
- Pieces (keys `piece.*`): `King` → "Rey", `Rook` → "Torre", `Bishop` → "Alfil", `Gold General` → "General de oro", `Silver General` → "General de plata", `Knight` → "Caballo", `Lance` → "Lanza", `Pawn` → "Peón". In puzzle and lesson prose the generals are shortened: "oro", "plata" ("un oro", "una plata", "oros y plata").
- Promoted pieces: `Dragon` (`piece.rook.promoted`) → "Dragón", `Horse` (`piece.bishop.promoted`) → "Alfil promocionado", `Promoted Knight` → "Caballo promocionado", `Promoted Lance` → "Lanza promocionada", `Promoted Pawn` → "Peón promocionado", `Promoted Silver` → "General de plata promocionado". The tokin shows as "tokin" in lesson text.
- Promotion: `Promotion` → "Promoción" (`tutorial.promotion.title`), `Promote` → "Promocionar" (`promotion.promote`), `Promote?` → "¿Promocionar?", `Keep` → "Mantener" (decline promotion). Body: "Cuando una pieza alcanza el lado opuesto, puedes promocionarla para obtener nuevas capacidades."
- Drops: the word is **"colocación"** (269 strings) and **"colocar"** (68): `Drop Drills` → "Ejercicios de colocación", `Drop Mistake` → "Error de colocación", "Mate por colocación de oro", "Colocar %1$@ en %2$@" (`board.drop.hint`), "Combinaciones de colocación", "Horquilla por colocación", "Clavada por colocación", "Doble de colocación". There is no "drop" or "reintroducir" anywhere. Captured pieces: `Pieces in Hand` → "Piezas en mano" (also "en la mano", 29 strings). Body: "Las piezas capturadas pasan a tu bando. Toca una y luego toca una casilla vacía para colocarla."
- Other rule and game words: `Checkmate` → "Jaque mate", `Check!` → "¡Jaque!", `Draw` → "Tablas", `Resign` → "Abandonar", `Moves` → "Jugadas", `Move` → "Jugada", `Board` → "Tablero", `Flip Board` → "Girar el tablero", `Sente` / `Gote` → "Sente" / "Gote" (side = "bando", 39 strings), "nifu" kept as "nifu" (7), `Sennichite — Draw by repetition` → "Sennichite: tablas por repetición", `Handicap` → "Hándicap" (with accent; `Handicap shogi (komaochi)` → "Shogi con hándicap (komaochi)"), `Static Rook` → "Torre estática", `Ranging Rook` → "Torre móvil", `Yagura`, `Mino`, `Anaguma` kept, `Castle` → "castillo" (149 strings), `Fork` → "horquilla" (43), `Pin` → "clavada" (25), `Skewer` → "enfilada", `Hanging Piece` → "Pieza colgada", `Interpose` → "Interposición".
- Names of Japanese concepts stay Japanese: "tsume" lowercase without accent (46 strings, 0 "tsumé"), "joseki" (14) and "jōseki" with macron (6), "tesuji", "yose", "komaochi", "kyu/dan".

Flags
- **S1 (opponents):** the code has 8 `OpponentTier` levels: Novice → "Novato", Beginner → "Principiante", Casual → "Casual", Club Player → "Jugador de club", Intermediate → "Intermedio", Advanced → "Avanzado", Expert → "Experto", Master → "Maestro". The Spanish store description says "SUBE UNA ESCALERA DE 40 RIVALES" and "501 problemas tsume" (the site says 40 opponents too); check the 40 against the blueprint.
- **S2 (rating words, three values):** `Estimated Rating` → "Puntuación estimada" (`progress.estimatedRating`, `progress.rating`) but "Nivel estimado" (`gc.leaderboard.estimated_rating.title`, achievements "Alcanza un nivel estimado de 1000", "Nivel 1000"), and the dashboard tile `Rating` → "Puntuación". "Elo" appears as "ELO" (`%lld ELO · %@`). Kyu/dan rank is "rango" (`Your rank` → "Tu rango", `dashboard.progression.title`), `Kyu / Dan ladder` → "Escala kyu/dan". Pick "puntuación" or "nivel" for the site (the English site says rating).
- **S3 (horse):** the app calls the promoted bishop "Alfil promocionado" in the piece list, but explanatory text says "El alfil promocionado (caballo, 馬)" and puzzle titles "Colocación que neutraliza un caballo o dragón encaramado" where "caballo" means the promoted bishop. "Caballo" is also the knight (`piece.knight`). Ambiguous for the reader.
- **S4 (joseki spelling):** "joseki" (14) vs "jōseki" with macron (6): `module.josekiLab.title` → "Laboratorio de jōseki", `explanation.josekiInaccuracy.1.summary` → "Desviación del joseki", `gc.achievement.joseki.title` → "Estudiante de joseki".
- **S5 (positioning):** `skill.positioning` → "Posicionamiento" (same in four key families). The English site uses it as a skill name; consistent.
- **S6 (International):** the "Western" piece set is called "Internacional" (`settings.pieceSet.western`, `onboarding.style.international`); the setting is "Estilo de piezas" (`settings.pieceSet`, `settings.pieceStyle`).
- **S7 (best value):** `BEST VALUE` (`paywall.bestValue`) → "MEJOR VALOR" (a calque; Observa and RightSplit use "Mejor valor" too).
- **S8 (Family Sharing):** the app uses Apple's Spain term **"En familia"** ("Premium mediante En familia", "Compatible con En familia", "Para configurar En familia, abre Ajustes → ID de Apple → En familia en tu iPhone o iPad."). The master says Family Sharing is a product fact; write "En familia" (the name of the Apple feature in Spanish).
- **S9 (Dashboard tab):** `tab.dashboard` → "Inicio" (not "Panel").
- **S10 (cosmetic):** "oros y plata" (plural/singular mix) in `concept.anaguma-castle.body`; "Colocación de oro que golpea al alfil promocionado" for the English "Gold drop hitting the horse".
- Tsume title: `Tsume-Shogi: Forced Checkmate` → "Tsume: el jaque mate forzado". `Tsume Trail` → "Recorrido tsume".
- `Premium Lifetime` → "Premium de por vida" matches the store IAP name "Premium de por vida".
- `Go deeper` → "Profundiza más" (`paywall.hero.deepAnalysis.title`); the app has no "Deep Analysis" label. No "skill radar" label either; `Your skill profile` → "Tu perfil de habilidades".
- Apostrophe check: this catalog uses straight and typographic quotes inconsistently; Spanish quotes use « » ("«casi del todo»").

### Glossary

| English term on site | English UI string (key) | Spanish UI string (verbatim) | Note |
|---|---|---|---|
| Tab: Dashboard | `Dashboard` (`tab.dashboard`) | Inicio | S9 |
| Tab: Play | `Play` (`tab.play`) | Jugar | |
| Tab: Analysis | `Analysis` (`tab.analysis`) | Análisis | |
| Tab: Training | `Training` (`tab.training`) | Entrenamiento | |
| Tab: Progress | `Progress` (`tab.progress`) | Progreso | |
| Premium | `Shogiful Premium` (`settings.premium.name`) | Shogiful Premium | |
| Premium · Monthly | `Premium Monthly` (`paywall.plan.monthly`) | Premium mensual | |
| Premium · Annual | `Premium Yearly` (`paywall.plan.yearly`) | Premium anual | |
| Lifetime | `Premium Lifetime` (`paywall.plan.lifetime`) | Premium de por vida | matches the store IAP name |
| Upgrade | `Upgrade to Premium` (`settings.premium.upgrade`) | Pasar a Premium | `Premium Active` → "Premium activo", `Free Plan` → "Plan gratuito" |
| Family Sharing | `Premium via Family Sharing` (`settings.premium.familyShared.title`) | Premium mediante En familia | S8 |
| Best value | `BEST VALUE` (`paywall.bestValue`) | MEJOR VALOR | S7 |
| Start free trial | `Start Free Trial` (`paywall.startTrial`) | Iniciar prueba gratuita | `paywall.trial.compound.format` → "Prueba gratuita de %lld días" |
| Tsume-shogi | `Tsume-Shogi: Forced Checkmate` (`concept.tsume-basics.title`) | Tsume: el jaque mate forzado | S4 |
| Tsume Trail | `Tsume Trail` (`module.tsumeTrail.title`) | Recorrido tsume | |
| Drop Drills | `Drop Drills` (`module.dropDrills.title`) | Ejercicios de colocación | drops = "colocación" |
| Castle Atelier | `Castle Atelier` (`module.castleAtelier.title`) | Taller de castillos | |
| Joseki Lab | `Joseki Lab` (`module.josekiLab.title`) | Laboratorio de jōseki | S4 |
| Tesuji / Yose | `Tesuji Cards` / `Yose Trainer` | Tarjetas tesuji / Entrenador yose | |
| Daily plan / assessment | `Daily Plan` / `Skill Assessment` | Plan diario / Test de nivel | |
| Lessons | `Lessons` (`hub.lessons.title`) | Lecciones | |
| Handicap play | `Handicap` (`kif.import.preview.handicap`) | Hándicap | `Komaochi` → "Komaochi"; "Shogi con hándicap (komaochi)" |
| Game review | `Game Review` (`analysis.review.title`) | Revisión de partida | `Review Game` → "Revisar partida" |
| Deep analysis | `Go deeper` (`paywall.hero.deepAnalysis.title`) | Profundiza más | the app has no "Deep Analysis" label |
| Engine | `Engine ready` | Motor listo | "motor"; `YaneuraOu` stays |
| Western / kanji piece sets | `International` / `Traditional (Kanji)` | Internacional / Tradicional (kanji) | S6 |
| Piece style setting | `Piece Style` (`settings.pieceSet`) | Estilo de piezas | |
| KIF import | `Import KIF` / `Copy KIF` / `Share KIF` | Importar KIF / Copiar KIF / Compartir KIF | |
| In-game coach | `In-game Coach` | Entrenador en partida | `Coach's tip` → "Consejo del entrenador", `Unlimited Coach` → "Entrenador ilimitado" |
| Today's training | `Today's Training` | Entrenamiento de hoy | |
| Train weaknesses | `Train These Weaknesses` | Entrenar estas debilidades | |
| Estimated rating | `Estimated Rating` | Puntuación estimada | S2 ("Nivel estimado" in Game Center) |
| Accuracy trend | `Accuracy Trend` | Tendencia de precisión | |
| Skill profile | `Your skill profile` | Tu perfil de habilidades | no "radar" string |
| Five skills | `Tactics` / `Defense` / `Positioning` / `Endgame` / `Openings` | Táctica / Defensa / Posicionamiento / Final / Aperturas | |
| Blunder / Mistake / Inaccuracy | `Blunder` / `Mistake` / `Inaccuracy` | Error grave / Error / Imprecisión | |
| Drop mistake | `Drop Mistake` | Error de colocación | |
| Castle weakness | `Castle Weakness` | Debilidad del castillo | |
| Hanging piece | `Hanging Piece` | Pieza colgada | |
| Missed fork | `Missed Fork` | Horquilla perdida | |
| Missed tsume | `Missed Tsume` | Tsume perdido | |
| Passive move | `Passive move — tempo lost` | Jugada pasiva: tempo perdido | |
| Opponent tiers | `Novice`…`Master` (`opponentTier.*`) | Novato, Principiante, Casual, Jugador de club, Intermedio, Avanzado, Experto, Maestro | S1 |
| Kyu / Dan | `Kyu / Dan ladder` | Escala kyu/dan | `Your rank` → "Tu rango" |
| Resign | `Resign` | Abandonar | |
| Promotion prompt | `Promote?` (`promotion.title`) | ¿Promocionar? | buttons "Promocionar" / "Mantener" |
| Pieces in hand | `Pieces in Hand` | Piezas en mano | |
| Checkmate / Check / Draw | `Checkmate` / `Check!` / `Draw` | Jaque mate / ¡Jaque! / Tablas | |
| Restore Purchases | `Restore Purchases` (`paywall.restore`) | Restaurar compras | |
| Manage subscription | `Manage subscription` (`settings.premium.manage`) | Gestionar suscripción | |

Paid tier names as the Spanish UI shows them: **Shogiful Premium** with plans **Premium mensual / Premium anual / Premium de por vida**, "MEJOR VALOR", "Iniciar prueba gratuita", "Restaurar compras", "Gestionar suscripción", "Premium mediante En familia". Trial note: "%@, luego se renueva automáticamente. Cancela cuando quieras." Lifetime note: "El desbloqueo de por vida también se puede compartir: cómpralo una vez y todos los miembros de la familia obtienen Premium." Tips are personal to the buyer ("Las propinas opcionales son personales del comprador (regla de Apple para los consumibles).").

### Spanish App Store listing (https://apps.apple.com/es/app/id6761656926, read 2026-11-19)

- Name: **Shogiful: Ajedrez japonés** (English "Shogiful Learn & Analyze Shogi"; no space before the colon)
- Subtitle: **Shogi: táctica y análisis IA** (English "Japanese Chess Tactics Trainer")
- Category: **Juegos de mesa** (English "Board")
- Price: Gratis. In-app purchases as shown: Premium mensual **1,99 €**, Premium anual **9,99 €**, Premium de por vida **22,99 €**, Mecenas **5,99 €**, Gran apoyo **9,99 €**, Un café **1,99 €** (US: Supporter $4.99, Huge Support $9.99, Coffee $1.99; lifetime $19.99)
- Idiomas: "Español y 32 más"
- Compatibility: iOS 18.0, iPadOS 18.0, macOS 15.0 (M1), visionOS 2.0. Size 149 MB.
- Description register: tú (17 hits, 0 usted). It says "tu entrenador personal de shogi", "501 problemas tsume", "UNA ESCALERA DE 40 RIVALES".

---

## Cross-app terms

| Concept | Value in each app |
|---|---|
| Restore purchases | "Restaurar compras" in all five (consistent) |
| Settings | "Ajustes" in Observa, Pawza, RightSplit, Shogiful (Pawza also "Configuración" in 2 strings) |
| Free | "Gratis" (Observa, Pawza, RightSplit); "Plan gratuito" / "nivel gratuito" for the tier |
| Best value | "Mejor valor" (Observa, RightSplit), "MEJOR VALOR" (Shogiful), "Mejor opción" (Pawza) |
| Lifetime | "De por vida" in UI (Observa, Pawza, RightSplit "Pro+ de por vida", Shogiful "Premium de por vida"); the store IAP names for Observa, Pawza, RightSplit say "compra única" |
| Monthly / Yearly | "Mensual" / "Anual" (all four subscription apps) |
| Free trial | "Iniciar prueba gratuita" (Observa, Shogiful); "Comenzar prueba gratuita de 7 días" (Pawza); "Prueba gratis de %lld días" (RightSplit) |
| Upgrade | "Actualizar a Premium" (Observa), "Pasar a Premium" (Shogiful), "Mejora a Pawza Pro" (Pawza), "Mejorar a Pro+" (RightSplit): four verbs |
| Unlock | "Desbloquear" (infinitive) in most buttons; "Desbloquea" (imperative) in Observa and Pawza |
| Premium tier name | Observa "Premium", Shogiful "Premium", Pawza "Pro" / "Pawza Pro", RightSplit "Pro+" |
| Add | "Añadir" / "añade" (Spain form) everywhere; Observa also "agregar" (6) |
| Score | "puntuación" (Observa, Shogiful dashboard) |
| Scan | "escanear" (Pawza, RightSplit; no "digitalizar") |
| Family Sharing | "En familia" (Shogiful; the only app with the string) |
| Tip | "Propina" (RightSplit); "Propinas" also means Shogiful's tip purchases (store IAP names "Mecenas", "Gran apoyo", "Un café") |
| Apple Health | "Apple Health" (English product name kept, Observa) |
| Coach | "Entrenador" (Shogiful), "Coach" in Observa's store subtitle |
| Training | "Entrenamiento" (Observa, Shogiful) |
| Locale code | `es` in four apps; **`es-ES` in Mockly** |
| Store title punctuation | no space before the colon in all five Spanish names (unlike French) |

## Flags

App-side string bugs (also belong in ISSUES.md after review by the main session)
1. **Observa, missing accents (O10):** `Your Sleep Quality score is built from four factors:…` has an unaccented Spanish value ("Tu puntuacion de Calidad del Sueno… Que tan ininterrumpido fue tu sueno? … Restauracion… Se recupero…") with no inverted question marks, and `Your VO₂ Max indicates excellent aerobic fitness…` → "VO₂ Max indica excelente condicion aerobica con capacidad superior." The `es-MX` copy has the same defects. App-side fix.
2. **Observa, English left in (O8, O11):** "Desbloquea Lifetime Access", "Desbloquea HRV Trends", four `VO₂ max …` explanation strings identical to English, and "HRV" in 18 strings where the rest of the app says "VFC".
3. **Pawza, permission prompts in English (P1):** camera and photo-library texts are English build settings; there is no `InfoPlist.xcstrings` (project knownRegions include `es`). Same defect in German and French.
4. **Mockly, locale code (M1):** the catalog has `es-ES` and `es-MX` but no `es`; check that it matches your 'es' tooling and Xcode language mapping. The Spanish store page lists no in-app purchases while the app sells translation packs (M2).
5. **RightSplit, "ingresa" (R3) and tax word (R4):** Latin-American "ingresa los artículos" (2 strings) and "Impuesto" where a Spain user expects "IVA".

Register
6. All five apps are **tú**. No tú/usted mix, no vosotros, no vos found. The site writes tú, so quoting UI strings needs no register change. (Contrast with French, where Observa, Pawza and RightSplit were vous.)

Terminology inconsistencies that decide site wording
7. **Observa:** "preparación" (Readiness, 151) vs "Disposición moderada"/"disponibilidad" (5); "línea base" (149) vs "referencia" (55); "control matinal" (7) vs Watch "Registro"; "FC en reposo" / "Frecuencia cardíaca en reposo" / "FCR". HRV: UI "VFC", but "HRV" in 18 strings, widgets and the store description; SDNN only in explanatory sentences. The English site says "Pro"; the Spanish app and store say "Premium".
8. **Shogiful:** rating has three values ("Puntuación estimada", "Nivel estimado", "Puntuación"); "caballo" is both the knight and (in prose) the promoted bishop; "joseki" vs "jōseki"; drops are "colocación"/"colocar", never "drop"; resign is "Abandonar"; promoted bishop is "Alfil promocionado", promoted rook "Dragón"; Family Sharing is "En familia".
9. **RightSplit:** the app says "recibo", the Spanish store name and description say "ticket" (R2). "Dividir" is the split word; "compartir" is only share.
10. **Pawza:** "Registros" for health records vs "Ficha del cuidador" for the sitter document; best value is "Mejor opción" while Observa and RightSplit say "Mejor valor"; "Ánimo" (mood) is a short form.
11. **Cross-app:** four different upgrade verbs and three different free-trial strings (table above); "Desbloquear" vs "Desbloquea". Decide one wording for the site's own paywall-style text, and quote the app string verbatim when the page names an in-app button.

Store listing notes
12. **Mockly's Spanish store name is not localized** ("Mockly: Screenshot Maker"); its Spanish subtitle "50 idiomas, un clic" differs from the US "50 Languages, One Workflow" ("un clic" is a different claim).
13. **Observa's store subtitle uses "Puntaje"** (Latin-American) while the app says "puntuación".
14. **Observa US subtitle not verified (429)**; the French glossary read "Readiness, Sleep & Cycle Coach" on 2026-11-07.
15. The seller name shown on the store pages is the owner's personal name and was not copied anywhere. Prices above are reference only; the master file `MASTER.md` / `MASTER-prices.csv` is the source for prices, platforms, trials and Family Sharing.


---

## Spanish glossary, batch 4: soon, tare, taskful-day, wanderwiki, xiangqiful, clippet

Method. Extracted 2026-11-19, read-only, from each app's string catalogs under `~/Downloads/<source>/` (`.xcstrings` is JSON, parsed with `python3 -I`; worktrees, `.build`, DerivedData and Pods ignored). I counted keys with `shouldTranslate` not false and a non-blank key; a key counts as Spanish only if every `localizations.es` string unit has state `translated` (plural/substitution variations included). Locale code `es` is Spain Spanish; `es-MX` exists separately in the Xiangqiful catalog and was ignored. Spanish values are copied verbatim from the catalogs. No app has `.lproj` folders or JSON localizations. Register counts are strings whose Spanish value contains a tú marker (`tu/tus/te/ti/contigo/tú`) versus usted/ustedes/vos markers, plus a first-word imperative check (Toca/Elige/Añade/Abre versus Toque/Elija/Añada/Abra); usted and vos counts are 0 everywhere, so every app writes **tú** (the apparent "usted" hits of a loose regex were third-person "su/puede/tiene" and were discarded). Counts undercount imperatives but show the split. The Spanish App Store pages were fetched on 2026-11-19 with curl (Safari User-Agent, `Accept-Language: es-ES`) from `https://apps.apple.com/es/app/id<ID>` and read from the raw `serialized-server-data` JSON (lockup title and subtitle, in-app purchase list, languages, category); localized names also cross-checked with `itunes.apple.com/lookup?country=es&lang=es_es`. US pages returned HTTP 429 for Soon., Tare and Taskful Day, so the English subtitles for those three come from the 2026-11-07 French glossary (labelled as such); WanderWiki and Xiangqiful US pages were read live. Prices are reference only (`formattedPrice` and the store page print a non-breaking space U+00A0 before €); the site prints prices from its catalog. The seller's personal name and address appear on the store pages and are deliberately not copied anywhere. Clippet returned HTTP 404 on the es storefront and the lookup API returned no result for either storefront (not released), so its listing section uses the Spanish text prepared in `~/Downloads/clipboard/marketing/aso/` (labelled unpublished).

Cross-app summary:
- Every released app is fully in Spanish (100 % in the main catalogs); only non-user-facing stray keys are missing.
- Register is uniform: **tú** in all six apps, all permission prompts and widget descriptions (0 usted, 0 vos). Safe for a tú site; no register conversion needed when quoting app strings.
- The `es` locale is mostly Spain Spanish ("móvil", "ordenador", "vídeo", "Ajustes", "Añadir", "Gestionar suscripción", "Cuenta atrás", "Archivos") but Soon. and Taskful Day carry Latin-American leftovers ("cuenta regresiva", "Agregar", "Administrar suscripción", "Apple Clima", "Mantén presionado"); details in each section and in Flags.
- "Lifetime" is rendered five ways: "De por vida" (Soon., Taskful Day, WanderWiki, Xiangqiful settings text), "Vitalicio" (Xiangqiful paywall), "Lifetime" left in English (Clippet, one Taskful Day string), "compra única" (store product names for Soon., Taskful Day, WanderWiki), "de por vida" in Clippet's planned store product.
- "Restore purchases" is "Restaurar compras" everywhere (consistent; no "los").
- "Settings" is "Ajustes" everywhere (Spain iOS term).
- "Subscribe/manage": "Gestionar suscripción" in Taskful Day, WanderWiki, Xiangqiful, Clippet; "Administrar suscripción" only in Soon.

---

### 1. Soon. (`soon`, source `countdown/`, ID 6757280643)

### Spanish coverage
| Catalog | keys | `es` translated | % |
|---|---|---|---|
| countdown/Localizable.xcstrings (main app, includes paywall) | 741 | 741 | 100 % |
| countdown/AppShortcuts.xcstrings (Siri and Spotlight phrases) | 13 | 13 | 100 % |
| countdown/InfoPlist.xcstrings | 6 | 5 | 83 % (only the stray key `Soon` is missing; display name, calendar and location permission texts are in Spanish) |
| CountdownWidgets/Localizable.xcstrings | 184 | 182 | 98.9 % (missing only the format strings `%@ ` and `%@ %@`) |

Not in Spanish: nothing user-visible. Widget gallery names stay English by design (`Soon · Ring`, `Soon · Timeline`, `Soon · StandBy`, `Soon · Hero`, `Soon · Dots`, `Soon · Agenda`, `Soon · Clean`, `Soon · Feature`, `Soon · Horizon`, `Soon · Inline`, `Soon · Lock Row`, `Soon · Moment`, `Soon · Month` and the rest of the `Soon · …` names). **Verdict: app is in Spanish: yes.**

### Glossary
| English term on site | English UI string (key) | Spanish UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Home tab | `Home` | Inicio | |
| Plan tab | `Plan` | Plan | |
| Search tab | `Search` | Buscar | verb, not "Búsqueda" |
| Profile tab | `Profile` | Perfil | |
| Plan Mode | `Plan mode reminders` | Recordatorios del modo plan | only UI string naming the mode, so the Spanish name is **modo plan**. No standalone "Plan Mode" label |
| Premium | `Premium` | Premium | `Go Premium` → "Hazte Premium"; `Open Soon. to upgrade to Premium.` → "Abre Soon. para pasar a Premium."; `Premium feature. Double tap to upgrade.` → "Función premium. Toca dos veces para mejorar." (lower-case "premium" there) |
| Free | `Free` | Gratis | |
| Monthly / Annual | `Monthly` / `Yearly` | Mensual / Anual | app says "Yearly", not "Annual"; both give "Anual" |
| Lifetime | `Lifetime` | De por vida | also `One-time purchase` → "Compra única". The store IAP is "Premium compra única" |
| 7-day free trial | `1 week free` / `Free trial` | 1 semana gratis / Prueba gratuita | |
| Restore purchases | `Restore Purchases` | Restaurar compras | |
| Countdown | `Countdown` | Cuenta atrás | FLAG: 22 strings in the main catalog use "cuenta regresiva" / "cuentas regresivas" (Latin-American) against 21 with "cuenta atrás" (Spain), e.g. `Add countdowns` → "Agregar cuentas regresivas", `Add a Countdown` → "Añadir una cuenta atrás". The widgets catalog and the Spanish store listing use "cuenta atrás" only. The site should write "cuenta atrás" |
| Event / moment | `Event` / `Moment` / `Moments` | Evento / Momento / Momentos | both words exist as separate keys (unlike French); `Events` → "Eventos"; `Event Vibe` → "Ambiente del evento" |
| Memories | `Memories` / `Memory` | Recuerdos / Recuerdo | |
| Reminders / event notifications | `Reminders` | Recordatorios | |
| Reflection mode | `Notes` | Notas | no UI string says "Reflection" |
| Daily notes | `Personalized daily notes` / `Weather & daily notes` | Notas diarias personalizadas / Tiempo y notas diarias | `Forecasts and a fresh thought each day` → "Pronósticos y un pensamiento nuevo cada día." |
| Weather | `Weather` / `Weather forecast` / `Smart weather forecast` | Tiempo / Pronóstico del tiempo / Pronóstico del tiempo inteligente | FLAG: attribution strings say "Atribución Apple Clima", "Datos meteorológicos proporcionados por Apple Clima"; "Clima" is the Latin-American name, the Spain app is "Tiempo". Also "Pronóstico" is more Latin-American; Spain says "previsión" (0 uses) |
| Calendar import | `Import from your calendar` / `Turn calendar events into countdowns` | Importar de tu calendario / Convertir eventos del calendario en cuentas regresivas | the second is one of the "regresivas" strings. `Imported from Calendar` → "Importado del calendario" |
| Recurring events | `Recurring countdowns` / `Repeat` | Cuentas regresivas recurrentes / Repetir | |
| Natural language search | `Search` | Buscar | example hints: "“cumpleaños este año” — ventanas de tiempo naturales", "“el verano pasado” — explora recuerdos" |
| Timeline / checklist | `Timeline` / `Checklist` | Cronología / Lista | FLAG: three terms for the timeline: main app "Cronología", widgets "línea de tiempo" (`TIMELINE` → "LÍNEA DE TIEMPO"), suggestions "cronograma" (`We'll suggest a starter checklist and timeline for %@ events.` → "Te sugeriremos una lista inicial y un cronograma para eventos de %@."); the store listing says "línea temporal". Checklist is only "Lista" |
| Themes | `Theme` / `All themes unlocked` | Tema / Todos los temas desbloqueados | theme names are not localized |
| Final Countdown | `Final Countdown` | Cuenta atrás final | |
| Widget styles | `Progress Rings`, `TIMELINE` | Anillos de progreso, LÍNEA DE TIEMPO | gallery names stay English |
| StandBy | `Soon · StandBy` | Soon · StandBy | description: "Una cuenta atrás enorme de mesilla optimizada para el modo StandBy." |
| Lock Screen / Home Screen | `Keep on Lock Screen`; `Your countdown on Home Screen and Lock Screen.` | Mantener en la pantalla de bloqueo; Tu cuenta regresiva en la pantalla de inicio y de bloqueo | FLAG: Lock Screen is "pantalla de bloqueo" in the main app and "pantalla bloqueada" in 5 strings (widgets and the Dynamic Island text, `Remove this countdown from the Lock Screen.` → "Quita esta cuenta atrás de la pantalla bloqueada."). Apple's Spain iOS term is "pantalla de bloqueo" (the store listing uses both) |
| Event types | `Trip` `Wedding` `Birthday` `Anniversary` `Concert` `Baby` `Exam` `Work` `Holiday` `Health` `Sport` | Viaje, Boda, Cumpleaños, Aniversario, Concierto, Bebé, Examen, Trabajo, Festivo, Salud, Deporte | `Holiday` → "Festivo" (public holiday), not "Vacaciones" |
| Baby mode | `Baby` | Bebé | |
| On This Day | `ON THIS DAY` | UN DÍA COMO HOY | `Turn on On This Day reminders in Settings to receive these.` → "Activa los recordatorios de Un día como hoy en Ajustes para recibirlos." |
| Milestone | `Add milestone` | Añadir hito | `Edit Milestone` → "Editar hito" |
| Streak (widget) | `Day streak` / `day streak` | Racha de días / días seguidos | |
| Count up | `days since` / `%lld days since` | días desde / hace %lld días | |
| Pin | `Pin to top` | Fijar arriba | |
| iCloud sync | `iCloud Sync` | Sincronización de iCloud | check against the site claim (on-device and own iCloud); Clippet and Taskful Day say "Sincronización con iCloud" |
| Save | `Save` / `Save moment` | Guardar / Guardar momento | |

Other flags:
- **Latin-American leftovers (Soon. only)**: "Agrega un momento" / "Agrega cuentas regresivas" (9 strings with "Agreg-") against "Añadir/Añade" in 29 others; "Administrar suscripción" (the only app that says it); "Apple Clima"; "cuenta regresiva". Bring the site and quotes to Spain wording.
- Mixed verb forms in Siri phrases: "Añade una cuenta atrás en ${applicationName}", "Crea…", "Abre…", "Muestra…" (tú imperatives) but also "Añadir un momento en ${applicationName}" (infinitive). All are tú-compatible.
- Title-case residue: `Widget Tip` → "Consejo de Widget"; `Tips` → "Consejos" (the tip jar section, `TIP JAR` → "PROPINA").
- Permission prompts (verbatim): calendar "Soon. lee tus eventos del calendario para que puedas convertirlos en cuentas regresivas. No se cambia ni se comparte nada."; location "La ubicación se usa para mostrar pronósticos del tiempo para tus eventos de cuenta regresiva." (another "regresiva" string).
- Premium wording elsewhere: `Manage Subscription` → "Administrar suscripción"; `Purchases Restored` → "Compras restauradas"; `Support the Developer` → "Apoyar al desarrollador"; `One-time tip. Not a subscription.` → "Propina única. Sin suscripción."; `Auto-renews until cancelled.` → "Se renueva automáticamente hasta que se cancele."
- Register: tú. Main app 60 strings with tú pronouns (tu/tus/te/ti), widgets 32, permission prompts 2; imperatives "Añade/Agrega/Toca/Activa/Elige/Quita" (40 main, 19 widgets); 0 usted, 0 vos. No string mixes registers.

### Paid tier names in the Spanish UI
Premium; plan labels Mensual / Anual / De por vida; "Prueba gratuita" and "1 semana gratis"; "Restaurar compras"; "Hazte Premium"; "Administrar suscripción". Store product names: "Premium mensual", "Premium anual", "Premium compra única", "Apoyar al desarrollador".

### Spanish App Store listing (checked 2026-11-19, https://apps.apple.com/es/app/id6757280643)
- Name: **Soon. Días Hasta Eventos** (US: "Soon. - Days Until Big Events", so it differs; no hyphen and "Eventos" capitalized)
- Subtitle: **Boda Viaje y Bebé Cuenta Atrás** (US, from the 2026-11-07 French glossary: "Wedding, Trip & Baby Countdown"; FLAG: no comma between Boda and Viaje, Title Case)
- In-app purchases (reference): `Apoyar al desarrollador 1,00 €` · `Premium compra única 14,99 €` · `Premium mensual 1,99 €` · `Premium anual 9,99 €` (US: $1.00 / $12.99 / $1.99 / $9.99 per the French glossary)
- Languages line: **Español y 35 más**
- Category: **Estilo de vida** (also "Utilidades"; US: Lifestyle / Utilities). Family Sharing: "En familia" listed
- Description (excerpt, store text uses "cuenta atrás", "pantalla bloqueada", "línea temporal", "móvil", "26 widgets", "Dynamic Island"): "Se acerca algo bonito. Soon. lo mantiene a la vista: la fecha que esperas vive en tu pantalla de inicio y en tu pantalla bloqueada…"

---

### 2. Tare (`tare`, source `weightbalance/`, ID 6806255929)

### Spanish coverage
| Catalog | keys | `es` translated | % |
|---|---|---|---|
| weightbalance/Localizable.xcstrings (main app, the only catalog) | 121 | 121 | 100 % |

No InfoPlist.xcstrings and no permission prompts; the display name stays "Tare". **Verdict: app is in Spanish: yes.**

### Glossary
| English term on site | English UI string (key) | Spanish UI string (verbatim) | Note |
|---|---|---|---|
| Chapter I…X | `Chapter %lld` | Capítulo %lld | |
| Unlock / buy chapters | `Open Chapters %lld to %lld` / `Buy Chapters %lld to %lld, %@` / `Buy Chapter %lld, %@` | Abrir los capítulos %1$lld a %2$lld / Comprar los capítulos %1$lld a %2$lld, %3$@ / Comprar el capítulo %1$lld, %2$@ | locked chapters: "Capítulo %lld, no comprado" |
| Unlock text | `%@ more %lld chapters of handcrafted levels. Yours forever.` | %1$@ %2$#@chapters@ más de niveles hechos a mano. Tuyos para siempre. | plural variants "capítulo" / "capítulos". FLAG: the sentence reads "%@ … capítulos más de niveles" (the price placeholder precedes the count); check word order on screen |
| Restore purchases | `Restore purchases` | Restaurar compras | |
| Settings | `Settings` | Ajustes | |
| Hints | `Hints` / `Hint` | Pistas / Pista | |
| Three gold stars | `Marks` | Estrellas | setting is "Marks" in English, "Estrellas" in Spanish; no key says "gold" |
| Sound / Haptics | `Sound` / `Haptics` | Sonido / Vibración | singular "Vibración" |
| High contrast | `High contrast` | Alto contraste | |
| Beam | `Beam %lld` | Barra %lld | **barra** (feminine): "Barra %lld, colgada de la barra %2$lld…". The store listing also says "barras" ("hasta que todas las barras queden en equilibrio"). The arm stays "brazo": `%@ arm, notch %lld` → "Brazo %1$@, muesca %2$lld" |
| Hook / notch | `empty hook` / `notch` | gancho vacío / muesca | `Every hook filled. Not balanced.` → "Todos los ganchos ocupados. Sin equilibrio." |
| Weight | `%@, weight %lld` | %1$@, peso %2$lld | hidden: `hidden %@` → "%@, peso oculto"; `cannot settle, hidden weight` → "no puede estabilizarse, peso oculto". Weights are named by colour and shape (`cobalt kite` → "cometa cobalto", `vermillion disc` → "disco bermellón", `teal drop` → "gota verde azulado", `soot ring` → "anillo hollín", `bone fan` → "abanico hueso", `plum lozenge` → "rombo ciruela", `violet pebble` → "guijarro violeta", `chrome lens` → "lente cromada", `terracotta crescent` → "media luna terracota", `leaf petal` → "pétalo verde hoja") |
| Pans | (no key) | (none) | Tare has no pans; the beams hang from hooks on notches. The only "scale" string is the reference one |
| Picture cards | `Reference scale` | Balanza de referencia | VoiceOver wording ("Balanza de referencia, inclinada, lado izquierdo más pesado."); no UI string says "picture card" |
| Shelf (weights below) | `Tray` / `Return to tray` | Bandeja / Devolver a la bandeja | `%@ returned to the tray.` → "%@ de vuelta en la bandeja." |
| Balanced | `Balanced` / `balanced` | En equilibrio / en equilibrio | `Balanced. Level complete.` → "En equilibrio. Nivel completado." |
| Mobile | `Mobile` | Móvil | the hanging sculpture. FLAG: "móvil" is also the Spanish word for phone (the Soon. and Clippet strings use it that way), so "el móvil" on the site needs a gloss on first use |
| Play | `Play` | Juego | noun, not an action verb |
| Level | `Level %lld` | Nivel %lld | `Level %lld, solved` → "Nivel %lld, resuelto" |
| Restart / Pause / Resume | `Restart level` / `Pause` / `Resume` | Reiniciar el nivel / Pausa / Continuar | `Paused` → "En pausa"; `Exit to grid` → "Volver a la cuadrícula" |
| Chapter names | `The Hang`, `The Secret`, `The Cascade`, `The Exhibition`, `The Ledger`, `The Inventory`, `The Fulcrum`, `The Forgery`, `The Restoration`, `The Retrospective` | El Montaje, El Secreto, La Cascada, La Exposición, Las Cuentas, El Inventario, El Fulcro, La Falsificación, La Reparación, La Antología | in the catalog's order. Title Case in Spanish ("El Montaje" with capital M). "El Fulcro" is a rare word (RAE "fulcro", the lever's point of support); "La Reparación" for "The Restoration" |
| Worlds | `Morning Sky`, `Twilight Meadow`, `Deep Sea`, `Evening Stars`, `Coral Reef`, `Firefly Forest`, `Polar Night`, `Rose Dawn`, `Summer Fields`, `Sunset Hills` | Cielo de la mañana, Pradera del crepúsculo, Mar profundo, Estrellas de la noche, Arrecife de coral, Bosque de luciérnagas, Noche polar, Alba rosada, Campos de verano, Colinas del atardecer | `Canvas` → "Lienzo"; `Automatic, each chapter its own world` → "Automático, cada capítulo con su propio mundo" |
| Share / rate | `Share Tare` / `Rate Tare` | Compartir Tare / Valorar Tare | |
| Terms | `Terms of use` / `Privacy` | Términos de uso / Privacidad | |
| Chapters (IAP) | store product | Capítulos II–X | settled name, see the project rule; matches the store |

Register: tú (4 accessibility hints "Toca dos veces para…", 0 tú pronouns, 0 usted). The unlock text "Tuyos para siempre." is a possessive in tú. Safe for tú.

### Paid tier names in the Spanish UI
There is no tier name: Tare is free with chapter packs. The Spanish UI sells chapters through "Comprar los capítulos %1$lld a %2$lld, %3$@" and "Abrir los capítulos %1$lld a %2$lld", and the unlock text reads "…más de niveles hechos a mano. Tuyos para siempre." The store IAP is named **"Capítulos II–X"**. Locked levels are announced as "Capítulo %lld, no comprado".

### Spanish App Store listing (checked 2026-11-19, https://apps.apple.com/es/app/id6806255929)
- Name: **Tare: Rompecabezas de lógica** (US: "Tare: Balance Logic Puzzle", so it differs; store text also says "puzle")
- Subtitle: **Equilibrio y pesos misteriosos** (US, from the 2026-11-07 French glossary: "Brain Teaser & Hidden Weights")
- In-app purchase (reference): `Capítulos II–X 2,99 €` (US: "Chapters II–X $2.99")
- Languages line: **Español y 43 más**
- Category: **Puzle** (also tagged "Juegos", "Recreativos"; US: Puzzle). Family Sharing: "En familia" listed
- Description terms: "pesos", "barras", "estrellas doradas", "pistas", "niveles hechos a mano" ("Una barra se equilibra cuando peso × distancia es igual en los dos lados"). Matches the app.

---

### 3. Taskful Day (`taskful-day`, source `TaskLogger/`, ID 6757345400; iPhone, iPad, Mac and a Watch target in the source)

### Spanish coverage
| Catalog | keys | `es` translated | % |
|---|---|---|---|
| TaskLogger/Localization/Localizable.xcstrings (main app) | 1427 | 1427 | 100 % |
| TaskfulDayKit Localizable.xcstrings (shared package, Watch strings) | 114 | 112 | 98.2 % (missing `End focus session`, `Extend focus session`) |
| TaskLogger/InfoPlist.xcstrings | 7 | 7 | 100 % (calendar, Reminders, microphone, speech permission texts) |
| TaskLogger/AppShortcuts.xcstrings | 12 | 12 | 100 % |
| TaskLoggerWidgetsExtension Localizable + InfoPlist | 420 + 3 | 420 + 3 | 100 % |
| watch app AppShortcuts.xcstrings | 4 | 4 | 100 % |

Not in Spanish: only the two TaskfulDayKit focus-session strings (they fall back to English). **Verdict: app is in Spanish: yes (two shared-package strings missing).**

### Glossary
| English term on site | English UI string (key) | Spanish UI string (verbatim) | Note |
|---|---|---|---|
| Day Clock | `clock.title`, `pro.feature.clock_view` | Reloj del día | `pro.feature.clock_view.desc` → "Visualiza tu día en un reloj de 24 horas." |
| Energy River | `river.title`, `pro.feature.energy_river` | Río de energía | desc: "Ve tu día como una línea de tiempo que fluye con calma." |
| Day Map | `pro.feature.day_map` | Mapa del día | picker/title `map.title` → "Mapa"; desc "Vista espacial con información sobre la densidad de energía." |
| Focus Orbit / Focus Mode | `pro.feature.focus_orbit` | Modo concentración | FLAG: four terms for focus: the Pro feature "Modo concentración", `focus.enter` "Enfoque", `pad.focus.enter` "Concentrarse", sessions "Sesión de enfoque" / `focus.start` "Iniciar enfoque", insights "Tiempo de enfoque", "Enfoque profundo". No UI string says "Focus Orbit" (the key name only). Needs a decision (enfoque vs concentración) |
| Inbox | `inbox.list.title` / `inbox.title` | Bandeja de entrada / Agregar a la bandeja | FLAG: "Bandeja de entrada" (list title and widget) versus "la bandeja" (empty state "La bandeja está vacía.", "Captura rápida a la bandeja", "Nuevo elemento en bandeja"); watch uses "Bandeja vacía" |
| Today / Tomorrow | `inbox.chip.today` / `inbox.chip.tomorrow` | Hoy / Mañana | `inbox.chip.later` → "Después"; `schedule.next_week` → "Próxima semana" |
| Tabs | `tab.tasks`, `tab.all_tasks`, `tab.analytics`, `tab.settings`, `tab.add` | Tareas, Todas las tareas, Análisis, Ajustes, Añadir | |
| Insights / analytics | `analytics.insights.title` / `pro.feature.analytics` | Insights / Análisis e insights completos | FLAG: English loanword "insights" left in 17 strings ("Tus insights te esperan", "Los insights no están disponibles temporalmente"); the tab is "Análisis". No Spanish term chosen for Insights |
| Journal | `journal.title` | Diario | "Abre el Diario"; entries "Entradas recientes" |
| Mood | `mood.timeline.title` / `journal.mood.prompt` | Ánimo / ¿Cómo te sintió el día? | mood scale: Genial, Bien, Neutral, Estresado. FLAG: "¿Cómo te sintió el día?" is ungrammatical (should be "¿Cómo te fue el día?"). Pattern: "Patrón de ánimo" |
| Workspaces | `pro.feature.workspaces` / `pad.workspace.*` | Múltiples espacios de trabajo / Espacio de trabajo, Todos los espacios, Gestionar espacios… | Pro label "Múltiples espacios de trabajo"; the plain word is "espacio" in Mac/iPad strings |
| Carry forward | `today.carry_forward.title` / `today.carry_forward.button` / `settings.auto_carry_forward.title` / `pad.canvas.carry.title` | Mover a hoy / Mover a hoy / Mover tareas pendientes adelante / Trasladar | FLAG: three verbs for the one feature ("Mover a hoy", "Mover tareas pendientes adelante", "Trasladar automáticamente"; banner "Las tareas pendientes ahora avanzan automáticamente."). `Rollover` → "Reprogramaciones" / "Tasa de reprogramación" |
| Voice capture | `pad.sidebar.voice.a11y` / `voice.create_task` / `pro.feature.voice` | Captura por voz / Crear tarea / Entrada por voz más inteligente | paywall title also "Entrada por voz más inteligente" |
| iCloud sync | `settings.icloud_sync` | Sincronización con iCloud | "Tus tareas permanecen privadas y sincronizadas a través de tu iCloud." |
| Apple Reminders import | `settings.import_reminders` / `pro.feature.reminders` | Importar desde Recordatorios / Reimportar recordatorios | Pro title "Importar desde Recordatorios" |
| Widgets (Pro) | `pro.widgets.unlock_all` / `widget.gallery.pro_widgets` | Desbloquear todos los widgets / Widgets Pro | `widget.gallery.unlock_pro` → "Desbloquea Pro para acceder a todos los widgets." |
| Pro | `pro.paywall.title` / `settings.pro.unlock` | Taskful Day Pro / Desbloquear Pro | consistent "Desbloquear" ("Desbloquea Pro" in the gallery is the same verb) |
| Free | `settings.pro.status.free` / `checklist.pro.limit.description` | Plan gratuito / La versión gratuita incluye 1 elemento por tarea. | FLAG: "plan gratuito" versus "versión gratuita" |
| Monthly / Yearly / Lifetime | `pro.plan.monthly` / `.yearly` / `.lifetime` | Mensual / Anual / De por vida | `pro.buy_lifetime` → "Comprar de por vida"; status "Pro de por vida"; badge `pro.badge.one_time` → "Pago único"; FLAG: `pro.terms.lifetime` → "Lifetime es una compra única. Sin renovaciones." (English word left in) |
| 7-day free trial | `pro.trial.badge` / `pro.start_trial` | Prueba gratuita de 7 días / Iniciar prueba gratuita | `onboarding.trial.subtitle` "Todas las funciones Pro están activas durante tus primeros 7 días — gratis, sin tarjeta." |
| Restore purchases | `pro.restore` | Restaurar compras | |
| Schedule (week grid) | `overview.schedule` / `form.section.schedule` | Agenda / Programación | `Weekly` → "Semanal"; `Next week` → "Semana siguiente"; unscheduled → "Aún sin hora" |
| Overdue / Later | `analytics.overdue` / `inbox.chip.later` | Atrasadas / Después | `Overdue pressure` → "Presión por retrasos"; "Retraso más antiguo" |
| Streak | `analytics.streaks.title` | Rachas | "Racha actual", "Mejor racha" |
| Quick Add | `Quick Add` | Agregar rapido | FLAG: missing accent ("rápido") and "Agregar" (the app otherwise uses "Añadir"); `today.quick_add.placeholder` → "Añadir tarea..." |
| Natural-language capture | `Quickly add a task using natural language` | Añade una tarea rápidamente usando lenguaje natural | placeholder "Describe tu tarea de forma natural, por ejemplo: "Comprar comida mañana prioridad alta"" |

Other flags:
- **Latin-American leftovers**: `inbox.title` "Agregar a la bandeja" and `Quick Add` "Agregar rapido" (2 "Agreg-" strings against 38 "Añad-"); "Mantén presionado y arrastra para reprogramar" (`a11y.day_map_zone.hint`; Spain iOS says "Mantén pulsado").
- Register: tú. Main catalog 131 strings with tú pronouns, widgets 26, Kit 4, permission prompts 4; imperatives Toca/Añade/Ve/Abre/Elige (62 main, 17 widgets); 0 usted, 0 vos. "Insight" sentences are tú ("Has estado presente durante %d días. Sin presión — solo reconocimiento.", "Mantenlo suave.").
- Permission prompts (verbatim): calendar "Muestra los eventos de tu calendario junto a tus tareas para tener todo el plan del día en un solo lugar."; Reminders "Taskful Day puede importar tus Recordatorios de Apple para ayudarte a planificar tu día en un solo lugar."; microphone "Taskful Day usa el micrófono para capturar tu voz y crear tareas rápidamente."; speech "Taskful Day usa reconocimiento de voz para convertir tu voz en texto de tareas."
- The paywall lists Day Clock, Day Map, Energy River and Focus Mode as Pro features; the site's Free tier says "All four visual day views". Check against the code before translating the Free tier (same flag as French).
- Siri phrases use tú ("Añadir tarea en ${applicationName}", "Cuántas tareas tengo en ${applicationName}", "Recuérdamelo en ${applicationName}" on the Watch).

### Paid tier names in the Spanish UI
"Taskful Day Pro"; plan labels Mensual / Anual / De por vida; status "Pro mensual", "Pro anual", "Pro de por vida", "Plan gratuito"; "Iniciar prueba gratuita"; "Restaurar compras"; "Desbloquear Pro"; "Gestionar suscripción". Store products: "Taskful Day Pro mensual", "Taskful Day Pro anual", "Taskful Day Pro compra única", "Apoyar al desarrollador".

### Spanish App Store listing (checked 2026-11-19, https://apps.apple.com/es/app/id6757345400)
- Name: **Taskful Day: Planificador** (US: "Taskful Day: Day Planner", so it differs)
- Subtitle: **Lista Tareas & Agenda** (US, from the 2026-11-07 French glossary: "Calm Task Tracker & To-Do List"; FLAG: Title Case and no "de" between Lista and Tareas)
- In-app purchases (reference): `Apoyar al desarrollador 1,00 €` · `Taskful Day Pro compra única 44,99 €` · `Taskful Day Pro anual 29,99 €` · `Taskful Day Pro mensual 2,99 €` (US per the French glossary: $1.00 / $39.99 / $24.99 / $2.99)
- Languages line: **Español y 33 más**
- Category: **Productividad** (also "Utilidades"; US: Productivity). Family Sharing: "En familia" listed. The lookup API lists Mac among supported devices
- Description terms: "Reloj del día", "Río de energía", "Mapa del día", "Hoy", "captura en lenguaje natural", "centro de control" (matches the app, which does not say "centro de control" itself).

---

### 4. WanderWiki (`wanderwiki`, source `WanderWiki/`, ID 6758459119)

### Spanish coverage
| Catalog | keys | `es` translated | % |
|---|---|---|---|
| WanderWiki/Resources/Localizable.xcstrings (main app) | 425 | 425 | 100 % |
| WanderWikiWidget/Localizable.xcstrings | 129 | 129 | 100 % |

No InfoPlist.xcstrings and no AppShortcuts catalog; the display name comes from build settings and no permission texts are declared. **Verdict: app is in Spanish: yes.**

### Glossary
| English term on site | English UI string (key) | Spanish UI string (verbatim) | Note |
|---|---|---|---|
| Random | `random_mode` | Aleatorio | |
| Browse | `browse_title` | Explorar | store text also "En Explorar tienes 16 categorías" |
| For You | `for_you_mode` | Para ti | quoted «Para ti» in running text |
| Today in History | `Today in history` / `On This Day` | Un día como hoy | both English terms give the same Spanish string; `Today in history: %@` → "Hoy en la historia: %@"; `feature_history` → "Descubre qué pasó hoy en la historia" |
| On This Day categories | `Events` / `Births` / `Deaths` / `Holidays` | Eventos / Nacimientos / Fallecimientos / Festividades | |
| Tabs | `feed_tab` / `profile_tab` / `settings` | Feed / Perfil / Ajustes | FLAG: "Feed" loanword in 6 strings ("Feed personalizado", "El feed personalizado solo está disponible en inglés por ahora."); the Spanish listing also uses "feed" |
| WanderWiki Plus | `unlock_premium` / `Premium feature` | Desbloquear Premium / Función premium | FLAG: no "Plus" string; the tier is "Premium". Capitalization: "Premium" on a button, "premium" in "Función premium" and "una experiencia premium" |
| Monthly / Annual / Weekly / Lifetime | `monthly` / `yearly` / `weekly` / `lifetime` | Mensual / Anual / Semanal / De por vida | `subscribe_*` keys give the same words; suffix `paywall_monthly_per_month` → "al mes". `Unlock Lifetime Access` → "Desbloquear acceso de por vida"; `paywall_lifetime_own` → "WanderWiki tuyo para siempre" |
| Best long-term value | `best_value` | Mejor oferta | |
| Free trial | `%lld-day free trial` / `Start %lld-Day Free Trial` | Prueba gratuita de %lld días / Iniciar prueba gratuita de %lld días | "Comienza tu prueba gratuita de %lld días. Cancela en cualquier momento." |
| Free articles per day | `%lld free articles left today` | Te quedan %lld artículos gratis hoy | |
| Restore purchases | `restore_purchases` | Restaurar compras | |
| Saved | `saved` / `Saved` | Guardado / Guardados | list header "Guardados" |
| Liked list | `liked` / `like` | Te gusta / Me gusta | `no_liked_articles_hint` → "Toca el corazón en los artículos que te gusten" |
| Folders | `Folders` / `New folder` | Carpetas / Nueva carpeta | |
| Read aloud | `Listen` | Escuchar | |
| Where Next | `Where next` | ¿Y ahora qué? | |
| Show less / hide | `Show less like this` / `Hide this article` | Mostrar menos de esto / Ocultar este artículo | |
| Reader themes | `Reader Theme`, `Sepia`, `Solarized` | Tema del lector, Sepia, Solarized | |
| Search | `Search Wikipedia` | Buscar en Wikipedia | |
| Reading streak | `%lld-day streak` / `Streak reminder` | Racha de %lld días / Recordatorio de racha | `Don't break your streak` → "No rompas tu racha" |
| Widgets | `On This Day`, `Reading Year`, `Continue Reading`, `Got a Minute`, `Two Doors` | Un día como hoy, Año de lectura, Seguir leyendo, ¿Tienes un minuto?, Dos puertas | control `Surprise Me` → "Sorpréndeme" |
| Control: Surprise Me | `Surprise Me` | Sorpréndeme | tú |
| On-device summaries | `AI summary: %@` | Resumen con IA: %@ | |
| 16 topics | `interest_*` | Ciencia, Tecnología, Historia, Artes, Música, Deportes, Naturaleza, Espacio, Filosofía, Geografía, Literatura, Cine, Gastronomía, Arquitectura, Matemáticas, Política | `movies` → "Cine", `food` → "Gastronomía", `space` → "Espacio" |
| No ads | `feature_no_ads` / `onboarding_benefit_no_ads_title` | Experiencia sin anuncios / Sin anuncios. Sin ruido. | `tip_bullet_no_ads` → "Sin anuncios. Sin rastreo. Sin inversores." |
| Offline reading | `Offline Reading` | Lectura sin conexión | `Ready offline` → "Disponibles sin conexión" |
| Manage subscription | `manage_subscription` | Gestionar suscripción | |

Other flags:
- `for_you_english_only` → "El feed personalizado solo está disponible en inglés por ahora." The site says native category queries work in 17 editions; the string may be stale (same flag as French and German). `For You isn't available in %@ yet — showing Random.` → «Para ti» aún no está disponible en %@: se muestra Aleatorio.
- Register: tú (41 main strings, 4 widget strings with tú pronouns; imperatives Toca/Abre/Elige/Prueba/Guarda, 38 main and 5 widget; one "usted-looking" hit is the third-person "Esto eliminará permanentemente todos tus artículos guardados…"). 0 usted, 0 vos.
- "Mantén" is used ("mantén la racha", "Mantén WanderWiki independiente…"), no "presionar" in this app.
- The paywall disclosure is impersonal: "La suscripción se renueva automáticamente a menos que se cancele al menos 24 horas antes del final del período."

### Paid tier names in the Spanish UI
"Premium" (button "Desbloquear Premium"; headline "WanderWiki es una experiencia premium."); plan labels Mensual / Anual / Semanal / De por vida; lifetime pitch "WanderWiki tuyo para siempre"; "Mejor oferta"; "Restaurar compras". Store products: "WanderWiki mensual", "WanderWiki anual", "WanderWiki semanal", "WanderWiki compra única", "Apoyar al desarrollador". FLAG: there is a weekly plan the site does not list (same as French).

### Spanish App Store listing (checked 2026-11-19, https://apps.apple.com/es/app/id6758459119)
- Name: **WanderWiki: descubre y aprende** (US: "WanderWiki: Swipe to Discover", so it differs)
- Subtitle: **Datos, historia y curiosidades** (US, read live 2026-11-19: "Daily facts, history & trivia")
- In-app purchases (reference): `WanderWiki semanal 0,99 €` · `Apoyar al desarrollador 1,00 €` · `WanderWiki compra única 29,99 €` · `WanderWiki anual 9,99 €` · `WanderWiki mensual 1,99 €` (US: Weekly $0.99, Support the Developer $1.00, Lifetime $24.99, Yearly $8.99, Monthly $1.99)
- Languages line: **Español y 33 más**
- Category: **Educación** (also "Referencia"; US: Education / Reference). Family Sharing: "En familia" listed
- Description terms: "Explora Wikipedia, una idea a la vez", "20 artículos gratis cada día", "En Explorar tienes 16 categorías", "Con Premium, Para ti crea un feed", "17 idiomas", "UN DÍA COMO HOY".

---

### 5. Xiangqiful (`xiangqiful`, source `Xiangqi/`, ID 6794340136; iPhone, iPad, Mac, Game Center)

### Spanish coverage
| Catalog | keys | `es` translated | % |
|---|---|---|---|
| Xiangqi/Localization/Localizable.xcstrings (main app, includes the paywall) | 3273 | 3273 | 100 % |
| Xiangqi/Localization/InfoPlist.xcstrings | 2 | 2 | 100 % (display name only, stays "Xiangqiful") |

No widget or extension catalogs. **Verdict: app is in Spanish: yes.** The catalog also has a separate `es-MX` locale (not used here).

### Glossary
| English term on site | English UI string (key) | Spanish UI string (verbatim) | Note |
|---|---|---|---|
| Tabs | `tab.dashboard`, `tab.play`, `tab.training`, `tab.analysis`, `tab.progress` | Inicio, Jugar, Entrenamiento, Análisis, Progreso | |
| Game Review | `analysis.review.title` | Revisión de la partida | |
| Analyze | `analysis.analyse` | Analizar | |
| Move grades | `classification.best/great/good/book/inaccuracy/mistake/blunder` | Mejor, Excelente, Buena, Teoría, Imprecisión, Error, Error grave | `Book` → "Teoría" (opening theory); `Blunder` → "Error grave" (a two-word term; French "Gaffe"). "Mejor" and "Buena" are bare adjectives (gender differs: "Mejor"/"Buena") |
| Accuracy | `analysis.accuracy.title` | Precisión | `%@ accurate` → "%@ de precisión" |
| Estimated rating | `progress.estimatedRating` | Clasificación estimada | "Clasificación" rather than "Elo"; the chess word "Elo" is not used |
| Skill profile / radar | `progress.radar.title` | Perfil de habilidades | paywall: "Radar de habilidades completo, tendencias y progreso semanal" |
| Weakness trends | `progress.weaknesses.title` | Tendencias de debilidades | paywall hero: "tus tendencias de puntos débiles" (two wordings) |
| Five skills | `skill.category.tactics/defense/positioning/endgame/openings` | Táctica, Defensa, Posicionamiento, Final, Aperturas | "Final" is the xiangqi/chess term (not "Fin de partida") |
| Phases | `phase.opening/middlegame/endgame` | Apertura, Medio juego, Final | |
| Today's plan | `training.plan.title` | Plan de hoy | |
| Lessons / 8 tracks | `module.lessons.title`; `lesson.track.*.title` | Lecciones; Fundamentos, Aperturas, Defensa del Palacio, Táctica de Cañón, Técnica de Caballo, Medio Juego, Final, Avanzado | the store text says "ocho itinerarios" (the app does not use "itinerario"; track word is not shown). FLAG: Title Case on "Defensa del Palacio", "Táctica de Cañón", "Técnica de Caballo", "Medio Juego" |
| Skill assessment | `module.skillAssessment.title` | Evaluación de Nivel | FLAG: Title Case; the store text also says "Evaluación de Nivel de 15 posiciones" |
| Drill modules | `module.tactics.title`, `cannonRange`, `horseTrails`, `palaceWorkshop`, `endgameStudio`, `openingLab`, `mateTrail`, `tacticCards`, `handicapHouse` | Patio de Táctica, Galería de Cañones, Rutas del Caballo, Taller del Palacio, Estudio de Finales, Laboratorio de Aperturas, Ruta de Mate, Cartas Tácticas, Casa de Hándicap | FLAG: Title Case; "Tactics Yard" → "Patio de Táctica" |
| Mate problems / puzzles | `training.kind.mate` / `progress.stat.puzzles` | Problema de mate / Problemas | |
| Coach hints | `paywall.benefit.coach` | Pistas ilimitadas del entrenador en partida | "Pista" for hint (consistent with Tare) |
| Named mistakes | `mistake.*.name`; `lesson.cannon.ironBolt.title` | Táctica de cañón pasada por alto, Pieza atrapada, Mate pasado por alto, Pieza colgada, Horquilla pasada por alto, Clavada pasada por alto, Enfilada pasada por alto, Debilidad del palacio, General expuesto, Imprecisión de apertura; "El Cerrojo de hierro" (lesson title), "El Cerrojo de Hierro (tiěménshuān)" in a lesson body | the mistake-name pattern is "X pasado/a por alto" (missed). "Cerrojo de hierro" capitalization varies |
| Piece style (setting) | `board.pieceSet.title` / `board.pieceSet.traditional` / `.western` / `.hybrid` | Piezas / Tradicional / Occidental / Híbrido | **setting `Pieces` → "Piezas"**. This is the site's "piece style". Store text: "Empieza con símbolos occidentales o con un juego híbrido" |
| Piece set (finish) | `board.pieceFinish.title` and values | Acabado de las piezas; Marfil, Madera tallada, Melamina de club, Jade, Canto rodado, Porcelana, Laca dorada, Palisandro y latón | the eight finishes the site calls "piece sets". FLAG: `game.settings.pieceSet` (English "Piece set") is "Juego de piezas", used in the board-settings sheet: the app has both "Juego de piezas" (sheet title) and "Acabado de las piezas" (finish), and "Piezas" for the style. Proposed site wording: **estilo de piezas** (Tradicional/Occidental/Híbrido) and **juego de piezas** (the eight finishes), but the app label for the finish group is "Acabado de las piezas" |
| Characters | `board.charset.title` / `.traditional` / `.standard` | Caracteres / Tradicional / Simplificado | |
| Notation | `board.notation.title` / `.wxf` / `.chinese` | Notación de jugadas / WXF / Chino | `game.settings.notation` → "Notación" |
| Boards | `board.theme.*` | Boj, Palisandro, Mesa de piedra del parque, Tapete de club, Rollo de papel xuan, Laca roja y oro, Mármol y jade; `3D Board` → "Tablero 3D" | the seven boards; `board.theme.title` → "Tablero". Boxwood = "Boj", Rosewood = "Palisandro" |
| Flip board / New game | `game.toolbar.flip` / `mac.command.newGame` | Girar tablero / Partida nueva | |
| Premium | `settings.premium.upgrade` | Mejorar a Premium | "Welcome to Premium" and the plan label "Premium" are in the paywall; "Mejorar a Premium" |
| Free | `settings.premium.free` | Plan gratuito | |
| Monthly / Yearly / Lifetime | `paywall.plan.monthly` / `.yearly` / `.lifetime` | Mensual / Anual / Vitalicio | FLAG: "Vitalicio" (paywall, 6 strings: "Comprar Vitalicio de todos modos", "Ya tienes Vitalicio…") versus "De por vida" in settings (`settings.premium.lifetimeNoManage` → "De por vida — nada que renovar, nada que cancelar") and in the store product "Premium de por vida" |
| Best value | `paywall.bestValue` | Mejor valor | FLAG: calque of "best value"; WanderWiki says "Mejor oferta" |
| Start free trial | `paywall.startTrial` | Empezar prueba gratis | `%lld-day free trial` → "Prueba gratis de %lld días" (WanderWiki/Taskful say "prueba gratuita") |
| Restore purchases | `paywall.restore` | Restaurar compras | |
| Check / checkmate / stalemate | `game.status.check` / `game.reason.checkmate.win` / `gc.achievement.stalemate_win.title` | Jaque / Diste jaque mate / Estancamiento | stalemate = "estancamiento" ("En xiangqi, no tener jugadas hace perder"); perpetual check = "jaque perpetuo" |
| Sides | `board.side.red` / `board.side.black` | Rojo / Negro | `Play as Red` → "Jugar con Rojo" |
| Palace / river | (text) | palacio / río | "Defensa del Palacio", "el tablero y el río" |

**Spanish piece names the app uses** (`piece.*`): General (general), Consejero (advisor), Elefante (elephant), Caballo (horse), Carro (chariot), Cañón (cannon), Soldado (soldier). Lower-case inline forms: general, consejero, elefante, caballo, carro, cañón, soldado. The cannon's "screen" is "pantalla" (e.g. "anota dónde está la pantalla de cada cañón"); the horse's "leg" is "pata" ("la regla de la pata"). The pinyin names stay in running text (chángjiāng, kùnbì, tiěménshuān). "Carro" (not "torre") is the xiangqi chariot, which differs from chess.

Other flags:
- **Register is tú** (240 strings with tú pronouns tu/tus/te/ti; 39 first-word tú imperatives such as Toca/Abre/Busca; 0 usted, 0 vos). The words "presiona/presionar" (6 strings) are the verb "to pressure" in chess talk ("presiona la columna b", "Rojo va con un carro de ventaja y presiona"), not the Latin-American "to press"; no defect.
- "Hándicap" and "Casa de Hándicap" use the accented Spanish form.
- Stale string: `paywall.benefit.opponents` ("All 40 opponents…") → "Los 40 rivales, desbloqueados de inmediato" is unused in code (per the German note), so do not use it.
- Title-case Spanish module and track names ("Patio de Táctica", "Cartas Tácticas") read as English-style capitalization; Spanish uses sentence case.
- Paywall benefits (verbatim): "Análisis de partidas ilimitado", "Pistas ilimitadas del entrenador en partida", "Análisis profundo del motor con varias líneas", "Todos los ejercicios de cada módulo", "Radar de habilidades completo, tendencias y progreso semanal". Free limits and the 2/3/2-a-day figures live in strings with `%lld`.
- `diagnostic.engine.nnueMissing` → "Falta el archivo de evaluación del motor. Reinstala la app para jugar contra el ordenador." ("ordenador", Spain-correct).

### Paid tier names in the Spanish UI
"Xiangqiful Premium"; plan labels Mensual / Anual / Vitalicio; "Plan gratuito"; "Empezar prueba gratis"; "Restaurar compras"; "Gestionar suscripción". Store products: "Premium mensual", "Premium anual", "Premium de por vida", and tip items "Mecenas", "Gran apoyo", "Un café".

### Spanish App Store listing (checked 2026-11-19, https://apps.apple.com/es/app/id6794340136)
- Name: **Xiangqiful: Ajedrez Chino** (US: "Xiangqiful Learn Xiangqi & AI", so it differs; FLAG: Title Case "Chino")
- Subtitle: **Aprende xiangqi: táctica e IA** (US, read live 2026-11-19: "Chinese Chess Tactics Trainer")
- In-app purchases (reference): `Premium anual 9,99 €` · `Premium mensual 1,99 €` · `Mecenas 5,99 €` · `Gran apoyo 9,99 €` · `Un café 1,99 €` · `Premium de por vida 22,99 €` (US: Premium Monthly $1.99, Premium Yearly $9.99, Supporter $4.99, Huge Support $9.99, Coffee $1.99, Premium Lifetime $19.99)
- Languages line: **Español y 33 más**
- Category: **Juegos de mesa** (US: Board). Game Center and Family Sharing ("En familia") listed. Lookup API lists Mac among supported devices.
- Description terms: "xiangqi", "ocho itinerarios", "80 lecciones gratis", "símbolos occidentales o … un juego híbrido", "Evaluación de Nivel de 15 posiciones", "jaque mate", "motor", store says "no tener jugadas hace perder".

---

### 6. Clippet (`clippet`, source `clipboard/`, ID 6829498729, NOT released)

Built from the English page `_apps/clippet.md`, the catalogs, and `~/Downloads/clipboard/marketing/aso/` (listing.json, purchases.json). The ASO README says all 40 App Store locales are written.

### Spanish coverage
| Catalog | keys | `es` translated | % |
|---|---|---|---|
| clipboard/Localizable.xcstrings (main app, paywall) | 638 | 638 | 100 % |
| clipboard/AppShortcuts.xcstrings (Siri and Spotlight) | 2 | 2 | 100 % |
| clipboard/InfoPlist.xcstrings | 7 | 7 | 100 % (permissions: contacts, Face ID, photo library, Reminders; plus the two file-type names) |
| ClipboardKit Localizable.xcstrings | 26 | 26 | 100 % |
| ClipboardKeyboard Localizable + InfoPlist | 104 + 1 | 104 + 1 | 100 % |
| ClipboardAction Localizable + InfoPlist | 1 + 1 | 1 + 1 | 100 % |
| ClipboardWidgets Localizable + InfoPlist | 63 + 1 | 63 + 1 | 100 % |
| ClipboardShare Localizable + InfoPlist | 28 + 1 | 28 + 1 | 100 % |
| ClipboardMacBridge Localizable.xcstrings | 19 | 19 | 100 % |

Permission prompts are in Spanish (verbatim): contacts "Guarda como contacto nuevo un número de teléfono o una tarjeta de visita de un elemento cuando eliges «Añadir a Contactos»."; Face ID "Permite que el bloqueo de la app desbloquee Clippet por ti, para que solo tú veas tus elementos."; photo library "Guarda en tu fototeca la foto o el vídeo de un elemento cuando eliges «Guardar en Fotos»."; Reminders "Añade un recordatorio a la app Recordatorios cuando ejecutas una acción de recordatorio que configuraste para un elemento." Siri phrases: "Pegar última copia en ${applicationName}", "Guardar mi última copia en ${applicationName}". **Verdict: app is in Spanish: yes, everywhere (all widget, keyboard, share and Mac extensions too).**

### Glossary
| English term on site | English UI string (key) | Spanish UI string (verbatim) | Note |
|---|---|---|---|
| Clipboard | `Clipboard Access` | portapapeles ("Acceso al portapapeles", "Supervisar portapapeles") | store name "Clippet: Portapapeles" |
| Clip | `Clip` / `Search Clips` | Elemento / Buscar elementos | matches the listing ("elemento"); plural variants "%lld elemento antiguo está oculto" / "elementos antiguos están ocultos" |
| Library | (text) | biblioteca ("Sus elementos permanecen en tu biblioteca.") | the photo library is "fototeca" (Face ID and photo prompts) |
| Smart Actions | `Smart Actions` | Acciones inteligentes | listing: "Las Acciones inteligentes reconocen…" |
| Custom actions | `Custom Actions` | Acciones personalizadas | |
| Boards | `Boards` / `New Board` / `Add to Board` | Tableros / Nuevo tablero / Añadir al tablero | listing: "tableros de colores" (consistent) |
| Tags | `Tags` | Etiquetas | listing "etiquetas" |
| Pin | `Pin` / `Pinned` | Fijar / Fijados | widget "Pinned Clips" → "Elementos fijados"; listing "Fija arriba" |
| Quick Paste | `Quick Paste` | Pegado rápido | |
| Quick Add (widget) | `Quick Add` | Añadir rápido | verb phrase, not a noun; `Add Clip` → "Añadir elemento" |
| Paste | `Paste` | Pegar | |
| App Lock | `App Lock` | Bloqueo de la app | `Face ID Lock` → "Bloqueo con Face ID" |
| iCloud Sync | `iCloud Sync` | Sincronización con iCloud | |
| Backup | `Backup` | Copia de seguridad | file type "Copia de seguridad de Clippet" |
| Auto-delete | `Auto-Delete` | Borrado automático | `Auto-delete in %@?` → "¿Borrar automáticamente en %@?"; `Auto-Delete Sensitive Clips` → "Borrar automáticamente elementos sensibles" |
| Menu bar | `Menu Bar` | Barra de menús | |
| Open at login | `Open at Login` | Abrir al iniciar sesión | listing/Mac copy: "Clippet se abre cuando inicias sesión en tu Mac"; macOS "Ítems de inicio de sesión" |
| Save to Clippet | `Save to Clippet` | Guardar en Clippet | |
| Clippet keyboard | `Clippet Keyboard` | Teclado de Clippet | |
| Quick Look | `Quick Look` | Vista Rápida | listing also "Vista Rápida"; macOS Spain writes "Vista rápida" (capital R is off) |
| Copy as plain text | `Copy as Plain Text` | Copiar como texto sin formato | |
| Search | `Search` | Buscar | |
| Settings | `Settings` | Ajustes | |
| Content types | `Link`, `Images`, `Videos`, `PDFs`, `Audio`, `Files`, `Code`, `Text` | Enlace, Imágenes, Vídeos, PDF, Audio, Archivos, Código, Texto | |
| Sensitive | `sensitive content` | contenido sensible | |
| Older clips hidden | `%lld older clips are hidden` | plural variations ("%lld elemento antiguo está oculto", …) | `See Older Clips` → "Ver elementos más antiguos"; `Not Now` → "Ahora no" |
| Widgets | `Latest Clip`, `Pinned Clips`, `Add Clip`, `Recently copied` | Último elemento, Elementos fijados, Añadir elemento, Copiado recientemente | |
| Free trial | `Start Free Trial` / `%lld days free` | Empezar prueba gratuita / plural "%lld día gratis", … | |
| Lifetime | `Lifetime` / `Buy Lifetime` | Lifetime / Comprar Lifetime | FLAG: English word left in 5 strings ("Comprar Lifetime", "Cambiar a Lifetime", "Lifetime incluye Clippet Pro, así que puedes cancelar tu suscripción."); the planned store product is "Clippet Pro de por vida" |

Register: tú (73 main strings, 8 keyboard, 2 widget, 2 Kit with tú pronouns; imperatives Toca/Añade/Pega/Ve/Ordena; 0 usted, 0 vos). Consistent.

### Paid tier names in the Spanish UI
**"Clippet Pro"**; "Obtener Clippet Pro" (purchase button); plan labels Mensual / Anual / Lifetime; "Empezar prueba gratuita"; "Restaurar compras"; "Gestionar suscripción"; "Suscribirse mensualmente", "Suscribirse anualmente"; the description of the purchase: "Una sola compra desbloquea Clippet Pro en tu iPhone, iPad y Mac, y En familia lo comparte con tu familia." Planned store product names (`marketing/aso/purchases.json`, es-ES): "Clippet Pro mensual", "Clippet Pro anual", "Clippet Pro de por vida".

### Spanish App Store listing
Not live: https://apps.apple.com/es/app/id6829498729 returned HTTP 404 on 2026-11-19, and the lookup API returned no result for es or us. The prepared listing (`~/Downloads/clipboard/marketing/aso/listing.json`, es-ES, updated 2026-11-02; not published, so reference only):
- Name: **Clippet: Portapapeles**
- Subtitle: **Copiar y pegar con historial**
- Promotional text: "Todo lo que copias, guardado. Textos, enlaces, imágenes, PDF y código reaparecen con una búsqueda en Clippet, un historial del portapapeles para iPhone, iPad y Mac."
- Terms used in the description: portapapeles; elemento (clip); Acciones inteligentes; tableros; etiquetas; Fija arriba; barra de menús; Vista Rápida; fototeca; tu dispositivo. Register: tú.
- Keywords es-ES (iOS): teclado, gestor, copia, pega, texto, enlace, notas, fragmentos, widget, sincronizar, código, rápido, guardar
- Languages line: not available (page not live); the ASO README says 40 locales. Category: not confirmed.

---

### Cross-app terms (Spanish, as the apps write them)
- Settings = Ajustes (all six); Restore purchases = Restaurar compras; Manage subscription = Gestionar suscripción (Soon. alone says "Administrar").
- Free = Gratis (Soon.) / Plan gratuito (Taskful Day, Xiangqiful) / versión gratuita (Taskful Day body); Free trial = Prueba gratuita (Soon., Taskful Day, WanderWiki, Clippet) / Prueba gratis (Xiangqiful).
- Monthly / Yearly = Mensual / Anual; Weekly = Semanal (WanderWiki); Lifetime = De por vida, except Vitalicio (Xiangqiful paywall) and Lifetime (Clippet, one Taskful Day string); store products say "compra única" (Soon., Taskful Day, WanderWiki) or "de por vida" (Xiangqiful, Clippet plan).
- Streak = Racha (Soon., Taskful Day, WanderWiki).
- Countdown = Cuenta atrás (Spain); Moment = Momento; Memory = Recuerdo; On This Day / Today in History = Un día como hoy (Soon., WanderWiki).
- Hint = Pista (Tare, Xiangqiful); Level = Nivel; Chapter = Capítulo; Pin = Fijar (Soon., Clippet).
- Add = Añadir (default); Agregar is a stray Latin-American form in Soon. (9) and Taskful Day (2).
- Lock Screen = pantalla de bloqueo (preferred) / pantalla bloqueada; Home Screen = pantalla de inicio; menu bar = barra de menús; app switcher = selector de app; Quick Look = Vista Rápida; photo library = fototeca; widget = widget.
- Tú everywhere; imperatives Toca / Elige / Añade / Abre / Pega / Ve; "Mantén pulsado" (Soon.) versus "Mantén presionado" (Taskful Day).

### Flags (app-side string bugs, register mixes, missing Spanish)
1. **Soon. mixes Spain and Latin-American Spanish** in one catalog: "cuenta regresiva" (22 strings) vs "cuenta atrás" (21), "Agrega/Agregar" (9) vs "Añade/Añadir" (29), "Administrar suscripción", "Apple Clima" (Weather app is "Tiempo" in Spain), "Pronóstico" (Spain: "previsión"). The Spanish store listing and the widgets use Spain wording only.
2. **Taskful Day**: "Agregar rapido" (missing accent, Latin-American verb), "Agregar a la bandeja"; "¿Cómo te sintió el día?" (ungrammatical); English "Lifetime es una compra única" and 17 strings with English "insights"; four terms for focus (Enfoque / Concentrarse / Modo concentración / Sesión de enfoque); three verbs for carry forward; "Mantén presionado".
3. **Lifetime is inconsistent across the portfolio**: Clippet keeps the English word "Lifetime" in 5 UI strings while its planned store product is "Clippet Pro de por vida"; Xiangqiful's paywall says "Vitalicio" while its store product is "Premium de por vida"; Soon., WanderWiki, Taskful Day use "De por vida". The site must pick one ("de por vida").
4. **Xiangqiful setting names**: "Piezas" (style: Tradicional/Occidental/Híbrido), "Acabado de las piezas" (the eight finishes), and "Juego de piezas" (`game.settings.pieceSet`, the board sheet) coexist; the site's "piece style" = Piezas, "piece set" = Acabado/Juego de piezas. Title-case module names ("Patio de Táctica", "Casa de Hándicap") and "Mejor valor" (calque).
5. **Tare**: beam = "barra" (store and app agree); "Móvil" for the hanging sculpture collides with "móvil" (phone); "El Fulcro" is a rare word; the unlock text puts the price before the chapter count ("%1$@ %2$#@chapters@ más de niveles…"), check on screen. Chapter names are Title Case. Tare has no pans.
6. **WanderWiki**: `for_you_english_only` ("solo está disponible en inglés") looks stale against the site's 17 editions; "Feed" is an English loanword in 6 strings; weekly plan exists and the site does not list it.
7. **Store listing issues**: Soon. subtitle "Boda Viaje y Bebé Cuenta Atrás" (no comma, Title Case); Taskful Day subtitle "Lista Tareas & Agenda" (no "de", Title Case); Xiangqiful name "Ajedrez Chino" (Title Case). Store descriptions use "cuenta atrás", "pantalla bloqueada" and "línea temporal" where the Soon. app says "cuenta regresiva" / "pantalla de bloqueo" / "cronología".
8. **Missing Spanish**: only non-user-facing keys (`Soon` in InfoPlist, `%@ ` and `%@ %@` in Soon. widgets) and two Taskful Day Kit strings (`End focus session`, `Extend focus session`, which fall back to English on the Watch). Siri/App Shortcuts catalogs exist and are 100 % Spanish for Soon., Taskful Day (iPhone and Watch) and Clippet; Tare, WanderWiki and Xiangqiful have none.
9. **Register**: no usted or vos anywhere in the six apps; no mixes within a string. Safe to write the site in tú.
10. **Clippet is unreleased**: the store page and lookup API return nothing; the es-ES listing text under `~/Downloads/clipboard/marketing/aso/` is the only Spanish store source and is unpublished. The French doc says the main catalog has 634 keys; the catalog now has 638 (counted 2026-11-19).
11. **Shared scratchpad collision**: my first coverage script was overwritten by another agent's `cov.py` in `scratchpad/es-research/`; my results above were recomputed with scripts in `scratchpad/es-research/D-work/`.


---


## Additions from Tier 4 batch 1 (2026-11-19, checked in the catalogs by the reviewers)

- AfterShift (`es.lproj/Localizable.strings`): Recovery Timeline «Línea de recuperación» (`timeline.title`); debt trend «Deuda en aumento», Estable,
  Recuperando (`debtTrend.*`); Excelente (`score.excellent`).
- GymLogger X (`Localizations/es.json`): Strength Progress states «Estancamiento: %@» (`analytics_plateau_title`), «En observación: %@»
  (`analytics_plateau_watch_title`), «Estancamiento previsto» (`analytics_plateau_predicted`); the site uses these. Other forms in the app
  («Meseta detectada», «Estancamiento detectado», «Puntaje de sobrecarga») are flagged in ISSUES.md I-0190; never copy them.
- LiftLog (`CoreLift/Resources/Localizable.xcstrings`): progression review Progresaste, Mantén, Fallado, Descarga; «Descanso completado»,
  «serie efectiva», «Añadir/Quitar 15 segundos», «Ajuste fino», «Cronómetro de descanso».
- MediaKit (`MediaKit/Localizable.xcstrings`): «Comprimir vídeo», Modo, «Tamaño objetivo», Avanzado, «Resolución máx.», Códec,
  «Tasa de bits de audio», «64 kbps (voz)».
- Observa (`HealthLogger/Localizable.xcstrings`): «¿Por qué esta puntuación?», «Tu rango habitual», puntuación de preparación. The catalog writes
  «cardíaca» with an accent; the site follows Apple Spain («cardiaca»).
- Pawza (`PetCare/Localizable.xcstrings`): reminders Repetición, Nunca, Urgente (Time-sensitive), Atrasado, Hoy, «Esta semana», «Más tarde»,
  «Supera los modos de concentración»; «PDF de visita al veterinario».

## Additions from Tier 4 batch 2 (2026-11-19)

- GymLogger X (`es.json`): «Insertar semana de descarga» (`insert_deload_week`), «Marcar como descarga» (`mark_as_deload`), «Volumen de series»,
  «Pico de volumen», «Descanso insuficiente», «Recuperación». Avoid the English «deload» strings flagged in I-0190.
- MediaKit: «Mantener el original (remux)» (picker), «Convertir», «Formato de salida», «Ejecutar». The Matroska error's «Conservar original (remux)»
  is an app mismatch (I-0422).
- Soon. (countdown catalog): tab «Plan», «modo plan», «Restaurar sugerencias», «Preparar la bolsa del hospital», «Instalar la silla del coche»,
  «Recordatorios del modo plan»; the wedding list's «Cena de ensayo» is a US custom (I-0427).
- Millrace: «Deshacer ese movimiento» (card), Pack de diseño 1/2, Pack de verano, Pack de invierno, Colección completa, «Apoya al desarrollador»;
  «usos para deshacer» in prose (the catalog's «Fichas de deshacer» collides with the game's tiles).
- EarnLock: «Desbloqueo de emergencia», «plan gratis», «%@ para desbloquear».
