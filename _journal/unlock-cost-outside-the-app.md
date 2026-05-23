---
layout: journal
slug: unlock-cost-outside-the-app
title: "The unlock cost has to live outside the app"
date: 2026-05-23
lede: "Every screen-time blocker on the App Store has the same secret. If you tap hard enough, it folds. A short essay on why every app in this category eventually adds a tap-through escape — and what to build instead."
quick_answer: "Most screen-time blockers — Opal, one sec, ScreenZen, Forest — let the user dismiss the lock with a button, a wait-out timer, or a PIN they set themselves. The unlock cost lives inside the app, which means the user can lower it from inside the moment of craving. A real blocker has to denominate the unlock cost in something the craving cannot reach. Time-of-wait does not work because waiting is itself a tap. Body movement does — steps, active minutes, active calories — because the cost has to be paid in the rest of the user's life, not in the app. EarnLock is the version of the category that takes that constraint seriously."
faq:
  - q: "Why don't most screen-time blockers actually block?"
    a: "Because every app in this category eventually adds a tap-through escape — Opal's 'I really need this' button, one sec's wait-out timer, ScreenZen's dismissible pause, Forest's give-up-a-tree mechanic. The user sets the rules on a calm Sunday and encounters them on a Thursday night when they are not calm. The Sunday version wants a wall; the Thursday version wants a door; whichever one rules the App Store rating ships in the next release. The unlock cost lives inside the app, so the user can lower it from inside the moment of craving."
  - q: "How is EarnLock different from Opal, one sec, ScreenZen, or Forest?"
    a: "EarnLock's unlock cost lives outside the app. The blocked apps stay blocked until the user hits a daily activity goal measured by Apple Health on the device — steps in the free tier, active minutes or active energy in Premium. There is no tap-through button, no wait-out timer, no PIN the user can change in the moment, and no give-up mechanic. The user picks the goal on a calm day; the craving cannot renegotiate it. The shield over each blocked app shows a live progress ring with the exact count remaining (\"Earn 2,026 more steps to unlock\"), so the unlock is a destination rather than a wall."
  - q: "What happens on a day I genuinely can't hit the goal?"
    a: "EarnLock ships one math-gated emergency unlock per day. Triggering it requires solving a real arithmetic problem — not a four-digit PIN set thirty seconds ago. The math is hard enough that you cannot solve it mid-doomscroll without breaking concentration. After you use it, the next emergency unlock is not available until local midnight. The cap exists because the friction is the product; raising the cap would defeat the design."
  - q: "Why does EarnLock have no account, no server, no analytics SDK?"
    a: "A screen-time app sees more about a user's habits than almost any other software they install — which apps they want to avoid, how often they try to break the rules, what time of day they fail. That dataset is more intimate than location or messages. The only safe thing to do with it is to never let it leave the device. EarnLock has no account, no analytics SDK, no advertising SDK, no third-party SDKs of any kind, and no EarnLock server. HealthKit is read on-device only. Family Controls hands EarnLock opaque tokens — even EarnLock cannot see which apps the user picked to block. Apple's App Privacy nutrition label reads 'Data Not Collected' for every release."
mentioned_apps:
  - earnlock
  - taskful-day
read_time: "6 min read"
excerpt: "Every screen-time blocker on the App Store has a tap-through escape, because anything stricter gets one-star reviews. The fix is to put the unlock cost somewhere the craving cannot reach — measured by a sensor, paid for in the rest of the user's life. The structural argument behind EarnLock."
---

Every screen-time blocker on the App Store has the same secret. If you tap hard enough, it folds.

Open Opal mid-session and tap "I really need to use this." Open one sec and wait the ten seconds. Open ScreenZen and dismiss the pause. Forest lets you give up a tree. Even Brick — which goes so far as to ship you a physical NFC tag — lets you unlock with the tag from across the room.

These are not blockers. They are friction. The distinction matters.

A blocker has a cost you cannot pay from inside the moment of craving. Friction has a cost you can pay in two taps, and the design relies on the *hope* that you won't.

The reason every app in this category eventually adds a tap-through escape is App Store ratings. The user sets up the blocker on a Sunday afternoon when they are calm, and they encounter the blocker on a Thursday night when they are not. The Sunday version of the user wants a wall. The Thursday version wants a door. Whichever one rules the rating distribution ships in the next release.

So the apps end up with a door, and the door gets easier to open every version.

## Where the cost has to live

If the cost of unlocking lives inside the app, the user can lower it. They wrote the PIN. They set the timer. They picked the pause length. None of these are obstacles in the moment of craving — they are bookmarks from a previous self, and the current self has the credentials.

The cost has to live somewhere the craving cannot reach. There are two reasonable candidates: time and the body.

Time is already taken — that's the wait-out model. one sec and ScreenZen do this. It does not work, because waiting is itself a tap. The user sets down the phone, picks it back up, ten seconds passed, the lock is gone. The user paid in attention, which is the same currency they were trying to defend in the first place. Nothing about the wait translates into anything the user benefits from later.

The body is the other candidate. If the unlock costs steps, or active minutes, or active calories, the user cannot pay it from the couch. They have to go outside, or get on the floor, or move through the room. And — this is the part that makes the design defensible rather than merely strict — the cost is denominated in something the user's life *also benefits from*. It is the only kind of unlock cost that is both real and useful.

