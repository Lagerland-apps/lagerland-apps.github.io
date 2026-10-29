---
layout: journal
slug: shipping-app-store-screenshots-in-39-languages
title: "How to ship a localised App Store screenshot set in 39 languages without losing your weekend"
seo:
  title: "Localized App Store Screenshots in 39 Languages, Fast"
  description: "Mockly lists 50 App Store languages; most apps ship one. Why localizing screenshots eats a weekend per release, and a workflow that scales."
  keywords:
    - "localized app store screenshots"
    - "app store screenshot localization"
    - "app store screenshots multiple languages"
    - "fastlane frameit alternative"
    - "localize screenshots"
    - "app store locales"
date: 2026-05-13
lede: "App Store Connect takes screenshots in dozens of languages, and Mockly lists 50 of them. Most indie apps ship in one, because the manual workflow can eat a weekend on the first release, and any change to a single screenshot means redoing the localisation pass. This post walks through a workflow that keeps the text editable, so adding languages becomes mostly mechanical work."
quick_answer: "Localising App Store screenshots by hand is slow because every language repeats every step: design, translate, lay out, export per device size, and upload per language in App Store Connect. The fix is to keep the text as a separate, editable layer that is never baked into the screenshot image. Capture your base screenshots once, build the layout with text on top, translate the text for each language with AI or a translator, export each language from the same source, and upload through the App Store Connect API instead of the web form. Mockly works this way: one project holds up to 50 App Store languages, translates the text blocks with your own OpenAI, Anthropic, or Google key or through a CSV file, and uploads to App Store Connect."
faq:
  - q: "What's the actual time cost of manual screenshot localisation for 39 languages?"
    a: "It adds up to many hours per release for a typical indie app with six screenshots per device size. The work splits into building each base screenshot, translating every caption into every language (with revisions), laying out each language and device combination, and uploading through the App Store Connect web form one language at a time. Every time you change one source screenshot, most of the localisation pass has to be redone. Mockly now lists 50 App Store languages, and the cost grows with each one you add."
  - q: "Why is the manual workflow so slow?"
    a: "Most screenshot designs bake text into the image, so every language needs a separate flat re-render. The App Store Connect web form was not built for bulk upload: you pick a language, then a device size, then select the files by hand. Human translation round trips add days, and machine translation pasted into a fixed layout often overflows or breaks the design."
  - q: "What does 'text as an overlay layer' mean in practice?"
    a: "The base screenshot is a clean capture of the app UI with no marketing text in it. The feature copy ('Track every workout in one tap.') lives in a separate text layer on top of the screenshot in your design tool: a Figma component, a Sketch text node, or a text block in Mockly. When you localise, only the text layer changes per language, and the screenshot underneath can stay the same in every version. That is what makes many languages cheap."
  - q: "How does AI translation handle right-to-left languages like Arabic and Hebrew?"
    a: "Check them by hand. A translation pasted into a layout built for English keeps the English alignment, which can look wrong to an Arabic or Hebrew reader. Treat those languages as their own layout: in Mockly, unlink the language from the source and adjust its text blocks, and have a native speaker review the first release."
  - q: "Is App Store Connect's bulk upload API actually faster than the web UI?"
    a: "For a full multi-language set, yes. The web form makes you select each language, pick each device size, add the files, and wait for each upload before moving on. The App Store Connect API lets a tool upload every language and device size in one run without that clicking. Mockly uses the API with your own App Store Connect key, and fastlane deliver does the same from the command line."
mentioned_apps:
  - mockly
read_time: "8 min read"
excerpt: "App Store Connect takes screenshots in dozens of languages, and Mockly lists 50. Most indie apps ship in one because the manual workflow eats a weekend per release. This post walks through a workflow that keeps the text editable, so adding languages becomes mechanical."
last_updated: 2026-10-29
---

App Store Connect takes screenshots in dozens of languages, and Mockly's language list now holds 50 of them. Almost every indie app ships in one, usually en-US, sometimes also Japanese or German. The gap between what's possible and what gets done comes down to the manual workflow, which can consume a whole weekend on the first attempt and an evening on every release after that.

The title of this post says 39, the number it started with. The workflow below is the same whatever the count, and the rest of the post uses today's number where it describes Mockly.

This is the workflow I'd recommend to any indie developer going from one language to many. The manual workflow is expensive because most screenshot pipelines bake text into images, which makes the localisation pass grow in human hours with every language you add. If you keep text as an editable overlay layer, the human work stays roughly the same and the per-language work becomes mechanical, which is a much better trade.

## Why the manual workflow is so slow

If you're doing this by hand today, a release with 6 screenshots per device size across a few device sizes (iPhone 6.9", iPad 13", Mac) breaks down like this:

- **Design pass:** building the 6 base screenshots in Figma or your design tool of choice. This is the real creative work, and the time is well spent.

- **Localisation prep:** getting the feature copy translated. Either you wait for human translators (a multi-day round trip), or you batch-paste into an AI tool and fix the worst output, or you've already invested in a translation memory tool.

- **Layout pass:** this is the slow part. 6 screenshots in 39 languages is 234 layouts, and at 50 languages it's 300. If text is a layer, each one is a quick check. If text is baked in, each one is an edit and a re-render.

- **App Store Connect upload pass:** the web form works per language and per device size. You select a language, add 6 files for the iPhone size, wait for the upload, switch to iPad, add 6 more, repeat for Mac, switch to the next language, and do it all again.

The total depends almost entirely on whether your screenshot pipeline keeps text as a layer or bakes it in. Every later release that changes a single source screenshot or a single string repeats most of the pain.

