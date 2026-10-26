# Keyword research, German (Germany)

Part of the language sheet `_i18n/de.md`.


Collected 2026-10-26. Source marks: **G** = Google suggest (hl=de, gl=de), **B** = Bing autosuggest (mkt=de-DE),
**A** = App Store search hints (storefront 143443-4,29, Germany/German), **S** = App Store search results
(itunes.apple.com/search, country=de), used only for competitor names and the vocabulary in their German titles.
Every query below was returned by one of these sources; nothing was invented. Search Console data is not included
(not yet: Claude in Chrome was not connected on 2026-10-26; add a Germany-filtered export when available).

## Method note

- **Google suggest: worked.** 148 requests, about 0.8 s apart. Alphabet suffixes only on 4 seeds
  (trainingstagebuch app, schach app, countdown app iphone, hrv app; plus one on rechnung teilen app).
- **Bing autosuggest (api.bing.com/osjson.aspx, mkt=de-DE): worked.** Noisier than Google: it often mixes in
  English or Dutch results and loosely related queries.
- **App Store search hints (MZSearchHints, German storefront header): worked** for single-word and common seeds
  (43 terms). Several two-word seeds returned an empty hint list ("hund impfpass", "schritte bildschirmzeit",
  "hrv apple watch", "tagesplaner mac", "wikipedia zufall").
- **iTunes Search API (country=de): worked** (25 searches) for competitor names.
- **People also ask: not collected.** It needs a live Google results page, and scripted fetches of that page
  run into a consent wall and CAPTCHA, which I did not try to get around. The FAQ questions below come from
  question-style autocomplete ("wie", "welche", "beste", "was ist") instead.
- Weak spots: German Google suggest returns little or nothing for the privacy/studio themes (home, about,
  transparency) and for several long app-specific seeds. Where a seed returned nothing, that is stated and the
  pick comes from what did return.
- Good sign: some of our own German App Store listings already show up in the A hints/S results:
  "pawza: haustier-gesundheit" (A), "shogiful: shogi lernen & üben" (A), "AfterShift: Schlaf & Schicht" (S),
  "Tare: Logikrätsel & Denkspiel" (S).

---

## Home (/de/): studio of privacy-first Apple apps

- **Decision (main session, 2026-10-26): primary `apps ohne tracking`.** "apps ohne abo" is not usable: the house
  rule allows "ohne Abo" only for LiftLog, Millrace, Mockly and Tare, and 16 of the 20 apps sell a subscription.
- Research pick, not used: `apps ohne abo` (G, B). Real demand, matches the studio (most apps have lifetime or one-time
  options; mind the house rule that "no subscription" is only said for LiftLog/Millrace/Mockly/Tare). If the
  title should lean on privacy instead: `apps ohne tracking` (G) has demand but low volume signals.
- **Secondary:** `apps ohne tracking` (G); `iphone apps ohne werbung` (G, B); `datenschutzfreundliche apps` (G).
- **FAQ-style (from suggest):**
  - welche apps tracken mich (G)
  - app tracking deaktivieren iphone (G)
  - wo finde ich abos auf dem iphone (B)
  - was ist app tracking (B)
- **Notes:** "datenschutz apps iphone" returned only "iphone datenschutz apps werden nicht angezeigt" (a settings
  problem, not intent). "apps ohne datensammlung" returned nothing on G and B. Germans phrase privacy as
  "ohne Tracking", "ohne Werbung", "ohne Abo", "ohne Anmeldung" (seen on trainingstagebuch, tagesplaner and
  splitwise alternative seeds too). "ohne Anmeldung" is a useful phrase for "no account".
  English "privacy" is not used in consumer queries.

## Apps hub (/de/apps/): all apps

- **Decision (main session, 2026-10-26): primary `iphone apps ohne werbung`** (G, B); `beste iphone apps` and
  `nützliche iphone apps` as secondaries. "iphone apps ohne abo" is out for the same house rule as on the home page.
- Research pick: `beste iphone apps` (G, B). Generic, but it is the real phrase; pair it with the studio angle in
  the title (for example around "ohne Abo/ohne Tracking").
- **Secondary:** `nützliche iphone apps` (G; B has "nützliche apps iphone"); `iphone apps ohne abo` (B only; G
  returned nothing); `beste iphone apps kostenpflichtig` (G).
- **FAQ-style:**
  - beste iphone apps kostenlos (G)
  - nützliche kostenlose apps iphone (G)
  - welche apple abos gibt es (B)
