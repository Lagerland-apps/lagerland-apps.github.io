---
layout: journal
slug: planning-on-phone-finishing-on-desk
title: "The day I plan on my phone is not the day I finish at my desk"
seo:
  title: "Why a Daily Planner Should Be a Native Mac App"
  description: "Taskful Day is a calm daily planner built natively for the Mac, not a stretched iPhone window. One Universal Purchase covers iPhone, iPad and Mac."
  keywords:
    - "mac daily planner"
    - "native mac planner app"
    - "planner for macbook"
    - "mac to-do app"
    - "universal purchase planner"
    - "taskful day"
date: 2026-05-02
last_updated: 2026-10-26
lede: "Taskful Day shipped on the Mac this week. This short essay explains why a calm daily planner had to be a native Mac app instead of a stretched-iPhone Catalyst window, and why it's one Universal Purchase across iPhone, iPad, and Mac instead of three separate licenses."
quick_answer: "Taskful Day is now native on macOS alongside iPhone and iPad, built in SwiftUI with AppKit underpinnings instead of Catalyst. The three platforms share one Universal Purchase, so Pro unlocked on iPhone activates the Mac app automatically. Sync runs through the user's own iCloud account via CloudKit. The studio operates no servers and stores no tasks."
faq:
  - q: "Is Taskful Day available on Mac?"
    a: "Yes. Taskful Day is now native on macOS alongside iPhone and iPad, built in SwiftUI with AppKit underpinnings instead of Catalyst. The window resizes the way a Mac window should, the menu bar is populated, keyboard shortcuts are real Mac shortcuts, and a menu bar item supports quick capture without opening the main window."
  - q: "Do I have to pay separately for Taskful Day on Mac?"
    a: "No. Taskful Day is one Universal Purchase across iPhone, iPad, and Mac. If you bought Pro on your iPhone, signing into the same Apple ID on the Mac activates Pro automatically. Pro is {P_MONTHLY@taskful-day} a month or {P_LIFETIME@taskful-day} lifetime, applied to every device you sign in with."
  - q: "How does Taskful Day sync between iPhone, iPad, and Mac?"
    a: "Taskful Day syncs through your personal iCloud account using CloudKit. The studio operates no servers and stores no tasks. Deleting the app on every device and signing out of iCloud removes the data entirely. The trade-off is that there is no shared cloud space for team task lists."
  - q: "Is Taskful Day a replacement for Things 3, TickTick, or Sorted3?"
    a: "No. Things 3 is GTD-style with a long-lived project tree. TickTick is a cross-platform Swiss-army knife. Sorted3 is a strict time-blocked planner. Taskful Day is for one realistic day at a time, and unfinished tasks roll forward as follow-ups without being marked red."
mentioned_apps:
  - taskful-day
read_time: "5 min read"
excerpt: "Taskful Day is now native on macOS alongside iPhone and iPad, with iCloud sync and one Universal Purchase across all three platforms. This post explains why a planner has to live where the work happens, why a native AppKit Mac app matters more than a Catalyst port for an app you keep open all day, and where Taskful Day sits next to Things 3, TickTick, and Sorted³."
---

I do not plan my day on a phone in the kitchen and then carry the plan, unchanged, to a desk for eight hours.

Nobody does. The plan I make at the coffee maker has three tasks on it, and the day I'd like to have has nine. The work happens somewhere in between, and until this week my planner didn't run on the device I do that work on.

[Taskful Day](/apps/taskful-day/) shipped on the Mac on Wednesday. This Saturday essay is about why the Mac was the missing piece, and what I did and did not do to make it work.

## Why I didn't use Catalyst

For several years Apple has made it easy to bring an iPad app to the Mac. You click a checkbox in Xcode, set a few capabilities, fix the obvious touch-target sins and ship. A lot of indie planners and to-do apps reach the Mac this way, and structurally they are an iPad window with a menu bar.

Catalyst is fine for an app you open once and dismiss, like a calculator or a unit converter. It is not fine for an app you keep open in a corner of the screen for eight hours, next to Slack, your calendar and the document you're trying to finish. The pixels look wrong, the keyboard shortcuts feel pasted on, and the window doesn't behave like a Mac window.

So Taskful Day on Mac is a SwiftUI app built for the Mac first, with AppKit underneath wherever SwiftUI doesn't yet give a Mac app what it needs. The window resizes the way you expect, the keyboard shortcuts are real Mac shortcuts, and the menu bar is populated. Drag-and-drop works as it should on macOS, including into and out of other apps, and a menu bar item handles quick capture without opening the main window.

