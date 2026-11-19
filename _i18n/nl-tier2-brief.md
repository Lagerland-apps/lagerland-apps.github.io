# Writer brief: Dutch (nl, Netherlands) Tier 2, batch 1 (guides and audience pages)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/nl-writer-brief.md` first and follow all of it.** This file adds what is different for Tier 2.
Where the two disagree, this file wins. Scratch folder for anything you save (never write scratch files in the repo):
`/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-MVirY8/10bb35b8-de8b-405d-996b-c7615d2e76fa/scratchpad/nl-t2/`
(below: `$S`).

## Your inputs

- The ENGLISH source page (`guides/<slug>.html` or `for/<slug>.html`): it holds the facts. Write from its meaning.
- The ITALIAN page with the same path under `it/`: STRUCTURAL template only (Liquid, JSON-LD skeleton, card and table
  markup, how links and tokens are written, `{%- include t.html -%}` and token includes, how the store-data sentences
  and the check-date line are placed). The Italian writers replaced US-only context (US prices, US ratings) with
  Italy data; you do the same with NETHERLANDS data. Never translate from Italian. Watch for Italian structures
  leaking in.
- `/Users/anttiaittamaa/Downloads/githubcode/nl-tier2-research-2026-11-19.md`: your page's row (Dutch primary and
  secondary queries, demand) and the Dutch App Store data in «Raw data» (which competitors are sold in the Netherlands,
  Dutch store names, Dutch rating counts and averages, euro prices of paid apps, which listings have a Dutch UI).
- `$S/iap-nl.txt`: the in-app purchase rows of each competitor on its Dutch App Store page, fetched 2026-11-19 (the raw
  pages are in `$S/sources/store/<id>.html`). Use ONLY these rows for competitor in-app prices.
- `_i18n/nl.md` (sheet), `_i18n/nl-apple-terms.md`, `_i18n/nl-glossary.md` (the sections of the apps your page names),
  and the Dutch app pages `nl/apps/<slug>/index.md` of our apps your page names (feature names and wording already
  reviewed; reuse them).
- The copy-editing skill `~/.claude/skills/copy-editing/SKILL.md`: read it and run its Seven Sweeps and AI-tell removal
  on your finished Dutch before you reply.

## Pages in this batch

| Page | Write to | Primary query (visible form) |
|---|---|---|
| guides/best-chess-apps-iphone.html | nl/guides/best-chess-apps-iphone.html | `beste schaak app` (visible: «beste schaakapp») |
| guides/best-logic-puzzle-games-iphone.html | nl/guides/best-logic-puzzle-games-iphone.html | `puzzelspellen voor volwassenen` (+ `leuke denkspelletjes app`) |
| guides/workout-app-without-subscription.html | nl/guides/workout-app-without-subscription.html | `gratis gym app`, angle «zonder abonnement» |
| guides/best-xiangqi-apps-iphone.html | nl/guides/best-xiangqi-apps-iphone.html | `chinees schaken online` |
| for/shift-workers.html | nl/for/shift-workers.html | `ploegendienst gezondheid` |
| for/apple-health-power-users.html | nl/for/apple-health-power-users.html | `beste apple watch apps` (+ `apple watch apps gezondheid`) |
| for/calm-productivity.html | nl/for/calm-productivity.html | `productiviteit app iphone` |
| (local-only, no English twin) | nl/guides/schermtijd-beperken-iphone.html | `schermtijd beperken iphone` |
| guides/index.html, for/index.html (hubs, second wave) | nl/guides/index.html, nl/for/index.html | brand-led |

Keyword collisions to respect (these belong to Tier 1 app pages; never your primary or in your `seo.title`; a mention in
body text is fine): `schaak app`, `schaken leren app`, `schaak app zonder reclame` (Chessful); `logische puzzel app`,
`puzzel app zonder reclame` (Millrace); `beste puzzelgames iphone`, `denkspelletjes app`, `breinbreker` (Tare);
`chinees schaken`, `xiangqi`, `xiangqi app` alone (Xiangqiful); `krachttraining app`, `sportschool app`,
`fitness app zonder abonnement` (LiftLog); `gym app apple watch`, `workout app apple watch` (GymLogger X);
`hrv apple watch`, `slaap app apple watch` (Observa); `slapen na nachtdienst` and its variants, `ploegendienst slaap`,
`ploegendienst app` (AfterShift); `to do lijst app`, `dagplanner app` (Taskful Day); `apps blokkeren iphone`,
`app limiet iphone` (EarnLock). The main session moves `beste schaak app` off Chessful and `schermtijd beperken` off
EarnLock to you.

## Competitors (TRANSLATION.md 6.4 and 6.6)

