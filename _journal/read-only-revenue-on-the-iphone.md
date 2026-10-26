---
layout: journal
slug: read-only-revenue-on-the-iphone
title: "A glanceable dashboard for App Store revenue, on the iPhone"
seo:
  title: "App Store Revenue Dashboard for iPhone: AppMeta Pulse"
  description: "An App Store Connect dashboard for iPhone that shows revenue, subscriptions and downloads, with no build, pricing or metadata controls."
  keywords:
    - "app store revenue dashboard"
    - "ios app revenue checker"
    - "app store connect iphone app"
    - "read-only app store connect"
    - "app revenue tracker"
    - "appmeta pulse"
date: 2026-04-18
last_updated: 2026-10-26
lede: "Your accountant doesn't need write access to App Store Connect, and neither does your designer, your spouse or your co-founder. Nobody in your weekly bookkeeping needs to be able to change your app's metadata to know how it's selling. AppMeta Pulse started as my answer to that. It turned out narrower: a quick revenue check for the account owner, on their own devices."
quick_answer: "AppMeta Pulse is a glanceable iPhone dashboard for App Store revenue, subscription health and country-level rollups, built on the App Store Connect API, with no build, pricing or metadata controls. The free download opens a demo on sample data; your own numbers need a subscription or the lifetime unlock."
faq:
  - q: "How can I check my App Store revenue on my iPhone?"
    a: "AppMeta Pulse is an iPhone dashboard built on the App Store Connect API's sales and subscription reports. It shows revenue per app for the latest day, the last 7 days and the last 30 days, along with subscription health and country-level rollups. The 7-Day Dashboard widget on the Home Screen shows proceeds, units and new subscriptions against the previous seven days."
  - q: "Can I share App Store revenue with my accountant without giving them full access?"
    a: "Not with AppMeta Pulse. It has no way to give another person access to your account's data. It shows your numbers on your own devices, and you can export a CSV of a period's sales to send yourself. To give an accountant ongoing access, add them in App Store Connect with a role such as Finance or Sales."
  - q: "What is the difference between AppMeta and AppMeta Pulse?"
    a: "AppMeta is the native Mac client for the write side of App Store Connect: metadata editing, review responses and version submission. AppMeta Pulse is the iPhone monitoring companion for revenue, subscription health and country rollups, and since the end of April 2026 it also shows customer reviews you can reply to. The two share an API surface and a pricing approach, and they do different jobs."
  - q: "How much does AppMeta Pulse cost?"
    a: "AppMeta Pulse is free to download, and the free download opens a demo on sample data. Your own numbers, the portfolio view and the widgets need a subscription or the lifetime unlock. When this post was written that was $0.99 a month, $8.99 a year, or $17.99 lifetime; the App Store now lists {P_MONTHLY@appmeta-pulse} a month, {P_YEARLY@appmeta-pulse} a year, or {P_LIFETIME@appmeta-pulse} lifetime. The lifetime tier is the recommended option for a tool you use briefly but rely on."
mentioned_apps:
  - appmeta-pulse
  - appmeta
read_time: "5 min read"
excerpt: "AppMeta Pulse is the iPhone companion to AppMeta, a revenue and subscription dashboard for indie iOS developers. This post makes the case for a glanceable revenue tool. It has been corrected, because Pulse never shipped the sharing it once described."
---

*Updated September 22, 2026: an earlier version of this post described shareable access tokens, a strictly read-only design and no App Store analytics. AppMeta Pulse never shipped token sharing, can send replies to customer reviews, and reads App Store impressions and page views. The post is corrected below. For current plans and prices, see the [AppMeta Pulse page](/apps/appmeta-pulse/).*

*Updated October 25, 2026: this post also described a free tier with one app and 30 days of history. Pulse never had one. The free download opens a demo on sample data, and everything else needs a subscription or the lifetime unlock. The widget description is corrected too.*

A small post for the third Saturday in April. Tax week is just behind us in the US, the indie iOS calendar is in the lull between Q1 and WWDC, and most studios are reconciling their books.

This one's about [AppMeta Pulse](/apps/appmeta-pulse/), the iPhone app this studio ships for that moment. It is the smallest, simplest tool in the catalogue, and I am asked surprisingly often why it exists.

## The setup problem

Two months ago [I wrote](/journal/native-mac-client-for-app-store-connect/) about AppMeta, the native Mac client for the *write* side of App Store Connect, where you edit metadata, respond to reviews and submit versions. AppMeta Pulse is the *monitoring* counterpart. It looks at App Store revenue and not much else.

