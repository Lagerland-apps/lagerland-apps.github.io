# Dutch keyword research (nl, Netherlands), Tier 1

Part of the language sheet `_i18n/nl.md` (its keyword table holds the final primaries and overrides this file where they differ). Researched 2026-11-19 by two agents.

## Dutch keyword research, part A

Research pass of 2026-11-19 for the Netherlands (nl-NL), part A: Home, Apps hub, About, Support hub, Transparency, and the
app pages aftershift, allpaid, appmeta, appmeta-pulse, chessful, earnlock, gymlogger-x, liftlog, mediakit. Part B (the
other apps) is a separate file. Format follows `_i18n/pt-keywords.md`.

Source marks: **G** = Google suggest (`client=firefox&hl=nl&gl=nl`), **B** = Bing autosuggest (`qsonhs.aspx`,
`mkt=nl-NL`), **A** = App Store search hints (`MZSearchHints`, storefront header `143452-10,29`, Netherlands),
**S** = iTunes Search API (`country=nl&entity=software&lang=nl_nl`), used for competitor names and the vocabulary of
Dutch app titles. Every keyword below was returned by one of these sources; nothing was invented. "Echo" means the source
returned only the seed itself back (the phrase exists, no tail demand). Search Console data for the Netherlands was not
read, and "People also ask" was not collected (it needs a live results page); the FAQ-style questions come from question
forms in G and B suggest, and where no question form was returned the question is marked "inferred from seed".

## Method note

