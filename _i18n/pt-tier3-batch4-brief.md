# Writer brief: Portuguese (pt, Portugal) Tier 3, batch 4 (the must-have comparisons left)

Batch 4 reuses the batch 1 to 3 brief with these changes: the pages table, the store file
(`/Users/anttiaittamaa/Downloads/githubcode/pt-tier3-store-batch4-2026-11-19.md`), the collisions and the review lessons at
the end (now including batch 3). Where this header and the rest disagree, this header wins.

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/pt-writer-brief.md` first and follow all of it** (except its scratch path: use the one below). This file
adds what is different for Tier 3. Where the two disagree, this file wins.

Scratch folder for anything you save: `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-SuqGrw/ac5625c2-89a4-434e-865e-fa71b5eeaae2/scratchpad/pt-t3b4/`
(never write scratch files in the repo).

## Your inputs

- The English source page `alternatives/<slug>.html`: it holds the facts about OUR app and the comparison.
- The Spanish page `es/alternatives/<slug>.html` (reviewed, committed): STRUCTURAL template only (Liquid, JSON-LD
  skeleton, table and card markup, how links and tokens are written, how the Spanish writer replaced US competitor data
  with Spain data). Never translate from Spanish; write from English. Watch for Spanish leaking in («Comparativas»,
  «suscripción», «valoraciones», «frente a», «ficha» for a card, «caráter»).
- `/Users/anttiaittamaa/Downloads/githubcode/pt-tier3-research-2026-11-19.md`: your page's row (Portuguese primary
  query, the Portuguese suggest phrasings that show demand).
- `/Users/anttiaittamaa/Downloads/githubcode/pt-tier3-store-batch4-2026-11-19.md`: the competitor in the PORTUGUESE App
  Store, checked today (Portuguese store name, Portuguese ratings, languages, IAP rows in euro, full store description).
- `_i18n/pt.md` (sheet: register, typography, glossary, tells to cut, ALL of it), `_i18n/pt-apple-terms.md`,
  `_i18n/pt-glossary.md` (your app's section), `_i18n/pt-keywords.md` (your app's section), and the Portuguese app page
  `pt/apps/<app>/index.md` (its wording, tier names and feature names are reviewed: reuse them).

## Pages in this batch

| English source | Write to | Our app | Primary query (secondaries in the research file, «Batch 4 shortlist») | Template (structure only) | Nearest reviewed pt page |
|---|---|---|---|---|---|
| alternatives/athlytic.html | pt/alternatives/athlytic.html | Observa | athlytic (+ athlytic vs oura, athlytic apple watch) | es/ | pt/alternatives/bevel.html, welltory.html |
| alternatives/hrv4training.html | pt/alternatives/hrv4training.html | Observa | hrv4training como funciona (+ hrv4training grátis, hrv4training apple watch) | es/ | pt/alternatives/welltory.html |
| alternatives/stronglifts-5x5.html | pt/alternatives/stronglifts-5x5.html | GymLogger X | stronglifts 5x5 (+ stronglifts app) | es/ | pt/alternatives/strong-workout-app.html, jefit.html |
| alternatives/ladder.html | pt/alternatives/ladder.html | LiftLog | ladder app (+ ladder app preço; never «ladder» alone: it means ladders) | fr/ | pt/alternatives/hevy.html |
| alternatives/countdown-star.html | pt/alternatives/countdown-star.html | Soon. (its first pt comparison) | countdown star (+ countdown star widget) | de/ | pt/apps/soon/index.md, pt/guides/como-fazer-contagem-decrescente-iphone.html |
| alternatives/izip.html | pt/alternatives/izip.html | MediaKit | izip (+ izip grátis) | es/ | pt/alternatives/documents-by-readdle.html |
| alternatives/image-size.html | pt/alternatives/image-size.html | MediaKit | tamanho da imagem (the competitor's Portuguese store name; + image size app) | de/ | pt/alternatives/cloudconvert.html |
| alternatives/convertio.html | pt/alternatives/convertio.html | MediaKit | convertio grátis (+ como funciona o convertio, convertio ou cloudconvert: this page owns it) | es/ | pt/alternatives/cloudconvert.html |
| alternatives/wondershare-uniconverter.html | pt/alternatives/wondershare-uniconverter.html | MediaKit | uniconverter grátis (+ wondershare uniconverter preço, uniconverter é seguro) | es/ | pt/alternatives/handbrake.html |
| alternatives/magnus-trainer.html | pt/alternatives/magnus-trainer.html | Chessful | magnus trainer (+ magnus trainer grátis) | es/ | pt/alternatives/chess-com.html |
| alternatives/chessable.html | pt/alternatives/chessable.html | Chessful | chessable (+ chessable grátis, chessable pro) | es/ | pt/alternatives/lichess.html |
| alternatives/nonograms-katana.html | pt/alternatives/nonograms-katana.html | Tare (its first pt comparison) | nonogramas katana (+ nonograms katana) | fr/ | pt/apps/tare/index.md, pt/alternatives/kami-2.html |
| alternatives/baba-is-you.html | pt/alternatives/baba-is-you.html | Tare | baba is you (+ baba is you português, baba is you preço) | es/ | pt/apps/tare/index.md, pt/alternatives/flow-free.html |
| alternatives/wikipedia-app.html | pt/alternatives/wikipedia-app.html | WanderWiki (its first pt comparison) | app da wikipédia (+ wikipédia offline) | es/ | pt/apps/wanderwiki/index.md |
| alternatives/kiwix.html | pt/alternatives/kiwix.html | WanderWiki | kiwix como funciona (+ kiwix o que é, kiwix offline) | es/ | pt/apps/wanderwiki/index.md |
| alternatives/jomo.html | pt/alternatives/jomo.html | EarnLock | jomo app (+ jomo como funciona) | fr/ | pt/alternatives/opal.html, one-sec.html |

The hub, `/pt/llms.txt` and inbound links are done after your pages by another agent. Thirty reviewed Portuguese
comparisons already exist under pt/alternatives/: read the nearest one in the table and reuse its wording for our app,
its footnote pattern and its skeleton. Soon., Tare and WanderWiki have no Portuguese comparison yet: use their Portuguese
app pages (and for Tare the logic guide `pt/guides/best-logic-puzzle-games-iphone.html`).

Keyword collisions: every keyword in the `seo.keywords` of your app's Portuguese app page, of the logic and countdown
guides, and every primary in `_i18n/pt.md` «Tier 2 keywords» and «Tier 3 keywords», belongs to another page: never your
primary or in your `seo.title`; avoid them in your seo.keywords too. Examples: Soon. `contagem decrescente iphone`,
`contagem decrescente widget`, `app contador de dias`; countdown guide `como fazer contagem decrescente no iphone`; MediaKit
`comprimir vídeo iphone`, `comprimir pdf iphone`, `converter heic para jpg`; Tare `melhores jogos de puzzle iphone`, `jogos de
puzzle iphone`, `jogos offline iphone`; WanderWiki `wikipedia aleatória`; Chessful `app xadrez`; LiftLog `app treino ginásio`;
EarnLock `bloquear apps iphone`; Observa `hrv apple watch`, `app sono apple watch`; GymLogger X `app treino apple watch`,
`app treino de força`; cloudconvert page `cloudconvert grátis`. Within this batch: the four MediaKit pages (izip,
image-size, convertio, uniconverter) must not share a title pattern, nor athlytic and hrv4training, nor the two Chessful,
two Tare or two WanderWiki pages.

Batch-specific facts:
- Countdown Star (576177593) is the store app the English page compares; a separate «Countdown Star (Sem anúncios)» listing
  exists (569371565, ★6): mention it only if the English page talks about an ad-free paid version.
- Image Size: the Portuguese store name is «Tamanho da Imagem» (670766542, ★84, listing in Portuguese).
- UniConverter: three Mac App Store listings exist in Portugal (store file). Use only what the English page compares; give
  euro prices from the store file only for the listing the English page means.
- Convertio is a web service. The only Portuguese store listing named Convertio is published by another seller (store file):
  never use its data; say, as the Spanish page does, that no official Convertio app is listed in the Portuguese App Store
  (consultado a 19 de novembro de 2026) only if the English page talks about apps. Web plan prices in dollars: describe the
  model in words, no number (as the cloudconvert page did). The English 1 GB free-tier cap is not market-specific: keep it.
- Wikipedia's app is «Wikipédia» in the Portuguese store (324715238); write «Wikipédia» in prose (sheet).
- Kiwix: free, in the store file; leave its ratings out.
- Athlytic, LADDER and Chessable listings are not in Portuguese (store file); Jomo's Portuguese store title is Brazilian
  («Reduza o tempo de tela»): quote it once as the store name if useful, never adopt «tela» in our prose («ecrã»).
- Paid apps and IAP: only as the store file shows (price line and IAP rows).
- «Sem subscrição» house rule: allowed for LiftLog, Millrace, Mockly and Tare. In this batch that means the LADDER page (LiftLog) and the two Tare pages (Tare is free with one unlock, via tokens). Every other app here sells subscriptions.

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
  `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-SuqGrw/ac5625c2-89a4-434e-865e-fa71b5eeaae2/scratchpad/pt-t3b4/research/page-<slug>-<id>.html`;
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

## Lessons from the batch 2 reviews

- Don't add a verdict to quick_answer that the English page doesn't make («é a melhor escolha para quem…»).
- «opção vitalícia» for lifetime everywhere (never «numa só compra», «uma só vez», «só se paga por subscrição»).
- «em relação a» (not «face a/ao»), «As duas apps» (not «Ambas» with masculine app names), «verificado a» (not «revista a»),
  no unclear «o seu / a sua», no footnote meta sentences, masculine article on app names («o AutoSleep»), no en dash in a
  quoted store title.
- No added FAQ unless every fact in it is on the English page; never a language FAQ unless the English page discusses
  languages (a query like «X em português» is answered with one plain sentence from the store file, once).
- Keywords: only real queries from the research file or `_i18n/pt-keywords.md`; 3 or 4 real ones beat 5 with an invention.
- Check every « €» has U+00A0 (some tools turn it into a plain space).

## Do NOT

Run `jekyll build`, `i18n.py map` or the stamp script; touch any file but your own; edit English, Spanish, Italian, Dutch,
French, German files or other Portuguese files. Other sessions (Dutch, Spanish, Italian) work in this same checkout:
never run `git` commands that change state. Do not fetch apps.apple.com yourself (the store file has the data; it 429s
under load); the iTunes lookup API (`https://itunes.apple.com/lookup?country=pt&lang=pt_pt&id=<ID>`) is fine if you need
one more field.

## Reply with

The items in pt-writer-brief.md «Reply with», plus every competitor fact you dropped because Portuguese data was
missing, and every place where the Portuguese store contradicted the English page.

## Lessons from the batch 3 reviews

Read `_i18n/pt.md` «Tells to cut», especially the «From the Tier 3 batch 3 reviews» and «batch 3 Millrace and hub» paragraphs:
silence in the store is not a contradiction (keep the English fact); «tem anúncios» not «vive de anúncios»; «na nuvem»;
masculine agreement with app names («um bom candidato», «o Productive»); «Para quem …» not anacoluthon; «críticas» for App Store
reviews, never «classificações» for ranks; no implied roadmap («sem versão em português», never «ainda não existem»); trial terms
never read into IAP row names; table cells with a noun; no footnote widening the source list.

## Another Portuguese session is working in this checkout

A Tier 4 (journal) session edits pt/journal/*, pt/llms.txt and some pt guide pages right now. Touch ONLY your own new file.
