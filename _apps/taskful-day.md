---
layout: app
slug: taskful-day
name: "Taskful Day"
tagline: "A day planner where unfinished tasks move on without guilt."
quick_answer: "Taskful Day is a day planner for iPhone, iPad, Mac, and Apple Watch. Unfinished tasks carry forward to today on their own, so the Today list never turns into a red overdue pile, and you can add a task by typing a sentence, speaking it, asking Siri, or using your watch. The free version lets you create up to 50 tasks in total. Pro ({P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once) adds unlimited tasks, iCloud sync, the Day Clock, Energy River, and Day Map views, and 21 Home Screen widgets, and every new install gets 7 days of Pro free with no card. There is no account to create, and the app has no ads or tracking."
category: productivity
status: live

app_store_url: "https://apps.apple.com/app/id6757345400"

price:
  model: freemium
price_tier: "Pro"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew."

plans:
  - name: "Free"
    price: "$0"
    summary: "The planner, for up to 50 tasks in total. Every new install starts with 7 days of Pro, no card needed."
    features:
      - "Create up to 50 tasks (a lifetime total: deleting tasks doesn't reset it)"
      - "Type-a-sentence capture, the Inbox, Siri, and voice capture on iPhone and iPad"
      - "Automatic carry-forward, recurring tasks, and reminders you can snooze"
      - "Journal and the weekly Analytics view"
      - "3 Lock Screen widgets and the Control Center capture button"
      - "Apple Watch: Now, Today, Tomorrow, and capture from your wrist"
      - "One workspace and 5 themes"
  - name: "Pro · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "All of Pro, billed monthly."
    features:
      - "Unlimited tasks, workspaces, checklist steps, and check-ins"
      - "Day Clock, Energy River, Day Map, and the Schedule week grid"
      - "The Focus Mode timer, with a Live Activity on iPhone"
      - "21 Home Screen widgets, up to a full page on iOS 27"
      - "iCloud Sync through your own private iCloud"
      - "Monthly, quarterly, and yearly Analytics, plus 10 more themes"
      - "Re-import from Apple Reminders whenever you like"
  - name: "Pro · Annual"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "Same Pro features, billed once a year. ~{SAVE_YEARLY}% cheaper than paying monthly."
    features:
      - "Everything in Pro · Monthly"
      - "~{SAVE_YEARLY}% cheaper than monthly over a year"
      - "Cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All Pro features for one payment."
    features:
      - "Everything in Pro · Annual"
      - "One-time purchase, no renewal"

icon: "/assets/icons/taskful-day.png"
og_image: "/assets/og/taskful-day.png"

seo:
  title: "Taskful Day: Calm Day Planner for iPhone, iPad & Mac"
  description: "Day planner for iPhone, iPad, Mac, and Apple Watch. Unfinished tasks carry forward on their own. 21 widgets, no account. Try Pro free for 7 days."
  keywords:
    - daily planner app
    - daily planner Mac
    - to do list Mac
    - Mac productivity app
    - macOS planner app
    - calm to do list
    - daily task planner
    - focus planner app
    - daily schedule planner
    - task manager iPhone
    - daily planner iPad
    - to do list iPad
    - iPad productivity app
    - productivity planner
    - ADHD planner app
    - daily organizer app
    - focus timer planner
    - guilt-free to do list
    - mindful productivity app
    - iCloud sync planner
    - cross-platform planner Apple
    - apple watch to do list
    - time blocking app

hero:
  pre_headline: "A day planner for iPhone, iPad, Mac, and Apple Watch."
  headline: "What you don't finish today is waiting on tomorrow's list."
  secondary: "Unfinished tasks carry forward on their own, and the Today list shows no overdue badge. Free to download, with 7 days of Pro on every new install and no card needed."
  subheadline: "Type a task the way you'd say it and Taskful Day picks out the date, time, and priority. With Pro, see the day as a 24-hour clock, a river of time, or a map, block out the week on a grid, and keep it all in front of you with 21 Home Screen widgets."
  cta_label: "Download Free"
  alt: "Taskful Day today's plan view on iPhone with a focus session running"

