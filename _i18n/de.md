# Language sheet: German (de), Germany

Never published (`_i18n` is excluded from the build). Rulebook: TRANSLATION.md. Read this sheet before writing or
reviewing any German page. Every decision a translator would otherwise make differently per page lives here.

## Status

| Item | Status |
|---|---|
| Setup (config default, locales.yml block, `_data/i18n/de.yml`, sitemap and feed stubs) | done 2026-10-26 |
| Keyword research (Tier 1) | done 2026-10-26 without Search Console country data (see Keywords) |
| Tier 1 pages | done 2026-10-27: home, apps hub, 20 app pages, 20 support pages, 20 privacy policies, about, support hub, transparency, /de/llms.txt, /de/llms-full.txt, OG cards |
| Live | yes, `live: true` since 2026-10-27 (Tier 1). Tiers 2 to 4 not started |
| Native review | none yet (NATIVE REVIEWER: none). Every page is logged as "no native review yet" |
| Build time | 14 s with the setup in place (9.9 s before Phase 0) |

## Market and register

- Market: Germany. Folder `/de/`, `<html lang="de">`, hreflang `de` (also serves Austria and Switzerland, who see
  EUR prices; the App Store link opens their own storefront), og:locale `de_DE`, territory DEU, currency EUR.
- Engines (TRANSLATION.md 7.4): Google first, then Bing (also feeds DuckDuckGo, Ecosia, Copilot). Tools: Search
  Console, Bing Webmaster Tools. IndexNow covers Bing and Seznam.