- **Requests: about 740**, 0.9 s apart, generic Safari User-Agent. 189 seeds (studio and privacy 34, support 12, the nine
  app themes about 120, question forms 20), each sent to G, B and A, and to S when the seed was four words or fewer.
  Raw JSON is in the session scratchpad, not the repo. No alphabet suffix sweep was run: the first pass already showed
  most themes return 0 to 10 suggestions, so the seeds were widened by synonym instead (for example "krachttraining
  bijhouden", "trainingslogboek app", "sportschool app").
- **Google suggest: worked.** Localisation is good (Dutch forms; the Dutch App Store term "Schermtijd" comes back). Noise
  to ignore: Belgian place names ("schaaklessen gent", "app studio brussel"), Dutch town names ("sportschool appingedam",
  "sportschool appelscha", "nachtdienst appelpop"), year and model suffixes ("iphone 17 pro max", "2026"), English and
  German tails ("workout app apple watch not working", "apple watch training app wird nicht angezeigt").
- **Bing: worked but noisy.** Leaks German, Spanish and English ("beste apps für apple watch", "apps para limpiar iphone").
  Often echoes the seed or returns unrelated "hoe ... een app" questions for long seeds.
- **App Store hints: worked** after dropping the `Accept-Language` header (with it the endpoint returned an empty list).
  Hints are mostly app titles, so they confirm competitor vocabulary rather than demand.
- **iTunes Search API: worked.** Our own Dutch listings already show: "AfterShift: Slaap & Ploegen", "Chessful: Train &
  Analyseer", "GymLogger X: Training Tracker", "AllPaid – Rekeningen bijhouden", "Metrics"-style competitors for App Store
  Connect. Use these as the live Dutch title vocabulary.
- **Dutch Apple term:** Screen Time is **Schermtijd** (G, B, A, S all return it; "Tijd voor scherm" or "Schermgebruik" were
  not returned).
- **Vocabulary decisions for the Netherlands** (evidence in the sections):
  - Ads: **reclame** leads ("apps zonder reclame", G 10 suggestions; S titles "Zonder Reclame"), **advertenties** is
    weaker ("apps zonder advertenties", G echo; S "AdBlocker - Geen Advertenties").
  - Subscription: **abonnement**, verb **opzeggen** ("abonnement opzeggen iphone", G 10). "Annuleren" was not returned.
  - Refund: **terugbetaling** (G "terugbetaling app store", "apple terugbetaling aanvragen") and the colloquial **geld
    terug** (G, B). "Restitutie" was not returned.
  - Restore purchases: **aankopen herstellen** (G). Apple's own button label is not verified here.
  - Shift work: **ploegendienst** (G, A, S) and **nachtdienst** (G). "Shiftwerk" returned nothing (the seed "slaap
    shiftwerk" gave only S titles). Dutch titles say "Ploegen" and "Ploegendienst" ("AfterShift: Slaap & Ploegen").
  - Bills: **rekeningen** (G "rekeningen bijhouden app", S titles), **vaste lasten** (G, B: fixed monthly costs, a
    budgeting word), **betalingsherinnering** (S only). Not "facturen".
  - Strength: **krachttraining** (G, B, S). Gym: **sportschool** (G, B, A, S), but "gym" is common in titles and in G
    seeds ("gym app apple watch"). Log: **logboek** (S titles: "Trainingslogboek", "Sportschool Logboek"; G echo),
    **bijhouden** (G "krachttraining bijhouden app").
  - Compress: both **comprimeren** and **verkleinen** are typed: "pdf comprimeren" (G 8, B 8) and "pdf verkleinen" (G 8,
    B 8) are equally strong; for video, "video verkleinen iphone" (G 3) and "video comprimeren iphone" (G 2) are close.
    HEIC: "heic naar jpg" (G 8, B 8, A 8), verbs "omzetten" and "converteren" both appear.
  - Chess: **schaak app**, **schaken** (verb, in "schaken leren app", "schaken voor beginners"), **schaakpartij**,
    **schaakanalyse**.
  - Belgian or Flemish: nothing Flemish-only was returned beyond place names. "Schaakles" (singular) appears once (G
    "schaakles app") next to "schaaklessen"; not used as a keyword.
- **Weak or empty in Dutch suggest** (so the pages cannot lean on them): "apps zonder tracking", "privacyvriendelijke apps",
  "reclamevrije apps", "advertentievrije apps" (all empty on G and B), "apps zonder abonnement" (G only dating apps),
  "app ontwikkelaar finland", "kleine app ontwikkelaar", "onafhankelijke app ontwikkelaar" (all empty), "app
  tracking transparantie", "privacylabel app store", "app privacyrapport", "apps volgen toestaan" (empty), "schaak analyse
  app" and "schaak coach app" (empty), "scrollen stoppen app" (empty), "sportschool logboek app" (empty), "app store
  zoekwoorden", "app store verkoopcijfers", "app store inkomsten" on G and B (only S titles), the earn-by-walking idea
  ("wandelen om apps te ontgrendelen", "apps ontgrendelen met stappen": B noise; only A and S show it as competitor app
  titles).
- **Collisions to avoid** are listed per page and in the table at the end.

---

## Home (/nl/): studio of calm, privacy-first Apple apps

- **Primary:** `apps zonder reclame` (G: 10 suggestions, all category tails: "muziek apps zonder reclame", "spelletjes
  apps zonder reclame", "gratis apps zonder reclame", "puzzel apps zonder reclame"; S confirms the phrase in app titles:
  "Mahjong Zonder Reclame", "Sudoku zonder reclame"). No B echo; B returns "youtube app zonder reclame", "radio app
  zonder reclame", "kijk app zonder reclame". Moderate: the phrase exists and is how Dutch people ask for ad-free apps,
  but the head is played by games and media apps, not studios.
- **Secondary:** `apps zonder reclame iphone` (S titles and B tails; G returned nothing for the exact seed);
  `spelletjes apps zonder reclame` and `puzzel apps zonder reclame` (G; only relevant to the puzzle apps, so use in
  body, not title); `indie apps iphone` is deliberately given to About, not here.
- **FAQ-style (inferred from seed, no on-topic question form returned):** "Zijn er iPhone-apps zonder reclame?";
  "Welke apps verkopen geen gegevens?"; "Wat is het verschil tussen een gratis app met reclame en een app met eenmalige
  aankoop?" (the last from B: "iphone zonder abonnement aanbieding", "apple iphone kopen zonder abonnement" show people
  do search the "zonder abonnement" shape, but for phones, not apps).
- **Notes:** brand and trust page. "Zonder tracking", "privacyvriendelijk", "reclamevrij" and "advertentievrij" returned
  nothing, so those words belong in body copy, not the title. "Zonder abonnement" is allowed on the site only for LiftLog,
  Millrace, Mockly and Tare. G shows "apps zonder abonnement" only as dating apps.

## Apps hub (/nl/apps/): all apps, iPhone, iPad, Mac, Apple Watch

- **Primary:** `beste apps iphone` (G: 10 suggestions; B: "beste apps iphone", "beste muziek apps iphone"). Strong
  head term. G adds model and year tails ("iphone 17 pro max", "2025", "2026"): avoid dated titles.
- **Secondary:** `beste apps ipad` (G 8; B "beste ipad apps", "beste apps voor ipad"); `beste apps apple watch` (G 4; B
  "app voor apple watch"); `apps voor mac` (G "apps voor macbook", "apps macos"; B "apps voor macbook"; also G
  "beste apps macos", "beste mac apps 2026", "beste gratis mac apps").
- **FAQ-style (from suggest):**
  - Wat zijn de beste apps voor iPhone? (G "beste apps iphone")
  - Wat zijn de beste gratis apps voor iPhone? (G "beste gratis apps iphone", "gratis apps iphone")
  - Wat zijn de beste apps voor Apple Watch? (G, B)
  - Welke apps heb je nodig op je Mac? (B "welke apps moet je hebben" was returned for a related seed; inferred)
  - Welke Apple Watch is de beste? (B, off topic, not used)
- **Notes:** "gratis apps iphone" is strong (G 8) but misleading for this studio, where several apps are paid or have
  in-app purchases; keep it out of title and description. B for "beste apps mac" returned a German tail ("zum musik
  machen"). S for generic head terms returns big brands, so the hub cannot hope to rank for them; it should win on
  "ploegendienst", "schermtijd", "krachttraining" long tails through its app cards.

## About (/nl/lagerland-apps/): one-person indie studio in Finland

- **Primary:** `indie apps iphone` (G echo, plus "best indie iphone apps"; the Dutch form is English-borrowed "indie").
  Weak. Honest brand page: the page should be led by the studio name, not by this phrase.
- **Secondary:** `apps van een kleine ontwikkelaar` (B returned only unrelated "hoe ontwikkel je een app" questions;
  the phrase itself is not confirmed: use as body wording only); `indie ontwikkelaar apps` (S titles only, developer
  tools).
- **FAQ-style (inferred from seed, none returned):** "Wie maakt de apps van Lagerland Apps?"; "Waar zit Lagerland Apps?";
  "Waarom verzamelen jullie geen gegevens?". Nearby B questions: "hoe ontwikkel je een app", "wat kost het ontwikkelen
  van een app" (developer audience, not our reader).
- **Notes:** "app ontwikkelaar finland", "kleine app ontwikkelaar" and "onafhankelijke app ontwikkelaar" returned nothing
  on G or B. "App studio" (G, B, A) returns Brussel and Roncq local firms and a no-code tool: do not target it. This page
  does not compete with Home for `apps zonder reclame`.

## Support hub (/nl/support/): cancel subscription, refund, restore purchases, contact

- **Primary:** `abonnement opzeggen iphone` (G: 10 suggestions, mostly brand tails: "spotify abonnement opzeggen iphone",
  "tinder", "flitsmeister"; B "app abonnement opzeggen iphone"). Strong head; the support page answers the Apple-wide
  question, brand tails belong to the brands.
- **Secondary:** `app abonnement opzeggen` (G 10: "app abonnement opzeggen iphone", "app store abonnement opzeggen",
  "abonnement app opzeggen ipad"); `abonnement opzeggen app store` (G echo; B 8 including "opzeggen van een abonnement");
  `terugbetaling app store` (G 2, B 1) and `geld terug app store` (G 2, B tails); `aankopen herstellen` (G 7: "aankopen
  herstellen app store", "aankopen herstellen apple"); `apple terugbetaling aanvragen` (G 4).
- **FAQ-style (from suggest):**
  - Hoe zeg ik een abonnement op in de App Store? (G, exact; B "hoe kan ik een abonnement opzeggen")
  - Hoe zeg ik een app-abonnement op op mijn iPhone? (G "hoe abonnement opzeggen iphone")
  - Kan ik een abonnement altijd opzeggen? (B "kan je een abonnement altijd opzeggen")
  - Hoe vraag ik een terugbetaling aan bij Apple? (G "apple een terugbetaling aanvragen", "terugbetaling aanvragen app store")
  - Hoe herstel ik mijn aankopen? (G "aankopen herstellen", "aankopen herstellen app store")
  - Kan ik een abonnement delen met mijn gezin? (B "app delen met gezin"; G only brand tails; inferred)
- **Notes:** G and B for "in-app aankoop terugbetalen" and "aankoop herstellen iphone" returned almost nothing. The B
  terugbetaling results are Google Play. "App store support contact" returned only English tails and phone-number queries.
  Dutch-language Apple term for Family Sharing was not checked in this pass.

## Transparency (/nl/transparency/): privacy manifests, App Tracking Transparency, what each app collects

- **Primary:** `app tracking transparency` (G 7: "(att)", "apple", "ios", "framework"; B "app tracking transparency att",
  "ios"). Developer-heavy audience and English: Dutch has no returned localised form ("app tracking transparantie":
  empty). Use the English term with a Dutch explanation.
- **Secondary:** `app privacy labels` (G 6: "app store privacy labels", "apple app privacy labels", "app privacy nutrition
  labels"); `privacy app store` (G 8); `app privacy iphone` (G 8, "app privacy report iphone"); `trackers in apps` (G 2,
  echo).
- **FAQ-style (inferred from seed; B returned only English or developer variants):**
  - Wat is App Tracking Transparency? (B "what is a transparency app", "apple's app tracking transparency")
  - Wat zijn privacylabels in de App Store? (G "app store privacy labels"; B for "wat is een privacylabel" returned
    "wat is een privacybeleid", so the Dutch word "privacylabel" is not confirmed)
  - Welke gegevens verzamelen apps? (B "op welke manier verzamelen apps gegevens", "waarom verzamelen apps en websites
    data")
  - Hoe weet ik of een app mij volgt? (inferred; B returned generic app questions)
- **Notes:** "privacylabel app store", "apps volgen toestaan", "app privacyrapport" and "wat verzamelt een app" returned
  nothing useful. S for "privacy" returns VPNs, Signal and ad blockers: the competition for the word is security
  products. Treat the page as a trust page; do not claim a primary keyword it cannot win.

## aftershift: sleep for shift and night workers

- **Primary:** `slapen na nachtdienst` (G 8: "slecht slapen na nachtdienst", "hoelang slapen na nachtdienst", "beter
  slapen na nachtdienst", "goed slapen na nachtdienst"; B only unrelated). Clear informational demand in Dutch.
- **Secondary:** `ploegendienst slaap` (G "ploegendienst slaapproblemen", "slaapritme ploegendienst"; A "shiftrest:
  ploegendienst slaap"; S "AfterShift: Slaap & Ploegen" and three competitors); `slaapschuld` (G 8: "slaapschuld
  inhalen", "slaapschuld berekenen", B "slaapschuld", A "slaapschuld: slaaptracker", "backlogged: slaapschuld");
  `ploegendienst app` (G, B, A, S; but this is roster apps: "Supershift - Ploegenrooster", "ShiftCal"); `slaap app` (G 8,
  B, A, S: generic head, competitor "Sleep Cycle").
- **FAQ-style (from suggest):**
  - Hoelang moet je slapen na een nachtdienst? (G "hoelang slapen na nachtdienst", "hoelang slapen na een nachtdienst")
  - Waarom lukt slapen na een nachtdienst niet? (G "slapen na nachtdienst lukt niet")
  - Hoe kun je beter slapen na een nachtdienst? (G "beter slapen na nachtdienst")
  - Zijn nachtdiensten slecht voor je? (B "zijn nachtdiensten slecht voor je", "hoe slecht zijn nachtdiensten")
  - Wat is slaapschuld en kun je het inhalen? (G, B "wat is slaapschuld", "slaapschuld inhalen")
  - Wat is het beste slaapritme bij nachtdienst? (G "beste slaapritme nachtdienst")
- **Notes:** "shiftwerk" and "nachtdienst app" returned nothing useful (B: Apotheke noise). This is the best-evidenced
  page in the set: nine question forms from G alone. Collision: `ploegendienst app` is a roster-app keyword that other
  studio pages do not use; no other page takes `slaap`.

## allpaid: bill and payment reminders, no bank login

- **Primary:** `rekeningen bijhouden app` (G echo, plus "app rekeningen bijhouden"; S lists our own listing "AllPaid –
  Rekeningen bijhouden" and "Denk & Betaal: Rekeningen", "FIX: Vaste lasten & rekeningen"). Moderate.
- **Secondary:** `vaste lasten app` (G 8: "vaste lasten overzicht app", "vaste lasten bijhouden app"; B echo; S 8
  titles). This is the stronger head but it is budgeting-flavoured (huishoudboekje apps); `app voor vaste lasten` (G 4:
  "beste app voor vaste lasten", "app om vaste lasten bij te houden"); `betalingsherinnering iphone` (S titles only:
  "Betalingsherinnering", "Rekening Herinnering Vervaldag"); `app betalingen bijhouden` (G echo; S lists AllPaid).
- **FAQ-style (from B suggest, near the topic):**
  - Wat zijn vaste lasten? (B "wat betekent vaste lasten", "wat zijn mijn vaste lasten")
  - Hoe maak ik een overzicht van mijn vaste lasten? (B "vaste lasten overzicht maken", "overzicht vaste lasten per maand")
  - Hoe lang moet je rekeningen bewaren? (B "hoe lang moet je rekeningen bewaren")
  - Mag je herinneringskosten in rekening brengen? (B, tangential: late fees)
  - Kan ik een app gebruiken om rekeningen niet te vergeten? (inferred; the seed "app rekeningen niet vergeten" returned
    B noise)
- **Notes:** "betaalherinnering app" and "rekeningen herinnering app" returned only S titles. "No bank login" has no
  suggest evidence. The vaste lasten audience wants budgeting; AllPaid is a reminder app, so use "vaste lasten" in
  secondary wording only, and decide the title with the reviewer. If the writer prefers `vaste lasten app` as primary it
  stays free (no other page uses it).

## appmeta (Mac): App Store Connect metadata and ASO tool for developers

- **Primary:** `aso tool` (G 8: "aso tool free", "aso tool app store", "aso tools best"; B 2; A "aso tool - ai keyword
  tracker", "lookapp - aso tool"; S 6 titles). Strong, but English. Dutch developers type the English abbreviation;
  "app store optimalisatie" returned only a G echo and S titles.
- **Secondary:** `app store connect mac app` (G 8, but half is "cannot connect to app store" noise); `app metadata editor`
  (G, "app metadata analyzer"); `app store connect metadata` (G 8: "missing metadata" errors); `aso app store` (G 7, B 3);
  `app store optimalisatie` (G echo).
- **FAQ-style (from suggest):**
  - Wat is een ASO-tool? (G "aso tool meaning")
  - Wat is App Store Connect? (B "was ist app store connect" as the nearest form; inferred in Dutch)
  - Hoe bewerk ik app-metadata in App Store Connect? (G "app metadata editor", "app store connect metadata")
  - Wat betekent "missing metadata" in App Store Connect? (G "app store connect missing metadata" and variants: strong
    intent, but English phrasing)
- **Notes:** the audience is developers and reads English; the Dutch page should use the English terms (App Store Connect,
  ASO, metadata) in the title and Dutch only in the sentences. "App store zoekwoorden" and "app store beschrijving
  schrijven" returned S titles and B noise only. Collision: appmeta takes `aso tool` and metadata words; appmeta-pulse
  takes App Store Connect analytics and sales.

## appmeta-pulse: App Store Connect on iPhone, sales and analytics

- **Primary:** `app store connect analytics` (G 8: "delayed", "api", "not working"; B 8: "apple app store analytics"). Strong
  but developer English; answer-style "not working" tails are support questions.
- **Secondary:** `app store connect iphone` (G 8: "app store connect iphone only", "iphone app store connect"; mixed with
  "cannot connect to app store iphone 16" noise); `app store sales report` (G "app store sales report", "app store sales
  ios"; B "app store sales"); `app inkomsten bijhouden` is NOT a keyword (G returned household-budget results); S shows the
  Dutch vocabulary of competitors: "Metrics: omzet en verkoop ASC", "StoreMate: App-omzet analyse", "Lumetric for App Store
  Connect", "Repdio for App Store Connect".
- **FAQ-style (from suggest):**
  - Waarom loopt App Store Connect Analytics achter? (G "app store connect analytics delayed", "not enough data", "down")
  - Waar vind ik mijn App Store-verkopen? (inferred; "app store connect verkoop" gave only B account-creation noise)
  - Is er een App Store Connect-app voor iPhone? (G "app store connect iphone", "app store connect app")
  - Hoe bekijk ik mijn app-omzet? (S titles "omzet en verkoop", inferred)
- **Notes:** "app store inkomsten", "app store verkoopcijfers" and "app downloads bijhouden" returned only S titles or off-topic
  results. Word "omzet" appears in S titles; Dutch developers also say "inkomsten" and "verkoop". Keep the primary on the
  English phrase and use Dutch "omzet en verkoop" in the description.

## chessful: chess app, game analysis, lessons

- **Primary:** `schaak app` (G 8: "schaak app zonder reclame", "schaak app nederlands", "schaak app gratis", "schaak app
  kinderen", "schaak app voor beginners"; B "schaak app gratis", "schaak app"). Strong head with clear sub-intents.
- **Secondary:** `beste schaak app` (G 8: "voor beginners", "iphone", "ipad", "om te leren"; B "de beste schaak app");
  `schaken leren app` (G 4, B 2, S "Schaken: Leren, Spelen & Coach"); `schaakanalyse` (G 2: "schaakanalyse online"; B 2:
  "schaak analyse tool"); `schaakpartij analyseren` (G, B, S "Schaak – Analysebord", "Gambit - Schaak Analyse");
  `schaakpuzzels app` (G, S 8, B "schaakpuzzels oplossen"); `schaaklessen` (G 7, B 7; local lesson offers Gent and
  Amsterdam: audience wants teachers, so lower priority).
- **FAQ-style (from suggest):**
  - Wat is de beste schaak-app? (G "beste schaak app")
  - Wat is een goede app om schaken te leren? (G exact, "wat is een goede app om schaken te leren")
  - Hoe leer ik schaken als beginner? (G, B "schaken voor beginners" with "app", "oefeningen", "spelregels", "tegen
    computer")
  - Is er een schaak-app zonder reclame? (G "schaak app zonder reclame")
  - Is er een Nederlandse schaak-app? (G "schaak app nederlands")
  - Hoe analyseer ik een schaakpartij? (G, B "schaakpartij analyseren"; the "hoe analyseer ik" question form returned
    only Schaar and Schaats noise, so it is a de-facto inferred question)
- **Notes:** "schaak analyse app" and "schaak coach app" returned nothing. The Dutch App Store verb is "schaken" in titles
  ("Schaken: Leren, Spelen & Coach") and our own title is "Chessful: Train & Analyseer". Collision: chessful owns all
  `schaak` and `schaken` queries in part A; part B's Shogiful and Xiangqiful pages should not take `schaak app`.

## earnlock: block apps and screen time, earn time with steps

- **Primary:** `apps blokkeren iphone` (G 8: "apps tijdelijk blokkeren iphone", "bepaalde apps blokkeren op iphone",
  "apps blokkeren na bepaalde tijd iphone"; B echo; S 7 titles: "AppBLock", "Refocus: app blokkeren & sites", "Apps
  Blokkeren - Blokkeer App"). Strong. Beware: G also returns "reclame in apps blokkeren iphone" and "apps downloaden
  blokkeren iphone" (parental and ad-block intents).
- **Secondary:** `schermtijd verdienen` (G 3: "schermtijd verdienen app", "schermtijd verdienen kinderen"; B 1; A
  "schermtijd verdienen: kids"; S "Blocus: Verdien schermtijd", "ScrollToll: Schermtijd-gym", "Pushscroll: Sport, Dan
  Scroll"); `schermtijd beperken` (G 8, B 3, A 6, S 8: highest-volume parent of the cluster); `app limiet iphone` (G 5: "app
  limiet instellen iphone", "werkt niet", "code"; the Apple feature is "App-limieten" in Schermtijd); `tijdslimiet apps
  iphone` (G 3); `telefoonverslaving app` (G echo, S "Naze: Stop Telefoonverslaving", "Jomo - Schermtijd verminderen");
  `stappenteller app` (G 8: "stappenteller app apple watch", "stappenteller app gratis"; for the step mechanic).
- **FAQ-style (from suggest):**
  - Hoe blokkeer je apps op iPhone? (G "hoe blokkeer je apps op iphone")
  - Hoe kun je apps tijdelijk blokkeren? (G "app tijdelijk blokkeren", "hoe app tijdelijk blokkeren")
  - Wat te doen als je verslaafd bent aan je telefoon? (G "verslaafd aan telefoon wat te doen")
  - Hoe gebruik ik mijn telefoon minder? (G "hoe telefoon minder gebruiken", "app om minder op telefoon te zitten")
  - Werkt de app-limiet op iPhone niet? (G "app limiet iphone werkt niet")
  - Kan ik schermtijd verdienen met stappen? (S titles "Apps ontgrendelen met stappen", "brb: Lopend ontgrendelen", "StepLock
    - Loop & Ontgrendel"; G and B returned no matching question)
- **Notes:** the walking mechanic has no suggest demand ("wandelen om apps te ontgrendelen", "apps blokkeren stappen",
  "apps ontgrendelen met stappen": no G, B noise, only A and S as competitor app titles), so `schermtijd verdienen` is the
  nearest real query. Many S results carry "kids": Dutch parents search "schermtijd kinderen" (G 8, B 5), but EarnLock is for
  adults; keep copy neutral. Collision: `schermtijd` words stay on earnlock; no other page takes them.

## gymlogger-x: Apple Watch strength workout log

- **Primary:** `gym app apple watch` (G 8: "gym tracking app apple watch", "best gym app apple watch", "apple watch gym tracker
  app"; B 7 mixed). English phrasing is dominant in Dutch suggest for the Watch theme.
- **Secondary:** `apple watch krachttraining` (G 4: "apple watch functionele krachttraining", "apple watch traditionele
  krachttraining", "apple watch workout krachttraining"); `krachttraining app apple watch` (G echo; B returned German
  "apple watch krafttraining tracken"); `workout app apple watch` (G 8, mostly "not working" and "missing" tails, so
  support intent); `workout logger` (G 7, A 8 titles: "workout logger: gym tracker", "easy workout logger"). Apple's own
  Dutch name for the type is "Traditionele krachttraining" and "Functionele krachttraining" (G).
- **FAQ-style (from suggest):**
  - Wat is de beste gym-app voor Apple Watch? (G "best gym app apple watch")
  - Hoe houd ik krachttraining bij met Apple Watch? (G "apple watch krachttraining"; B German "apple watch krafttraining
    tracken" as the nearest form; inferred in Dutch)
  - Wat is het verschil tussen functionele en traditionele krachttraining op Apple Watch? (G "apple watch functionele
    krachttraining", "apple watch traditionele krachttraining")
  - Waarom verdwijnt de Workout-app van mijn Apple Watch? (G "workout app apple watch verdwenen", "missing", "deleted":
    support intent, mention only if the page can answer it)
  - Is er een gratis gym-app voor Apple Watch? (G "free gym app apple watch")
- **Notes:** `apple watch gewichten` (B 2, S titles) is thin. Collision with liftlog: liftlog takes `krachttraining app`
  and `workout log app`; gymlogger-x takes everything that contains "apple watch" or "gym app". Keep "Apple Watch" in the
  first words of the gymlogger-x title so the two stay separate.

## liftlog: gym workout log, no subscription

- **Primary:** `krachttraining app` (G 6: "krachttraining app vrouwen", "krachttraining app gratis", "krachttraining apple
  watch"; B "krachttraining app", "app krachttraining vrouwen"; S titles: "StrongLifts 5x5 Krachttraining", "RepCount - Gym
  Workout Tracker"). Note G and B also return "krachttraining apparaat" (equipment): intent is mixed.
- **Secondary:** `workout log app` (G 8, B 2, A "gym tracker: workout log app", S 8: Hevy, Strong, Fitlist; English phrase,
  strong); `krachttraining bijhouden` (G 3: "krachttraining bijhouden app", "krachttraining bijhouden garmin");
  `trainingslogboek app` (G echo; S 8 titles: "Trainingslogboek: GymKing", "Overlood: Sportschool Logboek");
  `sportschool app` (G, B, A, S, but half is "sportschool apparaten" and gym-chain apps like Basic-Fit); `fitness app
  zonder abonnement` (G echo only; B and S noise). `training bijhouden app` (G echo).
- **FAQ-style (from suggest):**
  - Wat is de beste app om krachttraining bij te houden? (G "krachttraining bijhouden app")
  - Is er een gratis krachttraining-app? (G "krachttraining app gratis")
  - Welke app houdt mijn sportschoolschema bij? (G "sportschool schema app", "trainingsschema app")
  - Is er een trainingsschema-app zonder abonnement? (G "fitness app zonder abonnement" echo; B "fit for free abonnementen"
    as noise: inferred from seed)
  - Hoe houd ik mijn gewichten bij in de sportschool? (G "fitness app gewichten bijhouden")
- **Notes:** "zonder abonnement" has very little Dutch demand: G echo only for fitness, nothing for sportschool or
  krachttraining. The house rule allows "zonder abonnement" for LiftLog only, so use it in body copy and the lead, not as the
  primary. `workout log app` is the strongest phrase but is English; it is a good secondary. Collisions: see gymlogger-x
  above; also `workout tracker` (G 8 but English, template tails) is left unused by both.

## mediakit: compress video and PDF, convert HEIC on iPhone and Mac

- **Primary:** `video comprimeren iphone` (G 2: "video comprimeren iphone gratis"; B 1; S "Compressor - video comprimeren",
  "Compress Videos & Resize Video"). Moderate. Chosen because the app name and the first feature are compression. Its twin
  `video verkleinen iphone` (G 3: "video mb verkleinen iphone", "video verkleinen voor mail iphone"; B 1; S "Squeeze -
  Video Verkleinen") is of equal strength: use it in the H1 or description so both verbs are covered.
- **Secondary:** `pdf comprimeren` (G 8, B 8, A 4, S 8: "pdf comprimeren gratis", "zonder registratie", "macbook", "mac",
  "ilovepdf") and `pdf verkleinen` (G 8, B 8, A 7, S 8); `heic naar jpg` (G 8, B 8, A 8, S 7: strongest single phrase in the
  whole research set, with "heic converteren naar jpg" G 8, B 8); `foto verkleinen iphone` (G 7: "app", "mb", "bestandsgrootte",
  B 2); `pdf verkleinen mac` (G 8: "pdf verkleinen mac gratis", "zonder kwaliteitsverlies mac"); `video comprimeren mac` (G 2:
  "video comprimeren macbook").
- **FAQ-style (from suggest):**
  - Hoe verklein ik een video op iPhone? (B "video op iphone kleiner maken", "hoe verklein ik een video"; G "video
    verkleinen iphone")
  - Hoe verklein ik een video om te mailen? (G "video verkleinen voor mail iphone")
  - Hoe comprimeer ik een pdf zonder kwaliteitsverlies? (G "pdf verkleinen zonder kwaliteitsverlies mac")
  - Hoe verklein ik een pdf-bestand gratis? (B "hoe verklein ik een pdf bestand gratis")
  - Hoe zet ik HEIC om naar JPG? (B "hoe heic omzetten naar jpg", "heic naar jpg omzetten"; G "heic naar jpg iphone")
  - Hoe zet ik HEIC automatisch op JPG op iPhone? (G "heic naar jpg instellen iphone", "iphone jpg vs heic")
- **Notes:** the page covers three tools and the demand differs by tool. `heic naar jpg` is the biggest demand but the
  competition is online converters and free apps ("ConvertMagic", "HEIC Converter"); `pdf comprimeren` ("zonder upload": A
  returns "pdf comprimeren - geen upload", a privacy angle that matches the studio) is next. Recommendation: keep the
  title on compression (`video comprimeren iphone` + "PDF" + "HEIC") and put `heic naar jpg` and `pdf comprimeren` in
  H2 sections and FAQ. G for Mac tails is noisy ("pdf verkleinern" in B is German). "Foto's converteren iphone" returned
  only "foto converteren naar pdf iphone". Collision: no other page takes `pdf`, `heic`, `comprimeren` or `verkleinen`.

---

## Summary table and collision map

| page | primary | secondaries |
|---|---|---|
| Home /nl/ | apps zonder reclame | apps zonder reclame iphone; spelletjes apps zonder reclame; puzzel apps zonder reclame |
| Apps hub /nl/apps/ | beste apps iphone | beste apps ipad; beste apps apple watch; apps voor mac |
| About /nl/lagerland-apps/ | indie apps iphone (weak, brand-led page) | apps van een kleine ontwikkelaar (body only); indie ontwikkelaar apps |
| Support /nl/support/ | abonnement opzeggen iphone | app abonnement opzeggen; abonnement opzeggen app store; terugbetaling app store; geld terug app store; aankopen herstellen |
| Transparency /nl/transparency/ | app tracking transparency | app privacy labels; privacy app store; app privacy iphone |
| aftershift | slapen na nachtdienst | ploegendienst slaap; slaapschuld; ploegendienst app; slaap app |
| allpaid | rekeningen bijhouden app | vaste lasten app; app voor vaste lasten; betalingsherinnering iphone |
| appmeta | aso tool | app store connect mac app; app metadata editor; aso app store |
| appmeta-pulse | app store connect analytics | app store connect iphone; app store sales report |
| chessful | schaak app | beste schaak app; schaken leren app; schaakanalyse; schaakpartij analyseren; schaakpuzzels app |
| earnlock | apps blokkeren iphone | schermtijd verdienen; schermtijd beperken; app limiet iphone; telefoonverslaving app |
| gymlogger-x | gym app apple watch | apple watch krachttraining; workout app apple watch; workout logger |
| liftlog | krachttraining app | workout log app; krachttraining bijhouden; trainingslogboek app; sportschool app |
| mediakit | video comprimeren iphone | pdf comprimeren; pdf verkleinen; heic naar jpg; foto verkleinen iphone |

Splits recorded:

- Home and About do not share a primary: Home takes `apps zonder reclame`, About takes `indie apps iphone`.
- aftershift keeps all `slaap` and `nachtdienst` words; earnlock keeps all `schermtijd` and `apps blokkeren` words; no
  other page uses either set.
- gymlogger-x (`gym app apple watch`, `apple watch krachttraining`) and liftlog (`krachttraining app`, `workout log app`)
  are split by the words "apple watch". `workout tracker` is left unused (English, template and printable tails).
- appmeta (`aso tool`, metadata) and appmeta-pulse (`app store connect analytics`, sales): "App Store Connect" is in both
  titles by name but each owns its own head keyword.
- Hub's `beste apps apple watch` does not collide with gymlogger-x `gym app apple watch` (different heads).
- mediakit owns `comprimeren`/`verkleinen`; chessful owns `schaak`/`schaken` for part A.
- Words to use in title tails only if the writer wants more reach: `apps zonder reclame` for any puzzle page in part B
  (G "puzzel apps zonder reclame", "spelletjes apps zonder reclame") is a Home secondary; tell part B so it is not
  taken as primary there.


---

## Dutch keyword research, part B

Part of the language sheet `_i18n/nl.md` (to be written). Research pass on 2026-11-19, part B: twelve app pages (millrace,
mockly, observa, pawza, rightsplit, shogiful, soon, tare, taskful-day, wanderwiki, xiangqiful, clippet). Part A (studio
pages and the other apps) is a separate file. Format follows `_i18n/pt-keywords.md`.

Source marks: **G** = Google suggest (`hl=nl&gl=nl`, `client=firefox`), **GQ** = Google suggest with a question or
modifier prefix (hoe, wat is, welke, beste, gratis, kan ik, waarom), **GAZ** = Google suggest with an a-z suffix, **B** =
Bing autosuggest (`qsonhs`, `mkt=nl-NL`), **A** = App Store search hints (`MZSearchHints`, storefront `143452-10,29`,
Netherlands), **S** = iTunes Search API (`country=nl`, `lang=nl_nl`), used for competitor names and for the vocabulary of
Dutch app titles. Every query below was returned by one of these sources; nothing is invented. "Echo" means the source
returned only the seed itself (proves the phrase exists, shows no tail demand). Search Console for the Netherlands was
not read. People also ask was not collected (it needs a live results page).

### Method note

- **Requests: about 2,200**, 0.4 to 0.5 s apart, generic Safari User-Agent, no personal data sent. Run 1: 117 seeds on G,
  B, A and S; the first four seeds of each page also got 7 question prefixes and a-z suffixes on G. Run 2: 125 gap-filling
  seeds on G, B, A and S (variants, spelling forms, Tare and the collision checks). Scripts and raw JSON are in the
  session scratchpad, not the repo.
- **Google suggest worked** and is well localised for Dutch (hl=nl gl=nl): nearly all Dutch seeds return Dutch tails
  (unlike pt-PT, no Brazilian-style drift). It is thin for app-intent phrases: most `<thing> app` seeds return 0 to 10
  suggestions, and Dutch long tails are often only the seed. English-language developer and tech topics (Mockly, Observa's
  "hrv", Clippet's "clipboard manager", WanderWiki's "random wikipedia") come back in English even with `hl=nl`: Dutch
  people type those in English or in mixed form. Where that is so the note says so; the keyword is recorded as typed.
- **Bing (`api.bing.com/qsonhs.aspx?mkt=nl-NL`) worked but is noisy**: German ("wie heißt die app für screenshot",
  "welche apple watch habe ich"), English and nonsense leak in (`bonesplitter` for "bon splitten", `aflapin` for
  "aftelapp"). B is used only to confirm a phrase when it returns the phrase itself or a close Dutch tail.
- **App Store hints worked** for the Netherlands storefront (response is a plist; the first `<string>` "Suggestions" and the
  `https://` entries are artefacts and were dropped). Hints are Dutch app-title vocabulary ("aftellen naar gebeurtenissen",
  "to-do lijst & planner", "rekening splitsen", "dagplanner", "hartslagvariabiliteit"). Empty for most English or
  developer terms.
- **iTunes Search API worked.** Apple's own Dutch search shows our own listings already: `Shogiful: Japans schaken` (hit
  for the seed "japans schaken"). Competitor title vocabulary: "Logische puzzels", "Rekenpuzzel", "Breinbreker",
  "Rekening splitsen", "Kosten delen", "Slaaptracker", "Herstel & Slaap", "Hartslagmeter", "Mijn Huisdier-app",
  "Huisdierzorg", "Bonnetjes splitten", "to-do lijst & takenbeheer".
- **Vocabulary decisions for the Netherlands** (evidence in the sections):
  - Split a bill: **`rekening splitsen`** is the standard form (G, A, S); G itself rewrites "splitten" to "splitsen" ("rekening splitsen app",
    "bon splitsen") and returns only one "splitten" tail (`rekening splitten berekenen`). `Splitten` stays in S titles
    ("Bonnetjes Splitten"). Use "splitsen" as the keyword, "splitten" is acceptable colloquial body copy.
  - Share costs: **`kosten delen`** (G 8 tails, B). "Verdelen" is weaker (G echo `kosten verdelen app`).
  - Countdown: both **`aftel app`** (A, G, B) and **`aftellen app`** (G 10) are searched, and the loan `countdown app` is as
    big (G 10, B 8, A 8). Dutch spelling is "aftelapp" as a compound, but searchers type it as two words.
  - To-do: **`to do lijst`** (no hyphen) dominates over `to-do lijst` and `todo`. G even returns the spelling dispute
    `to-do lijst of to-do-lijst`. `Takenlijst` is the Dutch-word twin with equal suggest depth.
  - Clipboard: **`klembord`** (G, B). Dutch compound `klembordgeschiedenis` appears (G) but "klembord geschiedenis" is
    typed far more. "Clipboard manager" is typed in English for Mac (G 10).
  - Heart-rate variability: **`hartslagvariabiliteit`** (full word, G 10 and B 7, A) and the English abbreviation **`hrv`**
    (G, always with "apple watch"). Never "hartslagvariatie" (not returned). HRV on Apple Watch is SDNN: the research
    returned `hrv sdnn vs rmssd` only in English (G, B); no Dutch query names SDNN.
  - "Readiness score" is typed in English even by Dutch searchers (G, B); the Dutch "herstelscore" returned nothing.
  - Chess family: **`chinees schaken`** (Xiangqi) and **`japans schaken`** (Shogi) are both Dutch, and A/S show app titles
    built from the same words.
  - Belgian/Flemish notes (not keywords): G returns `tikkie alternatief belgie`, `verplichte vaccinaties kat belgie`,
    `vaccinatie hond belgie`, `shogi belgium`; Flemish speakers say "Payconiq/Bancontact" instead of Tikkie.
- **Weak or empty in Dutch suggest:** the whole "no subscription / no ads" theme (`puzzelspel zonder advertenties`,
  `puzzelspel offline`, `puzzelspel zonder internet`: empty on G, B, A), `huisdier gezondheid app`, `dierenpaspoort app`,
  `medicijnen huisdier herinnering` (empty on G and B; only S lists apps), `taken doorschuiven`, `aftellen tentamen`,
  `chinees schaak app`, `xiangqi leren`, `shogi leren`, `japans schaak app`, `wikipedia swipen`, `herstel score apple watch`.
  Do not use these as keywords.

### Collision map (one primary per page)

| page | primary | split from |
|---|---|---|
| millrace | `logische puzzel app` | Tare takes `puzzelgames iphone`; Millrace never uses "puzzelgames" in H1 or title |
| tare | `beste puzzelgames iphone` | Millrace takes the logic/number side; `balans puzzel` is crossword-clue noise, avoid |
| shogiful | `shogi app` | xiangqiful takes `chinees schaken`; neither takes `schaak app` (Chessful, another agent) |
| xiangqiful | `chinees schaken` | `japans schaken` stays with Shogiful as a secondary |
| soon | `aftel app` | no overlap |
| taskful-day | `to do lijst app` | no other to-do page |
| clippet | `klembord geschiedenis` | no overlap |

---

## millrace (/nl/apps/millrace/): tile puzzle with a proven shortest solution

Never searched or used the number title the app replaced. Only logic and puzzle queries.

- **Primary:** `logische puzzel app`. G echo ("logische puzzel app"); S confirms the vocabulary ("Sudoku: Logische puzzels",
  "Easy Game - Logische puzzels", "Cross Logic - Logische Puzzels"); A hint `logica puzzels` ("kakuro cijfer logica puzzels",
  "slinky sort logica-puzzelspel"). Close sibling with more tail: `logica puzzels` (G 7: online, kinderen, app, groep 8,
  denksport, `logica puzzelspel`; B `logica puzzels online`) and `logica puzzels app` (G).
- **Secondary:**
  - `getallenspel` (G 2, B 8, A "getallenspel: match & merge", "getallenspel: concentratie"): fits a number-merge tile
    puzzle; strong in B but kids' arithmetic mixes in ("getallen splitsen groep 3").
  - `puzzel app zonder reclame` (G, 4th suggestion of `puzzel app`, which has 10 G tails: gratis, kinderen, android,
    volkskrant, trouw); also G echo `puzzelspel zonder reclame`.
  - `rekenpuzzel` (G 10, B 8, A 8, S "Cross Math: Rekenpuzzel", "Number Mash"): the number-puzzle audience; mostly
    school ("groep 4 to 8") and "volwassenen". Use only as a supporting phrase.
- **Strength notes:** G for the generic head `puzzelspel` (puzzelspelletjes, online, volwassenen, switch, ps5, kinderen) and
  `puzzelspellen` (G 8, B 8, A 7) is big but console, children and online dominated: that is not the Millrace audience.
  `hersenspel app` G only gives `hersen spelletjes app`; `denkspel iphone`, `logica spel iphone`, `cijferpuzzel app`,
  `tegels samenvoegen spel`, `puzzelspel offline` are empty.
- **FAQ-style (from suggest):**
  - welke puzzel app zonder reclame (nearest: G `puzzel app zonder reclame`)
  - beste puzzel app gratis (G `puzzel app gratis`)
  - logische puzzels voor volwassenen (G `puzzelspel volwassenen`, B `puzzel spelletjes voor volwassenen`)
  - leuke puzzelspellen (G `leuke puzzelspellen`)
  - is er een puzzelspel zonder reclame (G echo `puzzelspel zonder reclame`)
  - puzzelspel ipad (G `puzzelspel ipad`)
- **Notes:** do not write "app voor kinderen" or "groep" phrases: they dominate the numeric suggest but the app is not
  for school use. `breinbreker` (G 10, B 8, A app titles "Busparkeren: Breinbreker") is a usable body word for puzzles.

## tare (/nl/apps/tare/): wordless balance logic puzzle

- **Primary:** `beste puzzelgames iphone` (G, three separate seeds returned it: `puzzelspel iphone`, `puzzelspellen iphone`,
  `beste puzzelspellen iphone`). Pair it with the phrase `puzzelspel iphone` (G, plus `leukste puzzelspel iphone`) in the
  body. This follows the Portuguese split: Tare takes the general "best puzzle games iPhone" head, Millrace the logic head.
- **Secondary:**
  - `denkspelletjes app` (G; `denkspelletjes` G 9 with volwassenen, ouderen, kind; B 8; A `focsy: offline denkspelletjes`);
  - `breinbreker` (G 10, B 8, A "Not Not 2 - Een breinbreker", "Shadow Blocks: 3D breinbreker"; S confirms): Dutch app
    titles use it for puzzle games, a fit for a deduction puzzle;
  - `hersen spelletjes app` (G, from `hersenspel app`; `hersenspelletjes` G 9 but dog-enrichment games dominate: "hersenspelletjes
    hond", so avoid the bare form).
- **Strength notes:** the mechanic words are dead. `balans puzzel`, `weegschaal puzzel` and `gewichten puzzel` return
  crossword-solver noise (G `balans puzzelwoord`, `weegschaal puzzelwoordenboek`, `in balans puzzelwoordenboek 3 letters`;
  B `puzzelwoord voor balans`). `puzzelspel zonder woorden`, `balanspuzzel app`, `raadsel gewichten balans` are empty. Do
  not put "balans puzzel" in the title or H1 as the target; describe the mechanic in body copy only.
- **FAQ-style (from suggest):**
  - beste puzzelgames iphone (G)
  - welke denkspelletjes app voor volwassenen (G `denkspelletjes volwassenen`)
  - hersenspelletjes voor volwassenen (B `hersenspelletjes volwassenen`)
  - zijn er breinbrekers zonder woorden (no suggest; closest G `breinbrekers volwassenen`)
  - breinbrekers met oplossingen (G, B `breinbrekers online`)
- **Notes:** "zonder woorden" has no suggest evidence; the writer may state the fact (wordless) but not claim it as a search
  term. Keep the Millrace and Tare pages linked to each other in one sentence (shared cluster), with different H1 words.

## mockly (/nl/apps/mockly/): Mac app for App Store screenshots

- **Primary:** `app store screenshots` (G 10: generator, mockup, requirements, sizes, figma, free, guidelines, inspiration;
  B 6; Dutch developers type it in English; the Dutch seed `app store screenshots maken` returned only Bing noise
  about phone screenshots). S confirms the competitor set: "Screenshot Studio - App Mockup", "Screenshots Pro",
  "StoreView: App Screenshot Tool", "Picasso App Screenshot Studio", "SMPRO: Mockup & Screenshot".
- **Secondary:** `app store screenshot generator` (G, B, many GAZ tails: free, online, ai, ipad, github, figma, canva);
  `app store screenshot sizes` (G, B `app store connect screenshots sizes`); `mockup app store` (G, 9 suggestions:
  free, figma, generator, size, play store).
- **Strength notes:** Dutch-word seeds (`app store afbeeldingen`, `screenshots vertalen app store`, `app screenshots maken`,
  `iphone mockup maken`, `mockup maker mac`) are empty or consumer noise ("screenshot maken op iphone"). `screenshot maker`
  (G 9, A "ishots - app screenshot maker", "storeshots") is too wide: it is mostly "take a screenshot". The Dutch page should
  keep "App Store-screenshots" (the term with a hyphen is correct Dutch spelling for "App Store" as a first element)
  in title and H1, and let the English search term appear as the product category.
- **FAQ-style (from suggest, English as typed):**
  - app store screenshot sizes (G, B)
  - app store required screenshots (GAZ)
  - app store number of screenshots (GAZ)
  - app store connect screenshots not uploading (GAZ)
  - app store screenshots best practices (GAZ)
  - app store screenshot generator free (G)
- **Notes:** audience is developers; keep the FAQ queries in the form they are typed (English nouns, Dutch grammar around them).
  Do not target `screenshot maken` (consumer, how-to). "Mockup" is the Dutch word as is (G `mockup app store`).

## observa (/nl/apps/observa/): Apple Health readiness, sleep and HRV

- **Primary:** `hrv apple watch` (G 10: betrouwbaar, se, ultra, meaning; B `hrv meten apple watch`, `hrv apple watch app`;
  S confirms apps "Stress Monitor: HRV & Hartslag", "Welltory"; A has `ready: hrv & readiness score`). The page title
  can use `HRV` as the leading word and put "hartslagvariabiliteit" in the quick answer.
- **Secondary:**
  - `hartslagvariabiliteit apple watch` (G echo; the seed `hartslagvariabiliteit` has 10 G tails and 7 B: in slaap, verbeteren, hoog,
    laag, normaal, normaalwaarden, meten; GAZ: `hartslagvariabiliteit apple watch`, `per leeftijd`, `en leeftijd`);
  - `slaapscore apple watch` (G 10: uitzetten, werkt niet, instellen, meten; B echo; S "Slaaptracker", "Tide: Herstel & Slaap");
  - `readiness score apple watch` (G, B; also `readiness score apple`, `readiness score iphone`, G): typed in English.
  Also usable: `slaap app apple watch` (G 9: werkt niet, downloaden, gratis, beste), `stress meten apple watch` (G 4, B 8),
  `apple gezondheid app` (G 10, A, S; Apple's own Dutch name is "Gezondheid").
- **Strength notes:** the Dutch long tails for HRV are mostly informational (what is a good HRV, normal values by age);
  they match the FAQ block, not the app title. `herstel apple watch` (G 5: "herstel meten apple watch", "cardio herstel apple watch")
  is the recovery angle. `hrv app` G 9 ("hrv app iphone", "hrv apple health"), B 8. `apple watch herstel score` is empty (Bing returned
  unrelated "welke apple watch heb ik"). `hrv sdnn` is English only (G 10, B 7: "hrv sdnn vs rmssd", "normal range").
- **FAQ-style (from suggest):**
  - wat is een goede hrv apple watch (GQ)
  - is hrv apple watch betrouwbaar (GQ; G `hrv apple watch betrouwbaar`)
  - hoe hrv meten apple watch (GQ; B `hrv meten apple watch`)
  - beste hrv app apple watch (GQ)
  - wat is een normale hartslagvariabiliteit (GQ)
  - hoe verbeter je hartslagvariabiliteit (GQ)
  - kan je stress meten met apple watch (G)
  - slaapscore apple watch werkt niet (G)
- **Notes:** HRV is SDNN on Apple Watch, never RMSSD (project rule); no Dutch suggest names either, so the FAQ answer states it
  plainly. `hartslagvariabiliteit tabel`, `... per leeftijd`, `... normaal` (G) show the demand is for normal ranges: keep the
  FAQ medical-claim-free (compare to your own baseline, not to a population table).

## pawza (/nl/apps/pawza/): pet health records

- **Primary:** `vaccinatieboekje hond` (G 5: kwijt, kopen, vol, hoesje; B `vaccinatieboekje hond kwijt`, `vaccinatieboekje online`;
  G also `vaccinatieboekje kat` with 5 tails). The intent is the paper booklet; the page positions the app as the
  place to keep and scan it, never as an official passport.
- **Secondary:**
  - `vaccinaties kat` (G 10: kosten, schema, nodig, pension, verplicht, buitenland; B `vaccinatie kat schema`, `vaccinatie kat prijs`);
    GQ gives the questions below;
  - `dierenpaspoort` (G 10: kwijt, hoesje, aanvragen, kopen, kat; B 8; A `pawsdoc - dierenpaspoort`, a competitor);
  - `huisdieren app` (G echo, B `huisdieren app`; G tails are apartment noise: `huisdieren appartement`, so the keyword is weak) or
    `app dierenarts` (G 4: `mijn dierenarts app`, `app de dierenarts review`; that is a Dutch brand ("De Dierenarts"), so
    treat it as neutral).
  Also: `gewicht hond bijhouden` (G echo; S "Furiend", "Huisdieren Bijhouden - Soulkin"), `medisch dossier huisdier` (G 2).
- **Strength notes:** empty on G and B: `huisdier gezondheid app`, `dierenpaspoort app`, `digitaal vaccinatieboekje hond`,
  `huisdieren app dierenarts`, `medicijnen hond herinnering`, `dierenarts bonnetjes bewaren`, `entingen hond app`. S shows
  that apps with Dutch titles exist ("Huisdier Medicijn Herinnering", "Huisdier Medicijnen・TailCare", "PetFetch -
  Huisdierplanner", "Huisdierzorg"), but they are not searched in Google. The App Store hint `mypetapp mijn huisdier-app`
  (A) is the only app-title echo for `huisdier app`.
- **FAQ-style (from suggest):**
  - welke vaccinaties heeft mijn kat nodig (GQ)
  - hoe vaak vaccinaties kat (GQ)
  - wat kosten vaccinaties kat (GQ)
  - vaccinatieboekje hond kwijt (G, B)
  - vaccinatieboekje kat kwijt (G)
  - dierenpaspoort kwijt (G, B)
  - vaccinatie hond kosten (G, B)
- **Notes:** "Entingen" is Flemish (not returned for NL); the Netherlands says "vaccinatie". Belgium tails
  (`vaccinatie hond belgie`, `verplichte vaccinaties kat belgie`) are a note. Do not give veterinary or vaccination-schedule
  advice in the FAQ; answer only "where do I keep the proof of vaccination and how do I find it again".

## rightsplit (/nl/apps/rightsplit/): scan the bill and split it

- **Primary:** `rekening splitsen app` (G echo and via `rekening splitsen`: 9 tails: app, online, restaurant, rabobank,
  revolut, ing; A hints list three competitors: "BilliePay: Rekening splitsen", "Evens: Rekening splitsen", "Tabsnap: Rekening
  splitsen"; S confirms "Tabsnap: Rekening splitsen", "Kosten Delen: Rekening App", "Splitzz - Bonnetjes Splitten").
- **Secondary:**
  - `kosten delen app` (G 8: samen, beste, vakantie, vrienden, gratis; GQ `beste kosten delen app`, `welke app voor kosten delen`; B 2);
  - `tikkie alternatief` (G 3: belgie, buitenland; B 2; GAZ `alternatief voor tikkie`): comparison intent, trademark
    caution (Tikkie is another company's product; use it only on a comparison page);
  - `bonnetje splitsen` (G echo, `bon splitsen` G echo, `rekening splitsen restaurant` G);
  - `splitwise alternatief` (G 2, B 4 English tails).
  Also `kassabon scannen app` (G echo; S "Bonnen scannen: Slipbook", "ScanTicket").
- **Strength notes:** G rewrites "splitten" to "splitsen" ("rekening splitten app" returned `rekening splitsen app`). `tikkie`
  itself is huge (G 9, B 8, A 7) but that is a payment-request brand, not a split calculator. `rekening splitsen vrienden`,
  `uitgaven delen vrienden`, `restaurant rekening verdelen`, `samen uit eten rekening verdelen` are empty or near-empty;
  `geld verdelen vrienden` (G 2). Bing is poor here (`bonesplitter` noise).
- **FAQ-style (from suggest):**
  - welke app voor kosten delen (GQ)
  - beste kosten delen app (GQ)
  - gratis app kosten delen (GQ)
  - app kosten delen vakantie (GAZ)
  - app kosten delen vrienden (GAZ)
  - hoe rekening splitsen restaurant (G `rekening splitsen restaurant`)
  - alternatief voor tikkie (GAZ)
- **Notes:** the page must make clear that RightSplit does not move money (no payment claim): Dutch searchers associate
  "splitsen" with Tikkie payment requests. Flemish: `tikkie alternatief belgie` (G) shows the brand is used in Belgium too, but
  the Belgian payment term is Payconiq; not returned, so a note only.

## shogiful (/nl/apps/shogiful/): shogi app

- **Primary:** `shogi app` (G 10 including `shogi app ios`, `shogi app store`, `shogi application`; B 8: for beginners, free,
  offline, download, with tutorials; GAZ many: best shogi app iphone, shogi learning app, shogi lernen app). The tails are
  English: Dutch searchers type the English phrase. A hints `shogi` (8, all apps) and S confirm competitors ("Shogi Wars",
  "PiyoShogi", "Shogi Lv.100 Entry Edition", "Shogi Master", "Shogi - Classic Shogi Master").
- **Secondary:**
  - `japans schaken` (G echo; A hint **`shogiful: japans schaken`** (our own listing title); S `Shogiful: Japans schaken` ranked
    in Dutch search; the strongest Dutch-word phrase);
  - `shogi regels` / `shogi spelregels` (G echo each; B returned `shogi regeln` and `shogi spielregeln` German);
  - `shogi online` (G 10, B 8; no Dutch tail).
  Also `japans schaakspel` (G 2, B echo; `japans schaakspel 5 letters` is crossword noise), `shogi bordspel` (G echo),
  `shogi gratis` (GQ), `wat is shogi` (G echo; Bing noise).
- **Strength notes:** the bare seed `shogi` is dominated by games, anime and `shoghi effendi` (GAZ), and `shogi leren`, `shogi uitleg`,
  `shogi spelen`, `shogi tegen computer`, `japans schaak app`, `shogi vs schaken` are empty. The Dutch word "schaken" attaches
  to Japan (`japans schaken`), China (`chinees schaken`) or chess itself (Chessful's, not this page's).
- **FAQ-style (from suggest):**
  - wat is shogi (GQ, G)
  - shogi regels (G)
  - shogi spelregels (G)
  - shogi gratis (GQ)
  - shogi app for beginners (B, English as typed)
  - shogi app offline (B)
  - best shogi app iphone (GAZ)
- **Notes:** "Japans schaken" (capital J only at sentence start). Do not use `schaak app` (Chessful). Do not claim "Japanese
  chess" equals chess: say shogi is a related game that has drops (captured pieces return), a fact from the blueprint.

## soon (/nl/apps/soon/): countdown app with widgets

- **Primary:** `aftel app` (seed `aftelapp` returned G `aftel app` with 8 tails: vakantie, iphone, met widget, gratis, pensioen; A first hint
  `aftel app`; B echo; GQ `gratis aftel app`). Also `aftellen app` (G 10: iphone widget, gratis, dagen countdown, vakantie, naar pensioen;
  A `aftellen app & widget`). Use `aftel app` in the title and `aftellen` in body.
- **Secondary:**
  - `countdown app` (G 10: apple, gratis, iphone, android; B 8; A 8; GQ `beste countdown app iphone`): the English loan is as big
    as the Dutch word; Dutch searchers use both;
  - `countdown widget iphone` (G 10: lock screen, home screen, gratis; B 2; A `countdown widget`, `daymark: aftelwidget`,
    `outside: aftelwidget`);
  - `aftellen naar vakantie` (G 10, B 2, A `aftellen vakantie`; with app: `aftellen naar vakantie app`, `app aftellen naar vakantie gratis`);
  - `aftellen bruiloft app` (G; `aftellen bruiloft` G 2) and `aftellen zwangerschap app` (G; `aftellen zwangerschap` G 5, one tail is
    "quote").
- **Strength notes:** `hoeveel dagen tot` returns date-specific queries (kerst, sinterklaas, gta 6) which are not app queries.
  `aftellen app iphone` (G; `aftellen app iphone widget` G), `dagen aftellen app` (G 5), `app aftellen naar pensioen` and `aftel app
  pensioen` (G) are real demand: pensioen (retirement) is a Dutch favourite, but check the app's feature claim before using it.
  Empty: `aftellen tentamen`, `dagen tot vakantie app` (B noise), `aftellen naar geboorte` (G echo only).
- **FAQ-style (from suggest):**
  - gratis aftel app (GQ)
  - beste countdown app iphone (GQ)
  - aftel app met widget (G)
  - app aftellen naar vakantie gratis (G)
  - app aftellen naar pensioen (G)
  - aftellen bruiloft app (G)
  - dagen aftellen app iphone (G)
- **Notes:** "gratis" tails are everywhere; the price must come from the master (tokens), and no "gratis" claim is allowed unless
  the master says free or there is a free tier. Soon.'s name has a trailing dot: write "Soon." in prose as in English.

## taskful-day (/nl/apps/taskful-day/): day planner, tasks move on

- **Primary:** `to do lijst app` (G 10: gratis, delen, beste, huishouden, maken; GQ `beste to do lijst app`, `gratis to do lijst app`;
  A `to do lijst` 7: "Todoist: to-do lijst & planner", "2Do: to-do lijst & takenbeheer", "mijn to-do lijst & dagplanner"; B 8, in
  English spelling "to do list app"). Largest Dutch to-do demand; very competitive, but the App Store hints show the
  Dutch title vocabulary.
- **Secondary:**
  - `dagplanner app` (G 4: gratis, kind, beste; B echo; A `dagplanner` 7: "Dagplanner - Kalender, agenda", "Dagplanner: Routine &
    Taken"; `dagelijkse planner app` G): the closest match to the app's own "day planner" claim;
  - `takenlijst app` (G 10: gratis, iphone, apple, delen; B 3; A `takenlijst` 7: "T3T - Takenlijst en planner");
  - `to do lijst iphone` (G 6: maken op iphone, gezamenlijke; B `to do list iphone widget`).
- **Strength notes:** `dagplanning` and `dagplanner` (without "app") are dominated by children's daily schedule cards
  ("dagplanning kaartjes", "dagplanner kind", "kleuters", "autisme"): add "app" or "iphone". `to do lijst app apple watch`
  and `takenlijst app apple watch` are empty in G (Bing noise); the English `to do list app apple watch` (G 3) shows the phrase as
  typed. `taken doorschuiven`, `taken niet afgerond` are empty. `planner app` (G 9) is Microsoft Planner dominated.
- **FAQ-style (from suggest):**
  - beste to do lijst app (GQ)
  - gratis to do lijst app (GQ)
  - gezamenlijke to do lijst app (G, B)
  - beste takenlijst app (GQ)
  - gratis dagplanner app (GQ)
  - to do lijst maken iphone (G)
  - dagplanner app gratis (G)
- **Notes:** `to do lijst` without hyphen is the typed form; G debates `to-do lijst of to-do-lijst` (official spelling is
  with hyphens, "to-do-lijst", which the writer may use in prose; the keyword stays unhyphenated). Shared-list tails
  (`delen`, `gezamenlijke`) are real demand; do not claim sharing unless the blueprint lists it. Avoid collision with
  Chessful-type Dutch generic "agenda" pages.

## wanderwiki (/nl/apps/wanderwiki/): random Wikipedia articles

- **Primary:** `willekeurige wikipedia pagina` (G echo, B echo, GAZ echo; `wikipedia willekeurige pagina` G, B; `willekeurig artikel` G
  echo; `wikipedia willekeurig` G). Dutch searchers type this when they want a random article. The English `random wikipedia`
  has far more tail (below).
- **Secondary:**
  - `random wikipedia` (G 10: page, page generator, artikel, article generator, game; B 8, incl. `random wikipedia artikel` in
    mixed form): Dutch users type the English phrase;
  - `wikipedia app` (G 10, B 8, GQ `wikipedia app gratis`; GAZ `heeft wikipedia een app`, `wikipedia app artikel offline`; the
    tails mix Apple-the-fruit and Apple-the-brand noise ("wikipedia appel")) as a supporting phrase for the app;
  - `leuke weetjes app` (G echo) and `interessante feitjes` (G 7: over jezelf, over nederland, geschiedenis).
- **Strength notes:** `wikipedia lezen`, `wikipedia swipen`, `nuttige feiten app` are empty or noise; `kennis app` (G 9) is
  government and education apps ("kennis app lvb", "npo kennis app"). `leerzame apps` (G 9) is toddler education. Not usable.
- **FAQ-style (from suggest):**
  - heeft wikipedia een app (GAZ)
  - wikipedia app gratis (GQ)
  - is er een wikipedia app voor iphone (G `wikipedia iphone`: tails are iPhone-the-device pages; nearest app question
    comes from GAZ `download wikipedia on iphone`, English as typed)
  - wikipedia app artikel offline (GAZ)
  - willekeurige wikipedia pagina (G, B)
  - random wikipedia artikel (G, B)
- **Notes:** the page needs "Wikipedia" in the title and H1 but not as a claim of affiliation (no logo or implied endorsement);
  language editions come from the blueprint (32).

## xiangqiful (/nl/apps/xiangqiful/): Chinese chess

- **Primary:** `chinees schaken` (G 7: spelregels, online, uitleg, bordspel, kopen, `wat is chinees schaken`; GQ `hoe werkt chinees schaken`;
  A 6: `chinees schaken leren`, `chinees schaken offline`, `chinees schaken: leer & speel`, `xiangqi - chinees schaken`,
  `xiangqi: chinees schaken`; GAZ `chinees schaken regels`).
- **Secondary:**
  - `xiangqi` (G 10, B 8, A 8; tails English: how to play, rules, vs chess, set): the technical name, also used in the App Store
    hints ("xiangqi - chinees schaken");
  - `chinees schaken spelregels` (G echo; `chinees schaken regels` GAZ);
  - `chinees schaken leren` (A echo; G empty);
  - `xiangqi app` (G 7, B 2; GAZ `xiangqi app store`, `best xiangqi app`).
  Also `chinees schaakspel` (G 4, B 1: koffer, kopen, antiek: that is the physical board), `xiangqi online` (G 10, B 8).
- **Strength notes:** `chinees schaak app`, `chinees schaken app`, `xiangqi leren`, `xiangqi uitleg`, `xiangqi spelen` are empty; B for
  "chinees schaken" returns place-name noise (Schagen, Schalkwijk, "chinese schalen"). The physical-game tails (kopen, koffer,
  bordspel) are a different intent. `chinees schaken tegen computer` is empty (Bing returns Western chess).
- **FAQ-style (from suggest):**
  - wat is chinees schaken (GQ)
  - hoe werkt chinees schaken (GQ)
  - chinees schaken spelregels (G)
  - chinees schaken uitleg (G)
  - chinees schaken online (G)
  - xiangqi how to play (G, English as typed)
  - xiangqi vs chess (G, English as typed)
- **Notes:** Xiangqi and Shogi split: this page owns `chinees schaken`, Shogiful owns `shogi app`/`japans schaken`; each page
  links to the other and to Chessful for plain chess. Do not use `schaak app` (Chessful).

## clippet (/nl/apps/clippet/): clipboard history for iPhone, iPad and Mac (unreleased, pages unlisted)

Do not index or push the page live; the keywords are recorded for the launch.

- **Primary:** `klembord geschiedenis` (G 10: windows, android, macbook, iphone, terughalen, openen, samsung; B 8: openen, windows,
  bekijken, inschakelen, sneltoets, terughalen). Platform tails fit: `klembord geschiedenis iphone` (G), `klembord geschiedenis
  macbook` (G), `klembord geschiedenis bekijken` (G, B).
- **Secondary:**
  - `klembord iphone` (G 10: openen, wissen, bekijken, terughalen; GQ `hoe zie ik mijn klembord iphone`, `wat is klembord iphone`,
    `waar kan ik klembord vinden op iphone`);
  - `clipboard manager mac` (G 10: free, macos, maccy, open source, tahoe; B echo; GAZ `best clipboard manager mac`): typed in English;
  - `kopieer geschiedenis` (G 9: windows, macbook, iphone, mac, bekijken; B 3), plus `klembord manager` (G echo; A "Clipbox: klembord
    manager").
  Also `universeel klembord` (G 3: apple, werkt niet): Apple's Universal Clipboard, a possible comparison hook.
- **Strength notes:** `clipboard manager iphone` (G 6: free, shortcut, best) is English. `klembord manager iphone`, `kopieerlijst iphone`,
  `klembord mac` as a plain seed returns "macrame"/"makro" Bing noise but G has `klembord macbook` (9 tails). `klembordgeschiedenis`
  as one word appears in G (`klembordgeschiedenis mac`, `klembordgeschiedenis apple`) but searchers mostly type two words.
- **FAQ-style (from suggest):**
  - hoe zie ik mijn klembord iphone (GQ)
  - waar kan ik klembord vinden op iphone (GQ)
  - wat is klembord iphone (GQ)
  - klembord geschiedenis terughalen (G, B)
  - klembord geschiedenis bekijken (G, B)
  - klembord geschiedenis openen (G, B)
  - universeel klembord werkt niet (G)
- **Notes:** the Netherlands sees "klembord" for both iOS (Apple's own Dutch UI term: "Klembord") and Windows. The page
  should state which platform it covers (iPhone, iPad and Mac). Keep the English "clipboard manager" in the FAQ as the Mac developer
  audience types it. Check Apple's term for "Universal Clipboard" in `nl-apple-terms.md` (not read in this pass).

---

## Summary table

| page | primary | secondaries |
|---|---|---|
| millrace | logische puzzel app | getallenspel; puzzel app zonder reclame; rekenpuzzel |
| tare | beste puzzelgames iphone | denkspelletjes app; breinbreker; hersen spelletjes app |
| mockly | app store screenshots | app store screenshot generator; app store screenshot sizes; mockup app store |
| observa | hrv apple watch | hartslagvariabiliteit apple watch; slaapscore apple watch; readiness score apple watch |
| pawza | vaccinatieboekje hond | vaccinaties kat; dierenpaspoort; huisdieren app |
| rightsplit | rekening splitsen app | kosten delen app; tikkie alternatief; bonnetje splitsen |
| shogiful | shogi app | japans schaken; shogi regels / shogi spelregels; shogi online |
| soon | aftel app | countdown app; countdown widget iphone; aftellen naar vakantie |
| taskful-day | to do lijst app | dagplanner app; takenlijst app; to do lijst iphone |
| wanderwiki | willekeurige wikipedia pagina | random wikipedia; wikipedia app; leuke weetjes app |
| xiangqiful | chinees schaken | xiangqi; chinees schaken spelregels; xiangqi app |
| clippet | klembord geschiedenis | klembord iphone; clipboard manager mac; kopieer geschiedenis |
