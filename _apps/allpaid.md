---
layout: app
slug: allpaid
name: "AllPaid"
tagline: "Bill and contract reminders for iPhone, with no bank login."
quick_answer: "AllPaid is a bill and contract reminder for iPhone that never asks for your bank login. You add rent, utilities, subscriptions, and contracts once, and AllPaid reminds you at 9:00 before each due date, moves a bill to its next date when you mark it paid, and reminds you before a contract ends. It is free for up to 3 bills; Pro adds unlimited bills, more reminders, Spending Analytics, payment history, and iCloud Sync for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once. There is no account and there are no ads, and your bills stay on your iPhone."
category: finance
status: live

app_store_url: "https://apps.apple.com/app/id6757253009"

price:
  model: freemium
price_tier: "Pro"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. For eligible Apple Accounts, Monthly starts with a {TRIAL} and Annual with a 7-day free trial. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew."

plans:
  - name: "Free"
    price: "$0"
    summary: "Three bills with reminders, contract tracking, every widget, and Face ID lock. Free for good."
    features:
      - "Track up to 3 bills"
      - "A reminder at 9:00 the day before each due date"
      - "Contract end dates with one renewal reminder"
      - "Spending overview: what your bills cost per month and per year"
      - "All ten widgets, Siri, and App Lock with Face ID"
      - "One attachment per bill"
  - name: "Pro · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Full Pro, billed monthly, starting with a {TRIAL}. Cancel anytime."
    features:
      - "Unlimited bills"
      - "Several reminders per bill, plus one on the due day"
      - "Spending Analytics by category, by bill, and by month"
      - "Full payment history, and any month in the monthly summary"
      - "Up to 50 attachments per bill"
      - "iCloud Sync through your own private iCloud"
      - "Family Sharing with up to 5 family members"
  - name: "Pro · Annual"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "Same Pro features, billed once a year, starting with a 7-day free trial. ~{SAVE_YEARLY}% cheaper than paying monthly."
    features:
      - "Everything in Pro · Monthly"
      - "~{SAVE_YEARLY}% cheaper than monthly over a year"
      - "Cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All Pro features for one payment."
    features:
      - "Everything in Pro · Annual"
      - "One-time purchase, no renewal"
      - "Family Sharing with up to 5 family members"
    highlight_label: "Pay once"

icon: "/assets/icons/allpaid.png"
og_image: "/assets/og/allpaid.png"

seo:
  title: "AllPaid: Bill Tracker for iPhone, No Bank Login"
  description: "Bill reminder app for iPhone with no bank login. Track due dates, subscriptions, and contract renewals. Free for 3 bills; {P_LIFETIME} lifetime option."
  keywords:
    - bill tracker app
    - bill tracker iPhone no bank login
    - bill reminder app
    - subscription tracker iPhone
    - bill due date reminder
    - contract renewal reminder
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
  pre_headline: "For rent, utilities, subscriptions, and contracts you pay by hand"
  headline: "Never forget a bill or a contract renewal, and keep your bank login to yourself."
  secondary: "A calm bill reminder for iPhone"
  subheadline: "Add a bill once. AllPaid reminds you at 9:00 on the days you choose, lets you mark it paid straight from the notification, and tells you before a contract ends and renews. Your bills stay on your iPhone, and Face ID can lock them."
  cta_label: "Download Free"
  alt: "AllPaid, a bill and contract reminder app for iPhone"

who_for:
  - "You pay rent, utilities, phone, insurance, or loans by hand and worry about missing one"
  - "You juggle subscriptions and contracts (broadband, phone, insurance, domains) and want to see the end date before an auto-renewal hits"
  - "You won't connect your bank account to a third-party app through Plaid, and you don't want another sign-up"
  - "You split a bill with a flatmate or partner and want to send them a note when it's due"
  - "You want one Pro purchase to cover your household through Family Sharing"

