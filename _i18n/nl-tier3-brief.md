# Writer brief: Dutch (nl, Netherlands) Tier 3, batch 1 (comparison pages)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/nl-writer-brief.md` first and follow all of it.** This file adds what is different for Tier 3.
Where the two disagree, this file wins. Scratch folder for notes and anything you fetch (never write scratch files in
the repo): `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-UxGsub/f5e34407-a458-4d5c-863d-92d8a8cb7431/scratchpad/nl-t3/`
(below: `$S`).

## Your inputs

- The ENGLISH source page `alternatives/<slug>.html`: it holds the facts about OUR app and the comparison. Write from
  its meaning, as a Dutch copywriter would, not sentence by sentence.
- The ITALIAN page `it/alternatives/<slug>.html`: STRUCTURAL template only (Liquid, JSON-LD skeleton, table and card
  markup, how links and tokens are written, how the store-data sentences and the check-date line are placed, how US
  competitor data was replaced with one store's data, how known English-side errors were handled). The Italian page is
  reviewed and already avoids the English-side errors listed in ISSUES.md for these pages; follow its choices where they
  concern facts. Never translate from Italian; watch for Italian structures leaking in.
- `/Users/anttiaittamaa/Downloads/githubcode/nl-tier3-research-2026-11-19.md`: your page's row (Dutch primary query and
  the Dutch suggest phrasings that show demand). Your `seo.keywords` come only from that row, `_i18n/nl-keywords.md`
  or the research file's evidence column.
- `/Users/anttiaittamaa/Downloads/githubcode/nl-tier3-store-2026-11-19.md`: the competitor in the DUTCH App Store,
  checked today (Dutch store name, Dutch ratings, languages, in-app rows in euro, full Dutch description; Oura's EU web
  price).
- `_i18n/nl.md` (sheet: register je, typography, glossary, ALL of «Tells to cut»), `_i18n/nl-apple-terms.md`,
  `_i18n/nl-glossary.md` (your app's section), `_i18n/nl-keywords.md` (your app's section), and the Dutch app page
  `nl/apps/<app>/index.md` (its wording, tier names and feature names are reviewed: reuse them).
- The copy-editing skill `~/.claude/skills/copy-editing/SKILL.md`: read it and run its Seven Sweeps and AI-tell removal on
  your finished Dutch before you reply.

## Pages in this batch

| English source | Write to | Our app | Primary query (search form → visible form) | Structural model |
|---|---|---|---|---|
| (local-only) | nl/alternatives/wiebetaaltwat-alternatief.html | RightSplit | `wie betaalt wat alternatief` → «alternatief voor WieBetaaltWat» | it/alternatives/alternativa-a-splid.html |
| alternatives/tricount.html | nl/alternatives/tricount.html | RightSplit | `alternatief voor tricount` (twin `tricount hoe werkt het`) | it/alternatives/tricount.html |
| alternatives/splitwise.html | nl/alternatives/splitwise.html | RightSplit | `gratis alternatief voor splitwise` | it/alternatives/splitwise.html |
| alternatives/whoop.html | nl/alternatives/whoop.html | Observa | `whoop alternatief zonder abonnement` | it/alternatives/whoop.html |
| alternatives/oura.html | nl/alternatives/oura.html | Observa | `oura ring alternatief zonder abonnement` (twin `oura ring abonnement`) | it/alternatives/oura.html |
| alternatives/chess-com.html | nl/alternatives/chess-com.html | Chessful | `chess.com abonnement` (twin `chess com gratis premium`) | it/alternatives/chess-com.html |
| alternatives/forest.html | nl/alternatives/forest.html | EarnLock | `forest app gratis` | it/alternatives/forest.html |
| alternatives/hevy.html | nl/alternatives/hevy.html | LiftLog | `hevy app gratis` | it/alternatives/hevy.html |
| (local-only) | nl/alternatives/dyme-alternatief.html | AllPaid | `dyme app alternatief` | it/alternatives/alternativa-a-wallet-budgetbakers.html |
| alternatives/pdf-expert.html | nl/alternatives/pdf-expert.html | MediaKit | `pdf expert kosten` | it/alternatives/pdf-expert.html |

The hub `nl/alternatives/index.html`, the llms lines and the inbound links are done by the main session after your page.

