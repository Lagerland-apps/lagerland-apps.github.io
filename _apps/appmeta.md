---
layout: app
slug: appmeta
name: "AppMeta"
tagline: "App Store Connect, native on your Mac."
quick_answer: "AppMeta is a native macOS client for App Store Connect. It edits app metadata across all 50 ASC locales side-by-side, previews every diff before it pushes, runs AI keyword analysis through your own provider (Anthropic, OpenAI, Google, any OpenAI-compatible endpoint, or Apple Intelligence on-device), manages TestFlight and reviews, and handles full submission flow. macOS 14+ Sonoma. App Store Connect API v1 with JWT and a .p8 key stored in macOS Keychain — no app-specific passwords, no browser session. $17.99/year or $29.99 lifetime."
category: developer-tools
platforms: ["macOS"]
status: live

app_store_url: "https://apps.apple.com/app/id6758547802"

price:
  model: freemium
  value: "$17.99/year or $29.99 lifetime"
schema_price: "17.99"
schema_high_price: "29.99"
schema_offer_count: "2"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. The lifetime tier is a one-time purchase — no auto-renew."

plans:
  - name: "Annual"
    price: "$17.99/yr"
    summary: "Full AppMeta, billed once a year. Cancel anytime."
    features:
      - "All 50 App Store Connect locales, side-by-side editing"
      - "Word-level diff preview before any push"
      - "On-device keyword diagnosis (no AI required)"
      - "Five AI providers — BYO key (incl. Apple Intelligence on-device)"
      - "TestFlight, reviews, IAPs, Subscription Groups, Game Center"
      - "Sales Analytics + crash diagnostics"
  - name: "Lifetime"
    price: "$29.99 once"
    summary: "All AppMeta features. Roughly 16 months of annual — then yours."
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
  description: "Native Mac client for App Store Connect. 50 locales, IAP + Game Center + reviews + TestFlight in one Mac app. BYO-AI keywords. $17.99/yr or $29.99 lifetime."
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
  secondary: "The native Mac client that handles all 50 locales, In-App Purchases, Subscription Groups, and Game Center — same tool Lagerland ships 19 apps with."
  subheadline: "AppMeta edits metadata across all 50 ASC locales side-by-side, manages In-App Purchases and Subscription Groups, edits Game Center Achievements and Leaderboards, previews word-level diffs before any push, and runs AI keyword analysis through your own provider — including Apple Intelligence on-device for the times you don't want a single character leaving the Mac. Five AI providers supported (Anthropic, OpenAI, Google, Ollama / LM Studio, Apple Intelligence). $17.99/year or $29.99 lifetime."
  cta_label: "Download Free"
  alt: "AppMeta — native Mac editor for App Store Connect metadata with side-by-side locales and word-level diff preview"

who_for:
  - "You ship iOS or macOS apps and the App Store Connect web UI is the slowest tool in your release flow"
  - "You manage metadata across 10+ locales and refuse to scroll through 50 separate tabs to update one field"
  - "You've been burned by a silent overwrite on ASC web and want a diff preview before anything pushes"
  - "You want keyboard-first editing with the speed of a native Mac app, not a re-skinned browser"
  - "You'd rather pay $29.99 once than rent ASC tooling for $10–$70/month indefinitely"
  - "You want your ASC credentials in macOS Keychain, not a browser session that times out daily"

who_not_for:
  - "You ship one app a year and the ASC web UI is good enough for the few times you touch it"
  - "Your release pipeline is fully automated through Fastlane / CI and you never edit metadata by hand"
  - "You need competitive rank tracking, keyword popularity scoring, and competitor intelligence — that's Appfigures / AppTweak / Sensor Tower territory, not AppMeta's"
  - "You want a web-based dashboard your whole team can hit from any browser — AppMetaHub or ASO.dev fit that better"

