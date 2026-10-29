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
last_updated: 2026-10-29
lede: "App Store screenshots do more marketing work for an indie app than anything else, and most indie developers, past versions of me included, treat them as the worst chore of every release. Mockly is the studio's case that this workflow belongs in a native Mac app, and that a YAML-driven CI script is the wrong home for it."
quick_answer: "Mockly is a native Mac alternative to fastlane frameit and deliver for indie iOS developers who treat App Store screenshots as editorial work. You put your own captures on six 3D device models, add text, images, and backgrounds, keep up to 50 App Store languages in one project, and upload the set to App Store Connect with your API key. It costs {P_APP@mockly} once, with no subscription."
faq:
  - q: "Is there a native Mac alternative to fastlane snapshot?"
    a: "Mockly is a native macOS app that covers the design and upload side of what fastlane frameit and deliver do, for indie iOS developers whose screenshot work is editorial. It doesn't drive the simulator, so you still take the captures yourself or with fastlane snapshot. Mockly puts them on 3D device models, holds up to 50 App Store languages in one project, and uploads to App Store Connect. You don't need Ruby or YAML."
  - q: "How much does Mockly cost?"
    a: "Mockly is {P_APP@mockly} once, with no subscription, and every editor feature comes with the purchase. If you use AI Translate, it runs on your own OpenAI, Anthropic, or Google key, and your provider bills you for that use."
  - q: "Does Mockly replace fastlane entirely?"
    a: "No. Studios with deep CI/CD investments and pipelines that regenerate screenshots on every release should keep fastlane. Mockly covers the editorial step on top of the captures, deciding what each screenshot says with overlay copy and multiple devices, which is most of the work for design-led indie shops."
  - q: "How are device frames rendered in Mockly?"
    a: "Mockly has six 3D device models: iPhone 17 Pro Max, iPad Pro 11-inch and 12.9-inch, MacBook Pro 16-inch, Apple Watch Ultra, and Apple Watch Series 11. You set each one's rotation on three axes, its scale, and its offset, choose perspective or orthographic projection, and render it Realistic, Clay, or UI Only. A flat PNG frame only works straight on, and a 3D model keeps the screen on the device at any angle."
mentioned_apps:
  - mockly
  - appmeta
read_time: "6 min read"
excerpt: "Most indie developers automate App Store screenshots with fastlane. Mockly goes the other way: a native Mac app with 3D device models, up to 50 App Store languages in one project, and direct upload to App Store Connect. This post explains why a GUI tool can beat a CI pipeline for screenshot work, and why the studio sells it for {P_APP@mockly} once, with no subscription."
---

