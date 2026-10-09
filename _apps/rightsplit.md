---
layout: app
slug: rightsplit
name: "RightSplit"
tagline: "Split bills from receipts."
quick_answer: "RightSplit is a receipt-scanning bill splitter for iPhone. Snap a photo of any restaurant or bar receipt, assign each item to the person who ordered it, split shared dishes, spread tax and tip fairly, and send everyone their total via iMessage or WhatsApp. Free for equal splits, tip and your first receipt scan; Pro+ ($3.99/year or $7.99 lifetime) unlocks unlimited scans, item-by-item splits and Spaces for trips and shared homes. No ads, no account, no tracking — receipts read on-device with Apple's Vision framework."
category: finance
platforms: ["iOS"]
status: live

app_store_url: "https://apps.apple.com/app/id6757268612"

price:
  model: freemium
  value: "Free — Pro+ from $3.99/yr or $7.99 lifetime"
schema_price: "0"
schema_high_price: "7.99"
schema_offer_count: "3"
price_currency: "USD"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. The lifetime tier is a one-time purchase — no auto-renew."

icon: "/assets/icons/rightsplit.png"
og_image: "/assets/og/rightsplit.png"

seo:
  title: "Bill Splitter for iPhone — Scan, Split, Send | RightSplit"
  description: "Scan a receipt on iPhone. Item-by-item splits, shared dishes, fair tip math, send via iMessage or WhatsApp. No account. Free; Pro+ $3.99/yr or $7.99 once."
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
  pre_headline: "Free forever for equal splits, tip calc and your first receipt scan. Pro+ unlocks unlimited scans and item-by-item fairness — $3.99/year, or $7.99 once and you own it. No subscription trap. No card on file just to try it."
  cta_label: "Download Free"
  alt: "RightSplit on iPhone — the Scan Receipt screen, ready to photograph a restaurant bill"

who_for:
  - "You split restaurant bills with friends who ordered different things"
  - "You share rent, utilities, or groceries with roommates and want fair per-item math"
  - "You travel in groups and need to settle bills without awkward maths at the table"
  - "You'd rather scan a receipt than type 12 line items manually"
  - "You refuse to create another account just to split one dinner"

who_not_for:
  - "You want a shared group ledger that everyone adds to and checks from their own phone (use Splitwise)"
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
    description: "Tax and tip shared out fairly with rounding, then everyone's total goes out via text, WhatsApp, or copy. From photo to payment request in under a minute."
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
    description: "Free keeps your last five splits; Pro+ keeps every one. Look up who owed what, settle disputes, or reference old totals without re-scanning."

plans:
  - name: "Free"
    price: "$0 forever"
    summary: "Equal splits, tip calculator, and your first receipt scan."
    features:
      - "One free receipt scan — on-device OCR, item assignment, send"
      - "Equal splitting between 2 and 50 people"
      - "Tip calculator with fair rounding"
      - "Your last 5 splits in history"
      - "No account, no tracking, no ads"
  - name: "Pro+ · yearly"
    price: "$3.99 / year"
    summary: "Unlimited scans and item-by-item splitting — what most people install RightSplit for."
    features:
      - "Everything in Free"
      - "Unlimited receipt scans"
      - "Item-level fairness — assign each line to who ordered it"
      - "Shared dishes, uneven splits and per-person tip breakdown"
      - "Send totals via iMessage or WhatsApp"
      - "Spaces for trips and shared homes — balances and a settle-up plan"
      - "Unlimited split history"
      - "Cancel anytime — no penalty"
  - name: "Pro+ · lifetime"
    highlight: true
    price: "$7.99 once"
    summary: "Most chosen. Pay once, own it forever — pays for itself in two years vs the yearly tier."
    features:
      - "Everything in Pro+ yearly"
      - "One purchase, no recurring charge"
      - "All future feature updates"
      - "No card on file after the App Store buy"

