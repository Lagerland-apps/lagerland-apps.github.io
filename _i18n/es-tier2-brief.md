# Writer brief: Spanish (es, Spain) Tier 2, batch 1 (guides and audience pages)

Never published (`_i18n` is excluded from the build). Repo root:
`/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/`.

**Read `_i18n/es-writer-brief.md` first and follow all of it.** This file adds what is different for Tier 2.
Where the two disagree, this file wins.

## Your inputs

- The English source page (`guides/<slug>.html` or `for/<slug>.html`): it holds the facts.
- The French page with the same path under `fr/`: structural template only (Liquid, JSON-LD skeleton, card and table
  markup, how links and tokens are written). The French writers already replaced US-only context (US prices, US
  ratings) with France data; you do the same with SPAIN data. Never translate from French.
- `/Users/anttiaittamaa/Downloads/githubcode/es-tier2-research-2026-11-19.md`: your page's row (Spanish primary and
  secondary queries, demand) and the Spanish App Store data at the bottom (which competitors are sold in Spain, their
  Spanish store names, Spanish rating counts, Spanish in-app prices where fetched).
- `_i18n/es.md` (sheet), `_i18n/es-apple-terms.md`, `_i18n/es-glossary.md` (the sections of the apps your page names).

## Pages in this batch

| Page | Write to | Primary query |
|---|---|---|
| guides/best-chess-apps-iphone.html | es/guides/best-chess-apps-iphone.html | mejor app de ajedrez |
| guides/best-logic-puzzle-games-iphone.html | es/guides/best-logic-puzzle-games-iphone.html | mejores juegos de lógica iphone |
| guides/workout-app-without-subscription.html | es/guides/workout-app-without-subscription.html | mejor app gimnasio gratis (angle: sin suscripción) |
| guides/best-xiangqi-apps-iphone.html | es/guides/best-xiangqi-apps-iphone.html | ajedrez chino online |
| for/shift-workers.html | es/for/shift-workers.html | trabajo a turnos y salud |
| for/apple-health-power-users.html | es/for/apple-health-power-users.html | mejores apps salud apple watch |
| for/calm-productivity.html | es/for/calm-productivity.html | mejores apps de productividad iphone |
| (local-only, no English twin) | es/guides/limitar-tiempo-de-pantalla-iphone.html | como limitar el tiempo de pantalla en iphone |
| guides/index.html, for/index.html (hubs, written last) | es/guides/index.html, es/for/index.html | brand-led |

Keyword collisions to respect: `ajedrez chino` belongs to the Xiangqiful app page, `dormir después de trabajar de
noche` to AfterShift, `hrv apple watch` to Observa, `app lista de tareas` and `app para organizar el día` to Taskful
Day, `bloquear apps iphone` to EarnLock, `app registro gimnasio` to LiftLog. Don't use those as your primary or in your
`seo.title`; a mention in body text is fine.

## Competitors (Tier 2 rules, TRANSLATION.md 6.4 and 6.6)

- A "best X apps" page lists only apps sold in the Spanish App Store (research file). An app marked NOT SOLD IN SPAIN
  is dropped, with any sentence that depends on it.
- Competitor facts are per market. Ratings: only the Spanish count and average from the research file, written as
  «El App Store de España le da 4,7 sobre 5 con 56.297 valoraciones (consultado el 19 de noviembre de 2026)», or
  leave ratings out. Never the US or French numbers.
- Competitor prices: only Spanish euro prices from the research file (or from `es-t2/iap-out.md` in the session
  scratch, path given in your prompt if any), typed as `13,99 €` with U+00A0, with «(App Store de España, consultado
  el 19 de noviembre de 2026)» once per page. A US-dollar figure on the English page with no Spanish price in the data:
  drop the number and keep the qualitative fact («de pago», «suscripción mensual o anual», «compra única»). Never
  convert dollars. Never arithmetic on OUR prices; arithmetic on a competitor's verified euro price is allowed only
  where the English page does the same calculation (state the inputs).
- Competitor names are written as in English (Chess.com, Hevy, Strong); the Spanish store title may be mentioned once
  where it helps people find the app («en el App Store de España aparece como «Ajedrez - Jugar y Aprender»»).
- App Store links to competitors: `https://apps.apple.com/es/app/id<ID>`.
- Feature claims about competitors: only what the English page says (or, on the local-only page, what the app's own
  Spanish App Store description says, see below).

## Links

