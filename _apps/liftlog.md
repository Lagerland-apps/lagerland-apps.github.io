---
layout: app
slug: liftlog
name: "LiftLog"
tagline: "The lift log that feels like equipment."
quick_answer: "LiftLog is a design-led strength training log for iPhone built around tabular numerics, a custom haptic keypad for logging sets, and athlete-grade polish. It ships 40 ready programs (StrongLifts 5×5, Starting Strength, PPL, Upper/Lower, 5/3/1 and more) whose weights progress automatically, and tracks estimated 1RM, volume, and Rep PRs at 1/3/5/10 reps. Free 7-day trial, no card. Pay-what-you-can one-time from {P_IAP:Minimum} to {P_IAP:Patron}. No subscription, no tracking, no account."
category: fitness
status: live

app_store_url: "https://apps.apple.com/app/id6760043411"

price:
  model: one-time
price_override: "Free 7-day trial — then {P_IAP_MIN}–{P_IAP_MAX} (pay what you can, one-time)"
free_tier: false

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. All four tiers are one-time purchases — same app, no recurring fees, no auto-renew — and Family Sharing is on, so one purchase covers your household."
pricing_note: "Every price is on the App Store listing. There is no subscription to cancel: seven days free with no card, then one payment at the tier you choose."

plans:
  - name: "Free trial"
    price: "$0 / 7 days"
    summary: "Full access. No card. No auto-renew."
    features:
      - "All 40 programs and automatic progression"
      - "Tabular numerics + haptic keypad"
      - "1RM, Rep PRs, 26-week activity heatmap"
      - "Widgets, Siri, and Apple Health export"
  - name: "Fair"
    price: "{P_IAP:Minimum} once"
    summary: "Entry tier. The whole app, forever."
    features:
      - "Everything in the trial"
      - "Lifetime access — one purchase"
      - "All future feature updates"
      - "No subscription, no auto-renew"
  - name: "Good"
    price: "{P_IAP:Suggested} once"
    summary: "The honest middle. Same app, picked because the work is worth it."
    features:
      - "Everything in Fair"
      - "Supports continued development"
  - name: "Generous"
    highlight: true
    highlight_label: "Preselected in the app"
    price: "{P_IAP:Supporter} once"
    summary: "The tier the paywall preselects. In the app, it's the one marked as funding three months of development."
    features:
      - "Everything in Good"
      - "Funds new programs and analytics"
  - name: "Patron"
    price: "{P_IAP:Patron} once"
    summary: "Top tier. For fans backing a tiny indie studio."
    features:
      - "Everything in Generous"
      - "Same app — no hidden Patron-only features"
      - "Direct support email gets answered first"

icon: "/assets/icons/liftlog.png"
og_image: "/assets/og/liftlog.png"

seo:
  title: "Strength Training Log for iPhone — Pay Once | LiftLog"
  description: "Design-led strength log for iPhone: 40 programs that progress on their own, 1RM and PRs, haptic sets. 7 days free, no card — then pay what you can, once."
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
  subheadline: "Design-led strength tracker for iPhone — tabular numerics, a custom haptic keypad for every set, 40 ready programs (StrongLifts, PPL, Upper/Lower, 5/3/1) whose weights progress on their own, and PR moments rendered with the polish of a piece of equipment."
  pre_headline: "Open it. Log one workout. If LiftLog isn't worth {P_IAP:Minimum} to you, don't pay. Seven days free, no card on file, no auto-renew — then you decide what it's worth, once."
  cta_label: "Start 7-Day Free Trial — No Card"
  alt: "LiftLog workout session on iPhone — bench press set rows in large tabular numerics, two sets checked off, and last session's 100 kg × 5 shown above them"