That's what [EarnLock](/apps/earnlock/) does. The blocked apps stay blocked until the user hits a daily activity goal measured on Apple Health. Steps in the free tier. Active minutes or active energy in Premium. The user picks the goal on a calm day. The Thursday version of the user does not get to renegotiate it, because the Thursday version of the user does not have a tap-through.

## Why the shield matters

There is a second design choice that follows from the first.

Apple's Family Controls API will, by default, render a generic restriction screen over any app you block. *This app has been restricted by Screen Time.* It looks like a system prompt. It teaches the user nothing — no count of what is left, no relationship to the goal, no sense that the cost is reachable.

EarnLock paints its own shield. The shield shows a circular progress ring, the current step count, and the exact number remaining: *Earn 2,026 more steps to unlock*. When the user attempts to open Instagram, they are not told they are restricted. They are told they are 2,026 steps from Instagram. The unlock is a destination, not a wall.

This is small but it matters. A wall produces resentment. A destination produces motion. The shield is what turns the body-cost mechanic from a punishment into a price tag.

## Where the failure modes live

Designing it this way does ship two real costs.

The first is that some days the user will not hit the goal. They will not see Instagram that day. The right product response is to make that survivable without being undermineable. EarnLock includes one math-gated emergency unlock per day — solve a real arithmetic problem, get one unlock, then nothing until midnight. The math is hard enough that you cannot solve it mid-doomscroll without breaking concentration. It is the door for the genuine emergency, and only that.

The second is that streaks are dangerous in this category. If the app tells the user "you've blocked Instagram 47 days in a row," they start protecting the number for its own sake — and then a sick day or a snowed-in day breaks the streak and the user quits the whole thing. EarnLock ships a streak because users ask for it, but a single rest day per week protects the count, and there is no notification shaming the user for missing a day. The streak is allowed to exist; it is not allowed to become the thing the user is actually optimising.

(I wrote a [separate essay about why streak counters are a debt instrument](/journal/streaks-are-a-debt/). The short version is: any time you ship a streak, you owe the user a rest mechanism, or you are building a guilt loop with a different label.)

## The shadow week

There is one more piece worth naming, because it is the part most blockers get wrong on day one.

When a user installs a screen-time app, the app does not know anything about that user yet. It does not know which apps they actually overuse, what time of day the urge spikes, or how much real time they would have spent had nothing blocked them. So the app picks a default — usually generous, sometimes hostile — and the user either bounces because it is too strict or bounces because it does nothing.

EarnLock starts in **shadow mode** for the first week. Nothing is blocked. The app watches: which apps the user opens, when, for how long. At the end of the week it shows the user a screen that says, in effect, *here is what you would have lost — about 30 minutes a day, 23 separate block events this week — based on your own behaviour. Enable real blocking?* The user makes the call with their own data, not with a guess from a stranger who has never seen their phone.

This is, I think, the right default for any tool that proposes to change a user's behaviour. The first week should not be the tool acting on the user. It should be the tool earning the right to act, by demonstrating that it understands what is actually happening.

## Why no account, no server, no SDK

The last piece is structural rather than behavioural.

A screen-time app sees more about a user's habits than almost any other software they install. Which apps they want to avoid. How often they try to break the rules. What time of day they fail. How long their attention lasts. This is, by a wide margin, the most psychologically intimate dataset a phone can produce — more intimate than location, more intimate than messages, more intimate than the photo library.

The only safe thing to do with that data is to never let it leave the device.

EarnLock has no account, no sign-up screen, no analytics SDK, no advertising SDK, no third-party SDKs of any kind, and no EarnLock server anywhere. HealthKit is read on-device only and never transmitted. Family Controls hands EarnLock opaque tokens — even *we* cannot see which apps the user picked to block. Apple's App Privacy nutrition label reads "Data Not Collected" for every release.

This is the right default for any app that sits between a user and their own behaviour. There should not be a database that knows the user tried to open Instagram 47 times last Tuesday. There should not be a server that knows they missed their step goal for a week in February. There should not be an account that ties any of this to an email address. The mechanism is private because the mechanism is *intimate*, and the right response to intimacy is restraint.

## What this trades away

The honest cost of this design is reach.

A screen-time app with no account cannot sync state through a third-party backend. (EarnLock uses CloudKit through the user's own Apple ID for the iPhone-to-Watch handoff, which is the only acceptable alternative.) A screen-time app with no analytics SDK cannot run growth experiments on cohorts of strangers. A screen-time app with no tap-through escape will get some one-star reviews from people who wanted a door.

These are the costs. I think they are the right costs to pay.

A screen-time blocker that can be talked out of blocking in the moment is not a blocker — it is decoration. A screen-time blocker that ships behavioural data to a third-party server is not a tool — it is a study you didn't sign up for.

[EarnLock](/apps/earnlock/) is the version of the category that takes both of those positions seriously. Free; Premium $1.99/month or $9.99/year, both with a 7-day free trial, or $19.99 lifetime. Every paid tier — Monthly, Yearly, and Lifetime — is Family Sharing eligible.

If you can unlock it in two taps, it isn't a blocker.
