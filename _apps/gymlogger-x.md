---
layout: app
slug: gymlogger-x
name: "GymLogger X"
tagline: "Log sets fast, follow a proven program, and spot a stalled lift early."
quick_answer: "GymLogger X is a strength training log for iPhone, with an Apple Watch app, for lifters who want fast set logging and a program to follow. Logging, the Apple Watch app, the Smart Program Creator, and 6 of its 44 ready-made programs are free, one program at a time. Pro adds all 44 programs, your full history, and Insights that flag plateaus, fatigue, and muscle imbalances from your own logs, for {P_MONTHLY}/month or {P_YEARLY}/year (each starts with a {TRIAL}) or {P_LIFETIME} once. There are no ads, and you never make an account."
category: fitness
status: live

app_store_url: "https://apps.apple.com/app/id6755734580"

price:
  model: freemium
price_tier: "Pro"

# Plans grid: Free / Pro Monthly / Pro Annual / Lifetime. The plans_footnote
# carries the USD-pricing disclaimer for international buyers and the App Store
# refund pointer, so purchase questions are answered next to the price.
plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew. Pro Monthly, Pro Annual, and Lifetime all support Family Sharing."

plans:
  - name: "Free"
    price: "$0"
    summary: "Log every workout, run one program, and keep the last 30 days of history."
    features:
      - "Unlimited workout logging on iPhone and Apple Watch"
      - "Supersets, giant sets, warm-up sets, and a plate calculator that knows your gym's plates"
      - "The Heart Rate Rest Timer, with an Apple Watch"
      - "1,500 exercises with search and filters, and a history and chart for each one"
      - "One program at a time: one of 6 free programs, your own, or one from the Smart Program Creator"
      - "Up to 3 workout templates and the last 30 days of history"
      - "Weekly Summary, Live Activities, the Start Workout control, and some small and Lock Screen widgets"
      - "Apple Health export and iCloud sync"
  - name: "Pro Monthly"
    price: "{P_MONTHLY} / mo"
    kind: monthly
    summary: "All of Pro, billed monthly. Starts with a {TRIAL}."
    features:
      - "All 44 programs, with as many active programs and templates as you want"
      - "Your full workout history and every personal record"
      - "Insights: Next Move, readiness, load ratio, muscle balance, and plateau status"
      - "Recovery and fatigue signals, Set Volume against MEV, MAV, and MRV, and the muscle heatmap"
      - "Animated exercise demos with instructions, and your own custom exercises"
      - "Import workouts and programs from CSV"
      - "Every widget size, full-page widgets on iOS 27, and 8 color themes"
      - "Cancel anytime"
  - name: "Pro Annual"
    price: "{P_YEARLY} / year"
    kind: yearly
    summary: "All of Pro, billed once a year. ~{SAVE_YEARLY}% cheaper than paying monthly. Starts with a {TRIAL}."
    features:
      - "Everything in Pro Monthly"
      - "~{SAVE_YEARLY}% cheaper than 12 months of Pro Monthly"
      - "Cancel anytime"
  - name: "Lifetime"
    price: "{P_LIFETIME} one-time"
    kind: lifetime
    summary: "All of Pro for one payment."
    features:
      - "Everything in Pro, unlocked for good"
      - "One-time purchase that never renews"
      - "Family Sharing"
    highlight_label: "Pay once"

icon: "/assets/icons/gymlogger-x.png"
og_image: "/assets/og/gymlogger-x.png"

seo:
  title: "Strength Training Log for iPhone & Apple Watch | GymLogger X"
  description: "Strength training log for iPhone and Apple Watch: 1,500 exercises, 44 programs, and plateau and fatigue signals from your own logs. Free, no account."
  keywords:
    - strength training log app
    - Apple Watch strength training app
    - workout log iPhone
    - gym tracker Apple Watch
    - Strong app alternative
    - Hevy alternative
    - Fitbod alternative
    - Caliber alternative
    - lifetime price workout tracker
    - strength training app no account
    - gym log app offline
    - PPL upper lower tracker
    - 5x5 program app
    - plateau detection workout app
    - progressive overload tracker
    - training program generator iPhone
    - plate calculator app
    - powerlifting log app
    - hypertrophy program app

hero:
  pre_headline: "Strength training log for iPhone and Apple Watch"
  headline: "Know what to lift today, and spot a stalled lift early."
  secondary: "1,500 exercises, 44 ready-made programs (6 of them free), and 40 languages. There are no ads, and you never make an account."
  subheadline: "Every set row shows what you lifted last time. The rest timer runs on your Lock Screen, and with an Apple Watch it can tell you when your heart rate has recovered. Pro reads your own logs and names the next move: rest, push, or work on a weak point."
  cta_label: "Download Free"
  alt: "GymLogger X workout on iPhone: an upper-body strength day with barbell bench press sets and last time's 225 lbs × 6 shown"

