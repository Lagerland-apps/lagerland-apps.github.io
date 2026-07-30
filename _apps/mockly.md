---
layout: app
slug: mockly
name: "Mockly"
tagline: "Professional App Store screenshots for Mac."
quick_answer: "Mockly is a native macOS app that turns your screenshots into App Store–ready exports: real 3D device frames rendered with Apple's Metal framework, percentage-based layouts that scale across every device size, AI translation across 39 App Store locales, and direct upload to App Store Connect by device and locale. Everything runs locally on your Mac — no server, no account, no upload of pre-release assets to a third party. One-time $12.99, Family Sharing included. Subscription competitors in this category run $19–$49 per month."
category: graphics
platforms: ["macOS"]
status: live
jump_nav: true

redirect_from:
  - /apps/screenflow-studio/
  - /apps/screenflow-studio/index.html

app_store_url: "https://apps.apple.com/app/id6756589122"

price:
  model: one-time-purchase
  value: "$12.99 — one-time purchase"
schema_price: "12.99"
price_currency: "USD"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. Mockly is a one-time purchase — no auto-renew, no recurring fees."

value_math:
  label: "How the price compares."
  body: "Subscription App Store screenshot tools in this category run $19–$49 per month — $228–$588 over a year. Mockly is $12.99, once, with Family Sharing. Less than a single month of most of them."

icon: "/assets/icons/mockly.png"
og_image: "/assets/og/mockly.png"

seo:
  title: "App Store Screenshot Maker for Mac — Mockly"
  description: "Native Mac App Store screenshot maker: real 3D device frames, AI translation, direct ASC upload. One-time $12.99 — never a subscription."
  keywords:
    - App Store screenshot maker for Mac
    - App Store screenshot generator
    - native Mac App Store screenshots
    - 3D device frame Mac app
    - Metal-rendered screenshot tool
    - App Store Connect upload tool
    - App Store screenshot localization Mac
    - one-time purchase screenshot tool
    - Fastlane snapshot alternative
    - Picsew alternative Mac
    - Screenshot Studio alternative
    - AppLaunchpad alternative
    - Screenshots Pro alternative
    - Rotato alternative
    - ASO screenshot maker
    - indie developer screenshot tool

hero:
  device: mac
  pre_headline: "App Store screenshots. Done right."
  headline: "App Store Screenshot Maker for Mac."
  subheadline: "Real 3D device frames rendered in Metal. AI translation across 39 App Store locales. Direct upload to App Store Connect, by device and language. Everything on your Mac — no browser, no server, no upload of your pre-release screenshots to anyone."
  cta_label: "Get Mockly"
  alt: "Mockly — 3D iPhone device mockup with App Store screenshot composed on Mac"

who_for:
  - "You're an indie iOS, iPadOS, or macOS developer shipping apps in multiple languages"
  - "You're a solo marketer or ASO professional producing App Store screenshots without a designer in the loop"
  - "You need real 3D Metal-rendered device frames, not flat 2D mockup overlays"
  - "You want to upload finished screenshots directly to App Store Connect, by device size and locale — not through a browser"
  - "You'd rather pay $12.99 once than $19–$49/month forever for a SaaS subscription"
  - "You ship pre-release apps under NDA and don't want screenshots routed through a third-party server"

who_not_for:
  - "Your team has Fastlane snapshot and frameit fully wired into CI and you never touch GUI tools"
  - "You only ship a single-locale app and don't need localization management"
  - "You're building marketing campaign creatives outside the App Store (Figma is the right tool for that)"
  - "You want App Store Preview video assets (Mockly handles still screenshots, not video)"

alternatives_to:
  - "Screenshot Studio"
  - "AppLaunchpad"
  - "Screenshots.pro"
  - "Rotato"
  - "Previewed"
  - "AppMockUp"
  - "Picsew"
  - "Fastlane frameit / snapshot"

