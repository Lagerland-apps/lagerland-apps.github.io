---
layout: app
slug: appmeta-pulse
name: "AppMeta Pulse"
tagline: "Your App Store sales, subscriptions, and reviews on your iPhone, with the history kept."
quick_answer: "AppMeta Pulse is an iPhone app for indie developers who sell on the App Store: it shows proceeds, MRR, subscribers, trials, and reviews for all your apps from App Store Connect, and keeps every day it fetches on your iPhone after Apple's roughly one-year window has passed. You can answer reviews one at a time or up to 25 at once, with reply drafts written on-device by Apple Intelligence (iOS 26 on a supported iPhone, English drafts), and follow the month on 12 Home Screen and Lock Screen widgets. It needs an App Store Connect API key with the Admin role, which stays in your iPhone's Keychain, and it carries no ads, tracking, or third-party analytics. The free download opens a demo on sample data; your own numbers cost {P_MONTHLY}/month or {P_YEARLY}/year, each starting with a {TRIAL}, or {P_LIFETIME} once."
category: business
status: live

app_store_url: "https://apps.apple.com/app/id6758788164"

price:
  model: subscription
price_lead: "Free trial"
price_tier: "Pro"
free_tier: false

# Enable in-page "Jump to" anchor nav (renders only when sections exist).
jump_nav: true

# Structured pricing tiers, from the live App Store In-App Purchases list
# (US, UK, Canada, Australia, euro and other storefronts checked 2026-10-25):
# monthly, yearly and lifetime (prices from _data/catalog.json). The free download only opens a demo
# on sample data; your own numbers need a subscription or Lifetime.
plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew. You create the App Store Connect API key (.p8) yourself in App Store Connect under Users and Access, Integrations, with the Admin role, and it is stored in this iPhone's Keychain. The API access page lists the endpoints the app calls."

plans:
  - name: "Free download"
    price: "$0"
    summary: "Try the app on sample data before you pay. Your own numbers need Pro or Lifetime."
    features:
      - "Demo with five sample apps and 455 days of sample data, for up to 3 days of use"
      - "Connect your own App Store Connect API key (Admin role) once you subscribe or buy Lifetime"
      - "iPhone only, iOS 17 or later"
  - name: "Pro"
    price: "{P_MONTHLY} / mo · {P_YEARLY} / yr"
    kind: monthly
    summary: "Every feature on your own App Store Connect data, billed monthly or yearly. Each plan starts with a {TRIAL}; cancel anytime."
    features:
      - "Proceeds or sales, units, MRR, subscribers, trials, and churn for every app"
      - "Sales history kept on your iPhone, with year-over-year comparison as it grows"
      - "Read, translate, and answer reviews, up to 25 at once, with on-device reply drafts"
      - "12 Home Screen and Lock Screen widgets"
      - "Optional iCloud Sync across your iPhones"
      - "Yearly saves about {SAVE_YEARLY}% against paying monthly"
  - name: "Lifetime"
    price: "{P_LIFETIME} one-time"
    kind: lifetime
    summary: "Every Pro feature for one payment."
    highlight_label: "One-time purchase"
    features:
      - "Everything in Pro, unlocked for good"
      - "One payment, with no renewal"
      - "Restore it on another iPhone with Restore Purchases"

icon: "/assets/icons/appmeta-pulse.png"
og_image: "/assets/og/appmeta-pulse.png"

seo:
  title: "AppMeta Pulse: App Store Connect Dashboard for iPhone"
  description: "App Store Connect dashboard for iPhone: proceeds, MRR, and reviews for every app, sales history kept past Apple's one year, and 12 widgets."
  keywords:
    - App Store Connect iPhone app
    - App Store Connect dashboard iPhone
    - app store revenue tracker iPhone
    - indie iOS developer dashboard
    - app store analytics iPhone
    - AppStats alternative
    - App Sales alternative
    - Appfigures alternative iPhone
    - subscription metrics iPhone
    - app store downloads tracker
    - app store proceeds tracker
    - app store connect companion
    - sales and trends iPhone
    - app store sales history
    - reply to app store reviews iPhone
    - app store connect widgets
    - indie developer revenue iPhone
    - app store connect API client
    - app store subscription dashboard
    - app store mrr tracker

