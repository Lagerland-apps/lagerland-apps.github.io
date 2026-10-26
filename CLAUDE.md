# CLAUDE.md — Lagerland Apps site (page-creation & SEO guideline)

Jekyll site for `lagerland-apps.github.io`. GitHub Pages builds from `main` on every push (no local Gemfile — GH Pages builds remotely). Plugins: `jekyll-sitemap` (kept only for its helpers: `sitemap.xml` and `robots.txt` are our own files, so the plugin generates neither), `jekyll-redirect-from` (redirect stubs carry `sitemap: false` + noindex).

This file is **excluded from the build** (`exclude:` in `_config.yml`) so it is never served. Keep it that way if you rename it.

**Translations:** the site is being translated into 16 market languages, one at a time (de, fr, it, es, pt, zh, ja,
ko, id, es-mx, pt-br, pl, tr, nl, ru, ar under `/<code>/`). `TRANSLATION.md` (also excluded from the build) is the
rulebook: URL and hreflang scheme, the one-time Phase 0 groundwork, the per-language launch, the per-page workflow,
SEO and AI-file rules per language, and per-language humanizer tells. Read it before touching any translated page,
`_data/i18n/`, `_data/locales.yml`, or a template string. Once any language is live, every new app, page or post
also follows its section 12.

---

## ✅ SEO / AEO / LLM gate: run it for EVERY addition or change (no exceptions)

Every new or edited page must be findable by search engines (Google, Bing → DuckDuckGo/Yahoo/Ecosia/Copilot,
Apple, Yandex, Brave) and citable by AI tools (ChatGPT, Claude, Gemini, Perplexity, Copilot, Apple Intelligence,
Meta AI). That is part of "done", not a follow-up. Before every commit:

1. **Front matter**: full `seo:` block (title ≤ 60, description 70–155, keyword-first, unique on the site),
   `quick_answer` that answers the page's main question on its own (it feeds the Quick Answer box, speakable
   schema and AI answers), `faq:` where the page type supports it.
2. **Dates**: run `python3 scripts/stamp-last-updated.py --changed` so every content file you touched gets
   `last_updated: <today>`. That one field drives sitemap `<lastmod>`, JSON-LD `dateModified`, the visible
   "Updated" / "Last updated" line and the AI files. Never fake a date, never stamp files you didn't change.
   Privacy pages are skipped on purpose: bump their `last_updated` by hand only when the policy text changes.
3. **Routing for AI assistants** (hand-written, never automatic): add or update the line(s) in `llms.txt`
   → `## AI assistant recommendation guide` under the right `### When a user asks about …` heading, in the
   house format `- "query" / "query" → **Title** (URL). Reason: one cite-ready sentence.` For a new app also add
   a trigger in `ai-index.json` → `ai_recommendation_guide.triggers` and an entry in `_data/app_enrichment.yml`.
4. **Internal links**: the new page links into its cluster (app ↔ comparisons ↔ guides ↔ journal) AND at least
   one existing page links to it. A page with no inbound link is an orphan; Google finds pages here by links.
