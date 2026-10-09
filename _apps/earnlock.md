---
layout: app
slug: earnlock
name: "EarnLock"
tagline: "Earn your screen time. Move, then scroll."
quick_answer: "EarnLock is an iOS and Apple Watch app that locks distracting apps — Instagram, TikTok, X, Reddit, YouTube, anything you choose — until you earn your screen time by hitting a daily activity goal you set yourself. The free tier locks one app and unlocks it via daily steps; Premium adds unlimited apps, active minutes, and active energy. Apple's Family Controls renders a custom shield with a live progress ring (\"3,412 steps until unlock\") over each blocked app. Widgets keep the count visible, and Premium adds a Live Activity plus the Apple Watch app and complications, which read Apple Health directly so the count works without the iPhone. Streaks, rest days, a math-gated emergency unlock (1/day), most-attempted-blocked-app insights, a screen-time-saved estimate, and a reflection log are all built in. 39 locales (incl. 2 RTL), no account, no analytics SDK, no server. Free; Premium $1.99/month, $9.99/year (with a 7-day free trial), or $19.99 lifetime. Every paid tier — Monthly, Yearly, and Lifetime — is Family Sharing eligible: one purchase covers up to 5 family members at no extra cost."
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
    summary: "One blocked app with steps-based unlocks, free forever. No trial, no card, no account."
    features:
      - "Block one app or one category via Apple's Family Controls picker"
      - "Steps-based daily goal — when you cross it, your apps unlock"
      - "Partial unlocks — from 50% of your goal, a timed window (progress × 120 min) opens"
      - "Custom shield with live progress ring on every blocked app"
      - "Lock Screen and Home Screen widgets keep the count visible"
      - "Math-gated emergency unlock — once per day, real friction"
      - "Streak engine + weekly rest day"
      - "Shadow Week, today's insights (most-attempted app, time-saved estimate), one-tap reflection"
      - "On-device only — no account, no server, no analytics SDK"
  - name: "Premium · Monthly"
    price: "$1.99/mo"
    summary: "Full Premium, billed monthly. Cancel anytime."
    features:
      - "Unlimited blocked apps and categories"
      - "Active minutes goal (HealthKit Exercise Time) — better for runners and gym sessions"
      - "Active energy goal (kcal) — better for high-intensity training"
      - "Apple Watch app + complications — count on the wrist, no iPhone needed"
      - "Live Activity + Dynamic Island countdown"
      - "Week + Month insights — goal-met heatmap, totals, best week"
      - "Reflection log — your one-tap reflections, broken down month by month"
      - "Smart Schedules — a different goal tier (or blocking off) for work hours, evenings, weekends, sleep"
      - "Streak shields — every 7th day at 150% of your goal banks one (up to 3)"
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

spotlight:
  overline: "What makes EarnLock different"
  heading: "For the first week, EarnLock doesn't block anything. It watches."
  lead: "Most screen-time blockers ask you to set the rules on day one — pick the apps, set the goal, ship. The problem: you don't know which apps you actually overuse, and you don't know what step goal is realistic for you. So you guess, and the wall is either too strict (you bounce on day two) or too loose (it does nothing). Shadow Week is how EarnLock answers that. For the first seven days, nothing is blocked. EarnLock just watches — when and how often you open the apps you picked. At the end of the week you see, in your own data, what real blocking would have cost: the number of block events you'd have hit and the estimated screen-time saved per day. Then real blocking starts — with the calibration you couldn't have made on day one. No other screen-time blocker on the App Store does this."
  stats:
    - value: "7 days"
      label: "Shadow window — no blocking, just observation"
    - value: "Your data"
      label: "Calibration uses your actual behaviour, not category defaults"
    - value: "One tap"
      label: "Start real blocking early if you're ready — otherwise it begins on its own after day 7"

hero:
  headline: "Block the doomscroll until you move."
  secondary: "Earn your screen time."
  subheadline: "EarnLock locks Instagram, TikTok, X, YouTube, Reddit — whatever you pick — until you hit a daily activity goal you set yourself. Steps in the free tier; active minutes or calories in Premium. The shield over each blocked app shows a live progress ring counting down (\"3,412 steps until unlock\"). The Apple Watch app keeps the count on your wrist when the iPhone isn't with you. No account. No analytics SDK. No server. $19.99 lifetime."
  cta_label: "Download Free"
  cta_subline: "$19.99 lifetime · pay once, no subscriptions, no account."
  alt: "EarnLock home screen on iPhone showing 1,974 steps on a live progress ring with “Earn 2,026 more steps to unlock” beneath, and the Locked apps grid including Instagram and TikTok"