who_not_for:
  - "You want full budgeting with bank connections and automatic transaction categorization"
  - "You run a business and need double-entry accounting"
  - "You want several people managing the same household bills together"
  - "You want a paid service to negotiate your bills down for you"
  - "You need the app on iPad, Mac, or Apple Watch (AllPaid is an iPhone app)"

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
  story: "AllPaid is for people who won't give a bill tracker their bank login. When an app links your bank through an aggregator such as Plaid, it can usually read every transaction in the account, which is far more than anyone needs to remember that rent is due. So AllPaid works from what you type in. You add each bill once, and the app handles the rest: the reminder, the next due date, and the contract that is about to renew. There is no account, and the app sends nothing to us. The trade-off is real. AllPaid can't find a forgotten subscription you never entered. Everything you do enter stays on your iPhone, or in your own iCloud if you turn on iCloud Sync with Pro."
  signals:
    - "Bills stay on your iPhone; optional iCloud Sync (Pro) uses your own private iCloud, which we have no access to"
    - "Built on Apple frameworks only, with no analytics, ad, or third-party SDKs"
    - "Paid for by the people who buy Pro, with no ads and no investors"
    - "{APP_COUNT} live apps in the catalogue, all following the same data rules: no tracking, no ads, no required accounts"
  external_link:
    label: "Read the Lagerland studio backstory →"
    href: "/lagerland-apps/"
  support_email: "support@lagerland.app"
  response_time: "Support emails go to one inbox and are answered personally, usually within a day."

value_points:
  - title: "Reminders that fit the bill"
    description: "The \"days before\" choices change with how often a bill repeats, so AllPaid only offers reminders that can actually fire. Each one arrives at 9:00, and you can mark the bill paid or snooze it from the notification."
  - title: "Contract renewals you see coming"
    description: "Add a contract's start and end dates, whether it auto-renews, and the renewal amount. AllPaid reminds you before it ends, so you can cancel or renegotiate before the new price starts."
  - title: "Your bank login stays out of it"
    description: "AllPaid doesn't connect to a bank and doesn't ask you to sign up. Your bills stay on your iPhone, and App Lock can put them behind Face ID, Touch ID, or your passcode."
  - title: "A lifetime option for Pro"
    description: "Free covers three bills and all ten widgets. Pro is {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once, and one purchase covers up to five family members through Family Sharing. No subscription required."

how_it_works:
  intro: "AllPaid works from what you enter. It never connects to a bank, so every bill starts with you adding it once. This is how a bill moves through the app."
  steps:
    - title: "Add the bill"
      detail: "Give it a name, a due date, and how often it repeats: one-time, weekly, bi-weekly, monthly, quarterly, semi-annual, yearly, or every N days, weeks, or months. The amount is optional. Type a familiar name and AllPaid suggests the category and repeat (\"Looks like Netflix\"); tap Apply to use them. Popular providers show their real logo. Free holds 3 bills; Pro has no limit."
    - title: "Choose when to be reminded"
      detail: "Reminders arrive at 9:00. Free reminds you the day before each due date. Pro lets you pick several days before, from choices that fit the bill's repeat, plus a reminder on the due day. From the notification you can mark the bill paid, or choose Remind in 2 hours or Remind tomorrow."
    - title: "Mark it paid"
      detail: "Tap Mark paid in the list, on the bill, or in the notification. A recurring bill moves to its next due date and a one-time bill moves to Paid. Undo is one tap away. If an amount changes from month to month, AllPaid can ask what you actually paid. Bills you flag as Auto-pay move forward on their own after the charge date, with a heads-up instead of a reminder to pay."
    - title: "Track the contract behind it"
      detail: "Turn on Track contract end date to add the start and end dates, Auto-renews if not cancelled, the renewal amount, the provider, and notes. A progress bar shows how far through the contract you are, and a reminder at 10:00 comes before it ends. When it renews, Mark as renewed files the old period under Past Renewals and moves the end date forward."
    - title: "Keep the paperwork with it"
      detail: "Attach the PDF contract, a receipt, or a photo of a letter to the bill it belongs to, from Files or Photos. Free keeps one attachment per bill; Pro keeps up to 50."
    - title: "See what your bills cost"
      detail: "The free Spending overview shows the monthly and yearly cost of your recurring bills, split by bill and category, with this month's total due, paid, and remaining. Pro adds Spending Analytics with a monthly trend, full payment history, and any past or future month in the monthly summary."
    - title: "Keep it on your iPhone"
      detail: "There is no account and nothing is uploaded to us. Bills, payments, and attachments live on your iPhone. App Lock asks for Face ID, Touch ID, or your passcode. With Pro, iCloud Sync copies your bills to your own private iCloud. See the per-app <a href=\"/transparency/#allpaid\">transparency entry</a> for third-party SDKs and tracking domains (there are none)."

