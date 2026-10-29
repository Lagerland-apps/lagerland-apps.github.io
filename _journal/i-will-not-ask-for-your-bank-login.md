---
layout: journal
slug: i-will-not-ask-for-your-bank-login
title: "I will not ask for your bank login"
seo:
  title: "A Bill Tracker That Never Asks for Your Bank Login"
  description: "Bank-aggregator apps want read access to your checking account. AllPaid tracks bills and subscriptions manually, on purpose, without a bank login or Plaid."
  keywords:
    - "bill tracker without bank login"
    - "expense tracker no bank connection"
    - "subscription tracker no plaid"
    - "manual bill tracker"
    - "no bank link finance app"
    - "allpaid"
date: 2026-01-31
last_updated: 2026-10-29
lede: "It's the last day of January and the bank-aggregator apps are advertising themselves into every podcast in America. The pitch is convenience. The price is your read access to your own checking account. AllPaid deliberately skips the bank connection."
quick_answer: "Bill tracker apps that ask for bank logins route credentials through aggregators like Plaid, which can usually read every transaction in the account until you revoke access, far more than the recurring charges the user wants to see. AllPaid never connects to a bank. You add bills by hand, they stay on your iPhone, and there is no account to create."
faq:
  - q: "Is there a bill tracker that does not require connecting to my bank?"
    a: "AllPaid is a manual-first iOS bill and subscription tracker that never connects to a bank or to an aggregator like Plaid. You type each bill in once and the app keeps it on your iPhone. There is no account, so AllPaid never asks for your email. Nothing leaves the phone unless you share a bill or turn on iCloud Sync (Pro), which uses your own private iCloud."
  - q: "What does Plaid actually see when a bill app asks me to log in to my bank?"
    a: "Plaid stores credentials or an OAuth token derived from them and gains persistent read access to every transaction in the account, not only recurring charges. That access continues until you revoke it. Aggregators are regulated businesses, and the data also feeds their wider products, which onboarding screens rarely mention."
  - q: "Will AllPaid catch forgotten subscriptions I do not remember paying for?"
    a: "No. In that one case a bank-linked app has a real edge. If finding forgotten charges from years ago is your main need, an aggregator-based tool is the better fit. AllPaid is for people who know roughly what they pay for and want reminders without handing over their transaction history."
  - q: "How much does AllPaid cost?"
    a: "AllPaid is free for up to 3 bills, with reminders, contract end dates, all ten widgets, Siri, and App Lock. Pro adds unlimited bills, more reminders, Spending Analytics, payment history, and iCloud Sync for {P_MONTHLY@allpaid} a month, {P_YEARLY@allpaid} a year, or {P_LIFETIME@allpaid} once. You never create an account, and the app carries no ads, analytics, or third-party SDKs."
mentioned_apps:
  - allpaid
read_time: "5 min read"
excerpt: "Most modern bill-tracking apps connect to your bank through Plaid or a similar aggregator. AllPaid is intentionally manual-first. This post explains the structural reasons against bank linking, what users trade away, and why a manual entry tool can still compete on convenience."
---

It is the last Saturday of January. I have just done my own taxes for the year, which is a job I always do badly and never on time. While doing them I noticed that three of the apps on the *Productivity* charts of the App Store are bill trackers that connect to your bank. Two of them have grown sharply in the last twelve months. All of them open with the same onboarding flow:

> *To get started, please log in to your bank.*

[AllPaid](/apps/allpaid/), the bill-tracking and subscription-management app this studio ships, does not have that flow and is not going to. This post explains why.

## What does "log in to your bank" actually do?

When a non-bank app asks you to log in to your bank, what happens underneath isn't quite what most users think. You're typing your bank password into a third-party screen. That third party is almost always **Plaid**, occasionally MX or Finicity. The third party stores your credentials or, in newer arrangements, holds an OAuth token issued by your bank. Either way it gets persistent **read access** to your account: transactions, balances, and often historical statements.

The app you actually wanted to use then connects to *the third party*, not your bank, and pulls a feed of transactions filtered through that aggregator's models.