**Keyword collisions** (Tier 1 and Tier 2 pages own these; never your primary or in your `seo.title`; a mention in body
text or a secondary keyword is fine): `rekening splitsen app`, `kosten delen app`, `bonnetje splitsen` (RightSplit);
`hrv apple watch`, `slaapscore apple watch`, `readiness score apple watch` (Observa); `schaak app`, `schaak app iphone`
(Chessful), `beste schaak app` (chess guide); `apps blokkeren iphone`, `apps blokkeren voor bepaalde tijd` (EarnLock),
`schermtijd beperken iphone` (screen-time guide); `krachttraining app`, `workout log app` (LiftLog), `gratis gym app`
(workout guide); `rekeningen bijhouden app`, `vaste lasten app`, `betalingsherinnering iphone` (AllPaid),
`huishoudboekje app zonder bankrekening` (bill-tracker guide); `video comprimeren iphone`, `pdf comprimeren`, `pdf
verkleinen` (MediaKit). The three RightSplit pages must not share a primary or a seo.title pattern; nor the two Observa
pages. `tricount of splitwise` may be a secondary on both; `splitwise of wie betaalt wat` on both Splitwise and WieBetaaltWat.

**Search forms vs spelling** (sheet decision): searchers type «forest app gratis», «hevy app gratis». Visible text uses
correct Dutch: «Forest-app», «de app Hevy», «Chess.com-abonnement». The raw search forms go only in `seo.keywords`.

## Competitor facts (TRANSLATION.md 6.4)

- Every fact about the competitor is per market. Use ONLY the Dutch store file (and what the English page says that is
  not market-specific, such as how the product works). A US price, US rating, US check date («checked 29 October», «US
  App Store») or US-only feature on a Dutch page is wrong.
- **Prices**: only the euro amounts in the store file's in-app rows (or Oura's EU web price, with its source), typed
  `€ 3,49` with U+00A0 between € and the digit, and «(Nederlandse App Store, bekeken op 19 november 2026)» once per page
  (Oura: «(website van Oura, bekeken op 19 november 2026)»). Several rows for one plan: «vanaf» the lowest, or a range
  «van € 25,00 tot € 27,95 per jaar», as the Italian page does. Rows are not labelled with a period when the row name
  doesn't say it (Splitwise Pro € 2,99 / € 29,99 / € 47,99: «Splitwise Pro kost in de Nederlandse App Store tussen € 2,99
  en € 47,99, afhankelijk van de periode»; never guess which is monthly). A plan the English page prices but the Dutch
  rows don't show: keep the qualitative fact («betaald abonnement», «per maand of per jaar») and drop the number. WHOOP:
  no Dutch price exists (store shows no rows, website blocked): keep it qualitative. Never convert dollars. Never
  arithmetic on OUR prices; on a competitor's euro price only where the English page does the same calculation.
- **Ratings**: only the Dutch count and average from the store file, as «In de Nederlandse App Store heeft het een 4,7 van
  de 5, op basis van 41.703 beoordelingen (bekeken op 19 november 2026)» (four digits without a dot: «1309»; five or more
  with one: «41.703»), or leave ratings out.
- Competitor names as in English (Tricount, Splitwise, WHOOP or Whoop as the English page writes it, Oura, Chess.com,
  Forest, Hevy, PDF Expert, WieBetaaltWat, Dyme). The Dutch store title at most once where it helps people find the app
  (Chess.com appears as «Schaken - Speel & Leer Online»). Competitor App Store links: `https://apps.apple.com/nl/app/id<ID>`.
- Whether a competitor has a Dutch interface: only from the store file's «NL UI», and only where the page talks about
  language. Hevy, Forest, WHOOP and PDF Expert listings have no Dutch; Tricount, Splitwise, Oura, Chess.com and
  WieBetaaltWat have. Dyme's listing text is Dutch but its language list doesn't show NL: don't claim either way.
- Feature claims about competitors: only what the English page says, cross-checked against the Dutch description. If the
  Dutch description contradicts the English page (a feature gone, now free, now paid), follow the Dutch store file and
  report the English-side error in your reply. Short quotes from a listing under 15 words; never put your own
  translation of an English listing in quotes.
- App Privacy labels: the store file has none. Where the English page points at a competitor's privacy label (Forest),
  say neutrally that the label is on its App Store page; never state what it says.

## Our apps' rules on these pages

- Prices only through tokens (`{P_MONTHLY@observa}` etc.), single braces, exactly as the Italian page writes them.
  Never put U+00A0 inside a token or a Liquid tag.
