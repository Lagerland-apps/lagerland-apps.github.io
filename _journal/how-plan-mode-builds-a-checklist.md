---
layout: journal
slug: how-plan-mode-builds-a-checklist
title: "How Plan Mode builds a wedding (or trip, or pregnancy) checklist"
seo:
  title: "A Countdown App That Builds Your Event Checklist for You"
  description: "Most countdown apps stop at the day count. Soon.'s Plan Mode builds a wedding, trip, or pregnancy checklist and schedules each task backward from the date."
  keywords:
    - "wedding countdown checklist"
    - "trip planning checklist app"
    - "event checklist app"
    - "countdown with checklist"
    - "pregnancy countdown"
    - "soon app"
date: 2026-05-13
lede: "Most countdown apps stop at the number of days. Soon.'s Plan Mode also builds a checklist for the event type and schedules each task backward from the date. This is how the template engine works, why it counts down to the date (T-minus) and not up from today (T-plus), and what we left out on purpose."
quick_answer: "Plan Mode is the part of Soon. that turns an event date into a scheduled checklist. Each event type (Trip, Wedding, Birthday, Pregnancy, Graduation, Move, Concert, Anniversary) loads a built-in template of tasks anchored to T-minus offsets (T-90, T-30, T-14, T-3, T-1). When an event is created, Soon. places every task on its own calendar day backward from the event date. Reminders fire on the day each task is due, with no daily nag. The templates ship inside the app, and Plan Mode uses no AI generation, no tracking and no cloud sync."
faq:
  - q: "What is Plan Mode in Soon.?"
    a: "Plan Mode is the planning layer built into every Soon. countdown. When you create an event and pick a type (Trip, Wedding, Birthday, Pregnancy, Graduation, Move, Concert), Plan Mode loads a checklist template for that type, anchors each task to a T-minus offset (e.g. T-30 for 'book transport'), and schedules every task on its own calendar day backward from the event date. You see the checklist; the schedule runs underneath."
  - q: "Why does Plan Mode use T-minus offsets instead of calendar dates?"
    a: "T-minus anchoring (T-30, T-14, T-3) lets a single template work for any event date in any year. A trip in seven months and a trip in three weeks get the same logic (book transport thirty days out, pack three days before) without the template needing to know what year it is. It also makes the checklist easier to read: 'twenty-one days to go' communicates faster than 'September 14th' when you're scanning a Lock Screen widget."
  - q: "Does Plan Mode use AI to generate the checklist?"
    a: "No. Each template is written once and shipped with the app, and no model is called at any point. A person wrote the wedding, pregnancy, and trip templates. We did this on purpose: templates that ship in the binary cannot leak event details to a server, are the same for every user, and do not change between app launches."
  - q: "Can I customise a Plan Mode template?"
    a: "Yes. Every task in a Plan Mode template can be edited, rescheduled, hidden, or replaced. The shipped template is only a starting point. Add a task at T-50 ('confirm marriage licence requirements'), shift 'pack' from T-3 to T-5, or hide reminders you don't need. Your edits apply to that event only and never overwrite the shared template."
  - q: "Do Plan Mode reminders fire all at once?"
    a: "No. If you enable event notifications (Premium), Soon. sends one notification per task on the day that task is due. A trip in 30 days gets a single 'book transport' nudge at T-30, where a daily countdown would send 30 reminders. The free tier never notifies."
mentioned_apps:
  - soon
read_time: "6 min read"
excerpt: "Most countdown apps show you days. Soon.'s Plan Mode shows you what to do with them, using event-type templates anchored to T-minus offsets and scheduled backward from the date, with no AI involved. A note on the design."
last_updated: 2026-10-26
---

Most countdown apps stop at days because days are easy. Subtract one date from another and you get a number. You can render that number large, pin a photo behind it, and ship.

Soon. does that too. Plan Mode is the layer after the number, and it is what makes Soon. a planner: a checklist of what to do between now and the date, matched to the event type, scheduled backward from the date, and shown one task at a time.

This post is the design note for that engine: what it does, what it leaves out on purpose, and why.

## Templates instead of generation

Every Plan Mode checklist is a template. There are templates for Trip, Wedding, Birthday, Pregnancy, Graduation, Move, Concert, and Anniversary, plus a blank Custom type for anything else.

The templates are written once, shipped in the app binary, and the same for every user. We chose that on purpose, and the choice needs some defending.

The alternative is generation: when an event is created, send the event type and date to a server (or an on-device LLM) and get back a personalised checklist. We considered it and decided against it for four reasons.

1. **Generation requires data leaving the device.** Even with a local model, the design pressure is to give the model more context so the output gets better, and the more context you collect, the weaker the privacy guarantee gets. Templates that ship in the binary cannot leak event details.

