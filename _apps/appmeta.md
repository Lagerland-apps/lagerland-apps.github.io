---
layout: app
slug: appmeta
name: "AppMeta"
tagline: "App Store Connect, native on your Mac."
quick_answer: "AppMeta is a native macOS client for App Store Connect. It edits app metadata across all 50 ASC locales side-by-side, shows each changed field next to the live App Store Connect value before it pushes, checks your keywords on-device and, if you turn it on, estimates live keyword difficulty and demand from the App Store. AI translation and keyword suggestions run through your own provider (Anthropic, OpenAI, Google, any OpenAI-compatible endpoint, or Apple Intelligence on-device). It also edits In-App Purchases, subscriptions and Game Center, manages TestFlight builds and reviews, and submits versions for review. macOS 14+ Sonoma. App Store Connect API v1 with a team key (.p8) stored in macOS Keychain — no app-specific passwords, no browser session. The free download runs in demo mode; connecting your account takes Pro at {P_YEARLY}/year or {P_LIFETIME} lifetime."
category: developer-tools
status: live

app_store_url: "https://apps.apple.com/app/id6758547802"

price:
  model: freemium
price_override: "{P_YEARLY}/year or {P_LIFETIME} lifetime"
free_tier: false

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. The free download runs in demo mode with sample data; connecting your own App Store Connect account needs Pro. Refunds are handled by Apple via the standard App Store refund flow. The lifetime tier is a one-time purchase — no auto-renew."

plans:
  - name: "Annual"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "Full AppMeta, billed once a year. Cancel anytime."
    features:
      - "All 50 App Store Connect locales, side-by-side editing"
      - "Live value next to your edit before any push"
      - "On-device keyword diagnosis (no AI required)"
      - "Live keyword difficulty and demand (opt-in)"
      - "Five AI options — your own key, a local model, or Apple Intelligence on-device"
      - "TestFlight, reviews, IAPs, Subscription Groups, Game Center"
      - "Sales analytics + performance diagnostics"
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All AppMeta features. About 20 months of annual — then yours."
    features:
      - "Everything in Annual"
      - "One-time purchase, no renewal"
      - "Future AppMeta features included"
      - "Restores on every Mac signed in with the same Apple ID"
    highlight: true
    highlight_label: "Best value"

icon: "/assets/icons/appmeta.png"
og_image: "/assets/og/appmeta.png"

seo:
  title: "AppMeta — App Store Connect for Mac with IAPs + Game Center"
  description: "Native Mac client for App Store Connect. 50 locales, IAP + Game Center + reviews + TestFlight in one app. BYO-AI keywords. {P_YEARLY}/yr or {P_LIFETIME} lifetime."
  keywords:
    - app store connect Mac app
    - app store connect native Mac client
    - App Store Connect metadata editor
    - Itsyconnect alternative
    - Fastlane deliver alternative
    - NativeConnect alternative
    - ASO tool macOS
    - In-App Purchase editor Mac
    - Game Center metadata editor
    - Subscription Group editor Mac
    - app store keyword analyzer Mac
    - app store localization tool 50 locales
    - TestFlight manager Mac
    - app review management Mac
    - app screenshot upload Mac
    - indie iOS developer tools Mac
    - app submission tool macOS
    - Apple Intelligence ASO
    - on-device AI keyword analysis

hero:
  device: mac
  headline: "App Store Connect. Finally native."
  secondary: "The native Mac client that handles all 50 locales, In-App Purchases, Subscription Groups, and Game Center — same tool Lagerland ships {APP_COUNT} apps with."
  subheadline: "AppMeta edits metadata across all 50 ASC locales side-by-side, manages In-App Purchases and Subscription Groups, edits Game Center Achievements and Leaderboards, shows the live App Store Connect value next to every change before a push, and checks your keywords on-device, with optional live difficulty and demand readings from the App Store. AI translation and keyword ideas run through your own provider — including Apple Intelligence on-device for the times you don't want a single character leaving the Mac. Five AI options (Anthropic, OpenAI, Google, Ollama / LM Studio, Apple Intelligence). {P_YEARLY}/year or {P_LIFETIME} lifetime."
  cta_label: "Download Free"
  alt: "AppMeta on macOS — the What's New field for every locale in one view, with the app's versions as tabs"

who_for:
  - "You ship iOS or macOS apps and the App Store Connect web UI is the slowest tool in your release flow"
  - "You manage metadata across 10+ locales and refuse to scroll through 50 separate tabs to update one field"
  - "You've been burned by a silent overwrite on ASC web and want to see the live value next to your change before anything pushes"
  - "You want keyboard shortcuts and the speed of a native Mac app, not a re-skinned browser"
  - "You'd rather pay {P_LIFETIME} once than rent ASC tooling for $10–$70/month indefinitely"
  - "You want your ASC credentials in macOS Keychain, not a browser session that times out daily"

who_not_for:
  - "You ship one app a year and the ASC web UI is good enough for the few times you touch it"
  - "Your release pipeline is fully automated through Fastlane / CI and you never edit metadata by hand"
  - "You need keyword rank tracking over time and competitor keyword research — that's Appfigures / AppTweak / Sensor Tower territory, not AppMeta's"
  - "You need team seats, or a tool that runs in a browser or on Windows — AppMetaHub (web) or ASO.dev (seats, more platforms) fit that better"

