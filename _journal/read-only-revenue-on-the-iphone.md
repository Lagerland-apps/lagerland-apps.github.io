---
layout: journal
slug: read-only-revenue-on-the-iphone
title: "A calm dashboard for App Store revenue, on the iPhone"
seo:
  title: "A Calm App Store Revenue Dashboard for iPhone"
  description: "An App Store Connect dashboard for iPhone — revenue, subscriptions, and downloads — with no build, pricing, or metadata controls."
  keywords:
    - "app store revenue dashboard"
    - "ios app revenue checker"
    - "app store connect iphone app"
    - "read-only app store connect"
    - "app revenue tracker"
    - "appmeta pulse"
date: 2026-04-18
last_updated: 2026-10-25
lede: "Your accountant doesn't need write-access to App Store Connect. Your designer doesn't either. Your spouse, your co-founder, your weekly bookkeeping flow — none of them need to be able to change your app's metadata in order to know how it's selling. AppMeta Pulse started as my answer to that; it turned out narrower — a quick revenue check for the account owner, on their own devices."
quick_answer: "AppMeta Pulse is a glanceable iPhone dashboard for App Store revenue, subscription health, and country-level rollups, built on the App Store Connect API, with no build, pricing, or metadata controls. The free download opens a demo on sample data; your own numbers need a subscription or the lifetime unlock."
faq:
  - q: "How can I check my App Store revenue on my iPhone?"
    a: "AppMeta Pulse is an iPhone dashboard built on the App Store Connect API's sales and subscription reports. It surfaces the latest day's, last 7 days' and last 30 days' revenue per app, subscription health, and country-level rollups. The 7-Day Dashboard widget on the Home Screen shows proceeds, units, and new subscriptions against the previous seven days."
  - q: "Can I share App Store revenue with my accountant without giving them full access?"
    a: "Not with AppMeta Pulse. It has no way to give another person access to your account's data: it shows your numbers on your own devices, and you can export a CSV of a period's sales to send yourself. To give an accountant ongoing access, add them in App Store Connect with a role such as Finance or Sales."
  - q: "What is the difference between AppMeta and AppMeta Pulse?"
    a: "AppMeta is the native Mac client for the write surface of App Store Connect — metadata editing, review responses, version submission. AppMeta Pulse is the iPhone-side monitoring companion: revenue, subscription health, and country rollups, plus, since the end of April 2026, customer reviews you can reply to. They share an API surface and a pricing philosophy but solve different jobs."
  - q: "How much does AppMeta Pulse cost?"
    a: "AppMeta Pulse is free to download, and the free download opens a demo on sample data. Your own numbers, the portfolio view, and the widgets need a subscription or the lifetime unlock. When this post was written that was $0.99 a month, $8.99 a year, or $17.99 lifetime; the App Store now lists $0.99 a month, $1.99 a year, or $2.99 lifetime. The lifetime tier is the recommended option for a tool used briefly but relied on."
mentioned_apps:
  - appmeta-pulse
  - appmeta
read_time: "5 min read"
excerpt: "AppMeta Pulse is the iPhone-side companion to AppMeta — a revenue and subscription dashboard for indie iOS developers. This post explains the case for a glanceable revenue tool; it has been corrected, because Pulse never shipped the sharing it once described."
---

*Updated September 22, 2026: an earlier version of this post described shareable access tokens, a strictly read-only design and no App Store analytics. AppMeta Pulse never shipped token sharing, can send replies to customer reviews, and reads App Store impressions and page views. The post is corrected below. For current plans and prices, see the [AppMeta Pulse page](/apps/appmeta-pulse/).*

*Updated October 25, 2026: this post also described a free tier with one app and 30 days of history. Pulse never had one: the free download opens a demo on sample data, and everything else needs a subscription or the lifetime unlock. The widget description is corrected too.*

A small post for the third Saturday in April. Tax week is just behind us in the US, the indie-iOS calendar is in the lull between Q1 and WWDC, and most studios are doing the quiet financial reconciliation that the season demands.

This one's about [AppMeta Pulse](/apps/appmeta-pulse/), the iPhone app this studio ships for that exact moment. It is the smallest, simplest tool in the catalogue. I am, surprisingly often, asked why it exists.

## The setup problem

Two months ago [I wrote](/journal/native-mac-client-for-app-store-connect/) about AppMeta — the native Mac client for App Store Connect's *write* surface, the part where you edit metadata and respond to reviews and submit versions. AppMeta Pulse is the *monitoring* counterpart. It looks at App Store revenue and not much else.

The reason there are two apps, and not one, is a structural permissions problem most indies hit eventually.