alternatives_to:
  - "Itsyconnect"
  - "NativeConnect"
  - "App Store Connect web UI"
  - "Fastlane deliver"
  - "AppMetaHub"
  - "ASO.dev"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Why we built this"
  heading: "We ship 19 apps. AppMeta is the tool we built for ourselves."
  story: "AppMeta exists because every other workflow for managing App Store metadata broke for us at scale. The web UI is fine when you ship one app — it's torture when you ship 19. Fastlane deliver is great in CI but unworkable for interactive editing across 50 locales. NativeConnect was the closest native competitor and quietly let its marketing domain expire mid-2025. So we built the tool we needed: a native Mac app that opens fast, edits all 50 ASC locales side-by-side, shows a word-level diff before anything pushes, and runs AI keyword analysis through whichever provider we trust that week — including Apple Intelligence on-device for the times we don't want a single character leaving the Mac. Every Lagerland release on the App Store ships through AppMeta. It's the tool we use every day."
  signals:
    - "Same tool Lagerland uses to ship every release of all 19 apps in the catalogue"
    - "Built on the App Store Connect API v1 with JWT auth and .p8 keys stored in macOS Keychain — no app-specific passwords, no browser session"
    - "SwiftUI + SwiftData, macOS 14+ Sonoma minimum, no analytics SDKs, no backend servers"
    - "Five AI providers supported out of the box — Anthropic, OpenAI, Google, OpenAI-compatible (Ollama / LM Studio), Apple Intelligence on-device"
  external_link:
    label: "See the 19 Lagerland apps shipped with AppMeta →"
    href: "/apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally — usually within a day."

value_points:
  - title: "All 50 ASC locales, side-by-side"
    description: "AppMeta loads the canonical App Store Connect locale set — all 50, including the 11 Indian-region locales Apple added in 2026 (Bangla, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu, plus Slovenian and Urdu). Edit them at once or one at a time. Never tab-switch through 50 browser pages again."
  - title: "Diff preview before any push"
    description: "Word-level diff on every field, every locale. Push per-field, per-locale, or everything in one shot. Rollback-friendly workflow — no silent overwrites, no surprise revisions sneaking through."
  - title: "Five AI providers. Your key, your spend."
    description: "Keyword diagnosis runs locally — overlaps with subtitle, duplicate stems, wasted-character usage, locale-gap detection. Generation uses whichever provider you trust: Anthropic Claude (Sonnet 4.6 default), OpenAI GPT (GPT-4o default), Google Gemini (2.0 Flash), any OpenAI-compatible endpoint (Ollama on llama3.2, LM Studio, local proxies), or Apple Intelligence on-device (requires macOS 26 — zero API key, zero network)."
  - title: "Pay annually, or pay once and ship forever"
    description: "$17.99/year or $29.99 lifetime. Compare: AppMetaHub Indie is $120/year; ASO.dev Indie is $224.99/year. AppMeta's lifetime tier costs less than two months of ASO.dev Indie — and doesn't disappear when you stop paying."

how_it_works:
  intro: "AppMeta is a native macOS client for the App Store Connect API v1. JWT auth with a .p8 key, edits stored locally in SwiftData, diffs computed against your last fetched snapshot. Here's how a metadata change moves through it."
  steps:
    - title: "Connect with your App Store Connect API key (.p8)"
      detail: "AppMeta uses the modern App Store Connect API v1, not an app-specific password and not a scraped browser session. Generate a .p8 key in App Store Connect's Users and Access, paste the Issuer ID, Key ID, and the .p8 file into AppMeta once. The private key is stored in macOS Keychain — never in a plaintext file, never sent to a Lagerland server, never sent anywhere except api.appstoreconnect.apple.com."
    - title: "Fetch metadata for all 50 locales"
      detail: "AppMeta pulls the current state of your app's metadata across all 50 ASC locales — including the 11 Indian-region locales added in 2026 (Bangla, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu, plus Slovenian and Urdu) — and stores it locally in SwiftData. From this point on you can work offline, with sync happening on push."
    - title: "Edit side-by-side, keyboard-first"
      detail: "Every editable ASC field — name (30 chars), subtitle (30 chars), promotional text (170 chars), keywords (100 chars), description (4000 chars), what's new (4000 chars), support and marketing URLs — with real-time character-count validation. Keyboard-first navigation between fields and locales. Never wait on a browser page-load again."
    - title: "Run keyword diagnosis (no AI required)"
      detail: "AppMeta's Keyword Optimizer runs entirely on-device against the metadata you've already entered: detects keyword/subtitle overlap (wasted ranking surface), duplicate stems within a locale ('app' and 'application' both eat your 100 chars), locales with keywords no other locale uses (opportunity gaps), and storefront coverage gaps. No network call, no API key, no AI."
    - title: "Generate suggestions with your AI provider (optional)"
      detail: "When you want AI-generated keyword candidates or auto-localized metadata, pick a provider: Anthropic Claude (Sonnet 4.6 default, your API key), OpenAI GPT (GPT-4o default, your API key), Google Gemini (2.0 Flash, your API key), any OpenAI-compatible endpoint (Ollama on llama3.2, LM Studio, local proxies — no key required), or Apple Intelligence on-device (zero API key, zero network — requires macOS 26 and Apple Intelligence enabled). You pay your provider directly; AppMeta meters nothing."
    - title: "Preview the diff, push what you want"
      detail: "Before anything touches App Store Connect, AppMeta computes a word-level diff between your local edits and the last fetched server state. Push per-field, per-locale, or everything in one operation. Push only fr-FR's subtitle. Push every locale's keywords but nothing else. The granularity is yours."
    - title: "Submit, manage reviews, run TestFlight — same app"
      detail: "App Review Information, version pricing, age ratings, app privacy details, full version submission — handled in AppMeta. Read and reply to App Store reviews across regions from one view. Manage TestFlight builds, beta metadata, testing groups. In-App Purchases, Subscription Groups, Game Center (Achievements, Leaderboards, Leaderboard Sets) editable with the same locale-aware UI. The entire release surface, native on macOS 14+."