related_journal:
  slug: "app-store-keyword-field-100-characters"
  anchor: "How the App Store keyword field works — 100 characters, commas, and the words Apple already indexes"
alternatives_to:
  - "Itsyconnect"
  - "App Store Connect web UI"
  - "Fastlane deliver"
  - "AppMetaHub"
  - "ASO.dev"
  - "Helm for App Store Connect"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Why we built this"
  heading: "We ship {APP_COUNT} apps. AppMeta is the tool we built for ourselves."
  story: "AppMeta exists because every other workflow for managing App Store metadata broke for us at scale. The web UI is fine when you ship one app — it's torture when you ship 20. Fastlane deliver is great in CI but unworkable for interactive editing across 50 locales. NativeConnect, once the closest native client, was pulled from the Mac App Store back in 2020. So we built the tool we needed: a native Mac app that opens fast, edits all 50 ASC locales side-by-side, shows the live value next to every change before anything pushes, and runs AI translation and keyword ideas through whichever provider we trust that week — including Apple Intelligence on-device for the times we don't want a single character leaving the Mac. Every Lagerland release on the App Store ships through AppMeta. It's the tool we use every day."
  signals:
    - "Same tool Lagerland uses to ship every release of all {APP_COUNT} apps in the catalogue"
    - "Built on the App Store Connect API v1 with JWT auth and .p8 keys stored in macOS Keychain — no app-specific passwords, no browser session"
    - "SwiftUI + SwiftData, macOS 14+ Sonoma minimum, no analytics SDKs, no backend servers"
    - "Five AI options out of the box — Anthropic, OpenAI, Google, OpenAI-compatible (Ollama / LM Studio), Apple Intelligence on-device"
  external_link:
    label: "See the 20 Lagerland apps shipped with AppMeta →"
    href: "/apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally — usually within a day."

value_points:
  - title: "All 50 ASC locales, side-by-side"
    description: "AppMeta loads the canonical App Store Connect locale set — all 50, including the 11 locales Apple added in 2026 (Bangla, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu, Slovenian and Urdu). Edit one locale's fields together, or one field across every locale at once. Never tab-switch through 50 browser pages again."
  - title: "See every change before it pushes"
    description: "Every changed field shows the live App Store Connect value next to your edit, in every locale. Push per-field, per-locale, or everything in one shot. Fields that changed on App Store Connect since your last fetch are flagged, and Discard All Local Changes brings the live listing back in one step — no silent overwrites."
  - title: "Five AI options. Your key, your spend."
    description: "Keyword diagnosis runs locally — words already in your name or subtitle, words repeated across phrases, wasted characters, and the same phrases repeated across locales. Translation and keyword suggestions use whichever provider you trust: Anthropic Claude, OpenAI GPT or Google Gemini with your own key, any OpenAI-compatible endpoint (Ollama, LM Studio, local proxies), or Apple Intelligence on-device (requires macOS 26 — zero API key, zero network)."
  - title: "Pay annually, or pay once and ship forever"
    description: "{P_YEARLY}/year or {P_LIFETIME} lifetime. Compare: AppMetaHub Indie was $120/year in May 2026; ASO.dev Indie is $348/year per seat, billed yearly. AppMeta's lifetime tier costs about what one month of ASO.dev Indie does — and doesn't disappear when you stop paying."

