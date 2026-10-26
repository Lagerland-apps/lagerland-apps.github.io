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
last_updated: 2026-10-26
lede: "Every screen-time blocker on the App Store has the same secret. If you tap hard enough, it folds. A short essay on why every app in this category eventually adds a tap-through escape, and what to build in its place."
quick_answer: "Most screen-time blockers (Opal, one sec, ScreenZen, Forest) let the user dismiss the lock with a button, a wait-out timer, or a PIN they set themselves. The unlock cost lives inside the app, so the user can lower it in the middle of a craving. A real blocker has to charge the unlock cost in something the craving cannot reach. Waiting does not work, because waiting is itself a tap. Body movement does (steps, active minutes, active calories), because the user has to pay it in the rest of their life, outside the app. EarnLock is the version of the category built around that constraint."
faq:
  - q: "Why don't most screen-time blockers actually block?"
    a: "Because every app in this category eventually adds a tap-through escape: Opal's 'I really need this' button, one sec's wait-out timer, ScreenZen's dismissible pause, Forest's give-up-a-tree mechanic. The user sets the rules on a calm Sunday and meets them on a Thursday night when they are not calm. The Sunday version wants a wall and the Thursday version wants a door, and whichever one drives the App Store rating ships in the next release. Because the unlock cost lives inside the app, the user can lower it in the middle of a craving."
  - q: "How is EarnLock different from Opal, one sec, ScreenZen, or Forest?"
    a: "EarnLock's unlock cost lives outside the app. The blocked apps stay blocked until the user hits a daily activity goal measured by Apple Health on the device: steps in the free tier, active minutes or active energy in Premium. There is no tap-through button, wait-out timer, give-up mechanic, or PIN the user can change in the moment. The user picks the goal on a calm day, and the craving cannot renegotiate it. The shield over each blocked app shows a live progress ring with the exact count remaining (\"Earn 2,026 more steps to unlock\"), so the unlock reads as a destination the user can reach."
  - q: "What happens on a day I genuinely can't hit the goal?"
    a: "EarnLock ships one math-gated emergency unlock per day. Triggering it means solving a real arithmetic problem, which is harder than typing a four-digit PIN you set thirty seconds ago. The math is hard enough that you cannot solve it mid-doomscroll without breaking concentration. Once you use it, the next emergency unlock is not available until local midnight. The cap exists because the friction is the product, and raising it would defeat the design."
  - q: "Why does EarnLock have no account, no server, no analytics SDK?"
    a: "A screen-time app sees more about a user's habits than almost any other software they install: which apps they want to avoid, how often they try to break the rules, what time of day they fail. That dataset is more intimate than location or messages, and the only safe thing to do with it is to keep it on the device. EarnLock has no account, no analytics SDK, no advertising SDK, no third-party SDKs of any kind, and no EarnLock server. HealthKit is read on-device only. Family Controls hands EarnLock opaque tokens, so even EarnLock cannot see which apps the user picked to block. Apple's App Privacy nutrition label reads 'Data Not Collected' for every release."
mentioned_apps:
  - earnlock
  - taskful-day
read_time: "6 min read"
excerpt: "Every screen-time blocker on the App Store has a tap-through escape, because anything stricter gets one-star reviews. The fix is to put the unlock cost somewhere the craving cannot reach: measured by a sensor and paid for in the rest of the user's life. The structural argument behind EarnLock."
---

Every screen-time blocker on the App Store has the same secret. If you tap hard enough, it folds.

Open Opal mid-session and tap "I really need to use this." Open one sec and wait the ten seconds. Open ScreenZen and dismiss the pause. Forest lets you give up a tree. Even Brick, which goes as far as shipping you a physical NFC tag, lets you unlock with the tag from across the room.

What these apps add is friction, which is different from blocking.

A blocker has a cost you cannot pay in the middle of a craving. Friction has a cost you can pay in two taps, and the design relies on the *hope* that you won't.

App Store ratings are why every app in this category eventually adds a tap-through escape. The user sets up the blocker on a Sunday afternoon when they are calm and runs into it on a Thursday night when they are not. The Sunday version of the user wants a wall. The Thursday version wants a door. Whichever one drives the rating distribution ships in the next release.

So the apps end up with a door, and it gets easier to open with every version.

## Where the cost has to live

If the cost of unlocking lives inside the app, the user can lower it. They wrote the PIN, set the timer, and picked the pause length. In the moment of craving none of these is an obstacle. They are notes left by an earlier self, and the current self has the credentials.

The cost has to live somewhere the craving cannot reach. There are two reasonable candidates: time and the body.

Time is already taken by the wait-out model that one sec and ScreenZen use. It doesn't work, because waiting is itself a tap. The user puts the phone down, picks it back up, ten seconds have passed, and the lock is gone. They paid in attention, the same thing they were trying to protect in the first place, and the wait gives them nothing they benefit from later.

