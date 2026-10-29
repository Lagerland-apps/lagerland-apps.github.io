---
layout: app
slug: observa
name: "Observa"
tagline: "Readiness, sleep, and HRV from Apple Health, explained."
quick_answer: "Observa is an iPhone, iPad, and Apple Watch app that turns your Apple Health data into a daily Readiness score, a Sleep Score, and a stress read, each measured against your own baseline and explained in plain language. Ask \"Should I train today?\" and it answers Push, Maintain, Recover, or Rest, with the reason. There is no account and no ads, and your health data stays on your device. The daily scores are free, every Pro feature is unlocked for your first 7 days without signup, and Pro costs {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once."
category: health
status: live
jump_nav: true

app_store_url: "https://apps.apple.com/app/id6757438990"

price:
  model: freemium
price_tier: "Pro"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew. Every paid plan supports Family Sharing, and Pro works on iPhone, iPad, and Apple Watch."

release_notes:
  - date: "2026-10-16"
    note: "Apple Watch workout screens now in your language, plus fixes for the training call, sleep consistency across time zones, and symptom saving."
  - date: "2026-10-03"
    note: "Full-page widgets on iOS 27 (Today, Folio, Last 14 days, and Trend), and \"Why this score?\" opens straight from the Today widget."
  - date: "2026-09-11"
    note: "Apple Watch app with complications, a Workout Live Activity, \"Should I train today?\" in Siri, and \"Why this score?\" explainers."
  - date: "2026-08-12"
    note: "Configurable widgets (Focus, Trend, Stack, Grid, Breakdown, and Insight), water imported from Apple Health, and sleep debt measured against your own goal."
  - date: "2026-07-10"
    note: "Pro: Functional Age, an estimate of how your fitness compares with people of your age."

plans:
  - name: "Free"
    price: "$0"
    summary: "Your daily scores, the reasons behind them, and a training call every morning. Free for good, with no account."
    features:
      - "Readiness, Sleep Score, Stress, and Today's Plan"
      - "\"Why this score?\" and \"Should I train today?\""
      - "A daily coaching note and a morning check-in"
      - "7-day trends"
      - "Siri and Shortcuts, plus Readiness, check-in, water, and workouts on Apple Watch"
      - "Every Pro feature for your first 7 days, with no signup or card"
  - name: "Pro · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Full Pro, billed monthly. Starts with a {TRIAL}. Cancel anytime."
    features:
      - "Trends over 30, 90, and 365 days"
      - "The full analysis screen behind every metric"
      - "Functional Age, Advanced HRV, ECG history, and heart-rate recovery"
      - "Training Status, Load Trends, Personal Records, and Workout Replay"
      - "Your data in Home Screen and Lock Screen widgets"
      - "All 14 themes, and workout reports as PDF without a watermark"
      - "Cancel anytime"
  - name: "Pro · Annual"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "Same Pro features, billed once a year. Starts with a {TRIAL}. ~{SAVE_YEARLY}% cheaper than paying monthly."
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
      - "Family Sharing included"

icon: "/assets/icons/observa.png"
og_image: "/assets/og/observa.png"

seo:
  title: "Apple Health Insights for Readiness, Sleep & HRV: Observa"
  description: "A daily Readiness score from your Apple Health sleep, HRV, and heart data, with every score explained and all analysis on your device. Free, with Pro."
  keywords:
    - Apple Health insights app
    - readiness score app
    - should I train today app
    - HRV app Apple Watch
    - SDNN HRV tracker iPhone
    - sleep score app iPhone
    - sleep debt tracker
    - recovery app Apple Watch
    - private health app
    - functional age app
    - Apple Watch readiness complication
    - AutoSleep alternative
    - Athlytic alternative
    - Bevel alternative

hero:
  pre_headline: "Apple Health insights for readiness, sleep, and HRV"
  headline: "Know whether to train today, and why."
  secondary: "A daily Readiness score from your sleep, HRV, resting heart rate, and training load, with a plain-language reason behind every number."
  subheadline: "Observa reads what your iPhone and Apple Watch already save to Apple Health and measures each night and morning against your own baseline, not a generic target. There is no account to create, and your health data stays on your device."
  cta_label: "Download Free"
  alt: "Observa on iPhone explaining today's Readiness, sleep, and HRV from Apple Health"

