---
layout: app
slug: allpaid
name: "AllPaid"
tagline: "Bills, calmly handled, with no bank login."
quick_answer: "AllPaid is a calm bill and subscription tracker for iPhone that doesn't ask for your bank login. It auto-fills the price and billing cycle for 40 common services (Netflix, Spotify, ChatGPT, Claude, Adobe, Microsoft 365, iCloud, rent, utilities, and more), shows every due date on a monthly calendar, sends one reminder before each payment, and breaks down spending by category. It is free, with Pro from {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} lifetime (≈40% of comparable lifetime unlocks). It has no ads, no account, and no tracking."
category: finance
status: live

app_store_url: "https://apps.apple.com/app/id6757253009"

price:
  model: freemium
price_tier: "Pro"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew."

plans:
  - name: "Free"
    price: "$0"
    summary: "Bill tracking, calendar, reminders, widgets, Siri, and Live Activities, free for good."
    features:
      - "Track up to 3 bills"
      - "Monthly calendar with daily totals"
      - "40-service catalog with auto-fill"
      - "A reminder before each due date"
      - "Home Screen / Lock Screen widgets, Siri, Live Activities"
  - name: "Pro · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Full Pro, billed monthly. Cancel anytime."
    features:
      - "Unlimited bills"
      - "Spending analytics: category breakdown, monthly trends, per-bill totals"
      - "Multiple reminders per bill"
      - "Full payment history"
      - "iCloud Sync across your devices"
  - name: "Pro · Annual"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "Same Pro features, billed once a year. ~{SAVE_YEARLY}% cheaper than paying monthly."
    features:
      - "Everything in Pro · Monthly"
      - "~{SAVE_YEARLY}% cheaper than monthly over a year"
      - "Cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All Pro features for one payment, about what {LIFETIME_MONTHS} months of monthly Pro would cost."
    features:
      - "Everything in Pro · Annual"
      - "One-time purchase, no renewal"
      - "Family Sharing with up to 5 family members at no extra cost"
      - "About 40% of what comparable iPhone bill trackers charge for a lifetime unlock"
      - "Restores on every device signed in with the same Apple ID"
    highlight_label: "Best long-term value"

icon: "/assets/icons/allpaid.png"
og_image: "/assets/og/allpaid.png"

seo:
  title: "AllPaid: Bill Tracker for iPhone, No Bank Login"
  description: "Bill tracker for iPhone with no bank login. 40 services auto-detected (Netflix, ChatGPT, rent, utilities). {P_LIFETIME} lifetime, no subscription required."
  keywords:
    - bill tracker app
    - bill tracker iPhone no bank login
    - bill reminder app
    - subscription tracker iPhone
    - bill due date reminder
    - monthly bill organizer
    - payment reminder app
    - subscription manager app
    - bill calendar app
    - manual bill tracker
    - bill tracker no Plaid
    - bill tracker without bank linking
    - private bill tracker iPhone
    - subscription renewal reminder
    - utility bill tracker
    - rent reminder app
    - bill payment tracker

hero:
  headline: "Every bill in one calm place."
  secondary: "A bill tracker for people who won't hand a bank login to a third-party app."
  subheadline: "AllPaid auto-fills the typical price and billing cycle for 40 common services (Netflix, Spotify, ChatGPT, Claude, Adobe, Microsoft 365, iCloud, rent, utilities), shows every due date on a monthly calendar, and sends one reminder before payment day. Nothing leaves your device unless you turn on iCloud Sync. It is free, with Pro from {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} lifetime, about 40% of what comparable iPhone bill trackers charge for a lifetime unlock."
  cta_label: "Download Free"
  alt: "AllPaid monthly bill calendar on iPhone with upcoming due dates and a daily total"

who_for:
  - "You've missed a due date in the last six months and it cost you money"
  - "You want an overview of your bills without opening your bank app"
  - "You track 10 to 50 subscriptions and want a clear view of what you're actually paying for"
  - "You want to share a single bill with a partner or roommate through the iOS share sheet, without a shared account or Family Sharing"
  - "You won't connect your real bank accounts to a third-party budgeting app through Plaid"

who_not_for:
  - "You want full budgeting with bank connections and automatic transaction categorization"
  - "You run a business and need double-entry accounting"
  - "You want collaborative multi-user household finance management"
  - "You want a paid service to negotiate your bills down for you"

