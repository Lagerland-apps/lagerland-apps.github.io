---
layout: app
slug: mockly
name: "Mockly"
tagline: "Professional App Store screenshots for Mac."
quick_answer: "Mockly is a native macOS app that turns your screenshots into App Store-ready exports. It frames them in real 3D devices rendered with Apple's Metal framework, uses percentage-based layouts that scale across every device size, translates text into 39 App Store locales with AI, and uploads directly to App Store Connect by device and locale. Everything runs locally on your Mac, with no server, no account, and no upload of pre-release assets to a third party. It costs {P_APP} once, with Family Sharing included. Subscription competitors in this category charge $19 to $49 per month."
category: graphics
status: live
jump_nav: true

redirect_from:
  - /apps/screenflow-studio/
  - /apps/screenflow-studio/index.html

app_store_url: "https://apps.apple.com/app/id6756589122"

price:
  model: one-time-purchase

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple through the standard App Store refund flow. Mockly is a one-time purchase with no auto-renew and no recurring fees."

value_math:
  label: "How the price compares."
  body: "Subscription App Store screenshot tools in this category charge $19 to $49 per month, or $228 to $588 a year. Mockly is {P_APP} once, with Family Sharing, which is less than a single month of most of them."

icon: "/assets/icons/mockly.png"
og_image: "/assets/og/mockly.png"

seo:
  title: "App Store Screenshot Maker for Mac: Mockly"
  description: "Native Mac App Store screenshot maker with real 3D device frames, AI translation, and direct ASC upload. {P_APP} once, no subscription."
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
  pre_headline: "App Store screenshots, made on your Mac."
  headline: "App Store Screenshot Maker for Mac."
  subheadline: "Mockly renders real 3D device frames in Metal, translates your captions into 39 App Store locales with AI, and uploads straight to App Store Connect by device and language. It all happens on your Mac, so your pre-release screenshots never go through a browser or anyone's server."
  cta_label: "Get Mockly"
  alt: "Mockly 3D iPhone device mockup with an App Store screenshot composed on Mac"

who_for:
  - "You're an indie iOS, iPadOS, or macOS developer shipping apps in multiple languages"
  - "You're a solo marketer or ASO professional making App Store screenshots without a designer"
  - "You want real 3D device frames rendered in Metal instead of flat 2D mockup overlays"
  - "You want to upload finished screenshots to App Store Connect by device size and locale, without a browser"
  - "You'd rather pay {P_APP} once than $19 to $49 a month for a SaaS subscription"
  - "You ship pre-release apps under NDA and don't want screenshots routed through a third-party server"

who_not_for:
  - "Your team has Fastlane snapshot and frameit fully wired into CI and you never touch GUI tools"
  - "You only ship a single-locale app and don't need localization management"
  - "You're making marketing campaign creatives for use outside the App Store (Figma fits that better)"
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
  - title: "Real 3D device frames"
    description: "Device frames are 3D models rendered with Metal. Rotate, scale, and position them with numeric values. The preview matches the export pixel for pixel, so what you submit is what you saw."
  - title: "Ship in every App Store locale"
    description: "Mockly translates overlaid text in place into 39 App Store locales and keeps your fonts, positioning, and right-to-left languages intact. Every market lives in one project."
  - title: "Upload without leaving the app"
    description: "Mockly uploads to App Store Connect directly, sorted by device size and locale, so you don't open a browser or move files around by hand."
  - title: "One price, no subscription"
    description: "Pay {P_APP} once. Subscription competitors in this category charge $19 to $49 per month, or $228 to $588 a year. Mockly costs less than a single month of those tools."

