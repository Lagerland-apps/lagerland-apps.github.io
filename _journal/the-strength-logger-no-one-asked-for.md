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
last_updated: 2026-10-25
lede: "Strong, Hevy, and Fitbod already exist. The strength-training logger market is well-served. I shipped GymLogger X anyway, and the reason isn't features — it's that I wanted the wrist, not the phone screen, to be where a workout gets logged."
quick_answer: "GymLogger X puts strength-training logging on the Apple Watch. You start the session on the iPhone, then enter each set, run rest timers and watch live heart rate from the wrist while the phone stays in your bag. The iPhone keeps the record and handles analytics, program editing, and history. Pro adds plateau detection that informs without lecturing. Pricing is free core, $17.99 a year, or $39.99 lifetime."
faq:
  - q: "Is there a strength-training app built around logging on Apple Watch?"
    a: "GymLogger X is. You start the session on the iPhone; after that, set entry, rest timers, and live heart rate happen on the wrist, and the phone, which keeps the record, can stay in your bag. Analytics, program editing, and history review live on the iPhone, where they benefit from a bigger screen."
  - q: "How is GymLogger X different from Strong, Hevy, or Fitbod?"
    a: "Strong, Hevy, Fitbod, and Caliber are designed phone-first. GymLogger X designs the session around logging from the wrist, with the iPhone running it in the background. It is also free at the core, with $17.99 a year or a $39.99 lifetime tier — and roughly 30% of paid users pick lifetime because training history is a long-term asset."
  - q: "Does GymLogger X automatically restructure my program when I plateau?"
    a: "No. The plateau detection feature flags an exercise when its estimated 1RM has stopped climbing across your recent sessions while your volume holds steady, names the likely cause (too much volume, intensity held too high, too little variation, or too little recovery), and suggests two things to try. It informs without lecturing. Programming changes are the lifter's call, not the app's."
  - q: "Does GymLogger X work without a subscription?"
    a: "Yes. Core logging is free forever. Pro adds plateau detection and analytics for $17.99 a year, with a $39.99 lifetime option for users who do not want a subscription on a tool they intend to use for a decade. LiftLog is the sister iPhone-first app with pay-what-you-can pricing."
mentioned_apps:
  - gymlogger-x
  - liftlog
read_time: "5 min read"
excerpt: "GymLogger X exists in a crowded category. This post explains the specific bet behind it: set logging on the Apple Watch, with the iPhone running the session in your bag, a $39.99 lifetime option, and plateau detection that doesn't lecture. With a small note on why daylight-saving weekend is the worst weekend to start a new training program."
---

It's the first weekend of March. The clocks shift forward in the US tomorrow night, which makes this — by quirk of biology rather than calendar — the worst week of the year to [start a new training program](/journal/choosing-a-strength-program-you-will-finish/). More on that in a moment.

I want to use this weekend's post to explain something specific: why this studio shipped a strength-training logger at all, when the category is one of the most well-served on the App Store.

## Why ship another strength logger into a crowded category?

[GymLogger X](/apps/gymlogger-x/) competes against Strong (the long-running incumbent), Hevy (the rising design-led upstart), Fitbod (the AI-program one), Caliber (the coach-network one), and a long tail of niche loggers. All of them are good apps. The category is not under-served in the obvious sense.

When I started building GymLogger X in late 2025, friends in the indie community asked me, gently, why. The honest answer was: not because of features. It was because of one specific thing the incumbents got structurally wrong.

## Logging on the wrist

Most strength loggers on the App Store are designed around the phone. The session is laid out for the phone screen, and the watch app, where there is one, is a smaller version of it that lets you peek at the next set, maybe start a rest timer, sometimes log a set if you tap through three menus.

That is backwards for the actual gym experience. In the gym, your phone is in a bag or on a bench, somewhere not on your body. Your watch is on your body. The watch is the device that's *with* you between sets. The watch is where logging should happen.

Building a logger around the wrist is technically harder than building a phone-first logger. The screen is small, the input vocabulary is constrained (Digital Crown, taps, voice), the latency budget for syncing back to the phone is tight, and Apple's WatchKit constraints are real. The reason most apps don't do it is that the engineering cost is significant and the user-base willing to *use* it is narrower than the iPhone audience.

