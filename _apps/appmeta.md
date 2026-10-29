---
layout: app
slug: appmeta
name: "AppMeta"
tagline: "Edit, diff, and push your App Store listing from your Mac."
quick_answer: "AppMeta is a Mac app for indie developers who manage their own App Store Connect listings. It puts every locale in one window, shows a field-level diff against the live listing before you push, and measures keyword difficulty and demand against the live App Store with the evidence shown. In-App Purchases, subscriptions, TestFlight, Game Center, reviews, and submission are in the same app, and it talks straight to Apple with your API key kept in the Mac Keychain. The free download runs Demo Mode on sample data; connecting your own account needs Pro, at {P_YEARLY}/year or {P_LIFETIME} once, on macOS 14 or later."
category: developer-tools
status: live

app_store_url: "https://apps.apple.com/app/id6758547802"

price:
  model: freemium
price_override: "{P_YEARLY}/year or {P_LIFETIME} lifetime"
free_tier: false

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. The free download runs Demo Mode with sample data, and connecting your own App Store Connect account needs Pro. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew."

plans:
  - name: "Yearly"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "All of AppMeta Pro, billed once a year. Cancel anytime."
    features:
      - "Every locale in one editor, or one field across all locales"
      - "A field-level diff against App Store Connect before every listing push"
      - "Keyword health: wasted characters, duplicates, and overlaps"
      - "Live keyword difficulty and demand with the evidence (off until you turn it on)"
      - "AI translation with Apple Intelligence on your Mac, your own key, or a local model"
      - "In-App Purchases, subscriptions, Game Center, TestFlight, and submission"
      - "Reviews, Sales & Analytics, and Diagnostics"
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All of AppMeta Pro, paid once."
    features:
      - "Everything in Yearly"
      - "One-time purchase, no renewal"
      - "Restore your purchase from Settings"
    highlight: true
    highlight_label: "Best value"

icon: "/assets/icons/appmeta.png"
og_image: "/assets/og/appmeta.png"

seo:
  title: "AppMeta: App Store Connect Mac App for Metadata & ASO"
  description: "App Store Connect on your Mac: edit every locale, see a field-level diff before you push, and check keyword difficulty with the evidence shown."
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
    - app store keyword difficulty Mac
    - app store localization tool
    - TestFlight manager Mac
    - app review management Mac
    - app screenshot upload Mac
    - indie iOS developer tools Mac
    - app submission tool macOS
    - Apple Intelligence app store translation

hero:
  device: mac
  pre_headline: "For indie Apple developers who manage their own App Store Connect listings"
  headline: "Edit every locale on your Mac. See the diff before you push."
  secondary: "AppMeta is a native Mac app for App Store Connect. Your API key stays in the Mac Keychain, and the app talks to App Store Connect directly, with no AppMeta server in between."
  subheadline: "Edit the name, subtitle, keywords, and description for every locale in one window, or one field across all of them. Before you push, each change sits next to its live value in App Store Connect, and only the fields you changed go out. Keyword difficulty and demand come from the live App Store, with the evidence listed. Try every screen free in Demo Mode, then connect your account with Pro at {P_YEARLY}/year or {P_LIFETIME} once."
  cta_label: "Download Free"
  alt: "AppMeta on macOS showing the What's New field for every locale in one view, with the app's versions as tabs"

who_for:
  - "You manage your own App Store Connect listings in several locales, and the web UI makes you edit them one locale at a time"
  - "You want to see exactly what a push will change before it reaches the store"
  - "You work on keywords and want the evidence behind a difficulty score, not a bare number"
  - "You also handle In-App Purchases, subscriptions, TestFlight, Game Center, and review replies, and want them in one Mac app"
  - "You want your API key in the Mac Keychain and your App Store Connect requests going straight to Apple"
  - "You'd rather pay {P_LIFETIME} once than keep a monthly subscription for App Store Connect tooling"

who_not_for:
  - "You don't have an App Store Connect account. Without one, AppMeta only runs Demo Mode on sample data"
  - "Your release pipeline is fully automated through Fastlane or CI and you never edit metadata by hand"
  - "You need keyword rank tracking over time and competitor keyword research, which is what Appfigures, AppTweak, and Sensor Tower do"
  - "You need team seats, or a tool that runs in a browser, on iPhone, or on Windows; AppMetaHub (web) or ASO.dev (seats, more platforms) fit that better"

