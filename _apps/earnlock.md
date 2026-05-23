---
layout: app
slug: earnlock
name: "EarnLock"
tagline: "Earn your screen time. Move, then scroll."
quick_answer: "EarnLock is an iOS and Apple Watch app that locks distracting apps — Instagram, TikTok, X, Reddit, YouTube, anything you choose — until you earn your screen time by hitting a daily activity goal you set yourself. The free tier unlocks via daily steps; Premium adds active minutes and active energy. Apple's Family Controls renders a custom shield with a live progress ring (\"3,412 steps until unlock\") over each blocked app. Live Activities and lock-screen widgets keep the count visible; the Apple Watch app and complications read Apple Health directly so the count works without the iPhone. Streaks, rest days, a math-gated emergency unlock (1/day), most-attempted-blocked-app insights, a screen-time-saved estimate, and a reflection log are all built in. 39 locales (incl. 2 RTL), no account, no analytics SDK, no server. Free; Premium $1.99/month or $9.99/year (both with a 7-day free trial), or $19.99 lifetime. Every paid tier — Monthly, Yearly, and Lifetime — is Family Sharing eligible: one purchase covers up to 5 family members at no extra cost."
category: lifestyle
platforms: ["iOS", "watchOS"]
status: live
jump_nav: true

app_store_url: "https://apps.apple.com/app/id6771099230"

price:
  model: freemium
  value: "Free — Premium from $1.99/mo or $19.99 lifetime"
schema_price: "0"
schema_high_price: "19.99"
schema_offer_count: "4"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. Lifetime is a one-time purchase — $19.99 once, no auto-renew, no card kept on file beyond Apple's own. Every paid tier (Monthly, Yearly, Lifetime) is Family Sharing eligible — one purchase covers up to 5 family members at no extra cost."

release_notes:
  - date: "2026-05-22"
    note: "EarnLock 1.0 — Family Controls shield with live progress ring, HealthKit-driven goal engine, Apple Watch complications, Live Activities, math-gated emergency unlock, streak engine with rest days, 39 locales."

plans:
  - name: "Free"
    price: "$0"
    summary: "Steps-based unlocks, free forever. No trial, no card, no account."
    features:
      - "Block any iOS app or category via Apple's Family Controls picker"
      - "Steps-based daily goal — when you cross it, your apps unlock"
      - "Custom shield with live progress ring on every blocked app"
      - "Lock-screen widget + Live Activity keep the count visible"
      - "Apple Watch app + complication (steps source, on-wrist count)"
      - "Math-gated emergency unlock — once per day, real friction"
      - "Streak engine + weekly rest day"
      - "On-device only — no account, no server, no analytics SDK"
  - name: "Premium · Monthly"
    price: "$1.99/mo"
    summary: "Full Premium, billed monthly. 7-day free trial. Cancel anytime."
    features:
      - "Active minutes goal (HealthKit Exercise Time) — better for runners and gym sessions"
      - "Active energy goal (kcal) — better for high-intensity training"
      - "Partial-progress windows: 60% of goal = 60% of the day unlocked"
      - "Most-attempted-blocked-app insights (which app you tap most while shielded)"
      - "Screen-time-saved estimate based on your historical use of blocked apps"
      - "Reflection log — short journal prompt at end of each unlocked block"
      - "Schedule profiles (weekday vs weekend, morning-only, etc.)"
      - "7-day free trial — cancel before day 7 and pay nothing"
      - "Family Sharing — covers up to 5 family members at no extra cost"
  - name: "Premium · Yearly"
    price: "$9.99/yr"
    summary: "Same Premium features, billed once a year. 7-day free trial. ~58% cheaper than monthly."
    features:
      - "Everything in Premium · Monthly"
      - "7-day free trial — cancel before day 7 and pay nothing"
      - "~58% cheaper than paying monthly all year"
      - "Family Sharing — covers up to 5 family members at no extra cost"
      - "Cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "$19.99 once"
    summary: "All Premium features, forever. Roughly 10 months of monthly Premium — then yours."
    features:
      - "Everything in Premium · Yearly"
      - "One-time purchase — $19.99 once, no renewal, no auto-charge"
      - "Family Sharing — covers up to 5 family members at no extra cost"
      - "Future Premium features included — no upsell on what you already paid for"
      - "Breaks even versus monthly Premium in roughly 10 months of use"
    highlight_label: "Best value · cheapest lifetime among screen-time blockers"