how_it_works:
  intro: "From receipt photo to payment request in under sixty seconds — no manual entry, no account required, no upload."
  steps:
    - title: "Point the camera at the receipt"
      detail: "Apple's on-device Vision framework (VNRecognizeTextRequest) reads every line item, price, and total. Works on thermal restaurant receipts, bar tabs, printed bills, and photographs of digital receipts. Nothing is uploaded — the receipt image stays on the phone."
    - title: "Tap items to assign them"
      detail: "Each line item gets tagged to the person who ordered it. Shared bottles and appetizers split evenly between the people who actually shared them, not across the whole table."
    - title: "Tax and tip, shared fairly"
      detail: "The tax and any tip or service charge printed on the receipt are spread in proportion to each person's subtotal — so the person who ordered the $14 salad pays a smaller share than the person who ordered the $48 steak. Splitting without a receipt? Pick the tip on the split screen: presets of 0, 15, 18 and 20%, or a 0–30% slider. Fair rounding ensures the totals add up to the penny."
    - title: "Send everyone their part"
      detail: "Tap a name to send that person their amount via iMessage or WhatsApp — 'Hey Mike! Your share of the bill at Luigi's is $23.40.' — or copy the full breakdown to paste anywhere. Sending is part of your free first scan, then Pro+. From scan to settled in under a minute."

plateau_disclosure:
  title: "How RightSplit calculates fair tips, splits, and rounding"
  rule: "Each person's subtotal is the sum of the items they ordered plus their proportional share of any shared items (a bottle split four ways is 25% to each person who shared it). Their tip is calculated as (their subtotal ÷ total subtotal) × the tip on the bill (tax is shared the same way) — so the person who ordered the $14 salad pays a smaller share of the tip than the person who ordered the $48 steak. Every amount is kept in whole cents and the per-person totals always add up to the bill: when a shared item doesn't divide evenly, the leftover cents go one each to people who shared it, and any rounding left over on tax and tip goes to the last person on the list."
  what_it_does_not_do: "It does not round each person's tip down (which would silently under-collect the total), apply a uniform tip across diners (which is mathematically just equal-splitting in disguise), or stack a second tip on top of a service charge that's already printed on the receipt (a printed service charge or gratuity line is read as the tip and shared out like tax — RightSplit doesn't add another)."
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
        - "Electronic / digital receipts — screenshots of emailed or in-app receipts, picked from your photos or shared into RightSplit"
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
        - "Item-based split — each person pays for what they ordered (Pro+, and your free first scan)"
        - "Proportional tip — tip distributed by share of subtotal, not by headcount"
        - "Fair rounding — leftover cents handed out one at a time, so totals add up to the penny"
        - "VAT / tax-inclusive vs tax-exclusive math — handled per-receipt"
    - heading: "Languages &amp; currency"
      items:
        - "The receipt scanner reads 16 languages on-device — pick yours in Options"
        - "58 currencies, including no-decimal ones like ¥ and ₩ — prices are read in the currency you set"
        - "Splits stay in the receipt's currency; Pro+ adds an approximate home-currency figure from European Central Bank daily rates"
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
        - "Free + $3.99/yr or $7.99 lifetime"
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
        - "On-device (Apple Vision); 1 free scan, then Pro+"
        - "Pro tier only, cloud OCR"
        - "Photo-tap, no OCR"
        - "Manual entry"
    - feature: "Item-level splitting"
      values:
        - "Pro+ (and your free first scan)"
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
        - "On your phone only — Pro+ Spaces, no shared sync"
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
  footnote: "Competitor details reflect publicly documented features as of 2026. Splitwise is the right tool when the whole group needs to see and add to a shared balance; RightSplit is built for the single bill, with Pro+ Spaces for trips and shared homes kept on one phone."