- **Notes:** "mac apps ohne abo" returned nothing on G. Year/model variants are common ("beste iphone apps 2026",
  "beste apps iphone 17 pro") (G); avoid dated titles per house style.

## About (/de/about/): one-person studio, Finland

- **Primary:** no real query found. `app entwickler finnland` and `indie app entwickler` returned nothing on G.
  Closest real phrase: `indie entwickler` (G, B), also `indie entwickler deutschland`, `indie entwickler bedeutung`
  (G). Recommendation: title it on the brand ("Lagerland Apps") plus "Indie-Entwickler aus Finnland"; this page
  will rank on brand, not on generic demand.
- **Secondary:** `indie entwickler` (G, B); `indie entwickler bedeutung` (G).
- **FAQ-style:** was macht ein app entwickler (B); wie entwickelt man eine app (B). These are off-topic for an
  about page; no on-topic question suggestions exist.
- **Notes:** "app entwickler ein mann" only returned "app entwickler mannheim". "Indie" is used as-is in German.

## Support hub (/de/support/)

- **Primary:** `app abo kündigen iphone` (G, B). Strongest support-type demand and it fits the hub (cancel,
  restore, contact).
- **Secondary:** `käufe wiederherstellen iphone` (G) / `app käufe wiederherstellen iphone` (G);
  `in app kauf wiederherstellen` (G); `app store abo kündigen iphone` (G).
- **FAQ-style:**
  - wie kann ich app abo kündigen iphone (G)
  - app abo kündigen iphone probezeit (G)
  - wo finde ich abos auf dem iphone (B) / abos im iphone finden (B)
  - wie kündige ich ein abo bei apple (B)
  - apple abo kündigen ohne iphone (G, B)
