---
layout: app
slug: gymlogger-x
name: "GymLogger X"
quick_answer: "GymLogger X is a fast, minimalist strength training tracker for iPhone and Apple Watch — built as a private alternative to Strong, Hevy, and Fitbod. You start a session on the iPhone, then log each set's reps and weight from the wrist, with rest timers and live heart rate. The Smart Program Creator builds periodized programs (PPL, Upper/Lower, Full Body and more) with scheduled deload weeks, the app tracks estimated 1RM, and Pro flags a plateau when a lift's estimated 1RM stops climbing across your four most recent sessions while volume holds. Free at the core. $1.99/month, $17.99/year, or $39.99 lifetime — the cheapest one-time tier among major lifting apps. No ads, no tracking, no account."
category: fitness
platforms: ["iOS", "watchOS"]
status: live

app_store_url: "https://apps.apple.com/app/id6755734580"

price:
  model: freemium
  value: "Free — Pro from $1.99/mo, $17.99/yr, or $39.99 lifetime"
schema_price: "0"
schema_high_price: "39.99"
schema_offer_count: "4"

# Plans grid — Free / Pro Monthly / Pro Annual / Lifetime. The plans_footnote
# carries the USD-pricing disclaimer for international buyers and the App-Store
# refund pointer so the most common purchase-friction objections are answered
# next to the price, not buried in the FAQ.
plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. The lifetime tier is a one-time purchase — no auto-renew, no card kept on file beyond Apple's own."

plans:
  - name: "Free"
    price: "$0"
    summary: "Core logging, free forever. No trial, no card, no account."
    features:
      - "Unlimited set / rep / weight logging on iPhone and Apple Watch"
      - "1,500 exercises with muscle and equipment filters"
      - "One program at a time — built by hand, by the Smart Program Creator, or picked from six free built-ins (Linear 5×5, the Golden Six, split routines)"
      - "Up to three saved workout templates"
      - "PR alerts, per-exercise 1RM and volume charts, and the last 30 days of history"
      - "Apple Health workout export and a plate calculator"
      - "On-device storage, synced through your own iCloud"
  - name: "Pro Monthly"
    price: "$1.99 / mo"
    summary: "Full Pro, billed monthly. Cancel anytime."
    features:
      - "Unlimited programs and templates"
      - "The full program library: 38 more programs, from 5×5 ramps and the Texas Method to a peaking block"
      - "Your full workout history, PR board and strength trends"
      - "Plateau detection (the published adaptive-threshold rule)"
      - "Muscle balance (push:pull, upper:lower, front:back), training load and readiness analytics"
      - "Animated exercise demos and custom exercises"
      - "Import workouts and programs from CSV"
  - name: "Pro Annual"
    price: "$17.99 / year"
    summary: "Same Pro features, billed once a year. ~25% cheaper than paying monthly."
    features:
      - "Everything in Pro Monthly"
      - "~25% cheaper than paying monthly all year"
      - "Cancel anytime"
  - name: "Lifetime"
    price: "$39.99 one-time"
    summary: "Everything in Pro, forever. About one in three Pro users picks this tier — training history is a multi-year asset."
    features:
      - "Everything in Pro Annual — permanently unlocked"
      - "No subscription, no auto-renew, no expiring access"
      - "Family Sharing — share with up to 5 family members at no extra cost"
      - "Break-even vs the annual tier in ~2.2 years of use"
      - "Cheapest lifetime tier among major lifting apps ($39.99 vs Hevy $74.99 vs Strong $99.99)"
      - "Future Pro features included — no upsell on what you already paid for"
    highlight_label: "Best value · ~1 in 3 pick this"

icon: "/assets/icons/gymlogger-x.png"
og_image: "/assets/og/gymlogger-x.png"

seo:
  title: "GymLogger X — Strong & Hevy Alternative for Apple Watch"
  description: "A private alternative to Strong, Hevy & Fitbod. Apple Watch set logging, smart programs & plateau detection. $39.99 lifetime — no account."
  keywords:
    - Strong app alternative
    - Hevy alternative
    - Fitbod alternative
    - Caliber alternative
    - workout tracker no subscription
    - Apple Watch strength training app
    - private workout log iPhone
    - lifetime price workout tracker
    - strength training app no account
    - gym log app offline
    - PPL upper lower tracker
    - 1RM calculator app
    - plateau detection workout app
    - progressive overload tracker
    - training program generator iPhone
    - powerlifting log app
    - hypertrophy program app

