---
layout: journal
slug: the-strength-logger-no-one-asked-for
title: "Why I shipped a Strong-style logger that nobody asked for"
seo:
  title: "An Apple Watch-First Strength Logger (Strong-Style)"
  description: "Why GymLogger X puts set logging on the Apple Watch, with the iPhone running the session in your bag, when Strong, Hevy and Fitbod own the category."
  keywords:
    - "apple watch workout logger"
    - "strength log apple watch"
    - "watch-first lifting app"
    - "strong alternative apple watch"
    - "gym logger watch"
    - "gymlogger x"
date: 2026-03-07
last_updated: 2026-10-26
lede: "Strong, Hevy and Fitbod already exist, and the market for strength-training loggers is well served. I shipped GymLogger X anyway, because I wanted workouts to be logged on the wrist instead of on the phone screen."
quick_answer: "GymLogger X puts strength-training logging on the Apple Watch. You start the session on the iPhone, then enter each set, run rest timers and watch live heart rate from the wrist while the phone stays in your bag. The iPhone keeps the record and handles analytics, program editing and history. Pro adds plateau detection that flags a stalled lift without lecturing you. Core logging is free; Pro is {P_YEARLY@gymlogger-x} a year or {P_LIFETIME@gymlogger-x} lifetime."
faq:
  - q: "Is there a strength-training app built around logging on Apple Watch?"
    a: "GymLogger X is one. You start the session on the iPhone; after that, set entry, rest timers and live heart rate happen on the wrist, and the phone, which keeps the record, can stay in your bag. Analytics, program editing and history review live on the iPhone, where the bigger screen helps."
  - q: "How is GymLogger X different from Strong, Hevy, or Fitbod?"
    a: "Strong, Hevy, Fitbod and Caliber are designed phone-first. GymLogger X designs the session around logging from the wrist, with the iPhone running it in the background. Its core is also free, with {P_YEARLY@gymlogger-x} a year or a {P_LIFETIME@gymlogger-x} lifetime tier, and roughly 30% of paid users pick lifetime because training history is a long-term asset."
  - q: "Does GymLogger X automatically restructure my program when I plateau?"
    a: "No. The plateau detection feature flags an exercise when its estimated 1RM has stopped climbing across your recent sessions while your volume holds steady. It names the likely cause (too much volume, intensity held too high, too little variation, or too little recovery) and suggests two things to try. It doesn't lecture, and changes to the program stay the lifter's call."
  - q: "Does GymLogger X work without a subscription?"
    a: "Yes. Core logging is free for good. Pro adds plateau detection and analytics for {P_YEARLY@gymlogger-x} a year, with a {P_LIFETIME@gymlogger-x} lifetime option for users who don't want a subscription on a tool they intend to use for a decade. LiftLog is the sister iPhone-first app, with pay-what-you-can pricing."
mentioned_apps:
  - gymlogger-x
  - liftlog
read_time: "5 min read"
excerpt: "GymLogger X entered a crowded category. This post explains the bet behind it: set logging on the Apple Watch with the iPhone running the session in your bag, a $39.99 lifetime option, and plateau detection that doesn't lecture. It ends with a note on why daylight-saving weekend is the worst weekend to start a new training program."
---

It's the first weekend of March. The clocks shift forward in the US tomorrow night, which, through a quirk of biology, makes this the worst week of the year to [start a new training program](/journal/choosing-a-strength-program-you-will-finish/). More on that later.

This weekend's post is about why this studio shipped a strength-training logger at all, when the category is one of the best served on the App Store.

## Why ship another strength logger into a crowded category?

[GymLogger X](/apps/gymlogger-x/) competes with Strong (the long-running incumbent), Hevy (the design-led upstart), Fitbod (the AI-program one), Caliber (the coach-network one) and a long tail of niche loggers. They are all good apps, and the category is not under-served in any obvious way.

When I started building GymLogger X in late 2025, friends in the indie community asked me, gently, why. Features weren't the reason. The incumbents had one specific thing structurally wrong.

## Logging on the wrist

Most strength loggers on the App Store are designed around the phone. The session is laid out for the phone screen, and the watch app, where there is one, is a smaller version of it that lets you peek at the next set, maybe start a rest timer, and sometimes log a set if you tap through three menus.

