---
layout: app
slug: liftlog
name: "LiftLog"
tagline: "The gym log you pay for once and keep."
quick_answer: "LiftLog is a gym workout tracker for iPhone that you pay for once: 7 days free with no card, then a one-time purchase from {P_IAP:Minimum} to {P_IAP:Patron}, with no subscription and Family Sharing on. It fills in each set from your last session, starts the rest timer for you, and flags a personal best the moment you set it. It comes with 1,500 exercises with animated demos, 40 ready-made programs that can suggest your next weight, and 10 Home Screen and Lock Screen widgets. Your workouts stay on your iPhone, and there is no account and no analytics."
category: fitness
status: live

app_store_url: "https://apps.apple.com/app/id6760043411"

price:
  model: one-time
price_override: "Free 7-day trial, then {P_IAP_MIN} to {P_IAP_MAX} once (you choose the tier)"
free_tier: false

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple handles refunds through the standard App Store refund flow. All four tiers are one-time purchases of the same app, nothing renews, and Family Sharing is on, so one purchase covers your family group."
pricing_note: "There is no subscription to cancel. You get 7 days free with no card, then you make one payment at the tier you choose."

plans:
  - name: "Free trial"
    price: "$0 / 7 days"
    summary: "The whole app for a week, with no card on file."
    features:
      - "Logging, programs, and smart weight suggestions"
      - "All 1,500 exercises and the 40-program catalog"
      - "Widgets, Siri, and Apple Health export"
      - "Your history stays readable and exportable if you don't buy"
  - name: "Fair"
    price: "{P_IAP:Minimum} once"
    summary: "The entry tier. The full app, paid for once."
    features:
      - "Everything in the trial, for good"
      - "Future updates included"
      - "Family Sharing"
      - "No subscription and no renewal"
  - name: "Good"
    price: "{P_IAP:Suggested} once"
    summary: "The same app at a higher price, for people who want to give more."
    features:
      - "Everything in Fair"
      - "The extra helps fund development"
  - name: "Generous"
    highlight: true
    highlight_label: "Our pick"
    price: "{P_IAP:Supporter} once"
    summary: "The same app again. A bigger share goes into building it."
    features:
      - "Everything in Good"
      - "The extra helps fund development"
  - name: "Patron"
    price: "{P_IAP:Patron} once"
    summary: "The top tier, for lifters who want to back the work."
    features:
      - "Everything in Generous"
      - "Same app; there are no Patron-only features"

icon: "/assets/icons/liftlog.png"
og_image: "/assets/og/liftlog.png"

seo:
  title: "Gym Workout Tracker for iPhone, No Subscription | LiftLog"
  description: "Gym workout tracker for iPhone: 1,500 animated exercises, 40 programs, auto rest timer and PR alerts. Free for 7 days, then pay once. No subscription."
  keywords:
    - gym workout tracker iphone
    - workout app no subscription
    - strength training log
    - one time purchase workout app
    - lifting log app
    - offline workout tracker
    - progressive overload app
    - pr tracker iphone

hero:
  pre_headline: "For lifters who want a fast log and no monthly bill"
  headline: "The gym log you pay for once and keep."
  secondary: "When you reach the bar, your last weight and reps are already in the row."
  subheadline: "Tap a check mark to log the set and the rest timer starts on its own. Run one of 40 ready-made programs that suggest your next weight, or build your own. Try everything free for 7 days with no card, then pay once."
  cta_label: "Try 7 Days Free, No Card"
  alt: "LiftLog workout session on iPhone: bench press set rows, two sets checked off, and last session's 100 kg × 5 shown above them"

who_for:
  - "You lift weights (strength, bodybuilding, or powerlifting-style training) and want to log a set without fighting the phone"
  - "You want a ready-made routine and would rather load a program than type one in"
  - "You're done with monthly fees and accounts, and want to pay once for an app that keeps working offline"
  - "You want your streak, your week, and your next session on the Home Screen, the Lock Screen, or from Siri"
  - "You'd like exercise names and how-to steps in your own language"

who_not_for:
  - "You want to log sets on Apple Watch, or want automatic rep counting or heart rate"
  - "You need your log on iPad or Mac, or synced between devices"
  - "You want a social feed, friends, or an AI coach that writes your workouts"
  - "You want to use the app indefinitely without paying: after the 7-day trial, logging new workouts needs the one-time purchase"

alternatives_to:
  - "Strong"
  - "Hevy"
  - "Caliber"
  - "Ladder"
  - "Heavyset"

