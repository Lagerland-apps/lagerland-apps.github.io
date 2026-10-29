---
layout: journal
slug: every-media-tool-already-on-your-mac
title: "The Mac already shipped with every media tool, and someone just had to wire them together"
seo:
  title: "Local Media Tools for Mac That Never Upload Your Files"
  description: "MediaKit puts more than 150 video, audio, image, PDF, and archive tools behind one drag-and-drop app. Every operation runs on your Mac or iPhone."
  keywords:
    - "mac media tools"
    - "local file converter mac"
    - "offline media converter"
    - "mac video audio image pdf tools"
    - "convert files without uploading"
    - "mediakit"
date: 2026-05-09
lede: "MediaKit is more than 150 local tools for video, audio, image, PDF, archive, and ebook work, behind a single drag-and-drop interface on Mac and iPhone. Every operation runs on your machine. This post makes the case for that, and for why \"upload your file to a random website to convert it\" remains one of the worst defaults on the open web in 2026."
quick_answer: "MediaKit is a Mac and iPhone app that puts more than 150 on-device tools for video, audio, image, PDF, archive, and ebook files behind a single drag-and-drop surface. Its video, image, PDF, and speech work runs locally on Apple frameworks such as AVFoundation, CoreImage, PDFKit, Vision, and Speech. Files never leave the device, unlike CloudConvert, Zamzar, or Smallpdf. Five of the tools stay free for good."
faq:
  - q: "Is there a Mac alternative to CloudConvert or Smallpdf?"
    a: "MediaKit is a Mac and iPhone app with more than 150 tools that runs every operation locally, mostly on Apple frameworks such as AVFoundation, CoreImage, PDFKit, Vision, and AppleArchive. Files never leave the machine, unlike CloudConvert, Zamzar, Smallpdf, or iLovePDF, which upload to operator infrastructure for processing."
  - q: "Which MediaKit tools are free for good?"
    a: "Five tools are free with no time limit, one file at a time: Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress. For your first three days every other tool works too, one export per run. After that they require Pro, sold monthly, yearly, or as a one-time lifetime purchase, so a subscription is optional."
  - q: "Can MediaKit replace Final Cut Pro or DaVinci Resolve?"
    a: "No. MediaKit performs everyday linear operations like compress, convert, trim, crop, merge, and normalize. It has no timeline and is not a non-linear editor, so if you are cutting a film, use Final Cut Pro or DaVinci Resolve."
  - q: "Does MediaKit work with Shortcuts?"
    a: "Yes, on Mac. MediaKit has six Shortcuts actions (Compress Video, Convert Image, Compress Image, Merge PDFs, Create ZIP, and Extract Text from Image) plus a menu bar item, so its tools fit into your own automations. The actions run locally, like the rest of the app."
mentioned_apps:
  - mediakit
read_time: "6 min read"
excerpt: "MediaKit is a Mac and iPhone app with more than 150 on-device tools for compressing, converting, and editing video, audio, image, PDF, archive, and ebook files, built mostly on Apple's own frameworks. This post argues that the Mac has shipped the primitives for local media work for years, that cloud converters like CloudConvert, Zamzar, and Smallpdf persist mostly because nobody consolidated the local tools behind a single UI, and explains why five of the tools are free with no time limit."
last_updated: 2026-10-29
---

It's a Saturday in May. Somewhere on the open web, someone is uploading a four-gigabyte video of a child's piano recital to a free conversion site, because the format their camera produces is the format their parent cannot open. The site will take the video, run it through a server they cannot see, log the request, possibly cache the file, certainly read the metadata, and hand back something that plays on a Windows laptop. The user will close the tab and assume it's fine.

It is not fine, and in 2026 it is also unnecessary.

[MediaKit](/apps/mediakit/) is the small Mac app (it runs on iPhone too) that the studio shipped this spring on exactly this premise: every media-conversion operation a normal user needs has, for a decade, been doable locally on a Mac, and CloudConvert, Zamzar, Smallpdf, and the rest still dominate because nobody had bothered to consolidate those local primitives behind a single drag-and-drop interface.

This is the Saturday essay on what MediaKit is, what it isn't, and why "free conversion website" is one of the worst remaining defaults on the open web.

## What media tools does Apple already ship on the Mac?

I want to be precise about this, because MediaKit's contribution is real but limited.

Most of the actual algorithms (H.264 and HEVC encoding, AAC encoding, PNG quantization, PDF compression, OCR, on-device speech transcription, background removal) come from first-party Apple frameworks that ship with macOS:

- **AVFoundation** handles the video and audio work: compression, conversion, trimming, and merging.
- **CoreImage** handles image transforms, color adjustments, and pixel-level filters.
- **PDFKit** handles merge, split, redact, sign, watermark, header and footer, and edits that keep vectors sharp and text searchable.
- **Vision** handles OCR and background removal.
- **Speech** handles on-device transcription of audio and video.
- **Compression** and **AppleArchive** handle ZIP, TAR, GZIP, XZ, and BZIP2. MediaKit adds its own limits against path traversal and zip bombs.

