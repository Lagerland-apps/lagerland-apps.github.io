# Writer brief: Portuguese (pt, Portugal) Tier 3, batch 1 (comparison pages)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/pt-writer-brief.md` first and follow all of it** (except its scratch path: use the one below). This file
adds what is different for Tier 3. Where the two disagree, this file wins.

Scratch folder for anything you save: `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-vvPVmP/a07fe73c-d938-475e-b597-e41503062630/scratchpad/pt-t3/`
(never write scratch files in the repo).

## Your inputs

- The English source page `alternatives/<slug>.html`: it holds the facts about OUR app and the comparison.
- The Spanish page `es/alternatives/<slug>.html` (reviewed, committed): STRUCTURAL template only (Liquid, JSON-LD
  skeleton, table and card markup, how links and tokens are written, how the Spanish writer replaced US competitor data
  with Spain data). Never translate from Spanish; write from English. Watch for Spanish leaking in («Comparativas»,
  «suscripción», «valoraciones», «frente a», «ficha» for a card, «caráter»).
- `/Users/anttiaittamaa/Downloads/githubcode/pt-tier3-research-2026-11-19.md`: your page's row (Portuguese primary
  query, the Portuguese suggest phrasings that show demand).
- `/Users/anttiaittamaa/Downloads/githubcode/pt-tier3-store-2026-11-19.md`: the competitor in the PORTUGUESE App
  Store, checked today (Portuguese store name, Portuguese ratings, languages, IAP rows in euro, full store description).
- `_i18n/pt.md` (sheet: register, typography, glossary, tells to cut, ALL of it), `_i18n/pt-apple-terms.md`,
  `_i18n/pt-glossary.md` (your app's section), `_i18n/pt-keywords.md` (your app's section), and the Portuguese app page
  `pt/apps/<app>/index.md` (its wording, tier names and feature names are reviewed: reuse them).

## Pages in this batch

| English source | Write to | Our app | Primary query (secondaries in the research file) |
|---|---|---|---|
| alternatives/whoop.html | pt/alternatives/whoop.html | Observa | alternativa a whoop (+ whoop sem subscrição, whoop ou apple watch) |
| alternatives/oura.html | pt/alternatives/oura.html | Observa | oura ring ou apple watch (+ oura ring tem subscrição) |
| alternatives/splitwise.html | pt/alternatives/splitwise.html | RightSplit | alternativa ao splitwise |
| alternatives/tricount.html | pt/alternatives/tricount.html | RightSplit | alternativa a tricount (+ tricount como funciona) |
| alternatives/hevy.html | pt/alternatives/hevy.html | LiftLog | hevy como funciona (+ hevy pro preço, hevy ou strong) |
| alternatives/chess-com.html | pt/alternatives/chess-com.html | Chessful | chess.com premium preço (+ alternativa chess com) |
| alternatives/lichess.html | pt/alternatives/lichess.html | Chessful | chess.com ou lichess |
| alternatives/pdf-expert.html | pt/alternatives/pdf-expert.html | MediaKit | pdf expert grátis mac (+ pdf expert preço) |
| alternatives/forest.html | pt/alternatives/forest.html | EarnLock | forest app como funciona |
| alternatives/opal.html | pt/alternatives/opal.html | EarnLock | opal app como funciona |

The hub `pt/alternatives/index.html`, the `/pt/llms.txt` lines and the inbound links are done after your pages by
another agent. Do not touch them.

Keyword collisions (Tier 1 and 2 pages own these; never your primary or in your `seo.title`; fine in body text or as a
secondary keyword): `dividir conta restaurante`, `app para dividir contas`, `app para dividir despesas com amigos`
(RightSplit), `app xadrez` (Chessful), `melhor app de xadrez` (chess guide), `hrv apple watch`, `app sono apple watch`
(Observa), `app treino ginásio` (LiftLog), `app de treino grátis` (workout guide), `bloquear apps iphone` (EarnLock),
`limitar tempo de ecrã iphone` (screen-time guide), `comprimir pdf iphone`, `comprimir vídeo iphone` (MediaKit). The
pairs in this batch must not share a primary or a `seo.title` pattern: tricount owns `alternativa a tricount`,
splitwise owns `alternativa ao splitwise` (`tricount ou splitwise` may be a secondary on both); chess-com owns
`chess.com premium preço`, lichess owns `chess.com ou lichess`; whoop owns `alternativa a whoop`, oura owns `oura ring ou
apple watch` (`oura ou whoop` may be a secondary on both); forest owns `forest app como funciona`, opal owns `opal app como
funciona`.

Grammar of brand names: write keywords exactly as people type them (lowercase, «alternativa a whoop»), but prose and
titles in correct European Portuguese («alternativa à Whoop» if the writer treats Whoop as «a pulseira», or «ao WHOOP» as
an app; pick one per page and keep it). Our apps take the masculine article (sheet).

## Competitor facts (TRANSLATION.md 6.4)

- Every fact about the competitor is per market. Use ONLY the Portuguese store file (and what the English page says that
  is not market-specific, such as how the product works). A US price, a US rating or a US-only feature on a Portuguese
  page is wrong.