value_points:
  - title: "Real 3D, not flat mockups"
    description: "Metal-powered rendering with actual 3D device frames. Rotate, scale, and position with numeric precision. The preview matches the export pixel-for-pixel — no surprises at submission time."
  - title: "Ship in every App Store locale"
    description: "Translates overlaid text in-place across 39 App Store locales while preserving fonts, positioning, and right-to-left languages. Manage every market from one project."
  - title: "Upload without leaving the app"
    description: "Direct App Store Connect upload, by device size and locale. The workflow that should have existed years ago — no browser, no manual file shuffling."
  - title: "One price. No subscription. Forever."
    description: "Pay $12.99 once. Subscription competitors in this category charge $19–$49 per month — $228–$588 over a year. Mockly costs less than a single month of those tools."

how_it_works:
  intro: "Mockly is a deterministic render pipeline plus an App Store Connect uploader. Here's exactly what it does, end to end."
  steps:
    - title: "Drop your raw screenshots in"
      detail: "Bulk-import screenshots organised by language and device size from a folder, or drag them in one at a time. Mockly detects resolution and routes each image to the correct device class."
    - title: "Frame each shot in a real 3D device"
      detail: "Every device frame is a real 3D model rendered with Apple's Metal framework — not a 2D PNG overlay. Rotate, tilt, scale, and position with numeric precision. The on-screen preview is what the exporter will produce."
    - title: "Layout with percentage-based coordinates"
      detail: "Position every element with percentage coordinates rather than pixels. Your layout stays perfect across iPhone 6.9\", 6.7\", 6.5\", 5.5\", iPad 13\", 12.9\", 11\", Mac 2880×1800, Apple Watch 410×502, and visionOS 3840×2160 without per-resolution adjustment."
    - title: "Localise overlaid text into 39 App Store locales"
      detail: "Mockly's AI translation pass localises every overlaid text element in place — preserving fonts, positioning, and right-to-left scripts — for any combination of the 39 locales App Store Connect accepts. You bring your own API key; nothing is routed through a Lagerland server."
    - title: "Render the export bundle"
      detail: "Every device class × every locale × every screenshot is rendered as a separate file at the exact dimensions App Store Connect requires (iPhone 6.9\" 1290×2868, iPad 13\" 2064×2752, Mac 2880×1800, and so on). Deterministic — re-render the same project tomorrow and the bytes are identical."
    - title: "Upload directly to App Store Connect"
      detail: "Authenticate with your App Store Connect account via Apple's secure framework (credentials never leave Keychain), and Mockly uploads each screenshot to the correct device size and locale slot. What previously took 30 minutes of manual file-shuffling per release becomes one button."

example_insights:
  overline: "What Mockly actually exports"
  heading: "Real exports, at the exact dimensions App Store Connect requires."
  intro: "What Mockly produces in practice — captioned exports across device classes and locales."
  cards:
    - headline: "iPhone 6.9\" — exact 1290×2868 output"
      body: "A 3D-framed iPhone 16 Pro Max screenshot with overlaid feature copy, rendered locally at 1290×2868 in roughly 50ms on an M-series Mac. Deterministic — re-render the same project tomorrow and the bytes are identical."
      tag: "Render · Determinism"
    - headline: "Same layout, 39 locales"
      body: "One project produces 39 sets of localised screenshots — Japanese, Simplified Chinese, German, French, Arabic — with text translated in-place and fonts preserved."
      tag: "Localisation · Scale"
    - headline: "iPad 13\" — landscape and portrait"
      body: "iPad Pro M4 device frame at 2064×2752, with landscape orientation handled natively. Same layout system; different aspect ratio."
      tag: "Device · iPad"
    - headline: "Mac 2880×1800 — Studio Display crop"
      body: "Mac App Store screenshots in the exact 2880×1800 dimensions App Store Connect expects, with bezel options and shadow control."
      tag: "Device · Mac"
    - headline: "Apple Watch + Apple Vision Pro coverage"
      body: "Single source produces Watch 410×502 frames and visionOS 3840×2160 environment renders alongside the iPhone set."
      tag: "Device · Coverage"
    - headline: "Bulk upload to App Store Connect"
      body: "234 screenshots (6 sets × 39 locales) uploaded to the correct device + locale slots in App Store Connect in under two minutes. No browser tabs."
      tag: "Workflow · Upload"