plateau_disclosure:
  title: "How LiftLog spots a personal best and suggests your next weight"
  rule: "A personal best is measured against your estimated 1RM history for that exercise. You pick the formula in Settings: Adaptive (recommended), Brzycki, or Epley. Each exercise page keeps your Personal Bests (Est. 1RM, Best Set, and Best Volume) and your Rep PRs. When a program exercise has a progression scheme (Double progression, Linear, % of training max, or RPE / RIR), LiftLog fills each pending set with the weight the program prescribes. After the workout, a Progression review marks each of those exercises as Progressed, Hold, Missed, or Deload."
  what_it_does_not_do: "Warm-up sets never count toward personal bests and don't start the rest timer. RPE is added by editing a set after the workout, not on the live set row, so the RPE scheme only works when you enter it. LiftLog doesn't count reps, read heart rate, or give medical advice."
  notes:
    - "Smart weight suggestions are on by default. One switch in Settings turns them off."
    - "The Estimated 1RM, Volume, and Avg RPE charts on each exercise appear once you have two sessions."
    - "Relative strength shows a lift as a multiple of your bodyweight, once you've logged a bodyweight entry."
    - "Calorie figures sent to Apple Health are estimates."

training_vocabulary:
  collapse_by_default: true
  intro: "LiftLog uses the terms programmed training already uses: double and linear progression, training max, RPE, supersets, and deloads."
  groups:
    - heading: "Programming"
      items:
        - "Progression per exercise: Double progression, Linear, % of training max, or RPE / RIR"
        - "40 ready-made programs: 20 for strength, 17 for hypertrophy, and 3 general, from 10 beginner to 8 advanced"
        - "Filter the catalog by goal, days per week, and equipment"
        - "One Active Program at a time, so the next workout is always known"
        - "A post-workout Progression review: Progressed, Hold, Missed, or Deload"
    - heading: "Sets &amp; loading"
      items:
        - "Working sets, warm-up sets, timed warm-ups, and timed sets for planks and holds"
        - "Supersets (two exercises) and giant sets (three or more), with focus moving to the next exercise"
        - "Rest per exercise: presets from 30 seconds to 5 minutes, or fine-tuned from 10 to 600 seconds"
        - "Plate Calculator: the plates for each side of the bar, with “Bar only” and “Not exact” notes"
        - "RPE from 1 to 10, optional, added when you edit a logged set"
    - heading: "Body &amp; balance"
      items:
        - "Bodyweight plus waist, chest, arms, thighs, hips, and neck"
        - "Relative strength: a lift as a multiple of bodyweight"
        - "Muscle Coverage: set counts for your top 8 muscles over 30 days"
        - "Library filters across 23 muscle groups and by equipment"
    - heading: "Analytics"
      items:
        - "Estimated 1RM with Adaptive, Brzycki, or Epley"
        - "Personal Bests and Rep PRs for every exercise"
        - "Last 30 days against the 30 before"
        - "Activity heatmap and Workout Duration over 3 months"
        - "Sessions per exercise over the last 90 days"

comparison_table:
  intro: "LiftLog against the most-searched iPhone strength trackers on pricing model, what you give up to use each one, and whether your training history stays yours."
  competitors:
    - "LiftLog"
    - "Strong"
    - "Hevy"
    - "Fitbod"
  rows:
    - feature: "Pricing model"
      values:
        - "One-time purchase, {P_IAP:Minimum} to {P_IAP:Patron}"
        - "Free + Pro subscription"
        - "Free + Pro subscription"
        - "Subscription only"
    - feature: "Free trial with no card required"
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
        - "40 programs; suggested weights per exercise"
        - "Manual via routines"
        - "Manual via routines"
        - "AI auto-progression"
    - feature: "Estimated 1RM + Rep PRs"
      values:
        - "✓ Adaptive, Brzycki, or Epley"
        - "✓ Pro"
        - "✓"
        - "✓"
    - feature: "Apple Watch logging"
      values:
        - "No"
        - "Yes"
        - "Yes"
        - "Yes"
    - feature: "Social feed / leaderboards"
      values:
        - "None"
        - "Limited"
        - "Yes (core feature)"
        - "Limited"
    - feature: "Training history after you stop paying"
      values:
        - "Readable and exportable, even if you never buy"
        - "Read-only without Pro"
        - "Read-only without Pro"
        - "Lost when sub lapses"
  footnote: "Competitor details reflect publicly documented features as of 2026. With LiftLog you choose your tier once: {P_IAP:Minimum} Fair, {P_IAP:Suggested} Good, {P_IAP:Supporter} Generous, or {P_IAP:Patron} Patron. The App Store is the canonical source for current pricing."