- A "best X apps" page lists only apps sold in the Dutch App Store (research file). NOT SOLD IN NL: Chessis (not in the
  research file; a search of the Dutch store on 2026-11-19 found no Chessis), xiangqi app 403941510. Drop them with
  every sentence that depends on them; one plain sentence that an app is left out because it is not in the Dutch App
  Store is fine where the Italian page has one. Caliber (id 1482405410) IS sold in the Netherlands (★44, English only).
- Ratings: only the Dutch count and average from the research file, written e.g. «In de Nederlandse App Store heeft
  het een 4,7 van de 5, op basis van 41.703 beoordelingen (bekeken op 19 november 2026)» (four digits without
  separator, five or more with a dot: «41.703»), or leave ratings out. Never US or Italian numbers. An app with fewer
  than 5 Dutch ratings: no rating sentence.
- Competitor prices: only the Dutch euro rows in `$S/iap-nl.txt` or a paid app's price in the research file. Write them
  as `€ 3,49` with U+00A0 between € and the digit, with «(Nederlandse App Store, bekeken op 19 november 2026)» once per
  page where the Italian page has its check-date line. A competitor price the English page gives but the Dutch rows
  don't have: drop the number, keep the qualitative fact («betaald», «abonnement per maand of per jaar», «eenmalige
  aankoop»). Never convert dollars. Never arithmetic on OUR prices; on a competitor's verified euro price only where the
  English page does the same calculation (state the inputs; one rule for every app, see I-0352 below).
- Several apps show more than one price for the same plan (Hevy Pro monthly € 3,49 and € 4,49): say «vanaf» with the
  lowest, or give both as the Italian page does.
- Competitor names as in English (Chess.com, Hevy, Strong). The Dutch store title may be mentioned once where it helps
  (Chess.com appears as «Schaken - Speel & Leer Online»).
- App Store links to competitors: `https://apps.apple.com/nl/app/id<ID>`.
- Feature claims about competitors: only what the English page says (or, on the local-only page, what the app's own
  Dutch App Store description says). Whether a competitor has a Dutch interface: only from the research file's
  NL-lang column, and only where the page talks about language.

## Links

- `{% include l.html url="..." %}` for every internal link, as the Italian page does (resolves to the Dutch page
  when it exists at build time, else English with the marker). Do not hard-code `/nl/` URLs in body links. The
  pages of this batch will all exist, so link to them through l.html where the English page links to its twin.
- Links to comparison pages (`/alternatives/...`) and journal posts stay through l.html (English for now).
- JSON-LD URLs: absolute `https://lagerland.app/nl/...` for this page and its breadcrumb, as the Italian page writes
  `/it/`. `"inLanguage": "nl"`.

## Known English-side issues (ISSUES.md) to handle the way the Italian page did

- I-0351 chess guide: no «(2026)» / «eerlijk» padding in title or description; no stale «Bijgewerkt oktober 2026» overline
  (the layout shows the date); no US Premium price (Dutch IAP rows for Chess.com or nothing); no Chessis card; drop the
  «vs Chessis» comparison link (Chessis is not sold here).
- I-0349 xiangqi guide: give no puzzle count for Chinese Chess - Best XiangQi unless its Dutch listing states one
  (`curl -s "https://itunes.apple.com/lookup?country=nl&lang=nl_nl&id=1144533571"`, field `description`; save it to
  `$S/sources/competitors/1144533571.json`).
- I-0352 / I-0071 workout guide: one rule for all apps in any ten-year comparison (each app's LOWEST verified Dutch
  monthly price); no straight quotes in the H1.
- I-0310 logic guide: Nonograms Katana VIP price only from the Dutch IAP rows; otherwise no number.
- I-0353 apple-health page: add a short «geen medisch advies» line only if the Italian page has one (check).

## Health pages (shift-workers, apple-health-power-users)