who_for:
  - "Your Apple Watch saves sleep, HRV, and heart data to Apple Health, and you want to know what the numbers mean"
  - "You train and want a straight answer each morning: push, maintain, recover, or rest"
  - "You track your sleep and want sleep debt measured against your own goal, not a fixed 8 hours"
  - "You'd rather glance at your watch, a widget, or ask Siri than dig through dashboards"
  - "You want health insights without an account, ads, or a cloud upload"

who_not_for:
  - "You want a diagnosis or a medical device (Observa shows what Apple Health recorded and does not detect conditions)"
  - "You don't use Apple Health, since every score is built from the data in it"
  - "You want calorie goals or diet logging (nutrition in Observa is context only)"
  - "You need a Mac or Android app, sync across devices, or a full data export"

alternatives_to:
  - "Bevel"
  - "Gentler Streak"
  - "AutoSleep"
  - "Athlytic"
  - "Whoop"
  - "Oura"
  - "HRV4Training"
  - "Welltory"
  - "Apple Health (for interpretation)"

value_points:
  - title: "Private by construction"
    description: "Observa has no account and no ads, and it carries no analytics SDKs. The app makes no network calls of its own, so your health data is processed and stored on your device. Only purchases and the links you open use the internet."
  - title: "Measured against you"
    description: "Readiness, Sleep, and Stress compare you with your own typical range and show how confident each read is. For roughly the first week, Readiness says \"Building your baseline\" while Observa learns your normal."
  - title: "Every score explained"
    description: "Tap \"Why this score?\" to see which signals sit in your usual range and which moved the score most. It covers Readiness, Sleep, and Stress, on iPhone and on Apple Watch."
  - title: "Answers wherever you look"
    description: "Ask Siri \"Should I train today?\", check a widget on your Home Screen or Lock Screen, or raise your wrist to a complication. The answer comes with its reason."

how_it_works:
  intro: "From Apple Health to a straight answer each morning, in six steps."
  steps:
    - title: "Allow Apple Health access"
      detail: "Observa asks for the core categories up front, such as sleep, heart rate, HRV, and workouts. Optional ones, like ECG, cycle, or body measurements, stay off until you turn them on in Privacy & Permissions."
    - title: "Observa learns your baseline"
      detail: "Scores compare you with your own typical range. Readiness shows \"Building your baseline\" for about the first 7 nights and labels its confidence as your data builds up."
    - title: "Read your morning scores"
      detail: "Readiness runs from 0 to 100 and weighs sleep at 35%, HRV at 25%, resting heart rate at 25%, and training load at 15%. The Sleep Score and Stress sit alongside it, and \"Why this score?\" shows what moved each one."
    - title: "Decide what to do today"
      detail: "\"Should I train today?\" returns Push, Maintain, Recover, or Rest from your readiness and training load, with the reason. Today's Plan suggests a recovery focus and an intensity."
    - title: "See what tends to matter for you"
      detail: "Patterns ranks the habits that tend to line up with your recovery, sleep, and HRV over 14, 28, or 90 days. Each card shows its confidence and why you're seeing it. Patterns are associations, not causes."
    - title: "Everything stays on the device"
      detail: "The analysis runs on your iPhone, iPad, or Apple Watch. There is no account and no iCloud sync, and the app makes no network calls of its own."

example_insights:
  intro: "The kinds of cards Observa shows. The wording below is illustrative; yours is built from your own Apple Health data."
  cards:
    - headline: "Should I train today? Maintain."
      body: "Readiness is Moderate. Sleep and resting heart rate are in your usual range, and HRV is below it, so keep today's session steady."
      tag: "Recovery · Training call"
    - headline: "Why this score?"
      body: "HRV moved your Readiness most today. Sleep, resting heart rate, and training load are all within your usual range."
      tag: "Recovery · Explainer"
    - headline: "Sleep debt: slight."
      body: "You slept less than your own sleep goal over recent nights. Observa measures debt against the goal you set."
      tag: "Sleep · Debt"
    - headline: "Stress: moderate."
      body: "The drivers are named: resting heart rate above your usual range and a short night. A 7-day micro-trend shows which way it's heading."
      tag: "Stress · Drivers"
    - headline: "Later workouts tend to line up with lower HRV."
      body: "A ranked pattern with its confidence label. Tap \"Why am I seeing this?\" for the details, then mark it Feels accurate or Doesn't apply."
      tag: "HRV · Pattern"
    - headline: "Your chronotype: Intermediate."
      body: "Classified from your last 14 nights. Pro adds recommendations and a circadian timeline."
      tag: "Sleep · Chronotype"