how_it_works:
  intro: "AppMeta is a native macOS client for the App Store Connect API v1. JWT auth with a .p8 key, edits stored locally in SwiftData, changes compared against your last fetched snapshot. Here's how a metadata change moves through it."
  steps:
    - title: "Connect with your App Store Connect API key (.p8)"
      detail: "AppMeta uses the modern App Store Connect API v1, not an app-specific password and not a scraped browser session. Generate a team key in App Store Connect's Users and Access, then enter the Issuer ID, Key ID, and the .p8 file into AppMeta once. Individual keys won't work, because they have no Issuer ID. AppMeta checks the key against your app list before saving it. All three values go into macOS Keychain on that Mac only, and the private key never leaves it: AppMeta signs short-lived tokens with it, and those go only to api.appstoreconnect.apple.com — never to a Lagerland server."
    - title: "Fetch metadata for all your locales"
      detail: "AppMeta pulls the current state of your app's metadata in every locale it has, and can add any of the 50 ASC locales — including the 11 added in 2026 (Bangla, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu, Slovenian and Urdu). It stores the working copy locally in SwiftData, so your edits survive a relaunch and only go to App Store Connect when you push."
    - title: "Edit side-by-side, with shortcuts"
      detail: "Every editable ASC field — name (30 chars), subtitle (30 chars), promotional text (170 chars), keywords (100 chars), description (4000 chars), what's new (4000 chars), support, marketing and privacy policy URLs — with live character counts that count the way App Store Connect does. Work locale by locale, or pick one field and edit it in every locale at once, copying from the previous version where it helps. Keyboard shortcuts move between locales, open the change preview and push. Never wait on a browser page-load again."
    - title: "Run keyword diagnosis (no AI required)"
      detail: "AppMeta's Keyword Optimizer runs entirely on-device against the metadata you've already entered: it flags keyword words that already appear in your name or subtitle (wasted ranking surface), words repeated across keyword phrases, duplicate phrases, fields over the limit, and the same phrase repeated across locales that share a language or storefront. It matches exact words, so plurals and other word forms are still yours to catch. A storefront view shows which of 57 storefronts your localizations cover directly, by fallback, or not at all. No network call, no API key, no AI."
    - title: "Check live difficulty and demand (optional)"
      detail: "Turn on live keyword research and AppMeta asks the App Store itself. Difficulty is a 0–100 score built from the ten apps that rank for a phrase — their ratings and how closely their names and subtitles target it — and you can open the evidence behind every score. Demand comes from Apple's search suggestions, or from Apple's own popularity figures if you connect your Apple Ads account. The two combine into an opportunity reading, and a sweep can check every combination your name, subtitle and keyword field can spell out. It's off until you switch it on."
    - title: "Generate suggestions with your AI provider (optional)"
      detail: "When you want AI-generated keyword candidates or translated metadata, pick a provider: Anthropic Claude, OpenAI GPT or Google Gemini (your API key), any OpenAI-compatible endpoint (Ollama, LM Studio, local proxies — no key required), or Apple Intelligence on-device (zero API key, zero network — requires macOS 26 and Apple Intelligence enabled). You pay your provider directly; AppMeta meters nothing."
    - title: "Preview the changes, push what you want"
      detail: "Before anything touches App Store Connect, AppMeta lists every changed field with the last fetched App Store Connect value next to your edit. Push per-field, per-locale, or everything in one operation. Push only fr-FR's subtitle. Push every locale's keywords but nothing else. Refresh first, and any field that changed on App Store Connect since your last fetch is flagged, or shows its new live value next to your edit, rather than being overwritten unseen. The granularity is yours."
    - title: "Submit, manage reviews, run TestFlight — same app"
      detail: "App Review Information, base price and territory availability, categories, age ratings, phased release, attaching a build and submitting the version for review — handled in AppMeta. App Privacy details are the exception: AppMeta checks that a privacy policy URL is set and opens App Store Connect for the data declarations. Read and reply to App Store reviews from every storefront in one list. In TestFlight, edit What to Test and the beta description, add builds to groups, set export compliance and expire builds. In-App Purchases, Subscription Groups, Game Center (Achievements, Leaderboards, Leaderboard Sets) editable with the same locale-aware UI. The release surface, native on macOS 14+."

features:
  - title: "All 50 App Store Connect locales — including the 11 added in 2026"
    description: "AppMeta ships with the canonical App Store Connect locale set: 50 locales as of 2026, including Bangla, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu, Slovenian, and Urdu — the 11 locales Apple added in 2026. Edit locale by locale, or one field across every locale side by side. Live character counts on every field, measured the way App Store Connect measures them."
  - title: "The live value next to your edit, before every push"
    description: "Every changed field shows the last fetched App Store Connect value beside your edit before it touches App Store Connect. Push per-field, per-locale, or everything in one operation. Refresh before you push and fields that changed on the server since your last fetch are flagged, so a teammate's edit or an automated pipeline's change shows up instead of being overwritten unseen — the failure mode that plagues the web UI."
  - title: "Five AI options — your key, your spend, your choice"
    description: "Generate keyword suggestions and translate your listing through whichever model you trust: <a href=\"https://www.anthropic.com/claude\" rel=\"noopener\" target=\"_blank\">Anthropic Claude</a>, <a href=\"https://platform.openai.com/\" rel=\"noopener\" target=\"_blank\">OpenAI GPT</a> or <a href=\"https://ai.google.dev/\" rel=\"noopener\" target=\"_blank\">Google Gemini</a> with your own key, any OpenAI-compatible endpoint (<a href=\"https://ollama.com/\" rel=\"noopener\" target=\"_blank\">Ollama</a>, LM Studio, local proxies — no key required), or <a href=\"https://www.apple.com/apple-intelligence/\" rel=\"noopener\" target=\"_blank\">Apple Intelligence</a> on-device (macOS 26 required, zero API key, zero network call). You pay your provider directly. AppMeta meters nothing."
  - title: "On-device keyword diagnosis — no AI required"
    description: "AppMeta's Keyword Optimizer runs entirely locally against the metadata you've already entered. It flags keyword words already in your name or subtitle, words repeated across phrases, duplicate phrases, fields over the limit, and phrases repeated across locales that share a language or storefront. Search coverage counts the one-, two- and three-word combinations your name, subtitle and keywords can form, and a storefront view maps which of 57 storefronts your localizations cover. Matching is exact-word, so plurals aren't merged. Useful even with zero AI configured."
  - title: "Live keyword difficulty, demand and competitor pricing (opt-in)"
    description: "Switch on live research and AppMeta reads the App Store directly: a 0–100 difficulty score from the ten apps that rank for each phrase, with every app and number behind it on show; demand from Apple's search suggestions, or Apple's popularity figures if you connect your own Apple Ads account; and an opportunity reading that combines the two. Add competitor apps to compare the in-app purchase prices the App Store lists for them with yours, territory by territory. Live research stays off until you turn it on, competitor checks run only for apps you add, and a blank is shown as unknown, never as zero."
  - title: "App Store Connect API v1 with .p8 / JWT — credentials in macOS Keychain"
    description: "AppMeta uses Apple's modern App Store Connect API v1 with JWT authentication and a team .p8 key (individual keys aren't supported, because they have no Issuer ID). No app-specific password, no scraped browser session. The Issuer ID, Key ID and private key are stored in macOS Keychain as this-Mac-only items — never in a plaintext file. Tokens signed with the key go only to api.appstoreconnect.apple.com. AppMeta's other requests go to Apple's public App Store endpoints, Apple Ads (if you connect it), the European Central Bank's exchange-rate API for sales charts, and your chosen AI provider — never to a Lagerland server."
  - title: "Submissions, reviews, TestFlight, IAPs, Game Center — one app"
    description: "App Review Information, base price and availability, categories, age ratings, phased release and submission for review. Read and reply to App Store reviews from every storefront, filtered by rating. TestFlight: What to Test, beta description, adding builds to groups, export compliance and expiry. Create and edit In-App Purchases, subscriptions and Subscription Groups — localizations, prices, availability and introductory offers. Edit Game Center Achievements, Leaderboards, and Leaderboard Sets with locale-aware UI. App Privacy details stay in App Store Connect."
  - title: "Sales analytics and diagnostics built in"
    description: "The Sales and Analytics view pulls proceeds, units and subscription reports through the ASC API, plus the App Store funnel from Apple's analytics reports, converted to one currency with ECB exchange rates. Diagnostics shows Apple's performance metrics (launch time, memory, hangs, disk writes, battery, terminations) and, per build, hang and disk-write signatures with their call stacks — the data Xcode Organizer surfaces, in a faster, browse-able UI."
  - title: "Screenshot upload for Apple's device classes — including IAP review screenshots"
    description: "Drag-and-drop screenshot upload for iPhone, iPad, Mac, Apple Watch and Apple TV display sizes. Also handles the hyper-specific case competitors usually miss: the review screenshot Apple requires for each In-App Purchase and subscription, which the ASC web UI buries three menus deep. Apple Vision Pro screenshots and App Preview videos aren't supported yet."