example_insights:
  overline: "What AllPaid says, word for word"
  heading: "What AllPaid tells you, and when."
  intro: "AllPaid keeps its wording plain. These are the lines you see in the app, and what each one means."
  cards:
    - tag: "Reminder"
      headline: "\"Bill due soon\""
      body: "Arrives at 9:00 before the due date. Free sends it the day before; Pro can send it on several days you pick and adds \"Bill due today\" on the day itself. Mark the bill paid from the notification, or choose Remind in 2 hours or Remind tomorrow."
    - tag: "Contract"
      headline: "\"Contract ending soon\""
      body: "Arrives at 10:00 before a contract's end date. If you renewed, tap Mark as renewed and the old period moves to Past Renewals. If you need more time to decide, choose Remind in 1 week."
    - tag: "Auto-pay"
      headline: "\"Auto-pay coming up\""
      body: "For bills you flag as Auto-pay, such as a direct debit. You get a heads-up instead of a reminder to pay, and the bill moves to its next date on its own once the charge date passes."
    - tag: "Bills list"
      headline: "\"Due date passed\""
      body: "This is what a missed bill says in AllPaid; there is no red overdue state. When everything is settled, the list reads \"All bills paid\", and after a run of paid months it adds \"On track for\" and the number of months."

features:
  - title: "Mark paid from the notification"
    description: "Tap Mark paid in the app or on the reminder itself. A recurring bill moves to its next due date, and Undo takes it back if you tapped too soon."
  - title: "Contract end dates and renewals"
    description: "Track when a contract started and ends, whether it auto-renews, and what it will cost after renewal. A reminder comes before the end date, and the list shows contracts ending soon. Pro allows several reminders per contract."
  - title: "Ten widgets"
    description: "Next Bill, Monthly Calendar, Contracts, Horizon, Paid Rhythm, Coming Up, Week Ahead, Month Progress, Recurring Bills, and a Lock Screen version of Next Bill, with extra-large layouts on iOS 27. All ten are free; Paid Rhythm and Horizon show older months with Pro. Tap a widget to open the right screen."
  - title: "Documents attached to the bill"
    description: "Keep the PDF contract, the receipt, or a photo of the policy with the bill it belongs to, and preview it in the app. One attachment per bill on Free, up to 50 on Pro."
  - title: "Spending overview and Spending Analytics"
    description: "The free Spending overview shows what your recurring bills cost per month and per year, by bill and by category, across 19 categories. Spending Analytics (Pro) adds totals, the average per month, and a monthly trend, and Pro keeps the full payment history."
  - title: "Auto-pay bills"
    description: "Flag a direct debit as Auto-pay. AllPaid sends \"Auto-pay coming up\" instead of a reminder to pay and moves the bill forward on its own. A list filter shows or hides auto-pay bills."
  - title: "Siri, iOS Search, and Face ID"
    description: "Ask Siri \"What bills are due in AllPaid\" and it reads out the bills due in the next seven days. iOS Search finds any bill by name. App Lock opens AllPaid only with Face ID, Touch ID, or your passcode."
  - title: "Search, sort, share, and notes"
    description: "Search finds any bill, and you can sort by due date, name, or amount. Notes hold account numbers or confirmation IDs. Share bill sends a short message about a bill to a partner or flatmate through the share sheet."
  - title: "In 37 languages"
    description: "The app, its widgets, and its permission prompts are translated into 37 languages. Choose light or dark, or follow your iPhone's setting."
  - title: "No bank login"
    description: "AllPaid does not connect to your bank and does not use <a href=\"https://en.wikipedia.org/wiki/Plaid_(company)\" rel=\"noopener\" target=\"_blank\">Plaid</a> or any other bank-aggregation API. You add bills yourself, and your bank credentials never touch the app. If you'd rather have automatic detection and don't mind handing over a bank login, the <a href=\"/alternatives/rocket-money/\">Rocket Money comparison</a> walks through the trade-off in detail."