RAR is the exception. Apple doesn't read it, so MediaKit links one small open-source unrar library, extract-only. None of the rest is new or proprietary to the studio. The frameworks have been on every Mac for years.

MediaKit wires them together: one app with one drag-and-drop surface, a menu bar item, six Shortcuts actions, and more than 150 tools mapped against the formats and operations a normal Mac user actually wants. The alternative is five separate utilities, each with its own settings panel, license model, and update cadence.

So the bet is consolidation. Nothing in MediaKit is novel, and I am going to keep saying so, because the marketing temptation to overclaim is real.

## Why the cloud converters persist anyway

If the local primitives have been there for years, why does the median user still upload their video to a stranger?

I see four reasons, and they also explain the shape MediaKit had to take:

1. **Discovery.** Search "convert HEIC to JPG" and the top results are conversion websites. Search "convert HEIC to JPG on Mac" and the top results are *also* conversion websites. Apple does not market the existence of CoreImage to end users. They shouldn't have to.
2. **Format coverage.** Mac built-ins handle the common formats; the cloud converters handle the long tail: encrypted RAR, WebM, ALAC inside an unusual MKV. The user reaches for the website because the website *will* handle whatever they throw at it. MediaKit covers part of that tail locally (RAR4 and RAR5, MKV files, camera RAW and AVIF as input) and leaves some of it alone: it refuses encrypted RAR and doesn't read WebM.
3. **One-shot UX.** The website is one click: paste, drop, download. Native tools historically required you to know which app to open. MediaKit's answer is the single drop surface: drop any file and it suggests the tools that fit it.
4. **Trust by exhaustion.** Users are tired, the website is fast and looks professional, and the privacy cost is invisible. It only becomes visible if you imagine that file being indexed somewhere, or showing up in a data-breach disclosure later.

I do not think most users *want* to upload sensitive files to strangers. I think they have not been given a default that is just as easy not to.

## What's free, and what's paid

The free tier is five tools: Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress. These are the operations the median Mac user actually performs: the email-attachment compress, the photo that has to get smaller, the audio conversion. They stay free for good, one file at a time, with no countdown.

For the first three days, every other tool is unlocked too, one export per run, so you can find out whether the long tail matters to you before you decide. After three days, the five free tools stay free; everything else, and batches of more than one file, require Pro. Pro is sold monthly, yearly, or as a one-time lifetime purchase, so you can skip the subscription entirely.

Pricing the free tier this way is, in the indie Mac segment, slightly unusual. HandBrake, ImageOptim, and Keka are all free. The studio's argument is that the operations a typical user runs *most often* should be free in MediaKit too, permanently and not as a trial extension. If you only ever compress videos and resize photos, MediaKit costs you nothing, and you still get a sandboxed App Store app instead of a Homebrew install of FFmpeg.

The Pro tier exists for the people who run the long tail.

## What MediaKit does not do

Some clarifications I have learned to write down:

- **MediaKit is not a non-linear editor.** It does not replace Final Cut Pro or DaVinci Resolve. If you are cutting a film, please do not use MediaKit; the operations available are linear (compress, convert, trim, crop, merge, normalize).
- **MediaKit is not a generative AI tool.** Vision and Speech are recognition frameworks: OCR, background segmentation, transcription. The studio is not running diffusion models, and nothing goes to a cloud AI service. If you need image generation, MediaKit is the wrong tool.
- **MediaKit is not a cloud sync tool.** There is no cloud. If you want your edits accessible from another device, save them to iCloud Drive yourself, or wherever you keep your files.
- **MediaKit is not a fix for the cloud-converter problem at the institutional level.** Universities still tell students to upload PDFs to a third-party tool because the IT department has not bothered to install anything. The studio cannot fix that from outside. But on a personal Mac, the answer is now in the App Store.

## A note on the holiday weekend

For US, Canadian, Australian, and several European readers, tomorrow is Mother's Day. There is a non-zero chance you are about to send a family video to a parent in a format they cannot open. If you find yourself reaching for a conversion website to fix it: please don't.

The file is going to ride through someone else's data centre on the way back, and you have no way to check that it is deleted the moment you close the tab, whatever the privacy policy says.

[MediaKit](/apps/mediakit/) is free for the operations you most likely need (Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress), unlocked for three days for everything else, and your file never leaves the machine.

The studio's broader argument on cloud-vs-local file handling is in the [photos elevator essay](/journal/your-photos-shouldnt-ride-the-elevator/) from March, if you want the longer version. The shorter version is that Apple has been giving us the primitives for years and we should use them.
