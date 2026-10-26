---
layout: journal
slug: building-a-sleep-app-for-night-shifts
title: "Building a sleep app for nurses, pilots, and the people who don't have a 9-to-5"
seo:
  title: "A Sleep App Built for Night-Shift and Rotating Schedules"
  description: "Most sleep apps assume a 9-to-5. AfterShift is for nurses, pilots, and shift workers on rotating schedules, whose sleep keeps moving with the roster."
  keywords:
    - "sleep app for shift workers"
    - "night shift sleep app"
    - "rotating shift sleep"
    - "shift work sleep"
    - "sleep app nurses"
    - "aftershift"
date: 2026-01-24
last_updated: 2026-10-26
lede: "Most sleep apps assume an 11pm bedtime and a 7am alarm. The people who keep hospitals, planes, and emergency rooms running don't live that way. AfterShift is the app I built after hearing the same complaint from too many friends in scrubs."
quick_answer: "AfterShift is a sleep app for rotating-shift workers such as nurses, pilots, and paramedics, whose schedules break the 9-to-5 assumptions built into generic sleep trackers. It treats daytime sleep blocks and pre-shift naps as normal, calculates a forward-looking Shift Recovery Score, times caffeine cutoffs against upcoming shifts, and imports rotations from calendar feeds automatically."
faq:
  - q: "What is the best sleep app for night shift nurses?"
    a: "AfterShift is made for rotating-shift workers, including ICU and ER nurses. It counts daytime sleep blocks and pre-shift naps as normal sleep instead of penalising them, and its Shift Recovery Score is calibrated against shift-work fatigue research, not the resting heart rate of the average 9-to-5 user."
  - q: "How does AfterShift handle caffeine timing for shift workers?"
    a: "AfterShift uses caffeine's half-life of roughly five hours and your upcoming shift block to recommend the latest sensible cutoff that still protects your post-shift sleep. The recommendation updates automatically when shifts change. Users consistently name caffeine timing as the most useful feature."
  - q: "Can AfterShift import my shift rotation from my employer's calendar?"
    a: "Yes. Most large healthcare and aviation employers publish rotations to a calendar feed staff can subscribe to. AfterShift imports shifts from that calendar so you do not have to enter them by hand (keeping the feed synced automatically in the background is a Premium feature). Sleep windows are planned from your shift times and sleep target, and your actual sleep is read from Apple Health."
  - q: "Is AfterShift a medical device or sleep disorder tool?"
    a: "No. AfterShift is an informational app. Its Shift Recovery Score is not a diagnosis, and the app does not replace a sleep clinic. Suspected sleep disorders such as narcolepsy or apnoea need a clinician to evaluate them."
mentioned_apps:
  - aftershift
  - observa
read_time: "6 min read"
excerpt: "Most sleep apps are designed around the 9-to-5. AfterShift was built for rotating-shift workers such as nurses, pilots, and first responders, with a Shift Recovery Score, caffeine timing set against the next block, and calendar shift import. This post covers the design constraints and what generic sleep apps get wrong about night shift life."
---

A friend who works ICU nights asked me, in 2024, why none of her sleep apps understood what she was doing.

She'd open one of the popular ones, log a five-hour daytime sleep, and the app would politely tell her she'd had a *poor night* and should try going to bed earlier. The app meant well. Its model of a human was someone who sleeps at night. Her model of a human was a nurse who sleeps when the rotation allows.

That conversation was the start of [AfterShift](/apps/aftershift/). This is what I learned building it.

## Why is the 9-to-5 assumption everywhere in sleep apps?

Open any major consumer sleep app and walk through onboarding. You'll be asked when you go to bed, when you wake up, and what your weekend pattern is. The app assumes a five-day workweek with weekends free, and it assumes "night" means one uninterrupted block of darkness.

Now take a typical nurse's twelve-hour rotation: three days on, three days off, a two-week cycle, with days flipping to nights halfway through. Her sleep windows might be 10pm-6am one week and 9am-3pm the next, with a chaotic transition night in between. The sleep app's model breaks, its recovery scores make no sense, and its caffeine recommendations actively harm her. (Most rosters like hers are variations on a handful of named patterns; [rotating shift schedules explained](/journal/rotating-shift-schedules-explained/) lays out DuPont, 2-2-3 and the rest, and which are hardest on sleep.)

