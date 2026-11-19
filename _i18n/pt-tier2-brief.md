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
