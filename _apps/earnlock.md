---
layout: app
slug: earnlock
name: "EarnLock"
tagline: "Lock distracting apps until you earn them with steps."
quick_answer: "EarnLock is an iPhone app that keeps the apps you lose time to locked until you have moved enough that day, with Apple Health keeping score. Reach half your goal and they open for an hour; reach all of it and they stay open until midnight. Locking one app or category with a step goal is free for good, every widget included, and Premium ({P_MONTHLY}/month or {P_YEARLY}/year, each starting with a {TRIAL}, or {P_LIFETIME} once) adds unlimited apps, active minutes and calories, the Apple Watch app, and Smart Schedules. There is no account, and your data stays on your iPhone."
category: lifestyle
status: live
jump_nav: true

app_store_url: "https://apps.apple.com/app/id6771099230"

price:
  model: freemium

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew. Monthly, Yearly, and Lifetime all support Family Sharing."

release_notes:
  - date: "2026-05-22"
    note: "EarnLock 1.0: apps that unlock when you hit a daily activity goal, partial and full unlocks, Shadow Week, a math-gated emergency unlock, streaks with a weekly rest day, widgets, a Live Activity, and the Apple Watch app."

plans:
  - name: "Free"
    price: "$0"
    summary: "One locked app or category, earned with steps. Free for good, with no account."
    features:
      - "Lock one app or one category with Apple's Screen Time picker"
      - "A daily step goal: Light, Standard, Challenge, your own number, or Adaptive"
      - "An hour of access at halfway, and everything open until midnight at 100%"
      - "A screen over each locked app showing how many steps are left"
      - "Shadow Week: seven days of counting before anything is blocked"
      - "Every widget, Lock Screen and full-page widgets included"
      - "Streaks with a weekly rest day, and milestone cards"
      - "The Insights Day view and one-tap Reflect"
      - "A math-gated emergency unlock, once a day"
  - name: "Premium · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "All of Premium, billed monthly, starting with a {TRIAL}. Cancel anytime."
    features:
      - "Unlimited locked apps and categories"
      - "Earn with active minutes or active calories as well as steps"
      - "The Apple Watch app and complications"
      - "A Live Activity and Dynamic Island countdown"
      - "Smart Schedules for work hours, evenings, weekends, and sleep"
      - "Insights Week and Month, with a heatmap and your reflection log"
      - "Streak shields"
      - "Skip the 24-hour wait on lowering your goal, once a week"
      - "Midnight, Ember, and Mono app icons"
      - "Family Sharing"
  - name: "Premium · Yearly"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "The same Premium, billed once a year, starting with a {TRIAL}. About {SAVE_YEARLY}% less than paying monthly."
    features:
      - "Everything in Premium · Monthly"
      - "Starts with a {TRIAL}"
      - "~{SAVE_YEARLY}% less than paying monthly for a year"
      - "Family Sharing"
      - "Cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All of Premium for one payment."
    features:
      - "Everything in Premium · Yearly"
      - "One-time purchase, no renewal"
      - "Restores through your Apple ID on a new iPhone"
      - "Family Sharing"
    highlight_label: "Pay once"

icon: "/assets/icons/earnlock.png"
og_image: "/assets/og/earnlock.png"

seo:
  title: "EarnLock: Block Apps Until You Walk, Free for One App"
  description: "Lock Instagram, TikTok, or any app until you hit a daily step goal. Halfway opens an hour. Free for one app, no account, data stays on your iPhone."
  keywords:
    - earn screen time app
    - block apps until you walk
    - walk to unlock apps
    - steps unlock apps iphone
    - exercise to unlock phone
    - screen time blocker activity
    - block instagram until you walk
    - app blocker no account
    - apple watch screen time blocker
    - lifetime app blocker
    - opal alternative
    - one sec alternative
    - screenzen alternative
    - brick alternative no hardware

