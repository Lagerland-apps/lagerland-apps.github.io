---
layout: app
slug: liftlog
name: "LiftLog"
tagline: "The lift log that feels like equipment."
quick_answer: "LiftLog is a design-led strength training log for iPhone built around tabular numerics, haptic-rich workout sessions, and athlete-grade polish. It supports periodized programs (PPL, Upper/Lower, 5/3/1), tracks 1RM, volume, and Rep PRs at 1/3/5 reps. Free 7-day trial, no card. Pay-what-you-can one-time from $9.99 to $39.99. No subscription, no tracking, no account."
category: fitness
platforms: ["iOS"]
status: live

app_store_url: "https://apps.apple.com/app/id6760043411"

price:
  model: one-time
  value: "Free 7-day trial — then $9.99–$39.99 (pay what you can, one-time)"
schema_price: "9.99"

plans:
  - name: "Free trial"
    price: "$0 / 7 days"
    summary: "Full access. No card. No auto-renew."
    features:
      - "Every periodized program template"
      - "Tabular numerics + haptic keypad"
      - "1RM, Rep PRs, 90-day heatmap"
      - "Optional iCloud sync — no account"
  - name: "Fair"
    price: "$9.99 once"
    summary: "Entry tier. The whole app, forever."
    features:
      - "Everything in the trial"
      - "Lifetime access — one purchase"
      - "All future feature updates"
      - "No subscription, no auto-renew"
  - name: "Good"
    price: "$19.99 once"
    summary: "The honest middle. Same app, picked because the work is worth it."
    features:
      - "Everything in Fair"
      - "Supports continued development"
  - name: "Generous"
    highlight: true
    price: "$29.99 once"
    summary: "Most chosen. Pays for a few weeks of focused work."
    features:
      - "Everything in Good"
      - "Funds new programs and analytics"
  - name: "Patron"
    price: "$39.99 once"
    summary: "Top tier. For fans backing a tiny indie studio."
    features:
      - "Everything in Generous"
      - "Same app — no hidden Patron-only features"
      - "Direct support email gets answered first"

icon: "/assets/icons/liftlog.png"
og_image: "/assets/og/liftlog.png"

seo:
  title: "Strength Training Log for iPhone — Pay What You Can | LiftLog"
  description: "Design-led strength training log for iPhone. Periodized programs, 1RM analytics, haptic sets, PRs. Free 7-day trial, no card — then pay what you can, one-time."
  keywords:
    - premium workout tracker iphone
    - design-led strength training app
    - minimalist lifting log
    - athlete grade workout app
    - iOS strength training tracker
    - beautiful workout app iphone
    - tabular workout numerics
    - haptic workout app
    - personal record tracker iphone
    - lift tracker app
    - barbell training log
    - powerlifting log app
    - hypertrophy workout tracker
    - PR tracker iphone
    - 1RM calculator workout app
    - volume tracker lifting
    - progressive overload app
    - rest timer workout app
    - workout session app iphone
    - premium fitness app no ads
    - pay what you can workout app
    - workout app no subscription
    - no auto-renew fitness app
    - one time purchase workout tracker
    - 7 day free trial fitness app no card

hero:
  headline: "The strength training log for iPhone."
  secondary: "Train the way you log."
  subheadline: "Design-led strength tracker for iPhone — tabular numerics, haptic-rich workout sessions, periodized programs (PPL, Upper/Lower, 5/3/1, DUP), and PR moments rendered with the polish of a piece of equipment."
  pre_headline: "Open it. Log one workout. If LiftLog isn't worth $9.99 to you, don't pay. Seven days free, no card on file, no auto-renew — then you decide what it's worth, once."
  cta_label: "Start 7-Day Free Trial — No Card"
  alt: "LiftLog strength training session on iPhone — custom haptic numeric keypad, tabular set numerics, and rest-timer ring"

who_for:
  - "You lift seriously and want a log that feels as deliberate as your training"
  - "You appreciate craft — typography, depth, motion — and notice when an app cuts corners"
  - "You want big, legible, tabular numerics during a working set, not body-copy text"
  - "You follow a structured program — PPL, Upper/Lower, Full Body, 5/3/1, hypertrophy blocks — and want it visualized cleanly"
  - "You celebrate PRs and want them to feel like a moment, not a row in a list"

who_not_for:
  - "You primarily do cardio, group fitness, or bodyweight-only routines"
  - "You want a social feed, public leaderboards, or workout sharing"
  - "You want a coach in your ear or guided video workouts during sessions"
  - "You prefer maximum feature surface area over editorial restraint"

