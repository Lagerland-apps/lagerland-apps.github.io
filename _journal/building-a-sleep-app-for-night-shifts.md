---
layout: journal
slug: building-a-sleep-app-for-night-shifts
title: "Building a sleep app for nurses, pilots, and the people who don't have a 9-to-5"
seo:
  title: "A Sleep App Built for Night-Shift and Rotating Schedules"
  description: "Most sleep apps assume a 9-to-5. AfterShift is for nurses, paramedics, and other shift workers whose sleep moves with a rotating roster."
  keywords:
    - "sleep app for shift workers"
    - "night shift sleep app"
    - "rotating shift sleep"
    - "shift work sleep"
    - "sleep app nurses"
    - "aftershift"
date: 2026-01-24
last_updated: 2026-10-29
lede: "Most sleep apps assume an 11pm bedtime and a 7am alarm. The people who keep hospitals, airports, and emergency rooms running don't live that way. AfterShift is the app I built after hearing the same complaint from too many friends in scrubs."
quick_answer: "AfterShift is an iPhone sleep app for rotating-shift workers such as nurses, paramedics, and firefighters, whose schedules break the 9-to-5 assumptions built into generic sleep trackers. It measures sleep shift to shift instead of midnight to midnight, with naps included, reads your sleep from Apple Health, fills your roster from a repeating rotation, and times wind-down, caffeine cut-off, and nap reminders to your next shift. A Readiness rating for the next shift is part of Premium."
faq:
  - q: "What is the best sleep app for night shift nurses?"
    a: "AfterShift is made for rotating-shift workers, including ICU and ER nurses. It measures your sleep in the window between one shift and the next, so a daytime sleep block or a pre-shift nap counts toward the sleep between your shifts instead of being judged against a night you didn't have. With Premium, a Readiness rating tells you how recovered you are for the next shift. Its scores are informational, not clinically validated."
  - q: "How does AfterShift handle caffeine timing for shift workers?"
    a: "AfterShift sends a caffeine cut-off reminder timed to your next shift. The cut-off adapts to what you drank and to the caffeine sensitivity you set. On the Today tab, you log a coffee in one tap, or long-press for espresso, an energy drink, or tea."
  - q: "Can AfterShift import my shift rotation from my employer's calendar?"
    a: "Yes. If your employer publishes the roster to a calendar you subscribe to, AfterShift can read it and detect your shifts. The free version imports from one calendar, by hand, for the next 14 days. Premium adds multiple calendars, automatic sync each time you open the app, and overtime tracking. You can also set a repeating rotation once and let the app fill the next 8 weeks. Your actual sleep is read from Apple Health."
  - q: "Is AfterShift a medical device or sleep disorder tool?"
    a: "No. AfterShift is an informational app. Its scores are not a diagnosis, and the app does not replace a sleep clinic. Suspected sleep disorders such as narcolepsy or apnoea need a clinician to evaluate them."
mentioned_apps:
  - aftershift
  - observa
read_time: "6 min read"
excerpt: "Most sleep apps are designed around the 9-to-5. AfterShift was built for rotating-shift workers such as nurses, paramedics, and firefighters, with recovery measured shift to shift, caffeine cut-off reminders timed to the next shift, and calendar shift import. This post covers the design constraints and what generic sleep apps get wrong about night shift life."
---

A friend who works ICU nights asked me, in 2024, why none of her sleep apps understood what she was doing.

She'd open one of the popular ones, log a five-hour daytime sleep, and the app would politely tell her she'd had a *poor night* and should try going to bed earlier. The app meant well. Its model of a human was someone who sleeps at night. Her model of a human was a nurse who sleeps when the rotation allows.

That conversation was the start of [AfterShift](/apps/aftershift/). This is what I learned building it.

## Why is the 9-to-5 assumption everywhere in sleep apps?

Open any major consumer sleep app and walk through onboarding. You'll be asked when you go to bed, when you wake up, and what your weekend pattern is. The app assumes a five-day workweek with weekends free, and it assumes "night" means one uninterrupted block of darkness.

Now take a typical nurse's twelve-hour rotation: three days on, three days off, a two-week cycle, with days flipping to nights halfway through. Her sleep windows might be 10pm-6am one week and 9am-3pm the next, with a chaotic transition night in between. The sleep app's model breaks, its recovery scores make no sense, and its caffeine recommendations actively harm her. (Most rosters like hers are variations on a handful of named patterns; [rotating shift schedules explained](/journal/rotating-shift-schedules-explained/) lays out DuPont, 2-2-3 and the rest, and which are hardest on sleep.)