how_it_works:
  intro: "Mockly is a deterministic render pipeline with an App Store Connect uploader. These are the steps from raw screenshot to upload."
  steps:
    - title: "Drop your raw screenshots in"
      detail: "Bulk-import a folder of screenshots organised by language and device size, or drag them in one at a time. Mockly reads each image's resolution and puts it in the right device class."
    - title: "Frame each shot in a real 3D device"
      detail: "Every device frame is a 3D model rendered with Apple's Metal framework instead of a 2D PNG overlay. Rotate, tilt, scale, and position it with numeric values. The exporter produces exactly what the on-screen preview shows."
    - title: "Layout with percentage-based coordinates"
      detail: "Position every element with percentage coordinates. The same layout holds across iPhone 6.9\", 6.7\", 6.5\", 5.5\", iPad 13\", 12.9\", 11\", Mac 2880×1800, Apple Watch 410×502, and visionOS 3840×2160 without per-resolution adjustment."
    - title: "Localise overlaid text into 39 App Store locales"
      detail: "Mockly's AI translation pass localises every overlaid text element in place, keeping fonts, positioning, and right-to-left scripts, for any combination of the 39 locales App Store Connect accepts. You bring your own API key, and nothing goes through a Lagerland server."
    - title: "Render the export bundle"
      detail: "Each screenshot is rendered once per device class and locale, as a separate file at the exact dimensions App Store Connect requires (iPhone 6.9\" 1290×2868, iPad 13\" 2064×2752, Mac 2880×1800, and so on). Rendering is deterministic: re-render the same project tomorrow and the bytes are identical."
    - title: "Upload directly to App Store Connect"
      detail: "Sign in to App Store Connect through Apple's secure framework (credentials never leave Keychain), and Mockly uploads each screenshot to the correct device size and locale slot. That replaces about 30 minutes of moving files by hand per release with one button."

example_insights:
  overline: "What Mockly exports"
  heading: "Exports at the exact dimensions App Store Connect requires."
  intro: "Examples of captioned exports across device classes and locales."
  cards:
    - headline: "iPhone 6.9\": exact 1290×2868 output"
      body: "A 3D-framed iPhone 16 Pro Max screenshot with overlaid feature copy, rendered locally at 1290×2868 in roughly 50ms on an M-series Mac. Re-render the same project tomorrow and the bytes are identical."
      tag: "Render · Determinism"
    - headline: "Same layout, 39 locales"
      body: "One project produces 39 sets of localised screenshots (Japanese, Simplified Chinese, German, French, Arabic, and the rest), with text translated in place and fonts preserved."
      tag: "Localisation · Scale"
    - headline: "iPad 13\" in landscape and portrait"
      body: "iPad Pro M4 device frame at 2064×2752, with native landscape support. The layout system is the same; only the aspect ratio changes."
      tag: "Device · iPad"
    - headline: "Mac 2880×1800, Studio Display crop"
      body: "Mac App Store screenshots in the exact 2880×1800 dimensions App Store Connect expects, with bezel options and shadow control."
      tag: "Device · Mac"
    - headline: "Apple Watch + Apple Vision Pro coverage"
      body: "The same source produces Watch 410×502 frames and visionOS 3840×2160 environment renders alongside the iPhone set."
      tag: "Device · Coverage"
    - headline: "Bulk upload to App Store Connect"
      body: "234 screenshots (6 sets × 39 locales) uploaded to the correct device and locale slots in App Store Connect in under two minutes, without opening a browser tab."
      tag: "Workflow · Upload"

features:
  - title: "3D Metal rendering engine"
    description: "Device frames are 3D models rendered with Apple's Metal framework instead of flat 2D PNG overlays. Output is deterministic, so your preview matches your export pixel for pixel."
  - title: "Localise across 39 App Store locales"
    description: "AI translation replaces text in place for every locale App Store Connect accepts, keeping fonts, positioning, and right-to-left scripts. Bring your own API key."
  - title: "Direct App Store Connect upload"
    description: "Mockly signs in through Apple's secure framework and sends each screenshot to the correct device size and locale slot. Credentials stay in Keychain and never pass through a Lagerland server."
  - title: "Percentage-based precision layout"
    description: "Position elements with percentage coordinates instead of pixels, and the layout holds across iPhone 6.9\" / 6.7\" / 6.5\" / 5.5\", iPad 13\" / 12.9\" / 11\", Mac 2880×1800, Apple Watch 410×502, and visionOS 3840×2160."
  - title: "Bulk import and smart templates"
    description: "Drop in a folder of raw screenshots organised by language and device, and Mockly puts each file in the right slot. Start from a template or build your own layout."
  - title: "Native Mac, sandboxed, on-device"
    description: "A native macOS app, not an Electron wrapper, and it is sandboxed, signed, and notarised. Your pre-release screenshots never leave your Mac for a third-party server. Apple's App Privacy nutrition label lists zero data collected."