features:
  - title: "All 50 App Store Connect locales — including the 11 added in 2026"
    description: "AppMeta ships with the canonical App Store Connect locale set: 50 locales as of 2026, including Bangla, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu, Slovenian, and Urdu — the 11 locales Apple added in 2026. Side-by-side editing across all of them. Real-time character-count validation on every field."
  - title: "Word-level diff preview before every push"
    description: "Every change shows a word-level diff against your last fetched server state before it touches App Store Connect. Push per-field, per-locale, or everything in one operation. No silent overwrites — the failure mode that plagues the web UI for anyone editing in parallel with a teammate or running an automated pipeline alongside manual edits."
  - title: "Five AI providers — your key, your spend, your choice"
    description: "Generate keyword suggestions and auto-localize through whichever model you trust: <a href=\"https://www.anthropic.com/claude\" rel=\"noopener\" target=\"_blank\">Anthropic Claude</a> (Sonnet 4.6 default), <a href=\"https://platform.openai.com/\" rel=\"noopener\" target=\"_blank\">OpenAI GPT</a> (GPT-4o default), <a href=\"https://ai.google.dev/\" rel=\"noopener\" target=\"_blank\">Google Gemini</a> (2.0 Flash), any OpenAI-compatible endpoint (<a href=\"https://ollama.com/\" rel=\"noopener\" target=\"_blank\">Ollama</a> on llama3.2, LM Studio, local proxies — no key required), or <a href=\"https://www.apple.com/apple-intelligence/\" rel=\"noopener\" target=\"_blank\">Apple Intelligence</a> on-device (macOS 26 required, zero API key, zero network call). You pay your provider directly. AppMeta meters nothing."
  - title: "On-device keyword diagnosis — no AI required"
    description: "AppMeta's Keyword Optimizer runs entirely locally against the metadata you've already entered. Detects keyword/subtitle overlaps, duplicate stems within a locale, locale-gap opportunities, search-coverage gaps, and storefront-coverage anomalies. Useful even with zero AI configured."
  - title: "App Store Connect API v1 with .p8 / JWT — credentials in macOS Keychain"
    description: "AppMeta uses Apple's modern App Store Connect API v1 with JWT authentication and a .p8 key. No app-specific password, no scraped browser session. The private key is stored in macOS Keychain — never in a plaintext file. The only network endpoint AppMeta talks to is api.appstoreconnect.apple.com (and your chosen AI provider's API, if any)."
  - title: "Submissions, reviews, TestFlight, IAPs, Game Center — one app"
    description: "App Review Information, version pricing, age ratings, privacy details, full submission flow. Read and reply to App Store reviews across regions. Manage TestFlight builds and testing groups. Edit In-App Purchases and Subscription Groups. Edit Game Center Achievements, Leaderboards, and Leaderboard Sets — all with locale-aware UI. The entire ASC release surface, native on the Mac."
  - title: "Sales analytics and diagnostics built in"
    description: "Sales Analytics view pulls revenue and unit data through the ASC API. Diagnostics tab inspects crash signatures, call stacks, and performance metrics — the same data App Store Connect surfaces under Xcode Organizer, in a faster, browse-able UI."
  - title: "Screenshot upload for every device — including IAP review screenshots"
    description: "Drag-and-drop screenshot management for every App Store device class (iPhone, iPad, Mac, Apple Watch, Apple TV, Apple Vision). Also handles the hyper-specific case competitors usually miss: review screenshots for In-App Purchases and Subscription Groups, which Apple requires for review but which the ASC web UI buries three menus deep."