hero:
  headline: "Strength training log for iPhone & Apple Watch."
  secondary: "Train smarter. Lift stronger."
  subheadline: "Your training history shouldn't be a subscription. GymLogger X is a private workout tracker with Apple Watch set logging, smart periodized programs, estimated-1RM tracking, and a $39.99 lifetime price. No ads, no account, no AI talking through your sets."
  cta_label: "Download Free"
  alt: "GymLogger X Push Day workout on iPhone — barbell bench press set 1 logged at 12 reps × 80 kg beside last session's sets, with the rest timer running"

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
    - "Architecture is GDPR-first: on-device storage, sync through your own iCloud, zero analytics SDKs"
    - "Lagerland's App Store catalogue is 20 privacy-first apps, all with the same data discipline"
    - "Funded by honest paid software — no ads, no investor pressure, no growth-hacking"
  external_link:
    href: "/lagerland-apps/"
    label: "Read the Lagerland studio backstory →"

# Plateau detection transparency — the algorithm rule disclosed publicly
plateau_disclosure:
  title: "How GymLogger X plateau detection actually works"
  rule: "Pro flags a plateau on an exercise when two signals agree across your four most recent non-deload sessions: the trend in estimated 1RM (Epley) fails to clear an improvement threshold computed from your own 90-day rate of gain on that lift — kept between 0.05% and 1% per session — while total volume has not fallen more than 3%, meaning you are working at least as hard for no more strength. Confirming also requires either a fatigue signal (training the lift twice in seven days, on back-to-back days, or with volume rising) or at least six non-deload sessions on the lift, plus a computed confidence score of at least 0.4; below that the flag is suppressed rather than shown to you. Three sessions meeting the same strength-and-volume test raise an earlier Monitoring flag instead. Detection stays off entirely for your first 12 weeks of training, and lifts whose 90-day rate of gain is under 0.08% per session, including lifts that have not moved at all, go to a separate trend analysis that labels them progressing, maintaining, regressing or uncertain, because a four-session window cannot tell a 0.08% gain from zero. We update this page when the thresholds change."
  what_it_does_not_do: "It will not auto-restructure your program or change your weights. It will not nag you with notifications. It surfaces the flag on the exercise with the likely cause — volume too high, intensity held too high, too little variation, or too little recovery — and two suggestions, such as a deload week or a change of rep range, and lets you decide. Programming changes are the lifter's call, not the app's."

# Method note — the same algorithm as plateau_disclosure, but structured as
# HowToStep[] so the layout emits HowTo JSON-LD eligible for SERP HowTo
# rendering and AI Overview citation. The visible "how-it-works" include
# also renders these steps as a numbered method list.
how_it_works:
  intro: "GymLogger X turns logged sets into a plateau warning using a transparent three-step rule. No machine-learning black box — you can audit every step."
  steps:
    - title: "Estimate 1RM from every set"
      detail: "Each set's load and reps are converted to an estimated 1RM using the Epley formula (weight × (1 + reps / 30)), with reps capped at 30; a single counts as its own 1RM. The session's per-exercise e1RM is the highest value across its sets, and deload sessions — those from a generated program's deload week, plus any you mark as one — are dropped from the analysis entirely so a light week cannot manufacture a flat trend."
    - title: "Compare against a threshold built from your own rate of gain"
      detail: "Rather than one fixed percentage for everybody, GymLogger X measures how fast you have actually been gaining on that lift over the last 90 days and sets the bar from that, kept between 0.05% and 1% per session. It then fits a trend line through your four most recent non-deload sessions. Detection needs at least eight sessions on the lift, relaxed to five if you train it infrequently, and a lift gaining under 0.08% per session over 90 days gets a trend reading instead of a plateau flag."
    - title: "Surface the flag, name the cause, leave the call to you"
      detail: "If the trend fails to clear your threshold while total volume holds within 3%, the exercise is flagged — as Monitoring after three such sessions, and as a confirmed plateau after four, provided a fatigue signal or at least six sessions on the lift back it up and the confidence score reaches 0.4. A confirmed flag names the likely cause (volume, intensity, variation, or recovery) and two suggestions. It does not auto-restructure your program and does not send notifications. Programming changes are the lifter's call, not the app's."