screenshots:
  - src: "/assets/screenshots/appmeta/1.png"
    alt: "AppMeta on macOS — the What's New field for every locale in one view, with the app's versions as tabs"
  - src: "/assets/screenshots/appmeta/2.png"
    alt: "AppMeta — In-App Purchase editor with base-territory price, territory availability, review screenshot and reference name"
  - src: "/assets/screenshots/appmeta/3.png"
    alt: "AppMeta — TestFlight build detail with expiry, export compliance, What to Test and group distribution"
  - src: "/assets/screenshots/appmeta/4.png"
    alt: "AppMeta — locale list with sync status next to the App Info and version metadata fields for one locale"

comparison_table:
  intro: "Each row below is a question an indie iOS developer actually asks before paying for an ASC tool. Itsyconnect is the closest direct competitor — a free, MIT-licensed Mac client built on Electron, with BYO-AI and an MCP server. AppMetaHub (web) and ASO.dev (apps for Mac, iPhone, Windows and more) are subscription competitors. Fastlane deliver is the free CLI baseline."
  competitors: ["AppMeta", "Itsyconnect", "AppMetaHub", "ASO.dev", "Fastlane deliver"]
  rows:
    - feature: "Native Mac app (not a browser / not a CLI)"
      values: ["Yes — SwiftUI + SwiftData, macOS 14+", "Desktop app built on Electron (Next.js / React)", "No — web only", "Yes — plus iPhone, iPad, Windows, Linux and Android apps", "No — CLI only"]
    - feature: "Pricing model"
      values: ["{P_YEARLY}/yr or {P_LIFETIME} lifetime", "Free, no limits (MIT open source)", "$10/mo Indie · $23/mo Pro", "Per seat: $29/mo Indie · $69/mo Pro, billed yearly", "Free (open source)"]
    - feature: "3-year total cost (Indie tier)"
      values: ["{P_LIFETIME} lifetime (or $53.97 annual)", "$0", "≈ $360 (12 × $10 × 3)", "≈ $1,044 (3 × $348, billed yearly)", "$0"]
    - feature: "Number of App Store Connect locales supported"
      values: ["50 — canonical 2026 set, including the 11 added in 2026", "All locales at once (count not published)", "37", "50", "Per-locale .txt files"]
    - feature: "Manages In-App Purchases + Subscription Groups + Game Center"
      values: ["Yes — all three, locale-aware UI", "No — not in its README or source", "No — metadata + screenshots focus", "IAPs and subscriptions yes; Game Center not listed", "No"]
    - feature: "Screenshot upload (drag-and-drop, IAP review screenshots)"
      values: ["Yes — iPhone, iPad, Mac, Watch, TV, plus IAP / subscription review screenshots (no App Previews)", "Yes", "Yes — drag-and-drop", "Yes", "Yes — from screenshot folders, plus App Previews"]
    - feature: "Review changes before push"
      values: ["Live value next to your edit — push by field, locale or all", "Opt-in diff mode; push all at once", "Yes — word-level", "Yes — change highlighting", "HTML preview of local files; no comparison with live"]
    - feature: "AI (bring your own key)"
      values: ["5 options — Anthropic, OpenAI, Google, OpenAI-compatible (Ollama / LM Studio), Apple Intelligence on-device", "6 providers — Anthropic, OpenAI, Google, xAI, Mistral, DeepSeek", "Yes — Pro plan only", "Translation: Google Translate, or DeepL / ChatGPT / Claude with your keys", "No"]
    - feature: "Apple Intelligence on-device support (no API key, no network)"
      values: ["Yes — macOS 26 required", "No — six cloud providers", "No", "No", "No"]
    - feature: "Diagnostics + sales analytics in-app"
      values: ["Yes — sales, subscriptions, App Store funnel, performance metrics, hang and disk-write call stacks", "Yes — crash tracking, analytics", "No", "Yes — analytics & A/B testing", "No"]
    - feature: "MCP server (Claude Code / Cursor / Codex integration)"
      values: ["No", "Yes — Claude Code, Cursor, Codex, OpenCode", "Yes", "Yes — local", "No"]
    - feature: "Open source"
      values: ["No — proprietary, funded by paid software", "Yes — MIT, plus a self-hosted Docker option", "No", "No", "Yes — MIT licensed"]
    - feature: "Where your App Store Connect key is stored"
      values: ["Mac Keychain, this Mac only", "AES-256-GCM, master key in the Keychain", "Stored server-side", "On device; optional encrypted sync for teams", "Local .p8 file or Apple ID session"]
  footnote: "Itsyconnect, ASO.dev and fastlane details were checked on 2026-10-25: Itsyconnect against its GitHub README and v1.14.2 release, ASO.dev against its pricing page (per seat, excluding VAT), fastlane against docs.fastlane.tools. AppMetaHub figures come from its landing page as of 2026-05-13 and weren't rechecked; Indie was then $10/mo billed annually ($120/year). Verify current pricing before switching."