features:
  - title: "3D Metal rendering engine"
    description: "Real 3D device frames rendered with Apple's Metal framework — not flat 2D PNG overlays. Deterministic output: your preview matches your export pixel-for-pixel."
  - title: "Localise across 39 App Store locales"
    description: "AI-powered in-place text translation across every locale App Store Connect accepts. Bring your own API key; preserves fonts, positioning, and right-to-left scripts."
  - title: "Direct App Store Connect upload"
    description: "Authenticated via Apple's secure framework. Mockly submits each screenshot to the correct device size × locale slot. Credentials stay in Keychain — never routed through a Lagerland server."
  - title: "Percentage-based precision layout"
    description: "Position elements with percentage coordinates rather than pixels. Layouts stay perfect across iPhone 6.9\" / 6.7\" / 6.5\" / 5.5\", iPad 13\" / 12.9\" / 11\", Mac 2880×1800, Apple Watch 410×502, and visionOS 3840×2160."
  - title: "Bulk import and smart templates"
    description: "Drop a folder of raw screenshots organised by language and device — Mockly routes each file to the right slot. Start from professional templates or build custom layouts from scratch."
  - title: "Native Mac, sandboxed, on-device"
    description: "A real macOS app — not an Electron wrapper. Sandboxed, signed, notarised. Your pre-release screenshots never leave your Mac for a third-party server. Apple's App Privacy nutrition label lists zero data collected."

screenshots:
  - src: "/assets/screenshots/mockly/1.png"
    caption: "Mockly's 3D Metal renderer composing a real device frame on Mac."
  - src: "/assets/screenshots/mockly/2.png"
    caption: "Percentage-based layout editor — one project, every device size."
  - src: "/assets/screenshots/mockly/3.png"
    caption: "AI translation pass localising overlaid text in-place across 39 App Store locales."
  - src: "/assets/screenshots/mockly/4.png"
    caption: "Bulk import: drop a folder organised by language and device, Mockly routes each file."
  - src: "/assets/screenshots/mockly/5.png"
    caption: "Render preview — what you see is what App Store Connect receives, byte-for-byte."
  - src: "/assets/screenshots/mockly/6.png"
    caption: "Direct App Store Connect upload by device size and locale. Credentials stay in Keychain."
  - src: "/assets/screenshots/mockly/7.png"
    caption: "Project library — every locale × every device class managed from one window."

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  app_privacy_label: "Apple's App Privacy nutrition label lists Mockly as collecting zero data. Pre-release screenshots, project files, and App Store Connect credentials never leave your Mac for a Lagerland server."
  notes:
    - "No analytics, no third-party trackers, no telemetry SDKs"
    - "No account required for the app itself — App Store Connect credentials are handled by Apple's frameworks and stored in Keychain"
    - "Pre-release screenshots and project files stored locally on your Mac"
    - "AI translation uses your own API key, called directly from your Mac — translations never route through a Lagerland server"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Who built this"
  heading: "A one-person studio. That's the point."
  story: "Mockly is built by a single independent developer at Lagerland Apps, working from Finland since 2025. After years of shipping indie iOS apps and watching the App Store screenshot pipeline get steadily worse — every credible competitor either subscription-priced, web-based, or both — Lagerland Apps built the tool that should have existed: native Mac, real 3D Metal rendering, AI translation that runs against your own API key, and a direct App Store Connect uploader that respects Keychain. Everything stays on your machine because that's the only architecture that makes sense for pre-release screenshots under NDA."
  signals:
    - "Native macOS app — Metal-rendered, sandboxed, notarised, no Electron wrapper"
    - "App Privacy nutrition label lists zero data collected"
    - "No analytics SDKs, no third-party trackers, no growth team — a one-person studio with a long-term commitment to the app"
    - "18 live apps in the catalogue, all under the same privacy philosophy: no tracking, no ads, no required accounts"
  external_link:
    label: "More apps from Lagerland Apps →"
    href: "/apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally — usually within a day."