related_journal:
  slug: "app-store-keyword-field-100-characters"
  anchor: "How the App Store keyword field works: 100 characters, commas, and the words Apple already indexes"
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
  heading: "We ship {APP_COUNT} apps. AppMeta is the tool we built to manage their listings."
  story: "The App Store Connect web UI works for one app in one language. Across many apps and dozens of locales it turns into editing one locale at a time, with no clear view of what a save will overwrite. Fastlane deliver is good in CI and awkward for hand edits. So we built a Mac app that puts every locale in one window, shows the live value next to each change before a push, and measures keywords against the live App Store with the evidence listed. It runs on the Mac and talks to Apple directly, so there is no AppMeta server holding your key or your listings."
  signals:
    - "Built on the App Store Connect API with a team key; the .p8, Issuer ID, and Key ID stay in the Mac Keychain"
    - "No AppMeta server, and no analytics or advertising SDKs"
    - "AppMeta itself is available in 17 localizations"
    - "Requires macOS 14 Sonoma or later"
  external_link:
    label: "See all Lagerland apps →"
    href: "/apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally, usually within a day."

value_points:
  - title: "See the diff before you push"
    description: "Every changed field sits next to its live App Store Connect value, labeled App Store Connect and Your Changes. Push one field, one locale, or all of them in a single confirmed action. Fields that changed in App Store Connect since your last fetch are flagged, and Discard All Local Changes restores the live listing in every locale with one command."
  - title: "Keyword research that shows its work"
    description: "Difficulty is a 0 to 100 score built from the ten apps you would rank against, and Show the working lists every app and number behind it. Demand comes from Apple's own search suggestions. Where Apple returns nothing, AppMeta says so instead of showing a zero. Live research stays off until you turn it on."
  - title: "Runs on your Mac, talks straight to Apple"
    description: "There is no AppMeta server. Your .p8 key, Issuer ID, and Key ID live in the Mac Keychain on that Mac only, and requests go directly to App Store Connect. An AI provider sees your text only if you add your own key and use it."
  - title: "One app for the whole release"
    description: "Your listing, In-App Purchases and subscriptions, TestFlight, Game Center, submission checks, reviews, and sales live in one three-column window, with keyboard shortcuts to refresh, preview, and push."

how_it_works:
  intro: "AppMeta is a native Mac client for the App Store Connect API. It signs requests on your Mac with your own key, keeps your edits in a local copy, and compares them with the live listing before anything is pushed. A release goes through these steps."
  steps:
    - title: "Connect with your App Store Connect API key"
      detail: "Create a team API key in App Store Connect under Users and Access, then enter the Issuer ID, Key ID, and .p8 file in AppMeta. Validate Connection tests the key before it is saved. All three go into the Mac Keychain as items for that Mac only, never synced to iCloud. AppMeta signs short-lived tokens with the key on your Mac, and the .p8 itself never leaves it. You can add several accounts and switch between them in the sidebar."
    - title: "Fetch your listing"
      detail: "Refresh (⌘R) pulls the current metadata for every locale of the selected version. Your edits are stored on the Mac, so they survive a relaunch and only reach App Store Connect when you push. Apps with iOS and macOS versions get a row per platform, each with its own edits."
    - title: "Edit by locale, or one field across every locale"
      detail: "The Localizations tab edits the name, subtitle, description, keywords, promotional text, What's New, and the marketing, support, and privacy policy URLs for each locale. The Fields tab flips it: pick one field and edit it in every language at once. Character counts match the way App Store Connect counts, so a Hindi keyword field that a simple character count puts at 66/100 shows 99/100, as Apple counts it."
    - title: "Clean up your keywords"
      detail: "The Keywords tab shows each locale's keyword field against the 100-character limit with a Health Summary: Issues, Wasted Chars, Unique Tokens, and Efficiency. It flags words repeated across your name, subtitle, and keywords, and across locales. Remove Duplicates and Fix Overlaps clean them up. Storefront Coverage shows which of 57 storefronts your localizations reach, and Search Coverage estimates how many search queries your metadata can match."
    - title: "Measure difficulty and demand (optional)"
      detail: "Turn on live keyword difficulty in Settings and AppMeta measures each phrase against the App Store. Difficulty is a 0 to 100 score from the top ten apps for the phrase, with the evidence listed. Demand shows whether Apple's search suggestions return the phrase, and at which position. Opportunity combines the two and sorts the list. Measure Combinations tests every phrase your name, subtitle, and keywords can form, shows the plan first, and stops when you say so. Connect an Apple Ads account if you want Apple's popularity scores too."
    - title: "Translate and get keyword ideas (optional)"
      detail: "AI Translate drafts up to 20 target locales from a source locale in one batch, keeping your brand name and each field's limit. In the Keywords tab, AI can suggest keywords and replace redundant ones. Pick the provider in Settings: Apple Intelligence on your Mac (macOS 26 on a Mac that supports it, no key), Anthropic, OpenAI, or Google with your own key, or a local OpenAI-compatible server such as Ollama or LM Studio."
    - title: "Preview, then push"
      detail: "Preview (⌘⇧D) lists every changed field, App Store Connect on one side and Your Changes on the other. Push one field, one locale (⌘↩), or everything (⌘⇧↩), which asks you to confirm how many fields it will overwrite. Invalid values are blocked before they leave the Mac."
    - title: "Finish the release in the same app"
      detail: "Attach a build, add the version for review, and manage phased release for the iOS version. The Submission tab walks through App Review Info, Content Rights, Categories, Pricing, Availability, Age Rating, License Agreement, Privacy, and Copyright; Privacy is a read-only summary with a link to App Store Connect. TestFlight, In-App Purchases, Game Center, reviews, sales, and diagnostics each have their own tab."

