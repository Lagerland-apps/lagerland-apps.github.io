---
layout: journal
slug: apple-watch-hrv-without-a-baseline
title: "Why your Apple Watch HRV number means almost nothing without a baseline"
seo:
  title: "Apple Watch HRV: Why the Number Means Nothing Alone"
  description: "Apple Watch HRV: a 42 ms reading can be great or alarming, and only a baseline tells you which. What it measures, what it misses, how to read yours."
  keywords:
    - "apple watch hrv"
    - "hrv baseline"
    - "what is a good hrv"
    - "apple watch heart rate variability"
    - "how to read hrv"
    - "hrv normal range"
date: 2026-05-13
last_updated: 2026-10-26
lede: "A 42ms HRV reading on Apple Watch can be excellent, average, or alarming, and you can't tell which without context. On its own, the number is one of the most misread metrics in consumer health. This post covers what HRV tells you, what it doesn't, and why a personal baseline is the only frame that makes the reading usable."
quick_answer: "Raw HRV (heart-rate variability, reported as SDNN on Apple Watch) is meaningful only against your own rolling baseline. Absolute HRV varies 3 to 10× between individuals depending on age, sex, fitness, posture, measurement timing, and which wrist the watch is on. Read your Apple Watch HRV as a percent deviation from your personal 60-day mean. Comparing your number to a friend's, a population average, or a 'normal range' chart on the internet will almost always mislead you."
faq:
  - q: "Is 42ms HRV good or bad?"
    a: "It depends entirely on whose 42ms it is. For someone whose 60-day baseline is 38ms, 42ms is above average and a good recovery signal. For someone whose baseline is 80ms, 42ms is half their normal and likely signals significant stress, illness, or accumulated training load. The same absolute number is good news in one body and bad news in another, which is why every HRV app worth using compares you to yourself."
  - q: "Why is Apple Watch HRV so different from chest-strap HRV?"
    a: "Apple Watch measures HRV (SDNN) at variable times during the day and overnight when you're still, using optical photoplethysmography. Chest straps measure continuously from electrical activity. The two are different measurements taken in different conditions, so the absolute numbers don't map onto each other. Your watch's readings of you over time do. Your trend is reliable; your absolute number set against a chest-strap chart is not."
  - q: "How much does HRV vary day to day for the same person?"
    a: "A lot. Day-to-day swings of 10 to 25% are normal for a healthy adult, so a single low reading is almost never meaningful. Look at the 7-day rolling average against your 60-day baseline. Single-day HRV is mostly noise."
  - q: "Why does HRV drop in winter?"
    a: "Seasonal cardiovascular adaptation. Cold exposure, less daylight, lower aerobic activity, and altered sleep patterns all shift autonomic balance toward sympathetic dominance. A 10 to 20% winter dip is common and not pathological. One of the most common interpretation mistakes is reading it as 'I'm broken' when it means 'winter HRV runs lower for me'."
  - q: "Does Apple Watch report RMSSD, SDNN, or lnRMSSD?"
    a: "SDNN. Apple Health stores Apple Watch HRV as SDNN, the standard deviation of the intervals between successive heartbeats, in milliseconds, and it is the only HRV metric HealthKit exposes. Sports science favours RMSSD (the root-mean-square of successive RR-interval differences) and its natural log, lnRMSSD, for parasympathetic tone. Those are different measurements from SDNN, so an Apple Watch reading can't simply be 'converted' into RMSSD. Observa does compute RMSSD and pNN50, but only from the occasional ECG recordings you take on your Apple Watch. The passive daily HRV stream is SDNN."
mentioned_apps:
  - observa
read_time: "7 min read"
excerpt: "A 42ms Apple Watch HRV reading is excellent for one person and alarming for another. This post explains why absolute HRV numbers vary 3 to 10× between bodies, why your personal baseline is the only frame that makes Apple Watch HRV usable, and how to read trends the way a sports scientist would."
---

Apple Watch measures one of the most informative numbers in consumer physiology, and almost nobody uses it correctly.

Open the Health app and tap Heart Rate Variability. You'll see a column of numbers from the last few weeks, probably some 25s, some 45s, some 80s, and a "Range" chart that looks vaguely informative. If you've fallen into the wrong corner of the internet, you may have read that HRV "should" be above 50ms or that anything below 30 is "concerning." That is about as useful as being told your "normal" body temperature should be 99°F regardless of who you are. The number is real. The frame is wrong.

## What HRV actually measures

HRV, or heart-rate variability, is the variation in time between consecutive heartbeats. Apple Watch reports SDNN, the standard deviation of the intervals between successive normal heartbeats (the NN, or RR, intervals), in milliseconds. Higher generally means more parasympathetic ("rest-and-digest") nervous-system activity, and lower generally means more sympathetic ("fight-or-flight") activity. A consistently higher trend correlates with cardiovascular fitness, recovery quality, and parasympathetic dominance.

So far, so good. The trouble starts when the same words apply to two people whose absolute numbers differ by a factor of three.

## The variation between people is enormous

Absolute HRV in healthy adults ranges roughly from 15ms to 150ms in SDNN terms, a 10× spread. These factors move someone's individual baseline:

- **Age.** Most longitudinal studies find HRV declines roughly 0.5 to 1ms per year after age 30. A 45-year-old with 35ms HRV and a 25-year-old with 70ms may both be in perfect parasympathetic health for their age.
- **Sex.** Average HRV is somewhat lower in adult women than men, though the variation within each sex is much larger than the difference between them.
- **Fitness level.** Endurance-trained people routinely show 50 to 100% higher resting HRV than untrained people. That isn't proportionally informative either: well-conditioned athletes often sit in ranges a generic chart would call "elevated."
- **Body position.** HRV is higher lying down than seated, and higher seated than standing.
- **Time of day.** Higher overnight, lower during active hours.
- **Measurement method.** Apple Watch's optical PPG at variable times produces different numbers than a chest strap or a research-grade ECG, even on the same person at the same moment.

HRV is one of those biological metrics where *yours* is the only one that means anything. Comparing your 42ms to a friend's 65ms tells you nothing.

## The right frame: your own 60-day baseline

The only HRV readings you can reliably interpret look like one of these:

- **"Today's HRV (SDNN) is X% above/below my own 7-day rolling average."**
- **"This week's mean is X% above/below my own 60-day rolling average."**

Both compare you with yourself, which cancels out nearly every confounder above. Your age and sex don't change in 60 days, your fitness doesn't change dramatically, and your watch is the same watch. What does change is *whatever moved your physiology this week compared with last quarter*, and that's the question worth asking.

Sixty days works as a baseline window for three reasons. It's roughly two menstrual cycles, so cyclical variation averages out. It covers two typical training mesocycles, so short-term adaptation doesn't dominate. And it gives enough non-overlapping weekly samples for a standard deviation to mean something; with fewer, the SD itself is noisy.

[Observa](/apps/observa/) uses this baseline window, and so do most peer-reviewed sports-science HRV studies, for the same reasons.

## What a single low reading does and doesn't mean

A morning where your HRV is 30% below your 7-day average means *something happened*: late food, alcohol, poor sleep, a stressful evening, the start of an illness, hard training the day before, or ordinary day-to-day biological noise. By itself it doesn't tell you to rest, train hard, panic, or rejoice.

A *pattern* is diagnostic. Three consecutive days more than one standard deviation below baseline is signal. A single 25% drop after a known stressor tells you about that stressor, not your health. A 25% drop with no identifiable cause that hasn't resolved within 72 hours warrants attention, from a clinician and not a consumer app.

For self-experimentation, I think this threshold is roughly right: **at least 10 same-condition observations across a 60-day window, and at least one standard deviation of separation between conditions**, before you treat a finding as anything but noise. Most consumer apps surface "insights" with far thinner statistical backing, which is mostly why those insights are mostly wrong.

## Why HRV drops in winter (and other seasonal noise)

If you wear an Apple Watch through a northern-hemisphere winter, expect your HRV baseline to drop 10 to 20% from October to February. The usual causes are cold exposure, less daylight, less aerobic activity, more time indoors, and altered sleep. None of them is pathological, and all of them pull the number down.

Reading a winter dip as "I'm broken" is one of the most common interpretation mistakes. The correct reading is "winter HRV runs lower for me, and here's the new baseline to measure deviations from." The baseline is supposed to drift, because your physiology drifts with the world.

## What this means in practice

A few practical rules follow from all this:

1. **Never compare your number to anyone else's.** Not a friend's, not a stranger's on Reddit, not a "normal range" infographic. Compare yourself to yourself.

2. **Track trends.** A single day's HRV is mostly noise. The 7-day rolling mean is signal, and the 60-day baseline is the frame that makes the signal interpretable.

3. **Read it as a deviation from your own baseline.** HRV is roughly log-normally distributed, so the same millisecond gap means more at a low baseline than a high one. Expressing today's SDNN as a percentage deviation from your personal rolling mean is what makes it interpretable.

4. **Identify your stressors.** If your HRV consistently drops after late workouts, alcohol, or long screen time, you can act on that. The drop isn't the problem; the unknown cause is.

5. **Expect seasonal drift.** Lower in winter and higher in summer is normal. A pandemic, an illness, life stress, or a new baby will all move the baseline too. Treat it as a moving frame of reference.

[Observa](/apps/observa/) does this automatically. It computes your 60-day rolling HRV (SDNN) baseline, scores each day's reading against your own deviation, and tells you in plain English when something is genuinely outside your normal range and when it isn't. Everything runs on-device, so the only comparison Observa ever makes is *you, today, against you, on average*, which is the only HRV comparison worth making.

## TL;DR

- **Absolute HRV varies 3 to 10× between healthy adults.** Comparing your number to anyone else's is meaningless.
- **Your 60-day rolling baseline is the only frame that makes HRV usable.** Day-to-day swings of 10 to 25% are normal.
- **Trends matter; single points don't.** Three consecutive days more than one SD below baseline is signal. One day is noise.
- **Winter HRV runs lower than summer.** Seasonal drift is normal, and treating it as illness is the common error.
- **Read SDNN as a deviation from your own baseline.** HRV is roughly log-normally distributed, so compare each day to your personal mean as a percentage, not to raw millisecond thresholds.

The number has always been in your Health app. What was missing is a baseline to read it against.
