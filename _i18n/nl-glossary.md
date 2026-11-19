# Dutch glossary per app (nl, Netherlands)

Part of the language sheet `_i18n/nl.md`. Extracted 2026-11-19 by four research agents from each app's string catalogs (read-only, locale `nl`) and its Dutch App Store listing (iTunes lookup API country=nl, apps.apple.com/nl, and the App Store Connect nl-NL localizations). Dutch UI strings are verbatim: use them on the site exactly, except where a row is flagged as defective; then use the clean form and say so.

## Dutch glossary, batch 1: aftershift, allpaid, appmeta, appmeta-pulse, chessful

Method (checked 2026-11-19). Read-only extraction from each app's source folder under `~/Downloads/` (`shiftworkersleep/`, `billreminder/`, `metabuilder/`, `metabuilder_phone/`, `Chessful/`). `.xcstrings` catalogs were parsed as JSON with `python3 -I`; AfterShift's legacy `nl.lproj/*.strings` and `.stringsdict` were converted with `plutil`. "total" = translatable keys (`shouldTranslate: false` and blank keys excluded; stale keys are counted, the stale figure is given in brackets); "nl" = keys with an `nl` value (plural/substitution variations and `stringSet`s count as translated); "same as English" = value identical to the English value (mostly brand names, `%@` format strings, "OK", "Premium", so it overstates real gaps; the real English leftovers are listed in Flags). The Dutch locale key is bare `nl` in every catalog (no `nl-NL`, no `nl-BE`). Chessful's `.claude/worktrees/*` catalog copies were excluded. Dutch values are copied verbatim (apostrophes, dashes, capitalization as in source). App Store data: iTunes lookup API (`country=nl&lang=nl_nl`) plus the product pages `apps.apple.com/nl/app/id<ID>` (generic Safari UA, `Accept-Language: nl-NL`, `curl -sL`; all five pages answered 200 without rate limiting; subtitles and in-app purchase names are read from the page's `serialized-server-data`). The listing pages also print the seller's personal name and address; deliberately not copied.

Register counts are regexes on the Dutch values and are approximate. **je-forms** = the words je / jij / jou / jouw / jezelf / jullie; **u-forms** = the standalone words u / uw / uzelf. The bare token "u" is also the abbreviation of "uur" in AfterShift ("%@u", "6 u"), so its u-count is all false positives. Imperatives ("Voeg toe", "Bekijk", "Kies") carry no pronoun and are not counted, but they are the je-imperative (singular), never "Voeg ... toe" in the formal plural-looking style.

### Register verdict (decides the site's formality)

| App (catalog) | values | je-forms | u-forms | Verdict |
|---|---|---|---|---|
| AfterShift `Localizable.strings` | 1480 | **287** | 13 (all "u" = uur) | **je**, consistent |
| AfterShift widget | 15 | 8 | 0 | je |
| AllPaid (main + two widget catalogs) | 679 | **55** (42 + 8 + 5) | 0 | **je**, consistent |
| AppMeta (macOS) | none | none | none | no Dutch UI |
| AppMeta Pulse (main) | 1412 | **169** | 0 | **je**, consistent |
| AppMeta Pulse widget | 256 | 16 | 0 | je |
| Chessful `Localizable` | 2133 | **358** | 1 ("Ken uzelf", a proverb) | **je** |
| Chessful `Lessons` | 3649 | **1117** | 0 | **je** |

Summary: all four apps that have a Dutch UI write **je / jij** with no mix. The only "u" form anywhere is the proverb "Ken uzelf" in Chessful. The Dutch App Store descriptions of AfterShift, AllPaid, AppMeta Pulse and Chessful are also je ("Je dag begint als je dienst erop zit.", "Vergeet nooit meer een rekening.", "Je App Store-verkopen, MRR en recensies op je iPhone", "Je hebt de partij verloren en weet niet welke zet het deed."). This matches the default register in TRANSLATION.md 13. The text is Netherlands Dutch throughout: 0 hits for Flemish/Belgian markers (gelieve, gsm, aub, wegens), 0 split compounds ("slaap score" etc.), "we" and "ons" used for the studio in AfterShift, AllPaid, Pulse and Chessful ("Stuur ons een e-mail — we lezen alles.").

---

### 1. AfterShift (`aftershift`, source `shiftworkersleep/`, ID 6757163182)

### Dutch coverage
- Main app, legacy `.lproj` (no xcstrings): `en.lproj/Localizable.strings` 1484 keys, `nl.lproj/Localizable.strings` 1484 keys, 0 missing, 0 extra, 33 values identical to English (all legitimate: "Premium", "REM", "OK", "Coach", "Trends", "Timing", "Espresso", "Top 3", "Panama (2-2-3)", format strings; two real leftovers, see Flags). **100 %**. `Localizable.stringsdict` for `nl`: 4 plural keys (`plural.hours` "%d uur"/"%d uur", `plural.days` "%d dag"/"%d dagen", `plural.daysRemaining` "%d dag resterend"/"%d dagen resterend", `plural.naps` "%d dutje"/"%d dutjes").
- `nl.lproj/AppShortcuts.strings`: 16 Siri phrases, all Dutch: "Wanneer is mijn volgende dienst in ${applicationName}", "Wat is mijn volgende dienst in ${applicationName}", "Volgende dienst in ${applicationName}", "Vraag ${applicationName} wanneer mijn volgende dienst is", "Registreer slaap in ${applicationName}", "Leg slaap vast in ${applicationName}", "Registreer mijn slaap in ${applicationName}", "Vertel ${applicationName} dat ik heb geslapen", "Wanneer is mijn volgende slaapvenster in ${applicationName}", "Wat is mijn slaapvenster in ${applicationName}", "Vraag ${applicationName} wanneer ik moet slapen", "Wanneer moet ik slapen volgens ${applicationName}", "Ben ik klaar voor mijn dienst in ${applicationName}", "Vraag ${applicationName} of ik klaar ben voor mijn dienst", "Hoe fit ben ik volgens ${applicationName}", "Check mijn dienstgereedheid in ${applicationName}". Three different words for readiness across the phrases (klaar, fit, dienstgereedheid), see Flags.
- Widget `shiftworkersleepWidget/Localizable.xcstrings`: 15 / 15 → 100 % (0 identical): 7 gallery names + descriptions + "End nap" ("Dutje stoppen").
- InfoPlist: `nl.lproj/InfoPlist.strings` has 2 keys: `CFBundleDisplayName` ("AfterShift") and `NSHealthShareUsageDescription` ("AfterShift leest je slaapgegevens uit Apple Gezondheid om slaapschuld en herstel tussen diensten te berekenen."). **English-only:** `NSCalendarsUsageDescription` and `NSCalendarsFullAccessUsageDescription` are Xcode build settings with no localization ("AfterShift reads your calendar events to automatically detect work shifts. No data is uploaded — everything stays on your device."), so the calendar permission prompt is English on a Dutch device.
- Paywall (`paywall.*`) fully translated.
- **Verdict: app is in Dutch: yes** (one English permission prompt; two or three English technique names).

### Register (AfterShift)
je: 287 of 1480 ("Hiermee verdwijnen %d komende diensten. Diensten die je al gewerkt hebt, blijven in je rooster staan.", "Blijft op je telefoon — helpt zien wat voor jou werkt.", "Deel met je gezin — tot 5 leden", "Hoe ziet je rooster eruit?"). No u/uw. The studio speaks as "we" ("We lezen slaapdata om je herstel tussen diensten te berekenen. We schrijven of delen je gegevens nooit."). Buttons are infinitives ("Dienst toevoegen", "Slaaprapport exporteren", "Aankopen herstellen", "Diensttypes beheren…"); Siri phrases are imperative ("Registreer", "Leg vast", "Vraag"). No mix.

### Glossary
| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Today (screen / tab) | Today (`tab.today`) | Vandaag | other tabs: `tab.sleep` "Slaap", `tab.roster` "Rooster", `tab.coach` "Coach", `tab.settings` "Instellingen" |
| Coach (screen) | Coach (`tab.coach`, `coach.title`) | Coach | unchanged English loan |
| Roster (shift calendar) | Roster (`tab.roster`) | Rooster | widget `widget.gallery.roster.name` also "Rooster"; "Terugkerend dienstrooster" for the rotation; 34 values use "rooster", 2 "dienstrooster", 5 "ploeg…" ("Drieploegendienst"); consistent |
| Settings | Settings (`tab.settings`) | Instellingen | |
| Shift Recovery Score | Shift Recovery Score (`recovery.shiftRecoveryScore`) | Herstelscore na dienst | "na dienst" = "after shift"; the site's "Shift Recovery Score" loses "per shift"; `paywall.premium.recoveryScore` "Herstelscore die rekening houdt met ploegendienst" |
| Sleep Score | Sleep Score (`sleepScore.title`) | Slaapscore | closed compound; `sleepScore.unlock` "Slaapscore ontgrendelen" |
| Readiness | Readiness (`readiness.title`; widget `widget.gallery.readiness.name`) | Paraatheid | **Flag:** `shiftChange.readiness` "Paraatheid", `intent.readiness.title` "Shift Readiness" = "Dienstgereedheid", `readiness.locked` "Readiness locked" = "Herstel vergrendeld" (means "recovery locked"), `intent.readiness.description` "hoe goed je klaar bent", Siri "Hoe fit ben ik". Use "Paraatheid" |
| On-call | On-call (`sleepScore.onCall`, `shift.onCall`) | Oproepbaar | also `schedule.irregular` "Irregular/On-Call" = "Onregelmatig/Oproepbaar"; `shiftType.behavior.onCall` "Oproepbaar — onvoorspelbare uren"; `coach.onCall.title` "Herstelmodus bij oproepdienst"; `sleepScore.onCallNote` "oproepdiensten". Mixed "oproepbaar" (state) and "oproepdienst" (duty). "Oproepbaar" literally "reachable on call"; Dutch shift/health workers say "bereikbaarheidsdienst" or "achterwacht"; the app's term is what users see |
| Naps | Naps (`naps.title`) / Nap (`nap.label`) | Dutjes / Dutje | 84 values, consistent; `nap.title` "Nap Time" = "Dutje"; `today.logNap` "Log Nap" = "Dutje loggen" ("loggen" is an anglicism, Siri uses "Registreer") |
| Nap window | Optional nap window (`notification.napWindow.title`) | Optioneel dutjesvenster | `insight.notification.napWindow.title` "Nap window" = "Dutjesvenster" (closed compound with -s-) |
| Sleep window | Sleep window (`notification.sleepWindow.title`) | Slaapvenster | `intent.sleepWindow.title` same family |
| Sleep Timing | Sleep Timing (`timing.title`) | Slaaptiming | `paywall.free.sleepTiming` "Slaaptiming tussen diensten" |
| Sleep debt (trend) | Sleep debt trend (`debtTrend.title`); widget Sleep Debt | Slaapschuldtrend | widget `widget.gallery.sleepDebt.name` "Slaapschuld"; export `export.sleepDebtSection` "SLAAPSCHULDTREND" |
| Sleep stages Awake / Core / Deep / REM | `stages.awake/core/deep/rem` | Wakker / Licht / Diep / REM | `stages.sleepStages` "Slaapfasen"; "Core" → "Licht" is the app's own choice; the Dutch Apple Gezondheid stage label for Core should be checked before the site relies on "Licht" |
| Time in bed | Time in bed (`timing.timeInBed`) | Tijd in bed | `paywall.free.timeInBed` "Tijd in bed en efficiëntie" |
| Fragmentation / Sleep Continuity | Fragmentation (`continuity.fragmentation`); `continuity.awakenings` | Fragmentatie; Ontwakingen | `paywall.premium.fragmentation` "Fragmentatie- en continuïteitsinzichten"; **Flag:** "Ontwakingen" is stilted Dutch for "Awakenings" (natural: "Keren wakker") |
| Caffeine timing | Caffeine timing (`coach.caffeine.title`) | Timing van cafeïne | **Flag, four forms:** `caffeine.header` "Cafeïnetiming", `technique.caffeineTiming.title` "Cafeïne-timing" (hyphen), `coach.caffeine.title` "Timing van cafeïne", reminder title "Cafeïnestop" |
| Caffeine cut-off (reminder) | Caffeine cutoff (`notification.caffeineCutoff.title`) | Cafeïnestop | `insight.notification.caffeineCutoff.title` same; body "Gebruik je cafeïne? Dit is een goed moment om te stoppen."; `settings.caffeineSensitivity` "Cafeïnegevoeligheid" |
| Wind-down reminder | Wind down (`notification.windDown.title`) | Ontspannen | **Flag, three forms:** `insight.notification.windDown.title` "Ontspantijd", `playbook.step.windDown.title` "Tot rust komen — bodyscan, gedimd licht.", body "afbouwen van prikkels"; Live Activity text uses "afbouwvenster" |
| Calendar shift import | Import from calendar (`roster.calendarImport`) | Importeren uit agenda | calendar = "agenda" (32 values), "kalender" only twice; `onboarding.calendar.title` "Importeer je rooster" |
| Calendar Sync (Premium) | Calendar Sync (`calendar.sectionTitle`) | Agendasynchronisatie | `paywall.premium.calendarSync` "Automatische agendasynchronisatie en overurenregistratie"; `calendar.upgradeAutoSync` "Upgrade: automatische synchronisatie, meerdere agenda's en overuren" |
| Overtime | Overtime: (`nextShift.overtime`) | Overwerk: | `nextShift.overtime.addOneHour` "1 uur overwerk toevoegen"; paywall says "overuren" / "overurenregistratie"; mix overwerk / overuren (both correct Dutch) |
| Add a shift | Add shift (`roster.addShift`, `today.addShift`) | Dienst toevoegen | "dienst" = shift throughout; never "shift" |
| Shift types | Day / Evening / Night / Off (`shift.day/evening/night/off`) | Dag / Avond / Nacht / Vrij | `settings.shiftTypes` "Diensttypes" (also "diensttype", "Diensttypes beheren…"); `shift.evening` "Avond" |
| Shift change | Shift change impact (`shiftChange.title`) | Impact van dienstwijziging | `premium.overtime.title` "Impact dienstwijziging"; `overtime.changed` "Diensttijd gewijzigd van %@ naar %@."; consistent "wijziging/gewijzigd" |
| Repeating rotation | Repeating rotation (`roster.rotation`) | Terugkerend dienstrooster | `rotation.presets` "Common rotations" = "Veelvoorkomende cycli" (cyclus = rotation cycle). **Flag:** `roster.tapToAdd` "Tik op + om een dienst toe te voegen" drops "or set up a repeating rotation" |
| Three-shift (day, evening, night) | Three-shift rotation (`rotation.preset.threeShift`) | Drieploegendienst | sub: "Dag → avond → nacht, 2 van elk" |
| 4 on / 4 off | `rotation.preset.fourOnFourOff` | 4 op / 4 af | sub "Vier nachten, dan vier dagen vrij" |
| 4 on / 3 off | `rotation.preset.fourOnThreeOff` | 4 op / 3 af | sub "Vier dagen, dan drie vrij" |
| 2 days / 2 nights | `rotation.preset.ddnn` | 2 dag / 2 nacht | singular forms; sub "Twee dagen, twee nachten, vier vrij" |
| Panama (2-2-3) | `rotation.preset.panama` | Panama (2-2-3) | sub "2-2-3 roterend, om het weekend vrij" |
| Fixed nights / Fixed days | `rotation.preset.fixedNights/fixedDays` | Vaste nachtdienst / Vaste dagdienst | subs "Vijf nachten, weekenden vrij" / "Vijf dagen, weekenden vrij" |
| Schedule type (setup) | Rotating Shifts / Fixed Schedule / Irregular (`schedule.*`) | Wisselende diensten / Vast schema / Onregelmatig | "schema" here, "rooster" elsewhere |
| Trends | Trends (`trends.title`) | Trends | `today.section.trends` "Trends & Insights" = "Trends en inzichten" |
| Do this now (playbook) | Do this now (`playbook.cardKicker`) | Doe dit nu | widget `widget.label.doThisNow` same; "playbook" left in English in `paywall.lock.smartPlaybook` ("Slim playbook"), `paywall.lock.customScenarios` ("playbook-scenario's") |
| Techniques | Techniques (`library.title`) | Technieken | `technique.cognitiveShuffle.title` "Cognitive Shuffle" left English |
| Export / PDF report | Export Sleep Report (`settings.exportReport`) | Slaaprapport exporteren | `export.title` "AFTERSHIFT SLAAPRAPPORT"; `export.pdf.filename` "AfterShift-Rapport-%@.pdf"; `settings.exportHint` "Genereer een slaaprapport van 14 dagen"; footer "Deel met je arts." |
| Lock Screen countdown | Shift countdown on Lock Screen (`liveactivity.settings.title`) | Dienstaftelling op toegangsscherm | **Dutch Apple term for Lock Screen is "toegangsscherm"** (4 values); "Live Activity" = "live-activiteit" |
| Widgets: Next Shift, Shift Plan, Rhythm, Sleep Debt, Roster, Readiness, Sleep Graph | `widget.gallery.*.name` | Volgende dienst, Plan voor je dienst, Ritme, Slaapschuld, Rooster, Paraatheid, Slaapgrafiek | descriptions in je: "Live aftellen tot je volgende dienst.", "Je paraatheid in één oogopslag." |
| Apple Health | (Apple Health) | Apple Health | **Flag:** `settings.health.title` "Apple Health" (20 values) vs "Gezondheid-app" / "Gezondheid" (5 + 10 values, "Gezondheid → Overzicht → Slaap") vs the permission prompt "Apple Gezondheid" (InfoPlist). Three forms for one thing |
| Family Sharing | Share with your family — up to 5 members (`paywall.premium.familySharing`) | Deel met je gezin — tot 5 leden | |
| Siri / Shortcuts | AppShortcuts phrases | see coverage | |
| No account / data stays on device | Data stays on your device; No ads | Gegevens blijven op je apparaat; Geen advertenties | `onboarding.privacyNote` "Je gegevens blijven privé en op je apparaat."; `paywall.privacyFirst` "Privacy voorop" |

### Paid tier names in the Dutch UI (AfterShift)
- Tier: **AfterShift Premium** (`paywall.premiumTitle`), chip "Premium" (`pro.chipLabel`), badge "PREMIUM"; settings status `settings.premiumActive` "Premium Actief" (capital A); "Premium-functie", "Premium-functies" (hyphenated). `paywall.continuePremium` "Ga door met Premium", `paywall.tryPremium` "Probeer AfterShift Premium", `paywall.unlockForever` "Ontgrendel Premium voor altijd". The word "Pro" never appears.
- Periods: `paywall.monthly/yearly/lifetime` "Maandelijks" / "Jaarlijks" / "Levenslang"; `paywall.month` "maand", `paywall.year` "jaar", `paywall.perMonthLong` "per maand"; `paywall.payOnce` "Eenmalig betalen"; `paywall.lifetimeDisclosure` "Eenmalige aankoop. Geen abonnement. Alle Premium-functies, voor altijd."; `paywall.lifetimeDetail` "Alle toekomstige updates inbegrepen". **Flag:** `paywall.bestValue` "Best value" = "Beste deal" (colloquial; Pulse uses "Voordeligst", Chessful "BESTE WAARDE").
- Trial: `paywall.startTrial` "Start 7 dagen gratis proefperiode"; `paywall.7dayTrial` "7 dagen gratis proberen"; `paywall.freeFor7Days` "7 dagen gratis"; `settings.trialActive` "Gratis proefperiode actief"; `paywall.noChargeToday` "Vandaag geen kosten. Je wordt niet belast als je opzegt voor het einde van de proefperiode."; `paywall.cancelAnytime` "Op elk moment opzegbaar. Geen medische claims." Trial word: "proefperiode".
- Restore: `paywall.restorePurchases` "Aankopen herstellen". Subscription disclosure: "Abonnementen worden automatisch verlengd tenzij opgezegd in Instellingen."

### Dutch App Store listing (checked 2026-11-19)
- Name (lookup `trackName` and page title): **AfterShift: Slaap & Ploegen**. Subtitle (product page): **Herstel, dutjes & vermoeidheid**.
- Description is in Dutch (je): "Je dag begint als je dienst erop zit. AfterShift volgt je slaap en herstel op basis van je rooster…". Languages 34, includes NL. Category "Health & Fitness" (lookup `primaryGenreName`), price "Gratis" with in-app purchases, minimum iOS 17.6.
- In-app purchases on the page: `Premium maandabonnement € 3,99`, `Premium jaarabonnement € 29,99`, `Premium eenmalige aankoop € 44,99`, `Ontwikkelaar steunen € 1,00`. Store IAP names use "Premium" like the app, "maandabonnement", "jaarabonnement", "eenmalige aankoop" (not "Levenslang"). Prices are reference only.

---

### 2. AllPaid (`allpaid`, source `billreminder/`, ID 6757253009)

### Dutch coverage
- Main `billreminder/Localizable.xcstrings`: 494 total (464 non-stale), 494 nl → **100 %**; 31 values identical to English: brand/format ("AllPaid", "AllPaid Pro", "Pro", "OK", "DataVault", "Streaming", "Entertainment", "Internet", "Water", "Type") plus real leftovers "Contract start", "Start Pro", "1 week", "%@ / week", "%@/week" (see Flags).
- `InfoPlist.xcstrings`: 3 / 3 → 100 %; `NSFaceIDUsageDescription` "Face ID of Touch ID vereisen om de app te openen." (the Mac variant "Touch ID of je Mac-wachtwoord vereisen om de app te openen." lives in the main catalog); display names are the brand (2 identical).
- Widget `billreminderWidget/Localizable.xcstrings`: 58 keys, 57 nl (only `%lld` untranslated, format only), 5 identical ("Horizon", "Treemap", "Streaming", "Entertainment", "+%lld"). `billreminderWidgetShared/Widget.xcstrings`: 130 / 130 → 100 %, 10 identical ("Later", "Open AllPaid", format strings).
- **Not localized:** Siri App Shortcut phrases (`Services/AppIntents/BillsDueIntent.swift`: "What bills are due in \(.applicationName)" and two more). No `AppShortcuts.xcstrings` / `.strings` exists, so the spoken phrases are English-only on a Dutch device. The intent title "Bills Due This Week" = "Rekeningen deze week" is translated. The Dutch page must not promise Dutch Siri phrases.
- **Verdict: app is in Dutch: yes** (all UI, notifications, widgets and the Face ID prompt; only Siri phrases are English).

### Register (AllPaid)
je: 42 of 492 in the main catalog + 8 of 57 + 5 of 130 in the widgets ("Voeg je eerste rekening toe", "AllPaid houdt je rekeningen bij", "Rekeningen horen niet in je hoofd.", "Rekeningen die je toevoegt, verschijnen hier."). No u/uw. The studio speaks as "we" ("We waarschuwen je altijd 7 dagen voor automatische verlenging."). Buttons mix infinitive and imperative: "Rekening toevoegen", "Als betaald markeren", "Aankopen herstellen" (infinitive) vs "Annuleer", "Verwijder", "Ontgrendel AllPaid", "Markeer als verlengd" (imperative). See Flags.

### Glossary
| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Bills | Bills | Rekeningen | "rekening" for bill (never "factuur"); ambiguous with bank account, but the Dutch word for a bill to pay; `Recurring bills` "Terugkerende rekeningen"; `Bills Due This Week` "Rekeningen deze week" |
| Add a bill | Add Bill | Rekening toevoegen | `Edit Bill` "Rekening bewerken", `Delete Bill` "Rekening verwijderen" |
| Mark paid | Mark as paid / Mark paid | Als betaald markeren | both keys same value; `Mark as renewed` "Markeer als verlengd" (imperative, inconsistent) |
| Paid | Paid | Betaald | `Paid · %@` "Betaald · %@"; `No paid bills yet` "Nog geen betaalde rekeningen" |
| Undo | Undo | Ongedaan maken | distinct from Cancel "Annuleer" |
| Snooze (notification) | Remind in 2 hours / Remind tomorrow / Remind in 1 week | Herinner over 2 uur / Herinner morgen / Herinner over 1 week | imperative; no single "Snooze" string |
| Monthly calendar (widget/screen) | Monthly Calendar | Maandkalender | "kalender" here, "agenda" is not used in AllPaid |
| Total due | Total due | Totaal verschuldigd | |
| Due date / due today | Due date / Due today / Due in %lld days | Vervaldatum / Vervalt vandaag / Vervalt over %lld dagen | consistent "vervallen" |
| Upcoming | Upcoming / Coming Up / Coming up | Binnenkort | `Next Bill` "Volgende rekening", `No upcoming bills` "Geen komende rekeningen" |
| Reminders | Reminders | Herinneringen | `Due-day reminders` "Herinneringen op de vervaldatum"; `Remind me 1 day before` "Herinner me 1 dag van tevoren" |
| Multiple reminders per bill (Pro) | Multiple reminders per bill | Meerdere herinneringen per rekening | "Meerdere herinneringen per contract is een Pro-functie." (grammar: "is" after plural subject) |
| Spending overview / Spending Analytics (Pro) | Spending overview / Spending Analytics | Uitgavenoverzicht / Uitgavenanalyse | `Unlock spending analytics with Pro.` "Ontgrendel uitgavenanalyse met Pro." |
| Category breakdown | By category | Per categorie | `Categories` "Categorieën" |
| Monthly trends | Monthly trend | Maandelijkse trend | `Monthly summary` "Maandoverzicht" |
| Full payment history | Full payment history / Payment History | Volledige betalingsgeschiedenis / Betalingsgeschiedenis | |
| Unlimited bills | Unlimited bills | Onbeperkte rekeningen | |
| iCloud Sync | iCloud Sync | iCloud-synchronisatie | hyphen after iCloud; "iCloud-account", "iCloud-accountstatus" |
| Search / Sort / Notes / Share | Search bills / Sort by / Notes / Share bill | Rekeningen zoeken / Sorteren op / Notities / Rekening delen | `Share app with friends` "Deel de app met vrienden" |
| Billing cycles | Weekly / Bi-weekly / Monthly / Quarterly / Semi-annual / Yearly / One-time / Custom | Wekelijks / Tweewekelijks / Maandelijks / Driemaandelijks / Halfjaarlijks / Jaarlijks / Eenmalig / Aangepast | |
| Categories (examples) | Streaming / Subscriptions / Utilities / Housing / Insurance / Rent / Loans / Taxes / Savings / Groceries / Education / Childcare / Pets / Charity / Other | Streaming / Abonnementen / Nutsvoorzieningen / Wonen / Verzekering / Huur / Leningen / Belastingen / Sparen / Boodschappen / Onderwijs / Kinderopvang / Huisdieren / Goede doelen / Overig | also "Internet & telefoon", "Creditcard", "Vervoer", "Gezondheid & fitness", "Elektriciteit", "Entertainment" (English kept) |
| Contracts | Contract / Contracts / Contract ends | Contract / Contracten / Contract eindigt | `Contract ending soon` "Contract eindigt binnenkort", `Contracts ending soon` "Contracten die bijna eindigen", `Contract start` "Contract start" (English homograph, reads as a verb), `Renewal amount` "Verlengingsbedrag", `Past Renewals` "Eerdere verlengingen", `Auto-renews` "Verlengt automatisch" |
| Auto-pay | Auto-pay | Automatisch betalen | `Auto-pay today` "Automatische betaling vandaag" |
| Documents attached to the bill | Manage attachments / DataVault | Bijlagen beheren / DataVault | `DataVault` kept as product name; `No attachments yet` "Nog geen bijlagen" |
| App lock (Face ID) | App Lock | App-vergrendeling | `App Locked` "App vergrendeld"; the Face ID prompt is Dutch |
| Family Sharing | Share with up to 5 family members / via Family Sharing | Deel met maximaal 5 gezinsleden / via Delen met gezin | "Delen met gezin" is the Apple Dutch name; `Managed by your family organizer.` "Beheerd door de organisator van je gezin." |
| Widgets (ten) | Next Bill, Horizon, Paid Rhythm, Coming Up, Week Ahead, Month Progress, Recurring Bills, Monthly Calendar, Contracts | Volgende rekening, Horizon, Betaalritme, Binnenkort, Komende week, Maandvoortgang, Terugkerende rekeningen, Maandkalender, Contracten | "Horizon" left English |
| Free tier | Free plan | Gratis abonnement | **Flag:** "abonnement" = subscription; "Het gratis abonnement staat maximaal 3 rekeningen toe." the free tier is not a subscription (Chessful uses "Gratis plan") |
| Pro | Pro / AllPaid Pro / Upgrade to Pro | Pro / AllPaid Pro / Upgraden naar Pro | `Unlock AllPaid Pro` "Ontgrendel AllPaid Pro"; `Start Pro` "Start Pro" (identical); "Pro-functie"; `Upgrade to Pro` "Upgraden naar Pro" vs `Upgrade to Pro to see…` "Upgrade naar Pro om…" |
| Lifetime | Lifetime / Buy Lifetime Access | Levenslang / Levenslange toegang kopen | `One-time purchase` "Eenmalige aankoop" |
| Privacy / no bank login | Privacy Policy | Privacybeleid | `Face ID or Touch ID` prompt; no "no bank login" string in the catalog |

### Paid tier names in the Dutch UI (AllPaid)
- Tier: **Pro** ("AllPaid Pro", "Pro-functie", "Mis je Pro?" style not present). Titles: `Unlock AllPaid` "Ontgrendel AllPaid", `Unlock AllPaid Pro` "Ontgrendel AllPaid Pro", `Start Pro` "Start Pro", `Try Pro free for 7 days` "Probeer Pro 7 dagen gratis", `Try Pro free for %@` "Probeer Pro %@ gratis".
- Periods: "Maandelijks" / "Jaarlijks" / "Levenslang"; `Per month` "Per maand", `Per year` "Per jaar", `%@/mo` "%@/mnd", `Save %lld%%` "Bespaar %lld%%", `Usually %@/mo` "Normaal %@/mnd". Lifetime text: "De betaling wordt in rekening gebracht op je Apple ID als eenmalige aankoop. Geen abonnement, geen terugkerende kosten." (here "Apple ID", Pulse writes "Apple Account-ID").
- Trial: `Start free trial` "Start gratis proefperiode"; `Cancel anytime. No charge until the trial ends.` "Op elk moment opzegbaar. Geen kosten tot het einde van de proefperiode."; "proefperiode" 2 values.
- Restore: `Restore Purchases` "Aankopen herstellen"; `No purchases to restore.` "Geen aankopen om te herstellen."
- Store IAP names (page): `AllPaid Pro maandelijks € 1,99`, `AllPaid Pro jaarlijks € 14,99`, `AllPaid Pro eenmalig € 29,99`.

### Dutch App Store listing (checked 2026-11-19)
- Name: **AllPaid – Rekeningen bijhouden** (en dash as on the page). Subtitle: **Op tijd betalen, zonder stress**.
- Description in Dutch (je): "Vergeet nooit meer een rekening. Een rekening betalen is het makkelijke deel…". Languages 34 incl. NL; category Utilities; "Gratis"; iOS 17.0, devices include Mac.

---

### 3. AppMeta (`appmeta`, macOS, source `metabuilder/`, ID 6758547802)

### Dutch coverage
- `metabuilder/Localizable.xcstrings`: 2300 translatable keys (35 stale); localizations present: ar, de, en-AU, en-CA, en-GB, es, es-MX, fr, fr-CA, it, ja, ko, pt-BR, pt-PT, ru, tr (2282 each) and `en` (103). **No `nl` value in any key; `nl` is not in the project's `knownRegions`** (en, Base, ar, de, es, fr, it, ja, ko, pt-BR, ru, tr, …). No other catalog or `nl.lproj` exists.
- **Verdict: app is in Dutch: no.** The Mac interface is English on a Dutch Mac. The English page says "17 localizations covering 11 languages" and does not list Dutch, so no Dutch page may claim a Dutch interface. The listing editor still manages Dutch App Store metadata (ASC locale `nl-NL`), which is a feature, not an interface language.

### Register (AppMeta)
None (no Dutch UI strings). Dutch page copy follows the site default (je).

### Glossary
No Dutch UI strings exist, so there is nothing verbatim to quote. The Dutch site page must pick its own terms; AppMeta's sibling AppMeta Pulse is the only same-vendor Dutch UI, and its terms for shared concepts are: App Store Connect (unchanged), API-sleutel (API key), `.p8`-sleutelbestand, Vendor Number (unchanged), recensies (reviews), abonnementen (subscriptions), TestFlight (not in Pulse), Analytics (unchanged), Instellingen (Settings), Land of regio (Territory). Where the English page names an AppMeta feature, the Dutch term is a site choice:

| English term on site | English UI string (key) | Dutch UI string | Note |
|---|---|---|---|
| Every locale in one window / Locales | Locales | – | no Dutch UI; Pulse says "Land of regio" for Territory, not locale |
| Field-level diff before push | Preview / Apply Change / Apply to All %lld Locales | – | no Dutch UI |
| Keyword research (difficulty, demand) | Apple Ads popularity %lld/100, AI Suggest Keywords | – | no Dutch UI |
| AI Translation | AI Translate / AI Translation | – | no Dutch UI |
| In-App Purchases, subscriptions, Game Center | In-App Purchases / Subscriptions | – | Pulse: "In-app aankopen", "Abonnementen" |
| TestFlight, reviews, submission | App Store Review / App Review Information | – | Pulse: "Recensies" |
| Sales & Analytics, Diagnostics | Analytics | – | Pulse: "Verkoop", "Analytics" |
| Tiers | AppMeta Yearly / AppMeta Lifetime / Unlock AppMeta Pro / Unlock Lifetime — %@ | – | English tier names "Yearly", "Lifetime", "Pro" |

### Paid tier names in the Dutch UI (AppMeta)
None. English UI: "Unlock AppMeta Pro", "Yearly", "Lifetime", "Restore Purchases", "Yearly = 5× Monthly". The Dutch store IAP names are the English ones: `AppMeta Yearly € 19,99`, `AppMeta Lifetime € 34,99` (page, NL storefront).

### Dutch App Store listing (checked 2026-11-19)
- Name: **AppMeta for App Store Connect** (English, untranslated). Subtitle on the Dutch product page: **Diensten** (a Dutch word, "Services", read from the page lockup; the English subtitle could not be compared because apps.apple.com/us answered 429; treat as unverified and ask the owner). Description is **English** ("One wrong paste can ship a broken keyword field in a language you can't read…"). Languages 11, no NL. Category Utilities; "Gratis"; iOS... macOS 14.0.

---

### 4. AppMeta Pulse (`appmeta-pulse`, source `metabuilder_phone/`, ID 6758788164)

### Dutch coverage
- Main `metabuilder_phone/Localizable.xcstrings`: 1418 total (3 stale), 1418 nl → **100 %**; 70 identical to English (units and abbreviations "MRR", "MTD", "QTD", "OK", "Analytics", "Dashboard", "Downloads", "Filters", "Issuer ID", "Key ID", "Cache", "Details", "App Store Connect", plus plural templates `%#@arg2@`).
- Widget `AppMetaPulseWidget/Localizable.xcstrings`: 256 / 256 → 100 %; 24 identical ("MRR", "MTD", "WTD", "QTD", "YTD", "Week", "WEEK", "Basis", format strings).
- `AppShortcuts.xcstrings`: 3 keys, each a `stringSet` of phrases, all with `nl`: "Open ${applicationName}" / "Toon de omzet van vandaag in ${applicationName}" / "Verkoop van vandaag in ${applicationName}"; "Toon analytics in ${applicationName}" / "App Store-conversie in ${applicationName}"; "Toon abonnees in ${applicationName}" / "Actieve abonnementen in ${applicationName}". The first phrase "Open ${applicationName}" is identical to English (correct: Dutch uses the same).
- No InfoPlist catalog (no usage-description keys in the project).
- **Verdict: app is in Dutch: yes**, including widgets and Siri phrases.

### Register (AppMeta Pulse)
je: 169 of 1412 in the main catalog, 16 of 256 in the widget ("Als je nu verwijdert of opnieuw synchroniseert…", "In jouw taal", "Ontgrendel AppMeta Pulse voor je 7-daagse prestaties."). No u/uw. Buttons and commands are the je-imperative ("Voeg account toe", "Bewaar", "Kies bestand…", "Open Instellingen", "Wis filters"); help text uses "we"/"ons" ("Stuur ons een e-mail — we lezen alles."). No mix.