- «Geen abonnement» only for LiftLog (house rule). Observa, RightSplit, Chessful, EarnLock, MediaKit and AllPaid sell
  subscriptions: write «geen abonnement nodig» / «abonnement niet verplicht» or «levenslange optie / eenmalige aankoop»
  only where the English page and the catalog support it. The WHOOP and Oura pages answer the «zonder abonnement» query
  by stating the facts (WHOOP and Oura need a paid membership; Observa's daily scores are free and Premium has a one-time
  lifetime option, through tokens), never by calling Observa «zonder abonnement». A seo.title like «Whoop-alternatief
  zonder abonnement» must not read as if Observa had none: «zonder verplicht abonnement» is the Italian solution (ISSUES.md has
  the item on alternatives/whoop.html's «no subscription» keyword and FAQ).
- Observa: «HRV (SDNN)», never RMSSD as Observa's HRV; «Gereedheid» / gereedheidsscore (Observa's Dutch UI); tier
  Premium; de Gezondheid-app. Medical caveats on the WHOOP and Oura pages stay exactly as strong as in English.
- RightSplit: tier Pro+, «Ruimtes» (the Dutch page's word), «Verdelen per artikel»; RightSplit never moves money; its
  payment links as `nl/apps/rightsplit/index.md` describes them (the Siri phrase note if you quote one). Chessful tier Pro.
  LiftLog tiers Eerlijk / Goed / Genereus / Mecenas. EarnLock tier Premium. MediaKit tier Pro, «pdf» lowercase in prose.
  AllPaid tier Pro.
- Disclose that the app is ours where the English page does («Transparantie:» or a plain sentence that Lagerland Apps
  makes the app and publishes the comparison).
- «we/wij» only where the English says "we".

## Links

- Internal links with `{% include l.html url="..." %}` exactly as the Italian page writes them; never hard-code `/nl/`
  in body links (l.html picks the Dutch page when it exists at build time, else English with the marker). Every page in
  this batch will exist, so keep links between them through l.html where the English page links its twin. The two
  local-only pages and the hub are linked as plain `/nl/alternatives/<slug>/` hrefs.
- The hub in the breadcrumb: `{{ site.url }}/nl/alternatives/` with the name «Vergelijkingen».
- JSON-LD: absolute `https://lagerland.app/nl/...` URLs (or `{{ site.url }}/nl/...` as the Italian page writes them),
  `"inLanguage": "nl"` wherever the Italian page has `"it"`.

## Local-only pages (TRANSLATION.md 6.7)

Front matter for both: `layout: default`, `local_only: true`, NO `ref`, NO `translated_from`, the permalink below,
`title`, `quick_answer`, full `seo`, `last_updated: 2026-11-19`; FAQ visible + in JSON-LD; `datePublished` 2026-11-19 where
the model has one. Read the structural model AND `fr/alternatives/alternative-bankin.html` for the shape.

### `nl/alternatives/wiebetaaltwat-alternatief.html` (permalink `/nl/alternatives/wiebetaaltwat-alternatief/`)

- WieBetaaltWat (id 1154059529, seller Splitser BV) is the Dutch default for group expenses (★62.348, 4,7). Facts ONLY
  from its Dutch description and in-app rows in the store file: shared lists that every participant edits, an account
  («Log in of maak gratis een account aan»), balances, settling with iDEAL or Bancontact or a payment request, 150+
  currencies, receipt photos, recurring expenses, reminders. In-app rows: «WieBetaaltWat Ad-free € 2,99», «WieBetaaltWat
  Premium» € 1,99 and € 9,99, «Steun WieBetaaltWat» tips; the listing does not say what Premium adds: don't guess (you may
  say the app has an ad-free purchase, a Premium purchase and voluntary support payments). Its claim of 5 million users is
  its own marketing: attribute it («volgens de eigen productpagina») or leave it out. No claims about its security, data
  use or company beyond the listing.
- The honest angle, like the Italian Splid page: WieBetaaltWat is a shared ledger for a group that keeps adding
  expenses over weeks; RightSplit is for one bill or receipt you split now on your own phone (scan, split per item, send
  each person their amount and payment link), without accounts; Pro+ Ruimtes keep a running balance for a trip or house
  but only on your phone, without sync. Say plainly when WieBetaaltWat is the better choice (everyone adds expenses from
  their own phone; settling with iDEAL inside the app).
- RightSplit facts from `_apps/rightsplit.md`, `nl/apps/rightsplit/index.md`, its glossary section and APP_BLUEPRINT.md §10
  (`~/Downloads/splitit/APP_BLUEPRINT.md`, claims register only). Prices via `{P_…@rightsplit}` tokens.
