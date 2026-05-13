---
layout: app
slug: rightsplit
name: "RightSplit"
tagline: "Split bills from receipts."
quick_answer: "RightSplit is a receipt-scanning bill splitter for iPhone. Snap a photo of any restaurant or bar receipt, assign each item to the person who ordered it, split shared dishes, add tip, and send everyone their total via iMessage or WhatsApp. Free; Pro is $1.99/year or $7.99 lifetime. No ads, no account, no tracking — receipts read on-device with Apple's Vision framework."
category: finance
platforms: ["iOS"]
status: live

app_store_url: "https://apps.apple.com/app/id6757268612"

price:
  model: freemium
  value: "Free — Pro from $1.99/yr"
schema_price: "0"
schema_high_price: "7.99"
schema_offer_count: "3"

icon: "/assets/icons/rightsplit.png"
og_image: "/assets/og/rightsplit.png"

seo:
  title: "Bill Splitter for iPhone — Scan, Split, Send | RightSplit"
  description: "Scan a receipt on iPhone. Item-by-item splits, shared dishes, fair tip math, send via iMessage or WhatsApp. No account. Free; Pro $1.99/yr or $7.99 lifetime."
  keywords:
    - bill splitter app
    - receipt scanner splitter
    - split restaurant bill app
    - split bill with friends
    - group expense splitter
    - receipt bill split
    - tip calculator splitter
    - dinner bill divider
    - fair bill splitting app
    - split shared expenses
    - scan receipt split bill
    - restaurant bill calculator

hero:
  headline: "Bill splitter for iPhone."
  secondary: "Scan it. Split it. Done."
  subheadline: "You ordered the $14 salad. You paid for someone's $48 steak. RightSplit scans the receipt, reads every line item, and calculates exactly what each person owes — including shared bottles and tip — in under sixty seconds. iMessage or WhatsApp the totals. No account, no sign-up."
  pre_headline: "Free forever for equal splits and tip calc. Pro unlocks item-by-item fairness — $1.99/year, or $7.99 once and you own it. No subscription trap. No card on file just to try it."
  cta_label: "Download Free"
  alt: "RightSplit on iPhone — restaurant receipt items being assigned per person with tip calculated"

who_for:
  - "You split restaurant bills with friends who ordered different things"
  - "You share rent, utilities, or groceries with roommates and want fair per-item math"
  - "You travel in groups and need to settle bills without awkward maths at the table"
  - "You'd rather scan a receipt than type 12 line items manually"
  - "You refuse to create another account just to split one dinner"

who_not_for:
  - "You want long-running group ledgers with multi-month settlements (use Splitwise)"
  - "You need business expense reports or reimbursement workflows"
  - "You always split evenly and a calculator is faster"

alternatives_to:
  - "Splitwise"
  - "Tricount"
  - "Settle Up"
  - "Tab"
  - "Venmo split"

value_points:
  - title: "Scan, don't type"
    description: "Snap a photo of the receipt. RightSplit detects items automatically. No manual entry, no squinting at numbers, no math."
  - title: "Split by what people ordered"
    description: "Assign items to the people who ordered them. Shared a bottle? Split that item between the group. Everyone pays exactly what's fair."
  - title: "Tip and send instantly"
    description: "Add tip with rounding, then share everyone's total via text, WhatsApp, or copy. From photo to payment request in under a minute."
  - title: "No ads, no account"
    description: "Free, clean, and private. No tracking, no data selling, no sign-up required."

features:
  - title: "Instant receipt scanning"
    description: "Point your camera at a receipt and RightSplit reads it. Items, prices, and totals are detected automatically — no manual data entry. Works with restaurant receipts, bar tabs, and grocery bills."
  - title: "Item-level fairness"
    description: "Assign each item to the person who ordered it. Split shared dishes, bottles, and appetizers between multiple people. No more equal splits when someone ordered lobster and you had a salad."
  - title: "Smart tip calculation"
    description: "Add a percentage tip and RightSplit distributes it proportionally based on what each person ordered. Fair rounding ensures the numbers add up cleanly."
  - title: "Send in seconds"
    description: "Share each person's total via text message, WhatsApp, or copy the summary to paste anywhere. From receipt photo to payment request in under 60 seconds."
  - title: "Split history"
    description: "Pro keeps a record of past splits. Look up who owed what, settle disputes, or reference old totals without re-scanning."

