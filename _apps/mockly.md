---
layout: app
slug: mockly
name: "Mockly"
tagline: "Build, translate, and upload App Store screenshots on your Mac."
quick_answer: "Mockly is a Mac app for building App Store screenshots. You put your real screenshots on 3D iPhone, iPad, MacBook Pro, and Apple Watch models, add text and backgrounds, and keep all 50 App Store languages in one project, translated with AI through your own OpenAI, Anthropic, or Google key or through a CSV file. It exports exact-size PNG or HEIC files, or uploads the pages to App Store Connect with your API key. Mockly costs {P_APP} once, with no subscription, and runs on macOS 14 or later."
category: graphics
status: live
jump_nav: true

redirect_from:
  - /apps/screenflow-studio/
  - /apps/screenflow-studio/index.html

app_store_url: "https://apps.apple.com/app/id6756589122"

price:
  model: one-time-purchase

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple handles refunds through the standard App Store refund flow. Mockly is a one-time purchase and does not renew."

value_math:
  label: "What it costs."
  body: "Mockly is {P_APP} once, with no subscription, and every editor feature comes with the purchase. AI translation runs on your own OpenAI, Anthropic, or Google key, so your provider bills you for it directly."

icon: "/assets/icons/mockly.png"
og_image: "/assets/og/mockly.png"

seo:
  title: "App Store Screenshot Maker for Mac in 50 Languages: Mockly"
  description: "Make App Store screenshots on your Mac with 3D iPhone, iPad, MacBook, and Apple Watch models, in 50 languages, and upload them to App Store Connect."
  keywords:
    - app store screenshot maker for mac
    - app store screenshot generator
    - localize app store screenshots
    - app store screenshots in 50 languages
    - 3d device mockup mac
    - upload screenshots to app store connect
    - one-time purchase screenshot tool
    - indie developer screenshot tool

hero:
  device: mac
  pre_headline: "App Store screenshot maker for Mac"
  headline: "Design your App Store screenshots once, then ship them in 50 languages."
  secondary: "For indie Apple developers. One purchase, no subscription."
  subheadline: "Put your real screenshots on 3D iPhone, iPad, MacBook Pro, and Apple Watch models, write the captions once, and translate them with your own OpenAI, Anthropic, or Google key. When the set is ready, Mockly exports exact-size PNG or HEIC files or uploads the pages straight to App Store Connect."
  cta_label: "Get Mockly"
  alt: "Mockly on a Mac with three iPhone screenshot pages side by side, the Localizations list, and the artboard settings"

who_for:
  - "You're an indie iOS or macOS developer who makes your own App Store screenshots"
  - "You ship in several languages and want each language's text, screenshots, and layout in one project"
  - "You work with a translator and want the screenshot text as a CSV file you can hand over and import back"
  - "You already pay for OpenAI, Anthropic, or Google and want to translate captions with that key"
  - "You'd rather buy a screenshot tool once than subscribe to one"

who_not_for:
  - "You need App Store preview videos. Mockly makes still screenshots"
  - "You want to start from a library of ready-made templates. In Mockly you build each layout yourself"
  - "Your screenshots are captured and framed in CI with fastlane, and nobody opens a design tool"
  - "You work on Windows, the web, or an iPad. Mockly runs on a Mac only"
  - "You need to upload to Google Play. Mockly has a Google Play artboard size, but it uploads to App Store Connect only"

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
  - title: "Fifty App Store languages in one project"
    description: "Add any of the 50 App Store Connect languages and give each one its own text, screenshots, and images. A language follows your source language until you unlink it, so a long German headline or a different Japanese background changes that language and leaves the rest alone."
  - title: "Upload from the app"
    description: "Connect your App Store Connect API key, and Mockly lists your apps and versions, renders the pages, and uploads them for the languages you pick. The upload replaces the screenshots already in that display type, so check the set before you send it."
  - title: "Real 3D devices at any angle"
    description: "Six 3D models: iPhone 17 Pro Max, iPad Pro 11-inch and 12.9-inch, MacBook Pro 16-inch, Apple Watch Ultra, and Apple Watch Series 11. Turn each one on three axes and render it Realistic, Clay, or UI Only."
  - title: "Bought once"
    description: "Mockly is {P_APP} once, with no subscription. AI translation uses your own OpenAI, Anthropic, or Google key, and your provider bills you for it."