hero:
  pre_headline: "For indie developers who sell apps and subscriptions on the App Store"
  headline: "Your whole App Store business on your iPhone, kept for good."
  secondary: "App Store Connect serves about a year of daily sales. AppMeta Pulse stores every day it fetches on your iPhone, so year-over-year comparison fills in as your history grows."
  subheadline: "Proceeds, MRR, subscribers, and reviews for every app you sell, on 12 Home Screen and Lock Screen widgets. Answer reviews from your phone, with reply drafts written on-device by Apple Intelligence."
  cta_label: "Download Free"
  alt: "AppMeta Pulse App Store Connect dashboard on iPhone, showing seven days of proceeds, units, new subscriptions, and monthly subscription revenue across a multi-app portfolio"

who_for:
  - "You sell apps or subscriptions on the App Store and check your numbers more often than you open App Store Connect"
  - "You want sales history that doesn't stop at Apple's one-year window, and a fair year-over-year comparison"
  - "You answer App Store reviews and would rather do it from your phone, in bulk when they pile up"
  - "You want this month's pace on your Home Screen without opening an app"
  - "You'd rather your API key and your numbers didn't pass through someone else's server"

who_not_for:
  - "You want an alert the moment a sale comes in; AppMeta Pulse sends no notifications"
  - "You want it on iPad or Mac; AppMeta Pulse runs on iPhone only"
  - "You can't create an Admin API key; App Manager and Developer keys can't read sales reports"
  - "You want to edit your listing, in-app purchases, or TestFlight. Our Mac app AppMeta does that"

related_journal:
  slug: "app-store-proceeds-vs-sales"
  anchor: "App Store proceeds vs sales: what each money column in App Store Connect means"
alternatives_to:
  - "AppStats"
  - "App Sales - Store Reports"
  - "Appfigures"
  - "App Store Connect (official Apple app)"
  - "RevenueCat"

value_points:
  - title: "History that outlasts App Store Connect"
    description: "Apple serves about a year of daily sales. AppMeta Pulse keeps every day it fetches on your iPhone until you delete it, plus an original copy of each report Apple sends. Once a full year is stored, Trends compares this year with last year."
  - title: "Reviews answered from your phone"
    description: "Every app's reviews in one list, unanswered low-star ones first. Translate foreign-language reviews on the device, then reply one by one or to up to 25 at once. On iOS 26 with Apple Intelligence on a supported iPhone, the app writes two English drafts on the device for you to edit and send."
  - title: "12 widgets, four of them for the month"
    description: "Proceeds, subscriptions, and reviews on the Home Screen and Lock Screen. Pace, Ledger, Shape, and Where It Moved show how the week or month is going and which app moved the number."
  - title: "Your key stays on your iPhone"
    description: "The .p8 key lives in this iPhone's Keychain and never syncs, even with iCloud Sync on. Requests go from your iPhone to Apple. There is no AppMeta Pulse server in between."

features:
  - title: "Dashboard"
    description: "Proceeds or sales for the latest day or the last 7, 30, 60, or 90 days, with the change against the period before. Units and new subscribers sit next to it, with MRR, active subscriptions, and active trials below. A footer tells you whether Sales, Subscriptions, and Analytics are up to date."
  - title: "Subscriptions"
    description: "Active subscribers, trials, churn, and MRR, per app or across all of them, with a By Product table and charts for 30, 60, or 90 days. Recent activity lists new, converted, and cancelled subscriptions."
  - title: "Trends and year over year"
    description: "Compare 7, 30, or 90 days, the year to date, or a custom length with the previous period or with last year, across Sales, Proceeds, Units, Subs, IAPs, MRR, and Updates. By Year shows downloads per year from Apple's yearly reports, and By Territory an app's top eight countries."
  - title: "Every app side by side"
    description: "A searchable list of your apps with the latest day, units, a 7-day total, and a sparkline. Open one for its chart against the previous period, its top five territories, and its reviews."
  - title: "App Store funnel"
    description: "Impressions, product page views, downloads, and conversion rate, with a rolling 14-day conversion chart. Apple's analytics arrive about two days after the day they cover."
  - title: "Reviews, replies, and templates"
    description: "Filter reviews by app, stars, sentiment, or reply status. Sentiment and recurring phrases are worked out on the device. Write, edit, or delete your public responses, save reusable templates, and reply to up to 25 unanswered reviews in one go."
  - title: "iCloud Sync and a second iPhone"
    description: "Optional iCloud Sync keeps history, reviews, settings, and templates on all your iPhones through your private iCloud. Another iPhone on the same Apple Account can show your numbers without the API key stored on it."
  - title: "Your currency, your language"
    description: "Amounts convert to your currency with the European Central Bank's monthly average rates, so treat them as estimates. Switch between several App Store Connect accounts, export sales to CSV, and use the app in 17 languages besides English."