who_for:
  - "Unfinished lists leave you feeling behind, and you want leftover tasks to move to today without a red overdue pile"
  - "You plan around time and like to see the day as a clock or a timeline, or to block out the week on a grid"
  - "You capture on the go: a typed sentence, your voice, Siri, Control Center, or your Apple Watch"
  - "You plan at your Mac and check the day on your iPhone, iPad, or watch"
  - "You want your planner on the Home Screen, not buried in an app"
  - "You'd rather not create an account, and you want your tasks on your device or in your own iCloud"

who_not_for:
  - "You manage team projects and need shared lists with assignees"
  - "You run a GTD system built on tags, contexts, and nested projects"
  - "You want Kanban boards, Gantt charts, or dependency graphs"
  - "You need two-way sync with Apple Calendar or Reminders (Taskful Day shows Calendar events read-only and imports Reminders one way)"
  - "You need Android or a web app"

alternatives_to:
  - "Streaks"
  - "Habitica"
  - "Productive"
  - "Way of Life"
  - "HabitNow"
  - "Things 3"
  - "TickTick"
  - "Todoist"
  - "Structured"
  - "Sorted³"

comparison_table:
  intro: "Each row below answers a question people ask when shopping for a day planner. Streaks, Things 3, TickTick, and Structured each do something well. Taskful Day fits if you want one day at a time, leftover tasks that move forward on their own, and one app for iPhone, iPad, Mac, and Apple Watch."
  competitors: ["Taskful Day", "Streaks", "Things 3", "TickTick", "Structured"]
  rows:
    - feature: "Single-day focus (no infinite backlog)"
      values: ["Yes, built around today", "Habits only", "No, multi-project", "No, multi-project", "Yes, timeline-first"]
    - feature: "Streaks at the center of the app"
      values: ["No, a streak is one stat in Analytics", "Yes, streaks are the product", "No", "Badges and achievements", "No"]
    - feature: "Built-in focus timer"
      values: ["Yes, Focus Mode (Pro)", "No", "No", "Yes, Premium tier", "Yes"]
    - feature: "On iPhone, iPad, AND Mac"
      values: ["Yes, plus an Apple Watch app", "iOS / iPad / Watch", "Separate purchase per platform", "Cross-platform via account", "iOS + macOS Catalyst"]
    - feature: "One-time lifetime purchase option"
      values: ["{P_LIFETIME} lifetime", "One-time purchase (iOS)", "One-time purchase per platform", "Subscription only", "Subscription, one-time also available"]
    - feature: "No account required"
      values: ["Yes, optional sync through your own iCloud (Pro)", "Yes", "Yes, iCloud sync", "Account required", "Account required for sync"]
    - feature: "Third-party tracking or analytics SDKs"
      values: ["None", "See its App Store privacy label", "See its App Store privacy label", "See its App Store privacy label", "See its App Store privacy label"]
  footnote: "Competitor pricing and features reflect each app's public landing page and App Store description on 2026-05. Apps change often, so check current pricing on the App Store before switching."

value_points:
  - title: "Leftovers move on by themselves"
    description: "When you open Taskful Day on a new day, yesterday's unfinished tasks are already on today's list. The original date is kept for your Analytics, and the Today list shows no overdue badge. One switch in Settings turns it off."
  - title: "Capture it the way you think it"
    description: "Type \"dentist tomorrow 3pm high priority\" and the date, time, and priority land in their fields. The keyword rules understand 8 languages. Speak a task on iPhone or iPad, ask Siri, tap the Control Center button, or dictate on your watch."
  - title: "See the day, then plan the week"
    description: "With Pro, the Day Clock lays your tasks around a 24-hour dial, Energy River draws the day as a flowing timeline, and Day Map shows where the day is crowded. The Schedule grid lets you drag tasks across a week of hours, with your Apple Calendar events shown beside them."
  - title: "Private by design"
    description: "There's no account and no Lagerland server. The app carries no analytics or third-party SDKs. Your tasks stay on the device unless you turn on iCloud Sync, which uses your own private iCloud."