icon: "/assets/icons/earnlock.png"
og_image: "/assets/og/earnlock.png"

seo:
  title: "EarnLock — Block Apps Until You Walk · $19.99 Lifetime"
  description: "Lock Instagram, TikTok, X until you hit your daily step goal. Custom shield, Apple Watch, no account, no server. $19.99 lifetime — or free."
  keywords:
    - earn screen time app
    - block apps until you walk
    - walk to unlock apps
    - exercise to unlock phone
    - steps unlock apps iPhone
    - screen time blocker activity
    - Opal alternative
    - one sec alternative
    - ScreenZen alternative
    - Jomo alternative
    - Forest app alternative
    - Brick alternative no hardware
    - Unpluq alternative
    - block Instagram until you walk
    - block TikTok with steps
    - HealthKit screen time blocker
    - Family Controls custom shield
    - Apple Watch screen time blocker
    - digital wellbeing app iPhone
    - app blocker no subscription
    - lifetime app blocker
    - screen time blocker no account
    - private screen time app
    - shield app with progress ring
    - distraction blocker iOS
    - movement-based app blocker
    - activity goal app blocker
    - block social media until exercise
    - phone addiction app movement
    - mindful tech use iPhone

hero:
  headline: "Block the doomscroll until you move."
  secondary: "Earn your screen time."
  subheadline: "EarnLock locks Instagram, TikTok, X, YouTube, Reddit — whatever you pick — until you hit a daily activity goal you set yourself. Steps in the free tier; active minutes or calories in Premium. The shield over each blocked app shows a live progress ring counting down (\"3,412 steps until unlock\"). The Apple Watch app keeps the count on your wrist when the iPhone isn't with you. No account. No analytics SDK. No server. $19.99 lifetime."
  cta_label: "Download Free"
  cta_subline: "$19.99 lifetime · pay once, no subscriptions, no account."
  alt: "EarnLock home screen on iPhone showing a daily step goal of 7,500, a live progress ring at 46%, and the list of currently shielded apps including Instagram and TikTok"

founder:
  overline: "Why we built this"
  heading: "Built by people who lost too many evenings to the feed."
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple studio · Finland"
  location: "Finland"
  photo: "/assets/icons/lagerland-mark.png"
  bio: "Every screen-time app we tried had the same flaw: the unlock cost nothing real. Tap \"give me another minute,\" tap \"emergency,\" tap a four-digit code you set thirty seconds ago. The friction is theatre. EarnLock makes the cost concrete — walk a kilometre, finish a 30-minute Exercise Time block, burn 400 active calories — and the apps unlock on their own. The shield over each blocked app shows you exactly how far you are from your daily goal. The Apple Watch carries the count when the iPhone isn't with you. There is no account, no server, no analytics SDK, no advertising SDK. Lagerland is a small Apple studio in Finland — no team, no investors. The studio's other 15 apps run on the same data discipline."
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails are answered personally, usually within a day."
  signals:
    - "100% on-device — no EarnLock server, ever (verified by Apple's App Privacy nutrition label: Data Not Collected)"
    - "Zero third-party SDKs — no Firebase, Mixpanel, Amplitude, Segment, ad networks, or crash reporters"
    - "Family Controls authorized in `.individual` mode only — EarnLock is self-restriction software, never parental control"
    - "Lagerland's App Store catalogue is 15 privacy-first apps, all with the same data discipline"
  external_link:
    href: "/lagerland-apps/"
    label: "Read the Lagerland studio backstory →"

