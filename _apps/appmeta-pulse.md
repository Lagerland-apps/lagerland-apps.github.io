---
layout: app
slug: appmeta-pulse
name: "AppMeta Pulse"
tagline: "The monitoring-first App Store Connect dashboard for indie iOS developers."
quick_answer: "AppMeta Pulse is a monitoring-first App Store Connect dashboard for iPhone. Indie iOS developers use it to check proceeds or sales, MRR, active subscriptions, trial conversions, and downloads across their whole app portfolio in seconds, and to reply to App Store reviews, without opening a browser. It has no controls for builds, pricing, or metadata. It has 12 Home Screen and Lock Screen widgets and runs on Apple's official App Store Connect API with an Admin key you create. The App Store also offers it on Apple silicon Macs and Apple Vision Pro, where it runs as the iPhone app. The download is free and opens a demo on sample data; your own numbers cost {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} lifetime, with a 7-day free trial. It has no ads, tracking, or analytics SDKs."
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
# $0.99/month, $1.99/year, $2.99 lifetime. The free download only opens a demo
# on sample data; your own numbers need a subscription or Lifetime.
plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. The lifetime tier is a one-time purchase: it does not auto-renew, and no card is kept on file beyond Apple's own. You generate the App Store Connect API key (.p8) yourself in App Store Connect → Users and Access → Integrations with the Admin role, and it is stored on-device in Keychain. The methodology page lists the endpoints it calls."

plans:
  - name: "Free download"
    price: "$0"
    summary: "Try the whole app on sample data in demo mode. Your own numbers need a subscription, which starts with a 7-day free trial, or Lifetime."
    features:
      - "Demo mode with sample apps and numbers, for up to three days"
      - "Connect your own App Store Connect API key (Admin role) once you subscribe; it stays in this iPhone's Keychain"
      - "iPhone app; the App Store also offers it on Apple silicon Macs and Apple Vision Pro"
      - "No analytics SDKs and no tracking, as the App Store privacy label shows"
  - name: "Pro"
    price: "{P_MONTHLY} / mo · {P_YEARLY} / yr"
    kind: monthly
    summary: "Your own numbers, monthly or yearly. 7-day free trial; cancel anytime."
    features:
      - "Proceeds or sales, units, and new subscriptions across your portfolio"
      - "MRR, active subscriptions, trials, trial-to-paid conversion, churn, and cancellations"
      - "Per-app breakdowns and period-over-period trends"
      - "Top territories per app from Sales and Trends data"
      - "12 Home Screen and Lock Screen widgets, and replies to App Store reviews"
      - "Yearly is about {SAVE_YEARLY}% cheaper than monthly billing ({P_YEARLY} vs {P_MONTHLY_ANNUAL}/yr)"
  - name: "Lifetime"
    price: "{P_LIFETIME} one-time"
    kind: lifetime
    summary: "Pay once, use forever."
    highlight_label: "Best long-term value"
    features:
      - "Everything in Pro, unlocked permanently"
      - "Costs about a year and a half of the yearly plan"
      - "{P_LIFETIME}, against AppStats' $49.99 lifetime"
      - "Future Pro features included at no extra cost"
      - "No subscription or auto-renew, and access does not expire"

icon: "/assets/icons/appmeta-pulse.png"
og_image: "/assets/og/appmeta-pulse.png"

seo:
  title: "AppMeta Pulse: App Store Connect Dashboard for iPhone"
  description: "Monitoring-first App Store Connect dashboard for indie iOS devs: proceeds, MRR and subscriptions in seconds on iPhone. From {P_MONTHLY}/mo, no tracking."
  keywords:
    - App Store Connect iPhone app
    - App Store Connect dashboard iPhone
    - app store revenue tracker iPhone
    - read-only App Store Connect
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
    - app store financial reports iPhone
    - portfolio revenue dashboard
    - indie developer revenue iPhone
    - app store connect API client
    - app store subscription dashboard
    - app store mrr tracker

