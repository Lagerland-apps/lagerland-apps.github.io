---
layout: journal
slug: native-mac-client-for-app-store-connect
title: "On building a native Mac client for App Store Connect"
date: 2026-02-21
lede: "App Store Connect is the most consequential web app most indie developers use, and it has been the same web app for ten years. AppMeta is the studio's quietest app and arguably the most useful — a native Mac client for the ASC API, built for the day you're shipping in fourteen locales and need to stop scrolling."
read_time: "6 min read"
excerpt: "AppMeta is a native Mac client for the App Store Connect API — per-locale metadata editing, diff preview, keyword analysis, review responses, and version submission. This post explains why the indie iOS workflow needed it, what the trade-offs are, and why the studio shipped it as a $44.99 lifetime purchase rather than a subscription."
---

App Store Connect — Apple's web tool for shipping apps — is the single most consequential web app in the indie iOS developer's day. It's how you manage metadata, push builds to TestFlight, respond to reviews, set pricing, file privacy declarations, and submit for review. Almost every studio I know spends an hour a day in it during ship weeks.

It is also, structurally, a web app from 2014 that has accreted features for a decade. It works. It is also, on a long-haul flight or in a tab adjacent to fifteen others, miserable.

[AppMeta](/apps/appmeta/) is the native Mac client I built to stop being miserable.

## The problem ASC has, specifically

App Store Connect's design constraints are not Apple's fault, in fairness. They are managing the metadata for several million apps across two hundred regions in forty languages, with regulatory edge cases in every market. Building a great web tool against that surface area is a hard problem, and the team that ships ASC ships a *lot*.

What ASC isn't optimised for is the workflow of an indie developer with five-to-fifty apps shipping across twenty locales. Specifically:

- **Localised metadata editing is one-locale-at-a-time.** Editing a description in fourteen languages means switching the locale dropdown fourteen times. There is no side-by-side view.
- **Keyword fields are 100 characters per locale**, with no cross-locale gap analysis. Indies rediscover the same keyword waste in every language because there's no tool to surface it.
- **Review responses are a per-app web flow** with no inbox. If you have ten apps, you have ten places to check.
- **Version submission requires a multi-step flow with hidden state.** "Did I save the export compliance? Did I tick advertising identifier? Did I attach the encryption form?" These have all bitten me.
- **The web app does not run while you're offline.** The flight where you wanted to triage twelve reviews in a row is the flight you can't.

Every one of these is a real friction. None of them are catastrophic individually. Together they are why I had a recurring "App Store Connect" calendar block on my Friday afternoons for two years before I shipped AppMeta.

## What a native client actually changes

The core of AppMeta is a Mac client that talks directly to the App Store Connect REST API and gives you a side-by-side view of your apps' metadata. The four things it changes:

**Side-by-side localised editing.** The English description is in the left pane. The German, French, Japanese, and Spanish versions are tabs in the right pane. You edit one, the diff is highlighted across the others, and you push when you're ready. The hour-long localisation pass collapses into ten minutes.

**Diff preview before push.** AppMeta shows you exactly what will change against the current live metadata before the push happens. This is the feature I trust more than I trust myself, because *it caught a typo in five different localisations on the day before I would have shipped them.* Once that happens to you once, you do not ship without a diff preview again.

**Cross-locale keyword analysis.** AppMeta computes per-character keyword utilisation across every locale and surfaces wasted space, duplicates, and gaps. This used to be a spreadsheet I maintained by hand. It is now a panel in the app.

**A review inbox across every app in the catalogue.** Instead of clicking through ten app pages to triage reviews, AppMeta gives you a single inbox sorted by recency. Tap a review, type a response, send. The response goes through ASC's regulated channels — Apple is the source of truth — but the workflow lives in one place.

There's also version submission, screenshot management, pricing changes, and a few smaller things. The point isn't the feature checklist. The point is that *every minute of friction the web tool adds* compounds over a year of shipping.

## Why a lifetime price, not a subscription

This is the question I get most about AppMeta, and I want to be plain about it.

App Store Connect tooling is a developer tool. Developer tools have a long history of subscription-priced services — JetBrains, Sketch, Figma, Linear. The market would absolutely pay $19.99 a month for a good ASC client. I considered it.

The reason I shipped AppMeta as a one-time $44.99 purchase is that subscriptions create a specific bad incentive for a tool like this: every month, you have to ship enough perceived value to justify the recurring charge. That pressure pushes the roadmap toward *more features*, not toward the right features. AppMeta's job is to be a fast, reliable native client. Adding features for the sake of a renewal cycle would compromise that.

A one-time purchase forces a different discipline: ship a tool that's worth $44.99 once, and let the work earn the next purchase from a new user, not extract a renewal from an existing one. The tradeoff is slower revenue. The advantage is honest design.

## What AppMeta is not

AppMeta is not a build pipeline tool. It does not replace fastlane, Xcode Cloud, or your CI. It does not generate screenshots — that's [ScreenFlow Studio](/apps/screenflow-studio/)'s job. It does not analyse revenue — that's [AppMeta Pulse](/apps/appmeta-pulse/), the iPhone-side companion.

It is, specifically, the native client for the metadata-and-review portion of App Store Connect. The thing you spend an hour a day in during ship weeks. The thing that needed to stop being miserable.

## The plain version

If you're an indie iOS or macOS developer shipping in multiple locales and you've ever spent a Friday afternoon doing the locale-dropdown dance, [AppMeta](/apps/appmeta/) is the studio's answer. $44.99, one-time, lifetime. Demo mode is free if you want to look around before you buy.

If you're not an indie developer, this post has been twelve hundred words about a niche tool, and you've made it admirably far. Thanks for reading. The next post will be about chess.