spotlight:
  overline: "What makes EarnLock different"
  heading: "For the first week, EarnLock blocks nothing and counts every reach."
  lead: "Most blockers ask for the rules on day one, before you know which app is the problem or what goal you can keep. EarnLock starts with a Shadow Week. For seven days after you pick your apps, blocking is only simulated, and every time you open one of them EarnLock counts the block you would have hit. Then \"Your shadow week is done\" shows your own numbers next to an \"Enable real blocking\" button, so your first real lock is set from what you actually do. Later you can run another Shadow Week from Settings and compare then with now."
  stats:
    - value: "7 days"
      label: "Blocking is simulated while EarnLock counts your opens"
    - value: "Your numbers"
      label: "The summary shows how often you would have been blocked"
    - value: "Free"
      label: "Shadow Week, its replay, and its history are in the free tier"

hero:
  pre_headline: "For anyone who has tapped straight past a screen-time limit"
  headline: "Your feeds stay locked until you've moved."
  secondary: "Move first, scroll later."
  subheadline: "Pick the apps that eat your evenings and set a daily goal. Halfway there, they open for an hour. Hit the goal and they stay open until midnight. Apple Health keeps score, and nothing leaves your iPhone."
  cta_label: "Download Free"
  cta_subline: "Free for one app · no account needed"
  alt: "EarnLock home screen on iPhone showing 1,974 steps on a live progress ring with “Earn 2,026 more steps to unlock” beneath, and the Locked apps grid including Instagram and TikTok"

founder:
  overline: "Why we built this"
  heading: "Why EarnLock's key is a walk."
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple studio · Finland"
  location: "Finland"
  photo: "/assets/icons/lagerland-mark.png"
  bio: "Every screen-time tool we tried could be talked out of its lock: a passcode we had set ourselves, a timer we could sit out, a button offering one more minute. EarnLock makes the key a walk. You move, Apple Health counts it, and the apps open. Half a goal still earns an hour, because a lock that gives nothing for a bad day is the one people switch off. Lagerland Apps is a one-person studio in Finland with no investors or advertisers, and the studio's other {APP_COUNT_OTHER} apps follow the same data rules."
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails are answered personally, usually within a day."
  signals:
    - "No EarnLock server: the app makes no network connections of its own"
    - "No third-party SDKs of any kind, including analytics, ads, and crash reporting"
    - "No account; Premium restores through your Apple ID"
    - "Lagerland's App Store catalogue is {APP_COUNT} privacy-first apps under the same data rules"
  external_link:
    href: "/lagerland-apps/"
    label: "Read the Lagerland studio backstory →"

how_it_works:
  intro: "EarnLock locks apps with Apple's Screen Time controls and measures the key with Apple Health. This is the whole rule, and all of it runs on your iPhone."
  steps:
    - title: "Pick the apps, then the goal"
      detail: "Choose apps or whole categories in Apple's own Screen Time picker: one on the free tier, as many as you like with Premium. Then pick a unit and a goal. Steps are free; active minutes and active calories come with Premium. Light, Standard, and Challenge mean 4,000, 8,000, or 12,000 steps (20, 30, or 45 active minutes; 150, 300, or 500 active calories). You can also type your own number or choose Adaptive, which rises 3% after a day you hit and eases 5% after a day you miss."
    - title: "Open a locked app and see what's left"
      detail: "A locked app shows EarnLock's screen instead, with exactly how far you are, for example \"2,026 steps until unlock\". Earn it takes you to EarnLock. Your progress comes from Apple Health as you move and shows on the Today screen and in the widgets."
    - title: "Halfway opens a window, the full goal opens the day"
      detail: "At 50% of your goal your locked apps open for a window sized to your progress, an hour at halfway, and lock again by themselves when it ends. At 100% they stay open until midnight, when everything locks and the day starts over. For a real emergency, solve a two-digit math problem and pick 15, 30, or 60 minutes, once a day."

