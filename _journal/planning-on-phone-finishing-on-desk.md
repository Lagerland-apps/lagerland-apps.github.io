---
layout: journal
slug: planning-on-phone-finishing-on-desk
title: "The day I plan on my phone is not the day I finish at my desk"
seo:
  title: "Why a Daily Planner Belongs on Your Mac, Too"
  description: "Why a daily planner has to run on the Mac where the work happens: Taskful Day on Mac, with menus, shortcuts, desktop widgets, and iCloud sync in Pro."
  keywords:
    - "mac daily planner"
    - "daily planner for iphone and mac"
    - "planner for macbook"
    - "mac to-do app"
    - "planner with icloud sync"
    - "taskful day"
date: 2026-05-02
last_updated: 2026-10-29
lede: "Taskful Day shipped on the Mac this week. This short essay explains why a daily planner has to run on the Mac where the work happens, what it took to make an iPad-born app behave like a Mac app you keep open all day, and why it is one app across iPhone, iPad, and Mac."
quick_answer: "Taskful Day runs on Mac (macOS 14 or later) as well as iPhone, iPad, and Apple Watch. On the Mac it is a Mac Catalyst app with its own toolbar, menus, keyboard shortcuts, right-click menus, multiple windows, and desktop widgets; voice capture stays on iPhone and iPad. It is one App Store app, free to download on each device. With Pro, sync runs through your own private iCloud; Taskful Day has no server of its own, so the studio stores no tasks."
faq:
  - q: "Is Taskful Day available on Mac?"
    a: "Yes. Taskful Day runs on Mac with macOS 14 or later, as well as on iPhone, iPad, and Apple Watch. On the Mac it is a Mac Catalyst app with a toolbar, menus, keyboard shortcuts such as ⌘N for a new task, right-click menus, multiple windows, and desktop widgets. Voice capture and Lock Screen widgets stay on iPhone and iPad, and the focus Live Activity on iPhone."
  - q: "Do I have to pay separately for Taskful Day on Mac?"
    a: "There is no separate Mac app to buy. Taskful Day is a single App Store app that runs on iPhone, iPad, and Mac, and it's free to download on each. Pro is {P_MONTHLY@taskful-day} a month, {P_YEARLY@taskful-day} a year, or {P_LIFETIME@taskful-day} once, and every new install gets 7 days of Pro free with no card."
  - q: "How does Taskful Day sync between iPhone, iPad, and Mac?"
    a: "With Pro, Taskful Day syncs through your own private iCloud. Tasks, checklists, reminders, workspaces, the Inbox, and your Journal stay in step across your devices. Taskful Day has no server of its own, so the studio stores no tasks. The trade-off is that there is no shared cloud space for team task lists."
  - q: "Is Taskful Day a replacement for Things 3, TickTick, or Sorted3?"
    a: "No. Things 3 is GTD-style with a long-lived project tree. TickTick is a cross-platform Swiss-army knife. Sorted3 is a strict time-blocked planner. Taskful Day is for one day at a time, and unfinished tasks carry forward to today on their own, with no overdue badge on the Today list."
mentioned_apps:
  - taskful-day
read_time: "5 min read"
excerpt: "Taskful Day now runs on the Mac alongside iPhone and iPad. This post explains why a planner has to live where the work happens, what it took to make a Mac Catalyst app behave like a Mac app you keep open all day, how sync through your own iCloud works, and where Taskful Day sits next to Things 3, TickTick, and Sorted³."
---

I do not plan my day on a phone in the kitchen and then carry the plan, unchanged, to a desk for eight hours.

Nobody does. The plan I make at the coffee maker has three tasks on it, and the day I'd like to have has nine. The work happens somewhere in between, and until this week my planner didn't run on the device I do that work on.

[Taskful Day](/apps/taskful-day/) shipped on the Mac on Wednesday. This Saturday essay is about why the Mac was the missing piece, and what it took to make the app feel at home there.

## Making it behave like a Mac app

For several years Apple has made it easy to bring an iPad app to the Mac with Mac Catalyst. You tick a checkbox in Xcode, set a few capabilities, fix the obvious touch-target sins, and ship. A lot of indie planners and to-do apps reach the Mac this way, and the lazy version is an iPad window with a menu bar.

That is fine for an app you open once and dismiss, like a calculator. It isn't fine for an app you keep open in a corner of the screen for eight hours, next to Slack, your calendar, and the document you're trying to finish. If the keyboard shortcuts feel pasted on and the window doesn't act like a Mac window, you notice it all day.