plans:
  - name: "Free"
    price: "$0 forever"
    summary: "Equal splits, tip calculator, share via iMessage or WhatsApp."
    features:
      - "Scan receipts with on-device OCR"
      - "Equal splitting between any number of people"
      - "Tip calculator with fair rounding"
      - "Share totals via iMessage or WhatsApp"
      - "No account, no tracking, no ads"
  - name: "Pro · yearly"
    price: "$1.99 / year"
    summary: "Item-by-item splitting — what most people install RightSplit for."
    features:
      - "Everything in Free"
      - "Item-level fairness — assign each line to who ordered it"
      - "Split shared dishes proportionally"
      - "Per-person tip breakdown"
      - "Split history"
      - "Cancel anytime — no penalty"
  - name: "Pro · lifetime"
    highlight: true
    price: "$7.99 once"
    summary: "Most chosen. Pay once, own it forever — about four years of yearly for the price of two."
    features:
      - "Everything in Pro yearly"
      - "One purchase, no recurring charge"
      - "All future feature updates"
      - "No card on file after the App Store buy"

how_it_works:
  intro: "From receipt photo to payment request in under sixty seconds — no manual entry, no account required, no upload."
  steps:
    - title: "Point the camera at the receipt"
      detail: "Apple's on-device Vision framework (VNRecognizeTextRequest) reads every line item, price, and total. Works on thermal restaurant receipts, bar tabs, printed bills, and photographs of digital receipts. Nothing is uploaded — the receipt image stays on the phone."
    - title: "Tap items to assign them"
      detail: "Each line item gets tagged to the person who ordered it. Shared bottles and appetizers split proportionally between the people who actually shared them, not equally across the whole table."
    - title: "Add tip"
      detail: "Choose a tip percentage. RightSplit distributes the tip proportionally across each person's subtotal — so the person who ordered the $14 salad pays a fair share of tip, not the same as the person who ordered the $48 steak. Fair rounding ensures the totals add up to the penny."
    - title: "Send everyone their part"
      detail: "Tap Share. Each person gets a clean line via iMessage, WhatsApp, or copy-paste — 'You owe $23.40: salad, glass of wine, share of bottle, tip.' From scan to settled in under a minute."

plateau_disclosure:
  title: "How RightSplit calculates fair tips, splits, and rounding"
  rule: "Each person's subtotal is the sum of the items they ordered plus their proportional share of any shared items (a bottle split four ways is 25% to each person who shared it). Their tip is calculated as (their subtotal ÷ total subtotal) × the tip amount you chose — so the person who ordered the $14 salad pays a smaller share of the tip than the person who ordered the $48 steak. Final per-person totals are rounded to the nearest cent with a fairness pass: if rounding leaves a one-cent gap, RightSplit assigns the cent to the highest subtotal, never charging a person more than their share rounded up."
  what_it_does_not_do: "It does not round each person's tip down (which would silently under-collect the total), apply a uniform tip across diners (which is mathematically just equal-splitting in disguise), or 'distribute' a service charge that's already printed on the receipt (RightSplit reads the printed total — if your receipt includes service, that's the number it works from)."
  notes:
    - "Tax handling matches the receipt: tax-exclusive receipts (US standard) distribute tax proportionally; tax-inclusive receipts (EU/UK VAT) use the printed line totals directly."
    - "If you tap a line item to correct a mis-read, the corrected value flows through the splits and tip math immediately — no need to re-scan."
    - "All math runs on-device. No prices, totals, or contact data are uploaded — receipt OCR is Apple's on-device Vision framework."

training_vocabulary:
  overline: "Speaks the language"
  heading: "Built for people who actually want to look at the math"
  intro: "RightSplit shows its work — every value on screen is something you can verify against the original receipt photo."
  collapse_by_default: true
  groups:
    - heading: "Receipt formats"
      items:
        - "Thermal receipts — the classic restaurant printout (most common, scans best)"
        - "Electronic / digital receipts — emailed PDFs, screenshots of mobile receipts"
        - "Bar tabs and itemised counters — taproom totals with abbreviated item names"
        - "Photo of a screen — when a server shows you the bill on a tablet"
        - "Faded or wrinkled receipts — OCR works best on flat, well-lit shots"
    - heading: "Tip conventions"
      items:
        - "United States: 18–22% expected, applied to pre-tax subtotal in most states"
        - "United Kingdom: 12.5% service charge often included on the bill itself"
        - "Continental Europe: service usually included; small rounding-up tip optional"
        - "Japan / South Korea: no tipping — the line is omitted entirely"
        - "RightSplit handles all of the above: pick the tip percentage or set it to 0"
    - heading: "Bill math"
      items:
        - "Equal split — divide total by N people (the math RightSplit Free does)"
        - "Item-based split — each person pays for what they ordered (the Pro feature)"
        - "Proportional tip — tip distributed by share of subtotal, not by headcount"
        - "Fair rounding — sub-cent gaps assigned to highest subtotal, never short"
        - "VAT / tax-inclusive vs tax-exclusive math — handled per-receipt"
    - heading: "Languages &amp; currency"
      items:
        - "Apple Vision framework recognizes text in 18+ languages on-device"
        - "Reads currency symbols ($, €, £, ¥, ₩, ₹, etc.) as printed"
        - "No live currency conversion — splits stay in the receipt's currency"
        - "Decimal separators: handles both 1,234.56 (US) and 1.234,56 (EU) formats"