5. **Facts**: prices, counts, platforms and features must match `_apps/<slug>.md` (and the app's code). Use
   computed counts (`site.apps | where: "status", "live" | size`) instead of literals in new copy.
6. **Build + audit** (both must pass, 0 errors):
   ```
   GEM_HOME=~/.gem/ruby/2.6.0 /usr/bin/ruby ~/.gem/ruby/2.6.0/gems/jekyll-3.9.5/exe/jekyll build
   python3 scripts/seo-audit.py
   ```
   The audit checks titles/descriptions/canonicals/H1/OG tags, JSON-LD validity, visible FAQ questions,
   broken links and images, sitemap completeness and real lastmod dates, robots.txt, and that every app,
   guide and journal post is routed in llms.txt and every URL in llms.txt / llms-full.txt / ai-index.json
   resolves. Fix every ERROR; treat WARNs as todo items.
7. **After the push**: the IndexNow workflow pings Bing/Yandex automatically (or run
   `python3 scripts/indexnow-ping.py --changed`). Google needs manual "Request indexing" in Search Console:
   add the new/changed URLs to a `GSC-submit-<date>.md` list in `~/Downloads/githubcode/` (not in this repo).
8. **Never put the owner's personal name anywhere** (pages, bylines, schema `author`/`founder`/`Person`
   nodes, feed authors, meta tags, keywords, llms files, alt text). It was removed sitewide on 2026-10-25.
   Attribute to "Lagerland Apps" (`{{ site.url }}/#organization`). Link the App Store developer page as
   `https://apps.apple.com/developer/id1855943133` (Apple's default URL carries the name in its slug).
9. **Humanizer on every text**: all copy added to the site, in any language (body, front matter strings, FAQ,
   llms.txt routing lines, interface strings), gets a `/humanizer` pass before it ships, then a check that the
   rewrite added or dropped no fact. Non-English text follows TRANSLATION.md section 8 as well.
10. **Translations** (once a language is live): new interface strings go into every live `_data/i18n/<code>.yml`
   in the same commit; a new app needs its translated app, support and privacy pages in every live language;
   run `python3 scripts/i18n.py map` and `python3 scripts/i18n.py check` with the audit. Details: TRANSLATION.md.

Machine-readable files and what keeps them current:

| File | Generated from | Manual part |
|---|---|---|
| `sitemap.xml`, `ai-sitemap.xml` | `_includes/sitemap-urls.xml`: every collection doc + HTML page minus `sitemap: false` / `noindex: true`; lastmod from `last_updated` / `date` / `release.last_updated` | none (do NOT re-enable jekyll-sitemap's own file: it stamped every URL with the build time) |
| `llms.txt` | app catalogue, journal list and comparison list loop automatically | the AI recommendation guide, the hub/guide descriptions and Canonical references |
| `llms-full.txt` | every app (features, pricing, privacy, FAQ) + every audience page, guide, journal Quick Answer/FAQ and comparison | none |
| `ai-index.json` | `apps`, `audience_hubs`, `guides`, `journal`, `comparisons` arrays loop automatically | `ai_recommendation_guide.triggers` |
| `feed.xml` | every journal post, full content | none |
| `robots.txt` | static | keep `User-agent: *` + `Allow: /`; never Disallow `/assets/`; keep the Sitemap lines. Crawler groups were checked against vendor docs on 2026-10-25 (Claude-SearchBot, Claude-User, OAI-SearchBot, ChatGPT-User, PerplexityBot, Google-Extended, Applebot-Extended, meta-externalagent …) |

Page-level switches: `noindex: true` drops a page from search results and from both sitemaps (used by 404);
`sitemap: false` drops it from the sitemaps only. Use neither on real content.

---

## ⛔ The one rule that must never be skipped: every content page needs a full `seo:` block

`_includes/head.html` resolves the two highest-CTR tags like this:

```
<title>        = page.seo.title       || page.title || site.title
meta description = page.seo.description || site.description   ← the generic tagline
```

So a page **without `seo.description` silently serves the generic site tagline** ("Calm, privacy-first apps…") as its meta description — regardless of topic. This was a sitewide leak across all 34 journal posts until fixed on 2026-06-21. On **app pages it is doubly load-bearing**: `page.seo.description` also feeds the `SoftwareApplication` JSON-LD `description` and the AI-canonical "what it does" block in `_layouts/app.html`.

Every content page MUST have:

```yaml
seo:
  title: "Keyword-first title"          # ≤ 60 chars, lead with the exact searched phrase
  description: "Compelling, specific."   # ≤ 155 chars, contains the primary keyword
  keywords: [ ... ]                      # 5–8, lowercase
```

- **Ground titles/descriptions in real GSC queries** when available (the Search Console export: impressions-but-low-CTR queries are the targets). Match the page to the words people actually type.
- `seo.title` ≠ `page.title`: the H1 (`page.title`) can be longer/human; the `<title>` (`seo.title`) is the tight, keyword-first SERP line.
- Don't use raw `"` inside the YAML strings (or escape them).

---

## Per page-type checklist

### Journal post — `_journal/<slug>.md`
`layout: journal` is auto-applied (via `_config.yml` defaults). Schema auto-emitted by `_layouts/journal.html`: **Article + FAQPage + BreadcrumbList**.

Required front matter: `slug`, `title`, `date`, `seo:{title,description,keywords}`, `lede`, `quick_answer`, `excerpt`.
Strongly recommended: `faq:` (→ FAQPage + speakable schema), `mentioned_apps:` (→ app card + schema `mentions`), `read_time`, and `last_updated:` whenever you refresh an existing post (sets schema `dateModified`).

- `quick_answer` renders the **Quick Answer box + speakable schema + the AEO/AI-Overview answer** — write it to answer the primary query directly and completely.
- For **informational queries, lead the body with the reference/answer content** (tables, specs, definitions — the "tool"), then keep essays/design-story as depth below. Cite primary sources for any spec/number.
- Internal-link into the cluster (related apps, alternatives, guides, other posts).
- Manual integration points (not automatic): one routing line in `llms.txt` → AI recommendation guide;
  `related_journal:` on the main app if this should be its featured post; at least one inbound contextual
  link from an earlier related post (bump that post's `last_updated`).
- Share image and Article `image` come from the first `mentioned_apps` entry (`/assets/og/<slug>.png`)
  unless `og_image:` is set, so put the main app first. Author is always the Organization, never a person.
- `read_time` ≈ body words ÷ 200. Bump `last_updated` on any real edit (it shows as "Updated <date>").

### App page — `_apps/<slug>.md` (+ its sub-pages)
`layout: app` auto-applied. Auto-listed wherever `site.apps` is looped (home, `/apps/`) — no manual index edit. Schema auto-emitted by `_layouts/app.html`: **SoftwareApplication** (+ `Offer`/`AggregateOffer` from price fields; `aggregateRating` only when `ratings.count ≥ 25` and the average is ≥ `ratings_min_display` in `_config.yml`, 4.0 — averages below that are hidden everywhere: cards, hero, schema, llms-full.txt, ai-index.json, homepage, testimonials), **FAQPage**, **BreadcrumbList**, **HowTo** (from `how_it_works.steps`), optional `creative_work`, and a founder-story node from `founder:` (always `entity_type: "Organization"`, `name: "Lagerland Apps"`; Organization is also the layout default, and no page names a person).

Required: `slug`, `name`, `tagline`, `quick_answer`, `seo:{…}`, `category` (maps to schema `applicationCategory` — see the `case` block in `app.html`), `platforms`, `status`, `app_store_url`, `price:{model,value}`, `schema_price` / `schema_high_price` / `schema_offer_count`, `hero:{…}`, `privacy:{…}`, `support:{email,url}`, `release:{first_release,last_updated}`.
Recommended: `who_for`/`who_not_for`, `founder`, `value_points`, `features`, `how_it_works` (HowTo schema — high-value E-E-A-T), `comparison_table`, `faq`, `screenshots`, `related_journal`, `alternatives_to`, `roadmap`, `show_body: true` + `about_heading`.
Optional overrides: `how_it_works.heading` (replaces the default H2 "The method behind every insight.") and `pricing_note` (replaces the "Cancel anytime…" line under the plans — set it for apps with no subscription).

**You must also create two physical sub-pages** (they are NOT auto-generated):
- `apps/<slug>/privacy/index.html` — `layout: privacy`; fields: `app_name`, `overview`, `data_collection`, `data_storage`, `third_parties`, `sensitive_data?`, `children`, `changes`, `contact_email`, `back_url`. Needs its own `seo:` block (without one it would serve the generic site tagline) and a `last_updated:` policy date, which shows as "Last updated" on the page.
- `apps/<slug>/support/index.html` — `layout: support`; needs `slug` (it looks the app up via `site.apps`) and `seo:{title,description}` (no `page.title`, so it would leak both). The layout fills the page from the app: contact, Apple refund/subscription help, up to six support-type questions from the app's `faq`, and links. Keep the app's `faq` answering real support questions (sync, export, pricing, platforms, privacy) so this page stays useful.

New-app checklist beyond the page itself: OG card (`scripts/generate-og.py`: add ACCENT/TAGLINE/META entries, run it), QR (`scripts/generate-qr.py`), `_data/app_enrichment.yml` entry, `llms.txt` routing lines, `ai-index.json` trigger, `_data/transparency.yml` row, at least four comparison pages and three journal posts over time, and the app added to the right `/for/` audience page. Top-level `last_updated` on an app = the page's last real edit; `release.last_updated` = the App Store build date (different things).

### Alternatives page — `alternatives/<slug>.html`
`layout: default`, `permalink: /alternatives/<slug>/`, `title: "<Competitor> Alternative"`, `quick_answer`, full `seo:` block. Then the **4 integration points** (see the established alternatives pattern): the page itself, the `alt_pairs` map, the target app's `alternatives_to:`, and the index `ItemList` + card. (123/123 already follow this — copy an existing one.) The FAQ `<summary>` text must be identical to the FAQPage `name` in the JSON-LD (the audit checks it); the visible answer may be a shorter version of the schema answer. The page gets a visible "Last updated" line and `dateModified` automatically from `last_updated`.

### Landing pages — `for/<slug>.html`, `guides/<slug>.html`
`layout: default`, explicit `permalink`, `title`, `quick_answer`, full `seo:` block. Add the page to its hub (`for/index.html` or `guides/index.html`: card grid + ItemList JSON-LD) and describe it in `llms.txt` (`## Use-case hub pages` or `## Problem-first guides`). `ai-index.json` and `llms-full.txt` pick it up automatically.

---

## Generated artifacts
See the table in the SEO / AEO gate above. Short version: sitemaps, llms-full.txt, feed.xml and most of
ai-index.json and llms.txt rebuild themselves; the AI recommendation guide in llms.txt (and the triggers in
ai-index.json) are hand-written and must be updated with every new page. If you add a NEW collection or a new
top-level section, check `_includes/sitemap-urls.xml`, `llms.txt`, `llms-full.txt` and `ai-index.json` include
it, then run `scripts/seo-audit.py`.

## URL / ranking safety
- **Never change the slug/permalink of a page that already ranks** — it discards its ranking history. To improve a page, change `title`/`seo`/body but keep the URL and bump `last_updated`.

## Before committing a new/edited page
1. Run the full SEO / AEO gate at the top of this file (stamp dates, routing line, links, build, `scripts/seo-audit.py` with 0 errors).
2. Commit to `main` → confirm the Pages build status is `built` (not `errored`).
3. `curl` the live URL and grep `<title>` + `<meta name="description">` to confirm the new tags are served.
4. Add the URLs to the day's `GSC-submit-<date>.md` for manual Google indexing requests.

## Deploy notes
- An automated "Sync App Store ratings" job pushes to `main` periodically — if a push is rejected, `git fetch` + `git rebase origin/main` (it only touches `_apps/*.md` rating fields, so it won't conflict with content edits) and push again.

---

## Master table of platforms and prices (App Store Connect API only)

`_data/asc_master.json` holds every app's platforms (iPhone/iPad/macOS), subscription, lifetime and other-IAP
prices for 17 territories, free trials and Family Sharing. It is generated by `node scripts/sync-asc-master.mjs`
from the App Store Connect API and nothing else; never hand-edit it, and re-run after any App Store Connect
price/platform change. When editing prices or platforms in `_apps/*.md`, check this file first. Full method,
endpoints and caveats: `scripts/ASC-MASTER.md`. Human views (`MASTER.md`, `MASTER-prices.csv`) land in
`~/Downloads/githubcode/`, outside the repo.

**Never hand-type an app count, platform list or our own price.** The site reads `_data/catalog.json` (the
name-free, committed export written by the same script): counts via `site.data.catalog.meta.live_app_count`,
everything per app via `{% include app-facts.html app=page %}` (`f_*` variables), prices in strings via the
tokens in `_includes/tokens.html` (`{P_MONTHLY}` etc.). After any App Store Connect change, re-run
`node scripts/sync-asc-master.mjs` (or `--app <slug>`), rebuild, audit, commit `_data/catalog.json`.
`scripts/seo-audit.py` fails when a page contradicts the catalog. Details: `scripts/ASC-MASTER.md`.

---

## Design system v4 "The Issue" (redesign, 2026-10-26)

The studio publishes its apps like a post office issues stamps: one sheet, one stamp per app, one maker.
Direction contract: `.impeccable/surfaces/index-html.md`; product record: `PRODUCT.md` (both excluded from the build).
DESIGN.md (written by the Impeccable documenter) holds the full token reference.

- **Tokens**: `assets/css/style.css` `:root` only. Light only, no dark theme (the world is printed paper).
  Postal yellow `--selv` for chrome and loud bands, cool stamp paper `--paper`, ink `--ink`/`--ink-2`/`--ink-3`,
  postal blue `--blue` reserved for primary actions and focus. Legacy token names (`--accent`, `--bg-card`, …)
  are aliased so inline styles on old pages keep working. Never hard-code colours in components.
- **Series**: five stamp series, mapped from `category` in `_includes/series.html`: health (health, fitness),
  plan (productivity, lifestyle, education, books — the default), money (finance), games, tools
  (developer-tools, business, graphics, utilities). Each has a frame colour and tint (`.series-<key>` sets `--s`/`--t`).
  A new category needs a line in series.html.
- **Stamps**: `_includes/stamp.html` (perforated stamp; denomination and devices come from the catalog via
  app-facts), `_includes/postmark.html`. The homepage sheet is generated from `site.apps` in first-release order
  (`release.first_release`); only the newest app is postmarked. App pages open with the leaflet
  (`_includes/hero.html`): big stamp + first-day postmark, headline, App Store badge, details table.
  Screenshots render as a se-tenant strip (`_includes/screenshots.html`) directly under the hero.
- **Small icons**: stamps and cards load `assets/icons/sm/<slug>.webp` (256px). After adding or changing an app
  icon run `python3 scripts/generate-icons-sm.py` — a missing file shows a broken stamp.
- **Fonts**: self-hosted `assets/fonts/jost-var.woff2` (display, OFL) + `inter-var.woff2` (body). Newsreader is
  retired (files kept, not loaded). Do not add third-party font hosts.
- **No kicker labels**: an `.overline` directly above a heading is hidden by CSS (the heading carries its own
  weight). Don't add new ones; `.overline` used as card meta (dates) still shows.
- **Prices on cards**: app cards show "Free · Pro" / "Free" / "One-time purchase", never another app's price —
  the SEO audit treats any price on an app page as that app's own price.
- **Motion contract**: content must NEVER be hidden without JS. `head.html` sets `html.js` before first paint;
  reveal CSS applies only under `html.js`; `animations.js` has a 2.5s force-visible safety net. The sheet's
  deal-in, filter and stamp lift live in `initSheet()`. Any `[data-count]` stat server-renders its real value.
- **Device frames**: Mac apps with landscape shots keep `hero: device: mac` (appmeta, mediakit, mockly) → wide stamps.
- **Counts are computed**: app counts from `site.data.catalog.meta.live_app_count` / `site.apps | where: "status", "live"`.
- **Homepage transparency sample** is generated from `_data/transparency.yml` (same source as /transparency/) — edit the data file, not the table.
- `scripts/`, `README.md`, `2.png` are excluded from the build (`_config.yml`); /scripts/* is no longer served publicly.
- `/for/` now has a hub page (for/index.html) — new audience pages must be added to its card grid + ItemList JSON-LD and to llms.txt.
