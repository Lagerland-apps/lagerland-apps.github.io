---
layout: journal
slug: liftlog-pay-what-you-can
title: "LiftLog ships. You pick the price."
seo:
  title: "LiftLog: A Strength Log With No Subscription, Pay Once"
  description: "A design-led iPhone strength log with no subscription: seven days free, then you pick a one-time price from {P_IAP:Minimum@liftlog} to {P_IAP:Patron@liftlog}. Why we skipped renting."
  keywords:
    - "strength log no subscription"
    - "workout tracker pay once"
    - "lifting log iphone"
    - "no subscription workout app"
    - "pay what you want app"
    - "liftlog"
date: 2026-04-25
last_updated: 2026-10-26
lede: "LiftLog, a design-led strength training log for iPhone, is on the App Store today. It has no subscription. After seven days free with no card on file, you decide what it's worth to you: {P_IAP:Minimum@liftlog}, {P_IAP:Suggested@liftlog}, {P_IAP:Supporter@liftlog}, or {P_IAP:Patron@liftlog}, paid once. This post explains why."
quick_answer: "LiftLog is a design-led iPhone strength training log priced on a pay-what-you-can model. After a seven-day free trial with no card on file, the user picks one of four one-time tiers (Fair {P_IAP:Minimum@liftlog}, Good {P_IAP:Suggested@liftlog}, Generous {P_IAP:Supporter@liftlog}, or Patron {P_IAP:Patron@liftlog}), and all four unlock the same app. There is no subscription and no auto-renew."
faq:
  - q: "How much does LiftLog cost after the free trial?"
    a: "After the seven-day card-free trial, LiftLog offers four one-time tiers: Fair {P_IAP:Minimum@liftlog}, Good {P_IAP:Suggested@liftlog}, Generous {P_IAP:Supporter@liftlog}, or Patron {P_IAP:Patron@liftlog}. All four unlock the same app; a higher price buys no extra features. There is no subscription and no auto-renewal."
  - q: "What is the difference between LiftLog and GymLogger X?"
    a: "GymLogger X is the studio's other strength logger, with an Apple Watch app for logging sets and Pro priced at {P_LIFETIME@gymlogger-x} lifetime or {P_YEARLY@gymlogger-x} a year. LiftLog is iPhone-only and design-led, with a custom haptic keypad and a pay-what-you-can purchase model. If you want to log from the watch, pick GymLogger X. If you live on iPhone and want polish, pick LiftLog."
  - q: "Why does LiftLog use pay-what-you-can pricing instead of a subscription?"
    a: "Strength training history gains value over years, and charging monthly rent on a user's own data felt wrong for a one-person studio. A one-time tier ladder lets the user decide what the app is worth to them, and the training journal stays accessible even if the studio disappears."
  - q: "Does LiftLog require an account or cloud sync?"
    a: "No account is required. Training history stays on your device. There is no third-party tracking, no advertising SDK, and no required login. The App Store processes the pay-what-you-can purchase, so the studio never sees a payment method or email address."
mentioned_apps:
  - liftlog
  - gymlogger-x
read_time: "6 min read"
excerpt: "LiftLog launches as Lagerland Apps's first pay-what-you-can app: a seven-day card-free trial, then a one-time tier the user chooses ({P_IAP:Minimum@liftlog} Fair / {P_IAP:Suggested@liftlog} Good / {P_IAP:Supporter@liftlog} Generous / {P_IAP:Patron@liftlog} Patron). This post covers the bet, the four tiers, why GymLogger X still exists alongside it, and what I'll be watching to see whether the model works."
---

[LiftLog](/apps/liftlog/) is on the App Store today.

The one thing to know about it: **there is no subscription.** You get seven days free with no card on file. After that, you choose a one-time tier between {P_IAP:Minimum@liftlog} and {P_IAP:Patron@liftlog} and you own the app. Nothing auto-renews, there's no trial trap, and a lapsed subscription can never lock you out of your training history.

The rest of this post covers why I built LiftLog this way and what I'm trying to learn from it.

## Subscription pricing is a tax on training history