how_it_works:
  intro: "Taskful Day plans one day at a time and moves whatever is left to the next one. This is how a day moves through it."
  steps:
    - title: "Capture it in one line"
      detail: "Type a sentence in the Add a task bar and Taskful Day picks out the date, time, priority, and category. Write \"Groceries: milk, eggs, bread\" and you get a checklist. For a thought you can't place yet, use the Inbox: it needs no fields, and you pick Today, Tomorrow, or Later when you're ready."
    - title: "Shape today"
      detail: "Add a duration, a category, notes, a repeat rule, or a reminder when you want one. Group the Today list by time of day or by category, and drag pending tasks into the order you'll do them."
    - title: "See how the day fits (Pro)"
      detail: "Swipe from the list to the Day Clock, Energy River, or Day Map. Energy River estimates the shape of your day from the tasks you scheduled; it doesn't measure your body. For the week ahead, the Schedule grid lets you move tasks between hours and days."
    - title: "Work on one thing"
      detail: "Open any task in Focus Mode to see it on its own, with its checklist steps and a few related tasks around it. With Pro, start a 10, 25, or 45 minute timer, or set your own between 5 and 120 minutes. On iPhone, follow it on the Lock Screen and in the Dynamic Island."
    - title: "Note how the day felt"
      detail: "In the Journal, pick Great, Good, Neutral, or Stressed and add a note if you like. The entry sits next to a summary of what you completed, what's still pending, and your focus time."
    - title: "Let the rest carry forward"
      detail: "Anything unfinished moves to today the next time you open the app. Recurring tasks keep their rhythm when they carry over. You can also carry tasks forward by hand from a past day, or select several and move them at once."
    - title: "Look back without a verdict"
      detail: "Analytics shows your completion rate, trends, and categories for the week, with longer ranges in Pro. Its footer says it plainly: \"This is just a pattern, not a judgment.\""

features:
  - title: "Natural-language capture"
    description: "Type it like you'd say it, and Taskful Day finds the date, time, and priority while keeping the title clean. Keyword rules cover English, German, French, Spanish, Italian, Portuguese, Swedish, and Finnish. Voice capture on iPhone and iPad shows you the parsed task before it's saved."
  - title: "Carry forward"
    description: "Unfinished tasks move to today automatically, on by default, with a switch in Settings and a per-task toggle. Batch \"Move to Today\" and a five-second Undo cover the rest."
  - title: "Day Clock, Energy River, and Day Map"
    description: "Three Pro views of the same day: a 24-hour dial with a Now hand, a flowing timeline with a full-screen landscape view on iPhone, and a map in Regions, Heatmap, or Day-part mode."
  - title: "Schedule week grid"
    description: "With Pro, <a href=\"https://en.wikipedia.org/wiki/Timeboxing\" rel=\"noopener\" target=\"_blank\">time-block</a> your week on a 7-day grid. Drag a task to move it, and each block's height follows its duration. Apple Calendar events can sit beside your tasks, read-only, and overlaps are flagged."
  - title: "Focus Mode"
    description: "One task on screen, its checklist steps, and related tasks orbiting around it. Pro adds the timer and a Live Activity on iPhone, with +5 min and End buttons on the Lock Screen and in the Dynamic Island."
  - title: "21 Home Screen widgets"
    description: "Next Task, Today's Tasks, Now & Next, From Earlier, Year in Squares, Month, Hours, and more, with Pro. Tick tasks off or carry them forward right from the widget. Six kinds fill a whole page on iOS 27, and eight come in extra-large on iPad. The three Lock Screen widgets are free."
  - title: "Apple Watch"
    description: "See Now, Today, and Tomorrow, swipe to complete or snooze, and dictate a new task with the same parser as the phone. The watch app needs the iPhone app installed. Pro adds Inbox triage, the workspace switcher, and two more complications."
  - title: "iPad and Mac"
    description: "On iPad, a three-zone layout with a sidebar, a month calendar, and multiple windows. On the Mac, a toolbar, menus, keyboard shortcuts like ⌘N for a new task, right-click menus, and widgets on the desktop. Voice capture is iPhone and iPad only."

