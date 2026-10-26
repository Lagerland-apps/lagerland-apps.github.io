---
layout: journal
slug: the-case-for-native-screenshot-tooling
title: "The case for a native App Store screenshot tool"
seo:
  title: "The Case for a Native App Store Screenshot Tool"
  description: "App Store screenshots do the most indie marketing work and are the worst release chore. The case for a native, capture-first screenshot tool."
  keywords:
    - "app store screenshot tool"
    - "screenshot generator mac"
    - "app store screenshot maker"
    - "device frame tool"
    - "marketing screenshots app"
    - "mockly"
date: 2026-03-14
last_updated: 2026-10-26
lede: "App Store screenshots do more marketing work for an indie app than anything else, and most indie developers, past versions of me included, treat them as the worst chore of every release. Mockly is the studio's case that this workflow belongs in a native Mac app, and that a YAML-driven CI script is the wrong home for it."
quick_answer: "Mockly is a native Mac alternative to fastlane snapshot, frameit, and deliver for indie iOS developers who treat App Store screenshots as editorial work. It composes layouts with 3D Metal-rendered device frames, swaps screenshots and copy across 20+ App Store locales, and uploads directly to App Store Connect. It costs $12.99 lifetime and supports Family Sharing."
faq:
  - q: "Is there a native Mac alternative to fastlane snapshot?"
    a: "Mockly is a native macOS app that replaces fastlane snapshot, frameit, and deliver for indie iOS developers whose screenshot work is editorial. It composes layouts with 3D Metal-rendered device frames, swaps screenshots and copy across 20+ App Store locales, and uploads directly to App Store Connect. You don't need Ruby, YAML, or Xcode UI tests."
  - q: "How much does Mockly cost?"
    a: "Mockly is {P_APP@mockly} lifetime with Family Sharing support, so a two-developer studio or co-founder pair can share a single license. The price is one-time on purpose, with no per-seat charge, because a small indie tool should treat its small indie users like a household and not like a contract."
  - q: "Does Mockly replace fastlane entirely?"
    a: "No. Studios with deep CI/CD investments and pipelines that regenerate screenshots on every release should keep fastlane. Mockly covers the editorial step upstream of the pipeline, deciding what each screenshot says with overlay copy and multiple devices, which is most of the work for design-led indie shops."
  - q: "How are device frames rendered in Mockly?"
    a: "Every iPhone and iPad model from the last six years is rendered in 3D with Metal at composition time, so rotation, perspective, lighting, and reflections behave correctly. A flat PNG composite cannot get a four-degree rotation right; Mockly's frames can."
mentioned_apps:
  - mockly
  - appmeta
read_time: "5 min read"
excerpt: "Most indie developers automate App Store screenshots with fastlane. Mockly goes the other way: a native Mac app with 3D Metal-rendered device frames, 20+ region localization, and direct upload to App Store Connect. This post explains why a GUI tool can beat a CI pipeline for screenshot work, and why the studio sells it as a $12.99 lifetime purchase with Family Sharing."
---