- Tikkie: you may mention it once only as the store file describes it (payment requests; «Groepie» for group expenses;
  a Dutch bank account and a Dutch, Belgian or German phone number needed), e.g. in an FAQ «wie betaalt wat of tikkie»,
  and only if it helps the reader. Keywords: `wie betaalt wat alternatief`, `alternatief voor wie betaalt wat`, `wie
  betaalt wat hoe werkt het`, `wie betaalt wat gratis`, `wie betaalt wat of tikkie`, `splitwise of wie betaalt wat`.
- Link the Dutch Tricount and Splitwise comparisons once each (l.html).

### `nl/alternatives/dyme-alternatief.html` (permalink `/nl/alternatives/dyme-alternatief/`)

- Dyme (id 1438647102, Dyme B.V.) links your bank accounts and sorts transactions, per its Dutch listing. Facts ONLY from
  its Dutch description and in-app rows in the store file (Dyme Silver € 8,99 per maand, € 17,99 per kwartaal, € 59,99 per
  jaar; Dyme Gold € 12,99 per maand, € 24,99 per kwartaal, € 69,99 per jaar: the rows name their period, so you may give
  them). Its listing names banks (ING, ABN Amro, Rabobank, bunq, SNS, ASN, Regiobank, Triodos): you may say its listing
  names these. Its savings claim («€800 per jaar» or similar) is its own marketing: leave it out. Nothing about its security,
  data sharing or company beyond the listing. The query intent includes «dyme betrouwbaar» / «dyme app veilig»: answer
  honestly that this page can only say what the listing says and that AllPaid never connects to a bank; never judge Dyme's
  safety.
- The honest angle, like the Italian Wallet page: Dyme reads your bank to show spending and subscriptions; AllPaid is
  manual: you enter the bills you must pay and it reminds you before each due date, with no bank connection and no
  account. Say when Dyme is the better choice (you want automatic categorisation of bank transactions and an overview of
  subscriptions found in your bank).
- AllPaid facts from `_apps/allpaid.md`, `nl/apps/allpaid/index.md` (its wording, reviewed), its glossary section and
  APP_BLUEPRINT.md §10 (`~/Downloads/billreminder/APP_BLUEPRINT.md`, claims register only). Prices via `{P_…@allpaid}`
  tokens. Link the Dutch bill-tracker guide once: `{% include l.html url="/guides/bill-tracker-without-bank-connection/" %}`
  (it already compares AllPaid with Dyme, Wallet and Spendee: read it and stay consistent with it).
- Keywords: `dyme app alternatief`, `dyme alternatief`, `alternatief voor dyme`, `dyme betrouwbaar`, `dyme ervaringen`,
  `dyme abonnement kosten`.

## Per-page notes

- **tricount**: Dutch listing title «tricount - Uitgaven delen», NL UI, no in-app rows. The Dutch description is the source
  for anything about its free use and accounts; read it. «tricount hoe werkt het» deserves an FAQ only if the listing or
  the English page answers it.
- **splitwise**: Dutch average 3,3 from 531 ratings: give it in the same neutral sentence as any other rating, no comment.
  Price per the Splitwise rule above.
- **whoop / oura**: see Observa rules. Oura's EU price from the website line in the store file, with «na belasting voor leden
  in de EU». WHOOP: no price.
- **chess-com**: in-app rows Gold € 4,99 to € 49,99, Platinum € 6,99 to € 84,99, Diamond € 12,99 to € 124,99 (unlabelled
  periods: give «vanaf» or the range per tier, never call a row monthly or yearly). ISSUES has English-side claims about
  cloud analysis and free-tier limits that the store contradicts: follow the Italian page's handling.
- **forest**: rows «Monthly (Early Bird)» € 7,59, «Annual (Early Bird)» € 45,49 plus consumables (Sunshine Elixir,
  Crystal). «Early Bird» may be an introductory price: say «vanaf».
- **hevy**: Pro Monthly € 3,49 and € 4,49, Yearly € 26,49, Lifetime € 89,99. The LiftLog table cell «Read-only without Pro»
  for Hevy history is disputed (ISSUES): follow the Italian page.
- **pdf-expert**: many rows (Basic € 9,99, Premium € 44,99 to € 53,99, «Mac & iOS» € 84,99, Education € 42,99): give the
  range or «vanaf», never label a period the row doesn't name. MediaKit is not a pdf editor: keep the English page's scope.