value_points:
  - title: "Pay once. Keep it."
    description: "Use everything free for 7 days with no card on file. Then buy LiftLog once at the tier you choose, from {P_IAP:Minimum} to {P_IAP:Patron}. Every tier unlocks the same app, nothing renews, and Family Sharing covers your family group. If you never buy, your history, charts, and exports stay open to you."
  - title: "Made for the minute between sets"
    description: "Weight and reps go in on a docked keypad that never covers the set you're on. Each row shows what you lifted last time, and the next set is already filled in from your last working set. Check it off and the rest timer starts."
  - title: "Programs that tell you what to lift"
    description: "Load one of 40 ready-made programs with sets, reps, and rest already in place, or build your own. With a progression scheme on an exercise, LiftLog fills in the weight the program calls for next."
  - title: "Your training stays on your iPhone"
    description: "There is no account to create. LiftLog carries no analytics, ads, or third-party SDKs, and it works fully offline. Export everything as JSON or CSV whenever you want."

features:
  - title: "Set logging that starts where you left off"
    description: "Start from an empty session, one of your three most recent workouts, a program day, or the Repeat Last button on Home. Each set row shows last session's numbers, such as 80×8, and a check mark commits the set. Warm-up sets and timed sets for planks and holds are built in."
  - title: "A rest timer that runs itself"
    description: "Logging a working set starts the rest timer. Add or take off 15 seconds, or skip it. It keeps running in the background, ends with a sound and a haptic, and can send a “Rest complete” notification if you've left the app. Each exercise can have its own rest, from 30 seconds to 5 minutes."
  - title: "40 ready-made programs, plus your own"
    description: "Browse Templates holds 40 programs based on well-known routines such as StrongLifts 5×5, Starting Strength, and 5/3/1, filterable by goal, days per week, and equipment. Use This Program copies one into your list with sets, reps, and rest set up. Build your own with supersets, giant sets, and timed sets, and pick one Active Program so the next workout is always ready."
  - title: "Smart weight suggestions"
    description: "Give a program exercise a progression scheme (Double progression, Linear, % of training max, or RPE / RIR) and each set arrives with the weight to lift. After the workout, the Progression review shows which lifts progressed, held, missed, or need a deload."
  - title: "Personal bests the moment they happen"
    description: "When a set beats your estimated 1RM history, a PR badge shows the improvement, the row glows, and your phone gives a success haptic. Workout Complete then lists duration, sets, volume, and new personal bests, and Save image turns it into a card you can share."
  - title: "1,500 exercises with animated demos"
    description: "Every exercise has a looping animation, How To steps, and the muscles it works. Search, or filter by equipment and 23 muscle groups. Exercise names and instructions come in 23 languages, set separately from the app language. If a lift is missing, you can create it straight from your search."
  - title: "Progress you can read at a glance"
    description: "The Progress tab shows this month, the last 30 days against the 30 before, an activity heatmap, Muscle Coverage, and workout duration. Each exercise has Estimated 1RM, Volume, and Avg RPE charts you can scrub with a finger. Log bodyweight and six body measurements to see your lifts relative to your weight."
  - title: "Widgets and Siri"
    description: "Ten widgets for the Home Screen and Lock Screen show your streak, your week, your training grid, and what's next. Tap Start on Next Session to begin the planned workout. Siri and Shortcuts can start your next workout, start a saved workout by name, log a set, start the rest timer, or tell you your streak and this week's volume."
  - title: "Offline, private, and portable"
    description: "Workouts, programs, and notes live on your iPhone. Export as JSON or CSV, restore from a backup, and recover a deleted workout for 30 days from Recently Deleted. You can send finished workouts to Apple Health if you turn it on; LiftLog never reads your health data."