who_for:
  - "You lift seriously and want a log that feels as deliberate as your training"
  - "You appreciate craft — typography, depth, motion — and notice when an app cuts corners"
  - "You want big, legible, tabular numerics during a working set, not body-copy text"
  - "You follow a structured program — StrongLifts, PPL, Upper/Lower, Full Body, 5/3/1, a hypertrophy split — and want next session's weights worked out for you"
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
  rule: "Estimated 1RM uses an Adaptive formula by default: Brzycki for 2–8 reps, a blend that shifts toward Epley — 1RM ≈ weight × (1 + reps / 30) — across 9–11 reps, and Epley at 12, so the trend line doesn't jump when your reps cross the hand-over. Brzycki or Epley alone can be picked in Settings. Personal bests are tracked per exercise: best estimated 1RM, heaviest set, and best session volume, plus Rep PRs — the heaviest weight you've lifted for at least 1, 3, 5, and 10 reps. The deload trigger is per exercise, not per week: when a lift falls short of its target sets and reps three sessions in a row, its next prescribed weight drops to 90%. Both numbers can be changed for each exercise (1–10 missed sessions, 50–100%)."
  what_it_does_not_do: "It does not invent rep ranges you didn't log or average across exercises. Warm-up sets are left out of PRs and estimates, and a single counts at its actual weight — the 1-rep column of Rep PRs shows your real heaviest single next to the estimate. There is no weekly volume ceiling or MRV calculation: deloads come from missed sessions on each lift, not from total volume."
  notes:
    - "Sets above 12 reps are left out of the 1RM estimate — both formulas lose accuracy that far out."
    - "RPE (1–10) is optional on any logged set. It feeds a per-exercise average-RPE chart and the RPE progression scheme; it does not change the 1RM estimate."
    - "Training Max (5/3/1) is a separate field per exercise — enter it yourself, or LiftLog starts it at 90% of your estimated 1RM (Jim Wendler's protocol uses 85–90% of a tested max). It drives program weights, not your PR history."
    - "Volume = reps × weight for each set. Bodyweight isn't added for chin-ups, dips, or pull-ups."

training_vocabulary:
  collapse_by_default: true
  intro: "LiftLog is built for lifters who already know what they're running. It speaks the language — double and linear progression, Training Max and AMRAP top sets (Wendler), and RPE-based autoregulation (Tuchscherer / Helms)."
  groups:
    - heading: "Programming"
      items:
        - "Progressive overload — applied automatically to every exercise with a progression rule, which the bundled programs set for you (switchable off in Settings)"
        - "Double progression, linear, percent of Training Max, or RPE autoregulation — chosen per exercise"
        - "5/3/1 with Training Max: the four-week 5s / 3s / 5-3-1 / deload wave, AMRAP top sets, Boring But Big and First Set Last templates"
        - "40 ready programs — StrongLifts 5×5, Starting Strength, GZCLP, Texas Method, Madcow, PHUL, PHAT, PPL, Upper/Lower, nSuns, Smolov — plus your own"
        - "Deload after a run of missed sessions — three by default, to 90%, editable per exercise"
    - heading: "Sets &amp; loading"
      items:
        - "Working sets, warm-up sets, AMRAP sets, and timed sets for holds"
        - "Supersets and giant sets — the rest timer starts after the last exercise of the round"
        - "RPE 1–10, optional on any logged set"
        - "Per-side plate breakdown on a standard 20 kg / 45 lb bar, down to 1.25 kg or 2.5 lb plates"
        - "Increment and rounding step per exercise, in 0.5 kg steps, for microloading"
    - heading: "Volume &amp; bodyweight"
      items:
        - "Working sets per muscle over the last 30 days, split into primary and secondary"
        - "Bodyweight and body measurements, with a 30-day trend"
        - "Relative strength — your best estimated 1RM as a multiple of bodyweight"
    - heading: "Analytics"
      items:
        - "Estimated 1RM (Adaptive Brzycki/Epley by default) — see method note above"
        - "Rep PRs at 1, 3, 5, and 10 reps — actual top sets, not just estimates"
        - "Best set and best session volume per exercise"
        - "Last 30 days vs. the prior 30 — workouts, volume, and sets"
        - "26-week activity heatmap"

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
        - "Pay-what-you-can {P_IAP:Minimum}–{P_IAP:Patron}, one-time"
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
    - feature: "Programs and weight progression"
      values:
        - "40 programs; per-exercise auto progression + deload after misses"
        - "Manual via routines"
        - "Manual via routines"
        - "AI auto-progression"
    - feature: "Estimated 1RM + Rep PRs"
      values:
        - "✓ Brzycki/Epley + actual 1/3/5/10"
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
  footnote: "Competitor details reflect publicly documented features as of 2026. LiftLog's pay-what-you-can pricing means you choose your tier — {P_IAP:Minimum} Fair, {P_IAP:Suggested} Good, {P_IAP:Supporter} Generous, {P_IAP:Patron} Patron — once. The App Store is the canonical source for current pricing."

