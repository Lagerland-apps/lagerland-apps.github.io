---
layout: journal
slug: shipping-app-store-screenshots-in-39-languages
title: "How to ship a localised App Store screenshot set in 39 languages without losing your weekend"
date: 2026-05-13
lede: "App Store Connect accepts screenshots in 39 locales. Most indie apps ship in one. The gap isn't ambition — it's that the manual workflow takes 10 to 30 hours per release, and any change to a single screenshot means redoing the localisation pass. This post walks through a reproducible workflow that takes 90 minutes for the first release and 15 minutes for each subsequent one."
quick_answer: "Localising App Store screenshots into 39 languages manually takes 10–30 hours per release: design once, translate text, lay out per locale, render per device size, upload per slot in App Store Connect. The reproducible workflow that fits in an afternoon: capture base-locale screenshots once, build the layout with text as a separate overlay layer (not baked into the image), run automated AI translation across all 39 locales preserving fonts and positioning, render each device × locale combination from a single source, and bulk-upload via the App Store Connect API. The trick is keeping text as an editable layer, not part of the image — which is the single architectural decision most indie screenshot pipelines get wrong."
faq:
  - q: "What's the actual time cost of manual screenshot localisation for 39 languages?"
    a: "Roughly 10 to 30 hours per release for a typical indie app shipping 6 screenshots per device class. The breakdown: 1–2 hours building each base screenshot, 1–3 hours translating 6 strings × 39 languages (with revisions), 4–8 hours laying out each locale × device combination, 2–4 hours uploading via the App Store Connect web UI (with locale-by-locale tab switching). And every time you tweak a single source screenshot, the localisation pass needs to be redone."
  - q: "Why is the manual workflow so slow?"
    a: "Three structural issues. First: most screenshot designs bake text into the image, which means every locale needs a separate flat re-render. Second: App Store Connect's web UI was not built for bulk upload — it's a per-locale, per-device-class form that requires manual file selection. Third: human translation roundtrips add days, and machine translation without preserving font and positioning produces output that looks broken in right-to-left languages."
  - q: "What does 'text as an overlay layer' mean in practice?"
    a: "The base screenshot is a clean capture of the app UI with no marketing text in it. The feature copy ('Track every workout in one tap.') lives in a separate text layer on top of the screenshot in your design tool — Figma component, Sketch text node, Mockly text overlay. When you localise, only the text layer changes per locale; the underlying screenshot stays the same across all 39 versions. This is what makes 39× rendering cheap instead of expensive."
  - q: "How does AI translation handle right-to-left languages like Arabic and Hebrew?"
    a: "Cleanly when the layout engine knows about RTL, badly when it doesn't. Apple's App Store Connect requires Arabic and Hebrew screenshots in right-to-left layout — meaning a left-aligned overlay text in English becomes right-aligned in Arabic, and the visual hierarchy may flip. A tool that runs AI translation and naively pastes the result into the same coordinates produces broken-looking Arabic. A tool that respects RTL layout via Apple's standard text-direction handling produces output that reads correctly to a native Arabic reader."
  - q: "Is App Store Connect's bulk upload API actually faster than the web UI?"
    a: "Yes — by 5 to 10× for a full 39-locale set. The web UI requires selecting each locale tab, dragging the file for each device size, waiting for upload confirmation, then repeating. The Connect API accepts a JSON manifest specifying every (locale, device class, screenshot slot) combination and uploads them in parallel. For 234 screenshots (6 sets × 39 locales) the web UI takes 2–4 hours of attention; the API takes under 3 minutes of compute."
mentioned_apps:
  - mockly
read_time: "10 min read"
excerpt: "App Store Connect accepts screenshots in 39 locales. Most indie apps ship in one because the manual workflow takes 10–30 hours per release. This post walks through a reproducible workflow that does it in 90 minutes for the first release and 15 minutes per release after."
---

App Store Connect accepts screenshots in 39 locales. Almost every indie app ships in one — usually en-US, sometimes also Japanese or German. The gap between what's possible and what gets done is rarely about ambition; it's about the manual workflow taking long enough to consume an entire weekend on the first attempt and an evening on every subsequent release.