how_it_works:
  heading: "From a blank project to screenshots in App Store Connect."
  intro: "A Mockly project is a list of pages, one per screenshot, with every language inside it. A release goes through these steps."
  steps:
    - title: "Lay out the pages"
      detail: "Pick an artboard preset (iPhone 6.9-inch or 6.5-inch, iPad, Mac, Apple Watch, a landscape variant, or the 1080×1920 Google Play size) and add a page for each screenshot. Rename, duplicate, and drag pages into order in the sidebar."
    - title: "Put your screenshots on 3D devices"
      detail: "Add a device, drop in its screen image, and set its rotation on X, Y, and Z, its scale, and its offset. To fill every page in every language at once, link a folder of images named by language, page, and device (for example de_de_page2_1.png), and Mockly puts each file on the right device."
    - title: "Write and style the text"
      detail: "Add text blocks with a font from the bundled library, stroke, and shadow, then use Copy Style to repeat the look on other blocks and pages. Set a colour, gradient, or built-in background, including panoramic ones, and add image layers for logos and badges."
    - title: "Add languages and translate"
      detail: "Add languages from the list of 50 and choose your source language. Translate the text blocks with AI Translate using your own key (blocks marked Do not translate are skipped), or export a CSV for a translator and import it back. Unlink a language when it needs its own text size, image, or background."
    - title: "Export or upload"
      detail: "Save Images exports every page as PNG or HEIC at the artboard's exact pixel size, for the current language or all of them. Or open Upload to App Store Connect: Mockly reads the display type from the artboard and replaces that type's screenshots for the languages you choose."

example_insights:
  overline: "What one project holds"
  heading: "One project holds every page, device, and language."
  intro: "What a single Mockly project can hold and produce."
  cards:
    - headline: "50 languages from one source"
      body: "Choose a source language and add any of the 50 App Store Connect languages, or add them all at once. Each language can carry its own text, screenshots, and images."
      tag: "Localization"
    - headline: "Six 3D device models"
      body: "iPhone 17 Pro Max, iPad Pro 11-inch and 12.9-inch, MacBook Pro 16-inch, Apple Watch Ultra, and Apple Watch Series 11, each with its own screen image per language if you want one."
      tag: "Devices"
    - headline: "Three device styles"
      body: "Render any device Realistic, Clay, or UI Only, in perspective or orthographic projection, with adjustable light."
      tag: "Rendering"
    - headline: "A folder of screenshots, placed for you"
      body: "Link a folder of simulator screenshots named by language, page, and device, and each file lands on the right device on every page, in every language."
      tag: "Import"
    - headline: "Screenshot text as a CSV"
      body: "The Text Editing tab shows every text block in every language. Export CSV for a translator or an agency, then import the finished file."
      tag: "Translation"
    - headline: "Exact-size PNG or HEIC"
      body: "Save Images writes each page at the artboard's exact pixel size, for one language or all of them, with file names based on the language code."
      tag: "Export"

features:
  - title: "Upload to App Store Connect"
    description: "Add your App Store Connect API key (Key ID, Issuer ID, and .p8 file), pick an app and version, and Mockly uploads the rendered pages for the languages you choose. It shows the progress of each file and a list of results. Existing screenshots for that display type are replaced."
  - title: "50 App Store languages"
    description: "Add languages one by one, add them all, or search by name. The link-to-source switch in the Devices, Images, Background, and Text tabs keeps a language in step with your source language or frees it for its own layout."
  - title: "AI Translate with your own key"
    description: "Translate the text blocks on one page or on all pages into the languages you pick, using OpenAI, Anthropic, or Google, and choose the model for each provider in Settings. AI output is machine translation, so read it before you ship."
  - title: "3D devices, camera, and light"
    description: "Six 3D models of iPhone, iPad, MacBook Pro, and Apple Watch, with rotation on three axes, scale, offset, and three styles. Switch between perspective and orthographic projection, set the light, and let a device run past the edge of the artboard with Device Overflow."
  - title: "Text, images, and backgrounds"
    description: "Text blocks with fonts, weights, stroke, and shadow, plus Copy Style. Image layers sit in front of or behind the devices, with shadow, border, corner radius, and a different image per language if you need one. Backgrounds can be a colour, a gradient, or a built-in image."
  - title: "A native Mac app"
    description: "Mockly runs on macOS 14 or later, on Apple Silicon and Intel Macs. Projects are files you save and reopen from Finder, and editing and exporting work offline. The interface is in 10 languages, including German, French, Japanese, and Korean."