### Glossary
| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Proceeds | Proceeds | Opbrengst | `Latest Proceeds` "Laatste opbrengst", `Monthly Proceeds` "Maandelijkse opbrengst", "Opbrengst %lld dagen"; Apple payout after commission = "Uitbetaling van Apple na commissie" |
| Sales | Sales | Verkoop | singular as a noun ("Verkoop vandaag", "Verkooprapporten", "Verkoop synchroniseert niet"); `Sales, downloads and refunds` "Verkopen, downloads en terugbetalingen" (plural once) |
| Revenue | Revenue | Omzet | `Revenue & proceeds` "Omzet en opbrengst"; `Monthly recurring revenue` "Maandelijks terugkerende omzet" |
| MRR | MRR | MRR | `MRR Target` "MRR-doel"; widget `Pace` etc. |
| Subscribers | Active subscribers | Actieve abonnees | **Flag:** "abonnees" (people) vs "abo's" (the count/product) vs "abonnementen"; `Active Subs` "Actieve abo's", `Active Subscriptions` "Actieve abonnementen", `Subs` "Abo's", `New Subs` "Nieuwe abo's", `Churn` kept |
| Trials | Trials / Active Trials / Free trial | Proefabo's / Actieve proefabo's / Gratis proefperiode | **Flag:** "proefabo's" (compressed, unnatural) vs "proefperiodes" ("Actieve abonnementen en proefperiodes", 4 widget values); `Trial → Paid` "Proef → abo"; `Trial Starts` "Proefstarts" |
| Churn | Churn / Monthly Churn | Churn / Churn per maand | `Monthly churn rate` "Churnpercentage per maand"; "Churn /mnd"; English loan kept; `Cancels` "Opzeggingen" |
| Reviews | Reviews / All Reviews | Recensies / Alle recensies | `Reply` "Reactie", `Reply to %lld reviews` "Reageer op %lld recensies", `Replied` "Beantwoord", `Response Templates` "Reactiesjablonen", `%lld responses` "%lld antwoorden". **Flag:** reactie / antwoord / beantwoord for the same thing |
| Reply drafts (AI, on device) | AI draft per review / Drafts are generated on-device. | AI-concept per recensie / Concepten worden op het apparaat gegenereerd. | "concept" = draft; `AI reply drafts, written on your device by Apple Intelligence.` "AI-reactieconcepten, op je apparaat geschreven door Apple Intelligence." |
| Translate reviews | Translate to %@ / Auto-translate Foreign Reviews | Vertaal naar %@ / Vertaal buitenlandse recensies automatisch | |
| Dashboard | Dashboard | Dashboard | unchanged (Chessful uses "Overzicht") |
| Subscriptions (screen) | Subscriptions | Abonnementen | `Subscription Status` "Abonnementsstatus", `Subscription reports` "Abonnementsrapporten" |
| Trends / year over year | Trends / Compare with last year / Year-over-year comparison in Trends. | Trends / Vergelijk met vorig jaar / Vergelijking met vorig jaar in Trends. | `vs Last Year` "t.o.v. vorig jaar" |
| App Store funnel | App Store funnel | App Store-funnel | `Funnel` "Funnel", `Impressions` "Vertoningen", `Product Page Views` "Paginaweergaven", `Conversion Rate` "Conversieratio", `Trial → Paid` |
| Every app side by side | App Breakdown / All Apps | Overzicht per app / Alle apps | `Per-app performance` "Prestaties per app" |
| Territory / countries | Territory / Territories / Country | Land/regio / Landen en regio's / Land of regio | Apple's wording "Land of regio" is used (and `Land-/regiocode`); consistent |
| Currency conversion | Convert to your preferred currency / Currency | Reken om naar je voorkeursvaluta / Valuta | `Multi-currency display via ECB monthly rates.` "Weergave in meerdere valuta's met maandelijkse ECB-koersen." |
| API key | API Credentials / Private Key / Issuer ID / Key ID / Vendor Number | API-inloggegevens / Privésleutel / Issuer ID / Key ID / Vendor Number | "API-sleutel" (70 "sleutel" values); `Drop your .p8 key file here` "Zet je .p8-sleutelbestand hier neer"; `Requires an Admin API key.` "Vereist een API-sleutel met de rol Beheerder."; Admin role = "Beheerder"; IDs left English |
| Sales history kept on device | Years of history / Data Retention / Report Archive | Jaren aan geschiedenis / Bewaartermijn / Rapportenarchief | `Extended Archive` "Uitgebreid rapportenarchief"; "Je geschiedenis bewaard" |
| Widgets | Home Screen widgets / widget names | widget(s) | "widget" 25 values; Lock Screen = "toegangsscherm", Home Screen = "beginscherm" (`Widgets voor het beginscherm`, `Widgets voor het beginscherm en het toegangsscherm.`); widget names: `7-Day Dashboard` "Dashboard 7 dagen", `30-Day Trends` "Trends 30 dagen", `App Breakdown` "Overzicht per app", `Ledger` "Grootboek", `Pace` "Tempo", `Shape` "Vorm", `Where It Moved` "Verschuivingen", `Active Subscriptions` "Actieve abonnementen" |
| Optional iCloud Sync | iCloud Sync / Turn on iCloud Sync | iCloud-synchronisatie / Zet iCloud-synchronisatie aan | `Optional iCloud sync to your own iCloud` "Optionele iCloud-synchronisatie met je eigen iCloud"; `Back up and sync with iCloud` "Maak een back-up en synchroniseer met iCloud"; "synchronisatie" 71 values, never "sync" |
| Mac / AI assistants (MCP) | AI Assistants / Connect an AI App / An MCP server for Claude, Cursor and other AI apps | AI-assistenten / Verbind een AI-app / Een MCP-server voor Claude, Cursor en andere AI-apps | `Ask your AI assistant` "Vraag het je AI-assistent"; `Let AI assistants read your reports` "AI-assistenten je rapporten laten lezen" |
| Demo / sample data | Try with sample data / Demo Mode | Probeer met voorbeeldgegevens / Demomodus | `Demo preview ended. Subscribe to continue with your data.` "Het demovoorbeeld is afgelopen. Abonneer je om verder te gaan met je gegevens." |
| Settings / Help | Settings / Help & FAQ / Support website | Instellingen / Help en FAQ / Supportwebsite | `AppMeta Pulse Help` "AppMeta Pulse-help" |
| Export | Export / Export as CSV… | Exporteer / Exporteer als CSV… | imperative; `Export as PDF…` "Exporteer als pdf…" (lowercase pdf) |
| Privacy | Privacy / No ads, no tracking | Privacy / Geen advertenties, geen tracking | `Read the full Privacy Policy` "Lees het volledige privacybeleid"; `No third-party analytics` "Geen analytics van derden"; `Where data lives` "Waar je gegevens staan" |
| Apple ID | Apple ID | Apple Account-ID | follows Apple's 2025 rename; AllPaid and Chessful still say "Apple ID" |

### Paid tier names in the Dutch UI (AppMeta Pulse)
- No "Pro"/"Premium" tier name. The product is the app itself: `Unlock AppMeta Pulse` "Ontgrendel AppMeta Pulse", `Unlock Lifetime Access` "Ontgrendel levenslange toegang", `Subscribe` "Abonneer", `Manage Subscription` "Beheer abonnement", widget lock text "AppMeta Pulse vergrendeld. Abonneer voor toegang."
- Periods: `Monthly` "Maandelijks", `Yearly` "Jaarlijks", `Lifetime` "Levenslang", `Weekly` "Wekelijks", `Quarterly` "Driemaandelijks"; `Billed monthly` "Maandelijks gefactureerd"; `Best Value` "Voordeligst"; `One-time purchase · Use forever` "Eenmalige aankoop · Voor altijd te gebruiken"; `Save %@` "Bespaar %@"; "Alle toekomstige updates inbegrepen".
- Trial: `Start Free Trial` "Start gratis proefperiode"; `No charge during your free trial` "Geen kosten tijdens je gratis proefperiode"; `Free for %1$@, then %2$@.` "Gratis gedurende %1$@, daarna %2$@."; year variant "Gratis proefperiode van %1$lld jaar, daarna %2$@ per jaar."
- Restore: `Restore Purchases` "Aankopen herstellen", `Restore Purchase` "Aankoop herstellen", `Subscription restored successfully.` "Abonnement hersteld."
- Store IAP names (page): `AppMeta Pulse Maandabonnement € 0,99`, `AppMeta Pulse Jaarabonnement € 6,99`, `AppMeta Pulse Levenslang € 14,99` (capital letters on the second word of "Jaarabonnement"/"Maandabonnement" are a Title-Case artefact; not copyable).

### Dutch App Store listing (checked 2026-11-19)
- Name: **AppMeta Pulse: App-omzet**. Subtitle: **Recensies beantwoorden met AI**.
- Description in Dutch (je): "Je App Store-verkopen, MRR en recensies op je iPhone, en nu ook op je Mac. AppMeta Pulse leest je App Store Connect-rapporten en bewaart je verkoopgeschiedenis voorgoed." Section headings in caps ("JE GESCHIEDENIS, VOORGOED BEWAARD"). Languages 15 incl. NL; category Business; "Gratis"; iOS 17.0; devices include Mac.

---

### 5. Chessful (`chessful`, source `Chessful/`, ID 6761336870)

### Dutch coverage
- `Chessful/Localizable.xcstrings`: 2146 total (33 stale), 2146 nl → **100 %**; 86 identical to English (names "Chessful", "Claude", "Game Center", "Blunder", "Expert", "En passant", the opponent first names "Luna", "Milo"…, board/piece-set names "Marble", "Marathon", "Frequent", format strings).
- `Chessful/Lessons.xcstrings` (the 156 lessons, exercises, puzzle text): 3649 / 3649 → 100 %; 15 identical (chess notation like "…♜a5+", "Zugzwang", "En passant").
- `InfoPlist.xcstrings`: 2 / 2 (both the brand "Chessful", identical). No permission prompts, no Siri/App Shortcuts, no widget.
- **Verdict: app is in Dutch: yes.** Large catalog translated in full, chess vocabulary is correct Dutch (paard, loper, toren, dame, rokade, pat, schaakmat, penning, vork, achterste rij).

### Register (Chessful)
je: 358 of 2133 (Localizable) and 1117 of 3649 (Lessons) ("Je hebt de gratis puzzels van vandaag gebruikt.", "Sta je voor in materiaal, dan is het…", "Bouw je openingsrepertoire op"). Only formal hit: `Know thyself`-style proverb "Ken uzelf". Studio speaks as "we" ("Een vaardigheid krijgt pas een score als we er genoeg van hebben gezien."). Mixed infinitive/imperative buttons: infinitive "Analyseren", "Importeren", "Aankopen herstellen" vs imperative "Annuleer", "Verwijder", "Analyseer je eerste partij", "Kies je bordstijl". No u/uw.

### Glossary
| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Game Review | Game Review / Review Game / Review Games | Partij bekijken / Bekijken / Spellen controleren | **Flag:** three different renderings; "Review" alone = "Herhalen" (repeat). Site term needs a choice |
| Mistake (explained) | Mistake / Mistakes / Every Mistake Explained | Fout / Fouten / Elke fout uitgelegd | `Mistake Detail` "Foutdetail", `Mistake Hunter` "Foutenjager", `Review past mistakes` "Eerdere fouten herhalen", `View 25 mistake details` "Bekijk details van 25 fouten" |
| Blunder | Blunder / Blunders | Blunder / Blunders | English loan kept |
| Game (a played game) | game | spel / partij | **Flag:** "spel" 30 values ("%d spellen geïmporteerd", "Spellen importeren", "Continue Game" "Spel hervatten") vs "partij/partijen" 75 values ("Analyseer je eerste partij", "Schone partij"). Chess usage is "partij"; "spel" is the game/app/board game |
| Stockfish analysis | Analyze with Stockfish / Stockfish is evaluating every move... | Analyseren met Stockfish / Elke zet wordt geëvalueerd... | `Stockfish (depth 12)` "Stockfish (diepte 12)"; "Analyse", "Analyseren" |
| Import (Chess.com / Lichess PGN) | Import from PGN / Import Games / Choose PGN File | Importeren uit PGN / Spellen importeren / PGN-bestand kiezen | `Paste PGN text` "PGN-tekst plakken", `Copy PGN` "PGN kopiëren"; Chess.com/Lichess names unchanged |
| Daily training from mistakes | Today's Training / Train Your Weaknesses / Training that adapts to your mistakes | Training van vandaag / Train je zwakheden / Training die zich aanpast aan je fouten | `Today's Session` "Sessie van vandaag"; `Weaknesses` "Zwaktes" (also "zwakke punten", "zwakheden"; **Flag:** three words); `%lld due today` "%lld voor vandaag" |
| Puzzles from your mistakes | Puzzles from your real mistakes / Puzzle rating | Puzzels van je echte fouten / Puzzelrating | `Next puzzle` "Volgende puzzel"; `%lld free puzzles left today` "Gratis puzzels vandaag: nog %lld"; library credit "Puzzels: open database van Lichess.org (CC0)" |
| Coach hints | Hint / In-game Coach / Hint strength | Hint / Coach tijdens de partij / Hintsterkte | `Solved with a hint.` "Opgelost met een hint."; "A hint was used, so this one isn't rated." "Er is een hint gebruikt, dus deze telt niet mee voor je rating." |
| Endgames (96 positions) | Endgames / Endgame trainer / Unlock all endgames | Eindspelen / Eindspeltrainer / Ontgrendel alle eindspelen | `The first position of each category is free.` "De eerste stelling van elke categorie is gratis."; categories "Pioneneindspelen", "Toreneindspelen", "Paardeneindspelen", "Lopereindspelen", "Dame-eindspelen"; "stelling" = position |
| Opponents (40) | 40 Unique Opponents / Opponents | 40 unieke tegenstanders / Tegenstanders | tiers: `Novice` "Beginner", `Beginner` "Beginneling", `Casual` "Recreatief", `Intermediate` "Gemiddeld", `Advanced` "Gevorderd", `Expert` "Expert", `Master` "Meester". **Flag:** achievements say "beginnende", "halfgevorderde", "casual" for the same tiers ("Versla alle halfgevorderde tegenstanders" vs tier "Gemiddeld"); "Novice" and "Beginner" tiers become "Beginner" and "Beginneling" |
| Elo | %lld ELO / Performance ELO | %lld ELO / Prestatie-ELO | **Flag:** "ELO" capitals (3 values); the rating system is "Elo". Site text says "Elo"; `Estimated Rating` "Geschatte rating", `Rating` "Rating" |
| Boards (2D and 3D) | Classic 2D / 3D Board / Board Style / 3D Piece Style | Klassiek 2D / 3D-bord / Bordstijl / 3D-stukstijl | `Choose your board style` "Kies je bordstijl"; `boardStyle.marble` "Marmer", "Burled Wood" "Wortelnotenhout", "Ebony & Bird's-eye Maple" "Ebben & vogeloogesdoorn", "Brass & Pewter" "Messing & tin" |
| Opening repertoire | Opening Repertoire / White Repertoire / Black Repertoire | Openingsrepertoire / Repertoire met wit / Repertoire met zwart | `Build your opening repertoire` "Bouw je openingsrepertoire op" |
| Progress you can read | Progress / Skills / Weekly Comparison / Weakness Trends / Achievements | Voortgang / Vaardigheden / Wekelijkse vergelijking / Zwaktetrends / Prestaties | `Detailed Progress` "Gedetailleerde voortgang", `Rating Over Time` "Rating in de tijd", `Accuracy Trend` "Nauwkeurigheidstrend", `Insights` "Inzichten", `Dashboard` "Overzicht"; achievements ("59 achievements") = "Prestaties" |
| Streak | Streak / Day Streak | Reeks / Dagelijkse reeks | "%lld dagen reeks" (word order wrong: natural "reeks van %lld dagen"), "3-dagenreeks", "Winnende reeks" |
| Lessons (156) | Learn / %lld of %lld lessons completed | Leren / %1$lld van %2$lld lessen voltooid | tabs: `Play` "Spelen", `Learn` "Leren", `Training` "Training", `Insights` "Inzichten"; `Progress` "Voortgang" |
| Play against opponent | Play vs %@ | Speel tegen %@ | `%@'s move` "Zet van %@", `Black to move` "Zwart is aan zet" |
| Settings → Reset Everything | Reset Everything | Alles resetten | "reset" anglicism; `Settings` "Instellingen" |
| Game Center / leaderboards | Compete on leaderboards and earn achievements | Strijd in ranglijsten en verdien prestaties | `Sign in to Game Center` "Aanmelden bij Game Center" (vs Pulse "Log uit"/"Niet ingelogd": aanmelden vs inloggen) |
| Privacy / no account / offline | No Account. No Tracking. | Geen account. Geen tracking. | "Al je gegevens blijven op dit apparaat. Geen accounts, geen servers, geen tracking."; "Je schaakgegevens blijven op dit apparaat. Geen analytics, geen tracking. Game Center-scores en aankopen gaan uitsluitend via de servers van Apple." |
| Free tier | Free Plan | Gratis plan | `Free plan: %d of %d analyses left today.` "Gratis abonnement: vandaag nog %1$d van %2$d analyses over." (mix "plan" / "abonnement"); the free tier is not a subscription |
| iPhone, iPad, Mac | Universal / Mac | – | no dedicated strings; platform names unchanged |

### Paid tier names in the Dutch UI (Chessful)
- **The in-app tier name is "Premium", not "Pro"**: `Chessful Premium` "Chessful Premium", `Premium` "Premium", `Upgrade to Premium` "Upgrade naar Premium", `Premium restored. Your progress will appear once you analyze a game.` "Premium hersteld. Je voortgang verschijnt zodra je een partij analyseert.", "Alle functies ontgrendeld". The English site page says "Chessful Pro"; the App Store IAP names (Dutch page) also say "Chessful Pro maandabonnement / jaarabonnement / eenmalig". "Pro" occurs once in the Dutch catalog ("Pro-override (debug)"). Mismatch app vs store vs site, see Flags.
- Periods: `Monthly` "Maandelijks", `Yearly` "Jaarlijks", `Lifetime` "Levenslang", `Purchase Lifetime` "Levenslang kopen"; `Auto-renews monthly. Cancel anytime.` "Verlengt maandelijks automatisch. Op elk moment opzegbaar."; `Renews monthly` "Maandelijkse verlenging"; `%@, then %@/month. Cancel anytime.` "%@, daarna %@/maand. Op elk moment opzegbaar."; `BEST VALUE` "BESTE WAARDE" (calque); `$3.33/month · 3-day free trial` "$3,33/maand · 3 dagen gratis".
- Trial: `Start Free Trial` "Gratis proberen"; `%@ free trial` "%@ gratis proberen"; `3-day free trial` "3 dagen gratis". "Proefperiode" is not used in Chessful (Pulse and AfterShift do).
- Restore: **`Restore Purchases` = "Herstellen"** (short, loses "purchases") and `Already subscribed? Restore Purchases` "Al geabonneerd? Aankopen herstellen"; `Restore Failed` "Herstellen mislukt"; Manage: `Manage Subscription` "Abonnement beheren"; `Subscribe Now` "Nu abonneren".
- Store IAP names (page): `Chessful Pro maandabonnement € 2,99`, `Chessful Pro jaarabonnement € 17,99`, `Chessful Pro eenmalig € 34,99`, plus tips `Koffie trakteren € 1,99`, `Supporter € 5,99`, `Royale steun € 9,99`.

### Dutch App Store listing (checked 2026-11-19)
- Name: **Chessful: Train & Analyseer**. Subtitle: **Tactiek, Puzzels & Coach**.
- Description in Dutch (je): "Je hebt de partij verloren en weet niet welke zet het deed. Chessful wel. Stockfish controleert elke zet op je apparaat, en bij elke fout hoort een uitleg in gewone taal." Languages 33 incl. NL; category Games; "Gratis"; iOS 18.0; devices include Mac.

---

## Cross-app terms (how these five apps write recurring words in Dutch)

| Word | AfterShift | AllPaid | AppMeta | AppMeta Pulse | Chessful | Site choice suggested |
|---|---|---|---|---|---|---|
| subscription | abonnement ("Abonnementen worden automatisch verlengd") | abonnement; also (wrongly) the free tier | – | abonnement / abo's / abonnees | abonnement; "Gratis abonnement"/"Gratis plan" | **abonnement**, never "abo" in running text |
| lifetime | Levenslang; "Eenmalige aankoop" | Levenslang; "Levenslange toegang"; "Eenmalige aankoop" | – | Levenslang; "Levenslange toegang" | Levenslang; "Levenslang kopen" | **Levenslang** (the tier label) with "eenmalige aankoop" as the explanation. Store names say "eenmalig"/"Levenslang" (varies) |
| free trial | proefperiode, "7 dagen gratis proberen" | proefperiode | – | proefperiode (and "proefabo's") | "Gratis proberen", "3 dagen gratis" | **gratis proefperiode** |
| sync | synchronisatie, "synchroniseren" | iCloud-synchronisatie | – | synchronisatie (71 values) | – (no sync) | **synchronisatie / synchroniseren**; never "sync" |
| iCloud | – | iCloud-synchronisatie, iCloud-account | – | iCloud-synchronisatie, "iCloud-gegevens" | – | write **iCloud-synchronisatie** with a hyphen |
| Health | Apple Health (20) / Gezondheid-app (5) / Apple Gezondheid (permission prompt) | – | – | – | – | **mixed in AfterShift; pick one and check Apple's Dutch names** |
| widget | (7 gallery names, "widget" not in text) | widgets named, text uses "widgets" in Pulse only | – | **widget(s)** | – | **widget** (plural "widgets") |
| Lock Screen / Home Screen | toegangsscherm | – | – | toegangsscherm / beginscherm | – | **toegangsscherm**, **beginscherm** (Apple Dutch) |
| settings | Instellingen | Instellingen | – | Instellingen | Instellingen | **Instellingen** (consistent) |
| export | exporteren ("Slaaprapport exporteren") | – | – | Exporteer (imperative) | – | **exporteren**; PDF "pdf" lowercase in Pulse, "PDF" elsewhere |
| privacy | "Privacy voorop", "Privacybeleid" | Privacybeleid | – | "Privacy", "Privacybeleid" | "Privacy", "Gegevens & Privacy" | **privacy**, **privacybeleid** |
| no account | – (no string; "Gegevens blijven op je apparaat") | – | – | "Geen advertenties, geen tracking" | "Geen account. Geen tracking."; "Geen accounts, geen servers" | **geen account** |
| restore purchases | Aankopen herstellen | Aankopen herstellen | – | Aankopen herstellen | Herstellen (button), Aankopen herstellen (inline) | **Aankopen herstellen** |
| cancel anytime | Op elk moment opzegbaar | Op elk moment opzegbaar | – | – | Op elk moment opzegbaar | **op elk moment opzegbaar** |
| Premium vs Pro | Premium | Pro | Pro (English UI) | no tier name | **Premium in the app, Pro on the site/store** | per app; Chessful needs a decision |
| best value | Beste deal | – | – | Voordeligst | BESTE WAARDE | no shared label; **voordeligst** is the natural one |
| Cancel / Delete buttons | Annuleer? (not in sample), infinitives | Annuleer / Verwijder | – | Annuleer / Verwijder | Annuleer / Verwijder | imperative je-form in apps; site should avoid UI button names |

---

## Flags (app-side string bugs worth an issue)

Register: **no mix.** All four Dutch apps are je; the single "u" is the proverb "Ken uzelf" (Chessful). No issue for register.

1. **AppMeta (macOS) has no Dutch interface** (no `nl` in any of the 2300 keys, `nl` not in knownRegions) and the Dutch store page shows an English name, English description and the Dutch subtitle "Diensten" (source unclear). The Dutch site page for AppMeta must not claim a Dutch UI. If Dutch is wanted: add `nl` to the catalog (13 languages already carry it).
2. **Chessful tier name mismatch.** App paywall says "Premium" (`Chessful Premium`, "Upgrade naar Premium", "Premium hersteld", "Alle functies ontgrendeld"); the store IAP names (Dutch page) and the English site page say "Chessful Pro". One of the three must change; until then the Dutch site page should follow the site/store ("Pro") but a screenshot of the Dutch paywall will say "Premium". Chessful, AllPaid and AfterShift use different tier words (Pro / Pro / Premium).
3. **Chessful** `Restore Purchases` = "Herstellen" (button is too short; elsewhere "Aankopen herstellen"). `BEST VALUE` = "BESTE WAARDE" (calque). `Start Free Trial` = "Gratis proberen" while the same screen says "Gratis plan"/"Gratis abonnement" (free tier called both plan and subscription). `%lld day streak` = "%lld dagen reeks" (word order). `Game Review` has three renderings ("Partij bekijken", "Bekijken", "Spellen controleren"), `Review` alone = "Herhalen". "spel" (30 values) vs "partij" (75) for a played game. "ELO" (capitals) for Elo. Opponent tiers: "Intermediate" = "Gemiddeld" but achievements say "halfgevorderde", "Novice" = "Beginner" and "Beginner" = "Beginneling". Zwaktes / zwakke punten / zwakheden for weaknesses.
4. **AfterShift** `Readiness` has four renderings (Paraatheid, Dienstgereedheid, "Herstel vergrendeld" for "Readiness locked", Siri "Hoe fit ben ik"). `Caffeine Timing` has four forms (Cafeïnetiming / Cafeïne-timing / Timing van cafeïne / Cafeïnestop). `Wind down` has three (Ontspannen / Ontspantijd / Tot rust komen). `Apple Health` vs "Gezondheid-app" vs "Apple Gezondheid" (permission prompt). `roster.tapToAdd` drops "or set up a repeating rotation". `paywall.bestValue` "Beste deal" (colloquial). "Ontwakingen" for Awakenings. English leftovers: `technique.cognitiveShuffle.title` "Cognitive Shuffle", "playbook" in `paywall.lock.smartPlaybook` / `customScenarios`, `roster.whatIf.later` "%@ later", `rotation.weekN` "Week %d", `rotation.preset.ddnn` "2 dag / 2 nacht" (singular), "Dutje loggen" anglicism. `stages.core` "Licht" for Core: verify against Apple Gezondheid's Dutch label. **NSCalendarsUsageDescription / NSCalendarsFullAccessUsageDescription are English-only** (build settings, not in `nl.lproj/InfoPlist.strings`) — same defect as in pt.
5. **AllPaid** Siri App Shortcut phrases have no localization at all (English-only on Dutch devices; no `AppShortcuts.xcstrings`). English leftovers: `Contract start` (reads as a Dutch verb), `Start Pro`, `1 week`, `%@ / week`, `Horizon` (widget), "Entertainment". `Free plan` = "Gratis abonnement" (free tier is not a subscription). Inconsistent buttons ("Als betaald markeren" infinitive vs "Markeer als verlengd" imperative; "Annuleer", "Verwijder"). "Upgraden naar Pro" vs "Upgrade naar Pro om…". "Meerdere herinneringen per contract is een Pro-functie." (verb agreement).
6. **AppMeta Pulse** abo / abonnee / abonnement / proefabo mix (`Subs` "Abo's", `Active subscribers` "abonnees", `Trials` "Proefabo's" vs "proefperiodes"); `Reply` has three renderings (Reactie, antwoord, Beantwoord); `Done` = "Voltooid"/"Gereed" mixed (Chessful: "Klaar"); `Sales` singular "Verkoop" vs plural "Verkopen"; `Export as PDF…` "pdf" lowercase vs "PDF" elsewhere; `Refunds` = "Terugbet." (truncated abbreviation); `Best Value` = "Voordeligst" fine. Siri phrase 1 "Open ${applicationName}" is correctly identical.
7. Dutch App Store listings: AfterShift, AllPaid, AppMeta Pulse and Chessful have Dutch name, subtitle and description; **AppMeta (macOS) has none** (English description, English name). Store IAP names differ from the in-app names: AfterShift "Premium eenmalige aankoop", AllPaid "AllPaid Pro eenmalig", Pulse "AppMeta Pulse Levenslang", Chessful "Chessful Pro eenmalig" (the apps say "Levenslang").
8. The apps use **"Apple ID"** (AllPaid, Chessful, AfterShift) and **"Apple Account-ID"** (Pulse) for the same thing; the site should follow Apple's current Dutch name once verified in `nl-apple-terms.md`.


---

## Dutch glossary, batch 2: earnlock, gymlogger-x, liftlog, mediakit, millrace

Method (checked 2026-11-19, read-only; nothing in the app folders was run or built, nothing in the repo touched except this file). Coverage was counted with `python3 -I` over each app's `.xcstrings` catalogs (`strings` → key → `localizations.nl` → `stringUnit`, plural/substitution variations, or `stringSet`; keys with `shouldTranslate: false` and blank keys excluded; "translated" = every unit has state `translated`). The locale code is plain `nl` in every catalog (no `nl-NL`). "Identical to English" counts every `nl` value equal to the English key/value, including brand names, units and format-only strings (so it overstates real English left in; the real leftovers are listed per app). GymLogger X has no `.xcstrings`: its JSON files `GymLogger/Localizations/nl.json`, `GymLoggerWidget/Localizations/nl.json`, `GymLoggerWatch Watch App/Localizations/nl.json` were compared key by key with `en.json`, plus `GymLogger/nl.lproj/InfoPlist.strings`, `ExerciseTranslations.nl.json`, `RehabTranslations.nl.json` and `Programs/Data/coach_programs.json` (`localizedTitles.nl`). Register counts are rough regexes on the Dutch values (je = je/jij/jouw/jou/jezelf; u = a standalone lowercase `u`/`uw`, every hit hand-checked: the only hits are the hour abbreviation "24 u-cooldown", "1 u uitstellen", a Reddit handle `/u/ivysaur` and a `%u` format code, never a polite address). Dutch strings are copied verbatim (straight `'` or curly `’` as in the source; both occur, sometimes in the same catalog). Store data: iTunes lookup (`country=nl&lang=nl_nl`) plus `curl -sL --compressed` of `apps.apple.com/nl/app/id<ID>` with the Safari UA (EarnLock's page needed two 429 retries; all five pages were read). The store page also prints the seller's personal name and address; neither is copied here. Prices keep the NBSP before the digit (`€ 9,99`) and are reference only: the site prints prices from the catalog / `MASTER-prices.csv`. Apple's own Dutch names seen in these apps (Apple's NL terms, for the apple-terms sheet): Screen Time = `Schermtijd`; Health app = `Gezondheid` (`Apple Gezondheid` in the apps); Family Sharing = `Delen met gezin`; Shortcuts = `Opdrachten`; Lock Screen = `Toegangsscherm`; Notifications (Settings) = `Berichtgeving`; Photos = `Foto's`; Files = `Bestanden`.

Headline flags for the whole batch:
- **All five apps are in Dutch and all five address the user with je/jij.** No u-form anywhere. The site can write je and quote the UI without a register clash.
- **Four different words for "streak":** `Reeks` (EarnLock, LiftLog, GymLogger X, Millrace; also `Reeksen`, `Trainingsreeks`, `weken op rij`), but EarnLock has one `Streak-schilden` left in a sentence next to `Reeks-schilden`, and LiftLog has `Streakbadges`. Use `reeks`. Unlike Italian, `reeks` does not collide with "set", because every app writes `set` for a set.
- **"Undo" in Millrace is `terugdraaien`, not Apple's `ongedaan maken`** (13 values use `terugdraaien`/`Terugdraaitegoeden`/`terugdraaiingen`, 2 use `ongedaan maken`), and LiftLog's own delete warning uses `ongedaan worden gemaakt`. Millrace's store IAP names carry the same word (`50 keer terugdraaien`).
- **MediaKit tool names mix imperatives and infinitives** (`Comprimeer`, `Converteer`, `Stabiliseer`, `Transcribeer`, `Normaliseer`, `Splits`, `Vind duplicaten`, `Verwijder metadata` against `Inkorten`, `Samenvoegen`, `Redigeren`, `Versleutelen`, `Ondertekenen`, `Extraheren`). `Redact` = `Redigeren` is the wrong meaning ("to edit"); `Free` = `Vrij` (should be `Gratis`).
- **GymLogger X uses `Gevorderd` for two levels:** `program_level_intermediate` = `Gevorderd` and `program_level_advanced` = `Expert`, but `creator_level_intermediate` = `Gemiddeld` and `creator_level_advanced` = `Gevorderd`.
- **LiftLog's tier names differ between app and store:** in-app `Gul` / `Beschermheer`, store IAP `Genereus` / `Mecenas`; the in-app `Supporter` key is `Steuntje`. In-app `Eerlijk` / `Goed` match the store.
- **LiftLog still says "CoreLift" in 4 Dutch strings** (old name; the HealthKit explanation `CoreLift leest je gezondheidsgegevens nooit` is one of them) and has 10 keys with no Dutch.
- **EarnLock permission prompts (phone and Watch) are `needs_review`**; `Shadow Mode` appears in Dutch as `Schaduwmodus`, `schaduwweek` and, in one error string, `Shadow Mode`.
- **Store names that differ from the English name:** `EarnLock: App Blokker & Focus`, `Millrace: Getallenpuzzel` (means "number puzzle"; check against the English store name with the owner), `MediaKit Comprimeer Converteer`; GymLogger X and LiftLog keep the English names.

---

### 1. EarnLock (earnlock, source `EarnScreen`, ID 6771099230, has an Apple Watch app)

#### Dutch coverage

| Catalog | Keys | `nl` present | `nl` translated | Identical to English |
|---|---|---|---|---|
| EarnScreen/EarnScreen/Localizable.xcstrings (main app) | 620 | 620 | 620 (100%) | 32 |
| EarnScreen/EarnScreen/AppShortcuts.xcstrings | 9 | 9 | 9 | 0 |
| EarnScreen/EarnScreen/InfoPlist.xcstrings | 5 | 3 | 0 (all 3 `needs_review`) | 0 |
| EarnScreenLiveActivity/Localizable.xcstrings (widgets, Live Activity) | 148 | 148 | 148 | 6 |
| EarnScreenShield/Localizable.xcstrings | 6 | 6 | 6 | 0 |
| EarnScreenWatchComplications/Localizable.xcstrings | 13 | 13 | 13 | 8 |
| watchkitapp Watch App/Localizable.xcstrings | 28 | 28 | 28 | 8 |
| watchkitapp Watch App/InfoPlist.xcstrings | 4 | 2 | 0 (both `needs_review`) | 0 |
| EarnScreenDeviceActivity, EarnScreenShieldAction | 0 | n/a | n/a | empty catalogs |

All Localizable catalogs together: 815 keys, 815 translated (100%). The identical values are loanwords, units and brand names (`kcal`, `min`, `Premium`, `Mono`, `FOMO`, `Focus`, `Status`, `Trends`, `Week`, `Recent`, `Start`, `Privacy`, `App`, `Instagram`, `DELETE`, `EarnLock is Premium` on the Watch). Real English left in: `Kon Shadow Mode niet volgen` (key `Couldn't track Shadow Mode`), and `Minuten die Apple Health registreert als actieve beweging.` (`Apple Health` instead of `Apple Gezondheid`).

English-only gaps: `CFBundleDisplayName` and `CFBundleName` have no `nl` entry (the name stays "EarnLock", fine). The three phone permission prompts have Dutch text but are `needs_review`, and so are the two Watch prompts:
- `NSHealthShareUsageDescription`: `EarnLock leest je stappen, actieve minuten en actieve energie uit de Gezondheid-app om je voortgang te volgen richting het doel dat je geblokkeerde apps ontgrendelt. Deze gegevens verlaten je apparaat nooit.`
- `NSHealthUpdateUsageDescription`: `EarnLock leest alleen je activiteitsgegevens — er wordt niets naar de Gezondheid-app geschreven. Apple vereist deze toestemming omdat het HealthKit-framework technisch gezien gegevens kan schrijven.`
- `NSPhotoLibraryAddUsageDescription`: `Hiermee bewaar je een mijlpaalkaart in je fotobibliotheek. EarnLock leest je foto's nooit.`

Siri / App Shortcuts: 9 phrases, all Dutch and `translated` (no preposition problems): `Wat is mijn doel in ${applicationName}`, `Hoe dicht ben ik bij het ontgrendelen in ${applicationName}`, `Controleer mijn voortgang in ${applicationName}`, `Hoe ver ben ik van het ontgrendelen in ${applicationName}`, `Wanneer kan ik mijn apps openen in ${applicationName}`, `Ontgrendelvoortgang in ${applicationName}`, `Een focussessie starten in ${applicationName}`, `Vergrendel mijn apps in ${applicationName}`, `Begin met focussen met ${applicationName}`. The Dutch uses "in", the English "in" too.

Apple Watch app (Dutch): Watch catalog 28/28 and complications 13/13, both translated: `Open EarnLock op iPhone`, `Open de app op iPhone om dit horloge te synchroniseren.`, `Open de app op iPhone om te upgraden.`, `Loop om te beginnen met meten`, `Logged. Take a breath.` = `Genoteerd. Haal even adem.`, `Apple Gezondheid nodig`, `Geef toestemming op iPhone en kom hier terug.`, `Nog geen data`, `Ontgrendel voor %lld min`, `%@ tot ontgrendeling`, `Voortgang naar doel`, `Voortgang naar de ontgrendeling van vandaag.`. The Watch calls the watch "horloge" once; the product is `Apple Watch-app`.

**Verdict: app is in Dutch: yes** (100% of every Localizable catalog, widgets, Live Activity, shield, Watch, complications and Siri phrases; only the five permission prompts are `needs_review`).

#### Register

je/jij forms in 136 of 620 main-app values (plus 15 of 148 widget/Live Activity values, 2 of 6 shield values), 0 u/uw (the two `u` hits are the hour abbreviation: `Premium kan de 24 u-cooldown bij verlaging één keer per week overslaan.` and `1 u uitstellen`). The Watch and complication strings are short labels with no address. Examples: `Verdien je toegang`, `Je geblokkeerde apps blijven werken.`, `Wil je een doel dat zichzelf aanpast?`, `Meld je aan bij iCloud om Delen met gezin in te schakelen`. No mix.

#### Glossary

| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Free (tier) | `Free forever for one app. Go further with Premium.`; `Free locks one app. Premium has no limit.`; `Free plan locks 1 app. Tap to upgrade.` | `Altijd gratis voor één app. Meer met Premium.`; `Gratis vergrendelt één app. Premium heeft geen limiet.`; `Gratis vergrendelt 1 app. Tik om te upgraden.` | No standalone "Free" string. Consistent `gratis`. |
| Premium | `Premium` | `Premium` | `A Premium insight` = `Een Premium-inzicht`; `Premium-functies`; `Premium-voordeel`. Hyphenated compounds, correct. |
| Monthly / Yearly / Lifetime | `Monthly` / `Yearly` / `Lifetime` | `Maandelijks` / `Jaarlijks` / `Voor altijd` | **Flag:** Lifetime is `Voor altijd` in the bare label and `Levenslang` in `Premium · Levenslang` (key `Premium · Lifetime`); `Get Lifetime` = `Koop Voor altijd` (capital V mid-sentence). Two words for one tier. |
| Get Premium (button) | `Get Premium` | `Premium nemen` | Odd Dutch; `Upgrade`/`Premium kopen` would read better. `Upgrade` stays English (`Tik om te upgraden`, `Open EarnLock om te upgraden`). |
| Start free trial (button) | `Start free trial` | `Start gratis proefperiode` | |
| 7-day free trial | `7-day free trial, then %@/year`; `7-day free trial, then %@/month` | `Gratis proefperiode van 7 dagen, daarna %@/jaar`; `7 dagen gratis proberen, daarna %@/maand` | **Flag:** the two trial strings use different patterns (`Gratis proefperiode van 7 dagen` vs `7 dagen gratis proberen`). |
| Restore Purchases | `Restore Purchases` | `Herstel aankopen` | Imperative; `Hersteld — welkom terug.` (key `Restored — welcome back.`). Other apps write `Aankopen herstellen` (GymLogger X, LiftLog, Millrace) or both (MediaKit). |
| Today tab (site: "Today screen") | `Today`; `Go to Today` | `Vandaag`; `Ga naar Vandaag` | |
| Insights tab | `Insights` | `Inzichten` | `Insights (Week + Month)` = `Inzichten (week en maand)`; `Week + Maand inzichten` in another string (plus sign vs `en`). |
| Insights Day / Week / Month | `Day` / `Week` / `Month` | `Dag` / `Week` / `Maand` | |
| Settings tab | `Settings` | `Instellingen` | `Data & privacy` = `Gegevens en privacy`. |
| Shadow Week | `Shadow Week`; `Start Shadow Week`; `Run another Shadow Week`; `No Shadow Weeks yet` | `Schaduwweek`; `Schaduwweek starten`; `Nog een schaduwweek doen`; `Nog geen schaduwweken` | **Flag:** the app writes `schaduwweek` (lower-case, closed compound); the Mode strings: `Shadow Mode` = `Schaduwmodus`, `Today in Shadow Mode` = `Vandaag in Schaduwmodus`, `Shadow Mode summary` = `Schaduwmodus-samenvatting`, `8 PM during the Shadow Mode week.` = `Om 20:00 in de Schaduwmodus-week.`; one error string keeps English: `Kon Shadow Mode niet volgen`. `Your shadow week is done` = `Je schaduwweek is voorbij`; `Shadow Week history` = `Geschiedenis schaduwweken`; `Shadow Week in progress — Day %lld of %lld` = `Schaduwweek loopt — dag %1$lld van %2$lld`. |
| Enable real blocking | `Enable real blocking`; `Start real blocking now` | `Echte blokkering aanzetten`; `Begin nu met echte blokkering` | `aanzetten` vs `Begin ... met`; fine. |
| Emergency unlock | `Emergency unlock`; `Emergency unlock until %@` | `Nood-ontgrendeling`; `Nood-ontgrendeling tot %@` | Hyphenated; Dutch normally writes `noodontgrendeling` (closed). `Solve to continue` = `Los op om door te gaan`. |
| Partial unlock | `Partial — %lld min`; `Partially unlocked`; `Your partial unlock ends in 10 minutes.` | `Gedeeltelijk — %lld min`; `Gedeeltelijk ontgrendeld`; `Je gedeeltelijke ontgrendeling eindigt over 10 minuten.` | |
| Locked apps (grid) | `Locked apps`; `Unlimited blocked apps` | `Vergrendelde apps`; `Onbeperkt geblokkeerde apps` | **Flag:** `vergrendel-` (32 values) and `geblokkeerde`/`blokkering` (9+) both used for the same state; `Onbeperkt geblokkeerde apps` is ungrammatical (`Onbeperkt aantal geblokkeerde apps`). Use `vergrendeld` for the lock and `blokkeren` for the act. |
| Reflect (button) / reflection | `Reflect`; `Reflection summary`; `Reflections this month`; `Delete this reflection?` | `Reflecteer`; `Reflectie­samenvatting` (contains a soft hyphen U+00AD); `Reflecties deze maand`; `Deze reflectie verwijderen?` | Imperative button vs infinitive elsewhere. |
| Reflection prompt answers | `Boredom` / `Anxiety` / `FOMO` / `Habit` / `Other` | `Verveling` / `Onrust` / `FOMO` / `Gewoonte` / `Anders` | `Anxiety` = `Onrust` is a soft rendering ("restlessness"). |
| Smart Schedules | `Smart Schedules`; `Smart Schedules + custom app icons` | `Slimme schema's`; `Slimme schema's + aangepaste app-iconen` | One term in the app (`schema's`), but `Delete this schedule?` = `Deze planning verwijderen?` and `Delete schedule` = `Schema verwijderen` (planning vs schema). |
| Default schedules | `Work hours` / `Evenings` / `Weekends` / `Sleep` | `Werkuren` / `Avonden` / `Weekenden` / `Slaap` | |
| Goal tiers | `Light` / `Standard` / `Challenge` | `Licht` / `Standaard` / `Uitdaging` | |
| Daily goal | `Daily goal`; `Goal`; `Change goal`; `Pick your goal` | `Dagdoel`; `Doel`; `Doel wijzigen`; `Kies je doel` | Also `dagelijkse doel` (`...tot je je dagelijkse doel haalt`) next to `Dagdoel`. |
| Adaptive | `Adaptive` | `Adaptief` | `Zet Adaptief altijd aan in Instellingen.` |
| Steps / Active minutes / Active calories | `Steps` / `Active minutes` / `Active calories` | `Stappen` / `Actieve minuten` / `Actieve calorieën` | `Active minutes & calories` = `Actieve minuten en calorieën`. Plural: `%lld stap` / `%lld stappen`. |
| "N steps until unlock" (shield) | `%@ until unlock`; `1,247 steps until unlock`; `Earn %@ more %@ to unlock` | `nog %@ tot ontgrendeling`; `nog 1.247 stappen tot ontgrendeling`; `Verdien nog %1$@ %2$@ om te ontgrendelen` | Shield title `Earn your way in` = `Verdien je toegang`; button `Earn it` = `Verdien het`; widget/complication `%@ to unlock` = `%@ tot ontgrendeling`; Live Activity `%@ more %@ and you'll unlock %@.` = `Nog %@ %@ en je ontgrendelt %@.` |
| Streak | `Streak`; `Current streak`; `Streaks` | `Reeks`; `Huidige reeks`; `Reeksen` | **Flag:** `Streak shields — keep your streak through rest days` = `Streak-schilden — behoud je reeks op rustdagen` (English `Streak` left in); the plain key `Streak shields` = `Reeks-schilden`. `Streak at risk` = `Reeks loopt risico`. |
| Rest day | `Rest day`; `Weekly rest day`; `Rest day earned`; `Rest day taken` | `Rustdag`; `Wekelijkse rustdag`; `Rustdag verdiend`; `Rustdag genomen` | |
| Streak shield | `Shield saved your streak` (key text in Reeks-schilden) | `Reeks-schilden` | Singular `schild`: `...en gebruikt geen schild.` |
| Screen time saved (estimate) | `Screen time saved`; `Screen time saved (estimated)` | `Bespaarde schermtijd`; `Bespaarde schermtijd (geschat)` | One word `schermtijd`. |
| Most-attempted blocked app | `Most attempted blocked app today` | `Vandaag meest geprobeerde geblokkeerde app` | |
| Screen Time (Apple feature) | `Allow Screen Time access`; `iOS Settings → Screen Time → EarnLock` | `Schermtijd toestaan`; `Instellingen → Schermtijd → EarnLock` | Apple's NL name `Schermtijd`; `Schermtijd-toegang`, `Schermtijd-beperkingen`. Parental approval: `Parental approval required` = `Goedkeuring van ouders vereist`; `een ouder of voogd`. |
| Apple Health | `Apple Health` | `Apple Gezondheid` | `Apple Health` appears in two values (e.g. `Minuten die Apple Health registreert als actieve beweging.`, `...Apple Health tracks automatically` is `Apple Gezondheid houdt het bij.`). Permission prompts say `Gezondheid-app`. |
| Activity heatmap | `Activity heatmap` | `Activiteitskaart` | Other apps keep `Heatmap`. |
| Best week | `Best week` | `Beste week` | |
| App icons | `Midnight` / `Ember` / `Mono` | `Middernacht` / `Gloed` / `Mono` | `Alternate icons are a Premium perk.` = `Alternatieve iconen zijn een Premium-voordeel.` (`iconen`; the app also writes `app-iconen`). |
| Quiet hours | `Quiet hours` | `Stille uren` | |
| Focus session | `Focus session`; `Start focus session` | `Focussessie`; `Focussessie starten` | |
| Cooldown | `Cooldown active`; `Cooldown bypass` | `Cooldown actief`; `Cooldown overslaan` | English `cooldown` kept. |
| Widgets (Live Activity catalog) | `EarnLock — Contributions` / `— History` / `— Streak` / `— Summary` / `— Today & Month` / `— Lock Screen` / `— Pick apps` / `— Tap to set up` | `EarnLock — Verdiende dagen` / `— Geschiedenis` / `— Reeks` / `— Overzicht` / `— Vandaag & maand` / `— Toegangsscherm` / `— Kies apps` / `— Tik om in te stellen` | `Toegangsscherm` is Apple's NL Lock Screen term, correct. `Bigger squares. Large widget, past year only.` = `Grotere vakjes. Groot widget, alleen afgelopen jaar.` (`Groot widget`: widget is "het/de"; flag minor). |
| Apple Watch app | `Apple Watch app` | `Apple Watch-app` | |
| Family Sharing | `Family Sharing supported — Premium unlocks for up to five family members in your Apple Family group.` | `Werkt met Delen met gezin — Premium wordt ontgrendeld voor maximaal vijf gezinsleden in je Apple-gezinsgroep.` | Apple's NL term `Delen met gezin`. |

#### Paid tier names in the Dutch UI

`Premium` (tier name, not translated), `Premium · Maandelijks` / `Premium · Jaarlijks` / `Premium · Levenslang` (combined labels), bare labels `Maandelijks` / `Jaarlijks` / `Voor altijd`; buttons `Premium nemen`, `Koop Voor altijd`, `Start gratis proefperiode`; `Herstel aankopen`; product name `EarnLock Premium`. Trial: `Gratis proefperiode van 7 dagen, daarna %@/jaar`, `7 dagen gratis proberen, daarna %@/maand`. Lapsed: `Je geblokkeerde apps blijven werken. Premium-functies (Slimme schema's, Week + Maand inzichten, aangepaste iconen) zijn vergrendeld totdat je verlengt.` Dutch store IAP names: `EarnLock Premium eenmalig` € 22,99 · `EarnLock Premium jaarlijks` € 9,99 · `EarnLock Premium maandelijks` € 1,99 (store says `eenmalig`, the app says `Voor altijd`/`Levenslang`).

#### Dutch App Store listing (checked 2026-11-19)

- Name: **EarnLock: App Blokker & Focus** (English "EarnLock: App Blocker & Focus"). Page title "EarnLock: App Blokker & Focus".
- Subtitle: **Minder schermtijd via beweging** (English "Your steps unlock screen time").
- Category: **Productiviteit**. Price **Gratis** with in-app purchases. Age 9+. iOS 17.0+. Size 16,4 MB. Languages: "Nederlands en 32 andere".
- Description is in Dutch (starts "Het is weer elf uur 's avonds, en je kunt niet één ding noemen dat je hebt gezien."; section head `EERST BEWEGEN. DAN SCROLLEN.`; says `de Gezondheid-app`, `dagelijks doel in stappen`, `halverwege`, `middernacht`). Store release note is Dutch.

---

### 2. GymLogger X (gymlogger-x, source `GymLogger`, ID 6755734580)

#### Dutch coverage

No `.xcstrings`: text comes from JSON tables plus `nl.lproj/InfoPlist.strings`.