features:
  - title: "Readiness and the training call"
    description: "A 0 to 100 Readiness score each morning from sleep, HRV, resting heart rate, and training load, banded Ready, Moderate, or Low. \"Should I train today?\" turns it into Push, Maintain, Recover, or Rest, with the reason, in the app, through Siri, in a widget, or on your wrist."
  - title: "Sleep Score, stages, and sleep debt"
    description: "A daily Sleep Score from duration, efficiency, consistency, and overnight recovery signals. See your Deep, REM, Core, and Awake time, how your heart behaved overnight, and four Sleep Quality factors. Sleep debt is tracked against your own sleep goal, and a bedtime reminder helps keep the routine."
  - title: "Stress and Today's Plan"
    description: "A Low, Moderate, or High stress state with its drivers named, such as low HRV, elevated resting heart rate, or short sleep. Today's Plan turns your recovery into a focus and a suggested intensity."
  - title: "Patterns"
    description: "Find out which habits tend to line up with better recovery, sleep, and HRV. Up to four ranked cards over 14, 28, or 90 days, each with a confidence label and a \"Why am I seeing this?\" note. Patterns are associations, not causes, and the wording says so."
  - title: "Heart, HRV, and Functional Age"
    description: "Resting heart rate and HRV (SDNN, as Apple Health records it) against your baseline, plus cardio fitness from your VO₂ max. Pro adds Functional Age, a norm-based estimate of how your fitness compares with people of your age, and your ECG recordings and history from Apple Health. Both are informational, not clinical."
  - title: "Workouts and training load"
    description: "Training load compares your last 7 days with your last 28, and every workout gets an Effort Score from 0 to 100. Pro adds Training Status, Load Trends, Monotony & Strain, Personal Records, and Workout Replay with route, heart rate, and zones."
  - title: "Apple Watch app and complications"
    description: "Readiness, the training call, and \"Why this score?\" on your wrist, plus a morning check-in, water logging, and workout recording with live heart rate. The Watch app runs on its own on watchOS 10 or later, and its complications sit on your watch face."
  - title: "Widgets, Siri, and Live Activities"
    description: "Configure Home Screen and Lock Screen widgets with the metrics you choose; on iOS 27 there are full-page widgets too. Ask Siri for your Readiness or Sleep Score, or log water and your check-in by voice. Water and workouts also run as Live Activities."

screenshots:
  - src: "/assets/screenshots/observa/1.webp"
    alt: "Observa trends screen with sleep and stress trends, under the line: you have not been sleeping like you used to"
  - src: "/assets/screenshots/observa/2.webp"
    alt: "Observa chronotype analysis showing a morning lark profile"
  - src: "/assets/screenshots/observa/3.webp"
    alt: "Observa Home Screen widgets showing sleep, recovery, and steps"
  - src: "/assets/screenshots/observa/4.webp"
    alt: "Observa full-page widget with readiness and sleep for the whole morning"
  - src: "/assets/screenshots/observa/5.webp"
    alt: "Observa ECG recording from Apple Health next to HRV values"
  - src: "/assets/screenshots/observa/6.webp"
    alt: "Observa Readiness score with a seven-day comparison"
  - src: "/assets/screenshots/observa/7.webp"
    alt: "Observa respiratory trends chart"
  - src: "/assets/screenshots/observa/8.webp"
    alt: "Observa patterns screen with a calendar heatmap and goal progress"
  - src: "/assets/screenshots/observa/9.webp"
    alt: "Observa patterns screen with day-of-week averages"
  - src: "/assets/screenshots/observa/10.webp"
    alt: "Observa closing card: some apps you check, this one knows you"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  app_privacy_label: "Check the privacy details on Observa's App Store page before you download."
  notes:
    - "No account, no ads, and no tracking"
    - "Your health data is processed and stored on your device and never uploaded"
    - "No analytics or third-party SDKs, and no network calls of its own; only purchases and links you open go online"
    - "No iCloud sync. Delete All Data clears Observa's own data and leaves Apple Health untouched"
    - "Observa writes to Apple Health only when you log water or record a workout on Apple Watch"