value_points:
  - title: "Numbers are the product"
    description: "Weights, reps, PRs, and volume are rendered with tabular figures, calibrated tracking, and a stadium-scoreboard hierarchy. The set you're working on is the brightest thing on the screen — everything else recedes."
  - title: "Workout sessions designed for working sets"
    description: "A custom numeric keypad with haptic feedback. Set completion sweeps a green confirmation across the row. The rest timer counts down in a progress ring that stays pinned while you scroll. Built for thumbs holding a phone between sets — not a designer's portfolio shot."
  - title: "Pay what you can. Once."
    description: "Seven days free, no card required. Then choose what LiftLog is worth: {P_IAP:Minimum} Fair, {P_IAP:Suggested} Good, {P_IAP:Supporter} Generous, {P_IAP:Patron} Patron. One-time. No auto-renew. No trial trap. No subscription tax on your training history."
  - title: "PR moments that feel like moments"
    description: "When a set beats your best, LiftLog notices. A heavy haptic, a brief glow on the set, and a PR badge that stays on the row. Your best lifts deserve a celebration — not just a row."

features:
  - title: "Tabular numerics from end to end"
    description: "Every weight, rep, set, time, volume, and 1RM uses tabular figures — numbers that line up vertically across rows so trends are readable at a glance. No drift, no jitter, no wandering decimal points."
  - title: "Haptic-rich workout session view"
    description: "Custom numeric keypad replaces the system one — bigger keys, weight steps, a Log set key that starts your rest, and haptic feedback on every tap. Completing a set gives a haptic tap and a green sweep across the row. You feel the workout, not just see it."
  - title: "Programs that progress on their own"
    description: "Forty ready programs — StrongLifts 5×5, Starting Strength, GZCLP, Texas Method, Wendler 5/3/1, PHUL, Push / Pull / Legs, Upper / Lower and more — plus your own, with supersets and giant sets. Each exercise carries its own rule: double progression, linear, percent of Training Max, or RPE. When a workout ends, the recap shows next session's weight and reps for each of those lifts."
  - title: "Exercise library with anatomy-aware browsing"
    description: "1,500 exercises, each with an animated X-ray-style form demo, primary and secondary muscles, and a numbered How To with a connected vertical rail. Filter by muscle group or equipment, sort by most or recently used, or search in your language."
  - title: "Progress that earns its space"
    description: "All-time workouts, volume, and sets, plus the last 30 days against the prior 30. A 26-week activity heatmap shows your training rhythm at a glance. Per exercise: estimated 1RM trend, best set, best volume, and Rep PRs at 1, 3, 5, and 10 reps."
  - title: "Restraint is the design"
    description: "One accent color. One display typeface. One spacing scale. Every card uses the same elevation system. Every number uses the same numeric scale. The result: nothing competes for attention with the set you're about to lift."
  - title: "Privacy by default"
    description: "No third-party analytics. No advertising SDKs. No social feed. No required account. Workout history lives on your device — there is no cloud sync — and exports as JSON or CSV whenever you want it."
  - title: "Pay-what-you-can pricing — once"
    description: "Free for seven days, no card on file. After the trial, choose your tier: {P_IAP:Minimum} Fair, {P_IAP:Suggested} Good, {P_IAP:Supporter} Generous, {P_IAP:Patron} Patron. One-time payment. No auto-renew. No trial trap. You own it — and your training history isn't held hostage by a lapsed subscription."