It took longer than Catalyst would have, and I think it was the right call.

## One Universal Purchase for all three devices

The other decision: Taskful Day is one Universal Purchase across iPhone, iPad, and Mac. If you bought Pro on your iPhone two months ago, the Mac app activates Pro for you the first time you sign into the same Apple ID. You do not pay again, and there is no separate Mac SKU.

Many indie apps charge separately for the Mac version, and they have good reasons: the Mac app is often a lot of extra work for a smaller audience, and a per-platform price pays for it.

For a planner, though, charging twice works against what the app is for. Taskful Day exists because the day you plan on one device is the day you finish on another. Charging once for the device you plan on and again for the one you work on would make the pricing contradict the product.

So it's one purchase for every device. Universal Purchase has been around since 2020, and here it made the right setup easy.

## Sync through your own iCloud

Sync is the other place a planner can fail without anyone noticing. The day plan you make on your phone has to reach the Mac, the focus session you ran on the Mac has to show up in the iPhone widget, and none of it should pass through someone else's server.

Taskful Day syncs through your personal iCloud account using CloudKit. The studio has no servers involved, so I can't see your tasks, and I can't lose them in a database because there is no database. When you delete the app on every device and sign out of iCloud, the data is gone.

Most cross-platform planners work differently: you sign up for an account, your tasks live on the company's servers, and the apps are clients. The studio doesn't use that model anywhere in the catalogue, including here. The cost is that you cannot share a task list with a teammate through Taskful Day, because there is no shared cloud to share through. If you need that, Taskful Day is the wrong app for you, and I'd rather you used something else.

## What does "now on Mac" change for Taskful Day?

In practice, the Mac app changes three things.

- **Planning happens at the desk now.** The Day Clock and Energy River views, the two ways Taskful Day shows your day, work much better on a 27-inch display than a 6-inch one. You can see the whole day in one glance, and you can drag tasks across the day with a real pointing device.
- **Focus sessions don't need the phone.** Focus Orbit runs natively on macOS. You start a session at your desk, the rest of the desktop dims, the menu bar shows the countdown, and the iPhone stays a phone instead of a timer.
- **End-of-day journaling is faster on a keyboard.** The daily mood and reflection entry, which felt like a 60-second exercise on phone, becomes closer to two minutes of real writing on a keyboard. You write different things, so the pattern view shows you something different a month later.

The iPhone is still the device for capture: you think of something, tap, talk, and it's filed. The iPad is still where the morning review happens. The Mac is now where the work happens, and the planner sits next to it.

## Where this fits next to Things, TickTick, Sorted³

If you're comparing:

- **Things 3.** Things is a beautiful GTD-style task manager that assumes you want a project tree that lives forever. Taskful Day isn't GTD; it assumes you want one day at a time, and unfinished tasks roll forward without ceremony. If you live in the Areas, Projects, Tasks hierarchy, Things is the right choice.
- **TickTick.** TickTick is a cross-platform Swiss-army knife with reminders, calendars, habit tracking and Eisenhower matrices. Taskful Day does less on purpose: it has no habit tracker, no Pomodoro as such (the focus mode is more immersive than Pomodoro), and no team features.
- **Sorted³.** Sorted is a fantastic time-blocked planner. If you want every task to have a start and an end time, Sorted is the better tool. Taskful Day's Day Clock view does some of this, but its aim is a realistic plan you can finish, where Sorted's is to schedule every minute.

Taskful Day is one of several good calm-design planners. As of this week it is one of the few that ships natively on iPhone, iPad, and Mac with a single purchase and iCloud as the sync layer.

## Get it

The iPhone, iPad, and Mac apps are all available now. The core is free on every platform. Pro, which adds the focus session timer, advanced analytics, widgets, iCloud sync and unlimited follow-ups, is **{P_MONTHLY@taskful-day}/month** or **{P_LIFETIME@taskful-day} lifetime**, applied across every device you sign in with.

[Get Taskful Day](/apps/taskful-day/).

For the studio's view of streak-based habit apps and why I don't ship one, the [streak counter essay](/journal/streaks-are-a-debt/) makes the longer argument behind that choice in this app.

Next Saturday's entry is about the other thing I shipped this season: a Mac app full of local media tools, the kind people usually upload their files to a random website to use. I expect it to be a more pointed post.
