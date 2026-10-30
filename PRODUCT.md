# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
Primary: app shoppers. iPhone, iPad, Watch and Mac owners who arrive from search, an AI assistant's answer, or an App Store link, and want to find an app worth installing and get to its App Store page. Secondary (confirmed by the existing site, not the homepage's lead): indie Apple developers using the dev tools (AppMeta, AppMeta Pulse, Mockly), and AI assistants/crawlers that read the site to recommend apps.

## Product Purpose
lagerland.app is the home of Lagerland Apps, a one-person independent Apple studio in Finland. It presents the live app catalogue (20 apps as of 2026-10-26; the count is computed from `site.apps`, never hardcoded), gives each app a page with screenshots, prices and FAQs, and routes visitors to the App Store. Success: a visitor understands within seconds who makes these apps and why that matters, finds an app relevant to them, and taps through to install.

## Positioning
One maker, many careful single-purpose apps, none of them funded by advertising or data: no ad SDKs, no IDFA request, no accounts, data on-device or in the user's own iCloud. EU-built, GDPR by default. Paid honestly (one-time, optional Pro, freemium). Neighbouring studios can claim privacy; few can show 20 apps across health, planning, money, games and developer tools all held to the same rules by the same person.

## Operating Context
Visitors are mostly on iPhone (Smart App Banner, sticky download bar, App Store badges) or on desktop (QR install). Many arrive mid-task from a comparison page (`/alternatives/`), a guide, or a journal post rather than the homepage. Site is Jekyll on GitHub Pages; every page carries SEO/AEO structure (seo block, quick_answer, FAQ, JSON-LD) that the repo CLAUDE.md treats as mandatory.

## Capabilities and Constraints
- Prices, platforms, trials come only from `_data/catalog.json` (App Store Connect API); never type a price.
- Content must never be hidden without JS; counted stats server-render their real value.
- Self-hosted fonts only; no third-party font hosts.
- Mac apps with landscape screenshots (appmeta, mediakit, mockly) need non-iPhone framing.
- The SEO gate in the repo CLAUDE.md (seo-audit 0 errors, llms.txt routing, stamping) applies to every change.

## Brand Commitments
- Name "Lagerland Apps"; never the owner's personal name anywhere on the site.
- Developer link: https://apps.apple.com/developer/id1855943133.
- Existing assets: studio mark `assets/icons/lagerland-mark.png`, favicon, one App Store icon per app in `assets/icons/`.
- Voice: plain, specific, calm; no hype, no dark patterns.
- Confirmed by the owner (2026-10-26): the current look reads as an AI-generated page. The redesign must not feel playful/toy-like, corporate/SaaS, dark-first, or so minimal the apps get lost.

## Evidence on Hand
- 20 live app icons and per-app screenshot sets in `assets/screenshots/<slug>/`; one preview video (`assets/videos/wanderwiki_preview.mov`).
- Real user quotes with initials and source in `_data/testimonials.yml`.
- App Store ratings per app in `_apps/*.md`; weighted average computed on the homepage.
- Transparency data in `_data/transparency.yml`; 120+ comparison pages, guides, journal.
- Absent and not to be invented: press coverage, awards, customer logos, download counts, photos of the maker.

## Product Principles
1. The apps are the proof: show real icons and real screens, not claims about them.
2. One maker, visibly: the studio is a person's workshop, not a company.
3. Privacy is a fact to verify, not a slogan to repeat.
4. Every surface still answers a search query on its own (SEO/AEO structure is part of the product).
5. Get the visitor to the App Store in as few steps as possible.