Keep every caveat. No new health claims, numbers or studies. Where the English page cites a source, keep the citation.
Apple Health names exactly as nl-apple-terms.md (de Gezondheid-app, never «Apple Health» in our own words; HRV (SDNN)
for Observa; sleep stages as the sheet's glossary). Shift-workers: no Dutch labour-law claims (Arbeidstijdenwet) unless
the English page makes the general point; never cite a law or authority you did not read yourself today.

## Local-only page: `nl/guides/schermtijd-beperken-iphone.html` (TRANSLATION.md 6.7)

- Front matter: `local_only: true`, NO `ref`, NO `translated_from`, `permalink: /nl/guides/schermtijd-beperken-iphone/`,
  `last_updated: 2026-11-19`, full `seo`, `quick_answer`, faq in JSON-LD + visible, `datePublished` 2026-11-19.
- Structure: model it on `it/guides/limitare-tempo-di-utilizzo-iphone.html` (read it), but every fact must come from a
  Dutch or primary source you fetched yourself today:
  - Apple Netherlands' Screen Time page for iOS 27: `https://support.apple.com/nl-nl/guide/iphone/iphbfa595995/ios` and
    the rows in nl-apple-terms.md («Schermtijd», «Schema voor schermtijd», «tijdslimieten» …). Quote Apple's labels
    exactly as the page you fetched writes them (the always-allowed list label too: read it off the page), in ‘…’.
    iOS 27 names only; say the guide does not describe earlier versions.
  - Each competitor's own Dutch App Store description: `curl -s "https://itunes.apple.com/lookup?country=nl&lang=nl_nl&id=<ID>"`
    (field `description`). IDs: Opal 1497465230, one sec 1532875441, ScreenZen 1541027222, Jomo 1609960918, Cape
    6444819615, Forest 866450515, AppBlock 1515753232 (the same seven the Italian page uses; leave Brick out, it needs
    a hardware device). Several listings are English only: paraphrase into Dutch, never put your own translation in
    quotes as if it were the app's text. Describe each app only with what its listing says; no prices unless the
    listing or `$S/iap-nl.txt` states them. Dutch ratings from the research file.
  - EarnLock facts from `_apps/earnlock.md`, the Dutch page `nl/apps/earnlock/index.md` and its APP_BLUEPRINT.md §10
    (claims register only; the blueprint path is in `/Users/anttiaittamaa/Downloads/githubcode/.agents/product-marketing.md`).
    EarnLock's prices only through `{P_MONTHLY@earnlock}`, `{P_YEARLY@earnlock}`, `{P_LIFETIME@earnlock}` as the Italian
    page does. Disclose that EarnLock is ours, as the Italian page does.
- Save every page you fetch for facts into `$S/sources/schermtijd-beperken-iphone/` (one file per source, named by
  app or Apple page) so the reviewer can check claim by claim.
- Scope note as in the Italian page: these apps limit your own use; the guide does not cover parental controls
  («schermtijd kind» is a different question).
- Short quotes only (under 15 words), paraphrase the rest.

## Hubs (`nl/guides/index.html`, `nl/for/index.html`)

Written after the other pages, from their final Dutch H1s and descriptions. The guides hub lists the Dutch guides of
this batch AND the English-only ones still to come (shogi, bill tracker) through l.html, as the Italian hub did before
its batch 2 (check its git history: `git show 8cf9a81:it/guides/index.html`). Keep the CollectionPage / BreadcrumbList /
ItemList skeleton exactly; ItemList URLs point at the Dutch pages that exist and at English for the rest. The local-only
screen time guide gets a card and an ItemList entry. The for hub lists the three Dutch audience pages and
indie-ios-developers in English with the marker.

## Lessons from the earlier Tier 2 reviews (fr, es, it, pt): the most common must-fix items

- Softened hedges ("may" became "will") and hardened ones ("often" became "always"); keep the English strength.
- Added definitions or explanations that carry a claim the English page doesn't make.
- JSON-LD: keep the Italian skeleton exactly; a writer once pasted the ItemList into the breadcrumb. Every FAQ `name`
  equals its visible `<summary>` character for character; every schema answer says the same as the visible answer.
  Valid JSON (no raw " inside strings, no trailing commas).
- Price tokens are single-brace: `{P_MONTHLY@chessful}`, never `{{P_…}}`. Never put U+00A0 inside a Liquid tag or token
  (it breaks the build): only in visible prose.
- U+00A0 between € and the amount; NO space before %. Apple App Privacy labels quoted only from nl-apple-terms.md.
- Quote Apple labels exactly as the fetched page writes them, for each step. Never invent a condition. Never put your
  own translation of an English listing in quotes as if it were the app's text.
- Keep a competitor's privacy claim as strong as its listing; keep English hedges as strong as English.
- Dutch tells from Tier 1 (sheet § Tells): «hij»/«het» for a named app (write the name or «die»), «X komt met Y», outcome
  claims («lukt beter met X»), staged self-answered openers («Zoek je …?») in quick_answer and descriptions, split
  compounds in visible text, «u», Flemish words, title-case headings, «de» before app names, «naadloos», «cruciaal»,
  «niet alleen … maar ook», «Kortom», «Of je nu … of …», trailing participle clauses.

## Do NOT

Run `jekyll build`, `i18n.py map` or the stamp script; touch any file but your own; edit English or any other language's
files; edit `nl/llms.txt` or any app page (the main session wires hubs, llms lines and inbound links). Other sessions
(Spanish, Italian, Portuguese) work in this same checkout: never run `git` commands that change state (read-only
`git show`, `git log` are fine). Don't fetch apps.apple.com pages yourself (rate limits; use `$S/iap-nl.txt`); the
iTunes lookup API is fine.

## Reply with

The items in nl-writer-brief.md «Reply with», plus: the final H1 and seo.title, every competitor fact you dropped
because Dutch data was missing, the competitor prices you used (with the row from iap-nl.txt), and (local-only page)
the list of sources saved.