This is a real population. The US has about 4 million registered nurses and several hundred thousand commercial pilots, plus paramedics, firefighters, police, factory workers, refinery operators, and a long tail of other rotating-shift workers. Generic sleep apps serve none of them well.

## What "shift-aware" means in practice

The first difference between AfterShift and generic apps is *what counts as a sleep session*. AfterShift accepts:

- A primary sleep block of any length, at any time of day, on any day.
- Optional naps before or after the primary block. Pre-shift naps are a recognised fatigue countermeasure for night work, and post-shift "anchor sleeps" before transitioning back to days are another.
- Fragmented patterns. A six-hour sleep broken once is structurally different from an unbroken six hours, and the app treats it that way.

The second is the **Shift Recovery Score**, the metric I'm proudest of. It isn't a sleep score in the consumer sense. It's a forward-looking estimate: given the sleep you've had since your last shift, the rotation pattern you're on, and how fragmented your recent sleep has been, *how recovered are you for the next block?*

It's calibrated against shift-work fatigue research, not the average iPhone user's resting heart rate. A 7-hour daytime sleep before a night shift can score higher than an 8-hour night sleep before a day shift, because the first one sets you up for the coming work block and the second is misaligned with it. Generic sleep apps penalise the daytime sleep and reward the night sleep, which is backwards for this user.

## Caffeine timing deserves a whole feature

The other surprise in building AfterShift was how much research exists on caffeine timing for shift workers, and how little of it reaches consumer apps.

The short version: caffeine has a half-life of about five hours. A coffee three hours before bed leaves enough in your system to disrupt sleep onset and sleep architecture. A coffee at the start of a night shift keeps you alert when you least want it, at 9am when you finally try to sleep. The right strategy depends on which way your shift is rotating, and most shift workers work it out through years of trial and error.

AfterShift builds the strategy in. Tell the app your upcoming shift block and it gives you the latest sensible caffeine cutoff that still protects your post-shift sleep. It's not glamorous, but going by user feedback it is the most-mentioned feature. The rest of the routine for the day after a night shift, from blackout shades to the nap before the next one, is in [how to sleep after a night shift](/journal/how-to-sleep-after-a-night-shift/).

## What it takes off the user's plate

I also underestimated how much *administrative load* shift workers carry around their own sleep. Knowing when you slept and when your next shift starts, working out recovery in your head, deciding whether you need a nap: all of it runs in the background of their day, on top of the job itself.

AfterShift takes that over. Calendar shift import handles the schedule (most large employers publish rotations to a calendar feed nurses can subscribe to). Sleep windows are planned from the shift times, actual sleep is read from Apple Health, and the caffeine timing updates automatically when shifts change. The user doesn't have to keep doing the math.

With the math gone, the mental load drops, and with less load, people sleep better. I didn't predict that second-order effect.

## Who it isn't for

AfterShift isn't a general sleep tracker. If you have a stable 9-to-5 schedule, [Observa](/apps/observa/) is the better fit from the studio: it interprets all your Apple Health data, with sleep as one of the categories. AfterShift is for people whose schedule is the problem.

It is also not a clinical tool. Sleep disorders such as narcolepsy and sleep apnoea need a sleep clinic. AfterShift's Shift Recovery Score is informational and not a diagnosis. I'd rather lose users to a real doctor than oversell what consumer software can do.

## Why we built it

A whole category of work keeps modern infrastructure running (healthcare, transport, public safety, manufacturing), and consumer software has mostly designed around the people who do it. [AfterShift](/apps/aftershift/) was an experiment in designing *for* them, starting from the assumption that their schedule is the normal life of millions of people and not a deviation from it.

If you work nights, rotations, or anything else that breaks the 9-to-5 mould, the app is on the App Store. And if you know a nurse, pilot, or paramedic who has been putting up with a generic sleep tracker, send them the link.