alternatives_to:
  - "Rocket Money"
  - "Truebill"
  - "Bobby"
  - "Subby"
  - "TrackMySubs"
  - "Chronicle Bills"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Why we built this"
  heading: "For people who have already ruled out bank-linked apps."
  story: "AllPaid exists because every other bill tracker we tried wanted a bank login. Through Plaid, any app holding that login gets persistent read access to every transaction in the account, far more than the recurring charges people actually want to see. We went the other way: a manual-first tracker with a 40-service catalog that fills in the boring parts in seconds. Bills live on the device in SwiftData and sync only through your own private iCloud, if you turn that on. There is no account and nothing is uploaded to us. The trade-off: AllPaid will not catch a forgotten auto-renewal you never typed in. Everything it does track stays under your control."
  signals:
    - "Local SwiftData storage, with optional sync through your own private iCloud; zero third-party SDKs, and the App Store privacy label reads 'Data Not Collected'"
    - "40 recognised services across 18 categories; the catalog is hard-coded in the app binary and matched in English plus Finnish and German keywords"
    - "Paid for by people buying the software, with no ads, no investors, and no aggregator integrations"
    - "{APP_COUNT} live apps in the catalogue, all following the same data rules: no tracking, no ads, no required accounts"
  external_link:
    label: "Read the Lagerland studio backstory →"
    href: "/lagerland-apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally, usually within a day."

value_points:
  - title: "Smart bill detection (no bank link)"
    description: "Type 'Netflix,' 'Spotify,' or 'ChatGPT' and AllPaid auto-fills the typical price, billing cycle, and category from a built-in catalog of 40 recognized services. Nothing leaves your device."
  - title: "Monthly calendar, daily totals"
    description: "Every bill sits on a calendar showing what's due, what's paid, and what's still coming this month, so you see bunched billing days before they hit your account."
  - title: "Reminders that don't nag"
    description: "One notification before each due date. You can snooze it, mark the bill paid straight from the notification, or ask Siri what's due."
  - title: "Pay once, keep forever"
    description: "{P_LIFETIME} lifetime, about 40% of what comparable iPhone bill trackers charge for a lifetime unlock. The free tier handles the basics, and no subscription is required."

how_it_works:
  intro: "AllPaid is a manual bill tracker built around a 40-service catalog and a monthly calendar. It uses no bank connection, no Plaid, and no third-party login. This is how a bill moves through it."
  steps:
    - title: "Type the bill name (or pick from the catalog)"
      detail: "AllPaid ships with 40 recognized services across 18 categories: streaming (Netflix, Spotify, Disney+, YouTube Premium, Apple TV+, HBO Max, Amazon Prime, Crunchyroll, Apple Music), AI tools (ChatGPT, Claude Pro), productivity (Adobe, Microsoft 365, Dropbox, Google One, iCloud), housing (rent, mortgage), utilities (electricity, water, gas), internet & phone, insurance (car, health, home, life), transportation, gym, student loans, credit cards, other loans, taxes, savings, groceries, entertainment, pet care, childcare, and donations. Type any of those and the price, billing cycle, and category fill in. For anything outside the catalog, type the name and amount yourself, which takes about five seconds."
    - title: "Confirm the cycle (weekly to yearly, or custom)"
      detail: "Most catalog services default to monthly. Annual cycles are common (home insurance, some software, gym annual passes) and are projected forward on the calendar. AllPaid shows you exactly when the next charge lands, so you can fix a wrong cycle before the reminders go wrong."
    - title: "See the next 30 / 60 / 90 days at a glance"
      detail: "The monthly calendar projects every recurring bill forward. A daily total shows what's due, what's paid, and what's still coming. Heavy days (rent + utilities + 4 subscriptions all hitting the 1st) show up weeks before they arrive. Pro lets you step forward and back through other months."
    - title: "Get one reminder before each due date"
      detail: "AllPaid sends a single notification the day before each bill (Pro can add earlier ones, such as 14, 7, or 3 days ahead of a monthly bill, plus one on the due day). From the notification you can mark the bill paid, snooze it, or open it. There are no streaks, no red badges, and no follow-up nagging if you missed yesterday."
    - title: "Mark paid in one tap, from anywhere"
      detail: "Tap once in the app or on the notification, and undo if you tapped too fast. Each payment goes into a local history log that the analytics use."
    - title: "Watch spending clarify over weeks (Pro)"
      detail: "Pro adds analytics: a category breakdown with percentages (streaming, subscriptions, utilities, housing, insurance, etc.), per-bill totals, and a monthly-trends chart computed from your local payment history. You can answer 'how much do I actually spend on streaming?' without opening your bank app."
    - title: "Stays on your device, or in your own iCloud."
      detail: "No account, no upload to us, no third-party SDKs. Bills, payments, and analytics live in SwiftData on your iPhone; if you turn on iCloud Sync (Pro), they sync through your own private iCloud database. See the per-app <a href=\"/transparency/#allpaid\">transparency entry</a> for third-party SDKs and tracking domains (there are none)."

