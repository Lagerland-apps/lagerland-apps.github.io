---
layout: journal
slug: planning-on-phone-finishing-on-desk
title: "The day I plan on my phone is not the day I finish at my desk"
date: 2026-05-02
lede: "Taskful Day shipped on the Mac this week. This is the small essay on why a calm daily planner had to be a native Mac app — not a stretched-iPhone Catalyst window — and why it's one Universal Purchase across iPhone, iPad, and Mac instead of three separate licenses."
read_time: "5 min read"
excerpt: "Taskful Day is now native on macOS alongside iPhone and iPad, with iCloud sync and one Universal Purchase across all three platforms. This post explains why a planner has to live where the work happens, why a native AppKit Mac app matters more than a Catalyst port for an app you keep open all day, and where Taskful Day sits next to Things 3, TickTick, and Sorted³."
---

I do not plan my day on a phone in the kitchen and then carry the plan, unchanged, to a desk for eight hours.

Nobody does. The plan I make at the coffee maker has three tasks on it. The day I'd actually like to have has nine. Somewhere in between is where the work happens — and the device I do the work on has, until this week, not been the device my planner ran on.

[Taskful Day](/apps/taskful-day/) shipped on the Mac on Wednesday. This is the small Saturday essay on why that was the missing piece, and what I did and did not do to make it work.

## The Catalyst escape hatch I did not take

Apple has been generous, for the last several years, about how easy it is to bring an iPad app to the Mac. Click a checkbox in Xcode, set a few capabilities, fix the obvious touch-target sins, ship. A lot of indie planners and to-do apps live on the Mac this way. They are, structurally, an iPad window with a menu bar.

For an app you open once and dismiss — a calculator, a unit converter, a one-off utility — Catalyst is fine. For an app you keep open in a corner of the screen for eight hours, alongside Slack and your calendar and the document you're actually trying to finish, it is not. The pixels read wrong. The keyboard shortcuts feel pasted on. The window doesn't behave the way a Mac window behaves.

So I did not Catalyst this. Taskful Day on Mac is a SwiftUI app built for the Mac first, with AppKit underpinnings where SwiftUI doesn't yet give us the affordances a real Mac app needs. The window resizes the way you expect. The keyboard shortcuts are real Mac shortcuts. The menu bar is populated. Drag-and-drop works the way macOS drag-and-drop is supposed to, including into and out of other apps. There is a real menu bar item for quick capture without opening the main window.

It took longer than Catalyst would have. It is, I think, the correct shape.

## One Universal Purchase, not three

The other decision worth being explicit about: Taskful Day is one Universal Purchase across iPhone, iPad, and Mac. If you bought Pro on your iPhone two months ago, the Mac app activates Pro for you the first time you sign into the same Apple ID. You do not pay again. There is no separate Mac SKU.

This is not the default. Many indie apps charge separately for the Mac version, and there are legitimate reasons to — the Mac app is often a substantial chunk of additional work, and the audience is smaller, so a per-platform price compensates. I am not arguing those teams are wrong.

But for a planner specifically, asking the user to pay twice misses what the app is for. The whole point of Taskful Day is that the day you plan on one device is the day you finish on another. Splitting that across two purchases — pay for the planning surface, pay separately for the doing surface — would make the pricing model contradict the product.

So: one purchase, every device. Universal Purchase has been around since 2020; this is one of the cases where it actually makes the right shape easy.

## iCloud, not someone else's server

Sync is the other place a planner can fail quietly. The day plan you make on your phone has to be on the Mac, and the focus session you ran on the Mac has to show up in the iPhone widget, and none of this should happen on someone else's server.

Taskful Day syncs through your personal iCloud account using CloudKit. The studio has no servers in this loop. I cannot see your tasks. I cannot lose your tasks in a database, because there is no database. When you delete the app on every device and sign out of iCloud, the data is gone, end of story.

This is structurally different from the way most cross-platform planners work. The typical model is: sign up for an account, your tasks live on the company's servers, the apps are clients. The studio does not run that model anywhere in the catalogue, and I am not running it here. The trade is that you cannot share a task list with a teammate through Taskful Day, because there is no shared cloud surface to share through. If that's a workflow you need, the app is the wrong shape for you and I'd rather you use something else.

## What "now on Mac" actually unlocks

Three things, specifically, that the Mac app changes in practice:

- **Planning happens at the desk now.** The Day Clock and Energy River views — the two ways into the day that Taskful Day offers — work much better on a 27-inch display than a 6-inch one. You can see the whole day in one glance, and you can drag tasks across the day with a real pointing device.
- **Focus sessions don't need the phone.** Focus Orbit runs natively on macOS. You drop into a session at your desk, the rest of the desktop dims, the menu bar shows the countdown, and the iPhone is free to be a phone instead of a timer.
- **End-of-day journaling is faster on a keyboard.** The daily mood and reflection entry, which felt like a 60-second exercise on phone, is closer to two minutes of actual writing on a real keyboard. That changes what shows up in it, which changes what the pattern view shows you a month later.

The iPhone app is still the right device for capture — you think of something, you tap, you talk, it's filed. The iPad is still the right device for the morning review. The Mac is now the right device for the actual work, and the planner sits next to the work.

## Where this fits next to Things, TickTick, Sorted³

A quick note for users comparing:

- **Things 3.** Things is a beautiful GTD-style task manager. Taskful Day is not GTD. Things assumes you want a project tree that lives forever. Taskful Day assumes you want one day at a time, and unfinished tasks roll forward without ceremony. If you live in the Areas → Projects → Tasks hierarchy, Things is correct and Taskful Day is not.
- **TickTick.** TickTick is a cross-platform Swiss-army knife with reminders, calendars, habit tracking, Eisenhower matrices. Taskful Day deliberately does less. There is no habit tracker, no Pomodoro per se (the focus mode is more immersive than Pomodoro), no team features. Less surface area is the point.
- **Sorted³.** Sorted is a fantastic time-blocked planner. If you live in time-blocks specifically — meaning, every task gets a start and end — Sorted is the better tool. Taskful Day's Day Clock view does some of this, but the design philosophy is "realistic plan you can finish," not "schedule every minute."

There are good calm-design planners in this space and Taskful Day is not the only one. It is, as of this week, one of the few that ships natively on iPhone, iPad, and Mac with a single purchase and iCloud as the sync layer.

## Get it

The iPhone, iPad, and Mac apps are all available now. The core is free on every platform. Pro — focus session timer, advanced analytics, widgets, iCloud sync, unlimited follow-ups — is **€2.99/month** or **€49.99 lifetime**, applied across every device you sign in with.

[Get Taskful Day](/apps/taskful-day/).

If you are looking for the studio's broader take on streak-based habit apps and why I don't ship one, the [streak counter essay](/journal/streaks-are-a-debt/) is the long-form argument for the design choice you're already feeling in this app.

The next entry, on Saturday, is on the other thing I shipped this season — a Mac app full of local media tools, the kind people usually upload their files to a random website to use. It will, I expect, be a more pointed post.