# Founder block: Experience / Authority signal (rendered above features when present).
# entity_type lets the layout pick the correct schema.org itemtype (Person vs Organization).
founder:
  overline: "Why we built this"
  heading: "We lift, and we built this for lifters."
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple studio · Finland"
  location: "Finland"
  photo: "/assets/icons/lagerland-mark.png"
  bio: "We wanted a log that keeps up at the rack, a program we could follow without building one, and a clear signal when a lift stops moving. GymLogger X does those three things from your own training history, with the analysis worked out on your iPhone. It shows no ads, asks for no account, and keeps your workouts on your devices and in your own iCloud. Lagerland Apps is a small independent Apple studio in Finland, with no investors or advertisers behind it."
  support_email: "support@lagerland.app"
  response_time: "Support emails are answered personally, usually within a day."
  signals:
    - "Workouts are stored on your device and synced through your own iCloud, and the app has no analytics SDKs"
    - "Lagerland's App Store catalogue is {APP_COUNT} privacy-first apps, all handling data the same way"
    - "Funded by people who buy the apps, with no ads or investors"
  external_link:
    href: "/lagerland-apps/"
    label: "Read the Lagerland studio backstory"

# Plateau and insight transparency: what the app measures and what it leaves to you.
plateau_disclosure:
  title: "How GymLogger X spots a stalled lift"
  rule: "Every logged set feeds an estimated 1RM for that exercise, using the Epley formula on sets of 3 or more reps. Strength Progress (Pro) charts that estimate over time, keeps a Rep-Max table of estimated against actual bests, and gives each lift an overload score and a status: Plateau, Watching, or Plateau Predicted. Insights then compares your recent training with your own history: readiness, weekly load ratio, recovery debt, Push/Pull, Upper/Lower, and Front/Back balance, and weekly hard sets per muscle against the MEV, MAV, and MRV volume landmarks. Warm-up sets and deload weeks stay out of the set counts."
  what_it_does_not_do: "Everything is worked out by fixed rules on your iPhone. There is no chat bot and no language model, and nothing is sent to a server. The Next Move card and up to three coaching suggestions tell you what your data shows, and any change to your program is yours to make. The app sends no notifications. Readiness, fatigue, and the conditioning score are training guidance, not medical advice."

# Method note: structured as HowToStep[] so the layout emits HowTo JSON-LD.
# The visible "how-it-works" include also renders these steps as a numbered list.
how_it_works:
  intro: "GymLogger X turns the sets you log into a plain next step. It follows three steps, all on your iPhone."
  steps:
    - title: "Log weight and reps"
      detail: "Each set row shows your previous weight and reps and the target. Mark a set as a warm-up and it still counts toward tonnage but stays out of weekly set volume. Sessions from a deload week are recognized as deloads, and you can mark any past session as one."
    - title: "Estimate 1RM and follow the trend"
      detail: "GymLogger X estimates your 1RM with the Epley formula from sets of 3 or more reps and charts it for every exercise. With Pro, Strength Progress shows the trend, a Rep-Max table, an overload score, and a plateau status for each lift."
    - title: "Read the next move"
      detail: "With Pro, the Next Move card on the Progress tab says whether to rest, deal with a plateau, work on a weak point, or train as planned. Once you have enough history, up to three plain-language suggestions explain why. You decide what changes in your program."

who_for:
  - "You already lift and want a set logger that keeps up with weights, reps, supersets, and plates"
  - "You'd rather follow a proven program (5×5, push/pull/legs, upper/lower, full body, conjugate) than design one"
  - "You want estimated 1RM trends, PRs, volume per muscle, and plateau and fatigue signals from your own history"
  - "You wear an Apple Watch and want heart rate and calories attached to your lifting sessions"
  - "You're moving from a spreadsheet or another app and want to bring your history with you (CSV import, Pro)"
  - "You're a coach whose clients would rather follow your spreadsheet program in an app (Import Program, Pro)"

who_not_for:
  - "You mostly do cardio or group fitness classes"
  - "You want an AI chat coach or follow-along video workouts"
  - "You want to train with only your Apple Watch: every workout starts on the iPhone"
  - "You use Android, or want your log on iPad or Mac (GymLogger X runs on iPhone, with an Apple Watch app)"
  - "You want workout reminders: the app sends no notifications"

