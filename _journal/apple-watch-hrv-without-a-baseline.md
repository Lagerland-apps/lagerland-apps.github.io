---
layout: journal
slug: apple-watch-hrv-without-a-baseline
title: "Why your Apple Watch HRV number means almost nothing without a baseline"
seo:
  title: "Apple Watch HRV: Why the Number Means Nothing Alone"
  description: "Apple Watch HRV: a 42 ms reading can be great or alarming — you can't tell without a baseline. What it measures, what it doesn't, and how to read yours."
  keywords:
    - "apple watch hrv"
    - "hrv baseline"
    - "what is a good hrv"
    - "apple watch heart rate variability"
    - "how to read hrv"
    - "hrv normal range"
date: 2026-05-13
last_updated: 2026-07-11
lede: "A 42ms HRV reading on Apple Watch can be excellent, average, or alarming — and you can't tell which without context. The number on its own is one of the most-misread metrics in consumer health. Here's what HRV actually tells you, what it doesn't, and why a personal baseline is the only frame that makes the reading usable."
quick_answer: "Raw HRV (heart-rate variability, reported as SDNN on Apple Watch) is meaningful only against your own rolling baseline. Absolute HRV varies 3–10× between individuals based on age, sex, fitness, posture, measurement timing, and which wrist the watch is on. The right way to read your Apple Watch HRV is as a percent deviation from your personal 60-day mean. Comparing your number to a friend's, a population average, or a 'normal range' chart on the internet will almost always mislead you."
faq:
  - q: "Is 42ms HRV good or bad?"
    a: "It depends entirely on whose 42ms it is. For someone whose 60-day baseline is 38ms, 42ms is above average — a good recovery signal. For someone whose baseline is 80ms, 42ms is half their normal and likely signals significant stress, illness, or accumulated training load. The same absolute number is good news in one body and bad news in another. This is why every HRV-aware app worth using compares you to yourself."
  - q: "Why is Apple Watch HRV so different from chest-strap HRV?"
    a: "Apple Watch measures HRV (SDNN) at variable times during the day and overnight when you're still, using optical photoplethysmography. Chest straps measure continuously from electrical activity. The absolute numbers don't directly map — they're different measurements taken in different conditions. What does map is your watch's reading of you over time. Your trend is reliable; the absolute number compared to a chest-strap chart is not."
  - q: "How much does HRV vary day to day for the same person?"
    a: "A lot. 10–25% day-to-day swings are normal for a healthy adult. That's why a single low reading is almost never meaningful — what matters is the 7-day rolling average against your 60-day baseline. Single-day HRV is mostly noise."
  - q: "Why does HRV drop in winter?"
    a: "Seasonal cardiovascular adaptation. Cold exposure, less daylight, lower aerobic activity, and altered sleep patterns all shift autonomic balance toward sympathetic dominance. A 10–20% winter dip is common and not pathological. Reading a winter dip as 'I'm broken' rather than 'winter HRV runs lower for me' is one of the most common interpretation mistakes."
  - q: "Does Apple Watch report RMSSD, SDNN, or lnRMSSD?"
    a: "SDNN. Apple Health stores Apple Watch HRV as SDNN — the standard deviation of the intervals between successive heartbeats — in milliseconds, and it is the only HRV metric HealthKit exposes. RMSSD (the root-mean-square of successive RR-interval differences) and its natural log, lnRMSSD, are the metrics sports science favours for parasympathetic tone, but they are different measurements from SDNN, so an Apple Watch reading is not simply 'converted' into RMSSD. Observa does compute RMSSD and pNN50 — but only from the occasional ECG recordings you take on your Apple Watch, not from the passive daily HRV stream, which is SDNN."
mentioned_apps:
  - observa
read_time: "7 min read"
excerpt: "A 42ms Apple Watch HRV reading is excellent for one person and alarming for another. This post explains why absolute HRV numbers vary 3–10× between bodies, why your personal baseline is the only frame that makes Apple Watch HRV usable, and how to read trends like a sports scientist rather than guessing."
---

Apple Watch quietly measures one of the most informative numbers in consumer physiology — and almost nobody uses it correctly.

Open the Health app and tap on Heart Rate Variability. You'll see a column of numbers from the last few weeks. Probably some are 25, some are 45, some are 80. You'll see a "Range" chart that looks vaguely informative. You may, if you've fallen into the wrong corner of the internet, have read that HRV "should" be above 50ms or that anything below 30 is "concerning." This is approximately as useful as being told your "normal" body temperature should be 99°F regardless of who you are. The number is real. The frame is wrong.

## What HRV actually measures

HRV — heart-rate variability — is the variation in time between consecutive heartbeats. Apple Watch specifically reports SDNN, the standard deviation of the intervals between successive normal heartbeats (the NN, or RR, intervals), in milliseconds. Higher generally means more parasympathetic ("rest-and-digest") nervous-system activity. Lower generally means more sympathetic ("fight-or-flight") activity. A consistently higher trend correlates with cardiovascular fitness, recovery quality, and parasympathetic dominance.

So far, so good. The trouble starts when the same words apply to two people whose absolute numbers differ by a factor of three.

## The variation between people is enormous

Absolute HRV in healthy adults ranges roughly from 15ms to 150ms in SDNN terms. That's a 10× spread. The factors that move someone's individual baseline:

- **Age.** HRV declines roughly 0.5–1ms per year after age 30 in most longitudinal studies. A 45-year-old with 35ms HRV and a 25-year-old with 70ms may both be in perfect parasympathetic health for their age.
- **Sex.** Average HRV is somewhat lower in adult women than men, though the variation within each sex is much larger than the difference between sexes.
- **Fitness level.** Endurance-trained individuals routinely show 50–100% higher resting HRV than untrained individuals. This isn't proportionally informative either — well-conditioned athletes often have HRV in ranges that would look "elevated" in a generic chart.
- **Body position.** HRV is higher when supine than seated, higher seated than standing.
- **Time of day.** Higher overnight, lower during active hours.
- **Measurement method.** Apple Watch's optical PPG at variable times produces different numbers than a chest strap or a research-grade ECG, even on the same person at the same moment.

In other words: HRV is one of those biological metrics where *yours* is the only one that means anything. Comparing your 42ms to a friend's 65ms tells you nothing.

## The right frame: your own 60-day baseline

The only HRV reading that's reliably interpretable is one of these:

- **"Today's HRV (SDNN) is X% above/below my own 7-day rolling average."**
- **"This week's mean is X% above/below my own 60-day rolling average."**

Both are statements about you against yourself. Both compensate for nearly every confounder above — age doesn't change in 60 days, sex doesn't change, your fitness doesn't change dramatically, your watch is the same watch. What does change is what *moved your physiology this week relative to last quarter*. That's the question worth asking.

Sixty days is a useful baseline window for three reasons. First, it's roughly two menstrual cycles, so cyclical variation averages out. Second, it covers two typical training mesocycles, so transient adaptation doesn't dominate. Third, it provides enough non-overlapping weekly samples to make a standard deviation actually meaningful — fewer than that, and the SD itself is noisy.

This is the baseline window [Observa](/apps/observa/) uses, and it's the same window most peer-reviewed sports-science HRV studies use for the same reasons.

## What a single low reading does and doesn't mean

A single morning where your HRV is 30% below your 7-day average means *something happened* — late food, alcohol, poor sleep, a stressful evening, the start of an illness, intense training the day before, or just normal day-to-day biological noise. It does not, by itself, mean you should rest, train hard, panic, or rejoice.

What's diagnostic is a *pattern*. Three consecutive days more than one standard deviation below baseline is signal. A single 25% drop after a known stressor is information about that stressor, not your health. A 25% drop with no identifiable cause and no resolution within 72 hours warrants attention — but attention from a clinician, not a consumer app.

The pattern threshold I think is roughly right for self-experimentation is: **needs at least 10 same-condition observations across a 60-day window, and at least one standard deviation of separation between conditions**, before you should treat a finding as anything other than noise. Most consumer apps surface "insights" with far thinner statistical backing than this. That's mostly why their insights are mostly wrong.

## Why HRV drops in winter (and other seasonal noise)

If you wear an Apple Watch through a northern-hemisphere winter, expect a 10–20% drop in your HRV baseline from October to February. The usual suspects: cold exposure, less daylight, less aerobic activity, more indoor time, altered sleep patterns. None of these are pathological. All of them produce the same downward drift.

Reading a winter dip as "I'm broken" is one of the most common interpretation mistakes. Reading it as "winter HRV runs lower for me, here's the new baseline to measure deviations from" is the correct response. The baseline is supposed to drift — your physiology drifts with the world.

## What this means in practice

A few practical rules that fall out of all this:

1. **Never compare your number to anyone else's, ever.** Not a friend's, not a stranger's on Reddit, not a "normal range" infographic. The comparison is meaningless. Compare yourself to yourself.

2. **Track trends, not points.** A single day's HRV is mostly noise. The 7-day rolling mean is signal. The 60-day baseline is the frame that makes the signal interpretable.

3. **Read it as a deviation from your own baseline, not a raw number.** HRV is roughly log-normally distributed, so the same millisecond gap means more at a low baseline than a high one. Comparing today's SDNN to your personal rolling mean as a percentage deviation is what makes it interpretable.

4. **Identify your stressors.** If your HRV consistently drops after late workouts, after alcohol, after high screen time, that's actionable. The drop itself isn't the problem — the unknown cause is.

5. **Expect seasonal drift.** Winter lower, summer higher is normal. Pandemic, illness, life stress, a new baby — all expected baseline movers. The baseline is a moving frame, not an absolute reference.

[Observa](/apps/observa/) does this automatically: it computes your 60-day rolling HRV (SDNN) baseline, scores each day's reading against your own deviation, and tells you in plain English when something is genuinely outside your normal range — and when it isn't. Everything runs on-device, so the only comparison Observa ever makes is *you, today, against you, on average*. That's the only HRV comparison that's worth making.

## TL;DR

- **Absolute HRV varies 3–10× between healthy adults.** Comparing your number to anyone else's is meaningless.
- **Your 60-day rolling baseline is the only frame that makes HRV usable.** Day-to-day swings of 10–25% are normal.
- **Trends matter, single points don't.** Three consecutive days more than one SD below baseline is signal; one day is noise.
- **Winter HRV runs lower than summer.** Seasonal drift is normal. Pathologising it is the common error.
- **Read SDNN as a deviation from your own baseline.** HRV is roughly log-normally distributed, so compare each day to your personal mean as a percentage, not to raw millisecond thresholds.

The number was always there in your Health app. The only thing that's been missing is the frame that makes it informative.