value_points:
  - title: "Movement is the key"
    description: "Other blockers leave the key in your pocket: a password you chose, a delay you can sit through, a screen you dismiss. EarnLock opens your apps when Apple Health shows you've moved. The one other way in is a math-gated emergency unlock, once a day."
  - title: "Effort always buys something"
    description: "Halfway to your goal opens an hour of screen time right away, so a slow day still earns a window. Reach the full goal and your apps open by themselves until midnight."
  - title: "Free for one app, for good"
    description: "Lock one app or category with a step goal and you get partial and full unlocks, Shadow Week, streaks, the Insights Day view, and every widget. Premium is there for when one app isn't enough."
  - title: "Nothing leaves your iPhone"
    description: "There is no account to create and no EarnLock server to send anything to. Apple Health data is read on your iPhone and stays there, and the app carries no analytics or ad SDKs."

features:
  - title: "A lock that shows the price"
    description: "Open a locked app and EarnLock's screen covers it with what's left to earn, such as \"2,026 steps until unlock\". Tap Earn it to go to EarnLock and see your day."
  - title: "Steps, active minutes, or active calories"
    description: "Steps are free. Premium adds active minutes (Apple's Exercise minutes) and active calories, so a gym session or a bike ride can earn your apps too. EarnLock reads Apple Health on your iPhone, never writes to it, and updates in the background as you move."
  - title: "Goals that adapt, and a cooldown on lowering them"
    description: "Choose Adaptive and your goal rises 3% after a day you hit it and eases 5% after a day you miss, within fixed limits. Rest days don't count against it. Lowering a goal yourself takes effect after 24 hours, so a weak moment can't shrink it; Premium can skip that wait once a week."
  - title: "Emergency unlock, once a day"
    description: "For a real need, open Settings, solve a two-digit math problem, and pick 15, 30, or 60 minutes. You get one per day. The problem is enough friction to stop a reflex and quick enough for an actual emergency."
  - title: "Streaks with a weekly rest day"
    description: "Every day you reach your full goal adds to your streak. Pick a weekly rest day, and a miss on that day won't break it. With Premium, every seventh day at 150% of your goal banks a streak shield (you can hold three), and a shield covers a missed day automatically. At 7, 30, 100, and 365 days you get a milestone card to share or keep."
  - title: "Insights into when you reach"
    description: "The free Day view shows your activity by hour, the locked app you reached for most today, and an estimate of screen time saved. Each blocked attempt counts as 9 minutes, and the card is labelled as an estimate. Premium adds Week and Month views: days you hit your goal, average activity, your best week, and a heatmap of every day you earned."
  - title: "Reflect in one tap"
    description: "When you catch yourself reaching, tap Reflect on the Today screen and answer \"What were you hoping to find?\" with Boredom, Anxiety, FOMO, Habit, or Other. Logging is free. The reflection log and its monthly summary live in Premium's Month view."
  - title: "Smart Schedules"
    description: "Premium lets the rules change with the time of day. Start from Work hours, Evenings, Weekends, and Sleep, and set each one to Light, Standard, Challenge, or blocking off. Where two schedules overlap, the shorter one wins."
  - title: "Every widget is free"
    description: "Five Home Screen widgets and a Lock Screen widget come with every plan: today's ring, a grid of every day you earned, your history by month, 30 days, or year, your streak, and a summary. On iOS 27 a widget can fill a whole Home Screen page. If your phone slept through midnight, the Today widgets say \"Open the app to catch up\" instead of showing yesterday as today."
  - title: "Apple Watch and a Live Activity"
    description: "With Premium, the Apple Watch app reads its own Health data and shows your ring, your count, and how far you are from unlocking, with a Reflect button and complications for your watch face. On the iPhone, a Live Activity appears at 80% of your goal and counts down the last stretch on the Lock Screen and in the Dynamic Island."
  - title: "39 locales"
    description: "EarnLock is translated into 39 locales, including regional versions of English, Spanish, French, and Portuguese, and Arabic and Hebrew, which read right to left."

who_for:
  - "You open Instagram, TikTok, or YouTube without deciding to, and every blocker you've tried was easy to tap past"
  - "You want a push to move more and you're fine with Apple Health keeping score"
  - "You'd like to see your real habit for a week before anything gets blocked"
  - "You want to start free and pay only if one locked app isn't enough"
  - "You want no account, with your data kept on your iPhone"

