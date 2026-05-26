---
layout: journal
slug: app-store-screenshot-review-guidelines-explained
title: "What every App Store Review Guidelines screenshot rule actually means (and which ones get apps rejected)"
date: 2026-05-13
lede: "App Store Review Guidelines §2.3.3 looks like one short paragraph about screenshots. In practice it's the single most common reason indie apps get rejected during the screenshot pass. Here's what each clause actually means, the patterns that trigger rejection, and the ones reviewers wave through."
quick_answer: "App Store Review Guidelines §2.3.3 requires that screenshots show the app actually running on the device — real in-app UI, not just illustrations or conceptual mockups. Overlaid feature copy, coloured backgrounds, and 3D device frames around a real screen capture are fine. What gets rejected: screenshots that show fictional UI that isn't in the app, screenshots that show features that don't exist in the build under review, marketing-art screenshots with no actual in-app content at all, and screenshots that show in-app purchase prices or promotions inconsistently with the App Store listing. The fix is structural: render real screen captures inside a device frame, not the other way around."
faq:
  - q: "What does App Store Review Guidelines §2.3.3 actually say about screenshots?"
    a: "The exact wording (paraphrased to avoid quoting the live policy): screenshots should show the app in use, not Photoshopped conceptual art. Reviewers want screenshots that reflect the actual app experience a user will see after downloading. Marketing-style overlay text and decorative backgrounds are allowed; fictional features and prerelease UI that isn't shipping are not."
  - q: "What's the most common reason screenshots fail review?"
    a: "Showing features that don't exist in the binary under review. This happens most often with marketing-driven design pipelines where the screenshot designer used a previous build's UI or a concept mockup. The reviewer compares your screenshots against the actual app and rejects when the screenshot promises something the app doesn't deliver. Render real captures, not concepts."
  - q: "Can I overlay text and use coloured backgrounds on App Store screenshots?"
    a: "Yes. Overlay text, colour fields, gradient backgrounds, 3D device frames around the screen, and decorative elements are all allowed under §2.3.3 provided the visible screen content shows the real app. The rule is about what's inside the device frame, not what's outside it."
  - q: "Are 3D device frames OK for App Store screenshots?"
    a: "Yes — 3D device frames are explicitly fine. The device frame is treated as decorative styling around the real screen capture. What matters is that the content of the screen inside the frame is the actual app UI."
  - q: "Will showing in-app purchase prices in screenshots cause rejection?"
    a: "Sometimes — particularly if the prices in screenshots don't match the prices declared on the App Store listing, or if they're displayed in a confusing way. Apple has tightened this in recent years. Either show actual IAP prices as they appear in the App Store listing, or avoid displaying them altogether. Promotional prices that have expired are a common rejection trigger."
mentioned_apps:
  - mockly
read_time: "8 min read"
excerpt: "App Store Review Guidelines §2.3.3 is one paragraph long and quietly responsible for more screenshot rejections than any other rule. This post walks through what each clause actually means in practice, which screenshot patterns get rejected, and which ones reviewers wave through."
---

App Store Review Guidelines §2.3.3 looks deceptively simple. One short paragraph about how screenshots should "show the app in use." In practice it is one of the single most common rejection reasons for indie apps — the one that catches small teams who delegated the screenshot pass to a marketing designer with a Figma file.

This post is a working developer's read of what §2.3.3 actually means, which screenshot patterns reliably pass, and which ones get the polite "we've reviewed your screenshots and they don't appear to show actual functionality" rejection email at 2 AM the night before launch.

## What the guideline actually says

Apple's wording on §2.3.3 has been refined a few times since 2017, but the durable spirit is: a screenshot is meant to represent the app a user will receive. Not a future version. Not a concept. Not a marketing illustration of what you wish the app did. The actual app, in actual use.

The boundaries:

- **What's allowed:** Overlaid feature copy on top of a screen capture. Coloured background fields around the device. Gradient or photographic backgrounds. 3D device frames. Decorative typographic emphasis. Multiple screenshots in a sequence telling a story.
- **What gets rejected:** Fictional UI that isn't in the app. Features that haven't shipped yet. Pure marketing illustration with no real screen content. Screenshots whose UI was Photoshopped after capture to look prettier than the app actually does.

The rule, in plain language: the *content inside the device screen* must be the real app. Everything *around* the device frame is decorative styling and largely up to you.

## The five rejection patterns I've seen most often