who_for:
  - "You do strength training and want a fast, minimalist log — not a social fitness feed"
  - "You wear an Apple Watch and want to log sets from your wrist while the phone stays in your bag"
  - "You follow PPL, Upper/Lower, Full Body, or periodized programs and want plateau detection"
  - "You care about estimated 1RM and want a plateau rule you can read, not a black box"
  - "You're a coach who wants clients to follow your program day by day — imported from a spreadsheet (Pro)"
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
  - "Jefit"
  - "Caliber"
  - "Heavyset"
  - "StrongLifts 5x5"
  - "Alpha Progression"

# 6-row comparison table — fact-checked against each competitor's public App Store page,
# landing page, and pricing documentation. Sources and verification date in the footnote.
comparison_table:
  intro: "Strong, Hevy, and Fitbod are good apps — millions of people use them happily. The table below is the defensible side-by-side a careful lifter looks at when picking where to keep a decade of training history. Verified against each app's public sources on the date in the footnote."
  competitors: ["GymLogger X", "Strong", "Hevy", "Fitbod"]
  rows:
    - feature: "Cheapest one-time / lifetime tier"
      values: ["$39.99 lifetime", "$99.99 lifetime (Strong PRO Forever)", "$74.99 lifetime", "Subscription only — no lifetime"]
    - feature: "Use the app with no account or sign-up"
      values: ["Yes — no email, no Apple ID", "Account required (Apple / Google / email)", "Account required", "Account required"]
    - feature: "Apple Watch — log a full session without the iPhone"
      values: ["No — logs sets from the wrist; the iPhone runs the session", "Yes — full standalone", "Live-syncs to iPhone (not fully standalone)", "No — must connect to iPhone to log the workout"]
    - feature: "CSV export of every set / rep"
      values: ["No — Apple Health workout export only", "Pro tier only", "Yes", "Limited"]
    - feature: "Plateau / progression rule published in plain English"
      values: ["Yes — algorithm disclosed", "No", "No", "No — proprietary AI"]
    - feature: "App Store nutrition label"
      values: ["Data Not Collected", "Multiple data categories Linked to You", "Multiple data categories Linked to You", "Multiple data categories Linked to You"]
  footnote: "Verified 2026-05-13 against each app's public App Store page, developer landing page, and pricing / help documentation: strongapp.io, hevyapp.com, fitbod.me. Competitor offerings change frequently — re-verify before switching."

value_points:
  - title: "Log from the wrist"
    description: "Start the session on your iPhone, then log each set's reps and weight, run rest timers, and watch live heart rate on Apple Watch. The phone keeps the record and can stay in your bag."
  - title: "Programs built around you"
    description: "Smart Program Creator builds periodized Full Body, Upper/Lower, PPL, Push/Pull, Arnold, or Bro Split programs — linear, DUP, block, or wave — with scheduled deload weeks. Tell it your equipment, schedule, and injuries."
  - title: "Plateau detection that's actually transparent"
    description: "Pro flags a plateau when e1RM stops clearing a threshold set by your own 90-day rate of gain while volume holds steady. No black-box AI — the rule is published in plain English so you can argue with it."
  - title: "Cheapest lifetime tier. Your data, your devices."
    description: "$39.99 lifetime — cheaper than Hevy's $74.99 or Strong's $99.99 lifetime, and Fitbod doesn't offer one. Workouts stay on your devices and sync through your own iCloud, and every finished session can be saved to Apple Health."

features:
  - title: "Smart Program Creator"
    description: "Tell GymLogger X your goals, equipment, schedule, experience level, and injury history. It generates a periodized program — linear, DUP, block, or wave — with injury-aware exercise selection, a rep range and reps-in-reserve target for every exercise, and scheduled deload weeks. Supports Full Body, Upper/Lower, PPL, Push/Pull, Arnold, and Bro Split. Free accounts keep one program; Pro removes the limit. Not random workouts."
  - title: "Plateau detection (no black box)"
    description: "Pro insights flag stalls when an exercise's estimated 1RM stops clearing a threshold built from your own recent rate of gain, while total volume holds steady. Muscle balance (push:pull, upper:lower, front:back, plus neglected muscles), training load tracking, and fatigue monitoring help you read your own training. The rule is published — see below."
  - title: "A built-in program library"
    description: "44 ready-made programs: six free, including a linear 5×5 and the Golden Six, and 38 more with Pro — 5×5 variations, the Texas Method, Push/Pull/Legs, powerbuilding, glute specializations, and a 6-week peaking block. Preview every week before you start, or customize a copy."
  - title: "Apple Watch set logging"
    description: "Log reps and weight for each set from your wrist, with rest timers, live heart rate, and the workout at a glance. The iPhone starts and runs the session; sets logged on the watch wait there until the phone receives them."
  - title: "Numbers serious lifters actually use"
    description: "Personal records, estimated 1RM (Epley), volume trends, weekly summaries, weekly hard sets per muscle, and training consistency — all visualised clearly. A rep-max table at 1/3/5/8/10/12 reps per exercise, and a plate calculator for loading the bar."
  - title: "Templates, supersets, giant sets"
    description: "Save any workout as a template and reuse it next week with one tap (three templates on the free tier). Supersets and giant sets are native, not workarounds, and warm-up sets can be marked so they stay out of your weekly set counts. Consistency becomes effortless."