App Store screenshots are the most underrated assets in indie iOS marketing. They are the first thing a prospective user sees in a search result, and in my experience they do more to sell an app than the description, the keywords, or the rating. Yet most indie developers I know treat them as the worst chore of every release (that's anecdote, not a survey).

I treated them that way for five years. [Mockly](/apps/mockly/) is the studio's attempt at something better, and the rest of this post is what I learned shipping it.

## What is the fastlane status quo for App Store screenshots?

In the iOS indie world, most people generate screenshots with **fastlane snapshot**, a Ruby tool that drives the iOS simulator, takes screenshots in every required device size, and writes them to disk. Add **fastlane frameit** (device frames) and **fastlane deliver** (upload to App Store Connect) and you have a complete pipeline.

Fastlane deserves credit. It is genuinely useful, its team has done indie developers a public service for about a decade, and the tool is open source. If you already have a heavily customised CI pipeline and your screenshots fit fastlane's framing, it is a reasonable choice.

It is not comfortable to use, though. The workflow is:

1. Write Swift UI tests that drive your app to specific screens.
2. Maintain a config of devices, languages, and target screens.
3. Run a Ruby command-line tool that can take a long time for a multi-language release.
4. Hope that nothing in iOS or Xcode broke the simulator automation since the last release.
5. Swap or recompose by hand any screenshot that needs editorial work: text overlays, several devices in one image, before-and-after pairs.
6. Ship.

Every step adds friction, and it compounds. The Swift UI tests rot. The config grows. The simulator changes its rendering between Xcode versions without telling you. The editorial work happens in a separate tool (Pixelmator, Photoshop, or hand-coded SwiftUI), so the editorial assets and the automated assets drift apart. By the third release, half the studios I know have given up on the automated path and are screenshotting the simulator by hand.

## The native-app argument

Mockly is built on the bet that **most indie screenshot work is a GUI problem**, and automation solves the smaller part of it.

A GUI tool lets you work on the asset directly. You drop a capture from the simulator onto a 3D device, add a text overlay, put several devices on one page, and see the result immediately. Each language follows your source language until you unlink it, so a language can carry its own screenshots and text while the layout stays the same. The devices are 3D models rendered as you work, so a slight rotation keeps the screen on the device with the right perspective and light, which a flat frame overlay can't do.

The output is the same kind of file: PNG (or HEIC) at the exact pixel size of the artboard you picked. The *workflow* is what changes. Each screenshot becomes a small asset you own, edit, and re-export when needed, where a pipeline would regenerate it slightly differently every time the simulator runs.

That workflow fits studios that ship a carefully edited set of screenshots, with several devices in one image and overlay copy.

## What Mockly specifically does

The feature set, briefly:

- **3D device models.** Six of them: iPhone 17 Pro Max, iPad Pro 11-inch and 12.9-inch, MacBook Pro 16-inch, Apple Watch Ultra, and Apple Watch Series 11. Turn each on three axes, set the light, and render it Realistic, Clay, or UI Only.
- **Localised composition.** One project holds up to 50 App Store languages. Translate the text with AI on your own OpenAI, Anthropic, or Google key, or export a CSV for a translator, and Save Images exports every language at once.
- **Direct upload to App Store Connect.** You skip the fastlane deliver step. With your App Store Connect API key, the app uploads the pages for the languages you pick and replaces the screenshots already in that display type.
- **A folder of captures, placed for you.** Name your simulator captures by language, page, and device, link the folder, and each file lands on the right device in every language.
- **Editorial tools.** Text blocks with fonts, stroke, and shadow, Copy Style to repeat a look, image layers for logos and badges, and colour, gradient, or built-in backgrounds. There are no templates: you build each layout yourself, which is the part fastlane doesn't try to do.

Mockly deliberately leaves the automation pipeline alone. If your studio has a deep CI/CD investment and screenshots that regenerate from running tests on every release, keep fastlane in your stack. Mockly covers the editorial step on top of the captures, *deciding what the screenshot says*, for the studios where that is most of the work.

## Why {P_APP@mockly} once, with no subscription {#why-one-time-no-subscription}

The pricing follows the [AppMeta pricing decision](/journal/native-mac-client-for-app-store-connect/) from a few weeks back: a one-time purchase. AppMeta later added a yearly option next to its lifetime one; Mockly has no subscription at all.

Mockly is a tool small studios use a few times a year, around releases. A subscription would charge them every month for a job they do now and then. A single price with every editor feature included fits that rhythm better, and AI translation runs on the developer's own key, so the app has no running costs to pass on.

The studio earns less per user this way. In exchange, I think, it gets the right relationship with the user: a small indie tool should feel like something you own, and not like a contract.

## Who should stay with fastlane

Not every iOS developer should switch to Mockly. Fastlane serves the largest, most automated indie pipelines well, and many of them have years of customisation that would be expensive to abandon.

My claim is narrower. A sizeable share of indie developers, the studios where screenshot work is editorial first and pipelined second, would be better served by a GUI tool than a CI script. Few people build GUI tools for indie iOS workflows, because the audience is "just" tens of thousands of developers worldwide.

This studio happens to be part of that audience, and [Mockly](/apps/mockly/) is for it: {P_APP@mockly} once, with no subscription. If it doesn't fit your workflow, fastlane will still be there next release.

If you've ever sworn at a Ruby script in the middle of a Friday ship, this might be the weekend to reconsider which parts of the chore you actually need.