screenshots:
  - src: "/assets/screenshots/appmeta/1.png"
    alt: "AppMeta — App Store Connect metadata editor on macOS, side-by-side locale comparison"
  - src: "/assets/screenshots/appmeta/2.png"
    alt: "AppMeta — word-level diff preview before pushing changes to App Store Connect"
  - src: "/assets/screenshots/appmeta/3.png"
    alt: "AppMeta — keyword optimizer with overlap detection and locale-gap analysis on macOS"
  - src: "/assets/screenshots/appmeta/4.png"
    alt: "AppMeta — AI provider picker showing Anthropic Claude, OpenAI, Google Gemini, OpenAI-compatible, and Apple Intelligence options"

comparison_table:
  intro: "Each column below is a question an indie iOS developer actually asks before paying for an ASC tool. Itsyconnect is the closest direct competitor — a native Mac client, one-time priced, BYO-AI. AppMetaHub and ASO.dev are strong web/subscription competitors. NativeConnect's marketing site went offline mid-2025. Fastlane deliver is the free CLI baseline."
  competitors: ["AppMeta", "Itsyconnect", "NativeConnect", "AppMetaHub", "ASO.dev (Mac)", "Fastlane deliver"]
  rows:
    - feature: "Native Mac app (not a browser / not a CLI)"
      values: ["Yes — SwiftUI + SwiftData, macOS 14+", "Yes — native macOS", "Was native (AppKit) — currently inactive", "No — web only", "Yes — Universal app (iOS/iPad/Mac/Watch/Vision)", "No — CLI only"]
    - feature: "Pricing model"
      values: ["$17.99/yr or $29.99 lifetime", "€19.99 one-time, lifetime (free for 1 app)", "Was one-time (unverified)", "$10/mo Indie · $23/mo Pro", "$24.99/mo Indie · $68.99/mo Pro", "Free (open source)"]
    - feature: "3-year total cost (Indie tier)"
      values: ["$29.99 lifetime (or $68.97 annual)", "≈ $22 (€19.99 lifetime)", "Unknown", "≈ $360 (12 × $10 × 3)", "≈ $810 (12 × $22.50 × 3, yearly rate)", "$0"]
    - feature: "Number of App Store Connect locales supported"
      values: ["50 — canonical 2026 set, including the 11 added in 2026", "Not published", "Unverified — site offline", "37", "Multiple — count not published", "25+ via .txt files"]
    - feature: "Manages In-App Purchases + Subscription Groups + Game Center"
      values: ["Yes — all three, locale-aware UI", "No — not listed on site", "Partial (when active)", "No — metadata + screenshots focus", "IAPs yes; Game Center not mentioned", "No"]
    - feature: "Screenshot management (drag-and-drop, all device types, IAP review screenshots)"
      values: ["Yes — including IAP / subscription review screenshots", "Yes", "Yes (when active)", "Yes — drag-and-drop", "Yes", "Yes — via .txt files"]
    - feature: "Word-level diff before push"
      values: ["Yes — per-field, per-locale", "Yes — change tracking", "Was a key feature", "Yes — word-level", "Yes — change highlighting", "No — push or don't"]
    - feature: "AI keyword analysis (BYO API key)"
      values: ["5 providers — Anthropic, OpenAI, Google, OpenAI-compatible (Ollama / LM Studio), Apple Intelligence on-device", "6 providers — Anthropic, OpenAI, Google, xAI, Mistral, DeepSeek", "Unknown — site offline", "Yes — Pro plan only", "Yes — subscription tier dependent", "No"]
    - feature: "Apple Intelligence on-device support (no API key, no network)"
      values: ["Yes — macOS 26 required", "No — six cloud providers", "No", "No", "No", "No"]
    - feature: "Crash diagnostics + Sales Analytics in-app"
      values: ["Yes — crash signatures, call stacks, perf metrics, sales analytics", "Yes — crash tracking, analytics", "Partial (when active)", "No", "Yes — analytics & A/B testing", "No"]
    - feature: "MCP server (Claude Code / Cursor / Codex integration)"
      values: ["Not yet — on roadmap", "Yes — Claude Code, Cursor, Codex, OpenCode", "No", "Yes", "No", "No"]
    - feature: "Open source"
      values: ["No — proprietary, funded by paid software", "Yes — open source + self-hosted Docker option", "Unknown — inactive", "No", "No", "Yes — MIT licensed"]
    - feature: "Credentials in macOS Keychain"
      values: ["Yes — .p8 key in Keychain (hardware-encrypted)", "Yes — AES-256-GCM encrypted on-device", "Yes (when active)", "Stored server-side", "Yes — on-device storage", "Local .p8 file"]
  footnote: "Competitor pricing and features reflect each tool's public landing page and App Store description as of 2026-05-13. Itsyconnect Pro is €19.99 lifetime with a free tier for 1 app + 1 developer account; AppMetaHub Indie is $10/mo billed annually ($120/year); ASO.dev Indie is $24.99/mo or $224.99/year (yearly rate ≈ $18.75/mo); NativeConnect's marketing domain (nativeconnect.app) currently 301-redirects off-product so the App Store listing's status is unverified. Verify current pricing before switching."