how_it_works:
  intro: "EarnLock turns Apple's Family Controls into a goal-gated lock. The rule is published below in full; the algorithm is transparent and runs entirely on your device."
  steps:
    - title: "Pick what to block, set today's goal"
      detail: "Open the Family Controls picker (Apple's system UI — EarnLock never sees the app names you pick; iOS hands us opaque tokens) and select any combination of apps and categories. Set your daily goal: steps in the free tier, or active minutes / active energy in Premium. Defaults follow standard wellness guidelines (7,500 steps, 30 active minutes, 400 active kcal); change them to anything that matches your life."
    - title: "EarnLock reads HealthKit and renders a live shield"
      detail: "From the moment you wake your phone, EarnLock's DeviceActivityMonitor extension tracks your HealthKit progress on-device. When you open a blocked app, Apple's ManagedSettings framework calls EarnLock's ShieldConfiguration extension — we paint a custom shield over the app with a progress ring and plain text: \"3,412 steps until unlock\". The Apple Watch app and complication mirror the same count without the iPhone. Live Activities and lock-screen widgets keep it visible everywhere else."
    - title: "Cross the threshold, apps unlock for the day"
      detail: "When you hit 100% of your daily goal, every shielded app unlocks for the rest of the calendar day. Partial progress earns a partial-time window — Premium only — so a 60% day buys 60% of the unlocked hours instead of nothing. At local midnight, the shield resets. Streaks track consecutive goal-met days; rest days protect the streak when you genuinely need one. If something is on fire, the math-gated emergency unlock (1 per day cap) opens the apps after you solve a real arithmetic problem — no PIN, no four-digit recall."

value_points:
  - title: "Movement is the unlock — no PIN, no \"give me one more minute\""
    description: "Other screen-time apps unlock when you tap a button, recite a number, or wait out a timer. EarnLock unlocks when your body actually does the work — measured by Apple Health, not self-reported. The friction is real because the cost is real."
  - title: "Custom shield with a live progress ring"
    description: "Apple's Family Controls only renders a generic \"App Restricted\" shield by default. EarnLock ships a ShieldConfiguration extension that paints a circular progress ring with \"X steps until unlock\" copy live over every blocked app. You always know how close you are."
  - title: "Apple Watch — count on the wrist, complication on the face"
    description: "EarnLock's Watch app reads HealthKit directly, so the count works on long walks, runs, and gym sessions without the iPhone. Native complications surface the count on every watch face style — modular, circular, corner, graphic — so a glance tells you whether the apps will be open when you sit back down."
  - title: "Cheapest lifetime among screen-time blockers"
    description: "$19.99 lifetime — versus Opal at $99.99/yr, ScreenZen Premium at ~$60/yr, or Brick at $59 hardware. Free if you only need step-based goals. Local-first by architecture, not just by policy."

features:
  - title: "Family Controls shield with a live progress ring"
    description: "EarnLock includes a ShieldConfiguration extension that replaces Apple's generic restriction screen with a custom shield showing a circular progress ring and the exact number you have left — \"3,412 steps until unlock\", \"18 minutes of exercise until unlock\", \"187 active kcal until unlock\". The shield refreshes every time you open the blocked app, so the count is always current. The shield action button takes you straight to your goal screen, not to a paywall."
  - title: "HealthKit-driven goal engine"
    description: "Steps (free), active minutes (Premium), or active energy (Premium). Goals reset at local midnight in your device timezone — not at a server UTC boundary. EarnLock reads HealthKit on-device only, never writes to Health, and never transmits the data off the device. You can revoke access in iOS Settings → Privacy → Health → EarnLock at any time."
  - title: "Apple Watch app + complications"
    description: "The Watch app shows your live progress against today's goal, the shielded-app list, your streak count, and whether you have a rest day available. Complications mount on modular, circular, corner, and graphic faces. Watch and iPhone stay in sync via WatchConnectivity — when the count crosses on the Watch, the iPhone's shields drop within seconds."
  - title: "Live Activities + lock-screen widgets"
    description: "Live Activities run during long sessions (walks, workouts) and put the progress ring on the lock screen and in the Dynamic Island. Lock-screen widgets show the same count even when no session is active. Home Screen widgets in three sizes mirror the state. None of it requires unlocking the phone."
  - title: "Streak engine + rest-day support"
    description: "Daily goal-met days build a streak. One rest day per week protects the streak so a planned recovery day doesn't reset it — that's a deliberate health choice, not a failure. EarnLock never sends a notification shaming you for missing a day. Streak data is local; if you delete the app, it's gone."
  - title: "Math-gated emergency unlock (1 per day cap)"
    description: "For genuine emergencies, EarnLock includes one emergency unlock per day. Triggering it requires solving a real arithmetic problem (not a four-digit PIN you set thirty seconds ago) — enough friction to defeat impulse, not enough to defeat actual need. Once used, the next emergency unlock isn't available until local midnight."
  - title: "Most-attempted-blocked-app insights + screen-time-saved estimate"
    description: "Premium surfaces which blocked app you tap the most while shielded — usually a humbling number. Combined with your historical use of those apps (read from iOS's own Screen Time data, with your explicit permission), EarnLock estimates how many hours you saved this week, this month, this year. The estimate is conservative and disclosed; the methodology is published on the product page."
  - title: "Reflection log"
    description: "When the apps unlock for the day, EarnLock prompts a 20-second reflection: did you actually want them, or had you forgotten you were locked out? The log is local-only and timestamped. Over weeks it becomes a quiet record of which days the friction mattered — and which days you would have been fine without any of it."
  - title: "Schedule profiles (weekday / weekend / custom)"
    description: "Premium ships goal profiles so weekday goals (e.g., 5,000 steps, work-from-home) and weekend goals (e.g., 10,000 steps, longer walks) can be different. Profiles can also target a window — \"shield from 9 a.m. to 6 p.m. on weekdays\" — using Apple's Schedules framework."
  - title: "39 locales, including 2 RTL"
    description: "EarnLock ships in 39 languages out of the box — English, Spanish, French, German, Portuguese (BR + PT), Italian, Dutch, Polish, Russian, Ukrainian, Turkish, Arabic, Hebrew, Hindi, Indonesian, Malay, Thai, Vietnamese, Japanese, Korean, simplified and traditional Chinese, Finnish, Swedish, Norwegian, Danish, Greek, Czech, Slovak, Hungarian, Romanian, Croatian, Catalan, and more. Arabic and Hebrew render right-to-left."