screenshots:
  - src: "/assets/screenshots/allpaid/1.webp"
    alt: "AllPaid bills list on iPhone with upcoming bills, amounts and mark-as-paid buttons"
  - src: "/assets/screenshots/allpaid/2.webp"
    alt: "AllPaid analytics screen with total spending and a category donut chart"
  - src: "/assets/screenshots/allpaid/3.webp"
    alt: "AllPaid monthly summary with a due-date calendar, paid and remaining totals"
  - src: "/assets/screenshots/allpaid/4.webp"
    alt: "AllPaid lock screen notification reminding that a bill is due tomorrow"
  - src: "/assets/screenshots/allpaid/5.webp"
    alt: "AllPaid Home Screen widgets with a month calendar and upcoming bills"
  - src: "/assets/screenshots/allpaid/6.webp"
    alt: "AllPaid extra-large calendar widget showing bills due across a month"
  - src: "/assets/screenshots/allpaid/7.webp"
    alt: "AllPaid extra-large Horizon widget listing bills due this week with a running total"
  - src: "/assets/screenshots/allpaid/8.webp"
    alt: "AllPaid extra-large Paid Rhythm widget showing a year of paid bills as a heatmap"

comparison_table:
  intro: "Each row answers a question people ask when shopping for a bill tracker. Rocket Money, Bobby, and What's Due each do something well. AllPaid fits when you want manual entry, no bank login, a lifetime option, and analytics that stay on the device."
  competitors: ["AllPaid", "Rocket Money", "Bobby", "What's Due", "Spreadsheet"]
  rows:
    - feature: "Works without a bank login / Plaid"
      values: ["Yes, manual only", "No, Plaid required for detection", "Yes, manual only", "Yes, manual only", "Yes"]
    - feature: "Monthly calendar of due dates"
      values: ["Yes, month summary and Monthly Calendar widget", "Limited", "Limited", "Yes", "No"]
    - feature: "Spending analytics, category breakdown"
      values: ["Yes, Pro, on-device", "Yes, server-side", "Limited", "Limited", "Manual"]
    - feature: "One-time lifetime unlock available"
      values: ["{P_LIFETIME} lifetime", "Subscription only", "One-time purchase", "Yes, lifetime option", "n/a"]
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
  footnote: "Competitor pricing and features reflect each app's public landing page and App Store description as of 2026-05. Rocket Money's negotiation service is a separate fee. Apps change often, so check current pricing on the App Store before switching."

plateau_disclosure:
  title: "What AllPaid won't do for you"
  rule: "AllPaid is a bill and contract reminder that works from what you enter. It is deliberately not a full personal-finance app, and that limit is what keeps your bills private and on your iPhone."
  what_it_does_not_do: "AllPaid will not connect to your bank, import transactions, pay bills, negotiate them down, or scan your email for receipts. It will not notice a price rise until you update the amount. It has no budgets, income tracking, export, or currency conversion. Reminders come at a set time, 9:00 for bills and 10:00 for contracts."
  notes:
    - "Want automatic detection from your transactions? Try Rocket Money or Truebill, which need your bank login to do it."
    - "Want bill negotiation as a service? Rocket Money offers it for a percentage of the savings."
    - "Want full budgeting (envelopes, transaction tagging, net worth)? YNAB, Monarch Money, or Copilot are better fits."
    - "Want the strictest privacy for free? A spreadsheet still works. AllPaid is for people who want the reminder a spreadsheet can't send."