plateau_disclosure:
  title: "What AppMeta won't do for you"
  rule: "AppMeta is a native Mac client for the App Store Connect API v1 — an editing and submission surface that runs locally on macOS 14+. It's deliberately not a competitive-intelligence platform or a CI replacement. The trade-off is what keeps it one-time-priced and entirely on your Mac."
  what_it_does_not_do: "AppMeta will not track competitor keyword rankings — that's Appfigures, AppTweak, Sensor Tower, or RespectASO territory. It will not run inside your CI pipeline as a CLI — Fastlane deliver still belongs in CI, and AppMeta is for interactive editing on the desktop. It will not give you Apple Search Ads campaign management. It will not run on iOS or iPad (it's a macOS app, by design). AI keyword suggestions are only as good as the provider you point it at — bring an API key (Claude / GPT / Gemini) or use Ollama or Apple Intelligence on-device."
  notes:
    - "Want to drive AppMeta from Claude Code, Cursor, Codex, or OpenCode via MCP? Not yet — MCP server support is on the AppMeta roadmap. Itsyconnect ships it today if your workflow depends on it."
    - "Want competitive rank tracking and keyword popularity scoring? Pair AppMeta with Appfigures or AppTweak — different jobs, complementary tools."
    - "Want to run metadata pushes in CI? Keep Fastlane deliver in your release pipeline; AppMeta handles the interactive desktop editing flow."
    - "Want to edit from your iPhone or iPad? AppMeta is macOS only — ASO.dev's Universal app is the closest alternative for cross-Apple-platform editing."
    - "Want Apple Search Ads campaign management? That's a different product surface; AppMeta covers App Store Connect, not Apple Search Ads Manager."
    - "Want open source code you can audit and self-host? AppMeta is proprietary — funded by paid software, not advertising or telemetry. Itsyconnect is the open-source option in this category."

training_vocabulary:
  overline: "Speaks ASC's language"
  heading: "The fields, locales, and APIs AppMeta touches."
  intro: "AppMeta uses Apple's official App Store Connect API v1 with JWT authentication. Below is the canonical surface — the ASC fields with their character limits, the 50 locales supported, the auth model, and the API endpoints AppMeta talks to."
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
        - "Pricing & Availability (per-version, per-storefront)"
        - "Age ratings, App Privacy details, categories"
        - "TestFlight builds, beta metadata, testing groups"
        - "In-App Purchases & Subscription Groups (locale-aware)"
        - "Game Center: Achievements, Leaderboards, Leaderboard Sets"
        - "App Store reviews — read and reply"
        - "Sales Analytics + Diagnostics (crash signatures, perf metrics)"
    - heading: "50 ASC locales (2026)"
      items:
        - "ar-SA · bn · ca · cs · da · de-DE · el · en-AU · en-CA · en-GB · en-US"
        - "es-ES · es-MX · fi · fr-CA · fr-FR · gu · he · hi · hr · hu · id · it"
        - "ja · kn · ko · ml · mr · ms · nl-NL · no · or · pa · pl"
        - "pt-BR · pt-PT · ro · ru · sk · sl · sv · ta · te · th"
        - "tr · uk · ur · vi · zh-Hans · zh-Hant — plus the 11 locales Apple added in 2026"
    - heading: "Auth & API"
      items:
        - "App Store Connect API v1 (api.appstoreconnect.apple.com)"
        - "JWT authentication with .p8 private key"
        - "Issuer ID + Key ID stored in macOS Keychain"
        - ".p8 private key stored in macOS Keychain — never in a plaintext file"
        - "No app-specific password, no browser session, no scraping"
        - "Five AI providers: Anthropic Claude, OpenAI GPT, Google Gemini, OpenAI-compatible (Ollama / LM Studio), Apple Intelligence on-device"