who_for:
  - "You can't stop opening Instagram / TikTok / X / Reddit / YouTube and the existing screen-time tools never had real friction"
  - "You want a screen-time blocker tied to something concrete — movement — instead of a PIN you set thirty seconds ago"
  - "You wear an Apple Watch and want the count on your wrist, not just on the phone"
  - "You want digital wellbeing and a small fitness nudge from the same app, not two separate subscriptions"
  - "You're allergic to subscription-only screen-time apps and want a one-time lifetime option"
  - "You want zero account, zero analytics SDK, zero server — a tool that can't betray you"

who_not_for:
  - "You want parental controls over a child's device — EarnLock authorizes Family Controls in `.individual` mode only and never supports the `.child` mode"
  - "You can't or don't want to wear an iPhone / Apple Watch (steps are read from CoreMotion + Apple Health only)"
  - "You're looking for a strict, no-emergency-unlock blocker — EarnLock includes a math-gated daily emergency by design"
  - "You have a heart condition, eating disorder, or exercise-related injury that activity goals could affect — talk to your physician before relying on EarnLock's prompts"
  - "You train on Android — EarnLock is iOS + watchOS only and not planned for other platforms"

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
  intro: "Most screen-time apps unlock when you tap a button or wait out a timer. EarnLock unlocks when you actually move. The table below compares the public, verified facts; competitor pricing and mechanics change, so re-check before switching."
  competitors: ["EarnLock", "Opal", "one sec", "ScreenZen", "Apple Screen Time"]
  rows:
    - feature: "How blocked apps unlock"
      values: ["Daily activity goal hit (steps / active minutes / active calories)", "Tap-to-pause or wait out timer", "Mandatory 10-second breath pause", "Wait-out timer (e.g., 30s breathe)", "Type a parent / Screen Time passcode"]
    - feature: "Cheapest one-time / lifetime tier"
      values: ["$19.99 lifetime", "No lifetime — subscription only", "No lifetime — subscription only", "No lifetime — subscription only", "Free (system app)"]
    - feature: "Cheapest paid monthly tier"
      values: ["$1.99 / mo", "$7.99 / mo (annual)", "$2.99 / mo", "$2.99 / mo (varies)", "Free"]
    - feature: "Custom shield with live progress ring on the blocked app"
      values: ["Yes — ShieldConfiguration extension paints a ring + \"X steps until unlock\"", "Generic app-restricted screen", "Generic app-restricted screen", "Generic app-restricted screen", "Generic \"Screen Time\" screen"]
    - feature: "Apple Watch app + complications"
      values: ["Yes — first-class, reads HealthKit on the Watch", "iPhone only", "iPhone only", "iPhone only", "Yes — system-wide"]
    - feature: "Account or sign-up required"
      values: ["No — no email, no Apple ID required", "Account required", "Account required", "Account required", "Apple ID (system-level)"]
    - feature: "Third-party tracking SDKs"
      values: ["None — Data Not Collected (Apple-verified)", "Multiple — analytics & ads", "Some — analytics", "Some — analytics", "Apple only"]
    - feature: "Daily emergency unlock"
      values: ["Yes — 1/day, math-gated (real arithmetic)", "Yes — tap a button", "Tap-through after pause", "Tap-through after pause", "Requires passcode"]
  footnote: "Verified 2026-05-22 against each app's public App Store page, developer landing page, and pricing / help documentation. Competitor offerings change frequently — re-verify before switching. Mechanism descriptions are based on each app's own published documentation."