training_vocabulary:
  overline: "What AllPaid knows about bills"
  heading: "Built around how bills are actually billed."
  intro: "The categories, repeat options, contract fields, and widgets below are the ones you see in the app."
  groups:
    - heading: "19 categories"
      items:
        - "Streaming · Subscriptions · Entertainment"
        - "Utilities · Internet & Phone · Housing"
        - "Insurance · Transportation · Health & Fitness"
        - "Credit card · Loans · Taxes · Savings"
        - "Groceries · Education · Childcare · Pets"
        - "Charity · Other"
    - heading: "Repeat options"
      items:
        - "One-time"
        - "Weekly · Bi-weekly"
        - "Monthly · Quarterly"
        - "Semi-annual · Yearly"
        - "Every N days, weeks, or months"
    - heading: "Contract details"
      items:
        - "Start date · End date"
        - "Auto-renews if not cancelled"
        - "Renewal amount · Provider · Notes"
        - "Mark as renewed · Past Renewals"
    - heading: "Ten widgets"
      items:
        - "Next Bill · Next Bill (Lock Screen)"
        - "Monthly Calendar · Contracts"
        - "Horizon · Paid Rhythm"
        - "Coming Up · Week Ahead"
        - "Month Progress · Recurring Bills"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, analytics, or third-party SDKs in the app"
    - "No account or sign-up required"
    - "No bank connection: AllPaid does not use Plaid or any bank-aggregation API"
    - "Bills, payments, and attachments are stored on your iPhone; optional iCloud Sync (Pro) uses your own private iCloud"
    - "See the per-app <a href=\"/transparency/#allpaid\">transparency entry</a> for third-party SDKs and tracking domains (there are none)"