**1. The "future-build" screenshot.** The most common. A marketing team shipped a previous version's UI in the screenshot bundle, or used a Figma concept that hasn't been built yet. Reviewer downloads the app, can't find the feature, rejects. Always re-render screenshots from the actual build you're submitting.

**2. The "concept-art" screenshot.** Especially common in apps with rich graphics — games, drawing apps, AR apps. The screenshot is closer to a hero shot for a website than an in-app capture. Reviewer reads it as misleading. The fix is to find an in-app moment that genuinely looks like the hero shot and capture it.

**3. The "deleted-feature" screenshot.** Feature existed in version 2.4, was removed in 2.7, screenshots from 2.4 still uploaded for 2.7. Re-uploading old screenshots is one of the easier ways to inherit a rejection from your own past.

**4. The "in-app-purchase price mismatch."** Screenshot shows "$0.99 — limited time," App Store listing shows $4.99. Reviewer flags the inconsistency. Best practice: either show real IAP prices that match the listing, or don't show prices in screenshots at all.

**5. The "fictional metric" screenshot.** Common in fitness, finance, and analytics apps. Screenshot shows "247,891 active users this month" or "+42% sleep score" but the demo data in the app shipping today shows different numbers. Reviewer treats this as misrepresentation.

## What 3D device frames have to do with any of this

Short answer: nothing problematic. Long answer: 3D device frames are decorative styling around the real screen content. As long as the screen content is the real app, the device frame can be any aspect, perspective, or render quality.

This is also why a tool like [Mockly](/apps/mockly/) is structurally compliant with §2.3.3 by default: the workflow is *capture the real screen first, render the device frame around it second.* The screen content is your actual app capture; the frame is just a 3D render placed around it. Compliant by construction.

Compare that to "design-first" workflows where someone in Figma mocks up a concept screen, then drops it into a flat phone outline, then exports. That's the workflow most likely to drift into §2.3.3 territory. Not because the tool is the problem — Figma isn't — but because the workflow encourages designing screens that aren't in the app yet, and then forgetting to verify they ever ship.

## How to make your screenshot pipeline §2.3.3-safe

A few practical rules:

1. **Capture from a build, not a design tool.** Use Simulator, Xcode UI tests, or manual capture from a TestFlight build to produce the raw screen content. If it didn't come from a running build, it doesn't belong inside the device frame.

2. **Re-capture for every release.** It's tempting to reuse screenshots when only minor UI changes happened. Each time you do this you risk inheriting a rejection from a feature that quietly went away.

3. **Strip IAP prices unless you're certain.** If the prices are dynamic, regional, or change with promotions, leave them out of screenshots entirely. Show feature value rather than price.

4. **If you do show metrics, match the demo state of the shipping build.** Use the same fixture data your TestFlight build uses. Don't render "247K users" if the demo state shows "1.2K."

5. **Treat the device frame as cosmetics.** Pick the visual style that fits your brand — 3D Metal render, flat outline, tilted angle, transparent background, no frame at all. Reviewers don't care about the frame. They care about what's on the screen inside it.

## What about App Store Preview videos?

§2.3.3 applies to App Store Preview videos as well, with two extra caveats. First: 30 seconds maximum (15 seconds for Apple Watch). Second: the video must show actual app footage captured from a device — not screen-recorded mock-ups, not animated concept reels, not external camera footage of someone using the app. Apple checks this rigorously, especially for new apps.

Mockly focuses on still screenshots and doesn't generate App Preview videos — those have a different recording and submission pipeline. But the same §2.3.3 logic applies: real captures from real builds.

## TL;DR

- **§2.3.3 is about the screen content, not the device frame.** Decorative styling around the device is fine.
- **The screen content must be the real app you're shipping.** Concept art, future-build UI, deleted features, and Photoshopped renders are the common rejection paths.
- **Capture-first workflows pass cleanly.** Design-first workflows risk drift.
- **IAP prices in screenshots must match the App Store listing.** Or leave them out.
- **App Preview videos have the same rule** plus length limits and a hard "no mockup" requirement.
- **Tool note:** [Mockly](/apps/mockly/)'s workflow puts the captured screen first and renders the 3D frame around it — structurally compliant with §2.3.3 by default. The reverse-architecture (design first, capture later) is what trips most teams up.

The rule has been the same in spirit for nearly a decade. The rejection emails keep arriving because the asset pipeline in most indie shops doesn't make compliance the default — it makes it an afterthought.