founder:
  overline: "Why we built this"
  heading: "Built by people who lost too many evenings to the feed."
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple studio · Finland"
  location: "Finland"
  photo: "/assets/icons/lagerland-mark.png"
  bio: "Every screen-time app we tried had the same flaw: the unlock cost nothing real. Tap \"give me another minute,\" tap \"emergency,\" tap a four-digit code you set thirty seconds ago. The friction is theatre. EarnLock makes the cost concrete — walk a kilometre, finish a 30-minute Exercise Time block, burn 400 active calories — and the apps unlock on their own. The shield over each blocked app shows you exactly how far you are from your daily goal. The Apple Watch carries the count when the iPhone isn't with you. There is no account, no server, no analytics SDK, no advertising SDK. Lagerland is a small Apple studio in Finland — no team, no investors. The studio's other 19 apps run on the same data discipline."
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails are answered personally, usually within a day."
  signals:
    - "100% on-device — no EarnLock server, ever (Apple's App Privacy nutrition label: Data Not Collected)"
    - "Zero third-party SDKs — no Firebase, Mixpanel, Amplitude, Segment, ad networks, or crash reporters"
    - "Family Controls authorized in `.individual` mode only — EarnLock is self-restriction software, never parental control"
    - "Lagerland's App Store catalogue is 20 privacy-first apps, all with the same data discipline"
  external_link:
    href: "/lagerland-apps/"
    label: "Read the Lagerland studio backstory →"

how_it_works:
  intro: "EarnLock turns Apple's Family Controls into a goal-gated lock. The rule is published below in full; the algorithm is transparent and runs entirely on your device."
  steps:
    - title: "Pick what to block, set today's goal"
      detail: "Open the Family Controls picker (Apple's system UI — EarnLock never sees the app names you pick; iOS hands us opaque tokens) and select the apps and categories to block — one on the free tier, as many as you like with Premium. Set your daily goal: steps in the free tier, or active minutes / active energy in Premium. Each unit has three presets — Light, Standard (the default), and Challenge: 4,000 / 8,000 / 12,000 steps, 20 / 30 / 45 active minutes, or 150 / 300 / 500 active kcal — plus a custom number, or Adaptive, which starts at Standard and adjusts itself nightly."
    - title: "EarnLock reads HealthKit and renders a live shield"
      detail: "EarnLock reads your HealthKit progress on-device — whenever you open it, and in the background when iOS delivers new Health data. When you open a blocked app, Apple's ManagedSettings framework calls EarnLock's ShieldConfiguration extension — we paint a custom shield over the app with a progress ring and plain text: \"3,412 steps until unlock\". With Premium, the Apple Watch app and complication show the same count without the iPhone, and a Live Activity keeps it on the lock screen; widgets keep it visible everywhere else."
    - title: "Cross the threshold, apps unlock for the day"
      detail: "When you hit 100% of your daily goal, every shielded app unlocks for the rest of the calendar day. Partial progress counts too, on every tier: from 50% of your goal a timed window opens — progress × 120 minutes, so an hour at 50% and 96 minutes at 80% — and the same share of your individually picked apps unlocks for it. Below 50%, everything stays locked. At local midnight, the shield resets. Streaks track consecutive goal-met days; rest days protect the streak when you genuinely need one. If something is on fire, the math-gated emergency unlock (1 per day cap) opens the apps for 15, 30, or 60 minutes after you solve a real arithmetic problem — no PIN, no four-digit recall."