features:
  - title: "Every locale in one window"
    description: "Edit the name, subtitle, description, keywords, promotional text, What's New, and three URLs for each locale, with a state on every field (Modified, Conflict, Synced, Error, Locked) and a live character count against Apple's limit. Or open the Fields tab and work through one field in every language. AppMeta manages all 50 App Store Connect locale codes, sorted the way App Store Connect sorts them or in your own order."
  - title: "A field-level diff before every listing push"
    description: "Preview shows your edits next to what is live in App Store Connect, field by field. Only changed fields are pushed: one field, one locale, or all of them after a confirmation. If a locale changed in App Store Connect since your last fetch, a banner tells you, and Accept Remote takes the live version."
  - title: "Keyword difficulty and demand, with the evidence"
    description: "Difficulty is a 0 to 100 score from the top ten apps for a phrase, built from their ratings and metadata, and Show the working lists every app in the sample and every number used. Demand shows whether Apple's search suggestions return the phrase and at which rank. Each reading carries its storefront and how fresh it is, and results are cached on your Mac for 7 days. These are estimates from Apple's public search results and suggestions, not official search volume. Live research is off until you switch it on in Settings."
  - title: "Keyword health checks for every locale"
    description: "The Health Summary counts Issues, Wasted Chars, Unique Tokens, and Efficiency for each keyword field. AppMeta flags words repeated across name, subtitle, and keywords, and across locales, and Remove Duplicates and Fix Overlaps clean them up. Storefront Coverage maps your localizations to 57 storefronts, the Keyword Efficiency Dashboard compares locales and exports to JSON or CSV, and none of it needs AI."
  - title: "AI translation on your Mac, or with your own key"
    description: "AI Translate drafts several locales from one source, up to 20 per batch, keeping your brand name and each field's limit. With <a href=\"https://www.apple.com/apple-intelligence/\" rel=\"noopener\" target=\"_blank\">Apple Intelligence</a> selected (macOS 26 on a Mac that supports it), the text stays on your Mac and no key is needed. For a cloud model, add your own key for <a href=\"https://www.anthropic.com/claude\" rel=\"noopener\" target=\"_blank\">Anthropic Claude</a>, <a href=\"https://platform.openai.com/\" rel=\"noopener\" target=\"_blank\">OpenAI</a>, or <a href=\"https://ai.google.dev/\" rel=\"noopener\" target=\"_blank\">Google Gemini</a>, or point it at a local server such as <a href=\"https://ollama.com/\" rel=\"noopener\" target=\"_blank\">Ollama</a> or LM Studio. You pay your provider directly; AppMeta sells no AI usage."
  - title: "In-App Purchases, subscriptions, and Game Center"
    description: "Create and edit in-app purchases, subscription groups, and auto-renewing subscriptions, with localized display names and descriptions, price points with proceeds, territory availability, and introductory offers (Free Trial, Pay Up Front, Pay As You Go). Game Center covers leaderboards, achievements, and leaderboard sets with localized text. Metadata goes through push; prices, offers, availability, and review screenshots save to App Store Connect as soon as you set them."
  - title: "TestFlight, reviews, and submission"
    description: "Review builds with expiry warnings, edit What to Test per locale, turn beta groups on or off, and set export compliance. Read reviews from every storefront, filter by rating, and reply or delete a reply. Attach a build, add the version for review, and run phased release for the iOS version. Screenshots upload by drag and drop to each locale's screenshot sets."
  - title: "Sales & Analytics and Diagnostics"
    description: "Sales & Analytics shows proceeds, units, subscriptions, MRR, the discovery funnel, and revenue by territory, in one of 20 display currencies converted with ECB monthly rates. Press Sync Recent or Full Reload to fetch from Apple; opening the tab shows what is already on your Mac. Diagnostics shows hangs and disk writes with their call-stack logs, plus launch time, memory, battery, terminations, and animation hitches per build."