screenshots:
  - src: "/assets/screenshots/mockly/1.webp"
    alt: "Mockly for Mac: App Store screenshots without the busywork, with a project of three artboards"
  - src: "/assets/screenshots/mockly/2.webp"
    alt: "Mockly localization view for designing once and shipping every language"
  - src: "/assets/screenshots/mockly/3.webp"
    alt: "Mockly real-time 3D device frame preview"
  - src: "/assets/screenshots/mockly/4.webp"
    alt: "Mockly AI translation of screenshot captions"
  - src: "/assets/screenshots/mockly/5.webp"
    alt: "Mockly one-click upload of screenshots to App Store Connect"
  - src: "/assets/screenshots/mockly/6.webp"
    alt: "Mockly made for indie developers who ship, with a five-star rating badge"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  app_privacy_label: "Apple's App Privacy nutrition label lists Mockly as collecting zero data. Pre-release screenshots, project files, and App Store Connect credentials never leave your Mac for a Lagerland server."
  notes:
    - "No analytics, no third-party trackers, no telemetry SDKs"
    - "No account required for the app itself; App Store Connect credentials are handled by Apple's frameworks and stored in Keychain"
    - "Pre-release screenshots and project files stored locally on your Mac"
    - "AI translation uses your own API key, called directly from your Mac, and translations never go through a Lagerland server"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Who built this"
  heading: "Made by a one-person studio."
  story: "Mockly is built by a single independent developer at Lagerland Apps, working from Finland since 2025. After years of shipping indie iOS apps, we found every credible screenshot tool was subscription-priced, web-based, or both. So Lagerland Apps built a native Mac one, with 3D Metal rendering, AI translation that runs on your own API key, and a direct App Store Connect uploader that keeps credentials in Keychain. Everything stays on your machine, because pre-release screenshots under NDA shouldn't go anywhere else."
  signals:
    - "Native macOS app: Metal-rendered, sandboxed, and notarised, with no Electron wrapper"
    - "App Privacy nutrition label lists zero data collected"
    - "No analytics SDKs, third-party trackers, or growth team; a one-person studio that plans to keep the app going for the long term"
    - "{APP_COUNT} live apps in the catalogue, all with the same privacy rules: no tracking, no ads, and no required accounts"
  external_link:
    label: "More apps from Lagerland Apps →"
    href: "/apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally, usually within a day."

release_notes:
  - date: "2026-04-05"
    note: "Localisation pass expanded to all 39 App Store Connect locales, including right-to-left support for Arabic and Hebrew."
  - date: "2026-03-12"
    note: "Direct App Store Connect upload: push every device size and locale with one button. Credentials are handled through Apple's Keychain framework."
  - date: "2026-02-24"
    note: "Percentage-based layout engine: position elements with % coordinates so layouts scale across every device class without per-resolution adjustment."
  - date: "2026-02-12"
    note: "AI translation engine with bring-your-own API key. Preserves fonts, positioning, and right-to-left scripts."
  - date: "2026-02-01"
    note: "Mockly 1.0: native macOS, 3D Metal device-frame rendering, bulk import, and professional templates."