alternatives_to:
  - "Strong"
  - "Hevy"
  - "Fitbod"
  - "Jefit"
  - "Caliber"
  - "Heavyset"
  - "StrongLifts 5x5"
  - "Alpha Progression"

# Comparison table, competitor facts checked against each app's public sources (footnote).
# No typed prices: pricing models are described in words.
comparison_table:
  intro: "Strong, Hevy, and Fitbod are popular, capable apps. These are the practical differences when you choose where to keep years of training history."
  competitors: ["GymLogger X", "Strong", "Hevy", "Fitbod"]
  rows:
    - feature: "Pricing model"
      values: ["Free, with Pro monthly, yearly, or lifetime", "Free, with Pro subscription or lifetime", "Free, with Pro subscription or lifetime", "Subscription only"]
    - feature: "Use the app with no account or sign-up"
      values: ["Yes, nothing to sign up for", "Account required", "Account required", "Account required"]
    - feature: "Apple Watch: log a full session without the iPhone"
      values: ["No. You log sets on the wrist; the iPhone starts the session", "Yes, standalone", "Live-syncs with the iPhone", "No. The watch must connect to the iPhone"]
    - feature: "CSV export of every set"
      values: ["No. Workouts go to Apple Health", "Pro tier only", "Yes", "Limited"]
  footnote: "Competitor details checked on 2026-05-13 against each app's App Store page, website, and help pages (strongapp.io, hevyapp.com, fitbod.me). They change often, so check again before you switch. The App Store shows current prices."

value_points:
  - title: "Last time's numbers, already in the row"
    description: "Before you type anything, every set row shows your previous weight and reps and the target. Supersets and giant sets log like straight sets. The plate calculator works out each side of the bar from the plates your gym actually has, and the rest timer sits on your Lock Screen and in the Dynamic Island."
  - title: "44 programs, or one built around you"
    description: "Six programs are free, including Linear 5×5 Foundation and The Golden Six. Pro adds 38 more, from push/pull/legs and the Texas Method to the Conjugate Method and a 6-week peaking block. The Smart Program Creator builds a plan around your equipment, schedule, goals, and injuries. Start a Pro program while subscribed and you can finish it even if the subscription ends."
  - title: "Signals from your own logs"
    description: "With Pro, the Next Move card tells you to rest, deal with a plateau, work on a weak point, or train as planned. Behind it are your readiness, weekly load ratio, recovery debt, muscle balance, and plateau status for each lift, all worked out on your iPhone with no chat bot involved."
  - title: "Your wrist and your Home Screen"
    description: "The free Apple Watch app logs sets and shows live heart rate, calories, and rest. Its Heart Rate Rest Timer can tell you when your heart rate has recovered. Twelve widgets, two Live Activities, and a Start Workout control (iOS 18 or later) keep today's plan in view; on iOS 27, six widgets can fill a whole Home Screen page with Pro."

features:
  - title: "Fast set logging"
    description: "Start an empty workout or a saved template in two taps. Log weight and reps in kg or lbs, mark warm-up sets, add sets, swap an exercise for a program variant, and pick up where you left off if you leave mid-workout. The Workout Complete screen shows volume, your top lift, new records, and the muscles you trained."
  - title: "Training Programs"
    description: "44 ready-made programs, 1 to 8 weeks long, with filters for goal, level, days, and equipment. Six are free: Whole Body Program, The Golden Six, 2-, 3-, and 4-Day Split Routines, and Linear 5×5 Foundation. Pro adds 38, including push/pull/legs, German Volume Training, the Texas Method, Powerbuilding 5-Day, and Hybrid Strength (Lift + Run). Preview any program, or customize a copy."
  - title: "Smart Program Creator"
    description: "A step-by-step wizard asks about your equipment, goals, injuries, schedule, and preferences, then builds a program: full body, upper/lower, push/pull/legs, push/pull, Arnold, or bro split, for 4, 8, or 12 weeks or ongoing, with linear, undulating, block, or wave periodization. The preview shows deload weeks, a prehab warm-up, and injury accommodations, and you can swap exercises or regenerate. Free users keep one program at a time; Pro removes the limit."
  - title: "Insights and plateau signals (Pro)"
    description: "Estimated 1RM charts with a plateau status for each lift, readiness and fatigue signals, weekly load ratio, Push/Pull, Upper/Lower, and Front/Back balance, weekly sets per muscle against MEV, MAV, and MRV, a muscle heatmap over 7, 14, or 28 days, and every personal record in one list. Program reports end with adherence and a rule-based Coach Verdict."
  - title: "Apple Watch app"
    description: "Start the workout on your iPhone, then log sets on the wrist with weight and rep steppers, watch live heart rate, time, and calories, and run the rest ring with 15-second adjustments. Finished workouts are saved to Apple Health as strength training. The Watch app is free."
  - title: "Widgets and Live Activities"
    description: "Twelve widgets for the Home Screen and Lock Screen, including Training Grid (a year of training, one square per day), Muscle Map, Today, Lift Ladder, and Record. Two Live Activities show the running workout and the rest countdown on the Lock Screen and in the Dynamic Island. Some small and Lock Screen sizes are free; the rest need Pro."