who_not_for:
  - "You want parental controls for a child's device. EarnLock is for limiting your own iPhone and has no parent controls"
  - "You want a lock with no way out. EarnLock has a once-a-day emergency unlock by design, and iOS lets you turn off its Screen Time access"
  - "You can't carry an iPhone or wear an Apple Watch while you move. Progress comes only from Apple Health"
  - "You have a medical condition that daily activity goals could affect. EarnLock is not a medical device and gives no health advice, so ask your doctor first"
  - "You use an iPad, a Mac, or Android. EarnLock is an iPhone app, with an Apple Watch app in Premium"

alternatives_to:
  - "Opal"
  - "one sec"
  - "ScreenZen"
  - "Jomo"
  - "Forest"
  - "Brick"
  - "Unpluq"
  - "Stoic Mode"
  - "StepBloc"
  - "Time Out"
  - "Steppin"
  - "WalkMyScreen"
  - "Apple Screen Time (built-in)"

comparison_table:
  intro: "Most screen-time apps unlock when you tap a button or wait out a timer. EarnLock unlocks when you move. Competitor pricing and features change often, so check again before switching."
  competitors: ["EarnLock", "Opal", "one sec", "ScreenZen", "Apple Screen Time"]
  rows:
    - feature: "How blocked apps unlock"
      values: ["Daily activity goal (steps; active minutes or calories with Premium)", "Tap-to-pause or wait out timer", "Mandatory 10-second breath pause", "Wait-out timer (e.g., 30s breathe)", "Type a parent / Screen Time passcode"]
    - feature: "Cheapest one-time / lifetime tier"
      values: ["{P_LIFETIME} lifetime", "No lifetime, subscription only", "No lifetime, subscription only", "Free (optional tips)", "Free (system app)"]
    - feature: "Cheapest paid monthly tier"
      values: ["{P_MONTHLY} / mo", "$7.99 / mo (annual)", "$2.99 / mo", "Free (optional tips)", "Free"]
    - feature: "Blocked app shows what's left to unlock"
      values: ["Yes: \"N steps until unlock\"", "Generic app-restricted screen", "Generic app-restricted screen", "Generic app-restricted screen", "Generic \"Screen Time\" screen"]
    - feature: "Apple Watch app + complications"
      values: ["Yes (Premium); the watch reads its own Health data", "iPhone only", "iPhone only", "iPhone only", "Yes, system-wide"]
    - feature: "Account or sign-up required"
      values: ["No account needed", "Account required", "Account required", "Account required", "Apple ID (system-level)"]
    - feature: "Third-party tracking SDKs"
      values: ["None", "Multiple: analytics & ads", "Some: analytics", "Some: analytics", "Apple only"]
    - feature: "Daily emergency unlock"
      values: ["Yes, once a day, after a two-digit math problem", "Yes, tap a button", "Tap-through after pause", "Tap-through after pause", "Requires passcode"]
  footnote: "Verified 2026-05-22 against each app's public App Store page, developer landing page, and pricing / help documentation. Competitor offerings change often, so check again before switching. Mechanism descriptions are based on each app's own published documentation. ScreenZen's pricing model was rechecked on the German App Store on 2026-10-27."