example_insights:
  overline: "What an AppMeta diagnosis looks like"
  heading: "Real ASO outputs, in plain English."
  intro: "AppMeta's Keyword Optimizer runs on-device against your existing metadata before any AI is involved. These are the kinds of plain-English diagnoses it surfaces — none of them require an API key."
  cards:
    - tag: "Overlap · Wasted chars"
      headline: "Your en-US subtitle eats 14 characters of your keywords field."
      body: "AppMeta detected that 4 keywords in en-US already appear verbatim in your subtitle. App Store search treats subtitle + name + keywords as one corpus, so those 14 characters are not earning you any additional ranking. Replace them with 4 unranked stems and recover the surface area."
    - tag: "Locale gap · Opportunity"
      headline: "fr-FR has 7 keywords that no other locale uses."
      body: "Either those 7 French keywords are intentional (regional terms, brand names) or they're stale translations from an old version. AppMeta surfaces the gap; you decide. The most common cause: a French translator added regional vocabulary that never propagated to fr-CA, leaving you with a half-localized French market."
    - tag: "Duplicate stems · Cleanup"
      headline: "Your es-ES keywords contain both 'aplicación' and 'app' — pick one."
      body: "Apple's stemmer treats them as the same root. You're using two of your 100 character slots on the same ranking signal. AppMeta flags every duplicate stem within a locale automatically; pick whichever variant matches local search behavior and reclaim the chars."
    - tag: "Storefront coverage"
      headline: "Your 'productivity' keyword ranks in en-US but nowhere else."
      body: "AppMeta cross-references your keywords against the Storefront Intelligence dataset and flags terms that perform well in one storefront but appear unused in the rest. This is the cheapest A/B test in ASO — copy a working keyword from your strongest storefront into the four next-most-similar ones and watch."

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No backend servers — AppMeta runs entirely on your Mac"
    - "No third-party analytics SDKs, no tracking domains, no telemetry"
    - "App Store Connect credentials stored in macOS Keychain (issuer ID, key ID, .p8 private key) — never in plaintext, never sent to Lagerland"
    - "AppMeta talks only to <code>api.appstoreconnect.apple.com</code> (and your chosen AI provider, if you configure one)"
    - "AI provider API keys, when set, are stored in macOS Keychain via the same path as ASC credentials"
    - "See the per-app <a href=\"/transparency/#appmeta\">Privacy Manifest</a> for the declared API usage and tracking-domain list (it's empty)"

