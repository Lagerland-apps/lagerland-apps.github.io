# CLAUDE.md — Lagerland Apps site (page-creation & SEO guideline)

Jekyll site for `lagerland-apps.github.io`. GitHub Pages builds from `main` on every push (no local Gemfile — GH Pages builds remotely). Plugins: `jekyll-sitemap`, `jekyll-redirect-from`.

This file is **excluded from the build** (`exclude:` in `_config.yml`) so it is never served. Keep it that way if you rename it.

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

### App page — `_apps/<slug>.md` (+ its sub-pages)
`layout: app` auto-applied. Auto-listed wherever `site.apps` is looped (home, `/apps/`) — no manual index edit. Schema auto-emitted by `_layouts/app.html`: **SoftwareApplication** (+ `Offer`/`AggregateOffer` from price fields; `aggregateRating` only when `ratings.count ≥ 25`), **FAQPage**, **BreadcrumbList**, **HowTo** (from `how_it_works.steps`), optional `creative_work`, and a `Person`/`Organization` founder node.

Required: `slug`, `name`, `tagline`, `quick_answer`, `seo:{…}`, `category` (maps to schema `applicationCategory` — see the `case` block in `app.html`), `platforms`, `status`, `app_store_url`, `price:{model,value}`, `schema_price` / `schema_high_price` / `schema_offer_count`, `hero:{…}`, `privacy:{…}`, `support:{email,url}`, `release:{first_release,last_updated}`.
Recommended: `who_for`/`who_not_for`, `founder`, `value_points`, `features`, `how_it_works` (HowTo schema — high-value E-E-A-T), `comparison_table`, `faq`, `screenshots`, `related_journal`, `alternatives_to`, `roadmap`, `show_body: true` + `about_heading`.

**You must also create two physical sub-pages** (they are NOT auto-generated):
- `apps/<slug>/privacy/index.html` — `layout: privacy`; fields: `app_name`, `overview`, `data_collection`, `data_storage`, `third_parties`, `sensitive_data?`, `children`, `changes`, `contact_email`, `back_url`. **Add a `seo:` block here** (privacy pages currently leak the tagline).
- `apps/<slug>/support/index.html` — `layout: support`; needs `slug` (it looks the app up via `site.apps`). It has no `page.title`, so **without `seo.title` it leaks BOTH title and description** — add `seo:{title,description}`.

### Alternatives page — `alternatives/<slug>.html`
`layout: default`, `permalink: /alternatives/<slug>/`, `title: "<Competitor> Alternative"`, `quick_answer`, full `seo:` block. Then the **4 integration points** (see the established alternatives pattern): the page itself, the `alt_pairs` map, the target app's `alternatives_to:`, and the index `ItemList` + card. (96/96 already follow this — copy an existing one.)

### Landing pages — `for/<slug>.html`, `guides/<slug>.html`
`layout: default`, explicit `permalink`, `title`, `quick_answer`, full `seo:` block.

---

## Generated artifacts — auto-regenerate on build, usually no manual edit
- `sitemap.xml` — `jekyll-sitemap`; includes every page without `sitemap: false`.
- `llms.txt`, `llms-full.txt`, `ai-index.json`, `ai-sitemap.xml` — Jekyll templates (`layout: none` + `permalink`) that loop over collections; they rebuild automatically. **If you add a NEW collection or section, confirm these templates iterate it.**
- `feed.xml` — Atom feed of the journal.

## URL / ranking safety
- **Never change the slug/permalink of a page that already ranks** — it discards its ranking history. To improve a page, change `title`/`seo`/body but keep the URL and bump `last_updated`.

## Before committing a new/edited page
1. Front-matter YAML parses; `seo.title ≤ 60`, `seo.description ≤ 155`.
2. Internal links resolve (the cluster links in/out).
3. Commit to `main` → confirm the Pages build status is `built` (not `errored`).
4. `curl` the live URL and grep `<title>` + `<meta name="description">` to confirm the new tags are served.

## Deploy notes
- An automated "Sync App Store ratings" job pushes to `main` periodically — if a push is rejected, `git fetch` + `git rebase origin/main` (it only touches `_apps/*.md` rating fields, so it won't conflict with content edits) and push again.