plateau_disclosure:
  title: "What AppMeta won't do for you"
  rule: "AppMeta is a native Mac client for the App Store Connect API v1 — an editing and submission surface that runs locally on macOS 14+. It's deliberately not a competitive-intelligence platform or a CI replacement. The trade-off is what keeps it one-time-priced and entirely on your Mac."
  what_it_does_not_do: "AppMeta will not track keyword rankings over time or research competitors' keywords — that's Appfigures, AppTweak, Sensor Tower, or RespectASO territory; its live research estimates difficulty and demand for the phrases you check. It will not run inside your CI pipeline as a CLI — Fastlane deliver still belongs in CI, and AppMeta is for interactive editing on the desktop. It will not upload builds or give you Apple Search Ads campaign management. It will not run on iOS or iPad (it's a macOS app, by design). AI keyword suggestions are only as good as the provider you point it at — bring an API key (Claude / GPT / Gemini) or use Ollama or Apple Intelligence on-device."
  notes:
    - "Want to drive AppMeta from Claude Code, Cursor, Codex, or OpenCode via MCP? AppMeta has no MCP server. Itsyconnect ships one today if your workflow depends on it."
    - "Want rank tracking over time? Pair AppMeta with Appfigures or AppTweak — different jobs, complementary tools."
    - "Want to run metadata pushes in CI? Keep Fastlane deliver in your release pipeline; AppMeta handles the interactive desktop editing flow."
    - "Want to edit from your iPhone or iPad? AppMeta is macOS only — ASO.dev's iPhone and iPad apps are the closest alternative for editing away from the Mac."
    - "Want Apple Search Ads campaign management? That's a different product surface. AppMeta only reads keyword popularity from Apple Ads, and only if you connect your account."
    - "Want to change promotional text on a live version? AppMeta locks version fields once a version is live, promotional text included, so for now make that edit in App Store Connect."
    - "Want to fill in App Privacy details (the privacy 'nutrition label')? That stays in App Store Connect; AppMeta links you there from its submission checklist."
    - "Want open source code you can audit and self-host? AppMeta is proprietary — funded by paid software, not advertising or telemetry. Itsyconnect is the open-source option in this category."

