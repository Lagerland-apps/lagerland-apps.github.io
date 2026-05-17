---
layout: app
slug: allpaid
name: "AllPaid"
tagline: "Bills, calmly handled. No bank login."
quick_answer: "AllPaid is a calm bill and subscription tracker for iPhone, iPad, and Mac that doesn't ask for your bank login. It auto-fills the price and billing cycle for 31 common services — Netflix, Spotify, ChatGPT, Claude, Adobe, Microsoft 365, iCloud, rent, utilities, and more — shows every due date on a monthly calendar, sends one gentle reminder before each payment, and breaks down spending by category. Free, Pro from $1.99/month or $24.99 lifetime (≈40% of comparable lifetime unlocks). No ads, no account, no tracking."
category: finance
platforms: ["iOS"]
status: live

app_store_url: "https://apps.apple.com/app/id6757253009"

price:
  model: freemium
  value: "Free — Pro from $1.99/mo or $24.99 lifetime"
schema_price: "0"
schema_high_price: "24.99"
schema_offer_count: "3"

icon: "/assets/icons/allpaid.png"
og_image: "/assets/og/allpaid.png"

seo:
  title: "AllPaid — Bill Tracker for iPhone, No Bank Login"
  description: "Bill tracker for iPhone — no bank login. 31 services auto-detected (Netflix, ChatGPT, rent, utilities). $24.99 lifetime. No subscription required."
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
  headline: "Every bill. One calm place."
  secondary: "The bill tracker for people who refuse to hand a bank login to a third-party app."
  subheadline: "AllPaid auto-fills the typical price and billing cycle for 31 common services — Netflix, Spotify, ChatGPT, Claude, Adobe, Microsoft 365, iCloud, rent, utilities — shows every due date on a monthly calendar, and sends one gentle reminder before payment day. Nothing leaves your device. Free, with Pro from $1.99/month or $24.99 lifetime — about 40% of what comparable iPhone bill trackers charge for a lifetime unlock."
  cta_label: "Download Free"
  alt: "AllPaid — monthly bill calendar on iPhone with upcoming due dates and a daily total"

who_for:
  - "You've missed a due date in the last six months and it cost you money"
  - "You want a calm bill overview without opening your bank app"
  - "You track 10–50 subscriptions and need a clear 'what am I actually paying for' view"
  - "You want per-bill share with a partner or roommate via the iOS share sheet — no shared account, no Family Sharing required"
  - "You refuse to connect your real bank accounts to a third-party budgeting app via Plaid"

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
  - "Chronicle Bills"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Why we built this"
  heading: "For the user who already filtered out bank-linked apps."
  story: "AllPaid exists because every other bill tracker we tried wanted a bank login. Plaid grants any app holding that login persistent read access to every transaction in the account — far beyond the recurring charges users actually want surfaced. We took the other path: a manual-first tracker with a 31-service catalog that pre-fills the boring parts in seconds. Bills live on the device in SwiftData. No account. No upload. The trade-off is honest — AllPaid will not catch a forgotten auto-renewal you never typed in. Everything it does catch, you control."
  signals:
    - "Local SwiftData storage; the Privacy Manifest declares zero tracking domains and no required-reason APIs beyond standard local storage and notifications"
    - "31 recognised services across 10 categories — catalog is hard-coded in the app binary, matched in English plus Finnish and German keywords"
    - "Funded by honest paid software — no ads, no investor pressure, no aggregator integrations"
    - "15 live apps in the catalogue, all under the same data discipline: no tracking, no ads, no required accounts"
  external_link:
    label: "Read the Lagerland studio backstory →"
    href: "/lagerland-apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally — usually within a day."

value_points:
  - title: "Smart bill detection (no bank link)"
    description: "Type 'Netflix,' 'Spotify,' or 'ChatGPT' and AllPaid auto-fills the typical price, billing cycle, and category from a built-in catalog of 31 recognized services. Nothing leaves your device."
  - title: "Monthly calendar, daily totals"
    description: "Every bill on a visual calendar — what's due, what's paid, what's still coming this month. See bunched billing days before they hit your account."
  - title: "Reminders that don't nag"
    description: "One gentle notification before each due date. Snooze it. Mark paid directly from the notification. Or ask Siri what's due."
  - title: "Pay once, keep forever"
    description: "$24.99 lifetime — about 40% of what comparable iPhone bill trackers charge for a lifetime unlock. Free tier handles the basics. No subscription required."

