---
layout: journal
slug: the-strength-logger-no-one-asked-for
title: "Why I shipped a Strong-style logger that nobody asked for"
seo:
  title: "An Apple Watch-First Strength Logger (Strong-Style)"
  description: "Why GymLogger X puts set logging on the Apple Watch, with the iPhone running the workout, when Strong, Hevy, and Fitbod own the category."
  keywords:
    - "apple watch workout logger"
    - "strength log apple watch"
    - "watch-first lifting app"
    - "strong alternative apple watch"
    - "gym logger watch"
    - "gymlogger x"
date: 2026-03-07
last_updated: 2026-10-29
lede: "Strong, Hevy, and Fitbod already exist, and the market for strength-training loggers is well served. I shipped GymLogger X anyway, because I wanted workouts to be logged on the wrist instead of on the phone screen."
quick_answer: "GymLogger X is an iPhone strength log with a free Apple Watch app built for logging at the rack. You start the workout on the iPhone, then enter each set, run the rest timer, and see live heart rate on the wrist, while the iPhone keeps the record and handles analytics, programs, and history. Pro reads your own logs and gives each lift a plateau status without lecturing you. Logging is free; Pro is {P_MONTHLY@gymlogger-x} a month, {P_YEARLY@gymlogger-x} a year, or {P_LIFETIME@gymlogger-x} once."
faq:
  - q: "Is there a strength-training app built around logging on Apple Watch?"
    a: "GymLogger X is one. It is an iPhone app with a free Apple Watch app: you start the workout on the iPhone, then log each set, run the rest timer, and see live heart rate on the wrist, while the iPhone keeps the record. Analytics, programs, and history live on the iPhone, where the bigger screen helps."
  - q: "How is GymLogger X different from Strong, Hevy, or Fitbod?"
    a: "Most strength loggers are designed phone-first. GymLogger X's free Apple Watch app logs sets, runs the rest timer, and shows live heart rate, with the iPhone running the workout; Strong goes further with a standalone Watch app. GymLogger X also needs no account, logging is free, and Pro, which reads your own logs for plateau and fatigue signals, comes as a subscription or a {P_LIFETIME@gymlogger-x} one-time purchase."
  - q: "Does GymLogger X automatically restructure my program when I plateau?"
    a: "No. With Pro, Strength Progress gives each lift a plateau status (Plateau, Watching, or Plateau Predicted) from its estimated 1RM trend, and the Next Move card suggests what to do, such as a rest day or a change of approach. The app sends no notifications, and changes to the program stay the lifter's call."
  - q: "Does GymLogger X work without a subscription?"
    a: "Yes. Logging and the Apple Watch app are free for good. Pro adds Insights, plateau signals, and all 44 programs for {P_MONTHLY@gymlogger-x} a month or {P_YEARLY@gymlogger-x} a year, or {P_LIFETIME@gymlogger-x} once for users who don't want a subscription on a tool they intend to use for a decade. LiftLog, the studio's iPhone-only strength log, has no subscription at all: a free week, then one payment at a tier you choose."
mentioned_apps:
  - gymlogger-x
  - liftlog
read_time: "5 min read"
excerpt: "GymLogger X entered a crowded category. This post explains the bet behind it: set logging on the Apple Watch with the iPhone running the workout, a {P_LIFETIME@gymlogger-x} lifetime option, and plateau signals that don't lecture. It ends with a note on why daylight-saving weekend is the worst weekend to start a new training program."
---

It's the first weekend of March. The clocks shift forward in the US tomorrow night, which, through a quirk of biology, makes this the worst week of the year to [start a new training program](/journal/choosing-a-strength-program-you-will-finish/). More on that later.

This weekend's post is about why this studio shipped a strength-training logger at all, when the category is one of the best served on the App Store.

## Why ship another strength logger into a crowded category?

[GymLogger X](/apps/gymlogger-x/) competes with Strong (the long-running incumbent), Hevy (the design-led upstart), Fitbod (the AI-program one), Caliber (the coach-network one), and a long tail of niche loggers. They are all good apps, and the category is not under-served in any obvious way.

When I started building GymLogger X in 2025, friends in the indie community asked me, gently, why. Features weren't the reason. Most of the incumbents had one specific thing structurally wrong.

## Logging on the wrist

