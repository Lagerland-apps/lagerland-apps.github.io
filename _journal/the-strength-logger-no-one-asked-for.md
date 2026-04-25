---
layout: journal
slug: the-strength-logger-no-one-asked-for
title: "Why I shipped a Strong-style logger that nobody asked for"
date: 2026-03-07
lede: "Strong, Hevy, and Fitbod already exist. The strength-training logger market is well-served. I shipped GymLogger X anyway, and the reason isn't features — it's that nobody else seems to think Apple Watch deserves to be the actual workout log."
read_time: "5 min read"
excerpt: "GymLogger X exists in a crowded category. This post explains the specific bet behind it: Apple Watch as a first-class logging client (not a phone companion), a $44.99 lifetime option, and plateau detection that doesn't lecture. With a small note on why daylight-saving weekend is the worst weekend to start a new training program."
---

It's the first weekend of March. The clocks shift forward in the US tomorrow night, which makes this — by quirk of biology rather than calendar — the worst week of the year to start a new training program. More on that in a moment.

I want to use this weekend's post to explain something specific: why this studio shipped a strength-training logger at all, when the category is one of the most well-served on the App Store.

## The crowded category

[GymLogger X](/apps/gymlogger-x/) competes against Strong (the long-running incumbent), Hevy (the rising design-led upstart), Fitbod (the AI-program one), Caliber (the coach-network one), and a long tail of niche loggers. All of them are good apps. The category is not under-served in the obvious sense.

When I started building GymLogger X in 2023, friends in the indie community asked me, gently, why. The honest answer was: not because of features. It was because of one specific thing the incumbents got structurally wrong.

## Apple Watch as the actual log

Every major strength logger on the App Store treats Apple Watch as a *companion*. The phone is the source of truth. The watch is a small mirror that lets you peek at the next set, maybe start a rest timer, sometimes log a set if you tap through three menus.

This is exactly backwards for the actual gym experience. In the gym, your phone is in a locker, in a bag, on a bench, somewhere not on your body. Your watch is on your body. The watch is the device that's *with* you between sets. The watch is where the log should live.

Building a watch-first logger is technically harder than building a phone-first logger. The screen is small, the input vocabulary is constrained (Digital Crown, taps, voice), the latency budget for syncing back to the phone is tight, and Apple's WatchKit constraints are real. The reason most apps don't do it is that the engineering cost is significant and the user-base willing to *use* it is narrower than the iPhone audience.

I shipped GymLogger X anyway, with the watch as the primary interface and the phone as the *companion* that mirrors the watch's data. Set entry happens on the wrist. Rest timers happen on the wrist. Live heart rate is glanceable on the wrist. The phone is for analytics, program editing, and history review — the things that benefit from a bigger screen.

The user feedback has been clear: the people who want this *really* want it. The people who don't want this don't notice it's there. Both outcomes are fine.

## Plateau detection that doesn't lecture

The other piece of the bet is the analytics layer.

Most strength loggers track sets and reps and stop there. The Pro tiers add some trend lines. None of them, in my experience, will quietly tell you: *your bench press has been stalled at 100kg×5 for nine weeks across three different programs, and the most likely cause is your recovery, not your programming.*

GymLogger X Pro does try to make that observation, gently. The *plateau detection* feature looks at your last twelve weeks of data per exercise and flags when an exercise has stopped progressing despite consistent effort. The output is a small banner, not a notification — *"Your bench press is plateauing. Possible causes: training frequency, recovery, exercise selection. Tap for analysis."*

What it does *not* do is automatically restructure your program for you, change your weights, or send you a coach's nag. Those are real features in other apps. They are also things I think the user should choose to do, not the app's place to impose. Plateau detection in GymLogger X is informational. The next move is yours.

## The lifetime price

GymLogger X ships with a freemium model that the studio has stuck to: core logging is free forever, Pro is $17.99/year, and there is a one-time **$44.99 lifetime** option for users who don't want a subscription on a tool they intend to use for a decade.

The lifetime tier is the one I most often get asked about. The math on it is, candidly, not great for a studio chasing recurring revenue. A user who buys lifetime in year one and uses the app for seven years has paid the studio half what an annual subscriber would have paid. The lifetime tier exists anyway because strength training is a long-term practice and a user's training history should not be conditional on continuing a subscription.

About 30% of GymLogger X paid users choose the lifetime tier. They are vocal, they are loyal, and they are the user-base I'm most personally proud to serve.

## The daylight-saving note

Back to the calendar. This weekend the US shifts to daylight-saving time. Most US adults will lose an hour of sleep on Sunday night, and most of them will not realise that the loss has measurable consequences for the following week's training.

The research on this is unambiguous. Acute sleep restriction reduces strength performance by 5-10% on the day after, raises perceived exertion noticeably, and depresses recovery markers (HRV, resting heart rate) for several days. In the gym, this presents as: a lift that felt easy last Tuesday feels heavy this Tuesday, and the user blames their effort rather than their sleep.

If you started a new strength program on January 1 and you've been progressing well, this is the week the curve will flatten. **It is not your training. It is the time change.** Take Tuesday's session at last week's weights instead of pushing for new ones. Resume normal progression next week. GymLogger X will not lecture you, but I will.

## The plain take

[GymLogger X](/apps/gymlogger-x/) exists because the category had a structural gap — Apple Watch as a first-class logging client — and because nobody seemed to be building it. The lifetime price exists because strength training is a long game. The plateau detection exists because the data deserves an interpreter.

For the polished iPhone-first design tier of strength training, the studio also ships [LiftLog](/apps/liftlog/), a sister app with a completely different pricing experiment. They serve different lifters. Both are honest about what they're for.

Don't lift heavy on Tuesday. Lift heavy next Tuesday.