screenshots:
  - src: "/assets/screenshots/liftlog/1.png"
    alt: "LiftLog paywall: free for 7 days, no card and no auto-renew"
  - src: "/assets/screenshots/liftlog/2.png"
    alt: "LiftLog exercise detail for the barbell bench press with how-to steps"
  - src: "/assets/screenshots/liftlog/3.png"
    alt: "LiftLog personal bests and rep PRs with an estimated 1RM chart"
  - src: "/assets/screenshots/liftlog/4.png"
    alt: "LiftLog active workout logging weight and reps for each set"
  - src: "/assets/screenshots/liftlog/5.png"
    alt: "LiftLog home screen with the next workout and recent sessions"
  - src: "/assets/screenshots/liftlog/6.png"
    alt: "LiftLog paywall with one-time pricing tiers"
  - src: "/assets/screenshots/liftlog/7.png"
    alt: "LiftLog privacy screen: workouts stay on your phone with no account"
  - src: "/assets/screenshots/liftlog/8.png"
    alt: "LiftLog three-day push pull legs program detail"
  - src: "/assets/screenshots/liftlog/9.png"
    alt: "LiftLog progress screen with monthly workouts, volume and an activity heatmap"
  - src: "/assets/screenshots/liftlog/10.png"
    alt: "LiftLog programs list with the active program"
  - src: "/assets/screenshots/liftlog/11.png"
    alt: "LiftLog set entry with a numeric keypad for weight and reps"
  - src: "/assets/screenshots/liftlog/12.png"
    alt: "LiftLog templates catalog with goal and frequency filters"
  - src: "/assets/screenshots/liftlog/13.png"
    alt: "LiftLog rest timer between sets"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no analytics SDKs, no social feed"
    - "No account required — open the app and start lifting"
    - "All workout data stays on your device — there is no cloud sync"
    - "Backups and CSV exports go only where you send them — Lagerland Apps never sees or stores your data"
    - "Optional Apple Health export for workouts and active energy"

