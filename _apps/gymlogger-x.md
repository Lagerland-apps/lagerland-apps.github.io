---
layout: app
slug: gymlogger-x
name: "GymLogger X"
tagline: "Strength training. Logged fast."
quick_answer: "GymLogger X is a fast, minimalist strength training tracker for iPhone and Apple Watch — built as a private, no-subscription alternative to Strong, Hevy, and Fitbod. It logs every set from the wrist, generates periodized programs (PPL, Upper/Lower, Full Body) with automatic deloads, tracks RPE / 1RM / Wilks, and flags plateaus when an exercise stalls for nine or more weeks. Free at the core. $17.99/year or $44.99 lifetime. No ads, no tracking, no account."
category: fitness
platforms: ["iOS"]
status: live

app_store_url: "https://apps.apple.com/app/id6755734580"

price:
  model: freemium
  value: "Free — Pro from $17.99/yr or $44.99 lifetime"
schema_price: "0"
schema_high_price: "44.99"
schema_offer_count: "3"

icon: "/assets/icons/gymlogger-x.png"
og_image: "/assets/og/gymlogger-x.png"

seo:
  title: "GymLogger X — Strong & Hevy Alternative for Apple Watch"
  description: "A private, no-subscription alternative to Strong, Hevy & Fitbod. Real Apple Watch logging, smart programs, RPE & plateau detection. $44.99 lifetime. iOS only."
  keywords:
    - Strong app alternative
    - Hevy alternative
    - Fitbod alternative
    - Caliber alternative
    - workout tracker no subscription
    - Apple Watch strength training app
    - Apple Watch workout log no phone
    - private workout log iPhone
    - lifetime price workout tracker
    - strength training app no account
    - gym log app offline
    - PPL upper lower tracker
    - RPE RIR tracker iOS
    - 1RM calculator app
    - Wilks DOTS calculator
    - plateau detection workout app
    - progressive overload tracker
    - training program generator iPhone
    - powerlifting log app
    - hypertrophy program app

hero:
  headline: "Strength training log for iPhone & Apple Watch."
  secondary: "Train smarter. Lift stronger."
  subheadline: "Your training history shouldn't be a subscription. GymLogger X is a private workout tracker with first-class Apple Watch logging, smart periodized programs, RPE and 1RM tracking, and a $44.99 lifetime price. No ads, no account, no AI talking through your sets."
  cta_label: "Download Free"
  alt: "GymLogger X — strength workout being logged on iPhone with set, rep, and weight details"

# Founder block — Experience / Authority signal (rendered above features when present).
# Same schema as observa.md so the founder include can be reused across apps.
founder:
  overline: "Why I built this"
  heading: "From one lifter to another."
  name: "Antti Aittamaa"
  role: "Independent Apple developer, Lagerland Apps"
  location: "Finland"
  photo: "/assets/icons/lagerland-mark.png"
  bio: "I built GymLogger X because every workout app I tried either rented my training history through a subscription, leaked my data to ad networks, or treated Apple Watch as a second-class mirror of the iPhone screen. I lift four times a week — PPL into a touch of Upper/Lower when life gets busy — and I wanted a log I could rely on for a decade without paying rent on my own data. There's no team behind this. One person in Finland, shipping the app I wanted to use."
  support_email: "lagerland.apps@proton.me"
  response_time: "I reply to support emails personally, usually within a day."
  signals:
    - "Trains 4× a week — PPL with occasional Upper/Lower splits"
    - "Shipped 15 privacy-first Apple apps under Lagerland since 2025"
    - "Architecture is GDPR-first: local storage, optional iCloud sync, zero analytics SDKs"

# Plateau detection transparency — the algorithm rule disclosed publicly
plateau_disclosure:
  title: "How GymLogger X plateau detection actually works"
  rule: "Pro flags a plateau when an exercise's estimated 1RM has moved by less than 2% across nine or more consecutive sessions of consistent effort (stable RPE within ±0.5 and equal or higher volume)."
  what_it_does_not_do: "It will not auto-restructure your program. It will not nag you with notifications. It surfaces the flag on the exercise page with possible causes — training frequency, recovery, exercise selection, technique — and lets you decide. Programming changes are the lifter's call, not the app's."

