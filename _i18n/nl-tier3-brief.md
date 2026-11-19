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