screenshots:
  - src: "/assets/screenshots/mockly/1.webp"
    alt: "Mockly on a MacBook with three iPhone screenshot pages, the Localizations list, and the artboard settings"
  - src: "/assets/screenshots/mockly/2.webp"
    alt: "Mockly showing the same three screenshot pages with German captions"
  - src: "/assets/screenshots/mockly/3.webp"
    alt: "Mockly canvas with three iPhone pages next to the camera, lighting, and device overflow settings"
  - src: "/assets/screenshots/mockly/4.webp"
    alt: "Mockly AI Translation sheet with the source language, the scope, and the target languages"
  - src: "/assets/screenshots/mockly/5.webp"
    alt: "Mockly App Store Connect upload panel asking for the Issuer ID, Key ID, and private key"
  - src: "/assets/screenshots/mockly/6.webp"
    alt: "Mockly app icon above the editor with three iPhone screenshot pages"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  app_privacy_label: "Lagerland Apps collects no data from Mockly. Your projects and settings stay on your Mac, and your keys are kept in its Keychain. When you translate, the text and your key go to the AI provider you chose. When you upload, the screenshots go to Apple."
  notes:
    - "Mockly needs no account and contains no analytics or tracking SDKs. Lagerland Apps runs no server for it"
    - "Projects are files saved where you choose on your Mac"
    - "AI keys and your App Store Connect key are stored in the macOS Keychain and sent only to the provider you select or to Apple"
    - "AI Translate sends the text of your text blocks and the target languages to the provider you chose, signed with your key"
    - "Upload to App Store Connect sends the rendered screenshots to Apple"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Who built this"
  heading: "Made by a one-person studio in Finland."
  story: "Mockly is made by Lagerland Apps, a one-person studio in Finland. Every release of an Apple app needs screenshots for each device size and each language, and doing that by hand means exporting files one at a time and dragging them into App Store Connect. Mockly keeps the whole set in one Mac project: the pages, the 3D devices, the text in 50 languages, and the upload. It needs no account, and Lagerland Apps runs no server for it."
  signals:
    - "Native Mac app for macOS 14 or later, on Apple Silicon and Intel"
    - "Works without an account, and Lagerland Apps collects no data from it"
    - "One-time purchase with no subscription"
    - "{APP_COUNT} live apps from the same studio, none with ads or tracking"
  external_link:
    label: "More apps from Lagerland Apps →"
    href: "/apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally, usually within a day."

release_notes:
  - date: "2026-08-15"
    note: "Choose the AI model for each provider in Settings, and translate with an OpenAI, Anthropic, or Google key. A failed translation now says why it failed."
  - date: "2026-06-30"
    note: "Image layers with a different image per language, Help & Feedback in Settings, and fixes for reopening saved projects and the save prompt."
  - date: "2026-05-18"
    note: "App Store Connect upload fixes: the correct iPhone 6.9-inch artboard size, clearer error messages, and reuse of existing screenshot sets."
  - date: "2026-04-26"
    note: "AI translation of text blocks, and a new app icon."
  - date: "2026-03-15"
    note: "Rebuilt from scratch, under the earlier name ScreenFlow Studio: 3D devices, per-language overrides, App Store Connect upload, and bundled fonts and backgrounds."