| File | Keys | `nl` present | Identical to English |
|---|---|---|---|
| GymLogger/Localizations/nl.json (main app) | 2923 | 2923 (0 missing, 0 extra) | 145 (loanwords, units, `Home`, `Trends`, `Heatmap`, `Offline`, `Status`, `Superset`, `Push`, `Pull`) |
| GymLoggerWidget/Localizations/nl.json | 115 | 115 | 11 |
| GymLoggerWatch Watch App/Localizations/nl.json | 98 | 98 | 8 |
| GymLogger/nl.lproj/InfoPlist.strings | 4 | 4 | `CFBundleDisplayName`/`CFBundleName` = `GymLogger X` |
| ExerciseTranslations.nl.json | 1500 exercises (the English file holds 2856 entries, of which 1500 are the app's) | 1500 | 2 names unchanged |
| RehabTranslations.nl.json | 60 names, 68 notes, 64 keyword entries | all | not audited |
| Programs/Data/coach_programs.json `localizedTitles.nl` | 44 programs | 44 | 1 (`The Golden Six`) |

No state field exists in the JSON, so "translated" = present and different or a legitimate loanword. Real English left in (main app): `home_title` / `info.home.title` = `Home` (tab title, the app has Home/Training/Progress/Settings; Dutch alternatives: `Start`, as LiftLog does), `Trends`, `Heatmap`, `Offline`, `Spreadsheets (CSV)`. The widget catalog has `widget_calories_heart_rate` = `calorieën & hartslag te zien` (a fragment that only makes sense after another string).

Permission prompts (both Dutch, `InfoPlist.strings`): `NSHealthShareUsageDescription` = `GymLogger leest je hartslag en calorieën om trainingsinzichten te bieden en je fitnessvoortgang bij te houden.`; `NSHealthUpdateUsageDescription` = `GymLogger slaat je voltooide trainingen op in Apple Gezondheid om je activiteitsringen en trainingsgeschiedenis compleet te houden.` (the prompt says `GymLogger`, the app's name is `GymLogger X`; `Welkom bij GymLogger` is the same.)

Siri / App Shortcuts: **none exist** (no `AppShortcutsProvider`; the widget extension has intents for the Start Workout control and widget configuration only). Do not promise Dutch Siri phrases.

**Verdict: app is in Dutch: yes** (100% of the main, widget and Watch tables; exercise names, exercise instructions and the 44 program titles are localized too).

#### Register

je/jij forms in 315 of 2923 main values, 0 u/uw. Examples: `Zie wat werkt. Corrigeer wat niet werkt. Sneller vooruitgang.`, `Je bent achter`, `Laten we weer op schema komen.`, `Je lichaam is er klaar voor.`, `Sleep om te herschikken, tik op iconen om te verbergen of te vergrendelen`. Many buttons are neutral infinitives (`Training starten`, `Training beëindigen`) or imperatives (`Train vandaag`, `Track je eerste training`). No mix of je/u.

#### Glossary

| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Workout | `Start Workout` / `End Workout` / `Workout Complete!` / `Finish Workout` | `Training starten` / `Training beëindigen` / `Training voltooid!` / `Training voltooien` | The app writes `training` (391 values) and almost never `workout` (4 values). **Cross-app:** LiftLog and MediaKit-free words differ: LiftLog writes `workout` (65 values). |
| Training tab / Home / Progress / Settings | `Training` (`training_title`); `Home` (`home_title`); `Progress`; `Settings` | `Training`; `Home`; `Voortgang`; `Instellingen` | `Home` left in English; blueprint tabs: Home, Training, Progress, Settings. |
| Progress tab sub-tabs: Insights, Overview, Heatmap, Trends, PRs | `Insights`; `Overview`; `Heatmap`; `Trends`; `PRs` | `Inzichten`; `Overzicht`; `Heatmap`; `Trends`; `PR's` | `muscle_heatmap` = `Spier-heatmap` (hyphenated). `Guide` = `Gids`. |
| Set | `Set` / `Sets` (`set`, `sets`) | `Set` / `Sets` | Dutch loanword; plural `sets`. `Warm-up set` = `Warming-upset`. |
| Reps | `Reps` | `Herhalingen` | 59 `herhaling` values vs 6 `reps`: `Rep-Max table`, `Rep record` = `Reps-record`, `+1 Rep` = `+1 herhaling`. |
| Weight | `Weight` | `Gewicht` | `Best Weight` = `Beste gewicht` (grammar: `Best gewicht`). |
| Warm-up set | `Warm-up set`; `Mark as warm-up` | `Warming-upset`; `Markeren als warming-up` | `Warming-upset` is an odd compound; `warming-upset` is accepted but `opwarmset` is the usual word. Consistent `warming-up`. |
| Superset / Giant set | `Superset`; `Giant Set`; `Create Giant Set`; `Group as Giant Set` | `Superset`; `Giant set`; `Giant set aanmaken`; `Groepeer als giant set` | English `giant set` kept lower-case; **cross-app:** LiftLog says `Reuzenset`. |
| Rest timer | `Rest timer`; `Heart Rate Rest Timer` | `Rusttimer`; `Hartslag-rusttimer` | Watch: `Rust overslaan`, `SLIMME RUST` for `SMART REST`; `Heart Rate Rest Timer` is `Hartslag-rusttimer`. |
| Plate calculator | `Plate Calculator` | `Schijvencalculator` | |
| Estimated 1RM | `Estimated 1RM`; `Est. 1RM`; `Best 1RM` | `Geschat 1RM`; `Gesch. 1RM`; `Beste 1RM` | `1RM-voortgang`. |
| Personal records / PRs | `Personal Records`; `Current PR`; `NEW RECORD`; `PRs` | `Persoonlijke records`; `Huidig PR`; `NIEUW RECORD`; `PR's` | `PR` kept as the abbreviation; widget `Record`. |
| Next Move card | `Next Move` (`analytics_next_move_label`) | `Volgende stap` | Headlines: `Neem een rustdag`, `Varieer je %@-routine`, `Geef prioriteit aan %@`, `Klaar om hard te trainen`, `Blijf consistent trainen`. |
| Plateau status | `Plateau Detected`; `Monitoring`; `Progressing`; `Plateau Detection` | `Plateau gedetecteerd`; `Bewaken`; `Vooruitgang`; `Plateaudetectie` | `Monitoring` = `Bewaken` ("guarding") is a weak match (`Volgen`). |
| Readiness / fatigue | `Train Smart`; `Recovery Day`; `Ready`; `High Fatigue` | `Train slim`; `Hersteldag`; `Klaar`; `Hoge vermoeidheid` | Fatigue scale: `Zeer licht` / `Licht` / `Gebalanceerd` / `Hoge vermoeidheid` / `Zeer hoog`. |
| Strength Progress / overload | `Weight PR`; `More sets`; `Maintained`; `Regression` | `Gewicht-PR`; `Meer sets`; `Behouden`; `Terugval` | |
| Set Volume (MEV / MAV / MRV) | `Below MEV`; `In range`; `Near MRV`; `Above MRV` | `Onder MEV`; `Binnen bereik`; `Bijna MRV`; `Boven MRV` | Abbreviations kept English. `set_volume_warmup_caption`: `Sets die je als warming-up markeert, tellen niet mee`. |
| Weekly Summary | `Weekly Summary`; `WEEK IN REVIEW` | `Weekoverzicht`; `WEEK IN OVERZICHT` | `WEEK IN OVERZICHT` is a calque of "Week in review"; `weekrapport` appears in `Nog geen weekrapport` (key `No Weekly Report Yet`). |
| Training programs | `Programs`; `Program Details`; `Program Activated!` | `Programma's`; `Programmadetails`; `Programma geactiveerd!` | **Flag:** `Program Name` = `Schemanaam`, `Plan` = `Schema`, `has been added to your training programs` = `is toegevoegd aan je trainingsschema's` (programma vs schema vs trainingsschema for one thing). |
| Smart Program Creator | `Program Creator`; `Smart Program Creator — built around you` | `Programmamaker`; `Smart Program Creator — op jou afgestemd` | The paywall tile keeps the English name; `Programmamaker` elsewhere. Pick one for the site. |
| Training level | `Intermediate` / `Advanced` (`program_level_*`) vs (`creator_level_*`) | `Gevorderd` / `Expert` vs `Gemiddeld` / `Gevorderd` | **Flag (defect):** `Gevorderd` means Intermediate in `program_level_intermediate` and Advanced in `creator_level_advanced`. `Beginner` is unchanged. |
| Deload | `Deload`; `Take a deload week` | `Deload`; `Neem een deloadweek` | `Deload` kept (loanword), `deloadweek`, `Overweeg een deload`. |
| Periodization | `Periodization` | `Periodisering` | `Change reps/sets each week in a cycle` = `Wijzig herhalingen/sets elke week in een cyclus`. |
| Muscle heatmap | `Muscle Heatmap` | `Spier-heatmap` | `muscle_map` widget = `Spierkaart`. |
| Templates | `Templates`; `Workout Templates` | `Sjablonen`; `Trainingssjablonen` | |
| History / Exercises | `History`; `Exercises` | `Geschiedenis`; `Oefeningen` | |
| Streak | `Streak` | `Reeks` | Widget `Start streak!` = `Start reeks!`, `Weeks in a row` = `Weken op rij`. |
| Programs on the site: Whole Body Program, The Golden Six, 2-/3-/4-Day Split Routines, Linear 5×5 Foundation, push/pull/legs, German Volume Training, Texas Method, Powerbuilding 5-Day, Hybrid Strength (Lift + Run) | `coach_programs.json` titles | `Fullbody-programma`; `The Golden Six`; `2-daagse splitroutine` / `3-daagse splitroutine` / `4-daagse splitroutine`; `Lineair 5×5-fundament`; `Push / Pull / Benen (6 dagen)` and `Push/Pull/Benen 3 dagen`; `Duitse volumetraining (10×10)`; `Texas-methode`; `Powerbuilding in 5 dagen`; `Hybrid Kracht (Lift + Run)` | **Flags:** `Intermediate 5×5-ramp` and `Dumbbell Only Hypertrofie` are half English; `Push/Pull/Benen 3 dagen` vs `Push / Pull / Benen (6 dagen)` format mismatch; `Droge massa` / `Droge kracht` for `Lean Mass` / `Lean Strength` is bodybuilder slang. |
| Smart Program Creator splits | `Arnold Split`; `Bro Split` | `Arnold-split`; `Bro-split` | `Chest/Back, Shoulders/Arms, Legs` = `Borst/Rug, Schouders/Armen, Benen`. |
| Widgets | `Training Grid`; `Muscle Map`; `Today`; `Lift Ladder`; `Record` (`widget_plate`); `Ledger`; `Conditioning` | `Trainingsraster`; `Spierkaart`; `Vandaag`; `Krachtladder`; `Record`; `Grootboek`; `Conditie` | **Flag:** `Ledger` = `Grootboek` (accounting term) and `Lift Ladder` = `Krachtladder` are loose renderings; widget text `Which muscles you have stopped training.` = `Welke spieren je niet meer traint.` |
| Apple Watch app | `Apple Watch` (`settings_watch_section_title`) | `Apple Watch` | Watch labels in capitals: `SET LOGGEN`, `LOG VOLGENDE SET`, `LOG GEWICHT EN HERHALINGEN` (English `LOG` left in two), `Hartslag toegang geweigerd` (split compound; should be `Toegang tot hartslag geweigerd`). |
| iCloud Sync | `iCloud Sync` | `iCloud-synchronisatie` | Hyphen after `iCloud`; `Sync Workouts` = `Trainingen synchroniseren`; `Synced` = `Gesynchroniseerd`. |
| Apple Health | `Apple Health`; `Saved to Apple Health` | `Apple Health`; `Opgeslagen in Apple Health` | **Flag:** 10 in-app strings keep `Apple Health`, while the permission prompts and `onboarding` say `Apple Gezondheid` (0 `Apple Gezondheid` in the main table). The Watch hint says `Open Instellingen > Gezondheid op je Watch`. |
| Export / import CSV | `Export Diagnostics`; `Import from Spreadsheets` | `Diagnostiek exporteren`; `Spreadsheets (CSV)` | `Kies een CSV- of TXT-bestand geëxporteerd vanuit je vorige app of spreadsheet.` |
| Live Activities | none in catalog | none | No UI string. |

#### Paid tier names in the Dutch UI

`Pro` (not translated; `Pro actief`, `Pro-functie`, `Pro-status`, `Pro ontgrendeld!`), `GymLogger X Pro`; plan labels `Maandelijks` / `Jaarlijks` / `Levenslang` (`paywall_plan_lifetime`); `Levenslang Pro` (`paywall_lifetime_pro`), `LEVENSLANGE TOEGANG`, `Levenslange toegang kopen`, `Levenslang Pro ontgrendelen`; `Eenmalige betaling`; `Betaal eenmalig, voor altijd van jou. Geen verlenging.`; `Bezit GymLogger voor altijd`. Trial: `GRATIS VOOR 1 WEEK`, `1 week gratis proefperiode`, `1 week gratis proefperiode • BESTE WAARDE` (`BEST VALUE` = `BESTE WAARDE`, a calque; `Beste prijs`/`Voordeligst` is natural), `Start gratis proefperiode`, `Proefperiode eindigt morgen`, `Laatste dag van gratis proefperiode`, `Bespaar 17%`, `Ga verder met gratis versie`, `Gratis gebruiker`. Restore: `Aankopen herstellen` (both `paywall_restore` and `restore_purchases`). `Upgraden` / `Upgrade naar Pro` / `Upgrade om te ontgrendelen` use English `upgrade`. `Abonnement actief`. Store IAP names: `GymLogger X Pro eenmalig` € 44,99 · `GymLogger X Pro jaarlijks` € 19,99 · `GymLogger X Pro maandelijks` € 1,99 · `Support the developer` € 1,00 (English in the Dutch store; a gap for the owner).

#### Dutch App Store listing (checked 2026-11-19)

- Name: **GymLogger X: Training Tracker** (same as the English name).
- Subtitle: **Krachttraining & Sportschool** (English subtitle not re-fetched).
- Category: **Gezondheid en fitness**. Price **Gratis** with in-app purchases. Age 9+. iOS 17.6+. Size 232,7 MB. Languages: "Nederlands en 33 andere".
- Description is in Dutch (starts "Loop de gym in en weet precies wat je vandaag gaat tillen."; heads `VOLG EEN BEWEZEN SCHEMA`, `RUST OP ...`; says `kant-en-klare programma's`, `Smart Program Creator`, `RIR-doel (reps in reserve ...)`, `Pro`, `herhalingsbereik`). Release note is Dutch.

---

### 3. LiftLog (liftlog, source `CoreLift`, ID 6760043411)

#### Dutch coverage

| Catalog | Keys | `nl` present | `nl` translated | Identical to English |
|---|---|---|---|---|
| CoreLift/CoreLift/Resources/Localizable.xcstrings | 990 | 980 | 980 (99.0%) | 116 |
| CoreLift/CoreLift/Resources/AppShortcuts.xcstrings | 6 | 6 (each a `stringSet` of 3 to 4 phrasings) | 6 | 0 |
| CoreLift/CoreLift/Resources/InfoPlist.xcstrings | 4 | 2 | 2 | 0 |
| CoreLift/LiftLogWidgets/Resources/WidgetLocalizable.xcstrings | 137 | 137 | 137 | 14 |

(The `.claude/worktrees/` copies are ignored.) The 116 identical values are mostly program/routine names (`StrongLifts 5×5`, `Starting Strength (Rippetoe)`, `GZCLP`, `nSuns — Day 1 ...`), units and loanwords (`Sets`, `Volume`, `Superset`, `Deload`, `Beginner`, `RPE`, `Epley`).

**English-only gaps (10 keys without `nl` in the main catalog):** `Average`, `Best`, `Best run`, `By month`, `By weekday`, `min`, `Sessions in run`, `Weekly avg` (user-visible; the widget catalog has Dutch for them: `Gemiddelde`, `Record`, `Langste reeks`, `Per maand`, `Per dag van de week`, `Sessies in reeks`, `Gem./week`), plus the format-only `%@` and ` / %lld`. Also `CFBundleDisplayName` / `CFBundleName` have no `nl` (name stays "LiftLog"). The old name **CoreLift remains in 4 Dutch values:** `Toegang tot Gezondheid is uit. Schakel workouts in voor CoreLift via Instellingen › Gezondheid › ...`, `Berichtgeving staat uit. Schakel die in voor CoreLift via Instellingen › Berichtgeving.`, `Bewaar elke voltooide workout in Apple Gezondheid ... CoreLift leest je gezondheidsgegevens nooit.` and `Selecteer een CoreLift-reservekopie (.json) om te importeren.`

Permission prompts (Dutch, `translated`): `NSHealthShareUsageDescription` = `LiftLog leest je gegevens in Apple Gezondheid nooit. De app bewaart alleen je voltooide krachttrainingen, zodat ze meetellen voor je activiteitenringen.`; `NSHealthUpdateUsageDescription` = `LiftLog bewaart je voltooide krachttrainingen in Apple Gezondheid zodat ze meetellen voor je activiteitenringen. Je gezondheidsgegevens worden nooit gelezen.`

Siri / App Shortcuts (6 intents, 3 to 4 Dutch phrasings each, all `translated`): `Hoeveel heb ik deze week getild in ${applicationName}`, `Mijn volume van deze week in ${applicationName}`, `Bekijk mijn weekvolume in ${applicationName}`; `Log mijn set in ${applicationName}`, `Leg mijn set vast in ${applicationName}`, `Sla mijn set op in ${applicationName}`; `Start ${workout} met ${applicationName}`, `Begin ${workout} in ${applicationName}`; `Start mijn volgende workout met ${applicationName}`, `Volgende workout starten in ${applicationName}`; `Start mijn rusttimer in ${applicationName}`, `Zet de rusttimer aan in ${applicationName}`; `Wat is mijn reeks in ${applicationName}`, `Mijn ${applicationName} reeks`, `Hoeveel weken op rij in ${applicationName}`. One phrasing drops its preposition (`Begin mijn volgende ${applicationName} workout`), which Siri may not accept; `Mijn ${applicationName} reeks` is a bare noun phrase.

**Verdict: app is in Dutch: yes** (99.0% of the main catalog, widgets and Siri complete; 8 user-visible English fallbacks and 4 leftover "CoreLift" names).

#### Register

je/jij forms in 101 of 990 main values and 13 of 137 widget values, 0 u/uw (one `/u/ivysaur` Reddit handle in a program description). Examples: `Je gratis proefperiode kon niet worden gestart`, `Je traint meestal rond dit tijdstip — klaar voor de sessie van vandaag?`, `Kies wat op dit moment het beste past.` The paywall pitch is in the first person (`Betaal wat eerlijk voelt.`, `...helpen mij ...`). No mix.

#### Glossary

| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Tier Fair | `Fair` | `Eerlijk` | Store IAP: `Eerlijk`. |
| Tier Good | `Good` | `Goed` | Store IAP: `Goed`. |
| Tier Generous | `Generous` | `Gul` | **Flag:** store IAP is `Genereus`; `Gul` ("openhanded") reads fine but differs. |
| Tier Patron | `Patron` | `Beschermheer` | **Flag:** store IAP is `Mecenas`; `Beschermheer` is male-gendered and feudal. `Supporter` key = `Steuntje`. |
| Tier selection | `Select %@ tier at %@`; `Cancel and try a different tier` | `Kies %1$@-niveau voor %2$@`; `Annuleer en kies een ander niveau` | `niveau` for tier. |
| Pay what feels fair | `Pay what feels fair.`; `Most lifters pick this` | `Betaal wat eerlijk voelt.`; `Meest gekozen` | |
| One-time purchase | `One-time purchase`; `LiftLog is a one-time purchase. Every tier unlocks the same app ...` | `Eenmalige aankoop`; `LiftLog is een eenmalige aankoop. Elk niveau ontgrendelt dezelfde app ...` | `Pay %@ once` = `Eén keer %@ betalen`. |
| Free trial (7 days) | `Free Trial`; `%d days left in trial`; `Trial expired`; `No card. No trial trap. No auto-renew.` | `Gratis proefperiode`; `Nog %d dagen proefperiode`; `Proefperiode verlopen`; `Geen kaart. Geen proefval. Geen auto-verlenging.` | `proefval` is a coinage ("trial trap"); `auto-verlenging` is a calque of "auto-renew". |
| Restore Purchases | `Restore Purchases`; `Restore`; `Restore anytime` | `Aankopen herstellen`; `Herstel`; `Altijd te herstellen` | Infinitive button, noun `Herstel` for the short key. |
| Unlock | `Unlock LiftLog`; `Unlock to log new workouts` | `Ontgrendel LiftLog`; `Ontgrendel om nieuwe workouts vast te leggen` | |
| Family Sharing | `Family Sharing` | `Delen met gezin` | Apple's NL term. |
| Home tab | `Home` | `Start` | |
| Progress tab | `Progress` | `Voortgang` | `Progressed` = `Vooruitgang`; `Progression` = `Progressie`. |
| Workouts / Settings / History | `Workouts`; `Settings`; `History` | `Workouts`; `Instellingen`; `Geschiedenis` | **Cross-app:** `workout` here, `training` in GymLogger X. |
| Programs / Templates | `Programs`; `Templates`; `Browse Templates`; `Use This Program`; `Active Program` | `Programma's` (curly: `Programma’s`); `Sjablonen`; `Sjablonen bekijken`; `Dit programma gebruiken`; `Actief programma` | |
| Start a workout | `Start Workout`; `Start Empty Workout`; `Repeat Last`; `Repeat Recent` | `Workout starten`; `Lege workout starten`; `Laatste herhalen`; `Recente herhalen` | |
| Workout Complete | `Workout Complete` | `Workout voltooid` | |
| Set / Sets / Reps | `Sets`; `Reps`; `reps`; `Set %lld` | `Sets`; `Herh.`; `reps`; `Set %lld` | **Flag:** `Reps` = `Herh.` (abbreviation), `reps` stays English in 3 places, `herhalingen` in 14 values (three forms). Warm-up: `Add Warmup` = `Warming-up toevoegen`, `Warm-up set %lld` = `Warming-upset %lld`, `Add Timed Warmup` = `Tijdwarming-up toevoegen` (odd). |
| Superset / Giant set | `Superset`; `Giant Set` | `Superset`; `Reuzenset` | **Cross-app:** GymLogger X says `Giant set`. `Create Superset` = `Superset maken`. |
| Rest timer | `Rest timer`; `Start Rest Timer`; `Rest complete` | `Rusttimer`; `Rusttimer starten`; `Rust voltooid` | |
| Personal bests / PR | `Personal Bests`; `New Personal Bests`; `Personal record`; `PR`; `Closest to a PR` | `Persoonlijke records`; `Nieuwe records`; `Persoonlijk record`; `PR`; `Dicht bij een PR` | Widget `Best` = `Record`. |
| Estimated 1RM | `Estimated 1RM`; `Est. 1RM`; `1RM Formula` | `Geschat 1RM`; `Gesch. 1RM`; `1RM-formule` | Formula names (`Epley`, `Brzycki`) untranslated. |
| Progression scheme | `Double progression`; `% of training max`; `RPE / RIR`; `Training max` | `Dubbele progressie`; `% van trainingsmax`; `RPE / RIR`; `Trainingsmax` | |
| Deload | `Deload`; `Deload after`; `Deload to` | `Deload`; `Deload na`; `Deload naar` | |
| Muscle Coverage | `Muscle Coverage` | `Spierdekking` | `Coverage appears once you've logged some sets.` = `De dekking verschijnt zodra je wat sets hebt vastgelegd.` |
| Activity heatmap | `activity heatmap` | `activiteitenkaart` | Other apps: `Heatmap`. `Activity grid` = `Activiteitenraster`. |
| Training Grid (widget) | `Training Grid`; `Your training grid, GitHub style.` | `Trainingsraster`; `Je trainingsraster, GitHub-stijl.` | |
| Widgets | `Next Session`; `Momentum`; `Muscle Split`; `Training Grid` | `Volgende sessie`; `Momentum`; `Spierverdeling`; `Trainingsraster` | **Flag:** widget `Back` = `Terug` (body part "Rug" expected; `BACK` = `RUG` is right in caps). |
| Streak | `Streak`; `Training Streak`; `Check Training Streak`; `%lld week streak`; `Streak badge farm` | `Reeks`; `Trainingsreeks`; `Trainingsreeks opvragen`; `%lld weken op rij`; `Streakbadges` | **Flag:** `Streakbadges` keeps English, `%lld-week streak` = `Reeks van %lld weken` against `%lld week streak` = `%lld weken op rij`. |
| Recently Deleted | `Recently Deleted`; `Move to Recently Deleted` | `Recent verwijderd`; `Verplaats naar recent verwijderd` | |
| Export data | `Export Data (CSV)`; `Export Data (JSON)`; `Restore from Backup` | `Gegevens exporteren (CSV)`; `Gegevens exporteren (JSON)`; `Herstel uit reservekopie` | `backup` = `reservekopie`. |
| Bodyweight | `Bodyweight`; `Bodyweight & Measurements` | `Eigen lichaamsgewicht`; `Lichaamsgewicht en metingen` | `Eigen lichaamsgewicht` (exercise type) vs `Lichaamsgewicht`. |
| How To (exercise steps) | `How To` | `Uitvoering` | Good rendering. |
| Apple Health | `Apple Health` | `Apple Gezondheid` | |
| Siri & Shortcuts | `Siri & Shortcuts` | `Siri en Opdrachten` | Apple's NL name `Opdrachten`. MediaKit writes `Opdrachten en Siri`. |
| iCloud | none | none | LiftLog has no iCloud string; data stays on the phone. |

#### Paid tier names in the Dutch UI

No subscription and no Pro: four tiers of one purchase. In-app: `Eerlijk` / `Goed` / `Gul` / `Beschermheer` (+ `Steuntje` for the Supporter key); labelled `niveau`. Store IAP names (all prefixed `Volledige versie ·`): `Volledige versie · Eerlijk` € 9,99 · `Volledige versie · Goed` € 22,99 · `Volledige versie · Genereus` € 39,99 · `Volledige versie · Mecenas` € 44,99. Trial: `Gratis proefperiode` (7 days on the English site), `Nog %d dagen proefperiode`. `Eenmalige aankoop`, `Eén keer %@ betalen`, `Aankopen herstellen`, `Delen met gezin` (no `Pro`, no `Premium`, no monthly/yearly). **Flag (paywall):** `Strong Pro zou je $90 kosten over twee jaar. Hevy Pro $120.` is a competitor price claim in dollars shown to Dutch users (key `Strong Pro would cost you $90 over two years. Hevy Pro, $120.`).

#### Dutch App Store listing (checked 2026-11-19)

- Name: **LiftLog: Kracht & Gym Log**.
- Subtitle: **Sets, reps & krachtschema**.
- Category: **Gezondheid en fitness**. Price **Gratis** with in-app purchases. Age 4+. iOS 17.6+ (also Mac macOS 14.6+, visionOS 1.3+). Size 204,6 MB. Languages: "Nederlands en 43 andere".
- Description is in Dutch (starts "LiftLog vult het gewicht en de herhalingen van je vorige training alvast in, zodat elke set begint met het getal dat je moet verslaan. Je betaalt één keer en daarna nooit meer."; heads `EENMALIG BETALEN, JIJ KIEST DE PRIJS`, `GEMAAKT VOOR DE WERKSET`; says `persoonlijk record`, `Delen met gezin`, `abonnement`). The store text uses `training` where the app says `workout`.

---

### 4. MediaKit (mediakit, source `ClearCut`, ID 6761451361, iPhone and Mac)

#### Dutch coverage

| Catalog | Keys | `nl` present | `nl` translated | Identical to English |
|---|---|---|---|---|
| ClearCut/MediaKit/Localizable.xcstrings | 2583 | 2583 | 2583 (100%) | 182 |
| ClearCut/MediaKit/AppShortcuts.xcstrings | 6 | 6 (`stringSet`) | 6 | 0 |
| ClearCut/MediaKit/InfoPlist.xcstrings | 26 | 23 | 23 | 3 |
| ClearCut/MediaKitShareExtension/Localizable.xcstrings | 13 | 13 | 13 | 1 |

The identical values are formats, codecs, platform presets and font names (`HEVC`, `ProRes 422`, `Spotify (−14 LUFS)`, `iMessage (100 MB)`, `Helvetica`, `PNG`, `bottomLeft`, `Home`, `MediaKit Pro`, `Upgrade`). Real English left in the Dutch UI: the raw position values `bottom`, `bottomLeft`, `bottomRight`, `center`, `left`, `right`, `top`, `topLeft`, `topRight` (shown as such for watermark/caption position), the tab title `Home`, `Upgrade`, `Overlay X` / `Overlay Y`, and `Try-It` (kept as feature name in one string; `Try-It sample ready` = `Probeer-monster klaar`). The 3 missing InfoPlist keys are `CFBundleDisplayName`, `CFBundleName`, `NSHumanReadableCopyright` (name unchanged).

Permission prompts (Dutch): `NSPhotoLibraryAddUsageDescription` = `MediaKit bewaart bewerkte video’s en afbeeldingen in je fotobibliotheek.`; `NSSpeechRecognitionUsageDescription` = `MediaKit gebruikt spraakherkenning om audio en video naar tekst om te zetten wanneer je de tool Transcribeer gebruikt.` File-type names are localized (`PDF-document`, `Audiobestand`, `Stripboekarchief`, `E-book`, `Ondertitelbestand`).

Siri / App Shortcuts (6 intents, `stringSet`): `Comprimeer een video met ${applicationName}`, `Comprimeer een afbeelding met ...`, `Converteer een afbeelding met ...`, `Maak een ZIP met ...`, `Haal tekst uit een afbeelding met ...`, `Voeg pdf’s samen met ...`. The Dutch uses "met" (with), the English uses "with"; `Comprimeer een video` etc. are imperatives, natural for Siri. Pro intent phrases are all Dutch.

**Verdict: app is in Dutch: yes** (100% of Localizable, share extension, Siri phrases; 3 InfoPlist name keys by design).

#### Register

je/jij forms in 76 of 2583 main values (+ 2 of 13 share-extension values), 0 u/uw (the single `u` hit is the format code `%u`). The app is mostly short tool labels and error messages. Examples: `Onderteken met je vinger`, `Wijs de map naar een gedeelde Dropbox / iCloud / git-map ...`, `Je bestanden verlaten je Mac nooit`, `Geschikt voor Delen met gezin`. No mix.

#### Glossary

| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Free (tier) | `Free`; `Free — 5 tools available`; `MediaKit Free`; `Continue with Free Access` | `Vrij`; `Gratis — 5 tools beschikbaar`; `MediaKit Free`; `Doorgaan met gratis toegang` | **Flag (defect):** `Free` = `Vrij` ("free to move"); `Gratis` is used in other strings. `MediaKit Free` untranslated. |
| Pro | `MediaKit Pro`; `Upgrade to Pro`; `Go Pro for unlimited access + batch processing.` | `MediaKit Pro`; `Upgrade naar Pro`; `Ga Pro voor onbeperkte toegang + batchverwerking.` | `Media Info Pro` = `Media-info Pro`. |
| Free 3-day Pro access | `Free 3-day Pro access built in`; `^[%lld day] of free Pro access left` | `3 dagen gratis Pro-toegang inbegrepen`; `Nog %lld dag gratis Pro-toegang` / `Nog %lld dagen gratis Pro-toegang` | |
| Five free tools | `Free tier includes 5 unlimited tools forever. Pro unlocks the rest plus batch processing.` | `De gratis variant bevat 5 onbeperkte tools voor altijd. Pro ontgrendelt de rest plus batchverwerking.` | `tool(s)` kept as the word for tool. |
| Video Compress / Compress Video | `Compress Video`; `Compress` | `Video comprimeren`; `Comprimeer` | **Flag:** tool-name forms mix: imperative (`Comprimeer`, `Converteer`, `Stabiliseer`, `Normaliseer`, `Transcribeer`, `Splits`, `Vind duplicaten`, `Verwijder metadata`, `Herorden pagina's`, `Verwijder achtergrond`, `Wijzig grootte`, `Snijd bij`) and infinitive (`Video comprimeren`, `Inkorten`, `Samenvoegen`, `Redigeren`, `Versleutelen`, `Ondertekenen`, `Extraheren`, `Platmaken`). |
| Image Compress / Image Resize | `Compress Image`; `Resize` | `Afbeelding comprimeren`; `Wijzig grootte` | `Resize failed` = `Formaat wijzigen mislukt`; `Resize for the web` = `Formaat aanpassen voor het web` (three forms of "resize"). |
| Audio Convert | `Convert Image` (pattern) ; `Convert` | `Afbeelding converteren`; `Converteer` | |
| Trim | `Trim`; `Trim Timeline` | `Inkorten`; `Tijdlijn inkorten` | |
| Merge (video crossfade) | `Merge`; `Crossfade` | `Samenvoegen`; `Crossfade` | `Merge needs at least two clips` = `Samenvoegen vereist minstens twee clips`. |
| Stabilize | `Stabilize` | `Stabiliseer` | |
| Colour grade / LUT | `Color Grade`; `Color Grade (LUT)` | `Kleurgradatie`; `Kleurgradatie (LUT)` | **Flag:** `kleurgradatie` (tool) vs `kleurgrading` (description: `filmische kleurgrading`) and `grading`. |
| Auto Subtitle | `Auto Subtitle`; `Auto Subtitle + Translate`; `Try Auto Subtitle` | `Auto-ondertitels`; `Auto-ondertiteling + vertalen`; `Automatische ondertiteling proberen` | **Flag:** three forms (`Auto-ondertitels`, `Auto-ondertiteling`, `Automatische ondertiteling`); plus `Subtitle burn-in failed` = `Ondertitels inbranden mislukt`. |
| Transcribe | `Transcribe` | `Transcribeer` | |
| Normalize loudness | `Normalize`; `Normalize loudness` | `Normaliseer`; `Luidheid normaliseren` | `Loudness` = `Luidheid` (the term is `luidheid`, correct). |
| Noise reduce | `Noise Reduce`; `Noise sample` | `Ruis verminderen`; `Ruisvoorbeeld` | |
| Ringtone | `Ringtone` | `Beltoon` | |
| Remove BG | `Remove BG` | `Verwijder achtergrond` | |
| OCR | `OCR` | `OCR` | `Vision OCR` kept. |
| Smart Crop | `Smart Crop`; `Crop` | `Slim bijsnijden`; `Snijd bij` | |
| Collage / GIF Maker | `Collage`; `GIF Maker` | `Collage`; `GIF-maker` | |
| Find Duplicates / Smart Duplicate Finder | `Find Duplicates`; `Smart Duplicate Finder` | `Vind duplicaten`; `Slimme duplicaatvinder` | |
| Compare Takes | `Compare Takes`; `Compare Takes & Smart Duplicates` | `Vergelijk takes`; `Vergelijk takes & slimme duplicaten` | |
| PDF: Merge / Split / Reorder / Sign / Redact / Encrypt | `Merge`; `Split`; `Reorder Pages`; `Sign`; `Redact`; `Encrypt` | `Samenvoegen`; `Splits`; `Herorden pagina's`; `Ondertekenen`; `Redigeren`; `Versleutelen` | **Flag (wrong meaning):** `Redact` = `Redigeren` ("to edit"); `PDF redigeren`, `Rechthoeken redigeren`. Should be `Zwartmaken` or `Censureren`. `Sign with your finger` = `Onderteken met je vinger`. |
| Compression presets | `Screen` / `Ebook` / `Printer` / `Prepress` | `Scherm` / `E-book` / `Printer` / `Prepress` | `Ebook (150 DPI)` = `E-book (150 DPI)`; `Prepress (600 DPI)`. |
| Watermark / Page numbers | `Watermark`; `Page Numbers` | `Watermerk`; `Paginanummers` | |
| Flatten | `Flatten Form Fields` | `Formuliervelden platmaken` | `Flattening bakes form content permanently` = `Platmaken legt de formulierinhoud permanent vast`. |
| Archives and ebooks | `Extract`; `ZIP`; `BZIP2`; `EPUB Metadata` | `Extraheren`; `ZIP`; `BZIP2`; `EPUB-metadata` | `Extract audio` = `Audio extraheren`. |
| Strip Metadata | `Strip Metadata`; `Strip metadata (EXIF, GPS)` | `Verwijder metadata`; `Metadata verwijderen (EXIF, GPS)` | Imperative vs infinitive for the same tool. |
| Recipes | `Recipes`; `Delete Recipe`; `Browse Recipe Marketplace` | `Recepten`; `Recept verwijderen`; `Receptenmarktplaats bekijken` | Dutch `recept`; `Recipes — multi-step pipelines` = `Recepten — pijplijnen met meerdere stappen`, another string `meerstaps pipelines`. |
| Make It Fit | `Make It Fit`; `Make It Fit…` | `Passend maken`; `Passend maken…` | Not the English name; the site must decide whether to keep `Make It Fit`. |
| Queue / batch | `Queue`; `Add to Queue`; `Batch processing` | `Wachtrij`; `Aan wachtrij toevoegen`; `Batchverwerking` | `Process Queue` = `Verwerk wachtrij`; `Add this batch ...` = `Voeg deze batch toe aan de wachtrij`. |
| Library | `Library` | `Bibliotheek` | |
| Folder Automation (Mac) | `Folder Automation` | `Mapautomatisering` | `Folder automations need MediaKit Pro.` = `Mapautomatiseringen vereisen MediaKit Pro.` |
| Try-It samples (Mac) | `Try-It sample mode (⌘T)`; `Try-It sample ready` | `Try-It voorbeeldmodus (⌘T)`; `Probeer-monster klaar` | **Flag:** two renderings. |
| Run | `Run` | `Voer uit` | Site quotes `Voer uit`. |
| Saved space | `Saved %@`; `Saved` | `%@ bespaard`; `Bewaard` | `bewaard` for saved files, `bespaard` for space saved. |
| Shortcuts and Siri | `Shortcuts & Siri` | `Opdrachten en Siri` | App named `Opdrachten`. |
| Share sheet | `Share / Save to Files…` | `Deel / Bewaar in Bestanden…` | `iOS-deelmenu`. |
| Photos | `Photos`; `Save to Photos` | `Foto's`; `Bewaar in Foto’s` | Straight vs curly apostrophe in the same catalog. |
| Settings | `Settings`; `Reset All Settings` | `Instellingen`; `Reset alle instellingen` | |
| Your Plan (Settings) | `Your Plan` | `Je abonnement` | Lifetime holders see `Je abonnement`; `Manage subscription` = `Abonnement beheren` / `Beheer abonnement` (both). |
| Family Sharing | `Works with Family Sharing` | `Geschikt voor Delen met gezin` | Apple's NL term. |
| On-device / privacy | `On-device. Private. Forever yours when you go Lifetime.`; `Your Files Never Leave Your Mac` | `Op het apparaat. Privé. Voor altijd van jou met Lifetime.`; `Je bestanden verlaten je Mac nooit` | `op het apparaat` / `lokaal` (both used). |

#### Paid tier names in the Dutch UI

`MediaKit Pro` (not translated); `Pro` alone; plan labels `Maandelijks` / `Jaarlijks` (`Annual` key) / `Levenslang` (`Lifetime`); buttons `Koop levenslange toegang`, `Levenslange toegang krijgen`, `Abonneer op Pro`, `Abonneren — %@`, `Ontgrendel MediaKit Pro`, `Ontgrendel meer dan 150 tools`, `Upgrade naar Pro`. Trial: `%@ gratis proef`, `%@ gratis proberen · %@/mnd`, `%@ gratis proberen, daarna %@. Wordt automatisch verlengd tot opzegging — altijd opzegbaar in Instellingen.` and `%@ gratis proefperiode, daarna %@. ...` (**Flag:** three renderings of "free trial"; `Altijd opzegbaar` vs `Zeg op elk moment op`). Restore: `Herstel aankopen`, `Herstel aankoop`, `Aankopen herstellen`, `Herstellen` (four forms). The English site says "Free 3-day Pro access built in"; the app says `3 dagen gratis Pro-toegang inbegrepen`. Store IAP names: `MediaKit Pro maandabonnement` € 4,99 · `MediaKit Pro jaarabonnement` € 24,99 · `MediaKit Pro eenmalig` € 44,99.

#### Dutch App Store listing (checked 2026-11-19)

- Name: **MediaKit Comprimeer Converteer** (English store name differs: this is the Dutch-localised name using imperative verbs).
- Subtitle: **Video, Audio, Afbeelding & ZIP**.
- Category: **Diensten** (Apple's Dutch label for Utilities; iTunes returns `Utilities`). Price **Gratis** with in-app purchases. Age 4+. iOS 17.0+. Size 16,4 MB. Languages: "Nederlands en 11 andere".
- Description is in Dutch (starts "Een video verkleinen tot onder een uploadlimiet, of je locatie uit een foto halen voordat je hem plaatst."; heads `JE BESTANDEN BLIJVEN OP JE IPHONE`, `BEKIJK HET RESULTAAT VOORDAT JE HET BEWAART`; says `analyse-SDK`, `pdf's`, `Voer uit`). Release note is Dutch.

---

### 5. Millrace (millrace, source `thegame`, ID 6759511759)

(The number-title the game replaced is not written here; the Dutch catalog and the Dutch store text were checked and do not contain it.)

#### Dutch coverage

| Catalog | Keys | `nl` present | `nl` translated | Identical to English |
|---|---|---|---|---|
| thegame/thegame/Localizable.xcstrings | 333 | 333 | 333 (100%) | 10 |

The identical values: `Coach`, `Debug`, `Feedback`, `Game Center`, `Gameplay`, `Hint`, `Ladder`, `Level %lld`, `Score`, `Score: %lld` (all acceptable loanwords). No InfoPlist, AppShortcuts or widget catalog exists in the project, so there are no Dutch permission prompts or Siri phrases to check (the game asks for no system permission except optional Game Center sign-in). **Theme names** (`Studio Clay`, `Paper & Ink`, `Sakura Pastel`, `Amber`, `Heartwood`, `Concrete Studio`, `Sunset Dunes`, `Glacier Ice`, `Brushed Metal`, `Midnight Neon`, `Lido`, `Riviera`, `Agrumi`, `Hygge Hearth`, `Aurora Drift`, `Evergreen Noël`, `Classic`) and the chapter names appear in the catalog only as descriptions/chapter labels; the theme names themselves have no catalog key, so they stay English in the Dutch UI (consistent with the English site).

**Verdict: app is in Dutch: yes** (100% of the single catalog; `nl` code plain).

#### Register

je/jij forms in 34 of 333 values, 0 u/uw. Examples: `Je behoudt de pakketten die je al hebt — dit voegt alleen de rest toe.`, `Log in bij Game Center om prestaties en ranglijsten te bekijken.`, `Corrigeer fouten wanneer dat nodig is. Je krijgt er ook elke dag eentje gratis.` No mix.

#### Glossary

| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Campaign chapters | `Warm-up` / `Tactics` / `Pressure` / `Precision` / `Deep Water` / `Mastery` | `Opwarmen` / `Tactiek` / `Onder druk` / `Precisie` / `Diep water` / `Meesterschap` | No `Chapter` key; `Opwarmen` is a verb form, not `Warming-up`. |
| Level | `Level %lld` | `Level %lld` | `lijst met levels`, `onopgeloste level`. |
| Continue | `Continue` | `Doorgaan` | `Opens the next unsolved level` = `Opent het volgende onopgeloste level`. |
| Freeplay | `Freeplay` | `Vrij spel` | |
| Daily Challenge | `Daily Challenge`; `Daily challenge`; `Daily`; `Daily Best` | `Dagelijkse uitdaging`; `Dagelijkse uitdaging`; `Dagelijks`; `Dagelijkse beste` | `Dagelijkse beste` is a calque of "Daily Best". |
| Hint | `Hint` | `Hint` | `Dismiss tip` = `Tip sluiten`. |
| Undo | `Undo`; `10 Undos`; `Undo Tokens`; `Undo that move` | `Terugdraaien`; `10 keer terugdraaien`; `Terugdraaitegoeden`; `Die zet terugdraaien` | **Flag:** Apple's Dutch word is `ongedaan maken` (used in `%lld undos available` = `%lld keer ongedaan maken beschikbaar`, 2 values); the other 13 use `terugdraaien`. `Play daily to earn free undos.` = `Speel dagelijks om gratis terugdraaiingen te verdienen.` (`terugdraaiingen` is not a word). `Tokens added.` = `Tegoeden toegevoegd.` |
| Coaching notes | `Coaching notes`; `Coach` | `Coachnotities`; `Coach` | |
| Streaks / stats | `Current Streak`; `Longest Streak`; `Streak Rewards`; `Stats` | `Huidige reeks`; `Langste reeks`; `Reeksbeloningen`; `Statistieken` | `%lld-day streak: %lld undos` = `Reeks van %lld dagen: %lld keer terugdraaien`; `%lld-day streak: ..., claimed` = `..., geclaimd` (calque). |
| Best / best possible | `Best %lld moves`; `Best possible is %lld moves`; `Best Tile` | `Beste %lld zet` / `Beste %lld zetten`; `Beste oplossing is %lld zet` / `... zetten`; `Beste tegel` | `Best possible` → `Beste oplossing`. `Solved in %lld moves` = `Opgelost in %lld zet(ten)`; `Not solved` = `Niet opgelost`. |
| Moves / move limit | `%lld moves left`; `No moves left` | `Nog %lld zet` / `Nog %lld zetten`; `Geen zetten meer` | `zet` for move. |
| Tile / arrival cell | `%lld tiles arriving`; `Arrival 1`; `Tiles arrive here` | `%lld tegel onderweg` / `%lld tegels onderweg`; `Aankomst 1`; `Hier komen tegels aan` | `cell` = `vakje` (`16 vakjes`). `Blocked` = `Geblokkeerd`; `Tiles keep arriving at the marked cell. Block it and you lose.` = `Er blijven tegels aankomen op het gemarkeerde vakje. Blokkeer het en je verliest.` |
| Theme / theme packs | `Theme`; `Themes`; `Designer Pack 1`; `Summer Pack`; `Winter Pack` | `Thema`; `Thema's`; `Designerpakket 1`; `Zomerpakket`; `Winterpakket` | `Complete collection` = `Volledige collectie` (store IAP: `Complete collectie`); `Unlock All Themes` = `Alle thema's ontgrendelen`; `Restores your current theme` = `Zet je huidige thema terug`. |
| Tilt | `Tilt` | `Gekanteld` | A past participle where a label ("Kantelen") fits. |
| Game Center | `Leaderboards`; `Achievements` | `Ranglijsten`; `Prestaties` | |
| Accessibility | `Automatic` | `Automatisch` | `Show a directional pad to move tiles without swiping.` = `Toon een richtingspad om tegels te verplaatsen zonder te vegen.` (`richtingspad` for d-pad). |
| Sound / music / haptics | `Sound Effects`; `Music`; `Haptics` | `Geluidseffecten`; `Muziek`; `Haptische feedback` | |
| One-time purchases | `One-time`; `One-time purchases. No subscription. No ads, ever.` | `Eenmalig`; `Eenmalige aankopen. Geen abonnement. Nooit advertenties.` | **Cross-app:** `Eenmalige aankoop` (LiftLog, GymLogger X) / `Eenmalig`. |
| Restore | `Restore Purchases`; `Restore failed. Please try again.` | `Aankopen herstellen`; `Herstellen mislukt. Probeer het opnieuw.` | |
| Free | `Free · always yours` | `Gratis · altijd van jou` | |
| Privacy | `Privacy Policy` | `Privacybeleid` | |
| Settings | `Settings`; `Open Settings` | `Instellingen`; `Instellingen openen` | |

#### Paid tier names in the Dutch UI

No tiers or subscription: the game is free in full. Paid items are one-time theme packs (`Designerpakket 1`, `Designerpakket 2`, `Zomerpakket`, `Winterpakket`, `Volledige collectie`), and consumable undo bundles (`10 keer terugdraaien`, `50 keer terugdraaien`, `200 keer terugdraaien`) plus a tip `Steun de ontwikkelaar`. No trial. Restore: `Aankopen herstellen`. Store IAP names/prices: `Complete collectie` € 6,99 · `Designerpakket 1` € 1,99 · `Designerpakket 2` € 1,99 · `Zomerpakket` € 1,99 · `Winterpakket` € 1,99 · `10 keer terugdraaien` € 0,99 · `50 keer terugdraaien` € 2,99 · `200 keer terugdraaien` € 6,99 · `Steun de ontwikkelaar` € 1,99.

#### Dutch App Store listing (checked 2026-11-19)

- Name: **Millrace: Getallenpuzzel** ("Getallenpuzzel" = "number puzzle"; the English site calls it a tile-delivery puzzle: check with the owner).
- Subtitle: **64 levels, niets is toeval**.
- Category: **Bordspel** (Apple's Dutch label for Board games; iTunes returns `Games`). Price **Gratis** with in-app purchases. Age 4+. iOS 18.0+, iPhone and iPad. Size 313,1 MB. Languages: "Nederlands en 33 andere".
- Description is in Dutch (starts "Elk level in Millrace heeft een kortste oplossing, en een solver heeft die bewezen. Aan jou om hem te vinden."; says `bezorgpuzzel met tegels`, `zettenlimiet`, `hoofdstukken`). Release note Dutch.

---

## Cross-app terms (as the five apps write them in Dutch)

| Concept | Dutch used | Where it varies |
|---|---|---|
| Subscription | `abonnement` (`Abonnement actief`, `Je abonnement`, `Geen abonnement`) | Consistent. MediaKit store IAP: `maandabonnement` / `jaarabonnement`. |
| Lifetime | `Levenslang` (GymLogger X, MediaKit, EarnLock `Premium · Levenslang`), `Voor altijd` (EarnLock bare label) | EarnLock mixes both; store IAP says `eenmalig` (EarnLock, GymLogger X, MediaKit) and `Eerlijk/Goed/...` (LiftLog); Millrace `Eenmalig`. |
| Monthly / Yearly | `Maandelijks` / `Jaarlijks` | Identical in EarnLock, GymLogger X, MediaKit. |
| One-time purchase | `Eenmalige aankoop` (LiftLog), `Eenmalige betaling` (GymLogger X), `Eenmalig` / `Eenmalige aankopen` (Millrace) | Three wordings. |
| Free trial | `gratis proefperiode` (EarnLock, GymLogger X, LiftLog, MediaKit) | EarnLock `7 dagen gratis proberen`; MediaKit `gratis proef` and `gratis proberen`. |
| Restore Purchases | `Aankopen herstellen` (GymLogger X, LiftLog, Millrace, MediaKit), `Herstel aankopen` (EarnLock, MediaKit) | EarnLock and MediaKit use the imperative; MediaKit has four forms. |
| Free | `gratis` | MediaKit `Free` = `Vrij` (defect). |
| Pro / Premium | not translated: `Premium` (EarnLock), `Pro` (GymLogger X, MediaKit) | LiftLog and Millrace have none. |
| Upgrade | `upgraden`, `Upgrade` (English verb kept) | EarnLock, GymLogger X, MediaKit. |
| Sync / iCloud | `iCloud-synchronisatie`, `synchroniseren` (GymLogger X); `synchroniseren` (EarnLock `aankopen tussen apparaten te synchroniseren`) | LiftLog has no sync; MediaKit mentions `iCloud` only in file-import errors. |
| Apple Health | `Apple Gezondheid` (EarnLock, LiftLog, GymLogger X prompts), `Apple Health` (GymLogger X in-app, 10 values; EarnLock 1) | Apple's Dutch app is `Gezondheid`. |
| Screen Time | `Schermtijd` | EarnLock only; concept `schermtijd`. |
| Family Sharing | `Delen met gezin` (EarnLock, LiftLog, MediaKit) | Apple's NL term. |
| Widget | `widget`, `widgets` (EarnLock `Groot widget`, GymLogger X `Pro-widgets`) | Always English `widget`. |
| Settings | `Instellingen` | Identical in all five. |
| Export | `exporteren` (GymLogger X `Mijn gegevens exporteren` in EarnLock) | `Gegevens exporteren` (LiftLog, EarnLock). |
| Workout | `training` (GymLogger X: 391 values), `workout` (LiftLog: 65 values, Siri phrases), `workouts` (LiftLog tab) | Not the same word: the site must choose per app or one word for the site. `sessie` for a logged session. |
| Set | `set`, `sets` | Identical in GymLogger X, LiftLog; `Warming-upset`. |
| Rep | `herhaling`, `herhalingen` (GymLogger X); `Herh.`, `reps` (LiftLog) | Abbreviation and English `reps` in LiftLog and MediaKit-free text. |
| Giant set | `Giant set` (GymLogger X), `Reuzenset` (LiftLog) | Two words. |
| Streak | `Reeks` | `Streak-schilden` (EarnLock, one string), `Streakbadges` (LiftLog). |
| Undo | `terugdraaien` (Millrace), `ongedaan maken` (LiftLog, Millrace, Apple's term) | |
| Personal record | `persoonlijk record`, `PR` | `PR`/`PR's` (GymLogger X, LiftLog), `Record` widget (LiftLog, GymLogger X). |
| Rest timer | `Rusttimer` | Identical across apps; GymLogger X `Hartslag-rusttimer`. |
| Heatmap | `Heatmap` (GymLogger X, `Spier-heatmap`), `Activiteitskaart` (EarnLock), `activiteitenkaart` (LiftLog) | Three. |
| Privacy | `Privacy` (EarnLock label), `Privacybeleid` (EarnLock, Millrace), `Gegevens en privacy` (EarnLock) | `Privé` in MediaKit. |
| Shortcuts / Siri | `Opdrachten` (LiftLog `Siri en Opdrachten`, MediaKit `Opdrachten en Siri`) | Order differs. |
| Lock Screen | `Toegangsscherm` (EarnLock widgets) | Apple's term; correct. |
| Tool / feature | `tool` (MediaKit), `functie` (`Pro-functie`) | |
| Buttons / register | je-imperative (`Kies`, `Open`, `Verdien`) and infinitive (`Training starten`) | Both fine, mixed within each app. |

## Flags (app-side string bugs worth an issue)

1. **MediaKit:** `Free` = `Vrij` (should be `Gratis`); `Redact` = `Redigeren` (wrong meaning: use `Zwartmaken`/`Censureren`); tool names mix imperative and infinitive (`Comprimeer`/`Converteer`/`Stabiliseer`/`Splits` against `Inkorten`/`Samenvoegen`/`Versleutelen`); four forms of Restore Purchases and three of free trial; three forms of Auto Subtitle; raw position values `bottom`, `bottomLeft`, `center` etc. shown in English; `Make It Fit` = `Passend maken`; `Try-It` kept in one string and `Probeer-monster` in another; `Photos` apostrophes straight vs curly; Dutch store name `MediaKit Comprimeer Converteer` is a keyword string (check it with the owner).
2. **LiftLog:** 4 Dutch strings still say `CoreLift`; 8 user-visible English fallbacks in the main catalog (`Average`, `Best`, `Best run`, `By month`, `By weekday`, `min`, `Sessions in run`, `Weekly avg`); tier names `Gul`/`Beschermheer` against store `Genereus`/`Mecenas`; widget `Back` = `Terug` (should be `Rug`); paywall string `Strong Pro zou je $90 kosten over twee jaar. Hevy Pro $120.` (dollars, competitor price claim, shown to Dutch users); one Siri phrasing without its preposition (`Begin mijn volgende ${applicationName} workout`); `Streakbadges`, `proefval`, `auto-verlenging` are English or calques.
3. **GymLogger X:** `Gevorderd` means Intermediate in `program_level_intermediate` and Advanced in `creator_level_advanced` (and `Expert` for Advanced in the other table); tab title `Home` in English; `Apple Health` in 10 in-app strings against `Apple Gezondheid` in prompts; `Program` rendered as `Programma`, `Schema`, `trainingsschema`; Watch `LOG VOLGENDE SET` / `LOG GEWICHT EN HERHALINGEN` (English `LOG`), `Hartslag toegang geweigerd` (split compound), `calorieën & hartslag te zien` fragment; `Beste gewicht`; `BESTE WAARDE` (calque); program titles `Intermediate 5×5-ramp`, `Dumbbell Only Hypertrofie` (half English), `Push/Pull/Benen 3 dagen` vs `Push / Pull / Benen (6 dagen)`; store IAP `Support the developer` still English in the Dutch store (also in MediaKit-free: none).
4. **EarnLock:** five permission prompts (phone and Watch) are `needs_review`; `Kon Shadow Mode niet volgen` keeps English; `Shadow Mode` / `Schaduwmodus` / `schaduwweek` three forms; `Streak-schilden` vs `Reeks-schilden`; Lifetime is `Voor altijd` and `Levenslang`; `Koop Voor altijd` (capital V); `Premium nemen` for `Get Premium`; `Onbeperkt geblokkeerde apps`; `vergrendeld` vs `geblokkeerd`; `Reflectie­samenvatting` contains a soft hyphen (U+00AD); `Nood-ontgrendeling` should be closed; `planning` vs `schema` for schedules; `CFBundleDisplayName` / `CFBundleName` have no `nl`.
5. **Millrace:** `terugdraaien` (13 values) against `ongedaan maken` (2 values) for Undo, `terugdraaiingen` is not a word; `Gekanteld` for `Tilt`; `Dagelijkse beste`; `geclaimd`; the Dutch store name `Millrace: Getallenpuzzel` means "number puzzle" (owner to confirm; do not use on the site until confirmed).
6. **Siri:** GymLogger X has no Siri/App Shortcuts at all; EarnLock, LiftLog and MediaKit have complete Dutch phrases; Millrace has none (no catalog).
7. **Register is clean:** all five apps write je/jij, no u/uw, no mix. The site's je register matches the UI.


---

## Dutch glossary, batch 3: mockly, observa, pawza, rightsplit, shogiful

Method (checked 2026-11-19). Read-only. Source catalogs under `~/Downloads/` (`AppScreenMaker/`, `HealthLogger/`, `PetCare/`, `splitit/`, `shogi/`), every `.xcstrings` parsed as JSON with `python3`; locale key `nl` (Mockly checked for `nl`, `nl-NL`, `nl-BE`: none exists; no catalog has `nl-NL` or `nl-BE`, and no app has legacy `nl.lproj` folders). "Total" = keys with `shouldTranslate` not false and a non-blank key (stale keys counted; the non-stale figure is in brackets); "nl" = keys whose `nl` entry has a non-empty value (plural/substitution variations included); "needs_review" = value present but state `needs_review`; "identical" = `nl` value equal to the English value (mostly format-only keys, cognates such as "Hotel", "Camera", "Premium", brand names). Dutch values are copied verbatim (apostrophes and quotes as the catalog writes them). Register counts are rough regexes on the Dutch values: je-forms = `je / jij / jouw / jou / jezelf`; u-forms = `u / uw / uzelf` as pronoun (the time unit "u" for hours, as in "%lld u %lld min", is excluded by pattern). App Store data: iTunes lookup API (`country=nl&lang=nl_nl`) plus the `serialized-server-data` JSON of `apps.apple.com/nl/app/...` (Safari UA, `Accept-Language: nl-NL`, redirects followed; Shogiful's page returned 429 once and was read after a 45 s wait; all five pages were read). The listing page also prints the seller's personal name; it is not copied. Store prices print `€` + NBSP (U+00A0) + amount with a decimal comma (`€ 3,99`) and are reference only: the site prints prices from the catalog / `MASTER-prices.csv`. The Dutch App Store labels Family Sharing **Delen met gezin**, the Lock Screen **toegangsscherm**, the Home Screen **beginscherm**.

## Summary

| App | Main catalog `nl` | Extensions / other catalogs | InfoPlist / permissions | Register | Verdict |
|---|---|---|---|---|---|
| Mockly | **0/333: no Dutch locale at all** (10 languages: de, en, es-ES, es-MX, fr, ja, ko, pt-BR, tr, zh-Hans) | none | InfoPlist 0/4 | n/a | **no, the app is English-only for the Netherlands** |
| Observa | 6684/6684 have a value (6516/6516 non-stale); 12 `needs_review` (all `insight_signal_*`) | Watch 477/477, Widgets 403/403, AppShortcuts 14/15 (Siri phrase "Log water in ${applicationName}" has no `nl`; 4 more `needs_review`) | app 5/5, watch 5/5 | **je/jij about 960 strings, u/uw about 490: a hard mix** (flag O1) | **yes** (no English left in prose; one missing Siri phrase) |
| Pawza | 1322/1323 (the one gap is the format key `%@`); 15 stale | AppShortcuts 4/4 (1 identical to English); widgets share the main catalog | **none**: no InfoPlist catalog; camera and photo-library prompts are English build settings | **je/jij** (135), 2 `u` strings only in a vet e-mail template | **yes**, with the two permission prompts in English |
| RightSplit | 499/499 (411/411 non-stale; 88 stale) | Widgets 376/376, Share 3/3, SplititKit 65/65 | InfoPlist 5/5 | **je/jij** (75), no u/uw | **yes**; Siri spoken phrases are English only (no AppShortcuts catalog) |
| Shogiful | 3751/3751 (3738 non-stale); 1 empty value (`dashboard.accuracy %lld`) | none | InfoPlist 0/2 (display and bundle name only; the app requests no permissions) | **je/jij** (781), no u/uw | **yes** |

Keys without `nl` in the main catalogs: Pawza `%@` (format only). The Dutch store names and subtitles are in each app's section and in "Cross-app terms".

---

### 1. Mockly (`mockly`, source `AppScreenMaker/`, ID 6756589122, macOS)

### Dutch coverage

- `AppScreenMaker/Resources/Localizable.xcstrings`: 333 keys, **0 with a Dutch value**. The catalog holds 10 languages: de, en, es-ES, es-MX, fr, ja, ko, pt-BR, tr, zh-Hans. There is no `nl`, `nl-NL` or `nl-BE`.
- `AppScreenMaker/InfoPlist.xcstrings`: 4 keys, 0 in Dutch (`CFBundleDisplayName`, `CFBundleName`, `Mockly Project`, `NSHumanReadableCopyright`).
- No extensions, no Siri phrases, no widgets, no permission prompts, no `.lproj` files.
- Register: not applicable (no Dutch text).
- **Verdict: app is in Dutch: no.** A Dutch user runs Mockly in English (macOS falls back to English); the Dutch site page must not promise a Dutch interface and should say the interface is in English, German, French, Spanish, Portuguese, Turkish, Japanese, Korean and Chinese. The Dutch store page agrees: the language list reads "Duits, Engels, Frans, Japans, Koreaans, Portugees, Spaans, Turks, Vereenv. Chinees" ("Duits en 8 andere"), no Nederlands, and the description is the English text.
- The "50 languages" claim on the site refers to the App Store locales Mockly can build screenshots for, not to the app's own interface. Dutch is one of those App Store locales; keep that distinction in the Dutch wording.

Flags
- **M1 (no Dutch UI):** no Dutch locale in the app or in InfoPlist. Not an error for the page, but the Dutch page must say the interface is not Dutch.
- **M2 (store metadata not localized):** the Dutch store page shows the English description and no subtitle (see below).
- **M3 (translation packs):** the credit packs exist in the UI (Settings → Buy More) but are not on sale (MISSING_METADATA in App Store Connect, per the blueprint); the Dutch store page lists no in-app purchases either.

### Glossary

No Dutch UI strings exist. The table lists the English UI strings the English page mentions (all checked to exist in the catalog unless noted); the Dutch column is empty. On the Dutch page write plain Dutch and put the English button name in quotes where the page names a button, because the user sees the English string.

| English term on site | English UI string (key) | Dutch UI string | Note |
|---|---|---|---|
| Upload to App Store Connect | `Upload to App Store Connect` | none (English) | button |
| App Store Connect credentials | `App Store Connect Credentials` / `API Credentials` / `Delete Credentials` | none | settings section |
| Issuer ID / Key ID / .p8 key | `Issuer ID` / `Key ID` / `Import .p8 File` | none | |
| API key (bring your own) | `API Key` / `Own API Key` | none | |
| AI translation | `AI Translation` / `AI Translate` / `Translate All` / `Bulk Translations` / `AI Integration` | none | |
| Provider | `Provider` / `Default Provider` | none | OpenAI, Anthropic, Google are not catalog strings |
| Localization panel | `Localizations` / `Languages` / `Target Languages` / `Source Language` / `Add Language` | none | |
| Link-to-source switch | `Linked to source` | none | |
| Device models | `Devices` / `Device Style` / `Model` | none | the style names Realistic, Clay, UI Only are not catalog keys (not localizable in any language) |
| Artboard | `Artboard` / `Artboards` | none | |
| Export / Save images | `Export` / `Save Images` | none | |
| Text blocks / captions | `Text Block` / `Text Blocks` / `Text Editing` | none | |
| Copy Style | `Copy Style` | none | |
| CSV import/export | `Import CSV` / `Export CSV` | none | |
| Do not translate | `Do not translate` | none | per-block flag |
| Pages / Layers / Background | `Pages` / `Layers` / `Background` | none | |
| Camera / Lighting / Perspective | `Camera` / `Lighting` / `Perspective` / `Orthographic` | none | |
| Device Overflow | `Device Overflow` | none | |
| macOS Keychain | `Your API key is stored in the macOS Keychain. …` | none | Apple's Dutch name is "Sleutelhanger" (for `nl-apple-terms.md`) |
| Translation packs (IAP) | `Translation Packs` / `Translation Credits` / `Buy More` / `Restore Purchases` | none | M3 |
| Help & Feedback | `Help & Feedback` | none | |
| Powered by Claude | `Powered by Claude for high-quality screenshot localization.` | none | |
| Templates / Render styles / Percentage layout | no UI string | no UI string | |

### Paid tier names in the Dutch UI

Mockly is a paid app (one-time purchase, no tiers, no subscription). The only purchase UI is the translation-pack sheet, English only for the Netherlands. No Dutch IAP display names exist.

### Dutch App Store listing (https://apps.apple.com/nl/app/mockly-screenshot-maker/id6756589122, checked 2026-11-19)

- Name: **Mockly: Screenshot Maker** (same as English; lookup `trackName`).
- Subtitle: **none shown**. The page header line reads "Ontwikkelaarstools" (the category label, shown when there is no subtitle).
- Category: **Ontwikkelaarstools** (English "Developer Tools"). Price **€ 14,99** (paid). Age 4+. Size 34,9 MB. Compatibility "Vereist macOS 14.0 of nieuwer." (Mac only).
- In-app purchases: none listed.
- Talen: 9 (Duits, Engels, Frans, Japans, Koreaans, Portugees, Spaans, Turks, Vereenv. Chinees), **no Nederlands**.
- Description: **English** (starts "You finished the app. Now the store wants screenshots for every device size and every language…"). No Dutch vocabulary to extract.

---

### 2. Observa (`observa`, source `HealthLogger/`, ID 6757438990)

### Dutch coverage

- Main `HealthLogger/Localizable.xcstrings`: 6684 keys (6516 non-stale), all with an `nl` value; 6675 translated, **12 `needs_review`** (values present): `insight_signal_active_energy` → "Actieve energie", `insight_signal_bedtime_consistency` → "Bedtijdconsistentie", `insight_signal_morning_hrv` → "Ochtend-HRV", `insight_signal_readiness` → "Gereedheid", `insight_signal_recovery_score` → "Herstelscore", `insight_signal_respiratory_stability` → "Ademhalingsstabiliteit", `insight_signal_sleep_duration` → "Slaapduur", `insight_signal_sleep_score` → "Slaapscore", `insight_signal_spo2_stability` → "Stabiliteit bloedzuurstof", `insight_signal_steps` → "Stappen", `insight_signal_strain` → "Trainingsbelasting", `insight_signal_training_load` → "Trainingsbelasting". 227 values are identical to English: almost all format-only, brand or cognate (HRV, REM, ECG, RMSSD, pNN50, Premium, "Body Mass Index"); the only real English left in is `Mocha Espresso`, `30/90/365 trends` ("trends" is also Dutch) and the format key `rhythm_cell_level`. No sentence is half English.
- Watch `ObservaWatch/Localizable.xcstrings`: 477/477 (51 identical, mostly units, "HIIT", "Premium"). Widgets `ObservaWidgets/Localizable.xcstrings`: 403/403 (49 identical).
- `AppShortcuts.xcstrings`: 15 keys, 14 with an `nl` value (10 translated, 4 `needs_review`: "Mijn ochtendcheck-in loggen in ${applicationName}", "Moet ik vandaag trainen volgens ${applicationName}?", "Wat was mijn slaapscore in ${applicationName}?", "Wat is mijn gereedheid in ${applicationName}?"). **English-only gap: `Log water in ${applicationName}` has no `nl` entry at all.** The other Siri phrases: "Kan ik vandaag trainen volgens ${applicationName}?", "Hoe heb ik geslapen volgens ${applicationName}?", "Hoe is mijn herstel in ${applicationName}?", "Hydratatie loggen in ${applicationName}", "Ochtendcheck-in in ${applicationName}", and the shortcut titles "${applicationName} check-in", "${applicationName} water loggen", "${applicationName} gereedheid", "${applicationName} slaap", "${applicationName} trainingsadvies". "volgens ${applicationName}" is a loose rendering of "in ${applicationName}".
- `InfoPlist.xcstrings` (app and watch): 5/5 each in Dutch. `NSHealthShareUsageDescription`: "Observa leest je gezondheidsgegevens om inzichten te tonen over slaap, hart, activiteit en herstel. Alle gegevens worden op je apparaat verwerkt en nooit geüpload."; `NSHealthUpdateUsageDescription`: "Observa slaat gezondheidsgerelateerde invoeren op in Apple Gezondheid, zodat je gegevens op één plek blijven."; `NSSiriUsageDescription`: "Observa gebruikt Siri zodat je je gereedheids- of slaapscore kunt opvragen en hydratatie of je ochtendcheck-in met je stem kunt vastleggen." The permission prompts are Dutch and je-form; they say "Apple Gezondheid" while the app body says "Apple Health" (flag O3).
- **Verdict: app is in Dutch: yes** (all user-visible parts; 12 insight labels and 4 Siri phrases `needs_review`, 1 Siri phrase missing).

### Register

- Dutch values: je/jij/jouw about **960** of 7588 values across main, watch, widgets, InfoPlist and shortcuts (main alone 917); u/uw about **490** (all in main). **Mixed: yes (flag O1).** The mix is not by screen: the onboarding headline `onboarding_welcome_headline` is "Begrijp wat uw lichaam u vertelt", `onboarding_focus_headline` "Wat is voor u het belangrijkst?", while the same flow's `trends_building_title` is "Je basislijn wordt opgebouwd". The insight and explainer sentences in the long English-keyed strings are mostly u/uw ("HRV ligt binnen uw gebruikelijke bereik.", "Uw basislijn", "Uw slaapdoel", "Begrijp uw slaapkwaliteit"); the newer snake_case keys, Watch and widgets, InfoPlist and the coaching "guidance_*" strings are je. Adjacent pair in one screen family: `Your Baseline` → "Uw basislijn" vs `Building your baseline` → "Je basislijn wordt opgebouwd"; `All Premium features are unlocked for your first 7 days.` → "Alle Premium-functies zijn ontgrendeld tijdens uw eerste 7 dagen." vs `onboarding_paywall_free_trial_badge` "7 dagen gratis".
- **Verdict: je/jij is the site register; quote only the je strings.** Do not quote any u/uw string. The `needs_review`-free Watch/widget catalogs are clean je.

### How the Dutch UI labels HRV and sleep stages

- **HRV** is "**HRV**" (key `HRV`, `Advanced HRV` → "Geavanceerde HRV", `Morning HRV`, widget titles); long form `Heart Rate Variability` → "**Hartslagvariabiliteit**". Never "RMSSD" as the headline metric. House rule (Apple Health HRV is SDNN): the Dutch UI mentions SDNN in 3 explanatory strings only: "De standaarddeviatie van NN-intervallen (SDNN) weerspiegelt je algehele hartslagvariabiliteit uit alle bronnen — zowel sympathisch als parasympathisch. …", "De autonome balansindex (RMSSD/SDNN-verhouding) benadert …", "De verhouding tussen RMSSD en SDNN benadert …". RMSSD appears in 19 values (ECG path and the autonomic-balance ratio). The Dutch UI never labels the headline HRV "(SDNN)", and neither should the site; say SDNN only in the sentence about what Apple Health records.
- **Sleep stages** (`Sleep Stages` → "**Slaapstadia**"): Awake → "**Wakker**" (`Awake Time` → "Wakkere tijd"), **Core** → "**Kern**", Deep → "**Diep**" (`Deep Sleep` → "Diepe slaap"), REM → "**REM**" (`REM Sleep` → "REM-slaap"), Light (Watch) → "Licht". "Kern" is consistent with how Apple Health labels Core in Dutch. Variants for "stages": "Slaapstadia" (5 values, main), "slaapfase/slaapfasen" (26 values: widgets `widget.breakdown.sleepStages` "Slaapfases", `widget.desc.sleepBreakdown` "Slaapfasen van afgelopen nacht in één oogopslag.", store description "slaapfasen"). The site should pick one (store and widgets say fase; the main app says stadia).
- `Sleep Score` → "**Slaapscore**" (one word). `Sleep Debt` → "**Slaapschuld**" (27 values) vs "slaaptekort" (11 values, e.g. `Your body tracks sleep debt biologically…` → "Je lichaam houdt slaaptekort biologisch bij"); `Moderate Debt` → "Matige schuld" (calque; drops "slaap").

### Glossary

| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Tab: Sleep | `Sleep` | Slaap | tab bar: Sleep, Recovery, Heart, Patterns, More |
| Tab: Recovery | `Recovery` | Herstel | |
| Tab: Heart | `Heart` | Hart | |
| Tab: Patterns | `Patterns` | Patronen | Watch domain tab `watch.domain.patterns` / `watch.insights.patterns` → "patronen" (lowercase, defect O9) |
| Tab: More | `More` | Meer | |
| Readiness | `Readiness` | Gereedheid | **O2:** "gereedheid" 107 values vs "paraatheid" 55 values in prose (`Moderate Readiness` → "Matige paraatheid", "Lage paraatheid wijst op opgehoopte belasting"). Store description says "Gereedheid", store subtitle says "Paraatheid". Use **Gereedheid** |
| Readiness score | `Readiness Score` | Gereedheidsscore | "out of 100": `widget.a11y.outOf100` "%1$@ van 100" |
| Readiness bands | `readiness_ready` / `readiness_moderate` / `readiness_low` | Gereed / Matig / Laag | site: Ready, Moderate, Low; widget bands `widget.band.*` use Goed / Gemiddeld / Hoog / Laag / Zeer laag, `widget.bandStatus.*` GOED / REDELIJK / UITSTEKEND / LAAG: "Moderate" is "Matig" in the app and "Gemiddeld" in widgets |
| Sleep Score | `Sleep Score` | Slaapscore | |
| Stress | `Stress` | Stress | `widget.title.stressState` "Stresstoestand", `outcome_stress_level` "Stressniveau", `widget.breakdown.stressDrivers` "Stressfactoren", watch `watch.why.title.stress` "Waarom dit stressniveau?". Site "Low, Moderate, or High" = Laag / Matig / Hoog |
| Today's Plan | `Today's Plan` | Plan voor vandaag | also `Today's Plan. %@. %@` → "Plan van vandaag. %@. %@" (two wordings) |
| Training call | `Should I train today?` | Moet ik vandaag trainen? | short: `Train today?` → "Vandaag trainen?"; `${applicationName} training call` → "${applicationName} trainingsadvies"; Siri "Kan ik vandaag trainen volgens ${applicationName}?"; Watch tab `watch.tab.train` "Trainen" |
| Training call verdicts | `widget.train.verdict.push` / `.maintain` / `.recover` / `.rest` / `.unavailable` | Doorpakken / Onderhouden / Herstel / Rust / Te weinig | site: Push, Maintain, Recover, Rest; store description "Doorpakken, Onderhouden, Herstel of Rust"; spoken (Watch) "Vandaag lijkt een goede dag om door te zetten." / "Vandaag lijkt een onderhoudsdag." / "Vandaag lijkt een rustigere dag." / "Vandaag lijkt een rustdag."; `guidance_category_maintain` → "Stabiel"; `guidance_category_explore` → "sterk" (en "Strong", lowercase, defect O10) |
| Why this score? | `why.action.title` / `why.title.readiness` | Waarom deze score? | `why.title.sleep` "Waarom deze slaapscore?", `why.title.stress` "Waarom dit stressniveau?"; Watch action `watch.action.whyThis` → "Score uitgelegd" (store description quotes "Score uitgelegd") |
| Building your baseline | `Building Your Baseline` / `Building your baseline` | Je basislijn wordt opgebouwd | `Baseline` → "Basislijn" (138 values) vs "referentie…" (49 values, e.g. "referentiebereik", "Referentie"): **O4**; `Your baseline` → "Uw basislijn" (u). Widgets: "Gebruikelijk bereik" / "Boven het normale" / "Je bereik wordt geleerd" |
| Usual range | `Typical range` / `Your usual range` | Typisch bereik / Gebruikelijk bereik | Watch `Typical range` → "Typisch bereik", `watch.metric.typicalRange` → "Gebruikelijk bereik": two words for one concept |
| Confidence | `Confidence` | Betrouwbaarheid | "Patterns … confidence label" |
| Adjust Sleep | `Adjust Sleep` | Slaap aanpassen | `Adjusted by you` → "Zelf aangepast" |
| Sleep source | `Sleep Source` | Slaapbron | `No sleep sources found in Apple Health yet.` → "Nog geen slaapbronnen gevonden in Apple Health." |
| Sleep Quality (four factors) | `Sleep Quality` / `Continuity` / `Efficiency` / `Duration` | Slaapkwaliteit / Continuïteit / Efficiëntie / Duur | `Sleep Efficiency` → "Slaapefficiëntie" |
| Time in bed | `Time in Bed` | Tijd in bed | `In Bed` → "In bed" |
| Sleep debt | `Sleep Debt` | Slaapschuld | O5: slaapschuld 27 vs slaaptekort 11; `Moderate Debt` → "Matige schuld" |
| Sleep goal | `Your Sleep Goal` | Uw slaapdoel | `sleep goal` in prose "je slaapdoel" |
| Bedtime reminder | `Bedtime Reminders` | Bedtijdherinneringen | `Bedtime` → "Bedtijd"; `Wake Time` → "Wektijd"; wind-down: `guidance_action_bedtime_title` "Ontspanningsherinnering" |
| Chronotype | `Chronotype Analysis` | Chronotype-analyse | Morning lark `chronotype_morning_lark` → "Ochtendmens", Night owl → "Avondmens", Intermediate `chronotype_intermediate` → "Intermediair chronotype"; store "ochtendmens, avondmens"; `chronotype_schedule_too_variable` "Slaapschema te variabel" |
| Resting heart rate | `Resting Heart Rate` / `RHR` / `Resting HR` | Rusthartslag | **O6:** "rusthartslag" 82 vs "rustpols" 34 (`resting heart rate` → "rustpols"); Watch `Resting HR` → "Rusthartslag" |
| Sleep heart rate / overnight | `sleep HR` prose | slaaphartslag | |
| HRV | `HRV` | HRV | see section above; `HRV Trends` family; "HRV-niveau" |
| Heart rate variability | `Heart Rate Variability` | Hartslagvariabiliteit | |
| Functional Age | `functional_age_title` / `Unlock Functional Age` | Functionele leeftijd | `Meet your Functional Age` → "Maak kennis met je functionele leeftijd"; Watch locked item `watch.locked.functionalAge` "Functionele leeftijd" |
| Advanced HRV | `Advanced HRV` | Geavanceerde HRV | |
| ECG history | `ECG History` | ECG-geschiedenis | `ECG Recording` → "ECG-opname", `ECG Recordings` → "ECG-opnames"; `Sinus Rhythm` → "Sinusritme"; `Atrial Fibrillation` → "Atriumfibrilleren"; ECG strings sometimes use u ("Raadpleeg …") |
| Autonomic balance | `Autonomic Balance` | Autonome balans | |
| Heart-rate zone detail | `Heart Rate Zones` | Hartslagzones | `Zone distribution` → "Zoneverdeling"; Zone 2 "Zone 2-wandeling", "Z2" |
| Cardio fitness / VO₂ max | `Cardio Fitness` / `VO₂ Max` | Cardioconditie / VO₂ Max | prose also "cardiofitheid" ("Functionele leeftijd verandert langzaam. Veranderingen in cardiofitheid …"): two words |
| Trends & Analysis | `trends_hub_title` | Trends en analyse | `See Full Analysis` / `View Full Analysis` → "Volledige analyse bekijken"; `Trend` → "Trend"; `Monthly Trend` "Maandtrend" |
| Trend periods | `7 Days` / `7-Day Trend` / `7-day trends` | 7 dagen / 7-daagse trend / 7-daagse trends | also "7-dagentrends", "7-dagenvergelijking", "7-daags afgevlakt verloop": three compound styles for "7-day" |
| Explainers | `Unlock Metric Explainers` | Uitleg bij metingen ontgrendelen | |
| Patterns | `Patterns` | Patronen | `Why am I seeing this?` → "Waarom zie ik dit?"; `Insights` → "Inzichten"; `Insight` → "Inzicht" |
| Training load | `Training Load` | Trainingsbelasting | acute/chronic: "Acute belasting" / "chronische belasting"; widget `widget.metric.strainRatio.name` "Belastingsratio" (en "Load Ratio") |
| Monotony & Strain | `Monotony & Strain` | Monotonie en belasting | **O7:** `Strain` → "Belasting" and `Load` → "Belasting": two English terms collapse into one Dutch word; `widget.title.strainMonotony` → "Belasting en monotonie" |
| Load Trends | `Load Trends` | Belastingstrends | |
| Training Status | `Training Status` | Trainingsstatus | |
| Effort Score | `Effort Score` | Inspanningsscore | Watch `watch.workout.effort` → "Inspanning"; "from 0 to 100" |
| Personal Records | `Personal Records` | Persoonlijke records | |
| Workout Replay | `Workout Replay` | Trainingsherhalig | **O8 typo:** "Trainingsherhalig" (3 values: `Workout Replay`, `Unlock Workout Replay` "Ontgrendel trainingsherhalig", …); elsewhere "Herhaal deze training", "Herhaal je trainingen", `Unlock Replay` → "Ontgrendel herhaling": use "Trainingsherhaling" |
| Workouts / workout | `Workouts` / `Workout` | Trainingen / Training | "workout" appears in 23 values too ("workouttypen", "Persoonlijke records voor alle workouttypen") |
| Workout report as PDF | `Share as PDF` / `Share as PDF (Premium)` | Delen als PDF / Delen als PDF (Premium) | export: `Export Report` "Rapport exporteren"; `export_paywall_bullet_formats` "PNG en PDF, zonder watermerk"; `report_watermark` "Gemaakt met Observa" |
| Themes (14) | `Theme` / `More Themes` | Thema / Meer thema's | |
| Apple Watch app | `watch.tab.browse` / `.log` / `.train` | Bladeren / Loggen / Trainen | `watch.empty.title` "Nog niets"; `watch.freshness.stale` "Vandaag niet gesynchroniseerd"; `watch.locked.premiumOnIPhone` "Premium op iPhone" |
| Morning check-in | `Morning Check-In` / `Daily Check-In` | Ochtendcheck-in / Dagelijkse check-in | Watch `watch.action.checkIn` → "Ochtendcheck" and complication title `watch.complication.checkIn.title` → "Check": **O11** (ochtendcheck / ochtendcheck-in / check-in); `trends_count_format` "%d checks"; watch `watch.checkIn.progress` "Vraag %1$lld van %2$lld" |
| Water logging | `Log water` / `Hydration` | Water loggen / Hydratatie | Watch `watch.action.logWater` → "Water loggen"; `Water intake` → "Waterinname"; `widget.metric.hydration.short` → "Water"; logging verb: "loggen" (27 values) vs "vastleggen" |
| Widgets: Home / Lock Screen | `widget.archetype.*` | Focus / Raster / Stapel / Trend / Overzicht / Inzicht / Folio / "Meting op toegangsscherm" | widget kinds (`.title`): Focus, Grid "Raster", Stack "Stapel", Trend, Breakdown "Overzicht", Insight "Inzicht", Folio "Folio", Lock Screen Metric "Meting op toegangsscherm"; descriptions e.g. "Eén meting, groot in beeld. Jij kiest welke." Lock Screen = "toegangsscherm" (6 values), Home Screen = "beginscherm" ("Kies hoe Observa op je beginscherm verschijnt.") |
| Siri | AppShortcuts | see coverage | |
| Live Activities | no catalog key (system strings) | no UI string | |
| Apple Health | `Apple Health` | Apple Health | **O3:** main strings "Apple Health" (64 values, "Apple Health-machtigingen", "Open Apple Health-machtigingen"), InfoPlist "Apple Gezondheid" (6 values). Apple's Dutch app name is "Gezondheid" |
| Privacy & Permissions | `privacy_settings_section_title` | Privacy en machtigingen | `Privacy` → "Privacy" |
| Delete All Data | `Delete All Data` | Alle gegevens verwijderen | "Gegevens in Apple Health worden niet beïnvloed" |
| Restore from Backup | `store_restore_row_title` | Herstel van back-up | `store_restore_confirm_title` "Deze back-up herstellen?"; `store_restore_done_title` "Back-up hersteld" |
| Cycle context | `Cycle Context` | Cycluscontext | `Menstrual Cycle` → "Menstruatiecyclus" (English page does not cover cycle tracking) |
| Settings | `Settings` | Instellingen | |
| Coaching / daily coaching note | `Coaching` / `Daily coaching note` | Begeleiding / Dagelijkse coachingnotitie | store: "dagnotitie"; "Coach" is Dutch-usable |

### Paid tier names in the Dutch UI

- Title: **Premium** (`Premium`, `PREMIUM`, `onboarding_paywall_premium`, Watch `Premium`). The word "Pro" is not used. Compounds: "Premium-functies", "premiumtoegang"/"premium-toegang" (both in the same catalog: `Your premium access has been restored.` → "Je premium-toegang is hersteld." vs `Your premium access comes from a Family Sharing organizer.` → "Je premiumtoegang komt van een organisator van Delen met gezin."), "premium-abonnementsopties" (O12: three spellings).
- Period labels: **Maandelijks** (`Monthly`, `pricing_label_monthly`), **Jaarlijks** (`Yearly`, `pricing_label_yearly` → "Jaarlijks (beste waarde)"), **Levenslang** (`Lifetime`); CTAs: `onboarding_paywall_monthly_cta` "Start maandabonnement", `onboarding_paywall_yearly_cta` "Start jaarabonnement", `Start Monthly Plan` "Maandplan starten", `Start Yearly Plan` "Jaarplan starten", `onboarding_paywall_lifetime_cta` "Ontgrendel levenslange toegang", but `Unlock Lifetime Access` → "Ontgrendel Lifetime Access" (English left in, O13). `Plan` → "Abonnement". `%@/month` → "%@/maand", `%@/year` → "%@/jaar". Best value: `Best Value` / `Best value` → "**Beste waarde**" (calque of "Best value"; Shogiful says "BESTE KEUS" (typo)).
- Lifetime phrasing: `onboarding_paywall_lifetime_disclosure` / `One-time purchase. No subscription.` → "Eenmalige aankoop. Geen abonnement."
- Free trial: `Start Free Trial` → "Gratis proefperiode starten"; `Start %@ Free Trial` → "Start %@ gratis proefperiode"; `onboarding_paywall_free_trial_badge` → "7 dagen gratis"; `%@ free, then %@/month. Cancel anytime.` → "%@ gratis, daarna %@/maand. Annuleer op elk moment."; `Cancel anytime. No goals. No pressure. No diagnoses.` → "Annuleer op elk moment. Geen doelen. Geen druk. Geen diagnoses." The first-7-days full access: `Everything is unlocked for your first 7 days. No sign-up needed.` → "Tijdens uw eerste 7 dagen is alles ontgrendeld. Geen registratie nodig." (u). `Free vs Premium` → "Gratis vs Premium". Free export: `export_limit_alert_title` "Gratis export gebruikt".
- Restore: `Restore Purchases` → "Herstel aankopen" (imperative); `Purchases Restored` → "Aankopen hersteld"; `Your premium access has been restored.`
- Manage: `Manage Subscription` → "Abonnement beheren". Family Sharing: `Share with up to 5 family members` → "Deel met maximaal 5 gezinsleden", `One subscription covers your whole Family Sharing group.` → "Eén abonnement dekt je hele groep voor Delen met gezin."; Apple's term "Delen met gezin".

### Dutch App Store listing (https://apps.apple.com/nl/app/observa-hrv-herstelscore/id6757438990, checked 2026-11-19)

- Name: **Observa: HRV & Herstelscore** (lookup `trackName`).
- Subtitle: **Paraatheid, Slaap-Cyclus-Coach** (English "Readiness, Sleep & Cycle Coach"): the capitalised hyphen compound "Slaap-Cyclus-Coach" is odd Dutch, "Paraatheid" differs from the app's "Gereedheid" (O2), and the store name says "Herstelscore" where the app headline score is "Gereedheid".
- Category: **Gezondheid en fitness**. Price "Gratis" (store prints "Gratis"), age 9+, size 92,7 MB (lookup 92651520), minimum iOS 17.6. Talen: "Nederlands en 33 andere".
- IAP rows (store): `Premium maandabonnement € 3,99`, `Premium jaarabonnement € 24,99`, `Ontwikkelaar steunen € 1,00`, `Premium eenmalige aankoop € 59,99` (the store says "eenmalige aankoop" where the app says "Levenslang"). Reference only.
- Description: **Dutch**, je-form, consistent with the je register: "Observa leest die gegevens en vertelt je elke ochtend hoe klaar je bent, en waarom.", "Je Gereedheid is opgebouwd uit je slaap, HRV, rusthartslag en trainingsbelasting", "Tik op "Score uitgelegd"", "Doorpakken, Onderhouden, Herstel of Rust", "Slaapscore", "slaapfasen", "slaapschuld ten opzichte van je eigen slaapdoel", "ochtendmens, een avondmens", "Je functionele leeftijd", "een ochtendcheck-in van 10 seconden", "Apple Watch-app (watchOS 10 of nieuwer)", "complicaties voor je wijzerplaat", "Widgets op je beginscherm en toegangsscherm", "een gratis proefperiode van 1 week via de App Store", "Levenslang, werkt met Delen met gezin", "Observa is een welzijnsapp, geen medisch hulpmiddel."

---

### 3. Pawza (`pawza`, source `PetCare/`, ID 6773507068)

### Dutch coverage

- Main `PetCare/Localizable.xcstrings`: 1323 keys (1308 non-stale; 15 stale), 1322 with an `nl` value, all translated. The one gap is the format key `%@`. 42 values identical to English: cognates and loanwords ("Camera", "Checklist", "Details", "Document", "Doses", "iCloud", "Later", "Microchip", "Mild", "Open PDF", "Poster", "Privacy", "Puppy", "Recent", "Record", "Records", "Status", "Supplement", "Type", "Water", "Pawza Pro", "Apple Intelligence", "fl oz", "Chip:"), plus `Diagnoses (%lld)`, `Diagnoses: %@` and `Spreadsheets (CSV)` (Dutch too). No real English left in.
- `AppShortcuts.xcstrings`: 4/4: "Log zorg in ${applicationName}", "Log de stemming van ${pet} in ${applicationName}", "Log zorg voor ${pet} in ${applicationName}", and **`Log ${kind} in ${applicationName}` kept identical to English** (valid Dutch "Log" imperative but the English `${kind}` phrase is not translated; the other phrases use "Log zorg", the UI uses "Verzorging vastleggen" and "loggen").
- Widgets (`PetCareWidgets/`) have no catalog; their names come from the main catalog (see Glossary).
- **No `InfoPlist.xcstrings` and no `nl.lproj`.** `NSCameraUsageDescription` ("Pawza uses your camera to scan vet documents and take photos of your pets.") and `NSPhotoLibraryUsageDescription` ("Pawza needs photo access to import pictures of your pets and their documents.") are English build settings (`INFOPLIST_KEY_*`), so both permission prompts are **English on a Dutch device (flag P1)**. Dutch is a known region of the app (the catalog has `nl`), so this is a real gap. The display name is not localized.
- **Verdict: app is in Dutch: yes**, with the two permission prompts in English.

### Register

- je/jij/jouw in **135** values; u/uw in **2**, both the vet e-mail template ("Hallo, zou u mij het volledige medische dossier van %@ als één PDF kunnen mailen, met vaccinaties, medicijnen …?", "…van mijn huisdier…"). That is the user writing to a vet, so formal u is correct there and not an app register mix. Examples: "Je ziet …" style in the store text; "Gratis accounts kunnen één dier bijhouden. Met Pro voeg je er zoveel toe als je wilt.", "Je kunt Pawza verlaten; de import gaat door …", "Heb je hulp nodig, neem dan contact op met de ondersteuning", "Jouw gegevens, altijd van jou."
- Mixed: no. Site register je matches. Quote freely.
- Siri phrases are neutral imperatives ("Log zorg in …").

### Glossary

| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Pet / pets | `Pet` / `Pets` | Huisdier / Huisdieren | `Add pet` → "Dier toevoegen"; `Free accounts can track one pet` → "…één dier bijhouden": **P2** dier vs huisdier mixed; "Unlimited pets" → `Unlock unlimited pets, scans, photos, and Pro features.` "Ontgrendel onbeperkte huisdieren, scans, foto's en Pro-functies." Species: `Dog` "Hond", `Cat` "Kat", `Rabbit` "Konijn", `Bird` "Vogel", `Other` "Overig", `Puppy` "Puppy" |
| Care log | `Care log` | Verzorgingslogboek | `Daily care log (last 7 days)` → "Dagelijkse verzorging (laatste 7 dagen)"; store: "het verzorgingslogboek"; `Log care` → "Verzorging vastleggen" but Siri "Log zorg" and widget text "Log eten, drinken, een wandeling of toiletbezoek …"; `Care type` → "Zorgtype": **P3** care = verzorging / zorg |
| Medications | `Medications` / `Medication` | Medicijnen / Medicijn | `Add Medication` → "Medicijn toevoegen" vs `Add a medication` → "Voeg een medicijn toe" (infinitive vs imperative, **P4**); `Track medication schedule` → "Medicatieschema bijhouden"; "medicatiedoses" in a reminder string |
| Doses | `Doses` | Doses | Dutch plural "doses" is correct; store text "dosisherinnering", "dosis" |
| Vaccinations | `Vaccinations` / `Vaccination` | Vaccinaties / Vaccinatie | `Vaccines` → "Vaccins"; `Vaccination status` → "Vaccinatiestatus"; `Vaccination certificate` → "Vaccinatiebewijs"; `Vaccine due: %@` → "Vaccinatie nodig: %@"; `%@ booster due` → "%@-booster nodig"; `Time for %@'s %@ booster` → "Tijd voor %1$@'s %2$@-booster" |
| Symptoms | `Symptoms` / `Symptom` | Symptomen / Symptoom | `Severity` → "Ernst", `Mild` "Mild", `Moderate` "Matig", `Severe` "Ernstig" |
| Reminders | `Reminders` / `Reminder` | Herinneringen / Herinnering | `Snooze` → "Sluimeren" (Apple's own word for alarms; the notification action in the English page is "snooze it for an hour"); `Mark Done` → "Markeer als gereed"; `Done` → "Gereed" |
| Weight chart | `Weight` | Gewicht | `Log Weight` → "Gewicht loggen"; `Time for a weigh-in` → "Tijd om te wegen" |
| Weight alerts | `Weight alerts` | Gewichtswaarschuwingen | `Weight trend alerts` → "Waarschuwingen voor gewichtstrend"; store says "gewichtsmeldingen" ("Pro … gewichtsmeldingen") |
| Records | `Records` / `Record` | Records / Record | **P5:** untranslated loanword "Record(s)" 40+ values ("Add Record" → "Record toevoegen", "Review records" → "Controleer records"); store text says "dossier" ("vult Apple Intelligence het dossier in") and "records" ("Importeer eerdere records"); `Export your records` → "Exporteer je records" |
| Document scanning | `Scan` / `Scan a vet document` | Scannen | `Scan` → "Scannen" (button), `Free accounts include 10 document scans.` → "Gratis accounts bevatten 10 documentscans."; `Vaccination certificate, lab result, or invoice` → "vaccinatiebewijs, labuitslag of factuur" (capture string), `Lab results` → "Labresultaten" (two forms), `Prescription` → "Recept", `Invoice` → "Factuur", `Discharge notes` → "Ontslagnotities" |
| Review screen | `Review` / `Review records` | Controleer / Controleer records | imperative button; `Records ready to review` → "Records klaar om te controleren"; `Leave a review` → "Beoordeling achterlaten" |
| Apple Intelligence auto-fill | `AI auto-fill is ready on this iPhone…` | Automatisch invullen met AI staat klaar op deze iPhone — gescande gegevens worden voor je ingevuld. | `Apple Intelligence summaries` → "Apple Intelligence-samenvattingen"; Apple Vision is not a UI string |
| Import past records | `Import past records` | Importeer eerdere records | `Import past records (Pro)` → "Importeer eerdere records (Pro)"; `Import from a file` → "Importeer uit een bestand"; imperative here, "Importeren" elsewhere |
| Vet visit | `Vet visit` / `Vet visits` | Dierenartsbezoek / Dierenartsbezoeken | `Vet` → "Dierenarts" |
| Since last vet visit | `Since last vet visit` | Sinds het laatste dierenartsbezoek | also `Changes Since Last Visit` → "Wijzigingen sinds het laatste bezoek" |
| Vet Visit PDF | `Vet Visit PDF` | PDF dierenartsbezoek | other wording: "de dierenarts-PDF" (`…printed in the vet PDF and the sitter pack` → "…afgedrukt in de dierenarts-PDF en de oppasmap"), store "de dierenarts-PDF": **P6** two names; `What to discuss` → "Te bespreken" |
| Emergency Card | `Emergency Card` | Noodkaart | `Emergency Info` → "Noodinformatie"; `Emergency vet` → "Spoeddierenarts"; `Emergency clinic name` → "Naam spoedkliniek" |
| Lost Pet Kit | `Lost Pet Kit` | Vermist-kit | **P7:** hyphenated "Vermist-kit", "Vermist-poster" (`Lost Pet Poster`); store writes "de Vermist-kit"; `Lost pet` → "Huisdier vermist", `Lost dog` "Hond vermist", `Lost cat` "Kat vermist"; QR tag → "penning" (`ID Tag QR Codes` → "QR-codes voor de penning"; store: "een QR-penning voor de halsband") |
| Sitter Pack | `Sitter Pack` | Oppasmap | `Make a sitter pack` → "Maak een oppasmap"; store "de Oppasmap" |
| Compare Photos | `Compare Photos` | Foto's vergelijken | `Compare two photos` → "Vergelijk twee foto's" |
| Photo auto-sorting | `Photo auto-categorization` / `Photos sort themselves` | Automatische fotocategorisatie / Foto's sorteren zichzelf | `Auto-categorize with Pro` → "Automatisch categoriseren met Pro"; store "automatische fotosortering"; categories: "dierenartsbezoek, symptomen en bijzondere momenten" |
| Widgets (8) | `Care streak` / `Daily rhythm` / `Pet day` / `Quick log` / `Quick log button` / `The pack` / `Up next` / `Year in paws` | Zorgreeks / Dagritme / Huisdierdag / Snel loggen / Snel-logknop / De roedel / Hierna / Jaar in pootjes | `Up next` → "Hierna" is terse; description "Upcoming and overdue reminders for all your pets." → "Aankomende en achterstallige herinneringen voor al je huisdieren."; `Streak` family: "Beste reeks", "Huidige reeks", "%lld dagen op rij" |
| Control Center button | `Log care` (control) | Verzorging vastleggen | store: "het bedieningspaneel (iOS 18 of nieuwer)" (Apple's Dutch name is "Bedieningscentrum", flag P8) |
| Siri | AppShortcuts | see coverage | |
| iCloud sync | `iCloud Sync: syncing…` | iCloud-synchronisatie: synchroniseren… | `iCloud Sync needs attention — your data is safe on this device.` → "iCloud-synchronisatie vereist aandacht — je gegevens zijn veilig op dit apparaat."; `iCloud account` → "iCloud-account"; debug strings leak: "CloudKit wordt geactiveerd zodra de iCloud-rechten zijn toegevoegd.", "iCloud-synchronisatie: nog niet ingeschakeld in deze build." (P9) |
| Export / full data export | `Export your data` | Exporteer je gegevens | `Full backup (JSON)` → "Volledige back-up (JSON)", `Include photos in JSON backup` → "Foto's opnemen in JSON-reservekopie" (back-up vs reservekopie, **P10**); `Export everything` → "Alles exporteren"; "Pawza JSON, 11Pets CSV" |
| Import from another pet app | `Pawza JSON, 11Pets CSV, or any spreadsheet with pet names — we'll figure it out.` | Pawza-JSON, 11Pets-CSV of een willekeurig spreadsheet met huisdiernamen — wij zoeken het uit. | |
| Care types | `Food` / `Water` / `Walk` / `Toilet` / `Treat` / `Grooming` / `Mood` | Voer / Water / Wandeling / Behoefte / Snack / Vachtverzorging / Humeur | `Toilet` → "Behoefte" (widget text says "toiletbezoek", store "plasrondjes"); `Feeding` → "Voeren"; `Diet` → "Voeding"; `Activity` → "Activiteit"; store "eten, water, wandelingen, plasrondjes en humeur" |
| Free tier | `Free` | Gratis | **P11:** "Gratis accounts …" 3 strings, but Pawza has no account (the English says "Free accounts", the page says "No account") |
| Settings | `Settings` | Instellingen | |
| Privacy | `Privacy` | Privacy | identical to English |
| Support | `Support` | Support | identical to English (the same app writes "ondersteuning" in `3. Heb je hulp nodig, neem dan contact op met de ondersteuning`, **P12**) |

### Paid tier names in the Dutch UI

- Title: **Pawza Pro** (`Pawza Pro`, `Pro`, `Unlock Pawza Pro` → "Pawza Pro ontgrendelen", `Upgrade to Pawza Pro` → "Upgrade naar Pawza Pro", `Welcome to Pawza Pro` → "Welkom bij Pawza Pro", `%@ is a Pro feature` → "Pro-functie: %@", `Your Pawza Pro purchase is active again.` → "Je Pawza Pro-aankoop is weer actief."). The word "Premium" is not used.
- Plan labels: `Pro (Monthly)` → "Pro (maandelijks)", `Pro (Yearly)` → "Pro (jaarlijks)", `Pro (Lifetime)` → "Pro (levenslang)"; `Lifetime` → "Levenslang", `Buy Lifetime — %@` → "Levenslang kopen — %@". Billing text: "Maandelijks: 7 dagen gratis proberen, daarna %@ per maand, met maandelijkse automatische verlenging." / "Jaarlijks: 7 dagen gratis proberen, daarna %@ per jaar, met jaarlijkse automatische verlenging." / "Levenslang: eenmalige aankoop, geen automatische verlenging. Abonnementen worden automatisch verlengd, tenzij ze minstens 24 uur vóór het einde van de huidige periode worden opgezegd. Beheer of zeg ze op wanneer je wilt in de instellingen van je Apple ID."
- Trial: `Start 7-day free trial` → "7 dagen gratis proberen"; `7-DAY FREE TRIAL` → "7 DAGEN GRATIS PROBEREN" (the word "proberen" is the Pawza and RightSplit pattern; Observa/Shogiful say "proefperiode").
- Restore: `Restore Purchases` → "Herstel aankopen"; `Nothing to restore` → "Niets te herstellen"; `We didn't find any previous Pawza Pro purchases on your Apple ID.` → "We hebben geen eerdere Pawza Pro-aankopen op je Apple ID gevonden."
- Manage: `Manage subscription` → "Abonnement beheren"; `Manage your subscription in Settings → Apple ID → Subscriptions.` → "Beheer je abonnement via Instellingen → Apple ID → Abonnementen."; `Subscribe` → "Abonneren". Limits: "Gratis accounts bevatten 10 documentscans. Pro heft de limiet op." / "Gratis accounts bevatten 50 foto's." / "Je eerste import van records was gratis."

### Dutch App Store listing (https://apps.apple.com/nl/app/pawza-hond-kat-gezondheid/id6773507068, checked 2026-11-19)

- Name: **Pawza: Hond & Kat Gezondheid** (lookup `trackName`).
- Subtitle: **Enting, gewicht & herinnering** (the singular "herinnering" and "enting" are Flemish-leaning for vaccination; the app says "vaccinatie").
- Category: **Lifestyle**. Price "Gratis", age 4+, size 39,7 MB, minimum iOS 17.6. Talen: "Nederlands en 43 andere".
- IAP rows: `Pawza Pro jaarlijks € 22,99`, `Pawza Pro maandelijks € 2,99`, `Pawza Pro eenmalig € 44,99` (reference only).
- Description: **Dutch**, je-form ("Je ziet het ontbijt dat in de bak blijft en de extra rondjes naar de waterbak."). Vocabulary: "Doses, maaltijden, vaccinaties, wegingen en dierenartsbezoeken", "het dashboard, een widget op je begin- of toegangsscherm, het bedieningspaneel (iOS 18 of nieuwer) of Siri", "Alle acht widgets zijn gratis", "Gegeven … Gevoerd" (notification actions), "Voorraad bijhouden", "Pawza leest het op je apparaat", "Apple Intelligence vult het dossier in", "Importeer eerdere records", "gezondheidsoverzicht als PDF", "De Noodkaart", "de Vermist-kit", "een printbare poster, een QR-penning voor de halsband en een checklist", "de Oppasmap, onderdeel van Pawza Pro", "Een gewichtsgrafiek", "gewichtsmeldingen", "De fototijdlijn filtert op dierenartsbezoek, symptoom en mijlpaal", "iPhone Duo", "Delen met gezin", "gratis proefweek" (app: "7 dagen gratis proberen"), "Locatie- en EXIF-gegevens".

---

### 4. RightSplit (`rightsplit`, source `splitit/`, ID 6757268612)

### Dutch coverage

- Main `splitit/Localizable.xcstrings`: 499 keys (411 non-stale, 88 stale), 499 with `nl`, all translated; 33 identical to English (brand and cognate words: "Airbnb", "Hotel", "IBAN", "Dessert", "Pasta", "Omakase", "Restaurant", "Privacy", "Recent", "Status", "Water", "WhatsApp", "Community", `paypal.me username`, `revolut.me username`, `wise.com username`, "Pro+").
- Widgets `splititWidgets/Localizable.xcstrings`: 376/376 (21 identical; 346 non-stale). Share extension `splititShare/Localizable.xcstrings`: 3/3. Shared package `SplititKit/.../Localizable.xcstrings`: 65/65 (App Intents titles and Pocket Split strings).
- `InfoPlist.xcstrings`: 5/5: `CFBundleDisplayName` "RightSplit", `CFBundleName` "splitit" (internal name, same in all locales), `NSCameraUsageDescription` "RightSplit gebruikt de camera om restaurantbonnen te scannen voor het splitsen van de rekening.", `NSContactsUsageDescription` "RightSplit heeft toegang tot contacten om personen toe te voegen bij het splitsen van een rekening.", `NSPhotoLibraryAddUsageDescription` "RightSplit bewaart een afbeelding alleen in je fotobibliotheek als je daarvoor kiest." Permission prompts are Dutch.
- **Siri phrases: English only.** There is no AppShortcuts string catalog. The blueprint (§4.22) lists 9 spoken phrases ("Split a bill / Split the bill / Split a check in RightSplit", "Scan a receipt in …", "Split / Run / Start [template] in RightSplit"); only the shortcut titles in the Shortcuts app are translated (`Split a bill` → "Reken deel", `Scan a receipt` → "Scan een bonnetje", `Run a split template` → "Verdeelsjabloon uitvoeren"). A Dutch user must say the English phrase (flag R1).
- **Verdict: app is in Dutch: yes**, spoken Siri phrases excluded.

### Register

- je/jij/jouw in **75** values, u/uw in **0**. Examples: "Een dag nadat je een rekening gaat volgen, herinnert RightSplit je als iemand nog niet heeft betaald.", "Voeg minstens één manier toe om betaald te worden — Venmo, Revolut, PayPal.me, W…", "Hé %1$@! Jouw deel van de rekening bij %2$@ is %3$@." (the message the user sends, informal Hé), "Je naam (optioneel)", "Vind je RightSplit leuk?", "Iedereen is afgerekend — geen overschrijvingen nodig.", widgets "Badges die je verdient met verdelen.", "Elke dag dat je verdeelt, telt mee". Mixed: no. Many UI buttons are bare imperatives ("Voeg toe", "Wijzig", "Verwijder", "Annuleer", "Kopieer", "Deel") next to infinitives ("Persoon toevoegen", "Aankopen herstellen", "Opslaan"): see R3.

### Glossary

| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Scan receipt | `Scan receipt` / `Scan Receipt` / `Scan receipts` | Scan bon / Bon scannen / Scan bonnen | three word orders for one feature; widget action `Scan Receipt` "Bon scannen"; Intent `Scan a receipt` "Scan een bonnetje"; **R2:** "bon" (primary) vs "bonnetje" ("Kan items van het bonnetje niet lezen.", "Scan een bonnetje") |
| Receipt | `Receipt` | Bon | `Receipts` → "Bonnen"; `Receipt photo` → "Foto van bon"; `Receipt Language` → "Taal bon"; `Reading receipt...` → "Bon lezen..."; store: "de bon", "bonnen", "bonscanner" |
| Receipt language | `Receipt Language` | Taal bon | "Receipt language improves scanning accuracy." → "De taal van de bon verbetert de scannauwkeurigheid." |
| Split a bill (verb / button) | `Split it` / `Split Receipt` / `Split by items` / `Split a bill` | Verdelen / Bon verdelen / Verdelen per artikel / Reken deel | **R3:** the app mixes verdelen (principal), splitsen ("De rekening splitsen hoeft niet ongemakkelijk te zijn.", "Voeg minstens 2 personen toe om de rekening te splitsen") and delen ("Deel meer dan reizen.", store name "Delen & Groep"); `Split a bill` → "Reken deel" (Siri shortcut title, odd) |
| Split (the result, noun) | `Last split` / `Recent Splits` / `New split` / `Split Complete` | Laatste splitsing / Recente splitsingen / Nieuwe verdeling / Verdeling voltooid | noun: "splitsing" (History, Last Split widget) vs "verdeling" (widgets, `New Split`, `Split Stats` "Statistieken"): **R4**; `First Split` → "Eerste verdeling"; `%lld splits` → "%lld verdeling \| %lld verdelingen" |
| Equal split / tip | `Equal splits & tip` | Gelijke splitsing & fooi | `Split equally between the selected people.` → "Wordt gelijk verdeeld over de geselecteerde personen." |
| Split by items / shared dishes | `Split by items` / `Add shared item` / `Shared dishes` / `Shared items` | Verdelen per artikel / Gedeeld artikel toevoegen / Gedeelde gerechten / Gedeelde artikelen | `Item` → "Artikel" (widgets "Items", `%lld item(s)` "%lld item/items", `Edit items` "Items wijzigen", `Assign items` "Items toewijzen", widgets "post/posten"): **R5** artikel / item / post |
| Tap who had what | `TAP NAMES TO ASSIGN ITEMS` | TIK OP NAMEN OM ARTIKELEN TOE TE WIJZEN | `Person` → "Persoon", `People` → "Personen" |
| Tax | `Tax` | Belasting | **R6:** "Belasting" (tax) where the EU/NL receipt line is "btw"; the store text says "btw en fooi" ("Op een gescande bon volgen btw en fooi wat ieder heeft besteld") |
| Tip | `Tip` / `Tip included` | Fooi / Fooi inbegrepen | `Tip percent` → "Fooi percentage" (missing hyphen/compound, see R7) |
| Fair rounding | `Round fairly` | Eerlijk afronden | store "Eerlijk afronden" |
| Spaces | `Spaces` / `New space` / `Edit space` | Ruimtes / Nieuwe ruimte / Ruimte bewerken | store: "RUIMTES, VOOR DE REKENINGEN DIE BLIJVEN KOMEN"; `Space actions` → "Ruimteacties"; page: "Spaces for trips, households, and subscriptions" |
| Trips / Households / Subscriptions | `Trip` / `Trips` / `Household` / `Subscriptions` | Reis / Reizen / Huishouden / Abonnementen | `Create a trip to group multiple receipts.` → "Maak een reis om meerdere bonnen te groeperen."; `Edit trip` "Bewerk reis" vs `Edit space` "Ruimte bewerken" (word order, R3) |
| Settle up / fewest transfers | `Settle in` / `Settlement` / `Settle Up` | Afrekenen in / Afrekening / Vereffenen | **R8:** "afrekenen" (`Settle in` "Afrekenen in", "Iedereen is afgerekend") vs "vereffenen" (widget `Settle Up` "Vereffenen", "Alles vereffend", "Alles om te vereffenen op één pagina") vs "quitte" ("Alles quitte", "Iedereen quitte", store "quitte staat") |
| Who owes / owed | `owes` / `owed` / `Owed` / `Balance` / `Net` | betaalt / ontvangt / Verschuldigd / Saldo / Saldo | **R9:** `owes` → "betaalt" and `owed` → "ontvangt" (meaning shifted; not "is schuldig"), `Balance` and `Net` both "Saldo"; widget "wie wat verschuldigd is" |
| Payment requests | `Send Payment Requests` | Betalingsverzoeken versturen | `Payment reminder` → "Betalingsherinnering"; `Unpaid reminders` → "Betalingsherinneringen"; message: "Hé %1$@! Jouw deel van de rekening is %2$@."; `Text / WhatsApp share` → "Delen via bericht / WhatsApp" |
| Pay-Me Card | `Pay Me` / `Pay-Me Card` | Betaal mij / Pay-Me-kaart | **R10:** three spellings for the feature: widget/intent name "Betaal mij", card "Pay-Me-kaart" / "Pay Me-kaart", "Pay Me instellen", "Pay-Me-QR-code"; `Pay Me card is Pro+` → "Pay-Me-kaart is Pro+"; `Scan to pay me back` → "Scan en betaal terug" |
| Track who's paid | `Track who's paid` / `Track payments` | Volg wie betaald heeft / Volg betalingen | `Mark as paid` → "Markeer als betaald"; `Paid` → "Betaald"; `Payer` → "Betaler"; `%lld of %lld paid` → "%lld van %lld betaald" |
| Payment tracker on Lock Screen | `Lock-screen reminder of who's paid you back…` | Herinnering op vergrendelscherm wie je terug heeft betaald. | **R11:** "vergrendelscherm" (also `Your last per-person amount, on your lock screen.`) vs "toegangsscherm" (`Your last split, on your Lock Screen.`); Apple's Dutch term is "toegangsscherm" |
| Recurring bills | `Recurring bills` / `Recurring expense reminders` | Terugkerende rekeningen / Herinneringen voor terugkerende uitgaven | widget `No repeating bills` → "Geen vaste lasten"; store "Markeer de huur als maandelijks" |
| Split history | `History` / `Unlimited split history` | Geschiedenis / Onbeperkte verdeelgeschiedenis | `Last 5` → "Laatste 5"; `Recent receipts` "Recente bonnen" |
| Split templates | `Templates` / `Save as template` / `Use this template` | Sjablonen / Opslaan als sjabloon / Dit sjabloon gebruiken | `Split template` → "Verdeelsjabloon"; `Run a split template` → "Verdeelsjabloon uitvoeren" |
| Pocket Split keypad | `Pocket Split` | Verdeelcalculator | `Change Pocket Split people` → "Personen in Verdeelcalculator wijzigen"; `Clear Pocket Split` → "Verdeelcalculator wissen"; `Press a Pocket Split key` → "Toets op Verdeelcalculator indrukken"; the site's "Pocket Split" name is the English widget name |
| Widgets (12 free + 6 Pro+) | `Achievements` / `Coming Up` / `Last Split` / `Pay Me` / `Pinned Spaces` / `Pocket Split` / `Quick Actions` / `Receipt Roll` / `Recent Splits` / `Settle Up` / `Space` / `Split Graph` / `Split Rhythm` / `Split Stats` / `Streak Stats` / `Templates` / `Waiting On` | Prestaties / Binnenkort / Laatste splitsing / Betaal mij / Vastgezette ruimtes / Verdeelcalculator / Snelle acties / Bonnenrol / Recente splitsingen / Vereffenen / Ruimte / Verdeelgrafiek / Verdeelritme / Statistieken / Reeksstatistieken / Sjablonen / Wachten op | Intents: `New Split` "Nieuwe verdeling", `Run Template` "Sjabloon uitvoeren"; `Badges you earn by splitting` → "Badges die je verdient met verdelen." |
| Controls / Siri | AppShortcuts (none) | see coverage | |
| Home currency | `Home currency` | Standaardvaluta | `Home Currency` "Standaardvaluta", `Language & Currency` "Taal en valuta" |
| Currency conversion (ECB) | `European Central Bank rates` | Koersen van de Europese Centrale Bank | `Get exchange rates` → "Wisselkoersen ophalen"; `Mixed currencies` → "Gemengde valuta's" (store/site "mix currencies"); `Totals converted to %@` → "Totalen omgerekend naar %@" |
| Remember people / contacts | `Remember people` / `Contacts integration` | Personen onthouden / Contacten-integratie | `Forget all people` "Alle personen vergeten"; `From contacts` "Uit contacten" |
| Payment methods | `Add payment method` / `New method` / `Not set` | Betaalmethode toevoegen / Nieuwe methode / Niet ingesteld | handles: IBAN, PayPal.me, Revolut, Wise, Venmo, Apple Pay (brand names); `Set up a payment handle first` → "Stel eerst een betaalmethode in"; `Scan or tap a handle to pay me back.` → "Scan of tik op een betaalmethode om mij terug te betalen." |
| Categories | `Rail` / `Fuel` / `Fun` / `Groceries` / `Household` / `Utilities` / `Travel` / `Rent` | Platform / Brandstof / Plezier / Boodschappen / Huishouden / Nutsvoorzieningen / Reizen / Huur | **R12:** `Rail` → "Platform" (wrong; it is the train/rail category: should be "Trein" or "Openbaar vervoer"); `Utilities` → "Nutsvoorzieningen" (acceptable; "Vaste lasten" is the everyday word); `Uncategorized` → "Geen categorie" |
| Settings / Options | `Options` | Opties | `Appearance` → "Uiterlijk"; `Display` → "Weergave"; `Notifications` → "Meldingen" |

### Paid tier names in the Dutch UI

- Title: **Pro+** (`Pro`, `Pro+`; `Pro+ Yearly` → "Pro+ Jaarlijks", `Pro+ Lifetime` → "Pro+ Levenslang", `Unlock Pro+ Lifetime` → "Pro+ Lifetime ontgrendelen" (English "Lifetime" left in, **R13**), `Unlock Pro+` → "Pro+ ontgrendelen", `Unlock Pro+ — Pay once` → "Pro+ ontgrendelen — Eenmalig betalen", `Continue with Pro+` → "Doorgaan met Pro+", `Upgrade to Pro+` → "Upgraden naar Pro+", `Pro+ restored successfully!` → "Pro+ succesvol hersteld!"). "Pro" alone appears only in the key `Pro`. The store IAP row reads "RightSplit Pro+ jaarabo" (cut off mid-word; store-side defect, R14) and "Pro+ Eenmalige aankoop".
- Periods: `Monthly` → "Maandelijks", `Weekly` → "Wekelijks", `One-time` → "Eenmalig", `One-time purchase` → "Eenmalige aankoop", `%@ pay once` → "%@ eenmalig betalen", `Best value` → "Beste waarde", `%@ billed yearly` → "%@ jaarlijks gefactureerd", `Auto-renews yearly until canceled.` → "Wordt jaarlijks automatisch verlengd totdat je opzegt.", `Renews automatically. Cancel anytime.` → "Wordt automatisch verlengd. Op elk moment opzegbaar.", `No subscriptions. No renewals.` → "Geen abonnementen. Geen verlengingen.".
- Free trial: `%lld-day free trial` → "%lld dagen gratis proberen" (also week/month/year), `%lld days free` → "%lld dagen gratis", `paywall.trialThenBilled` → "%@ proefperiode, daarna %@"; the page says "3-day trial".
- Restore: `Restore purchases` / `Restore Purchases` → "Aankopen herstellen" (infinitive); `Couldn't restore purchases right now.` → "Kan aankopen nu niet herstellen."; `No active purchases found on this Apple ID.` → "Geen actieve aankopen gevonden op deze Apple ID."; `Manage subscription` → "Abonnement beheren"; `Unlock everything.` → "Ontgrendel alles."
- Free: `Free` → "Gratis"; `1 free` → "1 gratis"; "Open. Voer in. Klaar. Geen accounts. Geen tracking."

### Dutch App Store listing (https://apps.apple.com/nl/app/rightsplit-delen-groep/id6757268612, checked 2026-11-19)

- Name: **RightSplit: Delen & Groep** (lookup `trackName`).
- Subtitle: **Rekening & uitgaven scannen**.
- Category: **Diensten** (English "Utilities"). Price "Gratis", age 4+, size 18,2 MB, minimum iOS 17.0 (iPhone only). Talen: "Nederlands en 33 andere".
- IAP rows: `RightSplit Pro+ jaarabo` (cut off, € 4,99) and `Pro+ Eenmalige aankoop` (€ 8,99): reference only; the store titles are inconsistent in form.
- Description: **Dutch**, je-form ("De rekening landt midden op tafel en het gesprek valt stil."). Vocabulary: "Scan de bon, tik aan wie wat had en stuur iedereen precies zijn deel", "Een account heb je niet nodig", "Eerlijk afronden", "Deel gelijk, per artikel", "Op een gescande bon volgen btw en fooi wat ieder heeft besteld", "Kies een fooi van 0, 15, 18 of 20 procent of schuif naar maximaal 30", "Iedereen krijgt een bericht met precies zijn deel, via Berichten of WhatsApp", "PayPal.me, Revolut of Wise", "RUIMTES, VOOR DE REKENINGEN DIE BLIJVEN KOMEN", "het kleinste aantal betalingen waarmee iedereen quitte staat", "58 valuta … koersen van de Europese Centrale Bank", "18 widgets, een live activiteit en 4 bedieningselementen", "Je laatste verdeling staat klaar op je toegangsscherm", "Pro+ is er als jaarabonnement dat begint met 3 dagen gratis proberen, of als eenmalige aankoop", "Delen met gezin is inbegrepen". The store says "18 widgets"; the English page says 12 + 6.

---

### 5. Shogiful (`shogiful`, source `shogi/`, ID 6761656926)

### Dutch coverage

- `shogi/Localization/Localizable.xcstrings`: 3751 keys (3738 non-stale, 13 stale), all with an `nl` value, all translated; **1 empty `nl` value**: `dashboard.accuracy %lld` (the plain-number variant, unused alternate of `dashboard.accuracy %@` "Nauwkeurigheid %@"). 121 values identical to English: format-only keys, the Game Center achievement names (Japanese terms: "Fukkatsu", "Gyakuten", "Goren-shō", "Kanpeki", "Seimitsu", …), castle names (Mino, Yagura, Nakahara, Elmo), "Rating", "Blunder(s)", "Momentum", "Premium", `app.name` "Shogiful". No sentence is left in English.
- `InfoPlist.xcstrings`: 2 keys, **0 in Dutch** (`CFBundleDisplayName`, `CFBundleName`; the catalog holds only `en`). The app requests no permissions, so no prompt is affected; the Home Screen name stays "Shogiful".
- No extensions, no widgets, no Siri phrases (the app has none). The Mac app shares the catalog (`mac.command.*`, `mac.menu.*` Dutch).
- **Verdict: app is in Dutch: yes.**

### Register

- je/jij/jouw in **781** values, u/uw in **0**. Examples: "Je partij analyseren", "Tik op Analyseren om je zetten met YaneuraOu te beoordelen.", "Je hebt de gratis analyses van vandaag gebruikt. Ga onbeperkt om elke fout in elke partij te vinden.", "Weet je zeker dat je wilt opgeven?", "Jouw zet", "Meld je aan om mee te doen aan ranglijsten", lessons "Je hoeft niet elke opening te kennen — je moet er twee of drie grondig kennen." Mixed: no. Site register je matches. The Shogiful catalog uses bare imperatives in the UI ("Doorgaan", "Opnieuw", "Annuleren", "Resetten"); `settings.sync.restartCancel` "Annuleer" vs `common.cancel` "Annuleren".

### Glossary

Shogi terms: the Dutch UI keeps Japanese terms (Sente, Gote, tsume, tesuji, yose, joseki, komaochi, kyu/dan, sennichite, KIF, SFEN) and uses Dutch chess words for the rest. Piece names (`piece.*`): King "Koning", Rook "Toren", Bishop "Loper", Gold General "Gouden generaal", Silver General "Zilveren generaal", Knight "Paard", Lance "Lans", Pawn "Pion"; promoted: Dragon "Draak", Horse `piece.bishop.promoted` "Gepromoveerde loper" (English key says "Horse"; the Dutch drops the name), Promoted Knight "Gepromoveerd paard", Promoted Lance "Gepromoveerde lans", Promoted Pawn "Gepromoveerde pion", Promoted Silver "Gepromoveerd zilver".

| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Tabs | `tab.play` / `tab.analysis` / `tab.training` / `tab.progress` / `tab.dashboard` | Spelen / Analyse / Training / Voortgang / Dashboard | |
| Game review | `analysis.review.title` / `Game Review` | Partijbespreking | `analysis.analyse` "Partij analyseren"; `analysis.progress.title` "Je partij analyseren"; `dashboard.reviewGame` "Partij bekijken"; store "Elke zet geanalyseerd" |
| Analysis | `analysis.title` | Analyse | `Analyse Position` (Mac) → "Stelling analyseren"; `analysis.keyMoments` → "Sleutelmomenten"; `analysis.tab.moves` "Zetten", `.moments` "Momenten", `.insights` "Inzichten" |
| YaneuraOu engine | `analysis.progress.subtitle` | YaneuraOu beoordeelt elke zet... | `Engine` stays "Engine" ("Engine-threads", "Analysediepte" for `Analysis Depth`); store: "de YaneuraOu-engine" |
| Mistake types | `mistakeType.dropMistake` / `castleWeakness` / `missedTsume` / `promotionMistake` / `hangingPiece` / `endgameError` / `missedFork` / `missedPin` / `missedTactic` / `passiveMove` / `poorKingSafety` / `josekiInaccuracy` | Inzetfout / Kasteelzwakte / Gemiste tsume / Promotiefout / Hangend stuk / Eindspelfout / Gemiste vork / Gemiste penning / Gemiste tactiek / Passieve zet / Slechte koningsveiligheid / Joseki-onnauwkeurigheid | site examples "Drop Mistake, Promotion Mistake, Castle Weakness, Missed Tsume" |
| Severity | `classification.*` | Beste zet / Briljant / Sterke zet / Goede zet / Boekzet / Onnauwkeurigheid / Fout / Blunder | `analysis.severity.*`: Blunder "Blunder", Mistake "Fout", Inaccuracy "Onnauwkeurigheid"; site "Mistake / Blunder / Inaccuracy" |
| Coach hints | `settings.coach.title` / `analysis.coachTip.label` / `play.coach.bestMove` | In-game coach / Tip van de coach / Beste zet | `settings.coach.strength` → "Hintsterkte"; `paywall.hero.coachLimit.title` "Onbeperkte coach"; Free: "2 coachhints" (store) |
| Deep Lines | `analysis.deepLines` | Diepe varianten | paywall: "Analyse met meerdere varianten toont je niet alleen de beste zet, maar ook de t…"; site "Deep Lines: the engine's top three lines" |
| Skill Profile / Weakness Trends | `progress.skillProfile` / `progress.weaknessTrends` | Vaardigheidsprofiel / Zwaktetrends | `progress.weaknesses` "Zwaktes"; `hub.assessment.title` / `module.skillAssessment.title` "Niveautest"; `dashboard.focusAreas` "Aandachtspunten" |
| Estimated rating / kyu-dan rank | `progress.estimatedRating` | Geschatte rating | `Rating` stays "Rating"; `hub.progression.ladder.title` "Kyu/dan-ladder"; `hub.progression.unranked.title` "Geen rang"; `dashboard.progression.title` "Je rang"; onboarding "Beginner (15-kyū tot 10-kyū)", "Danhouder (Shodan en hoger)"; `hub.progression.title` "Progressie" vs tab "Voortgang" |
| Accuracy trend | `progress.accuracyTrend` | Nauwkeurigheidstrend | `analysis.accuracy` "Nauwkeurigheid"; `progress.avgAccuracy` "Gem. nauwkeurigheid" |
| Milestones / achievements | `gc.*` / `settings.gc.leaderboards` | Ranglijsten en prestaties | Game Center achievements: "Onderzoeker" (Analyseer tien partijen.), "Toegewijde" (Analyseer honderd partijen.), Japanese names kept ("Fukkatsu", "Meikyoku", "Sanren-shō") |
| Opponents (40) | `opponents.*` / `play.opponent.locked` | Tegenstanders | tiers `opponentTier.*`: Beginner "Beginner", Novice "Nieuweling", Casual "Recreatief", Intermediate "Gemiddeld", Advanced "Gevorderd", Club Player "Clubspeler", Expert "Expert", Master "Meester"; "Versla de vorige tegenstander om te ontgrendelen"; `opponents.feedback.*`; store "KLIM OP LANGS 40 TEGENSTANDERS" |
| Tsume Trail | `module.tsumeTrail.title` | Tsume-traject | subtitle "Problemen met gedwongen mat, van 1 tot 9 zetten."; **S1** "Trail" → "traject" is also the word for `lessonTrack` ("Trajecten"); `hub.tsumeTrail.ladder.title` "Niveaus van het traject"; store "501 TSUME-PROBLEMEN"; `Tsume` → "Tsume" |
| Tsume problems 1 to 9 moves | `hub.tsumeTrail.available %lld` | %lld problemen beschikbaar | `Mate in three` → "mat in drie", "Mat in 3", `Checkmate` → "Schaakmat" (8 values) vs "mat" (283 values) |
| Drop Drills | `module.dropDrills.title` | Inzetoefeningen | **S2:** "drop" = "inzet" (135 values: "Inzetfout", "Inzetvork", "Inzetmat", "Inzetpenning", "Blikseminzet", "Lokinzet", "Spiesinzet") vs "Zet neer" (`board.drop.hint` "Zet %1$@ neer op %2$@"), "Werp je %@ in" (`training.guide.nudge.drop`), "inworp" (calibration titles: "mat met paard-inworp"), "in te zetten" ("Tik op een gemarkeerd veld om in te zetten"). Store: "99 inzetoefeningen, om geslagen stukken terug in het spel te brengen" |
| Castle Atelier | `module.castleAtelier.title` | Kasteelatelier | **S3:** "kasteel/kastelen" 41 values (`Castles` "Kastelen", `castle.drill.complete.title` "Kasteel gebouwd", `Castle Weakness` "Kasteelzwakte") vs "burcht" 114 values (concept and opponent prose: "Elke burcht heeft 'sleutelvelden'", "Burchtbrekende aanvallen", "Meesterschap in burcht én eindspel"); store "62 burchtoefeningen, voor een veilig onderkomen voor je koning". Pick burcht or kasteel for the site; the app's tab-level labels are kasteel |
| Joseki Lab | `module.josekiLab.title` | Joseki-lab | |
| Tesuji Cards | `module.tesujiCards.title` | Tesuji-kaarten | `hub.tesujiCards.tapToFlip` "Tik om om te draaien"; `markRecalled` "Dit wist ik" |
| Yose Trainer | `module.yoseTrainer.title` | Yose-trainer | subtitle "Eindspelwedlopen: aanvallen, verdedigen, ruilen, vasthouden."; store "62 yose-races"; `patternKind.yoseRace` "Eindspelwedloop" (wedloop vs race) |
| Komaochi / handicap | `module.komaochiPractice.title` / `lessonTrack.handicap.title` | Komaochi / Handicap (Komaochi) | subtitle "Handicappartijen tegen de engine."; `kif.import.preview.handicap %@` "Voorgift: %@"; store "40 voorgiftscenario's, in Komaochi onder Training": **S4** handicap = "handicap" (UI) vs "voorgift" (KIF preview, store) |
| Lessons / tracks | `hub.lessons.title` / `lessonTrack.*.title` | Lessen / Trajecten: Grondbeginselen (Fundamentals), Openingen, Kastelen, Middenspel, Eindspel, Tsume, Handicap (Komaochi), Gevorderd | `module.lessons.subtitle` "Gestructureerd curriculum over acht trajecten."; store "80 lessen" |
| Daily training | `dashboard.todaysTraining` / `module.dailyPlan.title` | Training van vandaag / Dagplan | `training.beginSession` "Sessie beginnen"; `hub.training.exploreModules` "Modules verkennen"; `training.length.*` Express / Kort / Gemiddeld / Lang / Diep |
| Spaced repetition | no UI label | (no UI string; `hub.tesujiCards.markRecalled`) | the page's "Spaced repetition brings misses back" has no catalog string; wording: `training.reflection.5` "Het patroon herkennen wordt makkelijker met herhaling" |
| Boards (7) | `settings.boardTheme.*` | Hon-kaya / Hinoki / Ichō / Donker lak / Oefenmat / Shin-kaya / Walnoot | `settings.3dBoard` "3D-bord"; `settings.boardTheme` "Bordthema"; `settings.boardAndPieces` "Bord & stukken" |
| Piece sets (7) | `settings.pieceSet` / `settings.pieceStyle.*` | Stukstijl / Traditioneel (Kanji) / Internationaal / Schaak | the store: "kies de stukstijl Schaak"; site "Chess" piece set |
| Notation | `settings.notation` | Notatiestijl | `settings.notation.japanese` "Japans (▲７六歩)", `.western` "Westers (P-7f)" |
| KIF import and export | `kif.import.title` / `settings.data.importKIF` / `analysis.share.kifTitle` | KIF importeren / KIF importeren… / KIF delen | `kif.import.confirm` "Importeer" (imperative), `mac.command.copyKIF` "KIF kopiëren", `copySFEN` "SFEN kopiëren"; `kif.import.source.clipboard` "Vanuit klembord" |
| iCloud sync | `settings.sync.title` | iCloud-synchronisatie | `settings.sync.mode.local` "Alleen op dit apparaat"; `settings.sync.upgrade` "Upgrade naar Premium om iCloud-synchronisatie in te schakelen" |
| Game Center | `settings.gc.title` | Game Center | `settings.gc.signInHint` "Meld je aan om mee te doen aan ranglijsten" |
| Support the developer (tips) | `settings.section.support` / `settings.tip.*` | Steun de ontwikkelaar / Koffie, Supporter, Enorme steun | tips are consumables not shared with family |
| Result words | `game.result.*` | Remise / Schaakmat / Opgave / Verslagen / "Remise (zetherhaling)" / "Remise (impasse)" | `sennichite` stays "Sennichite" in status lines; `Resign` → "Opgeven", `Sente (first)` → "Sente (eerste)", `Gote (second)` → "Gote (tweede)" |
| Settings | `settings.title` | Instellingen | `settings.section.data` "Gegevens en privacy" |

### Paid tier names in the Dutch UI

- Title: **Shogiful Premium** (`settings.premium.name`; `Premium`; `Upgrade to Premium` → "Upgraden naar Premium"; `You're Premium` → "Welkom bij Premium"; `Premium via Family Sharing` → "Premium via Delen met gezin"; `settings.premium.active` "Premium actief"; `settings.premium.free` "Gratis plan"; `All features unlocked` → "Alle functies ontgrendeld"; `Limited analysis & training` → "Beperkte analyse en training").
- Plans: `paywall.plan.monthly` → "**Premium maandabonnement**", `paywall.plan.yearly` → "**Premium jaarabonnement**", `paywall.plan.lifetime` → "**Premium levenslang**"; `paywall.purchaseLifetime` → "Levenslang kopen", `paywall.oneTime` → "Eenmalige aankoop", `paywall.currentPlan` "HUIDIG PLAN", `paywall.renewsMonthly` "Verlengt maandelijks", `paywall.billing.then.month` "Daarna %@/maand". Best value: `paywall.bestValue` → "**BESTE KEUS**" (typo for "BESTE KEUZE"; flag S5).
- Trial: `paywall.startTrial` → "Gratis proefperiode starten"; `paywall.trial.compound.format` → "Gratis proefperiode van %lld dagen"; `paywall.trialNote` → "%@, daarna automatische verlenging. Altijd opzegbaar."; `trial.expired.title` "Je gratis proefperiode is afgelopen."; `trial.expired.skip` → "Beperkte gratis toegang gebruiken"; `onboarding.trial.skip` → "Doorgaan met beperkte gratis toegang"; `paywall.subscribeNow` → "Nu abonneren".
- Restore: `paywall.restore` → "Aankopen herstellen"; `paywall.restore.done` → "Hersteld: %@ is actief op deze Apple ID."; `paywall.restore.none` → "Op deze Apple ID staan geen aankopen om te herstellen."; Manage: `settings.premium.manage` → "Abonnement beheren".
- Family Sharing: `paywall.familySharing.sheet.title` → "Delen met gezin"; "De levenslange ontgrendeling is ook deelbaar — één keer kopen, ieder gezinslid krijgt Premium." (the English says "Premium Lifetime" can be shared; matches the page's "Family Sharing included").
- Free-tier labels in the Dutch UI: "Gratis plan", "Gratis proefperiode". Paywall benefits: "Vind elke fout in elke partij", "Train je zwaktes met tsume en gerichte oefeningen".

### Dutch App Store listing (https://apps.apple.com/nl/app/shogiful-japans-schaken/id6761656926, checked 2026-11-19)

- Name: **Shogiful: Japans schaken** (lookup `trackName`).
- Subtitle: **Shogi: tactiek & AI-analyse**.
- Category: **Bordspel** (iTunes lookup `primaryGenreName`: "Games"). Price "Gratis", age 4+, size 149 MB, iOS 18.0 or newer, plus iPad and Mac. Talen: "Nederlands en 32 andere".
- IAP rows: `Premium jaarabonnement € 9,99`, `Premium maandabonnement € 1,99`, `Supporter € 5,99`, `Enorme steun € 9,99`, `Koffie € 1,99`, `Premium levenslang € 22,99` (reference only).
- Description: **Dutch**, je-form ("Shogiful is je persoonlijke shogitrainer."). Vocabulary: "de YaneuraOu-engine op je iPhone of iPad analyseert elke zet", "501 tsume-problemen", "KLIM OP LANGS 40 TEGENSTANDERS", "381 los je gratis op, en Premium voegt er 120 aan toe", "99 inzetoefeningen", "62 burchtoefeningen", "55 joseki-oefeningen", "30 tesuji-kaarten", "62 yose-races", "40 voorgiftscenario's, in Komaochi onder Training", "80 lessen", "kies de stukstijl Schaak", "Live partijen kun je ook op een 3D-bord spelen", "Spelen is gratis en onbeperkt. Daarnaast krijg je elke dag 2 partijanalyses, 3 puzzels en 2 coachhints zonder kosten", "Premium maandabonnement en Premium jaarabonnement beginnen met een gratis proefperiode van 1 week", "Premium levenslang is een eenmalige aankoop", "Delen met gezin". Shogi is explained as "het Japanse schaakspel".

---

### Cross-app terms (how the five apps write recurring words in Dutch)

| Concept | Observa | Pawza | RightSplit | Shogiful | Note |
|---|---|---|---|---|---|
| Subscription | Abonnement ("Abonnement beheren") | Abonnement ("Abonnement beheren") | Abonnement ("Abonnement beheren") | Abonnement ("Abonnement beheren") | consistent; plans "maandabonnement/jaarabonnement" (Observa CTA, Shogiful plan names, store rows) |
| Monthly / yearly | Maandelijks / Jaarlijks | Pro (maandelijks) / Pro (jaarlijks) | Maandelijks, Pro+ Jaarlijks | Premium maandabonnement / Premium jaarabonnement | |
| Lifetime | Levenslang (+ "Lifetime Access" left in) | Levenslang | Levenslang (+ "Lifetime" in one string) | Levenslang | store: Observa "eenmalige aankoop", Pawza "eenmalig" |
| One-time | Eenmalige aankoop | Levenslang: eenmalige aankoop | Eenmalige aankoop | Eenmalige aankoop | |
| Free trial | Gratis proefperiode (starten) | 7 dagen gratis proberen | %lld dagen gratis proberen | Gratis proefperiode (starten) | two forms ("proefperiode" vs "gratis proberen") |
| Restore purchases | Herstel aankopen | Herstel aankopen | Aankopen herstellen | Aankopen herstellen | imperative vs infinitive |
| Best value | Beste waarde | (none) | Beste waarde | BESTE KEUS | |
| Family Sharing | Delen met gezin | Delen met gezin | (store only) | Delen met gezin | Apple's Dutch name |
| Sync / iCloud | gesynchroniseerd / Back-up | iCloud-synchronisatie | (none: no cloud sync) | iCloud-synchronisatie | "iCloud-account", "iCloud" hyphenated compounds |
| Health | "Apple Health" (main), "Apple Gezondheid" (InfoPlist) | "Gezondheid" (screen), "dierenarts" | n/a | n/a | Apple's name is "Gezondheid" |
| Widget | widget | widget | widget | n/a | "Widgets op je beginscherm en toegangsscherm" |
| Home / Lock Screen | beginscherm / toegangsscherm | begin- of toegangsscherm; "toegangsscherm" | Beginscherm / "toegangsscherm" and "vergrendelscherm" | n/a | Apple: beginscherm / toegangsscherm |
| Settings | Instellingen | Instellingen | Opties (Settings screen name varies) | Instellingen | |
| Export | Rapport exporteren, Delen als PDF | Exporteer je gegevens | Csv exporteren, Pdf exporteren ("Csv", "Pdf" lowercase) | n/a (KIF importeren / KIF delen) | RightSplit writes "Csv"/"Pdf" lowercase, other apps "CSV"/"PDF" |
| Privacy | Privacy en machtigingen | Privacy | Privacy / Privacybeleid | Gegevens en privacy / Privacybeleid | |
| Done / Cancel | n/a | Gereed / Annuleer | Gereed / Annuleer | Klaar / Annuleren | "Gereed" vs "Klaar" |
| Save | n/a | Bewaar | Opslaan / Wijzigingen bewaren | n/a | bewaren vs opslaan |
| Log / record | loggen (Water loggen) | loggen / vastleggen / Log zorg | noteren ("Noteer", "%@ noteren"), "registreren" | n/a | |
| Pet words | n/a | huisdier / dier, dierenarts, vaccinatie/vaccin/booster, medicijn, symptoom, verzorgingslogboek, noodkaart, oppasmap, penning | n/a | n/a | "vaccinatie" in app, "enting" in store subtitle |
| Split / bill words | n/a | n/a | verdelen / splitsen / delen; rekening; bon; fooi; ruimte; afrekenen / vereffenen / quitte; reeks (streak) | n/a | RightSplit |
| Shogi terms | n/a | n/a | n/a | Sente / Gote, tsume, tesuji, yose, joseki, komaochi, kyu/dan, sennichite, KIF, SFEN; drop = inzet; castle = kasteel/burcht; promotion = promotie; Loper/Toren/Paard/Lans/Pion/Gouden generaal/Zilveren generaal; mate = mat; checkmate = schaakmat | |

Shared Apple names to confirm in `nl-apple-terms.md`: Delen met gezin, Instellingen, Gezondheid, toegangsscherm, beginscherm, Bedieningscentrum (Control Center), Sleutelhanger (Keychain), Meldingen, Herstel aankopen.

---

### Flags (app-side string bugs worth an issue)

Mockly
- **M1/M2/M3** above (no Dutch UI; English store metadata; translation packs not on sale).

Observa
- **O1 (register mix, high):** about 490 u/uw strings in a je app; onboarding headlines and explainer sentences use u (`onboarding_welcome_headline` "Begrijp wat uw lichaam u vertelt", "HRV ligt binnen uw gebruikelijke bereik."), the rest je. App-side fix; the site writes je.
- **O2 (readiness, two words):** `Readiness` is "Gereedheid" (107 values) and "paraatheid" (55 values: `Moderate Readiness` "Matige paraatheid"); the store subtitle says "Paraatheid". The site: Gereedheid.
- **O3 (Apple Health name):** "Apple Health" (64 values) vs "Apple Gezondheid" (InfoPlist, 6 values); Apple's Dutch app is "Gezondheid".
- **O4 (baseline):** "basislijn" (138) vs "referentie…" (49) vs "gebruikelijk/normale bereik" (25); `Your Baseline` "Uw basislijn" next to `Building Your Baseline` "Je basislijn wordt opgebouwd".
- **O5 (sleep debt):** "slaapschuld" 27 vs "slaaptekort" 11; `Moderate Debt` "Matige schuld".
- **O6 (resting heart rate):** "rusthartslag" 82 vs "rustpols" 34.
- **O7 (Strain vs Load):** both collapse to "Belasting".
- **O8 (typo):** `Workout Replay` → "Trainingsherhalig" (3 strings; should be "Trainingsherhaling").
- **O9 (case):** Watch tab labels `watch.domain.patterns` / `watch.insights.patterns` → "patronen" (lowercase), iPhone tab "Patronen"; `guidance_category_explore` → "sterk" (en "Strong", lowercase).
- **O10 (stage names):** "Slaapstadia" (main) vs "Slaapfases/slaapfasen" (widgets, store).
- **O11 (check-in):** "Ochtendcheck-in" / "Ochtendcheck" / "Check" for one feature.
- **O12 (premium compounds):** "premium-toegang" / "premiumtoegang" / "premium-abonnementsopties" / "Premium-functies".
- **O13 (English left in):** `Unlock Lifetime Access` → "Ontgrendel Lifetime Access" next to `onboarding_paywall_lifetime_cta` "Ontgrendel levenslange toegang".
- **O14 (Siri):** `Log water in ${applicationName}` has no `nl` value; 4 more phrases and 12 `insight_signal_*` labels are `needs_review`.
- **O15 (store):** store subtitle "Paraatheid, Slaap-Cyclus-Coach" (odd capital hyphen compound); store name uses "Herstelscore" while the app headline score is Gereedheid.

Pawza
- **P1 (permission prompts, high):** camera and photo-library usage descriptions are English-only build settings; no InfoPlist catalog. Add `InfoPlist.xcstrings` with `NSCameraUsageDescription` and `NSPhotoLibraryUsageDescription`.
- **P2:** dier vs huisdier ("Dier toevoegen" / "Huisdieren").
- **P3:** care = verzorging / zorg ("Verzorging vastleggen", Siri "Log zorg", "Zorgtype", "Zorgreeks", "Verzorgingslogboek").
- **P4:** imperatives vs infinitives side by side ("Voeg een medicijn toe" / "Medicijn toevoegen", "Exporteer" / "Exporteren", "Importeer eerdere records").
- **P5:** untranslated loanword "Record(s)" (40+ strings) vs store "dossier".
- **P6:** two names for the vet PDF ("PDF dierenartsbezoek" vs "dierenarts-PDF").
- **P7:** hyphen compounds "Vermist-kit", "Vermist-poster" (Dutch closed compound would be "Vermistkit", "Vermistposter"); "Snel-logknop".
- **P8:** store says "bedieningspaneel" for Control Center (Apple: "Bedieningscentrum").
- **P9:** debug strings reach the catalog and UI: "Pijplijnfasen: vastleggen → OCR → … (tier `fullAI`)", "CloudKit wordt geactiveerd zodra de iCloud-rechten zijn toegevoegd.", "iCloud-synchronisatie: nog niet ingeschakeld in deze build.".
- **P10:** "back-up" vs "reservekopie" in the same export strings.
- **P11:** "Gratis accounts" in three strings although the app has no account.
- **P12:** "Support" left identical to English in one string while the app writes "ondersteuning" elsewhere; Siri phrase `Log ${kind} in ${applicationName}` identical to English.
- **P13 (store):** subtitle "Enting, gewicht & herinnering" ("enting" Flemish-leaning; the app says "vaccinatie").
- **P14:** `Toilet` → "Behoefte" in the log vs "toiletbezoek" / "plasrondjes" in widget and store copy; `Up next` → "Hierna".

RightSplit
- **R1 (Siri):** spoken phrases are English only (no AppShortcuts catalog); shortcut titles are Dutch ("Reken deel" is an odd title for "Split a bill").
- **R2:** "bon" vs "bonnetje".
- **R3:** verdelen / splitsen / delen and imperative vs infinitive buttons ("Voeg toe", "Wijzig", "Verwijder", "Bewerk reis" vs "Ruimte bewerken", "Persoon toevoegen").
- **R4:** splitsing vs verdeling for the noun "split".
- **R5:** artikel / item / post.
- **R6:** `Tax` → "Belasting" on EU receipts that show btw.
- **R7:** "Fooi percentage" (should be "Fooipercentage").
- **R8:** afrekenen / vereffenen / quitte.
- **R9:** `owes` → "betaalt", `owed` → "ontvangt"; `Balance` and `Net` both "Saldo".
- **R10:** Pay Me spelled "Betaal mij" / "Pay-Me-kaart" / "Pay Me".
- **R11:** "vergrendelscherm" vs "toegangsscherm".
- **R12:** `Rail` → "Platform" (wrong meaning).
- **R13:** `Unlock Pro+ Lifetime` → "Pro+ Lifetime ontgrendelen" (English left in) vs `Pro+ Lifetime` → "Pro+ Levenslang".
- **R14 (store):** IAP row "RightSplit Pro+ jaarabo" is cut off mid-word (store-side); the store description says "18 widgets", which equals the English page's 12 free plus 6 more with Pro+.

Shogiful
- **S1:** "Trail" and `lessonTrack` both "traject".
- **S2:** drop = inzet / zet neer / werp in / inworp.
- **S3:** kasteel (UI) vs burcht (prose, store).
- **S4:** handicap vs voorgift.
- **S5 (typo):** `paywall.bestValue` "BESTE KEUS" (should be "BESTE KEUZE").
- **S6:** `dashboard.accuracy %lld` has an empty `nl`.
- **S7:** `piece.bishop.promoted` English "Horse" becomes "Gepromoveerde loper"; the Japanese/English "Dragon Horse" naming is lost on one side of the pair (Dragon → "Draak" but Horse → "Gepromoveerde loper").
- **S8:** InfoPlist has no `nl` (display name only; harmless).
- **S9:** "Klaar" for Done here vs "Gereed" in Pawza and RightSplit; "Annuleren" vs "Annuleer".


---

## Dutch glossary, batch 4: soon, tare, taskful-day, wanderwiki, xiangqiful, clippet

Method (checked 2026-11-19). Read-only extraction from each app's string catalogs under `~/Downloads/` (`countdown/`, `weightbalance/`, `TaskLogger/`, `WanderWiki/`, `Xiangqi/`, `clipboard/`). Every catalog is `.xcstrings` (parsed as JSON with `python3 -I`); none of the six apps has legacy `nl.lproj` `.strings`/`.stringsdict` files. The Dutch locale code is plain `nl` everywhere (no `nl-NL`), and no catalog has a `needs_review` Dutch value. "total" = translatable keys (`shouldTranslate: false` and blank keys excluded; stale keys are counted, the stale number is given); "nl" = keys with an `nl` value (plural variations counted once). "Identical to English" counts values equal to the English value or key, most of which are brands, loanwords or format strings (the real English leftovers are named under Flags). Register counts are rough regexes on the Dutch values (je/jij/jou/jouw/jezelf/jullie vs u/uw/uzelf), every u/uw hit hand-checked. Dutch strings are verbatim (curly or straight quotes as in source). App Store data: iTunes lookup (`country=nl&lang=nl_nl`) plus the `serialized-server-data` JSON of `apps.apple.com/nl/app/id<ID>` (Safari UA, `Accept-Language: nl-NL`, `curl -sL`; four pages needed one 60 s wait after HTTP 429). The listing page also prints the seller's personal name; it is not copied here. Prices below are reference only: the site prints prices from the catalog / `MASTER-prices.csv`. The Dutch App Store prints Family Sharing as `Delen met gezin`.

Register across the six apps: **all six write je/jij** (no mix of forms except one string in Taskful Day, see its Register note). Imperative buttons are the bare stem in Soon, Taskful Day (a few), WanderWiki and Clippet ("Voeg toe", "Verwijder", "Bewaar", "Annuleer"), the infinitive in Tare, Xiangqiful and most of Taskful Day ("Taak toevoegen", "Annuleren"). Both styles occur inside the same catalog in Soon ("Voeg foto toe" vs "Foto aanpassen"), which is a style mix, not a register mix.

---

### 1. Soon. (`soon`, source `countdown/`, ID 6757280643)

### Dutch coverage
- `countdown/Localizable.xcstrings`: 741 total (87 stale) / 741 `nl`, 43 identical to English (Home, Premium, Widget, Baby, Concert, Sport, Story, Tips, the brand lines "Soon." / "Soon. Feedback" / "Soon. — feedback"). Stale keys are unused leftovers, so the live set is about 654.
- `CountdownWidgets/Localizable.xcstrings` (widgets, Live Activity, Control Center): 184 total (8 stale) / 182 `nl`; the 2 gaps are format-only keys (`%@ `, `%@ %@`). 40 identical: all 22 widget gallery names stay English ("Soon · Ring", "Soon · Rotating Stack", "Soon · StandBy", "Soon · Streak", "Soon · Year", "Soon · Timeline Full", "Soon · Lock Row" and so on), plus "Countdown", "Gate", "Moment", "Premium", "Stop".
- `countdown/AppShortcuts.xcstrings` (Siri): 13 / 13, 1 identical ("Open ${event} in ${applicationName}"). Phrases are je-neutral imperatives ("Voeg een aftelling toe in ${applicationName}", "Hoeveel dagen tot ${event} in ${applicationName}", "Toon mijn volgende moment in ${applicationName}", "Wat is het volgende in ${applicationName}"). Siri phrases ARE in Dutch.
- `countdown/InfoPlist.xcstrings`: 6 / 5 (missing: the key `Soon`, a display-name helper); calendar and location prompts translated ("Soon. leest je agenda-afspraken zodat je ze kunt omzetten naar aftelmomenten…", "Locatie wordt gebruikt om weersvoorspellingen te tonen voor je aftelevenementen…").
- Paywall (`Go Premium`, `Restore Purchases`, trial and renewal terms) all translated. No English-only gap that matters.
- **Verdict: app is in Dutch: yes** (widget gallery names excepted).

### Register
- je-marked values: about 70 of 741 in the main app and 34 of 184 in widgets; u/uw: 0. Examples: "Voeg je eerste moment toe", "Wil je een korte review achterlaten?", "Jouw moment", "Dagen tot jouw moment — altijd zichtbaar.", "Je moment heeft een naam nodig.". Both "je" and emphatic "jouw" appear ("Jouw beginscherm, jouw momenten."). No mix with u.

### Glossary
| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Moment(s) | Moment / Moments | Moment / Momenten | kept; the onboarding line "Elk moment is het wachten waard." |
| Countdown | Countdown (`Countdown`) | Aftelling | 68 values use "aftel-"; widget key `Countdown` stays "Countdown" and "Remove this countdown from the Lock Screen." = "Verwijder deze countdown van het toegangsscherm." (3 values with "countdown"). Use "aftelling" |
| Counts up / count-up / days since | Days since / count-up | dagen geleden; "optelling"; "telling" | `Pin a count-up to see your streak` = "Zet een optelling vast om je reeks te zien"; `Every day since your count-up began` = "Elke dag sinds je telling begon" (optelling vs telling) |
| Plan mode / Plan (tab) | Plan | Planning | The tab/button `Plan` = "Planning", but `Tap Plan to see yours.` = "Tik op Plan om die van jou te zien." (uses "Plan"); `Plan mode reminders` = "Herinneringen voor planmodus"; `Plan this moment` = "Dit moment plannen". Pick one for the tab: "Planning" |
| Checklist | Checklist | Checklist | |
| Timeline | Timeline | Tijdlijn | |
| Milestone | Milestone | Mijlpaal | `Add milestone` = "Mijlpaal toevoegen" |
| Reset to suggestions | Reset to suggestions | Terugzetten naar voorstellen | |
| Memory / Memories | Memory / Memories | Herinnering / Herinneringen | **Collision:** `Reminders` is also "Herinneringen" (see Flags) |
| Reminders | Reminders | Herinneringen | `Remind me` = "Herinner mij"; `Turn on reminders` = "Herinneringen inschakelen" |
| On This Day | ON THIS DAY / Remind me on this day | OP DEZE DAG / Herinner me op deze dag | `Anniversary reminders` = "Herinneringen op deze dag"; widget `On this day memory: %@` = "Herinnering op deze dag: %@" |
| Final Countdown (Live Activity) | Final Countdown | Laatste aftelling | `LIVE COUNTDOWN` = "LIVE-AFTELLING" |
| Keep on Lock Screen | Keep on Lock Screen | Op vergrendelscherm houden | the same Live Activity text says "vergrendelscherm"; the widget strings say "toegangsscherm" (see Lock Screen row) |
| Lock Screen | Lock Screen | vergrendelscherm (2 values) / toegangsscherm (5 values) | **Inconsistent:** `Your countdown on Home Screen and Lock Screen.` = "Je aftelling op het beginscherm en vergrendelscherm."; `Every Home Screen & Lock Screen widget` = "Alle widgets op het beginscherm en toegangsscherm"; `A glanceable countdown row for your lock screen.` = "…voor je toegangsscherm". Apple's Dutch is "toegangsscherm"? No: Apple uses "toegangsscherm" for the Lock Screen in iOS; "vergrendelscherm" is the older/colloquial form. Check Apple's term before the site fixes one |
| Home Screen | Home Screen | beginscherm | 7 values; `Put it on your\nhome screen.` = "Zet het op je\nbeginscherm." |
| StandBy | Soon · StandBy / StandBy | StandBy | `Massive bedside countdown tuned for StandBy mode.` = "Een enorme nachtkastje-aftelling, afgestemd op StandBy-modus." |
| Dynamic Island | Dynamic Island | Dynamic Island | kept in English |
| Control Center control | Choose which event the control shows. | bediening (generic) | "Control Center" itself does not appear in a Dutch value; Apple's NL name is Bedieningscentrum |
| Widget | Widget | Widget | 29 values; compounds "Widget-voorkeuren", "Widget-diagnose", "Widgetweergave"; `Share as widget` = "Deel als widget" |
| Widget names (26 widgets) | Soon · Ring, Rings, Month, Year, Timeline, Streak, Ticket, Hero, Horizon, Agenda, Dots, Inline, Clean… | unchanged, English | Gallery names are English; descriptions are Dutch ("Een voortgangsring voor je volgende moment.", "Een visuele tijdlijn van je volgende momenten.", "Zeven prachtige gestapelde aftelkaarten.") |
| Streak widget | Day streak / day streak | Dagenreeks / dagen op rij | `%1$lld day streak for %2$@` = "Reeks van %1$lld dagen voor %2$@": three forms (Dagenreeks, Reeks, dagen op rij) |
| Pin / pinned moment | Pin / Pinned / Pin multiple moments | Vastpinnen / Vastgemaakt / Meerdere momenten vastpinnen | `Keep this moment on the hero card.` = "Houd dit moment op de hoofdkaart."; widget text uses "vastgezet" ("Je vastgezette moment verschijnt…") vs "Vastgemaakt" (label) |
| Theme | Theme | Thema | `All themes unlocked` = "Alle thema's ontgrendeld" |
| Photo | Photos | Foto's | `Add Photo` = "Voeg foto toe" |
| Weather forecast | Weather forecast | Weersvoorspelling | `Smart weather forecast` = "Slimme weersvoorspelling"; `Weather` = "Weer"; `Powered by Apple WeatherKit` stays English; `Weather data provided by Apple Weather` = "Weergegevens geleverd door Apple Weather" (Weergegevens reads like "display data") |
| Daily notes (Calm / Playful) | Personalized daily notes / Calm / Playful | Persoonlijke dagelijkse notities / Rustig / Speels | `Tone` = "Toon" |
| Baby mode | Baby | Baby | the catalog string is "Baby"; `Week 20 · anatomy scan` = "Week 20 · 20-wekenecho", `Week 12 · first trimester ends` = "Week 12 · Einde eerste trimester" |
| Search | Search | Zoeken | `Try searching` = "Probeer te zoeken" |
| Calendar import | Import from your calendar / Turn calendar events into countdowns | Importeren uit je agenda / Agenda-evenementen omzetten in aftellingen | "agenda" for the calendar app/data |
| Siri / Spotlight | `${applicationName}` phrases | see coverage | |
| Share cards | Share / Share moment / Share without a watermark | Delen / Deel moment / Delen zonder watermerk | `Story` stays "Story" |
| iCloud Sync | iCloud Sync | iCloud-synchronisatie | hyphen compound; `Syncing` = "Synchroniseren", `Sync issue — will retry automatically` = "Synchronisatieprobleem — probeert automatisch opnieuw" |
| Export / Delete my data | Export My Data / Delete All My Data | Mijn gegevens exporteren / Al mijn gegevens verwijderen | `Download all your data as JSON` = "Download al je gegevens als JSON" |
| Settings | Settings | Instellingen | |
| Free | Free | Gratis | |
| Family Sharing | One subscription covers your whole Family Sharing group. | Eén abonnement dekt je hele Delen met gezin-groep. | Apple's name "Delen met gezin" |

### Paid tier names in the Dutch UI
- Tier: **Premium** (`Go Premium` = "Ga Premium"; `Unlock all features` = "Ontgrendel alle functies"; `Premium Status` = "Premiumstatus"; `Premium feature` = "Premium-functie"). Widgets also have a "Soon.+" label (`Unlock Soon.+` = "Soon.+ ontgrendelen", `Soon +`) that the site never mentions.
- Periods: Maandelijks / Jaarlijks / Levenslang (`Lifetime` = "Levenslang"); `One-time purchase` = "Eenmalige aankoop"; `One time — yours forever` = "Eenmalig — voor altijd van jou"; `%@/month` = "%@/maand"; `%@ / month, billed yearly` = "%@ / maand, jaarlijks gefactureerd"; `Save 50%` = "Bespaar 50%"; `Best value` = "Beste waarde" (calque; WanderWiki says "Beste deal").
- Trial: `Free trial` = "Gratis proefperiode"; `1 week free` = "1 week gratis"; `%lld days free` = "%lld dagen gratis"; `Cancel anytime` = "Op elk moment opzegbaar"; `Billed monthly — cancel anytime` = "Maandelijks gefactureerd — op elk moment opzegbaar"; `Auto-renews until cancelled.` = "Automatische verlenging tot opzegging."
- Restore: `Restore Purchases` = "Aankopen herstellen"; `Already paid? Restore here` = "Al betaald? Herstel hier"; `Purchases Restored` = "Aankopen hersteld". `Manage Subscription` = "Abonnement beheren". Terms: `Privacy Policy` = "Privacybeleid", `Terms of Use` = "Gebruiksvoorwaarden".
- Tip jar: `Support the Developer` = "Ondersteun de ontwikkelaar", `TIP JAR` = "FOOIENPOT", `One-time tip. Not a subscription.` = "Eenmalige fooi. Geen abonnement."

### Dutch App Store listing (checked 2026-11-19)
- Name: **Soon. - Dagen Tot Grote Events** (English "Soon. - Countdown"-style name; Dutch "events" is an anglicism and "Grote" is title-cased).
- Subtitle: **Bruiloft, Reis & Baby Aftellen**.
- Description is in Dutch: "Er komt iets moois aan. Soon. houdt het in beeld, zodat de datum waar je naar uitkijkt op je beginscherm en toegangsscherm staat…" (store text says "toegangsscherm", "aftellen", "moment", "gratis proefperiode van 1 week", "Delen met gezin"). Free, 36 languages ("Nederlands en 35 andere"). IAP rows: `Ondersteun de ontwikkelaar € 1,00`, `Premium eenmalige aankoop € 14,99`, `Premium maandabonnement € 1,99`, `Premium jaarabonnement € 9,99`.

---

### 2. Tare (`tare`, source `weightbalance/`, ID 6806255929)

### Dutch coverage
- `weightbalance/Localizable.xcstrings`: 121 total / 121 `nl`, 0 stale, 7 identical ("Feedback", "Hint", "Hints", "Level %lld", "Privacy", "Tare", format keys). **100 %.** 50 languages in the catalog.
- No Siri phrases, widgets or InfoPlist usage strings exist (the game asks for no permissions; no `INFOPLIST_KEY_NS…` key in the project). The puzzle itself has no words, so the catalog is the unlock screen, Settings, chapter names, accessibility labels and VoiceOver actions.
- **Verdict: app is in Dutch: yes.**

### Register
- je-marked: 1 ("Nog %1$@ hoofdstukken met handgemaakte levels. Voor altijd van jou."). u/uw: 0. The rest is neutral (infinitive buttons "Hoofdstuk %lld openen", "Tare delen", "Level opnieuw starten"; "Dubbeltik om te selecteren."). No mix.

### Glossary
| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Level | Level %lld | Level %lld | kept English ("level"); `Level %lld, solved` = "Level %1$lld, opgelost" |
| Chapter | Chapter %lld | Hoofdstuk %lld | `Chapter complete` = "Hoofdstuk voltooid"; `Open Chapter %lld` = "Hoofdstuk %lld openen" |
| Chapter I / Chapters II to X | `Buy Chapters %lld to %lld, %@` | Hoofdstuk %1$lld tot %2$lld kopen, %3$@ | **Defect:** singular "Hoofdstuk" before "tot" (the sibling `Open Chapters %lld to %lld` correctly says "Hoofdstukken %1$lld tot %2$lld openen"). The store IAP is named "Hoofdstukken II–X" |
| Chapter names (The Hang … The Retrospective) | The Secret, The Cascade, The Exhibition, The Forgery, The Fulcrum, The Hang, The Inventory, The Ledger, The Restoration, The Retrospective | Het Geheim, De Cascade, De Tentoonstelling, De Vervalsing, Het Draaipunt, Het Ophangen, De Inventaris, Het Kasboek, De Restauratie, De Terugblik | The Hang = "Het Ophangen" |
| World names | Morning Sky, Twilight Meadow, Deep Sea, Evening Stars, Rose Dawn, Firefly Forest, Coral Reef, Polar Night, Sunset Hills, Summer Fields | Ochtendhemel, Schemerweide, Diepzee, Avondsterren, Roze dageraad, Vuurvliegjesbos, Koraalrif, Poolnacht, Heuvels bij zonsondergang, Zomervelden | `Canvas` = "Doek"; `Automatic, each chapter its own world` = "Automatisch, elk hoofdstuk zijn eigen wereld" |
| Hanging mobile | Mobile | Mobiel | **Defect risk:** "Mobiel" is the Dutch word for a mobile phone; the art object (hangmobiel / mobile) is not clear. The catalog uses "Mobiel" as a label for the structure |
| Beam | Beam %lld | Balk %lld | `Beam %lld, hanging from Beam %lld` = "Balk %1$lld, hangt aan balk %2$lld" |
| Notch | notch %lld | inkeping %lld | "%@ arm, notch %lld" = "%1$@ arm, inkeping %2$lld" |
| Hook | empty hook / Every hook filled. Not balanced. | leeg haakje / Alle haakjes bezet. Niet in evenwicht. | |
| Weight | weight %lld | gewicht %lld | |
| Hidden weight ("?") | hidden %@ / cannot settle, hidden weight | %@, verborgen gewicht / kan niet tot rust komen, verborgen gewicht | |
| Tray | Tray / Return to tray | Bak / Terug in de bak | `%@ returned to the tray.` = "%@ terug in de bak." |
| Picture cards | (no catalog string) | none | The card art has no words; no Dutch term exists in the app. The store text and site need their own wording |
| Reference scale | Reference scale | Referentieweegschaal | `…tilted, left side heavier.` = "Referentieweegschaal, gekanteld, linkerkant zwaarder." |
| Balanced | Balanced / Balanced. Level complete. | In evenwicht / In evenwicht. Level voltooid. | |
| Hint(s) | Hint / Hints | Hint / Hints | kept English; `Suggested placement` = "Voorgestelde plek" |
| Stars (the "three gold stars") | Marks | Sterren | The English key is "Marks"; Dutch is "Sterren" |
| Sound / Haptics | Sound / Haptics | Geluid / Trillingen | "Trillingen" means vibrations; Apple's Dutch Settings name for haptics is "Haptiek" (verify before the site uses "trillingen" for the feature) |
| High contrast | High contrast | Hoog contrast | |
| Settings | Settings | Instellingen | |
| Pause / Resume | Pause / Resume | Pauze / Doorgaan | `Paused` = "Gepauzeerd" |
| Play | Play | Spel | **Defect (low):** the verb "Play" is the noun "Spel"; "Spelen" expected |
| Left / Right | Left / Right | Linker / Rechter | bare adjective; the labelled forms say "Links"/"Rechts" |
| Restart level | Restart level | Level opnieuw starten | |
| Exit to grid | Exit to grid | Terug naar het overzicht | |
| Share / Rate | Share Tare / Rate Tare | Tare delen / Tare beoordelen | |
| Privacy | Privacy | Privacy | |

### Paid tier names in the Dutch UI
- There is no "Full Access" or tier name in the catalog; the unlock is sold as chapters: `%@ more %lld chapters of handcrafted levels. Yours forever.` = "Nog %1$@ hoofdstukken met handgemaakte levels. Voor altijd van jou." (plural rule: hoofdstuk / hoofdstukken); `Buy Chapter %lld, %@` = "Hoofdstuk %1$lld kopen, %2$@"; `%lld chapters open in order, as Chapter %@ did.` = "Het opent / Ze openen op volgorde, net als hoofdstuk %2$@."; `Level %lld, not purchased` = "Level %lld, niet gekocht"; `Level %lld, locked` = "Level %lld, vergrendeld".
- Restore: `Restore purchases` = "Aankopen herstellen". Failure: `The store did not answer.` = "De store gaf geen antwoord." No trial, no subscription, no Family Sharing string. `Terms of use` = "Gebruiksvoorwaarden".

### Dutch App Store listing (checked 2026-11-19)
- Name: **Tare: Balans & Logica Puzzel**. Subtitle: **Denkspel & geheime gewichten**. Description is in Dutch ("Hang de gewichten op tot elke balk in evenwicht is. Tare is een woordloze balanspuzzel met 200 met de hand gebouwde levels…"; heading "ÉÉN REGEL"). Free, 44 languages ("Nederlands en 43 andere"). IAP: `Hoofdstukken II–X € 2,99`.

---

### 3. Taskful Day (`taskful-day`, source `TaskLogger/`, ID 6757345400)

### Dutch coverage
- `TaskLogger/Localization/Localizable.xcstrings` (iPhone, iPad, Mac): 1427 / 1427 `nl`, 1 stale, 74 identical (mostly "Taskful Day", "Taskful Day Pro", "Inbox", "Checklist", "Week", "Focus", "Status", "Filters", "Intelligence", "Momentum", "Heatmap", "Fitness", "Ember", "Mint", "Recent", "Details").
- `TaskLoggerWidgetsExtension/Localizable.xcstrings`: 420 / 420, 3 stale, 25 identical. `TaskfulDayKit/…/Localizable.xcstrings` (Watch and shared): 114 / 112; the 2 gaps are "End focus session" and "Extend focus session", which have no translation in any language (probably unused or code-only keys). `TaskLoggerWidgetsExtension/InfoPlist.xcstrings` 3 / 3.
- `TaskLogger/AppShortcuts.xcstrings`: 12 / 12; Watch `AppShortcuts.xcstrings`: 4 / 4. Siri phrases ARE in Dutch and je-neutral ("Taak toevoegen aan ${applicationName}", "Hoeveel taken heb ik in ${applicationName}", "Wat moet ik doen in ${applicationName}", "Herinner me in ${applicationName}", "Vastleggen in ${applicationName}").
- `TaskLogger/InfoPlist.xcstrings`: 7 / 7. The four permission prompts (calendar, microphone, Reminders, speech recognition) are Dutch and je: "Toon je agenda-afspraken naast je taken, zodat je hele dagplanning op één plek staat.", "Taskful Day gebruikt de microfoon om snel taken aan te maken met je stem.", "Taskful Day kan je Apple Herinneringen importeren zodat je je dag op één plek kunt plannen." ("Apple Herinneringen": Apple's app is called "Herinneringen").
- **Verdict: app is in Dutch: yes.**

### Register
- je-marked: about 184 in the main catalog, 27 in widgets, 8 in the kit, 4 in InfoPlist. **u/uw: 1 real hit**, `notification.limit.message` = "Uw apparaat kan maximaal 60 actieve herinneringen bevatten. De dichtstbijzijnde herinneringen worden bewaard…" (formal; the only one, the rest of the catalog writes je). Everything else: "Hoe vaak je afmaakt wat je plant", "Uitstekend ritme — je bent er consequent bij.", "Je hebt de limiet voor gratis taken bereikt.". Imperatives mix infinitive and bare stem ("Taak toevoegen" vs `tab.add` "Voeg toe").

### Glossary
| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Today (list) | Today (`date.today`) | Vandaag | |
| Tomorrow / Later | Tomorrow / Later | Morgen / Later | Inbox chips |
| Inbox | Inbox (`inbox.list.title`) | Inbox | `Quick capture to Inbox` = "Snel vastleggen in inbox" (lowercase) |
| Capture / Quick Capture | Quick Capture (`pad.sidebar.quick_capture`) | Snel vastleggen | `Voice capture` = "Spraakinvoer"; `Add a task` bar = "Taak toevoegen" |
| Natural-language capture | Quickly add a task using natural language | Voeg snel een taak toe met natuurlijke taal | |
| Carry forward | Carry forward / Carry Forward / Auto carry forward | Doorschuiven / Doorschuiven / Automatisch doorschuiven | **Mixed terms** for one feature (14 "doorschuiven/doorgeschoven", 3 "verplaatsen naar vandaag", 7 "naar vandaag halen"): `batch.carry_forward` "Move to Today" = "Verplaats naar vandaag"; `analytics.tasks_carried_forward` = "Doorgeschoven taken"; `settings.auto_carry_forward.title` "Move pending tasks forward" = "Openstaande taken doorschuiven"; `auto_carry_forward.migration.title` = "Onafgemaakte taken gaan nu automatisch mee naar de volgende dag."; `widget.a11y.carry_forward` "Bring %@ to today" = "%@ naar vandaag halen"; `pad.meta.rolled` "moved %d×" = "verplaatst %d×". The site's "carry forward" maps best to "doorschuiven" |
| Overdue | Overdue | Te laat | `No carried forward tasks` = "Geen doorgeschoven taken" |
| Pending / Completed | Pending / Completed | Openstaand / Voltooid | |
| Done | Done | Klaar (24) / Gereed (2) | `action.dismiss` "Done" = "Gereed" vs `common.done` = "Klaar" |
| Check-in (follow-up reminder) | Check-in / Check in / Check-ins / Check Later / Check back on / Follow-up | Controle / Nu controleren / Controles / Later opvolgen / Opvolgen op / Opvolging | **At least six names for one feature** (see Flags, I-0197). `followup.checkin.title` = "Controle", `followup.checkins.section.title` = "Controles", `followup.checkin.button` "Check in" = "Nu controleren", `followup.label` "Check later" = "Opvolgen", `followup.section.title` "Check Later" = "Later opvolgen", `followup.date.picker.title` "Check Back Date" = "Opvolgdatum", `followup.notification.body` = "Wil je "%@" controleren?", `followup.pro.limit.description` = "De gratis versie bevat 1 actieve controle. Upgrade voor onbeperkte controles.", `pad.canvas.followup.date` "Check on" = "Check op", `pad.canvas.followup.enabled` "Check back later" = "Later checken", `pad.canvas.followup.title` = "Opvolging", `watch.notification.fallback.followUp` = "Opvolging"; widget `widget.a11y.check_ins` "%lld check-ins" = "%lld check-ins" (English left in). "Controle" also means inspection/control, and `followup.checkin.subtitle` is "Heb je gekregen wat je nodig had?". Suggested site term: "opvolging" / "opvolgmoment", pending an owner choice |
| Day Clock | Day Clock (`clock.title`) | Dagklok | |
| Energy River | Energy River (`river.title`) | Energierivier | |
| Day Map | Day Map (`pro.feature.day_map`) | Dagkaart | modes: Regions = "Regio's" (`Regio’s`), Heatmap = "Heatmap", Day part = "Deel van de dag" |
| Schedule (week grid) | Schedule | Planning (form) / Plannen (action) / Agenda (`overview.schedule`) | Three Dutch words for `Schedule` |
| Focus Mode | Focus Mode (`pro.feature.focus_orbit`) | Focusmodus | `Start focus` = "Focus starten"; `Focus time` = "Focustijd"; `Focus Task` = "Hoofdtaak"; `Today's focus` = "Focus van vandaag"; `+5 min` stays "+5 min"; `End` = "Beëindigen" |
| Journal / mood | Journal (`journal.title`) / Great, Good, Neutral, Stressed | Dagboek / Geweldig, Goed, Neutraal, Gestrest | `How did your day feel?` = "Hoe voelde je dag?"; `Optional reflection...` = "Optionele reflectie..." |
| Analytics | Analytics (`tab.analytics`) | Analyses | plural "Analyses"; `Completion Rate` = "Voltooiingspercentage"; `How is this calculated?` = "Hoe wordt dit berekend?"; `This score reflects patterns, not performance.` = "Deze score weerspiegelt patronen, geen prestatie." |
| Streak | Streak / Current Streak | Reeks / Huidige reeks | `Days in a row with completed tasks` = "Opeenvolgende dagen met voltooide taken" |
| Workspace | Workspace | Werkruimte | 25 "werkruimte" values; 7 values shorten to "ruimte" ("Organiseer taken in aparte ruimtes", "Maak meerdere ruimtes…") |
| Checklist steps | Steps (`checklist.items_label`) | Stappen | `Free includes 1 item per task` = "De gratis versie bevat 1 item per taak." |
| Themes | Theme / Themes | Thema / Thema's | `insight.title.category` "Themes" = "Thema's" (a statistic of categories) |
| Priority | Priority / High / Medium / Low | Prioriteit / Hoog / Gemiddeld / Laag | |
| Recurring / Repeat | Repeat | Herhalen / Herhaal | `pad.canvas.recurrence.title` "Repeat" = "Herhaal" (bare stem) vs `recurrence.label` = "Herhalen" |
| Reminders | Reminder / Reminders | Herinnering / Herinneringen | `Apple Reminders` = "Apple Herinneringen" |
| Apple Reminders import | Re-import | Importeren | `%1$lld imported · %2$lld more with Pro` = "%1$lld geïmporteerd · %2$lld alleen met Pro" |
| Home Screen widgets | Next Task, Today's Tasks, Now & Next, From Earlier, Year in Squares, Hours, Focus Task, Quick Capture | Volgende taak, Taken van vandaag, Nu en straks, Van eerder, Jaar in vakjes, Uren, Hoofdtaak, Snel vastleggen | Month = "Maand", This Week = "Deze week", Streak = "Reeks", Momentum = "Momentum" (English) |
| Lock Screen widgets | `widget.config.lock_next.desc` "Your next task on the Lock Screen." | Je volgende taak op het toegangsscherm. | `hide titles on lock screen` = "…op het vergrendelscherm": both words again |
| Live Activity / Dynamic Island | Live Activity | (strings carry no term) | |
| Control Center capture | Quick capture button | Snel vastleggen | |
| Apple Watch | Now / Today / Tomorrow, complication, `watch.today.empty.allDone` "All done" | Nu / Vandaag / Morgen, "Alles klaar", "Niets vandaag", "Geniet ervan." | |
| iCloud Sync | iCloud Sync | iCloud-synchronisatie | `Enable iCloud Sync` = "iCloud-synchronisatie inschakelen" |
| Workspaces limit / free limits | Free includes 1 workspace | De gratis versie bevat 1 werkruimte. Upgrade naar Pro voor onbeperkte werkruimtes. | `Create up to 50 tasks`: `pro.feature.unlimited_tasks.desc` = "Je hebt 50 taken aangemaakt met het gratis plan." |
| Export | (Settings) | exporteren | 2 values |
| Settings | Settings | Instellingen | |

### Paid tier names in the Dutch UI
- Tier: **Pro** (55 values; "Pro-abonnementen bekijken", "Pro-proefperiode", "Pro behouden", "Pro hersteld.", `settings.pro.status.lifetime` "Pro Lifetime" = "Levenslang Pro", `pro.upgrade_button` = "Upgraden naar Pro"). `badge.pro` stays "PRO". Brand name "Taskful Day Pro" is identical in English.
- Periods: `pro.plan.monthly` = "Maandelijks", `pro.plan.yearly` = "Jaarlijks", `pro.plan.lifetime` = "Levenslang"; `pro.buy_lifetime` = "Levenslang kopen"; `pro.lifetime.owned` = "Eenmaal betalen. Voor altijd van jou."; `pro.terms.lifetime` = "Lifetime is een eenmalige aankoop. Geen verlenging." (English "Lifetime" left in; elsewhere "Levenslang").
- Trial: `pro.start_trial` = "Start gratis proefperiode van 7 dagen"; `pro.trial.badge` = "7 dagen gratis proefperiode"; `onboarding.trial.subtitle` = "Alle Pro-functies zijn de eerste 7 dagen actief — gratis, zonder creditcard."; `pad.sidebar.pro_trial.title` = "Proefperiode · %d dagen"; `trial.settings.status` = "Pro-proef — nog %lld dagen"; `trial.expired.title` = "Je gratis proefperiode is afgelopen".
- Restore: `pro.restore` = "Aankopen herstellen". Subscription: `settings.pro.manage` = "Abonnement beheren", `pro.terms.heading` = "Abonnementsvoorwaarden", `pro.terms.cancel_path` = "Op elk moment opzeggen in App Store › Account › Abonnementen." Tip: `tip.paywall.subheadline` = "Als Taskful Day je helpt, kun je een kleine fooi achterlaten. Geen abonnement. Geen druk."

### Dutch App Store listing (checked 2026-11-19)
- Name: **Taskful Day: Dagplanner**. Subtitle: **Takenlijst & Focus**. Description is in Dutch ("Plan de dag die je hebt, en laat gisteren los. Taskful Day is een rustige dagplanner… Onafgemaakte taken schuiven vanzelf door naar vandaag…"; the store says "schuiven door", so "doorschuiven" is the store word too). Free, 34 languages. IAP rows: `Ontwikkelaar steunen € 1,00`, `Taskful Day Pro eenmalig € 44,99`, `Taskful Day Pro jaarlijks € 29,99`, `Taskful Day Pro maandelijks € 2,99`.

---

### 4. WanderWiki (`wanderwiki`, source `WanderWiki/`, ID 6758459119)

### Dutch coverage
- `WanderWiki/Resources/Localizable.xcstrings`: 425 / 425 `nl`, 5 stale, 24 identical ("Feed", "Feedback", "Sepia", "Solarized", "Shuffle", "Cursor", "Open in Wikipedia", "WanderWiki Support", the demo article titles "Marie Curie", "Galileo Galilei", "Voyager 1", and the debug string "Skip (Debug)").
- `WanderWikiWidget/Localizable.xcstrings`: 129 / 129, 9 identical ("Offline", "Cursor", "Shuffle", "Tycho Brahe", "Open WanderWiki").
- Siri phrases and Shortcuts descriptions are in the main catalog ("Open WanderWiki en ontdek een willekeurig Wikipedia-artikel.", "Open WanderWiki bij artikelen over vandaag in de geschiedenis."); there is no `AppShortcuts.xcstrings` or InfoPlist catalog and no usage-description key in the project, so no permission prompt exists.
- **Verdict: app is in Dutch: yes.**

### Register
- je-marked: about 51 main + 12 widget values; u/uw: 0. Examples: "Je interesse: %@", "Elke dag waarop je iets uitlas, in één beeld.", "Vind je WanderWiki leuk?", "Kom morgen terug voor 20 meer, of ontgrendel nu onbeperkt lezen.". Colloquial contractions appear ("Nog één veeg houdt 'm in leven."). No mix.

### Glossary
| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Random | Random (`random_mode`) | Willekeurig | |
| For You | For You (`for_you_mode`) | Voor jou | `For You isn't available in %@ yet — showing Random.` = "‘Voor jou’ is nog niet beschikbaar in %@ — Willekeurig wordt getoond." |
| Today (feed tab) / Today in History | Today (`today_mode`) / Today in history / On This Day | Vandaag / Vandaag in de geschiedenis / Vandaag in de geschiedenis | The widget "On This Day" and the feed "Today in History" are the same Dutch string, which is fine; Soon. uses "Op deze dag" for its On This Day |
| Highlights / Events / Births / Deaths / Holidays | `today_category_*` | Hoogtepunten / Gebeurtenissen / Geboorten / Sterfgevallen / Feestdagen | **Collision:** `Editors' picks` is also "Hoogtepunten" |
| Browse (16 topics) | Browse (`browse_title`) / Browse categories | Bladeren / Categorieën bladeren | `Pick a category to start an endless swipe.` = "Kies een categorie om eindeloos te vegen." |
| Topics (interests) | Your Interests / Interest | Jouw interesses / Interesse | topics: Wetenschap, Technologie, Geschiedenis, Kunst, Muziek, Sport, Natuur, Ruimte, Filosofie, Geografie, Literatuur, Films, Eten, Architectuur, Wiskunde, Politiek |
| Swipe | Swipe to wander | Veeg om te verkennen | "vegen"/"veeg" for swiping |
| Where next | Where next | Waarheen nu | `Chase the thread` = "Volg de draad"; `Trail to` = "Spoor naar"; `The trail remembers where you came from.` = "Het spoor onthoudt waar je vandaan kwam." |
| Back to discovery | Back to discovery | Terug naar ontdekken | |
| Reader | Reader Theme | Leesthema | System / Sepia / Solarized / True Black = "Systeem" / "Sepia" / "Solarized" / "Diepzwart"; `Jump to top` = "Naar boven" |
| Reading time | Reading time: %lld min | Leestijd: %lld min | `~%lld min read` = "~%lld min lezen" |
| Listen | Listen | Luister | `Pause listening` = "Luisteren pauzeren", `Resume listening` = "Luisteren hervatten" |
| Save / Saved | Save / Saved / Bookmark | Bewaar? | The main labels vary: `save` = "Opslaan", `saved` = "Opgeslagen", but `Saved` (tab/section) = "Bewaard", `Save it for later` = "Bewaar voor later", `Anything saved` = "Alle bewaarde artikelen", error `Failed to save article` = "Artikel kon niet worden opgeslagen". 10 values say bewaar-, 7 say opslaan/opgeslagen (see Flags) |
| Like / Liked | Like / Liked | Vind ik leuk / Favorieten | `error_like_failed` = "Artikel kon niet worden geliked"; `Liked` list = "Favorieten" (not "liked"); `no_liked_articles` = "Nog geen favoriete artikelen" |
| Folders | Folders / Move to… | Mappen / Verplaats naar… | `New folder` = "Nieuwe map"; `Create folder` = "Map aanmaken"; `Icon` = "Symbool" |
| Offline copy | Offline copy / Ready offline | Offlinekopie / Offline beschikbaar | `Offline Reading` = "Offline lezen" |
| Streak | Streak / Don't break your streak | Reeks / Onderbreek je reeks niet | `%lld-day streak` = "Reeks van %lld dagen"; `Streak reminder` = "Reeksherinnering"; widget `Day streak` = "Dagenreeks" |
| Reading Year (widget) | Reading Year | Leesjaar | |
| Continue Reading (widget/control) | Continue Reading | Verder lezen | |
| Got a Minute (widget) | Got a Minute | Even tijd? | `%lld min · fits now` = "%lld min · past nu" |
| Two Doors (widget) | Two Doors | Twee deuren | `Far from your taste` = "Ver van je smaak"; `Strangeness` = "Afstand tot interesses" |
| Surprise Me (control) | Surprise Me | Verras me | |
| On This Day (widget) | On This Day | Vandaag in de geschiedenis | |
| Weekly recap | Your week of discovery / Share recap | Jouw week vol ontdekkingen / Overzicht delen | `You went deep` = "Je ging diep" |
| Delete My Data | Delete My Data (`delete_my_data`) | Mijn gegevens verwijderen | |
| Notifications / Daily article | Daily article | Dagelijks artikel | `Quiet hours` = "Stille uren"; `Notifications` = "Meldingen" |
| Language / Wikipedia edition | Wikipedia Language / App Language | Wikipedia-taal / App-taal | "edition" has no Dutch string; the app says "taal" |
| Share as image | Share as image (Story / Square) | Als afbeelding delen (Story) / (Vierkant) | |
| Show less like this | Show less like this | Minder zoals dit tonen | literal calque |
| Settings | Settings | Instellingen | |
| Free articles (daily 20) | %lld free articles left today | Nog %lld gratis artikelen vandaag | `Come back tomorrow for 20 more…` = "Kom morgen terug voor 20 meer, of ontgrendel nu onbeperkt lezen." |

### Paid tier names in the Dutch UI
- Tier: **Premium** (`unlock_premium` = "Premium ontgrendelen"; `Premium feature` = "Premiumfunctie"; `paywall_headline` = "WanderWiki is een premium-ervaring."). Features: `feature_unlimited_access` = "Onbeperkte toegang", `feature_personalized` = "Gepersonaliseerde feed", `feature_no_ads` = "Advertentievrije ervaring".
- Periods: `subscribe_monthly` "Maandelijks", `subscribe_yearly` "Jaarlijks", `subscribe_lifetime` "Levenslang", **`subscribe_weekly` "Wekelijks"** (the app still has a weekly plan; the store lists "WanderWiki weekabonnement € 0,99" while MASTER.md marks the weekly product "NOT FOR SALE (hidden)"). `Save %lld%%` = "Bespaar %lld%%"; `best_value` = "Beste deal"; `one_time_purchase` = "Eenmalige aankoop"; `unlock_lifetime_access` = "Levenslange toegang ontgrendelen"; `paywall_lifetime_own` = "WanderWiki voor altijd bezitten".
- Trial: `Start %lld-Day Free Trial` = "Start %lld dagen gratis proefperiode"; `%lld-day free trial` = "%lld dagen gratis proberen" (a third form); `Try it free for %lld days.\nCancel anytime.` = "Probeer het %lld dagen gratis.\nAnnuleer wanneer je wilt."; `trial_description` (fixed "3-day") = "Start je gratis proefperiode van 3 dagen om alle functies te ontgrendelen".
- Restore: `restore_purchases` = "Aankopen herstellen"; `restore_purchases_success` = "Aankopen succesvol hersteld!"; `manage_subscription` = "Abonnement beheren". Tip: `tip_the_developer` = "Geef de ontwikkelaar een fooi"; `support_developer` = "Steun de ontwikkelaar".

### Dutch App Store listing (checked 2026-11-19)
- Name: **WanderWiki: ontdek en leer**. Subtitle: **Feiten, geschiedenis & trivia**. Description is in Dutch ("Verken Wikipedia, één idee per keer. Ergens op Wikipedia staat een artikel dat je tot de laatste regel wilt lezen…"). Free, 34 languages. IAP rows: `WanderWiki maandabonnement € 1,99`, `WanderWiki weekabonnement € 0,99`, `Steun de ontwikkelaar € 1,00`, `WanderWiki eenmalige aankoop € 29,99`, `WanderWiki jaarabonnement € 9,99`.

---

### 5. Xiangqiful (`xiangqiful`, source `Xiangqi/`, ID 6794340136)

### Dutch coverage
- `Xiangqi/Localization/Localizable.xcstrings`: 3273 / 3273 `nl`, 0 stale, 83 identical (Blunder, Blunders, Coach, Premium, Xiangqiful Premium, Training, Rating, Club, Expert, Opening, Comeback, Momentum, Frequent, Supporter, Jade, the opponent names "Dòudou", "Nǎinai Chén", "Zhúxiāngzhāi Xiàngxìpǔ"). Composition: 1259 lesson, 695 drill, 219 Game Center, 216 opponent, 104 mistake, 97 module, 63 paywall strings.
- `Xiangqi/Localization/InfoPlist.xcstrings`: 2 / 2 (display name only). No Siri phrases, widgets or permission prompts exist in the project.
- **Verdict: app is in Dutch: yes**, including lesson text, drill hints, Game Center names and achievements.

### Register
- je-marked: about 471 values; u/uw: 0. Examples: "Partijen die je uitspeelt, verschijnen hier voor volledige…", "Die partij staat niet meer in je bibliotheek.", "Je hebt de fouten gezien. Tijd om ze op te lossen.". Drill hints use je as well ("Vraag je af wat Roods kanon op e2 zou zien…"). No mix. Informal tone ("Ik vind 'm geweldig").

### Glossary
| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Xiangqi / Chinese chess | Chinese chess (`dashboard.empty.subtitle`) | Chinees schaken | 63 values say "xiangqi" (`board.accessibility.board` "Xiangqi board" = "Xiangqi-bord"); store name says "Chinees Schaken" |
| Game / partij | game | partij | 203 values; `Start game` = "Start partij"; `Ladder game` = "Ladderpartij"; **plus** "spel" 24 times (`Play` tab) |
| Tabs | Home / Play / Training / Analysis / Progress | Start / Spelen / Training / Analyse / Voortgang | `tab.dashboard` "Home" = "Start" |
| Game Review (Analyze) | Game review / Analyze | Partijnabespreking / Analyseer | "analyse" 54 values; `Review, analysis and training always use the 2D board.` = "Nabespreking, analyse en training gebruiken altijd het 2D-bord." |
| Mate puzzles / Mate Trail | Mate Trail (`module.mateTrail.title`) | Matpad | `Consecutive-check mates, the native xiangqi puzzle.` = "Mat na een reeks schaken — de xiangqipuzzel bij uitstek."; `No mate problems yet` = "Nog geen matproblemen" (1 value); "puzzel" 24 values |
| Training puzzles | training puzzle | trainingspuzzel | `Solve your first training puzzle.` = "Los je eerste trainingspuzzel op." |
| Drill modules | Drill modules | Oefenmodules | `drill` = "oefening" (21), "drill" (2 values left in) |
| Opening Lab | Opening Lab | Openingslab | |
| Palace Workshop | Palace Workshop | Paleiswerkplaats | |
| Cannon Range | Cannon Range | Kanonbereik | |
| Horse Trails | Horse Trails | Paardenpaden | |
| Endgame Studio | Endgame Studio | Eindspelstudio | `Classical Studies` = "Klassieke studies" |
| Tactic Cards | Tactic Cards | Tactiekkaarten | |
| Tactics Yard | Tactics Yard | Tactiekplein | |
| Handicap House | Handicap House | Handicaphuis | `Two Horses` = "Twee Paarden", `One Chariot` = "Eén Wagen", `One Horse` = "Eén Paard", `Concede the Move` = "Zet Afstaan" |
| Lesson tracks | Fundamentals, Openings, Palace Defense, Cannon Tactics, Horse Technique, Middlegame, Endgame, Advanced | Basisprincipes, Openingen, Paleisverdediging, Kanontactiek, Paardtechniek, Middenspel, Eindspel, Gevorderd | `Lessons` = "Lessen"; `Eight tracks, from the board to the classics.` = "Acht trajecten, van het bord tot de klassiekers." |
| Skill assessment | Skill Assessment | Vaardigheidstoets | `Fifteen positions, one starting rating.` = "Vijftien stellingen, één startrating." |
| Pieces | General, Advisor, Elephant, Horse, Chariot, Cannon, Soldier | Generaal, Raadsheer, Olifant, Paard, Wagen, Kanon, Soldaat | pieces are lowercase inline ("raadsheer", "wagen") |
| Piece styles | Traditional / Western / Hybrid | Traditioneel / Westers / Hybride | `Characters` = "Karakters"; Simplified = "Vereenvoudigd"; `Move notation` = "Zetnotatie"; `Show coordinates` = "Coördinaten tonen" |
| Boards (7) | Boxwood, Rosewood, Park Stone Table, Club Mat, Xuan Paper Scroll, Red Lacquer & Gold, Marble & Jade | Palmhout, Palissanderhout, Stenen parktafel, Clubmat, Rol xuanpapier, Rood lakwerk en goud, Marmer en jade | `Boxwood` = "Palmhout" (boxwood is "buxus"; Palmhout is not the same wood, wrong meaning); `Board` = "Bord"; `3D Board` = "3D-bord" |
| Piece sets (8) | Ivory, Carved Wood, Club Melamine, Jade, River Stone, Rosewood & Brass, Porcelain, Gilded Lacquer | Ivoor, Gesneden hout, Clubmelamine, Jade, Rivierkiezel, Palissander en messing, Porselein, Verguld lakwerk | `Piece Finish` = "Afwerking van de stukken"; `Rosewood` board = "Palissanderhout" vs the piece set "Palissander" |
| Seven move grades | Best, Great, Good, Book, Inaccuracy, Mistake, Blunder | Beste, Uitstekend, Goed, Boekzet, Onnauwkeurigheid, Fout, Blunder | "Beste" is the inflected adjective; "Boekzet" for Book |
| Accuracy / key moments / advantage | Accuracy / Key moments / Better was / Best line | Nauwkeurigheid / Sleutelmomenten / Beter was / Beste variant | `Play the line` = "Speel de variant" |
| 13 mistake categories | Missed mate, Missed cannon tactic, Palace weakness, Trapped piece, Hanging piece, Missed fork/pin/skewer, Exposed general, Passive move, Opening inaccuracy, Endgame error, Missed tactic | Gemist mat, Gemiste kanontactiek, Paleiszwakte, Vastzittend stuk, Hangend stuk, Gemiste vork/pen/spies, Blootgestelde generaal, Passieve zet, Openingsonnauwkeurigheid, Eindspelfout, Gemiste tactiek | pattern names use Title Case ("Gemiste Mat", "Gemiste Slag") vs sentence case for categories ("Gemist mat") |
| 26 patterns (named) | Screenless cannon, Trapped horse, Broken advisors, Empty-Head Cannon, Palace breach, Iron Bolt, Lost initiative, Missed mate | Schermloos Kanon, Vastzittend Paard, Gebroken Raadsheren, Leegkopkanon, Paleisbres, IJzeren Grendel, Verloren Initiatief, Gemiste Mat | also "Gestapelde Kanonnen", "Hemel- en Aardekanonnen", "Twin Chariots" = "Tweelingwagens", "Palace Suffocation" = "Paleisverstikking" |
| 40 opponents / 8 tiers | Novice, Beginner, Casual, Club Player, Intermediate, Advanced, Expert, Master | Nieuweling, Beginner, Recreatief, Clubspeler, Halfgevorderd, Gevorderd, Expert, Meester | **Collision:** `progress.level.novice` "Novice" = "Beginner" and `progress.level.improver` "Improver" = "Gevorderd" (same Dutch as the tiers "Beginner"/"Gevorderd") |
| Opponent styles | Aggressive, Defensive, Cannoneer, Horse Specialist, River Controller, Positional, Endgame Grinder, Balanced | Agressief, Defensief, Kanonnier, Paardspecialist, Rivierbeheerser, Positioneel, Eindspelslijper, Evenwichtig | |
| Coach / hints | Coach / Unlimited hints | Coach / Onbeperkte hints | `%lld left today` = "Nog %lld vandaag."; "coachhints" in the paywall |
| Estimated rating | Estimated rating | Geschatte rating | `Rating in progress` = "Rating in opbouw" |
| Skill profile (radar) | Full skill radar | Volledige vaardighedenradar | The site says "skill profile"; the app says "vaardighedenradar" and "vaardigheden"; skill axes: Tactiek, Verdediging, Positiespel, Eindspel, Openingen |
| Streak | streak / Training Streak | reeks / Trainingsreeks | `Train today to keep it alive.` = "Train vandaag om je reeks levend te houden."; `Longest Win Streak` = "Langste Overwinningsreeks" |
| Import game / clipboard | Import a game / Clipboard | Een partij importeren / Klembord | `Read record` = "Partij inlezen"; WXF / ICCS / Chinese notation unchanged |
| Game Center | leaderboards / achievements | (Game Center names translated in Title Case) | "Steady Hand" = "Vaste Hand", "Top of the Ladder" = "Bovenaan de Ladder", "Puzzles Solved" = "Opgeloste Puzzels" |
| Settings sections | Board / Feel / Data & privacy / Support the developer | Bord / Gevoel / Gegevens en privacy / Steun de ontwikkelaar | `Haptics` = "Trillingen" (same Haptiek question as Tare) |
| Tips (Settings) | Buy a coffee / Supporter / Huge support | Trakteer op een koffie / Supporter / Enorme steun | store IAP names: "Koffie", "Supporter", "Enorme steun" |

### Paid tier names in the Dutch UI
- Tier: **Premium** (`paywall.success.title` = "Welkom bij Premium"; "Xiangqiful Premium" identical in English; `paywall.hero.general.title` = "Word meetbaar beter in xiangqi").
- Periods: `paywall.plan.monthly` "Maandelijks", `paywall.plan.yearly` "Jaarlijks", `paywall.plan.lifetime` "Levenslang"; `paywall.purchaseLifetime` = "Voor altijd ontgrendelen"; `paywall.oneTime` = "Eenmalige aankoop"; `paywall.perMonthSuffix` "/mo" = "/mnd"; `paywall.bestValue` = "Beste waarde"; `paywall.currentPlan` = "Huidig plan"; `paywall.billing.then.month` = "Daarna %@/maand". There is also a weekly string (`paywall.billing.then.week` = "Daarna %@/week") with no weekly product in MASTER.md.
- Trial: `paywall.startTrial` = "Start gratis proefperiode"; `paywall.trial.compound.format` "%lld-day free trial" = "%lld-daagse gratis proefperiode"; `paywall.autoRenewNote` = "Wordt automatisch verlengd totdat je opzegt. Je kunt op elk moment opzeggen in Instellingen.".
- Restore: `paywall.restore` = "Aankopen herstellen"; `paywall.restore.done` = "Hersteld: %@."; `paywall.restore.none` = "Er zijn geen eerdere aankopen gevonden op dit Apple-account." ("Apple-account" lowercase, hyphen; Clippet says "Apple Account"). Lifetime-vs-subscription warnings are translated ("Je hebt Levenslang al").

### Dutch App Store listing (checked 2026-11-19)
- Name: **Xiangqiful: Chinees Schaken**. Subtitle: **Leer xiangqi: tactiek en AI**. Description is in Dutch ("Je hoeft geen enkel Chinees karakter te kunnen lezen om met xiangqi te beginnen…"). Free, 34 languages. IAP rows: `Premium jaarabonnement € 9,99`, `Premium maandabonnement € 1,99`, `Supporter € 5,99`, `Enorme steun € 9,99`, `Koffie € 1,99`, `Premium levenslang € 22,99`.

---

### 6. Clippet (`clippet`, source `clipboard/`, ID 6829498729, unreleased, pages unlisted)

### Dutch coverage
- 13 catalogs, all `nl` complete: `clipboard/Localizable.xcstrings` 638 / 638 (38 identical: file types Audio, Code, Document, PDF, Video, JSON, Swift, Python, JavaScript, HTML, carriers FedEx, USPS, plus "Filter", "Link", "Open", "Tags", "Type", "Status", "Privacy", "Build", "Clippet Pro", "Open Google Translate"); `ClipboardKeyboard` 104 / 104; `ClipboardWidgets` 63 / 63; `ClipboardShare` 28 / 28; `ClipboardMacBridge` 19 / 19; `ClipboardKit` 26 / 26; `ClipboardAction` 1 / 1; plus `AppShortcuts` 2 / 2 and six `InfoPlist` files (7 + 1 + 1 + 1 + 1 + 1, all translated). No stale keys. All catalogs carry 40 locales.
- Siri: "Plak laatste kopie in ${applicationName}", "Bewaar mijn laatste kopie in ${applicationName}". Permission prompts (contacts, Face ID, photo library add, Reminders) are Dutch and je: "Bewaart een telefoonnummer of visitekaartje uit een knipsel als nieuw contact wanneer je Voeg toe aan Contacten kiest.", "Laat Appvergrendeling Clippet voor je ontgrendelen, zodat alleen jij je knipsels kunt zien."
- **Verdict: app is in Dutch: yes.**

### Register
- je-marked: about 98 main, 15 keyboard, 6 widget, 4 InfoPlist, 2 kit; u/uw: 0. Examples: "Geef Clippet in Instellingen toestemming om aan je fotobibliotheek toe te voegen", "Je knipsels kunnen nu niet worden getoond", "Houd je knipsels privé". Buttons are bare-stem imperatives in the same je tone ("Verwijder", "Bewaar", "Wijzig", "Plak", "Zoek", "Deel", "Ontgrendel"), including "Zoek in knipsels", "Voeg toe". No mix.

### Glossary
| English term on site | English UI string (key) | Dutch UI string (catalog, verbatim) | Note |
|---|---|---|---|
| Clip | Clip / Clips | Knipsel / Knipsels | 68 + 86 values; `Clipboard` = "Klembord" (16 values). "Knipsel" (a newspaper clipping) is the app's term; copy = "kopie" |
| Clipboard history | Clipboard Access / History | Klembordtoegang / Geschiedenis | `Keep History` = "Geschiedenis bewaren"; `Keep History Forever` = "Bewaar geschiedenis voor altijd" |
| Eight kinds of clip | Text, Links, Images, Videos, PDFs, Audio, Files, Code | Tekst, Links, Afbeeldingen, Video's, PDF's, Audio, Bestanden, Code | `Types to Save` = "Te bewaren typen"; `Document` = "Document"; code languages unchanged |
| Search | Search Clips / Search | Zoek in knipsels / Zoek | `Search Names` = "Zoek op namen"; `Pinned Matches` = "Vastgezette overeenkomsten" ("overeenkomsten" means agreements; "resultaten" meant) |
| Pins | Pinned | Vastgezet | 15 values; `Pinned Clips` = "Vastgezette knipsels" |
| Boards | Boards / Add to Board | Borden / Voeg toe aan bord | `Board Name` = "Naam van bord"; `Make a board in Clippet to keep clips together.` = "Maak in Clippet een bord om knipsels bij elkaar te houden." |
| Tags / Names | Tags / Name | Tags / Naam | `Add tag` = "Voeg tag toe"; `Tagged %@` = "Getagd met %@" |
| Smart Actions | Smart Actions | Slimme acties | `Add Custom Action` = "Voeg eigen actie toe"; `Translate` = "Vertaal"; `Web Search` = "Zoeken op het web"; `Remind Me at a Time` = "Herinner me op een tijdstip"; `Phone Number` = "Telefoonnummer"; `Flight Number` = "Vluchtnummer"; `Tracking Number` = "Trackingnummer"; `Package Tracking` = "Pakket volgen"; `QR Code` = "Qr-code" (lowercase "qr") |
| Quick Paste | Quick Paste | Snel plakken | `Quick Paste Shortcut` = "Sneltoets voor Snel plakken"; capitalized "Snel plakken" mid-sentence |
| Paste Last Copy (widget button) | Paste Last Copy | Plak laatste kopie | `Paste Last Copy into Clippet` = "Plak laatste kopie in Clippet" |
| Latest Clip / Pinned Clips / Quick Add (widgets) | Latest Clip, Pinned Clips, Quick Add | Laatste knipsel, Vastgezette knipsels, Snel toevoegen | `Latest Clip Widget` = "Widget Laatste knipsel" |
| Menu bar | Menu Bar | Menubalk | `Clippet blijft bewaren vanuit de menubalk`; `Open at Login` = "Open bij inloggen"; `Keep in Dock After Closing` = "Houd in Dock na sluiten" |
| Clippet keyboard | Clippet Keyboard / Clips in the Keyboard | Clippet-toetsenbord / Knipsels in het toetsenbord | `Allow Full Access` text: "Sta volledige toegang toe om je knipsels te tonen" |
| App Lock | App Lock | Appvergrendeling | `Face ID Lock` = "Face ID-vergrendeling"; `Optic ID Lock` = "Optic ID-vergrendeling"; `Clippet is locked` = "Clippet is vergrendeld"; `Redact Previews in App Switcher` = "Verberg voorvertoningen in appkiezer" |
| iCloud Sync & backups | iCloud Sync & Backup / Create Backup / Restore from Backup | iCloud-synchronisatie en back-up / Maak back-up / Herstel vanuit back-up | `Sync & Backup` = "Synchronisatie en back-up"; `Sync Now` = "Synchroniseer nu"; `Merge` = "Voeg samen"; `Replace` = "Vervang"; `Backup saved.` = "Back-up bewaard." |
| Auto-delete | Auto-Delete This Clip / Delete After | Verwijder dit knipsel automatisch / Verwijder na | `Auto-Delete Sensitive Clips` = "Gevoelige knipsels automatisch verwijderen" |
| Save | Save / Saved | Bewaar / Bewaard | 85 values say bewaar-, 0 say opslaan: consistent; `Save to Photos` = "Bewaar in Foto's" |
| Drop (iPad/Mac) | Added via drop | Toegevoegd via slepen | |
| Settings | Settings | Instellingen | 24 values |
| Privacy | Privacy | Privacy | `Keep Your Clips Private` = "Houd je knipsels privé" |

### Paid tier names in the Dutch UI
- Tier: **Clippet Pro** (identical in English: `Clippet Pro`, `Pro`; "Clippet Pro wordt ingeschakeld zodra de aankoop is goedgekeurd."). Plans: `Monthly` = "Maandelijks", `Lifetime` = "Levenslang" (not "Lifetime" as in the Spanish catalog), `Subscribe Monthly` = "Abonneer maandelijks", `Subscribe Yearly` = "Abonneer jaarlijks", `Buy Lifetime` = "Koop Levenslang", `Switch to Lifetime` = "Schakel over op Levenslang", `Pay Once Instead` = "Betaal liever eenmalig", `Pay once. No subscription.` = "Betaal eenmalig. Geen abonnement.", `One payment of %@. No subscription, nothing renews.` = "Eenmalige betaling van %@. Geen abonnement, niets wordt verlengd.", `%@ a month, billed yearly` = "%@ per maand, jaarlijks gefactureerd". Family Sharing: "Met één aankoop ontgrendel je Clippet Pro op je iPhone, iPad en Mac, en met Delen met gezin deel je het met je gezin."
- Trial: `Start Free Trial` = "Begin gratis proefperiode"; the trial/renewal line "Gratis voor %1$lld dag, daarna %2$@. Wordt automatisch verlengd tenzij je minstens %3$@ voor het einde van de periode opzegt in de abonnementsinstellingen van je Apple Account." (singular and plural variants exist).
- Restore: `Restore Purchases` = "Herstel aankopen" (verb first; the other five apps say "Aankopen herstellen"); `Manage Subscription` = "Beheer abonnement".

### Dutch App Store listing (checked 2026-11-19)
- iTunes lookup (`country=nl&lang=nl_nl`) returns **resultCount 0** and `apps.apple.com/nl/app/id6829498729` returns HTTP 404: Clippet is not on the store yet, so no name, subtitle or description exists. The in-app name is "Clippet" in every `InfoPlist` (`CFBundleDisplayName` = "Clippet"). The in-app strings and the English page name the plans "Clippet Pro" (monthly/yearly/lifetime); the Dutch store IAP names are not set.

---

## Cross-app terms (how these apps write recurring words in Dutch)

| Concept | Dutch in these six apps | Note |
|---|---|---|
| countdown | **aftelling** (Soon. 68 values, "Aftelling toevoegen", "Laatste aftelling"); "countdown" survives in 3 widget strings; "aftelmoment"/"aftelevenement" in two permission prompts | Soon.'s tagline "Aftellen" in the store; "teller" appears twice for "counter" |
| widget | **widget** (Soon. 29, Taskful Day 18); hyphen compounds "Widget-voorkeuren", "Widget-diagnose", "Soon.-widget"; closed "widgetweergave" | never "gadget" |
| subscription | **abonnement** ("Abonnement beheren" in Soon, Taskful Day, WanderWiki; "Beheer abonnement" in Clippet); "Abonneren", "Abonneer maandelijks" | "opzeggen" for cancelling a subscription, "annuleren" for cancel buttons; Soon. mixes "op elk moment opzegbaar" and "Annuleer" |
| lifetime | **Levenslang** (all six; Soon., Taskful Day, WanderWiki, Xiangqiful, Clippet "Levenslang"); "Eenmalige aankoop" / "Eenmalig" as the description | one English leak: Taskful Day `pro.terms.lifetime` "Lifetime is een eenmalige aankoop."; store IAP names say "eenmalige aankoop" (Soon., WanderWiki), "eenmalig" (Taskful Day), "levenslang" (Xiangqiful) |
| free trial | **gratis proefperiode** ("Start gratis proefperiode", "1 week gratis"); WanderWiki also "gratis proberen"; Xiangqiful "-daagse gratis proefperiode" | Taskful Day short form "Pro-proef" |
| restore purchases | **Aankopen herstellen** (Soon., Tare, Taskful Day, WanderWiki, Xiangqiful); Clippet "Herstel aankopen" | |
| sync | **synchronisatie** / "synchroniseren" (Soon. 9, Taskful Day 24, Clippet 28); never "sync" as a noun; always compounded with a hyphen: "iCloud-synchronisatie" | English "sync" appears only inside brand text |
| iCloud | **iCloud** (never translated); "iCloud-synchronisatie", "je persoonlijke iCloud" | `iCloud-account` in Taskful Day |
| settings | **Instellingen** (all six); "Open Instellingen", "de app Instellingen" | |
| export | **exporteren** ("Mijn gegevens exporteren", Soon.); noun "Export mislukt" and verb "Exporteren mislukt" both | |
| clipboard | **klembord** ("Kopieer naar klembord", Xiangqiful "Klembord", Clippet "Klembord…", 16 values) | Apple's NL word is "Klembord" |
| puzzle | **puzzel** (Xiangqiful "trainingspuzzel", Tare "balanspuzzel" in the store); Xiangqiful also "matprobleem" (1 value) and "oefening" for drills | Tare's `Hint`/`Hints` stay English |
| privacy | **Privacy** (Tare, Xiangqiful, Clippet, WanderWiki "Privacy & gegevens"), **Privacybeleid** for the policy; adjective **privé** | |
| Lock Screen | **toegangsscherm** (Soon. 5, Taskful Day 1, store) vs **vergrendelscherm** (Soon. 2, Taskful Day 1) | the two apps mix them inside one catalog; pick one for the site |
| Home Screen | **beginscherm** (Soon. 7 and Taskful Day 1) | |
| streak | **reeks** (Taskful Day, WanderWiki, Xiangqiful, Soon.); Soon. also "dagen op rij" | |
| Family Sharing | **Delen met gezin** | Apple's name; Soon. "Delen met gezin-groep" |
| reminders | **Herinneringen** (also Soon.'s "Memories") | collision in Soon. |
| Apple Account | "Apple Account" (Clippet), "Apple-account" (Xiangqiful), "Apple ID" (Soon. payment line) | |

## Flags (app-side string bugs worth an issue)

1. **Taskful Day, check-ins (extends I-0197):** the feature has at least six Dutch names across `followup.*` and `pad.canvas.followup.*`: "Controle/Controles" (title, section, button "Nu controleren"), "Opvolgen", "Later opvolgen", "Opvolging", "Opvolgdatum", "Later checken"/"Check op", and the widget accessibility string `widget.a11y.check_ins` left as "%lld check-ins". "Controle" also means inspection/control, so it reads as policing a task rather than following up. Needs one term and a native-speaker pass. Where: `TaskLogger/TaskLogger/Localization/Localizable.xcstrings` (nl), `TaskLoggerWidgetsExtension/Localizable.xcstrings`.
2. **Taskful Day, register:** `notification.limit.message` says "Uw apparaat kan maximaal 60 actieve herinneringen bevatten…" (formal); the whole app is je. Fix to "Je apparaat".
3. **Taskful Day, English left in:** `widget.a11y.check_ins` ("%lld check-ins"), `pro.terms.lifetime` ("Lifetime is een eenmalige aankoop."), `Taskful Day Pro` brand lines; `Done` is "Gereed" in `action.dismiss` and "Klaar" elsewhere (24 values); `Schedule` is "Planning", "Plannen" and "Agenda" in different places; carry forward has five phrasings ("doorschuiven", "verplaatsen naar vandaag", "naar vandaag halen", "mee naar de volgende dag", "verplaatst"). The kit keys "End focus session" and "Extend focus session" have no translation in any language.
4. **Soon., Memories vs Reminders:** both are "Herinneringen" (`Memories` and `Reminders`), so the tab/section for past moments and the notification setting have the same label. Needs a different word for one (e.g. "Terugblik" or "Herinneringen" vs "Meldingen").
5. **Soon., Lock Screen / countdown:** "toegangsscherm" (5) vs "vergrendelscherm" (2) and "countdown" (3, e.g. `Remove this countdown from the Lock Screen.`) vs "aftelling" (68); the key `Soon` is missing from InfoPlist; `I'm counting down something important with Soon..` has a double period in the English key (typo in the share text). `Anniversary` = "Jubileum", but `This is your anniversary` = "Dit is jouw verjaardag" and `Birthday` = "Verjaardag" (the on-this-day anniversary reads as a birthday). `Plan` tab = "Planning" but `Tap Plan…` = "Tik op Plan…". Widget gallery names stay English ("Soon · Ring").
6. **WanderWiki, wrong meaning in the widget:** `Because you read %@` (widget) = "Je interesse: %@" (means "Your interest: %@"). Also `Highlights` and `Editors' picks` are both "Hoogtepunten"; `Saved` is "Bewaard" in some places and "Opgeslagen" in others ("opslaan" in errors, "bewaar" in labels); `Like` = "Vind ik leuk" but the list is "Favorieten" and the error says "geliked"; `Show less like this` = "Minder zoals dit tonen" (calque); `Strangeness` = "Afstand tot interesses" (in the data key only).
7. **WanderWiki, weekly plan and trial:** the app still ships `subscribe_weekly` ("Wekelijks") and the store lists "WanderWiki weekabonnement € 0,99", while MASTER.md marks the weekly product "NOT FOR SALE (hidden)" and the site page lists no weekly plan; `trial_description` hard-codes "3 dagen" (the monthly/yearly trial is 1 week per MASTER.md). Check the paywall in the Dutch App Store.
8. **Tare:** `Buy Chapters %lld to %lld` = "Hoofdstuk %1$lld tot %2$lld kopen" (singular, the sibling Open string is plural); `Mobile` = "Mobiel" for the hanging mobile reads as "mobile phone"; `Play` = "Spel" (noun for a verb button); `Haptics` = "Trillingen" (Apple's Dutch is "Haptiek"; the same in Xiangqiful); `Left`/`Right` = "Linker"/"Rechter" as bare labels. The catalog has no "Full Access" or tier name: the store's IAP is "Hoofdstukken II–X" (consistent with the English "Chapters II–X").
9. **Xiangqiful:** `Boxwood` board = "Palmhout" (boxwood is "buxushout"; "palmhout" is a different wood); the seven grades use "Beste" (inflected adjective as a label) and "Boekzet" for Book; the tier names "Novice"/"Beginner" and the progress levels `Novice` = "Beginner", `Improver` = "Gevorderd" collide; pattern names are Title Case ("Gemiste Mat") while categories are sentence case ("Gemist mat"); "puzzel" (24) vs "matprobleem" (1) vs "oefening" for drills; `Apple-account` lowercase (Clippet: "Apple Account"); the store IAP name "Supporter € 5,99" and "Enorme steun € 9,99" vs the in-app "Trakteer op een koffie" ("Koffie" in the store). The site says "skill profile", the app says "vaardighedenradar".
10. **Clippet:** `Pinned Matches` = "Vastgezette overeenkomsten" (wrong sense, should be results); `Restore Purchases` = "Herstel aankopen" and `Manage Subscription` = "Beheer abonnement" are verb-first, unlike the sibling apps ("Aankopen herstellen", "Abonnement beheren"); `QR Code` = "Qr-code" (lowercase); "knipsel" (clip) is a consistent but unusual word for the product's main object (a newspaper clipping). Pre-release: no Dutch store listing exists yet; the Dutch store page and IAP names must be written for launch.
11. **Store listing names:** Soon. = "Soon. - Dagen Tot Grote Events" ("Events", Title Case "Tot Grote"); Tare = "Tare: Balans & Logica Puzzel" (title-cased puzzle); the store text of Soon. says "toegangsscherm". All five live listings are in Dutch.


---

