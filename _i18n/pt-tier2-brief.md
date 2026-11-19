# Writer brief: Portuguese (pt, Portugal) Tier 2, batch 1 (guides and audience pages)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/pt-writer-brief.md` first and follow all of it.** This file adds what is different for Tier 2.
Where the two disagree, this file wins. Scratch folder for anything you save: `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-n8q8Hr/80c59503-7bb0-423d-955c-db00baf42c73/scratchpad/pt-t2/` (never write scratch files in the repo).

## Your inputs

- The English source page (`guides/<slug>.html` or `for/<slug>.html`): it holds the facts.
- The Spanish page with the same path under `es/`: STRUCTURAL template only (Liquid, JSON-LD skeleton, card and table
  markup, how links and tokens are written, `{%- include t.html -%}` and token includes). The Spanish writers replaced
  US-only context (US prices, US ratings) with Spain data; you do the same with PORTUGAL data. Never translate from
  Spanish; write from English. Watch for Spanish words leaking in (Spanish «app de gimnasio», «suscripción», «valoraciones»).
- `/Users/anttiaittamaa/Downloads/githubcode/pt-tier2-research-2026-11-19.md`: your page's row (Portuguese primary and
  secondary queries, demand) and the Portuguese App Store data at the bottom (which competitors are sold in Portugal,
  Portuguese store names, Portuguese rating counts and averages, euro prices of paid apps).
- `_i18n/pt.md` (sheet), `_i18n/pt-apple-terms.md`, `_i18n/pt-glossary.md` (the sections of the apps your page names),
  and the Portuguese app pages `pt/apps/<slug>/index.md` of our apps your page names (feature names and wording already
  reviewed; reuse them).

## Pages in this batch

| Page | Write to | Primary query |
|---|---|---|
| guides/best-chess-apps-iphone.html | pt/guides/best-chess-apps-iphone.html | melhor app de xadrez |
| guides/best-logic-puzzle-games-iphone.html | pt/guides/best-logic-puzzle-games-iphone.html | melhores jogos de lógica para iphone |
| guides/workout-app-without-subscription.html | pt/guides/workout-app-without-subscription.html | app de treino grátis (angle: sem subscrição) |
| guides/best-xiangqi-apps-iphone.html | pt/guides/best-xiangqi-apps-iphone.html | xadrez chinês online |
| for/shift-workers.html | pt/for/shift-workers.html | trabalho por turnos saúde |
| for/apple-health-power-users.html | pt/for/apple-health-power-users.html | apps para apple watch + melhor app saúde iphone |
| for/calm-productivity.html | pt/for/calm-productivity.html | apps de produtividade iphone |
| (local-only, no English twin) | pt/guides/limitar-tempo-de-ecra-iphone.html | limitar tempo de ecrã iphone |
| guides/index.html, for/index.html (hubs, second wave) | pt/guides/index.html, pt/for/index.html | brand-led |

Keyword collisions to respect (these belong to Tier 1 app pages; never your primary or in your `seo.title`; a mention in
body text is fine): `app xadrez` (Chessful), `jogos de lógica iphone` (Millrace), `melhores jogos de puzzle iphone` (Tare),
`xadrez chinês`, `xiangqi` alone (Xiangqiful), `app treino ginásio` (LiftLog), `app treino apple watch` and
`app treino ginásio grátis` (GymLogger X), `hrv apple watch`, `app sono apple watch` (Observa), `como dormir de dia quem
trabalha à noite`, `distúrbio do sono trabalho por turnos` (AfterShift), `app lista de tarefas`, `app para organizar o dia`
(Taskful Day), `bloquear apps iphone` (EarnLock). The main session moves `melhor app de xadrez` off Chessful and
`tempo de ecrã iphone`, `limite de apps iphone` off EarnLock to you.

## Competitors (TRANSLATION.md 6.4 and 6.6)

- A "best X apps" page lists only apps sold in the Portuguese App Store (research file). An app marked NOT SOLD IN
  PORTUGAL is dropped, with any sentence that depends on it.
- Ratings: only the Portuguese count and average from the research file, written e.g. «Na App Store de Portugal tem
  4,8 em 5, com 9588 classificações (consultado a 19 de novembro de 2026)» (four digits without separator, five or
  more with U+00A0: «12 500»), or leave ratings out. Never US, Spanish or French numbers. An app with 0 Portuguese
  ratings: no rating sentence.