- **Formality: du**, lowercase, on every page, interface string, FAQ and privacy policy. Reasons:
  1. TRANSLATION.md 13 default for consumer apps in Germany.
  2. Our own German App Store listings already address the reader with du ("Deine Apple Watch hat die ganze
     Nacht mitgeschrieben. Observa liest es dir vor", Observa, checked 2026-10-26), and Apple's German App Store
     and iOS copy use du. A website in Sie would contradict the store page one tap away.
  3. Most of the apps' German interfaces use du. Exceptions found in the string catalogs (2026-10-26): Observa
     (about 880 Sie strings against 250 du) and AppMeta (about 174 Sie against 45 du) mostly use Sie, and Soon.,
     Taskful Day and others have a few stray Sie strings. That is an app-side inconsistency to fix in the apps
     (flagged in de-glossary.md); the site stays du everywhere, including the Observa and AppMeta pages.
  Never mix: no "Sie" anywhere, no "Ihr/Ihre" as address. Privacy policies also use du (consistent with
  Apple's German privacy copy); legal meaning stays exact.

## Typography and punctuation

- Quotes „…“ (outer), ‚…‘ (inner). Never "…" or “…” in German prose.
- Nouns capitalized; headings in sentence case (no English title case).
- Compounds closed or hyphenated, never split: Schlaftracker or Schlaf-Tracker, never "Schlaf Tracker". With a
  product name, hyphenate: Apple-Watch-App, App-Store-Seite, Lagerland-App, iCloud-Synchronisierung.
- No em or en dashes. A range is written "bis" or with a hyphen-minus only inside numbers with units ("3-5 kg"
  only if the source has a range; prefer "3 bis 5 kg").
- No Oxford comma: "A, B und C".
- Ellipsis with a space before it when it stands for a missing word: "wenn …".
- Numbers: decimal comma (4,8), thousands with a dot from five digits on (12.500); four-digit numbers without
  separator (6005), as the App Store shows them. Units metric, with a space: 8 h, 70 kg, 5 km, 20 °C.
- Times: 24-hour, "22:30 Uhr". Dates in prose: "26. Oktober 2026" (templates do this via date.html).
- Hyphenation: CSS `hyphens: auto` is on for German body text.

## Formats (checked 2026-10-26 in the German App Store storefront, apps.apple.com/de)

| What | Format seen | Where | In the site |
|---|---|---|---|
| Price | `9,99 €` (no-break space U+00A0 before €) | Things 3, apps.apple.com/de/app/id904237743 | locales.yml `EUR: position after, space U+00A0, decimal ",", group "."` |
| Free app | `Kostenlos · In-App-Käufe` | Observa, id6757438990 | `strings.free: "Kostenlos"` |
| Rating | `4,6`, `4,7` | WhatsApp, Things 3 | `strings.decimal: ","` (hero, cards, testimonials) |
| Rating count | `6005 BEWERTUNGEN`, `3,6 MIO. BEWERTUNGEN` | Things 3, WhatsApp | counts from the catalog, printed as integers |
| Dates on the store | `26.12.2022` (reviews) | WhatsApp | site prose uses the long form `26. Oktober 2026` (TRANSLATION.md 4.7) |
| Size | `90,7 MB` | Observa | not used on the site |

The German web storefront no longer lists in-app purchase prices; our own prices come from the catalog (territory
DEU) and print in the format above. Price line pattern: `Kostenlos, Premium ab 3,99 €/Monat, 24,99 €/Jahr oder
39,99 € einmalig` (strings.from "ab", per_month "/Monat", per_year "/Jahr", lifetime "einmalig", or "oder").
Trial label: `7 Tage gratis testen`. Zero price on plan cards: `{P_ZERO}` → `0 €`.

Note: the German App Store shows the developer's personal name as "Anbieter" and "Entwicklungsteam". That name
never goes on the site; attribute to "Lagerland Apps".

## Glossary

Two companion files hold the full lists: `_i18n/de-glossary.md` (per app: German coverage, feature names verbatim
from the string catalogs, German App Store name and subtitle) and `_i18n/de-apple-terms.md` (Apple's own German
names, each with its Apple source URL). Rule: a feature name is written exactly as the app's German interface
shows it; an Apple product or feature name exactly as Apple writes it in German.

All 20 apps have a German interface (string catalogs 99 to 100 % translated, checked 2026-10-26), so every app
page may say the app is available in German. Gaps to keep off the pages: AfterShift's calendar permission prompt,
Pawza's camera and photo permission prompts and AllPaid's Siri phrases are English only.

The terms that matter most across the site:

| English | German on the site | Source |
|---|---|---|
| (address) you | du, lowercase, never Sie | this sheet |
| Download on the App Store (badge) | Laden im / App Store | Apple's de-de badge files |
| Free (price) | Kostenlos | German App Store price line |
| In-App Purchases | In-App-Käufe | App Store, Apple support |
| subscription / manage subscriptions | Abo / Einstellungen → dein Name → Abonnements | support.apple.com/de-de/118428 |
| lifetime (purchase) | Einmalkauf (in prose); „einmalig“ in the price line | store listings use Einmalkauf |
| Family Sharing | Familienfreigabe | App Store, Apple support |
| Data Not Collected | Keine Daten erfasst (section: App-Datenschutz) | German App Store product page |
| Health app / Apple Health | die App „Health“ / Apple Health (unchanged) | support.apple.com/de-de |
| Heart Rate Variability (HRV) | Herzfrequenzvariabilität (HRV); Apple abbreviates HFV, Observa's UI says HRV and searches say „hrv“, so the site writes HRV. Always SDNN for Apple Health | Apple, Observa catalog, keywords |
| Screen Time | Bildschirmzeit | Apple support |
| Notifications | Mitteilungen | Apple support |
| Home Screen / Lock Screen / widgets | Home-Bildschirm / Sperrbildschirm / Widgets | Apple support |
| Live Activities / Smart Stack | Live-Aktivitäten / Smart-Stapel | Apple support |
| iCloud sync | iCloud-Synchronisierung; „mit iCloud synchronisieren“ | Apple support, app catalogs |

Per-app tier names follow each app's German UI (de-glossary.md): Premium for Observa, Soon., Shogiful,
Xiangqiful, WanderWiki (the app never says "Plus"); Pro+ for RightSplit; Pro for Pawza and Taskful Day. Where the
English site's tier name differs from the app (Observa "Pro" vs app "Premium", WanderWiki "Plus" vs "Premium",
Chessful "Pro" vs "Premium"), the German page follows the app and the mismatch is listed under "Open questions".

## Keyword research

Full notes, sources and FAQ-style questions per page: `_i18n/de-keywords.md` (Google suggest de/DE, Bing
autosuggest de-DE, App Store search hints and results for the German storefront, 2026-10-26). Search Console
data filtered to Germany is still missing: Claude in Chrome was not connected, and the newest local export
(July 2026, all countries) has no per-country queries. In it Germany is the 4th country by clicks (25 clicks,
3,882 impressions over three months). Revisit the primaries when a Germany-filtered export is available.

`seo.title`, the H1 and `quick_answer` of each page are written for its primary query.

| Page | Primary query | Secondary queries |
|---|---|---|
| Home (/de/): studio of privacy-first Apple apps | `apps ohne tracking` | `iphone apps ohne werbung`, `datenschutzfreundliche apps`, `apps ohne anmeldung` (phrase, see notes) |
| Apps hub (/de/apps/): all apps | `iphone apps ohne werbung` | `beste iphone apps`, `nützliche iphone apps` |
| About (/de/about/): one-person studio, Finland | none with demand: brand-led („Lagerland Apps“ + „Indie-Entwickler aus Finnland“) | `indie entwickler` |
| Support hub (/de/support/) | `app abo kündigen iphone` | `käufe wiederherstellen iphone`, `app käufe wiederherstellen iphone` |
| Transparency (/de/transparency/): tracking, SDKs, privacy manifests | `app tracking transparenz` | `app tracking deaktivieren iphone`, `privacy manifest` |
| AfterShift (shift-work sleep) | `schichtarbeit schlaf` | `nachtschicht schlafen`, `schichtarbeit schlafrhythmus`, `schichtarbeit app` |
| AllPaid (bill reminders, no bank login) | `fixkosten app` | `zahlungserinnerung app`, `rechnungen verwalten app` |
| AppMeta (App Store Connect for Mac) | `app store connect mac app` | `app store connect app`, `app store connect macos`, `app store connect dashboard` |
| AppMeta Pulse (App Store Connect dashboard on iPhone) | `app store connect dashboard` | `app store connect app`, `app store connect iphone`, `app store connect apps` |
| Chessful (chess learning and analysis) | `schach app` | `schach lernen app`, `schach app iphone`, `schach analyse app` |
| EarnLock (earn screen time by moving) | `bildschirmzeit reduzieren app` | `app blocker iphone`, `apps sperren iphone`, `bildschirmzeit app` |
| GymLogger X (strength tracker, Apple Watch) | `trainingstagebuch app` | `trainingstagebuch apple watch`, `apple watch krafttraining app`, `gym tracker app` |
| LiftLog (lift log, no subscription) | `krafttraining app` | `trainingstagebuch app ohne abo`, `gym app ohne abo`, `fitness tagebuch app` |
| MediaKit (compress/convert media on device) | `video komprimieren iphone` | `video komprimieren app`, `pdf komprimieren iphone`, `video konvertieren iphone` |
| Millrace (tile delivery puzzle; never write "2048") | `logik puzzle app` | `puzzle app offline`, `rätsel app ohne werbung`, `puzzle spiel iphone` |
| Mockly (App Store screenshots on Mac) | `app store screenshots erstellen` | `app store screenshots generator`, `screenshot mockup` |
| Observa (sleep, HRV, recovery from Apple Health) | `hrv app` | `hrv apple health`, `schlaf analyse app`, `hrv auswertung app` |
| Pawza (pet health records) | `haustier app` | `impfpass hund app`, `katzen app gesundheit`, `hunde app` |
| RightSplit (split bills from receipts) | `rechnung teilen app` | `kosten teilen app`, `splitwise alternative` |
| Shogiful (shogi) | `shogi app` | `japanisches schach`, `shogi regeln`, `shogi online` |
| Soon. (countdowns) | `countdown app iphone` | `countdown widget iphone`, `tage zählen app` |
| Tare (balance logic puzzle) | `logikrätsel app` | `waage rätsel` |
| Taskful Day (day planner, iPhone + Mac) | `tagesplaner app` | `to do app iphone`, `tagesplanung app`, `beste to do app mac` |
| WanderWiki (swipe Wikipedia) | `wikipedia zufälliger artikel` | `wikipedia app`, `wikipedia app offline`, `wissen app` |
| Xiangqiful (xiangqi) | `chinesisches schach` | `xiangqi app`, `chinesisches schach app`, `chinesisches schach regeln` |

Wording rules from the research: privacy is said as „ohne Tracking“, „ohne Werbung“, „ohne Anmeldung“ (the
English "privacy" is not searched); „Trainingstagebuch“ beats "Workout Tracker"; for AllPaid lead with
„Fixkosten“ and „Zahlungserinnerung“ (plain „Rechnung“ pulls in Apple invoice phishing); for Tare lead with
„Logikrätsel“ (plain „Waage“ means kitchen scales); receipts are „Kassenbon“; HRV, Shogi, Countdown, To-do,
App Store Connect, Privacy Manifest and Mockup stay English in German searches.

## Local competitors (for Tier 3)

Seen in German App Store results and suggestions (details per app in de-keywords.md): to be checked for German
storefront availability and prices before any comparison page is written (TRANSLATION.md 6.4).

## Open questions (English site vs app, found while building the glossary)

Not translated as-is; each needs the owner's call or an English fix first. Details in de-glossary.md.

- Soon.: site's free themes (Classic, Soft, Midnight) vs code (sunrise, ocean, forest; Midnight is Premium);
  "Pregnancy" type is "Baby" in the app and there is no Graduation or Move type; no "Reflection" string (it is
  "Notes"); the app has iCloud sync strings while the site says on-device only; language count 39 vs store
  "Deutsch und 35 weitere".
- Tare: German store IAP name says „Kapitel II–IV“, site says the purchase unlocks Chapters II to X.
- Taskful Day: no "Focus Orbit" string (app: Fokusmodus); paywall lists Day Clock, Day Map, Energy River and
  Focus Mode as Pro while the site's free tier includes them; a watch target exists while the site says no Watch app.
- WanderWiki: paid tier is "Premium" in the app, "Plus" on the site; weekly subscription not on the site; a string
  says the personalized feed is English-only.
- Observa: tier "Premium" (app, store) vs "Pro" (site, watch, widgets); the German store subtitle mentions cycle
  tracking („Zyklus“), which the site page doesn't cover.
- Mockly: display name in InfoPlist is still "ScreenFlow Studio"; translation packs exist in code but not on the
  site; German subtitle says 50 languages vs 39 locales on the site.
- Shogiful: site says 10 AI opponents across 4 tiers, code has 8 opponent tiers.
- Chessful: app strings include a 3-day trial, the site says 7-day; tier "Premium" in app vs "Chessful Pro" IAPs.
- EarnLock: site says "Tap Reflect on the Home screen"; the app's tab is "Today" („Heute“).
- AppMeta Pulse: German store prices came back as 0,99 € / 1,99 € / 2,99 €; prices on the site come from the
  catalog anyway, but worth confirming in App Store Connect.

## Tells to cut in German (TRANSLATION.md 8.2, plus what reviews find)

Found in reviews (batch 1, 2026-10-27): commas before „oder“/„und“ produced by templates (check rendered output,
not just the YAML); „Gratis“ creeping in for "Free" outside trial wording (the site says „Kostenlos“; „gratis
testen“ only for trials); „sie“ for „eine Person“ reads as "she", so rephrase when the subject is the developer;
calques „datierte Updates“, „Deine Wahl“, „Hilfe bekommen“, „Siehe …“; „aus {count} Bewertungen“ (write „bei“);
{n} patterns need singular forms („1 Tag“); short keyword stems („mac“, „sicher“) match ordinary words;
„indie X for indie X“ calques repeat words; „Leben“ for game lives (write „Lebenssystem“); „Dark Patterns“ left in
English (write „manipulative Tricks“); „Macher“ for "maker"; „kalkuliert“ for "priced" (it means costing: write
„legt die Preise fest“); stacked noun chains copied from English comparisons („X für Y einer Z vorziehen“); „Kein X
tut irgendetwas“ for "No X does anything"; „ohne Leben“ / „Lebenssystem“ for game lives (write „begrenzte
Leben“); „dort“ as filler; a generic „Pro“ tier where the app's German UI says Premium or Pro+.

Found in reviews (batch 5, 2026-10-27): „Hilfe mit“ for "help with" (write „Hilfe bei“); „X als Standard“ for
"X by default" (write „standardmäßig X“); „Bezahlt wird …“ for "funded by" (write „finanziert“); „sich vor X
rechtfertigen“ for "answer to X" (write „X Rechenschaft schuldig sein“); „App-Release“ (write „App-Version“ or
„Update“); „je“ for "ever" in conditionals (write „jemals“); „Reichweitenmessung“ for Apple's ad "measurement"
(write „Messung von Werbung“); „für Tracking verwendet“ (Apple writes „zum Tracking … verwendet“) and „tracken“
where Apple's label says „verfolgen“ („über Apps und Websites anderer Unternehmen hinweg verfolgen“); capital
„Sie“ after a colon meaning "they" (rephrase so it can't read as formal address); „mit“ + a quoted label in the
nominative („Apps mit <em>noch kein Manifest</em>“: write „mit dem Vermerk …“); lists that put free tiers among
ways to pay („bezahlen … mit kostenlosen Grundversionen“: give the free tier its own sentence).

Found in the AI-file review (2026-10-27): „Antwortmaschinen“ for "answer engines" (write „KI-Suchmaschinen“ or
„KI-Assistenten“); „gebaut für“ / „für X gebaut“ for "built for" (write „gedacht für“, „gemacht für“ or rephrase);
„gegen eine Basislinie rechnen/messen“ for "against a baseline" (write „an der Basislinie messen“); „gilt als“ for
"is/counts as" in a factual statement (it means "is considered"); „und das alles ohne …“ as a tacked-on closer;
„wagnisfinanziert“ for "VC-backed" (write „mit Risikokapital“); „kostenpflichtige Apps … oder kostenlos“ in one list
(calque of "paid apps sold as … or freemium"); „englisch sein“ for pages (write „auf Englisch“); feature lists that
end in „kostenlos“ while one item is paid (name the tier, Premium or Pro, next to the paid item).

Stock phrasing: „In der heutigen schnelllebigen Welt“, „Tauchen wir ein“, „Es ist wichtig zu beachten, dass“,
„spielt eine entscheidende Rolle“, „nahtlos“, „maßgeschneidert“, „ganzheitlich“, „Zusammenfassend lässt sich
sagen“, „nicht nur …, sondern auch …“. Translationese: split compounds, „Sinn machen“, English title case, du/Sie
mixed. Added for this site: „Erlebnis“ for "experience", „Lösung“ for an app, „smart“, „Game-Changer“,
„All-in-One“, „einfach“ in every sentence, stacked adjectives before nouns.

## House rules carried over

- No dashes; no roadmaps or dated promises; prices, counts, platforms and dates only through tokens and includes.
- "ohne Abo" only for LiftLog, Millrace, Mockly and Tare. For the others: „kein Abo nötig“ or „auch als
  Einmalkauf“, where true.
- „ruhig“ (calm) and „datenschutzfreundlich“ (privacy-first) once per page, where they state positioning.
- Millrace never mentions "2048". Observa's HRV is SDNN (Apple Health), never RMSSD.
- Never the owner's personal name. App names, competitor names and "Lagerland Apps" stay as written in English.

## Review log

| Page | Writer | Humanizer + fact diff + glossary | Back-translation | Native review |
|---|---|---|---|---|
| `_data/i18n/de.yml` | main session | 2026-10-26 (self); reviewer agent 2026-10-27, 8 must-fix + 29 should-fix applied | n/a | no native review yet |
| `/de/` home | writer agent | reviewer agent 2026-10-27, 2 must-fix + 15 should-fix applied (Pro tier label kept on stamps, see decisions) | 2026-10-27, 101 claims, matches English | no native review yet |
| `/de/apps/` hub | writer agent | reviewer agent 2026-10-27, 0 must-fix + 8 should-fix (6 applied; "jede App" and the #health anchor are fine once all app pages exist) | n/a | no native review yet |

## Decisions from reviews

- App Store category words follow Apple's German App Store: „Wirtschaft“ (Business), „Entwickler-Tools“ (Developer
  Tools). Reviewer's knowledge, not yet checked on a live storefront page.
- The App Store badge is drawn as SVG text with Apple's German wording („Laden im“ / „App Store“); Apple asks for
  its own badge artwork. Owner call whether to switch to Apple's de-de badge files.

- Stamp and card price labels keep the generic „Kostenlos · Pro“ (English "Free · Pro"): it stands for "has a
  paid upgrade" across all apps, as in English, and is short enough for the stamp. In running text name the tier
  each app's German UI uses (Premium, Pro+, Pro), or say „optionale Abos“.
- Taskful Day's devices on the home page are typed as „iPhone, iPad und Mac“, as on the English page, while the
  catalog also lists watchOS. Known exception until the Watch open question is settled; then take the list from
  the catalog.
- Until all 20 app pages exist, the German home and hub show only apps with a German page while counts from the
  catalog say 20. Go-live requires all 20, so this never ships.

- `privacy.data_collection` when the English value is "none": lowercase „keine“ (it prints mid-sentence in the quick
  reference: „Erfasste Daten: keine.“).
- Every app page's price note uses one sentence: „Die Preise gelten für den deutschen App Store. In anderen Ländern
  zeigt der App Store beim Kauf die Preise in deiner Landeswährung.“
- Four-digit numbers without a separator (1500 Übungen); from five digits a dot (12.500).
- who_for / who_not_for items are full sentences starting with „Du“ (headings „{name} passt zu dir:“).
- Competitor prices: US prices never appear; either a German-storefront price checked on the day (date in the
  page's footnote) or a plain description („Abo“, „Einmalkauf“).

- Plan card names follow the app's paywall wording (e.g. „Premium · Monatlich“ / „Jährlich“ / „Lebenslang“ or the
  app's own word for lifetime), not the App Store purchase names („Monatsabo“, „Jahresabo“).
- Where the English page contradicts itself or the app code on a checkable fact (a free-tier limit, the language of
  explanations), the German page states the one value that is consistent and backed by the code, and the case is
  listed in ~/Downloads/githubcode/english-issues-from-de-review-2026-10-27.md for the English fix. Open questions
  that need the owner's decision stay as on the English page.

- The site's "Best value" badge (highlight_label) is „Bestes Preis-Leistungs-Verhältnis“ on every page, and
  "Best long-term value" is „Auf lange Sicht das beste Angebot“; a "cheapest" claim („am günstigsten“) is not used
  for lifetime plans.
- Trial lengths are never typed: `{TRIAL}` (prints „7 Tage gratis testen“, use it alone or in brackets) or
  „kostenlose Testphase“ without a length. Plan cards print the trial label themselves.

## Apps still on English screenshots

All 20 (SCREENSHOTS: none yet). Alt texts and captions are German regardless.