screenshots:
  - src: "/assets/screenshots/appmeta/1.webp"
    alt: "AppMeta for Mac showing a diff preview of App Store metadata changes before pushing"
  - src: "/assets/screenshots/appmeta/2.webp"
    alt: "AppMeta for Mac pushing metadata for every locale at once"
  - src: "/assets/screenshots/appmeta/3.webp"
    alt: "AppMeta for Mac keyword coverage view across locales"
  - src: "/assets/screenshots/appmeta/4.webp"
    alt: "AppMeta for Mac reviews view for reading and replying to App Store reviews"
  - src: "/assets/screenshots/appmeta/5.webp"
    alt: "AppMeta for Mac sales dashboard with proceeds, units and charts"
  - src: "/assets/screenshots/appmeta/6.webp"
    alt: "AppMeta for Mac submission screen checking an app version before review"
  - src: "/assets/screenshots/appmeta/7.webp"
    alt: "AppMeta for Mac AI translation of app metadata into other languages"

comparison_table:
  intro: "Each row is a question indie iOS developers ask before paying for an ASC tool. Itsyconnect is the closest direct competitor: a free, MIT-licensed Mac client built on Electron, with BYO-AI and an MCP server. AppMetaHub (web) and ASO.dev (apps for Mac, iPhone, Windows, and more) are subscription competitors. Fastlane deliver is the free CLI baseline."
  competitors: ["AppMeta", "Itsyconnect", "AppMetaHub", "ASO.dev", "Fastlane deliver"]
  rows:
    - feature: "Native Mac app (not a browser / not a CLI)"
      values: ["Yes, native macOS app for macOS 14+", "Desktop app built on Electron (Next.js / React)", "No, web only", "Yes, plus iPhone, iPad, Windows, Linux, and Android apps", "No, CLI only"]
    - feature: "Pricing model"
      values: ["{P_YEARLY}/yr or {P_LIFETIME} lifetime", "Free, no limits (MIT open source)", "$10/mo Indie · $23/mo Pro", "Per seat: $29/mo Indie · $69/mo Pro, billed yearly", "Free (open source)"]
    - feature: "3-year total cost (Indie tier)"
      values: ["{P_LIFETIME} lifetime (or three years at {P_YEARLY})", "$0", "≈ $360 (12 × $10 × 3)", "≈ $1,044 (3 × $348, billed yearly)", "$0"]
    - feature: "Number of App Store Connect locales supported"
      values: ["50 App Store Connect locale codes", "All locales at once (count not published)", "37", "50", "Per-locale .txt files"]
    - feature: "Manages In-App Purchases + Subscription Groups + Game Center"
      values: ["Yes, all three, with localized text", "No, not in its README or source", "No, metadata + screenshots focus", "IAPs and subscriptions yes; Game Center not listed", "No"]
    - feature: "Screenshot upload (drag-and-drop, IAP review screenshots)"
      values: ["Yes: drag and drop to each locale's screenshot sets, plus IAP and subscription review screenshots", "Yes", "Yes, drag-and-drop", "Yes", "Yes, from screenshot folders, plus App Previews"]
    - feature: "Review changes before push"
      values: ["Field-level diff against the live listing; push by field, locale, or all", "Opt-in diff mode; push all at once", "Yes, word-level", "Yes, change highlighting", "HTML preview of local files; no comparison with live"]
    - feature: "AI (bring your own key)"
      values: ["5 options: Anthropic, OpenAI, Google, OpenAI-compatible (Ollama / LM Studio), Apple Intelligence on your Mac", "6 providers: Anthropic, OpenAI, Google, xAI, Mistral, DeepSeek", "Yes, Pro plan only", "Translation: Google Translate, or DeepL / ChatGPT / Claude with your keys", "No"]
    - feature: "Apple Intelligence on your Mac (no API key)"
      values: ["Yes, macOS 26 on a Mac that supports Apple Intelligence", "No, six cloud providers", "No", "No", "No"]
    - feature: "Diagnostics + sales analytics in-app"
      values: ["Yes: sales, subscriptions, App Store funnel, performance metrics, hang and disk-write logs", "Yes: crash tracking, analytics", "No", "Yes: analytics & A/B testing", "No"]
    - feature: "MCP server (Claude Code / Cursor / Codex integration)"
      values: ["No", "Yes: Claude Code, Cursor, Codex, OpenCode", "Yes", "Yes, local", "No"]
    - feature: "Open source"
      values: ["No, proprietary, funded by paid software", "Yes, MIT, plus a self-hosted Docker option", "No", "No", "Yes, MIT licensed"]
    - feature: "Where your App Store Connect key is stored"
      values: ["Mac Keychain, this Mac only, not synced to iCloud", "AES-256-GCM, master key in the Keychain", "Stored server-side", "On device; optional encrypted sync for teams", "Local .p8 file or Apple ID session"]
  footnote: "Itsyconnect, ASO.dev and fastlane details were checked on 2026-10-25: Itsyconnect against its GitHub README and v1.14.2 release, ASO.dev against its pricing page (per seat, excluding VAT), fastlane against docs.fastlane.tools. AppMetaHub figures come from its landing page as of 2026-05-13 and weren't rechecked; Indie was then $10/mo billed annually ($120/year). Verify current pricing before switching."