faq:
  - q: "What is AppMeta?"
    a: "AppMeta is a native macOS client for App Store Connect. It edits app metadata across all 50 ASC locales side-by-side, previews word-level diffs before any push, runs AI keyword analysis through whichever provider you trust (Anthropic Claude, OpenAI GPT, Google Gemini, OpenAI-compatible endpoints like Ollama, or Apple Intelligence on-device), and handles full submissions — TestFlight, reviews, In-App Purchases, Game Center — without a browser. macOS 14+ Sonoma. App Store Connect API v1 with JWT and a .p8 key in macOS Keychain. $17.99/year or $29.99 lifetime."
  - q: "Is AppMeta an alternative to App Store Connect?"
    a: "AppMeta works alongside App Store Connect using Apple's official ASC API v1. It provides a faster, safer editing surface than the web UI with features the browser doesn't have — side-by-side editing across all 50 locales, word-level diff preview before any push, keyword diagnosis without an AI call, and five AI providers when you do want generation. Everything goes through Apple's API; nothing is scraped, nothing is stored on a Lagerland server."
  - q: "How is AppMeta different from Fastlane deliver?"
    a: "Fastlane deliver is a CLI tool built for CI/CD pipelines — strong when you want metadata in version control and automatic uploads on every release. AppMeta is a desktop tool for the interactive editing surface itself — all 50 locales visible at once, word-level diffs before pushes, keyword optimization, review management, In-App Purchase and Game Center editing. They are complementary: many developers keep Fastlane deliver in their release pipeline and use AppMeta for the manual editing flow."
  - q: "How is AppMeta different from Itsyconnect?"
    a: "Itsyconnect is an excellent native Mac client for App Store Connect at €19.99 lifetime (≈$22) — close to AppMeta's $29.99 lifetime. The honest difference is scope. AppMeta manages In-App Purchases, Subscription Groups, and Game Center (Achievements, Leaderboards, Leaderboard Sets) with locale-aware UI — Itsyconnect doesn't list any of those three. AppMeta supports Apple Intelligence on-device for keyword analysis (zero API key, zero network call, requires macOS 26) — Itsyconnect offers six cloud-only AI providers (Anthropic, OpenAI, Google, xAI, Mistral, DeepSeek). Itsyconnect offers MCP integration with Claude Code, Cursor, Codex, and OpenCode — AppMeta does not yet, though it's on the roadmap. Itsyconnect is open source with a self-hosted Docker option; AppMeta is proprietary, funded by honest paid software. The decision: ship a simple app and never touch IAPs / Game Center and want MCP from your IDE → Itsyconnect is the cheaper fit. Ship across many locales, monetize through subscriptions, ship Game Center content, or want Apple Intelligence keyword analysis on-device → AppMeta is the broader-scope tool."
  - q: "How is AppMeta different from NativeConnect?"
    a: "NativeConnect was a native AppKit Mac client for App Store Connect in the same shape as AppMeta. As of 2026-05, the NativeConnect marketing website (nativeconnect.app) 301-redirects off-product, suggesting the project is no longer actively maintained. AppMeta is the actively-maintained native Mac client in that category — built on SwiftUI + SwiftData, macOS 14+, App Store Connect API v1, with regular updates. Verify NativeConnect's current status on the App Store before deciding."
  - q: "How is AppMeta different from AppMetaHub and ASO.dev?"
    a: "AppMetaHub and ASO.dev are excellent web-based metadata editors at subscription pricing — AppMetaHub Indie is $10/month, ASO.dev Indie is $24.99/month or $224.99/year. AppMeta is a native Mac app (not a browser) at $17.99/year or $29.99 lifetime. Three years of AppMetaHub Indie is around $360, three years of ASO.dev Indie is around $675, three years of AppMeta is $29.99 lifetime or $68.97 annual. The structural trade-off: web tools give you any-browser access; AppMeta gives you native performance, offline editing, and a lifetime option. AppMeta also supports more locales (50 vs AppMetaHub's 37 as of 2026-05)."
  - q: "Which AI providers does AppMeta support for keyword generation?"
    a: "Five, out of the box: Anthropic Claude (Sonnet 4.6 default, your API key), OpenAI GPT (GPT-4o default, your API key), Google Gemini (2.0 Flash, your API key), any OpenAI-compatible endpoint (Ollama on llama3.2, LM Studio, local proxies — no key required), and Apple Intelligence on-device (requires macOS 26 and Apple Intelligence enabled — zero API key, zero network call). You pay your provider directly; AppMeta does not meter, proxy, or store your prompts or responses anywhere. Switching providers is one menu pick."
  - q: "Does AppMeta need an AI API key to work?"
    a: "No. AppMeta's Keyword Optimizer — overlap detection, duplicate-stem cleanup, locale-gap analysis, storefront coverage diagnostics — runs entirely on-device against your existing metadata, with no AI call required. AI keyword generation is opt-in and requires either a third-party API key (Claude / GPT / Gemini), a local endpoint (Ollama / LM Studio), or macOS 26 with Apple Intelligence."
  - q: "Is AppMeta safe? Where do my App Store Connect credentials go?"
    a: "AppMeta uses Apple's official App Store Connect API v1 — no scraping, no app-specific password, no browser session. You generate a .p8 API key in App Store Connect (Users and Access → Keys → App Store Connect API) and paste the Issuer ID, Key ID, and .p8 file into AppMeta once. All three are stored in macOS Keychain — the private key is never written to a plaintext file. The only network endpoint AppMeta talks to is <code>api.appstoreconnect.apple.com</code> (and your chosen AI provider, if you configure one). See the per-app Privacy Manifest on the transparency page for the full declared API usage."
  - q: "Is AppMeta free?"
    a: "AppMeta is free to download with a full demo mode (browse the UI with sample data — no Apple Developer account required to evaluate the app). Pro is $17.99/year, or $29.99 lifetime — one-time, no recurring fees. Applies across every Mac you sign in to the App Store with. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Can I submit apps for review through AppMeta?"
    a: "Yes. AppMeta supports the full submission flow — App Review Information, version pricing and availability, categories, age ratings, App Privacy details, and version submission. The entire release surface without a browser tab."
  - q: "How many App Store Connect locales does AppMeta support?"
    a: "All 50 ASC locales as of 2026. AppMeta's canonical locale list includes the 11 locales Apple added in 2026: Bangla (bn), Gujarati (gu), Kannada (kn), Malayalam (ml), Marathi (mr), Odia (or), Punjabi (pa), Tamil (ta), Telugu (te), Slovenian (sl), and Urdu — alongside the previously-supported 39 locales. AppMeta updates the locale list when Apple does."
  - q: "Does AppMeta manage In-App Purchases, subscriptions, and Game Center?"
    a: "Yes. In-App Purchases and Subscription Groups are editable with locale-aware UI. Game Center Achievements, Leaderboards, and Leaderboard Sets are editable with the same per-locale workflow. Reviews are readable and repliable across all regions in one view."
  - q: "Will AppMeta replace Appfigures, AppTweak, or Sensor Tower?"
    a: "No — different tools for different jobs. AppMeta is a metadata editor and submission client for the App Store Connect API. Appfigures, AppTweak, Sensor Tower, and RespectASO are competitive-intelligence platforms — keyword rank tracking, popularity scoring, competitor research, market analysis. Most indie developers use one of each: AppMeta for editing, an intelligence platform for research."
  - q: "What macOS version does AppMeta require?"
    a: "macOS 14 (Sonoma) and later. Apple Intelligence on-device support requires macOS 26 and Apple Intelligence enabled. The other four AI providers (Anthropic, OpenAI, Google, OpenAI-compatible) work on any supported macOS version."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/appmeta/support/"