value_points:
  - title: "Movement is the unlock — no PIN, no \"give me one more minute\""
    description: "Other screen-time apps unlock when you tap a button, recite a number, or wait out a timer. EarnLock unlocks when your body actually does the work — measured by Apple Health, not self-reported. The friction is real because the cost is real."
  - title: "Custom shield with a live progress ring"
    description: "Apple's Family Controls only renders a generic \"App Restricted\" shield by default. EarnLock ships a ShieldConfiguration extension that paints a circular progress ring with \"X steps until unlock\" copy live over every blocked app. You always know how close you are."
  - title: "Apple Watch — count on the wrist, complication on the face"
    description: "EarnLock's Watch app (Premium) reads HealthKit directly, so the count works on long walks, runs, and gym sessions without the iPhone. Native complications in circular, corner, inline, and rectangular styles put the count on your watch face, so a glance tells you whether the apps will be open when you sit back down."
  - title: "Cheapest lifetime among screen-time blockers"
    description: "$19.99 lifetime — versus Opal at $99.99/yr, ScreenZen which is free with optional tips, or Brick at $59 hardware. Free if one blocked app and a step goal are enough. Local-first by architecture, not just by policy."

features:
  - title: "Family Controls shield with a live progress ring"
    description: "EarnLock includes a ShieldConfiguration extension that replaces Apple's generic restriction screen with a custom shield showing a circular progress ring and the exact number you have left — \"3,412 steps until unlock\", \"18 min until unlock\", \"187 kcal until unlock\". The number is EarnLock's latest Apple Health reading; if that reading is more than 45 minutes old, the shield asks you to open EarnLock instead of showing a stale count. The shield's one button closes it — iOS doesn't let a shield open another app — and the next time you open EarnLock it lands on your goal screen, not a paywall."
  - title: "HealthKit-driven goal engine"
    description: "Steps (free), active minutes (Premium), or active energy (Premium). Goals reset at local midnight in your device timezone — not at a server UTC boundary. EarnLock reads HealthKit on-device only, never writes to Health, and never transmits the data off the device. You can revoke access in iOS Settings → Privacy & Security → Health → EarnLock at any time."
  - title: "Apple Watch app + complications"
    description: "Premium includes a Watch app that reads HealthKit on the Watch itself and shows your live progress ring against today's goal, how much is left to unlock (or how many minutes you've earned), and a Reflect button. Complications come in circular, corner, inline, and rectangular styles. Watch and iPhone share only your goal settings over WatchConnectivity, not activity counts — the iPhone's shields lift once the Watch's activity has synced into Apple Health on the phone."
  - title: "Live Activities + lock-screen widgets"
    description: "The Live Activity (Premium) puts the progress ring on the lock screen and in the Dynamic Island once you're within 20% of your goal, counts down a partial-unlock window, and counts down to midnight once you've unlocked. Lock-screen widgets show the same count at any time, and Home Screen widgets — free, in every size — mirror the state. None of it requires unlocking the phone."
  - title: "Streak engine + rest-day support"
    description: "Daily goal-met days build a streak. One rest day per week protects the streak so a planned recovery day doesn't reset it — that's a deliberate health choice, not a failure. EarnLock never sends a notification shaming you for missing a day. Streak data is local; if you delete the app, it's gone."
  - title: "Math-gated emergency unlock (1 per day cap)"
    description: "For genuine emergencies, EarnLock includes one emergency unlock per day. Triggering it requires solving a real arithmetic problem (not a four-digit PIN you set thirty seconds ago) — enough friction to defeat impulse, not enough to defeat actual need. Once used, the next emergency unlock isn't available until local midnight."
  - title: "Most-attempted-blocked-app insights + screen-time-saved estimate"
    description: "The Insights Day tab — free on every tier — shows which blocked app you tried to open most today while it was shielded, usually a humbling number. Next to it sits a screen-time-saved estimate: every shielded attempt counts as roughly 9 minutes of scrolling avoided, and the card is labelled as an estimate. iOS doesn't let apps read your real per-app Screen Time numbers, so EarnLock doesn't claim to measure them. Premium adds the Week and Month views — a heatmap of goal-met days, totals, and your best week."
  - title: "Reflection log"
    description: "Tap Reflect on the Home screen and EarnLock asks one question — \"What were you hoping to find?\" — answered with a single tap: Boredom, Anxiety, FOMO, Habit, or Other. The prompt is free, and entries are local-only and timestamped. Premium's Month view turns them into a log — how many reflections, your top reasons, a recap for each finished month — a quiet record of what actually pulls you back to the feed."
  - title: "Smart Schedules (work hours / evenings / weekends / sleep)"
    description: "Premium's Smart Schedules change the rules by time of day. Each schedule is a window on the days you choose that either swaps in a goal tier — Light, Standard, or Challenge — or switches blocking off. EarnLock starts you with four you can edit: Work hours (weekdays 9–5, Standard), Evenings (6–11 p.m., Light), Weekends (Light), and Sleep (11 p.m.–7 a.m., blocking off). Where two overlap, the shorter, more specific window wins."
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
  - "You can't or don't want to wear an iPhone / Apple Watch (activity is read from Apple Health only)"
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
      values: ["Yes (Premium) — reads HealthKit on the Watch", "iPhone only", "iPhone only", "iPhone only", "Yes — system-wide"]
    - feature: "Account or sign-up required"
      values: ["No — no email, no Apple ID required", "Account required", "Account required", "Account required", "Apple ID (system-level)"]
    - feature: "Third-party tracking SDKs"
      values: ["None — Data Not Collected (App Store privacy label)", "Multiple — analytics & ads", "Some — analytics", "Some — analytics", "Apple only"]
    - feature: "Daily emergency unlock"
      values: ["Yes — 1/day, math-gated (real arithmetic)", "Yes — tap a button", "Tap-through after pause", "Tap-through after pause", "Requires passcode"]
  footnote: "Verified 2026-05-22 against each app's public App Store page, developer landing page, and pricing / help documentation. Competitor offerings change frequently — re-verify before switching. Mechanism descriptions are based on each app's own published documentation."