alternatives_to:
  - "Strong"
  - "Hevy"
  - "Caliber"
  - "Ladder"
  - "Heavyset"

plateau_disclosure:
  title: "How LiftLog calculates 1RM, volume, and the deload trigger"
  rule: "Estimated 1RM uses the Epley formula — 1RM ≈ weight × (1 + reps / 30) — the most widely cited estimator in the strength-training literature (Epley, 1985). PRs are detected per exercise across three rep buckets: best 1-rep (true 1RM), best 3-rep, and best 5-rep — plus best volume per session and best estimated 1RM across all sets. Weekly per-muscle volume is tracked against your trailing four-week MRV (Maximum Recoverable Volume); when accumulated volume crosses your MRV trend, the next week is rendered as an automatic deload."
  what_it_does_not_do: "It does not invent rep ranges you didn't log, average across exercises, or 'normalize' sets you tagged as warmup, drop, or failure. Estimated 1RM is shown alongside your actual top single — and the actual single always wins when you have one."
  notes:
    - "For reps above 10, estimated 1RM is less reliable — the page surfaces the rep count so you can judge it yourself."
    - "RPE / RIR, when logged, narrows the estimate (a 5@8 is treated differently than a 5@10)."
    - "Training Max (5/3/1) is a separate field — typically 85–90% of tested 1RM, per Jim Wendler's protocol — and drives program weights, not your PR history."
    - "Volume landmarks (MV / MEV / MAV / MRV) follow the framework popularized by Dr. Mike Israetel and the Renaissance Periodization team — and feed the automatic deload calculation."
    - "Volume = sets × reps × weight, with optional bodyweight loading on chin-ups, dips, and pull-ups."

training_vocabulary:
  collapse_by_default: true
  intro: "LiftLog is built for lifters who already know what they're running. It speaks the language — Renaissance Periodization volume landmarks (Israetel et al.), RPE-based autoregulation (Tuchscherer / Helms), and block periodization (Issurin)."
  groups:
    - heading: "Programming"
      items:
        - "Progressive overload — the central rule, applied automatically across mesocycles"
        - "Mesocycle, microcycle, deload week — rendered as a clean dashboard, not a wall of cards"
        - "Linear, DUP (Daily Undulating Periodization), block, wave, and conjugate periodization"
        - "5/3/1 with Training Max, AMRAP top sets, Boring But Big variants"
        - "PPL, Upper/Lower, Full Body 3×, Starting Strength, Bro Split, custom"
    - heading: "Sets &amp; loading"
      items:
        - "Working set, warmup set, top set, back-off set, drop set, failure set, cluster set"
        - "RPE 1–10 and RIR (Rep In Reserve), optional per program"
        - "Tempo notation across the three phases — eccentric (lowering), isometric (pause), concentric (lift)"
        - "Per-side plate breakdown with custom bar weight (20 kg, 45 lb, EZ bar, safety squat bar)"
    - heading: "Volume &amp; recovery"
      items:
        - "Weekly per-muscle volume in working sets — the unit research actually uses"
        - "MV (Maintenance Volume) — the floor that keeps strength where it is"
        - "MEV (Minimum Effective Volume) — the start of a mesocycle, the lowest dose that drives growth"
        - "MAV (Maximum Adaptive Volume) — the productive middle, where most weeks live"
        - "MRV (Maximum Recoverable Volume) — the ceiling before fatigue eats progress; deload trigger"
        - "Automatic deload weeks when accumulated volume crosses your MRV trend"
    - heading: "Analytics"
      items:
        - "Estimated 1RM (Epley) — see method note above"
        - "Rep PRs at 1, 3, and 5 reps — actual top sets, not just estimates"
        - "Best volume per session and per exercise"
        - "30-day, 90-day, and all-time deltas vs. prior period"
        - "GitHub-style 90-day activity heatmap"

