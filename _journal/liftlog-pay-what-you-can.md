---
layout: journal
slug: liftlog-pay-what-you-can
title: "LiftLog ships. You pick the price."
date: 2026-04-25
lede: "LiftLog — a design-led strength training log for iPhone — is on the App Store today. There is no subscription. After seven days free with no card on file, you decide what it's worth to you: $9.99, $19.99, $29.99, or $39.99. Once. Here's why."
read_time: "6 min read"
excerpt: "LiftLog launches as Lagerland Apps's first pay-what-you-can app — a seven-day card-free trial followed by a one-time tier the user chooses ($9.99 Fair / $19.99 Good / $29.99 Generous / $39.99 Patron). This post explains the bet, the four tiers, why GymLogger X still exists alongside it, and what I'll be watching to learn whether the model works."
---

[LiftLog](/apps/liftlog/) is on the App Store today.

If you only read one thing about it, read this: **there is no subscription.** Seven days free, no card on file. After that, you choose a one-time tier between $9.99 and $39.99 and you own the app. No auto-renew. No trial trap. Your training history is never held hostage by a lapsed subscription.

The rest of this post is about why I built LiftLog this way, and what I'm trying to learn by doing it.

## Subscription pricing is a tax on training history

Strength training is a long-term practice. The whole point is that you keep showing up, week after week, year after year, and the data you accumulate — the weights you've moved, the personal records you've broken, the volume you've put your body through — gets more valuable the longer you train.

Most workout-tracker apps charge a monthly subscription. The implication is straightforward: you stop paying, you lose the app, you often lose access to your own history. I find this morally awkward. The user generated the data. The user's effort produced the personal records. Charging rent on someone's own training journal feels like the wrong shape for the relationship.

I'm not naïve about the economics. Subscriptions smooth revenue, they fund support, they pay for ongoing development. There are good reasons services like Strong, Hevy, and Fitbod use them — and I don't think those teams are doing anything wrong. But I wanted to find out whether a different shape would work for a one-person studio shipping a single, finished product.

So LiftLog is one-time. You pay once, you own it.

## What "pay what you can" actually means here

After the seven-day free trial, the app shows you four tiers:

- **Fair — $9.99.** The entry tier. If LiftLog is genuinely the cheapest version of the app you can justify, this is the right choice. No guilt, no asterisk.
- **Good — $19.99.** The middle. If LiftLog has earned a serious amount of your training time and feels like the tool you'll keep using, this is the calibration most users will land on.
- **Generous — $29.99.** A step up for users who want the work supported, or who have benefited from indie software in the past and choose to lean in.
- **Patron — $39.99.** The top tier. Same app, no extra unlocks. This tier exists so people who want to back the studio at a level closer to a year of competitor subscriptions have a way to do that — without it being awkward, hidden, or a tip jar.

All four tiers unlock the same product. No content gating, no "premium" features behind a higher number. The choice is about what LiftLog is worth to you, not about which features you get.

### Why four tiers and not a slider

A slider would be more flexible, but every UX paper I've ever read on charitable giving and pay-what-you-want pricing says the same thing: when you give people too many options, they freeze, and when they freeze, the median paid amount drops. Four tiers gives people meaningful agency without overload.

Four also creates anchoring. If the only options were $9.99 and $19.99, almost everyone would pick $9.99. With $29.99 and $39.99 visible, $19.99 reads as moderate rather than top-end — and a meaningful number of users will choose to support the work above the median. That's the bet.

The labels matter too. Calling the tiers *Fair / Good / Generous / Patron* — instead of *Basic / Standard / Plus / Pro* — does something I want this app to do everywhere: it removes the implication that more money buys you more app. It doesn't. It buys the studio more runway. That distinction should be honest, not obscured.

## What this is not

A few clarifications, because I've already had two friends ask:

- **It's not freeware.** The seven-day trial is generous, no-card, no-pressure — but after that the app does ask you to choose a tier. I am not Strava-ing my way into a freemium grind. The trial is real; the purchase is real.
- **It's not a stunt.** I'm not running this as a one-week marketing experiment. Pay-what-you-can is the app's pricing model, full stop. If it doesn't work, I'll learn from that and write about it openly. If it does work, it stays.
- **It's not infinitely scalable.** This works for a one-person studio shipping a finished, focused product. It almost certainly does not work for a SaaS company with ongoing infrastructure costs and a 50-person team. I'm not arguing this should replace subscriptions everywhere — only that there's room for it in places where it fits.

## Why LiftLog *and* GymLogger X

Lagerland Apps already has a strength training app: [GymLogger X](/apps/gymlogger-x/). Apple Watch is a first-class client; Smart Programs and plateau detection do real work; the price is $44.99 lifetime or $17.99/year. That app is not going anywhere. People who want a fast Apple-Watch-led logger should buy GymLogger X — it's the better tool for that job.

LiftLog is a different bet:

- **Design-led, iPhone-first.** Tabular numerics, a custom haptic numeric keypad during sets, a restrained dark navy palette, periodized programs visualized as a clean dashboard. This is the app for lifters who care how their tools feel, not just what they do.
- **A pricing experiment.** GymLogger X is the conventional answer (lifetime + optional annual). LiftLog is the contrarian one (pay what you can, once). I want both in the catalogue so I can learn from both.

If you can't decide between them, the heuristic is simple: live on Apple Watch and want speed → GymLogger X. Live on iPhone and want polish → LiftLog. Want to support an indie studio's pricing experiment → LiftLog at the Patron tier. None of these are wrong answers.

## What I'll be watching

I'm going into this honestly uncertain about the outcome. The questions I want answered:

- **What's the median tier choice?** I expect $19.99 (Good). If it's $9.99 (Fair) by a wide margin, that tells me the anchoring isn't doing its job and I need to rethink the labels or the tier ladder.
- **What's the conversion rate from trial to paid tier?** Industry benchmarks for paid trials with no card up front sit around 5–15%. Removing the card requirement reduces friction, but it also removes the auto-renew lock-in that drives a lot of "subscription" revenue.
- **Do Patrons cluster geographically or demographically?** I don't track users individually, but the App Store gives me country-level rollups and tier-level revenue. If meaningful Patron volume comes from regions where $39.99 is a serious amount of money, that changes how I think about the model.
- **Do reviews mention the pricing?** This is the qualitative signal I care most about. If users find the tier ladder respectful and unusual, the model is working as intended. If it feels gimmicky or guilt-trippy, it's not — and I'll write a follow-up explaining what I changed.

I'll publish a follow-up here in three to six months with whatever the data says. Honest numbers, including the bad ones if they're bad.

## Try it free

If you train, [download LiftLog](/apps/liftlog/). Seven days, no card, full access. After that, pick a tier or don't — and if you don't, we part on good terms.

If pay-what-you-can pricing isn't your thing, [GymLogger X](/apps/gymlogger-x/) is right there at $44.99 lifetime. Same studio, same privacy principles, different shape.

Either way, your training history stays on your device, no third-party tracking, no advertising SDKs, no required account. The app is small. The studio is one person. The principles aren't going anywhere.

That's the whole thing.

---

[LiftLog is available on the App Store.](https://apps.apple.com/app/id6760043411) Free for seven days, no card required. After the trial: $9.99, $19.99, $29.99, or $39.99 — one-time, you choose.