screenshots:
  - src: "/assets/screenshots/earnlock/1.png"
    alt: "EarnLock home screen on iPhone — large progress ring at 1,974 steps with “Earn 2,026 more steps to unlock” beneath, and the Locked apps grid showing X, Instagram, Facebook, Discord, LinkedIn, TikTok, WhatsApp, Snapchat, and YouTube each marked with a lock badge"
  - src: "/assets/screenshots/earnlock/2.png"
    alt: "EarnLock home screen on iPhone after the goal is met — full green ring at 8,400 steps with “All apps unlocked until midnight ✓”, and a Shadow Mode card reading “Day 2 of 7 — You would have lost access 4 times today”"
  - src: "/assets/screenshots/earnlock/3.png"
    alt: "EarnLock Insights screen on iPhone — Month tab selected, May 2026 calendar heatmap of goal-met days, Total earned 187,600 steps, Best week (Week 3) at 64,800 steps"
  - src: "/assets/screenshots/earnlock/4.png"
    alt: "EarnLock Change goal sheet on iPhone — unit picker with Steps selected (Active minutes and Active calories also available), preset cards for Light 4,000 steps, Standard 8,000 steps, Challenge 12,000 steps, and a Custom 8,000 steps option, with a Save goal button"
  - src: "/assets/screenshots/earnlock/5.png"
    alt: "EarnLock Shadow Week graduation screen on iPhone — “Your shadow week is done — Ready to actually block? Your data shows you'd save ~30m/day”, with stats “23 times you'd have been blocked this week” and “~30m estimated time saved per day”, and an Enable real blocking button"
  - src: "/assets/screenshots/earnlock/6.png"
    alt: "EarnLock Choose Activities picker on iPhone — Apple's Family Controls list with Discord, Facebook, Instagram, LinkedIn, and Snapchat selected, plus All Apps & Categories and Social grouped at the top"
  - src: "/assets/screenshots/earnlock/7.png"
    alt: "EarnLock onboarding goal picker on iPhone — “Pick your goal — How hard do you want to work for it?” with three cards: Light 4,000 steps (≈ a 35-min walk), Standard 8,000 steps highlighted (≈ a 75-min walk), and Challenge 12,000 steps (≈ a 110-min walk)"

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
    a: "EarnLock is an iOS and Apple Watch app that locks distracting apps until you earn screen time by hitting a daily activity goal you set yourself. The free tier blocks one app with a steps goal; Premium adds unlimited apps, active minutes, and active calories. Apple's Family Controls paints a custom shield with a live progress ring (\"3,412 steps until unlock\") over every blocked app. Widgets, and in Premium the Live Activity, the Apple Watch app, and complications, all surface the count. Streaks, rest days, a math-gated emergency unlock, most-attempted-blocked-app insights, a screen-time-saved estimate, and a reflection log are all included. No account, no analytics SDK, no server. Free; Premium $1.99/month, $9.99/year (with a 7-day free trial), or $19.99 lifetime. Every paid tier (Monthly, Yearly, Lifetime) is Family Sharing eligible."
  - q: "How is EarnLock different from Opal, one sec, ScreenZen, or Forest?"
    a: "Four things. (1) The unlock cost is real — body movement measured by Apple Health, not a tap-through or a wait-out timer. (2) The shield over each blocked app shows a live progress ring with the exact number you have left, not Apple's generic restriction screen. (3) The Apple Watch is a first-class surface — count on the wrist, complications on the watch face — so the system works during a walk or run without the iPhone. (4) Pricing — $19.99 lifetime versus Opal's subscription-only ($7.99–$11.99/mo), ScreenZen (free, optional tips), or Brick's $59 hardware + app. No account is required for any of EarnLock's features."
  - q: "Which apps can EarnLock block?"
    a: "Any iOS app, and any of Apple's categories (Social Networking, Entertainment, Games, etc.) — one app or one category on the free tier, as many as you like with Premium. You pick from Apple's system Family Controls picker — iOS hands EarnLock opaque tokens, so even EarnLock cannot see the names of the apps you chose. The shield renders for every app in your selection across the entire device, and websites you add in the picker are shielded too."
  - q: "How does the activity goal work?"
    a: "You set a daily goal: steps (free tier), active minutes (Premium), or active energy in kcal (Premium). EarnLock reads HealthKit on-device and tracks your progress. When you cross the threshold, every shielded app unlocks for the rest of the calendar day. Partial progress pays too, on every tier: from 50% of your goal, a timed window of progress × 120 minutes opens (an hour at 50%, 96 minutes at 80%) and the same share of your individually picked apps unlocks for it — so an imperfect day still has some payoff. Below 50%, everything stays locked. Goals reset at local midnight."
  - q: "Does EarnLock work on Apple Watch without the iPhone?"
    a: "Yes, with Premium. The Watch app reads HealthKit on the Watch directly, so the count runs during long walks, runs, and gym sessions without the iPhone. Complications come in circular, corner, inline, and rectangular styles. The iPhone's shields lift once the Watch's activity has synced into Apple Health on the phone — the two share your goal settings over WatchConnectivity, not activity counts."
  - q: "What if I genuinely need to use a blocked app for something urgent?"
    a: "EarnLock includes one emergency unlock per day. Triggering it requires solving a real arithmetic problem — not a four-digit PIN you set thirty seconds ago. The math is hard enough to defeat impulse, not so hard it defeats actual need. After you use it, the next emergency unlock isn't available until local midnight. We don't ship a higher cap because the whole point of the friction is that it's friction."
  - q: "What about streaks and rest days?"
    a: "Daily goal-met days build a streak. You can pick one weekly rest day — a miss on that weekday never breaks the streak, so a planned recovery day doesn't reset it. For the unplanned ones — a sick day, a travel day — Premium adds streak shields: every 7th day you reach 150% of your goal banks one (up to 3), and a banked shield covers a missed day automatically. EarnLock never sends a notification shaming you for missing a day and never compares your streak to anyone else's; the one streak alert is an evening heads-up when a streak of three days or more is still exposed, and you can switch it off. Streak data is local-only — if you delete the app, the streak is gone with it."
  - q: "Is EarnLock free? What does Premium unlock?"
    a: "Blocking one app (or one category) with a steps-based daily goal is free forever — including the custom shield, partial unlocks from 50% of your goal, every widget, the math-gated emergency unlock, streaks with a weekly rest day, Shadow Week, today's insights (most-attempted app and the screen-time-saved estimate), and the one-tap reflection prompt. Premium unlocks unlimited blocked apps, the active-minutes and active-energy goals, the Apple Watch app + complications, the Live Activity, Smart Schedules, Week and Month insights, streak shields, the reflection log, and alternate app icons. Premium is $1.99/month, $9.99/year (with a 7-day free trial), or $19.99 lifetime. Every paid tier (Monthly, Yearly, Lifetime) is Family Sharing eligible: one purchase covers up to 5 family members at no extra cost."
  - q: "Does EarnLock collect any data?"
    a: "No. EarnLock has no account, no server, no analytics SDK, no advertising SDK, no third-party SDKs of any kind. HealthKit data is read on-device only and never transmitted off the device. The Family Controls picker hands EarnLock opaque tokens, so even EarnLock cannot tell which specific apps you chose to block. Apple's App Privacy nutrition label on the App Store shows \"Data Not Collected\" for every EarnLock release. See the full privacy policy for the line-by-line breakdown."
  - q: "Can EarnLock be used as parental control?"
    a: "No. EarnLock authorizes Apple's Family Controls in the `.individual` mode only — self-restriction by the device owner. It never enables the `.child` mode used for managing a Family Sharing minor, and it has no parent-side dashboard, no remote unlock, and no PIN that a parent sets. If you need parental controls, use iOS Settings → Screen Time → Family Sharing; that's what Apple's own tools are designed for."
  - q: "What devices does EarnLock support?"
    a: "iPhone running iOS 17 or later, and — for the Premium Watch app — Apple Watch running watchOS 10 or later. The shield, Live Activities, widgets, and Family Controls require iOS 17+ (Family Controls is iOS-only — there is no iPadOS or macOS version, because Apple's Family Controls framework does not ship on those platforms in a way that supports this app's mechanic)."
  - q: "Does EarnLock support Family Sharing?"
    a: "Yes — every paid tier. Monthly, Yearly, and Lifetime are all Family Sharing eligible, so one purchase by the family organizer covers up to 5 family members at no extra cost. After buying, set EarnLock to share in iOS Settings → your name → Family Sharing → Subscriptions / Purchases; each family member then sees EarnLock as available in their App Store account and can download it on their own devices. The activity data, blocked-app selection, and streak history stay local to each person's device — Family Sharing handles the billing entitlement only, never your personal data."
  - q: "Does the lifetime price ever change?"
    a: "Lifetime is a flat $19.99 — now and going forward. We're not planning a price increase. If that ever changes, the new price will be visible in the App Store and the in-app paywall before you confirm; existing Lifetime owners are never re-billed."
  - q: "How accurate is the screen-time-saved estimate?"
    a: "It's a deliberately simple, labelled estimate, not a measurement. iOS doesn't let apps read your real per-app Screen Time data, so EarnLock counts what it can observe on the device — each time the shield stops you opening a blocked app (repeat taps within 30 seconds count once) — and multiplies by an assumed 9 minutes per avoided open. Shadow Week's time-saved figure uses the same assumption, so the numbers never contradict each other."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/earnlock/support/"