screenshots:
  - src: "/assets/screenshots/earnlock/1.webp"
    alt: "EarnLock home screen on iPhone showing a step ring and locked apps that unlock as you walk"
  - src: "/assets/screenshots/earnlock/2.webp"
    alt: "EarnLock year grid showing days earned over twelve months"
  - src: "/assets/screenshots/earnlock/3.webp"
    alt: "EarnLock monthly insights with total steps and best week"
  - src: "/assets/screenshots/earnlock/4.webp"
    alt: "EarnLock Home Screen widgets showing steps and progress to unlock"
  - src: "/assets/screenshots/earnlock/5.webp"
    alt: "EarnLock Shadow Week summary before real app blocking is turned on"
  - src: "/assets/screenshots/earnlock/6.webp"
    alt: "EarnLock Live Activity and Apple Watch showing how close you are to unlocking"
  - src: "/assets/screenshots/earnlock/7.webp"
    alt: "EarnLock full-page widget with a progress calendar"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No account, and no analytics, advertising, or other third-party SDKs"
    - "The app makes no network connections of its own; links open in your browser"
    - "Apple Health is read on your iPhone, never written to, and never sent anywhere"
    - "Apple's Screen Time picker gives EarnLock opaque tokens instead of the names of your apps"
    - "You can export everything EarnLock stores as one file, or erase it all, in Settings"

faq:
  - q: "What is EarnLock?"
    a: "EarnLock is an iPhone app that keeps distracting apps locked until you reach a daily activity goal, measured by Apple Health. Half the goal opens them for an hour, and the full goal opens them until midnight. Locking one app or category with a step goal is free for good. Premium adds unlimited apps, active minutes and active calories, the Apple Watch app, a Live Activity, Smart Schedules, and Week and Month insights, for {P_MONTHLY}/month or {P_YEARLY}/year (each starting with a {TRIAL}) or {P_LIFETIME} once. There is no account, and your data stays on your iPhone."
  - q: "How is EarnLock different from Opal, one sec, ScreenZen, or Forest?"
    a: "Those apps put a pause, a timer, or a tap between you and the app. EarnLock puts a daily activity goal there, measured by Apple Health: halfway opens your apps for an hour, and the full goal opens them until midnight. It also starts with a Shadow Week that blocks nothing and counts how often you would have been blocked, so your first real lock fits your habit. It needs no account, locking one app is free for good, and Premium is available monthly, yearly, or as a one-time {P_LIFETIME} purchase."
  - q: "Which apps can EarnLock block?"
    a: "Any app or whole category you can choose in Apple's Screen Time picker. The free tier locks one app or one category, and Premium has no limit. The picker gives EarnLock opaque tokens, so the app never sees the names of what you chose."
  - q: "How does the activity goal work?"
    a: "You pick a unit and a daily goal: steps on the free tier, or active minutes or active calories with Premium. Presets are Light, Standard, and Challenge (4,000, 8,000, or 12,000 steps), or you can set your own number or choose Adaptive. EarnLock reads your progress from Apple Health on your iPhone. At 50% your locked apps open for a window sized to your progress, an hour at halfway, then lock again. At 100% they stay open until midnight. Below 50% everything stays locked, and the day resets at midnight."
  - q: "Does EarnLock work on Apple Watch?"
    a: "Yes, with Premium. The Watch app reads its own Health data and shows your ring, your count, and how far you are from unlocking, plus a Reflect button. Complications come in circular, corner, inline, and rectangular styles. Without Premium the Watch app shows a locked state. The iPhone is still the device that locks and unlocks your apps, and it passes your Premium status to the watch."
  - q: "What if I genuinely need to use a blocked app for something urgent?"
    a: "Use the emergency unlock in Settings. Solve a two-digit math problem, choose 15, 30, or 60 minutes, and your apps open. You get one per day. The math is enough friction to stop a reflex and quick enough for a real need."
  - q: "What about streaks and rest days?"
    a: "Every day you reach your full goal adds to your streak. You can pick a weekly rest day, and a miss on that day won't break the streak. With Premium, every seventh day at 150% of your goal banks a streak shield (you can hold three), and a shield covers a missed day automatically. A streak-at-risk reminder is one of the notification types you can switch off, and quiet hours keep reminders out of the night."
  - q: "Is EarnLock free? What does Premium unlock?"
    a: "Locking one app or one category with a step goal is free for good. The free tier includes partial and full unlocks, the screen that shows what's left on each locked app, Shadow Week, every widget, streaks with a weekly rest day, the Insights Day view, one-tap Reflect, and the emergency unlock. Premium adds unlimited apps, active minutes and active calories, the Apple Watch app and complications, the Live Activity, Smart Schedules, Week and Month insights with the reflection log, streak shields, a once-a-week skip of the 24-hour goal cooldown, and three alternate app icons. Premium is {P_MONTHLY}/month or {P_YEARLY}/year, each starting with a {TRIAL}, or {P_LIFETIME} once, and all three support Family Sharing."
  - q: "Does EarnLock collect any data?"
    a: "No. EarnLock has no account, makes no network connections of its own, and includes no analytics, advertising, or other third-party SDKs. Apple Health is read on your iPhone and never written to or sent anywhere. Your goals, streaks, reflections, and schedules are stored on the device. The Screen Time picker gives EarnLock opaque tokens, so the app can't see which apps you chose. The privacy policy has the details."
  - q: "Can I export or delete my EarnLock data?"
    a: "Yes. In Settings, Data & privacy, Export builds one file with your goal, streak and daily records, reflection log, schedules, and notification settings; Apple Health samples stay in Apple Health. Delete all data asks you to type DELETE, then erases what EarnLock stores and removes its locks."
  - q: "Can EarnLock be used as parental control?"
    a: "No. EarnLock is built for limiting your own iPhone. There is no parent side to it: nothing to manage remotely and no passcode for someone else to hold. For a child's device, use Screen Time with Family Sharing in iOS Settings."
  - q: "What devices does EarnLock support?"
    a: "iPhone with iOS 17 or later, in portrait. The Premium Apple Watch app needs watchOS 10 or later. The Control Center control needs iOS 18, and full-page widgets need iOS 27. EarnLock needs Apple Health and Screen Time access to work. There is no iPad, Mac, or Android version."
  - q: "Does EarnLock support Family Sharing?"
    a: "Yes. Monthly, Yearly, and Lifetime all support Family Sharing, so the members of your Apple family group can use Premium too. Each person's goals, locked apps, and streaks stay on their own iPhone."
  - q: "Is Lifetime really a one-time payment?"
    a: "Yes. Lifetime is one payment of {P_LIFETIME} with no renewal, and it restores through your Apple ID if you move to a new iPhone. The App Store shows the price before you confirm."
  - q: "How accurate is the screen-time-saved estimate?"
    a: "It's an estimate, and the card says so. iOS doesn't let apps read your real per-app Screen Time, so EarnLock counts what it can see: each time a locked app stops you. It multiplies those attempts by 9 minutes."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/earnlock/support/"