Most strength loggers on the App Store are designed around the phone. The session is laid out for the phone screen, and the watch app, where there is one, is a smaller version of it that lets you peek at the next set, maybe start a rest timer, and sometimes log a set if you tap through three menus.

That gets a gym session backwards. Between sets your phone is on the bench or the floor, and your watch is on your wrist. So the watch is where logging should be easy.

Building logging for the wrist is harder than building it for the phone. The screen is small, the input options are limited, the watch has to stay in step with the phone, and Apple's watchOS constraints are real. Most apps skip it because the engineering cost is significant and fewer people will *use* it than the iPhone audience.

I built GymLogger X's Watch app anyway. You start the workout on the iPhone, which keeps the record. On the wrist you log each set's weight and reps with steppers, run the rest timer, and see live heart rate, time, and calories, and the sets you log there go through the phone. The rest timer can also tell you when your heart rate has recovered. The iPhone handles analytics, programs, and history, which benefit from a bigger screen. The Watch app is free.

So far, the people who want this *really* want it, and the people who don't want it don't notice it's there. I'm fine with both.

## Plateau signals that don't lecture

The other half of the bet is the analytics.

Most strength loggers track sets and reps and stop there, and their Pro tiers add some trend lines. In my experience none of them will tell you: *your bench press has been stalled at 100kg×5 for nine weeks across three different programs, and the most likely cause is your recovery, not your programming.*

GymLogger X Pro tries to make that kind of observation, quietly. It estimates a one-rep max for each lift from your logged sets, and Strength Progress gives every lift a status: Plateau, Watching, or Plateau Predicted. Insights puts that next to your readiness, weekly load ratio, recovery debt, and muscle balance, and the Next Move card turns it into one suggestion: rest, deal with a plateau, work on a weak point, or train as planned. Once there is enough history, up to three plain-language suggestions explain why. It all runs by fixed rules on your iPhone, with no chat bot. The progress it measures is each lift's estimated one-rep max, and [how that estimate is calculated, and where the formulas stop being trustworthy](/journal/how-to-estimate-your-one-rep-max/), has its own post.

It does *not* restructure your program for you, change your weights, or nag you; the app sends no notifications at all. Other apps have those features. I think they are things the user should choose to do, and not the app's place to impose. In GymLogger X a plateau status is information, and the next move is yours. If it points toward a lighter week, [when to deload](/journal/when-to-deload/) covers the signs and what the evidence says.

## The lifetime price

GymLogger X ships with the freemium model the studio has stuck to: logging is free for good, Pro is {P_MONTHLY@gymlogger-x}/month or {P_YEARLY@gymlogger-x}/year, and there is a one-time {P_LIFETIME@gymlogger-x} lifetime option for users who don't want a subscription on a tool they intend to use for a decade.

The lifetime tier is the one I get asked about most. For a studio chasing recurring revenue, it is a poor deal: someone who buys lifetime in year one and trains with the app for seven years pays once, while a subscriber keeps paying. The tier exists anyway because strength training is a long-term practice, and a user's training history shouldn't depend on keeping a subscription going.

## The daylight-saving note

Back to the calendar. This weekend the US shifts to daylight-saving time. Most US adults will lose an hour of sleep on Sunday night, and most of them won't realise the loss has measurable consequences for the following week's training.

Studies of short-term sleep restriction tend to find the same pattern: strength performance dips the next day, the same work feels harder, and recovery markers such as HRV and resting heart rate take a while to settle. In the gym it shows up as a lift that felt easy last Tuesday feeling heavy this Tuesday, with the lifter blaming their effort instead of their sleep. If you rate your sets, [how RPE and reps in reserve work](/journal/rpe-and-rir-explained/) explains why the same load can rate harder after a short night.

If you started a new strength program on January 1 and have been progressing well, this is the week the curve will flatten, and the time change is the cause. Take Tuesday's session at last week's weights instead of pushing for new ones, and resume normal progression next week. GymLogger X won't lecture you about it, but I will.

## The short version

[GymLogger X](/apps/gymlogger-x/) exists because the category had a structural gap, logging designed for the wrist, and few apps seemed to be filling it. It has a lifetime price because strength training is a long game, and plateau signals because the data needs someone to interpret it.

For lifters who live on the iPhone, the studio also ships [LiftLog](/apps/liftlog/), a sister app you pay for once, with no subscription, at a tier you choose. The two serve different lifters.
