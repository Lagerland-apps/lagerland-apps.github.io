---
layout: journal
slug: read-only-revenue-on-the-iphone
title: "A read-only dashboard for App Store revenue, on the iPhone"
date: 2026-04-18
lede: "Your accountant doesn't need write-access to App Store Connect. Your designer doesn't either. Your spouse, your co-founder, your weekly bookkeeping flow — none of them need to be able to change your app's metadata in order to know how it's selling. AppMeta Pulse is the small iPhone app I built when I got tired of explaining that distinction."
read_time: "5 min read"
excerpt: "AppMeta Pulse is the iPhone-side companion to AppMeta — a read-only revenue, subscription, and refund dashboard for indie iOS developers. This post explains the case for a glanceable revenue tool, why read-only access matters for sharing portfolio metrics with a co-founder or accountant, and the freemium pricing structure."
---

A small post for the third Saturday in April. Tax week is just behind us in the US, the indie-iOS calendar is in the lull between Q1 and WWDC, and most studios are doing the quiet financial reconciliation that the season demands.

This one's about [AppMeta Pulse](/apps/appmeta-pulse/), the iPhone app this studio ships for that exact moment. It is the smallest, simplest tool in the catalogue. I am, surprisingly often, asked why it exists.

## The setup problem

Two months ago [I wrote](/journal/native-mac-client-for-app-store-connect/) about AppMeta — the native Mac client for App Store Connect's *write* surface, the part where you edit metadata and respond to reviews and submit versions. AppMeta Pulse is the *read* counterpart. It looks at App Store revenue and not much else.

The reason there are two apps, and not one, is a structural permissions problem most indies hit eventually.

App Store Connect has a single, monolithic role model. Either someone has access to your developer account, or they don't. Sub-roles exist (Admin, Developer, Marketing, etc.) but the specifics are coarse — Marketing can edit metadata; Finance can read sales reports; nobody can have *just* "read-only revenue access without seeing build artefacts or being able to respond to reviews."

This means: if you want your accountant to see your revenue numbers, you have to give them an account on App Store Connect, configure their role, accept that they can see things you'd rather they didn't, and trust them to log in to a developer-account web tool every time they want to check.

In practice, what most indies do is ship a screenshot of their numbers via Slack or iMessage. This is fine for one-off requests. It's terrible for any kind of regular reporting cadence.

AppMeta Pulse exists to be the answer.

## What read-only revenue access looks like

The bet behind AppMeta Pulse is that the *most-asked-for* thing — *"how is the app selling this week?"* — should be its own glanceable tool, separate from the editorial surface where you change pricing or push a new version.

The app sits on top of the App Store Connect API, scoped to the **read-only revenue endpoints**. It surfaces:

- Daily, weekly, and monthly revenue per app and across the portfolio.
- Subscription health: trials, conversions, churn, refunds.
- Country-level revenue rollups.
- Comparison views — week-over-week, month-over-month, year-over-year.
- Per-app vs. portfolio splits.

It does not surface anything you can edit. There is no metadata view, no review responses, no build management, no submission. It cannot do those things. It is structurally a read-only tool, and that's the whole point.

## Why "glanceable" matters

The form factor is iPhone, and the design is glanceable on purpose.

AppMeta does the desk work — the multi-locale metadata editing, the keyword analysis, the review inbox — and lives on the Mac. AppMeta Pulse does the *check-in* — the morning coffee, the weekly meeting with a co-founder, the quarterly review with the accountant — and lives on the phone.

The use case I designed for is: indie developer in a coffee shop, picks up phone, taps Pulse, sees yesterday's revenue against the seven-day average, decides whether to pay attention or get on with the day. This should take three seconds. It does.

The widget is, predictably, the highest-engagement surface. A small Home Screen widget shows yesterday's revenue and the week-over-week delta. A medium widget shows the last 30 days as a sparkline. The widget has no labels other than the dollar figure and the delta, because those are the only two numbers that matter at a glance.

## Sharing without granting

The other use case AppMeta Pulse handles cleanly is *sharing read-only access without granting write access*.

A co-founder, a designer working on a profit-share, an accountant doing quarterly bookkeeping — these people need to see numbers. They don't need to be able to change your app's pricing.

Pulse handles this with **shared access tokens** scoped to the read-only API surface. The studio owner generates a token in the app, shares it with the trusted party, and that party can install Pulse on their phone and see the same numbers as the owner — without ever logging in to App Store Connect, without having any role on the developer account, without being able to do anything beyond view.

If you want to revoke access, you rotate the token and the other party stops seeing data. There's no role to delete, no Apple ID to remove, no awkward back-and-forth. The relationship is bounded and reversible.

## The freemium structure

Pulse ships with a small free tier — single-app revenue, last 30 days, no sharing — and a Pro tier that unlocks the portfolio view, longer history, sharing, and widgets. Pro is $0.99/month, $8.99/year, or $17.99 lifetime.

The pricing is intentionally low. The argument: this is not a tool a studio uses for hours a day; it's a tool you check briefly and rely on. Pricing it like a productivity-software flagship would mismatch its actual position in the indie's stack. $17.99 lifetime puts it firmly in the "buy it and forget about it" tier, which is the right tier for what it does.

## What this is not

AppMeta Pulse is not a financial-planning tool. It does not project revenue, model scenarios, or replace your accountant. It does not do tax-related calculations.

It is also not a marketing-analytics tool. It does not connect to App Store Connect's *Analytics* surface (impressions, conversion rates, search terms). That's a deeper, more complicated dataset and the tooling for it would be a different app — possibly worth building, possibly not.

What Pulse does is one thing: surface your App Store revenue in a glanceable way, on your phone, sharable read-only with the people who need to see it. That's the whole pitch.

## A small note on the catalogue

This is, by my count, the third post this quarter about a tool aimed at indie iOS developers. It's also the last for a while — I want to come back to the consumer apps that occupy most of the catalogue, and the next few weekends will probably do that.

But for the indies who read this far, [AppMeta Pulse](/apps/appmeta-pulse/) might be the small, useful, $17.99-lifetime tool you didn't know you wanted. If your accountant has been asking for screenshots, this is the better answer.

Spring is the season of clean books. Use it.