screenshots:
  - src: "/assets/screenshots/appmeta-pulse/1.webp"
    alt: "AppMeta Pulse dashboard on iPhone showing proceeds and subscription status"
  - src: "/assets/screenshots/appmeta-pulse/2.webp"
    alt: "AppMeta Pulse 30-day trends widget for the Home Screen and Lock Screen"
  - src: "/assets/screenshots/appmeta-pulse/3.webp"
    alt: "AppMeta Pulse drafting a reply to a 1-star App Store review on device"
  - src: "/assets/screenshots/appmeta-pulse/4.webp"
    alt: "AppMeta Pulse apps list with proceeds and a 7-day trend for each app"
  - src: "/assets/screenshots/appmeta-pulse/5.webp"
    alt: "AppMeta Pulse analytics comparing this year with last year"
  - src: "/assets/screenshots/appmeta-pulse/6.webp"
    alt: "AppMeta Pulse subscription metrics: MRR, trials and churn"
  - src: "/assets/screenshots/appmeta-pulse/7.webp"
    alt: "AppMeta Pulse app analytics showing impressions, page views and downloads"
  - src: "/assets/screenshots/appmeta-pulse/8.webp"
    alt: "AppMeta Pulse feature summary for indie developers: iCloud sync, multiple teams, goals and shortcuts"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no tracking, and no third-party analytics or SDKs"
    - "No AppMeta Pulse server: requests go from your iPhone to Apple, and exchange rates come from the European Central Bank"
    - "The App Store Connect API key (.p8) stays in this iPhone's Keychain and never syncs"
    - "The only writes to App Store Connect are review replies you send and analytics report requests"
    - "Reply drafts, sentiment, and translation run on the device"
    - "iCloud Sync is optional and stores your data in your own private iCloud database"

