---
layout: journal
slug: every-media-tool-already-on-your-mac
title: "The Mac already shipped with every media tool — someone just had to wire them together"
seo:
  title: "133 Local Media Tools for Mac — No Uploads, No Cloud"
  description: "MediaKit puts 133 video, audio, image, PDF, and archive tools behind one drag-and-drop Mac app — every operation local, nothing ever leaves your machine."
  keywords:
    - "mac media tools"
    - "local file converter mac"
    - "offline media converter"
    - "mac video audio image pdf tools"
    - "convert files without uploading"
    - "mediakit"
date: 2026-05-09
lede: "MediaKit is 133 local tools for video, audio, image, PDF, and archive work, behind a single drag-and-drop Mac interface. None of the operations ever leave your machine. This post is the case for that — and why \"upload your file to a random website to convert it\" remains one of the worst defaults on the open web in 2026."
quick_answer: "MediaKit is a native macOS app that consolidates 133 on-device media conversion tools — video, audio, image, PDF, archive, ebook — behind a single drag-and-drop surface. Every operation runs locally on Apple frameworks like AVFoundation, CoreImage, PDFKit, Vision, and AppleArchive. Files never leave the machine, unlike CloudConvert, Zamzar, or Smallpdf. Five tools stay free forever."
faq:
  - q: "Is there a Mac alternative to CloudConvert or Smallpdf?"
    a: "MediaKit is a native macOS app with 133 conversion tools that runs every operation locally on Apple frameworks like AVFoundation, CoreImage, PDFKit, Vision, and AppleArchive. Files never leave the machine, unlike CloudConvert, Zamzar, Smallpdf, or iLovePDF, which upload to operator infrastructure for processing."
  - q: "Which MediaKit tools are free forever?"
    a: "Five tools stay free forever with no nag screen: Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress. The remaining 128 tools are unlocked during a three-day trial, then require a one-time Pro purchase. There is no subscription."
  - q: "Can MediaKit replace Final Cut Pro or DaVinci Resolve?"
    a: "No. MediaKit performs linear operations like compress, convert, trim, crop, merge, and normalize. It does not have a timeline and is not a non-linear editor. If you are cutting a film, use Final Cut Pro or DaVinci Resolve. MediaKit is for everyday conversions, not editorial work."
  - q: "Does MediaKit work with Shortcuts?"
    a: "Yes. MediaKit ships six Shortcuts actions plus a menu bar item, so its tools can be wired into automated workflows on a schedule or triggered from other apps. All Shortcuts actions run locally and never touch the internet."
mentioned_apps:
  - mediakit
read_time: "6 min read"
excerpt: "MediaKit is a native macOS app with 133 on-device tools for compressing, converting, and editing video, audio, image, PDF, archive, and ebook files — built on Apple's AVFoundation, CoreImage, PDFKit, Vision, Speech, Compression, and AppleArchive frameworks. This post argues that the Mac has shipped the primitives for local media work for years, that cloud converters like CloudConvert, Zamzar, and Smallpdf persist mostly because nobody consolidated the local tools behind a single UI, and explains the five-tools-free-forever pricing."
---

It's a Saturday in May. Somewhere on the open web, someone is uploading a four-gigabyte video of a child's piano recital to a free conversion site, because the format their camera produces is the format their parent cannot open. The site will take the video, run it through a server they cannot see, log the request, possibly cache the file, certainly read the metadata, and hand back something that plays on a Windows laptop. The user will close the tab and assume it's fine.

It is not fine. It is also, in 2026, unnecessary.

[MediaKit](/apps/mediakit/) is the small Mac app the studio shipped this spring on exactly this premise: every media-conversion operation a normal user needs has, for a decade, been doable locally on a Mac, and the persistent dominance of CloudConvert, Zamzar, Smallpdf, and the rest exists not because the local primitives are missing but because nobody had bothered to consolidate them behind a single drag-and-drop interface.

This is the Saturday essay on what MediaKit is, what it isn't, and why "free conversion website" is one of the worst remaining defaults on the open web.

## What media tools does Apple already ship on the Mac?

I want to be precise about this, because the contribution MediaKit makes is real but it is also limited, and it would be dishonest to claim otherwise.

The actual algorithms — H.264 encoding, HEVC encoding, AAC encoding, PNG quantization, PDF compression, RAR extraction, AES-256 archive encryption, OCR, on-device speech transcription, image upscaling, background removal — all of these are first-party Apple frameworks shipped with macOS. Specifically:

- **AVFoundation** handles every video and audio operation MediaKit performs. Compression, conversion, trimming, merging, frame-accurate cuts — all of it.
- **CoreImage** handles every image transform, color adjustment, and pixel-level filter.
- **PDFKit** handles merge, split, redact, sign, watermark, OCR, header/footer, and vector-preserving edits.
- **Vision** handles OCR, image classification, and background removal.
- **Speech** handles on-device transcription of audio and video.
- **Compression** and **AppleArchive** handle ZIP, TAR, GZIP, XZ, BZIP2, and RAR extraction, with path-traversal-safe extraction and AES-256 encryption.