App Store Connect has a single, monolithic role model. Either someone has access to your developer account, or they don't. Sub-roles exist (Admin, Developer, Marketing, etc.) but the specifics are coarse — Marketing can edit metadata; Finance can read sales reports; nobody can have *just* "read-only revenue access without seeing build artefacts or being able to respond to reviews."

This means: if you want your accountant to see your revenue numbers, you have to give them an account on App Store Connect, configure their role, accept that they can see things you'd rather they didn't, and trust them to log in to a developer-account web tool every time they want to check.

In practice, what most indies do is ship a screenshot of their numbers via Slack or iMessage. This is fine for one-off requests. It's terrible for any kind of regular reporting cadence.

AppMeta Pulse was first pitched as the answer. It turned out narrower: a fast, calm check for the account owner (see the correction below).

## What does glanceable revenue look like?

The bet behind AppMeta Pulse is that the *most-asked-for* thing — *"how is the app selling this week?"* — should be its own glanceable tool, separate from the editorial surface where you change pricing or push a new version.

The app sits on top of the App Store Connect API and reads your sales, subscription, and analytics reports. It surfaces:

- Daily, weekly, and monthly revenue per app and across the portfolio.
- Subscription health: trials, conversions, churn, cancellations.
- Country-level revenue rollups.
- Comparison views — this week against last week, this month against last month.
- Per-app vs. portfolio splits.

It does not surface anything you can edit, apart from replies to customer reviews, which arrived at the end of April 2026. There is no metadata editing, no build management, no submission. It cannot do those things, and that's the whole point.

## Why "glanceable" matters

The form factor is iPhone, and the design is glanceable on purpose.

AppMeta does the desk work — the multi-locale metadata editing, the keyword analysis, the review replies — and lives on the Mac. AppMeta Pulse does the *check-in* — the morning coffee, the weekly meeting with a co-founder, the quarterly review with the accountant — and lives on the phone.

The use case I designed for is: indie developer in a coffee shop, picks up phone, taps Pulse, sees the last seven days' proceeds against the seven before, decides whether to pay attention or get on with the day. This should take three seconds. It does.

The widget is, predictably, the surface I look at most. The small Pulse widget shows one figure, its label and how fresh the data is; the medium one adds a sparkline. The 7-Day Dashboard widget shows proceeds, units and new subscriptions, each with its change from the previous seven days, because those are the numbers that matter at a glance.

## What about sharing?

A use case this post originally claimed for AppMeta Pulse is *sharing read-only access without granting write access*.

A co-founder, a designer working on a profit-share, an accountant doing quarterly bookkeeping — these people need to see numbers. They don't need to be able to change your app's pricing.

Pulse doesn't do this. It has no shared access tokens and no way to give another person access to your account's data; you can export a CSV of a period's sales and send it yourself. The clean way to give someone ongoing read access remains an App Store Connect account with a limited role.

## The pricing structure

Pulse is free to download, and the free download runs a demo on sample data so you can see what it does. Your own numbers, the portfolio view, and the widgets need Pro. At the time of writing, Pro was $0.99/month, $8.99/year, or $17.99 lifetime; the App Store now lists $0.99/month, $1.99/year, or $2.99 lifetime.

The pricing is intentionally low. The argument: this is not a tool a studio uses for hours a day; it's a tool you check briefly and rely on. Pricing it like a productivity-software flagship would mismatch its actual position in the indie's stack. A one-time lifetime price puts it firmly in the "buy it and forget about it" tier, which is the right tier for what it does.

## What this is not

AppMeta Pulse is not a financial-planning tool. It does not project revenue, model scenarios, or replace your accountant. It does not do tax-related calculations, and it doesn't read Payments and Financial Reports; for when Apple's money actually arrives, see [when Apple pays developers](/journal/when-does-apple-pay-developers/).

It is also not a full marketing-analytics tool. From App Store Connect's analytics reports it uses only App Store impressions and product page views (it keeps a copy of the downloaded report).

What Pulse does is one thing: surface your App Store revenue in a glanceable way, on your phone. That's the whole pitch.

## A small note on the catalogue

This is, by my count, the third post this quarter about a tool aimed at indie iOS developers. It's also the last for a while — I want to come back to the consumer apps that occupy most of the catalogue, and the next few weekends will probably do that.

But for the indies who read this far, [AppMeta Pulse](/apps/appmeta-pulse/) might be the small, useful, pay-once tool you didn't know you wanted. If you keep opening App Store Connect just to see how yesterday went, this is the better answer.

Spring is the season of clean books. Use it.