App Store screenshots are the most underrated assets in indie iOS marketing. They are the first thing a prospective user sees in a search result, and they convert better than any description, keyword, or rating. Yet most indie developers I know treat them as the worst chore of every release (that's anecdote, not a survey).

I treated them that way for five years. [Mockly](/apps/mockly/) is the studio's attempt at something better, and the rest of this post is what I learned shipping it.

## What is the fastlane status quo for App Store screenshots?

In the iOS indie world, most people generate screenshots with **fastlane snapshot**, a Ruby tool that drives the iOS simulator, takes screenshots in every required device size, and writes them to disk. Add **fastlane frameit** (device frames) and **fastlane deliver** (upload to App Store Connect) and you have a complete pipeline.

Fastlane deserves credit. It is genuinely useful, its team has done indie developers a public service for nearly a decade, and the tool is open source. If you already have a heavily customised CI pipeline and your screenshots fit fastlane's templates, it is a reasonable choice.

It is not comfortable to use, though. The workflow is:

1. Write Swift UI tests that drive your app to specific screens.
2. Maintain a YAML config of devices, locales, and target screens.
3. Run a Ruby command-line tool that takes 30-90 minutes for a multi-locale ship.
4. Hope that nothing in iOS or Xcode broke the simulator automation since last release.
5. Manually swap or recompose any screenshot that needs editorial work: text overlays, multiple devices in one image, before/after pairs.
6. Ship.

Every step adds friction, and it compounds. The Swift UI tests rot. The YAML grows. The simulator changes its rendering between Xcode versions without telling you. The editorial work happens in a separate tool (Pixelmator, Photoshop, or hand-coded SwiftUI), so the editorial assets and the automated assets drift apart. By the third release, half the studios I know have given up on the automated path and are screenshotting the simulator by hand.

## The native-app argument

Mockly is built on the bet that **most indie screenshot work is a GUI problem**, and automation solves the smaller part of it.

A GUI tool lets you manipulate the asset directly. You drag the screenshot from the simulator into the app, pick a device frame from a library, add a text overlay, compose multi-device layouts, and see the final result immediately. The locale switcher swaps the underlying screenshot and keeps the layout. The 3D frames are rendered live instead of laid on as PNG overlays, so a four-degree rotation gets proper perspective and lighting, which a flat composite cannot match.

The output is the same PNG files at the App Store's required dimensions. The *workflow* is what changes. Each screenshot becomes a small asset you own, edit and re-export when needed, where a pipeline would regenerate it slightly differently every time the simulator runs.

That workflow fits studios that ship a polished, carefully edited set of screenshots: several devices in one image, overlay copy, motion blur on transition shots.

## What Mockly specifically does

The feature set, briefly:

- **3D Metal-rendered device frames.** Every iPhone and iPad model from the last six years, rendered when you compose the screenshot. Rotation, perspective, lighting, and reflections are physically rendered.
- **Localised composition.** A single layout, with text, multiple devices, and overlays, exports across 20+ App Store regions in one click. The locale switcher swaps screenshots and translates copy.
- **Direct upload to App Store Connect.** You skip the fastlane deliver step. The app talks to the ASC API and pushes to the right per-locale slot.
- **Templates.** A library of professionally designed templates for common patterns: the four-screenshot hook, the before-and-after, the device-and-watch pairing.
- **Editorial workflow.** Custom layouts, free positioning, drag-and-drop: the full composition tool that fastlane doesn't try to be.

Mockly deliberately leaves the automation pipeline alone. If your studio has a deep CI/CD investment and screenshots that regenerate from running tests on every release, keep fastlane in your stack. Mockly covers the editorial step upstream of the pipeline, *deciding what the screenshot says*, for the studios where that is most of the work.

## Why {P_APP@mockly} lifetime, with Family Sharing {#why-1299-lifetime-with-family-sharing}

The pricing follows the [AppMeta pricing decision](/journal/native-mac-client-for-app-store-connect/) from a few weeks back: a one-time purchase with lifetime access and no subscription.

Mockly adds **Family Sharing support**. A two-developer studio (me and a co-founder, two indie partners, a couple-run studio) can share a single {P_APP@mockly} license. I chose this on purpose. The alternative was per-seat pricing, which suits SaaS and doesn't suit a tool that small studios use now and then.

The studio loses some revenue to Family Sharing. In exchange, I think, it gets the right relationship with the user: a small indie tool should treat its small indie users like a household, and not like a contract.

## Who should stay with fastlane

Not every iOS developer should switch to Mockly. Fastlane serves the largest, most automated indie pipelines well, and many of them have years of customisation that would be expensive to abandon.

My claim is narrower. A sizeable share of indie developers, the studios where screenshot work is editorial first and pipelined second, would be better served by a GUI tool than a CI script. Almost nobody builds GUI tools for indie iOS workflows, because the audience is "just" tens of thousands of developers worldwide.

This studio happens to be part of that audience, and [Mockly](/apps/mockly/) is for it: {P_APP@mockly}, lifetime, with Family Sharing. If it doesn't fit your workflow, fastlane will still be there next release.

If you've ever sworn at a Ruby script in the middle of a Friday ship, this might be the weekend to reconsider which parts of the chore you actually need.