screenshots:
  - src: "/assets/screenshots/gymlogger-x/1.webp"
    alt: "GymLogger X workout on iPhone: barbell bench press sets with last time's 225 lbs × 6 shown beside the set rows"
  - src: "/assets/screenshots/gymlogger-x/2.webp"
    alt: "GymLogger X Progress Insights with a Next Move suggestion, a readiness score, and an estimated 1RM chart"
  - src: "/assets/screenshots/gymlogger-x/3.webp"
    alt: "GymLogger X Progress Overview with training load and a suggestion that there is room to push"
  - src: "/assets/screenshots/gymlogger-x/4.webp"
    alt: "GymLogger X Training Programs catalog with filters and programs such as Linear 5×5 Foundation and Upper/Lower"
  - src: "/assets/screenshots/gymlogger-x/5.webp"
    alt: "GymLogger X muscle heatmap showing overloaded quadriceps and undertrained glutes and chest"
  - src: "/assets/screenshots/gymlogger-x/6.webp"
    alt: "GymLogger X Home Screen widgets with a bench press record, a muscle map, and a year of sessions on a training grid"
  - src: "/assets/screenshots/gymlogger-x/7.webp"
    alt: "GymLogger X on Apple Watch showing heart rate and calories during barbell bench press, next to the workout on iPhone"
  - src: "/assets/screenshots/gymlogger-x/8.webp"
    alt: "GymLogger X feature tiles: no ads, no account, Apple Watch, Apple Health, iCloud sync, plate calculator, and Lock Screen widgets"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, and no third-party analytics or advertising SDKs"
    - "No account: there is nothing to sign up for"
    - "Workouts are stored on your iPhone and synced through your own private iCloud when you're signed in to iCloud"
    - "The app has no server of its own and sends your workouts nowhere else"
    - "Apple Health: finished workouts are saved as strength training, and heart rate and active energy are read for your insights"

coach_cta:
  title: "For Coaches"
  description: "Share your program as a spreadsheet (week, day, exercise, sets, and reps). Clients import it once with Pro and follow it day by day."
  cta_label: "See how coaches use it"
  url: "/apps/gymlogger-x/coaches/"

