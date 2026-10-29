---
layout: journal
slug: unlock-cost-outside-the-app
title: "The unlock cost has to live outside the app"
seo:
  title: "Why Every Screen-Time Blocker Folds, and What Doesn't"
  description: "Every screen-time blocker has the same secret: tap hard enough and it folds. Why the unlock cost must live outside the app, and how EarnLock does it."
  keywords:
    - "screen time blocker"
    - "screen time app that works"
    - "focus blocker"
    - "earn screen time app"
    - "exercise to unlock apps"
    - "earnlock"
date: 2026-05-23
last_updated: 2026-10-29
lede: "Every screen-time blocker on the App Store has the same secret. If you tap hard enough, it folds. A short essay on why every app in this category eventually adds a tap-through escape, and what to build in its place."
quick_answer: "Most screen-time blockers (Opal, one sec, ScreenZen, Forest) let you get past the lock with a button, a wait-out timer, or a rule you set yourself. The unlock cost lives inside the app, so you can lower it in the middle of a craving. A blocker that holds has to charge the unlock cost in something the craving can't reach. Waiting doesn't work, because waiting is itself a tap. Movement does (steps, active minutes, active calories), because you pay it in the rest of your life, outside the app. EarnLock is a blocker built around that constraint: your apps open at half your daily activity goal for an hour, and at the full goal until midnight."
faq:
  - q: "Why don't most screen-time blockers actually block?"
    a: "Because every app in this category eventually adds a tap-through escape: Opal's 'I really need this' button, one sec's wait-out timer, ScreenZen's dismissible pause, Forest's give-up-a-tree mechanic. You set the rules on a quiet Sunday and meet them on a Thursday night when you're tired and bored. The Sunday version wants a wall and the Thursday version wants a door, and whichever one drives the App Store rating ships in the next release. Because the unlock cost lives inside the app, you can lower it in the middle of a craving."
  - q: "How is EarnLock different from Opal, one sec, ScreenZen, or Forest?"
    a: "EarnLock's unlock cost lives outside the app. Locked apps stay locked until you reach a daily activity goal measured by Apple Health: steps on the free tier, active minutes or active calories with Premium. Halfway to the goal opens them for an hour, and the full goal opens them until midnight. There is no tap-through button or wait-out timer, and lowering your goal only takes effect after 24 hours, so a craving can't renegotiate it on the spot. Each locked app shows EarnLock's screen with exactly what's left, such as \"2,026 steps until unlock\", so the unlock reads as a place you can walk to."
  - q: "What happens on a day I genuinely can't hit the goal?"
    a: "Halfway still counts: at 50% of your goal your apps open for an hour. For real emergencies, EarnLock has one math-gated emergency unlock per day. You solve a two-digit math problem, pick 15, 30, or 60 minutes, and your apps open. The problem is enough friction to stop a reflex and quick enough for an actual emergency. After that, the next one isn't available until the following day."
  - q: "Why does EarnLock have no account, no server, and no analytics SDK?"
    a: "A screen-time app sees more about your habits than almost any other software you install: which apps you want to avoid, how often you try to break the rules, what time of day you give in. The only safe thing to do with that data is to keep it on the device. EarnLock has no account, makes no network connections of its own, and includes no analytics, advertising, or other third-party SDKs. Apple Health is read on your iPhone and never sent anywhere, and Apple's Screen Time picker gives EarnLock opaque tokens, so even EarnLock can't see which apps you chose."
mentioned_apps:
  - earnlock
  - taskful-day
read_time: "6 min read"
excerpt: "Every screen-time blocker on the App Store has a tap-through escape, because anything stricter gets one-star reviews. The fix is to put the unlock cost somewhere the craving can't reach: measured by a sensor and paid for in the rest of your life. The structural argument behind EarnLock."
---

Every screen-time blocker on the App Store has the same secret. If you tap hard enough, it folds.

Open Opal mid-session and tap "I really need to use this." Open one sec and wait the ten seconds. Open ScreenZen and dismiss the pause. Forest lets you give up a tree. Even Brick, which goes as far as shipping you a physical NFC tag, unlocks as soon as you walk over to the tag.

What these apps add is friction, which is different from blocking.

A blocker has a cost you can't pay in the middle of a craving. Friction has a cost you can pay in two taps, and the design relies on the *hope* that you won't.

App Store ratings are why every app in this category eventually adds a tap-through escape. You set up the blocker on a calm Sunday afternoon and run into it on a Thursday night when you're tired and bored. The Sunday version of you wants a wall. The Thursday version wants a door. Whichever one drives the rating distribution ships in the next release.

So the apps end up with a door, and it gets easier to open with every version.

## Where the cost has to live

If the cost of unlocking lives inside the app, you can lower it. You wrote the PIN, set the timer, and picked the pause length. In the moment of craving none of these is an obstacle. They are notes left by an earlier self, and the current self has the credentials.

The cost has to live somewhere the craving can't reach. There are two reasonable candidates: time and the body.