screenshots:
  - src: "/assets/screenshots/gymlogger-x/1.png"
    alt: "GymLogger X Push Day workout on iPhone — barbell bench press set 1 logged at 12 reps × 80 kg beside last session's sets, with a 47-second rest timer running"
  - src: "/assets/screenshots/gymlogger-x/2.png"
    alt: "GymLogger X Progress overview on iPhone with a trend summary, two exercises on plateau Monitoring, and a push/pull training-balance bar"
  - src: "/assets/screenshots/gymlogger-x/3.png"
    alt: "GymLogger X personal records tab on iPhone ranking top estimated 1RMs — barbell squat 105 kg, bench press 87.1 kg — with filters for best weight, highest reps, and 1RM"
  - src: "/assets/screenshots/gymlogger-x/4.png"
    alt: "GymLogger X workout template editor on iPhone for Push Day, with bench press and overhead press grouped as a superset"
  - src: "/assets/screenshots/gymlogger-x/5.png"
    alt: "GymLogger X Training screen on iPhone with Start Empty Workout, Start From Template, an active 2-Day Split Routine program, and a completed program"
  - src: "/assets/screenshots/gymlogger-x/6.png"
    alt: "GymLogger X 30-day muscle balance heatmap on iPhone, flagging overloaded quadriceps and front shoulders and neglected glutes"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no analytics SDKs, no social feed"
    - "No account required — no email, no Apple ID sign-in, no sign-up"
    - "Workouts stay on your devices and in your own private iCloud"
    - "Apple Health export — finished sessions are saved as strength-training workouts"
    - "GDPR-first by architecture, not by policy paragraph"

coach_cta:
  title: "For Coaches"
  description: "Coaches can recommend GymLogger X through a referral partnership, and clients can import a coach's spreadsheet program (Pro) and follow it day by day."
  cta_label: "Learn about the coach program"
  url: "/apps/gymlogger-x/coaches/"