example_insights:
  overline: "What an AllPaid month looks like"
  heading: "Real numbers, in plain English."
  intro: "The analytics are the main reason to use AllPaid. These are the kinds of plain-English answers Pro pulls from your own bill history, and none of it leaves your device."
  cards:
    - tag: "Calendar · Pattern"
      headline: "$612 of bills land on the 1st. Move $200 to autopay on the 5th."
      body: "Three subscriptions, your insurance, and a gym pass all renewed on the 1st of this month. $187 of that could move to the 5th if you change the renewal dates in those apps. The calendar shows the bunching weeks before it hits your account."
    - tag: "Category · Breakdown"
      headline: "Streaming is now your second-biggest category, behind housing."
      body: "Over the last 90 days, streaming reached $89/mo: Netflix $15.99, Spotify $9.99, Disney+ $8.99, YouTube Premium $13.99, Apple TV+ $9.99, HBO Max $9.99, Amazon Prime $8.99, Apple Music $10.99. Pro's category breakdown shows exactly what that share costs you each month."
    - tag: "AI · Subscriptions"
      headline: "You pay $40/mo across ChatGPT and Claude, the same as Adobe."
      body: "AI tools are now a top-five category for many users, and AllPaid recognises ChatGPT, OpenAI, Claude, and Anthropic out of the box. Pro's monthly-trend chart shows whether your AI spend is creeping up or holding steady."
    - tag: "Trial · Caught"
      headline: "Two annual renewals totalling $239 land in 21 days."
      body: "Annual bills are easy to forget. AllPaid projects yearly cycles forward and flags large upcoming charges early enough that you can decide whether to keep or cancel them before the renewal hits."

features:
  - title: "One-tap paid"
    description: "Mark any bill as paid with a single tap, in the app or straight from a notification. Undo right away if you tapped too fast."
  - title: "Widgets on Home Screen, Lock Screen, and StandBy"
    description: "See upcoming bills without opening the app. The full calendar widget puts your month on your Home Screen, and Lock Screen widgets show what's due before you unlock."
  - title: "Spending analytics (Pro)"
    description: "Pro breaks spending down across 19 categories: streaming, subscriptions, utilities, housing, insurance, transportation, credit cards, loans, taxes, and more. It adds a monthly trend chart computed from your local payment history and per-bill totals."
  - title: "Siri and Live Activities"
    description: "Ask Siri what bills are due. A Live Activity keeps the next bill due today or tomorrow on your Lock Screen and in the Dynamic Island, so you see it without opening the app."
  - title: "40 recognized services, 18 categories"
    description: "Auto-fill for Netflix, Spotify, Disney+, YouTube Premium, Apple TV+, HBO Max, Amazon Prime, Crunchyroll, Apple Music, ChatGPT, Claude Pro, Adobe, Microsoft 365, Dropbox, Google One, iCloud, electricity, water, gas, internet, phone, car/health/home/life insurance, rent, mortgage, car payment, transit, gym, student loans, credit cards, other loans, taxes, savings, groceries, entertainment, pet care, childcare, and donations. Names are matched in English plus Finnish and German keywords. Anything outside the catalog takes about five seconds to add by hand."
  - title: "Search, sort, share, and note"
    description: "Search finds any bill. Sort by due date, amount, or name. Add notes for account numbers or payment confirmation IDs. Share a single bill with a partner or roommate through the share sheet, with no shared account or household sign-up."
  - title: "No bank login, ever"
    description: "AllPaid does not connect to your bank and does not use <a href=\"https://en.wikipedia.org/wiki/Plaid_(company)\" rel=\"noopener\" target=\"_blank\">Plaid</a> or any other bank-aggregation API. The trade-off is that you add bills yourself (in seconds, from the catalog), and your bank credentials never touch this app or any server. If you'd rather have automatic detection and don't mind handing over a bank login, the <a href=\"/alternatives/rocket-money/\">Rocket Money comparison</a> walks through the trade-off in detail."