screenshots:
  - src: "/assets/screenshots/earnlock/1.png"
    alt: "EarnLock home screen on iPhone — large progress ring at 1,974 steps with \"Earn 2,026 more steps to unlock\" beneath, and the Locked apps grid showing X, Instagram, Facebook, Discord, LinkedIn, TikTok, WhatsApp, Snapchat, and YouTube each marked with a lock badge"
  - src: "/assets/screenshots/earnlock/2.png"
    alt: "EarnLock home screen on iPhone after the goal is met — full green ring at 8,400 steps with \"All apps unlocked until midnight ✓\", and a Shadow Mode card reading \"Day 2 of 7 — You would have lost access 4 times today\""
  - src: "/assets/screenshots/earnlock/3.png"
    alt: "EarnLock Insights screen on iPhone — Month tab selected, May 2026 calendar heatmap of goal-met days, Total earned 187,600 steps, Best week (Week 3) at 64,800 steps"
  - src: "/assets/screenshots/earnlock/4.png"
    alt: "EarnLock Change goal sheet on iPhone — unit picker with Steps selected (Active minutes and Active calories also available), preset cards for Light 4,000 steps, Standard 8,000 steps, Challenge 12,000 steps, and a Custom 8,000 steps option, with a Save goal button"
  - src: "/assets/screenshots/earnlock/5.png"
    alt: "EarnLock Shadow Week graduation screen on iPhone — \"Your shadow week is done — Ready to actually block? Your data shows you'd save ~30m/day\", with stats \"23 times you'd have been blocked this week\" and \"~30m estimated time saved per day\", and an Enable real blocking button"
  - src: "/assets/screenshots/earnlock/6.png"
    alt: "EarnLock Choose Activities picker on iPhone — Apple's Family Controls list with Discord, Facebook, Instagram, LinkedIn, and Snapchat selected, plus All Apps & Categories and Social grouped at the top"
  - src: "/assets/screenshots/earnlock/7.png"
    alt: "EarnLock onboarding goal picker on iPhone — \"Pick your goal — How hard do you want to work for it?\" with three cards: Light 4,000 steps (≈ a 35-min walk), Standard 8,000 steps highlighted (≈ a 75-min walk), and Challenge 12,000 steps (≈ a 110-min walk)"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  app_privacy_label: "Data Not Collected — verified on the App Store for every release."
  notes:
    - "Zero third-party SDKs — no Firebase, Mixpanel, Amplitude, Segment, ad networks, or crash reporters"
    - "No account required — no email, no Apple ID sign-up, no sign-in screen"
    - "HealthKit data is read-only and never transmitted off the device"
    - "Family Controls hands EarnLock opaque tokens — iOS does not let EarnLock see which app you blocked"
    - "Family Controls authorized in `.individual` mode only — EarnLock is self-restriction software, never parental control"
    - "No EarnLock server, ever — there is no backend to leak"