plateau_disclosure:
  title: "What AppMeta won't do for you"
  rule: "AppMeta is a Mac app for editing and shipping through the App Store Connect API. It is not a competitive-intelligence platform or a CI tool, and it is not affiliated with Apple."
  what_it_does_not_do: "AppMeta does not track keyword rankings over time or research competitors' keywords; Appfigures, AppTweak, Sensor Tower, and RespectASO do that. Its difficulty and demand figures are estimates from Apple's public search results and suggestions, not official search volume, and that source could change. It does not run in CI as a CLI, upload builds, add TestFlight testers, create beta groups, or manage Apple Ads campaigns. It runs on the Mac only. AI quality, cost, and privacy depend on the provider you pick."
  notes:
    - "Want every write to go through a diff? The diff covers listing metadata. In-App Purchase prices, introductory offers, availability, review screenshots, base price, Game Center pushes, and Add for Review write to App Store Connect directly."
    - "Want crash reports? Diagnostics shows hangs, disk writes, and performance metrics from Apple, which arrive 24 to 48 hours later. It is not a crash reporter."
    - "Want live numbers? Sales and reviews come from App Store Connect when you sync or refresh. Notifications for new reviews and diagnostics are local and checked while AppMeta is open."
    - "Want to fill in App Privacy details (the privacy 'nutrition label')? That stays in App Store Connect; AppMeta shows a read-only summary and links you there."
    - "Want to drive AppMeta from Claude Code, Cursor, Codex, or OpenCode via MCP? AppMeta has no MCP server. Itsyconnect ships one today if your workflow depends on it."
    - "Want to run metadata pushes in CI? Keep Fastlane deliver in your release pipeline; AppMeta handles the interactive desktop editing."
    - "Want Game Center images or leaderboard releases? Those stay in App Store Connect."
    - "Want open source code you can audit and self-host? AppMeta is proprietary and funded by sales, with no advertising or analytics SDKs. Itsyconnect is the open-source option in this category."

training_vocabulary:
  overline: "Speaks ASC's language"
  heading: "The fields, locales, and APIs AppMeta touches."
  intro: "AppMeta uses Apple's App Store Connect API with JWT authentication. These are the fields it edits with their character limits, the 50 locale codes it manages, the auth model, and the services it talks to."
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
        - "App Review Information, Content Rights, License Agreement, Copyright"
        - "Pricing (base country and price) and availability per territory"
        - "Age rating, categories, phased release (App Privacy details stay in App Store Connect)"
        - "TestFlight builds, What to Test, beta description, beta groups, export compliance"
        - "In-App Purchases, subscriptions, and Subscription Groups, with introductory offers"
        - "Game Center: Achievements, Leaderboards, Leaderboard Sets"
        - "App Store reviews: read, reply, and delete a reply"
        - "Sales & Analytics and Diagnostics (performance metrics, hang and disk-write signatures)"
    - heading: "50 App Store Connect locale codes"
      items:
        - "ar-SA · bn · ca · cs · da · de-DE · el · en-AU · en-CA · en-GB · en-US"
        - "es-ES · es-MX · fi · fr-CA · fr-FR · gu · he · hi · hr · hu · id · it"
        - "ja · kn · ko · ml · mr · ms · nl-NL · no · or · pa · pl"
        - "pt-BR · pt-PT · ro · ru · sk · sl · sv · ta · te · th"
        - "tr · uk · ur · vi · zh-Hans · zh-Hant"
    - heading: "Auth & API"
      items:
        - "App Store Connect API (api.appstoreconnect.apple.com)"
        - "JWT signed on your Mac with a team .p8 private key"
        - ".p8, Issuer ID, and Key ID in the Mac Keychain, this Mac only"
        - "No app-specific password, no browser session"
        - "Optional: Apple's public App Store search (keyword research), Apple Ads (popularity), ECB exchange rates (sales currency)"
        - "Five AI options: Anthropic Claude, OpenAI, Google Gemini, OpenAI-compatible (Ollama / LM Studio), Apple Intelligence on your Mac"

