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

## Open questions (English site vs app, found while building the glossary)

Details in fr-glossary.md. Most carry over from the German sheet's list; new from the French pass:

- GymLogger X ships a « Coach IA » string while the English site says there is no AI coach (code check needed).
- LiftLog's in-app tier labels (Juste / Bien / Généreux / Mécène) differ from its French App Store IAP names
  (Équitable / Correct / Généreux / Mécène). The site follows the app.
- Observa: « Débloquez Lifetime Access » half in English in the app; « Disponibilité » vs « préparation » for Readiness.
- Mockly: the French store sells no translation packs on its page; site says 39 locales, French subtitle says 50 langues.
- Shogiful: 8 opponent tiers in code vs the site's opponent count (as in the German sheet).
- Tare: the French store IAP is « Chapitres II–X », which matches the site (the German note « Kapitel II–IV » looks stale).
- WanderWiki: a weekly plan exists in the French store that the site does not list.
- From the Tier 1 reviews (English wording kept on the French pages until the owner decides; details in the
  session review logs, summarized in ~/Downloads/githubcode/fr-tier1-open-questions-2026-11-08.md):
  EarnLock partial unlock and shield rule vs blueprint; GymLogger X « Coach IA » string; AfterShift's two scores
  share one French UI string and its French Siri phrases may not ship; AllPaid « Services publics » vs « Charges »;
  AllPaid on iPad and Mac (master) but missing from the English home FAQ's Mac list; Millrace undo packs called
  « one-time purchases » in English value_points but consumable in the footnote; Millrace French store lists Mac
  and Vision; Tare policy says Chapters II to IV, store says II to X; Tare language count (English 50, store 44);
  AppMeta Pulse « Pro » vs no tier in the app, « 17 languages » = 17 localizations in 13 languages; AppMeta Apple
  ASC menu names in French vs English on Pulse; Soon. baby timeline weeks (France counts in SA); Soon. free pin
  limit implied but never stated; RightSplit tax/tip condition; Observa French screenshots 1, 2 and 10 address the
  reader with tu; Chessful French notation letters; « Autoriser l’accès complet » unconfirmed.

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

## Apps still on English screenshots

MediaKit and Mockly (no French set; TRANSLATION.md 6.8). The other 19 apps, Clippet included, have complete
French sets in `assets/screenshots/<slug>/fr/` (placed 2026-10-28). Alt texts and captions are French regardless.