screenshots:
  - src: "/assets/screenshots/allpaid/1.png"
    alt: "AllPaid bills list on iPhone with upcoming bills, amounts and mark-as-paid buttons"
  - src: "/assets/screenshots/allpaid/2.png"
    alt: "AllPaid analytics screen with total spending and a category donut chart"
  - src: "/assets/screenshots/allpaid/3.png"
    alt: "AllPaid monthly summary with a due-date calendar, paid and remaining totals"
  - src: "/assets/screenshots/allpaid/4.png"
    alt: "AllPaid lock screen notification reminding that a bill is due tomorrow"
  - src: "/assets/screenshots/allpaid/5.png"
    alt: "AllPaid Home Screen widgets with a month calendar and upcoming bills"
  - src: "/assets/screenshots/allpaid/6.png"
    alt: "AllPaid extra-large calendar widget showing bills due across a month"
  - src: "/assets/screenshots/allpaid/7.png"
    alt: "AllPaid extra-large horizon widget listing bills due this week with a running total"
  - src: "/assets/screenshots/allpaid/8.png"
    alt: "AllPaid extra-large rhythm widget showing a year of paid bills as a heatmap"

comparison_table:
  intro: "Each column below answers a question people ask when shopping for a bill tracker. Rocket Money, Bobby, and What's Due each do something well. AllPaid fits when you want manual entry, no bank login, the lowest lifetime price, and analytics that stay on the device."
  competitors: ["AllPaid", "Rocket Money", "Bobby", "What's Due", "Spreadsheet"]
  rows:
    - feature: "Works without a bank login / Plaid"
      values: ["Yes, manual only", "No, Plaid required for detection", "Yes, manual only", "Yes, manual only", "Yes"]
    - feature: "Auto-fills 30+ common services (catalog)"
      values: ["Yes, 40 services", "Yes, from your transactions", "Manual entry", "Manual entry", "No"]
    - feature: "Monthly calendar view with daily totals"
      values: ["Yes", "Limited", "Limited", "Yes", "No"]
    - feature: "Spending analytics, category breakdown"
      values: ["Yes, Pro, on-device", "Yes, server-side", "Limited", "Limited", "Manual"]
    - feature: "One-time lifetime unlock available"
      values: ["{P_LIFETIME} lifetime", "Subscription only ($6-12/mo)", "One-time pack (~$2.99)", "$59.99 lifetime", "n/a"]
    - feature: "Account / sign-up required"
      values: ["No", "Yes, bank credentials", "No", "No", "n/a"]
    - feature: "Zero third-party tracking SDKs"
      values: ["0", "Standard analytics + ads SDKs", "Standard analytics", "Standard analytics", "n/a"]
    - feature: "Bill negotiation service"
      values: ["No, out of scope", "Yes (paid, % of savings)", "No", "No", "No"]
    - feature: "Built-in subscription cancellation flow"
      values: ["No, out of scope", "Yes, Premium feature", "No", "No", "No"]
    - feature: "Catches forgotten / auto-renewing subscriptions you never entered"
      values: ["No, manual entry only", "Yes, from your transactions", "No", "No", "No"]
  footnote: "Competitor pricing and features reflect each app's public landing page and App Store description as of 2026-05. Rocket Money pricing is the publicly listed Premium range; the negotiation service is a separate fee. Apps change often, so check current pricing on the App Store before switching."