screenshots:
  - src: "/assets/screenshots/liftlog/1.webp"
    alt: "LiftLog paywall: free for 7 days, no card and no auto-renew"
  - src: "/assets/screenshots/liftlog/2.webp"
    alt: "LiftLog exercise detail for the barbell bench press with how-to steps"
  - src: "/assets/screenshots/liftlog/3.webp"
    alt: "LiftLog personal bests and rep PRs with an estimated 1RM chart"
  - src: "/assets/screenshots/liftlog/4.webp"
    alt: "LiftLog active workout logging weight and reps for each set"
  - src: "/assets/screenshots/liftlog/5.webp"
    alt: "LiftLog home screen with the next workout and recent sessions"
  - src: "/assets/screenshots/liftlog/6.webp"
    alt: "LiftLog paywall with one-time pricing tiers"
  - src: "/assets/screenshots/liftlog/7.webp"
    alt: "LiftLog privacy screen: workouts stay on your phone with no account"
  - src: "/assets/screenshots/liftlog/8.webp"
    alt: "LiftLog three-day push pull legs program detail"
  - src: "/assets/screenshots/liftlog/9.webp"
    alt: "LiftLog progress screen with monthly workouts, volume and an activity heatmap"
  - src: "/assets/screenshots/liftlog/10.webp"
    alt: "LiftLog programs list with the active program"
  - src: "/assets/screenshots/liftlog/11.webp"
    alt: "LiftLog set entry with a numeric keypad for weight and reps"
  - src: "/assets/screenshots/liftlog/12.webp"
    alt: "LiftLog templates catalog with goal and frequency filters"
  - src: "/assets/screenshots/liftlog/13.webp"
    alt: "LiftLog rest timer between sets"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "Carries no ads, analytics, or third-party SDKs"
    - "No account: open the app and start lifting"
    - "Workouts stay on your iPhone and every feature works offline; there is no cloud sync"
    - "Exports and backups go only where you send them. Lagerland Apps never receives your data"
    - "Apple Health is optional and write-only: finished workouts and estimated active energy"

faq:
  - q: "What is LiftLog?"
    a: "LiftLog is a gym workout tracker for iPhone. You log weight and reps on a docked keypad, each set is filled in from your last session, and the rest timer starts when you check a set off. It includes 1,500 exercises with animated demos, 40 ready-made programs that can suggest your next weight, personal best alerts, progress charts, 10 widgets, and Siri actions. It is free for 7 days with no card, then a one-time purchase from {P_IAP:Minimum} to {P_IAP:Patron}."
  - q: "How much does LiftLog cost, and is there a subscription?"
    a: "There is no subscription. LiftLog is free for 7 days with no card required. After that you buy it once at the tier you choose: {P_IAP:Minimum} (Fair), {P_IAP:Suggested} (Good), {P_IAP:Supporter} (Generous), or {P_IAP:Patron} (Patron). Every tier unlocks the same app, nothing renews, future updates are included, and Family Sharing is on, so one purchase covers your family group."
  - q: "What happens when the 7-day trial ends?"
    a: "If you don't buy, you keep read access. Your history, workout details, Progress charts, the exercise library, the Plate Calculator, widgets, Siri read-outs, data export and import, and Recently Deleted all stay free, and a workout already in progress can be finished. Starting new workouts, editing programs, creating custom exercises, editing logged sets, and logging bodyweight need the one-time purchase."
  - q: "Why are there four prices for the same app?"
    a: "LiftLog lets you pay what feels fair. All four tiers unlock exactly the same app; the higher amounts help fund its development. <a href=\"/journal/liftlog-pay-what-you-can/\">The launch journal post</a> explains the thinking."
  - q: "How is LiftLog different from GymLogger X?"
    a: "Both are strength trackers from Lagerland Apps. LiftLog runs on iPhone only and is a one-time purchase after a 7-day trial, with 40 ready-made programs, smart weight suggestions, and 10 widgets. GymLogger X is a separate app with its own Apple Watch app. Pick GymLogger X if you want to log sets from your wrist; its page lists its features and prices."
  - q: "Does LiftLog work with Apple Watch?"
    a: "No. LiftLog runs on iPhone only and has no Apple Watch app. It can save finished workouts to Apple Health so they count toward your Activity rings, if you turn that on."
  - q: "What programs does LiftLog include?"
    a: "Browse Templates holds 40 programs based on well-known routines such as StrongLifts 5×5, Starting Strength, Greyskull LP, Wendler 5/3/1, Texas Method, GZCLP, nSuns 531 LP, PHUL, PHAT, and German Volume Training. Twenty focus on strength, 17 on hypertrophy, and 3 are general; 10 are for beginners, 22 intermediate, and 8 advanced. Each loads with sets, reps, and rest in place, and you can build your own. The program names belong to their owners, who don't endorse LiftLog."
  - q: "Can LiftLog suggest the weight for my next session?"
    a: "Yes. Give a program exercise a progression scheme (Double progression, Linear, % of training max, or RPE / RIR) and LiftLog fills each pending set with the weight the program prescribes. After the workout, a Progression review marks each exercise as Progressed, Hold, Missed, or Deload. Smart weight suggestions are on by default and can be turned off in Settings."
  - q: "Does LiftLog track personal records and 1RM?"
    a: "Yes. A PR badge with the improvement appears the moment a set beats your estimated 1RM history. Each exercise page keeps your Personal Bests (Est. 1RM, Best Set, and Best Volume) and Rep PRs, with Estimated 1RM, Volume, and Avg RPE charts. You choose the 1RM formula in Settings: Adaptive (recommended), Brzycki, or Epley. Warm-up sets never count."
  - q: "Does LiftLog support RPE?"
    a: "Yes, as an option. You add an RPE from 1 to 10 by editing a set after the workout; there is no RPE field on the live set row. Each exercise then gets an average-RPE chart, and exercises on the RPE / RIR progression scheme use what you enter."
  - q: "Does LiftLog need an account or an internet connection?"
    a: "No. LiftLog needs no account, and every feature works offline, including all 1,500 exercise animations. The internet is used only to buy, restore a purchase, or open a link. Your workouts stay on your iPhone, and Lagerland Apps never receives them."
  - q: "Does LiftLog sync with iCloud? How do I move to a new iPhone?"
    a: "There is no iCloud or cross-device sync. To move your history, export a JSON backup in Settings and import it on the new iPhone. You can also export a CSV file at any time."
  - q: "Can I import workouts from Strong, Hevy, or another tracker?"
    a: "No. LiftLog imports only its own JSON backup. You can export your full history from LiftLog as JSON or CSV whenever you want."
  - q: "Is there a plate calculator?"
    a: "Yes. Open the Plate Calculator from the workout toolbar or from Settings, enter a target weight, and it shows which plates go on each side of the bar and the total. It notes when the bar alone is enough or when the weight can't be loaded exactly. It stays available after the trial."
  - q: "Can I use Siri with LiftLog?"
    a: "Yes. Say “Start my next workout with LiftLog”, or start a saved workout by name. During a workout, Siri can log the set you're on and start your rest timer. You can also ask for your training streak or this week's volume without opening the app. All six actions are in the Shortcuts app too."
  - q: "Which languages does LiftLog support?"
    a: "The app interface is translated into many languages, including German, French, Spanish, Japanese, and Arabic. Exercise names and instructions are available in 23 languages, and you can choose the exercise language separately from the app language."
  - q: "How current is the information on this page?"
    a: "We update this page with each App Store release; the dates are in the page footer. The four one-time tiers ({P_IAP:Minimum} / {P_IAP:Suggested} / {P_IAP:Supporter} / {P_IAP:Patron}) and the 7-day trial without a card match the App Store. If the App Store ever shows different prices, the App Store is canonical."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/liftlog/support/"