release:
  first_release: "2026-05-22"
  last_updated: "2026-05-22"

related_journal:
  slug: "what-an-iphone-app-can-actually-block"
  anchor: "What an iPhone app can actually block, and what it never will"

ratings:
  value: ""
  count: 0
  last_synced: "2026-05-22"
  display_label: "New release"
last_updated: 2026-10-29
---
EarnLock is an iPhone app that keeps the apps you lose time to locked until you reach a daily activity goal. Apple Health keeps score: steps on the free tier, or active minutes or active calories with Premium. Reach half your goal and your locked apps open for an hour. Reach all of it and they stay open until midnight, when everything locks again and the day starts over.

The first week is a Shadow Week. Blocking is only simulated while EarnLock counts how often you would have been blocked, and at the end you turn on real blocking with your own numbers in front of you. Open a locked app later and EarnLock's screen tells you exactly what's left, such as "2,026 steps until unlock". For real needs there is a math-gated emergency unlock, once a day.

Locking one app or category is free for good, and so are Shadow Week, streaks with a weekly rest day, the Insights Day view, one-tap Reflect, and every widget. Premium adds unlimited apps, active minutes and active calories, the Apple Watch app and complications, a Live Activity, Smart Schedules, Week and Month insights, and streak shields, for {P_MONTHLY}/month or {P_YEARLY}/year (each starting with a {TRIAL}) or {P_LIFETIME} once, with Family Sharing on all three. EarnLock needs iOS 17 or later and comes in 39 locales. It has no account and no third-party SDKs, and your data stays on your iPhone.