example_insights:
  overline: "What AppMeta's keyword views show"
  heading: "What the keyword views tell you."
  intro: "Examples of what the Keywords tab shows. The health checks run on your Mac against the metadata you already have; difficulty and demand need live research turned on."
  cards:
    - tag: "Overlap · Wasted chars"
      headline: "Keyword words that already sit in your subtitle."
      body: "Repeating words from your name or subtitle in the keyword field spends characters twice. The Health Summary counts those Wasted Chars per locale, and Fix Overlaps cleans them up."
    - tag: "Character count · Apple-accurate"
      headline: "A Hindi keyword field at 66/100 by simple count is 99/100 to Apple."
      body: "AppMeta counts characters the way App Store Connect does. A simple character count under-counts Hindi, Bangla, and Thai keyword fields, so a field that looks roomy can be nearly full. The count you see is the count Apple applies."
    - tag: "Difficulty · Evidence"
      headline: "Difficulty from 0 to 100, with the working shown."
      body: "Open a score and Show the working lists the ten apps in the sample and every number used. Each reading carries its storefront and how fresh it is, and a phrase Apple returns nothing for is marked as such, not scored zero."
    - tag: "Storefront coverage"
      headline: "Where your localizations reach across 57 storefronts."
      body: "Storefront Coverage maps your locales to 57 storefronts and scores duplication, expansion, and consistency. The app labels these as ASO best-practice heuristics, not an Apple table."

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No AppMeta server and no AppMeta account. AppMeta runs on your Mac and nothing is sent to Lagerland"
    - "No analytics, crash-reporting, or advertising SDKs, and no tracking"
    - "Your .p8 private key, Issuer ID, and Key ID are stored in the Mac Keychain as this-Mac-only items, not synced to iCloud. The .p8 never leaves your Mac"
    - "Listing and account data go to Apple through the App Store Connect API (<code>api.appstoreconnect.apple.com</code>)"
    - "Live keyword research, off until you turn it on, sends only the phrase and storefront to Apple's public App Store endpoints (<code>apps.apple.com</code>, <code>itunes.apple.com</code>, <code>search.itunes.apple.com</code>). Apple Ads (<code>api.ads.apple.com</code>, <code>appleid.apple.com</code>) is contacted only if you connect it. Sales currency conversion queries <code>data-api.ecb.europa.eu</code> for exchange rates"
    - "AI is optional. With Apple Intelligence or no AI, no text goes to an AI provider. With a cloud provider and your own key, the text you translate or analyze goes to that provider; AI keys are stored in the Mac Keychain"
    - "See the per-app <a href=\"/transparency/#appmeta\">Privacy Manifest</a> for the declared API usage and tracking-domain list (it's empty)"

