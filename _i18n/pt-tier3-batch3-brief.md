# Writer brief: Portuguese (pt, Portugal) Tier 3, batch 3 (comparison pages)

Batch 3 uses the batch 1 brief below with these changes: the pages table, the store file
(`/Users/anttiaittamaa/Downloads/githubcode/pt-tier3-store-batch3-2026-11-19.md`), the collisions and the batch 1 and 2 review
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

| English source | Write to | Our app | Primary query (secondaries in the research file, «Batch 3 shortlist») | Template (structure only) |
|---|---|---|---|---|
| alternatives/flow-free.html | pt/alternatives/flow-free.html | Millrace | flow free (+ flow free grátis, flow free game) | es/ |
| alternatives/two-dots.html | pt/alternatives/two-dots.html | Millrace | two dots (+ two dots grátis) | es/ |
| alternatives/kami-2.html | pt/alternatives/kami-2.html | Millrace | kami 2 | fr/ |
| alternatives/productive.html | pt/alternatives/productive.html | Taskful Day | productive app (+ productive app free, productive app pricing) | de/ |
| alternatives/streaks-app.html | pt/alternatives/streaks-app.html | Taskful Day | streaks app (+ streaks app iphone, streaks apple watch) | fr/ |
| alternatives/handbrake.html | pt/alternatives/handbrake.html | MediaKit | alternativa handbrake (+ handbrake como funciona, handbrake português) | es/ |
| alternatives/cloudconvert.html | pt/alternatives/cloudconvert.html | MediaKit | cloudconvert ou convertio (+ cloudconvert grátis, cloudconvert como funciona) | es/ |
| alternatives/welltory.html | pt/alternatives/welltory.html | Observa | welltory (+ welltory português, welltory grátis) | es/ |
| alternatives/jefit.html | pt/alternatives/jefit.html | GymLogger X | jefit em português (+ hevy ou jefit, jefit grátis) | es/ |
| alternatives/settle-up.html | pt/alternatives/settle-up.html | RightSplit | settle up como funciona (+ settle up grátis, settle up vs splitwise) | es/ |

The hub, `/pt/llms.txt` and inbound links are done after your pages by another agent. Twenty reviewed Portuguese
comparisons already exist under pt/alternatives/: read the one closest to yours (same app) and reuse its wording for our
app, its footnote pattern and its skeleton: MediaKit (pdf-expert, documents-by-readdle), Observa (whoop, oura, bevel),
GymLogger X (strong-workout-app, fitbod), RightSplit (splitwise, tricount), Taskful Day (habitica). Millrace has no
Portuguese comparison yet: use `pt/apps/millrace/index.md` and the logic guide `pt/guides/best-logic-puzzle-games-iphone.html`.

Keyword collisions (other pages own these; never your primary or in your `seo.title`; avoid them in seo.keywords too):
Millrace `jogos de lógica iphone`, `jogos de raciocínio lógico iphone`, `jogos sem anúncios iphone`; logic guide `melhores jogos
de lógica para iphone`; Tare `melhores jogos de puzzle iphone`, `jogos de puzzle iphone`, `jogos offline iphone`; Taskful Day
`app lista de tarefas`, `app tarefas diárias`, `app para organizar o dia`, `app to do list`; calm-productivity `apps de
produtividade iphone`; MediaKit `comprimir vídeo iphone`, `comprimir pdf iphone`, `converter heic para jpg`, `reduzir tamanho
vídeo whatsapp`; RightSplit `dividir conta restaurante`, `app para dividir contas`, `app para dividir despesas com amigos`,
`calculadora dividir conta`; Observa `hrv apple watch`, `app sono apple watch`, `qualidade do sono apple watch`; GymLogger X
`app treino apple watch`, `app treino de força`; LiftLog `app treino ginásio`; and every primary of the twenty existing
comparisons (`hevy ou strong` stays with hevy; `tricount ou splitwise` with the split pages). Within this batch, the three
Millrace pages must not share a title pattern, nor productive and streaks, nor handbrake and cloudconvert.

Millrace rules: NEVER write the number title it replaced (no «2048» anywhere, not even in keywords or alt text). Millrace
is free; «sem subscrição» is allowed for Millrace (house rule). Facts only from the English page and `pt/apps/millrace/index.md`.

HandBrake is not an App Store app: no Portuguese store data exists, so its facts come from the English page only (free,
open-source desktop app); add no price. CloudConvert is mainly a web service: use the store file for its iOS app (★2, leave
the rating out) and give its web prices only if the English page does AND you can avoid dollars (otherwise describe the
model in words: «créditos de conversão», «plano gratuito diário», as the English page says).

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