This post is the workflow I'd recommend any indie developer follow to get from one locale to 39, with the upfront cost compressed to about 90 minutes and the per-release cost reduced to about 15 minutes. The key insight is structural, not technical: the manual workflow is expensive because most screenshot pipelines bake text into images, which makes the localisation pass O(n) in human hours. If you keep text as an editable overlay layer, the localisation pass becomes O(1) in human hours and O(n) in machine compute — which is a much better trade.

## Why the manual workflow is so slow

If you're doing this manually today, your time probably looks something like this for a release with 6 screenshots per device class across 4 device classes (iPhone 6.9", 6.7", iPad 13", Mac):

- **Design pass:** 1–2 hours to build the 6 base screenshots in Figma or your design tool of choice. This is the actual creative work and it's fine.

- **Localisation prep:** 1–3 hours getting feature copy translated. Either you wait for human translators (multi-day roundtrip), or you batch-paste into ChatGPT/Claude/DeepL and edit the worst output, or you've already invested in a translation memory tool.

- **Layout pass:** Here's where it gets brutal. 6 screenshots × 39 locales = 234 unique layouts. If each takes 1 minute to render (in a fast workflow with text-as-layer) you get 4 hours. If each takes 5 minutes (baked-text workflow with per-locale edits and re-renders) you get 20 hours.

- **App Store Connect upload pass:** The web UI is a per-locale, per-device-class form. You select a locale tab, drag in 6 files for iPhone 6.9", wait for upload, switch to iPhone 6.7", drag in 6 more, repeat for iPad and Mac, switch to next locale, do it all again. Plan for 2–4 hours of attention.

That's 8 to 30 hours total per release, depending entirely on whether your screenshot pipeline keeps text as a layer or bakes it in. Every subsequent release that changes a single source screenshot or a single string repeats most of the pain.

This is the implicit reason almost every indie app ships in one or two locales. It's not the App Store Connect requirements that are unreasonable — Apple is right to want localised screenshots — it's that the consumer tooling makes the workflow so expensive that nobody actually does it.

## The architecture that makes 39 locales cheap

The structural shift is this: **keep your text as a separate, editable overlay layer, never baked into the screenshot image.** Once you adopt this constraint, everything downstream becomes mechanical.

What that means in each tool:

- **In Figma:** the base screenshot is one component (a flat image layer). The feature copy is a separate Text node on top of it. To localise, you duplicate the frame and edit the Text node's content; the base image stays referenced from the same source.

- **In Sketch:** same pattern. Flat screenshot layer, text node on top. Localise the text node.

- **In Mockly:** the architecture is built in — every screenshot is a project with the raw capture as one layer, the device frame as a 3D rendered layer, and overlaid text as separate editable text elements. AI translation operates on the text elements only; the captured screen content is byte-identical across all 39 locales.

The benefit compounds. Once text is a layer, you can:

1. Run AI translation against all 39 locales in seconds rather than days.
2. Render each (locale × device size) combination from the same source in milliseconds rather than minutes.
3. Re-render the entire 234-screenshot bundle bit-for-bit identically when you change a single string.

This is what makes the 15-minute-per-release cost work. The expensive parts (rendering, layout, upload) are mechanical compute, not human labour.

## The 90-minute first-release workflow

Assuming you've done the initial design pass already (the 1–2 hours of actual creative work) and you have base screenshots with text-as-layer:

**Step 1 (15 min):** Set up locale list. App Store Connect supports 39 locales; you don't have to ship all of them. Pick the 5–10 that match your largest addressable markets. Most indie apps see meaningful conversion lift from English + Japanese + Simplified Chinese + German + Spanish + Korean. Expand from there as data justifies.

**Step 2 (10 min):** Configure your AI translation provider. OpenAI's GPT-4, Anthropic's Claude, and DeepL are the three I'd recommend in 2026 — all produce App-Store-acceptable output with English/Japanese/Chinese/German source-target pairs. For RTL languages (Arabic, Hebrew), spot-check Claude or use a native speaker review pass for the first release.

**Step 3 (5 min):** Run translation. If you're using Mockly: paste your base text strings, select target locales, click "Translate." Output goes straight into the layered project per locale. If you're using a manual workflow: paste each base string into the AI tool, get the 39-locale output, paste back into your design tool one locale at a time.