release_notes:
  - date: "2026-04-05"
    note: "Localisation pass expanded to all 39 App Store Connect locales, including right-to-left support for Arabic and Hebrew."
  - date: "2026-03-12"
    note: "Direct App Store Connect upload pipeline — push every device size × locale in one button. Credentials handled via Apple's Keychain framework."
  - date: "2026-02-24"
    note: "Percentage-based layout engine — position elements with % coordinates so layouts scale across every device class without per-resolution adjustment."
  - date: "2026-02-12"
    note: "AI translation engine with bring-your-own API key. Preserves fonts, positioning, and right-to-left scripts."
  - date: "2026-02-01"
    note: "Mockly 1.0 — native macOS, 3D Metal device-frame rendering, bulk import, professional templates."

faq:
  - q: "What is Mockly?"
    a: "Mockly is a native macOS app for creating App Store screenshots using real 3D device frames rendered with Apple's Metal framework. It supports percentage-based layouts that scale across every device size, AI translation across 39 App Store locales, and direct upload to App Store Connect — all running locally on your Mac with no account and no server."
  - q: "How is Mockly different from other screenshot tools?"
    a: "Three structural differences. First: native Mac, not a web app — your pre-release screenshots never leave your machine. Second: real 3D Metal-rendered device frames, not flat 2D PNG overlays. Third: one-time $12.99 instead of $19–$49 per month. Direct App Store Connect upload removes the manual browser-uploading step that every web competitor still requires."
  - q: "What sizes does Mockly export?"
    a: "Every size App Store Connect requires. iPhone: 6.9\" (1290×2868), 6.7\" (1290×2796), 6.5\" (1242×2688), 5.5\" (1242×2208). iPad: 13\" (2064×2752), 12.9\" (2048×2732), 11\" (1668×2388). Mac App Store: 2880×1800, 2560×1600, 1440×900, 1280×800. Apple Watch: 410×502, 396×484, 368×448. Apple TV: 1920×1080, 3840×2160. visionOS: 3840×2160. Layouts scale automatically thanks to percentage-based positioning — one project produces every size."
  - q: "Does Mockly support all Apple App Store locales?"
    a: "Yes. Mockly supports all 39 locales App Store Connect accepts — including English (US, UK, AU, CA), Japanese, Simplified and Traditional Chinese, Korean, German, French (FR, CA), Spanish (ES, MX), Portuguese (PT, BR), Italian, Dutch, Polish, Czech, Slovak, Hungarian, Romanian, Russian, Turkish, Arabic, Hebrew, Greek, Swedish, Norwegian, Danish, Finnish, Indonesian, Malay, Thai, Vietnamese, Hindi, Ukrainian, Catalan, and Croatian. Right-to-left scripts (Arabic, Hebrew) are handled natively."
  - q: "Can I localise screenshots for multiple languages?"
    a: "Yes. Mockly's AI translation localises overlaid text in-place across the 39 App Store locales — preserving fonts, positioning, and right-to-left scripts. You bring your own API key; translations are called from your Mac and never routed through a Lagerland server. Bulk language management means one project can produce every locale."
  - q: "Is Mockly a subscription?"
    a: "No. Mockly is a one-time purchase at $12.99 with Family Sharing for up to six members. Subscription tools in this category run $19–$49 per month — $228–$588 over a year. Mockly costs less than a single month of most of them, and there are no recurring fees or feature gates."
  - q: "Can I upload directly to App Store Connect?"
    a: "Yes. Mockly authenticates with your App Store Connect account via Apple's secure framework, with credentials handled by macOS Keychain. It then submits each screenshot to the correct device size × locale slot in seconds. No browser, no manual file shuffling, no third-party server."
  - q: "Does Mockly handle App Store Preview videos?"
    a: "No — Mockly focuses on still screenshots, the highest-leverage App Store asset. App Store Preview video is a separate format with different recording, encoding, and submission requirements; we'd rather do screenshots well than spread thin across both."
  - q: "Does Mockly work with Fastlane?"
    a: "Mockly is a GUI alternative to Fastlane snapshot + frameit. If your team has Fastlane fully wired into CI/CD, you may not need Mockly — but most indie devs find the Fastlane setup-cost steeper than running a tool that ships with templates and a direct upload pipeline. Both can coexist."
  - q: "Does Mockly collect any data?"
    a: "No. Apple's App Privacy nutrition label lists Mockly as collecting zero data. No analytics, no telemetry SDKs, no account required for the app itself. All project files and pre-release screenshots stay on your Mac. AI translation runs against your own API key, called directly from your machine."
  - q: "How do Mockly screenshots comply with App Store Review Guidelines §2.3.3?"
    a: "App Store Review Guidelines §2.3.3 requires that screenshots show the app actually running on the device — not just illustrations, conceptual mockups, or pre-rendered marketing art that doesn't reflect in-app behaviour. Mockly renders your real captured screenshots inside a 3D device frame; the device is rendered, the screen content is the actual app. Overlaid feature copy and background colour treatments are fine under §2.3.3 as long as the screen content itself shows the real app. Mockly's default templates stay on the compliant side of the line — text overlays, colour fields, device frames around real UI captures, no fictional UI."
  - q: "How does Mockly compare to MockUPhone, LocaShot, Picasso, or AppMockUp?"
    a: "All four are web-based with different focuses. MockUPhone is a free device-mockup generator with no localisation or upload pipeline — useful for one-off marketing images, not a production screenshot workflow. LocaShot specialises in AI screenshot localisation across 30+ languages but doesn't render 3D device frames the way Mockly does. Picasso emphasises bulk upload to App Store Connect and Google Play with a strong template library, subscription-priced. AppMockUp is a long-standing mockup generator focused on iPhone and a handful of Android devices. Mockly is the only native Mac option with real 3D Metal rendering, on-device translation against your own API key, direct ASC upload, and a one-time price. If you want a free quick mockup, MockUPhone. If you want SaaS scale with team features, Picasso. If you want the Mac-native one-time-purchase indie option, Mockly."

related_apps:
  - appmeta
  - appmeta-pulse

related_journal:
  slug: why-mac-native-for-app-store-screenshots
  anchor: "Why Mac-native is the right architecture for App Store screenshots"

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/mockly/support/"

release:
  first_release: "2026-02-01"
  last_updated: "2026-05-27"
---
Mockly is a professional native macOS tool for creating App Store screenshots with real 3D device frames rendered using Apple's Metal framework. It features deterministic rendering (the on-screen preview matches the export pixel-for-pixel), percentage-based layout positioning that scales across every Apple device size (iPhone 6.9" through 5.5", iPad 13" through 11", Mac 2880×1800, Apple Watch 410×502, and visionOS 3840×2160), AI-powered in-place text translation across 39 App Store Connect locales, multi-language screenshot management, bulk import from folders organised by language, professional templates, and direct upload to App Store Connect with credentials managed by Apple's Keychain. Built for indie iOS, iPadOS, and macOS developers, studios, and ASO professionals shipping in multiple markets. One-time purchase at $12.99 with Family Sharing — subscription competitors in this category charge $19–$49 per month. No subscriptions, no tracking, no data collection, no upload of pre-release screenshots to a third-party server. Formerly known as ScreenFlow Studio — renamed to Mockly in 2026.