how_it_works:
  intro: "AllPaid is a manual bill tracker built around a 31-service catalog and a monthly calendar. No bank connection, no Plaid, no third-party login. Here's exactly how a bill moves through it."
  steps:
    - title: "Type the bill name (or pick from the catalog)"
      detail: "AllPaid ships with 31 recognized services across 10 categories — streaming (Netflix, Spotify, Disney+, YouTube Premium, Apple TV+, HBO Max, Amazon Prime, Crunchyroll, Apple Music), AI tools (ChatGPT, Claude Pro), productivity (Adobe, Microsoft 365, Dropbox, Google One, iCloud), housing (rent, mortgage), utilities (electricity, water, gas), internet & phone, insurance (car, health, home, life), transportation, gym, and student loans. Type any of those and the price, billing cycle, and category pre-fill. For anything not in the catalog, type the name and amount manually — it takes about five seconds."
    - title: "Confirm the cycle (monthly, yearly, custom)"
      detail: "Most catalog services default to monthly. Annual cycles — home insurance, some software, gym annual passes — are common and projected forward on the calendar. AllPaid does not assume; it shows you exactly when the next charge lands so you can fix a cycle before reminders go wrong."
    - title: "See the next 30 / 60 / 90 days at a glance"
      detail: "The monthly calendar projects every recurring bill forward. A daily total tells you what's due, what's paid, and what's still coming. Heavy days (rent + utilities + 4 subscriptions all hitting the 1st) become visible weeks before they bite."
    - title: "Get one reminder before each due date"
      detail: "AllPaid sends a single, gentle notification before each bill. From the notification you can mark paid, snooze, or open the bill. No streaks. No red badges. No nagging if you missed yesterday."
    - title: "Mark paid in one tap — from anywhere"
      detail: "Tap once in the app, the widget, or the notification. Undo if you tapped too fast. Each payment writes to a local history log used by analytics."
    - title: "Watch spending clarify over weeks (Pro)"
      detail: "Pro adds analytics: category breakdown with percentages (streaming, AI tools, utilities, housing, insurance, etc.), per-bill totals, and a monthly-trends chart computed from your local payment history. You can answer 'how much do I actually spend on streaming?' without opening your bank app."
    - title: "Stays on your device. Always."
      detail: "No account, no upload, no third-party SDKs. Bills, payments, and analytics live in SwiftData on your iPhone. See the per-app <a href=\"/transparency/#allpaid\">Privacy Manifest</a> for the full list of declared APIs and tracking domains (there are none)."

example_insights:
  overline: "What an AllPaid month looks like"
  heading: "Real numbers, in plain English."
  intro: "AllPaid's analytics are not 'an extra screen.' They are the point of the app. These are the kind of plain-English answers Pro surfaces from your own bill history — none of it leaves your device."
  cards:
    - tag: "Calendar · Pattern"
      headline: "$612 of bills land on the 1st. Move $200 to autopay on the 5th."
      body: "Three subscriptions, your insurance, and a gym pass all renewed on the 1st of this month — $187 of it could be moved to the 5th by changing renewal dates in those apps. The calendar surfaces the bunching weeks before it hits your account."
    - tag: "Category · Breakdown"
      headline: "Streaming is now your second-biggest category, behind housing."
      body: "Across the last 90 days, streaming hit $89/mo — Netflix $15.99, Spotify $9.99, Disney+ $8.99, YouTube Premium $13.99, Apple TV+ $9.99, HBO Max $9.99, Amazon Prime $8.99, Apple Music $10.99. Pro's category screen shows which two you've barely opened since the trial converted."
    - tag: "AI · Subscriptions"
      headline: "You pay $40/mo across ChatGPT and Claude. Same as Adobe."
      body: "AI tools are now a top-five category for many users — AllPaid recognises ChatGPT, OpenAI, Claude, and Anthropic out of the box. Pro's monthly-trend chart shows whether your AI spend is creeping up or steady."
    - tag: "Trial · Caught"
      headline: "Two annual renewals are landing in 21 days — totalling $239."
      body: "Annual bills are easy to forget. AllPaid projects yearly cycles forward and surfaces large upcoming charges in advance — long enough that you can decide to keep them or cancel before the renewal hits."