screenshots:
  - src: "/assets/screenshots/taskful-day/1.webp"
    alt: "Taskful Day today view with a week strip and pending tasks"
  - src: "/assets/screenshots/taskful-day/2.webp"
    alt: "Taskful Day clock view with tasks around a 24-hour dial"
  - src: "/assets/screenshots/taskful-day/3.webp"
    alt: "Taskful Day energy river chart across the day"
  - src: "/assets/screenshots/taskful-day/4.webp"
    alt: "Taskful Day map view grouping tasks by category region"
  - src: "/assets/screenshots/taskful-day/5.webp"
    alt: "Taskful Day heatmap of tasks by hour and category"
  - src: "/assets/screenshots/taskful-day/6.webp"
    alt: "Taskful Day day-part map of morning, afternoon and evening tasks"
  - src: "/assets/screenshots/taskful-day/7.webp"
    alt: "Taskful Day weekly schedule with task blocks"
  - src: "/assets/screenshots/taskful-day/8.webp"
    alt: "Taskful Day heatmap widget with active days and a today list"
  - src: "/assets/screenshots/taskful-day/9.webp"
    alt: "Taskful Day habits widget with streaks and a pattern"
  - src: "/assets/screenshots/taskful-day/10.webp"
    alt: "Taskful Day full-page widget with the next tasks"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No account, no ads, and no analytics or third-party SDKs"
    - "Tasks stay on your device unless you turn on iCloud Sync (Pro), which uses your own private iCloud"
    - "Voice capture runs on the device when your language supports it; otherwise audio goes to Apple's speech service only if you allow it"
    - "Calendar events are read for display only and never stored or synced"
    - "Export My Data and Delete All My Data are in Settings"