screenshots:
  - src: "/assets/screenshots/rightsplit/1.png"
    alt: "RightSplit receipt scanner on iPhone — take a photo of the restaurant bill or choose one from the gallery, and every line item and total is read on-device"
  - src: "/assets/screenshots/rightsplit/2.png"
    alt: "RightSplit split-by-items screen — each person's items and total, with the tip slider and people count above"
  - src: "/assets/screenshots/rightsplit/3.png"
    alt: "RightSplit shared items — a shared item split between the people who shared it, with a check showing how much of the total is still unassigned"
  - src: "/assets/screenshots/rightsplit/4.png"
    alt: "RightSplit split summary on iPhone — each person's total with Text and WhatsApp buttons, plus the receipt's subtotal, tax and tip"

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
    a: "RightSplit is a bill splitting app for iPhone that scans receipts, detects items automatically, and calculates what each person owes — including shared dishes, tip, and rounding. Share payment requests instantly via iMessage or WhatsApp. Free for equal splits and your first receipt scan; Pro+ unlocks unlimited scans, item-based splitting and Spaces at $3.99/year or $7.99 lifetime."
  - q: "How does the receipt scanner work?"
    a: "Take a photo of your receipt and RightSplit reads the items and prices automatically using Apple's on-device Vision framework (the same OCR Apple uses for Live Text). No manual typing required — it detects line items, totals, and tax. The receipt image never leaves your phone. Your first scan is free; unlimited scanning is part of Pro+."
  - q: "Which OCR engine does RightSplit use?"
    a: "Apple's <a href=\"https://developer.apple.com/documentation/vision\" rel=\"noopener\" target=\"_blank\">Vision framework</a> — specifically <a href=\"https://developer.apple.com/documentation/vision/vnrecognizetextrequest\" rel=\"noopener\" target=\"_blank\">VNRecognizeTextRequest</a> — running entirely on-device. That means three things: receipts work offline; receipt images are never uploaded to a server; and the OCR quality is whatever Apple ships in the current iOS release, improving with every Apple update."
  - q: "How accurate is the receipt scan?"
    a: "Accuracy depends on the receipt. Standard thermal restaurant receipts and clean printed bills read reliably. Faded receipts, very wrinkled paper, or photographs taken at a sharp angle can mis-read individual line items — in which case you can tap any item to correct the price or description before assigning. Before you send anything, the summary lists the receipt's subtotal, tax, tip and total so you can check them against the paper, and the saved receipt keeps its photo."
  - q: "Can I split shared dishes?"
    a: "Yes. Any item can be split between multiple people — bottles, appetizers, shared plates. The item's cost is divided evenly among the people who shared it, and tax and tip follow each person's subtotal."
  - q: "How do I send people their share?"
    a: "After splitting, tap a name to send that person their amount via iMessage or WhatsApp — 'Hey Mike! Your share of the bill at Luigi's is $23.40.' — or copy the full breakdown to paste into any app. Nothing to install on the other person's phone. Sending is included in your free first scan; after that it's part of Pro+."
  - q: "Is RightSplit free?"
    a: "Yes. Equal splits, the tip calculator, fair rounding, your last five splits and your first receipt scan are free forever. Pro+ unlocks unlimited scans, item-based splitting (the headline feature), uneven splits, per-person tip breakdown, sending totals by iMessage or WhatsApp, unlimited history, Spaces for trips and shared homes, home-currency conversion and the payment tracker — $3.99 per year, or $7.99 once and you own it. There's no card on file to start, and no auto-renew on the lifetime tier. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does RightSplit need an account?"
    a: "No. RightSplit works immediately with no sign-up, no account, and no personal information required. Only one person at the table needs the app — you scan, split, and send everyone their total."
  - q: "Does RightSplit store my receipts online?"
    a: "No. All receipt and bill data stays on your device. RightSplit has no servers, no cloud storage, no advertising SDKs, and no third-party analytics. Receipt OCR runs on-device with Apple's Vision framework — the photo never leaves your phone."
  - q: "Does RightSplit work offline?"
    a: "Yes. The entire scan-split-share workflow works without internet. Receipt OCR is on-device. The only steps that need a connection are the final share — iMessage and WhatsApp obviously need network, but you can also copy the summary and send it later — and refreshing the European Central Bank exchange rates used for currency conversion, which RightSplit caches on the phone."
  - q: "What languages does the receipt scanner read?"
    a: "Sixteen: English, French, German, Spanish, Italian, Portuguese, Dutch, Swedish, Danish, Finnish, Norwegian, Polish, Japanese, Korean, and Chinese (Simplified & Traditional). Pick the receipt's language under Receipt Language in the app's Options; English is always read alongside it, and the subtotal, tax and total lines in each of those languages are recognised so they aren't billed as dishes."
  - q: "Can RightSplit handle multi-currency receipts?"
    a: "RightSplit splits in the currency you set — 58 to choose from, including no-decimal currencies like yen and won — so a receipt in EUR, GBP, or any other currency comes out in that currency, tax and tip included. With Pro+, each person's total also shows an approximate amount in your home currency, using the European Central Bank's daily reference rates (30 of the 58 currencies have one), and a Space can mix currencies and settle in the one you choose."
  - q: "Does it handle tax-inclusive (VAT) receipts?"
    a: "Yes. RightSplit treats line items as their printed price. If your country's receipts include VAT in each line item (as is common in the EU and UK), the splits work the same way the receipt does — no extra math required. For tax-exclusive receipts (US standard), the tax line is distributed proportionally across line items."
  - q: "How many people can I split a bill between?"
    a: "On the split screen, anywhere from 2 to 50 people. A scanned receipt has no fixed cap, but realistically the workflow is designed for 2–12 people — the screen real estate gets tight beyond that, but the math holds. Pro+ Spaces can keep a trip's or a shared home's balances on your phone; when everyone in the group needs to see and add to the same ledger from their own phone, a group-based tool like <a href=\"/alternatives/splitwise/\">Splitwise</a> (or <a href=\"/alternatives/tricount/\">Tricount</a> for trip ledgers) is a better fit."
  - q: "Does RightSplit integrate with Apple Pay, Venmo, or PayPal?"
    a: "Not as a payment app — RightSplit never moves money. It calculates each person's total and shares it as text. From there, each person sends payment using whichever method they prefer — Apple Pay, Venmo, PayPal, Revolut, or cash. If you save your own Venmo, PayPal.me, Revolut or Wise handle, the pay button next to each person opens that service with their amount filled in where the service allows it. The deliberate choice: one app does the math; payment apps do payment. Nothing locked into a single ecosystem — see the full breakdown on the <a href=\"/alternatives/venmo-split/\">RightSplit vs Venmo Split comparison</a>."
  - q: "How is RightSplit different from Splitwise?"
    a: "<a href=\"/alternatives/splitwise/\">Splitwise</a> is built for shared group ledgers — roommates, ongoing trip costs, debts that accumulate over months, with everyone logging and checking balances from their own account. RightSplit is built for the single-bill workflow — one receipt, scanned, split, settled, done. No accounts to create, no friends to add. For a trip or a shared home, Pro+ Spaces collect receipts and expenses, keep each person's balance and work out who pays whom — but they live on your phone only, with no sync, so the rest of the group sees what you send them rather than a live shared balance. If you want both, both apps can live on the same phone. See the <a href=\"/alternatives/splitwise/\">full Splitwise comparison</a>, or compare against <a href=\"/alternatives/tab/\">Tab</a>, <a href=\"/alternatives/tricount/\">Tricount</a>, <a href=\"/alternatives/settle-up/\">Settle Up</a>, and <a href=\"/alternatives/venmo-split/\">Venmo Split</a>."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/rightsplit/support/"

release:
  first_release: "2026-03-01"
  last_updated: "2026-03-15"

related_journal:
  slug: "bill-splitting-math-tax-tip-shared-plates"
  anchor: "The bill-splitting math nobody agrees on: tax, tip and the shared plate"

ratings:
  value: "5.0"
  count: 1
  last_synced: "2026-04-15"
---
RightSplit is a bill splitting app for iPhone that scans receipts, detects items automatically, and calculates what each person owes. Supports item-level assignment so each person pays for what they ordered, with shared dish splitting for bottles, appetizers, and group items. Smart tip calculation distributes tips proportionally with fair rounding. Share payment requests instantly via iMessage, WhatsApp, or copy-paste. Receipt OCR runs on-device with Apple's Vision framework — receipts never leave your phone. Free with equal splitting, the tip calculator, your last five splits and your first receipt scan. Pro+ unlocks unlimited scans, item-based splitting, uneven splits, per-person tip breakdown, unlimited split history, and Spaces that keep a trip's or shared home's balances and settle-up plan on your phone — $3.99/year or $7.99 lifetime. No ads, no tracking, no account required.