features:
  - title: "One-tap paid, zero friction"
    description: "Mark any bill as paid with a single tap — from the app, from a notification, or from a widget. Undo instantly if you tapped too fast."
  - title: "Widgets on Home Screen, Lock Screen, and StandBy"
    description: "Upcoming bills at a glance without opening the app. The full calendar widget puts your month on your Home Screen. Lock Screen widgets catch your eye before you even unlock."
  - title: "Spending analytics that clarify (Pro)"
    description: "Pro breaks down spending by category — streaming, AI tools, subscriptions, utilities, housing, insurance, transportation, health, education. Monthly trend chart computed from your local payment history. Per-bill totals. Clarity, not anxiety."
  - title: "Siri and Live Activities"
    description: "Ask Siri what bills are due. Live Activities show today's and tomorrow's bills on your Lock Screen and Dynamic Island. Bills stay visible without opening the app."
  - title: "31 recognized services, 10 categories"
    description: "Auto-fill for Netflix, Spotify, Disney+, YouTube Premium, Apple TV+, HBO Max, Amazon Prime, Crunchyroll, Apple Music, ChatGPT, Claude Pro, Adobe, Microsoft 365, Dropbox, Google One, iCloud, electricity, water, gas, internet, phone, car/health/home/life insurance, rent, mortgage, car payment, transit, gym, and student loans. English plus Finnish and German keywords matched. Anything outside the catalog takes about five seconds to add manually."
  - title: "Search, sort, share, and note"
    description: "Find any bill instantly with search. Sort by due date, amount, or name. Add notes for account numbers or payment confirmation IDs. Share a single bill with a partner or roommate via the share sheet — no shared account, no household sign-up."
  - title: "No bank login. Ever."
    description: "AllPaid does not connect to your bank. It does not use <a href=\"https://en.wikipedia.org/wiki/Plaid_(company)\" rel=\"noopener\" target=\"_blank\">Plaid</a> or any other bank-aggregation API. The trade-off is honest: you add bills manually (in seconds, from the catalog), and your bank credentials never touch this app or any server. If you'd rather have automatic detection and don't mind handing over a bank login, the <a href=\"/alternatives/rocket-money/\">Rocket Money comparison</a> walks through the trade-off in detail."

screenshots:
  - src: "/assets/screenshots/allpaid/1.png"
    alt: "AllPaid — monthly bill calendar on iPhone with upcoming due dates and a daily total for each day"
  - src: "/assets/screenshots/allpaid/en-US_1_1.png"
    alt: "AllPaid — bill list on iPhone showing Netflix, Spotify, rent, and utilities with next due dates"
  - src: "/assets/screenshots/allpaid/3.png"
    alt: "AllPaid — Pro spending analytics on iPhone showing category breakdown by streaming, subscriptions, housing, and utilities"
  - src: "/assets/screenshots/allpaid/4.png"
    alt: "AllPaid — bill detail view on iPhone with amount, monthly cycle, next due date, and one-tap mark-as-paid"

comparison_table:
  intro: "Each column below is a question someone shopping for a bill tracker actually asks. Rocket Money, Bobby, and What's Due all do something well — AllPaid is the choice when you want manual entry, no bank login, the lowest lifetime price, and analytics that stay on the device."
  competitors: ["AllPaid", "Rocket Money", "Bobby", "What's Due", "Spreadsheet"]
  rows:
    - feature: "Works without a bank login / Plaid"
      values: ["Yes — manual only", "No — Plaid required for detection", "Yes — manual only", "Yes — manual only", "Yes"]
    - feature: "Auto-fills 30+ common services (catalog)"
      values: ["Yes — 31 services", "Yes — from your transactions", "Manual entry", "Manual entry", "No"]
    - feature: "Monthly calendar view with daily totals"
      values: ["Yes", "Limited", "Limited", "Yes", "No"]
    - feature: "Spending analytics, category breakdown"
      values: ["Yes — Pro, on-device", "Yes — server-side", "Limited", "Limited", "Manual"]
    - feature: "One-time lifetime unlock available"
      values: ["$24.99 lifetime", "Subscription only ($6–12/mo)", "One-time pack (~$2.99)", "$59.99 lifetime", "n/a"]
    - feature: "Account / sign-up required"
      values: ["No", "Yes — bank credentials", "No", "No", "n/a"]
    - feature: "Zero third-party tracking SDKs"
      values: ["0", "Standard analytics + ads SDKs", "Standard analytics", "Standard analytics", "n/a"]
    - feature: "Bill negotiation service"
      values: ["No — out of scope", "Yes (paid, % of savings)", "No", "No", "No"]
    - feature: "Built-in subscription cancellation flow"
      values: ["No — out of scope", "Yes — Premium feature", "No", "No", "No"]
    - feature: "Catches forgotten / auto-renewing subscriptions you never entered"
      values: ["No — manual entry only", "Yes — from your transactions", "No", "No", "No"]
  footnote: "Competitor pricing and features reflect each app's public landing page and App Store description as of 2026-05. Rocket Money pricing is the publicly listed Premium range; the negotiation service is a separate fee. Apps change frequently — verify current pricing on the App Store before switching."