faq:
  - q: "What is LiftLog?"
    a: "LiftLog is a design-led strength training log for iPhone. It's built around a tabular-numeric type system, haptic-rich workout sessions with a custom numeric keypad, 40 ready programs (StrongLifts 5×5, Starting Strength, PPL, Upper/Lower, 5/3/1, GZCLP and more) whose weights progress automatically, and per-exercise analytics — estimated 1RM, best set, best volume, Rep PRs at 1/3/5/10 reps, and a 26-week activity heatmap. Free seven-day trial, no card required, then a one-time pay-what-you-can purchase from {P_IAP:Minimum} to {P_IAP:Patron}."
  - q: "How is LiftLog different from GymLogger X?"
    a: "LiftLog and GymLogger X are sister apps from Lagerland Apps that approach strength training from different angles. GymLogger X is a fast, minimalist logger with an Apple Watch app for logging sets from the wrist (the Watch relays them to your iPhone) — free at the core, with Pro at $39.99 lifetime or $17.99 a year. LiftLog is design-led and iPhone-only: tabular numerics, haptic-rich sessions, restrained typography, and a pay-what-you-can one-time purchase from $9.99 to $39.99. Pick GymLogger X if you want to log from Apple Watch. Pick LiftLog if you care about the polish and craft of every screen — and like the idea of choosing your own price."
  - q: "How much does LiftLog cost?"
    a: "LiftLog is free for seven days — no card required and no auto-renew. After the trial, you choose what it's worth to you: {P_IAP:Minimum} (Fair), {P_IAP:Suggested} (Good), {P_IAP:Supporter} (Generous), or {P_IAP:Patron} (Patron). All four are one-time payments — no subscription, no recurring charge, no trial trap. Pick the tier that matches what the app is worth to you and you own it. Family Sharing is on, so one purchase covers your household."
  - q: "Why pay-what-you-can pricing?"
    a: "Strength training is a long-term practice. We don't think your training history should be held hostage by a lapsed subscription, and we don't want a credit card on file just to start. Seven days free without a card means you only pay if it earns your money. The four-tier ladder lets newer lifters in at {P_IAP:Minimum} while letting fans support the work at {P_IAP:Patron} — the same app, your call. The launch journal post explains the bet in more detail: https://lagerland-apps.github.io/journal/liftlog-pay-what-you-can/"
  - q: "Does LiftLog support Apple Watch?"
    a: "No — LiftLog is iPhone-only by design. The workout session view is built around a custom numeric keypad and haptic feedback that wouldn't translate to a small wrist screen. If you want to log from Apple Watch, GymLogger X is the better fit — it has an Apple Watch app for logging sets, which relays them to your iPhone."
  - q: "What programs does LiftLog support?"
    a: "LiftLog ships 40 ready programs: beginner templates (StrongLifts 5×5, Starting Strength, Greyskull LP, Reg Park 5×5, 5/3/1 for Beginners), strength programs (Wendler 5/3/1 Boring But Big, nSuns, GZCLP, Texas Method, Madcow 5×5, Bill Starr 5×5, Candito, Smolov, Westside), and hypertrophy splits (Push/Pull/Legs, Upper/Lower, PHUL, PHAT, German Volume Training, full-body and body-part splits) — plus any program you build yourself. Each exercise runs its own progression rule: double progression, linear, percent of Training Max (the 5/3/1 wave), or RPE. LiftLog does not schedule undulating, block, or conjugate periodization for you: in Texas Method, Madcow, and Westside the heavy day or main lift progresses automatically, and the light days and exercise rotation are set by hand."
  - q: "Does LiftLog track personal records?"
    a: "Yes. LiftLog tracks PRs per exercise — best estimated 1RM, heaviest set, best session volume, and Rep PRs at 1, 3, 5, and 10 reps. When a set beats your previous best mid-session, LiftLog marks it with a heavy haptic, a brief glow, and a PR badge on the row."
  - q: "Does LiftLog need an account or internet connection?"
    a: "No. LiftLog works fully offline with no account required. Workout data stays on your device. There is no cloud sync, so to move to a new phone you export a JSON backup and import it there. Lagerland Apps never sees or stores your data."
  - q: "Can I import workouts from Strong, Hevy, or another tracker?"
    a: "Not yet. LiftLog imports only its own JSON backup, which is how you move your history to a new phone. Export works at any time: your full history as a JSON backup or as a CSV file, from Settings."
  - q: "How does LiftLog estimate 1RM?"
    a: "By default LiftLog uses an Adaptive formula: Brzycki for sets of 2–8 reps, a blend that shifts toward Epley — 1RM ≈ weight × (1 + reps / 30) — across 9–11 reps, and Epley at 12. You can switch to Brzycki or Epley alone in Settings. A single counts at its actual weight, and sets above 12 reps are left out, because both formulas lose accuracy that far out. LiftLog also shows your actual heaviest sets for 1, 3, 5, and 10 reps, so you can compare the estimate with what you've really lifted."
  - q: "Does LiftLog support 5/3/1 and Training Max?"
    a: "Yes. In the Wendler 5/3/1 (Boring But Big) and 5/3/1 for Beginners programs, each main lift runs off a Training Max — enter your own, or LiftLog starts it at 90% of your estimated 1RM. The lift steps through the four-week wave (fives, threes, 5/3/1, then a 40/50/60% deload week) with an AMRAP top set, and beating the prescribed reps on that set raises the Training Max by 2.5 kg on upper-body lifts or 5 kg on lower-body lifts. The Boring But Big 5×10 and First Set Last back-off sets are taken off the same Training Max by hand. nSuns 531 LP runs off a Training Max too."
  - q: "Does LiftLog support RPE or RIR (Rep In Reserve)?"
    a: "RPE, yes — optionally. You can add an RPE (Rate of Perceived Exertion, 1–10) to any logged set from its workout in your history, and each exercise gets an average-RPE chart. Exercises set to the RPE progression scheme — used in Candito, GZCL Jacked & Tan, and Westside's max-effort lifts — move next session's weight up or down from the RPE of your last top set against a target, following the RPE-based autoregulation associated with Mike Tuchscherer and Eric Helms. There is no separate RIR field, and RPE does not change PR detection or the 1RM estimate."
  - q: "Is there a plate calculator?"
    a: "Yes. Open it from the active workout or from Settings, type a target weight or tap a common one, and it shows the plates for each side and draws the loaded bar. It assumes a standard 20 kg / 45 lb barbell and a standard plate set — 25 kg down to 1.25 kg, or 45 lb down to 2.5 lb — so it can't yet account for a different bar or for fractional plates."
  - q: "How fresh is LiftLog's content and pricing?"
    a: "This page is maintained alongside each App Store release. The last-updated and first-release dates are shown in the page footer. The pay-what-you-can tiers ({P_IAP:Minimum} / {P_IAP:Suggested} / {P_IAP:Supporter} / {P_IAP:Patron}) and the 7-day trial without a card are the live App Store configuration — if Apple's StoreKit ever shows different numbers, the App Store is canonical."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/liftlog/support/"