comparison_table:
  intro: "LiftLog versus the four most-searched iPhone strength trackers on three things lifters actually care about: pricing model, what you give up to use it, and whether your training history is yours forever."
  competitors:
    - "LiftLog"
    - "Strong"
    - "Hevy"
    - "Fitbod"
  rows:
    - feature: "Pricing model"
      values:
        - "Pay-what-you-can $9.99–$39.99, one-time"
        - "Free + Pro subscription"
        - "Free + Pro subscription"
        - "Subscription only"
    - feature: "Free trial — no card required"
      values:
        - "✓ 7 days, no card"
        - "Free tier (limited routines)"
        - "Free tier"
        - "Trial with card"
    - feature: "Account required"
      values:
        - "No"
        - "For sync"
        - "For sync + social"
        - "Yes"
    - feature: "Third-party tracking"
      values:
        - "None"
        - "Standard analytics"
        - "Standard analytics"
        - "Standard analytics"
    - feature: "Periodization (linear, DUP, block, wave)"
      values:
        - "All four + auto deload"
        - "Manual via routines"
        - "Manual via routines"
        - "AI auto-progression"
    - feature: "Estimated 1RM + Rep PRs (1/3/5)"
      values:
        - "✓ Epley + actual"
        - "✓ Pro"
        - "✓"
        - "✓"
    - feature: "Apple Watch logging"
      values:
        - "Not yet — see GymLogger X"
        - "Yes"
        - "Yes"
        - "Yes"
    - feature: "Social feed / leaderboards"
      values:
        - "None"
        - "Limited"
        - "Yes (core feature)"
        - "Limited"
    - feature: "Training history portable after you stop paying"
      values:
        - "Yes — you own it"
        - "Read-only without Pro"
        - "Read-only without Pro"
        - "Lost when sub lapses"
  footnote: "Competitor details reflect publicly documented features as of 2026. LiftLog's pay-what-you-can pricing means you choose your tier — $9.99 Fair, $19.99 Good, $29.99 Generous, $39.99 Patron — once. The App Store is the canonical source for current pricing."

value_points:
  - title: "Numbers are the product"
    description: "Weights, reps, PRs, and volume are rendered with tabular figures, calibrated tracking, and a stadium-scoreboard hierarchy. The set you're working on is the brightest thing on the screen — everything else recedes."
  - title: "Workout sessions designed for working sets"
    description: "A custom numeric keypad with haptic feedback. Set completion sweeps a green confirmation across the row. The rest timer wraps the screen with a progress ring. Built for thumbs holding a phone between sets — not a designer's portfolio shot."
  - title: "Pay what you can. Once."
    description: "Seven days free, no card required. Then choose what LiftLog is worth: $9.99 Fair, $19.99 Good, $29.99 Generous, $39.99 Patron. One-time. No auto-renew. No trial trap. No subscription tax on your training history."
  - title: "PR moments that feel like moments"
    description: "When you hit a personal record, LiftLog notices. A success haptic, a subtle glow pulse, a logged moment in your history. Your best lifts deserve a celebration — not just a row."

features:
  - title: "Tabular numerics from end to end"
    description: "Every weight, rep, set, time, volume, and 1RM uses tabular figures — numbers that line up vertically across rows so trends are readable at a glance. No drift, no jitter, no wandering decimal points."
  - title: "Haptic-rich workout session view"
    description: "Custom numeric keypad replaces the system one — bigger keys, calibrated taps, haptic feedback on every digit. Set completion is a deliberate gesture: spring animation, success haptic, green sweep. You feel the workout, not just see it."
  - title: "Programs with proper periodization"
    description: "Push / Pull / Legs, Bro Split, Upper / Lower, Starting Strength, Full Body 3× — and your own. Linear, DUP, block, or wave periodization with automatic deload weeks. Your weekly mesocycle is rendered as a clean dashboard, not a wall of cards."
  - title: "Exercise library with anatomy-aware browsing"
    description: "Each exercise has an X-ray-style anatomy render, primary and secondary muscle tags, and a numbered HOW-TO with a connected vertical rail. Browse by muscle group, equipment, or movement pattern. Find any exercise in two taps."
  - title: "Progress that earns its space"
    description: "Big stats — workouts, total volume, sets — over 30 days, 90 days, all time. Each stat ships with a delta vs. the prior period. A GitHub-style activity heatmap shows your last 90 days at a glance. Per-exercise: estimated 1RM, best set, best volume, and Rep PRs at 1, 3, and 5 reps."
  - title: "Restraint is the design"
    description: "One accent color. One display typeface. One spacing scale. Every card uses the same elevation system. Every number uses the same numeric scale. The result: nothing competes for attention with the set you're about to lift."
  - title: "Privacy by default"
    description: "No third-party analytics. No advertising SDKs. No social feed. No required account. Workout history lives on your device with optional iCloud sync to your own Apple ID."
  - title: "Pay-what-you-can pricing — once"
    description: "Free for seven days, no card on file. After the trial, choose your tier: $9.99 Fair, $19.99 Good, $29.99 Generous, $39.99 Patron. One-time payment. No auto-renew. No trial trap. You own it — and your training history isn't held hostage by a lapsed subscription."

