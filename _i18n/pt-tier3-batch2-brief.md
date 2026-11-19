# Writer brief: Portuguese (pt, Portugal) Tier 3, batch 2 (comparison pages)

Batch 2 uses the batch 1 brief below with these changes: the pages table, the store file
(`/Users/anttiaittamaa/Downloads/githubcode/pt-tier3-store-batch2-2026-11-19.md`), the collisions and the batch 1 review
lessons at the end. Where this header and the rest disagree, this header wins.

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

| English source | Write to | Our app | Primary query (secondaries in the research file, «Batch 2 shortlist») |
|---|---|---|---|
| alternatives/documents-by-readdle.html | pt/alternatives/documents-by-readdle.html | MediaKit | documents by readdle (+ app documents iphone) |
| alternatives/bevel.html | pt/alternatives/bevel.html | Observa | bevel app (+ bevel apple watch, bevel app grátis) |
| alternatives/autosleep.html | pt/alternatives/autosleep.html | Observa | autosleep apple watch (+ autosleep app) |
| alternatives/gentler-streak.html | pt/alternatives/gentler-streak.html | Observa | gentler streak (+ gentler streak premium, gentler streak grátis) |
| alternatives/strong-workout-app.html | pt/alternatives/strong-workout-app.html | GymLogger X | strong workout tracker (+ strong app grátis) |
| alternatives/fitbod.html | pt/alternatives/fitbod.html | GymLogger X | fitbod é pago (+ fitbod é bom, fitbod em português, fitbod preço) |
| alternatives/one-sec.html | pt/alternatives/one-sec.html | EarnLock | one sec app (+ one sec app grátis) |
| alternatives/screenzen.html | pt/alternatives/screenzen.html | EarnLock | screenzen (+ screenzen em português, screenzen como funciona) |
| alternatives/rise-sleep-tracker.html | pt/alternatives/rise-sleep-tracker.html | AfterShift | rise sleep tracker (+ rise sleep funciona, rise sleep grátis); template: fr/ and de/ twins (no Spanish one) |
| alternatives/habitica.html | pt/alternatives/habitica.html | Taskful Day | habitica em português (+ habitica app em português, habitica como funciona) |

The hub, `/pt/llms.txt` and inbound links are done after your pages by another agent. The ten batch 1 pages
(pt/alternatives/{whoop,oura,splitwise,tricount,hevy,chess-com,lichess,pdf-expert,forest,opal}.html) are reviewed and
live: read the one closest to yours (same app) and reuse its wording for our app, its footnote pattern and its structure.

Keyword collisions (other pages own these; never your primary or in your `seo.title`; avoid them in seo.keywords too):
`hrv apple watch`, `app sono apple watch` (Observa), `app treino apple watch`, `app treino de força`, `app treino ginásio
grátis` (GymLogger X), `app treino ginásio` (LiftLog), `app de treino grátis` (workout guide), `bloquear apps iphone`
(EarnLock), `limitar tempo de ecrã iphone` (screen-time guide), `comprimir vídeo iphone`, `comprimir pdf iphone`,
`converter heic para jpg` (MediaKit), `app lista de tarefas`, `app para organizar o dia` (Taskful Day), `como dormir de
dia quem trabalha à noite`, `dívida de sono` (AfterShift), `apps para apple watch`, `melhor app saúde iphone` (Apple Health
page), `apps de produtividade iphone`, `trabalho por turnos saúde`, and every batch 1 primary (`alternativa a whoop`,
`oura ring ou apple watch`, `hevy como funciona`, `opal app como funciona`, `forest app como funciona`, …). Within this
batch: bevel, autosleep and gentler-streak must not share a title pattern; strong and fitbod neither; one-sec and
screenzen neither.

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

## Lessons from the batch 1 reviews (fix these before you hand back)

- Never cite a US listing or US data on a Portuguese page: privacy labels, Family Sharing, devices and prices come from the
  Portuguese store file (raw product pages are saved in
  `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-vvPVmP/a07fe73c-d938-475e-b597-e41503062630/scratchpad/research/page-<slug>.html`;
  grep them for «Privacidade da app», «Partilha com a família», «Compatibilidade»). What the English page says about how the
  product works may stay, without a «US listing» attribution.
- «IAP rows: none shown» means no rows were rendered: never write «sem compras integradas» from it.
- Don't add competitor claims from the store description that the English page doesn't make (a feature list inside Pro,
  community size). Don't harden («só», «a alternativa» for "an alternative").
- seo.title in natural Portuguese that leads with the query, never a raw keyword string. Prose: «alternativa ao X» /
  «à X» with the article; keywords stay as people type them.
- Bullets under a card title ending «… se»: no infinitives, no second «se»; write «serve para quem…» + verb.
- «compras integradas» (never «compras na app» / «dentro da app»), «ficha» (never «listagem»), «opção vitalícia» (never
  «uma só vez» or «opção de compra única vitalícia»), «confirme» (never «confira»), «comparado com» / «vs» (never «frente
  a» / «face a»), no gendered words («servido», «farto»), no meta clauses about where a fact came from.
- One «consultado a 19 de novembro de 2026» per page; ratings with one decimal.
- Run the copy-editing skill file for real (read ~/.claude/skills/copy-editing/SKILL.md), not from memory.

## Do NOT

Run `jekyll build`, `i18n.py map` or the stamp script; touch any file but your own; edit English, Spanish, Italian, Dutch,
French, German files or other Portuguese files. Other sessions (Dutch, Spanish, Italian) work in this same checkout:
never run `git` commands that change state. Do not fetch apps.apple.com yourself (the store file has the data; it 429s
under load); the iTunes lookup API (`https://itunes.apple.com/lookup?country=pt&lang=pt_pt&id=<ID>`) is fine if you need
one more field.

## Reply with

The items in pt-writer-brief.md «Reply with», plus every competitor fact you dropped because Portuguese data was
missing, and every place where the Portuguese store contradicted the English page.
