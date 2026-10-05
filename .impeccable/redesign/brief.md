# Lagerland Apps — whole-site redesign: shared brief for every agent

Repo (read-only for you unless told otherwise): /home/user/lagerland-apps.github.io
Board dir (mock workspace): /tmp/claude-0/-home-user-lagerland-apps-github-io/5553b341-96c8-5ef2-9d5c-b9201c3f3508/scratchpad/board
Incumbent screenshots (current site, desktop + mobile): /tmp/claude-0/-home-user-lagerland-apps-github-io/5553b341-96c8-5ef2-9d5c-b9201c3f3508/scratchpad/before/
Locally built copy of the CURRENT site (static HTML): /tmp/claude-0/-home-user-lagerland-apps-github-io/5553b341-96c8-5ef2-9d5c-b9201c3f3508/scratchpad/site-before/

Read first: /home/user/lagerland-apps.github.io/PRODUCT.md and /home/user/lagerland-apps.github.io/CLAUDE.md.
Do NOT modify anything in the repo. This is a planning (shape) round: no site code is written.

## The ask (owner, verbatim intent)
"Redesign the whole site. Keep all existing permalinks, the seo/schema/quick_answer structure, and the App Store
conversion elements. I want all the app pages to have a unique feel — do not use the same static structure for each
page, build them from scratch. Provide me 3 different design styles on each page where I can select. The website must
be top of class, be creative."

## Owner decisions already made (binding)
1. Selection: the OWNER picks one of 3 styles per page; only the winner ships. (Each later build phase builds 3 real
   styles per page behind a review-only switcher; this round proposes them.)
2. Uniqueness: STANDALONE MICROSITES. Every app page is its own site: its own navigation, its own typography, its own
   world, its own page structure and section order. Only the footer links back to Lagerland.
3. "You decide what gives top-of-class pages" on the open incumbent rules. Decided as follows:
   - KEEP (binding): no-JS content guarantee — every word of content is in the server-rendered HTML and visible without
     JS (crawlers + AI citation). JS only enhances. Any animated number server-renders its real value.
   - KEEP (binding): prefers-reduced-motion disables non-essential motion.
   - RETIRED: "light + dark on every page". Each world commits to its own physical scene and lighting (one sentence: who,
     where, under what light). A world may be single-scheme (set color-scheme accordingly) or carry a designed pair only
     if its scene genuinely spans both.
   - RETIRED: Inter + Newsreader. Each microsite chooses its own faces; the studio site chooses its own.
   - NEW (binding): fonts are open-license faces available on Fontsource (npm @fontsource/<kebab-name>), self-hosted,
     latin subset, ≤ ~160 KB of font per page; no third-party font hosts (privacy brand).
   - NEW (binding): WCAG 2.2 AA contrast; keyboard focus visible and themed; mobile-first (most visitors arrive on a
     phone from Google / AI answers); static Jekyll on GitHub Pages (no build step, no npm bundling, plain CSS + small
     vanilla JS, no frameworks).

## Non-negotiable contract (every style must carry these, in its own vocabulary)
- Permalinks never change: /apps/<slug>/, /apps/<slug>/privacy/, /apps/<slug>/support/, /alternatives/<slug>/,
  /journal/<slug>/, /guides/<slug>/, /for/<slug>/, /transparency/, /lagerland-apps/, /support/.
- SEO/schema: <title>=seo.title, meta description=seo.description, canonical, OG/Twitter. App pages emit
  SoftwareApplication (+Offer/AggregateOffer), FAQPage, BreadcrumbList, HowTo (from how_it_works.steps), optional
  creative_work, founder Person/Organization. aggregateRating ONLY when ratings.count ≥ 25 (currently no app qualifies;
  highest is GymLogger X with 17) — so NO star ratings are shown anywhere.
- quick_answer renders as a visible Quick Answer block (+ speakable schema) HIGH on the page — it is the AEO answer.
- The "Quick reference" <details> ai-canonical block stays visible and crawlable (may be restyled/relocated, not hidden).
- App Store conversion elements: the official Apple "Download on the App Store" badge (Apple artwork — it may be framed,
  sized, placed in-world, but never redrawn, recoloured or restyled), Smart App Banner meta (head), desktop "scan to
  install" QR (assets/qr/<slug>.svg; shown on wide screens because desktop visitors must get the app onto their iPhone),
  a sticky download bar that appears after the hero action scrolls away (re-skinned in-world), price pills / price
  statement (from front matter price.model + price.value — never invent prices). Mac-only apps (appmeta, mockly) and Mac+iOS
  (mediakit) still use the App Store badge; the QR is less central for Mac-only apps.
- Privacy is SHOWN, not claimed: privacy statements link to the transparency record (/transparency/, _data/transparency.yml).
- E-E-A-T: maker/freshness line (Built by Lagerland Apps · last updated · first released · version), founder block where
  front matter has `founder`, privacy policy + support links.