screenshots:
  - src: "/assets/screenshots/liftlog/1.png"
    alt: "LiftLog workout session view on iPhone with custom haptic numeric keypad, tabular set numerics, and a rest-timer progress ring"
  - src: "/assets/screenshots/liftlog/2.png"
    alt: "LiftLog routines dashboard — Push/Pull/Legs, Upper/Lower, Starting Strength and 5/3/1 program cards with weekly mesocycle layout"
  - src: "/assets/screenshots/liftlog/3.png"
    alt: "LiftLog per-exercise progress screen with estimated 1RM trend line, best set, best volume, and Rep PRs at 1, 3 and 5 reps"
  - src: "/assets/screenshots/liftlog/4.png"
    alt: "LiftLog exercise library on iPhone — X-ray-style anatomy render, primary and secondary muscle tags, and a numbered HOW-TO rail"
  - src: "/assets/screenshots/liftlog/5.png"
    alt: "LiftLog GitHub-style 90-day activity heatmap and total volume / workouts / sets stats with 30-day deltas vs. the prior period"
  - src: "/assets/screenshots/liftlog/6.png"
    alt: "LiftLog personal record moment — success haptic, glow pulse, and PR badge logged in workout history"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no analytics SDKs, no social feed"
    - "No account required — open the app and start lifting"
    - "All workout data stays on your device by default"
    - "Optional iCloud sync uses your own Apple ID — Lagerland Apps never sees or stores your data"
    - "Optional Apple Health export for workouts and active energy"

faq:
  - q: "What is LiftLog?"
    a: "LiftLog is a design-led strength training log for iPhone. It's built around a tabular-numeric type system, haptic-rich workout sessions with a custom numeric keypad, periodized programs (PPL, Upper/Lower, Full Body, Starting Strength, Bro Split, custom), and deep per-exercise analytics — estimated 1RM, best set, best volume, Rep PRs at 1/3/5 reps, and a 90-day activity heatmap. Free seven-day trial, no card required, then a one-time pay-what-you-can purchase from $9.99 to $39.99."
  - q: "How is LiftLog different from GymLogger X?"
    a: "LiftLog and GymLogger X are sister apps from Lagerland Apps that approach strength training from different angles. GymLogger X is a fast, minimalist logger with Apple Watch as a first-class client — optimized for workflow speed at a $44.99 lifetime price. LiftLog is design-led and iPhone-first: tabular numerics, haptic-rich sessions, restrained typography, and a pay-what-you-can one-time purchase from $9.99 to $39.99. Pick GymLogger X if you live on Apple Watch. Pick LiftLog if you care about the polish and craft of every screen — and like the idea of choosing your own price."
  - q: "How much does LiftLog cost?"
    a: "LiftLog is free for seven days — no card required and no auto-renew. After the trial, you choose what it's worth to you: $9.99 (Fair), $19.99 (Good), $29.99 (Generous), or $39.99 (Patron). All four are one-time payments — no subscription, no recurring charge, no trial trap. Pick the tier that matches what the app is worth to you and you own it."
  - q: "Why pay-what-you-can pricing?"
    a: "Strength training is a long-term practice. We don't think your training history should be held hostage by a lapsed subscription, and we don't want a credit card on file just to start. Seven days free without a card means you only pay if it earns your money. The four-tier ladder lets newer lifters in at $9.99 while letting fans support the work at $39.99 — the same app, your call. The launch journal post explains the bet in more detail: https://lagerland-apps.github.io/journal/liftlog-pay-what-you-can/"
  - q: "Does LiftLog support Apple Watch?"
    a: "LiftLog is iPhone-first by design. The workout session view is built around a custom numeric keypad and haptic feedback that wouldn't translate to a small wrist screen. If you primarily log from Apple Watch, GymLogger X is the better fit — it treats Apple Watch as a first-class client."
  - q: "What programs does LiftLog support?"
    a: "PPL (Push/Pull/Legs), Upper/Lower, Full Body, 5/3/1, hypertrophy blocks, and custom periodized templates. Linear, DUP (Daily Undulating Periodization), block (model adapted from Vladimir Issurin's block periodization framework), conjugate (Westside Barbell tradition), and wave periodization — all with automatic deload weeks built in."
  - q: "Does LiftLog track personal records?"
    a: "Yes. LiftLog tracks PRs by exercise — best 1RM (estimated and actual), best volume, and best rep ranges. When you hit a new PR mid-session, LiftLog acknowledges it with a haptic and a quiet visual celebration."
  - q: "Does LiftLog need an account or internet connection?"
    a: "No. LiftLog works fully offline with no account required. Workout data stays on your device, with optional iCloud sync using your own Apple ID — Lagerland Apps never sees or stores your data."
  - q: "Can I import workouts from Strong, Hevy, or another tracker?"
    a: "Yes. LiftLog supports import from common workout-tracker CSV exports. Open the export from Strong, Hevy, or your previous logger and LiftLog will map exercises, sets, reps, and weights into your history."
  - q: "How does LiftLog estimate 1RM?"
    a: "LiftLog uses the Epley formula — 1RM ≈ weight × (1 + reps / 30) — as the default estimator, which is the most widely cited formula in strength training literature (Epley, 1985). For sets above 10 reps the estimate becomes less reliable, so LiftLog also surfaces your actual best 1-rep, 3-rep, and 5-rep sets so you can compare estimated vs. true single-rep performance. Your actual top single always wins over an estimate."
  - q: "Does LiftLog support 5/3/1 and Training Max?"
    a: "Yes. The 5/3/1 template lets you set a Training Max (typically 85–90% of your tested 1RM, per Jim Wendler's protocol) and runs the standard 5/3/1, 3/5/1, and Boring But Big variants on top of it. AMRAP top sets are logged with the rep count so your estimated 1RM updates after each cycle. Linear, DUP (Daily Undulating Periodization), block, and wave periodization are also built in, with automatic deload weeks."
  - q: "Does LiftLog support RPE or RIR (Rep In Reserve)?"
    a: "Yes — optionally. You can log each set with an RPE (Rate of Perceived Exertion, 1–10) or RIR value if you train with autoregulation, following the RPE-based autoregulation framework attributed to Mike Tuchscherer and refined for hypertrophy by Eric Helms (3D Muscle Journey / Iron Culture). The field is hidden by default to keep the working-set view uncluttered, and switches on per-program in settings. PR detection and 1RM estimation both factor RPE in when present."
  - q: "Is there a plate calculator?"
    a: "Yes. The session view shows the per-side plate breakdown for any working weight using your selected bar weight (default 20 kg / 45 lb, customizable per exercise for dumbbells, EZ bar, safety squat bar, etc.) and only counts plates you have in your gym profile."
  - q: "How fresh is LiftLog's content and pricing?"
    a: "This page is maintained alongside each App Store release. Current version notes, release date and last-updated date are shown in the page footer. The pay-what-you-can tiers ($9.99 / $19.99 / $29.99 / $39.99) and the 7-day trial without a card are the live App Store configuration — if Apple's StoreKit ever shows different numbers, the App Store is canonical."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/liftlog/support/"

