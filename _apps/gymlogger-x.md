---
layout: app
slug: gymlogger-x
name: "GymLogger X"
quick_answer: "GymLogger X is a fast, minimalist strength training tracker for iPhone and Apple Watch — built as a private alternative to Strong, Hevy, and Fitbod. It logs every set from the wrist, generates periodized programs (PPL, Upper/Lower, Full Body) with automatic deloads, tracks RPE / 1RM / Wilks, and flags plateaus when an exercise stalls for nine or more sessions of consistent effort. Free at the core. $17.99/year or $44.99 lifetime — the cheapest one-time tier among major lifting apps. No ads, no tracking, no account."
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
  description: "A private alternative to Strong, Hevy & Fitbod. Apple Watch logging, smart programs, RPE & plateau detection. $44.99 lifetime — no account."
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
# entity_type lets the layout pick the correct schema.org itemtype (Person vs Organization).
founder:
  overline: "Why we built this"
  heading: "Built by lifters, for lifters."
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple studio · Finland"
  location: "Finland"
  photo: "/assets/icons/lagerland-mark.png"
  bio: "GymLogger X exists because every workout app we tried either rented our training history through a subscription, leaked data to ad networks, or treated Apple Watch as a second-class mirror of the iPhone screen. We wanted a log we could rely on for a decade without paying rent on our own data — and we couldn't find one. There's no team, no investors, no advertisers behind Lagerland. A small Apple studio in Finland, building the apps we wanted to use."
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails are answered personally, usually within a day."
  signals:
    - "Architecture is GDPR-first: local storage, optional iCloud sync, zero analytics SDKs"
    - "Lagerland's App Store catalogue is 15 privacy-first apps, all with the same data discipline"
    - "Funded by honest paid software — no ads, no investor pressure, no growth-hacking"
  external_link:
    href: "/lagerland-apps/"
    label: "Read the Lagerland studio backstory →"

# Plateau detection transparency — the algorithm rule disclosed publicly
plateau_disclosure:
  title: "How GymLogger X plateau detection actually works"
  rule: "Pro flags a plateau on an exercise when its estimated 1RM has moved less than ~2% across nine or more consecutive sessions of consistent effort — same exercise, comparable RPE, equal or higher volume. The exact thresholds are tuned over time as we collect more training data; we update this page when they change."
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

# 7-row comparison table — fact-checked against each competitor's public App Store page,
# landing page, and pricing documentation. Sources and verification date in the footnote.
comparison_table:
  intro: "Strong, Hevy, and Fitbod are good apps — millions of people use them happily. The table below is the defensible side-by-side a careful lifter looks at when picking where to keep a decade of training history. Verified against each app's public sources on the date in the footnote."
  competitors: ["GymLogger X", "Strong", "Hevy", "Fitbod"]
  rows:
    - feature: "Cheapest one-time / lifetime tier"
      values: ["$44.99 lifetime", "$99.99 lifetime (Strong PRO Forever)", "$74.99 lifetime", "Subscription only — no lifetime"]
    - feature: "Use the app with no account or sign-up"
      values: ["Yes — no email, no Apple ID", "Account required (Apple / Google / email)", "Account required", "Account required"]
    - feature: "Apple Watch — log a full session without the iPhone"
      values: ["Yes — primary surface", "Yes — full standalone", "Live-syncs to iPhone (not fully standalone)", "No — must connect to iPhone to log the workout"]
    - feature: "RPE / RIR tracking in the free tier"
      values: ["Yes — first-class", "Pro tier only", "Pro tier only", "Not exposed (AI sets the load)"]
    - feature: "CSV export of every set / rep"
      values: ["Yes — free tier", "Pro tier only", "Yes", "Limited"]
    - feature: "Plateau / progression rule published in plain English"
      values: ["Yes — algorithm disclosed", "No", "No", "No — proprietary AI"]
    - feature: "App Store nutrition label"
      values: ["Data Not Collected", "Multiple data categories Linked to You", "Multiple data categories Linked to You", "Multiple data categories Linked to You"]
  footnote: "Verified 2026-05-13 against each app's public App Store page, developer landing page, and pricing / help documentation: strongapp.io, hevyapp.com, fitbod.me. Competitor offerings change frequently — re-verify before switching."