release:
  first_release: "2026-04-25"
  last_updated: "2026-10-23"

related_journal:
  slug: "liftlog-pay-what-you-can"
  anchor: "Why four prices for one app: the bet, in our own words"

ratings:
  value: "5.0"
  count: 2
  last_synced: "2026-10-29"
last_updated: 2026-10-29
---
LiftLog is a gym workout tracker for iPhone that you pay for once. The first 7 days are free with no card on file. After that you buy the app once at one of four tiers, from {P_IAP:Minimum} (Fair) to {P_IAP:Patron} (Patron). Every tier unlocks the same app, nothing renews, and Family Sharing is on. If you never buy, your history, charts, and exports stay open to you.

Logging is built for the minute between sets. Weight and reps go in on a docked keypad, each row shows what you lifted last time, and the next set is filled in from your last working set. Checking off a working set starts the rest timer, which keeps running in the background. A PR badge appears the moment a set beats your estimated 1RM history, and Workout Complete sums up the session in an image you can save.

LiftLog comes with 1,500 exercises, each with a looping animation and How To steps, and names and instructions in 23 languages. Browse Templates holds 40 ready-made programs based on well-known routines such as StrongLifts 5×5, Starting Strength, and 5/3/1. With a progression scheme on an exercise (double progression, linear, % of training max, or RPE), LiftLog suggests the weight for each set. The Progress tab adds an activity heatmap, 30-day comparisons, Muscle Coverage, and bodyweight with six body measurements.

Ten Home Screen and Lock Screen widgets and six Siri actions bring your streak, your week, and your next session outside the app. LiftLog needs no account, has no analytics or ads, and works fully offline. Workouts stay on your iPhone, with JSON and CSV export and optional Apple Health export. It runs on iPhone only; there is no Apple Watch app and no iCloud sync. The program names belong to their owners, who don't endorse LiftLog.