- Competitor prices: only Portuguese euro prices you verified today. Paid-app prices are in the research file. For
  in-app prices you may look up the app's Portugal page `https://apps.apple.com/pt/app/id<ID>` with curl (the
  «Compras integradas» rows; apps.apple.com rate-limits with HTTP 429: wait 60 s and retry once; if it fails, drop the
  number). Save what you fetched in `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-n8q8Hr/80c59503-7bb0-423d-955c-db00baf42c73/scratchpad/pt-t2/sources/competitors/<app>.html`. Type prices as `9,99 €` with U+00A0, with
  «(App Store de Portugal, consultado a 19 de novembro de 2026)» once per page. A dollar figure on the English page
  with no Portuguese price: drop the number, keep the qualitative fact («paga», «subscrição mensal ou anual», «compra
  única»). Never convert dollars. Never arithmetic on OUR prices; on a competitor's verified euro price only where the
  English page does the same calculation (state the inputs).
- Competitor names as in English (Chess.com, Hevy, Strong); the Portuguese store title may be mentioned once where it
  helps («na App Store de Portugal aparece como «Xadrez - Jogar e Aprender»»).
- App Store links to competitors: `https://apps.apple.com/pt/app/id<ID>`.
- Feature claims about competitors: only what the English page says (or, on the local-only page, what the app's own
  Portuguese App Store description says).

## Links

- `{% include l.html url="..." %}` for every internal link, as the Spanish page does (resolves to the Portuguese page
  when it exists at build time, else English with the marker). Do not hard-code `/pt/` URLs in body links. The
  pages of this batch will all exist, so link to them through l.html where the English page links to its twin.
- Links to comparison pages (`/alternatives/...`) and journal posts stay through l.html (they are English for now).

## Known English-side issues (ISSUES.md) to handle

- I-0351 chess guide: drop «(2026)»/«honest» padding from the title; no stale «Updated October 2026» overline (the
  layout shows the date); no US Premium price (use Portuguese store data or drop); Chessis is not in the Portuguese store
  (not in the research data: treat as not sold): no Chessis card; a «vs Chessis» comparison link may stay only if the
  Spanish page kept it, otherwise drop.
- I-0349 xiangqi guide: Chinese Chess - Best XiangQi has two puzzle counts (600+ / 1000+) on the English page: give no
  puzzle count for it unless its Portuguese listing (lookup API `country=pt&lang=pt_pt&id=1144533571`, field
  description) states one; save that description to sources/competitors.
- I-0352/I-0071 workout guide: use each app's LOWEST verified Portuguese monthly price in any ten-year comparison, the
  same rule for all three; no straight quotes in the H1.
- I-0310 logic guide: no Nonograms Katana VIP price unless verified on the Portuguese page today.
- I-0353 apple-health page: add a short «isto não é aconselhamento médico» line as the Spanish page did if the Spanish
  page has one (check); otherwise leave as English.

## YMYL pages (shift-workers, apple-health-power-users)

Keep every caveat. No new health claims, numbers or studies. Where the English page cites a source, keep the citation.
Apple Health names exactly as pt-apple-terms.md (a app Saúde; VFC (SDNN) for Observa's HRV; sleep stages Acordado,
REM, essencial, profundo). Shift-workers: no Portuguese labour-law claims (Código do Trabalho) unless the English page
makes the general point; never cite a law you did not read.

## Lessons from earlier Tier 2 reviews (French, Spanish): the most common must-fix items