I shipped GymLogger X anyway, with the watch as the interface you log on and the phone as the engine in your bag. You start the session on the iPhone, which keeps the record. After that, set entry happens on the wrist. Rest timers happen on the wrist. Live heart rate is glanceable on the wrist. The phone is for analytics, program editing, and history review — the things that benefit from a bigger screen.

The user feedback has been clear: the people who want this *really* want it. The people who don't want this don't notice it's there. Both outcomes are fine.

## Plateau detection that doesn't lecture

The other piece of the bet is the analytics layer.

Most strength loggers track sets and reps and stop there. The Pro tiers add some trend lines. None of them, in my experience, will quietly tell you: *your bench press has been stalled at 100kg×5 for nine weeks across three different programs, and the most likely cause is your recovery, not your programming.*

GymLogger X Pro does try to make that observation, gently. The *plateau detection* feature compares the estimated one-rep max across your four most recent sessions of each exercise and flags it when that number has stopped climbing while your training volume holds steady — stalled despite consistent effort. The output is a flag on the exercise, not a notification: it names the likely cause — too much volume, intensity held too high, too little variation, or too little recovery — and suggests two things to try, such as a deload week or a change of rep range. The progress it measures is each lift's estimated one-rep max, and [how that estimate is calculated, and where the formulas stop being trustworthy](/journal/how-to-estimate-your-one-rep-max/), has its own post.

What it does *not* do is automatically restructure your program for you, change your weights, or send you a coach's nag. Those are real features in other apps. They are also things I think the user should choose to do, not the app's place to impose. Plateau detection in GymLogger X is informational. The next move is yours, and if it points toward a lighter week, [when to deload](/journal/when-to-deload/) covers the signs and what the evidence says.

## The lifetime price

GymLogger X ships with a freemium model that the studio has stuck to: core logging is free forever, Pro is $17.99/year, and there is a one-time **$39.99 lifetime** option for users who don't want a subscription on a tool they intend to use for a decade.

The lifetime tier is the one I most often get asked about. The math on it is, candidly, not great for a studio chasing recurring revenue. A user who buys lifetime in year one and uses the app for seven years has paid the studio about a third of what an annual subscriber would have paid. The lifetime tier exists anyway because strength training is a long-term practice and a user's training history should not be conditional on continuing a subscription.

About 30% of GymLogger X paid users choose the lifetime tier. They are vocal, they are loyal, and they are the user-base I'm most personally proud to serve.

## The daylight-saving note

Back to the calendar. This weekend the US shifts to daylight-saving time. Most US adults will lose an hour of sleep on Sunday night, and most of them will not realise that the loss has measurable consequences for the following week's training.

The research on this is unambiguous. Acute sleep restriction reduces strength performance by 5-10% on the day after, raises perceived exertion noticeably, and depresses recovery markers (HRV, resting heart rate) for several days. In the gym, this presents as: a lift that felt easy last Tuesday feels heavy this Tuesday, and the user blames their effort rather than their sleep. If you rate your sets, [how RPE and reps in reserve work](/journal/rpe-and-rir-explained/) explains why the same load can rate harder after a short night.

If you started a new strength program on January 1 and you've been progressing well, this is the week the curve will flatten. **It is not your training. It is the time change.** Take Tuesday's session at last week's weights instead of pushing for new ones. Resume normal progression next week. GymLogger X will not lecture you, but I will.

## The plain take

[GymLogger X](/apps/gymlogger-x/) exists because the category had a structural gap — logging designed for the wrist rather than the phone screen — and because nobody seemed to be building it. The lifetime price exists because strength training is a long game. The plateau detection exists because the data deserves an interpreter.

For the polished iPhone-first design tier of strength training, the studio also ships [LiftLog](/apps/liftlog/), a sister app with a completely different pricing experiment. They serve different lifters. Both are honest about what they're for.

Don't lift heavy on Tuesday. Lift heavy next Tuesday.