faq:
  - q: "What is AppMeta?"
    a: "AppMeta is a native Mac app for App Store Connect, made for indie developers who manage their own listings. It edits every locale in one window, shows a field-level diff against the live listing before you push, and measures keyword difficulty and demand against the live App Store with the evidence shown. In-App Purchases, subscriptions, TestFlight, Game Center, reviews, submission, sales, and diagnostics are in the same app. It runs on macOS 14 or later and talks straight to Apple with your API key kept in the Mac Keychain. Demo Mode is free; connecting your account needs Pro at {P_YEARLY}/year or {P_LIFETIME} lifetime."
  - q: "Is AppMeta an alternative to App Store Connect?"
    a: "AppMeta works alongside App Store Connect through Apple's App Store Connect API. It is a faster place to do the editing: every locale in one window, one field across all locales, and a diff against the live listing before a push. Nothing is scraped from the website, and there is no AppMeta server in between. A few things still need App Store Connect itself, such as App Privacy details, Game Center images, and adding TestFlight testers. AppMeta is a third-party developer tool and is not affiliated with Apple."
  - q: "How is AppMeta different from Fastlane deliver?"
    a: "Fastlane deliver is a CLI tool for CI/CD pipelines. It works well when you want metadata in version control and automatic uploads on every release. AppMeta is a desktop tool for interactive editing: every locale of a field visible at once, a diff against the live value before a push, keyword research, review replies, and In-App Purchase and Game Center editing. The two work together: keep Fastlane deliver in your release pipeline and use AppMeta for hand edits."
  - q: "How is AppMeta different from Itsyconnect?"
    a: "Itsyconnect is a good App Store Connect client for the Mac, and it's free and MIT-licensed, built on Electron with a self-hosted Docker option. AppMeta is a native Mac app at {P_YEARLY}/year or {P_LIFETIME} lifetime. The main difference is scope. AppMeta creates and edits In-App Purchases, subscriptions, and Subscription Groups, and Game Center (Achievements, Leaderboards, Leaderboard Sets), with localized text; Itsyconnect doesn't cover any of those. AppMeta can run its AI with Apple Intelligence on your Mac (macOS 26 on a supported Mac) or a local model, while Itsyconnect offers six cloud providers (Anthropic, OpenAI, Google, xAI, Mistral, DeepSeek). Itsyconnect has an MCP server for Claude Code, Cursor, Codex, and OpenCode and a wider analytics view; AppMeta has no MCP server. If you don't sell IAPs or use Game Center, or you want free, open source, or MCP, pick Itsyconnect. If you monetize through in-app purchases, ship Game Center content, or want on-device AI, pick AppMeta. The full comparison is on the Itsyconnect alternative page."
  - q: "How is AppMeta different from NativeConnect?"
    a: "NativeConnect was a native Mac client for App Store Connect in the same shape as AppMeta. It was pulled from the Mac App Store in 2020 and hasn't been available since, so it isn't a current option. AppMeta is a native Mac client in that category, built on the App Store Connect API for macOS 14 or later, and it is updated regularly."
  - q: "How is AppMeta different from AppMetaHub and ASO.dev?"
    a: "AppMetaHub and ASO.dev are subscription tools. AppMetaHub is a web app; its Indie plan was $10/month in May 2026. ASO.dev has apps for Mac, iPhone, iPad, Windows, Linux, and Android and is priced per seat; Indie is $29/month billed yearly ($348/year) as of October 2026. AppMeta is a native Mac app at {P_YEARLY}/year or {P_LIFETIME} lifetime. Three years of AppMetaHub Indie is around $360, three years of ASO.dev Indie is around $1,044, and three years of AppMeta is {P_LIFETIME} lifetime or three payments of {P_YEARLY}. They give you a browser or more platforms, team seats, and (for ASO.dev) rank tracking. AppMeta gives you a native Mac app, edits kept on your Mac until you push, Game Center editing, and a lifetime option. AppMeta also manages more locales than AppMetaHub did in May 2026 (50 vs 37)."
  - q: "Which AI providers does AppMeta support?"
    a: "Five: Apple Intelligence on your Mac (macOS 26 on a Mac that supports it, no key), Anthropic Claude, OpenAI, and Google Gemini with your own API key, and any OpenAI-compatible server such as Ollama or LM Studio (no key needed). You pick the provider in Settings and pay it directly; AppMeta sells no AI usage. With a cloud provider, the text you translate or analyze goes from your Mac to that provider. With Apple Intelligence, it stays on your Mac."
  - q: "Does AppMeta need an AI API key to work?"
    a: "No. The listing editor, diff, push, and keyword health checks (wasted characters, duplicates, overlaps, storefront coverage) work without AI. Live difficulty and demand come from the App Store and need no AI key either. AI translation and keyword suggestions are optional and need Apple Intelligence, your own Anthropic, OpenAI, or Google key, or a local model."
  - q: "Is AppMeta safe? Where do my App Store Connect credentials go?"
    a: "AppMeta uses Apple's App Store Connect API, with no app-specific password and no browser session. You create a team API key in App Store Connect (Users and Access → Integrations → App Store Connect API) and enter the Issuer ID, Key ID, and .p8 file in AppMeta once. All three are stored in the Mac Keychain as items for that Mac only, not synced to iCloud. AppMeta signs short-lived tokens on your Mac, and the .p8 never leaves it. There is no AppMeta server. Other requests go to Apple's public App Store endpoints for keyword research (if you turn it on), Apple Ads (if you connect it), the European Central Bank for exchange rates, and your AI provider (if you add one). See the per-app Privacy Manifest on the transparency page for the declared API usage."
  - q: "Is AppMeta free?"
    a: "AppMeta is free to download and runs Demo Mode: every screen with sample apps, locales, keywords, IAPs, reviews, and sales, no account needed. Writes are disabled in Demo Mode. Connecting your own App Store Connect account needs Pro: {P_YEARLY}/year, or {P_LIFETIME} lifetime as a one-time purchase. Demo Mode lets you try every screen before you buy. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Can I submit apps for review through AppMeta?"
    a: "Yes. Attach a build, add the version for review, and manage phased release for the iOS version. The Submission tab checks App Review Info, Content Rights, Categories, Pricing, Availability, Age Rating, License Agreement, Privacy, and Copyright. App Privacy details are read-only in AppMeta, with a link to App Store Connect. Add for Review submits right away, without a confirmation step. Builds themselves are uploaded with Xcode, Transporter, or fastlane."
  - q: "How many App Store Connect locales does AppMeta support?"
    a: "AppMeta manages all 50 App Store Connect locale codes, from ar-SA to zh-Hant. You can sort them alphabetically the way App Store Connect does, by locale code, or in your own order, and add a locale to a version from the app."
  - q: "Does AppMeta manage In-App Purchases, subscriptions, and Game Center?"
    a: "Yes. Create and edit in-app purchases, subscription groups, and auto-renewing subscriptions, with localized names and descriptions, prices, territory availability, introductory offers, and review screenshots. Prices, offers, availability, and review screenshots save to App Store Connect as soon as you set them; metadata goes through push. Game Center covers Achievements, Leaderboards, and Leaderboard Sets with localized text. Game Center images and leaderboard releases stay in App Store Connect."
  - q: "Will AppMeta replace Appfigures, AppTweak, or Sensor Tower?"
    a: "No, they do different jobs. AppMeta is a metadata editor and release client for the App Store Connect API. It estimates difficulty and demand for the keywords you check, but it doesn't track rankings over time or research competitors' keywords. Appfigures, AppTweak, Sensor Tower, and RespectASO are competitive-intelligence platforms for rank tracking, competitor research, and market analysis. You can use both: AppMeta for editing and an intelligence platform for research."
  - q: "What macOS version does AppMeta require?"
    a: "macOS 14 (Sonoma) or later. Apple Intelligence translation needs macOS 26 on a Mac where Apple Intelligence is available. The other AI options (Anthropic, OpenAI, Google, OpenAI-compatible) work on any supported macOS version. AppMeta is Mac only, with no iPhone or iPad version."
  - q: "Which languages is AppMeta itself available in?"
    a: "AppMeta's interface is in 17 localizations covering 11 languages: English (US, UK, Australia, Canada), Arabic, German, Spanish (Spain, Mexico), French (France, Canada), Italian, Japanese, Korean, Portuguese (Brazil, Portugal), Russian, and Turkish. The listing editor manages all 50 App Store Connect locales whatever language the app runs in."

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
last_updated: 2026-10-29
---
AppMeta is a native Mac app for App Store Connect, made for indie Apple developers who manage their own listings in several locales. It edits the name, subtitle, description, keywords, promotional text, What's New, and URLs for every locale in one window, or one field across every locale, with character counts that match App Store Connect. Before a push, a field-level diff shows each change next to its live value, and only the fields you changed are pushed: one field, one locale, or all of them after a confirmation. Keyword tools flag wasted characters, duplicates, and overlaps, map coverage across 57 storefronts, and, when you turn live research on, measure difficulty from the top ten apps for a phrase and demand from Apple's search suggestions, with the evidence listed. AI translation and keyword suggestions are optional and run through Apple Intelligence on your Mac (macOS 26 on a supported Mac), your own Anthropic, OpenAI, or Google key, or a local model. The same app handles In-App Purchases, subscriptions, Game Center, TestFlight, submission, phased release, reviews, Sales & Analytics, and Diagnostics. AppMeta uses the App Store Connect API with a team .p8 key stored in the Mac Keychain, has no AppMeta server, and needs macOS 14 or later. Demo Mode is free; connecting your account needs Pro at {P_YEARLY}/year or {P_LIFETIME} lifetime. AppMeta is a third-party developer tool and is not affiliated with Apple.