hero:
  pre_headline: "For indie iOS developers shipping multiple apps."
  headline: "A fast, calm App Store Connect dashboard."
  secondary: "It collects no data at all, as its App Store privacy label declares. It costs a third of AppStats' monthly price, or {P_LIFETIME} for lifetime access."
  subheadline: "Check proceeds, MRR, active subscriptions, trial conversions, and downloads across your whole portfolio in seconds on your iPhone. It runs on Apple's official App Store Connect API, needs no browser, and has no build, pricing, or metadata controls to press by accident."
  cta_label: "Download Free"
  alt: "AppMeta Pulse App Store Connect dashboard on iPhone, showing seven days of proceeds, units, new subscriptions, and monthly subscription revenue across a multi-app portfolio"

who_for:
  - "You're an indie iOS developer or small studio shipping multiple apps and want daily revenue at a glance"
  - "You're tired of logging into App Store Connect in a browser just to check yesterday's proceeds"
  - "You want a dashboard with no pricing, build, or metadata controls, so you cannot accidentally change pricing, submit a build, or break metadata"
  - "You want MRR, subscription health, trial conversions, and downloads on one screen"
  - "You don't want your App Store Connect data passing through third-party analytics SDKs or ad networks"

who_not_for:
  - "You only ship one app and the App Store Connect web UI is already enough"
  - "You want an iPad layout; AppMeta Pulse is an iPhone app"
  - "You need to edit metadata, submit versions for review, or change pricing. Our sister app AppMeta does that"
  - "Your team already uses a shared enterprise analytics stack like RevenueCat, Sensor Tower, or Data.ai for paid plan reasons"

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
  - title: "Numbers on launch"
    description: "Your proceeds, subscriptions, and downloads for the latest reported day are on screen the moment the app opens. You skip loading App Store Connect in a browser, the nested reports, and the \"Sales and Trends\" spinner."
  - title: "Monitoring by design"
    description: "AppMeta Pulse has no code for changing pricing, submitting builds, editing metadata, or altering settings in your App Store Connect account. The only things it writes are the review replies you choose to send and the analytics report requests Apple needs to prepare impressions data."
  - title: "Apple's own terms"
    description: "Proceeds (after Apple's 15 to 30% cut and any tax), sales, units, active subscriptions, trial conversions, and cancellations, labelled with the same words App Store Connect uses."
  - title: "No data collection"
    description: "The app sends us no analytics, advertising tracking, usage data, or diagnostics, as declared on the App Store privacy label. Credentials live in the system Keychain, and queries go straight to Apple."

features:
  - title: "Revenue at a glance"
    description: "The latest day's proceeds (or sales, if you prefer), units, and new subscriptions appear as soon as you open the app. Per-app breakdowns show which apps are pulling their weight and which need attention. Every amount is converted into the display currency you choose, using the European Central Bank's monthly rates."
  - title: "Subscription health"
    description: "Monthly recurring revenue, active subscriptions, free trials in progress, trial-to-paid conversion rate, churn, and recent cancellations, without drilling through App Store Connect's nested Subscriptions reports."
  - title: "Trend comparison"
    description: "Compare the last 7, 30, or 90 days, the year to date, or a custom range with the period before or the same days last year. A revenue dip shows up early, and so does growth that ASC's default views keep behind tabs."
  - title: "Every app in the portfolio"
    description: "Whether you ship five apps or fifteen, you see how each one contributes to total proceeds, downloads, and subscription metrics, app by app across your whole App Store Connect catalogue."
  - title: "Sales & Trends + Subscription reports, on iPhone"
    description: "Apple splits these metrics between the \"Sales and Trends\" and \"Subscriptions\" sections of App Store Connect. Pulse puts them on one screen and refreshes on demand."
  - title: "Made for a quick look"
    description: "Laid out for a 10-second look over morning coffee, or an end-of-week trend review while you wait at the airport, with no browser to open."