faq:
  - q: "What is Mockly?"
    a: "Mockly is a Mac app for making App Store screenshots. You place your real screenshots on 3D iPhone, iPad, MacBook Pro, and Apple Watch models, add text, images, and backgrounds, and keep up to 50 App Store languages in one project. It exports PNG or HEIC files at exact sizes or uploads the pages to App Store Connect. It costs {P_APP} once, with no subscription."
  - q: "How is Mockly different from other screenshot tools?"
    a: "Mockly is a Mac app you buy once. One project holds all 50 App Store languages, each with its own text, screenshots, and layout where you need it, and translation runs through your own AI key or a CSV file. The devices are 3D models you can turn on three axes. When the set is done, Mockly uploads it to App Store Connect with your API key, so you don't drag files into the browser."
  - q: "What sizes does Mockly export?"
    a: "Mockly has artboard presets for iPhone 6.9-inch and 6.5-inch, iPad, Mac, and Apple Watch, landscape variants, and a 1080×1920 Google Play size. Save Images exports every page as PNG or HEIC at the exact pixel size of the artboard you picked, for the current language or for all of them."
  - q: "Does Mockly support all App Store languages?"
    a: "Yes. Mockly lists the 50 App Store Connect languages. Add them one at a time, add them all at once, or search by name. Each language can have its own text, screenshots, images, and background, or follow your source language."
  - q: "Can I localize screenshots for multiple languages?"
    a: "Yes. Write the text once in your source language, then translate it with AI Translate using your own OpenAI, Anthropic, or Google key, or export a CSV for a translator and import it back. Text blocks marked Do not translate are skipped. If one language needs a different layout, unlink it from the source and change only that language."
  - q: "Is Mockly a subscription?"
    a: "No. Mockly is a one-time purchase at {P_APP}, and every editor feature comes with it. AI Translate uses your own OpenAI, Anthropic, or Google key, and your provider bills you for that use."
  - q: "Can I upload directly to App Store Connect?"
    a: "Yes. Add your App Store Connect API key (Key ID, Issuer ID, and .p8 file) in Settings. Mockly lists your apps and versions, reads the display type from the artboard, renders the pages, and uploads them for the languages you choose. It replaces the screenshots already in that display type, and it shows the progress of each file and a list of results."
  - q: "Where does Mockly store my API keys?"
    a: "In the macOS Keychain on your Mac. Your AI key is sent only to the provider you selected, because that provider needs it to answer the request. Your App Store Connect key is used only to sign requests to Apple. Lagerland Apps runs no server and never sees either key."
  - q: "Does Mockly handle App Store preview videos?"
    a: "No. Mockly makes still screenshots and exports them as PNG or HEIC. It has no video or PDF export."
  - q: "Does Mockly work with Fastlane?"
    a: "Mockly is a Mac app you work in by hand, and fastlane snapshot and frameit run from scripts. If your screenshots are captured and framed in CI, you may not need Mockly. If you capture with fastlane and design in Mockly, link the output folder in Mockly once the files follow its naming pattern of language, page, and device."
  - q: "Does Mockly run on Windows, iPhone, or iPad?"
    a: "No. Mockly is a Mac app for macOS 14 or later, on Apple Silicon and Intel Macs. It makes screenshots for iPhone, iPad, Mac, and Apple Watch listings, plus a Google Play size."
  - q: "Does Mockly collect any data?"
    a: "No. Mockly needs no account and has no analytics or tracking SDKs, and Lagerland Apps runs no server for it. Projects and settings stay on your Mac, and your keys are kept in its Keychain. Text leaves the Mac only when you run AI Translate, and it goes, with your key, to the provider you chose. Screenshots leave it only when you upload them to App Store Connect."
  - q: "How do Mockly screenshots comply with App Store Review Guidelines §2.3.3?"
    a: "Guideline 2.3.3 asks for screenshots that show the app in use, not only title art, a login page, or a splash screen. In Mockly the screen of each 3D device shows a screenshot you captured from your app, and your text and background sit around it. Whether a set passes review depends on what your screenshots show, and Mockly can't guarantee App Store approval."
  - q: "How does Mockly compare to MockUPhone, LocaShot, Picasso, or AppMockUp?"
    a: "Compare them on the points that matter for your release: where the tool runs, how it's priced, how many App Store languages it handles, and whether it uploads to App Store Connect. Mockly runs on a Mac, costs {P_APP} once with no subscription, holds all 50 App Store languages in one project, translates with your own AI key or a CSV file, renders 3D devices, and uploads to App Store Connect with your API key. Check each of the others on its own site, since features and prices change."

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
last_updated: 2026-10-29
---
Mockly is a Mac app for making App Store screenshots, for indie iOS and macOS developers and small studios who ship in several languages. A project is a list of pages, one per screenshot. You place your real screenshots on six 3D device models (iPhone 17 Pro Max, iPad Pro 11-inch and 12.9-inch, MacBook Pro 16-inch, Apple Watch Ultra, and Apple Watch Series 11), add text blocks, image layers, and backgrounds, and keep up to 50 App Store Connect languages in the same project. Each language can follow the source language or carry its own text, screenshots, and layout. Text is translated with AI Translate through your own OpenAI, Anthropic, or Google key, or through a CSV file you export and import. Mockly exports PNG or HEIC files at the exact artboard size and uploads the rendered pages to App Store Connect with your API key, replacing the screenshots already in that display type. It runs on macOS 14 or later, on Apple Silicon and Intel, needs no account, and costs {P_APP} once with no subscription. Mockly was first released as ScreenFlow Studio and renamed in 2026.