founder:
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  overline: "Who built this"
  heading: "Made by a one-person studio"
  story: "Observa comes from Lagerland Apps, an independent studio in Finland. Apple Health collects a great deal about your sleep and your heart and says very little about what it means for today. Observa answers that question on the device itself, so nobody at Lagerland Apps ever sees your data."
  signals:
    - "Independent Apple developer, building privacy-first apps from Finland since 2025"
    - "Observa needs no account and carries no analytics SDKs; the analysis runs on your device"
    - "A one-person studio, paid for by people who buy the software, without investors or a growth team"
    - "{APP_COUNT} live apps in the catalogue, none with ads or tracking, and none that requires an account"
  external_link:
    label: "More apps from Lagerland Apps"
    href: "/apps/"
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails go to one inbox and are answered personally, usually within a day."

faq:
  - q: "What is Observa?"
    a: "Observa is a health insights app for iPhone, iPad, and Apple Watch. It reads your Apple Health data and turns it into a daily Readiness score, a Sleep Score, and a stress read, each measured against your own baseline and explained in plain language. It also answers \"Should I train today?\" and shows which habits tend to line up with your recovery, sleep, and HRV. There is no account, and the analysis runs on your device."
  - q: "How is Observa different from other health apps?"
    a: "Your scores are compared with your own typical range, not a generic target, and each one shows how confident it is. Every score comes with \"Why this score?\", which names the signals that moved it. Observa is also private by construction. You never create an account, and the app makes no network calls of its own, so your health data stays on your device."
  - q: "How does the Readiness score work?"
    a: "Readiness is a 0 to 100 score built each day from sleep (35%), HRV (25%), resting heart rate (25%), and training load (15%). Breathing, blood oxygen, body, energy, and cycle data can adjust it when you have them. It is banded Ready, Moderate, or Low, and for about the first 7 nights it shows \"Building your baseline\" while Observa learns your normal. \"Why this score?\" shows which signals moved it most."
  - q: "Does Observa work with Apple Watch?"
    a: "Yes, in two ways. Observa reads what your Apple Watch saves to Apple Health, such as sleep stages, heart rate, HRV, resting heart rate, blood oxygen, and workouts. It also has its own Apple Watch app for watchOS 10 or later, with Readiness, the training call, \"Why this score?\", a morning check-in, water logging, and workout recording, plus complications for your watch face. The Watch app runs on its own."
  - q: "Do I need an Apple Watch?"
    a: "Observa reads Apple Health, whichever device or app saved the data there. An Apple Watch is recommended, because sleep stages, HRV, blood oxygen, ECG, and VO₂ max only appear when a device records them."
  - q: "How does Observa handle HRV and ECG data?"
    a: "Apple Health records heart rate variability as SDNN, and that is the HRV Observa shows: your daily value against your own baseline, with 7 days of trend free and 30, 90, or 365 days with Pro. HRV also feeds 25% of your Readiness score. With Pro, the ECG card shows your latest ECG recording with its waveform and the classification history from Apple Health. Observa displays what Apple Health recorded; it does not detect or diagnose any condition."
  - q: "Is Observa free?"
    a: "Yes. Readiness, the Sleep Score, Stress, Today's Plan, \"Why this score?\", the training call, the daily coaching note, 7-day trends, and Siri are free for good. Every Pro feature is unlocked for your first 7 days, with no signup or card. Pro adds 30, 90, and 365-day trends, the full analysis screens, Functional Age, Advanced HRV, ECG history, training analysis, widget data, and all 14 themes. It costs {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once, with Family Sharing on every paid plan. Separately from those first 7 days in the app, the monthly and yearly subscriptions each start with a {TRIAL} through the App Store. Prices are in USD; the App Store shows your local currency at checkout."
  - q: "Does Observa give medical advice?"
    a: "No. Observa is not a medical device. It shows patterns and scores from data you already collect, for your own understanding. It does not diagnose, treat, or detect any condition, and its ECG, rhythm, and blood oxygen views display what Apple Health recorded. If something looks off, talk to a clinician."
  - q: "Does Observa upload my health data?"
    a: "No. Your health data is processed and stored on your device. Observa works without an account or servers and carries no analytics or third-party SDKs. The app makes no network calls of its own; only purchases and the links you open use the internet. Your data is never shared with anyone, Lagerland Apps included."
  - q: "Do I need to log anything manually?"
    a: "No. Observa reads Apple Health automatically, so the scores fill in from data your iPhone and Apple Watch already save. Logging is optional: a three-question morning check-in, water in one tap or by voice, symptoms, and body measurements."
  - q: "How does Observa decide which patterns to show?"
    a: "Patterns looks at your data over 14, 28, or 90 days and compares habits with outcomes such as recovery, sleep, and HRV, including delayed effects. A pattern only appears when it passes a significance check, and Observa shows up to four, ranked. Each card carries a confidence label and a \"Why am I seeing this?\" note, and you can mark it Feels accurate or Doesn't apply. The wording says \"tends to align with\", because these are associations, not causes."
  - q: "How is Observa an alternative to AutoSleep, Athlytic, or Bevel?"
    a: "Observa suits you if you want a daily Readiness score and a training call with the reasons spelled out, measured against your own baseline, and you'd rather your health data never leave your device. It has no account and no ads, and it runs on iPhone, iPad, and Apple Watch. The comparison pages go app by app: <a href=\"/alternatives/autosleep/\">AutoSleep</a>, <a href=\"/alternatives/athlytic/\">Athlytic</a>, <a href=\"/alternatives/bevel/\">Bevel</a>, <a href=\"/alternatives/gentler-streak/\">Gentler Streak</a>, <a href=\"/alternatives/whoop/\">Whoop</a>, <a href=\"/alternatives/oura/\">Oura</a>, <a href=\"/alternatives/hrv4training/\">HRV4Training</a>, and <a href=\"/alternatives/welltory/\">Welltory</a>."
  - q: "Does Observa sync between devices or export my data?"
    a: "No. There is no account and no iCloud sync, so Observa's data lives on the device. The Apple Watch app keeps in step with your iPhone directly. The only export is a workout report: free users can share one a month as a PNG with a watermark, and Pro shares unlimited reports as PNG or PDF without one. A Pro purchase restores through Restore Purchases in Settings."
  - q: "What does Observa actually measure?"
    a: "Everything comes from Apple Health. Sleep: duration, efficiency, consistency, stages, overnight heart rate and its dip, and sleep debt against your goal. Recovery: Readiness, HRV (SDNN), resting heart rate, and stress. Heart: walking heart rate, VO₂ max, heart-rate zones and recovery, and ECG recordings. Activity and workouts: steps, active minutes, distance, flights, training load, and Effort Score. Breathing: respiratory rate and blood oxygen. Body and energy: weight, body fat, lean mass, and active and resting energy. Optional cycle context widens your baselines across the month. Each one is read against your own typical range."
  - q: "Which iPhone, iPad, and Apple Watch does Observa need?"
    a: "Observa needs iOS 17.6 or later on iPhone or iPad, and the Apple Watch app needs watchOS 10 or later. The full-page widgets need iOS 27. There is no Mac or Android version, and on iPhone the app runs in portrait."

related_journal:
  slug: what-14-days-of-apple-health-can-reveal
  anchor: "What 14 days of Apple Health data is enough to reveal, and what isn't"

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/observa/support/"

release:
  first_release: "2026-01-01"
  last_updated: "2026-07-11"

ratings:
  value: "4.1"
  count: 13
  last_synced: "2026-10-10"
last_updated: 2026-10-29
---
Observa is a health insights app for iPhone, iPad, and Apple Watch that turns Apple Health data into a daily read on how recovered you are. Each morning it gives you a Readiness score from sleep, HRV (SDNN), resting heart rate, and training load, a Sleep Score, and a stress state, all measured against your own baseline. "Why this score?" names the signals behind each number, and "Should I train today?" answers Push, Maintain, Recover, or Rest, in the app, through Siri, in a widget, or on your wrist. Patterns shows which habits tend to line up with your recovery, sleep, and HRV. The daily scores are free; Pro adds long-term trends, full analysis screens, Functional Age, ECG history, and training analysis. Observa has no account and no ads, carries no analytics SDKs, and keeps your health data on your device.