faq:
  - q: "What is AllPaid?"
    a: "AllPaid is a bill and contract reminder for iPhone that works without a bank connection. You add bills, subscriptions, and contracts by hand; AllPaid reminds you at 9:00 before each due date, lets you mark a bill paid from the notification, and reminds you before a contract ends. It also has ten widgets, Siri, App Lock with Face ID, and a spending overview. It is free for up to 3 bills; Pro costs {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once."
  - q: "Does AllPaid fill in bills automatically?"
    a: "Partly. AllPaid never reads your bank, so it can't find bills on its own; you add each one by hand. When you type a familiar name such as Netflix, it suggests the category and how often the bill repeats, and you tap Apply to use them. Popular providers also show their real logo. The amount is optional, so you can add a bill even when it changes from month to month."
  - q: "How is AllPaid different from Rocket Money?"
    a: "Rocket Money connects to your bank, detects subscriptions from your transaction history, and offers a paid negotiation service that takes a percentage of any savings it finds. AllPaid does none of that. You add bills yourself, nothing leaves your iPhone unless you turn on iCloud Sync, and AllPaid is free for 3 bills with a one-time lifetime option for Pro. If automatic detection from transactions matters more to you than privacy, Rocket Money fits better. If you would rather not give your bank login to a third-party app, AllPaid is the better choice. The full Rocket Money alternative comparison goes through it line by line."
  - q: "Can AllPaid remind me before a contract renews?"
    a: "Yes. Turn on Track contract end date for a bill and add the start and end dates, whether it auto-renews, and the renewal amount. AllPaid reminds you at 10:00 before the end date, and the list shows contracts ending soon. If you renew, Mark as renewed keeps the old period under Past Renewals and moves the end date forward. Free allows one reminder per contract; Pro allows several."
  - q: "Does AllPaid catch free trials before they auto-renew?"
    a: "Only the ones you enter. AllPaid does not scan your email or transactions, so it can't find a trial you signed up for and forgot. Add the trial as a bill due on the day it converts, or as a contract that ends that day, and AllPaid reminds you before the date."
  - q: "Does AllPaid show my bills on a calendar?"
    a: "Yes. The Monthly Calendar widget shows all of the month's bills on your Home Screen, and the monthly summary in the app lists the month's bills and totals. Free shows the current month; with Pro you can step through past and future months."
  - q: "Is AllPaid a budgeting app?"
    a: "No. AllPaid covers bill tracking, subscriptions, contracts, and payment reminders. It does not do full budgeting, income tracking, or transaction categorization. If you want full budgeting, YNAB, Monarch Money, or Copilot are better fits."
  - q: "Is AllPaid free?"
    a: "Yes. Free tracks up to 3 bills with a reminder the day before each one, contract end dates, the spending overview, all ten widgets, Siri, and App Lock. Saving a fourth bill opens the Pro screen. Pro unlocks unlimited bills, several reminders per bill plus due-day reminders, Spending Analytics, full payment history, up to 50 attachments per bill, and iCloud Sync for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once. If your Apple Account is eligible, the monthly plan starts with a {TRIAL} and the yearly plan with a 7-day free trial. One Pro purchase covers up to 5 family members through Family Sharing. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does AllPaid work with Siri and widgets?"
    a: "Yes. Ask Siri \"What bills are due in AllPaid\" and it reads out the bills due in the next seven days. AllPaid has ten Home Screen and Lock Screen widgets, including Next Bill, Monthly Calendar, Coming Up, and Contracts, with extra-large layouts on iOS 27. Widgets open the app; they can't mark a bill paid."
  - q: "Does AllPaid work on iPad, Mac, or Apple Watch?"
    a: "No. AllPaid is an iPhone app and needs iOS 17 or later. There is no iPad, Mac, or Apple Watch version."
  - q: "Does AllPaid share my financial data?"
    a: "No. AllPaid has no server of its own to upload to, never connects to a bank, and carries no analytics, ad, or third-party SDKs. You don't create an account to use it. Your bills stay on your iPhone or, if you turn on iCloud Sync (Pro), in your own private iCloud, which we can't access. App Lock can require Face ID, Touch ID, or your passcode to open the app. The transparency page has the full breakdown."
  - q: "Can I share bills with someone?"
    a: "You can send one. Share bill opens the iOS share sheet with a short message about the bill and when it's due, which works for reminding a partner or flatmate about rent or internet. The other person doesn't get access to your bills, and AllPaid has no shared household account."
  - q: "Can I export my bills?"
    a: "No. AllPaid has no CSV, PDF, or calendar export. With Pro, iCloud Sync keeps a copy of your bills in your own private iCloud."

related_journal:
  slug: i-will-not-ask-for-your-bank-login
  anchor: "Why AllPaid will never ask for your bank login"

support:
  email: "support@lagerland.app"
  url: "/apps/allpaid/support/"

release:
  first_release: "2026-01-01"
  last_updated: "2026-05-13"
  last_audited: "2026-05-13"

ratings:
  value: "4.9"
  count: 7
  last_synced: "2026-10-19"
last_updated: 2026-10-30
---
AllPaid is a bill and contract reminder for iPhone, made for people who won't hand a bank login to a third-party app. You add each bill by hand with its due date and how often it repeats, from one-time to yearly or every N days, weeks, or months. Type a familiar name and AllPaid suggests the category and repeat. Reminders arrive at 9:00 before the due date, and you can mark a bill paid or snooze it straight from the notification. Contracts get their own fields: start and end dates, auto-renewal, and the renewal amount, with a reminder before the contract ends. PDFs and photos attach to the bill they belong to. The free Spending overview shows what your bills cost per month and per year; Pro adds Spending Analytics, full payment history, unlimited bills, and iCloud Sync through your own private iCloud. AllPaid has ten widgets, works with Siri, locks with Face ID, and is translated into 37 languages. It has no ads and no account, and it never connects to a bank. It is free for up to 3 bills, with Pro from {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once.
