---
layout: app
slug: clippet
name: "Clippet"
tagline: "A clipboard history for iPhone, iPad, and Mac that keeps every copy and finds it again."

# ── UNLISTED: PRE-LAUNCH ──────────────────────────────────────────────────────
# Clippet is not released yet. `status` is deliberately NOT "live": every listing
# on this site filters on `where: "status", "live"` (home, /apps/, llms.txt,
# llms-full.txt, ai-index.json, ai-sitemap.xml, footer, you-might-like,
# /lagerland-apps/, the /for/ hubs, the language hubs), so this page exists at
# its URL and appears nowhere else. `sitemap: false` keeps it out of
# sitemap.xml and `noindex: true` keeps it out of search results.
#
# The URLs are needed before release: the app links /apps/clippet/privacy/
# (purchase screen) and /apps/clippet/terms/ (Settings > About), and App Review
# opens them.
#
# ON LAUNCH: follow ~/Downloads/githubcode/CLIPPET-LAUNCH.md (outside the repo).
# In short: set status to "live", delete `sitemap: false` and `noindex: true`
# here and in every apps/clippet/* and de/apps/clippet/* page, set the release
# dates, add the transparency row, re-run the ASC sync, build, audit, push.
status: upcoming
sitemap: false
noindex: true
# ──────────────────────────────────────────────────────────────────────────────

quick_answer: "Clippet is a clipboard manager for iPhone, iPad, and Mac that keeps a searchable history of what you copy: text, links, images, videos, PDFs, audio, files, and code, each with its own preview. On the Mac it saves every copy in the background, even with its window closed. On iPhone and iPad it saves what you copied each time you open the app, because iOS doesn't let any app read the clipboard in the background. Smart Actions find phone numbers, addresses, dates, parcel and flight numbers, and one-time codes in your clips, on the device. Clips sync through your own iCloud with no account to create, and the app carries no ads or tracking. Clippet is free, and the free library shows your pinned clips and the last 30 days, with older clips kept, not deleted. Clippet Pro ({P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once) shows your whole history and adds boards, Quick Paste on ⌥⌘V on the Mac, your clips in the Clippet keyboard, and custom actions."
category: utilities
# Pre-launch only: MASTER.md marks iPhone, iPad and macOS as pending (⏳); the catalog lists live platforms only.
# Ignored once the catalog has them (_includes/app-facts.html). Delete on launch.
prelaunch_platforms: ["iOS", "iPadOS", "macOS"]

app_store_url: "https://apps.apple.com/app/id6829498729"

price:
  model: freemium
price_lead: "Free"
price_tier: "Clippet Pro"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Yearly starts with a {TRIAL} for new subscribers, which Apple offers only to eligible Apple Accounts. One purchase unlocks Clippet Pro on iPhone, iPad, and Mac, and all three plans work with Family Sharing. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew."

plans:
  - name: "Free"
    price: "$0"
    summary: "The full clipboard history, with your pinned clips and the last 30 days in view. Older clips stay saved."
    features:
      - "Automatic saving of all eight kinds of clip, plus the share sheet and Add Clip"
      - "Search, pins, tags, names, and full previews"
      - "Smart Actions and QR codes in screenshots"
      - "iCloud Sync and file backups"
      - "App Lock, skipped password-manager copies, and the card-number auto-delete offer"
      - "Home Screen, Lock Screen, and Mac desktop widgets"
      - "The Mac menu bar with your ten latest clips"
  - name: "Clippet Pro · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Every Pro feature, billed monthly."
    features:
      - "Your whole history in view, however old"
      - "Color-coded boards for projects, trips, and topics"
      - "Quick Paste on ⌥⌘V, pasting straight into other Mac apps"
      - "Your clips in the Clippet keyboard on iPhone and iPad"
      - "Custom actions: Translate, Reminder, Web Search, and more"
  - name: "Clippet Pro · Yearly"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "Every Pro feature, billed once a year, with a {TRIAL} for new subscribers. ~{SAVE_YEARLY}% cheaper than paying monthly."
    features:
      - "Everything in Clippet Pro · Monthly"
      - "{TRIAL} for new subscribers"
      - "Cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "Every Pro feature for one payment."
    features:
      - "Everything in Clippet Pro · Yearly"
      - "One-time purchase, no renewal"

icon: "/assets/icons/clippet.png"
og_image: "/assets/og/clippet.png"