screenshots:
  - src: "/assets/screenshots/appmeta-pulse/1.png"
    alt: "AppMeta Pulse dashboard on iPhone showing proceeds and subscription status"
  - src: "/assets/screenshots/appmeta-pulse/2.png"
    alt: "AppMeta Pulse 30-day trends widget for the Home Screen and Lock Screen"
  - src: "/assets/screenshots/appmeta-pulse/3.png"
    alt: "AppMeta Pulse drafting a reply to a 1-star App Store review on device"
  - src: "/assets/screenshots/appmeta-pulse/4.png"
    alt: "AppMeta Pulse apps list with proceeds and a 7-day trend for each app"
  - src: "/assets/screenshots/appmeta-pulse/5.png"
    alt: "AppMeta Pulse analytics comparing this year with last year"
  - src: "/assets/screenshots/appmeta-pulse/6.png"
    alt: "AppMeta Pulse subscription metrics: MRR, trials and churn"
  - src: "/assets/screenshots/appmeta-pulse/7.png"
    alt: "AppMeta Pulse app analytics showing impressions, page views and downloads"
  - src: "/assets/screenshots/appmeta-pulse/8.png"
    alt: "AppMeta Pulse feature summary for indie developers: iCloud sync, multiple teams, goals and shortcuts"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no third-party analytics or SDKs"
    - "Reads via Apple's official App Store Connect API; the only writes are review replies you send and analytics report requests"
    - "App Store Connect API key (.p8) and key ID stored in the system Keychain"
    - "Queries go to Apple's servers directly; no data is routed through Lagerland servers"
    - "No data, diagnostics, or usage telemetry collected"
    - "With iCloud Sync on, your data is also kept in your own private iCloud database, which we can't access; the .p8 key never syncs"