None of this is new. None of it is proprietary to the studio. The frameworks have been on every Mac for years. They are sandboxed, hardened-runtime-safe, and have been optimized for Apple Silicon since the M1 launched.

What MediaKit does is wire them together. One app. One drag-and-drop surface. One menu bar item. Six Shortcuts actions. 133 distinct tools mapped against the formats and operations a normal Mac user actually wants — instead of five separate utilities, each with its own settings panel, license model, and update cadence.

That's the whole bet. The bet is *consolidation*, not *novelty*. I am going to keep saying this honestly because the marketing temptation to overclaim is real.

## Why the cloud converters persist anyway

If the local primitives have been there for years, why does the median user still upload their video to a stranger?

A few reasons, and they are worth being clear about because they are also the reasons MediaKit needs to be a specific shape:

1. **Discovery.** Search "convert HEIC to JPG" and the top results are conversion websites. Search "convert HEIC to JPG on Mac" and the top results are *also* conversion websites. Apple does not market the existence of CoreImage to end users. They shouldn't have to.
2. **Format coverage.** Mac built-ins handle the common formats; the cloud converters handle the long tail — RAR v5 with encryption, AVIF, ALAC inside an unusual MKV. The user reaches for the website because the website *will* handle whatever they throw at it. MediaKit's goal is to cover the same long tail using Apple frameworks plus a handful of permissively-licensed local libraries — never a cloud round-trip.
3. **One-shot UX.** The website is one click — paste, drop, download. Native tools historically required you to know which app to open. The drag-and-drop unified surface in MediaKit is specifically a response to this. Drop any file, MediaKit picks the right tool.
4. **Trust by exhaustion.** Users are tired. The website is fast and looks professional. The privacy cost is invisible. The cost only becomes legible if you imagine that file being indexed somewhere, or showing up in a data-breach disclosure later.

I do not think most users *want* to upload sensitive files to strangers. I think they have not been given a default that is just as easy not to.

## What's free, and what's paid

The free-forever tier is five tools: **Video Compress, Image Compress, Image Resize, Audio Convert, PDF Compress.** These are the operations the median Mac user actually performs — the email-attachment compress, the iPhone-photo-to-JPG, the audio rip. They stay free, forever, with no nag screen, no countdown, no upsell modal blocking the export.

The first three days, every one of the 133 tools is unlocked, so you can find out whether the long tail matters to you before you decide. After three days, the five free tools stay free; the remaining 128 require Pro. There is no subscription you can forget to cancel — Pro is a one-time purchase.

Pricing the free tier this way is, in the indie Mac segment, slightly unusual. Handbrake is free. ImageOptim is free. Keka is free. The studio's argument is that the operations a typical user runs *most often* should be free in MediaKit too — not as a trial-extension trick, but as the actual long-term offer. If you only ever compress videos and convert HEIC, MediaKit costs you nothing, forever, and you still get a sandboxed App Store app instead of a Homebrew install of FFmpeg.

The Pro tier exists for the people who run the long tail. The studio is not trying to convert the free user into a Pro user — those are different users.

## What this is not

A few clarifications, because I have learned to write them:

- **MediaKit is not a non-linear editor.** It does not replace Final Cut Pro or DaVinci Resolve. If you are cutting a film, please do not use MediaKit; the operations available are linear (compress, convert, trim, crop, merge, normalize), not editorial. The studio is not going to add a timeline.
- **MediaKit is not a generative AI tool.** Vision and Speech are *recognition* frameworks — OCR, background segmentation, transcription. Image upscaling is real and produces a larger pixel buffer from a smaller one, but the studio is not running diffusion models. If you need image generation, MediaKit is the wrong tool.
- **MediaKit is not a cloud sync tool.** There is no cloud. If you want your edits accessible from another device, save them to iCloud Drive yourself, or wherever you keep your files.
- **MediaKit is not a fix for the cloud-converter problem at the institutional level.** Universities still tell students to upload PDFs to a third-party tool because the IT department has not bothered to install anything. The studio cannot fix that from outside. But on a personal Mac, the answer is now in the App Store.

## A note on the holiday weekend

For US, Canadian, Australian, and several European readers, tomorrow is Mother's Day. There is a non-zero chance you are about to send a family video to a parent in a format they cannot open. If you find yourself reaching for a conversion website to fix it: please don't.

The file is going to ride through someone else's data centre on the way back. It is not going to be deleted the moment you close the tab, regardless of what the privacy policy says.

[MediaKit](/apps/mediakit/) is free for the operation you most likely need (Video Compress, Image Compress, Audio Convert, PDF Compress), three days unlocked for everything else, and never leaves the machine. That's the whole pitch this weekend.

The studio's broader argument on cloud-vs-local file handling is in the [photos elevator essay](/journal/your-photos-shouldnt-ride-the-elevator/) from March, if you want the longer version. The shorter version is that Apple has been giving us the primitives for years and we should use them.