faq:
  - q: "What is Mockly?"
    a: "Mockly is a native macOS app for making App Store screenshots with real 3D device frames rendered by Apple's Metal framework. It has percentage-based layouts that scale across every device size, AI translation into 39 App Store locales, and direct upload to App Store Connect. It all runs locally on your Mac, with no account and no server."
  - q: "How is Mockly different from other screenshot tools?"
    a: "Mockly is a native Mac app, so your pre-release screenshots never leave your machine, while most competitors are web apps. Its device frames are 3D models rendered in Metal instead of flat 2D PNG overlays. It costs {P_APP} once instead of $19 to $49 per month. And it uploads to App Store Connect directly, which skips the browser upload step every web competitor still needs."
  - q: "What sizes does Mockly export?"
    a: "Every size App Store Connect requires. iPhone: 6.9\" (1290×2868), 6.7\" (1290×2796), 6.5\" (1242×2688), 5.5\" (1242×2208). iPad: 13\" (2064×2752), 12.9\" (2048×2732), 11\" (1668×2388). Mac App Store: 2880×1800, 2560×1600, 1440×900, 1280×800. Apple Watch: 410×502, 396×484, 368×448. Apple TV: 1920×1080, 3840×2160. visionOS: 3840×2160. Positions are stored as percentages, so layouts scale on their own and one project produces every size."
  - q: "Does Mockly support all Apple App Store locales?"
    a: "Yes. Mockly supports all 39 locales App Store Connect accepts, including English (US, UK, AU, CA), Japanese, Simplified and Traditional Chinese, Korean, German, French (FR, CA), Spanish (ES, MX), Portuguese (PT, BR), Italian, Dutch, Polish, Czech, Slovak, Hungarian, Romanian, Russian, Turkish, Arabic, Hebrew, Greek, Swedish, Norwegian, Danish, Finnish, Indonesian, Malay, Thai, Vietnamese, Hindi, Ukrainian, Catalan, and Croatian. It handles right-to-left scripts (Arabic, Hebrew) natively."
  - q: "Can I localise screenshots for multiple languages?"
    a: "Yes. Mockly's AI translation localises overlaid text in place across the 39 App Store locales and keeps fonts, positioning, and right-to-left scripts. You bring your own API key, the calls go out from your Mac, and nothing passes through a Lagerland server. One project can hold and produce every locale."
  - q: "Is Mockly a subscription?"
    a: "No. Mockly is a one-time purchase at {P_APP}, with Family Sharing for up to six members. Subscription tools in this category charge $19 to $49 per month, or $228 to $588 a year. Mockly costs less than a single month of most of them, with no recurring fees and no features held back."
  - q: "Can I upload directly to App Store Connect?"
    a: "Yes. Mockly signs in to your App Store Connect account through Apple's secure framework, with credentials kept in macOS Keychain. It then sends each screenshot to the correct device size and locale slot in seconds, without a browser, manual file handling, or a third-party server."
  - q: "Does Mockly handle App Store Preview videos?"
    a: "No. Mockly only makes still screenshots, which most visitors see first on an App Store page. App Store Preview video is a separate format with its own recording, encoding, and submission requirements, and we chose to focus on screenshots."
  - q: "Does Mockly work with Fastlane?"
    a: "Mockly is a GUI alternative to Fastlane snapshot and frameit. If your team has Fastlane fully wired into CI/CD, you may not need Mockly. Most indie developers find Fastlane takes more setup than a tool that comes with templates and a direct upload pipeline. The two can also be used side by side."
  - q: "Does Mockly collect any data?"
    a: "No. Apple's App Privacy nutrition label lists Mockly as collecting zero data. The app has no analytics or telemetry SDKs and needs no account. All project files and pre-release screenshots stay on your Mac, and AI translation calls go straight from your machine using your own API key."
  - q: "How do Mockly screenshots comply with App Store Review Guidelines §2.3.3?"
    a: "App Store Review Guidelines §2.3.3 requires screenshots to show the app running on the device, not just illustrations, conceptual mockups, or pre-rendered marketing art that doesn't match how the app behaves. Mockly places your real captured screenshots inside a rendered 3D device frame, so the screen content is the actual app. Overlaid feature copy and background colours are fine under §2.3.3 as long as the screen itself shows the real app. Mockly's default templates stay compliant: text overlays, colour fields, and device frames around real UI captures, with no invented UI."
  - q: "How does Mockly compare to MockUPhone, LocaShot, Picasso, or AppMockUp?"
    a: "All four are web-based, each with a different focus. MockUPhone is a free device-mockup generator with no localisation or upload pipeline, so it suits one-off marketing images more than a production screenshot workflow. LocaShot specialises in AI screenshot localisation across 30+ languages but doesn't render 3D device frames the way Mockly does. Picasso emphasises bulk upload to App Store Connect and Google Play with a strong template library, subscription-priced. AppMockUp is a long-standing mockup generator focused on iPhone and a handful of Android devices. Mockly is the only native Mac option with real 3D Metal rendering, on-device translation against your own API key, direct ASC upload, and a one-time price. For a quick free mockup, use MockUPhone. For a SaaS tool with team features, use Picasso. For a native Mac app you buy once, use Mockly."

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
last_updated: 2026-10-26
---
Mockly is a native macOS tool for making App Store screenshots with real 3D device frames rendered by Apple's Metal framework. Rendering is deterministic (the on-screen preview matches the export pixel for pixel). It has percentage-based layout positioning that scales across every Apple device size (iPhone 6.9" through 5.5", iPad 13" through 11", Mac 2880×1800, Apple Watch 410×502, and visionOS 3840×2160), AI translation of text in place across 39 App Store Connect locales, multi-language screenshot management, bulk import from folders organised by language, professional templates, and direct upload to App Store Connect with credentials managed by Apple's Keychain. It is made for indie iOS, iPadOS, and macOS developers, studios, and ASO professionals who ship in several markets. Mockly is a one-time purchase at {P_APP} with Family Sharing, while subscription competitors in this category charge $19 to $49 per month. It has no tracking and no data collection, and it never uploads pre-release screenshots to a third-party server. Mockly was formerly called ScreenFlow Studio and was renamed in 2026.