faq:
  - q: "What is AppMeta Pulse?"
    a: "AppMeta Pulse is an iPhone app that shows your App Store sales, subscriptions, and reviews from App Store Connect. It covers proceeds or sales, units, MRR, subscribers, trials, churn, and the App Store funnel for every app you sell, keeps your sales history on your iPhone after Apple's one-year window has passed, and lets you reply to reviews. It has 12 Home Screen and Lock Screen widgets. It can't change your prices, builds, or metadata."

  - q: "How far back does AppMeta Pulse keep my sales history?"
    a: "From the first day it fetches, for as long as you keep it. App Store Connect serves about the last 365 days of daily sales, so on first connect AppMeta Pulse fetches what Apple still has and then stores every new day on your iPhone. History is cleared only when you delete it or sign out. Year-over-year comparison appears once a full prior-year window is stored; until then Trends tells you the month it becomes available. Downloads per year can reach back further, up to 10 years, because they come from Apple's yearly reports."

  - q: "How is AppMeta Pulse different from AppStats, App Sales, or Appfigures?"
    a: "The comparison pages go app by app: <a href=\"/alternatives/appstats/\">AppStats</a>, <a href=\"/alternatives/app-sales-store-reports/\">App Sales - Store Reports</a>, and <a href=\"/alternatives/appfigures/\">Appfigures</a>. What AppMeta Pulse brings to that comparison: sales history kept on your iPhone past Apple's one-year window, review replies with on-device Apple Intelligence drafts and bulk reply for up to 25 reviews, 12 widgets including four for the week's or month's pace, and no server of ours between your iPhone and Apple."

  - q: "How is AppMeta Pulse different from the official App Store Connect app?"
    a: "Apple's <a href=\"https://apps.apple.com/us/app/app-store-connect/id1234793120\" rel=\"noopener\">App Store Connect app</a> is for running your account. AppMeta Pulse is for following the business: it keeps your sales history after Apple's one-year window has passed, compares this year with last year, puts proceeds, subscriptions, and pace on 12 widgets, and drafts review replies on the device. It can't change your prices, builds, or metadata. The only things it sends to App Store Connect are the review replies you write and the analytics report requests Apple needs. <a href=\"/alternatives/app-store-connect-app/\">The full comparison</a> goes feature by feature."

  - q: "What's the difference between sales and proceeds in App Store Connect?"
    a: "<em>Sales</em> is the gross amount customers paid before Apple's commission. <em>Proceeds</em> is what Apple owes you after its 15% (Small Business Program) or 30% (standard) cut and any VAT or sales tax it collects. The payment that reaches your bank can still differ from your proceeds, because of currency conversion, withholding tax, and bank fees. In AppMeta Pulse, the Show Amount setting switches every figure between proceeds and sales. See Apple's reference on <a href=\"https://developer.apple.com/help/app-store-connect/view-sales-and-trends/view-units-proceeds-sales-and-pre-orders/\" rel=\"noopener\">units, proceeds, and sales</a> for the official definitions."

  - q: "Does AppMeta Pulse use the App Store Connect API or the web dashboard?"
    a: "The official <a href=\"https://developer.apple.com/documentation/appstoreconnectapi\" rel=\"noopener\">App Store Connect API</a>. You create an API key with the Admin role in App Store Connect under Users and Access, Integrations, download the .p8 private key, and add the key file, Key ID, and Issuer ID to AppMeta Pulse, along with your Vendor Number for the sales reports. The key is stored in this iPhone's Keychain. AppMeta Pulse never reads the web dashboard. See <a href=\"/apps/appmeta-pulse/api-access/\">the API access page</a> for the exact endpoints, the role the key needs, and how the tokens are signed."

  - q: "What permissions does AppMeta Pulse request on my App Store Connect account?"
    a: "An API key with the Admin role, the role that can read sales reports; App Manager and Developer keys get a 403 error from Apple. AppMeta Pulse uses the key to read your sales and subscription reports, your app list, App Store analytics, and customer reviews. The only things it writes are the review replies you choose to send, edit, or delete, and the analytics report requests Apple needs before it prepares impressions data. It can't change your prices, builds, or metadata. You can revoke the key in App Store Connect at any time. <a href=\"/apps/appmeta-pulse/api-access/\">The API access page maps each role to its endpoints.</a>"

  - q: "How fresh is the data? Is it real-time?"
    a: "As fresh as Apple makes it. Apple publishes each day's sales report the following day, and App Store analytics such as impressions arrive about two days later. AppMeta Pulse refreshes in the background about once an hour, with iOS deciding the exact timing, and again when you open the app. The widgets update after each sync. It can't get Apple's data any faster than Apple publishes it, and the Dashboard footer shows whether each source is up to date."

  - q: "Can AppMeta Pulse draft replies to App Store reviews?"
    a: "Yes, on iOS 26 or later with Apple Intelligence on a supported iPhone. The reply composer offers two drafts written on the device, one apologetic and technical, one empathetic and supportive, and you edit and send. Drafts are in English. On any iPhone you can write replies yourself, insert a saved template, translate a foreign-language review on the device (iOS 18 or later), and answer up to 25 unanswered reviews at once with a template, a draft per review, or the same text. Nothing is posted until you send it."

  - q: "Can I see revenue by country?"
    a: "Yes. Each app's detail view lists its top five territories, and Trends shows the top eight countries for one app on sales or proceeds. Country detail is kept for 456 days; daily totals are kept in full. The figures come from Apple's daily sales reports, so reconcile payouts against the <a href=\"https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports/\" rel=\"noopener\">monthly financial reports</a> in App Store Connect."

  - q: "Is AppMeta Pulse safe for my credentials?"
    a: "The .p8 key and Key ID are stored in this iPhone's Keychain, available only on this device, and they never sync, even with iCloud Sync on. Requests go over HTTPS straight to Apple's API; nothing passes through a Lagerland Apps server. You can revoke the key in App Store Connect at any time."

  - q: "Can I accidentally change app settings?"
    a: "No. AppMeta Pulse can't change your prices, builds, or metadata, and it has no buttons for them. The one thing you can change is a review reply: you write it, tap send, and can edit or delete it later."

  - q: "Is AppMeta Pulse free?"
    a: "The download is free and opens a demo with five sample apps, for up to 3 days of use. To see your own numbers you need Pro at {P_MONTHLY}/month or {P_YEARLY}/year, each starting with a {TRIAL}, or Lifetime at {P_LIFETIME} once. Prices in USD; the App Store shows your local currency at checkout."

  - q: "Does it support multiple apps?"
    a: "Yes. AppMeta Pulse shows every app in your App Store Connect account, and you choose which ones it tracks. The Apps tab compares them side by side, and each app has its own chart, top territories, and reviews. If you work with more than one App Store Connect account, add each one and switch between them."

  - q: "Does AppMeta Pulse send notifications when a sale comes in?"
    a: "No. AppMeta Pulse sends no notifications. To see sales without opening the app, add a widget: the Home Screen and Lock Screen widgets refresh about once an hour during the day and after each sync."

  - q: "Does AppMeta Pulse work on iPad or Mac?"
    a: "No. AppMeta Pulse runs on iPhone only and needs iOS 17 or later. With iCloud Sync on, a second iPhone signed in to the same Apple Account can show your numbers without the API key stored on it."

  - q: "Which languages is AppMeta Pulse available in?"
    a: "English plus 17 languages: German, French (France and Canada), Spanish (Spain and Mexico), Italian, Dutch, Swedish, Portuguese (Brazil and Portugal), Russian, Ukrainian, Turkish, Japanese, Korean, and Chinese (Simplified and Traditional). The widgets and Siri phrases are translated too. Reply drafts from Apple Intelligence are in English."

  - q: "Who is AppMeta Pulse for?"
    a: "Indie developers and small studios who sell apps or subscriptions on the App Store and want their numbers, their history, and their reviews on the iPhone. It needs an App Store Connect API key with the Admin role. It pays off most when you sell several apps and want them on one screen."

  - q: "Does AppMeta Pulse collect any data?"
    a: "No. AppMeta Pulse has no server of its own, no analytics or crash-reporting SDKs, and no advertising identifier. App Store Connect requests go from your iPhone to Apple, app icons come from Apple's lookup service, and exchange rates come from the European Central Bank. Reply drafts, sentiment, and translation run on the device. With iCloud Sync on, your data is also stored in your own private iCloud database, which we can't access."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/appmeta-pulse/support/"