seo:
  title: "Clippet: Clipboard Manager for iPhone, iPad & Mac"
  description: "Clipboard manager for iPhone, iPad, and Mac. Keeps text, links, images, PDFs, and code, syncs via your iCloud, and pastes with ⌥⌘V. No account."
  keywords:
    - clipboard manager iphone
    - clipboard manager mac
    - clipboard history mac
    - clipboard history iphone
    - copy paste history
    - clipboard app ipad
    - clipboard sync iphone mac
    - paste history mac shortcut
    - clipboard keyboard iphone
    - snippet manager mac
    - private clipboard manager
    - paste app alternative
    - maccy alternative

hero:
  pre_headline: "A clipboard manager for iPhone, iPad, and Mac."
  headline: "Everything you copy, kept."
  secondary: "Your clipboard forgets the last thing you copied the moment you copy something new. Clippet keeps it. On the Mac every copy is saved in the background, even with the window closed, and on iPhone and iPad Clippet saves what you copied each time you open it."
  subheadline: "Text, links, images, videos, PDFs, audio, files, and code each keep a full preview, and one search finds last week's copy. Clips sync through your own iCloud, and Smart Actions turn a copied address, tracking number, or one-time code into a single tap."
  cta_label: "Download Free"
  alt: "Clippet's clipboard history on iPhone, with pinned and recent clips"

screenshots:
  - src: "/assets/screenshots/clippet/1.webp"
    alt: "Clippet library on iPhone with pinned clips, a text, a link, and a photo"
  - src: "/assets/screenshots/clippet/2.webp"
    alt: "Clippet Smart Actions offering Open in Maps, Call, Add to Contacts, and Add to Calendar for a copied text"
  - src: "/assets/screenshots/clippet/3.webp"
    alt: "Clippet image clip in full with its dimensions, size, and a Save to Photos button"
  - src: "/assets/screenshots/clippet/4.webp"
    alt: "Clippet search results for a copied invoice, with matches highlighted"
  - src: "/assets/screenshots/clippet/5.webp"
    alt: "Clippet board named Lisbon Trip holding an address, a photo, a link, and a flight"
  - src: "/assets/screenshots/clippet/6.webp"
    alt: "Clippet Auto-Delete sheet setting a clip to delete itself on a chosen date"
  - src: "/assets/screenshots/clippet/7.webp"
    alt: "Clippet code clip in syntax colors with a Copy as Plain Text button"
  - src: "/assets/screenshots/clippet/8.webp"
    alt: "Clippet app icon with its features listed: pins, boards, tags, custom names, auto-delete, QR codes, widgets, search, and dark mode"

who_for:
  - "You copy on your iPhone and need the same thing on your Mac a minute later"
  - "You work from the Mac keyboard and want last hour's copy one shortcut away"
  - "You copy addresses, phone numbers, tracking and flight numbers, dates, and codes, and want to act on them without retyping"
  - "You're a developer who copies snippets and wants them back in syntax colors, or as plain text"
  - "You collect links, screenshots, and documents for later and want them sorted by project"
  - "You want a clipboard history with no account, no ads, and a lock on it"

who_not_for:
  - "You want your iPhone to save copies in the background (iOS doesn't allow it for any app; Clippet saves when you open it)"
  - "You need a password manager or an encrypted vault"
  - "You need to search text inside images"
  - "You need Android, Windows, or a web app"
  - "You want to share one clipboard with a team"

alternatives_to:
  - "Paste"
  - "Maccy"
  - "Pastebot"
  - "Raycast"
  - "CopyClip"
  - "Flycut"
  - "Clipy"

comparison_table:
  intro: "Each row answers a question people ask when choosing a clipboard manager. Paste is the closest match, with apps for iPhone, iPad, and Mac. Maccy and Pastebot are Mac-only, and both do that job well. Clippet fits if you want one free app on all three devices, synced through your own iCloud, that also acts on the addresses, dates, and codes you copy."
  competitors: ["Clippet", "Paste", "Maccy", "Pastebot"]
  rows:
    - feature: "Runs on iPhone, iPad, and Mac"
      values: ["Yes, one app", "Yes", "Mac only", "Mac only"]
    - feature: "Sync between devices"
      values: ["Your own iCloud, free", "Your own iCloud", "No, stays on the Mac", "iCloud, between Macs"]
    - feature: "Keyboard for pasting clips on iPhone"
      values: ["Yes, the clip list with Clippet Pro", "Yes, Paste Keyboard", "No iPhone app", "No iPhone app"]
    - feature: "Global paste shortcut on Mac"
      values: ["⌥⌘V Quick Paste (Clippet Pro)", "⇧⌘V", "⇧⌘C", "⇧⌘V"]
    - feature: "Collections"
      values: ["Boards (Clippet Pro), free pins and tags", "Pinboards", "Pins", "Custom and Smart Pastebins"]
    - feature: "Leaves out password-manager copies"
      values: ["Yes, copies marked private", "Yes, Ignore confidential content", "Yes, by default", "Per-app blacklist"]
    - feature: "How you pay"
      values: ["Free; Clippet Pro monthly, yearly, or lifetime", "Free trial, then subscription or lifetime", "Free, or a one-time App Store purchase", "One-time direct, or subscription on the App Store"]
    - feature: "Analytics data on the App Store privacy label"
      values: ["None, the app has no analytics code", "Usage data and diagnostics", "Data Not Collected", "Data Not Collected"]
  footnote: "Competitor features, pricing models, and privacy labels come from each app's website and App Store page, checked on 2026-11-05. Apps change often, so check the App Store before you switch."