- Use `{% include l.html url="..." %}` for every internal link, as the French page does. It resolves to the Spanish
  page when it exists at build time (all Tier 1 pages, and the other pages of this batch), else English with the
  marker. Do not hard-code `/es/` URLs in body links.
- Each page links to at least one other page of this batch where the English page links to its twin, and to the
  relevant Spanish app pages.

## YMYL pages (shift-workers, apple-health-power-users)

Keep every caveat and every "not medical advice" line. No new health claims, numbers or studies. Where the English
page cites a source, keep the citation. Apple Health names exactly as es-apple-terms.md (Salud de Apple, la app Salud,
VFC (SDNN) for Observa's HRV, sleep stages Despierto, REM, Esencial, Sueño profundo).

## Lessons from the French and Spanish reviews (avoid these, they were the most common must-fix items)

- Softened hedges ("may" became "will") and hardened ones ("often" became "always"); keep the English strength.
- Added definitions or explanations that carry a claim the English page doesn't make.
- JSON-LD: keep the French skeleton exactly (WebPage / BreadcrumbList / ItemList / FAQPage nesting); a writer once
  pasted the ItemList into the breadcrumb. `"inLanguage": "es-ES"`. Every FAQ `name` equals its visible `<summary>`
  character for character; every schema answer says the same as the visible answer.
- Price tokens are single-brace: `{P_MONTHLY@chessful}`, never `{{P_…}}`. Tokens go inside text that the page
  passes through the token include, exactly as the French page does; copy its pattern.
- Apple App Privacy labels quoted only from es-apple-terms.md («No se recopilan datos»).
- «el App Store» masculine; «la app»; «el Apple Watch».

## Local-only page: `es/guides/limitar-tiempo-de-pantalla-iphone.html` (TRANSLATION.md 6.7)

- Front matter: `local_only: true`, NO `ref`, NO `translated_from`, `permalink: /es/guides/limitar-tiempo-de-pantalla-iphone/`,
  `last_updated: 2026-11-19`, full `seo`, `quick_answer`, faq in JSON-LD + visible, `datePublished` 2026-11-19.
- Structure: model it on `fr/guides/limiter-temps-ecran-iphone.html` (read it), but every fact must come from a Spanish
  or primary source you fetched yourself today:
  - Apple's Screen Time («Tiempo de uso») in iOS 27, Spain wording: https://support.apple.com/es-es/guide/iphone/iphbfa595995/ios
    and the rows in es-apple-terms.md («Horario de tiempo de uso», «Límites de tiempo»). iOS 27 names first. Do not
    describe iOS 26 labels (Apple Spain's older names were not verified).
  - Each competitor's own Spanish App Store description: `curl -s "https://itunes.apple.com/lookup?country=es&lang=es_es&id=<ID>"`
    (field `description`). IDs: Opal 1497465230, one sec 1532875441, ScreenZen 1541027222, Jomo 1609960918, Cape
    6444819615, Forest 866450515, AppBlock 1515753232. Brick (6448794069) has no Spanish listing: leave it out.
    Describe each app only with what its Spanish description says; no prices unless you can quote the Spanish listing.
  - EarnLock facts from `_apps/earnlock.md`, the Spanish page `es/apps/earnlock/index.md` and
    `~/Downloads/githubcode/.agents/product-marketing.md` → EarnLock's APP_BLUEPRINT.md §10 (claims register only).
    EarnLock's prices only through `{P_MONTHLY@earnlock}`, `{P_YEARLY@earnlock}`, `{P_LIFETIME@earnlock}` as the French
    page does. Disclose that EarnLock is ours, as the French page does.
- Save every page you fetch for facts into
  `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-Pj9vQR/70be057c-fdb0-4a19-959a-48f6b17f7b81/scratchpad/es-t2/sources/limitar-tiempo-de-pantalla-iphone/`
  (one file per source, named by app or Apple page) so the reviewer can check claim by claim.
- Scope note as in the French page: these apps limit your own use; the guide does not cover parental controls.
- Short quotes only (under 15 words), paraphrase the rest.

## Do NOT

Run `jekyll build`, `i18n.py map` or the stamp script; touch any file but your own; edit English, French, German or
Italian files; edit `es/llms.txt` or any app page (the main session wires hubs, llms lines and inbound links).
Other sessions (Italian, Portuguese) work in this same checkout: never run `git` commands that change state.

## Reply with

The items in es-writer-brief.md «Reply with», plus: every competitor fact you dropped because Spain data was missing,
and (local-only page) the list of sources saved.