Taskful Day on Mac is a Catalyst app built with Apple's "Optimize for Mac" option, and the work went into the parts you touch all day. It has a real toolbar and menus, Mac keyboard shortcuts such as ⌘N for a new task and ⌘⇧I for a new Inbox item, right-click menus, more than one window, and widgets on the desktop. Voice capture and Lock Screen widgets stay on the iPhone and the iPad, and the focus Live Activity stays on the iPhone.

It took longer than ticking the checkbox, and I think it was the right call.

## One app on every device

The other decision: Taskful Day is a single App Store app that runs on iPhone, iPad, and Mac, and it's free to download on each. There is no separate Mac edition to find.

Many indie apps sell the Mac version separately, and they have good reasons: the Mac app is often a lot of extra work for a smaller audience, and a separate price pays for it.

For a planner, though, splitting it up works against what the app is for. Taskful Day exists because the day you plan on one device is the day you finish on another. A Mac edition you had to find and set up on its own would make the product contradict itself.

## Sync through your own iCloud

Sync is the other place a planner can fail without anyone noticing. The plan you make on your phone has to reach the Mac, the task you tick off on the Mac has to disappear from the iPhone widget, and none of it should pass through someone else's server.

With Pro, Taskful Day syncs through your own private iCloud. Tasks, checklists, reminders, workspaces, the Inbox, and your Journal stay in step across your devices. The studio has no server in the path, so I can't see your tasks, and there is no database of ours to lose them from. Settings has Export My Data and Delete All My Data if you want a copy or a clean slate.

Most cross-platform planners work differently: you sign up for an account, your tasks live on the company's servers, and the apps are clients. The studio doesn't use that model anywhere in the catalogue, including here. The cost is that you can't share a task list with a teammate through Taskful Day, because there is no shared cloud to share through. If you need that, Taskful Day is the wrong app for you, and I'd rather you used something else.

## What does "now on Mac" change for Taskful Day?

In practice, the Mac app changes three things.

- **Planning happens at the desk now.** With Pro, the Day Clock, Energy River, and Day Map views work much better on a 27-inch display than a 6-inch one. You see the whole day at a glance, and on the Schedule week grid you drag tasks between hours and days with a real pointing device.
- **Focus happens where the work is.** Focus Mode puts one task on screen with its checklist steps, and Pro adds a timer of 10, 25, or 45 minutes, or anything from 5 to 120. Starting it at the desk means the phone can stay a phone.
- **End-of-day journaling is easier on a keyboard.** The Journal asks how the day felt (Great, Good, Neutral, or Stressed) and takes an optional note. On a keyboard I write longer notes, and they read differently when I look back a month later.

The iPhone is still the device for capture: you think of something, type it as a sentence or say it, and it's filed. The iPad is still where my morning review happens. The Mac is now where the work happens, and the planner sits next to it.

## Where this fits next to Things, TickTick, Sorted³

If you're comparing:

- **Things 3.** Things is a beautiful GTD-style task manager that assumes you want a project tree that lives forever. Taskful Day isn't GTD; it assumes you want one day at a time, and unfinished tasks carry forward without ceremony. If you live in the Areas, Projects, Tasks hierarchy, Things is the right choice.
- **TickTick.** TickTick is a cross-platform Swiss-army knife with reminders, calendars, habit tracking, and Eisenhower matrices. Taskful Day does less on purpose: it has no habit tracker or team features, and its focus tool is Focus Mode, one task on screen with a timer in Pro.
- **Sorted³.** Sorted is a fantastic time-blocked planner. If you want every task to have a start and an end time, Sorted is the better tool. Taskful Day's Day Clock and Schedule grid do some of this, but its aim is a plan you can finish, where Sorted's is to schedule every minute.

Taskful Day is one of several good planners in this space. What sets it apart is the carry-forward, the lack of an account, and one app across iPhone, iPad, Mac, and Apple Watch.

## Get it

Taskful Day is free to download on iPhone, iPad, and Mac, and every new install gets 7 days of Pro free with no card. After that, the free version lets you create up to 50 tasks in total. Pro adds unlimited tasks, iCloud Sync, the Day Clock, Energy River, and Day Map views, the Schedule week grid, the focus timer, and 21 Home Screen widgets, for **{P_MONTHLY@taskful-day}/month**, **{P_YEARLY@taskful-day}/year**, or **{P_LIFETIME@taskful-day} once**.

[Get Taskful Day](/apps/taskful-day/).

For the studio's view of streak-based habit apps, the [streak counter essay](/journal/streaks-are-a-debt/) makes the longer argument behind how this app treats a missed day.

The other thing I shipped this season is a Mac app full of local media tools, the kind people usually upload their files to a random website to use. [That post](/journal/every-media-tool-already-on-your-mac/) is more pointed.