- Softened hedges ("may" became "will") and hardened ones ("often" became "always"); keep the English strength.
- Added definitions or explanations that carry a claim the English page doesn't make.
- JSON-LD: keep the Spanish skeleton exactly (WebPage or CollectionPage / BreadcrumbList / ItemList / FAQPage nesting);
  a writer once pasted the ItemList into the breadcrumb. `"inLanguage": "pt-PT"`. Every FAQ `name` equals its visible
  `<summary>` character for character; every schema answer says the same as the visible answer. Valid JSON (no raw
  " inside strings, no trailing commas).
- Price tokens are single-brace: `{P_MONTHLY@chessful}`, never `{{P_…}}`; copy the Spanish page's token pattern.
- U+00A0 before € and units; NO space before %. Apple App Privacy labels quoted only from pt-apple-terms.md.
- No gendered audience words (cansado/cansada: rephrase impersonally); no «(2026)» or «guia honesto» padding; tracking =
  «seguimento»; Apple feature names bare in running text except where a tap is described; seo.keywords only real
  queries from the research file.
- Portuguese-specific from Tier 1: masculine article before app names («o Chessful», «do Hevy»), «a app», «a App
  Store»; impersonal register (no você, no tu); «subscrição» in prose; European vocabulary (ecrã, telemóvel, ginásio,
  descarregar, registar, guardar, Definições); AO90 (ótimo, ativo, leem/veem).

## Local-only page: `pt/guides/limitar-tempo-de-ecra-iphone.html` (TRANSLATION.md 6.7)

- Front matter: `local_only: true`, NO `ref`, NO `translated_from`, `permalink: /pt/guides/limitar-tempo-de-ecra-iphone/`,
  `last_updated: 2026-11-19`, full `seo`, `quick_answer`, faq in JSON-LD + visible, `datePublished` 2026-11-19.
- Structure: model it on `es/guides/limitar-tiempo-de-pantalla-iphone.html` (read it), but every fact must come from a
  Portuguese or primary source you fetched yourself today:
  - Apple Portugal's Screen Time page for iOS 27: `https://support.apple.com/pt-pt/guide/iphone/iphbfa595995/ios` and the
    rows in pt-apple-terms.md («Tempo de ecrã», «Horário de tempo de ecrã», «Limites de tempo», «Gerir tempo de ecrã»,
    «Partilhar entre dispositivos», «Ativar atividade em aplicações e sites»). Quote Apple's labels exactly as the page
    you fetched writes them (the always-allowed list label too: read it off the page). iOS 27 names only; say the guide
    does not describe earlier versions.
  - Each competitor's own Portuguese App Store description: `curl -s "https://itunes.apple.com/lookup?country=pt&lang=pt_pt&id=<ID>"`
    (field `description`). IDs: Opal 1497465230, one sec 1532875441, ScreenZen 1541027222, Jomo 1609960918, Cape
    6444819615, Forest 866450515, AppBlock 1515753232. Brick (6448794069) has no Portuguese listing: leave it out.
    Describe each app only with what its Portuguese description says (some listings are written in Brazilian
    Portuguese: paraphrase into European Portuguese, never quote a Brazilian sentence); no prices unless the listing
    states them. Portuguese ratings from the research file.
  - EarnLock facts from `_apps/earnlock.md`, the Portuguese page `pt/apps/earnlock/index.md` and its APP_BLUEPRINT.md §10
    (claims register only; find the blueprint path in `/Users/anttiaittamaa/Downloads/githubcode/.agents/product-marketing.md`).
    EarnLock's prices only through `{P_MONTHLY@earnlock}`, `{P_YEARLY@earnlock}`, `{P_LIFETIME@earnlock}` as the Spanish page
    does. Disclose that EarnLock is ours, as the Spanish page does.
- Save every page you fetch for facts into `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-n8q8Hr/80c59503-7bb0-423d-955c-db00baf42c73/scratchpad/pt-t2/sources/limitar-tempo-de-ecra-iphone/` (one file per source, named by
  app or Apple page) so the reviewer can check claim by claim.
- Scope note as in the Spanish page: these apps limit one's own use; the guide does not cover parental controls.
- Short quotes only (under 15 words), paraphrase the rest.

## Do NOT

Run `jekyll build`, `i18n.py map` or the stamp script; touch any file but your own; edit English, Spanish, French,
German or Italian files; edit `pt/llms.txt` or any app page (the main session wires hubs, llms lines and inbound links).
Other sessions (Spanish, Italian) work in this same checkout: never run `git` commands that change state (read-only
`git show`, `git log` are fine).

## Reply with

The items in pt-writer-brief.md «Reply with», plus: the final H1 and seo.title, every competitor fact you dropped because
Portugal data was missing, competitor prices you verified (with source file), and (local-only page) the list of sources saved.

---

## Batch 2 (2026-11-19)

Same rules as batch 1. Research rows: the «Batch 2» section at the bottom of the research file. The batch 1 Portuguese
pages (pt/guides/*.html, pt/for/*.html) are reviewed and committed: read one or two of them for tone, structure and the
Portugal-data patterns (rating and price sentences, check-date line), and reuse their wording where it fits.

| Page | Write to | Primary query |
|---|---|---|
| guides/best-shogi-apps-iphone.html | pt/guides/best-shogi-apps-iphone.html | shogi online |
| guides/bill-tracker-without-bank-connection.html | pt/guides/bill-tracker-without-bank-connection.html | app para gerir subscrições |
| (local-only) | pt/guides/como-fazer-contagem-decrescente-iphone.html | como fazer contagem decrescente no iphone |

- **Shogi**: Kakinoki Shogi is not sold in Portugal: drop it and every sentence that depends on it. None of the listed apps has
  a Portuguese listing or a Portuguese rating: no rating sentences; say which languages they offer only where the English page
  does. Shogiful is ours (pt/apps/shogiful/index.md and its glossary section give the feature names; prices via tokens).
  Spanish twin es/guides/best-shogi-apps-iphone.html is the structural template. Check ISSUES I-0354 (shogi guide: two
  wordings for Shogi Wars and the JSA, stale dates, Kanazawa without a URL) and I-0053 in
  /Users/anttiaittamaa/Downloads/githubcode/ISSUES.md and handle them the way the Spanish page did.
- **Bill tracker**: Rocket Money, Truebill, Monarch and Copilot are not sold in Portugal, and Portugal has no single bank-linked
  default. Rewrite the comparison around the two apps sold in Portugal whose OWN listing says they connect to the bank:
  **Wallet - Finanças pessoais** (BudgetBakers, id 1032467659) and **Spendee** (id 635861140). Moneyboard (id 625887028) may
  appear as the manual-entry option only if the English page's structure has a place for one (the English page's point is
  bank login vs no bank login). Use ONLY what each app's own Portuguese App Store description says: the saved lookups are in
  `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-n8q8Hr/80c59503-7bb0-423d-955c-db00baf42c73/scratchpad/pt-t2/sources/bill-tracker-without-bank-connection/lookup-<id>.json` (field `description`); both Wallet and Spendee listings
  are Brazilian Portuguese: paraphrase into European Portuguese, never quote a Brazilian sentence. Keep the English page's general
  points about bank aggregation only where they do not name a US company or a US rule; drop Plaid, US banks and US law. Never claim
  anything about their security, fees, data sharing or bank coverage in Portugal that the listing does not say (Wallet's listing
  gives a worldwide bank count; do not turn it into a Portuguese-bank claim). The French and Spanish twins
  (fr/ and es/guides/bill-tracker-without-bank-connection.html) did the same rewrite around Bankin'/Linxo and Fintonic: use the
  Spanish one as the structural model. AllPaid facts from `_apps/allpaid.md`, `pt/apps/allpaid/index.md`, its glossary section
  and its APP_BLUEPRINT.md §10; prices via `{P_…@allpaid}` tokens; disclose that AllPaid is ours. Portuguese ratings from the
  research file (Wallet 4,5 with 944, Spendee 4,7 with 1314, Moneyboard 4,7 with 4026). Check ISSUES I-0355 (bill-tracker guide:
  title-case seo.title, typed platforms, unsourced aggregator claims) and avoid each problem. «contas a pagar» where «conta»
  could mean a bank account (sheet).
- **Countdown (local-only)**: `local_only: true`, no `ref`, no `translated_from`, permalink
  `/pt/guides/como-fazer-contagem-decrescente-iphone/`, `datePublished` 2026-11-19. Model:
  `es/guides/como-poner-cuenta-atras-iphone.html` (and fr/guides/application-compte-a-rebours-iphone.html). Facts from:
  Apple Portugal's iOS 27 iPhone guide pages on widgets (home screen and lock screen; start at
  https://support.apple.com/pt-pt/guide/iphone/iphb8f1bf206/ios and pt-apple-terms.md, fetch and save every page you use),
  each app's Portuguese description via the lookup API (`curl -s "https://itunes.apple.com/lookup?country=pt&lang=pt_pt&id=<ID>"`;
  IDs 1403367428 Countdown, 576177593 Countdown Star, 1534850579 Countdown Buddy, 917514700 Contagens, 940109775 Big Days),
  Soon.'s `_apps/soon.md`, `pt/apps/soon/index.md` and its APP_BLUEPRINT.md §10 (prices via `{P_…@soon}` tokens; disclose it is
  ours). Portuguese ratings from the research file. «contagem decrescente», never «contagem regressiva» (Brazilian) except when
  naming Big Days' store title. If iOS itself has no countdown widget, say only what the Apple page you fetched shows. Sources go
  in `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-n8q8Hr/80c59503-7bb0-423d-955c-db00baf42c73/scratchpad/pt-t2/sources/como-fazer-contagem-decrescente-iphone/`.
- Blueprints: only §10 (claims register); §8 lists non-claims and §9 hidden items, never sources.

### Lessons from the batch 1 reviews (the most common fixes; avoid them)

- U+00A0 before every € (a writer typed 25 plain spaces). Single-brace tokens only (a writer wrote `{{P_MONTHLY@earnlock}}`).
- Quote Apple labels exactly as the fetched page writes them, for each step (Apple Portugal uses one label to switch a thing on
  and another to switch it off). Never invent a condition («À primeira vez»). Never put your own translation of an English or
  Brazilian listing in «» as if it were the app's text.
- Keep a competitor's privacy claim as strong as its listing («inteiramente», «nunca»); keep English hedges as strong as English.
- Competitor names as in English; the Portuguese store title at most once.
- Keywords: European forms only (never «iniciantes», «os apps», «academia», «celular», «tela», «controle»).
- Tells found: «dá para» (write «é possível»), «utilização» for "job", «deixa em paz», subjectless «quando falha»,
  «no próprio iCloud», «melhorias» for paid upgrades, «seguimento» for progress tracking («acompanhamento»), «Comparativas» and
  «frente ao» (Spanish leaks; write «vs»), «caráter» (pt-PT «carácter»), gendered words («farto», «atrasado», «Ser guiado»),
  «o editor deste guia» (write «que publica este guia»), trailing gerunds, one-line closers.