training_vocabulary:
  overline: "Speaks ASC's language"
  heading: "The fields, locales, and APIs AppMeta touches."
  intro: "AppMeta uses Apple's official App Store Connect API v1 with JWT authentication. Below is the canonical surface — the ASC fields with their character limits, the 50 locales supported, the auth model, and the endpoints AppMeta talks to."
  groups:
    - heading: "App Store fields (with limits)"
      items:
        - "App name (30 characters)"
        - "Subtitle (30 characters)"
        - "Promotional text (170 characters)"
        - "Keywords (100 characters, comma-separated)"
        - "Description (4000 characters)"
        - "What's New (4000 characters)"
        - "Support URL, Marketing URL, Privacy Policy URL"
    - heading: "Beyond metadata"
      items:
        - "App Review Information (contact, demo account, notes)"
        - "Pricing (base price; Apple equalizes the rest) and availability per territory"
        - "Age ratings, categories, phased release (App Privacy details stay in App Store Connect)"
        - "TestFlight builds, What to Test, beta description, build groups"
        - "In-App Purchases & Subscription Groups (locale-aware)"
        - "Game Center: Achievements, Leaderboards, Leaderboard Sets"
        - "App Store reviews — read and reply"
        - "Sales Analytics + Diagnostics (performance metrics, hang and disk-write signatures)"
    - heading: "50 ASC locales (2026)"
      items:
        - "ar-SA · bn · ca · cs · da · de-DE · el · en-AU · en-CA · en-GB · en-US"
        - "es-ES · es-MX · fi · fr-CA · fr-FR · gu · he · hi · hr · hu · id · it"
        - "ja · kn · ko · ml · mr · ms · nl-NL · no · or · pa · pl"
        - "pt-BR · pt-PT · ro · ru · sk · sl · sv · ta · te · th"
        - "tr · uk · ur · vi · zh-Hans · zh-Hant — including the 11 locales Apple added in 2026"
    - heading: "Auth & API"
      items:
        - "App Store Connect API v1 (api.appstoreconnect.apple.com)"
        - "JWT authentication with a team .p8 private key (individual keys have no Issuer ID)"
        - "Issuer ID + Key ID stored in macOS Keychain"
        - ".p8 private key stored in macOS Keychain — never in a plaintext file"
        - "No app-specific password, no browser session"
        - "Optional: App Store search and lookup, Apple Ads (popularity), ECB exchange rates"
        - "Five AI options: Anthropic Claude, OpenAI GPT, Google Gemini, OpenAI-compatible (Ollama / LM Studio), Apple Intelligence on-device"

example_insights:
  overline: "What an AppMeta diagnosis looks like"
  heading: "Real ASO outputs, in plain English."
  intro: "AppMeta's Keyword Optimizer runs on-device against your existing metadata before any AI is involved. These are the kinds of plain-English diagnoses it surfaces — none of them require an API key or a network call."
  cards:
    - tag: "Overlap · Wasted chars"
      headline: "Your en-US subtitle eats 14 characters of your keywords field."
      body: "AppMeta detected that 4 keywords in en-US already appear verbatim in your subtitle. Apple already indexes your name and subtitle, so those 14 characters are not earning you any additional ranking. Replace them with 4 new words and recover the surface area."
    - tag: "Cross-locale · Duplicates"
      headline: "en-GB repeats 6 of your en-US keyword phrases."
      body: "AppMeta flags phrases that appear in more than one locale of the same language, or in locales that share a storefront. If those locales are indexed in the same storefront, the repeats may be spending characters twice on one signal. AppMeta shows the overlap and suggests keeping each phrase in the primary locale; you decide."
    - tag: "Repeated words · Cleanup"
      headline: "Your es-ES keywords use 'fotos' in three different phrases."
      body: "A word only needs to appear once in the keyword field, so the second and third 'fotos' buy you nothing. AppMeta flags words repeated across phrases or already in the name and subtitle, and counts the characters they cost. It matches exact words, so 'foto' and 'fotos' count as different words — plurals are still yours to catch."
    - tag: "Storefront coverage"
      headline: "Brazil is covered only by your pt-PT listing."
      body: "AppMeta maps 57 storefronts to the localizations usually associated with them and shows which ones your locales cover directly, which are covered only by fallback, and which aren't covered at all. The mapping is ASO best practice, not an Apple table, and the app labels it that way."

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No backend servers — AppMeta runs entirely on your Mac, and nothing goes to Lagerland"
    - "No third-party analytics SDKs, no tracking domains, no telemetry"
    - "App Store Connect credentials stored in macOS Keychain (issuer ID, key ID, .p8 private key) as this-Mac-only items — never in plaintext, never sent to Lagerland"
    - "Tokens signed with your key go only to <code>api.appstoreconnect.apple.com</code>; analytics report files download from the storage links Apple's API returns"
    - "Other requests go to Apple or to a provider you pick: Apple's public App Store endpoints (<code>apps.apple.com</code>, <code>itunes.apple.com</code>, <code>search.itunes.apple.com</code>, <code>amp-api-edge.apps.apple.com</code>) for app icons, competitor prices and live keyword research, which is off until you turn it on; <code>api.ads.apple.com</code> and <code>appleid.apple.com</code> only if you connect Apple Ads; <code>data-api.ecb.europa.eu</code> for exchange rates in sales charts; and your chosen AI provider, if you configure one"
    - "AI provider API keys, when set, are stored in macOS Keychain via the same path as ASC credentials"
    - "See the per-app <a href=\"/transparency/#appmeta\">Privacy Manifest</a> for the declared API usage and tracking-domain list (it's empty)"