This is a real population. The US has about 4 million registered nurses, plus paramedics, firefighters, factory and logistics workers, airport ground crews, hotel and overnight staff, and a long tail of other people on rotating shifts or on call. Generic sleep apps serve none of them well.

## What "shift-aware" means in practice

The first difference between AfterShift and generic apps is *what counts as a sleep session*. AfterShift accepts:

- A primary sleep block of any length, at any time of day, on any day.
- Naps before or after the primary block. Pre-shift naps are a recognised fatigue countermeasure for night work, and post-shift "anchor sleeps" before transitioning back to days are another. In AfterShift, naps count toward the sleep between your shifts.
- Fragmented patterns. A six-hour sleep broken once is structurally different from an unbroken six hours. With Premium, a Sleep Continuity card shows how broken each sleep was.

The second difference is the day itself. AfterShift measures from the end of one shift to the start of the next, not from midnight to midnight. Sleep debt, the Recovery Timeline, and the Readiness rating all work on that window.

Readiness is the part I'm proudest of. It answers one question: *given the sleep you've had since your last shift, are you recovered enough for the next one?* It compares the sleep inside that window with your sleep target and rates you Low, OK, or Good. Readiness is part of Premium, as are the Sleep Score and Shift Recovery Score for each sleep. The Shift Recovery Score weighs duration, continuity, and sleep stages.

Generic sleep apps tend to penalise the daytime sleep before a night shift because it doesn't look like a night. AfterShift measures it against the window you actually had, which is the fair comparison for this user. Like every score in the app, Readiness is an informational rule of thumb and hasn't been clinically validated.

## Caffeine timing deserves a whole feature

The other surprise in building AfterShift was how much research exists on caffeine timing for shift workers, and how little of it reaches consumer apps.

The short version: caffeine has a half-life of about five hours. A coffee three hours before bed leaves enough in your system to disrupt sleep onset and sleep architecture. A coffee at the start of a night shift keeps you alert when you least want it, at 9am when you finally try to sleep. The right strategy depends on which way your shift is rotating, and most shift workers work it out through years of trial and error.

AfterShift builds part of that in. It sends a caffeine cut-off reminder timed to your next shift, and the cut-off adapts to what you drank and to your caffeine sensitivity. It's not glamorous, but it answers a question shift workers otherwise answer by guesswork. The rest of the routine for the day after a night shift, from blackout shades to the nap before the next one, is in [how to sleep after a night shift](/journal/how-to-sleep-after-a-night-shift/).

## What it takes off the user's plate

I also underestimated how much *administrative load* shift workers carry around their own sleep. Knowing when you slept and when your next shift starts, working out recovery in your head, deciding whether you need a nap: all of it runs in the background of their day, on top of the job itself.

AfterShift takes some of that over. Set your rotation once and the app fills the next 8 weeks of your roster, or import shifts from the calendar your employer publishes (one calendar by hand in the free version; automatic sync across several calendars with Premium). Sleep windows are planned from your shift times, actual sleep is read from Apple Health, and the wind-down, caffeine cut-off, and nap reminders are set relative to your next shift instead of the clock on the wall. The user doesn't have to keep doing the math.

## Who it isn't for

AfterShift isn't a general sleep tracker. If you have a stable 9-to-5 schedule, [Observa](/apps/observa/) is the better fit from the studio: it interprets all your Apple Health data, with sleep as one of the categories. AfterShift is for people whose schedule is the problem.

It is also not a clinical tool. Sleep disorders such as narcolepsy and sleep apnoea need a sleep clinic. AfterShift's scores are informational and not a diagnosis. I'd rather lose users to a real doctor than oversell what consumer software can do.

## Why we built it

A whole category of work keeps modern infrastructure running (healthcare, transport, public safety, manufacturing), and consumer software has mostly designed around the people who do it. [AfterShift](/apps/aftershift/) was an experiment in designing *for* them, starting from the assumption that their schedule is the normal life of millions of people and not a deviation from it.

If you work nights, rotations, or anything else that breaks the 9-to-5 mould, the app is on the App Store for iPhone. And if you know a nurse, paramedic, or firefighter who has been putting up with a generic sleep tracker, send them the link.