release:
  first_release: "2026-02-17"
  last_updated: "2026-10-13"

ratings:
  value: "4.0"
  count: 4
  last_synced: "2026-08-17"
show_body: true
about_heading: "Why AppMeta Pulse exists."

# Studio identity: Organization-mode founder block (no personal name).
founder:
  overline: "Who built this"
  heading: "An independent Apple studio that sells its own apps and built the dashboard it wanted to use."
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple studio · Finland"
  photo: "/assets/icons/lagerland-mark.png"
  bio: "We sell {APP_COUNT} apps through App Store Connect. Checking how they were doing meant a browser and a login, and App Store Connect only keeps about a year of daily sales, so last year's numbers kept slipping away. We wanted the figures on the phone, the history kept, the API key left on the device, and no server of ours in between. AppMeta Pulse is that app."
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails are answered personally, usually within a day."
  signals:
    - "Lagerland Apps sells {APP_COUNT} apps through App Store Connect and built AppMeta Pulse for its own portfolio"
    - "The app carries no ads, tracking, or third-party analytics"
    - "The API key stays in the iPhone's Keychain and requests go over HTTPS straight to Apple"
    - "Paid for by the apps' own sales, with no ads and no investors"
  external_link:
    href: "/alternatives/"
    label: "See how AppMeta Pulse compares to AppStats, App Sales, and Appfigures"

related_apps:
  - appmeta
  - mockly
last_updated: 2026-10-29
---

App Store Connect keeps about a year of daily sales. After that the days fall off, and with them any honest answer to "am I doing better than this time last year?" AppMeta Pulse fetches your sales and subscription reports through Apple's API and keeps every day on your iPhone until you delete it. It also keeps an original copy of each report Apple sends. Once a full year is stored, Trends puts this year next to last year, and the 12 widgets show how the current week or month is pacing.

Reviews live in the same place. Every app's reviews come in one list with unanswered low-star ones at the top. You can translate a review written in another language on the device, answer it, or select up to 25 and answer them in one go. On iOS 26 with Apple Intelligence, the reply composer writes two English drafts on the device for you to edit before you send.

AppMeta Pulse can't change your prices, builds, or metadata. It writes two things to App Store Connect: the review replies you send, and the analytics report requests Apple needs before it prepares impressions data. The .p8 key stays in this iPhone's Keychain and never syncs. There is no AppMeta Pulse server, so your numbers travel between your iPhone and Apple, and with iCloud Sync on, to your own private iCloud.

The figures use Apple's own words: <em>proceeds</em> (after Apple's 15% Small Business or 30% standard commission and tax), <em>sales</em> (gross before commission), and <em>units</em>, which count first-time downloads, not updates or re-downloads. They come from Apple's daily sales reports, so they are next-day numbers and can differ from the final amounts in your monthly <a href="https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports/" rel="noopener">financial reports</a>. Converted amounts use the European Central Bank's monthly average rates and are estimates, not Apple's payout figures.