release:
  first_release: "2026-04-25"
  last_updated: "2026-04-25"

related_journal:
  slug: "liftlog-pay-what-you-can"
  anchor: "Why pay-what-you-can pricing — the bet, in our own words"

ratings:
  value: "5.0"
  count: 1
  last_synced: "2026-04-29"
---
LiftLog is a design-led strength training log for iPhone. Built around a tabular-numeric type system, haptic-rich workout sessions, and a restrained dark navy palette inspired by athlete-grade equipment, LiftLog renders weights, reps, PRs, and volume with the clarity of a stadium scoreboard. The workout session view replaces the system numeric keypad with a custom haptic-feedback grid pad designed for thumbs between working sets; set completion plays a deliberate spring animation with a success haptic and a green confirmation sweep. Programs include Push / Pull / Legs, Bro Split, Upper / Lower, Starting Strength, and Full Body 3× — plus custom periodized templates with linear, DUP, block, or wave progression and automatic deload weeks. Progress tracking shows total workouts, total volume, total sets, and 30-day deltas vs. the prior period, alongside a GitHub-style 90-day activity heatmap. Per-exercise analytics include estimated 1RM trend lines, best set, best volume, and Rep PRs at 1, 3, and 5 reps. The exercise library browses by muscle group, equipment, or movement pattern, with X-ray-style anatomy renders and numbered HOW-TO steps connected by a vertical rail. Pricing is the unusual part: free for seven days with no card on file, no auto-renew, and no trial trap, after which the user picks a one-time tier — $9.99 (Fair), $19.99 (Good), $29.99 (Generous), or $39.99 (Patron). One purchase, no subscription, training history never held hostage. No third-party tracking, no advertising SDKs, no required account. Workout history stays on device with optional iCloud sync via your own Apple ID and optional Apple Health export. Sister app to GymLogger X — pick LiftLog for design-led iPhone polish and pay-what-you-can pricing; pick GymLogger X for Apple Watch first-class logging and a $44.99 lifetime price.