The body is the other candidate. If the unlock costs steps, active minutes, or active calories, the user cannot pay it from the couch. They have to go outside, get on the floor, or move around the room. What makes the design defensible, and more than merely strict, is that the user's life *also benefits from* the payment. It is the only kind of unlock cost that is both real and useful.

That's what [EarnLock](/apps/earnlock/) does. The blocked apps stay blocked until the user hits a daily activity goal measured in Apple Health: steps in the free tier, active minutes or active energy in Premium. The user picks the goal on a calm day, and the Thursday version of the user can't renegotiate it because there is no tap-through.

## Why the shield matters

A second design choice follows from the first.

By default, [Apple's Family Controls API](/journal/what-an-iphone-app-can-actually-block/) renders a generic restriction screen over any app you block: *This app has been restricted by Screen Time.* It looks like a system prompt. It tells the user nothing about what is left, how it relates to the goal, or whether the cost is reachable.

EarnLock paints its own shield, with a circular progress ring, the current step count, and the exact number remaining: *Earn 2,026 more steps to unlock*. A user who tries to open Instagram isn't told they are restricted. They're told they are 2,026 steps from Instagram, which is a place they can walk to.

It's a small detail with a big effect. A wall produces resentment, and a destination gets people moving. The shield is what turns the body-cost mechanic from a punishment into a price tag.

## Where the failure modes live

Designing it this way has two real costs.

The first is that on some days the user won't hit the goal and won't see Instagram that day. The product has to make that survivable without making it easy to undermine. EarnLock includes one math-gated emergency unlock per day: solve a real arithmetic problem, get one unlock, then nothing until midnight. The math is hard enough that you cannot solve it mid-doomscroll without breaking concentration. That door is for genuine emergencies only.

The second is that streaks are dangerous in this category. If the app tells the user "you've blocked Instagram 47 days in a row," they start protecting the number for its own sake, and then a sick day or a snowed-in day breaks the streak and they quit the whole thing. EarnLock ships a streak because users ask for it, but a single rest day per week protects the count, and no notification shames the user for missing a day. The streak can exist, but it can't become the thing the user is actually optimising.

(I wrote a [separate essay about why streak counters are a debt instrument](/journal/streaks-are-a-debt/). The short version: any time you ship a streak, you owe the user a rest mechanism, or you're building a guilt loop under another name.)

## The shadow week

One more piece deserves a name, because most blockers get it wrong on day one.

When a user installs a screen-time app, the app knows nothing about them yet: which apps they overuse, what time of day the urge spikes, or how much real time they would have spent if nothing blocked them. So it picks a default, usually generous and sometimes hostile, and the user leaves either because it is too strict or because it does nothing.

EarnLock starts in **shadow mode** for the first week. Nothing is blocked. The app watches which apps the user opens, when, and for how long. At the end of the week it shows a screen that says, in effect, *here is what you would have lost, about 30 minutes a day and 23 separate block events this week, based on your own behaviour. Enable real blocking?* The user decides with their own data and not with a stranger's guess about a phone they've never seen.

I think this is the right default for any tool that proposes to change someone's behaviour. In the first week the tool should earn the right to act, by showing it understands what is actually happening, before it acts on the user at all.

## Why no account, no server, no SDK

The last piece is about structure.

A screen-time app sees more about a user's habits than almost any other software they install: which apps they want to avoid, how often they try to break the rules, what time of day they fail, how long their attention lasts. By a wide margin it is the most psychologically intimate dataset a phone can produce, more intimate than location, messages, or the photo library.

The only safe thing to do with that data is to keep it on the device.

EarnLock has no account, no sign-up screen, no analytics SDK, no advertising SDK, no third-party SDKs of any kind, and no EarnLock server anywhere. HealthKit is read on-device only and never transmitted. Family Controls hands EarnLock opaque tokens, so even *we* cannot see which apps the user picked to block. Apple's App Privacy nutrition label reads "Data Not Collected" for every release.

Any app that sits between a user and their own behaviour should work this way. No database should know the user tried to open Instagram 47 times last Tuesday, no server should know they missed their step goal for a week in February, and no account should tie any of it to an email address. The data is intimate, and the right response to that is restraint.

## What this trades away

The cost of this design is reach.

A screen-time app with no account cannot sync state through a third-party backend. (EarnLock uses CloudKit through the user's own Apple ID for the iPhone-to-Watch handoff, which is the only acceptable alternative.) Without an analytics SDK it cannot run growth experiments on cohorts of strangers. And with no tap-through escape it will get some one-star reviews from people who wanted a door.

I think those are the right costs to pay.

A screen-time blocker that can be talked out of blocking in the moment is decoration. One that ships behavioural data to a third-party server is a study you didn't sign up for.

[EarnLock](/apps/earnlock/) takes both of those positions seriously. Free; Premium {P_MONTHLY@earnlock}/month, {P_YEARLY@earnlock}/year (with a 7-day free trial), or {P_LIFETIME@earnlock} lifetime. Every paid tier (Monthly, Yearly, and Lifetime) is Family Sharing eligible.

If you can unlock it in two taps, it isn't a blocker.