release:
  first_release: "2026-04-25"
  last_updated: "2026-10-23"

related_journal:
  slug: "liftlog-pay-what-you-can"
  anchor: "Why pay-what-you-can pricing — the bet, in our own words"

ratings:
  value: "5.0"
  count: 1
  last_synced: "2026-04-29"
last_updated: 2026-10-26
---
LiftLog is a design-led strength training log for iPhone. Built around a tabular-numeric type system, haptic-rich workout sessions, and a restrained navy palette in light and dark mode, LiftLog renders weights, reps, PRs, and volume with the clarity of a stadium scoreboard. The workout session view replaces the system numeric keypad with a custom haptic-feedback grid pad designed for thumbs between working sets; completing a set gives a haptic tap and a green sweep across the row, and a set that beats your best adds a heavy haptic, a brief glow, and a PR badge. LiftLog ships 40 ready programs — StrongLifts 5×5, Starting Strength, GZCLP, Texas Method, Wendler 5/3/1, PHUL, PHAT, Push / Pull / Legs, Upper / Lower and more — plus your own, with supersets and giant sets. Each exercise carries its own progression rule (double progression, linear, percent of Training Max, or RPE), and a lift that misses its targets three sessions in a row drops to 90%. Progress tracking shows total workouts, total volume, and total sets, the last 30 days against the prior 30, and a 26-week activity heatmap. Per-exercise analytics include estimated 1RM trend lines (Adaptive Brzycki/Epley by default), best set, best volume, and Rep PRs at 1, 3, 5, and 10 reps. The exercise library holds 1,500 exercises, each with an animated X-ray-style form demo and numbered How To steps, filterable by muscle group or equipment. Home Screen and Lock Screen widgets show your streak, week, and next session, and Siri can start a workout, log a set, or start your rest timer. Pricing is the unusual part: free for seven days with no card on file, no auto-renew, and no trial trap, after which the user picks a one-time tier — {P_IAP:Minimum} (Fair), {P_IAP:Suggested} (Good), {P_IAP:Supporter} (Generous), or {P_IAP:Patron} (Patron). One purchase, shared with your family through Family Sharing, no subscription, training history never held hostage. No third-party tracking, no advertising SDKs, no required account. Workout history stays on device — there is no cloud sync — with JSON and CSV export and optional Apple Health export. Sister app to GymLogger X — pick LiftLog for design-led iPhone polish and pay-what-you-can pricing; pick GymLogger X for logging from Apple Watch and a {P_IAP:Patron} lifetime price.