This is the standard architecture of fintech. It's regulated, and most of the time it works. It also has three properties that users should know about:

1. **Your bank credentials, or a token derived from them, now live somewhere they didn't live before.** That somewhere is a target.
2. **The aggregator can see every transaction in your account, in perpetuity, until you revoke access**, including when the app you signed up for doesn't need that data.
3. **Aggregators are a business.** Their growth depends on cross-selling the data they aggregate to other applications, anonymised or otherwise. The anonymisation is sometimes meaningful and sometimes not.

I don't think aggregators are evil. I do think the convenience tradeoff isn't priced into the user's mental model when they tap *Continue* on the onboarding screen.

## What you're actually buying

The promise of bank-linked bill apps is that they will *find* your subscriptions and bills automatically. You sign up, give them read access, and a list of recurring charges appears.

This works, and it is genuinely useful. It is also doing two things, and only one of them is what the user asked for.

The first is identifying recurring charges, which is the useful part.

The second is building a picture of *every other thing* you spend money on, which you never signed up for and which is the asset the company is actually building. The bill tracking is a pretext for the data pipeline. Some of these companies are open about it (for the ones whose business model is "find subscriptions you forgot about and offer to cancel them", that is the value exchange). Some are quieter.

Either way, the user pays with read access to their entire financial life for a feature that comes down to a list they could have written themselves in twenty minutes.

## The manual-first answer

[AllPaid](/apps/allpaid/) starts from a different premise: most people have somewhere between five and forty recurring bills, and entering them once is not a difficult problem.

The app is manual-first. You type in your bills, your subscriptions, the rent, the utilities, and the contracts that renew every year or two. The app keeps them on your iPhone, reminds you at 9:00 before each one is due, shows the month's bills in a monthly summary and a calendar widget, and lets you mark a bill paid straight from the notification. It reminds you before a contract ends, too, and can send a partner a short message about a bill that's coming up. Widgets and Siri keep the daily friction low: ask Siri *"What bills are due in AllPaid"* and it reads out the next seven days. A Pro tier adds Spending Analytics and full payment history, and those stay on the device as well.

What the app does not do, and will not do:

- It does not connect to your bank.
- It does not connect to a third-party aggregator.
- It does not have an account system, so it never asks for a login or an email address.
- It does not see anything you do not type into it.

On paper this is less convenient than a Plaid-connected app. In practice the gap is smaller than people expect. Entering everything the first time takes about fifteen minutes if you have a long list. After that, the work is tapping a notification to mark a bill paid, which is the same effort a bank-linked app asks for, at a lower cost.

## What this trades away

Bank-linked bill apps catch one category of bill that AllPaid will miss: **the subscription you signed up for, forgot about, and would not remember to enter into a manual app**. The classic "$8.99/month for that streaming service you used twice in 2023." That is a real benefit, and AllPaid does not offer it.

If [finding forgotten charges](/journal/find-every-recurring-charge/) is the user's primary need, a bank-linked tool is the better fit, and I'd recommend one. Just know what you are giving up when you connect it.

Manual-first works for everyone else: people who know roughly what they pay for, want a reminder to pay it, want to nudge a roommate when rent is due, want to see the month's bills at a glance, and don't want a third party reading their checking account in perpetuity.

## A note on tax season

This post is going up on the 31st of January, and the timing is deliberate. Tax season is when people look at their finances most carefully and most apprehensively. It is also the season when fintech apps run their biggest advertising spend, because conversion is highest when anxiety is highest.

[AllPaid](/apps/allpaid/) is meant to be the calmer answer in that window. It skips the bank login and the anxious onboarding, keeps your bills on your iPhone, and does the boring job of making sure you don't miss a bill or pay a late fee. It's free for up to three bills, with Pro at {P_MONTHLY@allpaid} a month, {P_YEARLY@allpaid} a year, or {P_LIFETIME@allpaid} once.

If this is the year you stop trading read access to your bank for features you could write down yourself, we think you're right.
