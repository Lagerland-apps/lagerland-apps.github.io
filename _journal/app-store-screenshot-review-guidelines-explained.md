---
layout: journal
slug: app-store-screenshot-review-guidelines-explained
title: "App Store screenshot guidelines (2026): sizes, requirements, and what gets rejected"
date: 2026-05-13
last_updated: 2026-06-21
seo:
  title: "App Store Screenshot Guidelines 2026: Sizes & Rules"
  description: "Current App Store screenshot specs — sizes (6.9-inch iPhone, 13-inch iPad), counts, and formats — plus the §2.3.3 rules that get apps rejected."
  keywords:
    - app store screenshot guidelines
    - apple app store screenshot guidelines
    - app store screenshot sizes
    - app store screenshot requirements
    - app store screenshot dimensions
    - app store screenshot specifications
    - app store review guidelines screenshots
    - app store screenshot rejection
    - app preview specifications
    - app store screenshot format
lede: "App Store screenshots have two sets of rules that get apps rejected or re-uploaded: the technical specs (which sizes, how many, what format) and Review Guideline §2.3.3 (what the screen is allowed to show). Here is both — the current 2026 specifications, and what each content clause actually means in practice."
quick_answer: "As of 2026, App Store screenshots require just one iPhone size — 6.9-inch (1320 × 2868 or 1290 × 2796) or 6.5-inch (1242 × 2688) — and Apple automatically scales it down to every smaller iPhone, so the old 5.5-inch and 6.7-inch uploads are no longer needed. iPad apps additionally need a 13-inch set (2064 × 2752 or 2048 × 2732); Mac apps use a 16:10 size. You upload 1 to 10 screenshots per localization as flattened PNG or JPEG. Beyond dimensions, Review Guideline §2.3.3 governs content: the screen inside the frame must be the real shipping app. Overlay text, colored backgrounds, and 3D device frames are all fine; fictional UI, unshipped or deleted features, mismatched in-app-purchase prices, and fabricated metrics are the common rejection triggers. App Preview videos follow the same content rule, run 15 to 30 seconds, and allow up to 3 per localization."
faq:
  - q: "What size do App Store screenshots need to be in 2026?"
    a: "You need one iPhone size: 6.9-inch (1320 × 2868, 1290 × 2796, or 1260 × 2736 portrait) or 6.5-inch (1242 × 2688 or 1284 × 2778) as the accepted alternative. Apple scales that set down to all smaller iPhones automatically. iPad apps also require a 13-inch set (2064 × 2752 or 2048 × 2732). Mac apps use a 16:10 ratio (1280 × 800, 1440 × 900, 2560 × 1600, or 2880 × 1800). Always confirm against Apple's current spec page before a release — the dimensions change with new hardware."
  - q: "Do you still need 5.5-inch and 6.7-inch App Store screenshots?"
    a: "No. Since Apple simplified screenshot delivery, a single 6.9-inch (or 6.5-inch) iPhone set is scaled to every smaller display — 6.3-inch, 6.1-inch, 5.5-inch, 4.7-inch and down. You can still upload size-specific screenshots if you want pixel-perfect control on a particular device, but you are no longer required to provide separate 5.5-inch or 6.7-inch bundles. This is the single biggest change to the screenshot workflow in years and the reason a lot of old fastlane configs now upload more sizes than they need to."
  - q: "How many screenshots can you upload to the App Store?"
    a: "One to ten per localization, per display size. Only the first two to three are visible in App Store search results without tapping through, so the order matters more than the count — front-load the screenshots that carry your strongest value proposition, and treat positions four through ten as depth for people who already swiped in."
  - q: "What file format do App Store screenshots have to be?"
    a: "PNG or JPEG (.png, .jpg, .jpeg), in the RGB color space. Flatten them — no alpha channel or transparency — and submit the full-resolution image at the exact pixel dimensions for the display size. Don't bake in a fake status bar or rounded corners beyond what the real capture has; upload the true screen content and let App Store Connect present it."
  - q: "What does App Store Review Guideline §2.3.3 actually say about screenshots?"
    a: "Paraphrased to avoid quoting the live policy: screenshots should show the app in use — the real experience a user gets after downloading — not conceptual art, a splash screen, or a login page. Marketing-style overlay text and decorative backgrounds are explicitly allowed; fictional features and prerelease UI that isn't shipping are not. The rule is about the content inside the device screen, not the styling around it."
  - q: "What's the most common reason App Store screenshots fail review?"
    a: "Showing features or UI that don't exist in the binary under review. It usually happens when the screenshot pass was handed to a designer working from a Figma concept or a previous build, so the reviewer downloads the app, can't find what the screenshot promises, and rejects under §2.3.3. Rendering real captures from the exact build you're submitting eliminates the entire category."
  - q: "Can I overlay text, use colored backgrounds, and 3D device frames on App Store screenshots?"
    a: "Yes — all three are fine under §2.3.3. Overlay copy, color fields, gradient or photographic backgrounds, decorative typography, and 3D device frames around the screen capture are treated as styling. What matters is that the content visible inside the device screen is the actual app. The frame and everything outside it is yours to brand."
  - q: "What are the App Store Preview video requirements?"
    a: "Up to 3 app previews per localization, each 15 to 30 seconds. iPhone previews are 886 × 1920 (portrait) for 6.9-inch through 6.1-inch displays; iPad previews are 1200 × 1600. Accepted formats are .mov, .m4v, and .mp4 (H.264 at roughly 10–12 Mbps or ProRes 422 HQ), 30 fps, with AAC audio. The §2.3.3 content rule applies: the footage must be captured from the real app, not an animated mockup or concept reel — Apple checks this rigorously for new apps."
