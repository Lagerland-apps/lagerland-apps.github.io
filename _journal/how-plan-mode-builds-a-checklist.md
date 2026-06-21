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
lede: "Most countdown apps stop at the number of days. Soon.'s Plan Mode goes one step further — it builds a tailored checklist for the event type and schedules each task backward from the date, so you don't have to. Here's exactly how the template engine works, why it's anchored to T-minus rather than T-plus, and what's deliberately not in it."
quick_answer: "Plan Mode is the part of Soon. that turns an event date into a scheduled checklist. Each event type — Trip, Wedding, Birthday, Pregnancy, Graduation, Move, Concert, Anniversary — loads a built-in template of tasks anchored to T-minus offsets (T-90, T-30, T-14, T-3, T-1). When an event is created, Soon. places every task on its own calendar day backward from the event date. Reminders fire on the day each task is due, not as a daily nag. Templates are shipped in the app — no AI generation, no surveillance, no cloud sync."
faq:
  - q: "What is Plan Mode in Soon.?"
    a: "Plan Mode is the planning layer built into every Soon. countdown. When you create an event and pick a type — Trip, Wedding, Birthday, Pregnancy, Graduation, Move, Concert — Plan Mode loads a checklist template for that type, anchors each task to a T-minus offset (e.g. T-30 for 'book transport'), and schedules every task on its own calendar day backward from the event date. You see the checklist; the schedule runs underneath."
  - q: "Why does Plan Mode use T-minus offsets instead of calendar dates?"
    a: "T-minus anchoring (T-30, T-14, T-3) lets a single template work for any event date in any year. A trip in seven months and a trip in three weeks get the same logic — book transport thirty days out, pack three days before — without the template needing to know what year it is. It also makes the checklist legible: 'twenty-one days to go' communicates faster than 'September 14th' when you're scanning a Lock Screen widget."
  - q: "Does Plan Mode use AI to generate the checklist?"
    a: "No. Each template is written once and shipped with the app. There is no AI generation, no inference, no model call. The wedding template was authored by a person; the pregnancy template was authored by a person; the trip template was authored by a person. This is intentional — templates that ship in the binary cannot leak event details to a server, do not vary between users, and do not change between app launches."
  - q: "Can I customise a Plan Mode template?"
    a: "Yes. Every task in a Plan Mode template can be edited, rescheduled, hidden, or replaced. The shipped template is a starting point, not a contract. Add a task at T-50 ('confirm marriage licence requirements'), shift 'pack' from T-3 to T-5, or hide reminders you don't need — your edits apply to that event only, never overwrite the shared template."
  - q: "Do Plan Mode reminders fire all at once?"
    a: "No. If you enable event notifications (Premium), Soon. sends one notification per task on the day that task is due. A trip in 30 days has a single 'book transport' nudge at T-30 — not 30 daily reminders. The free tier never notifies."
mentioned_apps:
  - soon
read_time: "6 min read"
excerpt: "Most countdown apps show you days. Soon.'s Plan Mode shows you what to do with them — event-type templates anchored to T-minus offsets, scheduled backward from the date, no AI involved. Here's the design."
---

The reason most countdown apps stop at days is that days are easy. A date subtracts from another date and the result is a number. You can render that number large, pin a photo behind it, and ship.

Soon. does that too. But the part that turns Soon. into a planner — Plan Mode — is the layer that comes after the number: a checklist of what to actually do between now and the date, tailored to the event type, scheduled backward from the date, and surfaced one task at a time.

This post is the design note for that engine. What it does, what it deliberately doesn't do, and why.

## Templates instead of generation

Every Plan Mode checklist is a template. There are templates for Trip, Wedding, Birthday, Pregnancy, Graduation, Move, Concert, and Anniversary — plus a blank-slate Custom type for anything else.

The templates are authored once, shipped in the app binary, and the same for every user. That is a deliberate choice and worth defending.

The alternative is generation: at event-create time, send the event type and date to a server (or an on-device LLM), get back a personalised checklist. We considered it and decided against it for four reasons.

1. **Generation requires data leaving the device.** Even if the model is local, the design pressure pushes toward "give the model more context so the output is better" — and the more context you collect, the more the privacy guarantee erodes. Templates that ship in the binary cannot leak event details.

2. **Generated checklists are inconsistent.** A wedding template authored once is the same checklist for every user. Two friends comparing notes get the same baseline. A generated checklist is a roll of the dice — sometimes it includes the rehearsal dinner, sometimes it doesn't, sometimes it adds a task that doesn't exist. We optimise for stability.

3. **Authoring is slow and that's a feature.** Writing a good wedding template forces a human to ask "is this the seventh task or the first?" An LLM doesn't ask that. The friction of authoring is the friction of getting it right.

4. **Templates can be audited.** A user can read the entire wedding template before installing the app. There is no hidden layer.