comparison_table:
  intro: "RightSplit versus the three most-searched bill splitters on the things people actually pick a tool for: how you pay for it, what you trade away to use it, and whether everyone at the table needs to install something."
  competitors:
    - "RightSplit"
    - "Splitwise"
    - "Tab"
    - "Tricount"
  rows:
    - feature: "Pricing"
      values:
        - "Free + $1.99/yr or $7.99 lifetime"
        - "Free + Pro subscription"
        - "Free"
        - "Free + Pro subscription"
    - feature: "Account required"
      values:
        - "No"
        - "Yes — for sync, social, ledgers"
        - "No"
        - "Optional"
    - feature: "Receipt OCR"
      values:
        - "On-device (Apple Vision)"
        - "Pro tier only, cloud OCR"
        - "Photo-tap, no OCR"
        - "Manual entry"
    - feature: "Item-level splitting"
      values:
        - "Pro tier"
        - "Manual via uneven splits"
        - "Yes"
        - "Manual via uneven splits"
    - feature: "Does the other person need to install the app?"
      values:
        - "No — share total as text"
        - "Yes — group requires sign-in"
        - "No"
        - "Yes — for group balance view"
    - feature: "Long-running group ledger"
      values:
        - "No — single-bill workflow"
        - "Yes — core feature"
        - "No"
        - "Yes"
    - feature: "Third-party tracking"
      values:
        - "None"
        - "Standard analytics"
        - "Standard analytics"
        - "Standard analytics"
    - feature: "Works fully offline"
      values:
        - "Yes (share needs network)"
        - "Limited"
        - "Yes"
        - "Limited"
  footnote: "Competitor details reflect publicly documented features as of 2026. Splitwise is the right tool for ongoing group balances; RightSplit is the right tool for the single-bill workflow."

screenshots:
  - src: "/assets/screenshots/rightsplit/1.png"
    alt: "RightSplit receipt scanner on iPhone — Apple Vision framework reading every line item and total from a restaurant receipt"
  - src: "/assets/screenshots/rightsplit/2.png"
    alt: "RightSplit item assignment screen — tap each line item to the person who ordered it; shared dishes split proportionally between selected people"
  - src: "/assets/screenshots/rightsplit/3.png"
    alt: "RightSplit tip calculator — percentage tip distributed proportionally across each person's subtotal with fair rounding so totals add up cleanly"
  - src: "/assets/screenshots/rightsplit/4.png"
    alt: "RightSplit share sheet on iPhone — send each person their formatted total via iMessage, WhatsApp, or copy to paste anywhere"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no tracking, no data selling"
    - "No account or sign-up required"
    - "Receipt and bill data stored locally on your device"
    - "Contact access used only when you choose to add friends"