faq:
  - q: "What is AppMeta Pulse?"
    a: "AppMeta Pulse is a fast, monitoring-first App Store Connect dashboard for iPhone; the App Store also offers it on Apple silicon Macs and Apple Vision Pro, where it runs as the iPhone app. It shows proceeds or sales, MRR, active subscriptions, trial conversions, and downloads for every app in your App Store Connect account, and lets you reply to customer reviews without opening a browser. It has no controls for builds, pricing, or metadata."

  - q: "How is AppMeta Pulse different from AppStats, App Sales, or Appfigures?"
    a: "All four target indie iOS developers checking App Store Connect on iPhone, with different trade-offs. <a href=\"/alternatives/appstats/\">AppStats</a> has an iPad version, a free tier for one app, and alerts, but costs ~3× the monthly price and its privacy label declares usage data and diagnostics. <a href=\"/alternatives/app-sales-store-reports/\">App Sales - Store Reports</a> has an iPad version and a higher App Store rating (★ 4.9 / 41), but its App Store privacy label declares that it tracks purchases, identifiers, and usage data for third-party advertising. <a href=\"/alternatives/appfigures/\">Appfigures</a> is a web/enterprise dashboard with deep cross-store reporting at $9.99+/month. AppMeta Pulse is the cheapest and the only one whose privacy label declares <em>zero</em> data collection. Pick AppMeta Pulse for price and zero tracking; pick one of the others if you need a feature only it has."

  - q: "How is AppMeta Pulse different from the official App Store Connect app?"
    a: "Apple's <a href=\"https://apps.apple.com/us/app/app-store-connect/id1234793120\" rel=\"noopener\">App Store Connect app</a> is a full management tool: it can submit builds, reply to reviews, manage TestFlight, and change metadata. AppMeta Pulse is a focused dashboard for quick monitoring. Apart from the analytics report requests Apple needs, the only thing it sends to App Store Connect is a review reply you write. It launches faster, reads more simply, and can't push a build by accident while you're at the coffee shop."

  - q: "What's the difference between sales and proceeds in App Store Connect?"
    a: "<em>Sales</em> is the gross amount customers paid before Apple's commission. <em>Proceeds</em> is what Apple owes you after its 15% (Small Business Program) or 30% (standard) cut and any VAT or sales tax it collects. The payment that reaches your bank can still differ from your proceeds, because of currency conversion, withholding tax, and bank fees. AppMeta Pulse displays proceeds by default, since that is the Sales and Trends figure closest to what you get paid, and lets you switch to gross sales in Settings → Display when you want to compare against Sales and Trends in the App Store Connect web UI. See Apple's reference on <a href=\"https://developer.apple.com/help/app-store-connect/view-sales-and-trends/view-units-proceeds-sales-and-pre-orders/\" rel=\"noopener\">units, proceeds, and sales</a> for the official definitions."

  - q: "Does AppMeta Pulse use the App Store Connect API or the web dashboard?"
    a: "The official <a href=\"https://developer.apple.com/documentation/appstoreconnectapi\" rel=\"noopener\">App Store Connect API</a>. You generate an API key with the Admin role in App Store Connect → Users and Access → Integrations, download the .p8 private key, and import the key file + Key ID + Issuer ID into AppMeta Pulse, along with your Vendor Number for the sales reports. The key material is stored in your system Keychain. AppMeta Pulse never scrapes the web dashboard. See <a href=\"/apps/appmeta-pulse/api-access/\">the API access methodology page</a> for the exact endpoints called, the role you need on the key, and the JWT lifecycle."

  - q: "What permissions does AppMeta Pulse request on my App Store Connect account?"
    a: "AppMeta Pulse asks for an API key with the Admin role. Admin is the role that covers sales reports, App Analytics, and review replies together; App Manager and Developer keys can't read sales reports, and Apple answers them with a 403 error. It uses the key to read your sales and subscription reports, your app catalog, App Store analytics, and customer reviews. The only things it writes are the review replies you choose to send and the analytics report requests Apple needs to prepare impressions data; it has no pricing, build, or metadata endpoints. You can revoke the key in App Store Connect at any time without uninstalling the app. <a href=\"/apps/appmeta-pulse/api-access/\">Full role-to-endpoint mapping is documented on the methodology page.</a>"

  - q: "How fresh is the data? Is it real-time?"
    a: "It is as fresh as Apple makes available. Apple publishes each day's Sales and Trends report the following day, generally by 8 a.m. Pacific Time, and the daily subscription reports follow the same schedule; App Store analytics such as impressions arrive a day or two later. AppMeta Pulse checks in the background about hourly until the new day lands (iOS decides the exact timing), and again when you open the app or pull to refresh; it cannot make Apple's data faster than Apple does. If a number looks stuck, it is almost always Apple's reporting cadence, not the app."

  - q: "Can I see revenue by country?"
    a: "Yes. Sales and Trends reports include country/territory breakdowns, and AppMeta Pulse lists each app's top five territories in its detail view and the top eight for the selected period in Trends. It doesn't read Apple's <a href=\"https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports/\" rel=\"noopener\">monthly financial reports</a>, so reconcile payments against those in App Store Connect."

  - q: "Is AppMeta Pulse safe for my credentials?"
    a: "Yes. The App Store Connect API key (.p8 file and key ID) are stored in the system Keychain, the same secure storage macOS and iOS use for passwords and Wi-Fi credentials. Queries go directly to Apple's API servers over HTTPS; nothing is routed through Lagerland Apps servers. You can revoke the key in App Store Connect at any time."

  - q: "Can I accidentally change app settings?"
    a: "No. There are no \"submit build,\" \"edit metadata,\" or \"change pricing\" buttons anywhere in the app, and it has no code for those App Store Connect endpoints, so pushing the wrong build or hiking the wrong price is impossible inside AppMeta Pulse. The one thing you can change is a review reply: you write it, tap send, and can edit or delete it later."

  - q: "Is AppMeta Pulse free?"
    a: "Free to download, and the free download opens a demo on sample data. To see your own numbers you need a subscription or the lifetime unlock: {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once, and the subscription starts with a 7-day free trial. The {P_LIFETIME} lifetime tier compares with AppStats' $49.99 lifetime."

  - q: "Does it support multiple apps?"
    a: "Yes. AppMeta Pulse shows performance metrics across every app in your App Store Connect account. Per-app breakdowns let you see how each app contributes to total proceeds, downloads, and subscription health, which the official App Store Connect web UI handles poorly on a phone. If you work with more than one App Store Connect team, you can add each account and switch between them."

  - q: "Who is AppMeta Pulse for?"
    a: "Indie iOS developers, founders, and small studio teams who check App Store metrics regularly and want a quicker way to monitor their business than the App Store Connect web interface or app. It helps most for publishers with several apps who want the whole portfolio on one screen."

  - q: "Does AppMeta Pulse collect any data?"
    a: "No. AppMeta Pulse has no analytics, third-party SDKs, or advertising trackers, and collects no usage data, diagnostics, or telemetry. Its App Store privacy label declares zero data collection, which you can check on the listing. With iCloud Sync on, your data is also kept in your own private iCloud database, which we can't access. App Store Connect requests go directly from your device to Apple, and exchange rates come from the European Central Bank's public API."

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
  heading: "An independent Apple studio that ships its own apps and built the dashboard it wanted to use."
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple studio · Finland"
  photo: "/assets/icons/lagerland-mark.png"
  bio: "Checking App Store revenue on a phone has been awkward for a decade. Apple's official App Store Connect app focuses on management (submitting builds, replying to reviews, editing metadata), not on the 10-second \"how did yesterday do?\" check that indie publishers make every day. Web-based dashboards cost $9.99+/month and route your data through third-party analytics. Other iPhone trackers charge more and collect usage data for advertising. We ship {APP_COUNT} apps through App Store Connect and wanted a private dashboard without ad SDKs or middleman servers, and with a privacy label that holds no surprises, so we built AppMeta Pulse."
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails are answered personally, usually within a day."
  signals:
    - "Lagerland Apps publishes {APP_COUNT} apps through App Store Connect, and AppMeta Pulse is the dashboard we use every day on our own portfolio"
    - "No third-party SDKs or advertising trackers, and no collected data, as declared on the App Store privacy label"
    - "The App Store Connect API key stays in the system Keychain and requests go over HTTPS straight to Apple, so your data never touches Lagerland servers"
    - "Paid for by the apps' own sales, with no ads and no investors"
  external_link:
    href: "/alternatives/"
    label: "See how AppMeta Pulse compares to AppStats, App Sales, and Appfigures"