faq:
  - q: "What is AppMeta?"
    a: "AppMeta is a native macOS client for App Store Connect. It edits app metadata across all 50 ASC locales side-by-side, shows the live App Store Connect value next to every change before a push, checks keywords on-device with optional live difficulty and demand readings, runs AI translation and keyword suggestions through whichever provider you trust (Anthropic Claude, OpenAI GPT, Google Gemini, OpenAI-compatible endpoints like Ollama, or Apple Intelligence on-device), and handles the rest of a release — TestFlight, reviews, In-App Purchases, Game Center and submission for review — without a browser. macOS 14+ Sonoma. App Store Connect API v1 with JWT and a team .p8 key in macOS Keychain. {P_YEARLY}/year or {P_LIFETIME} lifetime."
  - q: "Is AppMeta an alternative to App Store Connect?"
    a: "AppMeta works alongside App Store Connect using Apple's official ASC API v1. It provides a faster, safer editing surface than the web UI with features the browser doesn't have — side-by-side editing across all 50 locales, the live value next to your edit before any push, keyword diagnosis without an AI call, and five AI options when you do want generation. Your App Store Connect data goes through Apple's API; nothing is scraped from App Store Connect, and nothing is stored on a Lagerland server. A few things still need the website, such as App Privacy details."
  - q: "How is AppMeta different from Fastlane deliver?"
    a: "Fastlane deliver is a CLI tool built for CI/CD pipelines — strong when you want metadata in version control and automatic uploads on every release. AppMeta is a desktop tool for the interactive editing surface itself — every locale of a field visible at once, the live value next to each change before a push, keyword optimization, review management, In-App Purchase and Game Center editing. They are complementary: many developers keep Fastlane deliver in their release pipeline and use AppMeta for the manual editing flow."
  - q: "How is AppMeta different from Itsyconnect?"
    a: "Itsyconnect is a good App Store Connect client for the Mac, and it's free and MIT-licensed, built on Electron with a self-hosted Docker option. AppMeta is a native SwiftUI app at {P_YEARLY}/year or {P_LIFETIME} lifetime. The honest difference is scope. AppMeta creates and edits In-App Purchases, subscriptions and Subscription Groups, and Game Center (Achievements, Leaderboards, Leaderboard Sets), with locale-aware UI — Itsyconnect doesn't cover any of those. AppMeta can run its AI on-device with Apple Intelligence (zero API key, zero network call, requires macOS 26) or a local model — Itsyconnect offers six cloud providers (Anthropic, OpenAI, Google, xAI, Mistral, DeepSeek). Itsyconnect has an MCP server for Claude Code, Cursor, Codex, and OpenCode and a wider analytics view — AppMeta has no MCP server. The decision: you don't sell IAPs or use Game Center, or you want free, open source or MCP → Itsyconnect. You monetize through in-app purchases, ship Game Center content, or want on-device AI → AppMeta. The full comparison is on the Itsyconnect alternative page."
  - q: "How is AppMeta different from NativeConnect?"
    a: "NativeConnect was a native Mac client for App Store Connect in the same shape as AppMeta. It was pulled from the Mac App Store in 2020 and hasn't been available since, so it isn't a current option. AppMeta is an actively maintained native Mac client in that category — built on SwiftUI + SwiftData, macOS 14+, App Store Connect API v1, with regular updates."
  - q: "How is AppMeta different from AppMetaHub and ASO.dev?"
    a: "AppMetaHub and ASO.dev are subscription tools. AppMetaHub is a web app; its Indie plan was $10/month in May 2026. ASO.dev has apps for Mac, iPhone, iPad, Windows, Linux and Android and is priced per seat — Indie is $29/month billed yearly ($348/year) as of October 2026. AppMeta is a native Mac app at {P_YEARLY}/year or {P_LIFETIME} lifetime. Three years of AppMetaHub Indie is around $360, three years of ASO.dev Indie is around $1,044, three years of AppMeta is {P_LIFETIME} lifetime or $53.97 annual. The structural trade-off: they give you a browser or more platforms, team seats and (for ASO.dev) rank tracking; AppMeta gives you a native Mac app, edits saved locally until you push, Game Center editing and a lifetime option. AppMeta also supports more locales than AppMetaHub did in May 2026 (50 vs 37)."
  - q: "Which AI providers does AppMeta support for keyword generation?"
    a: "Five options, out of the box: Anthropic Claude, OpenAI GPT and Google Gemini with your own API key, any OpenAI-compatible endpoint (Ollama, LM Studio, local proxies — no key required), and Apple Intelligence on-device (requires macOS 26 and Apple Intelligence enabled — zero API key, zero network call). You pay your provider directly; requests go from your Mac straight to the provider, and AppMeta doesn't meter or proxy them. Switching providers is one menu pick."
  - q: "Does AppMeta need an AI API key to work?"
    a: "No. AppMeta's Keyword Optimizer — overlap detection, repeated-word cleanup, cross-locale duplicates, storefront coverage — runs entirely on-device against your existing metadata, with no AI call required. Live difficulty and demand readings come from the App Store and need no AI key either. AI keyword generation is opt-in and requires either a third-party API key (Claude / GPT / Gemini), a local endpoint (Ollama / LM Studio), or macOS 26 with Apple Intelligence."
  - q: "Is AppMeta safe? Where do my App Store Connect credentials go?"
    a: "AppMeta uses Apple's official App Store Connect API v1 — no scraping, no app-specific password, no browser session. You generate a team API key in App Store Connect (Users and Access → Integrations → App Store Connect API) and enter the Issuer ID, Key ID, and .p8 file into AppMeta once; individual keys aren't supported, because they have no Issuer ID. All three are stored in macOS Keychain as items that stay on that Mac — the private key is never written to a plaintext file. Tokens signed with it go only to <code>api.appstoreconnect.apple.com</code>. AppMeta also contacts Apple's public App Store endpoints (app icons, competitor prices and, if you turn it on, live keyword research), Apple Ads if you connect it, the European Central Bank's exchange-rate API for sales charts, and your chosen AI provider. None of these is a Lagerland server. See the per-app Privacy Manifest on the transparency page for the declared API usage."
  - q: "Is AppMeta free?"
    a: "AppMeta is free to download and runs in demo mode: you can walk through every screen with realistic sample data, no Apple Developer account required. Connecting your own App Store Connect account needs Pro — {P_YEARLY}/year, or {P_LIFETIME} lifetime, one-time, no recurring fees. Applies across every Mac you sign in to the App Store with. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Can I submit apps for review through AppMeta?"
    a: "Yes. App Review Information, base price and territory availability, categories, age ratings, phased release, attaching a build and submitting the version for review all happen in AppMeta. App Privacy details are the exception: AppMeta checks that a privacy policy URL is set and opens App Store Connect for the data declarations. Builds themselves are uploaded with Xcode, Transporter or fastlane."
  - q: "How many App Store Connect locales does AppMeta support?"
    a: "All 50 ASC locales as of 2026. AppMeta's canonical locale list includes the 11 locales Apple added in 2026: Bangla (bn), Gujarati (gu), Kannada (kn), Malayalam (ml), Marathi (mr), Odia (or), Punjabi (pa), Tamil (ta), Telugu (te), Slovenian (sl), and Urdu (ur) — alongside the previously-supported 39 locales. AppMeta updates the locale list when Apple does."
  - q: "Does AppMeta manage In-App Purchases, subscriptions, and Game Center?"
    a: "Yes. In-App Purchases, subscriptions and Subscription Groups are editable with locale-aware UI, including prices, availability, introductory offers and review screenshots. Game Center Achievements, Leaderboards, and Leaderboard Sets are editable with the same per-locale workflow. Reviews from every storefront are readable and repliable in one list."
  - q: "Will AppMeta replace Appfigures, AppTweak, or Sensor Tower?"
    a: "No — different tools for different jobs. AppMeta is a metadata editor and submission client for the App Store Connect API. It can estimate difficulty and demand for the keywords you check, but it doesn't track rankings over time or research competitors' keywords. Appfigures, AppTweak, Sensor Tower, and RespectASO are competitive-intelligence platforms — keyword rank tracking, competitor research, market analysis. Most indie developers use one of each: AppMeta for editing, an intelligence platform for research."
  - q: "What macOS version does AppMeta require?"
    a: "macOS 14 (Sonoma) and later. Apple Intelligence on-device support requires macOS 26 and Apple Intelligence enabled. The other four AI options (Anthropic, OpenAI, Google, OpenAI-compatible) work on any supported macOS version."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/appmeta/support/"