**Step 4 (20 min):** Render every (device × locale) combination. Mockly handles this with one button and ~50 milliseconds per render. A manual Figma workflow can be scripted with the Figma API but requires upfront setup; without scripting, this is the part where the 90-minute workflow stretches.

**Step 5 (10 min):** Spot-check the RTL languages and any high-stakes locale (Japanese typically — the character density is different from English and overflow is common). Adjust text overlay sizes if anything looks off.

**Step 6 (5 min):** Upload via App Store Connect API. Mockly's direct upload pipeline handles this; Fastlane `deliver` is the open-source alternative if you've invested in Fastlane setup. Either way: ~3 minutes of compute for a full 234-screenshot bundle.

Total: about 65 minutes if everything goes smoothly, 90 if you hit one or two spot-check issues. After this, every subsequent release is 15 minutes because the architecture is in place.

## What goes wrong, and how to avoid it

**RTL languages need explicit handling.** Arabic and Hebrew layouts flip — left-aligned overlay text should become right-aligned, and visual reading order may need to mirror. Tools that use Apple's standard text-direction APIs handle this automatically; tools that don't will produce broken-looking Arabic output. Always native-speaker-review the first Arabic release.

**Japanese and Chinese character density is different.** A 7-word English headline fits in a header band; the same headline in Japanese may be 3 characters wide, and in German may be 12 words long and overflow. Build the text overlay with auto-resize or explicit length budgets per locale, not fixed pixel widths.

**Sometimes the AI translation gets a domain term wrong.** "Workout" in fitness context translates differently from "workout" in general fitness. Use a glossary or instruct the AI translation tool with brand-specific term mappings. For a fitness app: provide a 5-term glossary mapping reps / sets / RPE / etc. to native equivalents.

**Don't translate proper nouns.** Your app name stays "Strava" in every locale. Some translation tools will helpfully render "Strava" into the target script (it shouldn't); confirm proper-noun handling on first run.

**App Store Connect rate limits matter for bulk upload.** The Connect API has burst limits. Tools that respect them (Mockly's pipeline, Fastlane deliver with proper config) upload cleanly; tools that hammer the API can get temporary backoff.

## What the actual tools cost

The economics for 2026 indie pipelines:

- **Figma + manual translation + manual upload:** Free (within Figma free plan). Time cost is the 10–30 hours described above. For an app shipping 3 releases per year that's 30–90 hours per year — half a developer-week.
- **Figma + AI translation (BYO API) + manual upload:** ~$2–5 of API calls per release. Time cost drops to 4–10 hours.
- **Subscription SaaS (Screenshots.pro / AppLaunchpad Pro / Screenshot Studio):** $19–$49 per month = $228–$588 per year. Time cost drops to 1–3 hours per release.
- **[Mockly](/apps/mockly/) (one-time $12.99):** Time cost drops to 90 min first release, 15 min subsequent releases. AI translation against your own API key (~$0.50–$2 per release at 2026 API prices).

The cost-of-tool is small compared to the cost-of-time. The decision is mostly about which workflow architecture you adopt, not which logo is on the tool.

## TL;DR

- **39-locale localisation manually costs 10–30 hours per release** and most indie apps skip it entirely for this reason.
- **The fix is architectural:** keep overlaid text as a separate editable layer in your design tool, never baked into the screenshot image.
- **Once text-as-layer is in place,** AI translation runs in seconds, rendering in milliseconds, and the App Store Connect API bulk-uploads in minutes.
- **First release: 90 minutes. Subsequent releases: 15 minutes.** The compounding return on the first hour of architecture work is months of reclaimed time per year.
- **Watch for RTL handling (Arabic/Hebrew),** character density differences (Japanese/Chinese/German), proper-noun preservation, and App Store Connect API rate limits.
- **Related reading:** [Why Mac-native is the right architecture for App Store screenshots](/journal/why-mac-native-for-app-store-screenshots/) explains why local rendering matters for the architecture above, and [What every App Store Review Guidelines screenshot rule actually means](/journal/app-store-screenshot-review-guidelines-explained/) covers the compliance side of the same pipeline.

The 39-locale workflow isn't about ambition. It's about whether your text layer is editable. Get that architecture right and the rest is mechanical.