mentioned_apps:
  - mockly
read_time: "10 min read"
excerpt: "The complete App Store screenshot reference: current 2026 size specifications (6.9-inch iPhone, 13-inch iPad, counts, formats) and a working developer's read of Review Guideline §2.3.3 — which screenshot patterns get rejected and which reviewers wave through."
---

App Store screenshots get apps held up for two completely different reasons, and most guides only cover one of them. The first is **technical**: wrong size, wrong format, a missing required device — App Store Connect bounces the upload before a human ever sees it. The second is **editorial**: the screenshot uploads fine, then a reviewer looks at it and decides the screen isn't showing the real app, and you get the polite "your screenshots don't appear to show actual functionality" rejection at 2 AM the night before launch.

This post covers both: the current specifications, then a working developer's read of Review Guideline §2.3.3 — which patterns reliably pass, and which ones get rejected.

## App Store screenshot specifications (2026)

The big change to internalize first: **you only need one iPhone size now.** Apple scales a single 6.9-inch (or 6.5-inch) set down to every smaller iPhone automatically. The old ritual of exporting 6.7-inch, 6.5-inch, and 5.5-inch bundles is gone.

**iPhone — required (pick one):**

| Display | Portrait dimensions | Devices |
|---|---|---|
| 6.9-inch | 1320 × 2868 · 1290 × 2796 · 1260 × 2736 | iPhone 17 / 16 Pro Max, Plus models |
| 6.5-inch | 1242 × 2688 · 1284 × 2778 | iPhone 14 Plus, 13/12 Pro Max, XS Max |

Provide one of those, and 6.3-inch, 6.1-inch, 5.5-inch, 4.7-inch, and 4-inch are all generated by scaling. You *may* still upload size-specific screenshots when you want pixel-perfect control on a given device — it's just no longer required.

**iPad — required if your app runs on iPad:**

| Display | Portrait dimensions | Devices |
|---|---|---|
| 13-inch | 2064 × 2752 · 2048 × 2732 | iPad Pro (M4), iPad Air (M2/M3/M4) |

The 11-inch and smaller iPad sizes scale from the 13-inch set.

**Mac — required if your app runs on Mac:** a 16:10 image at 1280 × 800, 1440 × 900, 2560 × 1600, or 2880 × 1800.

**Count, format, and order:**

- **1 to 10** screenshots per localization, per display size.
- **PNG or JPEG**, RGB, flattened (no alpha/transparency), at the exact pixel dimensions above.
- Only the **first two to three** appear in App Store search results without tapping in — so front-load your strongest screenshots and treat the rest as depth.