- **Notes:** "app support kontakt" returned only brand queries (apple store support kontakt). Germans say
  "Abo kündigen" (never "Subscription") and "Käufe wiederherstellen" (matches Apple's German UI label).

## Transparency (/de/transparency/): tracking, SDKs, privacy manifests

- **Primary:** `app tracking transparenz` (G; B returns the English "app tracking transparency" variants).
- **Secondary:** `app tracking deaktivieren iphone` (G); `privacy manifest` (G, B; developer audience, English
  term used as-is); `tracking sdk` (G).
- **FAQ-style:**
  - welche apps tracken mich (G)
  - was ist app tracking (B) / was bedeutet app tracking (B)
  - app tracking deaktivieren iphone (G)
  - was ist eine tracking app (B)
- **Notes:** "datenschutz manifest" and "apps die nicht tracken" returned nothing on G. Developer terms stay
  English: "privacy manifest", "SDK", "App Tracking Transparency" (B shows "app tracking transparency att",
  "missing privacy manifest", "itms-91061 missing privacy manifest"). Consumers use "App-Tracking" + German verbs.

---

## AfterShift (shift-work sleep)

- **Primary:** `schichtarbeit schlaf` (G, B). "schichtarbeit schlaf app" itself returned nothing on G.
- **Secondary:** `nachtschicht schlafen` (G, B); `schichtarbeit schlafrhythmus` (G); `schichtarbeit app` (G);
  `schlafrhythmus app` (G).
- **FAQ-style:**
  - nachtschicht schlafen wie lange (G)
  - nachtschicht schlafrhythmus einstellen (G)
  - nachtschicht schlaf aufteilen (G)
  - schlafstörungen schichtarbeit was tun (G)
  - schichtarbeit schlaf tipps (G)
- **Competitors (S):** Schlafmanagement Schichtarbeit, Peaks, ShiftRest, SleepShift, Schichtbox, Rested.
  A hints for "schicht" are mostly Schichtplan/Schichtkalender (roster apps, different intent).
- **Notes:** German words: "Schichtarbeit", "Nachtschicht", "Schichtdienst", "Schlafrhythmus", "Schlafstörung".
  "Nap" is not seen; use "Nickerchen"/"Schlaf aufteilen" in copy. English terms are not common here.

## AllPaid (bill reminders, no bank login)

- **Primary:** `fixkosten app` (G, B). "rechnungen erinnerung app" and "rechnungen app iphone" returned nothing
  on G; "fixkosten" is the word Germans use for recurring bills.
- **Secondary:** `zahlungserinnerung app` (G; A hint "zahlungserinnerung"); `rechnungen verwalten app` (G);
  `fixkosten app ios` (G); `fixkosten übersicht app` (G).
- **FAQ-style:** no question suggestions came back ("wie rechnungen im blick behalten" returned nothing on G;
  B only returned invoice-law questions). Closest usable phrases: `app rechnungen verwalten privat` (G),
  `monatliche fixkosten app` (G), `fixkosten app kostenlos` (G).
- **Competitors (S/A):** Billo (Fixkosten & Rechnungen), FIX, BillSnap ("Rechnungserinnerung"), DueMinder,
  budgetSum, Subdue, Fixkosten Kalender, Finanzguru-style "abos verwalten" apps; A hints "fixkosten &
  zahlungserinnerung", "rechnungserinnerung".
- **Notes:** Caution: "rechnungen app"/"zahlungserinnerung" on Google is dominated by Apple invoices and phishing
  ("zahlungserinnerung apple store fake"). "Rechnung" in German also means invoice-writing (A: "rechnung schreiben").
  Use "Fixkosten", "Zahlungserinnerung", "Rechnungserinnerung", "Rechnungen im Griff". No English.

## AppMeta (App Store Connect for Mac)

- **Primary:** `app store connect mac app` (G).
- **Secondary:** `app store connect app` (G, B); `app store connect macos` (G); `app store connect dashboard`
  (G, B).
- **FAQ-style:** app store connect app review time (G); what is app store connect / was ist app store connect (B).
  Developers search in English here.
- **Competitors (S Mac / A):** Helm for App Store Connect, AppDab, Appdesk, AppSales, Peek, plus Apple's own
  App Store Connect and Transporter.
- **Notes:** English product term throughout; German only in surrounding words ("statistiken" returned nothing).

## AppMeta Pulse (App Store Connect dashboard on iPhone)

- **Primary:** `app store connect dashboard` (G, B).
- **Secondary:** `app store connect app` (G, B); `app store connect iphone` (G); `app store connect apps` (G).
- **FAQ-style:** app store connect app review time (G); app store connect help (B). No German question suggestions.
- **Competitors (A):** "widgets -for app store connect", Peek, AppSales, Helm, AppDab (A hints for "app store
  connect").
- **Notes:** Same English vocabulary as AppMeta; "MRR", "proceeds" were not tested on suggest. Keep both pages'
  titles distinct (Mac app vs iPhone dashboard).

## Chessful (chess learning and analysis)

- **Primary:** `schach app` (G, B), with `schach lernen app` (G, B) as the intent the page actually serves.
  Suggest titling for "Schach lernen App" and keeping "Schach App" in the title too.
- **Secondary:** `schach lernen app` (G, B); `schach app iphone` (G); `schach analyse app` (G); `schach app ohne
  werbung` (G).
- **FAQ-style:**
  - welche schach app ist die beste (G)
  - welche schach app für anfänger (G)
  - beste schach app zum lernen (G)
  - beste schach app iphone (G, B has "beste schach app ios/ipad")
  - welche kostenlose schach app ist die beste (G)
- **Competitors:** lichess, duolingo (G: "schach app lichess", "schach lernen app duolingo"); S: "Schach - Spielen
  und Lernen", "Schach Ohne Werbung", Chess.com-type "Chess", Real Chess 3D.
- **Notes:** All German ("Schach", "lernen", "Analyse", "ohne Werbung", "für Anfänger", "offline" from A).

## EarnLock (earn screen time by moving)

- **Primary:** `bildschirmzeit reduzieren app` (G). The exact seed "bildschirmzeit app belohnung schritte"
  returned nothing on G.
- **Secondary:** `app blocker iphone` (G, B); `apps sperren iphone` (G, B); `bildschirmzeit app` (G, B);
  A hints `bildschirmzeit app blocker`, `bildschirmzeit sport` (A).
- **FAQ-style:**
  - wie bildschirmzeit reduzieren (G)
  - ab welcher bildschirmzeit ist man süchtig (B)
  - apps zeitlich sperren iphone (G)
  - einzelne apps sperren iphone (G)
- **Competitors (S):** StepStore, Steppin, Fitlock ("Bildschirmzeit Holen"), StepKey ("Gehen statt Scrollen"),
  Stridle, Unrot ("Verdien Bildschirmzeit"), Opal, one sec, ScreenZen, Fit to Scroll, Detach. "schritte belohnung
  app" (G) exists but is thin.
- **Notes:** German: "Bildschirmzeit", "Apps sperren", "reduzieren", "Gehen statt Scrollen", "verdienen".
  "App Blocker" is used as an English loan.

## GymLogger X (strength tracker, Apple Watch)

- **Primary:** `trainingstagebuch app` (G, B; A hint "trainingstagebuch").
- **Secondary:** `trainingstagebuch apple watch` (G); `apple watch krafttraining app` (G); `gym tracker app` (G, B);
  `strong app alternative` (G, B).
- **FAQ-style:**
  - beste trainingstagebuch app (G)
  - beste gym app für apple watch (G)
  - beste gym app zum tracken (G)
  - apple watch krafttraining tracken (B)
  - welche trainingsapp (G)
- **Competitors:** Strong ("strong app alternative" G/B), Hevy ("Hevy - Gym & Trainingstagebuch" S), GymBook,
  Alpha Progression, Gainsfire, RepCount, Lyfta, Liftsmith, Logwell (S/A).
- **Notes:** Both "Trainingstagebuch" (German, strongest) and "Gym Tracker" (English loan) are used.
  "trainingstagebuch app ohne anmeldung" (G) fits the no-account angle.

## LiftLog (lift log, no subscription)

- **Primary:** `krafttraining app` (G, B; A hint "krafttraining tracken").
- **Secondary:** `trainingstagebuch app ohne abo` (G); `gym app ohne abo` (G); `fitness tagebuch app` (G, B);
  `trainingsplan app krafttraining kostenlos` (G).
- **FAQ-style:**
  - beste gym app (G)
  - beste fitness tagebuch app (G)
  - beste gym app iphone (G)
  - beste gym app reddit (G)
- **Competitors:** same set as GymLogger X (Hevy, Strong, GymBook, Alpha Progression, StrongLifts 5x5 from A).
- **Notes:** Differentiate from GymLogger X by "ohne Abo" (LiftLog is allowed to say this). "Workout Tracker" is
  less common than "Trainingstagebuch"/"Krafttraining".

## MediaKit (compress/convert media on device)

- **Primary:** `video komprimieren iphone` (G, B).
- **Secondary:** `video komprimieren app` (G, B); `pdf komprimieren iphone` (G, B); `video konvertieren iphone` (G);
  `video in mp3 konvertieren iphone` (G).
- **FAQ-style:**
  - wie kann ich ein video komprimieren iphone (G)
  - iphone video komprimieren zum versenden (B)
  - wie komprimiere ich ein video (B)
  - pdf komprimieren iphone ohne app (G)
  - video komprimieren iphone nachträglich (G)
- **Competitors (S):** Video Komprimierer, Video Kompressor, FileShrink, Der Video Converter, Compress Videos.
- **Notes:** German verbs dominate: "komprimieren", "konvertieren", "verkleinern". "datei konvertieren app"
  returned nothing useful. "video komprimieren apple mac" (G) supports the Mac angle.

## Millrace (tile delivery puzzle; never write "2048")

- **Primary:** `logik puzzle app` (G; B returns English "logic puzzle app"; A hint "logik puzzle").
- **Secondary:** `puzzle app offline` (G); `rätsel app ohne werbung` (G); `puzzle spiel iphone` (G).
- **FAQ-style:** no question suggestions. Closest: `kostenlose rätsel app ohne werbung` (G), `rätsel app kostenlos
  erwachsene` (B).
- **Competitors (S):** Logik-Spiele Detektiv-Rätsel, Nonogram.com, Cross Logic, Logicals, Blockudoku.
- **Notes:** "Puzzle" is used as a German word; "Rätsel" and "Logikrätsel" are the native terms; "ohne Werbung"
  and "offline" are common modifiers. Weak demand overall; the page will compete on modifiers.

## Mockly (App Store screenshots on Mac)

- **Primary:** `app store screenshots erstellen` (G).
- **Secondary:** `app store screenshots generator` (G, B); `screenshot mockup` (G, B); `app store screenshots
  template` (G, B).
- **FAQ-style:** app store screenshots sizes (G) / app store connect screenshots sizes (B); app store
  screenshots guidelines (B). English only.
- **Competitors (S, incl. Mac):** App Screenshots: Store Maker, StoreView, Picasso, Appscreeny, Storeshot,
  Shotform, "Mockup - App Screenshot Design", App Store Screenshot Dev, App-Screenshot-Ersteller; G also shows
  figma, canva.
- **Notes:** Mixed language: English nouns ("App Store Screenshots", "Mockup", "Generator") + German verb
  ("erstellen"). "mockup erstellen mac" returned nothing.

## Observa (sleep, HRV, recovery from Apple Health)

- **Primary:** `hrv app` (G, B), with `hrv apple watch` (G, B) as the dominant variant.
- **Secondary:** `hrv apple health` (G); `schlaf analyse app` (G); `hrv auswertung app` (G); `apple health
  auswertung app` (G).
- **FAQ-style:**
  - was ist hrv (G, B)
  - was ist hrv im schlaf (G, B)
  - wie hrv verbessern (G) / wie kann ich meine hrv verbessern (B)
  - hrv apple watch werte (G)
  - hrv apple watch niedrig (G)
  - hrv apple watch genauigkeit (G)
- **Competitors:** Elite HRV, Kubios HRV, Welltory, Athlytic, HRV4Training, StressWatch (S/A).
- **Notes:** "HRV" is the term (no German spelled-out form in suggest). Keep the SDNN rule in copy. German for
  the rest: "Schlafanalyse", "Erholung", "Auswertung", "Werte".

## Pawza (pet health records)

- **Primary:** `haustier app` (G, B). Note mixed intent (virtual pet games show up: "haustier app für paare").
  The page should pair it with "Gesundheit" in the title: A hint `haustier gesundheit` (A, with many competitor
  names in that exact form).
- **Secondary:** `impfpass hund app` (G); `katzen app gesundheit` (G); `hunde app` (G, B); `haustier app iphone` (G).
- **FAQ-style:** no question suggestions. "welche haustier app" and "haustier gesundheit app" returned nothing on G.
  "beste app für hunde" (G) is the only nearby question form.
- **Competitors (S/A):** felmo (mobile vet), vetevo, Pawly ("Impfpass Hund & Katze"), Dogtorcito ("Impfpass
  Hund"), Vaccy, PetLog, Fellfolio, Pezz, VetPawl, Mascotty, Pettify, Petkeep; Pawza itself appears as
  "pawza: haustier-gesundheit" (A).
- **Notes:** German words: "Haustier", "Impfpass", "Gesundheit", "Tierarzt", "Hund & Katze". "tierarzt app"
  suggest is mostly local vet names. No English.

## RightSplit (split bills from receipts)

- **Primary:** `rechnung teilen app` (G; A hint "rechnung teilen").
- **Secondary:** `kosten teilen app` (G, B; A hint "kosten teilen"); `splitwise alternative` (G, B);
  `restaurant rechnung teilen app` (G); `kassenbon scannen app` (G, B).
- **FAQ-style:**
  - splitwise alternative ohne anmeldung (G)
  - kosten mit freunden teilen app (G)
  - urlaub kosten teilen app (G) / wg kosten teilen app (G)
  - rechnung teilen rechner (G)
- **Competitors:** Splitwise (G/B/S), Splid ("Abrechnen mit Freunden"), tricount ("Ausgaben teilen"), Split by
  Finanzguru, SplitHappens, Splittr, Splitzz; PayPal and Wero appear in G/B.
- **Notes:** "Rechnung teilen" and "Kosten teilen" are both strong; "Split Bill" is not used. "Kassenbon" is the
  word for receipt (not "Quittung" in suggest). "ohne Anmeldung" again.

## Shogiful (shogi)

- **Primary:** `shogi app` (G, B; A hint "shogi").
- **Secondary:** `japanisches schach` (G, B); `shogi regeln` (G); `shogi online` (G, B); `shogi spiel` (G).
- **FAQ-style:**
  - was ist shogi (G, B)
  - was ist schwerer schach oder shogi (G)
  - was ist älter schach oder shogi (G)
  - japanisches schach regeln (G)
- **Competitors:** Shogi Wars, Shogi Quest Online, Shogi Lv.100, PiyoShogi, Dr. Shogi, Shogi Lab (S/A); Shogiful
  already appears in A as "shogiful: shogi lernen & üben".
- **Notes:** "Shogi" is used as-is; "japanisches Schach" is the German explainer. Many results are English
  ("shogi app ios", "shogi app reddit").

## Soon. (countdowns)

- **Primary:** `countdown app iphone` (G, B).
- **Secondary:** `countdown widget iphone` (G, B; A hint "countdown widget"); `tage zählen app` (G, B);
  `countdown app urlaub` (G; A hint "countdown urlaub").
- **FAQ-style:**
  - beste countdown app (G, B) / beste countdown app für iphone (G, B)
  - countdown widget iphone sperrbildschirm (G)
  - tage zählen seit datum app (G)
  - beste kostenlose countdown app iphone (G)
- **Competitors (S/A):** Countdown Star, Countdown Buddy, Countdown App, Countdown Widget & Counter, Urlaubs-
  Countdown, Countdown Kalender.
- **Notes:** "Countdown" is fully adopted in German; "Tage zählen" is the native phrase; "Sperrbildschirm",
  "Widget", "Urlaub" are common modifiers.

## Tare (balance logic puzzle)

- **Primary:** `logikrätsel app` (G; A hint "logikrätsel").
- **Secondary:** `waage rätsel` (G; mixed intent: Silent Hill puzzles and the 12-coin riddle); `rätsel gewichte
  waage` (G); `logikrätsel erwachsene app` (G).
- **FAQ-style:** no question suggestions. Closest: `logikrätsel app kostenlos` (G), `gewicht ausgleichen waage
  rätsel` (B).
- **Competitors (S):** Waagenrätsel Logikspiel2026, Pomki: Die Obstwaage, Exactly 67, Rebalance; Tare itself
  ranks as "Tare: Logikrätsel & Denkspiel".
- **Notes:** "logik puzzle app waage" returned nothing. A hint "waage" is all kitchen/body scales, so "Waage" alone
  is the wrong lead word; use "Logikrätsel" and "Waagenrätsel"/"Balkenwaage" as support.

## Taskful Day (day planner, iPhone + Mac)

- **Primary:** `tagesplaner app` (G, B; A hint "tagesplaner").
- **Secondary:** `to do app iphone` (G, B); `tagesplanung app` (G, B); `beste to do app mac` (G); `aufgaben planer
  app` (G; B "aufgabenplaner app").
- **FAQ-style:**
  - beste to do app iphone (G)
  - beste app tagesplanung (G)
  - beste to do app mac (G)
  - tagesplaner app ohne anmeldung (B)
  - tagesplaner app mit erinnerung (B)
- **Competitors:** Microsoft To Do (G/B), Structured, Tiimo, Todoist, TickTick, Planwoo, Me+ (S/A).
- **Notes:** "To-do" is fully adopted; "Tagesplaner"/"Tagesplanung" are the native terms. "tagesplaner app adhs"
  (G) is a notable niche. "todo liste app mac" returned nothing on G.

## WanderWiki (swipe Wikipedia)

- **Primary:** `wikipedia zufälliger artikel` (G, B). "wikipedia app zufällige artikel" returned nothing, but
  `wikipedia app zufälliger artikel` (G) exists.
- **Secondary:** `wikipedia app` (G, B); `wikipedia app offline` (G); `wissen app` (G, B); `wikipedia
  zufallsartikel` (B).
- **FAQ-style:** no question suggestions. Nearby: `wikipedia zufälliger artikel spiel` (G), `wissen apps iphone` (G),
  `app wissen scrollen` (G).
- **Competitors (S):** Wikipedia (official), Wikipanion, Kiwix, DailyArt, Yuno.
- **Notes:** German uses "zufälliger Artikel" (singular) and "Zufallsartikel". "app wissen scrollen" (G) fits the
  swipe angle.

## Xiangqiful (xiangqi)

- **Primary:** `chinesisches schach` (G, B), with `xiangqi app` (G, B) in the title too. "chinesisches schach" has
  the broader German demand; "xiangqi app" is the exact app intent.
- **Secondary:** `xiangqi app` (G, B); `chinesisches schach app` (G); `chinesisches schach regeln` (G, B);
  `chinesisches schach lernen` (A).
- **FAQ-style:**
  - was ist xiangqi (G)
  - chinesisches schach regeln (G, B)
  - chinesisches schach anleitung (G)
  - xiangqi aussprache (G)
- **Competitors (S/A):** Xiangqi Chinese Chess Online, PvXiangqi ("Chinesisches Schach"), Xiangqi Classic,
  Xiangqi.com, Co Tuong Viet Nam, Chinese Chess - Best XiangQi.
- **Notes:** Both terms are used; German app listings pair them as "Xiangqi - Chinesisches Schach" (A).
  A hints "chinesisches schach offline" and "lernen" match the app.