related_apps:
  - appmeta
  - mockly
last_updated: 2026-10-26
---

Apple's own App Store Connect app is for <em>managing</em> a developer business: submitting builds, replying to reviews, editing metadata, and running TestFlight. It does that job well. It is slow for the question most indie publishers ask ten times a day, <em>how is yesterday looking?</em> On a phone, the official app puts three taps and a loading spinner between you and a number you wanted in two seconds.

AppMeta Pulse covers the other half: a monitoring-first dashboard for that daily check. It opens on the latest day's proceeds, MRR, active subscriptions, trial conversions, and downloads across every app you ship. You can drill into one app when something looks off or compare this week with last week, then close it and get back to work.

These limits are in the code. AppMeta Pulse has no code for submitting builds, changing pricing, or editing metadata. The only things it writes to App Store Connect are the review replies you choose to send and the analytics report requests Apple needs to prepare impressions data. The .p8 private key and key ID live in your system Keychain and never sync, even with iCloud Sync on. Queries hit Apple's API servers directly over HTTPS; nothing is routed through Lagerland Apps servers, and the App Store privacy label, which you can check on the listing, declares zero data collection.

The dashboard uses Apple's own vocabulary: <em>proceeds</em> (after Apple's 15% Small Business or 30% standard cut and country VAT), <em>sales</em> (gross before commission), <em>units</em>, <em>active subscriptions</em>, <em>trial conversions</em>, <em>cancellations</em>. You don't have to translate a third-party dashboard's relabelled numbers back into Apple's terms. The figures come from Sales and Trends, so they are next-day numbers and can differ from the final amounts in your monthly <a href="https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports/" rel="noopener">financial reports</a>.