Time is already taken by the wait-out model that one sec and ScreenZen use. It doesn't work, because waiting is itself a tap. You put the phone down, pick it back up, ten seconds have passed, and the lock is gone. You paid in attention, the thing you were trying to protect in the first place, and the wait gives you nothing you benefit from later.

The body is the other candidate. If the unlock costs steps, active minutes, or active calories, you can't pay it from the couch. You have to go outside, get on the floor, or move around the room. What makes the design defensible, and more than merely strict, is that your life *also benefits from* the payment. I can't think of another unlock cost that is both real and useful.

That's what [EarnLock](/apps/earnlock/) does. Locked apps stay locked until you reach a daily activity goal measured by Apple Health: steps on the free tier, active minutes or active calories with Premium. Halfway to the goal opens them for an hour; the full goal opens them until midnight. You pick the goal on a good day, and lowering it only takes effect after 24 hours, so the Thursday version of you can't renegotiate it on the spot.

## Why the lock screen matters

A second design choice follows from the first.

By default, [Apple's Screen Time controls](/journal/what-an-iphone-app-can-actually-block/) show a generic restriction screen over any app you block. It looks like a system prompt. It tells you nothing about what's left, how it relates to your goal, or whether the cost is reachable.

EarnLock replaces it with its own screen showing exactly what's left, *2,026 steps until unlock*, and an Earn it button that takes you to EarnLock. When you try to open Instagram, the screen doesn't just say you're restricted. It says you're 2,026 steps from Instagram, which is a place you can walk to.

It's a small detail with a big effect. A wall breeds resentment, and a destination gets people moving. That screen turns the body-cost mechanic from a punishment into a price tag.

## Where the failure modes live

Designing it this way has two real costs.

The first is that on some days you won't hit the goal. The product has to make that survivable without making it easy to undermine. Halfway already opens your apps for an hour. Beyond that, EarnLock has one math-gated emergency unlock per day: solve a two-digit math problem, pick 15, 30, or 60 minutes, and that's it until tomorrow. The problem is enough friction to stop a reflex and quick enough for a real emergency. That door is for genuine needs.

The second is that streaks are dangerous in this category. If the app tells you "you've hit your goal 47 days in a row," you start protecting the number for its own sake, and then a sick day or a snowed-in day breaks the streak and you quit the whole thing. EarnLock has a streak because people ask for one, but you can pick a weekly rest day that doesn't break it, and the streak-at-risk reminder is one you can switch off. The streak can exist, but it shouldn't become the thing you're actually optimizing.

(I wrote a [separate essay about why streak counters are a debt instrument](/journal/streaks-are-a-debt/). The short version: any time you ship a streak, you owe the user a rest mechanism, or you're building a guilt loop under another name.)

## The Shadow Week

One more piece deserves a name, because most blockers get it wrong on day one.

When you install a screen-time app, it knows nothing about you yet: which apps you overuse or what time of day the urge spikes. So it picks a default, usually generous and sometimes hostile, and you leave either because it's too strict or because it does nothing.

EarnLock starts with a **Shadow Week**. For the first seven days after you pick your apps, nothing is blocked; the app only counts how often you would have been blocked. At the end it shows "Your shadow week is done" with your own numbers next to an "Enable real blocking" button. You decide with your own data, not a stranger's guess about a phone they've never seen.

I think this is the right default for any tool that proposes to change someone's behaviour. In the first week the tool should earn the right to act, by showing it understands what is actually happening, before it acts on you at all.

## Why no account, no server, no SDK

The last piece is about structure.

A screen-time app sees more about your habits than almost any other software you install: which apps you want to avoid, how often you try to break the rules, what time of day you give in. I'd argue it is one of the most intimate datasets a phone can produce, closer to your messages than to your step count.

The only safe thing to do with that data is to keep it on the device.

EarnLock has no account and no sign-up screen, makes no network connections of its own, and includes no analytics, advertising, or other third-party SDKs. Apple Health is read on your iPhone and never sent anywhere. Apple's Screen Time picker gives EarnLock opaque tokens, so even *we* can't see which apps you chose to lock.

Any app that sits between you and your own behaviour should work this way. No database should know you tried to open Instagram 47 times last Tuesday, no server should know you missed your step goal for a week in February, and no account should tie any of it to an email address. The data is intimate, and the right response to that is restraint.

## What this trades away

The cost of this design is reach.

A screen-time app with no account and no server has nothing to sync through, so your data lives on one iPhone (Premium itself restores through your Apple Account). Without an analytics SDK it can't run growth experiments on cohorts of strangers. And with no tap-through escape it will get some one-star reviews from people who wanted a door.

I think those are the right costs to pay.

[EarnLock](/apps/earnlock/) is free for one locked app or category. Premium is {P_MONTHLY@earnlock}/month or {P_YEARLY@earnlock}/year, each starting with a {TRIAL@earnlock}, or {P_LIFETIME@earnlock} once, and all three support Family Sharing.

A screen-time blocker that can be talked out of blocking in the moment is decoration. One that ships behavioural data to a third-party server is a study you didn't sign up for.