There are two apps because of a permissions problem most indies hit eventually.

App Store Connect has one monolithic role model: either someone has access to your developer account, or they don't. Sub-roles exist (Admin, Developer, Marketing and so on), but they are coarse. Marketing can edit metadata and Finance can read sales reports, but nobody can have *just* "read-only revenue access without seeing build artefacts or being able to respond to reviews."

So if you want your accountant to see your revenue, you have to give them an App Store Connect account, configure their role, accept that they can see things you'd rather they didn't, and trust them to log in to a developer web tool every time they want to check.

In practice most indies send a screenshot of their numbers over Slack or iMessage. That works for a one-off request and is terrible for any regular reporting.

AppMeta Pulse was first pitched as the answer. It turned out narrower, a fast check for the account owner (see the correction below).

## What does glanceable revenue look like?

AppMeta Pulse bets that the question people ask most, *"how is the app selling this week?"*, deserves its own glanceable tool, separate from the editorial side where you change pricing or push a new version.

The app sits on top of the App Store Connect API and reads your sales, subscription and analytics reports. It shows:

- Daily, weekly and monthly revenue per app and across the portfolio.
- Subscription health: trials, conversions, churn, cancellations.
- Country-level revenue rollups.
- Comparison views: this week against last week, this month against last month.
- Per-app vs. portfolio splits.

Apart from replies to customer reviews, which arrived at the end of April 2026, nothing it shows can be edited. There is no metadata editing, build management or submission, and it is built so that it cannot do those things.

## Why the iPhone

The form factor is iPhone, and the design is meant to be read at a glance.

AppMeta does the desk work on the Mac: multi-locale metadata editing, keyword analysis, review replies. AppMeta Pulse does the *check-in* on the phone, over the morning coffee, in the weekly meeting with a co-founder or at the quarterly review with the accountant.

The use case I designed for: an indie developer in a coffee shop picks up the phone, taps Pulse, sees the last seven days' proceeds against the seven before, and decides whether to pay attention or get on with the day. That should take three seconds, and it does.

The widget is, predictably, what I look at most. The small Pulse widget shows one figure, its label and how fresh the data is; the medium one adds a sparkline. The 7-Day Dashboard widget shows proceeds, units and new subscriptions, each with its change from the previous seven days, because those are the numbers worth seeing at a glance.

## What about sharing?

This post originally claimed a use case for AppMeta Pulse that it doesn't cover: *sharing read-only access without granting write access*.

A co-founder, a designer on a profit share or an accountant doing quarterly bookkeeping needs to see the numbers, and none of them needs to be able to change your app's pricing.

Pulse doesn't solve this. It has no shared access tokens and no way to give another person access to your account's data, though you can export a CSV of a period's sales and send it yourself. The clean way to give someone ongoing read access is still an App Store Connect account with a limited role.

## The pricing structure

Pulse is free to download, and the free download runs a demo on sample data so you can see what it does. Your own numbers, the portfolio view and the widgets need Pro. At the time of writing, Pro was $0.99/month, $8.99/year, or $17.99 lifetime; the App Store now lists {P_MONTHLY@appmeta-pulse}/month, {P_YEARLY@appmeta-pulse}/year, or {P_LIFETIME@appmeta-pulse} lifetime.

The price is low on purpose. A studio doesn't use this tool for hours a day; it checks it briefly and relies on it. Pricing it like flagship productivity software would misjudge its place in an indie's toolkit. A one-time lifetime price puts it in the buy-it-and-forget-it tier, which suits what it does.

## What it doesn't do

AppMeta Pulse is not a financial-planning tool. It does not project revenue, model scenarios, or replace your accountant. It does no tax calculations, and it doesn't read Payments and Financial Reports; for when Apple's money actually arrives, see [when Apple pays developers](/journal/when-does-apple-pay-developers/).

Nor is it a full marketing-analytics tool. From App Store Connect's analytics reports it uses only App Store impressions and product page views (it keeps a copy of the downloaded report).

Pulse does one thing: it shows your App Store revenue at a glance, on your phone.

## A small note on the catalogue

By my count this is the third post this quarter about a tool for indie iOS developers. It's also the last for a while. I want to get back to the consumer apps that make up most of the catalogue, and the next few weekends will probably go to them.

If you're an indie who read this far and you keep opening App Store Connect just to see how yesterday went, [AppMeta Pulse](/apps/appmeta-pulse/) is a small pay-once tool that answers that faster. Spring is the season of clean books.