faq:
  - q: "What is EarnLock?"
    a: "EarnLock is an iOS and Apple Watch app that locks distracting apps until you earn screen time by hitting a daily activity goal you set yourself. The free tier uses steps; Premium adds active minutes and active calories. Apple's Family Controls paints a custom shield with a live progress ring (\"3,412 steps until unlock\") over every blocked app. Live Activities, lock-screen widgets, the Apple Watch app, and complications all surface the count. Streaks, rest days, a math-gated emergency unlock, most-attempted-blocked-app insights, a screen-time-saved estimate, and a reflection log are all included. No account, no analytics SDK, no server. Free; Premium $1.99/month or $9.99/year — both with a 7-day free trial — or $19.99 lifetime. Every paid tier (Monthly, Yearly, Lifetime) is Family Sharing eligible."
  - q: "How is EarnLock different from Opal, one sec, ScreenZen, or Forest?"
    a: "Four things. (1) The unlock cost is real — body movement measured by Apple Health, not a tap-through or a wait-out timer. (2) The shield over each blocked app shows a live progress ring with the exact number you have left, not Apple's generic restriction screen. (3) The Apple Watch is a first-class surface — count on the wrist, complications on every watch face — so the system works during a walk or run without the iPhone. (4) Pricing — $19.99 lifetime versus Opal's subscription-only ($7.99–$11.99/mo), ScreenZen Premium (~$60/yr), or Brick's $59 hardware + app. No account is required for any of EarnLock's features."
  - q: "Which apps can EarnLock block?"
    a: "Any iOS app, and any of Apple's categories (Social Networking, Entertainment, Games, etc.). You pick from Apple's system Family Controls picker — iOS hands EarnLock opaque tokens, so even EarnLock cannot see the names of the apps you chose. The shield renders for every app in your selection across the entire device, including Safari opens of the same domain when you select \"All web content\" in the picker."
  - q: "How does the activity goal work?"
    a: "You set a daily goal: steps (free tier), active minutes (Premium), or active energy in kcal (Premium). EarnLock reads HealthKit on-device and tracks your progress. When you cross the threshold, every shielded app unlocks for the rest of the calendar day. With Premium, partial progress earns a partial-time window — 60% of your goal buys 60% of the unlock window — so an imperfect day still has some payoff. Goals reset at local midnight."
  - q: "Does EarnLock work on Apple Watch without the iPhone?"
    a: "Yes. The Watch app reads HealthKit on the Watch directly, so the count runs during long walks, runs, and gym sessions without the iPhone. Complications mount on modular, circular, corner, and graphic faces. When the Watch crosses the goal, the iPhone's shields drop within seconds via WatchConnectivity."
  - q: "What if I genuinely need to use a blocked app for something urgent?"
    a: "EarnLock includes one emergency unlock per day. Triggering it requires solving a real arithmetic problem — not a four-digit PIN you set thirty seconds ago. The math is hard enough to defeat impulse, not so hard it defeats actual need. After you use it, the next emergency unlock isn't available until local midnight. We don't ship a higher cap because the whole point of the friction is that it's friction."
  - q: "What about streaks and rest days?"
    a: "Daily goal-met days build a streak. One rest day per week protects the streak so a planned recovery day (or a sick day, or a travel day) doesn't reset it. EarnLock never sends a notification shaming you for missing a day, never threatens to break your streak, and never compares your streak to anyone else's. Streak data is local-only — if you delete the app, the streak is gone with it."
  - q: "Is EarnLock free? What does Premium unlock?"
    a: "Core blocking with a steps-based daily goal is free forever — including the custom shield, the Apple Watch app + complication, Live Activities, widgets, the math-gated emergency unlock, streaks, and rest days. Premium unlocks the active-minutes and active-energy goals, partial-progress windows, schedule profiles (weekday / weekend), most-attempted-blocked-app insights, the screen-time-saved estimate, and the reflection log. Premium is $1.99/month or $9.99/year — both with a 7-day free trial — or $19.99 lifetime. Every paid tier (Monthly, Yearly, Lifetime) is Family Sharing eligible: one purchase covers up to 5 family members at no extra cost."
  - q: "Does EarnLock collect any data?"
    a: "No. EarnLock has no account, no server, no analytics SDK, no advertising SDK, no third-party SDKs of any kind. HealthKit data is read on-device only and never transmitted off the device. The Family Controls picker hands EarnLock opaque tokens, so even EarnLock cannot tell which specific apps you chose to block. Apple's App Privacy nutrition label on the App Store shows \"Data Not Collected\" for every EarnLock release. See the full privacy policy for the line-by-line breakdown."
  - q: "Can EarnLock be used as parental control?"
    a: "No. EarnLock authorizes Apple's Family Controls in the `.individual` mode only — self-restriction by the device owner. It never enables the `.child` mode used for managing a Family Sharing minor, and it has no parent-side dashboard, no remote unlock, and no PIN that a parent sets. If you need parental controls, use iOS Settings → Screen Time → Family Sharing; that's what Apple's own tools are designed for."
  - q: "What devices does EarnLock support?"
    a: "iPhone running iOS 17 or later, and Apple Watch running watchOS 10 or later. The shield, Live Activities, widgets, and Family Controls require iOS 17+ (Family Controls is iOS-only — there is no iPadOS or macOS version, because Apple's Family Controls framework does not ship on those platforms in a way that supports this app's mechanic)."
  - q: "Does EarnLock support Family Sharing?"
    a: "Yes — every paid tier. Monthly, Yearly, and Lifetime are all Family Sharing eligible, so one purchase by the family organizer covers up to 5 family members at no extra cost. After buying, set EarnLock to share in iOS Settings → your name → Family Sharing → Subscriptions / Purchases; each family member then sees EarnLock as available in their App Store account and can download it on their own devices. The activity data, blocked-app selection, and streak history stay local to each person's device — Family Sharing handles the billing entitlement only, never your personal data."
  - q: "Does the lifetime price ever change?"
    a: "Lifetime is a flat $19.99 — now and going forward. We're not planning a price increase. If that ever changes, the new price will be visible in the App Store and the in-app paywall before you confirm; existing Lifetime owners are never re-billed."
  - q: "How accurate is the screen-time-saved estimate?"
    a: "It's a conservative estimate computed locally from your iOS Screen Time data for the apps you've shielded with EarnLock. We take your trailing 14-day average daily use of each blocked app, multiply by the number of days the app was shielded and the goal was not met that day, and discount by 40% to avoid overclaiming (some of the saved time would have been replaced by another app, not by activity). The methodology is published, and the estimate is shown next to a footnote that says exactly what we discounted and why."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/earnlock/support/"

