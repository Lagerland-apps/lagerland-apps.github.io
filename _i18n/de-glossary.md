# German glossary per app (de)

Part of the language sheet `_i18n/de.md`. Extracted 2026-10-26 from each app's string catalog (read-only) and its German App Store listing. German UI strings are verbatim from the catalogs: use them exactly on the site, even where a flag says the app's own wording is inconsistent (pick the main-screen form named in the row). Store prices quoted here are for reference only: the site prints prices from the catalog, never from this file.

## German (de) glossary, batch 1: aftershift, allpaid, appmeta, appmeta-pulse, chessful

Extracted 2026-10-26 from each app's source catalogs (read-only) and the German App Store storefront.
Counting rules: "total" = catalog keys that are translatable (format-only keys such as `%@`, `%lld`, `·` excluded where marked
`shouldTranslate: false`); "de" = keys with a German value, state `translated` (or a translated plural/stringSet).
German values are copied verbatim from the catalogs. App Store strings came through WebFetch (a summarising fetcher), so
re-check € strings character by character in a browser before they go on a page.

Formality across catalogs (rough count of German values using Sie/Ihr vs du/dein):
AfterShift 4 / 195 (du), AllPaid 1 / 36 (du), AppMeta **174 / 45 (mixed, mostly Sie)**, AppMeta Pulse 3 / 127 (du), Chessful 6 / 256 (du).

---

### 1. AfterShift (`aftershift`, source `shiftworkersleep/`, ID 6757163182)

### German coverage
- Main app uses legacy `.lproj` files (no xcstrings): `en.lproj/Localizable.strings` 1438 keys, `de.lproj/Localizable.strings`
  1438 keys, 0 missing, 33 values identical to English (mostly "Premium", "Trends", "REM", "Pro", names). Plurals:
  `Localizable.stringsdict` en and de both present (same key count). → **100 %**
- Widget `shiftworkersleepWidget/Localizable.xcstrings`: 15 / 15 translatable keys in German → **100 %**
- InfoPlist: `de.lproj/InfoPlist.strings` localizes `CFBundleDisplayName` ("AfterShift") and `NSHealthShareUsageDescription`
  ("AfterShift liest deine Schlafdaten aus Apple Health, um Schlafdefizit und Erholung zwischen Schichten zu berechnen.").
  **Not localized:** `NSCalendarsUsageDescription` / `NSCalendarsFullAccessUsageDescription` (set only in the build settings,
  English), so the calendar permission prompt shows English on a German device.
- Paywall strings (`paywall.*`) are in the main catalog and translated.
- **Verdict: app is in German: yes** (one English permission prompt: calendar access).

### Glossary
| English term on site | English UI string (key) | German UI string (catalog) | Note |
|---|---|---|---|
| Today (screen / tab) | Today (`tab.today`) | Heute | |
| Coach (screen) | Coach (`tab.coach`, `coach.title`) | Ratgeber | |
| Roster (shift calendar) | Roster (`tab.roster`) | Dienstplan | Widget "Roster" also "Dienstplan" |
| Settings | Settings (`tab.settings`) | Einstellungen | |
| Shift Recovery Score | Shift Recovery Score (`recovery.shiftRecoveryScore`) | Schichterholungswert | **Flag:** `sleepScore.title` "Sleep Score" is also "Schichterholungswert", so the two scores share one German name; `sleepScore.unlock` says "Erholungswert freischalten" |
| Sleep Score | Sleep Score (`sleepScore.title`) | Schichterholungswert | see above; site should not present "Sleep Score" as a separate German term |
| Readiness | Readiness (`readiness.title`, widget `widget.gallery.readiness.name`) | Erholungszustand | **Flag:** inconsistent: `shiftChange.readiness` = "Erholungsbereitschaft", `readiness.locked` = "Bereitschaft gesperrt", `swap.headline.*` = "Bereitschaft …". "Bereitschaft" is also the word for On-call. Use "Erholungszustand" |
| On-call | On-call (`readiness.onCall`, `shift.onCall`) | Bereitschaft | `schedule.irregular` "Irregular/On-Call" = "Unregelmäßig/Bereitschaft"; `coach.onCall.title` "On-call recovery mode" = "Bereitschafts-Erholungsmodus" |
| Naps | Naps (`naps.title`) / Nap (`nap.label`) | Nickerchen | Log Nap (`today.logNap`) = "Nickerchen erfassen" |
| Nap window | Optional nap window (`notification.napWindow.title`) | Optionales Nickerchen-Fenster | `insight.notification.napWindow.title` "Nap window" = "Nickerchen-Fenster" |
| Sleep debt | Sleep debt trend (`debtTrend.title`); widget Sleep Debt | Schlafdefizit-Trend; Schlafdefizit | |
| Sleep stages Awake / Core / Deep / REM | `stages.awake/core/deep/rem` | Wach / Leicht / Tief / REM | Core → "Leicht" (Apple Health's German uses "Kern"; flag for review, don't fix) |
| Fragmentation | Fragmentation (`continuity.fragmentation`) | Fragmentierung | paywall `paywall.premium.fragmentation` "Fragmentation & continuity insights" = "Fragmentierungs- & Kontinuitätsanalysen" |
| Caffeine timing | Caffeine timing (`coach.caffeine.title`) | Koffein-Zeitpunkt | **Flag:** `caffeine.header` "Caffeine Timing" = "Koffeinkonsum" (means caffeine consumption); `caffeine.trend.excellent` "Exzellentes Koffein-Zeitpunkt…" is ungrammatical (should be "Exzellenter") |
| Caffeine cut-off | Caffeine cutoff (`notification.caffeineCutoff.title`) | Koffein-Stopp | |
| Wind-down reminder | Wind down (`notification.windDown.title`) | Entspannung | **Flag:** `insight.notification.windDown.title` "Wind-down time" = "Zeit zum Abschalten" |
| Calendar shift import | Import from calendar (`roster.calendarImport`) | Aus Kalender importieren | |
| Calendar sync (Premium) | Calendar Sync (`calendar.sectionTitle`) | Kalender-Synchronisierung | `calendar.upgradeAutoSync` = "Upgrade: Auto-Synchronisierung, mehrere Kalender & Überstunden" |
| Overtime | Overtime: (`nextShift.overtime`) | Überstunden: | |
| Repeating rotation | Repeating rotation (`roster.rotation`) | Wiederkehrender Schichtrhythmus | `rotation.presets` "Common rotations" = "Häufige Rhythmen". **Flag:** `roster.tapToAdd` German drops "or set up a repeating rotation" |
| Trends | Trends (`trends.title`) | Trends | `today.section.trends` "Trends & Insights" = "Trends & Einblicke" |
| Export / PDF report | Export Sleep Report (`settings.exportReport`) | Schlafbericht exportieren | `premium.export.title` "Export report" = "Bericht exportieren" |
| Premium | AfterShift Premium (`paywall.premiumTitle`) | AfterShift Premium | **Flag:** app also shows "Pro" (`locked.proBadge`, `pro.chipLabel`, "Unlock with Pro") in English and German; site uses Premium |
| Monthly / Annual | Monthly / Yearly (`paywall.monthly`, `paywall.yearly`) | Monatlich / Jährlich | |
| Lifetime | Lifetime (`paywall.lifetime`) | Einmalkauf | **Flag:** settings `settings.lifetimeActive` = "Lifetime Premium" (left English). App Store IAP name "Premium Einmalkauf" matches "Einmalkauf" |
| 7-day free trial | 7-day free trial (`paywall.7dayTrial`) | 7 Tage kostenlos testen | |
| Restore Purchases | Restore Purchases (`paywall.restorePurchases`) | Käufe wiederherstellen | |
| Widgets: Next Shift, Shift Plan, Rhythm, Sleep Graph | `widget.gallery.*.name` | Nächste Schicht, Plan zur Schicht, Rhythmus, Schlafverlauf | |

### German App Store listing
- Name: **AfterShift: Schlaf & Schicht** (differs from English)
- Subtitle: **Erholung, Energie & Müdigkeit** (differs)
- Price: Kostenlos · In-App-Käufe
- IAPs: `Premium Jahresabo 29,99 €` · `Premium Einmalkauf 44,99 €` · `Premium Monatsabo 3,99 €` · `Entwickler unterstützen 1,00 €`
- Sprachen: Deutsch und 33 weitere

---

### 2. AllPaid (`allpaid`, source `billreminder/`, ID 6757253009)

### German coverage
- Main `billreminder/Localizable.xcstrings`: 486 / 486 → **100 %** (36 values identical to English: "Pro", "Streaming", brand names)
- `InfoPlist.xcstrings`: 3 / 3 → 100 % (display name "AllPaid"; Face ID prompt "Face ID oder Touch ID zum Öffnen der App erforderlich.")
- Widget `billreminderWidget/Localizable.xcstrings`: 57 / 58 → 98.3 % (only `%lld` missing); `billreminderWidgetShared/Widget.xcstrings` 130 / 130 → 100 %
- **Not localized:** Siri App Shortcut phrases in `Services/AppIntents/BillsDueIntent.swift` ("What bills are due in …") have no
  AppShortcuts.xcstrings, so the Siri phrases are English only. Do not promise German Siri phrases on the page.
- **Verdict: app is in German: yes** (Siri phrases English only).

### Glossary
| English term on site | English UI string (key) | German UI string (catalog) | Note |
|---|---|---|---|
| Bills | Bills | Rechnungen | app uses "Rechnung" throughout |
| Add a bill | Add Bill | Rechnung hinzufügen | |
| Mark paid | Mark as paid / Mark paid | Als bezahlt markieren | notification action too |
| Undo | Undo | Widerrufen | |
| Snooze (notification) | Remind in 2 hours / Remind tomorrow | In 2 Stunden erinnern / Morgen erinnern | no single "Snooze" string |
| Monthly calendar | Monthly Calendar | Monatskalender | |
| Daily total / Total due | Total due | Gesamt fällig | |
| Upcoming | Upcoming | Bevorstehend | "No upcoming bills" = "Keine anstehenden Rechnungen" (anstehend vs bevorstehend, minor) |
| Reminders | Reminders | Erinnerungen | |
| Multiple reminders per bill (Pro) | Multiple reminders per bill | Mehrere Erinnerungen pro Rechnung | |
| Due-day reminder | Due-day reminders | Erinnerungen am Fälligkeitstag | |
| Spending analytics (Pro) | Spending Analytics | Ausgabenanalyse | tab/section "Analytics" = "Auswertung" |
| Category breakdown | By category | Nach Kategorie | |
| Monthly trends | Monthly trend | Monatlicher Trend | |
| Full payment history | Full payment history / Payment History | Vollständiger Zahlungsverlauf / Zahlungsverlauf | |
| Unlimited bills | Unlimited bills | Unbegrenzte Rechnungen | |
| iCloud Sync | iCloud Sync | iCloud-Synchronisation | |
| Search / Sort / Notes / Share | Search bills / Sort by / Notes / Share bill | Rechnungen suchen / Sortieren nach / Notizen / Rechnung teilen | |
| Billing cycles | Weekly / Bi-weekly / Monthly / Quarterly / Semi-annual / Yearly / Custom | Wöchentlich / Alle zwei Wochen / Monatlich / Vierteljährlich / Halbjährlich / Jährlich / Benutzerdefiniert | |
| Categories (examples) | Streaming / Subscriptions / Utilities / Housing / Insurance | Streaming / Abonnements / Nebenkosten / Wohnen / Versicherung | |
| Widgets: Next Bill, Horizon, Paid Rhythm | Next Bill / Horizon / Paid Rhythm | Nächste Rechnung / Horizont / Zahlungsrhythmus | |
| Free tier | Free plan | Kostenloser Plan | **Note:** `Free: 1` (= "Kostenlos: 1") refers to contract reminders, not bills; the free bill limit is 3 in code (`freeBillLimit = 3`) |
| Pro | Pro / AllPaid Pro | Pro / AllPaid Pro | |
| Lifetime | Lifetime / Buy Lifetime Access | Lebenslang / Lebenslangen Zugang kaufen | App Store IAP uses "Einmalkauf" (wording differs from in-app "Lebenslang") |
| 7-day free trial | Try Pro free for 7 days | Pro 7 Tage kostenlos testen | |
| Restore Purchases | Restore Purchases | Käufe wiederherstellen | |

### German App Store listing
- Name: **AllPaid – Rechnungen verwalten** (differs from English)
- Subtitle: **Pünktlich zahlen, ohne Stress** (differs)
- Price: Kostenlos · In-App-Käufe
- IAPs: `AllPaid Pro Jahresabo 14,99 €` · `AllPaid Pro Einmalkauf 29,99 €` · `AllPaid Pro Monatsabo 1,99 €`
- Sprachen: Deutsch und 33 weitere

