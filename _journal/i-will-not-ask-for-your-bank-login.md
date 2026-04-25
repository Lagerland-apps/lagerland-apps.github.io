---
layout: journal
slug: i-will-not-ask-for-your-bank-login
title: "I will not ask for your bank login"
date: 2026-01-31
lede: "It's the last day of January and the bank-aggregator apps are advertising themselves into every podcast in America. The pitch is convenience. The price is your read access to your own checking account. AllPaid takes the other path on purpose."
read_time: "5 min read"
excerpt: "Most modern bill-tracking apps connect to your bank through Plaid or a similar aggregator. AllPaid is intentionally manual-first. This post explains the structural reasons against bank linking, what users actually trade away, and why a manual entry tool can compete on convenience anyway."
---

It is the last Saturday of January. I have just done my own taxes for the year, which is a job I always do badly and never on time. While doing them I noticed that three of the apps on the *Productivity* charts of the App Store are bill trackers that connect to your bank. Two of them have grown sharply in the last twelve months. All of them open with the same onboarding flow:

> *To get started, please log in to your bank.*

[AllPaid](/apps/allpaid/), the bill-tracking and subscription-management app this studio ships, does not have that flow and is not going to. This is the post explaining why.

## What "log in to your bank" actually does

When a non-bank app asks you to log in to your bank, what's happening underneath isn't quite what most users think.

You're typing your bank password into a third-party screen. That third party is almost always **Plaid**, occasionally MX or Finicity. The third party stores credentials or — in newer arrangements — holds an OAuth token issued by your bank. Either way, the third party gets persistent **read access** to your account. Transactions, balances, and often historical statements.

The app you actually wanted to use then connects to *the third party*, not your bank, and pulls a feed of transactions filtered through that aggregator's models.

This isn't shady. It's the standard architecture of fintech, it's regulated, and most of the time it works. But it has three properties worth being honest about:

1. **Your bank credentials, or a token derived from them, now live somewhere they didn't live before.** That somewhere is a target.
2. **The aggregator can see every transaction in your account, in perpetuity, until you revoke access.** Even when the app you signed up for doesn't need that data.
3. **Aggregators are a business.** Their growth depends on cross-selling the data they aggregate to other applications, anonymised or otherwise. The anonymisation is sometimes meaningful and sometimes not.

I don't think aggregators are evil. I do think the convenience tradeoff isn't priced into the user's mental model when they tap *Continue* on the onboarding screen.

## What you're actually buying

The promise of bank-linked bill apps is that they will *find* your subscriptions and bills automatically. You sign up, give them read access, and a list of recurring charges appears.

This works! It is genuinely useful! It is also doing two specific things, and one of them is unrelated to the user's stated goal.

The first thing it does is identify recurring charges. Useful.

The second thing it does is build a picture of *every other thing* you spend money on, which is not what you signed up for and is the actual asset the company is building. The bill-tracking is a pretext for the data pipeline. Some of these companies are open about it (the ones whose business model is "find subscriptions you forgot about and offer to cancel them" — that's the value exchange). Some are quieter.

Either way, the user is paying with read access to their entire financial life for a feature that, in the end, is a list of things they could have written down themselves in twenty minutes.

## The manual-first answer

[AllPaid](/apps/allpaid/) is built around the opposite premise: most people have somewhere between five and forty recurring bills, and entering them once is not a difficult problem.

The app is manual-first. You type in your bills, your subscriptions, the rent, the utilities. The app stores them locally on your device, reminds you when they're due, supports a calendar view, lets you tick them off, and shares specific bills with a partner if needed. Widgets and Siri integration mean the daily friction is essentially zero — *"Hey Siri, what's due this week?"* takes one tap. There's a Pro tier that adds spending analytics and full payment history, also fully on-device.

What the app does not do, and will not do:

- It does not connect to your bank.
- It does not connect to a third-party aggregator.
- It does not have an account system. There is no login, no email collection, no profile.
- It does not see anything you do not type into it.

This is, on paper, less convenient than a Plaid-connected app. In practice, the convenience gap is smaller than people expect. The first-time entry takes about fifteen minutes if you have a long list. After that, the friction is a notification you tap to mark a bill paid — same friction, lower cost.

## What this trades away

I want to be precise about the tradeoff, because hand-waving it is dishonest.

Bank-linked bill apps catch one category of bill that AllPaid will miss: **the subscription you signed up for, forgot about, and would not remember to enter into a manual app**. The classic "$8.99/month for that streaming service you used twice in 2023." This is a real value proposition, and AllPaid does not solve it.

If finding forgotten charges is the user's primary need, a bank-linked tool is the better fit, and I'd recommend one honestly. The user just needs to walk in with their eyes open about what they are giving up.

For everyone else — the user who knows roughly what they pay for, wants to be reminded to actually pay, wants to share rent with a roommate, wants a calendar view of the next thirty days, and does not want a third party reading their checking account in perpetuity — manual-first works.

## A note on tax season

This post is going up on the 31st of January, and I am aware the timing is not accidental. Tax season is when people look at their finances most carefully and most apprehensively. It is also the season when fintech apps run their biggest advertising spend, because conversion is highest when anxiety is highest.

The point of [AllPaid](/apps/allpaid/) is to be the calmer answer in that window. No bank login. No surveillance. No anxiety-driven onboarding. Just the boring, useful, local thing that helps you not miss a bill and not pay a late fee. Costs $1.99 a month or $24.99 lifetime, no subscription required.

If this is the year you stop handing over read-access to your bank in exchange for features you could write yourself, this is the studio that thinks you're right.