value_points:
  - title: "Every kind of copy, with a preview"
    description: "Clippet keeps eight kinds of clip: text, links, images, videos, PDFs, audio, files, and code. A link shows its page title and image, a PDF its first page, and code its language in syntax colors. Copy the same thing twice and you still have one clip."
  - title: "It reads what you copied"
    description: "Smart Actions find phone numbers, addresses, dates, parcel and flight numbers, and one-time codes, and offer Call, Open in Maps, Add to Calendar, Track Package, or Copy Code. Copy a screenshot with a QR code and Clippet shows the link inside it. Detection runs on your device."
  - title: "Built for the Mac keyboard"
    description: "Clippet sits in the menu bar with your ten latest clips and keeps saving after you close its window. With Clippet Pro, ⌥⌘V opens Quick Paste over any app. Search, pick a clip, and with your permission it lands where you were typing."
  - title: "Private by design"
    description: "Clippet needs no account and carries no ads or analytics code. Copies that password managers mark as private are never saved. A copied card number is flagged with an offer to delete it after 30 minutes, and App Lock keeps the whole app behind Face ID, Touch ID, or Optic ID."

how_it_works:
  heading: "From copy to paste, and what happens in between"
  intro: "You copy the way you always have. Clippet keeps the copy, helps you find it, and puts it back where you need it."
  steps:
    - title: "Copy as usual"
      detail: "On the Mac, Clippet saves every copy while it runs, from the menu bar too. On iPhone and iPad it saves your newest copy each time you open the app; set Paste from Other Apps to Allow and iOS stops asking. The Latest Clip widget's Paste Last Copy button and the Clippet keyboard's Save button save a copy without opening the library. The share sheet sends anything to Clippet from any app."
    - title: "Find it again"
      detail: "Search reads the text, names, tags, link titles, and file names of every clip, ignores case and accents, and highlights what matched. Browse by type, pin the clips you reuse, and name the ones you'll want later. Search doesn't read text inside images."
    - title: "Act on it"
      detail: "Open a clip and Smart Actions suggest what to do with it: call the number, map the address, add the date to your calendar, or track the parcel. With Clippet Pro you can add your own action to any clip, such as a translation, a reminder, or a web search."
    - title: "Paste it where you need it"
      detail: "On the Mac, pick a clip in the menu bar to copy it, or press ⌥⌘V for Quick Paste (Clippet Pro). On iPhone and iPad, switch to the Clippet keyboard in any app and tap a clip to type it in; the clip list is Clippet Pro, and the keyboard's typing keys and Save stay free."
    - title: "Let it tidy itself"
      detail: "Set any clip to delete itself after 15 minutes, an hour, a day, or on a date, and its card counts down. Keep History clears clips you haven't used in 24 hours, 7 days, or 30 days, or keeps them forever. Pinned clips and clips on a board always stay. On iPhone and iPad a clip leaves the next time you open Clippet."