faq:
  - q: "What is RightSplit?"
    a: "RightSplit is a bill splitting app for iPhone that scans receipts, detects items automatically, and calculates what each person owes — including shared dishes, tip, and rounding. Share payment requests instantly via iMessage or WhatsApp. Free; Pro unlocks item-based splitting at $1.99/year or $7.99 lifetime."
  - q: "How does the receipt scanner work?"
    a: "Take a photo of your receipt and RightSplit reads the items and prices automatically using Apple's on-device Vision framework (the same OCR Apple uses for Live Text). No manual typing required — it detects line items, totals, and tax. The receipt image never leaves your phone."
  - q: "Which OCR engine does RightSplit use?"
    a: "Apple's Vision framework — specifically VNRecognizeTextRequest — running entirely on-device. That means three things: receipts work offline; receipt images are never uploaded to a server; and the OCR quality is whatever Apple ships in the current iOS release, improving with every Apple update."
  - q: "How accurate is the receipt scan?"
    a: "Accuracy depends on the receipt. Standard thermal restaurant receipts and clean printed bills read reliably. Faded receipts, very wrinkled paper, or photographs taken at a sharp angle can mis-read individual line items — in which case you can tap any item to correct the price or description before assigning. RightSplit always shows the parsed total alongside the original receipt photo so you can sanity-check it before splitting."
  - q: "Can I split shared dishes?"
    a: "Yes. Any item can be split between multiple people — bottles, appetizers, shared plates. Each person's share is calculated proportionally, including their share of the tip on that item."
  - q: "How do I send people their share?"
    a: "After splitting, tap to share via iMessage, WhatsApp, or copy the summary to paste into any app. Each person gets a clear line — 'You owe $23.40: salad, glass of wine, share of bottle, tip.' Nothing to install on the other person's phone."
  - q: "Is RightSplit free?"
    a: "Yes. Equal splitting and the tip calculator are free forever. Pro unlocks item-based splitting (the headline feature), uneven splits, per-person tip breakdown, and split history — $1.99 per year, or $7.99 once and you own it. There's no card on file to start, and no auto-renew on the lifetime tier."
  - q: "Does RightSplit need an account?"
    a: "No. RightSplit works immediately with no sign-up, no account, and no personal information required. Only one person at the table needs the app — you scan, split, and send everyone their total."
  - q: "Does RightSplit store my receipts online?"
    a: "No. All receipt and bill data stays on your device. RightSplit has no servers, no cloud storage, no advertising SDKs, and no third-party analytics. Receipt OCR runs on-device with Apple's Vision framework — the photo never leaves your phone."
  - q: "Does RightSplit work offline?"
    a: "Yes. The entire scan-split-share workflow works without internet. Receipt OCR is on-device. The only step that needs a connection is the final share — iMessage and WhatsApp obviously need network, but you can also copy the summary and send it later."
  - q: "What languages does the receipt scanner read?"
    a: "Apple's Vision framework supports text recognition in 18+ languages, including English, Spanish, French, Italian, German, Portuguese, Chinese (Simplified & Traditional), Japanese, Korean, Russian, Ukrainian, Arabic, Thai, Vietnamese, and more — the exact list expands with each iOS release. RightSplit uses whatever languages your iPhone has installed."
  - q: "Can RightSplit handle multi-currency receipts?"
    a: "RightSplit reads the numbers as printed. If your receipt is in EUR, GBP, or any other currency, the splits and tip math come out in that currency. You can change the displayed currency symbol in settings; conversion to your home currency is not currently part of the product."
  - q: "Does it handle tax-inclusive (VAT) receipts?"
    a: "Yes. RightSplit treats line items as their printed price. If your country's receipts include VAT in each line item (as is common in the EU and UK), the splits work the same way the receipt does — no extra math required. For tax-exclusive receipts (US standard), the tax line is distributed proportionally across line items."
  - q: "How many people can I split a bill between?"
    a: "There's no hard cap. Realistically, the workflow is designed for 2–12 people — the screen real estate gets tight beyond that, but the math holds. For long-running ledgers across many months and many people, a group-based tool like Splitwise is a better fit."
  - q: "Does RightSplit integrate with Apple Pay, Venmo, or PayPal?"
    a: "Not directly. RightSplit calculates each person's total and shares it as text. From there, each person sends payment using whichever method they prefer — Apple Pay, Venmo, PayPal, Revolut, or cash. The deliberate choice: one app does the math; payment apps do payment. Nothing locked into a single ecosystem."
  - q: "How is RightSplit different from Splitwise?"
    a: "Splitwise is built for long-running group ledgers — roommates, ongoing trip costs, debts that accumulate over months. RightSplit is built for the single-bill workflow — one receipt, scanned, split, settled, done. No accounts to create, no friends to add, no balances to maintain. If you want both, both apps can live on the same phone."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/rightsplit/support/"

release:
  first_release: "2026-03-01"
  last_updated: "2026-03-15"

ratings:
  value: "5.0"
  count: 1
  last_synced: "2026-04-15"
---
RightSplit is a bill splitting app for iPhone that scans receipts, detects items automatically, and calculates what each person owes. Supports item-level assignment so each person pays for what they ordered, with shared dish splitting for bottles, appetizers, and group items. Smart tip calculation distributes tips proportionally with fair rounding. Share payment requests instantly via iMessage, WhatsApp, or copy-paste. Receipt OCR runs on-device with Apple's Vision framework — receipts never leave your phone. Free with equal splitting and tip calculator. Pro unlocks item-based splitting, uneven splits, per-person tip breakdown, and split history — $1.99/year or $7.99 lifetime. No ads, no tracking, no account required.
