---
layout: journal
slug: your-apple-health-data-doesnt-mean-what-you-think
title: "Your Apple Health data isn't telling you what you think it's telling you"
date: 2026-01-17
lede: "Three years of HRV charts, ten thousand data points, and a feeling that none of it added up to anything. The story behind Observa, and why interpretation matters more than tracking."
read_time: "6 min read"
excerpt: "Apple Health surfaces hundreds of metrics with no narrative attached. This post explains the interpretation gap that motivated Observa, why correlation analysis beats raw charts, and what ‘plain-language insights’ actually look like in a privacy-first app."
---

I have worn an Apple Watch since 2018. By the time I started building [Observa](/apps/observa/), Apple Health had eight years of my data — sleep, heart rate, HRV, ECG readings, mindfulness minutes, workout sessions, blood oxygen, walking steadiness, the lot.

I had no idea what any of it meant.

I don't mean that in a glib way. I mean: I could open the Health app, watch a number go up and down, see a chart that resembled a small mountain range, and not be able to answer the only question that mattered — *should I do anything differently this week?*

That gap is what Observa was built to close.

## What Apple Health is good at

Before anything else: Apple Health is excellent at the thing it's built for. It collects, normalises, and persists health metrics with privacy guarantees no consumer system has ever offered. The charts are well-designed. The unit handling is meticulous. The data layer is honestly the best in the industry.

What Apple Health *isn't* trying to do — and shouldn't, in my view — is editorialise. It will not tell you that your HRV dropped because of last week's two short nights. It will not connect your morning resting heart rate to the wine you drank on Saturday. It will not say, "your training load is twenty percent above your eight-week average and your recovery scores are dropping; consider a deload week." Apple's deliberate restraint here is correct. Health data is sensitive, and over-interpretation is a real danger.

But for the user, that restraint leaves a gap. You have data. You don't have meaning.

## The chart-trance problem

If you've ever spent twenty minutes scrolling through a year of HRV measurements looking for a pattern, you know the failure mode I'm describing. The brain is bad at pattern-matching across noisy time-series data. We see trends that aren't there and miss trends that are. We anchor on the last measurement. We feel anxious about a single low reading and reassured by a single high one, neither of which means anything statistically.

This isn't a willpower problem. It's a *display* problem. A chart with seven hundred datapoints and no overlay is not a tool — it's a Rorschach test.

## What Observa does

Observa sits on top of Apple Health and answers a small set of questions explicitly:

- **What variable is most correlated with your sleep quality this month?** Maybe it's training volume. Maybe it's screen time before bed. Maybe it's day-of-week (don't underestimate Sunday-night anxiety as a predictor).
- **What does your HRV trend actually look like, normalised against your own baseline?** Not the population's. Yours. A 38 ms HRV reading is meaningless without knowing whether your personal baseline is 32 or 56.
- **Which days in the last 90 had the largest deviation from baseline, and what else changed on those days?** This is where the interesting stories live. The ones where you say "oh, of course, that was the week I flew through three time zones."
- **Is your training load consistent with your recovery, or is it diverging?** If both lines diverge, you are accumulating fatigue, regardless of how the individual workouts felt.

These aren't medical diagnostics. They're explicitly not. Observa cannot tell you whether you have a clinical sleep disorder, a cardiac issue, or an autoimmune condition. It will not pretend to. What it can do is take a year of your own data and turn it into three or four sentences a thoughtful coach might tell you if they had time to read it carefully — which most coaches don't.

## Why this had to be on-device

The other constraint that shaped Observa is the obvious one: health data should never leave your device.

This sounds like a statement of values, and it is, but it's also a technical decision with real product consequences. A cloud-based version of Observa would have access to better correlation models, larger datasets, and more compute. It would also be a target for breaches, a regulatory minefield in multiple jurisdictions, and — most importantly — a thing the user could not verify.

Observa's correlation analysis runs on the device using local models small enough to fit in the app bundle. The tradeoff is that the analyses are simpler than what a cloud service could do. The advantage is that no one but you ever sees a single data point. There's no cloud account to compromise. There's no employee with database access. There's no "we accidentally trained a model on your sleep data" press release in the future.

I think that's the right tradeoff for health data. I'm aware not everyone agrees, and there are use cases — clinical research, longitudinal population studies — where on-device cannot compete. Observa is not that product. It's the *interpretation layer* for one person's own life, owned by them.

## What this means in practice

If you've been opening the Health app, scrolling, and feeling vaguely unproductive about it, [Observa](/apps/observa/) is built for that exact moment. It reads what's already in your Health database (with your permission, scoped to the categories you allow) and produces a calm weekly read instead of a panel of charts.

It won't tell you what to eat. It won't tell you when to sleep. It will, occasionally, tell you something specific and useful — like "your resting heart rate has been elevated for three weeks and the most likely correlate is training volume" — and let you decide what to do with that.

That's the whole product. Apple's data layer plus a thin layer of honest interpretation. No tracking, no upload, no account, no medical advice — just the modest, useful thing that's missing.