release:
  first_release: "2026-05-22"
  last_updated: "2026-05-22"

ratings:
  value: ""
  count: 0
  last_synced: "2026-05-22"
  display_label: "New release"
---
EarnLock is an iOS and Apple Watch app that locks distracting apps until you earn screen time by hitting a daily activity goal — steps in the free tier, active minutes or active energy in Premium. Apple's Family Controls renders a custom shield with a live progress ring (\"3,412 steps until unlock\") over every blocked app, so you always know how far you are from the threshold. Apple Watch is a first-class surface: the Watch app reads HealthKit directly and complications mount on every watch face style, so the count keeps running on long walks, runs, and gym sessions without the iPhone. Live Activities and lock-screen widgets keep the same count visible everywhere else. Streaks build on consecutive goal-met days; one rest day per week protects the streak. A math-gated emergency unlock (1/day) handles genuine emergencies without becoming the default escape hatch. Premium adds partial-progress unlock windows, schedule profiles (weekday / weekend), most-attempted-blocked-app insights, a conservative screen-time-saved estimate with published methodology, and a 20-second reflection log when the apps unlock for the day. 39 locales out of the box including Arabic and Hebrew (RTL). No account, no analytics SDK, no advertising SDK, no third-party SDKs of any kind — and no EarnLock server, ever. HealthKit is read on-device only and never leaves the device; Family Controls hands EarnLock opaque tokens so iOS itself prevents EarnLock from seeing which apps you blocked. Apple's App Privacy nutrition label reads \"Data Not Collected\" for every release. Free; Premium $1.99/month or $9.99/year (both with a 7-day free trial), or $19.99 lifetime. Every paid tier — Monthly, Yearly, and Lifetime — is Family Sharing eligible, covering up to 5 family members at no extra cost. Cheapest lifetime tier among major screen-time blockers. iOS 17+ and watchOS 10+. Self-restriction only — never parental control.