who_for:
  - "You do strength training and want a fast, minimalist log — not a social fitness feed"
  - "You wear an Apple Watch and want real set/rep logging from your wrist, not a phone companion"
  - "You follow PPL, Upper/Lower, Full Body, or periodized programs and want plateau detection"
  - "You track RPE, RIR, or e1RM and want them first-class — not buried in settings"
  - "You're a coach who wants to ship programs to clients with structured periodization"
  - "You refuse subscription-locked workout apps and want a non-recurring lifetime option"

who_not_for:
  - "You primarily do cardio, group fitness, or bodyweight-only routines"
  - "You want guided video workouts or an AI trainer talking through sessions"
  - "You rely on social features, public leaderboards, or workout sharing"
  - "You train on Android (iOS only — for now)"

alternatives_to:
  - "Strong"
  - "Hevy"
  - "Fitbod"
  - "Caliber"
  - "Heavyset"

# 5-row comparison table — the most-aware buyer's exact question, answered
comparison_table:
  intro: "Every column below is a yes-or-no a serious lifter asks before switching workout apps. Strong, Hevy, and Fitbod each excel at something — GymLogger X is built for the lifter who wants Apple Watch as the actual log, a one-time price, and zero data extraction."
  competitors: ["GymLogger X", "Strong", "Hevy", "Fitbod"]
  rows:
    - feature: "Log sets from Apple Watch without iPhone"
      values: ["Yes — primary client", "Companion only", "Companion only", "Limited"]
    - feature: "One-time lifetime purchase"
      values: ["$44.99", "No (subscription only)", "No (subscription only)", "No (subscription only)"]
    - feature: "Works fully offline, no account required"
      values: ["Yes", "Account required", "Account required", "Account required"]
    - feature: "No third-party tracking SDKs"
      values: ["Zero", "Analytics + ads SDKs", "Analytics SDKs", "Analytics SDKs"]
    - feature: "Open data export (CSV + Apple Health)"
      values: ["Yes", "CSV (Pro)", "CSV", "Limited"]
    - feature: "RPE / RIR tracking"
      values: ["Yes", "Yes (Pro)", "Yes (Pro)", "No"]
    - feature: "Plateau detection rule disclosed publicly"
      values: ["Yes — published", "No", "No", "Opaque AI"]
  footnote: "Competitor positioning summarised from each app's public landing page and App Store description on 2026-05. Pricing and feature claims change frequently — verify before switching."

value_points:
  - title: "Apple Watch as the actual log"
    description: "Log every set, rep, RPE, and weight from your wrist. Rest timers, live heart rate, glanceable stats. The iPhone is the companion — not the other way around."
  - title: "Programs that adapt to you"
    description: "Smart Program Creator builds periodized PPL, Upper/Lower, Full Body, Arnold, or Bro Split — linear, DUP, block, or wave — with automatic deloads. Tell it your equipment, schedule, and injuries."
  - title: "Plateau detection that's actually transparent"
    description: "Pro flags a plateau when e1RM moves <2% across nine consecutive sessions at stable RPE. No black-box AI — the rule is published so you can argue with it."
  - title: "Lifetime price. Local data. Open exports."
    description: "$44.99 lifetime instead of forever subscriptions. All data on-device with optional iCloud sync. CSV and Apple Health export — your history is yours."

