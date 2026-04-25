---
layout: journal
slug: building-a-sleep-app-for-night-shifts
title: "Building a sleep app for nurses, pilots, and the people who don't have a 9-to-5"
date: 2026-01-24
lede: "Most sleep apps assume an 11pm bedtime and a 7am alarm. The people who keep hospitals, planes, and emergency rooms running don't live that life. AfterShift is the app I built after hearing the same complaint from too many friends in scrubs."
read_time: "6 min read"
excerpt: "Most sleep apps are designed for the 9-to-5. AfterShift was built specifically for rotating-shift workers — nurses, pilots, first responders — with a Shift Recovery Score, caffeine timing aligned to the next block, and calendar shift import. This post explains the design constraints and what generic sleep apps get wrong about night shift life."
---

A friend who works ICU nights asked me, in 2024, why none of her sleep apps understood what she was doing.

She'd open one of the popular ones, log a five-hour daytime sleep, and the app would politely tell her she'd had a *poor night* and should try going to bed earlier. The app meant well. The app's model of a human was that humans sleep at night. Her model of a human was that nurses sleep when the rotation lets them.

That conversation was the start of [AfterShift](/apps/aftershift/). This is what I learned building it.

## The 9-to-5 assumption is everywhere

Open any major consumer sleep app and walk through onboarding. You'll be asked when you go to bed, when you wake up, and what your weekend pattern is. The implicit model is a five-day workweek with weekends free, plus the assumption that "night" means a single uninterrupted block of darkness.

Now imagine a typical nurse's twelve-hour rotation: three days on, three days off, two-week cycle, with the days flipping to nights halfway through. Her sleep windows might be 10pm-6am one week, 9am-3pm the next, with a chaotic transition night in between. The sleep app's model breaks. The recovery scores are nonsensical. The caffeine recommendations actively harm her.

This is a real population. The US has about 4 million registered nurses, several hundred thousand commercial pilots, plus paramedics, firefighters, police, factory workers, refinery operators, and a long tail of other rotating-shift workers. Generic sleep apps don't serve any of them well.

## What "shift-aware" actually means

The first thing AfterShift does that generic apps don't is take a different view of *what counts as a sleep session*. It accepts:

- A primary sleep block of any length, at any time of day, on any day.
- Optional naps before or after the primary block. Pre-shift naps are a recognised fatigue countermeasure for night work. Post-shift "anchor sleeps" before transitioning back to days are another.
- Fragmented patterns. A six-hour sleep, broken once, is structurally different from an unbroken six hours, and the app treats it that way.

The second is the **Shift Recovery Score**, which is the metric I'm proudest of. It isn't a sleep score in the consumer sense. It's a forward-looking estimate: given the sleep you've had since your last shift, given the rotation pattern you're on, given how fragmented your recent sleep has been, *how recovered are you for the next block?*

It's calibrated against shift-work fatigue research, not against the average iPhone user's resting heart rate. A 7-hour daytime sleep before a night shift can produce a higher Shift Recovery Score than an 8-hour night sleep before a day shift, because the former is set up to support the upcoming work block and the latter is misaligned. Generic sleep apps reverse that — daytime sleep gets penalised, night sleep rewarded — which is exactly backwards for this user.

## Caffeine timing is a feature, not a footnote

The other surprise in building AfterShift was how much research exists on caffeine timing for shift workers, and how little of it makes it into consumer apps.

The simplified version: caffeine has a half-life of about five hours. Drinking it three hours before bed leaves enough in your system to disrupt sleep onset and architecture. Drinking it at the start of a night shift will keep you alert at the worst possible time — when you finally try to sleep at 9am. The right strategy depends on which way your shift is rotating, and most shift workers reverse-engineer it through years of trial and error.

AfterShift bakes the strategy in. Tell the app your upcoming shift block, and it will tell you the latest sensible caffeine cutoff to protect your post-shift sleep. It's not glamorous. It is, by user feedback, the single most-mentioned feature.

## What it takes off the user's plate

The other thing I underestimated when I started was how much *administrative load* shift workers carry around their own sleep. Knowing when you slept, knowing when your next shift starts, calculating recovery in your head, deciding whether you need a nap — all of this lives as background processing in their day, on top of the actual job.

AfterShift takes that load. Calendar shift import handles the schedule input automatically (most large employers publish rotations to a calendar feed nurses can subscribe to). The sleep windows are inferred from the existing Apple Health sleep data the user already has. The caffeine timing updates automatically when shifts change. The user doesn't have to keep doing math.

When the math goes away, the cognitive load goes down. When the cognitive load goes down, the actual sleep gets better. This is the second-order effect I didn't predict.

## Who it isn't for

AfterShift isn't a generalist sleep tracker. If you have a stable 9-to-5 schedule, [Observa](/apps/observa/) is the studio's better fit — it does interpretation across all your Apple Health data, with sleep as one of the categories. AfterShift narrows the lens specifically to people whose schedule is the problem.

It is also not a clinical tool. Sleep disorders, narcolepsy, sleep apnoea — these need a sleep clinic, not an app. AfterShift's Shift Recovery Score is informational; it is not a diagnosis. I'd rather lose users to a real doctor than oversell what consumer software can do.

## The point

There's a category of human work that powers most of modern infrastructure — healthcare, transport, public safety, manufacturing — and the consumer software industry has mostly designed around them. Building [AfterShift](/apps/aftershift/) was an experiment in designing *for* them, with the explicit assumption that their schedule isn't a deviation from normal but the actual normal of millions of people.

If you work nights, rotations, or anything that breaks the 9-to-5 mould, the app is on the App Store. And if you know a nurse, pilot, or paramedic who's been quietly suffering with a generic sleep tracker, send them the link.