2. **Generated checklists are inconsistent.** A wedding template written once is the same checklist for every user, so two friends comparing notes start from the same baseline. A generated checklist might include the rehearsal dinner one time and skip it the next, or add a task that doesn't exist. We optimise for stability.

3. **Writing templates by hand is slow, and that helps.** Writing a good wedding template forces a person to ask whether a task comes seventh or first. An LLM doesn't ask that, and the slow part of writing is where the order gets fixed.

4. **Templates can be audited.** A user can read the entire wedding template before installing the app. Nothing is hidden behind it.

So every Plan Mode template is a list, written by a person, and the same for everyone.

## T-minus, not T-plus

The second design decision is that tasks are anchored to T-minus offsets from the event date, not to calendar dates.

A Plan Mode template entry looks like this internally:

> *Trip · T-14 · "Buy travel adapter, check passport expiry"*

When you create a trip event with a date of, say, August 12th, Plan Mode walks every entry in the template and computes its calendar day from the event date: T-14 becomes July 29th, T-3 becomes August 9th, T-1 becomes August 11th. Every task lands on its own day.

Offsets let the template work for any event date in any year. A trip in seven months and a trip in three weeks use the same template; only the dates the offsets land on change. It is also how people think about prep. You tell your photographer *"two weeks before the wedding,"* not *"July 29th."*

The widgets benefit too. The Lock Screen, StandBy, and Home Screen widgets all show days to go, so T-minus is already the app's native unit, and the planning layer uses the same one.

## One notification per task

If you opt into event notifications (Premium), Soon. sends one notification per Plan Mode task, on the day that task is due. That means no daily notification and no single notification for the whole event.

For a trip 30 days out, the notifications across the month look like this:

```
T-30  Book flights
T-21  Reserve accommodation
T-14  Buy travel adapter, check passport expiry
T-10  Destination weather appears on widget
T-7   Refill any prescriptions
T-3   Pack (with weather-aware suggestions)
T-1   Charge devices, check-in opens
```

That's seven notifications over a month, each one something you can act on the day it arrives. A generic countdown app would fire "30 days until your trip!" every morning for thirty mornings, which tells you nothing new.

The free tier of Soon. doesn't notify at all. Plan Mode shows on the event card and the widget; notifications are a Premium addition for people who want to be prompted, where the free tier only shows the list.

## What Plan Mode leaves out

It doesn't restructure your checklist. If you hide a task, it stays hidden, and Soon. won't re-add it next week. If you move a task from T-14 to T-21, that is where it stays.

It doesn't share. Soon. is on-device only. Plan Mode checklists don't sync between users, so two people planning the same wedding each install Soon. and create the event separately. (Shared events through opt-in iCloud are on the long-term roadmap, and the privacy model has to survive that change.)

It doesn't optimise. No algorithm watches which tasks you complete and reweights the template. The template you start with is the template you get, and any personalisation comes from your own edits.

It doesn't track you. Soon. has no analytics SDK, no event-completion telemetry, and no feedback loop reporting whether a notification worked. We don't know which tasks users check off, ignore, or reschedule, and we don't want to.

We didn't forget these features. We considered and prototyped each of them, then removed them.

## The templates, in full

Every Plan Mode template is listed on the [Soon. landing page](/apps/soon/#templates): Trip (30-day), Wedding (90-day), Pregnancy (40-week), Birthday (14-day), Graduation (21-day), Move (45-day). Each is the exact task list you get when you create an event of that type, with the exact T-minus offsets that schedule the tasks.

The Pregnancy template counts in weeks (Week 28, Week 32, Week 35) because that's how pregnancy is discussed, by clinicians and by everyone else. The Wedding template starts at T-90 because the slow prep (vendor confirmation, save-the-dates, dress fittings) begins earlier than for other events. The Trip template starts at T-30 because in practice most trips aren't planned further ahead than that.

Those offsets are the author's judgement, with no usage data behind them. If they're wrong for your event, edit them.

## Beyond Soon.

Most apps that try to do planning end up either (a) too generic to be useful, or (b) so configurable that they need setup work nobody wants to do. Templates per event type sit between the two: they ship with sensible defaults, can be edited, and don't try to learn anything about you.

For a countdown app the engineering is light. A template is a list, and a T-minus offset is subtraction. The hard part is writing the lists well, which is a writing problem more than a technical one.

If you build planning features into a vertical app (workout, cooking, study, project), the same shape works: ship templates, anchor them to a meaningful zero such as the date, the deadline or the milestone, schedule backward, fire one prompt per task on its day, and stop there. Leave out the AI, the tracking and the auto-tuning, and ship the list.

---

[Soon. is available on the App Store.](https://apps.apple.com/app/id6757280643) It is free with 5 events, with no time limit; Premium unlocks weather intelligence, daily notes, recurring events, and one-task-per-day Plan Mode notifications. The full Plan Mode template gallery is on the [Soon. landing page](/apps/soon/#templates).