- Prices: only the euro amounts in the store file's IAP rows, typed `3,99 €` with U+00A0 before €, with «(App Store de
  Portugal, consultado a 19 de novembro de 2026)» once per page. The IAP rows name products, not always periods: say
  what the row name says («Premium mensal», «anual») and no more. Several rows for one plan: give a range as the
  Spanish Forest page does («entre 25,00 € e 27,95 € por ano»). No row for a plan the English page prices: keep the
  qualitative fact («subscrição mensal ou anual», «paga») and drop the number. Never convert dollars. Never arithmetic
  on OUR prices; arithmetic on a competitor's euro price only where the English page does the same calculation.
  A WHOOP or Oura membership sold outside the App Store has no verified Portuguese price: describe it («subscrição
  obrigatória», as the English page says) without a number (I-0174).
- Ratings: only the Portuguese count and average from the store file, as «Na App Store de Portugal tem 4,8 em 5, com
  3584 classificações (consultado a 19 de novembro de 2026)» (four digits without separator, five or more with U+00A0:
  «12 500»), or leave ratings out.
- Competitor names as in English (WHOOP or Whoop as the English page writes it, Oura, Splitwise, Tricount, Hevy,
  Chess.com, Lichess, PDF Expert, Forest, Opal). The Portuguese store title once where it helps people find the app.
  Competitor App Store links: `https://apps.apple.com/pt/app/id<ID>`.
- Where the competitor's listing is not in Portuguese (store file), you may say so once if the English page talks about
  languages; never invent the app's interface languages.
- Feature claims about competitors: only what the English page says, cross-checked against the Portuguese description;
  if the Portuguese description contradicts the English page (a feature gone, now free, now paid), follow the
  Portuguese store file and report the English-side error in your reply.

## Our apps' rules on these pages

- Prices only through tokens (`{P_MONTHLY@observa}` etc.), exactly as the Spanish page writes them. Single braces.
- «Sem subscrição» only for LiftLog (house rule). Observa, RightSplit, Chessful, EarnLock and MediaKit sell
  subscriptions: write «sem subscrição obrigatória» or «opção vitalícia» only where the English page and the catalog
  support it. The WHOOP and Oura pages answer the «sem subscrição» queries by stating facts (WHOOP and Oura need a
  membership, as the English page says; Observa's daily scores are free and Premium has a lifetime option, via tokens),
  never by calling Observa «sem subscrição» (I-0369: an English FAQ promises an alternative «without a subscription»;
  the Portuguese answer says «subscrição opcional» or equivalent).
- Observa: «VFC (SDNN)», never RMSSD as Observa's HRV; the score and tier names as `pt/apps/observa/index.md` writes
  them; «a app Saúde». Medical caveats on the WHOOP and Oura pages stay exactly as strong as in English.
- Opal page: EarnLock also locks websites picked in Apple's picker (I-0102, fixed in English): follow the English page.
- Chessful's PGN import: as the English page says now (2000 games).
- Tier names and feature names: from the Portuguese app page and the glossary (RightSplit Pro+ and its Spaces name,
  Chessful Pro, LiftLog's tiers, EarnLock Premium, MediaKit Pro, Observa Premium).
- Disclose that the app is ours where the English page does (Lagerland Apps publishes the comparison).

## Links

- Internal links with `{% include l.html url="..." %}` exactly as the Spanish pages write them; never hard-code `/pt/` in
  body links (l.html picks the Portuguese page when it exists, else English with the marker).
- Where the English page links another comparison of this batch, keep the link (l.html resolves it to Portuguese).
- Breadcrumb hub item: `{ "@type": "ListItem", "position": 2, "name": "Comparações", "item": "{{ site.url }}/pt/alternatives/" }`.
- `"inLanguage": "pt-PT"` wherever the Spanish page has `"es-ES"`; every `/es/` in URLs and `@id`s becomes `/pt/`.

## Lessons from earlier reviews (most common must-fix items)

- Softened or hardened hedges; added definitions that carry a claim; framing sentences added to FAQ answers.
- JSON-LD: keep the Spanish skeleton exactly (WebPage / BreadcrumbList / FAQPage nesting; never an ItemList inside the
  breadcrumb). Every FAQ `name` equals its visible `<summary>` character for character; the schema answer says the same
  as the visible answer.
- Price tokens single-brace. U+00A0 before every €; no space before %.
- No gendered audience words («farto», «atrasado», «cansado»): rephrase impersonally. No raw-keyword seo.titles; no
  «(2026)» padding; no meta description opening with a question; seo.keywords only real queries from the research file
  or pt-keywords.md, European forms only.
- Apple App Privacy labels quoted only from pt-apple-terms.md («Dados não recolhidos», section «Privacidade da app»).
- The sheet's «Tells to cut» list, all of it (Tier 1 and Tier 2 findings).

## Do NOT

Run `jekyll build`, `i18n.py map` or the stamp script; touch any file but your own; edit English, Spanish, Italian, Dutch,
French, German files or other Portuguese files. Other sessions (Dutch, Spanish, Italian) work in this same checkout:
never run `git` commands that change state. Do not fetch apps.apple.com yourself (the store file has the data; it 429s
under load); the iTunes lookup API (`https://itunes.apple.com/lookup?country=pt&lang=pt_pt&id=<ID>`) is fine if you need
one more field.

## Reply with

The items in pt-writer-brief.md «Reply with», plus every competitor fact you dropped because Portuguese data was
missing, and every place where the Portuguese store contradicted the English page.