---

### 3. AppMeta (`appmeta`, source `metabuilder/`, ID 6758547802, macOS)

### German coverage
- `metabuilder/Localizable.xcstrings`: 2280 / 2298 translatable keys → **99.2 %** (the 49 keys without `de` in the full dump are
  all format-only strings such as `%@`, `1D`, `P50`). 107 German values identical to English (product names, "Pro", "TestFlight").
- No InfoPlist.xcstrings; display name "AppMeta" from build settings (not localized, but it is a brand name). No permission prompts.
- No widgets or extensions.
- **Verdict: app is in German: yes**, with two quality flags: mixed formality (≈174 Sie vs ≈45 du values, e.g. "Synchronisieren Sie
  Verkaufsdaten…" next to du-form strings) and mixed "Keywords"/"Schlüsselwörter".

### Glossary
| English term on site | English UI string | German UI string (catalog) | Note |
|---|---|---|---|
| Locales | Locales | Sprachen | **Flag:** lowercase "locales" = "Sprachregionen"; inconsistent |
| Metadata | Metadata | Metadaten | |
| Name / Subtitle / Promotional Text / Description / What's New | same | Name / Untertitel / Werbetext / Beschreibung / Neue Funktionen | "What's New" label may differ from ASC's own German label; check before using ASC terminology on the page |
| Keywords | Keywords | Schlüsselwörter | **Flag:** some strings use "Keywords" ("Keywords analysieren", "Keywords generieren", "Aktuelle Keyword-Schwierigkeit abrufen") |
| Keyword Optimizer | Keyword Optimizer | Schlüsselwort-Optimierer | |
| Difficulty / Demand / Opportunity | Difficulty / Demand / Opportunity | Schwierigkeit / Nachfrage / Chance | |
| Search coverage | App Store Search Coverage / Coverage | App Store-Suchabdeckung / Abdeckung | |
| Preview changes (diff) | Preview Changes | Änderungen anzeigen | |
| Push | Push / Push All / Push Changes | Pushen / Alle pushen / Änderungen pushen | |
| Refresh | Refresh | Aktualisieren | |
| AI translation | AI Translation / Translate | KI-Übersetzung / Übersetzen | |
| AI provider | Provider / Default Provider | Anbieter / Standardanbieter | |
| Apple Intelligence | Apple Intelligence | Apple Intelligence | |
| Submit for review | Submit for Review | Zur Prüfung einreichen | |
| App Review Information | App Review Information | Informationen zur App-Prüfung | |
| Phased release / Age rating / Availability / Pricing | same | Stufenweise Freigabe / Altersfreigabe / Verfügbarkeit / Preisgestaltung | |
| Reviews | Reviews | Bewertungen | |
| TestFlight / What to Test | same | TestFlight / Was getestet werden soll | |
| In-App Purchases / Subscription Groups | same | In-App-Käufe / Abonnementgruppen | |
| Game Center Achievements / Leaderboards | Achievements / Leaderboards | Erfolge / Bestenlisten | |
| Sales and Analytics | Sales / Analytics | Verkäufe / Analysen | **Flag:** "Click Sales and Trends" → „Sales and Trends" (English) vs "Open Sales & Trends" → „Verkäufe und Trends" |
| Diagnostics | Diagnostics | Diagnose | |
| Screenshots | Screenshots | Screenshots | |
| Issuer ID / Key ID | same | Issuer ID / Key ID | left in English (as ASC) |
| Demo mode | Demo Mode | Demomodus | "Demo (Free)" = "Demo (kostenlos)" |
| Pro | Pro / AppMeta Pro / Unlock Pro | Pro / AppMeta Pro / Pro freischalten | |
| Annual / Lifetime | Yearly / Lifetime | Jährlich / Lebenslang | App Store IAP names "AppMeta Yearly" (untranslated) and "AppMeta Einmalkauf" |
| Restore Purchases | Restore Purchases | Käufe wiederherstellen | |

### German App Store listing
- Name: **AppMeta for App Store Connect** (same as English, not translated)
- Subtitle: **ASO, Metadaten & Rezensionen** (German)
- Price: Kostenlos · In-App-Käufe
- IAPs: `AppMeta Yearly 19,99 €` · `AppMeta Einmalkauf 34,99 €` (flag: "Yearly" IAP display name not localized in ASC)
- Sprachen: Deutsch und 10 weitere

---

### 4. AppMeta Pulse (`appmeta-pulse`, source `metabuilder_phone/`, ID 6758788164)

### German coverage
- Main `metabuilder_phone/Localizable.xcstrings`: 999 / 999 → **100 %** (75 values identical to English: "Dashboard", "MRR",
  "Downloads", "Apps", "Analytics", "YTD")
- `AppShortcuts.xcstrings` (Siri phrases): 3 / 3, German phrase sets translated (e.g. "Öffne ${applicationName}")
- Widget `AppMetaPulseWidget/Localizable.xcstrings`: 254 / 254 → **100 %**
- No InfoPlist.xcstrings; display names "AppMeta Pulse" / "AppMeta Pulse Widget" from build settings (brand, not localized).
- **Verdict: app is in German: yes.**

### Glossary
| English term on site | English UI string | German UI string (catalog) | Note |
|---|---|---|---|
| Dashboard | Dashboard | Dashboard | |
| Apps | Apps | Apps | |
| Analytics | Analytics | Analytics | left in English |
| Reviews | Reviews | Bewertungen | |
| Settings | Settings | Einstellungen | |
| Proceeds | Proceeds | Erlös | widget "PROCEEDS" = "ERLÖS" |
| Sales | Sales | Verkäufe | |
| Units | Units | Einheiten | widget "UNITS" = "EINH." |
| Revenue | Revenue | Umsatz | |
| MRR | MRR | MRR | |
| Active subscriptions | Active Subscriptions | Aktive Abonnements | |
| Trials | Trials / Active Trials | Probeabos / Aktive Probeabos | |
| Trial-to-paid conversion | Trial → Paid / Conversion | Probe → Abo / Konversion | |
| Churn | Monthly Churn / Churn /mo | Churn pro Monat / Churn/Mon. | |
| Cancellations | Cancels / Cancelled | Kündigungen / Gekündigt | |
| New subscriptions | New Subs | Neue Abos | |
| Downloads / Impressions / Product page views | Downloads / Impressions / Product Page Views | Downloads / Abrufe / Produktseitenaufrufe | "Impressions" = "Abrufe": check against App Store Connect's German analytics label before using it on the page |
| Top territories | Top Territories | Top-Länder und -Regionen | |
| Trend comparison | Compare / Previous period / Last year / Custom Range | Vergleich / Vorheriger Zeitraum / Vorjahr / Eigener Zeitraum | |
| Goals | Goals | Ziele | |
| iCloud sync | iCloud Sync | iCloud-Synchronisierung | AllPaid uses "iCloud-Synchronisation" (cross-app difference) |
| AI review reply drafts | Draft suggestions / AI draft per review | Entwurfsvorschläge / KI-Entwurf pro Bewertung | |
| Display currency | Convert to your preferred currency | In deine bevorzugte Währung umrechnen | |
| Demo mode | Demo Mode | Demomodus | |
| Pro (site plan name) | no UI string | n/a | app never says "Pro"; paywall uses Monthly / Yearly / Lifetime |
| Monthly / Yearly / Lifetime | Monthly / Yearly / Lifetime | Monatlich / Jährlich / Lebenslang | |
| Free trial | Start Free Trial | Kostenlos testen | paywall calls the trial "Kostenloses Probeabo" |
| Restore Purchases | Restore Purchases | Käufe wiederherstellen | |

### German App Store listing
- Name: **AppMeta Pulse: Umsatz & Abos** (differs from English)
- Subtitle: none shown on the fetched page
- IAPs as returned by the fetch: `AppMeta Pulse Lebenslang 2,99 €` · `AppMeta Pulse Jahresabo 1,99 €` · `AppMeta Pulse Monatsabo 0,99 €`.
  **Flag:** these look far lower than expected; verify in a browser before using them.
- Sprachen: Deutsch und 14 weitere (Deutsch, Englisch, Französisch, Italienisch, Japanisch, Koreanisch, Niederländisch,
  Portugiesisch, Russisch, Schwedisch, Spanisch, Tradit. Chinesisch, Türkisch, Ukrainisch, Vereinf. Chinesisch)

---

### 5. Chessful (`chessful`, source `Chessful/`, ID 6761336870)

### German coverage
- `Localizable.xcstrings`: 2111 / 2111 → **100 %** (76 values identical to English: "Stockfish", "Premium", "Training", notation)
- `Lessons.xcstrings`: 3649 / 3649 → 100 %
- `InfoPlist.xcstrings`: 2 / 2 → 100 % (display name "Chessful")
- No widget or watch targets.
- **Verdict: app is in German: yes.**

### Glossary
| English term on site | English UI string | German UI string (catalog) | Note |
|---|---|---|---|
| Dashboard (tab) | Dashboard | Übersicht | tab enum in `UI/MainTabView.swift` |
| Play (tab) | Play | Spielen | |
| Analysis (tab) | Analysis | Analyse | |
| Training (tab) | Training | Training | |
| Learn (tab) | Learn | Lernen | |
| Game review | Game Review | Spielbericht | **Flag:** "Game Analysis…" = "Partieanalyse…" (Spiel vs Partie) |
| Accuracy | Accuracy | Genauigkeit | |
| Key moments | Key Moments | Schlüsselmomente | |
| Blunder / Mistake / Inaccuracy | same | Patzer / Fehler / Ungenauigkeit | |
| Better move | See the better move / Best move | Besseren Zug ansehen / Bester Zug | |
| Today's training | Today's Training | Heutiges Training | |
| Train your weaknesses | Train Your Weaknesses | Trainiere deine Schwächen | |
| Skills (5 dimensions) | Skills | Fähigkeiten | |
| Tactics / Defense / Positional / Openings / Endgames | same | Taktik / Verteidigung / Positionell / Eröffnungen / Endspiele | |
| 40 AI opponents | 40 Unique Opponents | 40 einzigartige Gegner | |
| Progress | Progress | Fortschritt | |
| Rating | Rating | Wertung | |
| Achievements | Achievements | Erfolge | |
| 3D board | 3D Board | 3D-Brett | |
| Premium | Chessful Premium / Upgrade to Premium | Chessful Premium / Auf Premium upgraden | App Store IAPs are named "Chessful Pro …" (flag: store says Pro, app says Premium) |
| Free | Free Plan | Kostenloser Plan | |
| Monthly / Yearly / Lifetime | same | Monatlich / Jährlich / Lebenslang | |
| Free trial | Start Free Trial | Kostenlos testen | **Flag:** catalog also has "3-day free trial" = "3 Tage kostenlos" and "$3.33/month · 3-day free trial" (English source also says 3-day); site says 7-day. Check the live trial length |
| Restore Purchases | Restore Purchases | Käufe wiederherstellen | |

Other German flags in Chessful (don't fix the app): "Back-Rank Weakness" = "Grundreihenmatt verpasst" (means "missed back-rank mate", wrong
meaning); "Complete 10 sessions" = "Absolviere 10 Einheiten" but "Complete 100 sessions" = "Schließe 100 Sitzungen ab" (Einheiten vs
Sitzungen); "Defeat all Intermediate opponents" = "Besiege alle Fortgeschrittenen" collides with Advanced = "fortgeschrittenen Gegner";
"Review" = "Wiederholen" (fine for spaced repetition, wrong if used for game review).

### German App Store listing
- Name: **Chessful: Training & Analyse** (differs from English)
- Subtitle: **Rätsel, Coach, Elo & Übungen** (differs)
- Price: Kostenlos · In-App-Käufe
- IAPs: `Chessful Pro Einmalkauf 29,99 €` · `Chessful Pro Jahresabo 17,99 €` · `Chessful Pro Monatsabo 2,99 €` · `Großzügige Unterstützung 9,99 €` ·
  `Unterstützer 5,99 €` · `Kaffee spendieren 1,99 €`
- Sprachen: Deutsch und 32 weitere

## German glossary, batch 2: earnlock, gymlogger-x, liftlog, mediakit, millrace

Source: app string catalogs read 2026-10-26 (no files modified). German values copied verbatim from the catalogs.
App Store data fetched 2026-10-26 from apps.apple.com/de and /us.

---

### 1. EarnLock (earnlock, source `EarnScreen`, ID 6771099230)

### German coverage

| Catalog | Keys | `de` present | `de` translated | % |
|---|---|---|---|---|
| EarnScreen/Localizable.xcstrings (main app) | 613 | 612 | 612 | 99.8% |
| EarnScreen/AppShortcuts.xcstrings | 9 | 9 | 9 | 100% |
| EarnScreen/InfoPlist.xcstrings | 4 | 2 | 0 (both `needs_review`) | 0% translated / 50% present |
| EarnScreenLiveActivity | 147 | 147 | 147 | 100% |
| EarnScreenShield | 6 | 6 | 6 | 100% |
| EarnScreenWatchComplications | 13 | 13 | 13 | 100% |
| watchkitapp Watch App/Localizable | 28 | 28 | 28 | 100% |
| watchkitapp Watch App/InfoPlist | 2 | 2 | 0 (`needs_review`) | 0% translated |
| EarnScreenDeviceActivity, EarnScreenShieldAction | 0 | n/a | n/a | n/a (empty catalogs) |

InfoPlist: the two HealthKit permission texts have German values, but they're marked `needs_review`. CFBundleDisplayName/CFBundleName have no `de` entry, so the display name stays "EarnLock" in every language. The paywall strings live in Localizable and are translated.

**Verdict: the app is in German. Yes** (99.8% of the main app; widgets, Live Activity, shield, and Watch are at 100%).

### Glossary

| English term on site | English UI string (key) | German UI string (catalog) | Note |
|---|---|---|---|
| Free (tier) | no standalone "Free" string; e.g. `Free plan locks 1 app. Tap to upgrade.` | `Kostenlos sperrt 1 App. Zum Upgrade tippen.` | The app calls the free tier "Kostenlos" in some places and "Die Gratisversion" in others (`Free is limited to Steps…`). Flag: inconsistent. |
| Premium | `Premium` | `Premium` | |
| Monthly | `Monthly` | `Monatlich` | |
| Yearly | `Yearly` | `Jährlich` | |
| Lifetime | `Lifetime` | `Lebenslang` | The App Store IAP is named "EarnLock Premium Einmalkauf". The site may prefer "Einmalkauf", but the in-app label is "Lebenslang". |
| Get Premium (button) | `Get Premium` | `Premium holen` | |
| Start free trial (button) | `Start free trial` | `Kostenlos testen` | |
| 7-day free trial | `7-day free trial, then %@/year` | `7 Tage kostenlos testen, danach %@/Jahr` | |
| Restore Purchases | `Restore Purchases` | `Käufe wiederherstellen` | |
| Today tab (the site says "Home screen") | `Today` (tab) | `Heute` | Flag (site): the site says "Tap Reflect on the Home screen", but the app's tab is "Today". Use "Heute" in German. |
| Insights tab | `Insights` | `Auswertungen` | |
| Insights Day / Month view | `Day` / `Month` / `Week` | `Tag` / `Monat` / `Woche` | |
| Settings tab | `Settings` | `Einstellungen` | |
| Shadow Week | `Start Shadow Week` | `Beobachtungswoche starten` | Feature name = **Beobachtungswoche**. Used consistently in all 10 strings. |
| Reflect (button) | `Reflect` | `Reflektieren` | Same in the app, Live Activity, and Watch. |
| Reflection prompt | `What were you hoping to find?` | `Wonach hast du gesucht?` | |
| Reflection answers | `Boredom` / `Anxiety` / `FOMO` / `Habit` / `Other` | `Langeweile` / `Anspannung` / `FOMO` / `Gewohnheit` / `Sonstiges` | "Anxiety" became "Anspannung" (tension), a deliberate softening. Use it as is. |
| Smart Schedules | `Smart Schedules` / `Smart schedules` | `Intelligente Zeitpläne` / `Intelligente Pläne` | Flag: inconsistent. Three strings say "Intelligente Pläne" and one says "Intelligente Zeitpläne". The tab/section `Schedules` is `Zeitpläne`. |
| Goal tiers Light / Standard / Challenge | `Light` / `Standard` / `Challenge` | `Leicht` / `Standard` / `Herausforderung` | |
| Default schedules | `Work hours` / `Evenings` / `Weekends` / `Sleep` | `Arbeitszeit` / `Abends` / `Wochenenden` / `Schlaf` | |
| Daily goal | `Daily goal` | `Tagesziel` | |
| Steps | `Steps` | `Schritte` | |
| Active minutes | `Active minutes` | `Bewegungsminuten` | Flag: `Free is limited to Steps. Active Minutes and Active Calories…` uses `Aktive Minuten` instead. Prefer "Bewegungsminuten" (the goal-picker label). |
| Active energy / calories | `Active calories` | `Aktive Kalorien` | The site says "active energy". The app's goal label is "Aktive Kalorien", and its helper text uses "Aktive Energie". |
| "3,412 steps until unlock" (shield) | `%@ until unlock` (Shield) | `noch %@ bis zur Entsperrung` | Example in catalog: `noch 1.247 Schritte bis zur Entsperrung` (German thousands dot). |
| Emergency unlock | `Emergency unlock` | `Notentsperrung` | |
| Partial unlock | `Partial unlock` (Live Activity) | `Teilfreigabe` | Flag: the main app says `Teil-Entsperrung` (`Your partial unlock ends in 10 minutes.`). The two screens disagree. |
| Rest day | `Rest day` / `Weekly rest day` | `Ruhetag` / `Wöchentlicher Ruhetag` | |
| Streak | `Streak` | `Serie` | |
| Streak shields | `Streak shields` | `Serien-Schilde` | Flag: also `Serien-Schutzschilde` in another string. |
| Most-attempted blocked app | `Most attempted blocked app today` | `Am häufigsten versuchte gesperrte App heute` | |
| Screen time saved (estimate) | `Screen time saved (estimated)` | `Eingesparte Bildschirmzeit (geschätzt)` | Live Activity: `TIME SAVED` → `GESPARTE ZEIT`. |
| Family Sharing | `Family Sharing supported — …` | `Familienfreigabe unterstützt — …` | Apple's own term. |

Widgets: the site names lock-screen widgets, but no widget-name string matched in these catalogs.

### German App Store listing

- Name: **EarnLock: App-Blocker & Fokus** (English: "EarnLock: App Blocker & Focus"). It differs from English.
- Subtitle: **Bildschirmzeit erst verdienen** (English: "Your steps unlock screen time"). It differs.
- IAP prices as shown: `EarnLock Premium Einmalkauf 22,99 €` · `EarnLock Premium Jahresabo 9,99 €` · `EarnLock Premium Monatsabo 1,99 €`
- Sprachen: "Deutsch und 32 weitere"

---

### 2. GymLogger X (gymlogger-x, source `GymLogger`, ID 6755734580)

The app doesn't use .xcstrings or `de.lproj/Localizable.strings`. It loads UI text from JSON files through its own LocalizationManager: `GymLogger/Localizations/<lang>.json`, plus `GymLoggerWidget/Localizations/` and `GymLoggerWatch Watch App/Localizations/`. `de.lproj` holds only InfoPlist.strings.

### German coverage

| Catalog | Keys (en) | `de` present | % | identical to English |
|---|---|---|---|---|
| GymLogger/Localizations/de.json (main app) | 2849 | 2849 | 100% | 119 (mostly loanwords: Training, Deload, PRO, 1RM, e1RM) |
| GymLoggerWidget/Localizations/de.json | 115 | 115 | 100% | 3 |
| GymLoggerWatch Watch App/Localizations/de.json | 98 | 98 | 100% | 11 |
| GymLogger/de.lproj/InfoPlist.strings | display name + Health permissions | present | yes | Display name "GymLogger X"; the permission texts are German. |

Separate exercise and rehab name files also exist (`ExerciseTranslations.de.json`, `RehabTranslations.de.json`).

**Verdict: the app is in German. Yes** (100% of keys in the app, widget, and Watch; permission texts are localized).

### Glossary

| English term on site | English UI string (key) | German UI string | Note |
|---|---|---|---|
| Free | `free` = Free | `Kostenlos` | |
| Pro | `widget_pro` = Pro; `gymlogger_pro` = GymLogger X Pro | `Pro`; `GymLogger X Pro` | Badge: `PRO`. |
| Pro Monthly | `paywall_plan_monthly` = Monthly | `Monatlich` | |
| Pro Annual | `paywall_plan_yearly` = Yearly; `paywall_yearly_pro` = Yearly Pro | `Jährlich`; `Jährlich Pro` | The app says "Yearly", not "Annual". No "Annual" string exists. |
| Lifetime | `paywall_plan_lifetime` = Lifetime | `Lebenslang` | The App Store IAP is "GymLogger X Pro Einmalkauf". |
| Restore Purchases | `restore_purchases` | `Käufe wiederherstellen` | |
| Tabs: Home / Training / Progress / Settings | `home_title` / `training_title` / `progress` / `settings` | `Start` / `Training` / `Fortschritt` / `Einstellungen` | |
| Smart Program Creator | `paywall_tile_program_creator` = Smart Program Creator — built around you | `Smart Program Creator — für dich gemacht` | Kept in English inside the German UI. |
| Plateau detection | `plateau_detection` = Plateau Detection | `Plateau-Erkennung` | Status values: `Plateau erkannt` / `Beobachtung` / `Fortschritt`. |
| Estimated 1RM / e1RM | `analytics_estimated_1rm` = Estimated 1RM | `Geschätzter 1RM` | Widget stamp: `e1RM`. LiftLog uses "1WM" for the same idea, so keep the two apps apart. |
| Deload week | `insert_deload_week` = Insert Deload Week | `Deload-Woche einfügen` | Flag: inconsistent. The Creator says `creator_deload` → `Entlastung`, and `plateau_suggestion_deload` → `Mach eine Entlastungswoche`. Most strings use "Deload". |
| Periodization types: linear / DUP / block / wave | `creator_periodization_*` | `Linear` / `Undulierend (DUP)` / `Block` / `Wellen` | |
| Splits: Full Body / Upper/Lower / PPL / Push/Pull / Arnold / Bro | `creator_split_*` | `Ganzkörper` / `Oberkörper / Unterkörper` / `Push / Pull / Beine` / `Push / Pull` / `Arnold-Split` / `Bro-Split` | Flag: analytics uses `Oben/Unten` for Upper/Lower. |
| Program library | `programs` = Programs; `example_programs` = Example Programs | `Programme`; `Beispielprogramme` | Flag: `program_workouts` (en "Programs") → `Trainingseinheiten`, which looks like a wrong value. |
| The Golden Six (program) | `arnold_golden_six_name` | `The Golden Six` | Name left in English. |
| Rest timer | `watch_a11y_rest_timer` = Rest timer | `Pausentimer` | Watch HR timer: `Herzfrequenz-Pausentimer`. |
| Templates | `templates` | `Vorlagen` | `save_as_template` → `Als Vorlage speichern`. |
| Superset / Giant set | `superset` / `giant_set` | `Supersatz` / `Riesensatz` | LiftLog says `Giant Set`, so the two apps differ. |
| Warm-up set | `warmup_set` / `mark_as_warmup` | `Aufwärmsatz` / `Als Aufwärmsatz markieren` | |
| Personal records / PR board | `personal_records` = Personal Records | `Rekorde` | Flag: also `Persönliche Rekorde` and `Tracking persönlicher Rekorde`, which is inconsistent. |
| Rep-max table | `analytics_rep_max_table` = Rep-Max Table | `Wiederholungsmaxima` | |
| Plate calculator | `plate_calculator` | `Scheibenrechner` | |
| Muscle balance | `muscle_balance` | `Muskelbalance` | |
| Training load | `training_load` | `Trainingsbelastung` | |
| Weekly summary | `weekly_summary_title` | `Wochenzusammenfassung` | |
| Import a coach's spreadsheet program | `import_program` = Import Program; `import_from_spreadsheets` = Spreadsheets (CSV) | `Programm importieren`; `Tabellen (CSV)` | |
| Apple Health export | `health_saved_to_health` = Saved to Apple Health | `In Apple Health gespeichert` | |

Other flags: `widget_calories_heart_rate` ("calories & heart rate") → `Kalorien & Herzfrequenz zu sehen`, which has an extra "zu sehen" fragment. The app mixes "Training" and "Workout" (`Workouts in Apple Health speichern` vs `Trainings`).

### German App Store listing

- Name: **GymLogger X: Workout Tracker**, the same as English.
- Subtitle: **Krafttraining & Gym Tagebuch** (English: "Strength Training & Gym Log"). It differs.
- IAP prices as shown: `GymLogger X Pro Einmalkauf 44,99 €` · `GymLogger X Pro Jahresabo 19,99 €` · `Support the developer 1,00 €` (name not translated). The rest of the list is coach-program IAPs at `14,99 €` to `69,99 €`; their names include third-party coach names, so they're omitted here. No monthly subscription appeared in the top IAP list.
- Sprachen: "Deutsch und 33 weitere"

---

### 3. LiftLog (liftlog, source `CoreLift`, ID 6760043411)

### German coverage

| Catalog | Keys | `de` present | `de` translated | % |
|---|---|---|---|---|
| CoreLift/Resources/Localizable.xcstrings (main app) | 990 | 980 | 980 | 99.0% |
| CoreLift/Resources/AppShortcuts.xcstrings | 6 | 6 | 6 (stringSet `translated`) | 100% |
| CoreLift/Resources/InfoPlist.xcstrings | 4 | 2 | 2 | 50% (the Health permissions are translated; there's no display-name entry, so it uses the build setting "LiftLog") |
| LiftLogWidgets/WidgetLocalizable.xcstrings | 137 | 137 | 137 | 100% |

Flag: the German Health permission texts (and the English ones from the build settings) call the app **"CoreLift"**, not LiftLog: `CoreLift speichert deine abgeschlossenen Krafttrainings in Apple Health…`. This is an app-side naming bug, not a site issue.

**Verdict: the app is in German. Yes** (99% of the main app, 100% of the widgets).

### Glossary

| English term on site | English UI string (key) | German UI string | Note |
|---|---|---|---|
| Free trial | `Free Trial` | `Kostenlose Testphase` | `Free for 7 days.` → `7 Tage kostenlos.` |
| Tier: Fair | `Fair` | `Fair` | The App Store IAP is "Vollversion · Fair". |
| Tier: Good | `Good` | `Gut` | |
| Tier: Generous | `Generous` | `Großzügig` | |
| Tier: Patron | `Patron` | `Förderer` | |
| Restore Purchases | `Restore Purchases` | `Käufe wiederherstellen` | |
| Tabs: Home / Exercises / Programs / Progress / Settings | `Home` / `Exercises` / `Programs` / `Progress` / `Settings` | `Start` / `Übungen` / `Programme` / `Fortschritt` / `Einstellungen` | |
| Log set key | `Log set · start rest` | `Satz protokollieren · Pause starten` | Flag: the plain `Log Set` button is `Satz speichern`, so the two log-set labels disagree. |
| Rest timer | `Rest Timer` / `Rest timer` | `Pausen-Timer` | Flag: some strings spell it `Pausentimer` without the hyphen. |
| Estimated 1RM | `Estimated 1RM` | `Geschätztes 1WM` | Uses "1WM" (Wiederholungsmaximum). GymLogger X uses "1RM", so keep each app's own form. |
| Rep PRs | `Rep PRs` | `Wiederholungsrekorde` | PR badge: `PR`. |
| Personal bests | `Personal Bests` | `Persönliche Bestwerte` | `New Personal Bests` → `Neue Rekorde`, which is inconsistent. |
| Best set / Best volume | `Best Set` / `Best Volume` | `Bester Satz` / `Bestes Volumen` | |
| 26-week activity heatmap | `Complete workouts to see your progress and activity heatmap.` | `…Aktivitäts-Heatmap…` | The feature name is "Aktivitäts-Heatmap". |
| Last 30 days | `Last 30 days` | `Letzte 30 Tage` | |
| Training Max | `Training max` | `Trainingsmaximum` | |
| Double progression / Progression | `Double progression` / `Progression` | `Doppelte Progression` / `Progression` | |
| Deload (trigger) | `Deload` | `Entlastung` | Unlike GymLogger X, which mostly uses "Deload". |
| Adaptive 1RM formula | `Adaptive (recommended)` | `Adaptiv (empfohlen)` | |
| Superset / Giant set | `Superset` / `Giant Set` | `Supersatz` / `Giant Set` | |
| How To (exercise detail) | `How To` | `So geht’s` | Curly apostrophe in the catalog. |
| Workout | `Workout` | `Workout` | The app uses "Workout" throughout. |
| Export (JSON / CSV) | `Export Data (CSV)` / `Export Data (JSON)` | `Daten exportieren (CSV)` / `Daten exportieren (JSON)` | |
| Apple Health | `Apple Health` | `Apple Health` | |

Program names (StrongLifts 5×5, Starting Strength, 5/3/1…) stay in English. The program descriptions are translated.

### German App Store listing

- Name: **LiftLog: Krafttraining Log** (English: "LiftLog: Workout Gym Tracker"). It differs.
- Subtitle: **Sätze, Wiederholungen, Pläne** (English: "Sets, reps & strength programs"). It differs.
- IAP prices as shown: `Vollversion · Fair 9,99 €` · `Vollversion · Gut 22,99 €` · `Vollversion · Großzügig 39,99 €` · `Vollversion · Förderer 44,99 €`
- Sprachen: "Deutsch und 43 weitere"

---

### 4. MediaKit (mediakit, source `ClearCut`, ID 6761451361)

### German coverage

| Catalog | Keys | `de` present | `de` translated | % |
|---|---|---|---|---|
| MediaKit/Localizable.xcstrings (main app) | 2562 | 2562 | 2562 | 100% |
| MediaKit/AppShortcuts.xcstrings | 6 | 6 | 0 (all stringSet `needs_review`) | values present, unreviewed |
| MediaKit/InfoPlist.xcstrings | 25 | 22 | 22 | 88%. The Photo Library and Speech permissions are translated. The missing entries are CFBundleDisplayName, CFBundleName, and NSHumanReadableCopyright, so the name stays "MediaKit". |
| MediaKitShareExtension/Localizable.xcstrings | 13 | 13 | 13 | 100% |

**Verdict: the app is in German. Yes** (100% of the main app; the Shortcuts phrases are present but marked `needs_review`).

### Glossary

| English term on site | English UI string (key) | German UI string | Note |
|---|---|---|---|
| Pro | `Pro` | `Pro` | |
| Pro · Monthly | `Monthly` | `Monatlich` | |
| Pro · Annual | `Annual` | `Jährlich` | |
| Lifetime | `Lifetime` | `Lebenslang` | The App Store IAP is "MediaKit Pro Einmalkauf". |
| Free trial (3 days) | `Start Free Trial`; `Every tool, 3 days free` | `Kostenlose Testphase starten`; `Alle Werkzeuge, 3 Tage gratis` | Flag: inconsistent wording: `%@ Gratistest`, `%@ Gratis-Testphase`, `%@ kostenlos testen`. |
| Free tier (five tools stay free) | `Free tier` | `Kostenlose Stufe` | |
| Tool (generic) | e.g. `Add a Tool to the Recipe` | `Werkzeug` | The app says "Werkzeug" (one recipe string has "Tool-Kette"). |
| Video Compress / Image Compress | tool name `Compress` (id video.compress, image.compress); also `Compress Video` / `Compress Image` | `Komprimieren`; `Video komprimieren` / `Bild komprimieren` | Inside a category the tool shows just "Komprimieren". |
| Image Resize | tool name `Resize` | `Größe ändern` | |
| Audio Convert | tool name `Convert` | `Konvertieren` | |
| PDF Compress | tool name `Compress` (pdf.compress) | `Komprimieren` | |
| Categories: Video / Audio / Image / PDF / Archive / Ebook | same | `Video` / `Audio` / `Bild` / `PDF` / `Archiv` / `E-Book` | |
| Batch processing | `Batch Processing` | `Stapelverarbeitung` | |
| Export presets | `Preset` / `Platform preset` | `Vorgabe` / `Plattform-Vorgabe` | Flag: inconsistent. Some strings say `Voreinstellung`, and one says `Vorlage`. Prefer "Vorgabe". |
| Shortcuts actions | `Shortcuts & Siri` | `Kurzbefehle & Siri` | Apple's term "Kurzbefehle". The 6 action phrases are `needs_review`, e.g. `Video mit ${applicationName} komprimieren`. |
| Merge PDFs | `Merge PDFs` | `PDFs zusammenführen` | Flag: the Shortcuts description says `PDFs zusammenfügen`. |
| Extract text / OCR | `Extract Text from Image` / `OCR` | `Text aus Bild extrahieren` / `OCR` | |
| Remove background | `Remove background` | `Hintergrund entfernen` | |
| AI upscale | `AI Upscale` | `KI-Hochskalierung` | |
| Transcribe | `Transcribe` | `Transkribieren` | |
| Strip EXIF metadata | `Strip Metadata` | `Metadaten entfernen` | |
| Reduce noise | `Noise Reduce` / `Denoise` | `Rauschreduzierung` / `Rauschen entfernen` | |
| Normalize (EBU R128 / LUFS) | `Normalize loudness`; `EBU R128 loudness normalization` | `Lautheit normalisieren`; `EBU-R128-Lautheitsnormalisierung` | |
| Redact | `Redact PDF` | `PDF schwärzen` | |
| Compare two PDFs | `Compare` | `Vergleichen` | Flag: the "Compare Takes" tool is `Takes vergleichen` in some strings and `Aufnahmen vergleichen` in others. |
| Trim / Merge / Stabilize / Watermark / Sign / Encrypt | same | `Kürzen` / `Zusammenführen` / `Stabilisieren` / `Wasserzeichen` / `Unterschreiben` / `Verschlüsseln` | |
| Drop a file in | `Drop a file to preview` | `Datei zum Anzeigen ablegen` | The verb is "ablegen". |
| Menu bar | no UI string (MenuBarExtra titled "MediaKit") | n/a | Use Apple's term "Menüleiste". |
| Restore Purchases | `Restore Purchases` | `Käufe wiederherstellen` | |

### German App Store listing

- Name: **MediaKit: Komprimieren** (English: "MediaKit: Compress & Convert"). It differs.
- Subtitle: **Video, Audio, Bild, PDF & ZIP** (English: "Video, Audio, Image, PDF & ZIP"). It differs.
- IAP prices as shown: `MediaKit Pro Monatsabo 4,99 €` · `MediaKit Pro Jahresabo 24,99 €` · `MediaKit Pro Einmalkauf 44,99 €`
- Sprachen: "Deutsch und 11 weitere"

---

### 5. Millrace (millrace, source `thegame`, ID 6759511759)

Reminder: the site never writes the number that the old app name contained. None of the German strings below contain it, and the German catalog has 0 strings with it.

### German coverage

| Catalog | Keys | `de` present | `de` translated | % |
|---|---|---|---|---|
| thegame/Localizable.xcstrings (only catalog; no widgets or extensions) | 333 | 333 | 333 | 100% |
| InfoPlist | no InfoPlist.xcstrings | | | The display name "Millrace" comes from the build settings and isn't localized (the same name everywhere). The app requests no permissions. |

**Verdict: the app is in German. Yes (100%).**

### Glossary

| English term on site | English UI string (key) | German UI string | Note |
|---|---|---|---|
| Chapter: Warm-up | `Warm-up` | `Aufwärmen` | |
| Chapter: Tactics | `Tactics` | `Taktik` | |
| Chapter: Pressure | `Pressure` | `Druck` | |
| Chapter: Precision | `Precision` | `Präzision` | |
| Chapter: Deep Water | `Deep Water` | `Tiefes Wasser` | |
| Chapter: Mastery | `Mastery` | `Meisterschaft` | |
| Level | `Level %lld` | `Level %lld` | There's no "Chapter" string. |
| Freeplay | `Freeplay` | `Freies Spiel` | |
| Hint | `Hint` | `Tipp` | Flag: `Dismiss tip` is also `Tipp ausblenden`, so "Tipp" means two things in the UI. |
| The Coach | `Coach` | `Coach` | `Coaching notes` → `Hinweise vom Coach`. |
| Daily board / daily challenge | `Daily Challenge` / `Daily challenge` | `Tagesherausforderung` / `Tägliche Herausforderung` | Flag: inconsistent. There's no "daily board" string. Daily best: `Tagesbestwert`. |
| Undo | `Undo` | `Rückgängig` | Flag: the noun forms are awkward: `10 Undos` → `10 Rückgängig`, `Undo Tokens` → `Rückgängig-Token`. They're used verbatim in the App Store IAP names too. |
| Daily streak | `Current Streak` / `Streak Rewards` | `Aktuelle Serie` / `Serien-Belohnungen` | `%lld-day streak` → `%lld-Tage-Serie`. |
| Personal best | `Personal Best` | `Persönlicher Bestwert` | `Best` → `Bestwert`. |
| Move budget / moves left | `%lld moves left` | plural: `Noch %lld Zug` (one) | `No moves left` → `Keine Züge mehr`. There's no "move budget" string. |
| Target cell | `…This is the target cell.` | `…Dies ist das Zielfeld.` | VoiceOver string. The feature term is "Zielfeld". |
| Inlet | no UI string ("inlet" doesn't appear) | VoiceOver: `Hier kommen Kacheln an` | The app describes the inlet without naming it. The site needs its own German term. |
| Tile | (in strings) | `Kachel` | e.g. `Best Tile` → `Beste Kachel`. |
| Blocked (inlet blocked) | `Blocked` | `Blockiert` | |
| Theme / themes | `Theme` / `Themes` | `Theme` / `Themes` | Loanword. |
| Theme packs | `Designer Pack 1` / `Designer Pack 2` / `Summer Pack` / `Winter Pack` | `Designer-Paket 1` / `Designer-Paket 2` / `Sommer-Paket` / `Winter-Paket` | |
| Complete Collection | `Complete collection` | `Komplette Sammlung` | |
| Classic (free theme) and theme names (Studio Clay…) | no catalog entries | n/a | The theme names aren't localized, so they show in English. |
| Support the Developer (tip) | `Support the Developer` | `Entwickler unterstützen` | |
| Game Center leaderboards / achievements | `Leaderboards` / `Achievements` | `Bestenlisten` / `Erfolge` | |
| Settings: Haptics / Sound Effects / Music | same | `Haptik` / `Soundeffekte` / `Musik` | |
| Restore Purchases | `Restore Purchases` | `Käufe wiederherstellen` | |

### German App Store listing

- Name: **Millrace: Zahlen-Denkspiel** (English: "Millrace: Tile Delivery Puzzle"). It differs.
- Subtitle: **64 Rätsel-Level, kein Zufall** (English: "64 forged levels, one inlet"). It differs.
- IAP prices as shown: `Komplette Sammlung 6,99 €` · `Designer-Paket 1 1,99 €` · `Designer-Paket 2 1,99 €` · `Sommer-Paket 1,99 €` · `Winter-Paket 1,99 €` · `10 Rückgängig 0,99 €` · `50 Rückgängig 2,99 €` · `200 Rückgängig 6,99 €` · `Entwickler unterstützen 1,99 €`
- Sprachen: "Deutsch und 33 weitere"

## German glossary, batch 3: Mockly, Observa, Pawza, RightSplit, Shogiful

Extracted 2026-10-26 from the apps' string catalogs, read-only. German values are copied verbatim from the `de`
localization. The App Store data comes from apps.apple.com/de, read through WebFetch. That tool summarizes the
page, so check the price strings once by eye before they go on the site.

Summary

| App | Main target `de` | Extensions | InfoPlist / permissions | Verdict |
|---|---|---|---|---|
| Mockly | 333/334 (99.7%) | none | InfoPlist.xcstrings `de` present, but see flag M1 | **yes** |
| Observa | 6566/6566 (100%) | Watch 474/478 (99.2%), Widgets 402/402 (100%) | 5/5 app, 5/5 watch (Health, Siri texts in German) | **yes** |
| Pawza | 1321/1322 (99.9%) (widget target shares this catalog) | AppShortcuts 4/4 | **no**: camera/photo permission texts are English-only build settings | **yes** (permission prompts in English) |
| RightSplit | 492/492 (100%) | Widgets 376/376, Share 3/3, SplititKit 65/65 (all 100%) | 4/4 (camera, contacts in German) | **yes** |
| Shogiful | 3714/3714 (100%) | none | InfoPlist.xcstrings 0/2 (only display/bundle name, which needs no translation) | **yes** |

The keys still missing `de` are format-only strings (`''`, `'%@'`, `'0'`, `'100'`, `'%@ – %@'`). The exception is
Observa's `Last %@ nights` (main app). The Watch catalog has 4 untranslated keys.

---

### 1. Mockly (AppScreenMaker, ID 6756589122)

**Coverage.** `Resources/Localizable.xcstrings`: 334 keys, 333 with `de`, all in state translated (99.7%). The only
missing key is the empty string. The catalog has 10 languages: de, en, es-ES, es-MX, fr, ja, ko, pt-BR, tr,
zh-Hans. The app has no extensions. `InfoPlist.xcstrings` has 4 of 5 keys in German. The paywall is a set of
translation-credit packs, and those strings are translated. Register: almost entirely du (16 du against 1 Sie).
**Verdict: app is in German: yes.**

**Flags**
- **M1 (wrong display name):** `InfoPlist.xcstrings` sets `CFBundleDisplayName` and `CFBundleName` to
  "ScreenFlow Studio" in every language, en and de included. The build setting says `Mockly`. The catalog is in a
  synchronized group, so it is very likely compiled in, and Finder/Dock may show the old name "ScreenFlow Studio".
  The key `Mockly Project` also has no translations, while the old `ScreenFlow Studio Project` →
  "ScreenFlow Studio-Projekt" does. This needs fixing in the app, not on the site.
- **M2 (unlisted fact):** the app sells one-time **translation packs** ("Translation Packs" → "Übersetzungspakete",
  "Translation Credits" → "Übersetzungsguthaben") as an alternative to bringing your own API key, and the AI
  provider is Claude. The English site only mentions "bring your own API key". The German App Store page shows no
  IAPs, so the packs may not be live. Check this before the German page says "your own API key" only.
- **M3:** the German App Store subtitle says "50 Sprachen". The site says 39 App Store locales. Pick one number.
- "Powered by Claude für hochwertige Screenshot-Lokalisierung." is English and German mixed (it reads like machine
  translation).

**Glossary**

| English term on site | English UI string (key) | German UI string | Note |
|---|---|---|---|
| Upload to App Store Connect | `Upload to App Store Connect` | In App Store Connect hochladen | button |
| App Store Connect credentials | `App Store Connect Credentials` | App Store Connect-Zugangsdaten | settings section |
| API key (bring your own) | `API Key` / `Own API Key` | API-Schlüssel / Eigener API-Schlüssel | |
| AI translation | `AI Translation` | KI-Übersetzung | feature name |
| AI Translate (button) | `AI Translate` | Mit KI übersetzen | |
| Translate All | `Translate All` | Alle übersetzen | |
| Bulk translations | `Bulk Translations` | Sammel-Übersetzungen | |
| Localization panel / localise | `Localizations` | Lokalisierungen | |
| Languages / locales | `Languages` / `Target Languages` / `Source Language` | Sprachen / Zielsprachen / Quellsprache | the app says "Sprachen", not "Locales" |
| Device frames | `Devices` / `Device Style` | Geräte / Geräte-Stil | the app has no string for "3D device frame" or "Metal" |
| Artboard | `Artboard` / `Artboards` | Zeichenfläche / Zeichenflächen | |
| Export | `Export` / `Export %lld Artboards` | Exportieren / %lld Zeichenflächen exportieren | |
| Text overlays / captions | `Text Block` / `Text Blocks` | Textblock / Textblöcke | the app's own word for captions |
| Bulk import (auto-apply) | `Auto-apply screenshots to devices across all pages and languages.` | Screenshots werden automatisch auf Geräte über alle Seiten und Sprachen angewendet. | the app has no "Bulk Import" string |
| CSV import/export of translations | `Import CSV` / `Export CSV` | CSV importieren / CSV exportieren | |
| Background | `Background` | Hintergrund | |
| Shadow | `Shadow` | Schatten | |
| New Project | `New Project` | Neues Projekt | |
| macOS Keychain | `API keys are stored securely in the macOS Keychain…` | API-Schlüssel werden sicher im macOS-Schlüsselbund… | Keychain = "Schlüsselbund" |
| Translation packs (IAP) | `Translation Packs` | Übersetzungspakete | see M2 |
| Restore Purchases | `Restore Purchases` | Käufe wiederherstellen | |
| Templates | no UI string | no UI string | |
| Percentage-based layout | no UI string | no UI string | |

**German App Store listing (apps.apple.com/de/app/id6756589122)**
- Name: **Mockly: Screenshot Maker**
- Subtitle: **50 Sprachen, ein Workflow** (German subtitle)
- Price: **14,99 €** (paid app). No in-app purchases listed.
- Sprachen: "Deutsch und 8 weitere" (Deutsch, Englisch, Französisch, Japanisch, Koreanisch, Portugiesisch,
  Spanisch, Türkisch, Vereinf. Chinesisch)

---

### 2. Observa (HealthLogger, ID 6757438990)

**Coverage.** Main `HealthLogger/Localizable.xcstrings`: 6566 keys, all have `de`, 6554 are explicitly
"translated" (100%). Watch: 474/478 (99.2%). Widgets: 402/402 (100%). Both InfoPlist catalogs (app and watch) are
5/5 in German, including the Health and Siri permission texts. The catalogs hold 41 languages.
**Verdict: app is in German: yes.**

**How the German UI labels HRV:** plain **"HRV"** (keys `HRV`, `metric_label_hrv`, `widget.metric.hrv`). The long
form is **"Herzfrequenzvariabilität"** (`Heart Rate Variability`). The app has no short "HRV (SDNN)" label. SDNN
appears only in explanatory sentences ("Standard Deviation of NN intervals (SDNN)…"). RMSSD and pNN50 stay as they
are ("RMSSD", "pNN50", "Aus EKG abgeleitete RMSSD und pNN50"). For the site: write "HRV (SDNN)" the way the English
page does. Use RMSSD/pNN50 only for the ECG path, which matches the app's "Aus EKG abgeleitete…".

**Flags**
- **O1 (tier name):** most of the in-app paywall calls the tier **"Premium"** ("Premium freischalten", "Auf Premium
  upgraden", "Wöchentliche Reflexionen sind mit Premium verfügbar."). The German App Store IAPs are "Premium
  Jahresabo / Einmalkauf / Monatsabo". The Watch and widgets say **"Observa Pro"** ("Erfordert Observa Pro",
  "Observa Pro erforderlich", widget badge "Pro"). The English site says "Pro". Choose one for the German page.
  The App Store and the main app both say Premium.
- **O2 (register):** the German strings mix forms of address: about 881 strings use Sie, about 250 use du. Examples:
  "Kenne deine persönliche Basislinie" next to "Sehen Sie Ihre persönlichen Baseline-Bänder für Kontext.", and
  "Ihr persönlicher Referenzwert wird erstellt…". This is visible in the app.
- **O3 (inconsistent terms):** baseline appears as "Basislinie", "Baseline" and "Referenzwert". Weekly Reflection
  is "Wöchentliche Reflexion" in the app and "Wöchentlicher Rückblick" in the widget title. Resting HR appears as
  "Ruheherzfrequenz" and "Ruhepuls", and the widget title uses "Ruhepuls" while the widget name says
  "Ruheherzfrequenz". Confidence is "Konfidenz" and "Verlässlichkeit" (`why.section.confidence`). Best Value is
  "Bester Wert", "Bestes Preis-Leistungs-Verhältnis" and "Bestes Angebot".
- **O4:** key `ECG` has de = "ECG" (untranslated). Every other ECG string uses "EKG". "ECG AFib" → "EKG VHF".
- The German App Store subtitle mentions "Zyklus" (cycle). The English site page does not cover cycle tracking.
  This is a fact gap to check.
- The German storefront lists an extra tip IAP, "Entwickler unterstützen" (1,00 €).

**Glossary**

| English term on site | English UI string (key) | German UI string | Note |
|---|---|---|---|
| Tab: Sleep | `Sleep` | Schlaf | tab bar (Sleep, Recovery, Heart, Patterns, More) |
| Tab: Recovery | `Recovery` | Erholung | |
| Tab: Heart | `Heart` | Herz | |
| Tab: Patterns | `Patterns` | Muster | |
| Tab: More | `More` | Mehr | |
| HRV | `HRV` | HRV | see note above, no "(SDNN)" label |
| Heart rate variability | `Heart Rate Variability` | Herzfrequenzvariabilität | |
| ECG-derived RMSSD & pNN50 | `ECG-derived RMSSD & pNN50` | Aus EKG abgeleitete RMSSD und pNN50 | ECG path only |
| ECG | `ECG Recording` / `ECG Analysis` | EKG-Aufzeichnung / EKG-Analyse | bare `ECG` key is untranslated (O4) |
| Sinus rhythm | `Sinus Rhythm` | Sinusrhythmus | |
| Recovery readiness / Readiness score | `Readiness` / `Readiness Score` | Bereitschaft / Bereitschaftswert | App Store subtitle uses "Bereitschaft" |
| Resting heart rate (RHR) | `Resting Heart Rate` / `RHR` | Ruheherzfrequenz / Ruhepuls | inconsistent (O3) |
| Sleep efficiency | `Sleep Efficiency` | Schlafeffizienz | |
| Deep sleep / REM | `Deep Sleep` / `REM Sleep` | Tiefschlaf / REM-Schlaf | |
| Heart-rate dip | `Nocturnal Dip` | Nächtliche Absenkung | the app has no "sleep latency" label |
| Energy | `Energy` | Energie | |
| Personal baseline | `Baseline` | Basislinie | inconsistent (O3) |
| Confidence | `Confidence` | Konfidenz | |
| Patterns / correlations | `Correlation strength (r)` | Korrelationsstärke (r) | |
| Daily insight cards | `Daily insights` / `Insights` | Tägliche Erkenntnisse / Erkenntnisse | |
| Weekly reflection | `Weekly Reflection` | Wöchentliche Reflexion | widget: "Wöchentlicher Rückblick" |
| Long-term trends | `Long-Term Trends` | Langfristige Trends | also "Langzeittrends" |
| Morning check-in | `Morning Check-In` | Morgen-Check-in | |
| Pro / Premium tier | `Premium` / `Upgrade to Premium` | Premium / Auf Premium upgraden | O1 |
| Monthly / Yearly / Lifetime | `Monthly` / `Yearly` / `Lifetime` | Monatlich / Jährlich / Lebenslang | |
| Unlock Lifetime Access | `Unlock Lifetime Access` | Lebenslangen Zugang freischalten | |
| Restore Purchases | `Restore Purchases` | Käufe wiederherstellen | |

**German App Store listing (apps.apple.com/de/app/id6757438990)**
- Name: **Observa: HRV & Recovery Score** (English name kept in DE)
- Subtitle: **Bereitschaft, Schlaf & Zyklus** (German)
- Price: Kostenlos. IAPs: Premium Monatsabo **3,99 €**, Premium Jahresabo **24,99 €**, Premium Einmalkauf
  **59,99 €**, Entwickler unterstützen **1,00 €**
- Sprachen: "Deutsch und 33 weitere"

---

### 3. Pawza (PetCare, ID 6773507068)

**Coverage.** `PetCare/Localizable.xcstrings`: 1322 keys, 1321 with `de`, all translated (99.9%). The only missing
key is `%@`. The widget extension `PetCareWidgets` has no catalog of its own, but the pbxproj adds the app's
`Localizable.xcstrings` to the widget target, so widgets are German too. `AppShortcuts.xcstrings` is 4/4. The
catalog holds 50 languages. **There is no InfoPlist.xcstrings.** The camera and photo-library permission texts
exist only as English `INFOPLIST_KEY_…` build settings, so German users see English permission prompts.
Register: mostly du (80 against 7).
**Verdict: app is in German: yes** (permission prompts and display name come from build settings, in English).

**Flags**
- **P1:** the permission texts are not localized (see above).
- **P2 (inconsistent terms):** pet is "Tier"/"Tiere" almost everywhere, but "Haustiere" appears in "Schalte
  unbegrenzte Haustiere, Scans, Fotos und Pro-Funktionen frei." AI auto-fill is "KI-Autofill" in one string and
  "Automatisches Ausfüllen mit KI" in another. The iCloud account is "iCloud-Account" in one place and
  "iCloud-Konto" in another.
- **P3 (wrong meaning):** `Syncing with iCloud...` → "Mit iCloud synchronisieren …". That reads as a command, not a
  progress state.
- "Free accounts include 10 document scans" is translated as "Kostenlose Konten…", but the app has no accounts.
  This is minor.

**Glossary**

| English term on site | English UI string (key) | German UI string | Note |
|---|---|---|---|
| Tab: Pets | `Pets` | Tiere | tabs: Pets, Reminders, Settings |
| Tab: Reminders | `Reminders` | Erinnerungen | |
| Tab: Settings | `Settings` | Einstellungen | |
| Pet / Add pet | `Pet` / `Add Pet` | Tier / Tier hinzufügen | |
| Health records | `Records` | Einträge | |
| Vaccinations | `Vaccinations` | Impfungen | |
| Medications | `Medications` | Medikamente | |
| Vet visits | `Vet visits` | Tierarztbesuche | |
| Weight / weight trend | `Weight` / `Weight trend alerts` | Gewicht / Warnungen bei Gewichtstrend | |
| Document scanning | `Scan a vet document` | Tierarztdokument scannen | |
| AI auto-fill | `Unlock AI auto-fill` | Automatisches Ausfüllen mit KI freischalten | also "KI-Autofill" (P2) |
| AI summaries | `AI Summaries` / `AI summaries for every record` | KI-Zusammenfassungen / KI-Zusammenfassungen für jeden Eintrag | |
| Apple Intelligence summary | `Apple Intelligence summary` | Zusammenfassung von Apple Intelligence | |
| Vet-visit PDF | `Vet Visit PDF` / `Vet visit PDF generator` | Tierarztbesuch-PDF / Tierarztbesuch-PDF-Generator | short form "Tierarzt-PDF" |
| Emergency card | `Emergency Card` | Notfallkarte | |
| Photo gallery | `Unlimited photo gallery` | Unbegrenzte Fotogalerie | |
| Unlimited pets and scans | `Unlimited pets and scans` | Unbegrenzte Tiere und Scans | |
| Free / Pro | `Free` / `Pawza Pro` / `Pro` | Kostenlos / Pawza Pro / Pro | |
| Monthly / Yearly / Lifetime | `Monthly` / `Yearly` / `Lifetime` | Monatlich / Jährlich / Lebenslang | |
| 7-day free trial | `Start 7-day free trial` | 7 Tage gratis testen | |
| Due / Upcoming | `Due` / `Upcoming` | Fällig / Anstehend | |
| iCloud sync | `iCloud Sync: up to date.` | iCloud-Sync: aktuell. | |
| Restore Purchases | `Restore Purchases` | Käufe wiederherstellen | |

**German App Store listing (apps.apple.com/de/app/id6773507068)**
- Name: **Pawza: Haustier-Gesundheit** (German)
- Subtitle: **Impfpass, Termin & Erinnerung** (German)
- Price: Kostenlos. IAPs: Pawza Pro Monatsabo **2,99 €**, Pawza Pro Jahresabo **22,99 €**, Pawza Pro Einmalkauf
  **44,99 €**
- Sprachen: "Deutsch und 43 weitere"

---

### 4. RightSplit (splitit, ID 6757268612)

**Coverage.** Main `splitit/Localizable.xcstrings`: 492/492 (100%). Widgets: 376/376. Share extension: 3/3.
SplititKit package: 65/65. `InfoPlist.xcstrings`: 4/4 (camera and contacts texts in German). The catalogs hold
40 languages. Register: mostly du. I ignored the copy under `.claude/worktrees/`.
**Verdict: app is in German: yes.**

**Flags**
- **R1:** the lifetime tier is both "Pro+ Lebenslang" and "Pro+ Lifetime freischalten". The App Store calls it
  "RightSplit Pro+ Einmalkauf".
- **R2:** **Spaces** is translated as "Bereiche" ("Neuer Bereich"). That word is generic but consistent, so use it
  on the site.
- "Trips & shared expenses" → "Reisen & Ausgaben" drops "shared".
- "Everyone's settled — no transfers needed." uses an em dash in German too. That is fine in the UI, but don't copy
  it to the site (no-dash rule).

**Glossary**

| English term on site | English UI string (key) | German UI string | Note |
|---|---|---|---|
| Scan receipt | `Scan Receipt` | Beleg scannen | receipt = "Beleg" throughout |
| Receipts | `Receipts` | Belege | |
| Receipt language | `Receipt Language` | Belegsprache | |
| Item-level splits | `Split by items` | Nach Artikeln aufteilen | |
| Shared dishes | `Shared dishes` / `Add shared item` | Geteilte Gerichte / Geteilten Artikel hinzufügen | |
| Equal splitting | `Equal splits & tip` | Gleiche Aufteilung & Trinkgeld | |
| Per person | `Per person` / `Adjust per person` | Pro Person / Pro Person anpassen | |
| Tip | `Tip` / `Tip percent` | Trinkgeld / Trinkgeld in % | |
| Tax | `Tax` | Steuer | |
| Fair rounding | `Round fairly` | Fair runden | |
| Send totals (iMessage/WhatsApp) | `Text / WhatsApp share` / `Send Payment Requests` | Per Nachricht / WhatsApp teilen / Zahlungsaufforderungen senden | |
| Spaces | `Spaces` / `New space` | Bereiche / Neuer Bereich | R2 |
| Trips | `Trips` | Reisen | |
| Balances / settle-up | `Balance` / `Settlement` / `Settle in` | Saldo / Ausgleich / Abrechnen in | |
| Split history | `History` / `Unlimited split history` | Verlauf / Unbegrenzter Aufteilungsverlauf | |
| People | `People` | Personen | |
| Free | `Free` | Kostenlos | |
| Pro+ | `Pro+` / `Unlock Pro+` | Pro+ / Pro+ freischalten | |
| Pro+ yearly | `Pro+ Yearly` | Pro+ Jährlich | |
| Pro+ lifetime | `Pro+ Lifetime` | Pro+ Lebenslang | R1 |
| Restore Purchases | `Restore Purchases` | Käufe wiederherstellen | |

**German App Store listing (apps.apple.com/de/app/id6757268612)**
- Name: **RightSplit: Beleg Teilen** (German)
- Subtitle: **Ausgaben & Trinkgeld aufteilen** (German)
- Price: Kostenlos. IAPs: RightSplit Pro+ Jahresabo **4,99 €**, RightSplit Pro+ Einmalkauf **8,99 €**
- Sprachen: "Deutsch und 33 weitere"

---

### 5. Shogiful (shogi, ID 6761656926)

**Coverage.** `Localization/Localizable.xcstrings`: 3714/3714 with `de`, all translated (100%). The catalog holds
39 languages. The app has no extensions. `InfoPlist.xcstrings` has 0/2, but it contains only `CFBundleDisplayName`
and `CFBundleName` (Shogiful), and the app requests no permissions. Register: mostly du (519 against 29). The
paywall plans are translated.
**Verdict: app is in German: yes.**

**Flags**
- **S1 (fact):** the site says "10 AI opponents across 4 tiers". The code has 8 `OpponentTier` levels (Novice,
  Beginner, Casual, Club Player, Intermediate, Advanced, Expert, Master). Check the site claim.
- **S2:** the site's "Western piece sets" is called **"International"** in the app (`settings.pieceSet.western`).
  The setting is "Steinstil" (Piece Style). Shogi pieces are "Steine", and drops are "Einsetzen"
  ("Einsatzfehler", "Einsatz-Taktiker").
- Rating is "Wertung" / "Geschätzte Wertung". The dashboard tab is "Start" (key `tab.dashboard`, English
  "Dashboard").
- The app has no "skill radar" string. It shows "Dein Fähigkeitsprofil" (Your skill profile).
- `gc.achievement.tsume_addict.title` → "Tsume-Süchtiger" is masculine-only. This is minor.

**Glossary**

| English term on site | English UI string (key) | German UI string | Note |
|---|---|---|---|
| Tab: Dashboard | `Dashboard` (`tab.dashboard`) | Start | |
| Tab: Play | `Play` (`tab.play`) | Spielen | |
| Tab: Analysis | `Analysis` (`tab.analysis`) | Analyse | |
| Tab: Training | `Training` (`tab.training`) | Training | |
| Tab: Progress | `Progress` (`tab.progress`) | Fortschritt | |
| Premium | `Shogiful Premium` (`settings.premium.name`) | Shogiful Premium | |
| Premium · Monthly | `Premium Monthly` (`paywall.plan.monthly`) | Premium Monatsabo | matches App Store IAP name |
| Premium · Annual | `Premium Yearly` (`paywall.plan.yearly`) | Premium Jahresabo | |
| Lifetime | `Premium Lifetime` (`paywall.plan.lifetime`) | Premium Einmalkauf | |
| Tsume-shogi | `Tsume-Shogi: Forced Checkmate` | Tsume-Shogi: das erzwungene Matt | puzzles = "Tsume-Aufgaben" |
| Deep analysis | `Go deeper` (`paywall.hero.deepAnalysis.title`) | Geh tiefer | the app has no "Deep Analysis" label |
| Western / kanji piece sets | `International` / `Traditional (Kanji)` | International / Traditionell (Kanji) | S2 |
| Piece style setting | `Piece Style` | Steinstil | |
| Estimated rating | `Estimated Rating` | Geschätzte Wertung | |
| Accuracy trends | `Accuracy Trend` | Genauigkeitsverlauf | |
| Skill radar / profile | `Your skill profile` | Dein Fähigkeitsprofil | no "radar" string |
| Five skills | `Tactics` / `Defense` / `Positioning` / `Endgame` / `Openings` | Taktik / Verteidigung / Stellungsspiel / Endspiel / Eröffnungen | |
| Blunder / Mistake / Inaccuracy | `Blunder` / `Mistake` / `Inaccuracy` | Patzer / Fehler / Ungenauigkeit | |
| Drop mistake | `Drop Mistake` | Einsatzfehler | drop = "Einsetzen" |
| Promotion mistake | `Promotion Mistake` | Umwandlungsfehler | promote = "Umwandeln" |
| Castle weakness | `Castle Weakness` | Burgschwäche | |
| Hanging piece | `Hanging Piece` | Hängender Stein | |
| Missed fork | `Missed Fork` | Verpasste Gabel | |
| Missed tsume | `Missed Tsume` | Verpasstes Tsume | |
| Passive move | `Passive Move` | Passiver Zug | |
| Opponent tiers | `Novice`…`Master` (`opponentTier.*`) | Neuling, Anfänger, Gelegenheitsspieler, Vereinsspieler, Mittelstufe, Fortgeschritten, Experte, Meister | S1 |
| Restore Purchases | `Restore Purchases` | Käufe wiederherstellen | |

**German App Store listing (apps.apple.com/de/app/id6761656926)**
- Name: **Shogiful: Shogi lernen & üben** (German)
- Subtitle: **Japanisches Schach, KI-Analyse** (German)
- Price: Kostenlos. IAPs: Premium Monatsabo **1,99 €**, Premium Jahresabo **9,99 €**, Premium Einmalkauf **22,99 €**.
  Tip IAPs: Unterstützer 5,99 €, Riesige Unterstützung 9,99 €, Kaffee 1,99 €
- Sprachen: "Deutsch und 32 weitere"

## German glossary, batch 4: soon, tare, taskful-day, wanderwiki, xiangqiful

Extracted 2026-10-26 from each app's source string catalogs (read-only) and the German App Store storefront.
German values are copied verbatim from the catalogs. All `de` entries found are in state "translated".

Storefront price format (checked in the raw HTML for Tare): `2,99 €`, with a **no-break space (U+00A0)**
between the number and €. The other storefronts showed the same `x,xx €` pattern.

---

### 1. Soon. (`soon`, source `countdown`, ID 6757280643)

### German coverage
| Catalog | keys | `de` translated | % |
|---|---|---|---|
| countdown/Localizable.xcstrings (main app) | 741 | 741 | 100 % |
| countdown/AppShortcuts.xcstrings | 13 | 13 | 100 % |
| countdown/InfoPlist.xcstrings | 6 | 5 | 83 % (only the stray key `Soon` is missing; display name, calendar and location permission texts are in German) |
| CountdownWidgets/Localizable.xcstrings | 184 | 182 | 98.9 % (missing only the format strings `%@ ` and `%@ %@`) |

The paywall strings are in the main catalog and are translated. **Verdict: app is in German: yes.**

### Glossary
| English term on site | English UI string (key) | German UI string | Note |
|---|---|---|---|
| Home tab | `Home` | Start | tab |
| Plan tab | `Plan` | Planen | tab |
| Search tab | `Search` | Suche | tab |
| Profile tab | `Profile` | Profil | tab |
| Plan Mode | `Plan mode reminders` | Erinnerungen im Planmodus | the only UI string naming "Plan Mode", so the German name is **Planmodus**. There's no standalone "Plan Mode" label |
| Premium | `Premium` | Premium | |
| Free | `Free` | Kostenlos | |
| Monthly / Annual | `Monthly` / `Yearly` | Monatlich / Jährlich | the app says "Yearly", not "Annual" |
| Lifetime | `Lifetime` | Einmalkauf | not "Lebenslang" |
| 7-day free trial | `1 week free` / `Free trial` | 1 Woche gratis / Kostenlose Testversion | |
| Restore purchases | `Restore Purchases` | Käufe wiederherstellen | |
| Countdown / event / moment | `Countdown` / `Event` / `Moment` / `Moments` | Countdown / Ereignis / Moment / Momente | the app mostly calls events "moments" |
| Memories | `Memories` / `Memory` | Erinnerungen / Erinnerung | FLAG: same word as `Reminders` → "Erinnerungen", so German readers can't tell them apart |
| Reminders / event notifications | `Reminders` | Erinnerungen | see the flag above |
| Reflection mode | `Notes` (reflection section header) | Notizen | no UI string says "Reflection". The section is labelled "Notes" |
| Daily notes | `Personalized daily notes` / `Weather & daily notes` | Persönliche tägliche Notizen / Wetter & tägliche Notizen | |
| Live (destination) weather | `Weather` / `Weather forecast` / `Smart weather forecast` | Wetter / Wettervorhersage / Smarte Wettervorhersage | attribution: `Weather data provided by Apple Weather` → "Wetterdaten bereitgestellt von Apple Wetter" |
| Calendar import / sync | `Import from your calendar` / `Turn calendar events into countdowns` | Aus deinem Kalender importieren / Kalenderereignisse in Countdowns umwandeln | |
| Recurring events | `Recurring countdowns` / `Repeat` | Wiederkehrende Countdowns / Wiederholen | |
| Natural language search | `Search` | Suche | no UI string for the feature name. Example hints are lower-cased German: "“reise im juli” — filtert nach Kategorie und Datum" |
| Timeline / checklist | `Timeline` / `Checklist` | Zeitleiste / Checkliste | |
| Themes | `Theme` / `All themes unlocked` | Thema / Alle Themen freigeschaltet | theme names are not localized. FLAG: the site says the free themes are "Classic, Soft, Midnight", but the code's free themes are sunrise, ocean, and forest, and Midnight is Premium |
| Widget styles: ring / timeline | widget `Progress Rings`, `Soon · Ring`, `Soon · Timeline`, `TIMELINE` | Fortschrittsringe, Soon · Ring, Soon · Timeline, ZEITLEISTE | widget gallery names stay in English (`Soon · Rings`, `Soon · Timeline Full`) |
| StandBy | widget `Soon · StandBy` | Soon · StandBy | description: "…abgestimmt auf den StandBy-Modus" |
| Lock Screen / Home Screen | `Keep on Lock Screen` / `…Home Screen…` | Sperrbildschirm / Home-Bildschirm | FLAG: inconsistent, the catalog uses both "Home-Bildschirm" and "Homescreen" |
| Event types: Trip, Wedding, Birthday, Anniversary, Concert, Custom | `Trip` `Wedding` `Birthday` `Anniversary` `Concert` `Moment` | Reise, Hochzeit, Geburtstag, Jahrestag, Konzert, Moment | |
| Event type "Pregnancy" | `Baby` | Baby | FLAG: the app's category is "Baby", not "Pregnancy". The app has no "Graduation" or "Move" type. Its other types are Exam→Prüfung, Work→Arbeit, Holiday→Feiertag, Health→Gesundheit, Sport→Sport |
| On This Day (memories) | `ON THIS DAY` | AN DIESEM TAG | |

Other flags:
- The `Save` button → "Sichern" while `Save moment` → "Moment speichern", which is inconsistent.
- Formality mixes "Sie" and "du". Examples: `Plan this moment — …` → "Planen Sie diesen Moment …", `Plan your moments` → "Planen Sie Ihre Momente", `One time — yours forever` → "Einmalig – für immer Ihres". Almost everything else uses "du".
- The catalog has iCloud sync strings (`iCloud Sync` → "iCloud-Synchronisierung", "Deine Momente sind in iCloud gesichert"). The site says the data is on-device only. Check this before translating.

### German App Store listing
- Name: **Soon. - Tage bis große Events** (English: "Soon.", so it differs)
- Subtitle: **Hochzeit, Reise Baby Countdown**
- In-app purchases: `Entwickler unterstützen 1,00 €` · `Premium Einmalkauf 14,99 €` · `Premium Monatsabo 1,99 €` · `Premium Jahresabo 9,99 €`
- Sprachen: **Deutsch und 35 weitere** (the site says 39 languages)

---

### 2. Tare (`tare`, source `weightbalance`, ID 6806255929)

### German coverage
| Catalog | keys | `de` translated | % |
|---|---|---|---|
| weightbalance/Localizable.xcstrings (main app, the only catalog) | 121 | 121 | 100 % |

There is no InfoPlist.xcstrings. The display name "Tare" is set in the build settings, and the app has no permission prompts. The project's knownRegions include `de`. **Verdict: app is in German: yes.**

### Glossary
| English term on site | English UI string (key) | German UI string | Note |
|---|---|---|---|
| Chapter I…X | `Chapter %lld` | Kapitel %lld | |
| Unlock / buy chapters | `Open Chapters %lld to %lld` / `Buy Chapters %lld to %lld, %@` | Kapitel %1$lld bis %2$lld freischalten / Kapitel %1$lld bis %2$lld kaufen, %3$@ | |
| Restore purchases | `Restore purchases` | Käufe wiederherstellen | |
| Settings | `Settings` | Einstellungen | |
| Hints | `Hints` / `Hint` | Hinweise / Hinweis | |
| Three gold stars | `Marks` | Sterne | the setting is called "Marks" in English and "Sterne" in German |
| Sound / Haptics | `Sound` / `Haptics` | Ton / Haptik | |
| High contrast | `High contrast` | Hoher Kontrast | |
| Beam / hook / notch | `Beam %lld` / `empty hook` / `notch` | Balken %lld / leerer Haken / Kerbe | |
| Hidden "?" weight | `hidden %@` / `cannot settle, hidden weight` | %@, verdeckt / kann nicht zur Ruhe kommen, verdecktes Gewicht | the German word for "hidden" here is "verdeckt" |
| Picture cards | `Reference scale` | Vergleichswaage | no UI string says "picture card". VoiceOver reads the cards as "reference scale" |
| Shelf (weights below) | `Tray` / `Return to tray` | Ablage / Zurück in die Ablage | |
| Balanced | `Balanced` | Im Gleichgewicht | |
| Chapter names | `The Hang`, `The Secret`, `The Cascade`, `The Exhibition`, `The Ledger`, `The Inventory`, `The Fulcrum`, `The Forgery`, `The Restoration`, `The Retrospective` | Das Aufhängen, Das Geheimnis, Die Kaskade, Die Ausstellung, Die Bilanz, Die Inventur, Der Drehpunkt, Die Fälschung, Die Erneuerung, Der Rückblick | |
| Worlds | `Morning Sky`, `Twilight Meadow`, `Deep Sea`, `Evening Stars`, `Coral Reef`, `Firefly Forest`, `Polar Night`, `Rose Dawn`, `Summer Fields`, `Sunset Hills` | Morgenhimmel, Dämmerwiese, Tiefsee, Abendsterne, Korallenriff, Glühwürmchenwald, Polarnacht, Morgenröte, Sommerfelder, Hügel im Abendrot | |
| Mobile | `Mobile` | Mobile | |
| Play | `Play` | Spiel | FLAG: this is a noun ("game"). If it's a button, "Spielen" would be right |

### German App Store listing
- Name: **Tare: Logikrätsel & Denkspiel** (English: "Tare", so it differs)
- Subtitle: **Balance-Puzzle & Gehirnjogging**
- In-app purchase: `Kapitel II–IV 2,99 €` (U+00A0 before €). FLAG: the IAP is named "Chapters II–IV" in the German storefront, but the site says the one purchase unlocks Chapters II to X. Check the IAP display name in App Store Connect.
- Sprachen: **Deutsch und 43 weitere**

---

### 3. Taskful Day (`taskful-day`, source `TaskLogger`, ID 6757345400)

### German coverage
| Catalog | keys | `de` translated | % |
|---|---|---|---|
| TaskLogger/Localization/Localizable.xcstrings (main app) | 1421 (+1 not translatable) | 1421 | 100 % |
| TaskfulDayKit Localizable.xcstrings (shared package) | 113 | 111 | 98.2 % (missing `End focus session`, `Extend focus session`) |
| TaskLogger/InfoPlist.xcstrings | 7 | 7 | 100 % (calendar, reminders, microphone, and speech permission texts) |
| TaskLogger/AppShortcuts.xcstrings | 12 | 12 | 100 % |
| TaskLoggerWidgetsExtension Localizable + InfoPlist | 420 + 3 | 420 + 3 | 100 % |
| watch app AppShortcuts.xcstrings | 4 | 4 | 100 % (FLAG: the source has a watch target, and the site says there's no Watch app) |

**Verdict: app is in German: yes.**

### Glossary
| English term on site | English UI string (key) | German UI string | Note |
|---|---|---|---|
| Day Clock | `Day Clock` (`clock.title`, `pro.feature.clock_view`) | Tagesuhr | the picker label is `Clock` → "Uhr" |
| Energy River | `Energy River` (`river.title`) | Energiefluss | the picker label is `River` → "Fluss" |
| Day Map | `Day Map` (`pro.feature.day_map`) | Tageskarte | the picker and title use `Map` → "Karte" |
| Focus Orbit | `Focus Mode` (`pro.feature.focus_orbit`) | Fokusmodus | FLAG: no UI string says "Focus Orbit". The app calls it Focus Mode / Fokusmodus |
| Focus session | `Focus Session` / `Start Focus` | Fokus-Sitzung / Fokus starten | |
| Inbox | `Inbox` | Eingang | |
| Today / Tomorrow | `Today` / `Tomorrow` | Heute / Morgen | |
| Tabs | `Tasks`, `All Tasks`, `Analytics`, `Settings` | Aufgaben, Alle Aufgaben, Einblicke, Einstellungen | "Analytics" tab → "Einblicke" |
| Insights / analytics | `Insights` / `Full Analytics & Insights` | Einblicke / Einblicke & Statistiken | |
| Journal | `Journal` | Tagebuch | |
| Mood | `Mood` / `Mood pattern` | Stimmung / Stimmungsmuster | |
| Workspaces | `Workspace` / `Multiple Workspaces` | Arbeitsbereich / Mehrere Arbeitsbereiche | |
| Tasks roll forward | `Carry Forward` / `Auto carry-forward` / `Rollover` | Verschieben / Automatisch verschieben / Verschiebungen | FLAG: inconsistent, the iPad canvas uses "Übertragen" / "Automatisch übertragen" |
| Voice capture | `Voice capture` / `Voice Task` | Spracheingabe / Sprachaufgabe | |
| iCloud sync | `iCloud Sync` | iCloud-Synchronisierung (Pro list) / iCloud-Sync (Settings) | inconsistent between screens |
| Apple Reminders import | `Import from Reminders` / `Reminders Re-import` | Erinnerungen importieren / Aus Erinnerungen importieren / Apple Erinnerungen importieren | three variants |
| Widgets (Pro) | `All Widgets` | Widgets auf dem Homescreen | FLAG: this means "widgets on the Home Screen", not "all widgets" |
| Pro / Taskful Day Pro | `Taskful Day Pro` / `Unlock Pro` | Taskful Day Pro / Pro freischalten | |
| Free | `Free Plan` / `Available with Free` | Kostenlos / Mit Free verfügbar | inconsistent |
| Monthly / Yearly / Lifetime | `pro.plan.*` | Monatlich / Jährlich / Einmalig | Lifetime → "Einmalig" here (Soon. uses "Einmalkauf") |
| 7-day free trial | `7-day free trial` / `Start 7-day free trial` | 7 Tage kostenlos testen / Kostenlose Testphase starten | |
| Restore purchases | `Restore Purchases` | Käufe wiederherstellen | |

Other flags:
- `Smarter Voice Input` → "Sprachbasierte Eingabe" drops "smarter", but the paywall title is "Smartere Spracheingabe".
- The paywall lists Day Clock, Day Map, Energy River, and Focus Mode as Pro features. The site's Free tier says "All four visual day views", and the code partly gates them with `isPro`. Check before translating the Free tier.
- Formality mix: `settings.notifications.permission_message` uses "aktivieren Sie". Everything else uses "du".

### German App Store listing
- Name: **Taskful Day: Tagesplaner** (English: "Taskful Day", so it differs)
- Subtitle: **Aufgaben, To-Do & Routine**
- In-app purchases: `Taskful Day Pro Einmalkauf 44,99 €` · `Entwickler unterstützen 1,00 €` · `Taskful Day Pro Jahresabo 29,99 €` · `Taskful Day Pro Monatsabo 2,99 €`
- Sprachen: **Deutsch und 33 weitere**

---

### 4. WanderWiki (`wanderwiki`, source `WanderWiki`, ID 6758459119)

### German coverage
| Catalog | keys | `de` translated | % |
|---|---|---|---|
| WanderWiki/Resources/Localizable.xcstrings (main app) | 423 | 423 | 100 % |
| WanderWikiWidget/Localizable.xcstrings | 118 | 118 | 100 % |

There is no InfoPlist.xcstrings. The display name "WanderWiki" comes from the build settings, and no permission texts are localized (none are declared). **Verdict: app is in German: yes.**

### Glossary
| English term on site | English UI string (key) | German UI string | Note |
|---|---|---|---|
| Random | `Random` (`random_mode`) | Zufällig | |
| Browse | `Browse` (`browse_title`) | Stöbern | |
| For You | `For You` (`for_you_mode`) | Für dich | FLAG: `for_you_english_only` says "Der personalisierte Feed ist derzeit nur auf Englisch verfügbar." The site says native category queries work in 17 editions. The string may be stale |
| Today in History | `Today in history` / `On This Day` | Heute in der Geschichte | both English terms map to the same German string |
| On This Day categories | `Events` / `Births` / `Deaths` / `Holidays` | Ereignisse / Geburten / Todesfälle / Feiertage | no string found for "Selected" |
| Tabs | `Feed` / `Profile` / `settings` | Feed / Profil / Einstellungen | |
| WanderWiki Plus | `Unlock Premium` / `Premium feature` | Premium freischalten / Premium-Funktion | FLAG: the app has no "Plus" string. It calls the tier "Premium" ("WanderWiki ist ein Premium-Erlebnis.") |
| Monthly / Annual / Lifetime | `monthly` / `yearly` / `lifetime` | Monatlich / Jährlich / Lebenslang | |
| Best long-term value | `Best Value` | Bestes Angebot | |
| Free trial | `%lld-day free trial` | %lld Tage kostenlos testen | also "%lld-tägige Testversion starten" |
| 20 free articles a day | `%lld free articles left today` | Noch %lld kostenlose Artikel heute | |
| Restore purchases | `Restore Purchases` | Käufe wiederherstellen | |
| Saved | `saved` / `Saved` | Gespeichert / Gesichert | FLAG: two different German words for the same thing |
| Liked list | `Liked` | Favoriten | |
| Folders | `Folders` / `New folder` | Ordner / Neuer Ordner | |
| Read aloud | `Listen` | Anhören | |
| Where Next | `Where next` | Wohin als Nächstes | |
| Show less like this / Hide this article | same | Weniger davon anzeigen / Diesen Artikel ausblenden | |
| Reader themes | `Reader Theme`, `Sepia`, `Solarized` | Lesethema, Sepia, Solarized | |
| Search | `Search Wikipedia` | Wikipedia durchsuchen | |
| Reading streak | `%lld-day streak` / `Streak reminder` | %lld-Tage-Serie / Serien-Erinnerung | |
| Widgets | `On This Day`, `Reading Year`, `Continue Reading`, `Got a Minute`, `Two Doors` | Heute in der Geschichte, Lesejahr, Weiterlesen, Kurz Zeit?, Zwei Türen | |
| Control: Surprise Me | `Surprise Me` | Überrasch mich | |
| On-device summaries | `AI summary: %@` | KI-Zusammenfassung: %@ | |
| 16 topics | `interest_*` | Wissenschaft, Technologie, Geschichte, Kunst, Musik, Sport, Natur, Weltraum, Philosophie, Geografie, Literatur, Filme, Essen, Architektur, Mathematik, Politik | |

### German App Store listing
- Name: **WanderWiki: Wissen entdecken** (English: "WanderWiki", so it differs)
- Subtitle: **Fakten, Geschichte & Trivia**
- In-app purchases: `WanderWiki Jahresabo 9,99 €` · `WanderWiki Monatsabo 1,99 €` · `WanderWiki Wochenabo 0,99 €` · `Entwickler unterstützen 1,00 €` · `WanderWiki Einmalkauf 29,99 €`. FLAG: there's a weekly subscription ("Wochenabo") that the site doesn't list.
- Sprachen: **Deutsch und 33 weitere**

---

### 5. Xiangqiful (`xiangqiful`, source `Xiangqi`, ID 6794340136)

### German coverage
| Catalog | keys | `de` translated | % |
|---|---|---|---|
| Xiangqi/Localization/Localizable.xcstrings (main app, includes the paywall) | 3263 | 3263 | 100 % |
| Xiangqi/Localization/InfoPlist.xcstrings | 2 | 2 | 100 % (display name only, which stays "Xiangqiful") |

There are no widget or extension catalogs. **Verdict: app is in German: yes.**

### Glossary
| English term on site | English UI string (key) | German UI string | Note |
|---|---|---|---|
| Tabs | `Home`, `Play`, `Training`, `Analysis`, `Progress` (`tab.*`) | Start, Spielen, Training, Analyse, Fortschritt | |
| Game Review | `Game review` | Partieanalyse | |
| Analyze | `Analyze` | Analysieren | |
| Move grades | `Best`, `Great`, `Good`, `Book`, `Inaccuracy`, `Mistake`, `Blunder` (`classification.*`) | Bester Zug, Sehr guter Zug, Guter Zug, Buchzug, Ungenauigkeit, Fehler, Patzer | the counts header uses "Beste Züge" |
| Accuracy | `Accuracy` | Genauigkeit | |
| Estimated rating | `Estimated rating` | Geschätzte Wertung | FLAG: Game Center uses "Geschätzte Wertungszahl" |
| Skill profile / radar | `Skill profile` | Fähigkeitsprofil | paywall: "Fähigkeiten-Radar" |
| Weakness trends | `Weakness trends` | Schwächentrends | |
| Five skills | `Tactics`, `Defense`, `Positioning`, `Endgame`, `Openings` | Taktik, Verteidigung, Stellungsspiel, Endspiel, Eröffnungen | |
| Today's plan | `Today's plan` | Heutiger Plan | |
| Lessons / 8 tracks | `Lessons`; `Fundamentals`, `Openings`, `Palace Defense`, `Cannon Tactics`, `Horse Technique`, `Middlegame`, `Endgame`, `Advanced` | Lektionen; Grundlagen, Eröffnungen, Palastverteidigung, Kanonentaktik, Pferdetechnik, Mittelspiel, Endspiel, Fortgeschritten | |
| Skill assessment | `Skill Assessment` | Fähigkeitstest | |
| Drill modules | `Tactics Yard`, `Cannon Range`, `Horse Trails`, `Palace Workshop`, `Endgame Studio`, `Opening Lab`, `Mate Trail`, `Tactic Cards`, `Handicap House` | Taktikplatz, Kanonenbereich, Pferdepfade, Palastwerkstatt, Endspielstudio, Eröffnungslabor, Mattpfad, Taktikkarten, Vorgabehaus | |
| Mate problems / puzzles | `Mate problem` / `Puzzles` | Mattaufgabe / Aufgaben | |
| Coach hints | `Unlimited in-game coach hints` | Unbegrenzte Coach-Hinweise im Spiel | FLAG: the lesson and drill hint button is `Hint` → "Tipp", while the coach uses "Hinweise" |
| Named mistakes | `Screenless cannon`, `Trapped horse`, `Broken advisors`, `Iron Bolt`, `Missed mate` | Kanone ohne Schanzstein, Gefangenes Pferd, Beschädigte Beraterdeckung, Eiserner Riegel, Verpasstes Matt | FLAG: "screen" is "Schanzstein" in 131 strings and "Schirm" in 33. "Beschädigte Beraterdeckung" reads awkwardly. Ask a native reviewer |
| Piece sets | `Traditional` / `Western` / `Hybrid` | Traditionell / Westlich / Hybrid | setting: `Piece set` → "Figurensatz" |
| Characters | `Traditional` / `Simplified` | Traditionell / Vereinfacht | |
| Notation | `WXF` / `Chinese` | WXF / Chinesisch | |
| Boards | `Boxwood` / `Rosewood` / `3D Board` | Buchsbaum / Rosenholz / 3D-Brett | |
| Flip board / New game | `Flip board` / `New Game` | Brett drehen / Neue Partie | |
| Premium | `Xiangqiful Premium` / `Upgrade to Premium` | Xiangqiful Premium / Auf Premium upgraden | |
| Free | `Free plan` | Kostenloser Plan | |
| Monthly / Yearly / Lifetime | `paywall.plan.*` | Monatlich / Jährlich / Lebenslang | FLAG: Settings shows "Lifetime – nichts zu verlängern…", so English "Lifetime" stays untranslated there |
| Best value | `Best value` | Bester Wert | FLAG: a literal translation. WanderWiki uses "Bestes Angebot" |
| Start free trial | `Start free trial` | Kostenlose Testphase starten | |
| Restore purchases | `Restore purchases` | Käufe wiederherstellen | |

Note: the catalog has an unused stale string, `paywall.benefit.opponents` "All 40 opponents…" → "Alle 40 Gegner…". No Swift file references it, so don't use it.

### German App Store listing
- Name: **Xiangqiful Xiangqi lernen & KI** (English: "Xiangqiful", so it differs)
- Subtitle: **Chinesisches Schach, Taktik**
- In-app purchases: `Premium Jahresabo 9,99 €` · `Premium Monatsabo 1,99 €` · `Unterstützer 5,99 €` · `Riesige Unterstützung 9,99 €` · `Kaffee 1,99 €` · `Premium Einmalkauf 22,99 €`
- Sprachen: **Deutsch und 33 weitere**

