# Italian glossary per app (it, Italy)

Part of the language sheet `_i18n/it.md`. Extracted 2026-11-19 from each app's string catalogs (read-only, locale `it` in every catalog) and its Italian App Store listing (apps.apple.com/it and the iTunes lookup API, country=it). Italian UI strings are verbatim: use them exactly on the site, except where a Flags note says the app string is defective (English left in, voi forms, wrong meaning, inconsistent variants). Every app writes tu, like the site, except Observa's ~60 coaching strings in voi (app-side defect). **Mockly has no Italian interface.** Store prices here are reference only: the site prints prices from the catalog.

## Italian glossary, batch 1: aftershift, allpaid, appmeta, appmeta-pulse, chessful

Method (checked 2026-11-19). Read-only extraction from each app's source catalogs under `~/Downloads/` (`shiftworkersleep/`, `billreminder/`, `metabuilder/`, `metabuilder_phone/`, `Chessful/`). The xcstrings catalogs were parsed as JSON with `python3 -I`; AfterShift's legacy `it.lproj/*.strings` and `.stringsdict` were converted with `plutil -convert json`. "total" = translatable keys (`shouldTranslate: false` and blank keys excluded; stale keys are counted, the non-stale figure is given in brackets where it differs); "it" = keys whose `it` value has state `translated` (or plural/substitution variations, or a translated stringSet). The locale code is plain `it` in every catalog (no `it-IT`), and no catalog has `needs_review` Italian values. Italian values are copied verbatim (apostrophes `'` or `’`, `«»` and `—` as in source; both apostrophe styles occur in the same catalogs). Register counts are rough regexes on the Italian values (tu = tuo/tua/ti/te/hai/sei/puoi/vuoi/devi plus common tu imperatives such as "tocca", "aggiungi", "sblocca", "prova"; Lei = "Lei", Lei-subjunctive imperatives such as "tocchi", "aggiunga", "sblocchi"), and every Lei-looking hit was hand-checked: there are none (see Register). App Store data: iTunes lookup API (`country=it&lang=it_it`) plus the raw `serialized-server-data` JSON of `apps.apple.com/it/app/id<ID>` (Safari UA, `Accept-Language: it-IT`, redirects followed; the AppMeta page needed two 429 retries, all five Italian pages were read). The listing page also prints the seller's personal name; it is not copied here. Prices keep the NBSP (U+00A0) before `€` and are reference only: the site prints prices from the catalog / `MASTER-prices.csv`. The Italian App Store labels the ID `ID Apple` and Family Sharing `In famiglia` (AllPaid prints "tramite In famiglia").

Register across catalogs (rough): **all five apps write tu (informal singular)**, no Lei anywhere. Tu-marked values: AfterShift ~275 of 1484 (widget: "Il tuo stato di recupero", "Quanto sei indietro"), AllPaid ~81 of 494, AppMeta ~323 of 2265, AppMeta Pulse ~239 of 1415, Chessful Localizable ~388 of 2114 and Lessons ~1216 of 3649 (lesson imperatives: "Cerca difese che reagiscano", "Tieni il re nero nell'angolo"). The "Lei-looking" hits (159 in Lessons, a few dozen elsewhere) are all third-person "suo/sua/suoi" (a bishop's "suoi stessi pedoni", an account's "suoi dati") or third-person verbs, never an address to the user. Impersonal forms are used for some buttons ("Acquista a vita", "Ripristina acquisti", "Importa partite") that are the tu imperative or neutral. Siri phrases are tu or neutral ("Chiedi a ${applicationName} quando dormire", "Di' a ${applicationName} che ho dormito"). The site writes tu, so every Italian term can be quoted as is; care points are the defects under Flags.

---

### 1. AfterShift (`aftershift`, source `shiftworkersleep/`, ID 6757163182)

### Italian coverage
- Main app, legacy `.lproj` (no xcstrings): `en.lproj/Localizable.strings` 1484 keys, `it.lproj/Localizable.strings` 1484 keys, 0 missing, 0 extra, 26 values identical to English (`stages.rem` "REM", `pro.chipLabel` "Premium", `palette.*` "Lava"/"Aurora"/"Sakura", `common.ok` "OK", `caffeine.drink.espresso` "Espresso", `rotation.preset.panama` "Panama (2-2-3)", format-only keys). → **100 %**. `Localizable.stringsdict` en and it both present (4 plural keys: `plural.naps` "%d pisolino/pisolini", `plural.days` "%d giorno/giorni", `plural.hours` "%d ora/ore", `plural.daysRemaining` "%d giorno rimanente/giorni rimanenti").
- `it.lproj/AppShortcuts.strings`: 16 Siri/Shortcuts phrases in Italian, all tu or neutral: "Registra il sonno su ${applicationName}", "Quand'è il mio prossimo turno su ${applicationName}", "Prossimo turno su ${applicationName}", "Chiedi a ${applicationName} quando dormire", "Quand'è la mia prossima finestra di sonno su ${applicationName}", "Com'è il mio stato di recupero su ${applicationName}", "Segna quanto ho dormito su ${applicationName}", "Registra il mio sonno su ${applicationName}", "Qual è la mia finestra di sonno su ${applicationName}", "Ho dormito abbastanza per il turno su ${applicationName}", "Controlla il mio recupero su ${applicationName}", "Di' a ${applicationName} che ho dormito", "Qual è il mio prossimo turno su ${applicationName}", "Chiedi a ${applicationName} se ho recuperato abbastanza", "Chiedi a ${applicationName} quando inizia il mio turno", "Quando dovrei dormire su ${applicationName}". The Italian preposition is "su" (not "in"). Siri phrases ARE in Italian.
- Widget `shiftworkersleepWidget/Localizable.xcstrings`: 15 / 15 → 100 % (the widget gallery names and descriptions are the `widget.gallery.*` keys).
- InfoPlist: `it.lproj/InfoPlist.strings` has 2 keys: `CFBundleDisplayName` ("AfterShift") and `NSHealthShareUsageDescription` ("AfterShift legge i tuoi dati del sonno da Apple Salute per calcolare il debito di sonno e il recupero tra i turni."). **English-only:** `NSCalendarsUsageDescription` / `NSCalendarsFullAccessUsageDescription` are build settings (`INFOPLIST_KEY_*` in `project.pbxproj`) with no localization ("AfterShift reads your calendar events to automatically detect work shifts. No data is uploaded — everything stays on your device."), so the calendar permission prompt is English on an Italian device. `NSHealthUpdateUsageDescription` is debug-only.
- Paywall (`paywall.*`) translated. One in-app string states there is no Watch app: `watchSleep.help.step1` "Non c'è nulla da installare sul Watch. AfterShift non ha un'app per Watch: legge il sonno che il tuo Watch scrive già in Apple Salute."
- **Verdict: app is in Italian: yes**, with one English permission prompt (calendar access).

### Glossary
| English term on site | English UI string (key) | Italian UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Today (screen / tab) | Today (`tab.today`) | Oggi | |
| Coach (screen) | Coach (`tab.coach`, `coach.title`) | Consigli | Not "Coach": the tab is "Consigli" |
| Roster (shift calendar) | Roster (`tab.roster`) | Turni | widget `widget.gallery.roster.name` also "Turni"; `onboarding.calendar.title` "Import your roster" = "Importa il tuo turnario" (1 value); the store text says "turnazione" ("La tua turnazione, già compilata"); `roster.rotation` = "Ciclo di turni ricorrente". Three words for the roster concept (Turni / turnario / turnazione): pick one for the site |
| Settings | Settings (`tab.settings`) | Impostazioni | |
| Shift Recovery Score | Shift Recovery Score (`recovery.shiftRecoveryScore`) | Punteggio recupero turno | |
| Sleep Score | Sleep Score (`sleepScore.title`) | Punteggio del sonno | `sleepScore.unlock` = "Sblocca punteggio del sonno" |
| Readiness | Readiness (`readiness.title`; `shiftChange.readiness`; widget `widget.gallery.readiness.name`) | Stato di recupero | **Flag:** `intent.readiness.title` "Shift Readiness" = "Prontezza al turno" and `swap.headline.improved` = "La prontezza dovrebbe migliorare", `paywall.lock.readiness` "la tua prontezza"; `readiness.locked` = "Recupero bloccato". The store text says "Stato di recupero". Use "Stato di recupero" |
| On-call | On-call (`sleepScore.onCall`) | Reperibilità | `schedule.irregular` = "Irregolare/Reperibilità"; `coach.onCall.title` = "Modalità recupero reperibilità"; "reperibil-" 33 values, consistent |
| Naps | Naps (`naps.title`) / Nap (`nap.label`) | Pisolini / Pisolino | `today.logNap` = "Registra pisolino"; stringsdict "%d pisolino/pisolini"; "pisolin-" 76 values vs "sonnellino" 14 values (see Flags) |
| Nap window | Optional nap window (`notification.napWindow.title`) | Finestra pisolino facoltativa | `insight.notification.napWindow.title` = "Finestra pisolino" |
| Sleep window | Sleep window (`notification.sleepWindow.title`) | Finestra di sonno | `intent.sleepWindow.title` "Next Sleep Window" = "Prossima finestra di sonno" |
| Sleep Timing | Sleep Timing (`timing.title`) | Orario del sonno | `paywall.free.sleepTiming` = "Orari del sonno tra i turni" |
| Sleep debt | Sleep debt trend (`debtTrend.title`); widget | Tendenza debito di sonno / Debito di sonno | widget `widget.gallery.sleepDebt.name` = "Debito di sonno" |
| Sleep stages Awake / Core / Deep / REM | `stages.awake/core/deep/rem` | Sveglio / Leggero / Profondo / REM | `stages.sleepStages` = "Fasi del sonno"; Core → "Leggero" is the app's own choice: check it against Apple Salute's Italian stage labels before the site relies on it |
| Time in bed | Time in bed (`timing.timeInBed`) | Tempo a letto | |
| Fragmentation | Fragmentation (`continuity.fragmentation`) | Frammentazione | `paywall.premium.fragmentation` = "Approfondimenti su frammentazione e continuità" |
| Caffeine timing | Caffeine timing (`coach.caffeine.title`) | Orari della caffeina | **Flag, three forms:** `technique.caffeineTiming.title` "Caffeine Timing" = "Timing della caffeina" (anglicism), `caffeine.header` = "Orari caffeina", `caffeine.trend.excellent` = "Orari caffeina eccellenti nelle ultime 2 settimane" |
| Caffeine cut-off | Caffeine cutoff (`notification.caffeineCutoff.title`) | Stop caffeina | |
| Wind-down reminder | Wind down (`notification.windDown.title`) | Rilassamento | **Flag, three forms:** `insight.notification.windDown.title` "Wind-down time" = "Tempo di rilassamento"; `playbook.step.windDown.title` = "Rallenta — body scan, luci basse." (English "body scan" left in) |
| Calendar shift import | Import from calendar (`roster.calendarImport`) | Importa dal calendario | |
| Calendar sync (Premium) | Calendar Sync (`calendar.sectionTitle`) | Sincronizzazione calendario | `paywall.premium.calendarSync` = "Sincronizzazione automatica del calendario e monitoraggio degli straordinari"; `calendar.upgradeAutoSync` = "Upgrade: sincronizzazione automatica, più calendari e straordinari" ("Upgrade" left in English) |
| Overtime | Overtime: (`nextShift.overtime`) | Straordinario: | `nextShift.overtime.addOneHour` = "Aggiungi 1 ora di straordinario"; plural "straordinari" |
| Add a shift | Add shift (`roster.addShift`, `today.addShift`) | Aggiungi turno | consistent "Aggiungi" |
| Shift types | Day / Evening / Night / Off (`shift.day/evening/night/off`) | Giorno / Sera / Notte / Riposo | |
| Shift change | Shift change impact (`shiftChange.title`) | Impatto cambio turno | `insight.shiftChange.title` = "Cambio turno"; `overtime.extended` = "Turno cambiato da %@ a %@ (+%d min)." |
| Repeating rotation | Repeating rotation (`roster.rotation`) | Ciclo di turni ricorrente | `rotation.presets` "Common rotations" = "Cicli comuni". **Flag:** `roster.tapToAdd` = "Tocca + per aggiungere un turno" (drops "or set up a repeating rotation") |
| Three-shift (day → evening → night) | `rotation.preset.threeShift` (+ `.sub`) | Tre turni (sub: Giorno → sera → notte, 2 per ciascuno) | |
| 4-on-4-off | `rotation.preset.fourOnFourOff` | 4 in turno / 4 di riposo | sub: "Quattro notti, poi quattro giorni di riposo" |
| 4-on-3-off | `rotation.preset.fourOnThreeOff` | 4 in turno / 3 di riposo | sub: "Quattro giorni, poi tre di riposo" |
| 2 days / 2 nights | `rotation.preset.ddnn` | 2 giorni / 2 notti | sub: "Due giorni, due notti, quattro di riposo" |
| Panama/Pitman (2-2-3) | `rotation.preset.panama` | Panama (2-2-3) | sub: "2-2-3 a rotazione, un weekend libero su due" |
| Fixed nights | `rotation.preset.fixedNights` | Notti fisse | sub: "Cinque notti, weekend liberi" |
| Fixed days | `rotation.preset.fixedDays` | Giorni fissi | sub: "Cinque giorni, weekend liberi" |
| Trends | Trends (`trends.title`) | Tendenze | `today.section.trends` "Trends & Insights" = "Tendenze e approfondimenti"; `debtTrend.title` uses singular "Tendenza" |
| Do this now (playbook) | Do this now (`playbook.cardKicker`) | Fai così ora | tu imperative; widget `widget.label.doThisNow` = "Da fare ora" (different wording) |
| Techniques | Techniques (`library.title`) | Tecniche | |
| Export / PDF report | Export Sleep Report (`settings.exportReport`) | Esporta report sonno | **Flag:** "report" (8 values: `settings.exportReport`, `premium.export.title` "Esporta report") vs "rapporto" (2 values: `export.title` "RAPPORTO DEL SONNO AFTERSHIFT", `export.pdf.filename` "AfterShift-Rapporto-%@.pdf"). The store text of Pulse uses "report" |
| Live Activity / Lock Screen | Shift countdown on Lock Screen (`liveactivity.settings.title`) | Conto alla rovescia del turno sulla schermata di blocco | |
| Widgets: Next Shift, Shift Plan, Rhythm, Sleep Debt, Roster, Readiness (+ Sleep Graph) | `widget.gallery.*.name` | Prossimo turno, Piano per il turno, Ritmo, Debito di sonno, Turni, Stato di recupero, Grafico del sonno | descriptions e.g. "Conto alla rovescia in tempo reale fino al prossimo turno." |
| Family Sharing | Share with your family — up to 5 members (`paywall.premium.familySharing`) | Condividi con la tua famiglia — fino a 5 membri | Apple's Italian term is "In famiglia" |
| Siri / Shortcuts | AppShortcuts phrases | see coverage section | |

### Paid tier names in the Italian UI (AfterShift)
- Title: **AfterShift Premium** (`paywall.premiumTitle`, `pro.chipLabel` "Premium", `sleepScore.premium` "Premium"); `paywall.continuePremium` "Continua con Premium"; `paywall.tryPremium` "Prova AfterShift Premium"; `paywall.unlockForever` "Sblocca Premium per sempre". The word "Pro" never appears in the Italian UI (0 values); the site term is Premium.
- Periods: Mensile / Annuale / A vita (`paywall.monthly/yearly/lifetime`); `paywall.month` mese, `paywall.year` anno, `paywall.perMonthLong` "al mese"; `settings.lifetimeActive` "Premium a vita"; `paywall.payOnce` "Pagamento unico"; `paywall.lifetimeDisclosure` "Acquisto una tantum. Nessun abbonamento. Tutte le funzioni Premium, per sempre." `paywall.bestValue` "Miglior valore" (calque of "Best value"; AppMeta says "Conveniente", Pulse "Più conveniente").
- Trial: `paywall.startTrial` "Inizia 7 giorni di prova gratuita"; `paywall.7dayTrial` "7 giorni di prova gratuita"; `paywall.freeFor7Days` "gratis per 7 giorni"; `paywall.noChargeToday` "Nessun addebito oggi. Non ti verrà addebitato nulla se annulli prima della fine della prova."; `paywall.cancelAnytime` "Annulla quando vuoi. Nessuna indicazione medica."; `paywall.fullAccess` "Accesso completo. Annulla quando vuoi."
- Restore: `paywall.restorePurchases` "Ripristina acquisti". Terms: `paywall.privacyPolicy` "Informativa sulla privacy", `paywall.termsOfUse` "Termini di utilizzo". `paywall.purchasePendingMessage` "Il tuo acquisto è in attesa di approvazione." (drops the "you'll get access once it's confirmed" half).

### Italian App Store listing (checked 2026-11-19)
- Name: **AfterShift: Sonno & Turni** (English "AfterShift: Sleep & Shift Work"); colon, spaces and `&` as in English.
- Subtitle: **Recupero, riposo e fatica** (English "Recovery, naps & fatigue"; the Italian drops "naps" and says "riposo").
- Category: **Salute e benessere**. Price "Gratis" with "Acquisti in-app: Sì". Age 9+. Compatible: iPhone (iOS 17.6+), Mac (macOS 14.6+, Apple silicon chip M1 or later). Size 20,5 MB. Languages: "Italiano e altre 33 lingue".
- IAP rows («Acquisti in-app»): `Premium acquisto singolo 44,99 €` · `Sostieni lo sviluppatore 1,00 €` · `Premium annuale 29,99 €` · `Premium mensile 3,99 €`. Store IAP names say Premium; the lifetime row is "acquisto singolo" while the app says "A vita" / "Acquisto una tantum".
- Description (store, tu): "La tua giornata inizia quando finisce il turno." Vocabulary: "sonno e recupero", "Stato di recupero, debito di sonno e cronologia del tuo recupero", "La tua turnazione, già compilata", "turni", "tipi di turno", "giorni di riposo", "turnazioni da 12 ore". The store says "turnazione" for the roster where the app says "Turni" (and one "turnario").

---

### 2. AllPaid (`allpaid`, source `billreminder/`, ID 6757253009)

### Italian coverage
- Main `Localizable.xcstrings`: 494 / 494 → **100 %** (non-stale 464 / 464; 21 values identical to English: "Pro", "Streaming", "DataVault", brand names).
- `InfoPlist.xcstrings`: 3 / 3 → 100 % (display name "AllPaid"; `NSFaceIDUsageDescription` "Richiedi Face ID o Touch ID per aprire l'app." which is the in-app settings wording, an instruction to the user, not a "AllPaid richiede…" permission sentence; see Flags).
- Widget `billreminderWidget/Localizable.xcstrings`: 57 / 58 → 98.3 % (only `%lld` untranslated, format-only). `billreminderWidgetShared/Widget.xcstrings`: 130 / 130 → 100 %.
- **Not localized:** Siri App Shortcut phrases (`Services/AppIntents/BillsDueIntent.swift`): no `AppShortcuts.xcstrings`/`.strings` exists in the project, so the spoken phrases are English only. The intent title ("Bills Due This Week" → "Bollette questa settimana") is translated; the phrases are not. Do not promise Italian Siri phrases on the page.
- **Verdict: app is in Italian: yes** (Siri phrases English only).