features:
  - title: "Eight kinds of clip"
    description: "Text, links, images, videos, PDFs, audio, files, and code, each sorted on its own. Code is recognized as JSON, Swift, Python, JavaScript, HTML, CSS, SQL, or Shell Script. Choose which kinds to keep in Types to Save, and copy several things at once to get one clip for each."
  - title: "Search that reads every clip"
    description: "One field searches text, names, tags, link titles and addresses, file names, and board names. Matches are highlighted, pinned matches come first, and your last five searches are one tap away. Text inside images isn't searched."
  - title: "Smart Actions"
    description: "Phone numbers, email and postal addresses, dates, flight and parcel numbers (UPS, FedEx, USPS, DHL), one-time codes, QR codes, and business cards in images. Each comes with a one-tap action, found on your device. Clippet Pro adds custom actions, up to 20 per clip."
  - title: "Pins, boards, tags, and names"
    description: "Pin as many clips as you like to keep them at the top, free. Give a clip a name or tags so search finds it. With Clippet Pro, sort clips onto boards in eight colors, one for each project or trip."
  - title: "The Mac menu bar and Quick Paste"
    description: "Your ten latest clips are one click away in the menu bar, and Clippet can open at login. With Clippet Pro, ⌥⌘V opens Quick Paste over any app with search, type filters, and your 30 latest clips; ⏎ pastes, ⌘⏎ pastes as plain text. Pasting straight into another app needs macOS's Accessibility permission."
  - title: "The Clippet keyboard"
    description: "On iPhone and iPad, switch to the Clippet keyboard in any app. Tap a text, link, or code clip to type it in, or a picture or file to copy it. The clip list is Clippet Pro; the typing keys and Save, which keeps the text you just copied, are free. Showing clips needs Allow Full Access, and the keyboard makes no network requests."
  - title: "Widgets"
    description: "Latest Clip and Pinned Clips on the iPhone and iPad Home Screen and the Mac desktop, a Lock Screen widget on iPhone and iPad, and a Quick Add button that opens Add Clip. The widget's Paste Last Copy button saves what you just copied. With App Lock on, the widgets show no clips."
  - title: "iCloud Sync and backups"
    description: "Clips, boards, tags, and names sync across iPhone, iPad, and Mac through your own private iCloud database, with a status dot on every card. Create Backup saves your library to a file you keep; restore it by merging or replacing."
  - title: "App Lock and privacy controls"
    description: "Lock Clippet with Face ID, Touch ID, Optic ID, or your passcode, and choose how soon it locks again. On the Mac it also locks when the Mac sleeps or locks its screen. Hide your clips in the app switcher, and turn off link previews so Clippet never contacts a copied link's website."
  - title: "Drop to save on iPad and Mac"
    description: "Drop text, links, images, or files onto Clippet to save them, or onto a board to file them there. On the Mac every clip remembers the app you copied it from, and full menus and shortcuts drive the library: ⌘F to search, ⌘N to add, ⌘1 to ⌘9 to switch type."

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No account, no ads, no analytics, and no third-party code"
    - "Clips stay on your devices and sync only through your own private iCloud, which Lagerland Apps cannot read; iCloud Sync can be turned off"
    - "Copies that password managers mark as private are skipped before anything is read"
    - "Saving a link fetches its title and image from that website; turn off Fetch Link Previews and Clippet never contacts it"
    - "The keyboard and the widgets make no network requests"