So: every Plan Mode template is a list. A human-authored list. Same list for everyone.

## T-minus, not T-plus

The second design decision is that tasks are anchored to T-minus offsets from the event date, not to absolute calendar dates.

A Plan Mode template entry looks like this internally:

> *Trip · T-14 · "Buy travel adapter, check passport expiry"*

When you create a trip event with a date of, say, August 12th, Plan Mode walks every entry in the template and computes the calendar day from the event date: T-14 becomes July 29th, T-3 becomes August 9th, T-1 becomes August 11th. Every task lands on its own day.

The reason for T-minus rather than calendar dates is that the template needs to work for any event date in any year. A trip in seven months and a trip in three weeks both use the same template; only the anchoring offset changes. It also turns out to be the way humans actually think about prep — *"two weeks before the wedding"* is how you talk to your photographer, not *"July 29th."*

There's a second benefit: T-minus is what widgets render. The Lock Screen, StandBy, and Home Screen widgets all show days-to-go. T-minus is the native unit of the app, so the planning layer speaks the same language.

## One notification per task, not a stream

If you opt into event notifications (Premium), Soon. sends one notification per Plan Mode task on the day that task is due. Not one notification per day. Not one notification per event. One per task.

For a trip 30 days out, the notification stream looks like this across the whole month:

```
T-30  Book flights
T-21  Reserve accommodation
T-14  Buy travel adapter, check passport expiry
T-10  Destination weather appears on widget
T-7   Refill any prescriptions
T-3   Pack (with weather-aware suggestions)
T-1   Charge devices, check-in opens
```

That's seven notifications, spread over a month, each one actionable on the day it arrives. Compare that to the failure mode it replaces: a generic countdown app firing "30 days until your trip!" every morning for thirty mornings. That is noise, not signal.

The free tier of Soon. doesn't notify at all. Plan Mode is visible on the event card and the widget; the notifications layer is a Premium addition for users who want active prompting rather than passive presence.

## What Plan Mode deliberately doesn't do

It doesn't auto-restructure your checklist. If you hide a task, it stays hidden — Soon. doesn't quietly re-add it next week. If you reschedule a task from T-14 to T-21, that's where it lives.

It doesn't share. Soon. is on-device only. Plan Mode checklists don't sync between users, and two people planning the same wedding each install Soon. and create the event independently. (Shared events via opt-in iCloud are on the long-term roadmap; the privacy model has to stay intact.)

It doesn't optimise. There is no algorithm that watches your checklist completions and reweights the template. The template you ship with is the template you get. Personal customisation is your edits, not a model's drift.

It doesn't surveille. Soon. has no analytics SDK, no event-completion telemetry, no "did this notification work" feedback loop reporting home. We don't know — and don't want to know — which tasks users check off, which they ignore, or which they reschedule.

These are not features we forgot to build. They are features we considered, prototyped, and removed.

## The templates, in full

Every Plan Mode template is visible on the [Soon. landing page](/apps/soon/#templates) — Trip (30-day), Wedding (90-day), Pregnancy (40-week), Birthday (14-day), Graduation (21-day), Move (45-day). Each one is the exact task list you get when you create an event of that type, with the exact T-minus offsets that schedule the tasks.

The Pregnancy template is anchored to weeks (Week 28, Week 32, Week 35) rather than days because that's how pregnancy is talked about in clinical and personal contexts. The Wedding template runs to T-90 because the long-tail prep — vendor confirmation, save-the-dates, dress fittings — starts further out than other event types. The Trip template tops out at T-30 because most trips simply aren't planned earlier than that in practice.

Those choices are author judgments, not data-driven optimisations. If they're wrong for your event, you edit them.

## Why this matters beyond Soon.

Most apps that try to do "planning" end up either (a) generic to the point of uselessness, or (b) so configurable that they require setup work users don't want to do. The middle path is event-type-aware templates that ship with sensible defaults, are editable at the seam, and don't try to learn anything about you.

For a countdown app specifically, the engineering load of this is low. A template is a list. A T-minus offset is subtraction. The hard part is authoring the lists well — and that's not a technical problem, it's a writing problem.

If you build planning features into a vertical app — workout, cooking, study, project — the same shape applies: ship templates, anchor them to a meaningful zero (the date, the deadline, the milestone), schedule backward, fire one prompt per task on its day, and stop there. Don't AI it. Don't surveille it. Don't auto-tune it. Just ship the list.

That's all Plan Mode is.

---

[Soon. is available on the App Store.](https://apps.apple.com/app/id6757280643) Free with 5 events forever; Premium unlocks weather intelligence, daily notes, recurring events, and one-task-per-day Plan Mode notifications. The full Plan Mode template gallery is on the [Soon. landing page](/apps/soon/#templates).