plateau_disclosure:
  title: "What AllPaid won't do for you"
  rule: "AllPaid is a manual bill tracker built around a 31-service catalog and a monthly calendar. It is deliberately not a full personal-finance app. The trade-off is what keeps it private, on-device, and one-time-priced."
  what_it_does_not_do: "AllPaid will not connect to your bank. It will not import transactions automatically. It will not negotiate bills down on your behalf. It will not scan your email for receipts. It will not warn you about price hikes for bills you didn't enter — if Spotify raises its price, AllPaid only knows once you update the amount yourself. It is not a budgeting app, an expense categorizer, or a household-finance dashboard."
  notes:
    - "Want automatic detection from your transactions? Try Rocket Money or Truebill — the trade-off is they need your bank login."
    - "Want bill negotiation as a service? Rocket Money offers it for a percentage of the savings."
    - "Want full budgeting (envelopes, transaction tagging, net worth)? YNAB, Monarch Money, or Copilot are better fits."
    - "Want the cheapest possible option with the most rigid privacy? A spreadsheet still works — AllPaid is for everyone who has tried a spreadsheet and given up after week three."

training_vocabulary:
  overline: "The 31-service catalog"
  heading: "The bills AllPaid already knows."
  intro: "AllPaid recognises 31 common services across 10 categories out of the box. Type the name, get the typical price, cycle, and category pre-filled. Matched in English, plus Finnish and German keywords for utilities and housing (sähkö, vesi, vuokra, strom, wasser, miete)."
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
        - "Student loan"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no trackers, no third-party SDKs"
    - "No account or sign-up required"
    - "No bank connection — AllPaid does not use Plaid or any bank-aggregation API"
    - "All bills, payments, and analytics stored locally on your device"
    - "See the per-app <a href=\"/transparency/#allpaid\">Privacy Manifest</a> for the declared API usage and tracking-domain list (it's empty)"