plateau_disclosure:
  title: "What AllPaid won't do for you"
  rule: "AllPaid is a manual bill tracker built around a 40-service catalog and a monthly calendar. It is deliberately not a full personal-finance app, and that limit is what keeps it private, on-device, and available for a one-time price."
  what_it_does_not_do: "AllPaid will not connect to your bank, import transactions automatically, negotiate bills down for you, or scan your email for receipts. It will not warn you about price hikes for bills you didn't enter: if Spotify raises its price, AllPaid only knows once you update the amount yourself. It is not a budgeting app, an expense categorizer, or a household-finance dashboard."
  notes:
    - "Want automatic detection from your transactions? Try Rocket Money or Truebill, which need your bank login to do it."
    - "Want bill negotiation as a service? Rocket Money offers it for a percentage of the savings."
    - "Want full budgeting (envelopes, transaction tagging, net worth)? YNAB, Monarch Money, or Copilot are better fits."
    - "Want the cheapest option with the strictest privacy? A spreadsheet still works. AllPaid is for people who tried a spreadsheet and gave up after week three."

training_vocabulary:
  overline: "The 40-service catalog"
  heading: "The bills AllPaid already knows."
  intro: "AllPaid recognises 40 common services across 18 categories out of the box. Type the name and the typical price, cycle, and category fill in. Names are matched in English, plus Finnish and German keywords for utilities and housing (sähkö, vesi, vuokra, strom, wasser, miete)."
  groups:
    - heading: "Streaming"
      items:
        - "Netflix"
        - "Spotify"
        - "Disney+"
        - "YouTube Premium"
        - "Apple TV+"
        - "HBO Max"
        - "Amazon Prime"
        - "Crunchyroll"
        - "Apple Music"
    - heading: "AI tools, cloud & productivity"
      items:
        - "ChatGPT (OpenAI)"
        - "Claude Pro (Anthropic)"
        - "Adobe / Creative Cloud / Photoshop"
        - "Microsoft 365"
        - "Dropbox"
        - "Google One"
        - "iCloud"
    - heading: "Housing, utilities & connectivity"
      items:
        - "Rent · Mortgage"
        - "Electricity · Water · Gas"
        - "Internet · Phone"
    - heading: "Insurance, transportation & more"
      items:
        - "Car · Health · Home · Life insurance"
        - "Car payment · Transit pass"
        - "Gym"
        - "Student loan · Other loans"
        - "Credit card · Taxes · Savings"
        - "Groceries · Entertainment"
        - "Pet care · Childcare · Donations"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no trackers, no third-party SDKs"
    - "No account or sign-up required"
    - "No bank connection: AllPaid does not use Plaid or any bank-aggregation API"
    - "All bills, payments, and analytics stored locally on your device; optional iCloud Sync (Pro) uses your own private iCloud"
    - "See the per-app <a href=\"/transparency/#allpaid\">transparency entry</a> for third-party SDKs and tracking domains (there are none)"