That is why almost every indie app ships in one or two languages. Apple is right to want localised screenshots, and its requirements are reasonable. The consumer tooling makes the workflow so expensive that few people do it.

## The architecture that makes many languages cheap

Keep your text as a separate, editable overlay layer, and never bake it into the screenshot image. Once you adopt that constraint, everything downstream becomes mechanical.

What that means in each tool:

- **In Figma:** the base screenshot is one component (a flat image layer). The feature copy is a separate Text node on top of it. To localise, you duplicate the frame and edit the Text node's content, and the base image stays referenced from the same source.

- **In Sketch:** the same pattern. Flat screenshot layer, text node on top. Localise the text node.

- **In Mockly:** the structure is built in. A project is a list of pages, each with your screenshot on a 3D device, text blocks on top, and a background. Each language follows the source language until you unlink it, and AI Translate changes only the text blocks. If a language needs its own screenshots, a different image, or a smaller headline, you change that language and leave the rest alone.

Once text is a layer, you can:

1. Translate every caption into every language in one pass instead of one language at a time.
2. Export each language from the same source instead of rebuilding it.
3. Change a single string and export the set again without touching the layout.

That is how a release shrinks to a short session: the slow parts (layout, export, upload) become mechanical instead of manual.

## The first-release workflow

This assumes you've done the initial design pass (the real creative work) and have base screenshots with text as a layer.

**Step 1: Set up the language list.** Mockly lists 50 App Store languages, and you don't have to ship all of them. Start with the languages that match your largest markets, often English, Japanese, Simplified Chinese, German, Spanish, and Korean, and expand when your data justifies it.

**Step 2: Choose a translation route.** In Mockly you can add your own OpenAI, Anthropic, or Google key and choose the model for each provider in Settings, or export a CSV for a translator and import it back. For languages you can't read yourself, plan a native-speaker review on the first release. AI output is machine translation.

**Step 3: Translate.** In Mockly, open the Text Editing tab, choose AI Translate, pick the target languages, and translate one page or all pages. Text blocks marked Do not translate (your app name, for example) are skipped. In a manual workflow, you paste each base string into an AI tool and paste the results back into your design tool one language at a time.

**Step 4: Export every language.** Mockly's Save Images writes every page as PNG or HEIC at the artboard's exact pixel size, for the current language or all of them. A Figma workflow can be scripted with the Figma API, but that takes setup, and without it this is the step where the afternoon stretches.

**Step 5: Spot-check.** Look at any right-to-left language and any high-stakes language (often Japanese, where character density differs from English, and German, where headlines run long). If one needs its own text size or layout, unlink it and adjust only that language.

**Step 6: Upload.** Mockly uploads through the App Store Connect API with your API key, reads the display type from the artboard, and replaces the screenshots already in that display type for the languages you pick. fastlane `deliver` is the open-source alternative if you've already set up fastlane.

After the first release, later ones are mostly steps 3, 4, and 6, because the structure is already in place.

## What goes wrong, and how to avoid it

**Right-to-left languages need a look.** Arabic and Hebrew readers expect right-aligned text, and a caption pasted into an English layout keeps its English alignment. Treat these languages as their own layout, and have a native speaker review the first Arabic or Hebrew release.

**Japanese and Chinese character density is different.** A 7-word English headline fits in a header band. The same headline in Japanese may be a few characters wide, and in German it may run long and overflow. Set text sizes per language where needed instead of trusting one fixed width.

**Sometimes the AI translation gets a domain term wrong.** "Set" in a fitness app means something different from "set" in a settings screen. Give the translator, human or AI, a short glossary of your product terms, and read the output for the terms that matter.

**Don't translate proper nouns.** Your app name stays the same in every language. Some translation tools will helpfully transliterate it into the target script. In Mockly, mark that text block Do not translate, and check proper nouns on the first run.

**Uploads replace what's there.** Uploading through the API (Mockly or fastlane deliver) replaces the screenshots in that display type. Check the set before you send it, especially for languages you can't read.

## What the actual tools cost

The trade-offs for indie pipelines:

- **Figma, manual translation, and manual upload:** free within Figma's free plan. The cost is your time, and it repeats every release.
- **Figma, AI translation on your own key, and manual upload:** a small API bill per release. Translation gets quick, and layout and upload stay manual.
- **Subscription web tools (Screenshots.pro, AppLaunchpad, Screenshot Studio):** $19 to $49 per month when we last checked. Most of the workflow moves into the tool.
- **[Mockly](/apps/mockly/) (one-time {P_APP@mockly}, no subscription):** a Mac app that holds up to 50 languages in one project, translates with your own AI key (your provider bills you) or a CSV file, and uploads to App Store Connect.

The price of the tool is small next to the cost of your time. What matters most is which workflow architecture you adopt.

## TL;DR

- **Localising screenshots by hand costs many hours per release,** and most indie apps skip it for that reason.
- **The fix is architectural:** keep overlaid text as a separate editable layer in your design tool, and never bake it into the screenshot image.
- **Once text is a layer,** translation, export, and upload become mechanical steps you repeat each release.
- **The first release takes the longest.** Later releases reuse the same structure.
- **Watch for right-to-left languages (Arabic, Hebrew),** character density (Japanese, Chinese, German), proper nouns, and uploads that replace the existing set.
- **Related reading:** [Why Mac-native is the right architecture for App Store screenshots](/journal/why-mac-native-for-app-store-screenshots/) explains why local projects matter for the setup above, and [What every App Store Review Guidelines screenshot rule actually means](/journal/app-store-screenshot-review-guidelines-explained/) covers the compliance side of the same pipeline.

Whether you can ship every language comes down to whether your text layer is editable. Get that right and the rest is mechanical.