faq:
  - q: "What is AllPaid?"
    a: "AllPaid is a calm, privacy-first bill and subscription tracker for iPhone. It tracks bills, subscriptions, and due dates without any bank connection — manual entry plus a 31-service catalog that auto-fills price, cycle, and category. Includes a monthly calendar, gentle reminders, widgets, Siri, Live Activities, and on-device spending analytics. Free; Pro from $1.99/month or $24.99 lifetime."
  - q: "How does smart bill detection work?"
    a: "When you type a bill name — say 'Netflix' or 'ChatGPT' — AllPaid matches it against a built-in catalog of 31 recognized services and auto-fills the typical price, billing cycle, and category. Nothing leaves your device. The catalog covers streaming (Netflix, Spotify, Disney+, YouTube Premium, Apple TV+, HBO Max, Amazon Prime, Crunchyroll, Apple Music), AI tools (ChatGPT, Claude Pro), productivity (Adobe, Microsoft 365, Dropbox, Google One, iCloud), housing (rent, mortgage), utilities (electricity, water, gas), internet & phone, four kinds of insurance, transportation (car payment, transit), gym, and student loans. Matched in English plus Finnish and German keywords. For anything not in the catalog, type the name and amount manually — it takes about five seconds."
  - q: "How is AllPaid different from Rocket Money?"
    a: "Rocket Money connects to your bank, automatically detects subscriptions from your transaction history, and offers a paid negotiation service that takes a percentage of any savings it finds. AllPaid does none of that. You add bills manually (or via the 31-service catalog), nothing leaves your device, and there is no monthly fee for the core app. If automated detection from transactions matters more than privacy, Rocket Money fits better. If you would rather not give your bank login to a third-party app, AllPaid is built for you. See the full Rocket Money alternative comparison for the line-by-line breakdown."
  - q: "Does AllPaid catch free trials before they auto-renew?"
    a: "Only the ones you enter. AllPaid does not scan your email or transactions, so it cannot detect a trial you signed up for and forgot. What it can do: when you add a trial bill with the day it converts, AllPaid projects that date forward on the calendar and sends a gentle reminder the day before. Many users add a 'free trial — review by X' bill the moment they start a trial, and let AllPaid surface the deadline."
  - q: "What does the calendar actually show?"
    a: "Every bill projected forward on a monthly calendar — what's due, what's paid, and what's still coming. Each day shows a daily total. Heavy billing days (rent + utilities + four subscriptions all hitting the 1st) become visible weeks before they hit your bank account. You can scroll forward and look at the next 30, 60, or 90 days at a glance."
  - q: "Is AllPaid a budgeting app?"
    a: "No. AllPaid focuses specifically on bill tracking, subscription management, and payment reminders — not full budgeting or transaction categorization. There are no envelopes, no spending caps, and no automatic transaction tagging. If you want full budgeting, YNAB, Monarch Money, or Copilot are better fits."
  - q: "Is AllPaid free?"
    a: "Yes. Core bill tracking, the monthly calendar, reminders, widgets, Siri, and Live Activities are free. Pro unlocks unlimited bills, spending analytics (category breakdown, monthly trends, per-bill totals), multiple reminders per bill, and full payment history — $1.99/month or $24.99 lifetime. The $24.99 lifetime price is about 40% of what comparable iPhone bill trackers charge for a lifetime unlock."
  - q: "Does AllPaid work with Siri and widgets?"
    a: "Yes. Ask Siri what bills are due and get an instant answer. Home Screen widgets, Lock Screen widgets, and a full monthly-calendar widget all show upcoming bills without opening the app. Live Activities surface today's and tomorrow's bills on your Lock Screen and Dynamic Island."
  - q: "Does AllPaid share my financial data?"
    a: "No. AllPaid has no ads, no third-party trackers, no account requirement, no bank connection, and no data uploading. Your bill information stays entirely on your device. The Privacy Manifest declares zero tracking domains and no Required Reason APIs beyond the standard local-storage and notification permissions — see the full breakdown on the transparency page."
  - q: "Can I share bills with someone?"
    a: "Yes — one bill at a time, via the iOS share sheet. Useful for splitting rent, internet, or a streaming subscription with a partner or roommate. AllPaid does not require a shared account or a household sign-up — the share is per-bill, on your terms."

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
  value: "5.0"
  count: 3
  last_synced: "2026-05-17"
---
AllPaid is a calm, privacy-first bill and subscription tracker for iPhone. It is the bill tracker for people who refuse to hand a bank login to a third-party app. Bills are added manually or auto-filled from a built-in catalog of 31 common services across 10 categories — streaming (Netflix, Spotify, Disney+, YouTube Premium, Apple TV+, HBO Max, Amazon Prime, Crunchyroll, Apple Music), AI tools (ChatGPT, Claude Pro), productivity and cloud (Adobe, Microsoft 365, Dropbox, Google One, iCloud), housing (rent, mortgage), utilities (electricity, water, gas), internet and phone, four kinds of insurance, transportation, gym, and student loans. Matched in English plus Finnish and German keywords. A monthly calendar projects every recurring bill forward with daily totals — see bunched billing days weeks before they hit your account. Gentle reminders fire once before each due date with one-tap mark-as-paid from notifications, widgets, or Live Activities. Pro adds on-device spending analytics: category breakdown with percentages, monthly trend charts computed from your local payment history, per-bill totals, and unlimited bills. No ads, no trackers, no account, no Plaid, no bank connection. Free with optional Pro from $1.99/month or $24.99 lifetime — about 40% of what comparable iPhone bill trackers charge for a lifetime unlock.
