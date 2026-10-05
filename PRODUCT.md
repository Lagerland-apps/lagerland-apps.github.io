# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
The primary visitor is an app shopper arriving from Google or an AI answer (ChatGPT, Perplexity, AI Overviews), usually on a phone or desktop, looking for a specific app, a category tool, or an "alternative to X". Their job is to decide quickly whether an app is right and, on desktop, to get it onto their iPhone. Secondary audiences, not confirmed as separate priorities: privacy-minded Apple users browsing the whole catalogue, journal readers, and press.

## Product Purpose
lagerland-apps.github.io is the home of Lagerland Apps, an independent Apple developer's catalogue of iPhone, iPad, Apple Watch and Mac apps (productivity, health, finance, developer tools). The site presents each app, its comparisons with alternatives, guides, a journal, and a transparency record. Success is a visitor reaching the App Store listing for the right app, and the site being cited correctly by search engines and AI assistants.

## Positioning
Two claims a competing studio could not truthfully copy, both confirmed: (1) one independent developer whose apps are private by design, with no tracking, no ads and no accounts, backed by a published transparency record; (2) a small, calm, curated family of focused apps that share one approach, with honest head-to-head comparisons against alternatives.

## Operating Context
Jekyll site built remotely by GitHub Pages from `main` (plugins: jekyll-sitemap, jekyll-redirect-from). Content types: app pages (with privacy and support sub-pages), alternatives comparison pages, audience landing pages (`for/`), guides, journal posts, transparency page. Machine-readable surfaces (llms.txt, llms-full.txt, ai-index.json, ai-sitemap.xml, feed.xml) are generated from Jekyll templates. Design contracts live in `CLAUDE.md` (page-creation and SEO guideline, plus the v3 "Paper & Ink" design system notes).

## Capabilities and Constraints
- Every content page needs a full `seo:` block (title, description, keywords) and, where applicable, `quick_answer`; app pages emit SoftwareApplication, FAQPage, BreadcrumbList and HowTo schema from their layout.
- Existing permalinks must never change; ranking pages keep their URL.
- App Store conversion elements must be preserved: App Store badge include, Smart App Banner meta, desktop QR install, sticky download bar, price pills.
- App and comparison counts are computed from collections, never hard-coded.
- Generated assets (OG cards, QR codes) come from the scripts in `scripts/`.
- Undecided: whether light and dark themes, the no-JS content guarantee, and the current fonts are binding. They were not marked as must-keep in the interview; the v3 motion contract in CLAUDE.md remains the incumbent rule until the user says otherwise.

## Brand Commitments
Name: Lagerland Apps. Voice and positioning: calm, privacy-first, independent. No tracking, no ads, no accounts. Further identity constraints were not stated as binding.

## Evidence on Hand
Real content in the repo: app pages in `_apps/`, `_data/testimonials.yml`, `_data/transparency.yml`, `_data/app_enrichment.yml`, comparison pages in `alternatives/`, guides, and journal posts in `_journal/`. App Store ratings are synced by an automated job; `aggregateRating` is only emitted at 25 or more ratings. Do not fabricate testimonials, ratings, or user counts beyond these files.

## Product Principles
1. Findability first: a visitor and a crawler should both land on the answer immediately.
2. Privacy is shown, not claimed: back every privacy statement with the transparency record.
3. Honest comparison: alternatives pages state real trade-offs.
4. The route to the App Store is always short and obvious.
5. Calm over clever: one independent developer's voice, no growth-hack patterns.

## Accessibility & Inclusion
No product-specific standard was stated. Respect the existing prefers-color-scheme and reduced-motion behaviour unless a redesign decision changes them.