release:
  first_release: "2026-02-01"
  last_updated: "2026-05-13"
  last_audited: "2026-05-13"
  audit_round: "3 (response to Itsyconnect entering SERP)"

related_apps:
  - appmeta-pulse
  - mockly
---
AppMeta is a native macOS client for App Store Connect, built for indie iOS and macOS developers who ship more than one app and want their editing surface on the desktop rather than in a browser tab. It edits app metadata across all 50 ASC locales side-by-side — including the 11 Indian-region locales Apple added in 2026 (Bangla, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu, plus Slovenian and Urdu) — with real-time character-count validation, word-level diff preview before any push, and per-field, per-locale, or all-at-once sync granularity. Keyword diagnosis runs entirely on-device: keyword/subtitle overlap detection, duplicate-stem cleanup, locale-gap analysis, search-coverage diagnostics, and storefront-coverage anomalies. AI keyword generation is opt-in and runs through whichever provider you trust — Anthropic Claude (Sonnet 4.6 default), OpenAI GPT (GPT-4o), Google Gemini (2.0 Flash), any OpenAI-compatible endpoint (Ollama on llama3.2, LM Studio, local proxies), or Apple Intelligence on-device (macOS 26, zero API key, zero network call). The full release surface is in one app: TestFlight build management, beta metadata, review reading and reply, App Review Information, pricing, age ratings, App Privacy details, full version submission, In-App Purchases, Subscription Groups, and Game Center editing (Achievements, Leaderboards, Leaderboard Sets) with locale-aware UI. Built on the App Store Connect API v1 with JWT authentication and a .p8 private key stored in macOS Keychain — no app-specific password, no scraped browser session. SwiftUI + SwiftData, macOS 14+ Sonoma. No backend servers, no analytics SDKs, no tracking domains. $17.99/year or $29.99 lifetime. The same tool Lagerland ships every release of all 19 catalogue apps with.