release:
  first_release: "2026-05-22"
  last_updated: "2026-05-22"

related_journal:
  slug: "what-an-iphone-app-can-actually-block"
  anchor: "What an iPhone app can actually block - and what it never will"

ratings:
  value: ""
  count: 0
  last_synced: "2026-05-22"
  display_label: "New release"
---
EarnLock is an iOS and Apple Watch app that locks distracting apps until you earn screen time by hitting a daily activity goal — steps in the free tier, active minutes or active energy in Premium. Apple's Family Controls renders a custom shield with a live progress ring (\"3,412 steps until unlock\") over every blocked app, so you always know how far you are from the threshold. With Premium, Apple Watch is a first-class surface: the Watch app reads HealthKit directly and complications put the count on the watch face, so it keeps running on long walks, runs, and gym sessions without the iPhone. Widgets — and, in Premium, a Live Activity — keep the same count visible everywhere else. Partial progress pays too: from 50% of the goal, a timed window of progress × 120 minutes opens. Streaks build on consecutive goal-met days; one rest day per week protects the streak. A math-gated emergency unlock (1/day) handles genuine emergencies without becoming the default escape hatch. The free tier blocks one app and includes today's most-attempted-blocked-app card and a clearly labelled screen-time-saved estimate; Premium adds unlimited apps, Smart Schedules (work hours / evenings / weekends / sleep), Week and Month insights, streak shields, and a log of your one-tap reflections. 39 locales out of the box including Arabic and Hebrew (RTL). No account, no analytics SDK, no advertising SDK, no third-party SDKs of any kind — and no EarnLock server, ever. HealthKit is read on-device only and never leaves the device; Family Controls hands EarnLock opaque tokens so iOS itself prevents EarnLock from seeing which apps you blocked. Apple's App Privacy nutrition label reads \"Data Not Collected\" for every release. Free; Premium $1.99/month, $9.99/year (with a 7-day free trial), or $19.99 lifetime. Every paid tier — Monthly, Yearly, and Lifetime — is Family Sharing eligible, covering up to 5 family members at no extra cost. Cheapest lifetime tier among major screen-time blockers. iOS 17+ and watchOS 10+. Self-restriction only — never parental control.