faq:
  - q: "What is Clippet?"
    a: "Clippet is a clipboard manager for iPhone, iPad, and Mac. It keeps a history of what you copy (text, links, images, videos, PDFs, audio, files, and code) with a preview of each, lets you search, pin, tag, and name your clips, and finds phone numbers, addresses, dates, and codes inside them. Clips sync through your own iCloud, and there's no account."
  - q: "Does Clippet save my clipboard in the background on iPhone?"
    a: "No. iOS doesn't let any app read the clipboard in the background, so on iPhone and iPad Clippet saves your newest copy each time you open it. Set Paste from Other Apps to Allow for Clippet and it saves without asking. You can also save a copy without opening the library: tap Paste Last Copy on the Latest Clip widget, tap Save in the Clippet keyboard, or send anything to Clippet from the share sheet. On the Mac, Clippet saves every copy in the background while it runs."
  - q: "Does Clippet sync between iPhone and Mac?"
    a: "Yes, for free. iCloud Sync keeps your clips, boards, tags, and names in step across iPhone, iPad, and Mac through your own private iCloud database. Lagerland Apps has no server and can't read your clips. Turning sync on or off takes effect the next time the app starts."
  - q: "How do I paste from my clipboard history on Mac?"
    a: "Choose any of your ten latest clips in Clippet's menu bar to copy it, then press ⌘V. With Clippet Pro, press ⌥⌘V in any app to open Quick Paste: search or pick one of your 30 latest clips and press ⏎ to paste it, or ⌘⏎ to paste it as plain text. Pasting straight into the app needs macOS's Accessibility permission; without it, Clippet copies the clip and you press ⌘V. You can change the shortcut in Settings."
  - q: "How do I paste a saved clip on iPhone?"
    a: "Open the clip in Clippet and tap Copy, then paste as usual. With Clippet Pro you can skip the trip: switch to the Clippet keyboard in any app and tap a text, link, or code clip to type it where you're typing. A picture or file clip is copied, up to 8 MB, for you to paste. The keyboard needs Allow Full Access to show your clips."
  - q: "Is Clippet free?"
    a: "Yes. Clippet is free to download, and the free version saves all eight kinds of clip, syncs through iCloud, and includes search, pins, tags, Smart Actions, App Lock, widgets, and the Mac menu bar. The free library shows your pinned clips and the last 30 days. Clippet Pro adds your whole history, boards, Quick Paste on the Mac, your clips in the Clippet keyboard, and custom actions for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once. Prices in USD; the App Store shows your local currency at checkout."
  - q: "What happens to clips older than 30 days without Clippet Pro?"
    a: "They stay saved, on your device, in iCloud, and in your backups, and come back into view with Clippet Pro. Without Pro they're hidden from the library, search, and widgets. Pinned clips always show, however old, and pins are free and unlimited. Nothing is deleted because Pro ended; Keep History deletes only what you tell it to."
  - q: "Does Clippet save passwords I copy?"
    a: "Not when the password manager marks the copy as private, which is how password managers flag the passwords they copy. Clippet skips those copies before reading them; a copy that isn't marked is saved like any other. It also recognizes a copied payment card number and offers to delete that clip after 30 minutes, or another time you set. Clippet isn't a password manager or an encrypted vault, so keep passwords where they belong."
  - q: "Is Clippet private?"
    a: "Clippet needs no account and contains no ads, analytics, or third-party code, and Lagerland Apps runs no server for it. Your clips stay on your devices and in your own private iCloud. One thing does go out: when you save a link, Clippet asks that website for its title and image, the way a browser would. Turn off Fetch Link Previews in Settings and it never does."
  - q: "Can I lock Clippet?"
    a: "Yes, for free. App Lock puts Clippet behind Face ID, Touch ID, Optic ID, or your device passcode (your login password on a Mac), and locks immediately, after 1 minute, or after 5 minutes. On the Mac it also locks when the Mac sleeps or locks its screen. Copies are still saved while it's locked, and the widgets show no clips."
  - q: "Is the Mac version a separate purchase?"
    a: "No. Clippet is free on iPhone, iPad, and Mac, and one Clippet Pro purchase unlocks Pro on all of them for the same Apple Account. Monthly, Yearly, and Lifetime all work with Family Sharing."
  - q: "Can I back up my clips?"
    a: "Yes. Create Backup saves your clips, boards, and tags to a file wherever you choose, iCloud Drive included, and Restore from Backup merges it into your library or replaces the library with it. The file isn't encrypted, so clips holding a card number are left out of it."
  - q: "What do I need to run Clippet?"
    a: "iOS 26 or later on iPhone, iPadOS 26 or later on iPad, and macOS 26 or later on the Mac. Clippet works offline; iCloud Sync catches up when you're back online."
  - q: "Is Clippet available in other languages?"
    a: "Yes. Clippet's interface is translated into 40 languages, including German, French, Spanish, Japanese, Chinese, Arabic, and Hebrew."

related_apps: ["mediakit", "taskful-day", "mockly"]

support:
  email: "support@lagerland.app"
  url: "/apps/clippet/support/"

release:
  first_release: "2026-11-05"
  last_updated: "2026-11-05"
  version: "1.0"

show_body: true
about_heading: "What Clippet is: a clipboard that remembers"
last_updated: 2026-11-05
---
Clippet is a clipboard manager for iPhone, iPad, and Mac. Your clipboard holds one thing at a time, so every new copy erases the one before it. Clippet keeps them all: text, links, images, videos, PDFs, audio, files, and code, each with a preview you can open in full.

On the Mac it runs from the menu bar and saves every copy in the background. On iPhone and iPad, where iOS doesn't let apps read the clipboard in the background, it saves your newest copy each time you open it, and the Latest Clip widget and the Clippet keyboard save one without opening the library. Search reads every clip, Smart Actions turn an address, a date, or a tracking number into one tap, and iCloud Sync keeps your clips in step across your devices through your own iCloud.

Clippet is free. Clippet Pro shows your whole history and adds boards, Quick Paste on ⌥⌘V, your clips in the Clippet keyboard, and custom actions, as a subscription or a one-time purchase. It works without an account, and it carries no ads or tracking.