faq:
  - q: "What is GymLogger X?"
    a: "GymLogger X is a strength training log for iPhone, with an Apple Watch app. You log sets with last time's numbers already in the row, follow one of 44 ready-made programs or one the Smart Program Creator builds for you, and, with Pro, get plateau, fatigue, and muscle-balance signals from your own logs. It has 1,500 exercises (animated demos with Pro) and runs in 40 languages. The core is free; Pro is {P_MONTHLY}/month or {P_YEARLY}/year, each starting with a {TRIAL}, or {P_LIFETIME} once."
  - q: "How is GymLogger X different from Strong, Hevy, and Fitbod?"
    a: "GymLogger X needs no account; when we checked on 2026-05-13, Strong, Hevy, and Fitbod all asked you to sign up. Its Apple Watch app is free and has a rest timer that can tell you when your heart rate has recovered. Pro comes as a subscription or a one-time lifetime purchase. And its coaching is rule-based and worked out on your iPhone from your own logs, with no chat bot. The comparison pages go into detail: <a href=\"/alternatives/strong-workout-app/\">Strong</a> and <a href=\"/alternatives/fitbod/\">Fitbod</a>."
  - q: "What is the Smart Program Creator?"
    a: "It is a wizard that builds a program from your equipment, goals, injuries, schedule, and preferences. You pick a split (full body, upper/lower, push/pull/legs, push/pull, Arnold, or bro split), days per week, session length, a length of 4, 8, or 12 weeks or ongoing, and linear, undulating, block, or wave periodization. Injuries are entered by body part, with movements to avoid. The preview shows deload weeks, a prehab warm-up, and injury accommodations, and you can swap an exercise or regenerate before you start. It is free to use; free users keep one program at a time."
  - q: "Does GymLogger X support RPE and RIR?"
    a: "Not when you log. A logged set records weight and reps, plus whether it was a warm-up; there is no per-set RPE or RIR entry, and the analytics, plateau status included, work from weight and reps. <a href=\"/journal/rpe-and-rir-explained/\">RPE and RIR, explained</a> covers what that means if you rate every set."
  - q: "Does GymLogger X calculate Wilks, DOTS, or Sinclair?"
    a: "No. GymLogger X doesn't calculate Wilks, DOTS, or Sinclair scores. It estimates 1RM for every lift with the Epley formula, keeps a Rep-Max table and your personal records, and has a plate calculator for loading the bar."
  - q: "Does GymLogger X work on Apple Watch without the iPhone?"
    a: "No. The Apple Watch app is a companion: you start the workout on your iPhone, and sets you log on the watch go through the phone. On the wrist you log weight and reps, see heart rate, time, and calories, and run the rest timer. Heart rate and calories need Health permission on the watch."
  - q: "How does plateau detection work?"
    a: "GymLogger X estimates your 1RM for each exercise with the Epley formula, from sets of 3 or more reps, and follows the trend across your sessions. With Pro, Strength Progress gives each lift a status (Plateau, Watching, or Plateau Predicted) and an overload score, and the Next Move card turns that into a suggestion such as a rest day or a change of approach. It all runs on your iPhone by fixed rules. It doesn't change your program or send notifications; you decide what to do."
  - q: "Is GymLogger X free? What does Pro unlock?"
    a: "Logging is free for good: unlimited workouts on iPhone and Apple Watch, the Heart Rate Rest Timer, 1,500 exercises, one program at a time (6 free programs, your own, or one from the Smart Program Creator), 3 templates, the last 30 days of history, Apple Health export, and iCloud sync. Pro unlocks all 44 programs, unlimited programs and templates, your full history, Insights, recovery and plateau signals, the muscle heatmap, animated demos, custom exercises, CSV import, every widget, and 8 color themes. Pro is {P_MONTHLY}/month or {P_YEARLY}/year, each starting with a {TRIAL}, or {P_LIFETIME} once, and it supports Family Sharing. Prices are in USD; the App Store shows your local currency at checkout."
  - q: "What happens to my program if my Pro subscription ends?"
    a: "If you started a Pro program while subscribed, you can finish it after the subscription ends. Free limits apply to everything else: one active program, 3 templates, and the last 30 days of history, with older sessions kept and unlocked again when you upgrade."
  - q: "Does GymLogger X need an account or internet connection?"
    a: "No. There is no account and no sign-up, and logging works fully offline, exercise demos included. Workouts are stored on your iPhone and synced through your own private iCloud when you're signed in to iCloud, and finished workouts are saved to Apple Health. The app has no server of its own, so your workouts are never sent to us."
  - q: "Can I export my data if I leave?"
    a: "There is no file export. Each finished workout is saved to Apple Health as a strength training session, any workout can be shared as text, and the recap and Weekly Summary can be shared as images. Coming from another app or a spreadsheet? Pro imports workouts from CSV, TSV, or TXT files, with a column-mapping step."
  - q: "What if my exercise isn't in the 1,500-exercise library?"
    a: "Create it with Pro. A custom exercise takes a name, equipment, and muscle groups, and you log it like any built-in one. Pro also lets you edit the name, equipment, and muscles of built-in exercises, and reset them to the default."

support:
  email: "support@lagerland.app"
  url: "/apps/gymlogger-x/support/"

release:
  first_release: "2025-12-03"
  last_updated: "2026-10-16"

related_journal:
  slug: "choosing-a-strength-program-you-will-finish"
  anchor: "PPL, Upper/Lower, or 5/3/1: choosing a program you will actually finish"

ratings:
  value: "4.8"
  count: 17
  last_synced: "2026-06-22"
last_updated: 2026-10-30
---
GymLogger X is a strength training log for iPhone, with an Apple Watch app. Every set row shows what you lifted last time, supersets and giant sets log like straight sets, and the plate calculator loads the bar from the plates your gym has. You can follow one of 44 ready-made programs (6 free, 38 with Pro) or let the Smart Program Creator build one around your equipment, schedule, goals, and injuries. With Pro, Insights reads your own history and shows readiness, fatigue, weekly load ratio, muscle balance, and a plateau status for each lift, worked out by fixed rules on your iPhone. On Apple Watch you log sets, see live heart rate, and can let the rest timer tell you when your heart rate has recovered; the workout starts on the iPhone. The app has 1,500 exercises, 12 widgets, and two Live Activities, and runs in 40 languages. There are no ads and no account, and workouts sync through your own iCloud. The core is free; Pro costs {P_MONTHLY}/month or {P_YEARLY}/year, each starting with a {TRIAL}, or {P_LIFETIME} once.