- Counts are computed from collections (never hard-code "19 apps" / "96 comparisons").
- NEVER invent: ratings, review quotes, user counts, press mentions, prices, features. Use only front matter, the app's
  markdown body, _data/*.yml, journal posts, alternatives pages. Illustrative/demo material is allowed only if labelled
  as illustrative.

## Content each app microsite must be able to carry (from _layouts/app.html; front-matter blocks vary per app)
hero (headline, subheadline, pre_headline, cta), quick_answer, ai-canonical quick reference, trust facts (platforms, 0
third-party SDKs, no ads, local-first), spotlight (optional signature mechanic + stats), value_points, pricing
(_includes/pricing.html: plans/tiers), show_body markdown "About" prose, founder story, who_for / who_not_for,
screenshots (carousel), features (list), how_it_works (method steps → HowTo), insight_gallery, plateau_disclosure,
training_vocabulary, comparison_table (vs competitors) + inline CTA, related_journal, faq, roadmap, coach_cta,
privacy summary (data_collection / tracking / account_required / notes / Apple privacy label) + links to privacy policy
and support, alternatives_to (links to /alternatives/ pages), "you might also like" (other Lagerland apps), closing CTA,
maker/freshness. A style decides ORDER, GROUPING and FORM of these — the whole page, not just the hero.

## Surfaces that wear which world (decided; owner can override)
- STUDIO world: homepage /, /apps/ index, /alternatives/ index, /for/ hub + audience pages, /guides/ hub + guides,
  /journal/ index + 42 posts, /transparency/, /lagerland-apps/ (about), /support/, 404. Homepage is a Persuade surface;
  journal/guides/transparency/alternatives index are Read surfaces — the studio world must survive both.
- Each APP world (microsite): /apps/<slug>/ (Persuade), plus its /privacy/ and /support/ sub-pages and every
  /alternatives/<competitor>/ page that targets this app (Read-mode variants of the same world: the world owns the frame,
  the reading column stays calm).
- Microsite footer: one shared thin "A Lagerland app" strip linking back to the studio (home, all apps, transparency,
  privacy policy, support). That strip is the ONLY shared element across microsites.

## Assets that exist (do not assume others)
- App icons 1024px: assets/icons/<slug>.png (Tare has none yet; owner decided "no images yet" for Tare — upcoming, unlisted).
- Screenshots: assets/screenshots/<slug>/*.png — iPhone portrait 1206x2622, mostly dark UIs (Pawza, Soon., Taskful Day
  light UIs; Millrace amber/honey). Mac apps appmeta, mediakit, mockly have landscape Mac screenshots.
  Some files in wanderwiki/ and mockly/11.png, allpaid/33 are NOT images (ignore them).
- Downscaled copies for mocks: <board>/assets/<slug>/icon.png and s1.jpg..s4.jpg; studio mark <board>/assets/lagerland-mark.png.
- QR codes assets/qr/<slug>.svg; OG cards assets/og/<slug>.png; one video assets/videos/wanderwiki_preview.mov.
- No photography, no illustration library, no image generation available in this session. A direction that needs new
  raster art must say exactly what asset is needed (it becomes a later production task) and must still work with
  what exists now. Prefer worlds whose material is typographic, chromatic, structural, or drawn from the app's own UI.

## The incumbent (anti-reference)
v3 "Paper & Ink": warm cream ground, Newsreader serif display + Inter, purple accent, pill rows, card grids, one
identical template for all 20 app pages (icon+name badge, split hero copy-left/phone-right, badge row, trust bar of 4
stats, grid of value cards, numbered feature rows...). Treat it as evidence of what the subject is, never as authority.

## Calibration (read twice)
AI-generated interfaces cluster around: (a) warm cream ground + high-contrast serif display + terracotta/red accent;
(b) near-black + one neon accent + glowing edges; (c) broadsheet-editorial hairlines + italic display serif + small
tracked mono labels. Landing in one where the brief leaves aesthetics free means the self-check failed. If someone could
guess your aesthetic from the category alone ("chess → wood and gold", "health → dark dashboard with neon rings",
"finance → blue fintech", "dev tool → terminal green"), rework it.
Training-default faces — naming one requires a reason no other face could satisfy (subject association is never that
reason): Fraunces, Playfair Display, Cormorant, Lora, Crimson, Newsreader, Syne, Space Grotesk, Space Mono, IBM Plex,
Inter-as-display, DM Sans, DM Serif, Outfit, Plus Jakarta Sans, Instrument Sans.
Your measured rendition prior: warm/bookish/family/child-facing subjects come out cream + serif + italic + lamplight.
Treat that palette as already spent.
Light or dark is never picked by category: pick it from the use scene.

## Craft floor refusals (apply to every style and every mock)
No eyebrow/kicker label above headings (banned). No same-size icon+heading+text card grids as page structure. No
hero-metric template (big number + small label row). No section numbers 01/02/03 unless the sequence is real information
(e.g. how_it_works steps). No gradient text. No decorative glass/blur. No coloured border-left/right >1px callouts. No hard
offset shadows unless the world is genuinely neobrutalist. No sparklines/progress rings as filler. No monospace as a
"technical" costume (mono only for real data/code/measurements). No emoji/unicode as icons. No split hero
(copy left / phone right / badge row under it) and no centred-headline-over-a-row-of-cards — that is the template
whatever world paints it.

## Mode rules — Persuade (app pages and homepage)
The opening must make the offer intelligible and desirable, expose a clear action (here: the App Store download, in its
working form — the official badge, plus the QR on desktop), and demonstrate something only this product can prove.
The world may be the CARRIER of the page, never a picture of it: a page painted as a poster with no working parts fails;
a generic product page with the world as an accent also fails. Material coverage: the world's material is the ground and
major surfaces; its type sets the headlines. Commitment is depth, not performance: one dominant move plus material, type,
spacing; other regions hold still in that material. When the world is an object, the page is that one object seen once,
at one scale, keeping its real form. Text always reads; the primary action is unmistakable; sections keep a steady
vertical rhythm.

## Mode rules — Read (studio journal/guides; app privacy/support/alternatives pages)
The world owns the frame (masthead, rail, ground, title, openers, how tables/code/callouts are set); the reading column
stays calm (reading face, real contrast, 60–75ch measure). A guide reads as a guide, an article as an article.

## How a direction is derived (impeccable new-work §3)
1. Name the product's unique mechanism in one sentence, the audience's real scene, its cultural home, and what the first
   viewport must prove. Note the page this category always ships and its predictable opposite; both are the rut. The
   literal reading of the product's name/metaphor also joins the rut (at most one candidate may use it).
2. From the audience's cultural world list SEVEN concrete visual systems, artifacts, places, rituals, publications,
   notations, identity programs, data graphics or interfaces the audience knows by heart (not the tools they operate as
   costumes), each with one line on why it resonates AND how it can carry the mechanism, ordered by resonance (1 = most
   resonant). Near-duplicates count once. The seven must span at least THREE material families (e.g. print/paper,
   textile, signage/wayfinding, broadcast/screen, instrument/measurement, architecture/place, ritual/object, cartography...).
   Persuade surfaces also ask: what would this be as a physical object, and what did its world look like before the web?
3. Each direction joins a reusable visual world to a concrete page experience, decided as one.

## The three styles per surface (dice protocol — the roll service is offline, so the roll is "degraded": no catalog
## challengers; the dealt index still binds)
- Run: `/home/user/lagerland-apps.github.io/.claude/skills/impeccable/scripts/impeccable concept-seed --scope direction --mode persuade`
  (run it from /home/user/lagerland-apps.github.io). It prints a seed key and ASSIGNED INDEX N (1..7).
- Then run the same with `--from <key> --reroll 1` → index R1; if R1 == N, use `--reroll 2` (and so on) until distinct.
- STYLE A, kicker "THE ROLL": your candidate N, fully committed (never softened toward your favourite).
- STYLE B, kicker "IMPECCABLE’S PICK": your top-ranked candidate #1 — UNLESS N == 1 or R1 == 1; then STYLE B is the next
  distinct re-roll (kicker "SECOND ROLL") and STYLE A notes it also topped your list. The pick's risk line names its
  familiarity honestly when true.
- STYLE C, kicker "SECOND ROLL": candidate R1.
- Also write a one-line "canon" card: the category standard played straight (the owner's standing exit; never recommend it).
- Never expose seed/assignment metadata in user-facing labels other than these kickers.

## Style card anatomy (every style)
label (an evocative 2–4 word name), kicker, lineage (the real-world source), thesis (one sentence: the idea this page owns
and the category-default arrangement it refuses), scene (one sentence: who, where, under what light → scheme),
scheme (light | dark | pair), colorStrategy (Restrained | Committed | Full palette | Drenched), palette (4–7 hex values,
each with its role), type (display face, text face, optional utility face — each with weights and WHY it belongs to this
world; must exist on Fontsource), materials, firstViewportDesktop (exact composition at 1440: what is where, at what
scale, where the badge + QR + price sit), firstViewportMobile (exact composition at 390), conversion (how badge, QR,
sticky bar, price statement and Smart App Banner live in this world's vocabulary), visitorPath (ordered list of the
page's sections in this world's own forms, mapping the real front-matter blocks; this is a from-scratch structure, not
the incumbent order), navigation (the microsite's own nav in world vocabulary), signatureInteraction (name, technique,
no-JS fallback, reduced-motion behaviour), motionGrammar, readModeVariant (how privacy/support/alternatives pages wear
this world), assetsNeeded (any new raster/vector asset this style needs; say "none" if it runs on existing assets),
risk (honest), memoryTest (what a visitor would describe an hour later).