That is backwards for how a gym session goes. Your phone sits in a bag or on a bench, while your watch is on your wrist, with you between sets. So the watch is where logging should happen.

Building a logger around the wrist is harder than building a phone-first one. The screen is small, the input options are limited (Digital Crown, taps, voice), the latency budget for syncing back to the phone is tight, and Apple's WatchKit constraints are real. Most apps skip it because the engineering cost is significant and fewer people will *use* it than the iPhone audience.

I shipped GymLogger X anyway, with the watch as the interface you log on and the phone as the engine in your bag. You start the session on the iPhone, which keeps the record. After that, set entry and rest timers happen on the wrist, and live heart rate is there at a glance. The phone handles analytics, program editing and history review, which benefit from a bigger screen.

The feedback so far: the people who want this *really* want it, and the people who don't want it don't notice it's there. I'm fine with both.

## Plateau detection that doesn't lecture

The other half of the bet is the analytics.

Most strength loggers track sets and reps and stop there, and their Pro tiers add some trend lines. In my experience none of them will tell you: *your bench press has been stalled at 100kg×5 for nine weeks across three different programs, and the most likely cause is your recovery, not your programming.*

GymLogger X Pro tries to make that observation, gently. The *plateau detection* feature compares the estimated one-rep max across your four most recent sessions of each exercise and flags the exercise when that number has stopped climbing while your training volume holds steady, which means it has stalled despite consistent effort. The output is a flag on the exercise, not a notification. It names the likely cause (too much volume, intensity held too high, too little variation, or too little recovery) and suggests two things to try, such as a deload week or a change of rep range. The progress it measures is each lift's estimated one-rep max, and [how that estimate is calculated, and where the formulas stop being trustworthy](/journal/how-to-estimate-your-one-rep-max/), has its own post.

It does *not* restructure your program for you, change your weights, or send you a coach's nag. Other apps have those features. I think they are things the user should choose to do, and not the app's place to impose. Plateau detection in GymLogger X is information, and the next move is yours. If it points toward a lighter week, [when to deload](/journal/when-to-deload/) covers the signs and what the evidence says.

## The lifetime price

GymLogger X ships with the freemium model the studio has stuck to: core logging is free for good, Pro is {P_YEARLY@gymlogger-x}/year, and there is a one-time {P_LIFETIME@gymlogger-x} lifetime option for users who don't want a subscription on a tool they intend to use for a decade.

The lifetime tier is the one I get asked about most. For a studio chasing recurring revenue, the math on it is poor. A user who buys lifetime in year one and uses the app for seven years has paid the studio about a third of what an annual subscriber would have. The tier exists anyway because strength training is a long-term practice, and a user's training history shouldn't depend on keeping a subscription going.

About 30% of GymLogger X paid users choose the lifetime tier. They are vocal and loyal, and they are the users I'm proudest to serve.

## The daylight-saving note

Back to the calendar. This weekend the US shifts to daylight-saving time. Most US adults will lose an hour of sleep on Sunday night, and most of them won't realise the loss has measurable consequences for the following week's training.

The research on this is unambiguous. Acute sleep restriction reduces strength performance by 5-10% the next day, noticeably raises perceived exertion, and depresses recovery markers (HRV, resting heart rate) for several days. In the gym it shows up as a lift that felt easy last Tuesday feeling heavy this Tuesday, with the lifter blaming their effort instead of their sleep. If you rate your sets, [how RPE and reps in reserve work](/journal/rpe-and-rir-explained/) explains why the same load can rate harder after a short night.

If you started a new strength program on January 1 and have been progressing well, this is the week the curve will flatten, and the time change is the cause. Take Tuesday's session at last week's weights instead of pushing for new ones, and resume normal progression next week. GymLogger X won't lecture you about it, but I will.

## The short version

[GymLogger X](/apps/gymlogger-x/) exists because the category had a structural gap, logging designed for the wrist, and nobody seemed to be filling it. It has a lifetime price because strength training is a long game, and plateau detection because the data needs someone to interpret it.

For the polished iPhone-first side of strength training, the studio also ships [LiftLog](/apps/liftlog/), a sister app with a completely different pricing experiment. The two serve different lifters.