Apple revises these as new hardware ships; the numbers above are current as of June 2026. Before any release, confirm against [Apple's official screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/screenshot-specifications/). Now the half that the specs can't protect you from.

## What §2.3.3 actually says

Apple's wording on §2.3.3 has been refined a few times since 2017, but the durable spirit is: a screenshot represents the app a user will receive. Not a future version. Not a concept. Not a marketing illustration of what you wish the app did. The actual app, in actual use.

The boundaries:

- **What's allowed:** Overlaid feature copy on top of a screen capture. Colored background fields around the device. Gradient or photographic backgrounds. 3D device frames. Decorative typographic emphasis. Multiple screenshots in a sequence telling a story.
- **What gets rejected:** Fictional UI that isn't in the app. Features that haven't shipped yet. Pure marketing illustration with no real screen content. Screenshots whose UI was Photoshopped after capture to look prettier than the app actually does.

The rule, in plain language: the *content inside the device screen* must be the real app. Everything *around* the device frame is decorative styling and largely up to you.

## The five rejection patterns I've seen most often

**1. The "future-build" screenshot.** The most common. A marketing team shipped a previous version's UI in the screenshot bundle, or used a Figma concept that hasn't been built yet. Reviewer downloads the app, can't find the feature, rejects. Always re-render screenshots from the actual build you're submitting.

**2. The "concept-art" screenshot.** Especially common in apps with rich graphics — games, drawing apps, AR apps. The screenshot is closer to a hero shot for a website than an in-app capture. Reviewer reads it as misleading. The fix is to find an in-app moment that genuinely looks like the hero shot and capture it.

**3. The "deleted-feature" screenshot.** Feature existed in version 2.4, was removed in 2.7, screenshots from 2.4 still uploaded for 2.7. Re-uploading old screenshots is one of the easier ways to inherit a rejection from your own past.

**4. The "in-app-purchase price mismatch."** Screenshot shows "$0.99 — limited time," App Store listing shows $4.99. Reviewer flags the inconsistency. Best practice: either show real IAP prices that match the listing, or don't show prices in screenshots at all.

**5. The "fictional metric" screenshot.** Common in fitness, finance, and analytics apps. Screenshot shows "247,891 active users this month" or "+42% sleep score" but the demo data in the app shipping today shows different numbers. Reviewer treats this as misrepresentation.

## App Preview videos: specs and the same content rule

App Preview videos have their own specifications, then inherit §2.3.3 on top.

- **Up to 3** previews per localization, each **15 to 30 seconds**.
- **iPhone:** 886 × 1920 portrait (886 covers 6.9-inch through 6.1-inch). **iPad:** 1200 × 1600.
- **Formats:** `.mov`, `.m4v`, or `.mp4` — H.264 at roughly 10–12 Mbps or ProRes 422 (HQ), 30 fps, AAC audio.

Then the content rule, with teeth: the video must be **actual app footage captured from a device** — not a screen-recorded mockup, not an animated concept reel, not external camera footage of someone holding a phone. Apple checks this rigorously, especially for new apps.

## How to make your screenshot pipeline §2.3.3-safe

1. **Capture from a build, not a design tool.** Use Simulator, Xcode UI tests, or manual capture from a TestFlight build to produce the raw screen content. If it didn't come from a running build, it doesn't belong inside the device frame.

2. **Re-capture for every release.** It's tempting to reuse screenshots when only minor UI changes happened. Each time you do this you risk inheriting a rejection from a feature that quietly went away.

3. **Strip IAP prices unless you're certain.** If the prices are dynamic, regional, or change with promotions, leave them out of screenshots entirely. Show feature value rather than price.

4. **If you do show metrics, match the demo state of the shipping build.** Use the same fixture data your TestFlight build uses. Don't render "247K users" if the demo state shows "1.2K."

5. **Treat the device frame as cosmetics.** Pick the visual style that fits your brand — 3D Metal render, flat outline, tilted angle, transparent background, no frame at all. Reviewers don't care about the frame. They care about what's on the screen inside it.

The reason a capture-first tool like [Mockly](/apps/mockly/) is structurally compliant with §2.3.3 by default is that the workflow runs in the safe order: *capture the real screen first, render the device frame around it second.* The screen content is your actual app; the frame is just a render placed around it. The reverse — mock up a concept screen in Figma, drop it into a phone outline, export — is the workflow most likely to drift into rejection territory, because it encourages designing screens that aren't in the app yet.

## TL;DR

- **One iPhone size now.** 6.9-inch (1320 × 2868 / 1290 × 2796) or 6.5-inch (1242 × 2688); Apple scales it to smaller iPhones. iPad apps add 13-inch (2064 × 2752).
- **1–10 screenshots** per localization, PNG or JPEG, flattened. First 2–3 show in search — front-load them.
- **§2.3.3 is about the screen content, not the device frame.** Overlay text, backgrounds, and 3D frames are fine.
- **The screen must be the real shipping app.** Concept art, future-build UI, deleted features, fake metrics, and mismatched IAP prices are the common rejection paths.
- **App Previews:** up to 3, 15–30 seconds, 886 × 1920 on iPhone — same "real footage only" rule.
- **Capture-first workflows pass cleanly;** design-first workflows risk drift.

For the surrounding workflow, the [native screenshot tooling argument](/journal/the-case-for-native-screenshot-tooling/), [shipping screenshots in 39 languages](/journal/shipping-app-store-screenshots-in-39-languages/), and the rest of the [indie iOS developer tools](/for/indie-ios-developers/) go deeper. The specs change with each new device; the §2.3.3 spirit has held for nearly a decade. The rejection emails keep arriving because most indie pipelines make compliance an afterthought instead of the default.