faq:
  - q: "What is GymLogger X?"
    a: "GymLogger X is a fast, minimalist strength training tracker for iPhone and Apple Watch — a private alternative to Strong, Hevy, and Fitbod. It includes 1,500 exercises (animated demos with Pro), the Smart Program Creator, a 44-program library, estimated-1RM tracking, plateau detection, and Apple Watch set logging. Free at the core; Pro from $1.99/month, $17.99/year, or $39.99 lifetime."
  - q: "How is GymLogger X different from Strong, Hevy, and Fitbod?"
    a: "Four practical differences. First, no account is required — Strong, Hevy, and Fitbod all need one. Second, the session is built for logging from Apple Watch: set entry, rest timers, and live heart rate on the wrist while the iPhone runs the session in your bag. Third, the lifetime tier is $39.99 — cheaper than Hevy's $74.99 or Strong's $99.99 lifetime, and Fitbod doesn't offer one. Fourth, the plateau detection rule is published in plain English (e1RM failing to clear a threshold set by your own 90-day rate of gain, while volume holds steady) rather than hidden inside opaque AI."
  - q: "What is the Smart Program Creator?"
    a: "It generates personalised periodised training based on your goals, equipment, schedule, experience level, and injury history. Supports Full Body, Upper/Lower, PPL, Push/Pull, Arnold, and Bro Split with linear, DUP, block, or wave periodisation, a rep range and reps-in-reserve target for each exercise, and scheduled deload weeks. You can preview the whole program and swap exercises before you start. During a session each exercise pre-fills the weight you used last time; the app does not raise your weights for you. Free accounts keep one program; Pro removes the limit."
  - q: "Does GymLogger X support RPE and RIR?"
    a: "Partly. Programs from the Smart Program Creator give each exercise a reps-in-reserve (RIR) target, shown in the program preview, and programs imported from a spreadsheet can carry an RIR or RPE column. Logged sets record weight and reps only — there is no per-set RPE or RIR entry — and the analytics, including the plateau rule, work from those two numbers. <a href=\"/journal/rpe-and-rir-explained/\">RPE and RIR, explained</a> covers why, and what that means if you rate every set."
  - q: "Does GymLogger X calculate Wilks, DOTS, or Sinclair?"
    a: "No. GymLogger X does not compute Wilks, DOTS, or Sinclair scores. It tracks estimated 1RM (Epley) for every lift, a rep-max table at 1, 3, 5, 8, 10, and 12 reps, and your personal records, and it has a plate calculator for loading the bar."
  - q: "Does GymLogger X work on Apple Watch without the iPhone?"
    a: "No. The iPhone starts and runs the workout; the Apple Watch app is where you log each set's reps and weight, run rest timers, and see live heart rate. The phone can stay in your bag nearby, and sets logged on the watch wait there until the iPhone receives them."
  - q: "How does the plateau detection algorithm work?"
    a: "Plateau detection flags an exercise when its estimated 1RM (Epley) stops clearing an improvement threshold derived from your own 90-day rate of gain on that lift (kept between 0.05% and 1% per session), across your four most recent non-deload sessions, while total volume has not dropped more than 3%. Confirming needs a fatigue signal or at least six sessions on the lift behind it, and a confidence score of at least 0.4. We update the published rule when the thresholds change. The flag does not auto-restructure your program — it surfaces on the exercise with the likely cause (volume, intensity, variation, or recovery) and two suggestions, and leaves the programming call to you."
  - q: "Is GymLogger X free? What does Pro unlock?"
    a: "Core logging is free forever — unlimited set logging on iPhone and Apple Watch, the exercise library, one program at a time, three templates, the last 30 days of history, and Apple Health export. Pro unlocks unlimited programs and templates, the full 44-program library, your full history, plateau detection, muscle balance and training load analytics, animated demos, custom exercises, and CSV import. Pro is $1.99/month, $17.99/year, or $39.99 lifetime — pick the lifetime option if you plan to use the app for more than ~2 years. Lifetime supports Family Sharing — one purchase covers up to 5 family members at no extra cost. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does GymLogger X need an account or internet connection?"
    a: "No. Logging works fully offline with no account — no email, no Apple ID sign-in, no sign-up flow. Workouts are stored on your device and synced through your own private iCloud, and finished sessions can be saved to Apple Health. Lagerland's server never receives your workouts: the app sends it only a random install ID (with a referral code, if you used one) and, when you buy Pro, the purchase details needed to verify it."
  - q: "Can I export my data if I leave?"
    a: "Not as a spreadsheet — there is no CSV export of sets and reps yet. Each finished workout can be saved to Apple Health as a strength-training session, any workout can be shared as text listing every set, and your history stays in your own iCloud. Coming from another app? Pro can import your workouts from a CSV."
  - q: "What if my exercise isn't in the 1,500-exercise library?"
    a: "Create your own with Pro. A custom exercise takes a name, primary muscles, equipment, and difficulty, and is logged and tracked like any built-in lift, plateau detection included."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/gymlogger-x/support/"

release:
  first_release: "2025-12-03"
  last_updated: "2026-10-16"

related_journal:
  slug: "choosing-a-strength-program-you-will-finish"
  anchor: "PPL, Upper/Lower or 5/3/1 - choosing a program you will actually finish"

ratings:
  value: "4.8"
  count: 17
  last_synced: "2026-06-22"
---
GymLogger X is a fast, minimalist strength training tracker for iPhone and Apple Watch — built as a private alternative to Strong, Hevy, and Fitbod with the cheapest lifetime tier ($39.99) and no account required. The Smart Program Creator builds personalised periodised training (Full Body, Upper/Lower, PPL, Push/Pull, Arnold, Bro Split) with linear, DUP, block, or wave periodisation, reps-in-reserve targets, and scheduled deload weeks, and a 44-program library adds ready-made plans. Pro insights surface plateau detection (e1RM failing to clear a threshold derived from your own recent rate of gain, while volume holds steady), muscle balance analysis (push:pull, upper:lower, front:back), training load monitoring, and fatigue tracking. On Apple Watch you log each set's reps and weight, run rest timers, and see live heart rate while the iPhone runs the session. Tracks personal records, 1RM estimates (Epley), volume trends, and training consistency. No ads, no accounts, no tracking, no AI nagging. Free at the core; Pro from $1.99/month, $17.99/year, or $39.99 lifetime.