## Lessons from the earlier reviews (fr, es, it, pt, nl Tier 2): the most common must-fix items

- Softened or hardened hedges; added definitions or framing sentences that carry a claim; FAQ answers that add facts.
- JSON-LD: keep the Italian skeleton exactly (WebPage / BreadcrumbList / FAQPage nesting; never paste an ItemList into the
  breadcrumb). Every FAQ `name` equals its visible `<summary>` character for character; the schema answer says the same
  as the visible answer. Valid JSON (no raw " inside strings, no trailing commas).
- No raw-keyword seo.titles («Forest app gratis: …»), no «(2026)» padding, no meta description opening with a question,
  no staged self-answered openers («Zoek je …?») in quick_answer or descriptions.
- Dutch tells from the sheet, all of them: «hij/het/zijn» for a named app, «X komt met Y», «zet X naast Y» for "compares",
  outcome claims, split compounds in visible text, «u», Flemish words, title-case headings, «de» before app names,
  «naadloos», «cruciaal», «niet alleen … maar ook», «Kortom», «Of je nu … of …», «Let op:» disclosures.
- Only the site owner's name is banned; keep a competitor's maker if the English page names one.

## Do NOT

Run `jekyll build`, `i18n.py map` or the stamp script; touch any file but your own page; edit English or any other
language's files; edit `nl/llms.txt`, the hub or any app page. Other sessions (Spanish, Italian, Portuguese) work in this
same checkout: never run `git` commands that change state (read-only `git show`, `git log` are fine). Don't fetch
apps.apple.com pages (rate limits; the store file has the data); the iTunes lookup API is fine.

## Reply with

The items in nl-writer-brief.md «Reply with», plus: the final H1 and seo.title (character count), every competitor fact
you dropped because Dutch data was missing, the competitor prices and ratings you used (with the store-file row), every
place where the Dutch store contradicted the English page, and whether you ran the copy-editing skill in full. Also write
these notes to `$S/notes/<slug>.md` for the reviewer.

---

## Batch 2 (2026-11-19)

Same rules as batch 1, with these differences. Research rows: «Batch 2» at the bottom of the research file. Store and web
data: `/Users/anttiaittamaa/Downloads/githubcode/nl-tier3-store-batch2-2026-11-19.md`. Scratch folder for notes:
`/private/tmp/claude-501/-Users-anttiaittamaa-Downloads-githubcode/f5e34407-a458-4d5c-863d-92d8a8cb7431/scratchpad/nl-t3b2/`
(write your notes to `notes/<slug>.md` there). The batch 1 Dutch pages in `nl/alternatives/` are reviewed and live: read one
or two for tone and the Netherlands-data patterns (rating sentence, check-date line, «Transparantie:» disclosure), and reuse
their wording where it fits. Read the «From the Tier 3 reviews» tells in `_i18n/nl.md`: they come from batch 1.

| English source | Write to | Our app | Primary query | Structural model |
|---|---|---|---|---|
| alternatives/opal.html | nl/alternatives/opal.html | EarnLock | `opal app gratis` | it/alternatives/opal.html |
| alternatives/bevel.html | nl/alternatives/bevel.html | Observa | `bevel app ervaringen` | it/alternatives/bevel.html |
| alternatives/welltory.html | nl/alternatives/welltory.html | Observa | `welltory app kosten` | it/alternatives/welltory.html |
| (local-only) | nl/alternatives/sleep-cycle-alternatief.html | Observa | `sleep cycle gratis` | it/alternatives/alternativa-a-sleep-cycle.html |
| alternatives/lichess.html | nl/alternatives/lichess.html | Chessful | `chess com of lichess` | it/alternatives/lichess.html |
| (local-only) | nl/alternatives/tikkie-alternatief.html | RightSplit | `tikkie alternatief` | nl/alternatives/wiebetaaltwat-alternatief.html |
| alternatives/fitbod.html | nl/alternatives/fitbod.html | GymLogger X | `fitbod abonnement` | it/alternatives/fitbod.html |
| alternatives/stronglifts-5x5.html | nl/alternatives/stronglifts-5x5.html | GymLogger X | `stronglifts 5x5 schema` | es/alternatives/stronglifts-5x5.html |
| alternatives/handbrake.html | nl/alternatives/handbrake.html | MediaKit | `alternatief voor handbrake` | it/alternatives/handbrake.html |
| alternatives/cloudconvert.html | nl/alternatives/cloudconvert.html | MediaKit | `cloudconvert betrouwbaar` | it/alternatives/cloudconvert.html |

**Primaries and titles must stay distinct** from each other and from batch 1: Observa now has five pages (whoop, oura,
bevel, welltory, sleep-cycle-alternatief); Chessful two (chess-com, lichess: chess-com owns `chess.com abonnement`, Lichess
owns `chess com of lichess`); EarnLock two (forest, opal); MediaKit three (pdf-expert, handbrake, cloudconvert); RightSplit
four; GymLogger X two. Extra collisions: `beste schaak app` (chess guide), `gratis gym app` (workout guide), `gym app apple
watch`, `apple watch krachttraining`, `workout app apple watch` (GymLogger X app page), `slaap app apple watch`, `slaapscore
apple watch` (Observa), `video comprimeren iphone`, `heic naar jpg`, `pdf comprimeren` (MediaKit), `schermtijd beperken
iphone` (screen-time guide).

### Per page

- **opal**: rows are labelled (Weekly € 4,99 and € 9,99, Monthly € 19,99 to € 22,99, Yearly € 99,99, «Opal Pro Yearly» € 79,99;
  «Opal Pro Subscription» € 49,99 has no period). Stay consistent with how `nl/guides/schermtijd-beperken-iphone.html` and
  `nl/alternatives/forest.html` describe Opal and EarnLock. ISSUES I-0369 also names opal.html's Apple Watch row: follow the
  Italian page.
- **bevel**: Bevel Pro Monthly € 17,99, Annual € 99,99, plus «Bevel Intelligence-credits» packs (€ 5,99 to € 59,99). The Dutch
  listing is in Dutch (NL UI). Observa rules as batch 1 (HRV (SDNN), «Gereedheid», «zonder verplicht abonnement»).
- **welltory**: rows name their product («1-Year Premium» € 89,99, «Welltory Premium (1 year)» € 101,99, «Lifetime Premium»
  € 349,99, monthly rows € 13,49). Welltory measures with the camera per its listing: describe only what the listing says.
  Keep every health caveat exactly as strong as English; no medical claims.
- **sleep-cycle-alternatief** (local-only): front matter as for the batch 1 local-only pages (permalink
  `/nl/alternatives/sleep-cycle-alternatief/`). Sleep Cycle facts only from its Dutch description and rows (Premium rows have no
  period: give the range «van € 2,99 tot € 45,99»). Observa facts from `nl/apps/observa/index.md` and
  `~/Downloads/HealthLogger/APP_BLUEPRINT.md` §10. **Observa has no alarm and records no sound**: never imply it replaces Sleep
  Cycle's alarm or snore recording; say plainly when Sleep Cycle is the better choice. No medical claims. Keywords from the
  research row (`sleep cycle gratis`, `kan je sleep cycle gratis gebruiken`, `sleep cycle abonnement`, `abonnement sleep cycle
  opzeggen`, `sleep cycle nederlands`, `sleep cycle apple watch`).
- **lichess**: free, no in-app rows, NL UI, ★54 4,2. Must stay consistent with `nl/alternatives/chess-com.html` and
  `nl/guides/best-chess-apps-iphone.html` (both reviewed). Chessful tier «Pro» as the Dutch app page writes it; sign-in is
  «inloggen», never «aanmelden».
- **tikkie-alternatief** (local-only, permalink `/nl/alternatives/tikkie-alternatief/`): Tikkie facts only from its Dutch
  description (payment requests via a link, paid back with iDEAL | Wero, no transaction costs per the listing, a Dutch bank
  account and a Dutch, Belgian or German phone number needed, «Groepie» for shared group expenses where friends need the app,
  Tikkie Terug cashback, a business version for ABN AMRO business customers). Its security sentence («Je gegevens zijn dus
  veilig») is its own marketing: never repeat it as a fact. The honest angle: **RightSplit is not a payment app and never moves
  money**. It works out who owes what from a receipt (per item, tax and tip) and sends each person their amount, with a payment
  link only for PayPal.me or Revolut as primary method (Venmo and Wise open your profile; IBAN and Apple Pay add no link; no
  iDEAL link): see `nl/apps/rightsplit/index.md` and `~/Downloads/splitit/APP_BLUEPRINT.md` §10. Say plainly that if you want
  someone to pay you with iDEAL, Tikkie (or your bank's own payment request) is the tool, and that RightSplit is for splitting
  the bill first; many people use both. For «tikkie alternatief buitenland/belgie» searchers: say only what the listing says
  (a Dutch bank account is needed; Belgian and German phone numbers are accepted); never name other payment services as
  alternatives (no source). Link the Dutch WieBetaaltWat page once (plain href) because Tikkie's Groepie is a shared group list.
  Keywords: `tikkie alternatief`, `alternatief voor tikkie`, `tikkie alternatief buitenland`, `tikkie of betaalverzoek`.
- **fitbod**: rows Monthly Plan € 13,49 to € 17,99, «A Year of Fitbod Elite» € 81,99 and € 99,99, «(Legacy Pricing)» rows: leave
  the legacy rows out or say they exist. GymLogger X facts from `nl/apps/gymlogger-x/index.md` (reviewed Dutch UI names:
  ‘Krachtvoortgang’, ‘Wordt bewaakt’, ‘Plateau voorspeld’) and `_apps/gymlogger-x.md`; prices via `{P_…@gymlogger-x}` tokens.
  Stay consistent with `nl/guides/workout-app-without-subscription.html` (its Fitbod price sentence).
- **stronglifts-5x5**: rows labelled (Pro Weekly € 4,99, Monthly € 11,99, Quarterly € 29,99, Yearly € 59,99, «5 Years» € 199,99
  and € 249,99). NL UI. Dutch query `stronglifts 5x5 schema`: describe the 5x5 program only as the English page does (no new
  training advice).
- **handbrake**: not on the App Store. Facts from the store file's handbrake section (handbrake.fr, fetched today): free,
  open source, no account, Windows/Mac/Linux, no iPhone app. No «App Store» claim and no rating for HandBrake. The Dutch
  query `handbrake gratis downloaden nederlands`: never claim a Dutch interface (unknown).
- **cloudconvert**: a web service (plus an English-only iPhone app with ★6: no rating sentence). Free plan facts verbatim from
  the store file (€ 0, 10 conversion credits per day, 1 GB, 5 minutes); paid amounts are not in the fetched page: keep them
  qualitative. Files are uploaded to CloudConvert's servers; MediaKit converts on the device: that is the comparison. The
  query `cloudconvert betrouwbaar`: answer only with facts from the English page and the pricing page (no security verdict).

---

## Batch 3 (2026-11-19)

Same rules as batches 1 and 2. Research rows: «Batch 3» in the research file. Store and web data:
`/Users/anttiaittamaa/Downloads/githubcode/nl-tier3-store-batch3-2026-11-19.md`. Scratch for notes:
`/private/tmp/claude-501/-Users-anttiaittamaa-Downloads-githubcode/f5e34407-a458-4d5c-863d-92d8a8cb7431/scratchpad/nl-t3b3/notes/<slug>.md`.
Twenty reviewed Dutch comparisons are live in `nl/alternatives/`: read two or three for tone and patterns (forest and opal for
EarnLock, pdf-expert and handbrake for MediaKit), and read every «From the Tier 3 reviews» tell in `_i18n/nl.md` (batches 1 and 2).

| English source | Write to | Our app | Primary query | Structural model |
|---|---|---|---|---|
| alternatives/brick.html | nl/alternatives/brick.html | EarnLock | `brick telefoon` | de/alternatives/brick.html |
| alternatives/unpluq.html | nl/alternatives/unpluq.html | EarnLock | `unpluq` | de/alternatives/unpluq.html |
| alternatives/one-sec.html | nl/alternatives/one-sec.html | EarnLock | `one sec app gratis` | it/alternatives/one-sec.html |
| alternatives/screenzen.html | nl/alternatives/screenzen.html | EarnLock | `screenzen gratis` | es/alternatives/screenzen.html |
| alternatives/documents-by-readdle.html | nl/alternatives/documents-by-readdle.html | MediaKit | `documents by readdle gratis` | it/alternatives/documents-by-readdle.html |
| alternatives/flow-free.html | nl/alternatives/flow-free.html | Millrace | `flow free gratis` | it/alternatives/flow-free.html |
| alternatives/two-dots.html | nl/alternatives/two-dots.html | Millrace | `two dots gratis` | it/alternatives/two-dots.html |
| alternatives/nonograms-katana.html | nl/alternatives/nonograms-katana.html | Tare | `nonogrammen` | pt/alternatives/nonograms-katana.html |
| alternatives/autosleep.html | nl/alternatives/autosleep.html | Observa | `autosleep app` | es/alternatives/autosleep.html |
| alternatives/strong-workout-app.html | nl/alternatives/strong-workout-app.html | GymLogger X | `strong app gratis` | it/alternatives/strong-workout-app.html |

German, Spanish and Portuguese models are structure only: write from English, never translate from them.

**Distinct primaries and seo.title patterns** across all 30 Dutch comparisons. EarnLock now has six pages (forest, opal, brick,
unpluq, one-sec, screenzen): no two may share a title formula (avoid «X-app gratis …» on more than one; avoid «Alternatief voor X: …»
reused). Collisions to avoid as primary or in seo.title: `apps blokkeren iphone`, `schermtijd beperken iphone` (EarnLock / guide),
`logische puzzel app`, `puzzel app zonder reclame` (Millrace), `beste puzzelgames iphone`, `denkspelletjes app`, `breinbreker` (Tare),
`puzzelspellen voor volwassenen`, `nonogram app` (logic guide: `nonogram app` may be a secondary only), `slaap app apple watch` (Observa),
`gratis gym app` (workout guide), `gym app apple watch` (GymLogger X), `pdf comprimeren` (MediaKit).

### Per page

- **brick**: Brick is a physical device plus an app. The Dutch store listing has no in-app rows. Device prices from the maker's site
  were served for Finland: give NO device price; say the device is sold on the maker's website (getbrick.com), «Brick Night» exists
  per that site. No press quotes. EarnLock is software only: say so as the English page does.
- **unpluq**: Unpluq Tag (NFC) plus the Unpluq app; Premium in-app rows € 5,99 per month and € 54,99 per year (rows name the period);
  the site says the Tag works via the app with Premium required; no device price (Finland pricing). The seller, Unplug Technology B.V.,
  is a Dutch company: you may say so once; nothing more about the company. Its «1h 20m» claim: attribute or leave out.
- **one-sec**: rows labelled (pro 1 Month € 4,99, 1 Year € 14,99, Lifetime € 99,99, Family Plan 1 Month € 7,99, 1 Year € 24,99, Family
  Lifetime € 179,00). NL UI. Stay consistent with `nl/guides/schermtijd-beperken-iphone.html`.
- **screenzen**: free; its in-app rows are tips («Kind Tip» € 6,00 to «Fantastic Tip» € 45,00): say it is free with optional tips.
- **documents-by-readdle**: Documents Plus rows € 9,99, € 17,99, € 59,99 without periods (range only), and «Documents VPN» rows (€ 12,49
  to € 98,99): mention the VPN only if the English page does. MediaKit facts and Dutch UI names from `nl/apps/mediakit/index.md`.
- **flow-free** and **two-dots** (Millrace): **never write «2048», in any form, anywhere on the page** (house rule). Millrace facts from
  `_apps/millrace.md` and `nl/apps/millrace/index.md` only (64 levels, free, its own IAP via `{P_…@millrace}` tokens or catalog
  includes as the model does). «Geen abonnement» is allowed for Millrace. Flow Free rows are hints and packs (€ 0,99 to € 9,99, «Unlock
  All Packs and Remove Ads» € 5,99); Two Dots rows are power-ups, lives and currency (€ 0,99 to € 9,99). Two Dots has NL UI.
- **nonograms-katana** (Tare): NL UI, Dutch store name «Nonogrammen Katana». Rows: hints, «VIP versie» € 6,99, potions, rubies. Tare facts
  from `_apps/tare.md`, `nl/apps/tare/index.md` and these rules: Chapter I (20 levels) free; one purchase unlocks the rest (token); hints
  are opt-in and cost the third star; the puzzle itself is wordless; iOS/iPadOS 18; iPhone and iPad. «Geen abonnement» is allowed for
  Tare. The Tier 2 logic guide (`nl/guides/best-logic-puzzle-games-iphone.html`) already describes Nonograms Katana: stay consistent.
- **autosleep** (Observa): paid app € 9,99, no in-app rows, NL UI. Observa rules as before (HRV (SDNN), «Gereedheid», never «zonder
  abonnement»); health caveats as strong as English.
- **strong-workout-app** (GymLogger X): rows «Strong PRO (1 Month)» € 4,99 and € 5,99, «(6 Months)» € 20,49, «(1 Year)» € 24,49 to € 33,99,
  «Forever» € 89,99 and € 99,99, and an unlabelled «Strong PRO» € 3,99. Stay consistent with
  `nl/guides/workout-app-without-subscription.html` (its Strong price sentence). GymLogger X never «zonder abonnement».