Strength training is a long-term practice. You keep showing up, week after week, year after year, and the data you build up (the weights you've moved, the personal records you've broken, the volume you've put your body through) gets more valuable the longer you train.

Most workout-tracker apps charge a monthly subscription. Stop paying and you lose the app, and often access to your own history. I find this morally awkward. The user generated the data, and the user's effort produced the personal records. Charging rent on someone's own training journal is the wrong arrangement.

I know the economics. Subscriptions smooth revenue, fund support and pay for ongoing development. Services like Strong, Hevy, and Fitbod have good reasons to use them, and I don't think those teams are doing anything wrong. I wanted to find out whether another model would work for a one-person studio shipping a single, finished product.

So LiftLog is one-time. You pay once, you own it.

## What does "pay what you can" actually mean here?

After the seven-day free trial, the app shows you four tiers:

- **Fair, {P_IAP:Minimum@liftlog}.** The entry tier. If this is the most you can justify for the app, pick it, with no guilt and no asterisk.
- **Good, {P_IAP:Suggested@liftlog}.** The middle. If LiftLog has earned a serious share of your training time and you expect to keep using it, this is where I think most users will land.
- **Generous, {P_IAP:Supporter@liftlog}.** A step up for users who want to support the work, or who have benefited from indie software in the past and want to give back.
- **Patron, {P_IAP:Patron@liftlog}.** The top tier. Same app, no extra unlocks. It exists so people who want to back the studio at a level closer to a year of competitor subscriptions can do that openly, without a hidden option or a tip jar.

All four tiers unlock the same product. Nothing is locked behind a higher number. You choose what LiftLog is worth to you; the features are the same either way.

### Why four tiers and not a slider

A slider would be more flexible, but every UX paper I've read on charitable giving and pay-what-you-want pricing says the same thing: give people too many options and they freeze, and when they freeze, the median amount paid drops. Four tiers give people a real choice without overload.

Four also creates anchoring. If the only options were {P_IAP:Minimum@liftlog} and {P_IAP:Suggested@liftlog}, almost everyone would pick {P_IAP:Minimum@liftlog}. With {P_IAP:Supporter@liftlog} and {P_IAP:Patron@liftlog} visible, {P_IAP:Suggested@liftlog} reads as moderate instead of top-end, and some users will choose to pay above the median. That's the bet.

The labels matter too. Naming the tiers *Fair / Good / Generous / Patron* (and not *Basic / Standard / Plus / Pro*) makes clear that more money doesn't buy more app. It buys the studio more runway, and I want the labels to say so plainly.

## What this is not

A few clarifications, because two friends have already asked:

- **It's not freeware.** The seven-day trial is generous, needs no card and doesn't nag, but after that the app does ask you to choose a tier. I'm not Strava-ing my way into a freemium grind. The trial is real and so is the purchase.
- **It's not a stunt.** This isn't a one-week marketing experiment. Pay-what-you-can is the app's pricing model. If it doesn't work, I'll learn from that and write about it openly. If it does work, it stays.
- **It doesn't scale to everyone.** It works for a one-person studio shipping a finished, focused product. It almost certainly does not work for a SaaS company with ongoing infrastructure costs and a 50-person team. I'm only arguing that it has a place where it fits, and subscriptions can keep the rest.

## Why LiftLog *and* GymLogger X

Lagerland Apps already has a strength training app: [GymLogger X](/apps/gymlogger-x/). It has an Apple Watch app for logging sets from the wrist, generated programs and plateau detection, and costs {P_LIFETIME@gymlogger-x} lifetime or {P_YEARLY@gymlogger-x}/year. That app is staying. People who want a fast logger they can use from Apple Watch should buy GymLogger X; it's the better tool for that job.

LiftLog is a different bet:

- **Design-led, iPhone-first.** Tabular numerics, a custom haptic numeric keypad during sets, a restrained navy palette, and [programs](/journal/choosing-a-strength-program-you-will-finish/) you build yourself, with supersets and giant sets. It's for lifters who care how their tools feel as well as what they do.
- **A pricing experiment.** GymLogger X is the conventional answer (lifetime plus optional annual). LiftLog is the contrarian one (pay what you can, once). I want both in the catalogue so I can learn from both.

If you can't decide, it comes down to this. To log from Apple Watch, get GymLogger X. If you live on iPhone and want polish, get LiftLog. To support an indie studio's pricing experiment, get LiftLog at the Patron tier. Any of these is a fine choice.

## What I'll be watching

I honestly don't know how this will turn out. The questions I want answered:

- **What's the median tier choice?** I expect {P_IAP:Suggested@liftlog} (Good). If it's {P_IAP:Minimum@liftlog} (Fair) by a wide margin, the anchoring isn't working and I need to rethink the labels or the tier ladder.
- **What's the conversion rate from trial to paid tier?** Industry benchmarks for paid trials with no card up front sit around 5 to 15%. Dropping the card requirement reduces friction, but it also drops the auto-renew lock-in behind a lot of "subscription" revenue.
- **Do Patrons cluster geographically or demographically?** I don't track users individually, but the App Store gives me country-level rollups and tier-level revenue. If a lot of Patron purchases come from regions where {P_IAP:Patron@liftlog} is a serious amount of money, that changes how I think about the model.
- **Do reviews mention the pricing?** This is the qualitative signal I care about most. If users find the tier ladder respectful and unusual, the model is working. If it feels gimmicky or guilt-trippy, it isn't, and I'll write a follow-up explaining what I changed.

I'll publish a follow-up here in three to six months with whatever the data says, including the bad numbers if there are any.

## Try it free

If you train, [download LiftLog](/apps/liftlog/). You get seven days of full access with no card. After that, pick a tier or don't, and if you don't, we part on good terms.

If pay-what-you-can pricing isn't for you, [GymLogger X](/apps/gymlogger-x/) costs {P_LIFETIME@gymlogger-x} lifetime. It comes from the same studio with the same privacy principles and a different pricing model.

Either way, your training history stays on your device, with no third-party tracking, no advertising SDKs and no required account. The app is small, the studio is one person, and those principles stay.

---

[LiftLog is available on the App Store.](https://apps.apple.com/app/id6760043411) It's free for seven days with no card required. After the trial you choose a one-time price: {P_IAP:Minimum@liftlog}, {P_IAP:Suggested@liftlog}, {P_IAP:Supporter@liftlog}, or {P_IAP:Patron@liftlog}.