value_points:
  - title: "Apple Watch as the actual log"
    description: "Log every set, rep, RPE, and weight from your wrist. Rest timers, live heart rate, glanceable stats. The iPhone is the companion — not the other way around."
  - title: "Programs that adapt to you"
    description: "Smart Program Creator builds periodized PPL, Upper/Lower, Full Body, Arnold, or Bro Split — linear, DUP, block, or wave — with automatic deloads. Tell it your equipment, schedule, and injuries."
  - title: "Plateau detection that's actually transparent"
    description: "Pro flags a plateau when e1RM moves under ~2% across nine consecutive sessions of comparable effort. No black-box AI — the rule is published in plain English so you can argue with it."
  - title: "Cheapest lifetime tier. Local data. Open exports."
    description: "$44.99 lifetime — cheaper than Hevy's $74.99 or Strong's $99.99 lifetime, and Fitbod doesn't offer one. All data on-device with optional iCloud sync. CSV and Apple Health export in the free tier — your history is yours."

features:
  - title: "Smart Program Creator"
    description: "Tell GymLogger X your goals, equipment, schedule, experience level, and injury history. It generates a periodized program — linear, DUP, block, or wave — with injury-safe exercise selection, RPE-based load prescription, and automatic deload weeks. Supports PPL, Upper/Lower, Full Body, Arnold, and Bro Split. Not random workouts."
  - title: "Plateau detection (no black box)"
    description: "Pro insights flag stalls when an exercise's estimated 1RM moves under ~2% across nine consecutive sessions of comparable effort. Muscle imbalance detection (push:pull, quad:hamstring, biceps:triceps ratios), training load tracking, and fatigue monitoring help you read your own training. The rule is published — see below."
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
    a: "Four practical differences. First, no account is required — Strong, Hevy, and Fitbod all need one. Second, Apple Watch is treated as the primary logging surface, not a companion display. Third, the lifetime tier is $44.99 — cheaper than Hevy's $74.99 or Strong's $99.99 lifetime, and Fitbod doesn't offer one. Fourth, the plateau detection rule is published in plain English (e1RM under ~2% across nine consecutive sessions of comparable effort) rather than hidden inside opaque AI."
  - q: "What is the Smart Program Creator?"
    a: "It generates personalised periodised training based on your goals, equipment, schedule, experience level, and injury history. Supports PPL, Upper/Lower, Full Body, Arnold, and Bro Split with linear, DUP, block, or wave periodisation, RPE-based load prescription, and automatic deload weeks. The program adapts week-to-week as you log sets — it doesn't just print a static spreadsheet."
  - q: "Does GymLogger X support RPE and RIR?"
    a: "Yes. RPE (Rate of Perceived Exertion) and RIR (Reps in Reserve) are first-class — they prompt during set logging on iPhone and Apple Watch, drive Smart Program load prescription, and feed into the plateau detection rule. RPE distribution per exercise and per week is visualised in the progress dashboard."
  - q: "Does GymLogger X calculate Wilks, DOTS, or Sinclair?"
    a: "Yes. For powerlifters, GymLogger X computes Wilks (2020 coefficients) and DOTS automatically from logged top sets in the squat, bench press, and deadlift. Olympic lifters get Sinclair on snatch and clean & jerk. The warmup calculator handles working-set ramp-ups for any lift."
  - q: "Does GymLogger X work on Apple Watch without the iPhone?"
    a: "Yes. Apple Watch is the primary log — set entry, RPE prompt, rest timers, live heart rate, and glanceable stats all work standalone. Sessions sync to iPhone automatically when you're done. You do not need to bring your phone to the gym."
  - q: "How does the plateau detection algorithm work?"
    a: "Plateau detection flags an exercise when its estimated 1RM (Epley) has moved less than ~2% across nine or more consecutive sessions of consistent effort, where effort is gauged by comparable RPE and equal or higher set-volume. The exact thresholds are tuned as we collect more training data. The flag does not auto-restructure your program — it surfaces on the exercise page with possible causes (frequency, recovery, exercise selection, technique), and leaves the programming call to you."
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
GymLogger X is a fast, minimalist strength training tracker for iPhone and Apple Watch — built as a private alternative to Strong, Hevy, and Fitbod with the cheapest lifetime tier ($44.99) and no account required. The Smart Program Creator builds personalised periodised training (PPL, Upper/Lower, Full Body, Arnold, Bro Split) with linear, DUP, block, or wave periodisation, RPE-based load prescription, and automatic deloads. Pro insights surface plateau detection (e1RM moves under ~2% across nine consecutive sessions of comparable effort), muscle imbalance analysis (push:pull, quad:hamstring, biceps:triceps), training load monitoring, and fatigue tracking. Coach-designed premium programs add structured periodisation and progressive overload. Apple Watch is the primary client — set entry, RPE, rest timers, live heart rate, and automatic iPhone sync. Tracks personal records, 1RM estimates (Epley + Brzycki), RPE distribution, volume trends, Wilks/DOTS/Sinclair, and training consistency. No ads, no accounts, no tracking, no AI nagging. Free at the core; Pro from $17.99/year or $44.99 lifetime.