faq:
  - q: "What is Taskful Day?"
    a: "Taskful Day is a day planner and to-do list for iPhone, iPad, Mac, and Apple Watch. You plan one day at a time, unfinished tasks carry forward to the next day on their own, and you can add tasks by typing a sentence, speaking, asking Siri, or using your watch. Pro adds visual day views, a time-block week grid, a focus timer, 21 Home Screen widgets, and iCloud sync."
  - q: "Is Taskful Day available on Mac?"
    a: "Yes. Taskful Day runs on Mac with macOS 14 or later, with its own toolbar, menus, keyboard shortcuts, right-click menus, multiple windows, and desktop widgets. Voice capture and Lock Screen widgets stay on iPhone and iPad, and the focus Live Activity on iPhone. With Pro, iCloud Sync keeps your Mac and your other devices on the same plan."
  - q: "Is the Mac version a separate purchase?"
    a: "No. Taskful Day is a single App Store app that runs on iPhone, iPad, and Mac, and it's free to download on each."
  - q: "Does Taskful Day sync between iPhone, iPad, and Mac?"
    a: "Yes, with Pro. iCloud Sync is optional and runs through your own private iCloud, so tasks, checklists, reminders, workspaces, the Inbox, and your Journal stay in step across your devices. Taskful Day has no server of its own. Turning sync on or off takes an app restart."
  - q: "Is Taskful Day good for ADHD?"
    a: "Taskful Day isn't an ADHD tool or a medical product, but parts of its design may help if long lists overwhelm you. Unfinished tasks carry forward on their own, and the Today list shows no overdue badge. You can drop a thought into the Inbox and decide later when it happens. Focus Mode puts one task on screen at a time, and Pro adds a timer. The 7 free days of Pro on every new install let you try all of it first, with no card."
  - q: "Does Taskful Day work on Apple Watch?"
    a: "Yes. The Apple Watch app shows Now, Today, and Tomorrow, lets you complete or snooze tasks with a swipe, and captures new tasks by dictation or Scribble. It needs the iPhone app installed. Inbox triage, the workspace switcher, and the Carried Forward and Journal Streak complications are Pro; the Today complication is free."
  - q: "How is Taskful Day different from other to-do apps?"
    a: "Most to-do apps keep a growing backlog and mark what you missed. Taskful Day plans one day at a time, moves unfinished tasks to today automatically, and shows no overdue badge on the Today list. It also lets you see the day as a clock, a timeline, or a map, and works across iPhone, iPad, Mac, and Apple Watch without an account."
  - q: "Does Taskful Day have a focus timer?"
    a: "Yes, with Pro. Focus Mode shows one task with its checklist steps, and Pro adds a timer of 10, 25, or 45 minutes, or anything from 5 to 120. On iPhone the countdown also runs as a Live Activity on the Lock Screen and in the Dynamic Island."
  - q: "Is Taskful Day free?"
    a: "Taskful Day is free to download, and every new install gets 7 days of Pro with no card needed. After that, the free version lets you create up to 50 tasks in total, with one workspace. Pro adds unlimited tasks, iCloud Sync, the visual day views, the week grid, the focus timer, and 21 Home Screen widgets for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once. Prices in USD; the App Store shows your local currency at checkout."
  - q: "What happens when the 7 free days of Pro end?"
    a: "Your tasks stay. Pro themes switch back to System, and the free limits apply: 50 tasks in total, one workspace, one checklist step per task, and one active check-in. The free week starts on its own when onboarding ends. It is not an App Store subscription trial, and it never asks for payment details."
  - q: "Does Taskful Day track or sell my data?"
    a: "No. There's no account, no ads, and no analytics or third-party SDKs, and Taskful Day has no server of its own. Your data stays on the device, or in your own private iCloud if you turn on iCloud Sync."
  - q: "Can I import tasks from Apple Reminders?"
    a: "Yes. Taskful Day imports your incomplete reminders once, one way, skips duplicates, and turns bullet notes into checklist steps. On the free version the first import counts toward the 50-task total and shows how many reminders wait for Pro. Pro imports everything and can import again later."
  - q: "Does it work on iPad?"
    a: "Yes. On iPad, Taskful Day has a three-zone layout with a sidebar, a month calendar, and room for multiple windows, and eight of its widgets come in extra-large. It runs on iPadOS 17.6 or later."
  - q: "Can I export my data?"
    a: "Yes. Settings has Export My Data, which saves your tasks with their notes and checklist steps as a JSON file, and Delete All My Data, which erases everything."
  - q: "What macOS version does Taskful Day support?"
    a: "Taskful Day needs macOS 14 or later on the Mac, iOS 17.6 or later on iPhone, and iPadOS 17.6 or later on iPad. The Apple Watch app needs watchOS 10.6 or later."

related_journal:
  slug: planning-on-phone-finishing-on-desk
  anchor: "The day I plan on my phone is not the day I finish at my desk"

support:
  email: "support@lagerland.app"
  url: "/apps/taskful-day/support/"

release:
  first_release: "2026-01-01"
  last_updated: "2026-04-29"
  mac_first_release: "2026-04-29"

ratings:
  value: "5.0"
  count: 4
  last_synced: "2026-06-03"
last_updated: 2026-10-30
---
Taskful Day is a day planner for iPhone, iPad, Mac, and Apple Watch. You plan one day at a time, and whatever you don't finish moves to the next day on its own. Add tasks by typing a sentence, speaking, asking Siri, or using your watch. With Pro, see the day as a clock, a timeline, or a map, block out the week on a grid, and keep it on your Home Screen with 21 widgets. There's no account to create, and your tasks stay on your device or in your own iCloud.