features:
  - title: "Smart Program Creator"
    description: "Tell GymLogger X your goals, equipment, schedule, experience level, and injury history. It generates a periodized program — linear, DUP, block, or wave — with injury-safe exercise selection, RPE-based load prescription, and automatic deload weeks. Supports PPL, Upper/Lower, Full Body, Arnold, and Bro Split. Not random workouts."
  - title: "Plateau detection (no black box)"
    description: "Pro insights flag stalls when an exercise's estimated 1RM moves less than 2% across nine consecutive sessions of consistent effort. Muscle imbalance detection (push:pull, quad:hamstring, biceps:triceps ratios), training load tracking, and fatigue monitoring help you read your own training. The rule is published — see below."
  - title: "Coach-designed programs"
    description: "Premium programs built by named strength coaches with structured periodization, progressive overload, and clear week-by-week guidance. Hypertrophy, powerlifting foundations, intermediate peaking blocks. One-time purchases — no rented programming."
  - title: "Apple Watch that actually works"
    description: "Full workout logging from your wrist. Quick set entry, RPE prompt, rest timers, live heart rate, and glanceable stats. Syncs automatically when you're done. Not a companion app — the primary client."
  - title: "Numbers serious lifters actually use"
    description: "Personal records, estimated 1RM (Epley + Brzycki), volume trends, weekly summaries, RPE distribution, Wilks and DOTS for powerlifters, and training consistency — all visualised clearly. Per-exercise PR analytics at 1/3/5/10 reps. Warmup calculator for working sets."
  - title: "Templates, supersets, giant sets"
    description: "Save any workout as a template. Reuse it next week with one tap. Supersets and giant sets are native, not workarounds. Drop sets, rest-pause, AMRAP — all first-class. Consistency becomes effortless."

screenshots:
  - src: "/assets/screenshots/gymlogger-x/1.png"
    alt: "GymLogger X home screen on iPhone showing today's workout, last session weights, and the Apple Watch sync status indicator"
  - src: "/assets/screenshots/gymlogger-x/2.png"
    alt: "GymLogger X Smart Program Creator on iPhone — generating a 12-week PPL program with DUP periodization, RPE prescription, and automatic deload weeks"
  - src: "/assets/screenshots/gymlogger-x/3.png"
    alt: "GymLogger X exercise detail view with estimated 1RM trend, set-by-set RPE history, and a plateau warning flag for bench press"
  - src: "/assets/screenshots/gymlogger-x/4.png"
    alt: "GymLogger X Apple Watch set logging screen — bench press third set, 80kg by 6 reps at RPE 8, rest timer running"
  - src: "/assets/screenshots/gymlogger-x/5.png"
    alt: "GymLogger X progress dashboard on iPhone showing weekly volume by muscle group, 1RM trends, training consistency, and muscle imbalance ratios"
  - src: "/assets/screenshots/gymlogger-x/6.png"
    alt: "GymLogger X exercise library on iPhone — animated demonstration of a barbell back squat with muscle targeting and equipment filters"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no analytics SDKs, no social feed"
    - "No account required — no email, no Apple ID, no sign-up"
    - "All data stays on device (optional iCloud sync, end-to-end encrypted by Apple)"
    - "Open CSV export + Apple Health export — your data is portable, not hostage"
    - "GDPR-first by architecture, not by policy paragraph"

coach_cta:
  title: "For Coaches"
  description: "GymLogger X partners with named, credentialled strength coaches — not anonymous content creators. Programs ship with clear periodization, progression rules, and the coach's bio."
  cta_label: "Learn about the coach program"
  url: "/apps/gymlogger-x/coaches/"