### Glossary
| English term on site | English UI string (key) | Italian UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Bills | Bills | Bollette | "bolletta/bollette" used throughout (83 values); "fattura" 1 value only |
| Add a bill | Add Bill | Aggiungi bolletta | |
| Mark paid | Mark as paid / Mark paid | Segna come pagato / Segna come pagata | **Flag:** masculine vs feminine for the same action; `Couldn't mark as paid. Try again.` = "Impossibile contrassegnare come pagata. Riprova." (third verb: "contrassegnare") |
| Paid | Paid | Pagata | feminine; "Segna %@ come pagata"; `Mark as renewed` = "Segna come rinnovato" (masc.) |
| Undo | Undo | Annulla | **Flag:** same word as Cancel = "Annulla" (collision) |
| Snooze (notification) | Remind in 2 hours / Remind tomorrow / Remind in 1 week | Ricorda tra 2 ore / Ricorda domani / Ricorda tra 1 settimana | no single "Snooze" string |
| Monthly calendar | Monthly Calendar | Calendario mensile | |
| Total due | Total due | Totale dovuto | |
| Upcoming | Upcoming | In arrivo | "Auto-pay coming up" = "Pagamento automatico in arrivo" |
| Due date | Due date / Due today / Due tomorrow / Due in %lld days | Data di scadenza / Scadenza oggi / Scadenza domani / Scadenza tra %lld giorni | `Due date passed` = "Data di scadenza passata" (the store text quotes it); "scadenz-" 29 values |
| Reminders | Reminders | Promemoria | `Reminders are off` = "Promemoria disattivati" |
| Multiple reminders per bill (Pro) | Multiple reminders per bill | Più promemoria per bolletta | |
| Due-day reminder | Due-day reminders | Promemoria il giorno della scadenza | `Remind on due day` = "Ricorda il giorno della scadenza" |
| Spending analytics (Pro) | Spending Analytics | Analisi delle spese | "Analytics" alone = "Analisi" |
| Category breakdown | By category | Per categoria | |
| Monthly trends | Monthly trend | Tendenza mensile | |
| Full payment history | Full payment history / Payment History | Cronologia completa dei pagamenti / Cronologia pagamenti | `Its details, notes and payment history show up here.` uses "storico dei pagamenti" (1 value) |
| Unlimited bills | Unlimited bills | Bollette illimitate | |
| iCloud Sync | iCloud Sync | Sincronizzazione iCloud | capitalised "Sincronizzazione iCloud" as a feature name |
| Search / Sort / Notes / Share | Search bills / Sort by / Notes / Share bill | Cerca bollette / Ordina per / Note / Condividi bolletta | |
| Billing cycles | Weekly / Bi-weekly / Quarterly / Semi-annual / Custom | Settimanale / Quindicinale / Trimestrale / Semestrale / Personalizzato | "Quindicinale" for Bi-weekly means every 15 days, not strictly "every two weeks" ("bisettimanale" is ambiguous); acceptable |
| Categories (examples) | Streaming / Subscriptions / Utilities / Housing / Insurance | Streaming / Abbonamenti / Utenze / Abitazione / Assicurazione | "Utenze" for Utilities is correct Italian |
| Contracts | Contract / Contract ends | Contratto / Fine contratto | `Contract ending soon` = "Contratto in scadenza"; `Contracts ending soon` = "Contratti in scadenza"; `Contract reminders` = "Promemoria contratto" |
| Auto-pay | Auto-pay | Pagamento automatico | |
| Documents attached to the bill | Manage attachments / DataVault | Gestisci allegati / DataVault | "allegato/allegati"; `Attach PDFs and photos to any bill with Pro.` = "Allega PDF e foto a qualsiasi bolletta con Pro."; `DataVault` left as product name |
| App lock (Face ID) | App Lock | Blocco app | `Require Face ID or Touch ID to open the app.` = "Richiedi Face ID o Touch ID per aprire l'app." |
| Family Sharing | Share with up to 5 family members | Condividi con fino a 5 familiari | "con fino a" is awkward Italian ("fino a 5 familiari" reads better); `via Family Sharing` = "tramite In famiglia" (Apple's Italian name); `Managed by your family organizer.` = "Gestito dall’organizzatore della tua famiglia." |
| Widgets: Next Bill, Horizon, Paid Rhythm (+ Recurring Bills, Week Ahead, Month Progress, Monthly Calendar) | widget names | Prossima bolletta, Orizzonte, Ritmo dei pagamenti (+ Bollette ricorrenti, Prossima settimana, Avanzamento del mese, Calendario mensile) | |
| Free tier | Free plan | Piano gratuito | `Free plan allows up to 3 bills. Upgrade to Pro for unlimited bills.` = "Il piano gratuito consente fino a 3 bollette. Passa a Pro per bollette illimitate."; **Flag:** "Gli utenti free possono allegare 1 documento per bolletta" ("free" left in English) |
| Pro | Pro / AllPaid Pro / Upgrade to Pro | Pro / AllPaid Pro / Passa a Pro | `Unlock AllPaid Pro` = "Sblocca AllPaid Pro"; `Start Pro` = "Inizia con Pro"; `Pro feature` = "Funzione Pro" |
| Lifetime | Lifetime / Buy Lifetime Access | A vita / Acquista accesso a vita | `One-time` = "Una tantum"; `One-time purchase` = "Acquisto singolo"; the Apple ID disclosure says "acquisto unico" (three words for one-time) |
| 7-day free trial | Try Pro free for 7 days | Prova Pro gratis per 7 giorni | `Start free trial` = "Inizia la prova gratuita"; `Try Pro free for %@` = "Prova Pro gratis per %@" |
| Restore Purchases | Restore Purchases | Ripristina acquisti | |

### Paid tier names in the Italian UI (AllPaid)
Pro (`Pro`, `AllPaid Pro`); Mensile / Annuale / A vita (`Lifetime`); `Upgrade to Pro` = "Passa a Pro"; `Unlock` = "Sblocca" and `Unlock AllPaid` = "Sblocca AllPaid" (one verb); trial "Prova Pro gratis per 7 giorni"; cancellation wording mixes "Annulla quando vuoi" (`Cancel anytime`, `Cancel anytime. No charge until the trial ends.` = "Annulla quando vuoi. Nessun addebito fino al termine della prova.") with "Disdici quando vuoi" (`%@ · Cancel anytime.`, `Then %@ · Cancel anytime.`: 2 values; flag); purchase pending "Acquisto in attesa di approvazione. Avrai accesso una volta approvato."; one-time disclosure "Il pagamento sarà addebitato sul tuo ID Apple come acquisto unico. Nessun abbonamento, nessun addebito ricorrente."; restore "Ripristina acquisti".

### Italian App Store listing (checked 2026-11-19)
- Name: **AllPaid – Gestione Bollette** (en dash with spaces; English "AllPaid: Bill Tracker for iPhone & Mac, No Bank Login" is the site title, the English store name is "AllPaid: Bill Tracker"-type, not re-checked).
- Subtitle: **Paga in tempo, senza stress** (a tu-neutral imperative "Paga").
- Category: **Utility** (Apple's Italian label for Utilities). Price "Gratis" with "Acquisti in-app: Sì". Age 4+. Compatible: iPhone and iPad (iOS/iPadOS 17.0+) and Mac (the page lists more platforms). Size 17,8 MB. Languages: "Italiano e altre 33 lingue".
- IAP rows: `AllPaid Pro annuale 14,99 €` · `AllPaid Pro acquisto unico 29,99 €` · `AllPaid Pro mensile 1,99 €`. Store IAP names say Pro; lifetime is "acquisto unico" (the app says "A vita").
- Description (store, tu): "Non dimenticare mai più una bolletta." Headings: "ORA SU IPHONE, IPAD E MAC", "PROMEMORIA CHE MANTENGONO LA CALMA", "ANCHE I CONTRATTI", "IL TUO MESE A COLPO D'OCCHIO", "SEMPRE IN VISTA", "PRIVATO FIN DALL'INIZIO", "GRATIS E PRO". Vocabulary: "scadenza", "Sincronizzazione iCloud", "Data di scadenza passata".

---

### 3. AppMeta (`appmeta`, source `metabuilder/`, ID 6758547802, macOS)

### Italian coverage
- `metabuilder/Localizable.xcstrings`: 2282 / 2300 translatable keys → **99.2 %** (non-stale 2247 / 2265, also 99.2 %). The 18 keys without `it` are all format-only or symbol strings (` "%@"`, `(%lld %@)`, `%`, `%@ — %@`, `%@ — %@ (%@)`, `%@ %@ %@`, `%lld %@`, `$`, `$0`, `0%`, `1D`, `7D`, `30D`, `60D`, `90D`, `P50`, `P95`, `s`). 93 values identical to English (product names, "Pro", "Pro Pack", "Starter Pack", "TestFlight", "Issuer ID", "Key ID", "Provider", "Dashboard", "Copyright").
- No InfoPlist.xcstrings, no widgets, no extensions, no permission prompts; display name "AppMeta" is a brand name.
- **Verdict: app is in Italian: yes** (only format-only keys lack Italian).

### Glossary
| English term on site | English UI string | Italian UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Locales | Locales | Localizzazioni | "localizzazion-" 123 values; lowercase `locales` = "lingue" (29 values) and "locali" 9: **Flag**, mixed. "Localizzazioni" matches Apple's Italian App Store Connect |
| Metadata | Metadata | Metadati | |
| Name / Subtitle / Promotional Text / Description / What's New | same | Nome / Sottotitolo / Testo promozionale / Descrizione / Novità | |
| Keywords | Keywords | Parole chiave | consistent (69 values), no "keyword" |
| Keyword Optimizer | Keyword Optimizer | Ottimizzatore parole chiave | "Keyword Opportunities" = "Opportunità parole chiave", "Keyword Efficiency Dashboard" = "Dashboard efficienza parole chiave" (dropped "di") |
| Difficulty / Demand / Opportunity | same | Difficoltà / Domanda / Opportunità | `Difficulty %lld out of 100` = "Difficoltà %lld su 100" |
| Search coverage | App Store Search Coverage / Coverage | Copertura ricerca App Store / Copertura | |
| Preview changes (diff) | Preview Changes | Anteprima modifiche | `Diff previews and sync simulation` = "Anteprime delle differenze e simulazione di sincronizzazione"; `Diff-first safety` = "Sicurezza basata sulle differenze"; the store text keeps "diff" ("finché non hai visto il diff", "PRIMA IL DIFF, POI L'INVIO") |
| Push | Push / Push All / Push Changes | Pubblica / Pubblica tutto / Pubblica modifiche | "Pubblica" 72 values vs "Invia" 6: `Submit` = "Invia"; the store text says "invio" ("PRIMA IL DIFF, POI L'INVIO") |
| Refresh | Refresh | Aggiorna | |
| Fetch | Fetch / Fetch apps from App Store Connect | Recupera / Scarica le app da App Store Connect | **Flag:** "Recupera" 38 values vs "Scarica" 26 for the same action (`Fetch latest data from App Store Connect (⌘R)` = "Scarica gli ultimi dati…", `Fetch last 3 days of sales data` = "Recupera gli ultimi 3 giorni…") |
| Bulk actions | Bulk Actions / Bulk Copy | Azioni in blocco / Copia in blocco | |
| AI translation | AI Translation / Translate | Traduzione AI / Traduci | **Flag:** "AI" (57 values) in the app, "IA" in the store text ("provider di IA") and in AppMeta Pulse (25 values) |
| AI provider | Provider / Default Provider | Provider / Provider predefinito | `Use Your Own API Key` = "Usa la tua chiave API"; "chiave API" 17 values vs "API key" 4 (e.g. "Impossibile codificare la API key") |
| AI credits | AI Credits / Buy Credits / Starter Pack / Pro Pack | Crediti AI / Acquista crediti / Starter Pack / Pro Pack | `AppMeta AI Credits` = "Crediti AppMeta AI" |
| Apple Intelligence | Apple Intelligence | Apple Intelligence | |
| Submit for review | Submit for Review | Invia per la revisione | `This version cannot be submitted for review…` = "…non può essere inviata alla revisione…" (two prepositions) |
| App Review Information | App Review Information | Informazioni per la revisione dell'app | |
| Phased release / Age rating / Availability / Pricing | same | Rilascio graduale / Fascia d'età / Disponibilità / Prezzi | `Release to All` = "Rilascia a tutti" |
| Reviews / Ratings | Reviews / Ratings / Rating | Recensioni / Valutazioni / Valutazione | clean distinction |
| TestFlight / What to Test | same | TestFlight / Cosa testare | |
| In-App Purchases / Subscription Groups | same | Acquisti in-app / Gruppi di abbonamenti | "Acquisti in-app" is Apple's Italian term |
| Game Center Achievements / Leaderboards | Achievements / Leaderboards | Obiettivi / Classifiche | |
| Sales and Analytics | Sales / Analytics | Vendite / Analisi | "Analisi" 23 values; "Analytics" never left in English; `Sales & Trends` = "Vendite e tendenze" (consistent: `Open Sales & Trends` = "Apri Vendite e tendenze"; `Click Sales and Trends` = "Fai clic su Vendite e tendenze"; vendor-number help text "sotto Vendite e tendenze") |
| Diagnostics | Diagnostics | Diagnostica | |
| Screenshots | Screenshots | Screenshot | the store text also says "screenshot" |
| Issuer ID / Key ID | same | Issuer ID / Key ID | left English (`Different from the Issuer ID.` = "Diverso dall'Issuer ID.") |
| Territories | Territories | Territori | |
| Dashboard | Dashboard | Dashboard | `Open Dashboard` = "Apri dashboard" (lowercase mid-sentence) |
| Demo mode | Demo Mode | Modalità demo | `Demo (Free)` = "Demo (gratuita)"; `Explore Demo Mode` = "Esplora la Modalità demo" (capital M mid-sentence); the store text says "La Modalità demo" |
| Pro | Pro / AppMeta Pro / Unlock Pro | Pro / AppMeta Pro / Sblocca Pro | `Upgrade to Pro` = "Passa a Pro"; `Unlock AppMeta Pro` = "Sblocca AppMeta Pro" |
| Yearly / Lifetime | Yearly / Lifetime | Annuale / A vita | `Auto-renews yearly` = "Si rinnova automaticamente ogni anno"; `Most popular` = "Più popolare"; `Best Value` = "Conveniente"; `Pays off after ~%lld years` = "Si ripaga dopo circa %lld anni"; `Unlock Lifetime — %@` = "Sblocca a vita — %@" |
| Restore Purchases | Restore Purchases | Ripristina acquisti | `Manage Subscription` = "Gestisci abbonamento" |
| Add | Add | Aggiungi | consistent |

### Paid tier names in the Italian UI (AppMeta)
**AppMeta Pro** (`Pro`, `AppMeta Pro`); periods "Annuale" (`Yearly`) and "A vita" (`Lifetime`); no monthly plan; no free trial in the app (the `Free Trial` string is an analytics label = "Prova gratuita"). Paywall verbs: "Sblocca AppMeta Pro", "Passa a Pro", "Sblocca a vita — %@". Demo mode is free: "Demo (gratuita)". `Pay once, own forever` = "Paghi una volta, è tuo per sempre" (indicative "Paghi", unlike the imperative style used elsewhere).

### Italian App Store listing (checked 2026-11-19)
- Name: **AppMeta for App Store Connect** (identical to English, not translated).
- Subtitle: **ASO, metadati e recensioni** (English "Metadata & ASO Tools").
- Category: **Utility**. Mac only (macOS 14.0+); lookup `kind` = `mac-software`. Price "Gratis" (formattedPrice; in-app purchases). Age 4+. Size 9,8 MB. Languages: "Italiano e altre 10 lingue".
- IAP rows (this page prints them with only the two paid IAPs): `AppMeta Yearly 19,99 €` · `AppMeta Acquisto singolo 34,99 €`. **Flag:** "Yearly" display name not localized in the Italian store (English word), and "AppMeta Acquisto singolo" has no "Lifetime/a vita" word.
- Description (store, tu): "Un incolla sbagliato può pubblicare un campo parole chiave rovinato in una lingua che non sai leggere." Headings: "PRIMA IL DIFF, POI L'INVIO", "TRADUCI LA TUA SCHEDA", "PAROLE CHIAVE CON LE PROVE IN VISTA", "OLTRE LA SCHEDA", "FUNZIONA SUL TUO MAC", "PROVA TUTTO PRIMA". Vocabulary: "scheda App Store" (listing), "localizzate", "provider di IA", "Acquisti in-app e abbonamenti", "Preparazione all'invio", "Game Center: classifiche e obiettivi", "Recensioni da tutti gli Store", "grafici di vendite e analisi".

---

### 4. AppMeta Pulse (`appmeta-pulse`, source `metabuilder_phone/`, ID 6758788164)

### Italian coverage
- Main `metabuilder_phone/Localizable.xcstrings`: 1418 / 1418 → **100 %** (non-stale 1415 / 1415; 25 values identical to English, e.g. "MRR", "Funnel", "App Store Connect", "Account").
- `AppShortcuts.xcstrings` (Siri phrases): 3 / 3 keys carry a translated stringSet in `it`: "Apri ${applicationName} | Mostra il fatturato di oggi in ${applicationName} | Vendite di oggi in ${applicationName}"; "Mostra le analisi in ${applicationName} | Conversione dell’App Store in ${applicationName}"; "Mostra gli abbonati in ${applicationName} | Abbonamenti attivi in ${applicationName}". Siri phrases ARE in Italian (preposition "in", unlike AfterShift's "su").
- Widget `AppMetaPulseWidget/Localizable.xcstrings`: 256 / 256 → **100 %** (11 identical).
- No InfoPlist.xcstrings; display names "AppMeta Pulse" / "AppMeta Pulse Widget" are brand names; no permission prompts.
- **Verdict: app is in Italian: yes.**

### Glossary
| English term on site | English UI string | Italian UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Dashboard | Dashboard | Dashboard | `Start` = "Inizio" is the date-range label, not a tab; widget `Dashboard locked` = "Dashboard bloccata"; `Open Dashboard` = "Apri dashboard" |
| Apps | Apps | App | |
| Analytics | Analytics | Analisi | "Analisi" 41 values; no "Analytics" left in English |
| Reviews | Reviews | Recensioni | "Recension-" 74 values; `Reply` = "Risposta"; `Reply to this review` = "Rispondi a questa recensione" |
| Settings | Settings | Impostazioni | |
| Proceeds | Proceeds | Ricavi | clean distinction from Revenue = "Fatturato" (better than Spanish): "ricavi" 23 values (Proceeds), "fatturato" 8 (Revenue, e.g. "Fatturato di oggi", `Revenue & proceeds` = "Fatturato e ricavi"). The Siri phrase "Mostra il fatturato di oggi" maps to the revenue value |
| Sales | Sales | Vendite | |
| Units | Units | Unità | |
| Revenue | Revenue | Fatturato | see Proceeds |
| MRR | MRR | MRR | |
| Active subscriptions | Active Subscriptions / Active Subs | Abbonamenti attivi / Abb. attivi | `Subscription Status` = "Stato dell’abbonamento"; "Abbonati attivi" for active subscribers in help text |
| Trials | Trials / Active Trials | Prove / Prove attive | |
| Trial-to-paid conversion | Trial → Paid / Conversion | Prova → Abb. / Conversione | `Conversion Rate` = "Tasso di conversione" |
| Churn | Monthly Churn / Churn /mo | Churn mensile / Churn/mese | "churn" left in English (5 values); no "tasso di abbandono" |
| Cancellations | Cancels / Cancelled | Annullati / Annullati | |
| New subscriptions | New Subs | Nuovi abb. | |
| Downloads / Impressions / Product page views | Downloads / Impressions / Product Page Views | Download / Impressioni / Visualizz. pagina | |
| Top territories | Top Territories | Principali Paesi e regioni | capital P in "Paesi" mid-phrase |
| Trend comparison | Compare / Previous period / Last year / Custom Range | Confronta / Periodo precedente / Anno scorso / Intervallo personalizzato | `Compare with last year` = "Confronta con l’anno scorso" vs `Compare with Previous Year` = "Confronta con l’anno precedente" |
| Goals | Goals / Monthly Goal | Obiettivi / Obiettivo mensile | "obiettivo di ricavi mensili" |
| iCloud sync | iCloud Sync | Sincronizzazione iCloud | same wording as AllPaid |
| AI review reply drafts | Draft suggestions / AI draft per review | Bozze suggerite / Bozza IA per recensione | "Le bozze basate sull’IA" |
| Reply templates | Templates | Modelli | `Add template` = "Aggiungi modello", `Edit Template` = "Modifica modello", `Restore default templates` = "Ripristina modelli predefiniti" |
| Display currency | Convert to your preferred currency | Converti nella valuta che preferisci | `Currency` = "Valuta"; `Display` = "Visualizzazione" |
| Funnel | Funnel | Funnel | `Funnel by App` = "Funnel per app" (English left, no "imbuto") |
| Ledger (widget) | Ledger | Riepilogo | `Dashboard and Ledger widgets…` = "I widget Dashboard e Riepilogo…" |
| Demo mode | Try with sample data / Demo Mode | Prova con dati di esempio / Modalità demo | same word as AppMeta ("Modalità demo") |
| Widgets | Home Screen widgets | Widget della schermata Home | widget `Proceeds (Lock Screen)` = "Ricavi (Schermata di blocco)" |
| AI assistant (MCP) | Ask your AI assistant | Chiedi al tuo assistente IA | `AI Assistants` = "Assistenti IA"; "IA" 25 values, 0 "AI" (AppMeta says "AI") |
| Year over year | Year-over-year | (compare with last year) | no standalone key; wording "il confronto da un anno all’altro" in the help text |
| Reports | (report) | resoconti | "resoconto" 99 values, never "report" in the app; the store text says "report di App Store Connect" |
| Paywall bullets | Full access to revenue & subscription metrics / Per-app performance breakdowns / Trends and historical insights / All future updates included | Accesso completo alle metriche di fatturato e abbonamenti / Dettaglio delle prestazioni per app / Tendenze e approfondimenti storici / Tutti gli aggiornamenti futuri inclusi | |
| Pro (site plan name) | no UI string | n/a | the app never says "Pro"; gating is "Sblocca AppMeta Pulse" |
| Monthly / Yearly / Lifetime | Monthly / Yearly / Lifetime | Mensile / Annuale / A vita | `One-time purchase · Use forever` = "Acquisto una tantum · Usala per sempre"; `Best Value` = "Più conveniente"; `Billed monthly` = "Addebito mensile" |
| Free trial | Start Free Trial | Inizia la prova gratuita | `Billed yearly · Free trial included` = "Addebito annuale · Prova gratuita inclusa"; `No charge during your free trial` = "Nessun addebito durante la prova gratuita" |
| Restore Purchases | Restore Purchase / Restore Purchases | Ripristina acquisti / Ripristina acquisti | both plural (no singular flag unlike Spanish) |

### Paid tier names in the Italian UI (Pulse)
No tier name: the whole app is gated. Strings: "Sblocca AppMeta Pulse", "Sblocca l’accesso a vita" (`Unlock Lifetime Access`), `Subscribe` = "Abbonati"; periods Mensile / Annuale / A vita; trial "Inizia la prova gratuita"; restore "Ripristina acquisti" (paywall and settings). The store IAP names use "accesso a vita / annuale / mensile" ("AppMeta Pulse: accesso a vita"), the app says "A vita" / "accesso a vita".

### Italian App Store listing (checked 2026-11-19)
- Name: **AppMeta Pulse: Vendite di app** (English "AppMeta Pulse: App Sales & MRR").
- Subtitle: **Risposte IA alle recensioni** (English "Revenue & AI Review Replies"; the Italian keeps only the reply half).
- Category: **Economia** (English: Business). Compatible: iPhone (iOS 17.0+), Mac (macOS 14.0+), and more platform rows; the description says "e ora anche sul Mac". Price "Gratis" with "Acquisti in-app: Sì". Age 4+. Size 26,3 MB. Languages: "Italiano e altre 14 lingue".
- IAP rows: `AppMeta Pulse: accesso a vita 14,99 €` · `AppMeta Pulse: accesso annuale 6,99 €` · `AppMeta Pulse: accesso mensile 0,99 €` (colon after the app name, unlike the Spanish store).
- Description (store, tu): "Le vendite App Store, l'MRR e le recensioni sul tuo iPhone, e ora anche sul Mac." Headings: "IL TUO STORICO, CONSERVATO PER SEMPRE", "NOVITÀ: PULSE PER MAC", "NOVITÀ: CHIEDI AL TUO ASSISTENTE IA", "RISPONDI ALLE RECENSIONI", "12 WIDGET", "UN OBIETTIVO PER IL MESE", "NOVITÀ: MODALITÀ CHIARA", "14 LINGUE", "COSA TI SERVE". Vocabulary: "storico" (history, 1 app value "storico delle vendite"), "report di App Store Connect", "assistente IA".

---

### 5. Chessful (`chessful`, source `Chessful/`, ID 6761336870)

### Italian coverage
- `Localizable.xcstrings`: 2146 / 2146 → **100 %** (non-stale 2113 / 2113; 71 values identical to English: "Stockfish", "En passant", "Premium", notation).
- `Lessons.xcstrings`: 3649 / 3649 → 100 % (15 identical).
- `InfoPlist.xcstrings`: 2 / 2 → 100 % (`CFBundleDisplayName`/`CFBundleName` "Chessful", no permission prompts).
- No widget, watch, App Intents or AppShortcuts catalogs.
- **Verdict: app is in Italian: yes.**

### Glossary
| English term on site | English UI string | Italian UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Dashboard (tab) | Dashboard | Panoramica | not "Dashboard" (AppMeta/Pulse keep the English word) |
| Play (tab) | Play | Gioca | |
| Analysis (tab) | Analysis | Analisi | |
| Training (tab) | Training | Allenamento | |
| Learn (tab) | Learn | Impara | |
| Progress | Progress | Progresso | |
| Game review | Game Review | Revisione | `Review Game` = "Rivedi partita"; `Game Analysis…` = "Analisi della partita…"; `Analyze Game` = "Analizza" |
| Accuracy | Accuracy | Precisione | |
| Key moments | Key Moments | Momenti chiave | |
| Blunder / Mistake / Inaccuracy | same | Svista / Errore / Imprecisione | "svista" only 1 other value; `Mistake Detail` = "Dettaglio"; `Mistake Hunter` = "Cacciatore di errori" |
| Better move | See the better move / Best move | Vedi la mossa migliore / Mossa migliore | "mossa/mosse" in 224 values, no "giocata" beyond 2 |
| Today's training | Today's Training | Allenamento di oggi | |
| Train your weaknesses | Train Your Weaknesses | Allena le tue debolezze | tu; `Train your weaknesses daily` = "Allena le tue debolezze ogni giorno" |
| Skills (5 dimensions) | Skills | Abilità | |
| Tactics / Defense / Positional / Openings / Endgames | same | Tattica / Difesa / Posizionale / Aperture / Finali | "aperture" is the Italian chess term |
| Opening repertoire | Opening Repertoire | Repertorio di aperture | |
| 40 AI opponents | 40 Unique Opponents | 40 avversari unici | levels Beginner / Intermediate / Advanced / Master = Principiante / Intermedio / Avanzato / Maestro; "avversari/o" 62 values |
| Import games | Import Games / Import from PGN | Importa partite / Importa da PGN | `Analyze All` = "Analizza tutto" |
| Weekly comparison / Weakness trends | same | Confronto settimanale / Trend delle debolezze | "Trend" vs "tendenze" used elsewhere (AfterShift, AllPaid) |
| Rating / Elo | Rating | Valutazione | **Flag:** `Rating` = "Valutazione" but `Rating Over Time` = "Rating nel tempo", "Rating dei puzzle", "Il tuo rating" (English left in 8+ values); Elo printed as "%lld ELO" (all caps, 3 values) while the English store says "Elo"; "punteggio" 9 values |
| Achievements | Achievements | Traguardi | AppMeta (Game Center) says "Obiettivi" |
| 3D board | 3D Board / Board Style | Scacchiera 3D / Stile scacchiera | `Classic 2D` = "Classico 2D" |
| Puzzles | puzzle(s) | Puzzle (invariable) | "puzzle" 31 values vs "problemi" 4 vs "esercizi" 12; `Drill one skill with puzzles from your own mistakes.` = "Allena una sola abilità con problemi tratti dai tuoi errori." and `Play a game…` = "…diventano esercizi personalizzati" (**Flag:** three words); the store text says "esercizi" |
| Back-rank | Back-Rank Weakness | Matto sull’ultima traversa mancato | "ultima traversa" 26 values, "corridoio" 1; the store text uses the same «Matto sull’ultima traversa mancato» |
| Fork | A fork | Una forchetta / forchetta | consistent ("forchett-" 16 values, "doppio attacco" for `Missed a double attack`) |
| Free | Free Plan | Piano gratuito | |
| Pro (site) | Chessful Premium / Upgrade to Premium | app: Premium ("Chessful Premium", "Passa a Premium"); store: **Pro** ("Chessful Pro annuale") | owner decision 2026-11-08: the site says **Pro**; the app UI still says Premium (8 values) until the app fix (Kanban) |
| Monthly / Yearly / Lifetime | same | Mensile / Annuale / A vita | `Purchase Lifetime` = "Acquista a vita" |
| Free trial | Start Free Trial | Prova gratuita | `%@ free trial` = "%@ di prova gratuita"; the trial is 1 week (master), so the site uses the {TRIAL} token |
| Restore Purchases | Restore Purchases | Ripristina acquisti | `Already subscribed? Restore Purchases` = "Già abbonato? Ripristina acquisti" |
| Hint / Resign / New game | Hint / Resign / New Game | Suggerimento / Abbandona / Nuova partita | |
| Stockfish | Stockfish | Stockfish | |
| Streak | Streak / Day Streak | Serie | `%lld day streak` = "Serie di %lld giorni" |
| Tips / support | Tips help keep development going | Le mance aiutano a continuare lo sviluppo | "mance" 3 values; `Support the Developer` = "Supporta lo sviluppatore" vs store "Sostieni lo sviluppatore" (AfterShift store IAP) |

### Paid tier names in the Italian UI (Chessful)
App: **Premium** ("Chessful Premium", "Passa a Premium", "Premium. Apre la schermata di upgrade."; "upgrade" left in English); periods Mensile / Annuale / A vita; "Prova gratuita" (trial length via StoreKit at runtime). Store IAP names: **Chessful Pro mensile / annuale / acquisto unico** plus tips "Offri un caffè" / "Sostenitore" / "Grande sostegno". Owner decision 2026-11-08: the paid tier is **Pro** on the site.

### Italian App Store listing (checked 2026-11-19)
- Name: **Chessful: Allena & Analizza** (English "Chessful: Train & Analyze"); "Allena" is a tu imperative, `&` as in English.
- Subtitle: **Coach scacchi: tattica, puzzle** (English "Chess tactics, puzzles, coach"). "Coach" is left in English.
- Category: **Giochi da tavolo**. Price "Gratis" with "Acquisti in-app: Sì". Age 4+. Compatible: iPhone (iOS 18.0+), iPad (iPadOS 18.0+), Mac, more. Size 199,5 MB. Languages: "Italiano e altre 32 lingue".
- IAP rows: `Chessful Pro mensile 2,99 €` · `Chessful Pro annuale 17,99 €` · `Grande sostegno 9,99 €` · `Sostenitore 5,99 €` · `Offri un caffè 1,99 €` · `Chessful Pro acquisto unico 29,99 €`.
- Description (store, tu): "Hai perso la partita e non sai quale mossa l’ha decisa. Chessful lo sa." Headings: "Scopri cosa è andato storto", "Porta la cronologia delle tue partite", "Più da esercitare". Vocabulary: "esercizi", "errori", «Matto sull’ultima traversa mancato», «Analizza tutto», "file PGN", "Stockfish", "linguaggio semplice".

---

### Cross-app terms (this batch)
| Concept | Values seen | Recommendation |
|---|---|---|
| Restore Purchases | Ripristina acquisti (all five) | consistent |
| Lifetime | A vita (all five); store IAPs: "acquisto singolo" (AfterShift, AppMeta), "acquisto unico" (AllPaid, Chessful), "accesso a vita" (Pulse); AfterShift/AllPaid UI also "Acquisto una tantum" / "Acquisto singolo" / "acquisto unico" | app wording is "A vita"; store wording varies, use per app |
| Monthly / Yearly | Mensile / Annuale (all) | consistent |
| Unlock | Sblocca (AfterShift, AllPaid, AppMeta, Pulse) | consistent; Chessful says "Passa a Premium" |
| Free trial | Prova gratuita (all); AllPaid/AfterShift "Prova Pro gratis per 7 giorni" / "gratis per 7 giorni" | consistent |
| Reviews | Recensioni (AppMeta, Pulse) | consistent |
| Ratings | Valutazioni (AppMeta); Chessful "Rating"/"Valutazione" mixed | note |
| Analytics | Analisi (AppMeta, Pulse, AllPaid "Analisi delle spese", Chessful tab) | consistent |
| Dashboard | Dashboard (AppMeta, Pulse); Panoramica (Chessful tab) | choose per app |
| iCloud Sync | Sincronizzazione iCloud (AllPaid, Pulse) | consistent |
| Free tier | Piano gratuito (AllPaid, Chessful) | consistent |
| Add | Aggiungi (AllPaid, AppMeta, Pulse, AfterShift) | consistent |
| Report | "report" (AfterShift 8, AppMeta Pulse store) vs "rapporto" (AfterShift 2) vs "resoconto" (Pulse 99) | no single word; per app |
| AI | "AI" (AppMeta 57) vs "IA" (Pulse 25, AppMeta store text) | mixed across apps; Italian standard is "IA" |
| In-app purchases | Acquisti in-app (AppMeta, all store listings) | consistent |
| Settings | Impostazioni (all five) | consistent |
| Apple ID | "ID Apple" (AfterShift, AllPaid) | Apple's Italian form; use it |
| Family Sharing | "In famiglia" (AllPaid iOS string "tramite In famiglia") | Apple's Italian name |
| Cancel anytime | Annulla quando vuoi (AfterShift, AllPaid) / Disdici quando vuoi (AllPaid 2 values) | pick "Annulla quando vuoi" |
| Formality | tu in all five (no Lei) | site writes tu; no register mix between apps |
| Bills | Bollette (AllPaid) | consistent |

### Flags
1. **AfterShift mixed terms for the same concepts:** roster ("Turni" tab vs "turnario" vs store "turnazione"), caffeine timing ("Orari della caffeina", "Timing della caffeina", "Orari caffeina", "Stop caffeina"), readiness ("Stato di recupero" vs "Prontezza al turno" / "La prontezza dovrebbe migliorare" / "Recupero bloccato"), wind-down ("Rilassamento", "Tempo di rilassamento", "Rallenta"), nap ("pisolino" 76 vs "sonnellino" 14), report ("report" 8 vs "rapporto" 2, incl. PDF filename "AfterShift-Rapporto-%@.pdf"). English left in: "body scan" (`playbook.step.windDown.title`), "Upgrade" (`calendar.upgradeAutoSync`), "Timing" (`technique.caffeineTiming.title`). `paywall.bestValue` "Miglior valore" is a calque. `paywall.purchasePendingMessage` drops the "you'll get access once confirmed" half. `roster.tapToAdd` drops "or set up a repeating rotation". The site must pick one term per concept.
2. **AfterShift calendar permission prompts are English-only** (`NSCalendarsUsageDescription`, `NSCalendarsFullAccessUsageDescription` are build settings with no localization): an Italian device sees English. App-side fix; file in ISSUES.md if the owner agrees.
3. **AllPaid Siri phrases are English-only** (no AppShortcuts localization; `BillsDueIntent.swift`). Do not promise Italian Siri phrases on the AllPaid page.
4. **AllPaid string defects:** "Segna come pagato" vs "Segna come pagata" vs "contrassegnare come pagata"; "Annulla" for both Undo and Cancel; "Disdici quando vuoi" (2) vs "Annulla quando vuoi"; "Gli utenti free" (English "free"); "acquisto singolo" / "acquisto unico" / "una tantum" for the one-time purchase; `NSFaceIDUsageDescription` "Richiedi Face ID o Touch ID per aprire l'app." is the settings toggle text, not a permission sentence (should read like "AllPaid richiede Face ID o Touch ID per aprire l'app."); "Condividi con fino a 5 familiari" is awkward.
5. **AppMeta:** "Localizzazioni" (123) vs "lingue" (29) vs "locali" (9) for locales; "Recupera" (38) vs "Scarica" (26) for Fetch; "chiave API" vs "API key" ("Impossibile codificare la API key"); "AI" in the app vs "IA" in the store text and Pulse; `Issuer ID` / `Key ID` left English; "Invia per la revisione" / "inviata alla revisione" preposition mix; store IAP "AppMeta Yearly" is not localized and "AppMeta Acquisto singolo" has no lifetime word; `Pay once, own forever` is indicative ("Paghi una volta") while the rest is imperative.
6. **AppMeta Pulse:** "IA" here vs "AI" in AppMeta; "report" in the store text vs "resoconti" (99) in the app; "churn" and "Funnel" left in English; "Ricavi" / "Fatturato" is a good Proceeds / Revenue split (keep), but the store subtitle "Risposte IA alle recensioni" drops the revenue half of the English "Revenue & AI Review Replies"; "Principali Paesi e regioni" capital P; "Confronta con l’anno scorso" vs "…l’anno precedente".
7. **Chessful term mixes:** "Rating" left in English in 8+ values and `Rating` itself = "Valutazione" (and "punteggio" 9), "ELO" (all caps) vs Elo in English store text; "puzzle" (31) vs "problemi" (4) vs "esercizi" (12); "Trend delle debolezze" vs "tendenze" elsewhere; "Traguardi" (Chessful achievements) vs "Obiettivi" (AppMeta Game Center); the app still says Premium (8 values, "Passa a Premium", "upgrade" left English) while the store and the site say Pro (Kanban item). Store name "Chessful: Allena & Analizza" uses a tu imperative and the store subtitle leaves "Coach" in English. Stale 3-day trial strings may remain in the catalog (the trial is 1 week per the master).
8. **No Lei anywhere**, and all five apps are 99 to 100 % Italian: nothing missing beyond the AfterShift calendar prompts, AllPaid Siri phrases and AppMeta's 18 format-only keys. Counts differ from earlier sheets because the catalogs have grown. Prices must still come from `MASTER-prices.csv`.


---

## Italian glossary, batch 2: earnlock, gymlogger-x, liftlog, mediakit, millrace

Method (checked 2026-11-19, nothing modified outside this file): coverage was counted with `python3 -I` over each app's `.xcstrings` catalogs (`strings` → key → `localizations.it` → `stringUnit` / `variations` / `stringSet`; keys with `shouldTranslate: false` and blank keys excluded; a key counts as translated when every unit is in state `translated`). Worktrees, `.build`, DerivedData and Pods were ignored. Locale code is plain `it` in every catalog (no `it-IT` column anywhere; **Millrace has `it`, unlike Spanish where it used `es-ES`**). GymLogger X has no `.xcstrings`: its JSON files `GymLogger/GymLogger/Localizations/it.json`, `GymLoggerWidget/Localizations/it.json` and `GymLoggerWatch Watch App/Localizations/it.json` were compared key by key with `en.json`, and `GymLogger/it.lproj/InfoPlist.strings` was read. Italian strings are copied verbatim (plural variations shown as `one:` / `other:` / `many:`), keeping each catalog's apostrophes (straight `'` and curly `’` are mixed inside several catalogs). Register counts are rough regex counts of tu markers (tu/tuo/tua/ti/te, `hai`, `vuoi`, `puoi`, tu imperatives such as `Tocca`, `Scegli`, `Aggiungi`) versus Lei markers (`Lei`, `Suo/Sua`, `Selezioni`, `Inserisca`, `Scelga`, `Tocchi`, `Può`); hits were checked by hand. App Store data: iTunes lookup (`country=it&lang=it_it`) plus the raw `serialized-server-data` JSON of `https://apps.apple.com/it/app/id<ID>` (Safari UA, `Accept-Language: it-IT`, redirect followed, 429s retried after 30 s until 200). The seller block of the store page was not copied. Prices are reference only (the store prints `22,99 €` with a non-breaking space before the euro sign; the free download is `Gratis`). The Spanish glossary `_i18n/es-glossary.md` (batch 2) was the row checklist; the master file was not consulted (out of scope).

Headline flags for the whole batch:
- **All five apps are in Italian and all five address the user with tu.** No Lei string anywhere except one false hit (`Può essere attivo un solo programma alla volta.` in LiftLog is impersonal, not Lei). The site can write tu and quote the UI without a register clash.
- **"Serie" is both "streak" and "sets" in three apps.** EarnLock (`Serie attuale`, `Scudi serie`), LiftLog (`Streak` = `Serie`, `Sets` = `Serie`, `Best run` = `Miglior serie`) and Millrace (`Serie attuale`, `Ricompense serie`) all use `serie` for a streak, while GymLogger X and LiftLog use `Serie` for a set of reps. In LiftLog the two meanings sit side by side (`Serie migliore` = Best Set, `Miglior serie` = Best run). Site copy should pick `serie` for sets and a different word for streak, or quote the UI and explain.
- **LiftLog tier names differ between app and store in two tiers:** in-app `Equo` / `Bene` / `Generoso` / `Sostenitore` against store IAP `Equo` / `Buono` / `Generoso` / `Mecenate`. `Bene` is an adverb ("well") and reads wrong as a tier label; and the in-app `Supporter` key also translates to `Sostenitore` (same word as `Patron`).
- **GymLogger X leaves the tab title `Home` in English** (`home_title`, `info.home.title`) and keeps `Apple Health` in 10 in-app strings, while its permission prompt says `Apple Salute`. Five Program Creator strings lack their accents (`velocita`, `piu`).
- **LiftLog has 8 user-visible English fallbacks** in the main app (the same 8 as in Spanish); the widget catalog has Italian for them (`Media`, `Record`, `Miglior serie`, `Per mese`, `Per giorno della settimana`, `Media sett.`). The Siri hint tells Italian users to say the English phrases.
- **Store names, subtitles and IAP names differ from the in-app terms in several places:** `Mecenate` / `Buono` (LiftLog), `una tantum` (EarnLock, GymLogger X) against `acquisto unico` (MediaKit) and `Pagamento unico` / `Acquisti una tantum` (Millrace), and `Condivisione in famiglia` in two store descriptions against `In famiglia` in the apps.

---

### 1. EarnLock (earnlock, source `EarnScreen`, ID 6771099230, has an Apple Watch app)

#### Italian coverage

| Catalog | Keys | `it` present | `it` translated | % |
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

All Localizable catalogs together: 815 keys, 815 translated (100%), identical to the Spanish figures.

English-only or unreviewed: the three permission prompts (HealthKit read, HealthKit write, Photo Library add) have Italian text but are `needs_review`: `EarnLock legge i tuoi passi, i minuti di attività e l'energia attiva dall'app Salute per monitorare i progressi verso l'obiettivo che sblocca le tue app bloccate. Questi dati non lasciano mai il tuo dispositivo.` / `EarnLock si limita a leggere i tuoi dati di attività: non scrive nulla nell'app Salute. Apple richiede questa autorizzazione perché il framework HealthKit può tecnicamente scrivere dati.` / `Ti permette di salvare una scheda traguardo nella libreria Foto. EarnLock non legge mai le tue foto.` `CFBundleDisplayName` / `CFBundleName` have no `it` entry (name stays "EarnLock"). Siri / App Shortcuts phrases are Italian and `translated` (9 phrases, e.g. `Qual è il mio obiettivo in ${applicationName}`, `Quanto manca per sbloccare in ${applicationName}`, `Avvia una sessione di concentrazione in ${applicationName}`, `Blocca le mie app in ${applicationName}`, `Inizia a concentrarti con ${applicationName}`).

**Apple Watch app (Italian):** `watchkitapp Watch App/Localizable.xcstrings` is 28 of 28 translated (`Apri EarnLock su iPhone`, `Apri l'app su iPhone per l'upgrade.`, `Cammina per iniziare a tracciare`, `Logged. Take a breath.` = `Registrato. Fai un respiro.`, `Serve Apple Salute`, `EarnLock è Premium`); the complications catalog is 13 of 13 (`%@ per sbloccare`, `Progressi verso lo sblocco di oggi.`). The Watch InfoPlist health prompts are `needs_review`. The Watch wording is the same register (tu) as the phone.

**Verdict: app is in Italian: yes** (100% of every Localizable catalog, widgets, Live Activity, shield, Watch and Siri phrases; only the permission prompts are `needs_review`).

Register: tu. 93 of 777 strings carry tu markers (`Tocca per fare l'upgrade.`, `Guadagnati l'accesso`, `Cosa speravi di trovare?`), 0 Lei strings.

Wording flags:
- Screen Time as Apple's feature is `Tempo di utilizzo` (Apple's Italian name), but the concept "screen time" is written two ways: `tempo allo schermo` (`Tempo allo schermo risparmiato (stimato)`, `Con cosa vuoi guadagnare il tempo allo schermo?`) and `tempo di schermo` (`Guadagna tempo di schermo raggiungendo gli obiettivi di attività quotidiani.`).
- Lock Screen widget title is `EarnLock — Schermata Blocco`, another string says `schermata Blocco`; Apple's Italian iOS term is "schermata di blocco".
- Shadow Mode: `modalità osservazione` / `settimana di osservazione` everywhere except one error string: `Impossibile tracciare Shadow Mode` (English left in).
- Two different words for smart schedules: `Pianificazioni intelligenti` (key `Smart Schedules`) and `Pianificazioni smart` (key `Smart schedules`, and `Pianificazioni smart + icone personalizzate`).
- Streak is `Serie` (`Serie attuale`, `Scudi serie`, widget `EarnLock — Serie`), which is also the Italian word for sets; see the batch headline.
- `Scegli A vita` (capital A mid-sentence) for `Get Lifetime`.
- Free-trial strings: `Inizia la prova gratuita`, `Prova gratuita di 7 giorni, poi %@/anno`, `Prova gratuita di 7 giorni, poi %@/mese` (consistent, unlike Spanish).
- Free plan: `Il piano gratis blocca 1 app.` and `Il piano gratuito blocca un'app.` (`gratis` and `gratuito` for the same thing).
- Apostrophes: the Watch catalog uses curly `’` (`Apri l’app su iPhone per sincronizzare questo orologio.`), the phone app straight `'`.
- Family Sharing: `In famiglia` (Apple's Italian name) inside a sentence: `Supporta In famiglia — Premium si sblocca per un massimo di cinque membri del tuo gruppo Famiglia Apple.` (capital I mid-sentence).
- `Apple Salute` throughout (and `app Salute` / `Salute` in prompts); Apple's own app is "Salute", so `Apple Salute` is a calque but consistent.

#### Glossary

| English term on site | English UI string (key) | Italian UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Free (tier) | `Free forever for one app. Go further with Premium.`; `Free plan locks 1 app. Tap to upgrade.`; `Free locks one app. Premium has no limit.` | `Sempre gratis per un'app. Vai oltre con Premium.`; `Il piano gratis blocca 1 app. Tocca per fare l'upgrade.`; `Il piano gratuito blocca un'app. Premium senza limiti.` | No standalone "Free" string; `gratis` and `gratuito` both used. |
| Premium | `Premium` | `Premium` | |
| Monthly | `Monthly` | `Mensile` | |
| Yearly | `Yearly` | `Annuale` | |
| Lifetime | `Lifetime` | `A vita` | `Get Lifetime` → `Scegli A vita`. Store IAP: `EarnLock Premium una tantum`. |
| Get Premium (button) | `Get Premium` | `Passa a Premium` | tu imperative. |
| Start free trial (button) | `Start free trial` | `Inizia la prova gratuita` | |
| 7-day free trial | `7-day free trial, then %@/year`; `7-day free trial, then %@/month` | `Prova gratuita di 7 giorni, poi %@/anno`; `Prova gratuita di 7 giorni, poi %@/mese` | One pattern. |
| Restore Purchases | `Restore Purchases` | `Ripristina acquisti` | |
| Today tab (site says "Home screen") | `Today`; `Go to Today` | `Oggi`; `Vai a Oggi` | |
| Insights tab | `Insights` | `Analisi` | |
| Insights Day / Week / Month | `Day` / `Week` / `Month` | `Giorno` / `Settimana` / `Mese` | |
| Settings tab | `Settings` | `Impostazioni` | |
| Shadow Week | `Run another Shadow Week`; `No Shadow Weeks yet`; `Compared with your previous Shadow Week.` | `Fai un'altra settimana di osservazione`; `Ancora nessuna settimana di osservazione`; `Rispetto alla tua settimana di osservazione precedente.` | Feature name = **settimana di osservazione**; `Shadow Mode` → `modalità osservazione` (`Termina la modalità osservazione e blocca immediatamente`); `Start Shadow Week` → `Avvia la settimana di osservazione`. One string keeps `Shadow Mode`. |
| Enable real blocking | `Enable real blocking` | `Attiva il blocco reale` | |
| Reflect (button) | `Reflect` | `Rifletti` | |
| Reflection (noun) | `Reflection summary`; `Reflections this month` | `Riepilogo riflessioni`; `Riflessioni di questo mese` | |
| Reflection prompt | `What were you hoping to find?` | `Cosa speravi di trovare?` | |
| Reflection answers | `Boredom` / `Anxiety` / `FOMO` / `Habit` / `Other` | `Noia` / `Ansia` / `FOMO` / `Abitudine` / `Altro` | |
| Smart Schedules | `Smart Schedules` / `Smart schedules` | `Pianificazioni intelligenti` / `Pianificazioni smart` | **Inconsistent.** `Schedules` → `Pianificazioni`; `Smart Schedules + custom app icons` → `Pianificazioni smart + icone personalizzate`. |
| Goal tiers Light / Standard / Challenge | `Light` / `Standard` / `Challenge` | `Leggero` / `Standard` / `Sfida` | |
| Default schedules | `Work hours` / `Evenings` / `Weekends` / `Sleep` | `Orario di lavoro` / `Sere` / `Fine settimana` / `Sonno` | |
| Daily goal | `Daily goal` | `Obiettivo giornaliero` | `Progress to goal` → `Progressi verso l'obiettivo`. Another string says `obiettivi di attività quotidiani`: `giornaliero` and `quotidiano` mixed. |
| Adaptive goal | `Adaptive` | `Adattivo` | |
| Steps | `Steps` | `Passi` | `%lld steps` → one:`%lld passo` / other:`%lld passi` |
| Active minutes | `Active minutes` | `Minuti di attività` | Another string says `minuti attivi`. |
| Active energy / calories | `Active calories` | `Calorie attive` | Permission text: `energia attiva`. |
| "2,026 steps until unlock" (shield) | `%@ until unlock`; `1,247 steps until unlock` | `%@ allo sblocco`; `1.247 passi allo sblocco` | Shield button `Earn it` → `Guadagnatelo`; shield title `Earn your way in` → `Guadagnati l'accesso`; Watch/complication `%@ to unlock` → `%@ per sbloccare`. |
| Emergency unlock | `Emergency unlock` | `Sblocco di emergenza` | `Emergency unlock until %@` → `Sblocco di emergenza fino a %@`. Math gate: `Solve to continue` → `Risolvi per continuare`. |
| Partial unlock | `Partial unlock` | `Sblocco parziale` | `Lo sblocco parziale termina tra 10 minuti.` |
| Rest day | `Rest day` / `Weekly rest day` | `Giorno di riposo` / `Giorno di riposo settimanale` | |
| Streak | `Streak`; `Current streak` | `Serie`; `Serie attuale` | See batch headline: `serie` = sets elsewhere. |
| Streak shields | `Streak shields`; `Shield saved your streak` | `Scudi serie`; `Lo scudo ha salvato la tua serie` | |
| Most-attempted blocked app | `Most attempted blocked app today` | `App bloccata più tentata oggi` | |
| Screen time saved (estimate) | `Screen time saved (estimated)` | `Tempo allo schermo risparmiato (stimato)` | Live Activity: `TIME SAVED` → `TEMPO RISPARMIATO`. |
| Screen Time (Apple feature) | `Allow Screen Time access` | `Consenti l'accesso a Tempo di utilizzo` | Apple's Italian name. |
| Apple Health | `Apple Health` | `Apple Salute` | Also `app Salute` and bare `Salute`. |
| Locked apps | `Locked apps` | `App bloccate` | `app` throughout, unchanged plural. |
| Family Sharing | `Family Sharing supported — Premium unlocks for up to five family members in your Apple Family group.` | `Supporta In famiglia — Premium si sblocca per un massimo di cinque membri del tuo gruppo Famiglia Apple.` | Apple's Italian name "In famiglia"; store description says `Condivisione in famiglia` (LiftLog). |
| Activity heatmap | `Activity heatmap` | `Mappa termica attività` | |
| Best week / best month | `Best week` / `BEST MONTH` | `Settimana migliore` / `MESE MIGLIORE` | |
| App icons | `Midnight` / `Ember` / `Mono` | `Mezzanotte` / `Brace` / `Mono` | |
| Focus session | `Focus session` | `Sessione di concentrazione` | Siri: `Avvia una sessione di concentrazione`. |
| Milestone card | `Next milestone`; `A quiet milestone.` | `Prossimo traguardo`; `Un traguardo silenzioso.` | |
| Widgets (Live Activity catalog) | `EarnLock — Contributions` / `— History` / `— Streak` / `— Summary` / `— Today & Month` / `— Lock Screen` | `EarnLock — Contributi` / `— Cronologia` / `— Serie` / `— Riepilogo` / `— Oggi e mese` / `— Schermata Blocco` | `Deep Focus`, `Dynamic Island` and `Live Activity` have no UI string. |
| Apple Watch app | `Apple Watch app` | `App per Apple Watch` | |
| Parental approval | `Parental approval required` | `Approvazione di un genitore richiesta` | |

#### Paid tier names in the Italian UI

`Premium` (tier), `Mensile` / `Annuale` / `A vita`, combined labels (`Premium · Mensile`, `Premium · Annuale`, `Premium · A vita`, `Premium · Condiviso con te`); buttons `Passa a Premium`, `Scegli A vita`, `Inizia la prova gratuita`; `Ripristina acquisti`; `Gestisci l'abbonamento`; product name `EarnLock Premium`. Italian IAP display names on the store: `EarnLock Premium una tantum`, `EarnLock Premium annuale`, `EarnLock Premium mensile`.

#### Italian App Store listing (checked 2026-11-19)

- Name: **EarnLock: Blocca App e Focus** (English: "EarnLock: App Blocker & Focus"). Page title: "App EarnLock: Blocca App e Focus - App Store".
- Subtitle: **Benessere digitale e passi** (English: "Your steps unlock screen time").
- IAP rows («Acquisti in-app»): `EarnLock Premium una tantum` 22,99 € · `EarnLock Premium annuale` 9,99 € · `EarnLock Premium mensile` 1,99 €.
- Languages: «Italiano e altre 32 lingue». Category: **Produttività**. Age 9+. Minimum iOS 17.0. Price: `Gratis`.
- Description vocabulary (Italian): `Blocca qualsiasi app o categoria con i controlli di Tempo di utilizzo di Apple`; `obiettivo di attività giornaliero` / `obiettivo giornaliero in passi`; `Apple Salute tiene il conto`; `sblocco di emergenza`; `settimana di osservazione` ("PRIMA, UNA SETTIMANA DI OSSERVAZIONE"); `app bloccate`; `widget`; section heads `MUOVITI PRIMA. SCORRI DOPO.`, `DOVE STA LA CHIAVE`, `COSA OTTIENI`; `mezzanotte`. The store text matches the app on `Tempo di utilizzo`, `settimana di osservazione`, `sblocco`.

---

### 2. GymLogger X (gymlogger-x, source `GymLogger`, ID 6755734580)

The app has no `.xcstrings`; text comes from JSON files (`Localizations/it.json`, `GymLoggerWidget/Localizations/it.json`, `GymLoggerWatch Watch App/Localizations/it.json`) plus `GymLogger/it.lproj/InfoPlist.strings`. There is no AppShortcutsProvider (no Siri phrases). `ExerciseTranslations.it.json` exists (exercise names, not audited); no `RehabTranslations.it.json` was found (rehab names exist for other locales, not audited).

#### Italian coverage

| Catalog | Keys (en) | `it` present | % | identical to English |
|---|---|---|---|---|
| Localizations/it.json (main app) | 2923 | 2923 | 100% | 110 (units, `Volume`, `Core`, `Cardio`, `Coach`, `Info`, `Account`, `Offline`, `Pro`, RIR/RPE/ACWR/MEV/MRV, `Home`, `Apple Health`, `Push`, `Pull`, `Upper / Lower`, `Push / Pull`, `Plateau: %@`) |
| GymLoggerWidget/Localizations/it.json | 115 | 115 | 100% | 6 |
| GymLoggerWatch Watch App/Localizations/it.json | 98 | 98 | 100% | 8 |
| GymLogger/it.lproj/InfoPlist.strings | 4 keys | 4 | yes | Display name "GymLogger X"; both Health prompts are Italian (tu): `GymLogger legge la tua frequenza cardiaca e le calorie per fornire analisi sugli allenamenti e monitorare i tuoi progressi.` / `GymLogger salva i tuoi allenamenti completati in Apple Salute per mantenere i tuoi anelli di attività e la cronologia completi.` |

No missing keys, no empty values. **Verdict: app is in Italian: yes** (100% of keys in app, widget and Watch; permission prompts localized). Siri phrases: none exist.

Register: tu. 403 of 3136 strings carry tu markers; 0 Lei strings (unlike Spanish, no usted validation messages).

Defects (app-side; do not copy these into the site):
- **`home_title` and `info.home.title` = `Home`** (English left in as the tab title; note Italian iOS apps do commonly say "Home", so this is borderline, but the Spanish pass has `Inicio` and `training_title` is `Allenamento`).
- **Five Program Creator strings lost their accents**: `creator_goal_athletic_desc` = `Potenza, velocita e forza funzionale`; `creator_goal_strength_desc` = `Diventa piu forte con multiarticolari pesanti e poche ripetizioni`; `creator_periodization_block_desc` = `Fasi di piu settimane — ipertrofia poi forza poi picco`; `progression_maintain_push_reps` and `progression_push_reps` (`piu ripetizioni`). The rest of the Italian is correctly accented (the Spanish app had 99 unaccented strings; Italian has 5).
- **Giant set is two words**: `giant_set` = `Serie gigante`, `create_giant_set` = `Crea set gigante`; `add_set_to_all_description` = `Aggiungi +1 set a tutti gli esercizi della settimana` (`set` for sets, while `sets` = `Serie`).
- **Plateau is three words**: `plateau_detection` = `Rilevamento stallo`, `plateau_confirmed` = `Plateau rilevato`, `analytics_plateau_title` = `Plateau: %@` (identical to English), `plateau_none` = `Progressione` (key `Progressing`).
- **Rest timer is three terms**: `watch_a11y_rest_timer` = `Timer di recupero`, `settings_watch_hr_timer_title` = `Timer riposo con frequenza cardiaca`, `rest_time` = `Tempo di Riposo` (capital R); LiftLog says `Timer di riposo`.
- **`Apple Health` stays English in 10 in-app strings** (`health_saved_to_health` = `Salvato in Apple Health`, `health_manage_in_health` = `Gestisci in Apple Health`, `onboarding_health_bullet1`), while the InfoPlist prompt says `Apple Salute`.
- **Two trial labels**: `paywall_start_trial` = `Inizia Prova Gratuita` (Title Case), `paywall_cta_start_trial` = `Prova gratuita`.
- `share_just_finished` keeps a stray backslash: `Ho appena finito %@\!` (the English has it too).
- Title Case in sentences: `Creatore di Programmi`, `Pro a Vita`, `Stile di Periodizzazione`, `Inizia Prova Gratuita`, `Tempo di Riposo`.
- "AI Coach": `ai_coach` = `Coach AI` (Italian usually writes `IA`; the store subtitle says `Coach IA`; check against the English page, which says no language model or chat bot).

#### Glossary

| English term on site | English UI string (key) | Italian UI string (verbatim) | Note |
|---|---|---|---|
| Free | `free` = Free | `Gratis` | |
| Pro | `widget_pro` = Pro; `gymlogger_pro` = GymLogger X Pro | `Pro`; `GymLogger X Pro` | |
| Pro Monthly | `paywall_plan_monthly` = Monthly | `Mensile` | |
| Pro Annual | `paywall_plan_yearly` = Yearly; `paywall_yearly_pro` = Yearly Pro | `Annuale`; `Pro Annuale` | App says "Yearly", not "Annual". |
| Lifetime | `paywall_plan_lifetime` = Lifetime; `paywall_lifetime_pro` = Lifetime Pro; `paywall_lifetime_access` | `A vita`; `Pro a Vita`; `ACCESSO A VITA` | Capital V in `Pro a Vita`. Store IAP is `una tantum`. `paywall_lifetime_description` → `Paga una volta, tuo per sempre. Nessun rinnovo.` |
| Restore Purchases | `restore_purchases` | `Ripristina acquisti` | |
| Start free trial | `paywall_start_trial` = Start Free Trial; `paywall_trial_text` = 1-week free trial | `Inizia Prova Gratuita`; `1 settimana di prova gratuita` | `paywall_trial_best_value` → `1 settimana gratis • MIGLIOR VALORE`; `paywall_free_trial` → `GRATIS PER 1 SETTIMANA`. |
| Tabs: Home / Training / Progress / Settings | `home_title` / `training_title` / `progress` / `settings` | `Home` / `Allenamento` / `Progresso` / `Impostazioni` | |
| Smart Program Creator | `paywall_tile_program_creator` = Smart Program Creator — built around you | `Smart Program Creator — su misura per te` | English name kept; `creator_create_program` = `Crea programma intelligente`; `creator_title` = `Creatore di Programmi`. |
| Plateau detection | `plateau_detection` = Plateau Detection | `Rilevamento stallo` | Status labels: `plateau_confirmed` = `Plateau rilevato`, `plateau_watch` (Monitoring) = `Da osservare`, `plateau_none` (Progressing) = `Progressione`. |
| Estimated 1RM | `analytics_estimated_1rm` = Estimated 1RM | `1RM stimato` | `widget_e1rm_a11y` = `Massimale stimato su una ripetizione`. |
| Deload week | `insert_deload_week` = Insert Deload Week | `Inserisci settimana di scarico` | `load_deload` and `creator_deload` = `Scarico`; consistent (also in coach insights). |
| Periodization types: linear / DUP / block / wave | `creator_periodization_*` | see catalog | `creator_periodization` = `Stile di Periodizzazione`. (Type names not extracted.) |
| Splits: Full Body / Upper-Lower / PPL / Push-Pull / Arnold / Bro | `creator_split_*` | `Full body` / `Upper / Lower` / `Push / Pull / Gambe` / `Push / Pull` / `Split Arnold` / `Bro split` | Mostly English loanwords; `Upper / Lower` and `Push / Pull` identical to English. |
| Balance cards | `muscle_balance`; `front_back_balance`; `upper_lower_balance` | `Equilibrio muscolare`; `Anteriore / Posteriore`; `Parte superiore / inferiore` | |
| Program library | `programs` = Programs; `example_programs` = Example Programs | `Programmi`; `Programmi esempio` | `program_workouts` → `Allenamenti del programma`. `paywall_tile_programs` → `Oltre 35 programmi collaudati`. `training_gymlogger_programs` → `Programmi GymLogger`. |
| The Golden Six | `arnold_golden_six_name` | `The Golden Six` | Name left in English. |
| Rest timer | `watch_a11y_rest_timer` = Rest timer | `Timer di recupero` | `settings_watch_hr_timer_title` (Heart Rate Rest Timer) = `Timer riposo con frequenza cardiaca`; LiftLog `Timer di riposo`. |
| Templates | `templates`; `workout_templates` | `Modelli`; `Modelli di allenamento` | `save_as_template` → `Salva come modello`. |
| Superset / Giant set | `superset` / `giant_set` | `Superserie` / `Serie gigante` | `create_giant_set` = `Crea set gigante` (inconsistent). |
| Warm-up set | `warmup_set` / `mark_as_warmup` | `Serie di riscaldamento` / `Segna come riscaldamento` | |
| Sets / Reps | `sets` / `reps` | `Serie` / `Ripetizioni` | LiftLog uses `Ripetiz.` as the label. |
| Personal records | `personal_records` = Personal Records; `prs` = PRs | `Record personali`; `Record` | Consistent. |
| Rep-max table | `analytics_rep_max_table` = Rep-Max Table | `Tabella dei massimali` | |
| Strength progress | `analytics_strength_progress` | `Progresso di forza` | |
| Next Move card | `analytics_next_move_label` = Next Move | `Prossima mossa` | |
| Training load ratio | `analytics_acwr_title` | `Rapporto di carico di allenamento` | `training_load` = `Carico di allenamento`. |
| Set volume vs MEV / MAV / MRV | `analytics_set_volume` | `Volume di serie` | `set_volume_landmark_row` = `MEV %1$@ · MAV %2$@ · MRV %3$@` (unchanged); `set_volume_band_below` = `Sotto il MEV`. |
| Muscle heatmap | `muscle_heatmap` | `Mappa termica muscolare` | EarnLock `Mappa termica attività`; LiftLog `mappa di attività`. |
| Readiness / fatigue / recovery | `readiness_*`; `home_fatigue`; `home_recovery` | `prontezza`; `Livello di fatica`; `Recupero` | `readiness_explanation_intro` = `Il tuo punteggio di prontezza è calcolato in base a:`. `widget_description` = `Monitora i tuoi allenamenti e la prontezza.` |
| Plate calculator | `plate_calculator` | `Calcolo dischi` | LiftLog says `Calcolatore dischi`. |
| Weekly summary | `weekly_summary_title` | `Riepilogo settimanale` | |
| Custom exercises | `create_custom_exercise` | `Crea esercizio personalizzato` | |
| Import a coach's spreadsheet program | `import_program` = Import Program; `import_from_spreadsheets` = Spreadsheets (CSV) | `Importa programma`; `Fogli di calcolo (CSV)` | |
| Apple Health export | `health_saved_to_health` = Saved to Apple Health | `Salvato in Apple Health` | `Apple Health` in app, `Apple Salute` in permissions. |
| Start workout | `start_workout` = Start Workout | `Inizia allenamento` | `allenamento` is the app's word (381 strings); `sessione` appears in 74 (a logged session). |
| Family Sharing | `paywall_family_sharing_title` | `Include In famiglia` | `paywall_family_sharing_subtitle` → `Un solo acquisto. Fino a 6 familiari. Nessun costo aggiuntivo.` |
| iCloud sync | `icloud_sync` | `Sincronizzazione iCloud` | |
| One-time payment / No subscription | `paywall_one_time` / `paywall_no_subscription` | `Pagamento unico` / `Nessun abbonamento` | `paywall_best_value` → `MIGLIOR VALORE`; `paywall_most_popular` → `PIÙ POPOLARE`. |

#### Paid tier names in the Italian UI

`Gratis` / `GymLogger X Pro` / `Pro`; plan cards `Mensile`, `Annuale` (`Pro Annuale`), `A vita` (`Pro a Vita`, `ACCESSO A VITA`); `Inizia Prova Gratuita`, `1 settimana di prova gratuita`; `Ripristina acquisti`; `Pagamento unico`; `Nessun abbonamento`; `MIGLIOR VALORE`; `PIÙ POPOLARE`; `Include In famiglia`.

#### Italian App Store listing (checked 2026-11-19)

- Name: **GymLogger X: Tracker Palestra** (English: "GymLogger X: Workout Tracker"). Page title: App GymLogger X: Tracker Palestra - App Store.
- Subtitle: **Allenamento Forza & Palestra** (English: "Strength Training & Gym Log").
- IAP rows («Acquisti in-app»): `GymLogger X Pro una tantum` 44,99 € · `GymLogger X Pro annuale` 19,99 € · `Support the developer` 1,00 € (name not translated) · `GymLogger X Pro mensile` 1,99 €.
- Languages: «Italiano e altre 33 lingue». Category: **Salute e benessere**. Age 9+. Minimum iOS 17.6. Price: `Gratis`.
- Description vocabulary (Italian): `diario di allenamento per la forza`; `44 programmi pronti`; `Smart Program Creator`; `RIR (ripetizioni in riserva)`; `Pro`; `timer di riposo` (store) against `Timer di recupero` (app); `calcolo dischi`; `stallo` / `plateau`; `tabella dei massimali`; `1.500 ESERCIZI`; `widget della schermata di blocco`; `bilanciere`. The store says `timer di riposo` and `schermata di blocco`; the app says `recupero` for the Watch label.

---

### 3. LiftLog (liftlog, source `CoreLift`, ID 6760043411)

#### Italian coverage

| Catalog | Keys | `it` present | `it` translated | % |
|---|---|---|---|---|
| CoreLift/CoreLift/Resources/Localizable.xcstrings (main app) | 990 | 980 | 980 | 99.0% |
| CoreLift/CoreLift/Resources/AppShortcuts.xcstrings | 6 | 6 | 6 (stringSet, 3-4 phrasings each) | 100% |
| CoreLift/CoreLift/Resources/InfoPlist.xcstrings | 4 | 2 | 2 | 50% (both Health permission texts are Italian; `CFBundleDisplayName` / `CFBundleName` have no entry, so the name is "LiftLog") |
| LiftLogWidgets/Resources/WidgetLocalizable.xcstrings | 137 | 137 | 137 | 100% |

The 10 main-app keys without `it`: ` / %lld` and `%@` (symbols only) and eight real English words that are user-visible in the Italian app: `Average`, `Best`, `Best run`, `By month`, `By weekday`, `min`, `Sessions in run`, `Weekly avg` (same 8 as in Spanish; the widget catalog has Italian for them: `Media`, `Record`, `Miglior serie`, `Per mese`, `Per giorno della settimana`, `min`, `Sessioni nella serie`, `Media sett.`).

Siri: the App Shortcuts phrases are Italian (6 intents, 3-4 phrasings each, e.g. `Inizia il mio prossimo allenamento con ${applicationName}`, `Qual è la mia serie in ${applicationName}`, `Registra la mia serie in ${applicationName}`, `Avvia il mio timer di riposo in ${applicationName}`, `Quanto ho sollevato questa settimana in ${applicationName}`); one phrasing is missing its preposition (`Comincia il mio prossimo allenamento ${applicationName}`), but the Siri hint in Localizable tells users to say the English phrases: `Di’ «Start my next workout with LiftLog» per iniziare una sessione, oppure chiedi «What’s my streak in LiftLog?» e «How much did I lift this week in LiftLog?» per avere una risposta senza aprire l’app.` App-side inconsistency.

Permission texts name the app **LiftLog**: `LiftLog non legge mai i tuoi dati sulla salute in Apple Salute: salva soltanto i tuoi allenamenti di forza completati così da farli contare per i tuoi anelli Attività.` / `LiftLog salva i tuoi allenamenti di forza completati in Apple Salute così da farli contare per i tuoi anelli Attività. Non legge mai i tuoi dati sulla salute.`

**Verdict: app is in Italian: yes** (99% main app, 100% widgets and Shortcuts; 8 English fallbacks in the stats screens).

Register: tu. 162 of 1097 strings carry tu markers (`Imposta il massimale d'allenamento`, `Oggi non ti addebitiamo nulla. Ti ricordiamo tra 7 giorni.`), 0 real Lei strings (`Può essere attivo un solo programma alla volta.` is impersonal).

Wording flags:
- **`Streak` and `Sets` are both `Serie`** (`Serie di %lld settimane`, `Serie di riscaldamento %lld`, `Registra serie`), and `Best Set` = `Serie migliore` while widget `Best run` = `Miglior serie` and `Sessions in run` = `Sessioni nella serie`. Italian lifters say `serie` for sets, so the streak noun collides.
- `Good` = `Bene` (adverb); the store IAP says `Buono`. `Patron` = `Sostenitore`, and the key `Supporter` is also `Sostenitore`; the store IAP says `Mecenate`.
- Widget `Back` = `Indietro` (navigation word) where a body-part label is meant; neighbouring `BACK` = `SCHIENA`.
- Widget `Best` = `Record` (a label), fine, but the main-app `PR` badge = `RP` (an abbreviation used by nobody; Italian lifters say `PR` or `record`).
- `Rest Timer` = `Timer di riposo`; the Siri phrase uses `Avvia il mio timer di riposo`, another phrasing says `Fai partire il recupero` (recupero/riposo mixed); `Rest` = `Recupero`.
- `Reps` label is the abbreviation `Ripetiz.`; `Estimated 1RM` abbreviation `1RM stim.`; `Weekly avg` = `Media sett.`.
- Free-trial text: `Prova gratuita`, `Gratis per 7 giorni.`, `%d giorni restanti della prova` (consistent).
- `Siri & Shortcuts` = `Siri e Comandi rapidi` (Apple's Italian name is "Comandi rapidi"; MediaKit writes `Comandi Rapidi e Siri` with a capital R).
- `Training Max` renders as `massimale d'allenamento` in sentences.

#### Glossary

| English term on site | English UI string (key) | Italian UI string (verbatim) | Note |
|---|---|---|---|
| Free trial | `Free Trial`; `Free for 7 days.` | `Prova gratuita`; `Gratis per 7 giorni.` | `%d days left in trial` → `%d giorni restanti della prova`; `You won't be charged today. We'll remind you in 7 days.` → `Oggi non ti addebitiamo nulla. Ti ricordiamo tra 7 giorni.` |
| Tier: Fair | `Fair` | `Equo` | Same as the store (`Accesso completo · Equo`). |
| Tier: Good | `Good` | `Bene` | **Store IAP is `Accesso completo · Buono`.** |
| Tier: Generous | `Generous` | `Generoso` | Same as the store. |
| Tier: Patron | `Patron` | `Sostenitore` | **Store IAP is `Accesso completo · Mecenate`.** Also `Supporter` = `Sostenitore`. |
| Full access | `Full Access` | `Accesso completo` | |
| One-time purchase / no subscription | `One-time purchase`; `No subscription` | `Acquisto unico`; `Nessun abbonamento` | `Pay what feels fair.` → `Paga quello che ti sembra giusto.`; `One payment. Yours forever. Free for the next 7 days.` → `Un pagamento. Tuo per sempre. Gratis per i prossimi 7 giorni.` |
| Restore Purchases | `Restore Purchases` | `Ripristina acquisti` | |
| Tabs: Home / Exercises / Programs / Progress / Settings | same | `Home` / `Esercizi` / `Programmi` / `Progresso` / `Impostazioni` | `History` → `Cronologia`. |
| Log set key | `Log set · start rest`; `Log Set` | `Registra serie · avvia riposo`; `Registra serie` | Consistent verb `Registra`. |
| Rest timer | `Rest Timer` / `Rest timer` | `Timer di riposo` | |
| Estimated 1RM | `Estimated 1RM`; `Est. 1RM` | `1RM stimato`; `1RM stim.` | |
| Rep PRs | `Rep PRs`; `PR` | `Record di ripetizioni`; `RP` | See flag. |
| Personal bests | `Personal Bests`; `New Personal Bests`; `Personal record` | `Record personali`; `Nuovi record personali`; `Record personale` | |
| Best set / Best volume | `Best Set` / `Best Volume` | `Serie migliore` / `Miglior volume` | |
| Activity heatmap | `Complete workouts to see your progress and activity heatmap.` | `Completa allenamenti per vedere i tuoi progressi e la mappa di attività.` | Feature name = **mappa di attività**. Widget `Activity grid` has no `it` string in the main app. |
| Last 30 days | `Last 30 days` | `Ultimi 30 giorni` | |
| Training Max | `Set a training max` | `Imposta il massimale d'allenamento` | Noun: `massimale d'allenamento`; `% of training max` → `% del massimale d'allenamento`. |
| Double progression / Progression | `Double progression` / `Progression` | `Doppia progressione` / `Progressione` | |
| Deload (trigger) | `Deload` | `Scarico` | `Deload after` → `Scarico dopo`. |
| Adaptive 1RM formula | `Adaptive (recommended)`; `1RM Formula` | `Adattiva (consigliata)`; `Formula 1RM` | |
| Superset / Giant set | `Superset` / `Giant Set` | `Superserie` / `Serie gigante` | `Create Superset` → `Crea superserie`. |
| How To (exercise detail) | `How To` | `Come fare` | |
| Workout | `Workout` | `Allenamento` | |
| Sets / Reps | `Sets` / `Reps` | `Serie` / `Ripetiz.` | |
| Streak | `Streak` | `Serie` | `%lld week streak` → `Serie di %lld settimane`. |
| Export (JSON / CSV) | `Export Data (CSV)` / `Export Data (JSON)` | `Esporta dati (CSV)` / `Esporta dati (JSON)` | |
| Apple Health | `Apple Health` | `Apple Salute` | |
| Family Sharing | `Family Sharing` | `In famiglia` | Store description: `Condivisione in famiglia`. |
| Warm-up set | `Warm-up set %lld` | `Serie di riscaldamento %lld` | |
| Siri & Shortcuts | `Siri & Shortcuts` | `Siri e Comandi rapidi` | |
| Support | `Support`; `Funds 3 months of dev` | `Supporta`; `Finanzia 3 mesi di sviluppo` | |
| Plate calculator | `Plate calculator` | `Calcolatore dischi` | |
| Muscle labels | `Chest` / `Legs` / `Shoulders` / `Core` / `Bodyweight` | `Petto` / `Gambe` / `Spalle` / `Core` / `Corpo libero` | |

Program names (StrongLifts 5×5, 5/3/1, GZCLP, Greyskull LP, ...) stay in English; descriptions are Italian.

#### Paid tier names in the Italian UI

LiftLog has no Pro/Premium and no subscription: a one-time purchase with four tiers that all unlock the same app: `Equo` / `Bene` / `Generoso` / `Sostenitore` (in-app) against `Equo` / `Buono` / `Generoso` / `Mecenate` (App Store IAP names, each prefixed `Accesso completo · `); buttons `Sblocca`, `Sblocca LiftLog`, `Prova gratuita`, `Ripristina acquisti`; `Un pagamento. Tuo per sempre. Gratis per i prossimi 7 giorni.` Mismatches: Good (`Bene` / `Buono`) and Patron (`Sostenitore` / `Mecenate`); the Spanish pass found only one mismatch.

#### Italian App Store listing (checked 2026-11-19)

- Name: **LiftLog: Scheda Palestra** (English: "LiftLog: Workout Gym Tracker"). Page title: "App LiftLog: Scheda Palestra - App Store".
- Subtitle: **Serie, ripetizioni & forza** (English: "Sets, reps & strength programs").
- IAP rows («Acquisti in-app»): `Accesso completo · Buono` 22,99 € · `Accesso completo · Mecenate` 44,99 € · `Accesso completo · Equo` 9,99 € · `Accesso completo · Generoso` 39,99 €.
- Languages: «Italiano e altre 43 lingue». Category: **Salute e benessere**. Age 4+. Minimum iOS 17.6. Price: `Gratis`.
- Description vocabulary (Italian): `Prova LiftLog 7 giorni gratis, poi paghi una volta`; `Condivisione in famiglia`; `PAGHI UNA VOLTA, SCEGLI IL TUO PREZZO`; `serie effettiva`; `record personale`; `record di ripetizioni`; `timer di riposo`; `Superserie, serie giganti e serie a tempo`; `calcolatore dischi`; `40 PROGRAMMI`; `1RM stimato`; `massimale di allenamento` (store) against `massimale d'allenamento` (app); `bilanciere`. The store text uses `Registra la mia serie in LiftLog` for Siri (matches the app's first phrasing).

---

### 4. MediaKit (mediakit, source `ClearCut`, ID 6761451361)

#### Italian coverage

| Catalog | Keys | `it` present | `it` translated | % |
|---|---|---|---|---|
| ClearCut/MediaKit/Localizable.xcstrings (main app) | 2583 | 2583 | 2583 | 100% |
| ClearCut/MediaKit/AppShortcuts.xcstrings | 6 | 6 | 6 | 100% |
| ClearCut/MediaKit/InfoPlist.xcstrings | 26 | 23 | 23 | 88.5% (Photo Library add permission, Speech Recognition permission and the file-type names are Italian; missing: `CFBundleDisplayName`, `CFBundleName`, `NSHumanReadableCopyright`, so the name stays "MediaKit") |
| ClearCut/MediaKitShareExtension/Localizable.xcstrings | 13 | 13 | 13 | 100% |

Permission texts: `MediaKit salva i video e le immagini elaborati nella tua libreria di Foto.` / `MediaKit usa il riconoscimento vocale per trascrivere audio e video in testo quando esegui lo strumento Trascrivi.` Siri phrases are Italian: `Comprimi un video con ${applicationName}`, `Comprimi un’immagine con ${applicationName}`, `Converti un’immagine con ${applicationName}`, `Crea uno ZIP con ${applicationName}`, `Estrai testo da un’immagine con ${applicationName}`, `Unisci PDF con ${applicationName}`.

**Verdict: app is in Italian: yes** (100% of the main app, Shortcuts and share extension; permissions localized).

Register: tu. 208 of 2616 strings carry tu markers (`Trascina un file per l’anteprima`, `Scegli un file e premi Esecuzione passo-passo`, `Generato localmente sul tuo Mac`), 0 Lei strings.

Wording flags:
- `Free` (key) = `Libero` while `Free tier` = `Piano gratuito` (same false-synonym as Spanish `Libre`).
- `Archive` category = `Archivio` (fine; Italian "archivio" is also a file archive).
- `Make It Fit` = `Fai entrare` (reads as an imperative "make it enter"; consider keeping the English or a better verb on the site).
- `Batch Processing` = `Elaborazione in blocco` in the UI but the Pro upsell says `l’elaborazione in batch` (blocco/batch mixed).
- `Normalize loudness` = `Normalizza la sonorità`, `EBU R128 loudness normalization` = `Normalizzazione del volume EBU R128` (sonorità/volume mixed).
- `Shortcuts & Siri` = `Comandi Rapidi e Siri` (capital R; Apple's name is "Comandi rapidi").
- Family Sharing: `Compatibile con In Famiglia` (capital F; Apple's Italian name is "In famiglia").
- `Trim` = `Taglia`, `Crop` = `Ritaglia`; `Redact` = `Oscura` (single consistent word, unlike Spanish).
- Apostrophes: 86 strings use curly `’`, 183 straight `'`.
- Raw keys shown as values (identical to English, likely internal): `bottom`, `bottomLeft`, `center`, `left`.
- Free-trial strings: `Prova gratuita di %@`, `%@ di prova gratuita · %@/mese`, `Tutti gli strumenti, 3 giorni gratis` (consistent).
- `Upscale IA`, `Sottotitoli auto` (anglicism `upscale`, shortened `auto`).

#### Glossary

| English term on site | English UI string (key) | Italian UI string (verbatim) | Note |
|---|---|---|---|
| Pro | `Pro` | `Pro` | `Upgrade to Pro` → `Passa a Pro`; `Unlock Pro` → `Sblocca Pro`. |
| Pro · Monthly | `Monthly` | `Mensile` | |
| Pro · Annual | `Annual` | `Annuale` | The key here is "Annual". |
| Lifetime | `Lifetime` | `A vita` | `Buy Lifetime Access` → `Acquista accesso a vita`; `Get Lifetime Access` → `Ottieni l'accesso a vita`. Store IAP: `MediaKit Pro acquisto unico`. |
| Free trial (3 days) | `Every tool, 3 days free`; `%@ free trial`; `%@ free trial · %@/mo` | `Tutti gli strumenti, 3 giorni gratis`; `Prova gratuita di %@`; `%@ di prova gratuita · %@/mese` | |
| Free tier (five tools stay free) | `Free tier`; `Free` | `Piano gratuito`; `Libero` | `Free tier includes 5 unlimited tools forever. Pro unlocks the rest plus batch processing.` → `Il piano gratuito include 5 strumenti illimitati per sempre. Pro sblocca il resto e l’elaborazione in batch.` |
| Tool (generic) | `Tool`; `Add a Tool to the Recipe` | `Strumento`; `Aggiungi uno strumento alla ricetta` | |
| Recipes (chained tools) | `Recipes`; `Create a new multi-step recipe`; `Recipe Marketplace` | `Ricette`; `Crea una nuova ricetta in più passaggi`; `Marketplace ricette` | Feature name = **ricetta**; `Browse Recipe Marketplace` → `Sfoglia il marketplace delle ricette`. |
| Make It Fit | `Make It Fit` | `Fai entrare` | See flag. |
| Video / Image Compress | `Compress`; `Compress Video`; `Compress Image` | `Comprimi`; `Comprimi video`; `Comprimi immagine` | |
| Image Resize | `Resize` | `Ridimensiona` | |
| Convert (audio, image...) | `Convert`; `Convert Image` | `Converti`; `Converti immagine` | |
| Categories: Video / Audio / Image / PDF / Archive / Ebook | same | `Video` / `Audio` / `Immagine` / `PDF` / `Archivio` / `Ebook` | |
| Batch processing | `Batch Processing` | `Elaborazione in blocco` | Pro text: `elaborazione in batch`. |
| Export presets | `Preset`; `Platform preset` | `Preset`; `Preset di piattaforma` | English loanword kept. |
| Shortcuts actions | `Shortcuts & Siri` | `Comandi Rapidi e Siri` | |
| Merge | `Merge`; `Merge PDFs` | `Unisci`; `Unisci PDF` | |
| Extract text / OCR | `Extract Text from Image`; `OCR` | `Estrai testo dall’immagine`; `OCR` | |
| Remove background | `Remove background` | `Rimuovi lo sfondo` | |
| AI upscale | `AI Upscale` | `Upscale IA` | |
| Auto Subtitle | `Auto Subtitle`; `Auto Subtitle + Translate` | `Sottotitoli auto`; `Sottotitoli auto + traduzione` | |
| Transcribe | `Transcribe` | `Trascrivi` | |
| Strip EXIF metadata | `Strip Metadata` | `Rimuovi metadati` | |
| Reduce noise | `Noise Reduce` / `Denoise` | `Riduci rumore` / `Riduzione rumore` | |
| Normalize (EBU R128 / LUFS) | `Normalize loudness`; `EBU R128 loudness normalization` | `Normalizza la sonorità`; `Normalizzazione del volume EBU R128` | |
| Redact | `Redact PDF`; `Redact`; `Redact rectangles` | `Oscura PDF`; `Oscura`; `Oscura rettangoli` | Consistent. |
| Compare | `Compare`; `Compare Takes` | `Confronta`; `Confronta take` | |
| Smart Duplicate Finder | `Smart Duplicate Finder` | `Cerca duplicati intelligente` | |
| Trim / Stabilize / Watermark / Crop / Rotate / Flip / Sign / Encrypt | same | `Taglia` / `Stabilizza` / `Filigrana` / `Ritaglia` / `Ruota` / `Capovolgi` / `Firma` / `Cripta` | |
| Drop a file in | `Drop a file to preview` | `Trascina un file per l’anteprima` | |
| Watch folder / Folder Automation | `Watch folder`; `Folder Automation` | `Cartella monitorata`; `Automazione cartelle` | |
| Menu bar | no UI string | n/a | Apple's Italian term "barra dei menu"; not in the catalog. |
| Settings | `Settings` | `Impostazioni` | |
| Restore Purchases | `Restore Purchases` | `Ripristina acquisti` | |
| Share extension | `Open in MediaKit`; `Send to MediaKit` | `Apri in MediaKit`; `Invia a MediaKit` | |
| Family Sharing | `Works with Family Sharing` | `Compatibile con In Famiglia` | |

#### Paid tier names in the Italian UI

`Pro`; `Mensile` / `Annuale` / `A vita`; `Prova gratuita di %@`; `Piano gratuito`; `Passa a Pro`; `Sblocca Pro`; `Ripristina acquisti`. Store IAP names: `MediaKit Pro mensile`, `MediaKit Pro annuale`, `MediaKit Pro acquisto unico`.

#### Italian App Store listing (checked 2026-11-19)

- Name: **MediaKit: Comprimi e Converti** (English: "MediaKit: Compress & Convert").
- Subtitle: **Video, Audio, Immagini e PDF** (English: "Video, Audio, Image, PDF & ZIP").
- IAP rows («Acquisti in-app»): `MediaKit Pro annuale` 24,99 € · `MediaKit Pro acquisto unico` 44,99 € · `MediaKit Pro mensile` 4,99 €.
- Languages: «Italiano e altre 11 lingue». Category: **Utility**. Age 4+. Minimum iOS 17.0. Price: `Gratis`.
- Description vocabulary (Italian): `Oltre 150 strumenti per video, audio, foto, PDF e altro`; `sul dispositivo`; `Cinque restano gratuiti`; `ogni strumento Pro per 3 giorni`; `COSA PUOI FARE`; `Comprimi video`; `Sottotitoli auto`; `uniforma il volume secondo lo standard EBU R128` (store says `volume`, app `sonorità`); `Rimuovi lo sfondo con Apple Vision`; `PDF: unisci, dividi, firma, oscura, applica l'OCR e comprimi`; `filigrane`; `ebook`.

---

### 5. Millrace (millrace, source `thegame`, ID 6759511759)

The site never writes the number the old title contained, and none of the strings below contain it.

#### Italian coverage

| Catalog | Keys | `it` present | `it` translated | % |
|---|---|---|---|---|
| thegame/thegame/Localizable.xcstrings (only catalog) | 333 | 333 | 333 | 100% (locale code is plain `it`; no `it-IT`) |
| InfoPlist | no InfoPlist.xcstrings | | | Display name "Millrace" comes from the build settings; the app requests no permissions. |

Only a few strings are identical to English: `Debug`, `Feedback`, `Game Center` (and `Extra`). **Verdict: app is in Italian: yes (100%).** Siri: no App Shortcuts catalog. Register: tu (47 of 333 strings carry tu markers: `Unisci le tessere finché puoi.`, `Costruisci esattamente %@ sulla cella segnata`, `Se la blocchi, perdi.`), 0 Lei, 0 voi.

Wording flags:
- **`Undo` noun is `annullamento`** (`%lld annullamenti`, `10 annullamenti`, `Gettoni annullamento`, store IAP `50 annullamenti`, `200 annullamenti`); clean and consistent, unlike Spanish `deshacer`. The verb `Undo` is `Annulla`.
- `Blocked` = `Cella bloccata` (the key is the bare adjective; the translation adds `Cella`).
- `One-time` = `Pagamento unico` against the footer `Acquisti una tantum.` (two terms for one-time purchase), and the store says `acquisti una tantum` too.
- `Daily` = `Giornaliera` (feminine, agreeing with `Sfida`) as a bare label; `Daily Best` = `Record giornaliero`; `Dailies Played` = `Sfide giornaliere giocate`.
- `Haptics` = `Vibrazione`.
- `Achievements` = `Obiettivi` (Apple's Game Center term in Italian); `Leaderboards` = `Classifiche`.
- `Best` = `Record` but the hint of a minimum is `Il minimo possibile è %lld mosse` (many form `%lld di mosse`).
- Streak is `Serie` (`Serie attuale`, `Serie più lunga`, `Ricompense serie`), fine inside a game without sets.
- Packs: `Pacchetto Designer 1` / `Pacchetto Estate` / `Pacchetto Inverno` (the store IAP names match exactly).
- The store description says `tabellone` for the board and `tessere` for tiles; the app uses `cella` for the grid cell and `tessera` for a tile and has no `tabellone` string of that wording in the strings checked.

#### Glossary

| English term on site | English UI string (key) | Italian UI string (`it`, verbatim) | Note |
|---|---|---|---|
| Chapter: Warm-up | `Warm-up` | `Riscaldamento` | |
| Chapter: Tactics | `Tactics` | `Tattica` | |
| Chapter: Pressure | `Pressure` | `Pressione` | |
| Chapter: Precision | `Precision` | `Precisione` | |
| Chapter: Deep Water | `Deep Water` | `Acque profonde` | |
| Chapter: Mastery | `Mastery` | `Maestria` | |
| Level | `Level %lld` | `Livello %lld` | No "Chapter" string (no `capitolo` in the catalog); the store says "sei capitoli". |
| Puzzle | `Puzzles`; `Next puzzle`; `Puzzle not solved` | `Puzzle`; `Puzzle successivo`; `Puzzle non risolto` | Term = **puzzle** (invariable); the store title uses `rompicapo`. |
| Freeplay | `Freeplay` | `Gioco libero` | `Merge as long as you can. No goal, no move limit.` → `Unisci le tessere finché puoi. Nessun obiettivo, nessun limite di mosse.` |
| Hint | `Hint` | `Suggerimento` | `Dismiss tip` → `Ignora suggerimento`. |
| The Coach | `Coach`; `Coaching notes` | `Allenatore`; `Note dell'allenatore` | |
| Daily board / daily challenge | `Daily Challenge` / `Daily challenge` / `Daily` | `Sfida giornaliera` / `Sfida giornaliera` / `Giornaliera` | `Daily Best` → `Record giornaliero`. Store: `Sfida giornaliera`. |
| Undo | `Undo` | `Annulla` | Noun: `annullamento` / `annullamenti` (see flag). |
| Daily streak | `Current Streak` / `Longest Streak` / `Streak Rewards` | `Serie attuale` / `Serie più lunga` / `Ricompense serie` | `%lld-day streak: %lld undos` → `Serie di %lld giorni: %lld annullamenti`. |
| Personal best | `Personal Best` / `Best` / `NEW BEST` | `Record personale` / `Record` / `NUOVO RECORD` | `Best Score` → `Punteggio record`; `Best Tile` → `Tessera record`. |
| Move budget / moves left | `%lld moves left`; `No moves left` | one:`%lld mossa rimasta` / other:`%lld mosse rimaste`; `Nessuna mossa disponibile` | Unit = **mossa**. `Best possible is %lld moves` → one:`Il minimo possibile è %lld mossa` / other:`Il minimo possibile è %lld mosse` / many:`Il minimo possibile è %lld di mosse`. |
| Target cell | `This is the target cell.` | `Questa è la cella obiettivo.` (inside `Riga %lld, colonna %lld, vuota. Questa è la cella obiettivo.`) | VoiceOver; terms **cella obiettivo** / **cella segnata** (`Costruisci esattamente %@ sulla cella segnata`, `Le tessere continuano ad arrivare sulla cella segnata. Se la blocchi, perdi.`). Store: `un solo ingresso`. |
| Inlet | no UI string | `Qui arrivano le tessere, e la cella è bloccata.` | The app describes the inlet without naming it; the store subtitle says `ingresso` (`64 livelli, un solo ingresso`). The site needs its own Italian term. |
| Tile | `%lld tiles arriving` | one:`%lld tessera in arrivo` / many:`%lld di tessere in arrivo` / other:`%lld tessere in arrivo` | Term = **tessera**; `Highest tile %lld. %lld of 16 cells filled. Score %lld.` → `Tessera più alta %lld. %lld celle su 16 occupate. Punteggio %lld.` |
| Blocked | `Blocked` | `Cella bloccata` | |
| Theme / themes | `Theme` / `Themes` | `Tema` / `Temi` | |
| Theme packs | `Designer Pack 1` / `Designer Pack 2` / `Summer Pack` / `Winter Pack` | `Pacchetto Designer 1` / `Pacchetto Designer 2` / `Pacchetto Estate` / `Pacchetto Inverno` | Matches the store IAP names exactly. |
| Complete Collection | `Complete collection` | `Collezione completa` | `Unlock All Themes` → `Sblocca tutti i temi`; `Every theme. Forever.` → `Tutti i temi. Per sempre.` |
| Classic (free theme) and theme names | no catalog entries | n/a | Theme names are not localized. |
| Support the Developer (tip) | `Support the Developer` | `Sostieni lo sviluppatore` | Store IAP: `Sostieni lo sviluppatore`. |
| Game Center leaderboards / achievements | `Leaderboards` / `Achievements` | `Classifiche` / `Obiettivi` | |
| Settings: Haptics / Sound Effects / Music | same | `Vibrazione` / `Effetti sonori` / `Musica` | |
| Settings | `Settings` | `Impostazioni` | |
| No subscription | `One-time purchases. No subscription. No ads, ever.` | `Acquisti una tantum. Nessun abbonamento. Mai pubblicità.` | |
| Restore Purchases | `Restore Purchases` | `Ripristina acquisti` | |
| Unlock | `Unlock` / `Unlock %@` | `Sblocca` / `Sblocca %@` | |

#### Paid tier names in the Italian UI

Millrace has no Premium/Pro tier. It is free with one-time purchases: `Collezione completa`, `Pacchetto Designer 1`, `Pacchetto Designer 2`, `Pacchetto Estate`, `Pacchetto Inverno`, undo packs `10 annullamenti` / `50 annullamenti` / `200 annullamenti`, tip `Sostieni lo sviluppatore`; buttons `Sblocca`, `Sblocca %@`, `Ripristina acquisti`; label `Pagamento unico`. No free-trial string.

#### Italian App Store listing (checked 2026-11-19)

- Name: **Millrace: rompicapo di numeri** (English: "Millrace: Tile Delivery Puzzle"). Note: the Italian name calls it a number puzzle ("di numeri"); check this is not a stray reference to the old title's theme (no digits appear).
- Subtitle: **64 livelli, un solo ingresso** (English: "64 forged levels, one inlet").
- IAP rows («Acquisti in-app»): `Collezione completa` 6,99 € · `50 annullamenti` 2,99 € · `Pacchetto Inverno` 1,99 € · `Sostieni lo sviluppatore` 1,99 € · `200 annullamenti` 6,99 € · `10 annullamenti` 0,99 € · `Pacchetto Designer 2` 1,99 € · `Pacchetto Designer 1` 1,99 € · `Pacchetto Estate` 1,99 €.
- Languages: «Italiano e altre 33 lingue». Category: **Giochi da tavolo**. Age 4+. Minimum iOS 18.0. Price: `Gratis`.
- Description vocabulary (Italian): `rompicapo di consegna delle tessere`; `64 livelli in sei capitoli`; `limite di mosse`; `coda di tessere in arrivo`; `tabellone`; `Suggerimento`; `Sfida giornaliera`; `gettone annullamento`; `17 temi` (`Classic è incluso gratis`); `classifiche`, `obiettivi`; `acquisti una tantum`; `senza abbonamento`, `senza pubblicità`; `soluzione minima`.

---

### Cross-app terms (as the five apps write them in Italian)

| Concept | Italian used | Where it varies |
|---|---|---|
| Restore Purchases | `Ripristina acquisti` | Identical in all five. |
| Settings | `Impostazioni` | Identical in all five. |
| Apple Health | `Apple Salute` (EarnLock, LiftLog, GymLogger X permissions), `Apple Health` (GymLogger X in-app, 10 strings) | GymLogger X only. |
| Screen Time (Apple feature) | `Tempo di utilizzo` | EarnLock only; concept `tempo allo schermo` / `tempo di schermo`. |
| Family Sharing | `In famiglia` (EarnLock, GymLogger X, LiftLog), `In Famiglia` (MediaKit) | Capital F in MediaKit; store text says `Condivisione in famiglia`. |
| Monthly / Yearly or Annual | `Mensile` / `Annuale` | Identical wording across apps. |
| Lifetime | `A vita` | GymLogger X also `Pro a Vita`, `ACCESSO A VITA`. |
| One-time purchase | `una tantum` (store IAPs, Millrace footer), `acquisto unico` (LiftLog, MediaKit IAP), `Pagamento unico` (GymLogger X, Millrace label) | Three forms. |
| Free trial | `prova gratuita` | `prova gratis` once in GymLogger X; Millrace has none. |
| Streak | `Serie` | Collides with `serie` = sets (GymLogger X, LiftLog). |
| Personal best / PR | `Record personale`, `Record personali`, `Record` | LiftLog badge `RP`. |
| Sets / Reps | `Serie` / `Ripetizioni` (GymLogger X), `Serie` / `Ripetiz.` (LiftLog) | |
| Superset / giant set | `Superserie` / `Serie gigante` | GymLogger X `Crea set gigante` is the exception. |
| Deload | `Scarico` | Consistent. |
| Rest timer | `Timer di riposo` (LiftLog), `Timer di recupero` (GymLogger X Watch label), `Timer riposo con frequenza cardiaca` | |
| Workout | `Allenamento` (`sessione` for a logged session) | |
| Video | `video` (no accent) | |
| App | `app` / `App` (invariable plural) | |
| Heatmap | `Mappa termica` (EarnLock, GymLogger X), `mappa di attività` (LiftLog) | |
| Unlock | `Sblocca` / `Sblocco` | Identical across EarnLock, LiftLog, MediaKit, Millrace. |
| Premium / Pro | `Premium` (EarnLock), `Pro` (GymLogger X, MediaKit) | Not translated. |
| Lock Screen | `Schermata Blocco` (EarnLock widget title) | Apple's term would be `schermata di blocco`. |
| Siri & Shortcuts | `Siri e Comandi rapidi` (LiftLog), `Comandi Rapidi e Siri` (MediaKit) | Order and capitalization differ. |
| Mac | `questo Mac`, `tuo Mac` | Consistent in MediaKit. |

---

### Flags (app-side string bugs, register mixes, missing Italian)

1. **LiftLog tier mismatch (two tiers):** in-app `Bene` against store `Buono` for Good; in-app `Sostenitore` against store `Mecenate` for Patron (and `Supporter` is also `Sostenitore`). The site needs one choice per tier.
2. **LiftLog English fallbacks:** `Average`, `Best`, `Best run`, `By month`, `By weekday`, `min`, `Sessions in run`, `Weekly avg` have no `it` in `Localizable.xcstrings` (the widget catalog has them). The Siri hint tells Italian users to say English phrases; one Siri phrasing lacks its preposition (`Comincia il mio prossimo allenamento ${applicationName}`); widget `Back` = `Indietro` should be a body-part label.
3. **"Serie" for both streak and sets** (EarnLock, LiftLog, Millrace use it for streak; GymLogger X and LiftLog for sets). In LiftLog it creates ambiguity between `Serie migliore` (best set) and `Miglior serie` (best streak).
4. **GymLogger X:** `home_title` / `info.home.title` = `Home`; 5 unaccented Program Creator strings (`velocita`, `piu`: `creator_goal_athletic_desc`, `creator_goal_strength_desc`, `creator_periodization_block_desc`, `progression_maintain_push_reps`, `progression_push_reps`); `Crea set gigante` against `Serie gigante`; `Apple Health` in 10 in-app strings against `Apple Salute` in the prompts; two trial labels (`Inizia Prova Gratuita` / `Prova gratuita`); Title Case in sentences.
5. **EarnLock:** permission prompts (phone and Watch) are `needs_review`; `CFBundleDisplayName` has no `it` entry; `Impossibile tracciare Shadow Mode` keeps English; `Pianificazioni intelligenti` against `Pianificazioni smart`; `Schermata Blocco` is a calque; `tempo allo schermo` against `tempo di schermo`; `Scegli A vita` capital A.
6. **MediaKit:** `Free` = `Libero`, `Comandi Rapidi e Siri` (capital R), `Compatibile con In Famiglia` (capital F), `Fai entrare` for `Make It Fit`, `Elaborazione in blocco` against `batch`, `sonorità` against `volume` for loudness, raw values `bottom`, `bottomLeft`, `center`, `left` shown in English, no `it` for `CFBundleDisplayName` / `NSHumanReadableCopyright`.
7. **Millrace:** `One-time` = `Pagamento unico` against `Acquisti una tantum`; `Blocked` = `Cella bloccata`; store name `Millrace: rompicapo di numeri` should be checked with the owner (the name says "number puzzle", the English store name says "Tile Delivery Puzzle").
8. **Register is clean:** all five apps are tu. No Lei, no voi. Only false hits were found.
9. **Missing Italian:** no Italian for the Dynamic Island, Live Activity or Deep Focus names in EarnLock (no UI string), no `capitolo` string in Millrace, no menu bar string in MediaKit, no Siri phrases in GymLogger X (none exist), no Italian name for Millrace's inlet (the store subtitle uses `ingresso`).
10. **House rule for Millrace:** the old title's number appears nowhere in the Italian `it` column or the Italian store text (checked by search: 0 hits), and this file doesn't write it.


---

## Italian glossary, batch 3: mockly, observa, pawza, rightsplit, shogiful

Method (checked 2026-11-19). Read-only. Source catalogs under `~/Downloads/` (`AppScreenMaker/`, `HealthLogger/`, `PetCare/`, `splitit/`, `shogi/`), `.xcstrings` parsed as JSON with `python3 -I`, locale `it` (Mockly checked for `it` and `it-IT`; the catalog has neither). "Total" = keys with `shouldTranslate` not false and a non-blank key; "translated" = every string unit of the `it` entry has state `translated` (plural and substitution variations included); "other state" = value present but `needs_review`. Italian values are copied verbatim from the catalogs (apostrophes as the catalog writes them, straight `'` or typographic `’`). Terms and keys come from the Spanish model `_i18n/es-glossary.md` (batch 3 part) plus the English app pages `_apps/<slug>.md`. Register counts are regex counts over the `it` values, then hand-checked: tu markers (tu, tuo/tua/tuoi/tue, ti, puoi, hai, sei, vuoi, devi) and tu imperatives at string start (Tocca, Scegli, Aggiungi, Apri, Inizia, Sblocca, Registra, Scansiona); Lei markers (Lei, suo/sua for "your", Tocchi, Scelga, Aggiunga, Apra, Inizi) and voi markers (vostro/vostra, Valutate, Annotate, Cercate, Provate, state). Most regex hits for Lei imperatives are false positives (the noun "Passi" = steps, "Partite" = games, "Date" = dates, "Giochi" = games), listed per app. App Store data: iTunes lookup (`country=it&lang=it_it`) plus `curl -L` (Safari User-Agent, `Accept-Language: it-IT`) of the apps.apple.com/it page, parsed from the raw `serialized-server-data` JSON (not a summarizer). The first pass returned HTTP 429 (and a 301 without the slug), so pages were re-fetched with the lookup's canonical URL and pauses of 60 s. Prices use NO-BREAK SPACE (U+00A0) before the euro sign and are reference only. The seller block on the store pages carries the owner's personal name, address and phone; it was not copied. The master file `MASTER.md` / `MASTER-prices.csv` is the source for prices, platforms, trials and Family Sharing. "Apple's own names" (In famiglia, Apple Health, Impostazioni, ID Apple) belong in `it-apple-terms.md`; they are noted here only as the app writes them.

## Summary

| App | Main catalog `it` | Extensions / other catalogs | InfoPlist / permissions | Register | Verdict |
|---|---|---|---|---|---|
| Mockly | **0/333: no Italian locale at all** (10 languages: de, en, es-ES, es-MX, fr, ja, ko, pt-BR, tr, zh-Hans) | none | InfoPlist 0/4 | n/a | **no, the app is English-only for Italy** |
| Observa | 6672/6684 translated (99.8%); all 6684 have a value; 12 `needs_review` (all `insight_signal_*`) | Watch 477/477, Widgets 403/403, AppShortcuts 15/15 have a value (10 translated, 5 `needs_review`) | app 5/5, watch 5/5 | **tu, with about 60 voi strings** | **yes** (about 20 strings partly or fully English) |
| Pawza | 1322/1323 (99.9%) | AppShortcuts 4/4; no widget catalog (widgets share the main one) | **none**: no InfoPlist catalog; camera and photo texts are English build settings although `it` is a known region | tu | **yes** (permission prompts in English) |
| RightSplit | 499/499 (100%) | Widgets 376/376, Share 3/3, SplititKit 65/65 | InfoPlist 5/5 | tu (and impersonal "si") | **yes** |
| Shogiful | 3751/3751 (100%) | none | InfoPlist 0/2 (display and bundle name only, English-only catalog; the app requests no permissions) | tu | **yes** |

Keys without `it`: Pawza `%@` (format only). Italian store names and subtitles are in each app's section and in "Cross-app terms".

---

### 1. Mockly (`mockly`, source `AppScreenMaker/`, ID 6756589122, macOS)

### Italian coverage

- `AppScreenMaker/Resources/Localizable.xcstrings`: 333 keys, **0 with an Italian value**. The catalog holds 10 languages: de, en, es-ES, es-MX, fr, ja, ko, pt-BR, tr, zh-Hans. There is no `it` and no `it-IT`.
- `AppScreenMaker/InfoPlist.xcstrings`: 4 keys, 0 in Italian (`CFBundleDisplayName`, `CFBundleName`, `Mockly Project`, `NSHumanReadableCopyright`).
- No extensions, no Siri phrases, no widgets, no permission prompts, no `.lproj` files.
- Register: not applicable (no Italian text).
- **Verdict: app is in Italian: no.** An Italian user runs Mockly in English (macOS falls back to English; the Italian site must not promise an Italian interface). The Italian store page matches this: the description is the English text, the language list has 9 entries (Cinese Semplificato, Coreano, Francese, Giapponese, Inglese, Portoghese, Spagnolo, Tedesco, Turco) without Italiano.
- The "50 languages" claim on the site refers to the App Store locales Mockly can build screenshots for, not to the app's own interface. Italian is among those App Store locales; keep the site's wording clear on that.

Flags
- **M1 (no Italian UI):** no Italian locale in the app or in InfoPlist. Not an error for the page, but the Italian page must say the interface is English (and German, French, Spanish, Portuguese, Turkish, Japanese, Korean, Chinese).
- **M2 (store metadata not localized):** the Italian store page shows the English description and no subtitle (see section 5).
- **M3 (translation packs):** same open question as in the Spanish glossary (credit packs in the app vs no IAP rows on the store page). The Italian store page lists no in-app purchases either.

### Glossary

No Italian UI strings exist. The table lists the English UI strings the site mentions (all exist in the catalog, checked); the Italian column is empty. Write Italian page text in plain Italian and keep English product words in quotes when the page names a button (the user sees the English string).

| English term on site | English UI string (key) | Italian UI string | Note |
|---|---|---|---|
| Upload to App Store Connect | `Upload to App Store Connect` | none (English) | button |
| App Store Connect credentials | `App Store Connect Credentials` / `API Credentials` / `Delete Credentials` | none | settings section |
| Issuer ID / Key ID / .p8 key | `Issuer ID` / `Key ID` / `Import .p8 File` | none | |
| API key (bring your own) | `API Key` / `Own API Key` | none | |
| AI translation | `AI Translation` / `AI Translate` / `Translate All` / `Bulk Translations` / `AI Integration` | none | |
| Provider | `Provider` / `Default Provider` | none | OpenAI, Anthropic, Google are not catalog strings |
| Localization panel | `Localizations` / `Languages` / `Target Languages` / `Source Language` / `Add Language` | none | |
| Linked to source | `Linked to source` / `Changes follow %@` | none | the site's "link-to-source switch" |
| Device models | `Devices` / `Device Style` / `Model` | none | |
| Artboard | `Artboard` / `Artboards` | none | |
| Export / Save images | `Export` / `Export %lld Artboards` / `Save Images` | none | |
| Text blocks / captions | `Text Block` / `Text Blocks` / `Text Editing` | none | |
| Copy Style | `Copy Style` | none | |
| CSV import/export | `Import CSV` / `Export CSV` | none | |
| Do not translate | `Do not translate` | none | per-block flag |
| Pages / Layers / Background | `Pages` / `Layers` / `Background` | none | |
| Camera / Lighting / Perspective | `Camera` / `Lighting` / `Perspective` / `Orthographic` | none | |
| macOS Keychain | `Your API key is stored in the macOS Keychain.` | none | Italian macOS term is "Portachiavi" (Apple's name, for `it-apple-terms.md`) |
| Translation packs (IAP) | `Translation Packs` / `Translation Credits` / `Buy More` / `Restore Purchases` | none | M3 |
| Powered by Claude | `Powered by Claude for high-quality screenshot localization.` | none | |
| Templates / Render styles / Percentage layout | no UI string | no UI string | |

### Paid tier names in the Italian UI

Mockly is a paid app (one-time purchase, no tiers). The only purchase UI is the translation-pack sheet, English-only for Italy. No Italian IAP display names exist.

### Italian App Store listing (https://apps.apple.com/it/app/mockly-screenshot-maker/id6756589122, checked 2026-11-19)

- Name: **Mockly: Screenshot Maker** (same as English; lookup `trackName`).
- Subtitle: **none shown**. The page header line reads "Sviluppatori" (the category label "Developer Tools" in Italian, shown when there is no subtitle). Spanish shows "50 idiomas, un clic".
- Category: **Sviluppatori** (English "Developer Tools").
- Price: **14,99 €** (paid; US $12.99).
- In-app purchases: none listed ("Acquisti in-app" row absent).
- Lingue: 9 (Cinese Semplificato, Coreano, Francese, Giapponese, Inglese, Portoghese, Spagnolo, Tedesco, Turco), **no Italiano**.
- Compatibilità: "Richiede macOS 14.0 o versioni successive." (Mac only). Size 34,9 MB.
- Description: **English** (starts "You finished the app. Now the store wants screenshots for every device size and every language…"). No Italian vocabulary to extract. The page labels in Italian are Apple's.

---

### 2. Observa (`observa`, source `HealthLogger/`, ID 6757438990)

### Italian coverage

- Main `HealthLogger/Localizable.xcstrings`: 6684 keys, all 6684 with an `it` value, 6672 state translated (99.8%). 12 are `needs_review` (values present): `insight_signal_active_energy` → "Energia attiva", `insight_signal_bedtime_consistency` → "Regolarità dell'orario di sonno", `insight_signal_morning_hrv` → "HRV mattutina", `insight_signal_readiness` → "Prontezza", `insight_signal_recovery_score` → "Punteggio di recupero", `insight_signal_respiratory_stability` → "Stabilità respiratoria", `insight_signal_sleep_duration` → "Durata del sonno", `insight_signal_sleep_score` → "Punteggio sonno", `insight_signal_spo2_stability` → "Stabilità dell'ossigeno nel sangue", `insight_signal_steps` → "Passi", `insight_signal_strain` → "Sforzo dell'allenamento", `insight_signal_training_load` → "Carico di allenamento". 41 languages; `it` is plain `it`.
- Watch `ObservaWatch/Localizable.xcstrings`: 477/477. Widgets `ObservaWidgets/Localizable.xcstrings`: 403/403.
- `AppShortcuts.xcstrings`: 15 keys, all with an `it` value; 10 translated, 5 `needs_review`: "Log my ${applicationName} morning check-in" → "Registra il mio check-in mattutino in ${applicationName}", "Log water in ${applicationName}" → "Registra acqua in ${applicationName}", "Should I train today in ${applicationName}?" → "Dovrei allenarmi oggi secondo ${applicationName}?", "What was my ${applicationName} sleep score?" → "Qual era il mio punteggio sonno in ${applicationName}?", "What's my ${applicationName} readiness?" → "Qual è la mia prontezza in ${applicationName}?". Translated phrases: "Posso allenarmi oggi secondo ${applicationName}?", "Come ho dormito secondo ${applicationName}?", "Come va il mio recupero in ${applicationName}?", "Registra idratazione in ${applicationName}", "Check-in mattutino in ${applicationName}"; shortcut titles "Prontezza ${applicationName}", "Sonno ${applicationName}", "Consiglio allenamento ${applicationName}" (the training call), "${applicationName} check-in", "${applicationName} registra acqua".
- `InfoPlist.xcstrings`: app 5/5 and watch 5/5 in Italian. `NSHealthShareUsageDescription` "Observa legge i tuoi dati sanitari per mostrare informazioni su sonno, cuore, attività e recupero. Tutti i dati vengono elaborati sul tuo dispositivo e non vengono mai caricati."; `NSHealthUpdateUsageDescription` "Observa salva le voci relative alla salute in Apple Health in modo che i tuoi dati rimangano in un unico posto."; `NSSiriUsageDescription` "Observa usa Siri così puoi chiedere il tuo punteggio di prontezza o di sonno e registrare l'idratazione o il check-in del mattino con la voce." ("dati sanitari" here, "Apple Health" elsewhere; "check-in del mattino" vs the UI's "check-in mattutino".)
- **English left in (real defects, value present, state translated):** 4 `VO₂ max …` explanation strings identical to English (`VO₂ max combines lung capacity…`, `VO₂ max is used in research…`, `VO₂ max naturally declines with age…`, `VO₂ max represents the maximum amount of oxygen…`); about 10 strings that begin Italian and continue in English ("La tua attività pattern reflects your lifestyle as much as your fitness.", "La tua capacità aerobica capacity has room to grow.", "Il tuo VO₂ Max is in the excellent range.", "Camminare heart rate is especially useful for tracking recovery from illness or injury — it often returns to baseline before you feel fully recovered.", "Camminare speed is considered a vital sign by many geriatric researchers."); two fully English strings ("Your active minutes are accumulating but haven't reached the weekly goal.", "Your acute load significantly exceeds your chronic baseline." and "Your VO₂ max is estimated from outdoor walks, runs, or hikes with Apple Watch."). 18 strings in total hit this pattern.
- **Verdict: app is in Italian: yes** (all user-visible parts; about 18 strings partly or fully English, 12 insight labels and 5 Siri phrases `needs_review`).

Register
- **tu is the main register:** about 1100 of 6686 strings carry a tu marker (tuo/tua/tuoi, ti, puoi, hai, sei) and 270 start with a tu imperative ("Tocca", "Scegli", "Aggiungi", "Apri", "Inizia", "Sblocca", "Registra"). The 23 "Lei imperative" regex hits are all the noun "Passi" (steps). No Lei form ("Tocchi", "Scelga", "Lei", "La sua") anywhere.
- **But about 60 strings use voi** (vostro/vostra/vostri and plural imperatives), all in coaching and insight advice: "Valutate di aggiungere un giorno di recupero." (`Training load is high. Consider adding a recovery day.`), "Mantenete la vostra routine attuale.", "Date priorità al riposo. Cercate di dormire di più questo fine settimana.", "Provate ad aggiungere 15-20 minuti al sonno stasera.", "Usate la vostra flessibilità per adattarvi agli impegni sociali quando necessario.", "Variate l'intensità dell'allenamento durante la settimana.", "Pianificate i compiti impegnativi per il vostro picco naturale", "Partite da dove siete", "I pattern sono calcolati dai vostri dati personali.", "Ciò che conta di più è il vostro trend personale", "Valutate se state concedendo sufficiente recupero…", "Annotate la tempistica quando ne parlate con…". Plus "è possibile regolarlo" (impersonal, 2 strings). Watch and widgets: pure tu.
- **Verdict: tu (site register), mixed with voi in about 1% of the main catalog.** Mixed: yes, flag A1 below. Quote tu strings freely; do not quote the voi strings.

**How the Italian UI labels HRV:** **"HRV"**, never "VFC" (key `HRV` and `metric_label_hrv` → "HRV"; about 200 strings; all widget labels `widget.title.hrv`). The long form is **"Variabilità della frequenza cardiaca"** (`Heart Rate Variability`). The Italian store NAME says "VFC" ("Observa: VFC, Recupero & Score") while the app and the store description say "HRV". SDNN appears only in 3 explanatory strings ("La deviazione standard degli intervalli NN (SDNN) riflette la variabilità complessiva della frequenza cardiaca da tutte le fonti…" and the RMSSD/SDNN ratio texts). House rule: HRV is SDNN (Apple Health); **RMSSD (19 strings) appears only in the ECG path and in Premium upsell text** ("RMSSD e pNN50 derivati dall'ECG"; "Sblocca le tendenze RMSSD, la cronologia dell'equilibrio autonomo e le indicazioni di allenamento"; "Il tuo RMSSD è sotto la linea di base…"). Never write "RMSSD" for the headline HRV on the site. There is no "HRV (SDNN)" label in the UI.

Flags
- **A1 (register):** about 60 voi strings (see above) in an otherwise tu app. App-side fix; the site writes tu.
- **A2 (baseline, three words and two genders):** `Baseline` → "Riferimento" (146 strings: `Your baseline` → "Il tuo riferimento", "Riferimento pronto", "sopra il riferimento"), but "baseline" (32 strings, English left in: "Costruzione baseline", "Creazione della tua baseline", "Sblocca il baseline" masculine next to "la baseline" feminine, "Alla baseline") and "linea di base" (10: `Above Baseline` → "Sopra la linea di base"). Pick "riferimento" or "linea di base" (the site's "baseline" in English copy translates best as "valore di riferimento personale"; decide with the reviewer). Also "bande di riferimento".
- **A3 (readiness):** `Readiness` → "Prontezza" (140 strings; `Readiness Score` → "Punteggio di prontezza"; bands `readiness_ready` "Pronto", `readiness_moderate` "Moderato", `readiness_low` "Basso"; `Moderate Readiness` → "Prontezza moderata"). The Italian store description also says "Prontezza". Consistent. "disponibilità" (47) is plain "available", not readiness; "Energy availability" → "disponibilità energetica" is correct.
- **A4 (patterns, three words):** the tab `Patterns` → **"Pattern"** (English left in; 171 strings: "%lld pattern individuati"), but "schemi/schema" (161: "Uno schema chiaro che compare regolarmente nei tuoi dati.", "Schema ricorrente: %@") and "modelli" (53: "Modelli attività × qualità del sonno"). The store description says "Schemi dai tuoi dati". Pick "schemi" for the site (natural Italian) and note that the tab label in the app is "Pattern".
- **A5 (sleep stage "Core", five variants):** `Core` → "Nucleo", `widget.sleep.core` → "Base", prose "sonno di base (leggero)", `Target ranges: … Core 50-60%` → "Core 50-60%", and **`Core %@` → "Profondo %@"** which is the Deep word: a real defect (Core shown as Deep next to `Deep %@` → "Profondo %@"). Stage names otherwise: Deep → "Profondo"/"Sonno profondo", REM → "REM"/"Sonno REM", Awake → "Sveglio".
- **A6 (HRV in store name):** store name "VFC", app "HRV" (see above).
- **A7 (store subtitle):** "Sonno, Ciclo, Coach Prontezza" has no separator before "Prontezza" (reads as one phrase, "Coach Prontezza"); the English "Readiness, Sleep & Cycle Coach" order was changed.
- **A8 (best value, two values):** `Best Value` → "Miglior rapporto qualità-prezzo", `Best value` → "Miglior valore", `onboarding_paywall_best_value` → "Miglior valore", `pricing_label_yearly` → "Annuale (miglior valore)". Pawza says "Più conveniente", Shogiful "MIGLIOR VALORE".
- **A9 (English product names in buttons):** `Unlock Lifetime Access` → "Sblocca Lifetime Access", `Unlock HRV Trends` → "Sblocca HRV Trends", `Unlock Baseline` → "Sblocca il baseline" while the onboarding paywall says "Sblocca l'accesso a vita".
- **A10 (check-in, small mixes):** `Morning Check-In` → "Check-in mattutino" (UI), Siri permission "check-in del mattino", Watch tab `watch.tab.log` → "Registro", complication `watch.complication.checkIn.title` → "Check-in". Use "check-in mattutino".
- **A11 (resting heart rate):** "Frequenza cardiaca a riposo" (43), "FC a riposo" (58), "FCR" (18, the `RHR` key). `bpm` stays "bpm"; `brpm` stays "brpm" (English).
- **A12 (Siri phrases `needs_review`):** 5 phrases (see above). "secondo ${applicationName}" is a loose rendering of "in ${applicationName}".
- **A13 (family sharing):** the app writes Apple's Italian name **"In famiglia"** ("Un solo abbonamento copre tutto il tuo gruppo In famiglia.", "organizzatore In famiglia").
- `Sleep Score` → "Punteggio sonno" (UI, Siri) but `widget.title.sleepScore` → "Punteggio del sonno": two forms. `Moderate Debt` → "Debito moderato", `Sleep Debt` → "Debito di sonno": consistent here.
- `ECG` → "ECG"; `Cycle Context` → "Contesto del ciclo", `Menstrual Cycle` → "Ciclo mestruale". The English site page does not cover cycle tracking (fact gap, as in the other glossaries); the store subtitle mentions "Ciclo".

### Glossary

| English term on site | English UI string (key) | Italian UI string (verbatim) | Note |
|---|---|---|---|
| Tab: Sleep | `Sleep` | Sonno | tab bar: Sleep, Recovery, Heart, Patterns, More |
| Tab: Recovery | `Recovery` | Recupero | |
| Tab: Heart | `Heart` | Cuore | |
| Tab: Patterns | `Patterns` | Pattern | A4 |
| Tab: More | `More` | Altro | |
| HRV | `HRV` / `metric_label_hrv` | HRV | house rule: SDNN; no "(SDNN)" label; store name says "VFC" (A6) |
| Heart rate variability | `Heart Rate Variability` | Variabilità della frequenza cardiaca | |
| ECG-derived RMSSD & pNN50 | `ECG-derived RMSSD & pNN50` | RMSSD e pNN50 derivati dall'ECG | ECG path only |
| ECG | `ECG` / `ECG Recording` / `ECG Analysis` | ECG / Registrazione ECG / Analisi ECG | |
| Autonomic balance | `Autonomic Balance` | Equilibrio autonomo | |
| Sinus rhythm | `Sinus Rhythm` | Ritmo sinusale | |
| Readiness | `Readiness` | Prontezza | A3 |
| Readiness score | `Readiness Score` | Punteggio di prontezza | |
| Readiness bands | `readiness_ready` / `readiness_moderate` / `readiness_low` | Pronto / Moderato / Basso | site: Ready, Moderate, Low |
| Sleep Score | `Sleep Score` | Punteggio sonno | A: also "Punteggio del sonno" in widgets |
| Recovery score | `recovery score` | punteggio di recupero | `insight_signal_recovery_score` `needs_review` |
| Training call | `Should I train today?` | Dovrei allenarmi oggi? | Siri title `${applicationName} training call` → "Consiglio allenamento ${applicationName}"; Siri phrase "Posso allenarmi oggi secondo ${applicationName}?"; complication `watch.complication.train.title` → "Mi alleno oggi?" |
| Training call verdicts | `widget.train.verdict.push` / `.maintain` / `.recover` / `.rest` / `.unavailable` | Intenso / Mantieni / Recupera / Riposo / Pochi dati | site: Push, Maintain, Recover, Rest; the store description also says "Intenso, Mantieni, Recupera o Riposo"; `guidance_category_maintain` → "Stabile" |
| Why this score? | `why.action.title` / `watch.why.title.readiness` | Perché questo punteggio? | store description: «Perché?» |
| Resting heart rate | `Resting Heart Rate` / `RHR` | Frequenza cardiaca a riposo / FCR | A11 |
| Sleep efficiency | `Sleep Efficiency` | Efficienza del sonno | |
| Sleep stages | `Sleep Stages` | Fasi del sonno | |
| Deep sleep / REM / Core / Awake | `Deep Sleep` / `REM Sleep` / `Core` / `Awake` | Sonno profondo / Sonno REM / Nucleo / Sveglio | A5 |
| Sleep debt | `Sleep Debt` | Debito di sonno | |
| Sleep quality | `Sleep Quality` | Qualità del sonno | four factors: `Continuity` → "Continuità" |
| Adjust Sleep | `Adjust Sleep` | Modifica il sonno | |
| Sleep Source | `Sleep Source` | Fonte del sonno | |
| Bedtime consistency | `Bedtime Consistency` | Regolarità dell'orario di sonno | also "regolarità dell'ora di dormire" |
| Heart-rate dip | `Nocturnal Dip` | Calo notturno | |
| Heart rate recovery | `Heart Rate Recovery` | Recupero frequenza cardiaca | |
| Stress | `Stress` | Stress | levels `stress_level_low` / `_moderate` / `_high` → Basso / Moderato / Alto; `Stress State` widget → "Livello di stress" |
| Today's Plan | `Today's Plan` | Piano di oggi | |
| Functional Age | `Unlock Functional Age` / `Meet your Functional Age` | Sblocca l'età funzionale / Scopri la tua età funzionale | label "età funzionale"; store description "Età funzionale" |
| Chronotype | `Chronotype Analysis` | Analisi del cronotipo | `chronotype_morning_lark` → "Allodola mattiniera"; `chronotype_intermediate` → "Cronotipo intermedio"; the store description says "un'allodola, un gufo o una via di mezzo" |
| Training load | `Training Load` | Carico di allenamento | `Load Management` → "Gestione del carico" |
| Strain | `Strain` | Sforzo | `insight_signal_strain` → "Sforzo dell'allenamento" |
| Workouts | `Workouts` | Allenamenti | |
| Energy | `Energy` / `Active Energy` | Energia / Energia attiva | |
| Personal baseline | `Baseline` / `Your baseline` | Riferimento / Il tuo riferimento | A2 |
| Confidence | `Confidence` | Affidabilità | |
| Patterns / correlations | `Correlation strength (r)` | Forza della correlazione (r) | |
| Why am I seeing this? | `Why am I seeing this?` | Perché vedo questo? | |
| Insight cards | `Daily insights` / `Insights` | Analisi giornaliere / Analisi | also "osservazioni" ("Sblocca le osservazioni personali") and widget `Insight` → "Osservazione" |
| Weekly reflection | `Weekly Reflection` | Riflessione settimanale | `Unlock Weekly Reflections` → "Sblocca le riflessioni settimanali"; also "riepilogo" in a description |
| Trends & Analysis | `trends_hub_title` | Tendenze e analisi | |
| Long-term trends | `Long-Term Trends` | Tendenze a lungo termine | |
| Morning check-in | `Morning Check-In` | Check-in mattutino | A10 |
| Hydration / water | `Hydration` / `watch.action.logWater` | Idratazione / Registra acqua | |
| Apple Health | `Apple Health` | Apple Health | English product name kept |
| Apple Watch complications | `watch.complication.*.title` | Check-in / Idratazione / Metrica / Oggi / Mi alleno oggi? | descriptions "Il tuo check-in mattutino, a un tocco.", "L'acqua di oggi rispetto al tuo obiettivo.", "Allenarsi o no oggi, con un'occhiata." |
| Widgets (archetypes) | `widget.archetype.*.title` | Focus / Folio / Griglia / Pila / Andamento / Osservazione / Dettaglio / Metrica nella schermata di blocco | site names: Focus, Folio, Grid, Stack, Trend, Insight, Breakdown; `fortnight` is the two-week "Last 14 days" widget; `today` title not translated in this list (see catalog) |
| Premium tier | `Premium` / `Upgrade to Premium` / `Unlock Premium` | Premium / Passa a Premium / Sblocca Premium | the site says "Premium" |
| Monthly / Yearly / Lifetime | `Monthly` / `Yearly` / `Lifetime` | Mensile / Annuale / A vita | |
| Unlock lifetime | `Unlock Lifetime Access` / `onboarding_paywall_lifetime_cta` | Sblocca Lifetime Access / Sblocca l'accesso a vita | A9 |
| Start free trial | `Start Free Trial` / `Start %@ Free Trial` | Inizia la prova gratuita / Inizia %@ di prova gratuita | |
| Start plan | `Start Yearly Plan` | Inizia il piano annuale | `onboarding_paywall_yearly_cta` → "Inizia piano annuale" |
| Restore Purchases | `Restore Purchases` | Ripristina acquisti | |
| Free | `Free` | Gratuito | "livello gratuito", "piano gratuito"; `%@ free, then %@/year` → "%@ gratis, poi %@/anno" |
| Best value | `Best Value` / `Best value` | Miglior rapporto qualità-prezzo / Miglior valore | A8 |
| First week free | `All Premium features are unlocked for your first 7 days.` | Tutte le funzioni Premium sono sbloccate nei tuoi primi 7 giorni. | `Everything is unlocked for your first 7 days. No sign-up needed.` → "Tutto è sbloccato nei tuoi primi 7 giorni. Nessuna registrazione richiesta." |
| Family Sharing | `One subscription covers your whole Family Sharing group.` | Un solo abbonamento copre tutto il tuo gruppo In famiglia. | A13 |
| Manage subscription | `Manage Subscription` | Gestisci abbonamento | |
| Backup restore | `store_restore_confirm_title` | Ripristinare questo backup? | "Elimina backup" |

### Paid tier names in the Italian UI

**Premium** everywhere (paywall, Watch "Observa Premium lo sblocca. Apri Observa su iPhone.", widgets, "Premium su iPhone"). Plans **Mensile / Annuale / A vita**, "Passa a Premium", "Sblocca Premium", "Ripristina acquisti", "Inizia la prova gratuita". No "Pro" tier (the English site's tier name is also Premium). The Italian IAP display names on the store (see section 5): **Premium mensile**, **Premium annuale**, **Premium acquisto singolo**, **Sostieni lo sviluppatore** (tip).

### Italian App Store listing (https://apps.apple.com/it/app/observa-vfc-recupero-score/id6757438990, checked 2026-11-19)

- Name: **Observa: VFC, Recupero & Score** (English "Observa: HRV & Recovery Score"; "VFC" here vs "HRV" in the app, A6; "Score" kept in English next to "Recupero", while the app says "Punteggio").
- Subtitle: **Sonno, Ciclo, Coach Prontezza** (A7).
- Category: **Salute e benessere** (English "Health & Fitness").
- Price: Gratis. In-app purchases (« Acquisti in-app »): **Premium mensile 3,99 €**, **Sostieni lo sviluppatore 1,00 €**, **Premium annuale 24,99 €**, **Premium acquisto singolo 59,99 €** (the app says "A vita", the store says "acquisto singolo"; the Spanish store says "compra única" too).
- Lingue: "Italiano e altre 33" (34).
- Compatibilità: iPhone iOS 17.6, iPad iPadOS 17.6, Mac macOS 14.6 (M1 or later), Apple Vision visionOS 1.3, Apple Watch watchOS 10. Size 92,7 MB. Age 9+.
- Description vocabulary (tu, 0 Lei): "Prontezza" (always capitalised: "il tuo punteggio di Prontezza"), "HRV" ("dall'HRV", "un HRV migliore"), "frequenza cardiaca a riposo", "carico di allenamento", «Perché?», «Dovrei allenarmi oggi?», "Intenso, Mantieni, Recupera o Riposo", "Punteggio sonno", "fasi del sonno", "debito di sonno", "obiettivo di sonno", "fonte del sonno", "un'allodola, un gufo o una via di mezzo", "Schemi dai tuoi dati", «Sembra accurato» / «Non applicabile», "Età funzionale", "stima di benessere, non una misura clinica", "Check-in mattutino di 10 secondi", "carico di allenamento", "complicazioni per il quadrante", "widget della schermata Home e della schermata di blocco", "In famiglia", "Privata per scelta", "Gratis per iniziare", "7 giorni di accesso completo, senza registrazione e senza carta", "prova gratuita di 1 settimana", "A vita", "Observa è un'app per il benessere, non un dispositivo medico." It does not use "Pro" and does not use "linea di base" or "baseline" ("rispetto al tuo intervallo abituale").

---

### 3. Pawza (`pawza`, source `PetCare/`, ID 6773507068)

### Italian coverage

- `PetCare/Localizable.xcstrings`: 1323 keys, 1322 with `it`, all translated (99.9%). Missing: only the format-only key `%@`. 50 languages. The widget target shares this catalog.
- `AppShortcuts.xcstrings`: 4/4: "Registra ${kind} in ${applicationName}", "Registra l'umore di ${pet} in ${applicationName}", "Registra cura per ${pet} in ${applicationName}", "Registra cura in ${applicationName}".
- **No `InfoPlist.xcstrings`.** The camera and photo-library permission texts are `INFOPLIST_KEY_NSCameraUsageDescription` / `INFOPLIST_KEY_NSPhotoLibraryUsageDescription` build settings in English only ("Pawza uses your camera to scan vet documents and take photos of your pets.", "Pawza needs photo access to import pictures of your pets and their documents."), while the project's `knownRegions` includes `it`. Italian users see the permission prompts in English.
- Register: **tu.** 96 strings with tu markers, 193 that start with a tu imperative ("Aggiungi le allergie, il numero del tuo veterinario…", "Scegli un PDF con lo storico veterinario del tuo animale…", "Riprova tra qualche minuto."). No Lei or voi. The single "suo" hit is third person ("Il suo promemoria è urgente…", the reminder's).
- **Verdict: app is in Italian: yes** (permission prompts in English). About 0 English-left-in strings (the English-ratio check found none).

Flags
- **P1 (permission prompts):** English build settings, not localized (see above). Same defect in the German, French and Spanish glossaries. App-side.
- **P2 (records, three words):** `Records` (tab) → **"Schede"** (57 strings: `Import past records` → "Importa schede precedenti", `AI summaries for every record` → "Riepiloghi con IA per ogni scheda"), but `Add Record` → "Aggiungi documento" and `%lld records` → "%lld documenti" (30 strings with "documenti/documento"), and the PDF/clinic record is "cartella clinica" (6: "Il PDF della cartella clinica"). The store subtitle says **"Libretto"** ("Libretto, vaccini e promemoria"), the store description says "Scheda" ("Importa schede precedenti", "compila la scheda") and "Scheda di emergenza". Use "scheda" on the site.
- **P3 (logs):** `Care log` → "Diario di cura" (the site's care log), but `logs` → "registro/registri" (7: "Ancora nessun registro", "%lld registri oggi") and `Log care` → "Registra cura". "Registro" also clashes with "Schede" as records.
- **P4 (accounts):** `Free accounts can track one pet. Pro lets you add as many as you have.` → "Gli account gratuiti seguono un solo animale. Pro te ne fa aggiungere quanti ne hai." and `Free accounts include 10 document scans…` → "Gli account gratuiti includono 10 scansioni di documenti." The app has no accounts ("Nessun account, nessun server…"). Same issue as the French glossary; the site says "gratuito/Gratis".
- **P5 (auto-fill):** `Unlock AI auto-fill` → "Sblocca la compilazione automatica con IA" vs "Il riempimento automatico con IA è pronto su questo iPhone" (2 strings) vs "Compila con Apple Intelligence". Use "compilazione automatica".
- **P6 (summary, two nouns):** "Riepiloghi con IA" (12: `AI Summaries`) vs "riassunti con IA" (6: "I riassunti con IA richiedono iPhone 15 Pro o più recente", "Riassunto con IA non disponibile"). The store description says "riepilogo sanitario in PDF".
- **P7 (best value):** `Best value` → "Più conveniente" (Observa "Miglior valore", RightSplit "Miglior valore").
- **P8 (Pet word):** `Pet` → "Animale" (80 strings: "Aggiungi animale", "%lld animali"); "pet sitter" for the sitter ("Kit pet sitter"). The store name says "Cane e Gatto"; the site covers dogs, cats, rabbits, birds, reptiles and horses ("animale" is right; avoid "pet" alone except in "pet sitter").
- **P9 (language):** "Pro" lock message `%@ is a Pro feature` → "Funzione Pro: %@".
- **P10 (settings):** "Impostazioni" (13) and one "configurazione" (setup, fine).
- `Start 7-day free trial` → "Inizia la prova gratuita di 7 giorni"; banner `7-DAY FREE TRIAL` → "7 GIORNI DI PROVA GRATUITA". `Emergency vet` → "Pronto soccorso veterinario"; `Lost Pet Poster` → "Volantino animale smarrito".

### Glossary

| English term on site | English UI string (key) | Italian UI string (verbatim) | Note |
|---|---|---|---|
| Tab: Pets | `Pets` | Animali | tabs: Pets, Reminders, Settings |
| Tab: Reminders | `Reminders` | Promemoria | |
| Tab: Settings | `Settings` | Impostazioni | |
| Pet / Add pet | `Pet` / `Add Pet` | Animale / Aggiungi animale | P8 |
| Health records | `Records` | Schede | P2 |
| Vaccinations | `Vaccinations` / `Vaccines` | Vaccinazioni / Vaccini | two keys, two words |
| Medications | `Medications` / `Medication` | Farmaci / Farmaco | |
| Doses | `Doses` | Dosi | |
| Vet visits | `Vet visits` | Visite veterinarie | |
| Vet | `Vet` | Veterinario | `Emergency vet` → "Pronto soccorso veterinario" |
| Weight / weight alerts | `Weight` / `Weight trend alerts` | Peso / Avvisi sull'andamento del peso | |
| Symptoms | `Symptoms` | Sintomi | `Log Symptom` → "Registra sintomo" |
| Care log | `Care log` / `Log care` | Diario di cura / Registra cura | P3 |
| Walks | `Walks` | Passeggiate | |
| Mood | `Mood` | Umore | |
| Feeding | `Feeding` / `Log food` | Pasti / Registra pasto | `Dry food` → "Cibo secco" |
| Document scanning | `Scan a vet document` / `Scan` | Scansiona un documento veterinario / Scansiona | "scansione/scansiona" throughout (29), never "digitalizza" |
| Import past records | `Import past records` | Importa schede precedenti | store description: «Importa schede precedenti» |
| AI auto-fill | `Unlock AI auto-fill` | Sblocca la compilazione automatica con IA | P5 |
| AI summaries | `AI Summaries` / `AI summaries for every record` | Riepiloghi con IA / Riepiloghi con IA per ogni scheda | P6; "IA", not "AI" |
| Apple Intelligence | `Apple Intelligence summary` / `Fill with Apple Intelligence` | Riepilogo di Apple Intelligence / Compila con Apple Intelligence | |
| Vet-visit PDF | `Vet Visit PDF` / `Vet visit PDF generator` | PDF della visita veterinaria / Generatore di PDF per la visita veterinaria | store: "PDF per il veterinario" |
| Since last vet visit | `Since last vet visit` | Dall'ultima visita veterinaria | |
| Emergency Card | `Emergency Card` | Scheda di emergenza | `Emergency Info` → "Informazioni di emergenza" |
| Lost Pet Kit | `Lost Pet Kit` / `Lost Pet Poster` | Kit animale smarrito / Volantino animale smarrito | |
| Sitter Pack | `Sitter Pack` | Kit pet sitter | `Make a sitter pack` → "Crea il kit pet sitter" |
| Photo gallery | `Unlimited photo gallery` | Galleria foto illimitata | `Compare Photos` → "Confronto foto" |
| Unlimited pets and scans | `Unlimited pets and scans` | Animali e scansioni illimitati | |
| Free / Pro | `Free` / `Pro` / `Pawza Pro` | Gratis / Pro / Pawza Pro | |
| Unlock Pro | `Unlock Pawza Pro` / `Upgrade to Pawza Pro` | Sblocca Pawza Pro / Passa a Pawza Pro | |
| Monthly / Yearly / Lifetime | `Monthly` / `Yearly` / `Lifetime` | Mensile / Annuale / A vita | `Pro (Lifetime)` → "Pro (a vita)", `Buy Lifetime — %@` → "Acquista a vita — %@" |
| 7-day free trial | `Start 7-day free trial` | Inizia la prova gratuita di 7 giorni | |
| Subscribe | `Subscribe` | Abbonati | |
| Best value | `Best value` | Più conveniente | P7 |
| Due / Upcoming | `Due` / `Upcoming` | Scadenza / In arrivo | |
| iCloud sync | `iCloud Sync: up to date.` / `Syncing with iCloud...` | Sincronizzazione iCloud: aggiornata. / Sincronizzazione con iCloud… | |
| Restore Purchases | `Restore Purchases` | Ripristina acquisti | |

### Paid tier names in the Italian UI

**Pawza Pro** (also "Pro"), labels **Mensile / Annuale / A vita**, "Inizia la prova gratuita di 7 giorni", "Ripristina acquisti", "Abbonati", "Più conveniente", "Funzione Pro: %@". Italian IAP display names on the store: **Pawza Pro mensile**, **Pawza Pro annuale**, **Pawza Pro acquisto singolo**.

### Italian App Store listing (https://apps.apple.com/it/app/pawza-salute-del-cane-e-gatto/id6773507068, checked 2026-11-19)

- Name: **Pawza: Salute del Cane e Gatto** (English "Pawza: Pet Health & Records"; narrows the app to dogs and cats while the site covers rabbits, birds, reptiles and horses; the description says "PER CANI, GATTI E NON SOLO").
- Subtitle: **Libretto, vaccini e promemoria** (English "Vaccine Tracker & Reminders"; "Libretto" vs the app's "schede", P2).
- Category: **Stili e tendenze** (English "Lifestyle").
- Price: Gratis. In-app purchases: **Pawza Pro annuale 22,99 €**, **Pawza Pro mensile 2,99 €**, **Pawza Pro acquisto singolo 44,99 €** (US: $19.99 yearly, $2.99 monthly, $39.99 lifetime).
- Lingue: "Italiano e altre 43" (44).
- Compatibilità: iPhone iOS 17.6, iPadOS 17.6, macOS 14.6 (M1), visionOS 1.3. Size 39,7 MB.
- Description vocabulary (tu, 0 Lei): "ricorda al posto tuo", "Dosi, pasti, vaccini, pesate e visite veterinarie", "LA GIORNATA IN UN TOCCO", "widget nella schermata Home o di blocco", "Centro di Controllo", "Siri", "Somministrato" and "Ha mangiato" (notification buttons), "Monitora la scorta", "modalità Full Immersion", "ANNI DI DOCUMENTI, LETTI SUL DISPOSITIVO", "Fotografa un documento del veterinario", "Apple Intelligence compila la scheda", "Importa schede precedenti", "riepilogo sanitario in PDF", "Scheda di emergenza", "Kit animale smarrito", "volantino da stampare, una medaglietta QR e una checklist", "Kit pet sitter", "Il grafico del peso", "cronologia foto", "si ordinano da sole", "PER CANI, GATTI E NON SOLO", "PRIVATO PER PROGETTAZIONE", "Scansione e importazione avvengono sul tuo dispositivo", "Non ti serve un account", "tramite il tuo iCloud", "GRATIS SUBITO, PRO QUANDO SERVE", "una settimana di prova gratuita", "sblocco a vita una tantum", "In famiglia". It uses "scheda/schede" for records and "documenti" for papers.

---

### 4. RightSplit (`rightsplit`, source `splitit/`, ID 6757268612)

### Italian coverage

- Main `splitit/Localizable.xcstrings`: 499 keys, all 499 with `it` (100%). 40 languages.
- Widgets `splititWidgets`: 376/376. Share extension `splititShare`: 3/3 ("Aggiunta a RightSplit…", "Impossibile leggere questa immagine. Prova a condividerne un'altra.", "Fine"). SplititKit package (`Sources/SplititKit/Resources`): 65/65.
- `InfoPlist.xcstrings`: 5/5 in Italian: `CFBundleDisplayName` "RightSplit", `CFBundleName` "splitit", camera "RightSplit utilizza la fotocamera per scansionare gli scontrini del ristorante e dividere il conto.", contacts "RightSplit accede ai contatti per aggiungere persone quando si divide il conto.", photo-library add "RightSplit salva un'immagine nella libreria foto solo su richiesta." (impersonal "si divide", "su richiesta").
- No Siri phrases, no AppShortcuts catalog.
- Register: **tu.** 22 strings with tu markers in the main catalog (plus widgets 26) and 75 that start with a tu imperative ("Scansiona o tocca un metodo per ripagarmi.", "Scansiona prima uno scontrino, poi allegalo da qui.", "Aggiungi almeno 2 persone per dividere il conto", "Dai a questa divisione un nome riconoscibile…"). Many strings are infinitive or impersonal ("Inizia a dividere", "Divisioni avanzate disponibili quando servono"). No Lei, no voi. Regex hits "Date specifiche" is the noun (dates).
- **Verdict: app is in Italian: yes.**

Flags
- **R1 (tax word, real defect):** `Tax` → **"Tassa"** (the only occurrence; 1 string). Italian restaurant receipts show "IVA" (VAT); "tassa" reads as a fee or levy, not as tax on a bill. The store description says "tasse e mancia seguono quello che ha ordinato ciascuno". Check the Italian site copy ("IVA" or "imposte") before using "tassa".
- **R2 (receipt / bill):** `Receipt` → "Scontrino" (33 strings: "Scansiona scontrino", "Dividi scontrino", "Lingua scontrino") and `Bill` → "Conto" (12 strings: "Dividi un conto", "dividere il conto"). One string uses "ricevuta" ("Su questa ricevuta qualcuno è già segnato come pagante."). The store name and description use "scontrino" and "conto" (consistent). Use "scontrino" and "conto".
- **R3 (split verb):** "Dividi / divisione" (29: `Split by items` → "Dividi per articoli", `Split Complete` → "Divisione completata", `Start splitting` → "Inizia a dividere"); "Condividi" is only the share action (`Share` → "Condividi", `Share RightSplit` → "Condividi RightSplit", `Share Card` → "Condividi carta"). No ambiguity. `Split fairly.` → "Dividi equamente."
- **R4 (spaces):** `Spaces` → "Spazi" (`New space` → "Nuovo spazio"); the store description says "Spazio" capitalised ("in uno Spazio"). `Trips` → "Viaggi".
- **R5 (Send Feedback casing):** `Send feedback` → "Invia feedback" and `Send Feedback` → "Invia Feedback" (capital F; Italian does not capitalise). "feedback" is English left in (accepted in Italian).
- **R6 (Owed):** `owed` → "riceve", `owes` → "paga", `Owed` → "Dovuto" (ambiguous as a heading: "dovuto" = due, the debtor's side). Check where it is shown.
- **R7 (English left in):** `paypal.me username` → "paypal.me username", `revolut.me username` → "revolut.me username", `wise.com username` → "wise.com username" (placeholders; identical to English; brand names). `Pro+ restored successfully!` → "Pro+ ripristinato con successo!" ("con successo" is a calque).
- **R8 (plural):** the `many` plural category is handled in the widget catalog ("%lld di pagamenti"). The main catalog's `%lld expense` is correct ("%lld spesa" / "%lld spese").
- **R9 (best value):** `Best value` → "Miglior valore".
- **R10 (store pun):** the store description opens with "fare alla romana" (split the bill equally); the site can use it too.
- `Everyone's settled — no transfers needed.` → "Tutti sono in pari — nessun trasferimento necessario." (em dash in UI; do not copy to the site). `Pocket Split` → «Divisione lampo»; its widgets Settle Up → «Salda i conti», Waiting On → «In attesa di» (corrected 2026-11-19 in the page review; the first pass missed the key).

### Glossary

| English term on site | English UI string (key) | Italian UI string (verbatim) | Note |
|---|---|---|---|
| Scan receipt | `Scan Receipt` / `Scan receipt` / `Scan receipts` | Scansiona scontrino / Scansiona scontrino / Scansiona scontrini | R2 |
| Receipts | `Receipts` / `Receipt` | Scontrini / Scontrino | |
| Receipt language | `Receipt Language` | Lingua scontrino | |
| Item-level splits | `Split by items` | Dividi per articoli | R3 |
| Shared dishes | `Shared dishes` / `Add shared item` | Piatti condivisi / Aggiungi articolo condiviso | |
| Equal splitting | `Equal splits & tip` | Divisione equa e mancia | |
| Per person | `Per person` / `Adjust per person` | A persona / Regola a persona | |
| Tip | `Tip` / `Tip included` | Mancia / Mancia inclusa | |
| Tax | `Tax` | Tassa | R1 |
| Subtotal / Total | `Subtotal` / `Total` | Subtotale / Totale | |
| Fair rounding | `Round fairly` | Arrotonda equamente | store: "L'arrotondamento equo" |
| Send totals / payment requests | `Send Payment Requests` | Invia richieste di pagamento | `Payment reminder` → "Promemoria di pagamento" |
| Pay-Me card / payment link | `Pay Me` / `Pay-Me Card` | Pagami / Carta Pay-Me | `Pay Me card is Pro+` → "La carta Pay-Me è Pro+" |
| Text / WhatsApp share | `Text / WhatsApp share` | Condivisione SMS / WhatsApp | the site says iMessage/WhatsApp; the store says "via Messaggi o WhatsApp" |
| Paid | `Paid` | Pagato | |
| Spaces | `Spaces` / `New space` | Spazi / Nuovo spazio | R4 |
| Trips | `Trips` / `Trips & shared expenses` | Viaggi / Viaggi e spese condivise | |
| Balances / settle-up | `Balance` / `Settlement` / `Settle in` | Saldo / Regolamento / Salda in | "saldo conti" in "Spazi e saldo conti sono inclusi in Pro+" |
| Split history | `History` / `Unlimited split history` | Cronologia / Cronologia divisioni illimitata | |
| Templates | `Templates` / `Split template` | Modelli / Modello di divisione | |
| People | `People` | Persone | |
| Currency | `Currency` | Valuta | `Language & Currency` → "Lingua e valuta" |
| Free | `Free` | Gratis | |
| Pro+ | `Pro+` / `Unlock Pro+` / `Upgrade to Pro+` | Pro+ / Sblocca Pro+ / Passa a Pro+ | |
| Pro+ yearly | `Pro+ Yearly` | Pro+ Annuale | |
| Pro+ lifetime | `Pro+ Lifetime` / `Unlock Pro+ Lifetime` | Pro+ a vita / Sblocca Pro+ a vita | `Unlock Pro+ — Pay once` → "Sblocca Pro+ — Paga una volta"; `One-time purchase` → "Acquisto una tantum" |
| Free trial | `%lld-day free trial` | %lld giorni di prova gratis | |
| Best value | `Best value` | Miglior valore | R9 |
| Restore Purchases | `Restore Purchases` | Ripristina acquisti | |
| Split / Start | `Split Receipt` / `Start splitting` / `Split Complete` | Dividi scontrino / Inizia a dividere / Divisione completata | |
| Enter manually | `Enter Items Manually` | Inserisci articoli manualmente | |

### Paid tier names in the Italian UI

**Pro+** (no plain "Pro"), **Pro+ Annuale**, **Pro+ a vita**, "Sblocca Pro+", "Continua con Pro+", "Ripristina acquisti", "Acquisto una tantum". Auto-renew line: "Si rinnova automaticamente ogni anno finché non annulli." Legal line: "Il pagamento sarà addebitato sul tuo Apple ID. L'abbonamento si rinnova automaticamente a meno che non venga annullato almeno 24 ore prima…" and "Questo è un acquisto una tantum senza addebiti ricorrenti." Italian IAP display names on the store: **RightSplit Pro+ annuale**, **RightSplit Pro+ Una tantum**.

### Italian App Store listing (https://apps.apple.com/it/app/rightsplit-dividi-conto-spese/id6757268612, checked 2026-11-19)

- Name: **RightSplit: Dividi Conto Spese** (English "RightSplit: Bill Splitter Tip").
- Subtitle: **Scansiona scontrino con amici** (English "Scan & share group expenses").
- Category: **Utility** (English "Utilities").
- Price: Gratis. In-app purchases: **RightSplit Pro+ Una tantum 8,99 €**, **RightSplit Pro+ annuale 4,99 €** (US: $7.99 lifetime, $3.99 yearly).
- Lingue: "Italiano e altre 33" (34).
- Compatibilità: iOS 17.0, macOS 14.0 (M1), visionOS 1.0 (no iPad listed in the lookup device count; check the master). Size 18,2 MB.
- Description vocabulary (tu, 0 Lei): "fare alla romana", "Scansiona lo scontrino, tocca chi ha preso cosa e manda a ognuno la sua quota esatta", "Non serve un account", "Inquadra lo scontrino con la fotocamera", "righe", "Apple Intelligence", "uno scanner che funziona sul dispositivo", "16 lingue", "Dividi in parti uguali, articolo per articolo", "il resto si ribilanci", "tasse e mancia", "L'arrotondamento equo", "le quote fanno esattamente il totale", "mance predefinite (0, 15, 18 o 20%)", "CHIEDERE I SOLDI SENZA IMBARAZZO", "via Messaggi o WhatsApp", "PayPal.me, Revolut o Wise", "Con Pro+, i widget mostrano chi ti deve ancora dei soldi, e puoi segnare chi ha pagato", "SPAZI, PER LE SPESE CHE NON FINISCONO MAI", "il minor numero di pagamenti che rimette tutti in pari", "bonifici", "58 valute", "tassi della Banca centrale europea", "Attività live", "I TUOI DATI RESTANO CON TE", "«Dati non raccolti»", "Uso in aereo", "Disponibile in 34 lingue", "piano annuale che parte con 3 giorni di prova gratuita, oppure come acquisto unico", "In famiglia". It says "tasse" (not "tassa") once, and "bonifici", not "trasferimenti" as the app does.

---

### 5. Shogiful (`shogiful`, source `shogi/`, ID 6761656926)

### Italian coverage

- `Localization/Localizable.xcstrings`: 3751 keys, all 3751 with `it`, all translated (100%). 39 languages; plain `it`. Most keys are semantic (`tab.play`, `paywall.plan.monthly`), so look up by key. One identical-to-key entry (`piece.%@`, a format key).
- `InfoPlist.xcstrings`: 0/2 (only `CFBundleDisplayName` "Shogiful" and `CFBundleName` "shogi", one language only, no translation needed). The app requests no permissions.
- No extensions or Siri phrases.
- Register: **tu.** 619 strings with tu markers, 124 that start with a tu imperative ("Gioca una partita, poi torna qui per rivedere i tuoi errori", "Cerca due pezzi nemici sulla stessa diagonale", "Studia i joseki di Yagura, Mino e Anaguma"). No voi, no Lei: the 9 "Lei" regex hits are third-person "suo" for the opponent's pieces ("il suo argento", "la sua lancia") and 2 "Giochi" (see below). One ambiguous string: `joseki.centralRook.0001.intro` → "Giochi la Torre centrale dalla prima mossa: pedone in 5f, torre in 5h…" (tu indicative, "you play", not Lei imperative); `lesson.rookChoice.quiz.question` → "Giochi a torre mobile con la torre in 6h." (tu indicative).
- **Verdict: app is in Italian: yes.**

**Italian shogi terms the app uses**
- Pieces (keys `piece.*`): `King` → "Re", `Rook` → "Torre", `Bishop` → "Alfiere", `Gold General` → "Generale d’oro", `Silver General` → "Generale d’argento" (typographic apostrophe), `Knight` → "Cavallo", `Lance` → "Lancia", `Pawn` → "Pedone". In puzzle and lesson prose the generals are "oro" and "argento".
- Promoted pieces: `piece.rook.promoted` → "Drago", `piece.bishop.promoted` → "Alfiere promosso", `piece.knight.promoted` → "Cavallo promosso", `piece.lance.promoted` → "Lancia promossa", `piece.pawn.promoted` → "Pedone promosso", `piece.silver.promoted` → "Generale d’argento promosso". Prose: "la torre promossa (drago, 龍) e l’alfiere promosso (cavallo, 馬)".
- Promotion: `tutorial.promotion.title` → "Promozione", `promotion.title` → "Promuovere?", `promotion.promote` → "Promuovi", `promotion.keep` → "Mantieni". Body: "Quando un pezzo raggiunge il lato opposto, puoi promuoverlo per nuove capacità."
- Drops: the word is **"paracadute" / "paracadutare"** (382 strings; **never** "drop", "rimettere" once): `module.dropDrills.title` → "Esercizi di paracadute", `board.drop.hint` → "Paracaduta %1$@ in %2$@", `mistakeType.dropMistake` → "Errore di paracadute", "paracadutaggio" (noun: "Con un paracadutaggio la casa la scegli tu"), "matto da paracadute di cavallo", "forchetta di cavallo paracadutato". Captured pieces: `tutorial.drop.title` → "Pezzi in mano" (121 strings with "in mano"). Body: "I pezzi catturati passano dalla tua parte. Toccane uno, poi tocca una casa vuota per paracadutarlo." The English "drop" has no standard Italian term; "paracadutare" is the app's own coinage (the store description also says "esercizi di paracadute"). One string says "subito rimesso giù" (`joseki.staticRook.0001.note.12`).
- Other rule and game words: `game.result.checkmate` → "Scacco matto", `game.status.check` → "Scacco!", `game.result.draw` → "Patta", `game.result.resignation` → "Abbandono", `play.resign` → "Abbandona", "Hai vinto!", "Tocca a te", "mossa" (move), "casa" (square), "scacchiera" (board; `game.flipBoard` → "Ruota la scacchiera"), `side.sente` / `side.gote` → "Sente" / "Gote" ("Sente (Nero, muove per primo)", "Gote (Bianco, muove per secondo)"), "matto" for mate (301 strings: "matto d’argento"), `game.status.sennichite` → "Sennichite — patta per ripetizione", `game.result.impasse` → "Patta (stallo / jishōgi)", "handicap" lowercase and capitalised (96 strings; `kif.import.preview.handicap %@` → "Handicap: %@"; `module.komaochiPractice.title` → "Komaochi"), `joseki.staticRook.name` → "Torre statica", `joseki.rangingRook.name` → "Torre mobile", Yagura, Mino, Anaguma kept, castle → "castello" (148), fork → "forchetta" (44), pin → "inchiodato/inchiodare" (39: "argento inchiodato"), skewer: no "infilzata"; the key `concept.bishop-skewer` uses an Italian rendering in prose, hanging piece → "Pezzo in presa" (UI label `mistakeType.hangingPiece`) and "pezzo indifeso" (explanations).
- Names of Japanese concepts stay Japanese: "tsume" lowercase (49: "Lo tsume è l’arte del matto forzato"; "gli tsume"), "joseki" (15) and "jōseki" with macron (5), "tesuji", "yose", "komaochi", "kyu/dan", "uwate", "shitate".

Flags
- **S1 (drop = paracadute):** consistent but unusual (382 strings); Italian shogi writers say "drop" or "reinserimento/inserimento". The site must either follow the app ("esercizi di paracadute", as the store description does) or explain it. Decide with the reviewer; do not mix.
- **S2 (hanging piece, two terms):** `mistakeType.hangingPiece` → "Pezzo in presa" vs the explanation text "Pezzo indifeso" / "Pezzo lasciato indifeso". "In presa" is the chess-Italian for "en prise".
- **S3 (horse):** "cavallo" is both the knight (`piece.knight`) and, in prose, the promoted bishop ("l’alfiere promosso (cavallo, 馬)", "rimodella contro il cavallo promosso", "paracadute di cavallo" = knight drop). Ambiguous for the reader (same as in Spanish).
- **S4 (joseki spelling):** "joseki" (15) vs "jōseki" with macron (5): `module.josekiLab.title` → "Laboratorio jōseki", `explanation.josekiInaccuracy.1.summary` → "Deviazione dal joseki", `mistakeType.josekiInaccuracy` → "Imprecisione di jōseki".
- **S5 (coach):** "Coach" (`settings.coach.title` → "Coach in partita", `analysis.coachTip.label` → "Consiglio del coach", `paywall.hero.coachLimit.title` → "Coach illimitato") vs "allenatore" ("Il tuo allenatore personale di shogi" in onboarding and the store description, `module.yoseTrainer.title` → "Allenatore yose"). The store description also says "il Coach". Both are used; "Coach" is the feature, "allenatore" the persona.
- **S6 (rating):** one value everywhere: `progress.estimatedRating`, `progress.rating`, `gc.leaderboard.estimated_rating.title` → "Punteggio stimato"; the dashboard tile `dashboard.rating` → "Punteggio"; "ELO" in `game.opponentMeta %lld %@` → "%lld ELO · %@". Kyu/dan rank is "grado" (`dashboard.progression.title` → "Il tuo grado"), ladder `hub.progression.ladder.title` → "Scala kyu/dan", "livello" for the opponent level.
- **S7 (levels):** `opponentTier.novice` → "Novizio", `beginner` → "Principiante", `casual` → "Occasionale", `clubPlayer` → "Giocatore di club", `intermediate` → "Intermedio", `advanced` → "Avanzato", `expert` → "Esperto", `master` → "Maestro".
- **S8 (Family Sharing):** the app uses Apple's Italian name **"In famiglia"** ("Premium tramite In famiglia", "In famiglia supportato", "Per configurare In famiglia, apri Impostazioni → ID Apple → In famiglia sul tuo iPhone o iPad."). The store description also says "In famiglia".
- **S9 (Dashboard tab):** `tab.dashboard` → **"Home"** (English left in; the Italian tab is "Home").
- **S10 (best value):** `paywall.bestValue` → "MIGLIOR VALORE" (calque; same as Observa).
- **S11 (piece-set names):** the "Western" set is "Internazionale" (`settings.pieceSet.western`, `onboarding.style.international`), the third is "Scacchi" (`settings.pieceStyle.chess`), traditional is "Tradizionale (kanji)". The site describes three styles (kanji, kanji with arrows, chess pieces); the app's onboarding text "Internazionale: Kanji con frecce di movimento" is the arrows style, which differs from `settings.pieceSet.western` "Internazionale". Check the mapping with the blueprint.
- **S12 (store subtitle):** "Shogi: tattica e analisi IA" (see below).
- **S13 (tips):** the app's tip consumables are "Sostenitore", "Sostegno enorme", "Un caffè" (store IAP names). The in-app text: "Le mance facoltative restano all’acquirente originale (regola di Apple per i beni consumabili)." ("mance" = tips; "beni consumabili" a calque of "consumables").
- `Handicap` has no plain key; `kif.import.preview.handicap %@` → "Handicap: %@". `Go deeper` → "Vai più a fondo" (`paywall.hero.deepAnalysis.title`); `Deep Lines` → "Varianti profonde" (`analysis.deepLines`).

### Glossary

| English term on site | English UI string (key) | Italian UI string (verbatim) | Note |
|---|---|---|---|
| Tab: Dashboard | `Dashboard` (`tab.dashboard`) | Home | S9 |
| Tab: Play | `Play` (`tab.play`) | Gioca | |
| Tab: Analysis | `Analysis` (`tab.analysis`) | Analisi | |
| Tab: Training | `Training` (`tab.training`) | Allenamento | |
| Tab: Progress | `Progress` (`tab.progress`) | Progressi | |
| Premium | `Shogiful Premium` (`settings.premium.name`) | Shogiful Premium | |
| Premium · Monthly | `Premium Monthly` (`paywall.plan.monthly`) | Premium mensile | |
| Premium · Annual | `Premium Yearly` (`paywall.plan.yearly`) | Premium annuale | |
| Lifetime | `Premium Lifetime` (`paywall.plan.lifetime`) | Premium a vita | store IAP "Premium a vita" |
| Upgrade | `Upgrade to Premium` (`settings.premium.upgrade`) | Passa a Premium | `settings.premium.active` → "Premium attivo", `settings.premium.free` → "Piano gratuito" |
| Family Sharing | `Premium via Family Sharing` (`settings.premium.familyShared.title`) | Premium tramite In famiglia | S8 |
| Best value | `BEST VALUE` (`paywall.bestValue`) | MIGLIOR VALORE | S10 |
| Start free trial | `Start Free Trial` (`paywall.startTrial`) | Inizia la prova gratuita | `paywall.trial.compound.format` → "Prova gratuita di %lld giorni" |
| Subscribe | `paywall.subscribeNow` | Abbonati ora | `paywall.purchaseLifetime` → "Acquista a vita" |
| Tsume-shogi | `Tsume-Shogi: Forced Checkmate` (`concept.tsume-basics.title`) | Tsume: lo scacco matto forzato | |
| Tsume Trail | `module.tsumeTrail.title` | Percorso tsume | |
| Drop Drills | `module.dropDrills.title` | Esercizi di paracadute | S1 |
| Castle Atelier | `module.castleAtelier.title` | Atelier dei castelli | |
| Joseki Lab | `module.josekiLab.title` | Laboratorio jōseki | S4 |
| Tesuji / Yose | `module.tesujiCards.title` / `module.yoseTrainer.title` | Carte tesuji / Allenatore yose | |
| Daily plan / assessment | `module.dailyPlan.title` / `module.skillAssessment.title` | Piano giornaliero / Test del livello | `hub.assessment.title` → "Test del livello" |
| Lessons | `hub.lessons.title` / `module.lessons.title` | Lezioni | |
| Handicap play | `module.komaochiPractice.title` | Komaochi | `kif.import.preview.handicap %@` → "Handicap: %@" |
| Game review | `analysis.review.title` | Revisione partita | `dashboard.reviewGame` → "Rivedi partita" |
| Deep analysis | `paywall.hero.deepAnalysis.title` / `analysis.deepLines` | Vai più a fondo / Varianti profonde | the app has no "Deep Analysis" label |
| Engine | `engine.ready` | Motore pronto | "motore"; `YaneuraOu` stays |
| Western / kanji piece sets | `settings.pieceSet.western` / `settings.pieceSet.traditional` / `settings.pieceStyle.chess` | Internazionale / Tradizionale (kanji) / Scacchi | S11 |
| Piece style setting | `settings.pieceSet` / `settings.pieceStyle` | Stile dei pezzi | `settings.boardTheme` → "Tema scacchiera"; notation `settings.notation` → "Stile di notazione": "Giapponese (▲７六歩)", "Occidentale (P-7f)" |
| KIF import | `kif.import.title` / `mac.command.copyKIF` / `analysis.share.kifTitle` | Importa KIF / Copia KIF / Condividi KIF | |
| In-game coach | `settings.coach.title` | Coach in partita | S5; `analysis.coachTip.label` → "Consiglio del coach"; `paywall.hero.coachLimit.title` → "Coach illimitato" |
| Today's training | `dashboard.todaysTraining` | Allenamento di oggi | |
| Train weaknesses | `analysis.trainWeaknesses` | Allena queste debolezze | |
| Estimated rating | `progress.estimatedRating` | Punteggio stimato | S6 |
| Accuracy trend | `dashboard.accuracyTrend` / `progress.accuracyTrend` | Andamento precisione | |
| Skill profile | `progress.skillProfile` / `onboarding.outcomes.radar.label` | Profilo di abilità / Il tuo profilo di abilità | no "radar" label |
| Weakness trends | `progress.weaknessTrends` | Tendenze delle debolezze | |
| Five skills | `skill.tactics` / `skill.defense` / `skill.positioning` / `skill.endgame` / `skill.openings` | Tattica / Difesa / Posizionamento / Finale / Aperture | |
| Blunder / Mistake / Inaccuracy | `analysis.severity.blunder` / `.mistake` / `.inaccuracy` | Errore grave / Errore / Imprecisione | `classification.*`: Mossa migliore, Mossa di teoria, Brillante, Buona mossa, Ottima mossa |
| Drop mistake | `mistakeType.dropMistake` | Errore di paracadute | S1 |
| Castle weakness | `mistakeType.castleWeakness` | Debolezza del castello | |
| Hanging piece | `mistakeType.hangingPiece` | Pezzo in presa | S2 |
| Missed fork | `mistakeType.missedFork` | Forchetta mancata | |
| Missed tsume | `mistakeType.missedTsume` | Tsume mancato | |
| Passive move | `explanation.passiveMove.1.summary` | Mossa passiva: tempo perso | |
| Opponent tiers | `opponentTier.*` | Novizio, Principiante, Occasionale, Giocatore di club, Intermedio, Avanzato, Esperto, Maestro | S7 |
| Kyu / Dan | `hub.progression.ladder.title` | Scala kyu/dan | `dashboard.progression.title` → "Il tuo grado" |
| Resign | `play.resign` / `game.result.resignation` | Abbandona / Abbandono | |
| Promotion prompt | `promotion.title` | Promuovere? | buttons "Promuovi" / "Mantieni" |
| Pieces in hand | `tutorial.drop.title` | Pezzi in mano | |
| Checkmate / Check / Draw | `game.result.checkmate` / `game.status.check` / `game.result.draw` | Scacco matto / Scacco! / Patta | |
| Restore Purchases | `paywall.restore` | Ripristina acquisti | |
| Manage subscription | `settings.premium.manage` | Gestisci abbonamento | |
| Streak | `dashboard.streak` | Serie | |

### Paid tier names in the Italian UI

**Shogiful Premium** with plans **Premium mensile / Premium annuale / Premium a vita**, "MIGLIOR VALORE", "Inizia la prova gratuita", "Ripristina acquisti", "Gestisci abbonamento", "Premium tramite In famiglia", "Un acquisto unico: non c’è nulla da rinnovare o gestire." Trial note: "%@, poi si rinnova automaticamente. Annulla quando vuoi." Lifetime note: "Anche lo sblocco a vita è condivisibile — basta un solo acquisto e tutti i membri della famiglia ottengono Premium." Italian IAP display names on the store: **Premium mensile**, **Premium annuale**, **Premium a vita**, **Sostenitore**, **Sostegno enorme**, **Un caffè**.

### Italian App Store listing (https://apps.apple.com/it/app/shogiful-scacchi-giapponesi/id6761656926, checked 2026-11-19)

- Name: **Shogiful: Scacchi giapponesi** (English "Shogiful Learn & Analyze Shogi").
- Subtitle: **Shogi: tattica e analisi IA** (English "Japanese Chess Tactics Trainer"; "analisi IA" for the on-device engine).
- Category: **Giochi da tavolo** (English "Board").
- Price: Gratis. In-app purchases: **Premium mensile 1,99 €**, **Premium annuale 9,99 €**, **Sostenitore 5,99 €**, **Sostegno enorme 9,99 €**, **Un caffè 1,99 €**, **Premium a vita 22,99 €** (US: lifetime $19.99, Supporter $4.99, Huge Support $9.99, Coffee $1.99).
- Lingue: "Italiano e altre 32" (33).
- Compatibilità: iOS 18.0, iPadOS 18.0, macOS 15.0 (M1), visionOS 2.0. Size 149 MB.
- Description vocabulary (tu, 0 Lei): "Shogiful è il tuo allenatore personale di shogi", "il motore YaneuraOu", "affina il calcolo", "501 problemi tsume", "SALI UNA SCALA DI 40 AVVERSARI", "Vinci le partite per sbloccarne di nuovi", "OGNI MOSSA, ANALIZZATA", "il Coach può darti un suggerimento", "Gli tsume sono i problemi di matto dello shogi, gli scacchi giapponesi", "Ne risolvi 381 gratis, e Premium ne aggiunge altri 120", "99 esercizi di paracadute, per riportare in gioco i pezzi catturati", "62 esercizi sui castelli", "55 esercizi di jōseki", "30 carte tesuji", "62 sfide di yose", "40 scenari con handicap, in Komaochi, nella sezione Allenamento", "80 lezioni", "stile dei pezzi Scacchi", "scacchiera 3D", "PRIVATO E OFFLINE", "GIOCARE È GRATIS", "2 analisi di partita, 3 problemi e 2 suggerimenti del Coach", "Premium mensile e Premium annuale iniziano con 1 settimana di prova gratuita", "Premium a vita è un acquisto unico", "In famiglia", "ID Apple". It uses "esercizi di paracadute" (S1) and "jōseki" with macron.

---

## Cross-app terms

| Concept | Value in each app |
|---|---|
| Restore purchases | "Ripristina acquisti" in all four Italian apps (consistent; no "gli") |
| Settings | "Impostazioni" in Pawza, Observa, Shogiful, RightSplit (consistent) |
| Free | "Gratis" (Pawza, RightSplit; Observa's tier label "Gratuito"); "Piano gratuito" (Shogiful) |
| Best value | "Miglior valore" (Observa, RightSplit), "Miglior rapporto qualità-prezzo" (Observa, one string), "MIGLIOR VALORE" (Shogiful), "Più conveniente" (Pawza) |
| Lifetime | "A vita" in the UI (Observa, Pawza, RightSplit "Pro+ a vita", Shogiful "Premium a vita"); store IAP names say "acquisto singolo" (Observa, Pawza) or "Una tantum" (RightSplit) |
| Monthly / Yearly | "Mensile" / "Annuale" (all four) |
| Free trial | "Inizia la prova gratuita" (Observa, Shogiful); "Inizia la prova gratuita di 7 giorni" (Pawza); "%lld giorni di prova gratis" (RightSplit) |
| Upgrade | "Passa a Premium" (Observa, Shogiful), "Passa a Pawza Pro" (Pawza), "Passa a Pro+" (RightSplit): one verb, "Passa a" |
| Unlock | "Sblocca" (tu imperative) everywhere ("Sblocca Premium", "Sblocca Pawza Pro", "Sblocca Pro+"); no infinitive/imperative split as in Spanish |
| Premium tier name | Observa "Premium", Shogiful "Premium", Pawza "Pro" / "Pawza Pro", RightSplit "Pro+" |
| Add | "Aggiungi" (tu imperative) |
| Score | "Punteggio" (Observa, Shogiful dashboard "Punteggio" / "Punteggio stimato") |
| Scan | "Scansiona / scansione" (Pawza, RightSplit; no "digitalizza") |
| Family Sharing | "In famiglia" (Observa, Shogiful; also in the store descriptions) |
| Tip | "Mancia" (RightSplit); Shogiful tips are "Sostenitore", "Sostegno enorme", "Un caffè"; Observa tip "Sostieni lo sviluppatore" |
| Apple Health | "Apple Health" (English product name kept, Observa) |
| Coach | "Coach" (Shogiful feature, Observa store subtitle "Coach") and "allenatore" |
| Training | "Allenamento" (Observa, Shogiful) |
| Locale code | `it` in four apps; **no Italian in Mockly** |
| Store title punctuation | no space before the colon in all five Italian names |
| Store names | Mockly: Screenshot Maker (English); Observa: VFC, Recupero & Score; Pawza: Salute del Cane e Gatto; RightSplit: Dividi Conto Spese; Shogiful: Scacchi giapponesi |
| Store subtitles | Mockly none shown ("Sviluppatori" = category); Observa "Sonno, Ciclo, Coach Prontezza"; Pawza "Libretto, vaccini e promemoria"; RightSplit "Scansiona scontrino con amici"; Shogiful "Shogi: tattica e analisi IA" |
| English words kept | "check-in", "pattern" (tab), "feedback", "baseline" (Observa, partly), "coach", "widget", "Premium", "Pro+", "Home" (Shogiful tab), "Score" (Observa store name) |

## Flags

App-side Italian string problems (also belong in `ISSUES.md` after review by the main session)

1. **Mockly has no Italian localization** (333 UI strings and 4 InfoPlist keys with no `it` value; the Italian store page shows the English description and no subtitle; 9 store languages, no Italiano). Not a bug for the site, but the Italian page must not promise an Italian interface. If Italian is to be added: `it` in `Localizable.xcstrings` and `InfoPlist.xcstrings`, then Italian store metadata.
2. **Pawza, permission prompts in English (P1):** camera and photo-library texts are English build settings; there is no `InfoPlist.xcstrings` although `it` is a known region. Same defect as German, French and Spanish.
3. **Observa, voi strings in a tu app (A1):** about 60 strings use "voi" (vostro/vostra, "Valutate", "Date priorità… Cercate", "Provate", "Mantenete", "Usate", "Variate", "Pianificate", "Annotate") in coaching and insight advice. App-side fix to tu ("Valuta", "Dai priorità", "Cerca", "Prova"…).
4. **Observa, English left in (18 strings):** four `VO₂ max …` explanation strings identical to English, about 10 half-translated strings ("La tua attività pattern reflects your lifestyle…", "La tua capacità aerobica capacity has room to grow.", "Il tuo VO₂ Max is in the excellent range.", "Camminare heart rate is especially useful…", "Camminare speed is considered a vital sign…") and 3 fully English ("Your active minutes are accumulating…", "Your acute load significantly exceeds your chronic baseline.", "Your VO₂ max is estimated from outdoor walks…"). Also "Sblocca Lifetime Access", "Sblocca HRV Trends".
5. **Observa, sleep stage Core (A5):** `Core %@` → "Profondo %@" (the Deep word), `Core` → "Nucleo", `widget.sleep.core` → "Base", prose "sonno di base (leggero)" and "Core". Fix `Core %@` first (wrong meaning).
6. **Observa, baseline (A2) and patterns (A4):** "riferimento" (146) vs "baseline" (32, mixed gender "il baseline"/"la baseline") vs "linea di base" (10); "pattern" (171) vs "schemi" (161) vs "modelli" (53).
7. **Observa, store name says "VFC"** while the app and the store description say "HRV" (A6); the subtitle "Sonno, Ciclo, Coach Prontezza" lacks a separator (A7). Store metadata, not app code.
8. **RightSplit, "Tassa" for Tax (R1):** use "IVA" (or "imposte"); "tassa" is a levy, not the tax line of a restaurant bill. `Owed` → "Dovuto" is ambiguous (R6); "Invia Feedback" has a capital F (R5).
9. **Shogiful, "paracadute" for drops (S1):** 382 strings use a coined verb ("Paracaduta %1$@ in %2$@", "paracadutaggio"); consistent but non-standard. `tab.dashboard` → "Home" (English, S9). Hanging piece has two labels ("Pezzo in presa" UI, "indifeso" text, S2); "cavallo" means knight and promoted bishop (S3); joseki/jōseki (S4).
10. **Pawza, three words for records (P2)** ("schede", "documenti", "cartella clinica", plus the store's "Libretto") and "account gratuiti" where the app has no accounts (P4); "Riepiloghi" vs "riassunti" (P6).

Register
11. **Observa is tu except ~60 voi strings; Pawza, RightSplit and Shogiful are pure tu; Mockly has no Italian.** No Lei form in any catalog. The site writes tu, so quoting UI strings needs no register change, except the Observa voi strings, which must not be quoted.

Terminology that decides site wording
12. **Observa:** Readiness "Prontezza" (consistent); HRV "HRV" in the UI (store name "VFC"); RMSSD only in the ECG/Premium upsell path (house rule: HRV = SDNN); Family Sharing "In famiglia"; tier "Premium"; training-call verdicts "Intenso / Mantieni / Recupera / Riposo"; Siri phrases `needs_review`.
13. **Shogiful:** rating "Punteggio stimato" (one value), levels "Novizio…Maestro", drops "paracadute", Family Sharing "In famiglia".
14. **RightSplit:** "scontrino" (receipt), "conto" (bill), "Dividi" (split), "mancia" (tip), tax "Tassa" (R1), "Spazi", tier "Pro+".
15. **Pawza:** "scheda/schede" (records), "Animale", "Diario di cura", "Kit pet sitter", "Scheda di emergenza", "Kit animale smarrito", tier "Pawza Pro".
16. **Cross-app:** "Passa a" is the one upgrade verb; "Sblocca" the one unlock verb; "Ripristina acquisti" everywhere; "Miglior valore" vs "Più conveniente" vs "Miglior rapporto qualità-prezzo".

Store listing notes
17. **Mockly's Italian store page is English** (name, description) with no subtitle shown ("Sviluppatori" is the category); Observa's name uses "VFC"; Pawza's name narrows the app to "Cane e Gatto" and its subtitle says "Libretto" (the app says "schede"); RightSplit's subtitle says "scontrino" (app: "scontrino", consistent) and uses "Una tantum" in the IAP name.
18. The seller name, address and phone on the store pages are the owner's personal data and were not copied anywhere. Prices above are reference only; the master file is the source for prices, platforms, trials and Family Sharing.


---

## Italian glossary, batch 4: Soon., Tare, Taskful Day, WanderWiki, Xiangqiful, Clippet

**Method.** Written 2026-11-19 for the Italian (it, Italy) launch, in the structure of `es-glossary.md` (sections 1 to 6). Source: the `.xcstrings` catalogs under `~/Downloads/` (read-only, parsed as JSON with `python3 -I`), locale `it` (every catalog uses plain `it`, no `it-IT`). "Translated" means the `it` localization has a value; I also counted values identical to the English key (English left in) and counted register markers by regex, then hand-checked the hits (tu pronouns and imperatives against Lei subjunctive forms and capitalized Suo/Sua). Terms and keys come from the Spanish glossary's rows plus the English `_apps/<slug>.md` feature names. Store data: iTunes lookup (country=it, lang=it_it) for the name, languages, category and IAP prices; the subtitle, the IAP rows ("Acquisti in-app") and Family Sharing from the apps.apple.com/it page (serialized JSON, Safari UA, Accept-Language it-IT, one 429 retried after 60 s); the description vocabulary from the lookup `description`. The seller name on the store page is not recorded. Clippet is not released (page 404, lookup empty on 2026-11-19), so its row uses the prepared listing in `~/Downloads/clipboard/marketing/aso/listing.json` and `purchases.json` (reference only). Prices are reference only. Italian strings are quoted verbatim, including defects.

**Overall finding.** All six apps are in Italian and every one addresses the user with **tu**. No Lei form (no Tocchi/Aggiunga/Apra, no capitalized Suo/Sua/Lei) was found in any catalog; the only regex hits were false positives (`Conferma…` is a tu imperative, `Attivi: %lld` is an adjective, "La sua/Il suo" are third-person possessives). The site can be written in tu throughout.

---

### 1. Soon. (`soon`, source `countdown/`, ID 6757280643)

#### Italian coverage
| Catalog | keys | `it` translated | % |
|---|---|---|---|
| countdown/countdown/Localizable.xcstrings (main app, paywall) | 741 | 741 | 100 % |
| countdown/countdown/AppShortcuts.xcstrings (Siri, Spotlight) | 13 | 13 | 100 % |
| countdown/countdown/InfoPlist.xcstrings | 6 | 5 | 83 % (only the stray key `Soon` is empty; display name and the calendar and location permission texts are Italian) |
| countdown/CountdownWidgets/Localizable.xcstrings | 184 | 182 | 98.9 % (missing only the format strings `%@ ` and `%@ %@`) |

English left in: `Powered by Apple WeatherKit`, `Soon. — feedback`; the 22 widget gallery names `Soon · Ring`, `Soon · Timeline`, `Soon · StandBy`, `Soon · Hero`, `Soon · Dots`, `Soon · Agenda`, `Soon · Clean`, `Soon · Feature`, `Soon · Horizon`, `Soon · Inline`, `Soon · Lock Row`, `Soon · Moment`, `Soon · Month`, `Soon · Rotating Stack`, `Soon · Streak`, `Soon · Ticket`, `Soon · Year` and so on stay English by design (same as Spanish). **Verdict: app is in Italian: yes.**

#### Register
tu. Main app plus widgets: 83 strings with tu pronouns (tuo/tua/tuoi/tue/ti), 96 strings that open with a tu imperative (Aggiungi, Scegli, Tocca, Attiva, Rimuovi, Crea); 0 Lei. Siri phrases are tu-neutral ("Aggiungi un conto alla rovescia in ${applicationName}", "Quanto manca a ${event}…"). Not mixed.

#### Glossary
| English term on site | English UI string (key) | Italian UI string (verbatim) | Note |
|---|---|---|---|
| Home tab | `Home` | Home | English word kept, as Apple does |
| Plan tab | `Plan` | Piano | |
| Search tab | `Search` | Cerca | verb |
| Profile tab | `Profile` | Profilo | |
| Plan Mode | `Plan mode reminders` | Promemoria in modalità piano | only string naming the mode, so the Italian name is **modalità piano** (the store says "La modalità piano è gratuita") |
| Premium | `Premium` | Premium | `Go Premium` → "Passa a Premium"; `Premium feature. Double tap to upgrade.` → "Funzione Premium. Tocca due volte per passare a Premium."; `Open Soon. to upgrade to Premium.` → "Apri Soon. per passare a Premium." |
| Free | `Free` | Gratis | |
| Monthly / Annual | `Monthly` / `Yearly` | Mensile / Annuale | app says "Yearly", both give "Annuale" |
| Lifetime | `Lifetime` | A vita | `One-time purchase` → "Acquisto una tantum"; the store IAP is "Premium una tantum" |
| 7-day free trial | `1 week free` / `Free trial` | 1 settimana gratis / Prova gratuita | |
| Restore purchases | `Restore Purchases` | Ripristina acquisti | `Purchases Restored` → "Acquisti ripristinati" |
| Countdown | `Countdown` | Conto alla rovescia | **consistent**: 65 strings "conto/conti alla rovescia", 0 "countdown"; `Add countdowns` → "Aggiungi conti alla rovescia"; `Add a Countdown` → "Aggiungi un conto alla rovescia". The store text agrees. Count-up is "conteggio in avanti" (2 widget strings) |
| Event / moment | `Event` / `Moment` / `Moments` | Evento / Momento / Momenti | both words exist as separate keys; `Events` → "Eventi"; `Event Vibe` → "Atmosfera evento" |
| Memories | `Memories` / `Memory` | Ricordi / Ricordo | `Save as memory` → "Salva come ricordo" |
| Reminders | `Reminders` | Promemoria | |
| Reflection mode | `Notes` | Note | no UI string says "Reflection" |
| Daily notes | `Personalized daily notes` / `Weather & daily notes` | Note giornaliere personalizzate / Meteo e note giornaliere | `Forecasts and a fresh thought each day.` → "Previsioni e un pensiero nuovo ogni giorno." |
| Weather | `Weather` / `Weather forecast` / `Smart weather forecast` | Meteo / Previsioni meteo / Previsioni meteo intelligenti | attribution keeps Apple's own name: "Attribuzione Apple Weather", "Dati meteo forniti da Apple Weather" |
| Calendar import | `Import from your calendar` / `Turn calendar events into countdowns` | Importa dal tuo calendario / Trasforma eventi del calendario in conti alla rovescia | `Imported from Calendar` → "Importato dal calendario" |
| Recurring events | `Recurring countdowns` / `Repeat` | Conti alla rovescia ricorrenti / Ripeti | `Repeats` → "Ripetizione" |
| Natural language search | `Search` | Cerca | hints: "“compleanni quest'anno” — finestre temporali naturali", "“l'estate scorsa” — sfoglia i ricordi" |
| Timeline / checklist | `Timeline` / `Checklist` | Cronologia / Lista | FLAG: three words for the timeline: the section "Cronologia", but 10 other strings say "timeline" ("una timeline", "una checklist di partenza e una timeline") and the checklist is "Lista" in the section label but "checklist" in 3 sentences. The store text says "tappe su una cronologia" |
| Themes | `Theme` / `All themes unlocked` | Tema / Tutti i temi sbloccati | theme names are not localized |
| Final Countdown | `Final Countdown` | Conto alla rovescia finale | |
| Widget styles | `Progress Rings`, `TIMELINE` | Anelli di progresso, TIMELINE | gallery names stay English |
| StandBy | `Soon · StandBy` | Soon · StandBy | description: "Un enorme conto alla rovescia da comodino ottimizzato per la modalità StandBy." |
| Lock Screen / Home Screen | `Keep on Lock Screen`; `Your countdown on Home Screen and Lock Screen.` | Mantieni nella schermata di blocco; Il tuo conto alla rovescia su schermata Home e schermata di blocco | **consistent**: "schermata di blocco" (6), "schermata Home" (6); no "schermata bloccata" |
| Event types | `Trip` `Wedding` `Birthday` `Anniversary` `Concert` `Baby` `Exam` `Work` `Holiday` `Health` `Sport` | Viaggio, Matrimonio, Compleanno, Anniversario, Concerto, Bebè, Esame, Lavoro, Festività, Salute, Sport | `Holiday` → "Festività" (public holiday), not "Vacanza" |
| Baby mode | `Baby` | Bebè | |
| On This Day | `ON THIS DAY` | IN QUESTO GIORNO | `Turn on On This Day reminders in Settings to receive these.` → "Attiva i promemoria In questo giorno nelle Impostazioni per riceverli." (WanderWiki says "Accadde oggi" for the same idea) |
| Milestone | `Add milestone` | Aggiungi tappa | `Edit Milestone` → "Modifica tappa"; the store text says "tappe" too |
| Streak (widget) | `Day streak` / `day streak` | Serie di giorni / giorni di fila | |
| Count up | `days since` / `%lld days since` | giorni fa / %lld giorni fa | |
| Pin | `Pin to top` | Fissa in alto | |
| iCloud sync | `iCloud Sync` | Sincronizzazione iCloud | "Con iCloud" in the store text |
| Save | `Save` / `Save moment` | Salva / Salva momento | |
| Settings | `Settings` | Impostazioni | |
| Manage subscription | `Manage Subscription` | Gestisci abbonamento | |
| Tip jar | `TIP JAR` / `Send a Tip` / `Support the Developer` | BARATTOLO DELLE MANCE / Invia una mancia / Supporta lo sviluppatore | `One-time tip. Not a subscription.` → "Mancia una tantum. Non è un abbonamento."; `Tips` → "Consigli" and `Widget Tip` → "Suggerimento widget" use two other words |
| Family Sharing | (store/text) | In famiglia | `One subscription covers your whole Family…` → "…tutto il tuo gruppo In famiglia." (capital I mid-sentence) |

Siri/App Shortcuts (13, verbatim): "Aggiungi un conto alla rovescia in ${applicationName}", "Aggiungi un momento in ${applicationName}", "Crea un conto alla rovescia in …", "Nuovo conto alla rovescia in …", "Giorni a ${event} in …", "Quanto manca a ${event} in …", "Quanti giorni mancano a ${event} in …", "Apri ${event} in …", "Mostra ${event} in …", "Mostra il mio prossimo conto alla rovescia in …", "Mostra il mio prossimo momento in …", "Qual è il mio prossimo momento in …", "Cosa c'è dopo in …".

Permission prompts (verbatim): calendar "Soon. legge i tuoi eventi del calendario per trasformarli in conti alla rovescia. Nulla viene modificato o condiviso."; location "La posizione viene utilizzata per mostrare le previsioni meteo per i tuoi eventi di conto alla rovescia."

Other: apostrophes are mixed between straight (`Data dell'evento`, `Cosa c'è dopo`) and typographic (`fino all’annullamento`); Siri phrase "Giorni a ${event}" is terse next to "Quanto manca a ${event}".

#### Paid tier names in the Italian UI
Premium; plan labels Mensile / Annuale / A vita; "Prova gratuita", "1 settimana gratis"; "Ripristina acquisti"; "Passa a Premium" (`Go Premium with %@ plan for %@` → "Passa a Premium con piano %1$@ a %2$@"); "Gestisci abbonamento"; "Supporta lo sviluppatore". Store IAP names: "Premium mensile", "Premium annuale", "Premium una tantum", "Supporta lo sviluppatore".

#### Italian App Store listing (checked 2026-11-19, https://apps.apple.com/it/app/id6757280643)
- Name: **Soon. Giorni ai Grandi Eventi** (differs from US; Title Case "Grandi Eventi", no hyphen or colon)
- Subtitle: **Matrimonio, Viaggio & Bebè** (Title Case)
- In-app purchases (reference): `Supporta lo sviluppatore 1,00 €` · `Premium una tantum 14,99 €` · `Premium mensile 1,99 €` · `Premium annuale 9,99 €`
- Languages line: **Italiano e altre 35 lingue**. Category: **Stili e tendenze** (also "Utility"). Family Sharing: "In famiglia" listed
- Description vocabulary: "conto alla rovescia", "momento", "schermata Home", "schermata di blocco", "26 widget", "Dynamic Island", "modalità piano", "tappe su una cronologia", "momenti ricorrenti", "Premium", "A vita", "In famiglia", "Comandi Rapidi", "iCloud", "promemoria e previsioni". Opening: "Sta per arrivare qualcosa di bello. Soon. te lo tiene sotto gli occhi…". Register tu.

---

### 2. Tare (`tare`, source `weightbalance/`, ID 6806255929)

#### Italian coverage
| Catalog | keys | `it` translated | % |
|---|---|---|---|
| weightbalance/weightbalance/Localizable.xcstrings (the only catalog) | 121 | 121 | 100 % |

No InfoPlist, no permission prompts, no Siri phrases; the display name stays "Tare". **Verdict: app is in Italian: yes.**

#### Register
tu. Few strings carry the voice: 9 tu imperatives ("Tocca due volte per…", "Acquista il capitolo…", "Apri i capitoli…", "Riprova", "Appendi: %@"), 1 possessive ("Tuoi per sempre."), 0 Lei. Safe for tu.

#### Glossary
| English term on site | English UI string (key) | Italian UI string (verbatim) | Note |
|---|---|---|---|
| Chapter I…X | `Chapter %lld` | Capitolo %lld | `Chapter complete` → "Capitolo completato" |
| Unlock / buy chapters | `Open Chapters %lld to %lld` / `Buy Chapters %lld to %lld, %@` / `Buy Chapter %lld, %@` | Apri i capitoli da %1$lld a %2$lld / Acquista i capitoli da %1$lld a %2$lld, %3$@ / Acquista il capitolo %1$lld, %2$@ | locked: "Capitolo %lld, non acquistato" |
| Unlock text | `%@ more %lld chapters of handcrafted levels. Yours forever.` | Altri %1$@ %2$#@chapters@ di livelli fatti a mano. Tuoi per sempre. | plural "capitolo / capitoli". Check word order on screen: "%@" precedes the count (same note as Spanish) |
| Restore purchases | `Restore purchases` | Ripristina acquisti | |
| Settings | `Settings` | Impostazioni | |
| Hints | `Hints` / `Hint` | Suggerimenti / Suggerimento | Italian uses "suggerimento" (the store text too: "I suggerimenti restano spenti…"); Xiangqiful also says "suggerimenti" |
| Three gold stars | `Marks` | Stelle | store text: "stelle d'oro"; no UI key says "gold" |
| Sound / Haptics | `Sound` / `Haptics` | Suono / Vibrazione | |
| High contrast | `High contrast` | Contrasto elevato | store text: "il contrasto elevato" |
| Beam | `Beam %lld` | Asta %lld | **asta**: "Asta %1$lld, appesa all'asta %2$lld…"; the store text agrees ("ogni asta non è in equilibrio"). The arm stays "braccio": `%@ arm, notch %lld` → "Braccio %1$@, tacca %2$lld" |
| Hook / notch | `empty hook` / `notch` | gancio vuoto / tacca | `Every hook filled. Not balanced.` → "Tutti i ganci occupati. Non in equilibrio." |
| Weight | `%@, weight %lld` | %1$@, peso %2$lld | `hidden %@` → "%@, peso nascosto"; weights are named by colour and shape: `cobalt kite` → "aquilone cobalto", `vermillion disc` → "disco vermiglio", `teal drop` → "goccia verde acqua", `soot ring` → "anello fuliggine", `bone fan` → "ventaglio osso", `plum lozenge` → "rombo prugna", `violet pebble` → "ciottolo viola", `leaf petal` → "petalo verde foglia", `chrome lens` → "lente cromata", `terracotta crescent` → "mezzaluna terracotta" |
| Pans | (no key) | (none) | Tare has no pans |
| Picture cards | `Reference scale` | Bilancia di riferimento | VoiceOver wording ("Bilancia di riferimento, inclinata, lato sinistro più pesante."); no UI string says "picture card" |
| Shelf (weights below) | `Tray` / `Return to tray` | Vassoio / Rimetti sul vassoio | `%@ returned to the tray.` → "%@ di nuovo sul vassoio." |
| Balanced | `Balanced` / `balanced` | In equilibrio / in equilibrio | `Balanced. Level complete.` → "In equilibrio. Livello completato." |
| Mobile | `Mobile` | Scultura | the hanging sculpture is **scultura** in the app (not "mobile"); the store text avoids the word |
| Play | `Play` | Gioco | noun |
| Level | `Level %lld` | Livello %lld | `Level %lld, solved` → "Livello %lld, risolto" |
| Restart / Pause / Resume | `Restart level` / `Pause` / `Resume` | Ricomincia il livello / Pausa / Riprendi | `Paused` → "In pausa"; `Exit to grid` → "Torna alla griglia" |
| Chapter names | `The Hang`, `The Secret`, `The Cascade`, `The Exhibition`, `The Ledger`, `The Inventory`, `The Fulcrum`, `The Forgery`, `The Restoration`, `The Retrospective` | L'Allestimento, Il Segreto, La Cascata, L'Esposizione, Il Bilancio, L'Inventario, Il Fulcro, Il Falso, Il Restauro, L'Antologica | in the catalog's order; Title Case in Italian ("La Cascata") |
| Worlds | `Morning Sky`, `Twilight Meadow`, `Deep Sea`, `Evening Stars`, `Coral Reef`, `Firefly Forest`, `Polar Night`, `Rose Dawn`, `Summer Fields`, `Sunset Hills` | Cielo del mattino, Prato al crepuscolo, Mare profondo, Stelle della sera, Barriera corallina, Bosco delle lucciole, Notte polare, Alba rosata, Campi d'estate, Colline al tramonto | `Canvas` → "Tela"; `Automatic, each chapter its own world` → "Automatico, ogni capitolo con il suo mondo" |
| Share / rate | `Share Tare` / `Rate Tare` | Condividi Tare / Valuta Tare | |
| Terms | `Terms of use` / `Privacy` | Condizioni d'uso / Privacy | |
| Chapters (IAP) | store product | Capitoli II–X | settled name; matches the store |

#### Paid tier names in the Italian UI
No tier name: Tare is free with chapter packs. The UI sells chapters ("Acquista i capitoli da %1$lld a %2$lld, %3$@", "Apri il capitolo %lld", "…Tuoi per sempre."). Store IAP: **"Capitoli II–X"**.

#### Italian App Store listing (checked 2026-11-19, https://apps.apple.com/it/app/id6806255929)
- Name: **Tare: Puzzle Logico Rilassante** (differs from US "Tare: Balance Logic Puzzle"; Title Case)
- Subtitle: **Rompicapo con Pesi Nascosti** (Title Case; "Rompicapo" in the subtitle against "Puzzle" in the name)
- In-app purchase (reference): `Capitoli II–X 2,99 €`
- Languages line: **Italiano e altre 43 lingue**. Category: **Rompicapo** (also "Giochi", "Casual"). Family Sharing: "In famiglia" listed
- Description vocabulary: "puzzle di equilibrio senza parole", "200 livelli fatti a mano", "asta", "peso × distanza", "stelle d'oro", "suggerimenti", "dieci capitoli, dieci mondi luminosi", "VoiceOver, Riduci movimento e il contrasto elevato", "«In famiglia»". Matches the app. Register tu ("Pensa per tutto il tempo che vuoi").

---

### 3. Taskful Day (`taskful-day`, source `TaskLogger/`, ID 6757345400; iPhone, iPad, Mac, Watch target)

#### Italian coverage
| Catalog | keys | `it` translated | % |
|---|---|---|---|
| TaskLogger/Localization/Localizable.xcstrings (main app) | 1427 | 1427 | 100 % |
| TaskfulDayKit Localizable.xcstrings (shared package, Watch strings) | 114 | 112 | 98.2 % (missing `End focus session`, `Extend focus session`) |
| TaskLogger/InfoPlist.xcstrings | 7 | 7 | 100 % (calendar, Reminders, microphone, speech) |
| TaskLogger/AppShortcuts.xcstrings | 12 | 12 | 100 % |
| TaskLoggerWidgetsExtension Localizable + InfoPlist | 420 + 3 | 420 + 3 | 100 % |
| watchkitapp Watch App/AppShortcuts.xcstrings | 4 | 4 | 100 % |

English left in: `Taskful Day Pro` (brand), `Inbox` (widget name and 12 strings, see flags), "insight" in one sentence, "Lifetime" in one sentence, "focus". **Verdict: app is in Italian: yes** (two shared-package Watch strings fall back to English).

#### Register
tu. Main + widgets + Kit: 141 strings with tu pronouns, 121 opening with a tu imperative (Tocca, Aggiungi, Apri, Scegli, Scopri, Crea, Vedi), 0 Lei. Insight sentences are tu ("Ottimo ritmo — ti presenti con costanza.", "Sii gentile con te."). Siri phrases tu ("Quante cose ho oggi in …", "Cosa devo fare in …"). Not mixed.

#### Glossary
| English term on site | English UI string (key) | Italian UI string (verbatim) | Note |
|---|---|---|---|
| Day Clock | `clock.title`, `pro.feature.clock_view` | Orologio del giorno | desc: "Visualizza la tua giornata su un orologio di 24 ore." Store: "l'Orologio del giorno" |
| Energy River | `river.title`, `pro.feature.energy_river` | Fiume dell’energia / Fiume di energia | FLAG: two spellings (`river.title` "Fiume dell’energia", Pro feature "Fiume di energia"; short `day_experience.river` "Fiume"). Store text uses "Fiume di energia". Desc: "Visualizza la tua giornata come una timeline che scorre con calma." |
| Day Map | `pro.feature.day_map` | Mappa del giorno | `map.title` → "Mappa"; desc "Panoramica spaziale con analisi della densità energetica." |
| Focus Orbit / Focus Mode | `pro.feature.focus_orbit` | Modalità concentrazione | FLAG: three terms for focus: "Modalità concentrazione" (Pro feature, store), "Focus" (`focus.enter`, "Sessione focus", "Avvia focus", 20 strings) and "Concentrati" (`pad.focus.enter`). No string says "Focus Orbit" |
| Inbox | `inbox.list.title` / `inbox.title` | Posta in arrivo / Aggiungi alla casella | FLAG: three terms: "Posta in arrivo" (list title, the Mail word), "casella" ("La casella è vuota.", "Cattura rapida nella casella") and the English "Inbox" (widget names `widget.name.inbox`, `pad.inbox.empty.title` "La inbox è vuota") |
| Today / Tomorrow | `inbox.chip.today` / `inbox.chip.tomorrow` | Oggi / Domani | `inbox.chip.later` → "Più tardi"; `schedule.next_week` → "Prossima settimana" |
| Tabs | `tab.tasks`, `tab.all_tasks`, `tab.analytics`, `tab.settings`, `tab.add` | Attività, Tutte le attività, Analisi, Impostazioni, Aggiungi | |
| Insights / analytics | `analytics.insights.title` / `pro.feature.analytics` | Approfondimenti / Analisi e approfondimenti completi | consistent "approfondimenti" (15 strings); one stray English "insight" in `pro.preview.analytics.desc` ("punteggi, serie, tendenze e insight intelligenti"). The store text says "La scheda Analisi" |
| Journal | `journal.title` | Diario | entries "voci di diario" |
| Mood | `mood.timeline.title` / `journal.mood.prompt` | Umore / Come è stata la tua giornata? | scale: Fantastico, Bene, Neutro, Stressato; "Andamento dell’umore" |
| Workspaces | `pro.feature.workspaces` / `pad.workspace.*` | Spazi di lavoro multipli / Tutti gli spazi, Gestisci spazi di lavoro… | |
| Carry forward | `today.carry_forward.title` / `.button` / `settings.auto_carry_forward.title` / `pad.canvas.carry.title` | Rinvia a oggi / Rinvia / Sposta le attività in sospeso / Riporta | FLAG: four verbs for one feature (Rinvia, Sposta, Riporta, "rinviata"). "Rinvia" means "postpone", the opposite of moving a task to today. `accessibility.carry_forward_hint` → "Sposta %@ a oggi"; `auto_carry_forward.migration.title` → "Le attività non completate ora vengono spostate in automatico." (the store: "passano da sole a oggi") |
| Voice capture | `pad.sidebar.voice.a11y` / `voice.create_task` / `pro.feature.voice` | Cattura vocale / Crea attività / Input vocale intelligente | "Cattura" is the app's capture verb (14 strings); "Input vocale" is a loanword |
| iCloud sync | `settings.icloud_sync` | Sincronizzazione iCloud | |
| Apple Reminders import | `settings.import_reminders` / `pro.feature.reminders` | Importa da Promemoria / Reimportazione Promemoria | |
| Widgets (Pro) | `pro.widgets.unlock_all` / `widget.gallery.pro_widgets` | Sblocca tutti i widget / Widget Pro | `widget.gallery.unlock_pro` → "Sblocca Pro per accedere a tutti i widget." |
| Pro | `pro.paywall.title` / `settings.pro.unlock` | Taskful Day Pro / Sblocca Pro | consistent "Sblocca" |
| Free | `settings.pro.status.free` / `checklist.pro.limit.description` | Piano gratuito / La versione gratuita include 1 elemento per attività. | FLAG: "piano gratuito" against "versione gratuita" |
| Monthly / Yearly / Lifetime | `pro.plan.monthly` / `.yearly` / `.lifetime` | Mensile / Annuale / A vita | `pro.buy_lifetime` → "Acquista a vita"; status "Pro mensile", "Pro annuale", "Pro a vita"; `pro.badge.one_time` → "Una tantum"; FLAG: `pro.terms.lifetime` → "Lifetime è un acquisto unico. Nessun rinnovo." (English word left in) |
| 7-day free trial | `pro.trial.badge` / `pro.start_trial` | Prova gratuita di 7 giorni / Inizia la prova gratuita di 7 giorni | `onboarding.trial.subtitle` "Tutte le funzioni Pro sono attive per i tuoi primi 7 giorni — gratis, senza carta." |
| Restore purchases | `pro.restore` | Ripristina acquisti | |
| Schedule (week grid) | `overview.schedule` / `form.section.schedule` | Pianificazione | `a11y.reschedule` → "Riprogramma"; the store says "griglia a blocchi orari" |
| Overdue / Later | `analytics.overdue` / `inbox.chip.later` | In ritardo / Più tardi | "Tasso di rinvio", "Nessuna attività rinviata" |
| Streak | `analytics.streaks.title` | Serie | "Serie attuale", "Miglior serie" |
| Quick Add | `Quick Add` | Aggiunta rapida | `today.quick_add.placeholder` → "Aggiungi un compito..." |
| Natural-language capture | `Quickly add a task using natural language` | Aggiungi un'attività usando il linguaggio naturale | the store says "L'inserimento in linguaggio naturale" |
| Task | (many) | attività | **attività** is the term (268 strings), but "compito/compiti" appears in 23 (`Complete Task` → "Completa compito", `intent.task_count.empty` "Nessun compito per oggi.", "Hai creato 50 compiti con il piano gratuito"). FLAG |

Other flags:
- Mixed "attività" and "compito" (above); "Aggiungi un compito..." against "Aggiungi un'attività" for the same action.
- `a11y.day_map_zone.hint` → "Tocca due volte per espandere. Tieni premuto e trascina per riprogrammare." (fine).
- The paywall lists Day Clock, Day Map, Energy River and Focus Mode as Pro; the site's Free tier says "four visual day views" (same note as Spanish); the Italian store text agrees with Pro ("Quattro viste di una sola giornata… Pro aggiunge altre tre").
- Siri phrases (verbatim, main): "Aggiungi attività in ${applicationName}", "Completa attività in …", "Crea attività in …", "Segna attività come fatta in …", "Termina attività in …", "Quante attività ho in …", "Quante cose ho oggi in …", "Nuova attività in …", "Prossima attività in …", "Numero di attività in …", "Cosa devo fare in …", "Cosa c'è dopo in …". Watch: "Aggiungi attività in …", "Annota in …", "Nuova attività in …", "Ricordamelo in …" (note: Watch says "Annota" where the app says "Cattura"; main Siri "Completa attività" and the intent strings use "compito").
- Permission prompts (verbatim): calendar "Mostra gli eventi del calendario accanto alle tue attività, così l'intero programma della giornata è in un unico posto."; Reminders "Taskful Day può importare i tuoi Promemoria Apple per aiutarti a pianificare la giornata in un unico posto."; microphone "Taskful Day utilizza il microfono per consentirti di creare attività rapidamente con la voce."; speech "Taskful Day utilizza il riconoscimento vocale per trasformare la tua voce in testo delle attività."; copyright "© 2025 Taskful Day. Tutti i diritti riservati."

#### Paid tier names in the Italian UI
"Taskful Day Pro"; plan labels Mensile / Annuale / A vita; status "Pro mensile", "Pro annuale", "Pro a vita", "Piano gratuito"; "Inizia la prova gratuita di 7 giorni"; "Ripristina acquisti"; "Sblocca Pro"; "Gestisci abbonamento". Store IAP names: "Taskful Day Pro mensile", "Taskful Day Pro annuale", "Taskful Day Pro una tantum", "Sostieni lo sviluppatore".

#### Italian App Store listing (checked 2026-11-19, https://apps.apple.com/it/app/id6757345400)
- Name: **Taskful Day: Pianificatore** (US "Taskful Day: Day Planner")
- Subtitle: **Lista Attività & Focus** (Title Case; "Focus" English)
- In-app purchases (reference): `Sostieni lo sviluppatore 1,00 €` · `Taskful Day Pro una tantum 44,99 €` · `Taskful Day Pro annuale 29,99 €` · `Taskful Day Pro mensile 2,99 €`
- Languages line: **Italiano e altre 33 lingue**. Category: **Produttività** (also "Utility"). Family Sharing: "In famiglia" listed
- Description vocabulary: "planner giornaliero calmo", "Oggi", "inserimento in linguaggio naturale", "Centro di Controllo" (capitals), "Orologio del giorno", "Fiume di energia", "Mappa del giorno", "griglia a blocchi orari", "21 widget per la schermata Home", "widget per la schermata di blocco", "Modalità concentrazione", "Attività in tempo reale", "Apple Watch", "scheda Analisi", "sincronizzazione iCloud", "spazi di lavoro multipli", "le verifiche", "app Promemoria", "accesso a vita", "acquisto una tantum", "In famiglia". Register tu.

---

### 4. WanderWiki (`wanderwiki`, source `WanderWiki/`, ID 6758459119)

#### Italian coverage
| Catalog | keys | `it` translated | % |
|---|---|---|---|
| WanderWiki/Resources/Localizable.xcstrings (main app) | 425 | 425 | 100 % |
| WanderWikiWidget/Localizable.xcstrings | 129 | 129 | 100 % |

No InfoPlist, no AppShortcuts catalog. English left in: `Skip (Debug)` (a debug string), names (`Marie Curie`, `Voyager 1`, `Tycho Brahe`). **Verdict: app is in Italian: yes.**

#### Register
tu. 45 strings with tu pronouns, 48 opening with a tu imperative (Tocca, Scegli, Salva, Prova, Scopri), 0 Lei. Not mixed.

#### Glossary
| English term on site | English UI string (key) | Italian UI string (verbatim) | Note |
|---|---|---|---|
| Random | `random_mode` | Casuale | |
| Browse | `browse_title` | Esplora | the store text: "Esplora 16 categorie" |
| For You | `for_you_mode` | Per te | quoted «Per te» in running text |
| Today in History | `Today in history` / `On This Day` | Accadde oggi | both give the same string; `Today in history: %@` → "Oggi nella storia: %@"; `feature_history` → "Scopri cosa è successo oggi nella storia"; matches Italian Wikipedia's own name |
| On This Day categories | `Events` / `Births` / `Deaths` / `Holidays` | Eventi / Nascite / Morti / Festività | the store says "eventi, nascite, morti e festività" |
| Tabs | `feed_tab` / `profile_tab` / `settings` | Feed / Profilo / Impostazioni | "Feed" loanword in 6 strings ("Feed personalizzato") |
| WanderWiki Plus | `unlock_premium` / `Premium feature` | Sblocca Premium / Funzione premium | no "Plus" string; tier is "Premium". Capitalization: "Premium" on the button, "premium" in "Funzione premium" and "un'esperienza premium" |
| Monthly / Annual / Weekly / Lifetime | `monthly` / `yearly` / `weekly` / `lifetime` | Mensile / Annuale / Settimanale / A vita | `paywall_monthly_per_month` → "al mese"; `unlock_lifetime_access` → "Sblocca l'accesso a vita"; `paywall_lifetime_own` → "WanderWiki tuo per sempre" |
| Best long-term value | `best_value` | Miglior offerta | |
| Free trial | `%lld-day free trial` / `Start %lld-Day Free Trial` | Prova gratuita di %lld giorni / Inizia la prova gratuita di %lld giorni | |
| Free articles per day | `%lld free articles left today` | Ti restano %lld articoli gratis oggi | |
| Restore purchases | `restore_purchases` | Ripristina acquisti | |
| Saved | `saved` / `Saved` | Salvato / Salvati | |
| Liked list | `liked` / `like` | Ti piace / Mi piace | `no_liked_articles_hint` → "Tocca il cuore sugli articoli che ti piacciono" |
| Folders | `Folders` / `New folder` | Cartelle / Nuova cartella | |
| Read aloud | `Listen` | Ascolta | |
| Where Next | `Where next` | E adesso? | |
| Show less / hide | `Show less like this` / `Hide this article` | Mostra meno di questo / Nascondi questo articolo | |
| Reader themes | `Reader Theme`, `Sepia`, `Solarized` | Tema di lettura, Seppia, Solarized | |
| Search | `Search Wikipedia` | Cerca su Wikipedia | |
| Reading streak | `%lld-day streak` / `Streak reminder` | Serie di %lld giorni / Promemoria serie | `Don't break your streak` → "Non interrompere la tua serie"; store: "serie di lettura" |
| Widgets | `On This Day`, `Reading Year`, `Continue Reading`, `Got a Minute`, `Two Doors` | Accadde oggi, Anno di lettura, Riprendi la lettura, Hai un minuto?, Due porte | control `Surprise Me` → "Sorprendimi" |
| On-device summaries | `AI summary: %@` | Riassunto IA: %@ | "I riassunti IA vengono generati sul tuo dispositivo." ("IA" not "AI") |
| 16 topics | `interest_*` | Scienza, Tecnologia, Storia, Arti, Musica, Sport, Natura, Spazio, Filosofia, Geografia, Letteratura, Cinema, Gastronomia, Architettura, Matematica, Politica | `movies` → "Cinema", `food` → "Gastronomia" |
| No ads | `feature_no_ads` / `onboarding_benefit_no_ads_title` | Esperienza senza pubblicità / Niente pubblicità. Niente rumore. | `tip_bullet_no_ads` → "Niente pubblicità. Niente tracciamento. Niente investitori." |
| Offline reading | `Offline Reading` | Lettura offline | `Ready offline` → "Disponibili offline" |
| Manage subscription | `manage_subscription` | Gestisci abbonamento | |

Other flags:
- **`Cancel anytime.` → "Cancella in qualsiasi momento."** and `Start your %lld-day free trial. Cancel anytime.` → "…Cancella in qualsiasi momento." In Italian "cancellare" means delete; the verb for ending a subscription is "annullare" (the app uses "Annulla" for `Cancel` elsewhere, and the store description says "annullarlo"). The auto-renewal disclosure's "salvo cancellazione" is acceptable.
- `for_you_english_only` → "Il feed personalizzato è attualmente disponibile solo in inglese." The site says native category queries work in 17 editions; the string may be stale (same flag as the other languages). `For You isn't available in %@ yet — showing Random.` → "«Per te» non è ancora disponibile in %@ — viene mostrato Casuale."
- "Morti" is blunt; the Wikipedia Italian term is "Morti" in "Nati e morti", so it is acceptable.
- `Skip (Debug)` left in English (probably debug-only, confirm).
- Weekly plan exists in the app and store (`WanderWiki settimanale 0,99 €`); the site does not list it.

#### Paid tier names in the Italian UI
"Premium" (button "Sblocca Premium"; headline "WanderWiki è un'esperienza premium."); plan labels Mensile / Annuale / Settimanale / A vita; "Miglior offerta"; "Ripristina acquisti". Store IAP names: "WanderWiki mensile", "WanderWiki annuale", "WanderWiki settimanale", "WanderWiki acquisto singolo", "Sostieni lo sviluppatore".

#### Italian App Store listing (checked 2026-11-19, https://apps.apple.com/it/app/id6758459119)
- Name: **WanderWiki: scopri e impara** (US differs; sentence case)
- Subtitle: **Fatti, storia e curiosità**
- In-app purchases (reference): `WanderWiki annuale 9,99 €` · `WanderWiki settimanale 0,99 €` · `Sostieni lo sviluppatore 1,00 €` · `WanderWiki acquisto singolo 29,99 €` · `WanderWiki mensile 1,99 €`
- Languages line: **Italiano e altre 33 lingue**. Category: **Istruzione** (also "Consultazione"). Family Sharing: "In famiglia" listed
- Description vocabulary: "schede", "20 articoli gratis ogni giorno", "16 categorie", "«Per te»", "ACCADDE OGGI", "eventi, nascite, morti e festività", "In evidenza", "tempo di lettura", "cartelle", "promemoria serie", "serie di lettura", "riepilogo settimanale", "cinque widget", "«Anno di lettura»", "«Riprendi la lettura»", "«Hai un minuto?»", "«Due porte»", "schermata Home", "Premium", "Mensile o Annuale", "una settimana di prova gratuita", "A vita", "In famiglia", "annullarlo" (subscription), "Account Apple". Store text says "A vita" while the IAP row says "acquisto singolo". Register tu.

---

### 5. Xiangqiful (`xiangqiful`, source `Xiangqi/`, ID 6794340136; iPhone, iPad, Mac, Game Center)

#### Italian coverage
| Catalog | keys | `it` translated | % |
|---|---|---|---|
| Xiangqi/Localization/Localizable.xcstrings (main app, paywall) | 3273 | 3273 | 100 % |
| Xiangqi/Localization/InfoPlist.xcstrings | 2 | 2 | 100 % (display name stays "Xiangqiful") |

No widget or extension catalogs. English left in: `Xiangqiful Premium` (brand), `Focus: %@` (2 strings), pinyin names (`Zhāng Lǎoshī`, `Xīnwǔ Cánbiān`), format strings. **Verdict: app is in Italian: yes.**

#### Register
tu. 224 strings with tu pronouns, 46 opening with a tu imperative (Gioca, Tocca, Scegli, Scopri), many more mid-sentence ("Gioca la mossa che pensi vincente."); 0 Lei. "La sua / Il suo" occurrences are third-person (opponent biographies). Not mixed.

#### Glossary
| English term on site | English UI string (key) | Italian UI string (verbatim) | Note |
|---|---|---|---|
| Tabs | `tab.dashboard`, `tab.play`, `tab.training`, `tab.analysis`, `tab.progress` | Home, Gioca, Allenamento, Analisi, Progressi | |
| Game Review | `analysis.review.title` | Revisione della partita | |
| Analyze | `analysis.analyse` | Analizza | |
| Move grades | `classification.best/great/good/book/inaccuracy/mistake/blunder` | Ottima, Eccellente, Buona, Teoria, Imprecisione, Errore, Svista | `Blunder` → "Svista" (store: «da "Ottima" a "Svista"»); `Book` → "Teoria"; "Ottima" is the top grade, "Eccellente" the second |
| Accuracy | `analysis.accuracy.title` | Precisione | |
| Estimated rating | `progress.estimatedRating` | Punteggio stimato | "Punteggio", not "Elo"; store: «Un "Punteggio stimato"» |
| Skill profile / radar | `progress.radar.title` | Profilo di abilità | paywall: "Radar delle abilità completo, tendenze e progressi settimanali" (radar named "Radar delle abilità") |
| Weakness trends | `progress.weaknesses.title` | Tendenze delle debolezze | |
| Five skills | `skill.category.tactics/defense/positioning/endgame/openings` | Tattica, Difesa, Posizionamento, Finale, Aperture | |
| Phases | `phase.opening/middlegame/endgame` | Apertura, Mediogioco, Finale | |
| Today's plan | `training.plan.title` | Il piano di oggi | |
| Lessons / 8 tracks | `module.lessons.title`; `lesson.track.*.title` | Lezioni; Fondamenti, Aperture, Difesa del palazzo, Tattiche di cannone, Tecnica del cavallo, Mediogioco, Finale, Avanzato | tracks are "percorsi" in the store text ("otto percorsi"); sentence case here |
| Skill assessment | `module.skillAssessment.title` | Valutazione delle Abilità | FLAG: Title Case; the store says «la "Valutazione delle Abilità" (15 posizioni)» |
| Drill modules | `module.tactics`, `cannonRange`, `horseTrails`, `palaceWorkshop`, `endgameStudio`, `openingLab`, `mateTrail`, `tacticCards`, `handicapHouse` | Campo di Tattica, Poligono del Cannone, Sentieri del Cavallo, Officina del Palazzo, Studio dei Finali, Laboratorio delle Aperture, Percorso di Matto, Carte Tattiche, Casa degli Handicap | Title Case; store: «dal "Laboratorio delle Aperture" alla "Casa degli Handicap"» |
| Mate problems | `training.kind.mate` / `progress.stat.puzzles` | Problema di matto / Problemi | store: "902 problemi di matto" |
| Coach hints | `paywall.benefit.coach` | Suggerimenti illimitati dall'allenatore in partita | "suggerimento" (as Tare) |
| Named mistakes | `mistake.*.name` | Tattica di cannone mancata, Pezzo intrappolato, Matto mancato, Pezzo indifeso, Forchetta mancata, Inchiodatura mancata, Infilata mancata, Tattica mancata, Debolezza del palazzo, Generale esposto, Imprecisione di apertura, Errore di finale, Mossa passiva | the store also cites "Cavallo intrappolato" and "Consiglieri spezzati" |
| Piece style (setting) | `board.pieceSet.title` / `.traditional` / `.western` / `.hybrid` | Pezzi / Tradizionale / Occidentale / Ibrido | **setting `Pieces` → "Pezzi"** (the site's "piece style"). Store: «simboli occidentali o … un set ibrido» |
| Piece set (finish) | `board.pieceFinish.title` and values | Finitura dei pezzi; Avorio, Legno intagliato, Melammina da club, Giada, Ciottolo di fiume, Porcellana, Lacca dorata, Palissandro e ottone | the eight finishes. FLAG: `game.settings.pieceSet` also reads "Pezzi" (same label as `board.pieceSet.title`) |
| Characters | `board.charset.title` / `.traditional` / `.standard` | Caratteri / Tradizionale / Semplificato | |
| Notation | `board.notation.title` / `.wxf` / `.chinese` | Notazione delle mosse / WXF / Cinese | `game.settings.notation` → "Notazione" |
| Boards | `board.theme.*` | Bosso, Palissandro, Tavolo di pietra del parco, Tappetino da club, Rotolo di carta di riso, Lacca rossa e oro, Marmo e giada; `3D Board` | `board.theme.title` → "Scacchiera"; "carta di riso" for xuan paper is a loose rendering |
| Flip board / New game | `game.toolbar.flip` / `mac.command.newGame` | Capovolgi la scacchiera / Nuova partita | |
| Premium | `settings.premium.upgrade` | Passa a Premium | "Benvenuto in Premium" (`paywall.success.title`) |
| Free | `settings.premium.free` | Piano gratuito | |
| Monthly / Yearly / Lifetime | `paywall.plan.monthly` / `.yearly` / `.lifetime` | Mensile / Annuale / A Vita | FLAG: "A Vita" (Title Case, 6 paywall strings: "Acquista comunque A Vita", "Hai già A Vita"), "A vita" in settings (`settings.premium.lifetimeNoManage` "A vita — niente da rinnovare, niente da annullare") and the store IAP "Premium a vita"; `paywall.purchaseLifetime` → "Sblocca per sempre"; `paywall.oneTime` → "Acquisto una tantum" |
| Best value | `paywall.bestValue` | Il più conveniente | |
| Start free trial | `paywall.startTrial` | Inizia la prova gratuita | `paywall.trial.compound.format` → "Prova gratuita di %lld giorni" |
| Restore purchases | `paywall.restore` | Ripristina acquisti | |
| Check / checkmate / stalemate | `game.status.check` / `game.reason.checkmate.win` / `gc.achievement.stalemate_win.title` | Scacco / Scacco matto / Stallo | "matto" alone also used (153 strings: "Percorso di Matto", "Matto mancato", "Problema di matto"); perpetual check "scacco perpetuo (chángjiāng)" |
| Sides | `board.side.red` / `board.side.black` | Rosso / Nero | |
| Palace / river | (text) | palazzo / fiume | "Difesa del palazzo", "Il fiume non riposa mai" |
| Handicap | (text) | handicap | "Casa degli Handicap", "partita a handicap" |

**Italian piece names the app uses** (`piece.*`): Generale (general), Consigliere (advisor), Elefante (elephant), Carro (chariot), Cavallo (horse), Cannone (cannon), Soldato (soldier). Inline lower-case forms: generale, consigliere, elefante, carro, cavallo, cannone, soldato. Opening a cannon's "screen" is "schermo" ("il cannone davanti È lo schermo").

Other flags:
- `paywall.legal.privacy` → "Informativa sulla Privacy" and `paywall.legal.terms` → "Termini di Utilizzo" (Title Case; Tare and the store say "Condizioni d'uso" and the store's privacy line says "Informativa sulla privacy"). Inconsistent with the rest.
- `paywall.benefit.opponents` ("Tutti i 40 avversari, subito sbloccati") is reported unused in the code (same note as Spanish); do not use it as a claim source.
- Title Case on module names ("Campo di Tattica", "Carte Tattiche"), against Italian sentence case.
- Paywall benefits (verbatim): "Analisi delle partite illimitata", "Suggerimenti illimitati dall'allenatore in partita", "Analisi approfondita del motore su più linee", "Tutti gli esercizi di ogni modulo", "Problemi di allenamento illimitati", "Radar delle abilità completo, tendenze e progressi settimanali".
- `settings.tip.supporter` → "Sostenitore"; store tip IAPs "Sostenitore", "Sostegno enorme", "Un caffè".

#### Paid tier names in the Italian UI
"Xiangqiful Premium"; plan labels Mensile / Annuale / A Vita; "Piano gratuito"; "Inizia la prova gratuita"; "Ripristina acquisti"; "Gestisci abbonamento"; "Sblocca per sempre". Store IAP names: "Premium mensile", "Premium annuale", "Premium a vita", and tip items "Sostenitore", "Sostegno enorme", "Un caffè".

#### Italian App Store listing (checked 2026-11-19, https://apps.apple.com/it/app/id6794340136)
- Name: **Xiangqiful: Scacchi Cinesi** (US differs; Title Case "Cinesi")
- Subtitle: **Impara lo xiangqi: tattica, IA**
- In-app purchases (reference): `Premium annuale 9,99 €` · `Premium mensile 1,99 €` · `Sostenitore 5,99 €` · `Sostegno enorme 9,99 €` · `Un caffè 1,99 €` · `Premium a vita 22,99 €`
- Languages line: **Italiano e altre 33 lingue**. Category: **Giochi da tavolo**. Game Center and Family Sharing ("In famiglia") listed
- Description vocabulary: "xiangqi", "80 lezioni gratuite in otto percorsi", "simboli occidentali o … un set ibrido", "caratteri", "motore", "Pikafish", "sette gradi, da «Ottima» a «Svista»", "Precisione", "Momenti chiave", "902 problemi di matto", "nove moduli di allenamento", "Laboratorio delle Aperture", "Casa degli Handicap", "Il piano di oggi", "ripetizione spaziata", "Punteggio stimato", "Profilo di abilità", "Linee approfondite", "Classifiche di Game Center e 62 obiettivi", "scacco matto", "scacco all'infinito", "Mensile" / "Annuale" / "A Vita", "In famiglia". Register tu.

---

### 6. Clippet (`clippet`, source `clipboard/`, ID 6829498729, NOT released)

Built from `_apps/clippet.md`, the catalogs, and the prepared listing in `~/Downloads/clipboard/marketing/aso/` (listing.json, purchases.json).

#### Italian coverage
| Catalog | keys | `it` translated | % |
|---|---|---|---|
| clipboard/clipboard/Localizable.xcstrings (main app, paywall) | 638 | 638 | 100 % |
| clipboard/clipboard/AppShortcuts.xcstrings | 2 | 2 | 100 % |
| clipboard/clipboard/InfoPlist.xcstrings | 7 | 7 | 100 % (contacts, Face ID, photo library add, Reminders; two file-type names) |
| ClipboardKit Localizable.xcstrings | 26 | 26 | 100 % |
| ClipboardKeyboard Localizable + InfoPlist | 104 + 1 | 104 + 1 | 100 % |
| ClipboardAction Localizable + InfoPlist | 1 + 1 | 1 + 1 | 100 % |
| ClipboardWidgets Localizable + InfoPlist | 63 + 1 | 63 + 1 | 100 % |
| ClipboardShare Localizable + InfoPlist | 28 + 1 | 28 + 1 | 100 % |
| ClipboardMacBridge Localizable.xcstrings | 19 | 19 | 100 % |

English left in: `Clippet Pro` (brand), `%@ · %lld pages` (format). The catalogs include Italian plural forms with `many` ("%lld di elementi meno recenti sono nascosti"), which is correct. **Verdict: app is in Italian: yes, fully.**

Siri phrases (verbatim): "Incolla ultima copia in ${applicationName}", "Salva la mia ultima copia in ${applicationName}". Permission prompts (verbatim): contacts "Salva come nuovo contatto un numero di telefono o un biglietto da visita di un elemento quando scegli Aggiungi ai contatti."; Face ID "Permette a Blocco app di sbloccare Clippet per te, così solo tu puoi vedere i tuoi elementi."; photo library "Salva la foto o il video di un elemento nella tua libreria quando scegli Salva in Foto."; Reminders "Aggiunge un promemoria all’app Promemoria quando esegui un’azione Promemoria che hai impostato per un elemento."

#### Register
tu. 80 strings with tu pronouns, 136 opening with a tu imperative (Aggiungi, Incolla, Salva, Copia, Scegli, Tocca, Conferma la tua identità), 0 Lei. Consistent.

#### Glossary
| English term on site | English UI string (key) | Italian UI string (verbatim) | Note |
|---|---|---|---|
| Clipboard | `Clipboard Access` | Accesso agli appunti | **appunti** ("Copiato negli appunti."); store name "Clippet: Gestore Appunti" |
| Clip | `Clip` / `Search Clips` | Elemento / Cerca elementi | "elemento" (145 strings), plural "elementi"; "clip" never used |
| Library | (text) | libreria | "Aggiunge gli elementi di un file di backup o sostituisce la tua libreria con essi."; the photo library is also "libreria di foto" / "Foto" |
| Smart Actions | `Smart Actions` | Azioni intelligenti | listing: "Le Azioni intelligenti individuano…" |
| Custom actions | `Custom Actions` | Azioni personalizzate | `Add actions of your own…` → "Aggiungi azioni tue agli elementi con Clippet Pro." |
| Boards | `Boards` / `New Board` / `Add to Board` | Bacheche / Nuova bacheca / Aggiungi a bacheca | 26 strings, consistent; "Aggiungi a una bacheca" in the Share extension; listing "bacheche colorate" |
| Tags | `Tags` | Tag | English loanword, consistent (`Add Tag` → "Aggiungi tag") |
| Pin | `Pin` / `Pinned` | Fissa in alto / Fissati in alto | widget `Pinned Clips` → "Elementi fissati"; Mac menu "Fissato in alto" |
| Quick Paste | `Quick Paste` | Incolla rapido | |
| Quick Add (widget) | `Quick Add` | Aggiunta rapida | `Add Clip` → "Aggiungi elemento"; listing: «Imposta il widget piccolo su Aggiunta rapida» |
| Paste | `Paste` | Incolla | |
| App Lock | `App Lock` | Blocco app | `Face ID Lock` → "Blocco con Face ID" |
| iCloud Sync | `iCloud Sync` | Sincronizzazione iCloud | |
| Backup | `Backup` | Backup | file type "Backup di Clippet" |
| Auto-delete | `Auto-Delete` | Eliminazione automatica | `Auto-delete in %@?` → "Elimina tra %@?"; `Auto-Delete Sensitive Clips` → "Elimina automaticamente elementi sensibili" |
| Menu bar | `Menu Bar` | Barra dei menu | |
| Open at login | `Open at Login` | Apri al login | "Clippet si apre quando accedi al Mac e salva le tue copie dalla barra dei menu." |
| Save to Clippet | `Save to Clippet` | Salva in Clippet | |
| Clippet keyboard | `Clippet Keyboard` | Tastiera Clippet | |
| Quick Look | `Quick Look` | Visualizzazione rapida | listing: "i PDF si aprono in Visualizzazione rapida" |
| Copy as plain text | `Copy as Plain Text` | Copia come testo semplice | |
| Search | `Search` | Cerca | |
| Settings | `Settings` | Impostazioni | |
| Content types | `Link`, `Images`, `Videos`, `PDFs`, `Audio`, `Files`, `Code`, `Text` | Link, Immagini, Video, PDF, Audio, File, Codice, Testo | |
| Sensitive | `sensitive content` | contenuto sensibile | |
| Older clips hidden | `%lld older clips are hidden` | plurals ("%lld elemento meno recente è nascosto", "%lld di elementi meno recenti sono nascosti", …) | `See Older Clips` → "Vedi elementi meno recenti"; `Not Now` → "Non ora" |
| Widgets | `Latest Clip`, `Pinned Clips`, `Add Clip`, `Recently copied` | Ultimo elemento, Elementi fissati, Aggiungi elemento, Copiati di recente | |
| Free trial | `Start Free Trial` / `%lld days free` | Inizia la prova gratuita / plurals ("%lld giorno gratis", …) | |
| Lifetime | `Lifetime` / `Buy Lifetime` | A vita / Acquista a vita | consistent "a vita" ("Il piano a vita include Clippet Pro, quindi puoi annullare il tuo abbonamento."; `Switch to Lifetime` → "Passa al piano a vita"); no English "Lifetime" left (unlike Spanish) |
| App switcher | `…app switcher…` | elenco applicazioni | "Blocco app copre l’elenco applicazioni finché è attivo." FLAG: check against Apple's iOS term (see Flags) |

#### Paid tier names in the Italian UI
**"Clippet Pro"**; "Ottieni Clippet Pro"; plan labels Mensile / Annuale / A vita; "Inizia la prova gratuita"; "Ripristina acquisti"; "Gestisci abbonamento"; "Abbonati al piano mensile", "Abbonati al piano annuale"; "Passa al piano a vita". Planned store IAP names (`purchases.json`): "Clippet Pro mensile" ("Tutte le funzioni Pro, addebito mensile."), "Clippet Pro annuale" ("Tutte le funzioni Pro, addebito annuale."), "Clippet Pro a vita" ("Tutte le funzioni Pro con un solo pagamento.").

#### Italian App Store listing
Not live: https://apps.apple.com/it/app/id6829498729 returned HTTP 404 and the lookup returned no result on 2026-11-19. Prepared listing (`listing.json`, locale `it`, updated 2026-11-02; unpublished, reference only):
- Name: **Clippet: Gestore Appunti**
- Subtitle: **Copia e incolla con cronologia**
- Promotional text: "Tutto quello che copi, conservato. Testi, link, immagini, PDF e codice si ritrovano con una ricerca in Clippet, una cronologia degli appunti per iPhone, iPad e Mac."
- Vocabulary of the description: appunti; elemento; cronologia; anteprima; bacheche colorate; tag; "Fissa in alto"; Azioni intelligenti; "Visualizzazione rapida"; "libreria di foto"; barra dei menu; "elenco applicazioni"; "Aggiunta rapida"; "in background"; closing line "Termini di utilizzo (EULA)". Register tu.
- Keywords it (iOS): tastiera,storico,gestione,testo,link,note,frammenti,widget,sincronizza,codice,salva,veloce,multipla. Mac: barra,menu,scorciatoia,abbreviazioni,veloce,gestione,storico,testo,link,frammenti,sincronizza,codice. Note: the keyword "storico" while the listing says "cronologia".
- Prices (reference, ITA in `purchases.json`): Monthly 1,99 EUR, Yearly 9,99 EUR, Lifetime 22,99 EUR (full price; not a half-price country). Languages line and category: not available (page not live).

---

### Cross-app terms (Italian, as the apps write them)
- Settings = Impostazioni (all six); Restore purchases = Ripristina acquisti (all six); Manage subscription = Gestisci abbonamento (Soon., Taskful Day, WanderWiki, Xiangqiful, Clippet).
- Free = Gratis (Soon.), Piano gratuito (Taskful Day, Xiangqiful); Free trial = Prova gratuita (all; "1 settimana gratis" in Soon.).
- Monthly / Yearly = Mensile / Annuale; Weekly = Settimanale (WanderWiki). Lifetime = **A vita** in Soon., Taskful Day, WanderWiki, Clippet; **A Vita** (Title Case) in the Xiangqiful paywall; the store IAP rows say "una tantum" (Soon., Taskful Day), "acquisto singolo" (WanderWiki), "a vita" (Xiangqiful, Clippet plan), "una tantum" also in app badge strings. One English "Lifetime" survives in Taskful Day.
- Streak = Serie (Soon. "Serie di giorni", Taskful Day "Serie", WanderWiki "Serie di %lld giorni").
- Hint = Suggerimento (Tare, Xiangqiful); Level = Livello; Chapter = Capitolo; Beam = Asta (Tare).
- Pin = Fissa in alto (Soon., Clippet); Add = Aggiungi (all); Save = Salva.
- On This Day: "Accadde oggi" (WanderWiki, the Italian Wikipedia name) against "In questo giorno" (Soon.).
- Lock Screen = schermata di blocco; Home Screen = schermata Home; menu bar = barra dei menu; Quick Look = Visualizzazione rapida; widget = widget.
- Family Sharing = In famiglia (store and in-app text).
- Task = attività (Taskful Day, with stray "compito"); Reminders = Promemoria; calendar = calendario.
- AI = IA (WanderWiki "Riassunto IA", Xiangqiful store "IA").
- Support the developer: "Supporta lo sviluppatore" (Soon.) against "Sostieni lo sviluppatore" (Taskful Day, WanderWiki store IAP names).
- Register: tu everywhere; imperatives Tocca / Scegli / Aggiungi / Apri / Attiva / Gioca / Incolla; "Tieni premuto" for long press; "Tocca due volte" for double tap.

### Flags (app-side Italian string problems worth filing)
1. **WanderWiki** `Cancel anytime.` / `Start your %lld-day free trial. Cancel anytime.` → "Cancella in qualsiasi momento." (cancellare = delete; should be "Annulla"). Two strings.
2. **Taskful Day: carry forward** is "Rinvia a oggi" / "Rinvia" (= postpone) in the Today banner and button, "Sposta", "Riporta" and "rinviata" elsewhere; pick one verb (Sposta a oggi).
3. **Taskful Day: Inbox** has three terms: "Posta in arrivo" (list title; reads as Mail), "casella", and the English "Inbox" (widget names and 12 strings, "La inbox è vuota").
4. **Taskful Day: task** is "attività" in 268 strings and "compito/compiti" in 23 (including the quick-add placeholder "Aggiungi un compito..." and the intent strings).
5. **Taskful Day: focus** has "Modalità concentrazione" / "Focus" / "Concentrati" / "Sessione focus"; "Fiume dell’energia" against "Fiume di energia"; "Lifetime è un acquisto unico" (English word); one English "insight"; "Piano gratuito" against "versione gratuita"; two TaskfulDayKit Watch strings (`End focus session`, `Extend focus session`) have no Italian.
6. **Xiangqiful** paywall: "A Vita" (Title Case) in 6 strings against "A vita" in settings; "Informativa sulla Privacy" / "Termini di Utilizzo" in Title Case against the store's "Informativa sulla privacy" / "Condizioni d'uso"; `game.settings.pieceSet` and `board.pieceSet.title` both read "Pezzi"; Title Case module names ("Campo di Tattica", "Valutazione delle Abilità"); `paywall.benefit.opponents` is unused (per the German note).
7. **Soon.**: "Cronologia" (timeline section) against 10 uses of "timeline" and "Lista" against "checklist"; "gruppo In famiglia" (capital I); "Consigli" (`Tips`) against "Suggerimento widget" (`Widget Tip`); mixed straight and typographic apostrophes; empty InfoPlist key `Soon` and two widget format keys (cosmetic).
8. **Tare**: `Mobile` → "Scultura"; the unlock text puts the %@ before the plural chapter count ("Altri %1$@ %2$#@chapters@ di livelli…"), check on screen; chapter names in Title Case.
9. **Clippet** (unreleased): the EULA link appended to the Italian description (and to all 40 locales in `listing.json`) reads `https://www.apple.com/legal/internal-services/itunes/dev/stdeula/`, while the live apps use `…/legal/internet-services/itunes/dev/stdeula/`. The `internal-services` path looks like a typo; verify and fix in `listing.json` and App Store Connect before launch. Also: "elenco applicazioni" for the iOS app switcher (Apple's Italian term should be checked against `it-apple-terms.md`), and the listing keyword "storico" against the description's "cronologia".
10. **Store listings**: Title Case and mixed names: "Soon. Giorni ai Grandi Eventi", subtitle "Matrimonio, Viaggio & Bebè"; Tare subtitle "Rompicapo con Pesi Nascosti" (name says "Puzzle"); "Lista Attività & Focus"; "Xiangqiful: Scacchi Cinesi". IAP naming for the same thing differs: Lifetime is "Premium una tantum" (Soon.), "Taskful Day Pro una tantum", "WanderWiki acquisto singolo", "Premium a vita" (Xiangqiful), "Clippet Pro a vita" (planned); the tip IAP is "Supporta lo sviluppatore" (Soon.) against "Sostieni lo sviluppatore" (Taskful Day, WanderWiki). Taskful Day's store text writes "Centro di Controllo" with capitals.
11. **WanderWiki**: `for_you_english_only` ("solo in inglese") looks stale against the site's 17 editions; "Feed" is an English loanword in 6 strings; `Skip (Debug)` is untranslated (probably debug-only); the weekly plan (0,99 EUR) is not on the site.
12. **Register**: no Lei or mixed registers in any of the six apps; the site can use tu.
13. **Coverage**: complete for all six apps; the only gaps are non-user-facing (`Soon` InfoPlist key, `%@ ` / `%@ %@` widget formats) and the two TaskfulDayKit Watch strings.


---