faq:
  - q: "What is AllPaid?"
    a: "AllPaid is a privacy-first bill and subscription tracker for iPhone. It tracks bills, subscriptions, and due dates without any bank connection, using manual entry plus a 40-service catalog that auto-fills price, cycle, and category. It includes a monthly calendar, reminders, widgets, Siri, Live Activities, and on-device spending analytics. It is free; Pro costs {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} lifetime."
  - q: "How does smart bill detection work?"
    a: "When you type a bill name such as 'Netflix' or 'ChatGPT', AllPaid matches it against a built-in catalog of 40 recognized services and auto-fills the typical price, billing cycle, and category. Nothing leaves your device. The catalog covers streaming (Netflix, Spotify, Disney+, YouTube Premium, Apple TV+, HBO Max, Amazon Prime, Crunchyroll, Apple Music), AI tools (ChatGPT, Claude Pro), productivity (Adobe, Microsoft 365, Dropbox, Google One, iCloud), housing (rent, mortgage), utilities (electricity, water, gas), internet & phone, four kinds of insurance, transportation (car payment, transit), gym, student loans, credit cards, other loans, taxes, savings, groceries, entertainment, pet care, childcare, and donations. Names are matched in English plus Finnish and German keywords. For anything outside the catalog, type the name and amount yourself, which takes about five seconds."
  - q: "How is AllPaid different from Rocket Money?"
    a: "Rocket Money connects to your bank, detects subscriptions from your transaction history, and offers a paid negotiation service that takes a percentage of any savings it finds. AllPaid does none of that. You add bills yourself (or through the 40-service catalog), nothing leaves your device unless you turn on iCloud Sync, and the core app has no monthly fee. If automatic detection from transactions matters more to you than privacy, Rocket Money fits better. If you would rather not give your bank login to a third-party app, AllPaid is the better choice. The full Rocket Money alternative comparison goes through it line by line."
  - q: "Does AllPaid catch free trials before they auto-renew?"
    a: "Only the ones you enter. AllPaid does not scan your email or transactions, so it cannot detect a trial you signed up for and forgot. When you add a trial bill with the day it converts, AllPaid projects that date on the calendar and sends a reminder the day before. Many users add a 'free trial, review by X' bill the moment they start a trial and let AllPaid flag the deadline."
  - q: "What does the calendar actually show?"
    a: "Every bill projected forward on a monthly calendar: what's due, what's paid, and what's still coming, with a total for each day. Heavy billing days (rent + utilities + four subscriptions all hitting the 1st) show up weeks before they hit your bank account. With Pro you can step forward and back a month at a time to see what's coming."
  - q: "Is AllPaid a budgeting app?"
    a: "No. AllPaid covers bill tracking, subscription management, and payment reminders. It does not do full budgeting or transaction categorization, so there are no envelopes, no spending caps, and no automatic transaction tagging. If you want full budgeting, YNAB, Monarch Money, or Copilot are better fits."
  - q: "Is AllPaid free?"
    a: "Yes. Core bill tracking, the monthly calendar, reminders, widgets, Siri, and Live Activities are free. The free tier tracks up to 3 bills; saving a fourth opens the Pro upgrade screen. Pro unlocks unlimited bills, spending analytics (category breakdown, monthly trends, per-bill totals), multiple reminders per bill, and full payment history for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} lifetime. The {P_LIFETIME} lifetime price is about 40% of what comparable iPhone bill trackers charge for a lifetime unlock, and the Pro purchase supports Family Sharing, so one purchase covers up to 5 family members. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does AllPaid work with Siri and widgets?"
    a: "Yes. Ask Siri what bills are due and it answers right away. Home Screen widgets, Lock Screen widgets, and a full monthly-calendar widget show upcoming bills without opening the app. A Live Activity shows the next bill due today or tomorrow on your Lock Screen and in the Dynamic Island."
  - q: "Does AllPaid share my financial data?"
    a: "No. AllPaid has no ads, no third-party trackers, no account requirement, no bank connection, and no server of its own to upload to. Your bill information stays on your device or, if you turn on iCloud Sync (Pro), in your own private iCloud database. The App Store privacy label reads 'Data Not Collected', and the transparency page has the full breakdown."
  - q: "Can I share bills with someone?"
    a: "Yes, one bill at a time, through the iOS share sheet. That works for splitting rent, internet, or a streaming subscription with a partner or roommate. AllPaid does not require a shared account or a household sign-up, because each share covers a single bill."

related_journal:
  slug: i-will-not-ask-for-your-bank-login
  anchor: "Why AllPaid will never ask for your bank login"

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/allpaid/support/"

release:
  first_release: "2026-01-01"
  last_updated: "2026-05-13"
  last_audited: "2026-05-13"

ratings:
  value: "4.9"
  count: 7
  last_synced: "2026-10-19"
last_updated: 2026-10-26
---
AllPaid is a calm bill and subscription tracker for iPhone, made for people who won't hand a bank login to a third-party app. You add bills by hand or let them auto-fill from a built-in catalog of 40 common services across 18 categories: streaming (Netflix, Spotify, Disney+, YouTube Premium, Apple TV+, HBO Max, Amazon Prime, Crunchyroll, Apple Music), AI tools (ChatGPT, Claude Pro), productivity and cloud (Adobe, Microsoft 365, Dropbox, Google One, iCloud), housing (rent, mortgage), utilities (electricity, water, gas), internet and phone, four kinds of insurance, transportation, gym, student loans, credit cards, other loans, taxes, savings, groceries, entertainment, pet care, childcare, and donations. Names are matched in English plus Finnish and German keywords. A monthly calendar projects every recurring bill forward with daily totals, so you see bunched billing days weeks before they hit your account. A reminder fires once before each due date, and you can mark the bill paid with one tap in the app or straight from the notification. Pro adds on-device spending analytics (category breakdown with percentages, monthly trend charts computed from your local payment history, per-bill totals) and unlimited bills. AllPaid has no ads, no trackers, no account, and no bank connection through Plaid or anything else. It is free, with optional Pro from {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} lifetime, about 40% of what comparable iPhone bill trackers charge for a lifetime unlock.