faq:
  - q: "What is GymLogger X?"
    a: "GymLogger X is a fast, minimalist strength training tracker for iPhone and Apple Watch — a private, no-subscription alternative to Strong, Hevy, and Fitbod. It includes 1,500+ exercises with animated demos, the Smart Program Creator, RPE and 1RM tracking, plateau detection, coach-designed programs, and full Apple Watch logging. Free at the core; Pro from $17.99/year or $44.99 lifetime."
  - q: "How is GymLogger X different from Strong, Hevy, and Fitbod?"
    a: "Three things. First, Apple Watch is the primary client — set entry, RPE, and rest timers live on the wrist, not the phone. Second, the price model is free + $44.99 lifetime, not a forever subscription. Third, the plateau detection rule is published (it flags when an exercise's e1RM moves under 2% across nine consecutive sessions of stable effort) rather than hidden inside an opaque AI."
  - q: "What is the Smart Program Creator?"
    a: "It generates personalised periodised training based on your goals, equipment, schedule, experience level, and injury history. Supports PPL, Upper/Lower, Full Body, Arnold, and Bro Split with linear, DUP, block, or wave periodisation, RPE-based load prescription, and automatic deload weeks. The program adapts week-to-week as you log sets — it doesn't just print a static spreadsheet."
  - q: "Does GymLogger X support RPE and RIR?"
    a: "Yes. RPE (Rate of Perceived Exertion) and RIR (Reps in Reserve) are first-class — they prompt during set logging on iPhone and Apple Watch, drive Smart Program load prescription, and feed into the plateau detection rule. RPE distribution per exercise and per week is visualised in the progress dashboard."
  - q: "Does GymLogger X calculate Wilks, DOTS, or Sinclair?"
    a: "Yes. For powerlifters, GymLogger X computes Wilks (2020 coefficients) and DOTS automatically from logged top sets in the squat, bench press, and deadlift. Olympic lifters get Sinclair on snatch and clean & jerk. The warmup calculator handles working-set ramp-ups for any lift."
  - q: "Does GymLogger X work on Apple Watch without the iPhone?"
    a: "Yes. Apple Watch is the primary log — set entry, RPE prompt, rest timers, live heart rate, and glanceable stats all work standalone. Sessions sync to iPhone automatically when you're done. You do not need to bring your phone to the gym."
  - q: "How does the plateau detection algorithm work?"
    a: "Plateau detection flags an exercise when its estimated 1RM (Epley) has moved less than 2% across nine or more consecutive sessions of consistent effort, defined as stable RPE within ±0.5 and equal or higher set-volume. It does not auto-restructure your program — it shows the flag, lists possible causes (frequency, recovery, exercise selection, technique), and leaves the programming call to you."
  - q: "Is GymLogger X free? What does Pro unlock?"
    a: "Core logging is free forever — exercise library, manual programs, basic progress, full Apple Watch logging, CSV and Apple Health export. Pro unlocks the Smart Program Creator, plateau detection, muscle imbalance analysis, RPE distribution and training load analytics, animated demos, and Wilks/DOTS/Sinclair. Pro is $17.99/year or $44.99 lifetime — pick the lifetime option if you plan to use the app for more than three years."
  - q: "Does GymLogger X need an account or internet connection?"
    a: "No. GymLogger X works fully offline with no account required — no email, no Apple ID, no sign-up flow. All data is stored locally with optional iCloud sync (end-to-end encrypted by Apple) and Apple Health export. There is no server to leak."
  - q: "Can I export my data if I leave?"
    a: "Yes. Full CSV export of every set, rep, weight, RPE, and timestamp — plus an Apple Health export. Your training history is yours; the app's job is to log it, not lock it in."
  - q: "What if my exercise isn't in the 1,500-exercise library?"
    a: "Create your own. Custom exercises include muscle targeting, equipment, set/rep schemes, and a notes field. Your custom exercises feed into the Smart Program Creator and the plateau detection rule like any built-in lift."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/gymlogger-x/support/"

release:
  first_release: "2025-09-01"
  last_updated: "2026-05-13"

ratings:
  value: "4.8"
  count: 16
  last_synced: "2026-05-13"
  display_label: "Early access"
---
GymLogger X is a fast, minimalist strength training tracker for iPhone and Apple Watch — built as a private, no-subscription alternative to Strong, Hevy, and Fitbod. The Smart Program Creator builds personalised periodised training (PPL, Upper/Lower, Full Body, Arnold, Bro Split) with linear, DUP, block, or wave periodisation, RPE-based load prescription, and automatic deloads. Pro insights surface plateau detection (e1RM moves under 2% across nine consecutive sessions of stable RPE), muscle imbalance analysis (push:pull, quad:hamstring, biceps:triceps), training load monitoring, and fatigue tracking. Coach-designed premium programs from named strength coaches add structured periodisation and progressive overload. Apple Watch is the primary client — set entry, RPE, rest timers, live heart rate, and automatic iPhone sync. Tracks personal records, 1RM estimates, RPE distribution, volume trends, Wilks/DOTS/Sinclair, and training consistency. No ads, no accounts, no tracking, no AI nagging. Free at the core; Pro from $17.99/year or $44.99 lifetime.
