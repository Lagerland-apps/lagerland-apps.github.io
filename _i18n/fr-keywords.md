# Keyword research, French (France)

Part of the language sheet `_i18n/fr.md`. Two research passes on 2026-11-07 (part 1: studio pages and eight apps; part 2: the other thirteen apps). Search Console findings for France are summarized in the sheet.

## Part 1: studio pages, aftershift to liftlog

Pages: Home, Apps hub, About, Support hub, Transparency, and the app pages aftershift, allpaid, appmeta,
appmeta-pulse, chessful, earnlock, gymlogger-x, liftlog. Format follows `_i18n/de-keywords.md`.

Collected 2026-11-07. Source marks: **G** = Google suggest (hl=fr, gl=fr), **B** = Bing autosuggest (mkt=fr-FR),
**A** = App Store search hints (storefront 143442-3,29, France/French), **S** = iTunes Search API (country=fr),
used only for competitor names and the vocabulary in French app titles. Every query below was returned by one of
these sources; nothing was invented. Accents: Google often returns the unaccented form ("dormir apres travail de
nuit", "carnet d entrainement"); I write the accented form where the accented form was also returned or the
difference is only the accent, and mark the source anyway. Search Console data is not included.

## Method note

- **Requests: 496**, about 0.8 s apart. First run 443 (G 198, B 130, A 115), then 29 extra A hints (single
  words) and 24 S searches.
- **Google suggest: worked.** Alphabet suffixes (a b c d e f g h i l m o p r s t v) on 4 seeds only:
  application musculation, application échecs, travail posté sommeil, application rappel factures.
  Useful for musculation and échecs; "travail posté sommeil" yielded only a few extras; "application rappel
  factures" yielded nothing at all.
- **Bing (osjson, fr-FR): worked.** Noisy: it mixes in English, loosely related queries and generic
  "comment ..." questions, and returns nothing for many long seeds.
- **App Store hints (MZSearchHints, French header): worked** for single words and short seeds (sommeil, factures,
  échecs, musculation, temps d'écran, bloqueur, rappel factures), empty for most 3+ word seeds and for
  "travail de nuit", "apprendre échecs", "entraînement"-style combos. Hints for "pas" are useless (pass culture etc.).
- **iTunes Search API (country=fr): worked** for competitor names (24 searches). The French title style is
  "Name: Keyword & Keyword" or "Name - Keyword".
- **People also ask: not collected.** It needs a live Google results page; scripted fetches hit a consent wall
  and CAPTCHA, which I did not try to get around. FAQ items come from question-style suggest ("comment",
  "quelle", "meilleure", "c'est quoi") on G and B.
- **Weak spots:** French suggest returns nothing for the privacy/studio themes (Home, About, Transparency),
  nothing for "application rappel factures" / "appli rappel factures" / "rappel facture application" on G and B,
  and nothing for "sdk de suivi", "quelles applications me pistent", "applications qui ne pistent pas",
  "apps sans trackers", "studio d'applications indépendant", "développeur app indépendant finlande",
  "suivi entraînement musculation", "chronomètre repos musculation". For those pages the pick is the closest
  real phrase and it is said so.
- **Appli vs application:** both are typed. "application X" is the more common form in suggest (and the form
  Apple uses); "appli X" appears in parallel on G ("appli échecs", "appli musculation maison", "appli sans pub")
  and "app" mostly shows up as an English-style tail ("app fitness", "carnet de musculation app"). Recommend
  "application" in titles and H1, "appli" in body copy and FAQ.
- **Good sign:** our own French App Store listings already show in S: "AfterShift: Sommeil & Travail" and
  "Chessful: Entraîne & Analyse".

---

## Home (/fr/): studio of privacy-first Apple apps

- **Primary:** `application sans publicité` (G). Also `applis sans pub` (G) and `application sans pub iphone` (G).
  Caution: the demand is dominated by YouTube and music ("application youtube sans pub", "appli musique sans pub").
  It is still the real French phrase for "no ads".
- **Secondary:** `appli sans pub` (G); `application sans pub iphone` (G); `application sans compte` (G; weak,
  mostly means "without a Google/Apple account" for installing apps, which is a related audience).
- **Not usable as primary:** `application sans abonnement` (G): real demand (G "application gratuite sans
  abonnement", "application sport sans abonnement") but the house rule limits "sans abonnement" to LiftLog,
  Millrace, Mockly and Tare.
- **FAQ-style (from suggest):** none on-topic came back. "applications respectueuses de la vie privée" returned
  only "respect de la vie privée ..." legal queries (B). Nearest: `suppression pub sur iphone` (B).
- **Notes:** "apps sans tracking", "applis iphone sans tracking", "application sans publicité ni suivi" and
  "éditeur d'applications indépendant" returned nothing useful (G gave GPS queries for "tracking"). French
  speakers say "sans pub" / "sans publicité"; "suivi" is the word for tracking in Apple's French UI, but
  consumers rarely type it for apps. App Store title vocabulary for privacy: "Vie privée" ("HUSH : Anti-pub &
  vie privée", "Anti-piratage & vie privée", "vault: gardien de vie privée") (A, S). "Privacy" in English is
  not a consumer query.

## Apps hub (/fr/apps/): all apps

- **Primary:** `meilleures applications iphone` (G, B). Generic but it is the real phrase; pair it with the
  studio angle in the title. `meilleures applis iphone` (G) is the casual twin.
- **Secondary:** `applications utiles iphone` (G, B "iphone applications utiles"); `application sans pub iphone`
  (G); `meilleures applications mac` (G, B).
- **FAQ-style:**
  - meilleur application iphone gratuite (G)
  - application iphone utile gratuite (G)
  - applications utiles apple watch (G)
  - application ipad utile (G)
- **Notes:** G mixes in English ("best apps iphone", "top apps iphone", "best apps iphone 17") and years
  ("top jeux iphone 2025", "best apps iphone 2026"); avoid dated titles. "meilleure/meilleur" is often typed
  with the wrong agreement ("meilleur application iphone gratuite", "meilleur appli mac"); use the correct
  "meilleures". "applications iphone sans abonnement" was not tried as primary (house rule).

## About (/fr/lagerland-apps/): one-person studio, Finland

- **Primary:** no real query found. Closest real phrases: `développeur d'applications` (G, B; job-search
  intent: salaire, mobiles, web) and `developpeur app freelance` (G). Recommendation: title on the brand
  ("Lagerland Apps") plus "développeur indépendant" / "studio indépendant" in the description; this page ranks
  on brand, not on generic demand.
- **Secondary:** `développeur d'applications` (G, B); `developpeur ios freelance` (G).
- **FAQ-style:** none on-topic. G/B for "développeur d'applications" are salary and tech-stack questions.
- **Notes:** "développeur app indépendant finlande", "studio d'applications indépendant" returned nothing.
  "indépendant" yields "freelance" in French suggest, which is a different intent (a contractor for hire), so
  avoid "freelance" in copy. French people type "développeur" (also unaccented "developpeur") and
  "créateur d'application mobile" (G) for makers. "Indie" is not a French consumer term; use "indépendant".

## Support hub (/fr/support/)

- **Primary:** `annuler abonnement iphone` (G, B). Strongest support-type demand; fits the hub.
- **Secondary:** `annuler abonnement application iphone` (G); `restaurer achats apple` (G) /
  `restaurer achat iphone` (G, singular); `se faire rembourser application apple` (G).
- **FAQ-style:**
  - comment annuler un abonnement apple (G, B)
  - comment annuler un abonnement sur iphone (B)
  - comment résilier un abonnement sur iphone (B)
  - comment supprimer un abonnement sur iphone (B)
  - ou voir les abonnements iphone (G) / ou trouver mes abonnements apple (G)
  - comment se faire rembourser application iphone (G)
  - annuler abonnement app store iphone (G)
- **Notes:** French uses "annuler" (G) and "résilier" (B) for subscriptions, "abonnement" never
  "subscription". For restore, G returns the singular "restaurer achat iphone" while Apple's UI says
  "Restaurer les achats"; the question seed "comment restaurer achats application" returned nothing on G
  and unrelated "restaurer applications supprimées" on B. "contacter support application" returned nothing
  usable. "remboursement" (refund) is a clear sub-topic: "se faire rembourser achat app store" (G), "apple
  remboursement achat intégré" (B).

## Transparency (/fr/transparency/): tracking, SDKs, privacy manifests

- **Primary:** `app tracking transparency` (G, B). French searchers use the English Apple term; no French
  consumer phrasing has demand. French-language fallback: `suivi des applications iphone` (G).
- **Secondary:** `suivi des applications iphone` (G); `privacy manifest` (G, B; English, developer audience);
  `comment activer le suivi des applications sur iphone` (G).
- **FAQ-style:**
  - comment activer le suivi des applications sur iphone (G)
  - c'est quoi un tracking (B)
  - what is app tracking transparency (B; English even with a French seed)
  - app tracking transparency europe (G)
  - app tracking transparency meaning (G)
- **Notes:** "transparence du suivi des apps" gave only English ATT results on B and nothing on G.
  "désactiver suivi applications iphone" gave nothing on G and "désactiver un iphone" noise on B.
  "sdk de suivi", "quelles applications me pistent", "applications qui ne pistent pas", "apps sans trackers",
  "c'est quoi un privacy manifest" returned nothing useful. Developer terms stay English: "privacy manifest",
  "SDK", "App Tracking Transparency" (B shows "itms-91061 missing privacy manifest"). Apple's French UI says
  "Suivi" / "Autoriser les demandes de suivi des apps"; use that for the consumer-facing text.

---

## AfterShift (shift-work sleep)

- **Primary:** `travail de nuit sommeil` (G). The "travail posté" form also has demand: `travail posté sommeil`
  (G, B "sommeil et travail posté"). Write "travail posté et de nuit" in the title area.
- **Secondary:** `travail posté sommeil` (G, B); `dormir après travail de nuit` (G); `application suivi sommeil
  iphone` (G); `dette de sommeil` (G, B; A hints "dette de sommeil: suivi", "dette de sommeil: calculateur").
- **FAQ-style:**
  - dette de sommeil comment récupérer (G)
  - bien dormir apres une nuit de travail (G)
  - travail de nuit sommeil perturbé (G)
  - travail de nuit sommeil et alimentation (G)
  - travail de nuit conseil sommeil (G)
  - combien de temps de sommeil par nuit (B)
- **Competitors (S/A):** Peaks: Sommeil & Énergie, Rested : Sommeil & Énergie, Lueur: Sommeil posté,
  Shiftrest: Sommeil & Quarts, Gestion du sommeil en horaires, SleepShift AI, Timeshifter Shift Work,
  Rythme Circadien - Dawn. Roster apps (different intent): Vessa : Planning de travail, ShiftKal, ShiftDeck,
  Shifter – planning de travail, Shiftbase (A). Our listing: "AfterShift: Sommeil & Travail".
- **Notes:** "application sommeil travail de nuit", "application horaires de travail sommeil",
  "sommeil travail de nuit conseils" and "rythme de sommeil travail posté" returned nothing on G, only
  generic sleep queries on B. G gives "application travail de nuit" and "application planning travail posté"
  (roster intent). French words: "travail posté", "travail de nuit", "travailleur de nuit", "sommeil",
  "dette de sommeil", "rythme de sommeil". "sieste" is typed ("application sieste", G, but for babies).
  "Shift" survives in English only in roster app names; consumers do not type it.

## AllPaid (bill reminders, no bank login)

- **Primary:** `rappel factures` (A hints for the seed: "rappel factures: abonnements", "billwise: rappel
  factures", "pense à payer: rappel factures"; also the exact title wording of 5+ competitors in S). G and B
  return nothing for it, so the demand evidence is thin; it is the vocabulary competitors use.
- **Secondary:** `application rappel paiement` (G); `application calendrier paiement` (G);
  `app suivi abonnements` (G); `application gestion factures` (G; but see notes).
- **FAQ-style:** none for reminders. Closest real phrases: `appli gestion budget sans compte bancaire`
  (G), `application gestion budget sans banque` (G), `application gestion des factures` (G).
- **Competitors (S/A):** Rappel Factures: Abonnements, Pense à payer: Rappel Factures, Billwise: Rappel Factures,
  Rappel de Factures - BillSnap, Rappel de factures : DueMinder, Rappel de Factures: Billo, Factures: rappel
  échéances, Lumori: Factures & Rappels, Teiki: Factures & Abonnements, Sincap: Échéances & Factures,
  Abonnement & Facture: Subtrack, Aheado: Rappels & Échéances; A: "duetick : rappel abonnements".
- **Notes:** "facture" is double: a bill you receive and an invoice you issue. Suggest for "application gestion
  factures" / "application suivi des factures" is dominated by invoicing software (devis, factures
  fournisseurs) and B for "application factures sans connexion bancaire" is all invoice-making. Use
  "rappel factures", "échéances", "paiement", "abonnements" and "contrats" to keep the bill-reminder intent.
  "sans connexion bancaire" / "sans compte bancaire" does have a G echo (`appli gestion budget sans compte
  bancaire`). "application rappel factures" and "appli rappel factures" returned nothing.

## AppMeta (App Store Connect for Mac)

- **Primary:** `app store connect mac app` (G). Also `app store connect macos` (G).
- **Secondary:** `mots clés app store` (G); `metadata app store` (G; the English "metadata", unaccented, not
  "métadonnées"); `aso app store` (G, B).
- **FAQ-style:** `c'est quoi app store connect` (G); `what is app store connect` (B); `qu'est ce que
  l'app store` (B; consumer noise).
- **Competitors (S/A):** Helm pour App Store Connect, AppDab for App Store Connect, Appdesk pour App Store
  Connect, Peek for App Store Connect, ShipCue for App Store Connect (all A), Store Connect Studio,
  ASO Keyword Optimizer PutKey, Traducteur de métadonnées (S), plus Apple's own App Store Connect and TestFlight.
- **Notes:** French developers search in English: "app store connect", "aso", "metadata", "keywords"
  ("app store optimization keywords" G). "mots clés app store" is the one French form with G demand.
  "optimiser fiche app store", "éditeur app store connect" returned nothing useful.

## AppMeta Pulse (App Store Connect dashboard on iPhone)

- **Primary:** `app store connect iphone` (G).
- **Secondary:** `app store connect ios` (G); `app store connect api` (G, B); `app store connect application`
  (G).
- **FAQ-style:** `c'est quoi app store connect` (G); `app store connect login` (G, B).
- **Competitors (S/A):** Proceeds — Ventes App Store, AppDab for App Store Connect, Helm, Appdesk, Peek,
  ShipCue (A), Stripe Dashboard.
- **Notes:** French seeds "suivi ventes app store", "revenus app store développeur", "statistiques app store
  connect", "mrr abonnements application" return nothing relevant on G (B: generic sales tracking, "app store app
  revenue"). "MRR", "App Store Connect", "proceeds" stay English; the audience is developers. The title could
  use "ventes App Store" (title vocabulary of the one S competitor), but that has no suggest demand.

## Chessful (chess learning and analysis)

- **Primary:** `application échecs` (G, B). Casual twin `appli échecs` (G, B).
- **Secondary:** `apprendre les échecs application` (G); `analyse de parties d'échecs` (G, B);
  `meilleure application pour apprendre les echecs` (G); `application apprendre echecs` (G).
- **FAQ-style:**
  - quelle application pour apprendre les echecs (G)
  - meilleure appli échecs gratuit (G)
  - meilleure application échecs iphone (G)
  - analyser ses parties d'échecs (G)
  - comment progresser aux échecs (G)
  - comment apprendre les échecs seul (G) / comment étudier seul les échecs (G)
  - application échecs hors ligne (G)
- **Competitors (S/A):** Échecs - Jouer et apprendre, Échecs sans pub, Échecs : Analyse Stockfish,
  Analyse Échecs: Chess AI, MoveSense: Analyse Échecs, Chessigma, ChessFlare, Magnus Trainer: Apprends échecs,
  Theoria - Ouvertures d'échecs, Chessy : Coach d'Échecs IA, Lotus Chess – Coach, Problèmes d'Echecs (puzzles);
  A: Chess.com, Chessable, Reti: puzzles d'échecs, WeeChess - puzzles d'échecs, "échecs : coach d'ouvertures",
  "gym échecs: tactiques puzzles". Our listing: "Chessful: Entraîne & Analyse".
- **Notes:** "échecs" (plural, never "échec" for the game; B shows "application échec" as a variant) is the
  word; "jeu d'échecs". "Stockfish" is typed as-is (`stockfish application` G, B; `logiciel d échecs
  stockfish` G). "logiciel" competes with "application" for desktop intent. English leaks in G: "chess app
  ...", "app chess". "puzzles" is used in French ("puzzles d'échecs", G, A), not "problèmes" alone. "Elo" is
  typed ("application echecs elo", G). Strong audiences: "enfants" (many suggests), "débutant", "gratuit",
  "hors ligne", "sans pub".

## EarnLock (earn screen time by moving: app blocker)

- **Primary:** `bloqueur d'applications` (G, A hints list 6 apps with that title phrase, S).
- **Secondary:** `bloquer applications iphone` (G, B); `limiter temps d'écran` (G, B, A); `application pour
  réduire le temps d'écran` (B); `application pas quotidien` (G).
- **FAQ-style:**
  - comment réduire son temps d'écran (G, B)
  - comment limiter son temps d'écran (G)
  - réduire temps d'écran iphone (G)
  - application anti addiction telephone (G) / application contre addiction smartphone (G)
  - bloquer application iphone avec code (G)
- **Competitors (S/A):** Opal: Temps d'écran et Focus, one sec–temps d'écran & focus, Jomo - Meilleur temps
  d'écran, ScreenZen, Limit: temps d'écran focus, Blockrr – Temps d'Écran, Stay Focused - Bloqueur d'apps,
  RepLock : Bloqueur d'apps, Scrollr - Bloqueur d'apps, AppBlock: bloquer des applis, BlockIt - Pompes Temps
  d'écran, Walkgate : Marche & Débloque, Social Steps: Temps d'écran, Barake - temps d'écran gagné,
  Detox: Temps d'écran, Blob/Forge/Setl/Odak/Tenki (A: "bloqueur d'applications").
- **Notes:** "temps d'écran" is Apple's French name for Screen Time and the big keyword; most G suggests for it
  are about removing the limit or the code ("supprimer temps d'écran sans code"), parental control, and
  Samsung/Android. French App Store titles use "Temps d'écran" + "Focus" (English kept) and "bloqueur
  d'apps/applications". "marcher pour débloquer applications", "application pas quotidiens" (as a plural) gave
  nothing; "pas" alone in A hints is Pass culture etc. The earn-by-walking mechanic has almost no French query
  demand; S shows only two apps (Walkgate, Social Steps). "Verrouillage d'applications" (G) is the lock
  synonym.

## GymLogger X (strength workout tracker with Apple Watch)

- **Primary:** `application musculation apple watch` (G). If the page should lead on the generic head term:
  `carnet de musculation application` (G; A hint "carnet de musculation").
- **Secondary:** `carnet de musculation application` (G); `application musculation iphone` (B; G
  "application musculation gratuite iphone"); `programme musculation application` (G);
  `application suivi seance musculation` (G).
- **FAQ-style:**
  - meilleur application musculation apple watch (G)
  - meilleure application musculation iphone (G)
  - comment organiser ses séances de musculation (G, B)
  - comment répartir ses séances de musculation (G)
  - application musculation gratuite avis (G)
  - application programme musculation en salle (G)
- **Competitors (S/A):** Hevy Carnet de Musculation Gym, GymBook: Carnet de musculation, Lyfta : Carnet de
  musculation, Epilog : Carnet de Musculation, SeeGym : Carnet de Musculation, Carnet de Musculation RepCount,
  Alpha Progression Musculation, Gravl : Coach Personnel IA, FizzUp - Fitness & Musculation, Gym Day, Strong
  Workout Tracker Gym Log, Fitbod Workout & Gym Planner, Heft - Carnet d'Entraînement, Fitness Park App;
  A: "musculation: gravl", "gymshark", "gym rank".
- **Notes:** French uses "musculation" (also "muscu": A "carnet muscu", S "Carnet Muscu"), "carnet de
  musculation" for the log (very strong in S titles), "séance", "salle", "programme", "haltères", "poids du
  corps". "Apple Watch" stays English and is typed. "fitness" is used interchangeably with "musculation"
  ("application fitness apple watch" G). "Workout tracker" / "gym log" survive only in English titles.
  Caution: "carnet d'entraînement musculation" (G, B) is dominated by school PDFs (EPS, bac, lycée).

## LiftLog (lifting log, one purchase, no subscription)

- **Primary:** `application musculation sans abonnement` (G). "Sans abonnement" is allowed for LiftLog.
- **Secondary:** `application musculation gratuite sans abonnement` (G); `application fitness sans abonnement`
  (G); `application suivi musculation gratuite` (G).
- **FAQ-style:**
  - meilleure application musculation gratuite (G, B)
  - application musculation gratuite avis (G)
  - application de musculation gratuite (G, B)
  - meilleur application programme musculation (B)
- **Competitors (S/A):** Hevy Carnet de Musculation Gym, Strong Workout Tracker Gym Log, Liftoff: Heavy Workout
  Planner, Lift: Workout Tracker Gym Log, Gym Log: Free Workout Tracker, GymLog AI: Carnet Musculation,
  Journal Musculation - Swol, Basalt Lab: Carnet Musculation, SetGrip: Carnet de Musculation, StrengthLog,
  Alpha Progression Musculation, Metric – Musculation; A: Liftosaur, Liftoff.
- **Notes:** "achat unique" and "sans pub" variants returned nothing (`application musculation achat unique`:
  G empty, B drifted to gym equipment; `application musculation sans pub`: G empty). The "gratuite" demand is
  large and contradicts a paid-once offer: say "essai gratuit de 7 jours" only as far as the master file
  allows, and use "sans abonnement" as the differentiator. "Journal" appears in a few titles, "carnet" is
  the dominant word. Stay clear of "paiement unique" as a keyword: no suggest evidence.

---

## Summary table

| Page | Primary | Secondary 1 | Secondary 2 |
|---|---|---|---|
| Home | application sans publicité (G) | appli sans pub (G) | application sans pub iphone (G) |
| Apps hub | meilleures applications iphone (G, B) | applications utiles iphone (G, B) | application sans pub iphone (G) |
| About | brand "Lagerland Apps" (no real query; closest: développeur d'applications, G, B) | développeur d'applications (G, B) | developpeur ios freelance (G) |
| Support hub | annuler abonnement iphone (G, B) | restaurer achats apple (G) | se faire rembourser application apple (G) |
| Transparency | app tracking transparency (G, B) | suivi des applications iphone (G) | privacy manifest (G, B) |
| aftershift | travail de nuit sommeil (G) | travail posté sommeil (G, B) | dormir après travail de nuit (G) |
| allpaid | rappel factures (A, S titles) | application rappel paiement (G) | app suivi abonnements (G) |
| appmeta | app store connect mac app (G) | mots clés app store (G) | aso app store (G, B) |
| appmeta-pulse | app store connect iphone (G) | app store connect ios (G) | app store connect api (G, B) |
| chessful | application échecs (G, B) | apprendre les échecs application (G) | analyse de parties d'échecs (G, B) |
| earnlock | bloqueur d'applications (G, A) | bloquer applications iphone (G, B) | limiter temps d'écran (G, B, A) |
| gymlogger-x | application musculation apple watch (G) | carnet de musculation application (G) | programme musculation application (G) |
| liftlog | application musculation sans abonnement (G) | application musculation gratuite sans abonnement (G) | application fitness sans abonnement (G) |


## Part 2: mediakit to clippet

Tier 1 app pages: MediaKit, Millrace, Mockly, Observa, Pawza, RightSplit, Shogiful, Soon., Tare, Taskful Day,
WanderWiki, Xiangqiful, Clippet. Part of the language sheet `_i18n/fr.md` (format of `_i18n/de-keywords.md`).

Collected 2026-11-07. Source marks: **G** = Google suggest (hl=fr, gl=fr), **B** = Bing autosuggest (mkt=fr-FR),
**A** = App Store search hints (storefront 143442-3,29, France/French), **S** = App Store search results
(itunes.apple.com/search, country=fr), used only for competitor names and the vocabulary in their French titles.
Every query below was returned by one of these sources; nothing was invented. Accents are kept as the source
returned them: Google often returns the unaccented form (`casse tete`, `echecs chinois`) and the accented form as
separate suggestions, and people type both. Search Console data is not included (not part of this task).

## Method note

- **Google suggest: worked.** About 290 requests (seeds in three batches), 0.8 s apart. Alphabet suffixes (a to v,
  skipping rare letters) on 4 seeds only: `compte à rebours iphone`, `compresser vidéo iphone`,
  `jeu de logique iphone`, `échecs chinois`.
- **Bing autosuggest (mkt=fr-FR): worked.** Noisy. It drifts to unrelated or English phrases ("cassette iphone case",
  "application harvard" for "application hrv") and mixes in Windows, Microsoft and PC. Used mainly to confirm Google.
- **App Store search hints (France, French): worked** but returned nothing for most long seeds. Useful hits:
  `compte à rebours widget`, `compte à rebours mariage`, `shogi`, `échecs chinois`, `application to do list`,
  `partager l'addition`, `jeu de logique gratuit`, `compresser vidéo gratuit`, `presse papier iphone`.
- **iTunes Search API (country=fr): worked** (37 searches, 3 s apart) for competitor names and title vocabulary.
  Seller names are left out of the lists below on purpose.
- **People also ask: not collected.** It needs a live Google results page, which scripted fetches cannot get past
  (consent wall). I did not try to get around it. The FAQ lines come from question-style autocomplete
  ("comment", "quelle", "c'est quoi", "où est", "meilleur").
- **"application" vs "appli" vs "app":** `application` is what people type: "application compresser vidéo" (G, B),
  "application to do list" (G, B, A), "application compte à rebours" (G, B), "application carnet de santé
  animaux" (G), "application partage addition restaurant" (G), "application tricount" (G). The short forms
  appear second: `appli compte à rebours` (G, B), `appli compresser video` (G), `appli depenses partagés` (G),
  `app compresser video` (G), `app hrv` (G). `app` is rare except next to English words (`app hrv apple watch`).
  Use "application" in titles and H1; "appli" can appear once in the body.
- **Year/model variants** are common (`presse papier iphone 15`, `planificateur journalier 2026`); avoided per house
  style. Anything with "gratuit" is high volume on Google but only fits pages where a free tier is real
  (flagged below).
- **Nothing found at all** (returned empty on G, B and A): `app suivi hrv`, `hrv bon score`, `quand s'entraîner
  application`, `application pour diviser l'addition au restaurant`, `appli diviser addition`,
  `calculateur partage addition`, `tâches reportées application`, `échecs japonais application`,
  `xiangqi application`, `xiangqi débutant`, `échecs chinois application`, `échecs chinois iphone`,
  `jeu d'équilibre iphone`, `casse-tête balance`, `maquette iphone screenshot`, `wikipedia aléatoire application`,
  `widget écran verrouillé iphone compte à rebours`.
- **Misleading seeds to avoid:** `diviser addition` (arithmetic homework, "division addition multiplication"),
  `décompte iphone` (returns "facture iphone"), `jeu de balance` (crossword clue "jeu de balance 4 lettres"),
  `balance puzzle` (English, Silent Hill), `carnet de santé` alone (human health booklet, `mon carnet de santé`
  is the national service), `wikipedia swipe` (English), `hrv` alone for Honda HR-V ("application honda hrv").
- **Our own French listings already show up** in A/S: "Shogiful : échecs japonais" (A, S), "Xiangqiful : échecs
  chinois" (A, S), "Pawza: Carnet de Santé Animal" (S). These match the primaries chosen below.

---

## MediaKit (compress/convert video, images, PDF on device)

- **Primary:** `compresser vidéo iphone` (G, B). Variants people also type: `compresser video iphone` (G),
  `compresser une vidéo sur iphone` (B).
- **Secondary:** `compresser pdf iphone` (G, B); `convertir vidéo iphone en mp4` (G, B); `compresseur vidéo`
  (G, B, A; for the generic, non-iPhone head term). Also `application compresser vidéo` (G, B) and
  `logiciel compression video mac` (G) for the Mac side.
- **FAQ-style (from suggest):**
  - comment compresser une vidéo sur iphone (G, B)
  - comment réduire la taille d'une vidéo (B) / comment réduire une vidéo sur iphone (B)
  - compresser vidéo iphone pour envoyer par mail (G)
  - compresser vidéo sans perte de qualité (G, B)
  - convertir heic en jpg iphone (G, B) (HEIC is on the English page, so it can be answered)
  - peut on compresser une vidéo (B)
- **Competitors (S):** Compresseur vidéo - Rétrécir, Compress Videos & Resize Video, Compresser des vidéos,
  Compresser Vidéo · Réduire Mo, VideoSlimmer, Panda Video Compress & Convert, Compresseur Vidéo: VidFit,
  Video Compressor - Tinyfile, iLovePDF, Smallpdf, Documents (Readdle), PDF Expert; for conversion, "Convertisseur
  Vidéo: mp4 à mp3" style apps.
- **Notes:** French titles say "Compresser" or "Compresseur" + "Vidéo", often with "Réduire". "Gratuit" and
  "en ligne" trail almost every query (`compresser vidéo iphone en ligne gratuit`): searchers expect web tools, so
  the page must say it works on the device and uploads nothing. English terms kept: "mp4", "mov", "heic", "pdf",
  "mp3"; "video compressor / converter" appears only in app-store style queries (G). "Convertir" is the verb for
  format change, "compresser" (not "compacter") for size. Both "réduire la taille" and "compresser" are used; "alléger" appears in titles
  only. The queries are mostly one file type each, so the title should name video first, then PDF and photo.

## Millrace (tile-delivery logic puzzle; never write "2048")

- **Primary:** `jeu de logique iphone` (G); `jeux de logique ipad` (G). Head term `jeu de logique` is huge but
  dominated by kids' worksheets and web games ("jeu de logique cp", "à imprimer"); the iPhone form isolates app intent.
- **Secondary:** `jeu de logique sans pub` (G); `jeu de réflexion sans pub` (G); `jeux de logique app store` (G).
- **FAQ-style (from suggest):**
  - meilleur jeu de logique iphone (G)
  - meilleur jeu de logique ipad (G, as `meilleur jeux de logique ipad`)
  - quel est le meilleur jeu de réflexion (B: `le meilleur jeu de réflexion`)
  - quels sont les jeux de réflexion gratuits (B)
- **Competitors (S):** Impulse - Jeux de Réflexion, Jeux de logique - Énigmes, Easy Game - Jeux de logique,
  Nonogram.com - Jeu de logique, Arrow Puzzle: Jeu de réflexion, Brain Test: Casse-têtes, Sudoku.com - Casse-tête,
  Briques - Casse-tête logique, Water Sort Puzzle, Block Blast!. A hints: "cascade-jeu de logique",
  "happy queens : jeu de logique", "sudoku junior : jeu de logique".
- **Notes:** French titles use the pattern "Nom - Jeu de logique" or "Nom: Jeu de réflexion". "Sans pub" is the
  French search habit for ad-free (G has it for logique, réflexion and puzzle); the English page confirms Millrace
  has no ads, so "sans pub" is allowed. "Sans abonnement" is allowed for Millrace. "Jeu de tuiles" is a different
  market (mahjong/triple tile match, G empty, B "jeu de tuiles gratuit"), so do not lean on "tuiles" in the title.
  Do not target `jeu de logique gratuit` as the primary: the A hint exists, but the page is free with optional
  purchases, and the term is generic. `puzzle` is used for jigsaw intent in French ("puzzle gratuit sans
  téléchargement"), so prefer "jeu de logique" and "jeu de réflexion". "Casse-tête" is covered by Tare.
  Never write "2048" or seed it: no 2048 query was run.

## Mockly (App Store screenshots on Mac)

- **Primary:** `screenshot app store` (G, B). French searchers keep the English "screenshot" for this developer
  topic. The French `capture d'écran app store` returned only itself on G and, on B, Windows/Microsoft Store noise,
  so it carries almost no demand.
- **Secondary:** `app store screenshot maker` (G, B); `app store screenshot generator` (G, B); `mockup app store`
  (G). Optional: `mockup iphone gratuit` (G) is a broader, free-leaning query; do not use "gratuit" on this
  paid app.
- **FAQ-style (from suggest):** these are English/developer queries, no French question forms came back:
  - app store connect screenshots sizes (G, B)
  - app store mac screenshot size (G)
  - app store connect screenshots not uploading (G)
  - app to make app store screenshots (B)
- **Competitors (S):** Screenshot Studio : captures, Mockup & Démo : Screeny, Yada Studio : Captures d'écran,
  App Screenshots Maker, Screenshot Bro: Mockup Maker, App Screenshots: Store Maker, StoreShots, Aura Screenshot ·
  Maquettes IA, Store Connect Studio, Picasso App Screenshot Studio, Mockup Screenshot. On the web: Canva and
  Figma templates (G suggests `app store screenshot generator canva`, `... figma`).
- **Notes:** Searchers are developers and designers who type English: "screenshot", "mockup", "template",
  "generator", "maker", "app store connect". French copy should keep "screenshots" (and "mockup") in the title and
  use "captures d'écran" in the body. "Maquette" is the French word but the queries use "mockup". Hardly any
  French queries mention Mac. "Sans abonnement" is allowed for Mockly (one-time purchase).

## Observa (sleep, HRV, recovery from Apple Health; HRV is SDNN)

- **Primary:** `hrv apple watch` (G, B). French people write "HRV" in Latin letters; the French term "VFC"
  (variabilité de la fréquence cardiaque) is used in app titles and medical queries. The French-form primary if
  the title should avoid the English-looking mix is `application hrv` (G).
- **Secondary:** `variabilité de la fréquence cardiaque` (G, B); `application sommeil apple watch` (G);
  `application hrv` (G; also `app hrv apple watch` G).
- **FAQ-style (from suggest):**
  - hrv c'est quoi (G, B)
  - c'est quoi la variabilité cardiaque (G) / variabilité fréquence cardiaque c'est quoi (G)
  - variabilité de la fréquence cardiaque normale (G, B)
  - variabilité de la fréquence cardiaque basse (G)
  - suivi du sommeil apple watch (G, B)
  - application sommeil apple watch fiable (G)
  - score de sommeil apple watch (B)
  - récupération cardiaque apple watch (B)
- **Competitors (S):** Elite HRV, Kubios HRV - Daily Readiness, HRV4Training, Welltory: Battement du coeur,
  StressWatch : Moniteur VFC IA, Heartify: Ma Santé Cardiaque, Hearty : Cardio & VFC, HRV Tracker for Watch,
  Emuqu: Variabilité cardiaque, VFC & Fréquence Cardiaque, Bevel : Coach Santé IA, RISE: Tracker Sommeil & Réveil,
  Sleep Cycle - Suivi de Sommeil, Withings, Pillow. Stress/VFC apps dominate the French "hrv" results.
- **Notes:** French keeps "HRV" (G: `hrv c'est quoi`, `hrv garmin c'est quoi`), uses "VFC" mostly in app titles
  ("Moniteur VFC", "Suivi stress et VFC"), and translates "heart rate" and "sleep" fully (`fréquence cardiaque`,
  `suivi du sommeil`, `apple santé`). Do not write "RMSSD"; HRV in Observa is SDNN, so "VFC (SDNN)" is the
  accurate wording. Google also surfaces `cohérence cardiaque` (breathing technique) next to HRV; do not conflate
  it. "Readiness" and "recovery" have no French query equivalents: `score de récupération apple watch` (G) is the
  nearest, with `récupération` also pulling photo-recovery apps (S), so use "récupération" with "sport" or
  "entraînement". `application sommeil apple watch` and `suivi du sommeil` also draw sleep-apnea queries
  (B: "apnée du sommeil apple watch"), which Observa does not diagnose.

## Pawza (pet health records, vaccines, vet documents)

- **Primary:** `application carnet de santé animaux` (G). The product word is "carnet de santé", the national
  habit for the booklet; Pawza's own French listing is "Pawza: Carnet de Santé Animal" (S).
- **Secondary:** `application carnet de santé chien` (G); `carnet de vaccination chat` (G, B);
  `application santé animale` (G). Also `application vétérinaire` (G, B; weaker, leans to vet clinics).
- **FAQ-style (from suggest):**
  - carnet de santé chien gratuit (B) / carnet de santé chat gratuit (G: `carnet de santé chat pdf gratuit`)
  - carnet de vaccination chat pdf (G) / carnet de vaccination chien pdf (G)
  - carnet de santé chat perdu (G); carnet de vaccination chien perdu (G)
  - carnet de santé chien à imprimer (B)
  - rappel vaccin chien 1 an (B)
  - délai rappel vaccin chat (B)
  - carnet de vaccination en ligne (B)
- **Competitors (S):** Mon Compagnon : Soins Animaux, Medika - Carnet de santé, Carnet de Santé Animal - Dana,
  Galia - Carnet de Santé Animal, Pidoy, Pilou, Kyto, AnimalCare : Carnet Santé, Pattes, Patounes, Wagly, Petivet,
  Animoo, PetNote Family, Faunio, Animorix : carnet chien & chat, Neli – Carnet santé chien chat, PokiPaw, PawCare :
  Rappels Chien Chat. Crowded category with many small French apps.
- **Notes:** People search for the paper/PDF booklet far more than an app (`à imprimer`, `pdf`, `gratuit`,
  `perdu`), so the page needs a line that answers "carnet" in the app sense. The French title pattern is
  "Nom : Carnet de santé animal". Vocabulary: "animaux" is plural in queries (`santé animaux`), "chien/chat" are
  used by species, "vaccin" and "vaccination" both appear (`carnet de vaccination` for the document, `rappel
  vaccin` for the reminder). The English-only angles ("vet documents", "scan") returned nothing in French. No
  English terms kept ("pet" is never used). Pawza's page also covers rabbits, birds, reptiles and horses; no
  query for those came back, so leave species out of the title.

## RightSplit (split restaurant bills from a receipt photo)

- **Primary:** `partager l'addition` (G, A). Also `application partage addition` (G).
- **Secondary:** `application partage addition restaurant` (G); `partager l'addition entre amis` (G);
  `partager l'addition au restaurant` (G).
- **FAQ-style (from suggest):** French suggest returns few questions for this; closest real phrases:
  - partager l'addition au restaurant (G)
  - partager l'addition entre amis (G)
  - partager l'addition uber eats (G)
  - application tricount c'est quoi (G)
  - application dépenses partagées (G) / application budget partagé (G)
- **Competitors (S):** Billy - Partagez l'addition, Partage Addition & Pourboire, Partager Addition Pourboire,
  Partager l'addition au resto, FoodFair - Partage Addition, TallySplit: Partage d'addition, SplitSlip : partage
  d'addition, Splitty : Partager l'addition, TabCut — Partagez l'Addition, SplitPal - Partage de frais, Spliit,
  Splitou IA, Divide Bill – Partage & scan, Tricount (G: `application tricount`, `tricount alternative`),
  Splitwise (G: `splitwise alternative`). A hints: "partager l'addition : dépenses", "paylash: partager l'addition",
  "splity: partager l'addition", "tiko: partager l'addition".
- **Notes:** The verb is "partager" (not "diviser"): `diviser addition` is arithmetic homework, and
  `diviser l'addition en anglais` is a language query. Both "partage d'addition" and "partager l'addition" appear
  in titles. Noun forms: "partage de frais" and "dépenses partagées" for group expenses (Tricount-type, a
  different intent). "Tricount" is the French brand shorthand for this need. "Resto" appears in app titles
  ("au resto"). "Pourboire" (tip) pairs with the bill split in titles. "Ticket" without "restaurant" is a
  receipt (`scanner ticket partage` pulls budgeting scanners); `ticket restaurant` is the meal voucher, an
  unrelated intent, so do not use "ticket restaurant". Use "addition" (the bill at a French restaurant) and
  "reçu" or "ticket de caisse" only in the body. "Appli" is typed as often as "application" here (`appli
  partage addition restaurant` → G rewrites to `application partage addition restaurant`).

## Shogiful (shogi / Japanese chess)

- **Primary:** `shogi` (G, B, A). The French listing is already "Shogiful : échecs japonais" (A, S). Pair it with
  the descriptor in the title.
- **Secondary:** `échecs japonais` (G, B, A); `apprendre le shogi` (G, B); `jeu de shogi` (G, B).
- **FAQ-style (from suggest):**
  - comment jouer au shogi (B: `comment jouer au shogi`; G: `apprendre a jouer au shogi`)
  - shogi règles (G, B) / shogi règles de base (B)
  - échecs japonais regles (G)
  - shogi pièces (G, B)
  - shogi en ligne (G, B)
  - shogi échecs japonais (G)
  - shogi débutant (G)
- **Competitors (S/A):** Shogi ™, Dr. Shogi, Shogi Lv.100 Entry Edition, PiyoShogi, Shogi Castle: Japanese Chess,
  Maître du Shogi Classique, M.SHOGI, Everybody Shogi, Shogi Master, Shogi365 : Tsume Shogi, Shogi Deluxe,
  Shogi Live, Shogi Lite, Shogi Demon, Chess.com (Échecs - Jouer et apprendre). Shogi apps are few in France.
- **Notes:** Searchers use both "shogi" and "échecs japonais" (G returns "shogi échecs japonais"). "Jeu de
  shogi" often means the physical board (`jeu de shogi en bois`). Naruto/anime queries pollute the "échecs
  japonais" family (`échec japonais naruto`, `shogi naruto`); the page should be about rules and play. No query
  with "application" returned for shogi in French: `shogi application iphone` gave only English `best shogi app
  iphone` (G). Keep "shogi" untranslated, "kanji" as in the app.

## Soon. (countdown app and widgets)

- **Primary:** `compte à rebours iphone` (G, B).
- **Secondary:** `widget compte à rebours` (G, B, A); `application compte à rebours` (G, B).
  Event-specific: `compte à rebours mariage` (G, B, A), `application compte à rebours vacances` (G),
  `compte à rebours voyage iphone` (G), `compte à rebours examen` (G, B, A: "examens & bac").
- **FAQ-style (from suggest):**
  - comment mettre un compte à rebours sur iphone (G)
  - comment faire un compte à rebours sur iphone (G)
  - créer un compte à rebours sur iphone (G)
  - mettre un compte à rebours en widget iphone (G)
  - compte à rebours écran de verrouillage iphone (G)
  - compte à rebours iphone fond d'écran (G)
  - compte à rebours partagé iphone (G, as `compte a rebours partagé iphone`)
- **Competitors (S):** Compte à Rebours ◎, Compte à rebours - Widgets, Compte à rebours & Widget, Compte à
  rebours widgets, Big Days - Compte à rebours, Compte à rebours - cntdwn, Countdown Star, Countdown Buddy,
  DayCount, Minuteur Décompte. A hints: "widget compte à rebours 321", "d-day widget: compte à rebours",
  "dayly: widget compte à rebours".
- **Notes:** "compte à rebours" is the whole market; "décompte" is not used (`décompte iphone` returned
  "facture iphone"). "Widget" is kept in English; "application" is the dominant form with `appli` second
  (`appli compte à rebours iphone` G). Google's top suggestions include `fond d'écran` and `écran de verrouillage`
  (lock-screen use), which fits Soon.'s Lock Screen and StandBy widgets. "Naissance" returns
  `compte à rebours naissance gratuit` (G), so the baby due date use case is real; "retraite" (`application
  compte à rebours retraite` G) is also a French favourite but is not on the English page, so not claimed here.
  `gratuit` is a frequent tail (`compte à rebours iphone gratuit` G); Soon. has a real free tier (5 moments), so it
  is safe to use in the body.

## Tare (balance-scale logic puzzle)

- **Primary:** `jeu casse tête iphone gratuit` (G; also `jeu casse tete iphone` G and `casse tete ios` G).
  Tare is a free download with 20 free levels and an unlock, so "gratuit" is honest only as "free to start".
- **Secondary:** `jeu de réflexion iphone` (G, B-adjacent); `meilleur jeux de casse tete iphone` (G);
  `jeu de réflexion ipad` / `jeux de reflexion ipad` (G).
- **FAQ-style (from suggest):**
  - meilleur jeu de réflexion iphone (G)
  - meilleur jeu de reflexion mobile (G)
  - quels sont les jeux de réflexion gratuits (B)
  - comment résoudre un casse tête (B)
- **Competitors (S):** Brain Test : Casse-têtes, Briques - Casse-tête logique, Sudoku.com - Casse-tête,
  Polysphere: Casse-tête, Impulse - Jeux de Réflexion, Stack Tower: Jeu d'équilibre, Balancio : jeu d'équilibre,
  Duck: Jeu d'équilibre, Beasts of Balance, Balance de Maths:Jeu Éducatif, Family Tree! - Jeu de logique.
- **Notes:** The "balance" angle has no French demand: `jeu de balance` is a crossword clue, `jeu de poids` is
  weights for the gym, `jeu de pesée logique` pulls generic logic (B), and `balance puzzle` is English. Primary
  demand is the generic puzzle category, so the page ranks on "casse-tête" and "jeu de réflexion" while the
  copy explains the balance mechanic. Millrace owns `jeu de logique`; Tare takes `casse-tête`/`réflexion` to
  avoid competing with it. French app titles that use balance mean physics/stacking games ("jeu d'équilibre"),
  not weighing puzzles. "Sans abonnement" is allowed for Tare, "sans pub" too (page says no ads). "Sans mots"
  returned nothing relevant (`jeu de logique sans mots` → word games), so do not use "sans mots" in the title.

## Taskful Day (day planner for iPhone and Mac)

- **Primary:** `application to do list` (G, B, A).
- **Secondary:** `to do list iphone` (G, B); `application to do list mac` (G); `planificateur de journée` (G, B).
  Also `application planning journée` (G) and `application organisation journée` (G).
- **FAQ-style (from suggest):**
  - faire une to do list sur iphone (G)
  - meilleure application to do list iphone (G)
  - meilleure application to do list (B)
  - application to do list partagée (G, B)
  - application organisation journée gratuite (G)
  - application liste de tâches (G, B)
- **Competitors (S):** Microsoft To Do, Todoist : to do list et agenda, Structured - Planning & Agenda, To Do List -
  Rappels de tâches, Agenda Planificateur Journée, Brizemi : planning journée, DayPace: Planificateur & Focus,
  Calendars – agenda et rappels (Readdle), Google Tasks, Me+ Planificateur Quotidien, Vesper : journée et focus.
- **Notes:** French keeps "to do list" in English (written without hyphens: `to do list`, `application to do
  list`), next to translated `liste de tâches`, which is typed less. "Planificateur" and "planning" are the
  translated words for the day view; "agenda" is the calendar. "Planificateur journalier" is the printable
  planner (`à imprimer`, `2026`) and should be avoided, as it is paper intent. Widget/lock-screen variants appear
  in Google (`to do list iphone widget`). Nothing came back for "report des tâches" or guilt-free wording
  (`tâches reportées application` empty), so the carry-forward angle is a copy point, not a keyword.

## WanderWiki (swipe through Wikipedia articles)

- **Primary:** `wikipedia aléatoire` (G, B). Variant with higher specificity: `wikipedia article aléatoire` (G).
- **Secondary:** `wikipedia au hasard` (G, B); `application wikipedia` (G, B); `page wikipédia au hasard` (G).
- **FAQ-style (from suggest):** French returns few questions; closest real phrases:
  - article wikipedia au hasard (G, B)
  - page wiki au hasard (G)
  - jeu wikipedia (G, B)
  - application pour apprendre des choses tous les jours (G)
  - application wikipedia gratuit (G)
- **Competitors (S/A):** Wikipédia (the official app), WikiScroll: Défile et Apprends, Wikipanion, Kiwix,
  DailyArt, Wikicards : Wiki TCG, Wikigacha. A hints: "the wiki game - jeu wikipédia", "wikireveal: jeu wikipédia".
- **Notes:** French uses both "aléatoire" and "au hasard"; "page" and "article" are used interchangeably
  (`page wikipédia aléatoire`, `article wikipedia au hasard`). Accent on Wikipédia is optional in queries. English
  terms: "swipe" is not used in French queries (`wikipedia swipe` returned English only), "random" appears only in
  English-style queries (`wikipedia random article`). Do not claim the generic `application wikipedia` as the
  primary: it is dominated by the official app. Games with Wikipedia (`jeu wikipedia pedantix`) are a different
  intent. Also an English-only reading app note: WanderWiki shows articles in 32 Wikipedia language editions, so
  French readers can use the French edition; check the app's French UI before claiming it is translated.

## Xiangqiful (xiangqi / Chinese chess)

- **Primary:** `échecs chinois` (G, B, A).
- **Secondary:** `xiangqi` (G, B, A); `comment jouer aux échecs chinois` (G; B also returns generic chess
  how-to); `apprendre les échecs chinois` (G, B-adjacent).
- **FAQ-style (from suggest):**
  - échecs chinois règles (G: `echecs chinois regles`, `règles échecs chinois`)
  - échecs chinois pièces (G: `echecs chinois pieces`)
  - échecs chinois en ligne (G, B)
  - échecs chinois xiangqi (G)
  - xiangqi règles (G) / règles xiangqi (G: `regles xiangqi`)
  - xiangqi pièces (G)
  - échecs chinois hors ligne (A)
- **Competitors (S/A):** Xiangqi One - Échecs chinois, PVXiangqi: Échecs chinois, Xiangqi : Échecs Chinois Jeu,
  Xiangqi – Échecs Chinois, Échecs Chinois Hors Ligne, Poqi: Échecs Chinois Xiangqi, Xiangqi : échecs chinois,
  Jardin Xiangqi: Échecs chinois, Xiangqi-Échecs chinois online, Chinese Chess - Best XiangQi, Xiangqi Trainer,
  Xiangqi.com, Real Xiangqi, Chess.com. A hints: "jardin xiangqi: échecs chinois", "poqi: échecs chinois xiangqi",
  "xiangqi one - échecs chinois", "xiangqiful : échecs chinois".
- **Notes:** French titles follow "Xiangqi : échecs chinois", which our listing already uses. Searchers type
  "échecs chinois" for the game and "xiangqi" once they know the name (G also returns Vietnamese `xiangqi co
  tuong` and `xingqiu`). The alphabet pass on `échecs chinois` also pulled noise: "échecs pont chinois",
  "chinois echec champion monde", "jeu surnomme les echecs chinois cody" (crosswords). "Règles" and "pièces" lead
  every how-to query, so those words belong in the intro and FAQ. `échecs chinois iphone` and `xiangqi
  application` returned nothing, so skip "iphone" in the title. "Hors ligne" (offline) appears as an A hint and in
  one competitor title; use it only if the app works offline.

## Clippet (clipboard manager for iPhone, iPad and Mac; not released yet)

- **Primary:** `historique presse papier iphone` (G, B). Written with or without hyphen and plural ("presse-papier",
  "presse-papiers"); Google shows both.
- **Secondary:** `gestionnaire presse papier mac` (G; `gestionnaire presse papier mac gratuit` G);
  `application presse papier iphone` (G); `presse papier mac historique` (G).
- **FAQ-style (from suggest):**
  - où est le presse papier iphone (G, B)
  - où se trouve le presse papier sur iphone (B)
  - comment voir son historique de copier coller (B)
  - comment retrouver ce que j'ai copié sur iphone (G)
  - voir historique presse papier iphone (G)
  - voir historique copier coller mac (G)
  - presse papier universel ne fonctionne pas (G)
- **Competitors (S):** Paste – Gestion presse-papiers, Pasteboard - Presse-papiers, Clippo - Presse-papiers,
  ClipBox, Clipster, Octoclip, Pasted, EasyPaste, OnePaste, Cross Paste, PasteDock, Presse-papiers: Copier Coller,
  CopyMate, Clipboard History Mobile. A hint: "presse papier iphone".
- **Notes:** The French noun is "presse-papiers" (singular "presse-papier" is common in queries), and the
  action is "copier-coller". English "clipboard manager" is also typed (`clipboard manager mac`, `clipboard manager
  iphone`, `mac clipboard history`, all G), so keep "clipboard" visible in the body next to the French term.
  Informational intent dominates (`où est`, `voir`, `historique` of the built-in clipboard), so the page should
  lead with "Retrouvez tout ce que vous avez copié" and then name the app features. "Universal Clipboard" is
  called "presse-papiers universel" (G). Clippet is unreleased: keep the page `noindex` until launch;
  these keywords are for when it goes live.

---

## Summary table

| Page | Primary | Secondaries |
|---|---|---|
| mediakit | compresser vidéo iphone | compresser pdf iphone; convertir vidéo iphone en mp4 |
| millrace | jeu de logique iphone | jeu de logique sans pub; jeux de logique ipad |
| mockly | screenshot app store | app store screenshot maker; mockup app store |
| observa | hrv apple watch | variabilité de la fréquence cardiaque; application sommeil apple watch |
| pawza | application carnet de santé animaux | application carnet de santé chien; carnet de vaccination chat |
| rightsplit | partager l'addition | application partage addition restaurant; partager l'addition entre amis |
| shogiful | shogi | échecs japonais; apprendre le shogi |
| soon | compte à rebours iphone | widget compte à rebours; application compte à rebours |
| tare | jeu casse tête iphone gratuit | jeu de réflexion iphone; meilleur jeux de casse tete iphone |
| taskful-day | application to do list | to do list iphone; planificateur de journée |
| wanderwiki | wikipedia aléatoire | wikipedia au hasard; wikipedia article aléatoire |
| xiangqiful | échecs chinois | xiangqi; comment jouer aux échecs chinois |
| clippet | historique presse papier iphone | gestionnaire presse papier mac; application presse papier iphone |