release:
  first_release: "2026-02-01"
  last_updated: "2026-10-21"
  last_audited: "2026-10-25"
  audit_round: "4 (copy checked against the 2.7.0 source)"

related_apps:
  - appmeta-pulse
  - mockly
last_updated: 2026-10-26
---
AppMeta is a native macOS client for App Store Connect, built for indie iOS and macOS developers who ship more than one app and want their editing surface on the desktop rather than in a browser tab. It edits app metadata across all 50 ASC locales side-by-side — including the 11 locales Apple added in 2026 (Bangla, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu, Slovenian and Urdu) — with live character counts, the live App Store Connect value next to every change before a push, and per-field, per-locale, or all-at-once sync granularity. Keyword diagnosis runs entirely on-device: keyword/subtitle overlap detection, repeated-word cleanup, cross-locale duplicates, search-coverage counts, and storefront coverage. Live keyword research is opt-in: difficulty from the apps that rank for a phrase, demand from Apple's search suggestions or your own Apple Ads account, and competitor in-app purchase prices. AI keyword generation and translation are opt-in and run through whichever provider you trust — Anthropic Claude, OpenAI GPT, Google Gemini, any OpenAI-compatible endpoint (Ollama, LM Studio, local proxies), or Apple Intelligence on-device (macOS 26, zero API key, zero network call). The release surface is in one app: TestFlight builds and What to Test, review reading and reply, App Review Information, pricing and availability, age ratings, submission for review, In-App Purchases, Subscription Groups, and Game Center editing (Achievements, Leaderboards, Leaderboard Sets) with locale-aware UI. App Privacy details stay in App Store Connect. Built on the App Store Connect API v1 with JWT authentication and a team .p8 private key stored in macOS Keychain — no app-specific password, no scraped browser session. SwiftUI + SwiftData, macOS 14+ Sonoma. No backend servers, no analytics SDKs, no tracking domains. Free demo mode; {P_YEARLY}/year or {P_LIFETIME} lifetime to connect your account. The same tool Lagerland ships every release of all 20 catalogue apps with.
