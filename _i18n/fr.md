# Language sheet: French (fr), France

Never published (`_i18n` is excluded from the build). Rulebook: TRANSLATION.md. Read this sheet before writing or
reviewing any French page. Every decision a translator would otherwise make differently per page lives here.

## Status

| Item | Status |
|---|---|
| Setup (config default, locales.yml block, `_data/i18n/fr.yml`, sitemap and feed stubs, `day_one` date string) | done 2026-11-07 |
| Keyword research (Tier 1) | done 2026-11-07 (Search Console has almost no French queries yet; see Keywords) |
| Tier 1 pages | done 2026-11-08: home, apps hub, 21 app pages (Clippet unlisted), 21 support pages, 21 privacy policies + Clippet terms, about, support hub, transparency (+ `_data/i18n_transparency/fr.yml`), /fr/llms.txt, /fr/llms-full.txt, 21 OG cards |
| Live | yes, `live: true` since 2026-11-08 (Tier 1; go-live commit not yet pushed) |
| Tier 2, batch 1 | written and integrated 2026-11-08, no native review yet: hubs /fr/guides/ and /fr/for/; guides best-chess-apps-iphone, best-logic-puzzle-games-iphone, workout-app-without-subscription, best-shogi-apps-iphone, best-xiangqi-apps-iphone; for/shift-workers, for/apple-health-power-users, for/calm-productivity. Not yet: guides/bill-tracker-without-bank-connection (low demand; its US apps Rocket Money, Monarch and Copilot are not sold in France, needs a Bankin'/Linxo rewrite) and for/indie-ios-developers (French developers search in English). Research and French-store check of every named competitor: ~/Downloads/githubcode/fr-tier2-research-2026-11-08.md. Stale check before the batch: 0 French pages stale |
| Tier 2, batch 2 | written and integrated 2026-11-08, no native review yet: guides/bill-tracker-without-bank-connection (local rewrite: Bankin’ and Linxo replace Rocket Money, Truebill, Copilot and Monarch, which are not sold in France) and the first two local-only pages (6.7), /fr/guides/application-compte-a-rebours-iphone/ (Soon.) and /fr/guides/limiter-temps-ecran-iphone/ (EarnLock). for/indie-ios-developers stays English-only (no French demand). Tier 2 is complete for French. Research: ~/Downloads/githubcode/fr-tier2-batch2-research-2026-11-08.md. Stale check before the batch: 0 French pages stale |
| Tier 3, batch 1 | written and integrated 2026-11-08, no native review yet: hub /fr/alternatives/ and nine comparisons tricount, splitwise (RightSplit); chess-com, lichess (Chessful); opal, forest, one-sec (EarnLock); whoop (Observa); hevy (LiftLog); plus the local-only /fr/alternatives/alternative-bankin/ (AllPaid vs Bankin’ and Linxo). Demand research over all 123 English comparisons: ~/Downloads/githubcode/fr-tier3-research-2026-11-08.md (next batch listed there); French store check of each competitor (IAP rows, full French descriptions): ~/Downloads/githubcode/fr-tier3-store-2026-11-08.md. Stale check before the batch: 0 French pages stale |
| Tier 3, batch 2 | written and integrated 2026-11-08, no native review yet: bevel, oura, athlytic, welltory (Observa); fitbod, strong-workout-app (GymLogger X); pdf-expert (MediaKit); wikipedia-app (WanderWiki); screenzen (EarnLock); plus the local-only /fr/alternatives/splid/ (RightSplit; « Splid ou Tricount »). Hub now 20 cards. Store check: ~/Downloads/githubcode/fr-tier3-store-batch2-2026-11-08.md; shortlist in fr-tier3-research-2026-11-08.md (batch 2 section; next: AutoSleep, Habitica, Alpha Progression). Stale check before the batch: 0 French pages stale |
| Tier 3, batch 3 | written and integrated 2026-11-08, no native review yet: autosleep, gentler-streak (Observa); rise-sleep-tracker (AfterShift, its first French comparison); habitica, streaks-app (Taskful Day, its first); chessable (Chessful); jomo (EarnLock); stronglifts-5x5, alpha-progression (GymLogger X); cloudconvert (MediaKit). Hub now 30 cards. Store check: ~/Downloads/githubcode/fr-tier3-store-batch3-2026-11-08.md. Not sold in the French store: Wikiwand, Convertio, HandBrake. Sleep Cycle and Pillow have French demand but no English page (English first). Stale check before the batch: 0 French pages stale |
| Tier 4, batch 1 | written and integrated 2026-11-08, no native review yet: hub /fr/journal/ and nine posts how-many-steps-a-day-to-aim-for (EarnLock), how-long-to-rest-between-sets, choosing-a-strength-program-you-will-finish (LiftLog), how-to-estimate-your-one-rep-max, rpe-and-rir-explained (GymLogger X), how-to-sleep-after-a-night-shift (AfterShift), apple-watch-hrv-without-a-baseline (Observa), how-much-to-tip-in-the-us (RightSplit), compress-a-video-for-email (MediaKit), plus the local-only /fr/journal/travail-en-3x8/ (AfterShift; INRS, ANSES and Code du travail sources). Demand research: ~/Downloads/githubcode/fr-tier4-research-2026-11-08.md (next batch listed there). Stale check before the batch: 0 French pages stale |
| Tier 4, batch 2 | written and integrated 2026-11-08, no native review yet: puppy-and-kitten-vaccination-schedule, pet-medical-records-what-to-keep (Pawza), when-to-deload (GymLogger X), double-progression-explained (LiftLog), puzzle-games-without-ads-or-lives (Millrace), find-every-recurring-charge (AllPaid; Bankin’ and Linxo replace Rocket Money), what-an-iphone-app-can-actually-block (EarnLock), how-to-find-interesting-wikipedia-articles (WanderWiki), how-plan-mode-builds-a-checklist (Soon.), plus the local-only /fr/journal/passeport-europeen-chien-chat/ (Pawza; service-public, agriculture.gouv.fr, I-CAD, Your Europe, Regulation 576/2013). Hub now 20 posts. Stale check before the batch: 0 French pages stale |
| Tier 4, batch 3 | written and integrated 2026-11-08, no native review yet: your-photos-shouldnt-ride-the-elevator, every-media-tool-already-on-your-mac (MediaKit), apple-health-metrics-worth-interpreting (Observa), bill-splitting-math-tax-tip-shared-plates (RightSplit; France: prices « taxes et services compris », service-public.fr F22387), xiangqi-rules-for-chess-players (Xiangqiful), i-will-not-ask-for-your-bank-login (AllPaid; ACPR and Banque de France on aggregators), engine-depth-at-club-level-tune-down, 30-chess-mistake-motifs (Chessful), unlock-cost-outside-the-app (EarnLock), plus local-only /fr/journal/surcharge-progressive-musculation/ (ACSM 2009 abstract, ACSM 2026 position stand PMC12965823). Hub 30 posts. Research: ~/Downloads/githubcode/fr-tier4-research-2026-11-08.md § Batch 3. Stale check before the batch: 0 French pages stale |
| Native review | none (NATIVE REVIEWER: none). Every page is logged as "no native review yet" |
| Build time | 56 s before French (2026-11-07), 80 s with French Tier 1 (2026-11-08, clean run, `--profile`). Hot spot: `_includes/tx-app.html` 44 s over 968 calls, then footer 30 s: each new language makes it worse; worth a map lookup before the next language |

## Market and register

- Market: France. Folder `/fr/`, `<html lang="fr">`, hreflang `fr` (also serves Belgium, Switzerland, Luxembourg
  and Canada, who see EUR prices; the App Store link opens their own storefront), og:locale `fr_FR`, territory
  FRA, currency EUR.
- Engines (TRANSLATION.md 7.4): Google first, then Bing (also feeds DuckDuckGo, Ecosia, Qwant, Copilot). Tools:
  Search Console, Bing Webmaster Tools. IndexNow covers Bing and the engines that use it.
- **Formality: vous** on every page, interface string, FAQ and privacy policy. Reasons:
  1. TRANSLATION.md 13 default for France.
  2. Apple's French App Store, iOS and support pages address the reader with vous, and so do our own French
     App Store descriptions (LiftLog: « Essayez l'app gratuitement pendant 7 jours », Observa, checked 2026-11-07).
  3. A French reader expects vous from a company site, even a one-person studio; tu reads as a game or a youth brand.
  The apps' French interfaces are not consistent (fr-glossary.md, counted 2026-11-07): mostly tu in AfterShift,
  Shogiful, Xiangqiful, LiftLog and Chessful's lessons; mixed in EarnLock, Soon., Taskful Day, Pawza, Chessful;
  vous in AllPaid, AppMeta, AppMeta Pulse, MediaKit, Millrace, Mockly, Observa, RightSplit, Tare, WanderWiki,
  Clippet, GymLogger X (mostly). Chessful's French store name uses a tu imperative (« Entraîne & Analyse »).
  That is an app-side inconsistency to fix in the apps; the site stays vous everywhere. Feature names are copied
  from the app; a tu sentence from an app is never quoted on the site.
  Never mix: no tu, toi, ton, ta, tes anywhere.

## Typography and punctuation

House rules (TRANSLATION.md 8.3), with the characters to type:

- Quotes « … » with a narrow no-break space (U+202F) inside both marks. Inner quotes “…”. Never "…" in prose.
- Narrow no-break space (U+202F) before ; : ! ? (TRANSLATION.md 8.3). Note: Apple's own French pages use the
  regular no-break space U+00A0 there (checked in raw bytes on 8 pages, fr-apple-terms.md); the rulebook wins for
  our prose. Never a plain space, never no space.
- Regular no-break space (U+00A0) between a number and its unit, %, € or a thousands group: `3,99 €`, `80 %`,
  `35 °C`, `100 000`, `92,7 Mo`, `8 h`. This is what the French App Store prints (checked 2026-11-07).
- Apostrophe ’ (U+2019) in prose and YAML strings, as Apple writes it. In JSON-LD and llms files too.
- Headings in sentence case: only the first word and proper names take a capital. No English title case.
- Capitals keep their accents: « À vie », « État », « Écran ».
- No em or en dashes. A range is « de 3 à 5 kg ». Lists: « A, B et C » (no comma before et/ou).
- Ellipsis … (one character).
- Numbers: decimal comma (4,8), thousands with U+00A0 from five digits on (12 500); four-digit numbers without a
  separator (6005), as the App Store shows them. Metric units.
- Times: 24-hour, « 22 h 30 » in prose. Dates in prose: « 26 octobre 2026 » (templates use date.html; months
  lowercase; the first of the month « 1er novembre 2026 »).
- Ordinals: 1er, 1re, 2e (never 2ème, 2nd).
- « app » is fine in body copy and is feminine (« une app », « cette app », as Apple writes it); « application »
  in titles and H1 where it carries the search phrase. « appli » only where a keyword needs it, never in headings.
- Anglicisms: use the French word when one is in common use (« abonnement » not « subscription », « réglages »
  for iOS Settings, « courriel » no: French readers say « e-mail » or « adresse e-mail », as Apple does).
  Keep English where French searchers and Apple keep it: App Store, App Store Connect, widget, Dynamic Island,
  Apple Watch, iCloud, Siri, ASO, privacy manifest (Apple FR: « manifeste de confidentialité » in body text).

## Formats (checked 2026-11-07 in the French App Store storefront, apps.apple.com/fr)

| What | Format seen | Where | In the site |
|---|---|---|---|
| Price | `9,99 €` (no-break space U+00A0 before €) | Things 3, apps.apple.com/fr/app/id904237743; Observa id6757438990 IAP rows `3,99 €`, `24,99 €`, `59,99 €` | locales.yml `EUR: position after, space U+00A0, decimal ",", group U+00A0` |
| Free app | `Gratuit · Achats intégrés` | Observa, LiftLog | `strings.free: "Gratuit"` |
| Rating count | `2,3 k notes`, `1 notes` (sic) | Things 3, Observa | counts from the catalog, printed as integers |
| Rating value | `4,7` style, decimal comma | Things 3 | `strings.decimal: ","` |
| Dates on the store | `26/12/2019` (version history) | Things 3 | site prose uses the long form `26 octobre 2026` (TRANSLATION.md 4.7) |
| Size | `92,7 Mo` | Observa | not used on the site |
| Mac line | `Conçue pour iPad. Non validée pour macOS.` | Observa | not used |

The French web storefront still lists in-app purchase prices; our own prices come from the catalog (territory
FRA) and print in the format above. Price line pattern: `Gratuit, Premium à partir de 3,99 €/mois, 24,99 €/an ou
59,99 € à vie` (strings.from « à partir de », per_month « /mois », per_year « /an », lifetime « à vie », or « ou »).
Trial label: `7 jours d’essai gratuit`. Zero price on plan cards: `{P_ZERO}` → `0 €`.

Note: the French App Store shows the developer's personal name and address (« Création », « Fournisseur »).
That name never goes on the site; attribute to "Lagerland Apps".

## Glossary

Companion files: `_i18n/fr-glossary.md` (per app: French coverage, feature names verbatim from the string
catalogs, French App Store name and subtitle, flags) and `_i18n/fr-apple-terms.md` (Apple's own French names,
each with its Apple source URL). Rule: a feature name is written exactly as the app's French interface shows it;
an Apple product or feature name exactly as Apple writes it in French.

All 21 apps (20 live plus Clippet) have a French interface (98 to 100 % of each catalog, checked 2026-11-07), so
every app page may say the app is available in French. Gaps to keep off the pages: AfterShift's calendar
permission prompt, Pawza's camera and photo permission prompts, AllPaid's Siri phrases and LiftLog's Siri hint
are English only; LiftLog has 8 untranslated statistics labels; GymLogger X has unaccented French strings in the
program creator (app bug: never copy those spellings).

The terms that matter most across the site:

| English | French on the site | Source |
|---|---|---|
| (address) you | vous, never tu | this sheet |
| Download on the App Store (badge) | Télécharger dans / l’App Store (Mac: Télécharger dans le / Mac App Store) | Apple's fr-fr badge artwork |
| Free (price) | Gratuit | French App Store price line |
| In-App Purchases | Achats intégrés | App Store |
| subscription / cancel | abonnement; Réglages > [votre nom] > Abonnements > « Annuler l’abonnement » | support.apple.com/fr-fr/118428 |
| refund | reportaproblem.apple.com > « J’aimerais » > « Demander un remboursement » | support.apple.com/fr-fr/118223 |
| lifetime (purchase) | « à vie » (price line, plan cards, as the apps' paywalls say « À vie »); « achat unique » in prose | app catalogs, store IAP names |
| Family Sharing | partage familial (Apple FR lowercase in running text; « Partage familial » as a label) | App Store, Apple support |
| Data Not Collected | Données non collectées (section « Confidentialité de l’app ») | French App Store product page |
| Health app / Apple Health | l’app Santé / Apple Santé | support.apple.com/fr-fr, apple.com/fr/health |
| Heart Rate Variability (HRV) | variabilité de la fréquence cardiaque (VFC); always SDNN for Apple Health. Observa's UI says VFC | Apple FR, Observa catalog |
| Resting heart rate | fréquence cardiaque au repos | Apple FR |
| Screen Time | Temps d’écran | Apple support |
| Focus / Sleep Focus | mode de concentration / Concentration « Repos » | Apple support |
| Notifications | notifications | Apple support |
| Home Screen / Lock Screen / widgets | écran d’accueil / écran verrouillé / widgets | Apple support |
| Live Activities / Smart Stack | Activités en direct / Défilement intelligent | Apple support |
| iCloud sync | synchronisation iCloud | Apple support, app catalogs |
| Apple Account | compte Apple | Apple support |
| Settings (iOS) | Réglages | Apple support |

App Store categories as the French store prints them: Forme et santé, Productivité, Finance, Économie et
entreprise, Outils de développement, Casse-tête, Jeux de société, Utilitaires, Éducation, Livres, Style de vie,
Graphisme et design, Photo et vidéo, Références.

Per-app tier names follow each app's French UI (fr-glossary.md): Premium for Observa (the English site says Pro),
Soon., Shogiful, Xiangqiful, WanderWiki, EarnLock, Chessful; Pro+ for RightSplit; Pro for Pawza, Taskful Day,
GymLogger X; Clippet Pro. Where the English site's tier name differs from the app, the French page follows the
app, as German did.

## Keyword research

Full notes, sources and FAQ-style questions per page: `_i18n/fr-keywords.md` (Google suggest fr/FR, Bing
autosuggest fr-FR, App Store search hints and results for the French storefront, 2026-11-07).

Search Console, country France, checked 2026-11-07 (Chrome, /u/1/): the old github.io property has 63 clicks and
4,480 impressions from France over seven months, 221 queries, almost all in English (shogi piece names and
notation, Bevel, Welltory and Athlytic alternatives, Wikipedia random articles and Wikiwand, fastlane frameit,
Chessis). Only four or five French queries. The new lagerland.app property has 6 impressions since 2026-10-29.
French readers reach the English pages through English queries today, so the French primaries come from suggest
and the App Store. Revisit 4 to 6 weeks after go-live with the page filter `/fr/`.

`seo.title`, the H1 and `quick_answer` of each page are written for its primary query.

| Page | Primary query | Secondary queries |
|---|---|---|
| Home (/fr/): studio of privacy-first Apple apps | `application sans pub iphone` | `application sans publicité`, `appli sans pub` |
| Apps hub (/fr/apps/): all apps | `meilleures applications iphone` | `applications utiles iphone`, `application sans pub iphone` (shared with home, secondary only) |
| About (/fr/lagerland-apps/): one-person studio, Finland | none with demand: brand-led (« Lagerland Apps » + « développeur indépendant ») | `développeur d’applications` |
| Support hub (/fr/support/) | `annuler abonnement iphone` | `restaurer achats apple`, `se faire rembourser application apple` |
| Transparency (/fr/transparency/) | `app tracking transparency` (French searchers type the English) | `suivi des applications iphone`, `privacy manifest` |
| AfterShift (shift-work sleep) | `travail de nuit sommeil` | `travail posté sommeil`, `dormir après travail de nuit` |
| AllPaid (bill reminders, no bank login) | `rappel factures` (App Store hints only; no Google demand) | `application rappel paiement`, `app suivi abonnements` |
| AppMeta (App Store Connect for Mac) | `app store connect mac app` | `mots clés app store`, `aso app store` |
| AppMeta Pulse (App Store Connect on iPhone) | `app store connect iphone` | `app store connect ios`, `app store connect api` |
| Chessful (chess learning and analysis) | `application échecs` | `apprendre les échecs application`, `analyse de parties d’échecs` |
| EarnLock (earn screen time by moving) | `bloqueur d’applications` | `bloquer applications iphone`, `limiter temps d’écran` |
| GymLogger X (strength tracker, Apple Watch) | `application musculation apple watch` | `carnet de musculation application`, `programme musculation application` |
| LiftLog (lift log, no subscription) | `application musculation sans abonnement` | `application fitness sans abonnement`, `application musculation gratuite sans abonnement` |
| MediaKit (compress/convert media on device) | `compresser vidéo iphone` | `compresser pdf iphone`, `convertir vidéo iphone en mp4` |
| Millrace (tile delivery puzzle; never write "2048") | `jeu de logique iphone` | `jeu de logique sans pub`, `jeux de logique ipad` |
| Mockly (App Store screenshots on Mac) | `screenshot app store` | `app store screenshot maker`, `mockup app store` |
| Observa (sleep, HRV, recovery from Apple Health) | `hrv apple watch` | `variabilité de la fréquence cardiaque`, `application sommeil apple watch` |
| Pawza (pet health records) | `application carnet de santé animaux` | `application carnet de santé chien`, `carnet de vaccination chat` |
| RightSplit (split bills from receipts) | `partager l’addition` | `application partage addition restaurant`, `partager l’addition entre amis` |
| Shogiful (shogi) | `shogi` | `échecs japonais`, `apprendre le shogi` |
| Soon. (countdowns) | `compte à rebours iphone` | `widget compte à rebours`, `application compte à rebours` |
| Tare (balance logic puzzle) | `jeu casse-tête iphone` (suggest: « jeu casse tete iphone gratuit ») | `jeu de réflexion iphone`, `meilleur jeux de casse tete iphone` |
| Taskful Day (day planner, iPhone + Mac) | `application to do list` | `to do list iphone`, `planificateur de journée` |
| WanderWiki (swipe Wikipedia) | `wikipedia aléatoire` | `wikipedia au hasard`, `wikipedia article aléatoire` |
| Xiangqiful (xiangqi) | `échecs chinois` | `xiangqi`, `comment jouer aux échecs chinois` |
| Clippet (clipboard manager; unlisted until launch) | `historique presse-papier iphone` | `gestionnaire presse-papier mac`, `application presse-papier iphone` |
| /fr/guides/best-chess-apps-iphone/ | `meilleure application échecs` | `quelle application pour apprendre les échecs`, `application échecs sans pub`, `chess.com ou lichess` |
| /fr/guides/best-logic-puzzle-games-iphone/ | `jeux de logique iphone` | `jeu de logique sans pub`, `jeu de réflexion sans pub`, `meilleur jeu de logique iphone` |
| /fr/guides/workout-app-without-subscription/ | `application musculation sans abonnement` (shared with LiftLog) | `application fitness sans abonnement`, `application sport sans abonnement` |
| /fr/guides/best-shogi-apps-iphone/ | `application shogi` | `apprendre le shogi`, `échecs japonais`, `shogi en ligne` |
| /fr/guides/best-xiangqi-apps-iphone/ | `échecs chinois` (shared with Xiangqiful) | `xiangqi`, `apprendre les échecs chinois`, `échecs chinois en ligne` |
| /fr/for/shift-workers/ | `travail de nuit sommeil` (shared with AfterShift; owner question) | `dormir après travail de nuit`, `travail posté sommeil`, `application travail de nuit` |
| /fr/for/apple-health-power-users/ | `application apple santé` | `meilleure application santé apple watch`, `hrv apple watch` |
| /fr/for/calm-productivity/ | `application organisation journée` (concept « sans pression des séries » has no French query) | `application planning journée`, `application to do list iphone` |
| /fr/guides/bill-tracker-without-bank-connection/ | `application de gestion des abonnements` | `gérer mes abonnements iphone`, `application gestion budget sans banque`, `app suivi abonnements` |
| /fr/guides/application-compte-a-rebours-iphone/ (local-only) | `application compte à rebours` | `widget compte à rebours iphone`, `meilleure application compte à rebours`, `application compte à rebours vacances` / `retraite` / `voyage` |
| /fr/guides/limiter-temps-ecran-iphone/ (local-only) | `application pour limiter le temps d’écran iphone` | `réduire temps d’écran iphone`, `bloquer application iphone`, `application pour bloquer les réseaux sociaux` (child and parental-control intent is out of scope, said on the page) |
| /fr/alternatives/ (hub) | none of its own (brand names list) | the primaries of its pages |
| /fr/alternatives/tricount/ | `alternative tricount` | `alternative à tricount`, `application comme tricount`, `partager l’addition` |
| /fr/alternatives/splitwise/ | `alternative splitwise` | `splitwise gratuit`, `splitwise ou tricount` |
| /fr/alternatives/chess-com/ | `analyse partie chess.com gratuit` | `chess com analyse gratuite`, `chess.com gratuit ou payant`, `alternative chess.com` |
| /fr/alternatives/lichess/ | `lichess ou chess.com` | `alternative lichess`, `lichess analyse` (overlaps the chess guide's secondary `chess.com ou lichess`) |
| /fr/alternatives/opal/ | `application comme opal` | `alternative opal`, `opal app blocker`, `bloquer applications iphone` |
| /fr/alternatives/forest/ | `alternative forest` | `forest application gratuite`, `application comme forest` |
| /fr/alternatives/one-sec/ | `alternative one sec` | `application comme one sec`, `one sec app` |
| /fr/alternatives/whoop/ | `alternative whoop sans abonnement` (Observa is never « sans abonnement »: titles say « sans abonnement obligatoire ») | `alternative à whoop`, `alternative whoop apple watch` |
| /fr/alternatives/hevy/ | `alternative hevy` | `hevy app prix`, `application musculation sans abonnement` |
| /fr/alternatives/alternative-bankin/ (local-only) | `alternative bankin` | `alternative à bankin`, `application budget sans connexion bancaire`, `application gestion budget sans banque` |
| /fr/alternatives/bevel/ | `alternative bevel` | `bevel gratuit`, `bevel ou whoop`, `bevel vs athlytic` |
| /fr/alternatives/oura/ | `alternative oura` | `oura ring abonnement`, `oura ou apple watch`, `oura ou whoop` |
| /fr/alternatives/athlytic/ | `athlytic en français` (store lists English only) | `alternative athlytic`, `athlytic vs whoop` |
| /fr/alternatives/welltory/ | `welltory en français` (store lists EN, RU, ES) | `alternative welltory`, `welltory apple watch` |
| /fr/alternatives/fitbod/ | `alternative fitbod` | `fitbod gratuit`, `fitbod prix`, `fitbod en français` (store: EN, PT, ES) |
| /fr/alternatives/strong-workout-app/ | `strong ou hevy` (title on `alternative strong`) | `alternative strong`, `application musculation apple watch` |
| /fr/alternatives/pdf-expert/ | `alternative pdf expert` | `pdf expert gratuit`, `compresser pdf iphone` |
| /fr/alternatives/wikipedia-app/ | `application wikipédia` | `application wikipédia gratuit`, `wikipedia aléatoire` |
| /fr/alternatives/screenzen/ | `alternative screenzen` | `screenzen avis`, `screenzen gratuit` |
| /fr/alternatives/splid/ (local-only) | `splid ou tricount` | `alternative splid`, `splid app`, `application partage de dépenses` |
| /fr/alternatives/autosleep/ | `alternative autosleep` | `autosleep avis`, `autosleep vs oura` |
| /fr/alternatives/gentler-streak/ | `alternative gentler streak` | `gentler streak avis` |
| /fr/alternatives/rise-sleep-tracker/ | `alternative rise` (« l’app RISE », not the pillow brand) | `rise sleep app`, `application sommeil travail posté` |
| /fr/alternatives/habitica/ | `habitica français` (store lists French: « oui ») | `alternative habitica`, `habitica avis` |
| /fr/alternatives/streaks-app/ | `streaks application` | `alternative streaks`, `streaks apple watch` |
| /fr/alternatives/chessable/ | `chessable en français` (store lists English only) | `alternative chessable`, `chessable prix` |
| /fr/alternatives/jomo/ | `alternative jomo` | `jomo app`, `application comme jomo` |
| /fr/alternatives/stronglifts-5x5/ | `alternative stronglifts` | `stronglifts 5x5 app`, `stronglifts gratuit` |
| /fr/alternatives/alpha-progression/ | `alternative alpha progression` | `alpha progression avis`, `alpha progression pro` |
| /fr/alternatives/cloudconvert/ | `cloudconvert gratuit` | `cloudconvert en français`, `alternative cloudconvert` |
| /fr/journal/ (hub) | none of its own | the primaries of its posts |
| /fr/journal/how-many-steps-a-day-to-aim-for/ | `combien de pas par jour` | `nombre de pas par jour recommandé`, `10000 pas par jour`, `nombre de pas par jour selon âge` |
| /fr/journal/how-long-to-rest-between-sets/ | `temps de repos entre les séries` | `temps de récupération entre les séries`, `temps de repos entre séries hypertrophie` |
| /fr/journal/how-to-estimate-your-one-rep-max/ | `calcul 1rm` | `formule 1rm`, `calculer son 1rm`, `formule brzycki`, `formule epley 1rm` |
| /fr/journal/rpe-and-rir-explained/ | `rpe musculation` | `rir musculation`, `échelle rpe musculation`, `tableau rpe musculation`, `rpe 8 musculation` |
| /fr/journal/choosing-a-strength-program-you-will-finish/ | `programme ppl` | `full body ou split`, `programme upper lower`, `programme 5/3/1` |
| /fr/journal/how-to-sleep-after-a-night-shift/ | `bien dormir après une nuit de travail` | `combien de temps dormir après une nuit de travail`, `comment dormir après un travail de nuit` (« travail de nuit sommeil » stays with the app page, I-0022) |
| /fr/journal/apple-watch-hrv-without-a-baseline/ | `vfc normale` | `vfc apple watch`, `vfc basse`, `vfc normale apple watch`, `hrv apple watch` |
| /fr/journal/how-much-to-tip-in-the-us/ | `pourboire aux états-unis` | `pourboire usa`, `pourboire usa restaurant`, `combien de pourboire aux usa`, `tip aux usa` |
| /fr/journal/compress-a-video-for-email/ | `compresser une vidéo pour l’envoyer par mail` | `vidéo trop lourde pour envoyer par mail`, `envoyer une grosse vidéo par mail`, `taille max pièce jointe gmail` |
| /fr/journal/travail-en-3x8/ (local-only) | `travail en 3x8` | `3x8 horaires`, `travail en 3x8 c’est quoi`, `travail en 3x8 santé`, `2x8 3x8`, `5x8` |
| /fr/journal/puppy-and-kitten-vaccination-schedule/ | `vaccin chiot` | `vaccin chaton`, `rappel vaccin chien`, `calendrier vaccination chiot`, `vaccin rage chien obligatoire` |
| /fr/journal/pet-medical-records-what-to-keep/ | `carnet de santé chien` | `carnet de santé chat`, `carnet de santé chien en ligne`, `dossier médical chien` |
| /fr/journal/passeport-europeen-chien-chat/ (local-only) | `passeport européen chien` | `passeport européen chat`, `passeport européen chien obligatoire`, `passeport européen chien perdu`, `carnet de santé ou passeport chien` |
| /fr/journal/when-to-deload/ | `semaine de décharge musculation` | `deload musculation`, `semaine de deload`, `quand faire une semaine de décharge` |
| /fr/journal/double-progression-explained/ | `double progression musculation` | `double progression`, `progression musculation`, `surcharge progressive` |
| /fr/journal/puzzle-games-without-ads-or-lives/ | `jeux iphone sans pub` | `jeux sans pub iphone`, `jeux iphone gratuit sans pub`, `jeu de réflexion sans pub` (« jeu de logique sans pub » stays with the logic-puzzle guide) |
| /fr/journal/find-every-recurring-charge/ | `voir ses abonnements iphone` | `trouver ses abonnements`, `voir ses abonnements apple`, `prélèvements récurrents` |
| /fr/journal/what-an-iphone-app-can-actually-block/ | `comment bloquer une app sur iphone` | `bloquer une application iphone`, `contourner temps d’écran iphone` (« application pour limiter le temps d’écran » stays with the local-only guide) |
| /fr/journal/how-to-find-interesting-wikipedia-articles/ | `wikipedia page aléatoire` | `wikipedia article aléatoire`, `générateur de page wikipédia aléatoire` (« wikipedia aléatoire » stays with the WanderWiki page) |
| /fr/journal/how-plan-mode-builds-a-checklist/ | `application organisation mariage` | `checklist mariage`, `rétroplanning mariage`, `checklist voyage`, `application checklist` |

Wording rules from the research: « application » beats « appli » and « app » in searches, so titles and H1 use
« application »; body copy may say « app ». Privacy is searched as « sans pub », « sans publicité », rarely
« sans suivi »; « vie privée » has little consumer demand. For AllPaid lead with « rappel » and « échéances »
(plain « facture » pulls in invoicing software). Millrace takes « jeu de logique », Tare takes « casse-tête » and
« jeu de réflexion », so the two pages don't compete (« jeu de balance » is a crossword clue). Searchers keep these
in English: HRV, to do list, widget, screenshot, mockup, App Store Connect, ASO, app tracking transparency, privacy
manifest. Google often returns unaccented forms; pages write the accented French.

## Local competitors (for Tier 3)

Seen in French App Store results and suggestions (per app in fr-keywords.md): to be checked for availability and
prices in the French storefront before any comparison page is written (TRANSLATION.md 6.4).

Checked 2026-11-08 (fr-tier3-store-2026-11-08.md): Bankin’ (447040033, ★92 652 FR) and Linxo (440509306, ★11 508)
are the French bank-linked budget apps (local-only page done). Splid (991473495, ★2 325 FR, « Partager vos dépenses »)
is a French-market Tricount-style splitter with no English page: local-only page /fr/alternatives/splid/ done in batch 2. Tricount
(★98 114) dwarfs Splitwise (★495) in France.

## Open questions

Moved on 2026-11-08 to the master list `~/Downloads/githubcode/ISSUES.md` (the old text is in git history). New
English-side errors, app bugs and owner questions found while translating go there, never here.

## Tells to cut in French (TRANSLATION.md 8.2, plus what reviews find)

Stock phrasing: « Dans un monde en constante évolution », « Plongeons dans », « Il est important de noter que »,
« joue un rôle crucial », « incontournable », « véritable », « fluide », « En somme », « non seulement … mais
aussi », « Que vous soyez … ou … ». Translationese: English title case, missing narrow no-break spaces before
; : ! ? and inside « », « faire du sens », tu and vous mixed. Added for this site: « expérience » for an app,
« solution », « booster », « game changer », « tout-en-un », « simple » in every sentence, stacked « de » chains
copied from English noun stacks, the passive « est conçu pour » everywhere, « votre » in front of every noun.

Found in the interface-strings review (2026-11-07): sales adjectives that agree with « app » in labels (« Idéale
pour », « Moins adaptée à »: write « Convient surtout à », « Convient moins à »); audience labels written « Pour
l’app X » when the English names the users (« Pour les utilisateurs d’Apple Santé »); plural-with-count strings
with no singular (« {count} mises à jour »: reword so the count sits in brackets); « sans suivi » or « sans pub »
as a stand-in for "privacy-first" (they are narrower facts: write « respectueux de la vie privée » where the
English says privacy-first); « vis-à-vis » for "side-by-side"; « créations » for apps; « Société » for "Company"
in a one-person studio's footer; « émis par » for a place of issue (« émis à »); « pub » in running copy (write
« publicité »; « sans pub » only where it is the search phrase, e.g. a title).

Found in the Tier 1 reviews (2026-11-08): « tournent sur » for "run on" (« fonctionnent sur »); « balayage » for a swipe; « vrai(e) » as a sales adjective (« une vraie gestion », « une vraie app Mac »: write « complète », « native »); noun calques such as « décaleur de phase » (use a verb); « soignants » for "nurses" (don't widen the audience); « un tap », « d’une pression » (write « d’un seul toucher », « d’une touche »); « cédez » for "reach for" (adds guilt); « jeu » for a set of screenshots (reads as "game": « jeu de screenshots »); « dès que » for "once" in a condition; « compter à l’envers » / « décompter » for counting up or ticking people off (opposite meaning); « application compte à rebours » in prose (write « application de compte à rebours »; the noun-noun form only in keywords); « celles et ceux » doublets for a singular English subject; a missing « ne » (« déclare aucun »); « séchez » for being stuck; store IAP names where the English means the Settings label; « que Apple » without elision; « un jour sur sept » for "every seventh day". In policies: « bien » that strengthens a statement (« a bien été livré »), « n’y avons pas accès » for "we don't have it", « prélèvements » for charges (« débits »), « si » + conditional (« si nous préférerions »), « moyens de paiement » for payment details (« données de paiement »), agreement after a mixed-gender list.

Found in the Tier 2 reviews (2026-11-08): « sans paywall » (write « sans fonction payante »); « derrière le mur payant » (« réservé à la version payante »); « en un minimum de touches » for taps (« touchers »); « Ça fonctionne, et ça … » (spoken register); « sont de nous » (« sont les nôtres »); « est éditée par l’éditeur »; « pèse 15 % de » (« représente »); « travaille de pair avec » (« fonctionne avec »); « Curieux de savoir… ? » as a heading (gendered); gendered participles in a vous sentence (« où vous êtes éveillé »: rephrase with a noun); an app switching gender inside one page (always feminine, « l’app »); « Pourquoi » + noun subject without complex inversion; « (vérifiée le …) » after a plural or mixed subject; store IAP names quoted in prose (« Débloquez les packs et retirez les pubs ») instead of saying what the purchase does; store-language facts or competitor prices added where English is silent; narrowing calques (« pour le travail de nuit » for "shift workers": « travail posté ou de nuit »).

Found in the Tier 2 batch 2 review (2026-11-08): « le point de … est ailleurs » for "the point is"; « X n’est pas le bon choix : Y l’est » (English verb ellipsis); literal spatial metaphors (« l’effort tombe hors de l’écran »); « (en anglais) » after a product name to mean an English-only interface (readers take it for the link marker: write « dont l’interface est en anglais »); punctuation added inside a quoted competitor string; bold verdict labels (« À choisir si ») on every card (write « Convient surtout si », no bold); « y » after a sentence that names two places; feature counts that contradict each other across quick_answer, hero and section (« trois points » / « Cinq critères »).

Found in the Tier 3 batch 1 reviews (2026-11-08): « vit dans votre profil » for "lives in" (« est conservé dans »); « ses … » and « votre … » in one sentence; card titles that make the product the object of « vouloir » (« Convient surtout si vous voulez Chessful »: write « Chessful convient surtout si… »); « vrai échiquier » (« échiquier physique »); « contre des personnes » (« contre d’autres joueurs »); « Où tourne le moteur » in a heading (« Où s’exécute »); a widened claim (« réserve l’accès complet ») where English scopes it to one feature; gendered words in vous sentences: « vous vous entraînez seul » (« en solo »), « vous seul avez besoin de l’app » (« l’app n’est nécessaire que sur votre téléphone »), « être prévenu », « vous auriez été bloqué » (« les blocages que vous auriez rencontrés »), « Prêt à essayer ? » (« À essayer »), « lequel vous convient ? » about apps (« quelle app choisir ? »); a competitor treated as masculine next to a feminine « l’app » (« Hevy est gratuit »: « L’app Hevy est gratuite »); « faire bouger un score » (« faire varier »); « Comment X se compare-t-il à Y ? » (« X et Y : le comparatif »); « quoi que ce soit soit »; « à partir de » before a single price; « compte courant » or « solde courant » for a running tab (reads as a bank account: « solde commun »); « En partie » as the answer to "is X free?" for a free app with paid options; « chez vous » for "in your own country" (« près de chez vous »); « l’addition que vous avez sous les yeux » (« posée sur la table »); « d’une seule traite »; size adjectives on competitors without a source (« l’autre grande app »); « Les offres changent : vérifiez-les avant de changer » (« évoluent »); « ça marche » in FAQ answers; verb-less negation lists. Process tells: a competitor's exception repeated in every row (state it once, close to the store's wording); a footnote that credits the French store check with claims only the US listing supports (name both checks); quoting a competitor's button label the research doesn't show; store-description facts used to explain a missing price; two "effort" metrics on one page (add « (Strain) » to Whoop's every time). Hub and llms tells (R-wiring): « D’autres X existent en anglais : … (en anglais) » (language stated twice); a quick_answer opening on « Ces comparatifs » (nothing to point back to); « et plus » after a list of names in a title; the same verdict phrase on every hub card (vary « convient mieux », « reste le bon outil »); a verbless noun list for a workflow.

Found in the Tier 3 batch 2 reviews (2026-11-08): « l’App Store français ne lui connaît que l’anglais » (« d’après l’App Store français, … »); « abonnement compris » in a price question (« … et son abonnement »); « lequel du sommeil, de la VFC ou de… » (« ce qui l’a fait varier, entre X et Y »); « recevez Pousser » with a UI label as object (« obtenez »); « n’a rien de clinique » (« sans valeur clinique »); « bague » for the Oura ring (« anneau »); a subscription as the agent (« un abonnement qui réserve »: « une partie de l’analyse est réservée à l’abonnement »); « l’app saisit vos séries » (the reader logs: « permet de saisir »); « quand vous êtes connecté à iCloud » (« quand votre iPhone est connecté à votre compte iCloud »); « Option sans abonnement » as a label for an app that isn't (« Achat unique possible »); « X ajoute le côté social » (implies the other lacks it: « mise sur »); « modèle prêt » next to in-app « Modèles » (« préréglage »); UI-sounding names the app doesn't have (« éditeur de programmes »); a colon joining a fact to a verdict about another subject; « Combien coûte X, et combien coûte Y ? » (« Combien coûtent X et Y ? »); « pour quand vous vous ennuyez » (« pour tromper l’ennui »); « Ce qui survit à » (« ce qui reste intact »); a verb list ending on a bare noun (« chiffrer et OCR »); « bien plus complet » with nothing to compare against; « vous connecter » for sign in (« vous identifier »); U+202F added inside a quoted store name (quote it verbatim, or link « sa fiche » when it holds a dash); « fonctionne pour vous » (« fait son effet »); « continuez avec lui » (« continuez à l’utiliser »); « font le même métier » (« fonctionnent de la même façon »); « vous vaut une heure » (« rapporte une heure »); « On paie pour X en échange de » (« Si vous payez X, c’est pour… »); « hors un » (« à l’exception d’un »); « l’un ou l’autre » next to « laquelle » for two apps. Process tells: on « X en français ? » pages the language fact repeated in every block (quick_answer, H1, FAQ, footnote, at most one bullet); verdict filler added to a language FAQ; the competitor's English description dropped to make room for the language answer; an English billing period dropped where the store shows no in-app purchase (keep the period, drop only the amount); cards that set one competitor's store features against another's silence (say silence isn't absence); a visible FAQ answer longer than its schema text. Hub and llms tells (R-wiring-2): « propose … aucun compte » (negative item without « ne »); « tout gratuitement » (« toutes les fonctions gratuitement »); an unsourced superlative on a hub card; a hub quick_answer listing 20 names in one sentence (group by theme); a store-language fact on a card without the page's date; back-to-back cards opening with the same clause; « Voir la page X » as a standalone pointer (« Notre comparatif X … »).

Found in the Tier 3 batch 3 reviews (2026-11-08): Apple's French App Privacy labels must be quoted exactly (« Données utilisées pour vous suivre », « Données établissant un lien avec vous », « Données n’établissant aucun lien avec vous »; never « (non) liées à votre identité », « associées à vous », « liés à vous »); our price tokens are single-brace (`{P_MONTHLY@app}`; `{{P_…}}` is Liquid and doesn't render); doubled U+202F; a thousands group with a plain space (« 15 000 »: U+00A0); « remise(s) à zéro » for a weight reset (« baisse de la charge »); « vous fait reculer » (« baisse la charge »); « dedans » about an app's history; « est un autre outil : » as a colon reveal (« fonctionne autrement »); « semaines de décharge » where English says deloads; « écran d’accueil » for an app's own home screen (« l’écran d’accueil de l’app »); a Live Activity paraphrased (« Activité en direct »); made-up UI nouns (« constructeur de rotation »); « peut ne pas guider » for "may not be a reliable guide" (« n’est pas forcément un repère fiable »); « en passif » (« sans intervention »); gendered table labels (« Conçue pour »: « Public visé »); « recomparés » (« revérifiés »); « en une fois, à vie » (« à vie en achat unique »); « {P_LIFETIME} une fois » (« en achat unique »); a competitor's in-game jargon as a French noun (« une quotidienne »: « tâche quotidienne »); « Le téléchargement est gratuit jusqu’à 50 tâches » (« L’app est gratuite jusqu’à… »); « un suivi d’habitudes » as the noun for an app (« une app de suivi d’habitudes »); « payante » agreeing with a brand alone (« l’app Streaks installée »); « L’app est en anglais » (« n’existe qu’en anglais »); « X travaille vos erreurs » (« vous fait réviser vos erreurs »); « jusqu’à ce que le rappel soit automatique » (« les coups viennent d’eux-mêmes »); a yes/no question built from "What is an X alternative that…" (« Quelle alternative à X… ? »); « coûte-t-elle moins cher que » (« Combien coûtent X et Y ? »); « avant de payer » with no subject; « leur » for a company named in the singular. Process tells: a claim about a third competitor added to a FAQ; a French rating count in brackets after an older check date; two questions in one FAQ name; a plan list built from the store's truncated IAP rows; related-link framing that adds a reader situation; the same seo.title pattern on two pages for one app; a front-matter `title` reshaped around the query (keep « Alternative à X »); a platform fact slipped in through the language answer; a competitor price repeated in the footnote; a footnote that invents a US check date the English page doesn't give. Hub and llms tells (R-wiring-3): a writer rebuilding the hub JSON-LD put the ItemList into the breadcrumb and dropped `mainEntity` (always diff the JSON-LD skeleton against HEAD); a plain space plus U+202F before « : » in pasted names; verdicts forced by variety (« reste seule à recommander », « tournez-vous vers », « s’impose »); « gratuitement » for an app that only has a free version; a generic intent query routed to a competitor comparison instead of the app page; a hub quick_answer listing themes without naming the pairs.

Found in the Tier 4 batch 1 reviews (2026-11-08): « un frais de service » (always « des frais de service »; « relève des frais de service »); « un pourboire obligatoire … n’est pas un pourboire » (« un montant obligatoire »); a survey's hypothetical ("would tip") stated as a fact (keep the conditional); « nourriture » for a food bill (« repas »); « en bord de trottoir » for curbside; « Mail d’Apple » (« l’app Mail »); « la règle de travail » for a working rule; « vraie pièce jointe »; « avoir des décennies d’avance » for "decades older"; exercises as the subject of « se récupérer »; « série de tête » for top set and « séries allégées » for back-off (« série lourde (top set) », « séries de back-off »); « la fourchette repart de zéro »; « refaire la charge » (« reprendre la même charge »); « Inutile de… » that drops "rarely"; « split auquel vous pouvez assister »; « s’allonger dans l’autre sens »; « se plier » for a curve (« s’infléchir »); « allaient avec » for study associations (« étaient associés à »); « dans les hauts milliers »; « graphique de plage » (an invented Apple label); « de l’un à l’autre » for "into either"; « persiennes » for blinds; « vaseux »; « trajet simple » for one way (« trajet aller »); « en début de soirée » for "evening"; a neutral English group feminized (« des infirmières et des aides-soignantes »: « le personnel infirmier et aide-soignant »); odds described as risk (« cote multipliée par 1,95 »); gendered adjectives in vous advice (fatigué, frais, rassuré, endormi, « partez plus léger »: « dans la fatigue », « une fois la fatigue dissipée », « trouver ou garder le sommeil »). Process tells: an FAQ question rewritten as a worry question with a one-word softer answer; a hedge ("a good window", "rarely", "about") turned into a rule; a writer-added definition that slips in a claim (keep it to one neutral sentence); English link text left before « (en anglais) »; « Un exemple courant » with no source for the frequency; schedule variants or sequences on a local-only page that no fetched source gives; a source's advice moved into another context (a rest-day nap placed inside the night shift); a section H2 narrowed to iPhone when the English covers iPhone and Mac; read_time counted with front matter (body words only, ÷ 200); « N min » without U+00A0. Hub and llms tells (R-wiring-4): a `related_journal` anchor that keeps « (article en anglais) » after the post is translated (the layout then shows the French post with a false label: copy the French H1); « situent le bénéfice entre X et Y » for "grows up to X to Y, then flattens"; « ce qui pèse le plus est A, B et C » when the post lists more factors (« comptent parmi »); « les sources derrière »; pointers « sont dans notre article » / « voir notre article » (« Notre article X donne… »); a list in a title or description without « et » before the last item; an English-only line naming the same set twice; a plain space in « 10 000 pas ». Found in the Tier 4 batch 2 reviews (2026-11-08): a relative clause on « aller au bout » (« un programme que vous irez au bout »); « Aucun X n’a rien de… »; a hedge reversed by « tant que … loin de » for "until well past"; « un ou deux mois » for "a couple of months"; « ne remplacent pas un avis médical » for "not medical advice" (« ne constituent pas »); « athlètes de physique » (« culturisme »); app status labels paraphrased in lowercase when the catalog has them (« Pic de volume », « Repos insuffisant »); « se notent plus dur »; « repartir plus fort » for "push again"; English Wikipedia grades left bare (« article de qualité (featured article) » once); « éditeurs » for Wikipedia editors (« contributeurs »); « routes » for ways in; « collection commentée » for curated; « ce dont ils n’ont pas besoin » for "something they don't need"; « comment les jeux gratuits paient » (« se financent »); « StandBy » in prose (Apple FR « En veille »); "US prices" carried over (use the house line « Les prix indiqués sont ceux de l’App Store français… »); « jeux de recommandations »; « chat conversationnel » on a pet page; « Où X s’inscrit » (« La place de X »); « Seule X est obligatoire pour A » rewritten as « X n’est obligatoire que pour A » (changes the scope); « ouvert la nuit » for after-hours (« de garde »); « vétérinaire accrédité » (« habilité »); a source’s « doit veiller » softened to « recommande »; « passe à travers le mode de concentration » (« passe outre »); gendered participles in subscription prose (« vous vous êtes inscrit », « vous seul »); « bloquer » for "brick" (« rendre inutilisable »); « livraison » of a notification (« réception »); « par conception » (« à dessein »); « Niveaux de gris » (Apple: « Nuances de gris »); « balayage » of a statement (« examen »); a button label invented in « ». Process tells: a replaced competitor’s capabilities moved onto the French stand-ins through an FAQ question that names them; "by itself" dropped (inverts the claim); a local-only page claiming "no obligation" from the silence of the pages read when another official page states one; a French source’s rule merged with another source’s advice (embassy vs transport company). Hub and llms tells (R-wiring-4b): routing lines pasted with plain spaces before « : » and « ; » (check every new line for U+202F); a pointer sentence placed before a pronoun sentence (« Il est gratuit » then refers to the article: put the pointer last); « en repartant » for "expect to start" (« quitte à »); « des A jusqu’à B » for a list where B is not last; a French query answered only with English-Wikipedia facts; « compteurs de séries » for streaks on a gym-heavy site (« compteur de série (streak) »); « la fiche révèle » for "can usually be spotted"; the same query on an app line and a journal line, or an app-intent query on a journal line; a verb ellipsis between two links; a comma that widens « Seule … obligatoire pour »; U+00A0 inside « 6 à 8 semaines » (only before the unit).

Found in the Tier 4 batch 3 reviews (2026-11-08): an H2 reshaped around the search query narrows a section that covers more (put the query in the H1 and seo.title only); a query-first quick_answer followed by « cinq outils restent gratuits » implies the queried task is free (say whether it is); link anchors built on an English-title metaphor the French title dropped (« l’ascenseur »); « réflexe par défaut »; « ne crois pas que » + indicative; « son parent » (« sa mère ou son père »); « l’un des cent sites » (« l’un de la centaine de »); « de loin » for “loosely” (« à peu près »); « avance » for a piece that moves in every direction (« se déplace »); « un échec de » in chess prose (« défaillance »); « défense Philidor » for the rook ending (« position de Philidor »); « s. o. » (« sans objet »); « louer » next to rented compute; « changer de coup » for “deviate”; one phrase (« dernière rangée ») for both back ranks; « en plein élan d’envie » (« au plus fort de l’envie »); « laisse le payeur à X € de moins »; a vous version invented for an app string that is tu in the catalog (paraphrase instead); « vous l’auriez été » (a gendered participle hidden by elision); feminine agreement for RightSplit (masculine on its page); Apple Health labels invented from the watch app (« niveaux de bruit environnants »: Apple says « Niveaux sonores ambiants »; « Heures où l’on se lève »: « heures debout »); « VO₂ max » masculine (the site writes it feminine); a source’s hedge turned into fact (“often proposed as essential”); « surtout » for “only”; plain spaces before % and RM; a comma before « et » ending a list in a lede.

## Decisions from the Tier 1 reviews (2026-11-08)

- Apple's sleep stages in prose: éveil, sommeil paradoxal, sommeil lent, sommeil profond (Apple FR). Observa's UI label « Noyau » is not used in prose; AfterShift quotes its own UI labels (Éveillé, Léger, Profond, Paradoxal).
- « Demander l’autorisation d’achat » for Ask to Buy (Apple FR, support.apple.com/fr-fr/105055).
- Each app page may carry the FAQ « <app> existe-t-il/elle en français ? » (rulebook 6.2 local question; answered from the glossary verdict, naming the English-only gaps).
- Support pages: « annuler abonnement <app> » only for the 17 apps that sell a subscription; `support_words` tightened so the support pages pick pricing, offline, sync and platform questions (3 to 6 per app).
- The support hub states only what the English support page, layout and privacy pages state (no refund menu path of its own).
- Tier names follow the French UI except AppMeta Pulse, which keeps the English site's « Pro » (the app has no tier name; owner question below).
- Prices on comparison footnotes stay as the English page dates them (US App Store checks); no French competitor price was added.
- The transparency page keeps Apple's two ATT button labels in one parenthesis (accurate per fr-apple-terms.md; owner may drop for strict parity).

## Decisions from the Tier 2 reviews (2026-11-08)

- Competitor prices on French pages: the EUR row from the French App Store, typed with U+00A0 before €, plus a dated line
  « vérifiés dans l’App Store français le 8 novembre 2026 ». Only where the English page states an amount; where English gives
  only the plan structure, no French price is added (owner question below). Several rows for one product: « à partir de » the
  lowest, or the listed range. Arithmetic on competitor prices (the ten-year box) uses the lowest current monthly row.
- A competitor not sold in the French App Store is marked « absente de l’App Store français (vérifiée le 8 novembre 2026) »
  and kept out of every pick and ItemList. Shogi Wars, Shogi Quest Online and Kakinoki Shogi are absent (Shogi Wars and
  Shogi Quest are sold in BE and CH); the Tier 1 Shogiful page and /fr/llms.txt now say so where they sent readers to it.
- Hubs list only the French children; untranslated pages are listed under « Uniquement en anglais » in /fr/llms.txt.
- No hand-typed « Mis à jour en <mois> » overline on guides and /for/ pages: the layout prints the date.
- « Fédération japonaise de shogi » for the Japan Shogi Association (as on the Shogiful page).
- Primary queries keep the noun-noun search form only in seo.title and keywords; H1 and prose write « application d’échecs ».

## Decisions from Tier 2 batch 2 (2026-11-08)

- Local-only pages (TRANSLATION.md 6.7): `local_only: true`, no `ref`, French ASCII slug, canonical to itself, no hreflang or switcher (the templates
  already handle it). Hub cards link them with a plain `/fr/...` href (`l.html` only maps English URLs). An English twin can come later: add `ref`
  to both and drop `local_only`; the French slug stays.
- Our own rating counts are never stated on a French page (not even « pas encore de notes »); competitors’ French rating counts may be cited as a
  popularity signal with the dated check line.
- `{PLATFORMS}` prints OS names (« iOS, iPadOS, macOS »). In prose, use the Liquid device list `fr/index.html` uses (« iPhone, iPad et Mac »);
  the token is acceptable only as a label in front matter strings (owner question: a device-name token).
- Tier 1 pages that send readers to an app not sold in France get the same note as Shogi Wars: the French AllPaid FAQ now says Rocket Money is not
  sold in France and points to the guide; its budget FAQ names Bankin’, Linxo and YNAB instead of Monarch Money and Copilot (not sold in France).
- Apple Screen Time in iOS 27: « Temps accordés » (how long per day, the old App Limits) and « Programme de temps d’écran » (when, the old
  Downtime), checked against support.apple.com/en-us/guide/iphone/iphb0c7313c9/ios on 2026-11-08. Old names only « sur iOS 18 et versions antérieures ».

## Decisions from Tier 3 batch 1 (2026-11-08)

- Comparison pages: `isPartOf` `{{ site.url }}/fr/#website`; breadcrumb « Lagerland Apps » → « Comparatifs » (/fr/alternatives/) → the page `title`; `inLanguage: "fr"` on every JSON-LD block. The hub lists only the French pages and links the English hub with a plain href, hreflang="en" and the marker.
- Competitor facts: French store rows and descriptions replace US-store facts; a US-only claim the French store doesn't show is kept as English states it, and the footnote names both checks (US listing with its English date, French listing on 8 November 2026). One competitor French rating count per page, dated. One « X existe-t-il en français ? » FAQ allowed, answered from the store language list.
- No EUR amount where English gives none (Tricount, Splitwise, Chess.com, Lichess, one sec, Whoop). Whoop's membership: no amount and no claim about where it is sold; the footnote states only what the store shows (free app, no in-app purchase listed).
- Gender: a brand name used alone may be masculine (« EarnLock fonctionne-t-il », as the French app pages write it); « l’app X » is always feminine; never both for one app in one sentence.
- The search form « Alternative X » (no « à ») is allowed in seo.title and seo.description, not in H1 or prose.
- Local-only comparison: `/fr/alternatives/alternative-bankin/` (AllPaid vs Bankin’, Linxo as second example); competitor prices from the French store rows with the dated line; no security claims beyond the connection route (Bridge, ACPR) and the app lock; linked from the bill-tracker guide and the AllPaid FAQ.
- The chess guide's « Comparaisons détaillées » line carries one English marker per link (it used a single probe on the Chess.com link).
- Owner decisions, 2026-11-08 (on the batch's open questions):
  - Opal: the US-listing-only claims (block screens with quotes, Sign in with Apple, the Family Sharing note) stay as
    the English page states them, with the footnote naming which listing each comes from.
  - Forest on Apple Vision stays off the French page while the French listing doesn't show it.
  - Bankin’: keep the connection route (Bridge by Perspecteev, ACPR) and the app lock; nothing else about security.
  - Gender confirmed: a brand name alone may be masculine (« EarnLock fonctionne-t-il »), « l’app X » is feminine.

## Decisions from Tier 3 batch 2 (2026-11-08)

- An app's gender for the brand alone follows its French app page: GymLogger X, WanderWiki and EarnLock masculine; Observa feminine on the reviewed comparison pages (« Observa explique », « elle »); « l’app X » always feminine.
- Observa's free first week: « toutes les fonctionnalités Premium sont débloquées pendant vos 7 premiers jours » (app page wording; it is an in-app week, not the App Store {TRIAL}, and has no token).
- A competitor whose French store lists no French: say « d’après l’App Store français » with the date, once per block type; it answers « X en français ? » queries (Athlytic, Welltory, Fitbod).
- PDF Expert: the French IAP rows don't name their periods, so only the range « de 9,99 € à 84,99 € » (dated) with no period; the English lifetime option is attributed to the US listing.
- Oura: the French store's device list includes Apple Watch, so the French page doesn't repeat the English « no Apple Watch app » row (English-side issue).
- Local-only « Splid ou Tricount » page: Splid facts from its French store description and rows only; Tricount facts only from the reviewed French Tricount page; the page says the listings differ clearly only on price, and that silence on a point isn't absence.

## Decisions from Tier 3 batch 3 (2026-11-08)

- Brand gender, confirmed from the French app pages: AfterShift, Taskful Day, GymLogger X, EarnLock, WanderWiki masculine alone; Observa and Chessful feminine; « l’app X » always feminine.
- When the English page has no dated competitor check, the footnote covers only the French check (no invented US date).
- Competitor IAP rows are a truncated list (at most 10): never infer which plans exist from them; name the product only, or the amounts English states.
- Store descriptions that confirm an English claim may sharpen it only in the footnote; a store claim where English says something vaguer (« ni publicité ni pistage » vs "standard disclosures") is not added.
- No local-only page this batch: Sleep Cycle and Pillow belong on the English site first.

## Decisions from Tier 4 batch 1 (2026-11-08)

- Journal posts: `date` and `last_updated` 2026-11-08 (publish day), `translated_from` = the English `last_updated`, `read_time` « N min de lecture » with U+00A0 (body words ÷ 200, front matter excluded). The first person singular stays where the English essay uses « I » (« j’ai conçu »); the studio is never named as a person.
- External sources whose page is in English carry `{: hreflang="en"} (en anglais)` once, on first mention; Apple links go to the support.apple.com/fr-fr page with the same content, without a marker. US agencies and US-only facts stay as facts about their source; no French authority is added to a translated post.
- US tipping post: dollar amounts in French format (« 15 $ », « 8,25 $ »); US terms that a bill prints stay in English in brackets after the French (« pourboire automatique (automatic gratuity) »).
- Email post: « mail » in prose, as in the query « par mail » (owner may prefer « e-mail », ISSUES.md). Units Mo, Go, Mbit/s, kbit/s; UI labels quoted as the MediaKit catalog writes them (« 64 kbps (voix) »).
- Apple Watch rings: the green ring is « M’entraîner » and shows minutes of « effort intense » (support.apple.com/fr-fr/guide/watch/apd3bf6d85a6).
- Shift work: « 3x8 » (search form) in journal prose and titles; « 3×8 » only as AfterShift's preset name. Local-only /fr/journal/travail-en-3x8/: definitions from INRS (FAQ and brochure ED 6305), health effects from ANSES (22 June 2016), daily rest of 11 consecutive hours from Code du travail L3131-1 (checked on code.travail.gouv.fr, Légifrance blocks scripts); no pay, bonus or retirement rules.
- Gym vocabulary: force athlétique, pareur, barres de sécurité, exercices polyarticulaires, rowing haltère, effort perçu, super-séries (LiftLog UI « Super-série »), single / double, série lourde (top set), séries de back-off; « volume de charge (le tonnage) ». GymLogger X statuses as on its French app page (« Plateau détecté », « À surveiller », « Plateau prévu »; the analytics catalog says « Plateau », ISSUES.md).
- Inbound links: each post is linked from its app's French FAQ (GymLogger X, EarnLock, Observa, RightSplit, MediaKit), AfterShift's related_journal, and a « À lire aussi dans notre journal » line on /fr/for/shift-workers/ and the workout guide.

## Decisions from Tier 4 batch 2 (2026-11-08)

- Pet vaccines: core = « vaccins de base », non-core = « vaccins facultatifs (non-core) » on first mention (native call open, I-0267). French disease names: maladie de Carré, hépatite de Rubarth / adénovirose, parvovirose, leptospirose, toux du chenil, typhus, coryza, leucose féline; CHPPi / CHPPiL and « typhus-coryza » glossed once. AAHA = American Animal Hospital Association (« l’association américaine des hôpitaux vétérinaires »); USDA's accredited veterinarian = « vétérinaire habilité ».
- French rabies rule (vaccination and passport posts): only as the sources word it: agriculture.gouv.fr « Seule la vaccination contre la rage est réglementairement obligatoire pour les animaux voyageant hors de la France et pour les chiens de catégorie 1 et 2 » (and in Guyane); service-public F1839 / F36479: from 12 weeks (3 months), valid 21 days later, annual booster / frequency in the passport; F1839: category 1 and 2 dogs need the passport even inside France.
- A translated post may name a French equivalent of an English-only feature only when fetched and verified (fr.wikipedia « Article au hasard », Spécial:Page au hasard, « Le saviez-vous ? »; Apple FR « En veille », « Nuances de gris », « Partager entre les appareils », « Filtres de couleur »).
- Illustrative amounts in a US-written example may become euros when they are not a real service's price (subscription post: 99 €, 8,25 €); competitor prices stay as the English states them (Brick « environ 59 $ »).
- Bankin’ and Linxo stand in for Rocket Money only with the facts of the reviewed French pages (alternative-bankin, bill-tracker guide); an FAQ never lets Rocket Money's English capabilities pass to them.
- Inbound links this batch: Pawza FAQ (vaccination, passport) and related_journal (records), GymLogger X FAQ (deload), Millrace FAQ (games), WanderWiki FAQ (Wikipedia), EarnLock and Soon. related_journal anchors set to the French H1s, the countdown guide « À lire aussi » line (plan mode), batch-1 posts (double progression), and the Bankin’ page and screen-time guide through l.html (subscriptions, blocking).

## Decisions from Tier 4 batch 3 (2026-11-08)

- English fixed first when a writer found an error (same commit as the batch): Shortcuts on iPhone and Mac in both MediaKit posts, the app page FAQ and app_enrichment (I-0146, partly); the elevator post no longer says MediaKit « shipped » before its release and says HEIC conversion needs Pro (I-0145); 30-chess motifs #7 and #29 (I-0095), #27 renamed “Winning endgame simplified into a draw”, and Chessful’s type is “Missed Back-Rank Mate” (blueprint §6) in three posts; engine-depth’s inconsistent cost figures removed; the unsourced step comparison removed from apple-health-metrics (I-0014, second half); EarnLock halfway and “Earn it” wording corrected in unlock-cost (I-0084, I-0085, that post only); RightSplit’s pay link removed from bill-splitting (false in 1.9.1) and the free first scan described with its item assignment. German twins synced where the English changed (apple-health-metrics, bill-splitting, MediaKit app FAQ; de/apps/mediakit stays stale for older edits).
- Restaurant bills in France: menu prices include taxes and service (service-public.fr F22387: « taxes et services compris »); the US tax-and-tip example becomes an optional pourboire split in proportion, with recomputed euro examples. US tax rules stay as facts about the US.
- Bank aggregation (AllPaid post): facts only from the ACPR page and the Banque de France FAQ (fetched with a browser User-Agent). No re-authentication day count: the BdF FAQ still says 90 days, Regulation (EU) 2022/2360 sets 180 days since 25 July 2023, so the post says « régulièrement ». Plaid stays as a US example.
- Apple Health labels checked on support.apple.com/fr-fr: « heures debout », « minutes d’exercice », « étages montés », « Niveaux sonores des écouteurs », « Niveaux sonores ambiants », « Température au poignet », rings « Bouger », « M’entraîner », « Me lever », and « calories actives » for the Move ring (iph4c34a8a95). Metrics without a verified label are described in plain French.
- Chess: French notation (Fd3, De2, Cf4); « demi-coup » for ply; « position de Philidor » (endgame) and « pont de Lucena »; the short-side defence keeps its English name with a gloss (no French source found); « flying general » kept in English in brackets in the xiangqi post (fr.wikipedia describes the rule without naming it). Xiangqiful pieces as the catalog: général, conseiller, éléphant, cheval, chariot, canon, soldat; the horse’s « jambe ».
- Query moves: « contourner temps d’écran iphone » stays with what-an-iphone-app-can-actually-block (unlock-cost takes « application anti scroll »); « surcharge progressive » moves from double-progression to the local-only post; « échecs chinois règles » moves from the xiangqi guide to the rules post; « partager l’addition entre amis » moves from the RightSplit app line in llms.txt to the bill-splitting post.
- Inbound links: compress-a-video post (both MediaKit posts), steps post (Apple Health metrics, unlock-cost), blocking post (unlock-cost), subscriptions post (bank login), chess guide anchors (both Chessful posts), xiangqi guide card (rules post), double-progression definition (surcharge progressive), RightSplit and AllPaid related_journal anchors set to the French H1s.

## House rules carried over

- No dashes; no roadmaps or dated promises; prices, counts, platforms and dates only through tokens and includes.
- « sans abonnement » only for LiftLog, Millrace, Mockly and Tare. For the others: « aucun abonnement
  obligatoire » or « aussi en achat unique », where true.
- « calme » / « serein » (calm) and « respectueux de la vie privée » (privacy-first) once per page, where they
  state positioning.
- Millrace never mentions "2048". Observa's HRV is SDNN (Apple Health), never RMSSD.
- Never the owner's personal name. App names, competitor names and "Lagerland Apps" stay as written in English.

## Review log

| Page | Writer | Copy-editing + fact diff + glossary | Back-translation | Native review |
|---|---|---|---|---|
| `_data/i18n/fr.yml` | writer agent (Sonnet) with self copy-edit | reviewer agent 2026-11-07, 17 must-fix + 15 should-fix applied; site_title rewritten by the main session for the home query | n/a | no native review yet |
| `fr/` home | writer agent | reviewer R1 2026-11-08: 2 must-fix, 5 should-fix | 2026-11-08, 55 claims, 3 mismatches fixed | no native review yet |
| `fr/apps/` hub | writer agent | reviewer R1: 1 must-fix (extra guides button removed), 1 should-fix | n/a | no native review yet |
| 21 app pages | one writer agent each | reviewers R2 to R8 2026-11-08 (copy-editing, fact diff, glossary, app catalogs checked for UI names) | blind back-translation per page 2026-11-08, mismatches fixed by the reviewers | no native review yet |
| 21 support pages | 3 writer agents | reviewer R9 2026-11-08: all seo blocks rewritten; support_words string fixed by the main session | n/a | no native review yet |
| 21 privacy policies + Clippet terms | 7 writer agents | reviewers RP-A to RP-E 2026-11-08, sentence-by-sentence legal diff; « si nous préférerions » fixed on 13 pages | n/a | no native review yet |
| about | writer agent | reviewer R10 2026-11-08: 1 must-fix (gendered pronoun), 3 should-fix | 2026-11-08, 41 claims, 0 mismatches | no native review yet |
| support hub, transparency, `_data/i18n_transparency/fr.yml` | writer agents | reviewer R10 2026-11-08: support hub refund path removed (English doesn't state it), 8 data-file term fixes | n/a | no native review yet |
| /fr/llms.txt, /fr/llms-full.txt, OG cards | writer agent (45 routing lines) | main session checks (gate, i18n check) | n/a | no native review yet |
| Tier 2 batch 1: 5 guides, 3 audience pages | one writer agent (Sonnet) each | reviewers R-games and R-people 2026-11-08 (copy-editing, fact diff against English and the French-store check, glossary, SEO/schema); EUR prices not in English removed | n/a (Tier 2) | no native review yet |
| /fr/guides/, /fr/for/ hubs | writer agent (Sonnet) | reviewer R-people 2026-11-08 | n/a | no native review yet |
| /fr/llms.txt Tier 2 lines, Shogiful Shogi Wars note, LiftLog and Xiangqiful guide links | main session | reviewer R-wiring 2026-11-08 | n/a | no native review yet |
| Tier 2 batch 2: bill-tracker guide, two local-only guides | one writer agent (Sonnet) each | reviewer R-b2 2026-11-08: 18 must-fix, 41 should-fix (Soon. ratings statements removed, iOS 27 Screen Time names, Forest claim corrected, platform token replaced in prose); competitor facts against the full French store descriptions | n/a (Tier 2) | no native review yet |
| /fr/guides/ hub (3 cards), /fr/llms.txt (3 routing lines), llms-full intro, AllPaid/Soon./EarnLock FAQ links, AllPaid FAQ fixes | main session | reviewer R-b2 2026-11-08: 1 must-fix (numberOfItems), 5 should-fix | n/a | no native review yet |
| Tier 3 batch 1: 9 comparisons + local-only Bankin’ page | one writer agent (Sonnet) each | reviewers R-money, R-chess, R-screen, R-fit 2026-11-08 (copy-editing, fact diff against English and the French store check, glossary, SEO/schema): 64 must-fix in all, e.g. Venmo and « ni abonnement » restored on Tricount, Whoop « sold outside the App Store » and sensor claims removed, Forest partner name and Vision removed, Opal Concentration profonde stated once, Chess.com cloud claim scoped to Game Review, isPartOf unified | n/a (Tier 3) | no native review yet |
| /fr/alternatives/ hub, /fr/llms.txt (10 routing lines, query moves), RightSplit/AllPaid FAQ links, bill-tracker and chess guide links | hub and llms lines: writer agent (Sonnet); links: main session | reviewer R-wiring 2026-11-08 | n/a | no native review yet |
| Tier 3 batch 2: 9 comparisons + local-only Splid page | one writer agent (Sonnet) each | reviewers R-health, R-gym, R-tools, R-b2-last 2026-11-08: about 45 must-fix, e.g. Oura « abonnement mensuel » restored without amount, Athlytic and Welltory verdict filler and added facts removed, Welltory Mindfulness removed, PDF Expert trial and feature lists removed, Wikipédia offline and « près de 300 » removed, GymLogger X and WanderWiki gender aligned with their app pages, Splid quick_answer made to answer the query | n/a (Tier 3) | no native review yet |
| hub (+10 cards), /fr/llms.txt (10 lines, query moves), GymLogger X FAQ links, Tricount → Splid link, Whoop quick_answer | hub and llms lines: writer agent (Sonnet); links: main session | reviewer R-wiring-2 2026-11-08 | n/a | no native review yet |
| Tier 3 batch 3: 10 comparisons | one writer agent (Sonnet) each | reviewers R-health-3, R-misc-3, R-gym-3, R-taskful-3 2026-11-08: about 45 must-fix, e.g. CloudConvert price tokens in Liquid double braces and 19 doubled narrow spaces, Apple privacy labels quoted exactly, Alpha Progression Fitbod claim removed, Streaks « ni publicité ni pistage » removed, Habitica invented US check date removed, RISE melatonin caveat restored, StrongLifts « remises à zéro » fixed | n/a (Tier 3) | no native review yet |
| hub (+10 cards, group « Organiser sa journée »), /fr/llms.txt (10 lines) | writer agent (Sonnet) | reviewer R-wiring-3 2026-11-08 | n/a | no native review yet |
| Tier 4 batch 1: 9 journal posts + local-only travail-en-3x8 | one writer agent (Sonnet) each | reviewers R-fit-4, R-misc-4, R-health-4 2026-11-08 (copy-editing, fact diff against English, glossary and app catalogs, SEO/schema, typography; French sources of the 3x8 page re-read in raw text): about 75 must-fix, e.g. tipping « frais de service » contradiction and Pew conditional restored, 1RM added claim cut, « sans abonnement » added on the programs post cut, HRV FAQ 3 and the 60-day hedge restored, steps quick_answer meaning restored, 3x8 unsourced schedule variant and misplaced nap advice removed, Apple ring name « M’entraîner » | n/a (Tier 4) | no native review yet |
| /fr/journal/ hub, /fr/llms.txt (10 routing lines, Journal lines), inbound links on 7 French pages | hub and llms lines: writer agent (Sonnet); links: main session | reviewer R-wiring-4 2026-11-08 | n/a | no native review yet |
| Tier 4 batch 2: 9 journal posts + local-only passeport-europeen-chien-chat | one writer agent (Sonnet) each | reviewers R-gym-4b, R-misc-4b, R-pets-4b, R-screen-money-4b 2026-11-08 (copy-editing, fact diff, catalogs, SEO/schema; French public sources re-read in raw text): about 70 must-fix, e.g. passport « no obligation in France » corrected for category 1 and 2 dogs, rabies scope sentence restored, Rocket Money capabilities no longer passed to Bankin’/Linxo, « by itself » restored on the blocking post, microloading meaning reversal fixed, dead Apple link replaced, AAHA gloss corrected | n/a (Tier 4) | no native review yet |
| /fr/journal/ hub front matter, /fr/llms.txt (10 lines), inbound links on 9 French pages | hub and llms lines: writer agent (Sonnet); links: main session | reviewer R-wiring-4b 2026-11-08 | n/a | no native review yet |
| Tier 4 batch 3: 9 journal posts + local-only surcharge-progressive-musculation | one writer agent (Sonnet) each | reviewers R-media, R-chess, R-money-screen, R-health-gym 2026-11-08 (Opus; copy-editing, fact diff, catalogs, Apple labels, SEO, typography; French and EU sources re-fetched in raw text): about 70 must-fix, e.g. HEIC conversion implied free, Oxford commas, Philidor endgame name, an outdated 90-day DSP2 figure, Apple Health labels, hedges restored in the ACSM 2026 paraphrase | n/a | no native review yet |
| /fr/journal/ hub front matter, /fr/llms.txt (10 lines, 4 query moves, Journal lines), inbound links on 9 French pages | main session | checked in the gate (i18n check, seo-audit, preview at 320 px and desktop) | n/a | no native review yet |

## Apps still on English screenshots

MediaKit and Mockly (no French set; TRANSLATION.md 6.8). The other 19 apps, Clippet included, have complete
French sets in `assets/screenshots/<slug>/fr/` (placed 2026-10-28). Alt texts and captions are French regardless.
