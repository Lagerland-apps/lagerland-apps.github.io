---
layout: journal
slug: your-photos-shouldnt-ride-the-elevator
title: "Your photos shouldn't ride the elevator to a stranger's data centre"
date: 2026-03-28
lede: "Almost every online image converter you've used in the last decade uploaded your file to a server you don't control, processed it there, and gave you back a download. The convenience is real. The privacy implication is not small. MediaKit is the studio's argument that 133 of those tools should run on your Mac instead."
read_time: "5 min read"
excerpt: "MediaKit is a Mac app with 133 local conversion tools — video compression, HEIC to JPG bulk, PDF tooling, RAR v5 extraction on Apple Silicon, and more. This post argues for local-first media processing, explains the Shortcuts integration, and makes the case for the freemium structure (5 tools free forever, 128 behind Pro)."
---

Pick the most recent moment in the last week when you needed to convert a media file. A HEIC photo to JPG, a video compressed for Slack, a PDF merged with another PDF, a screen recording's audio extracted to MP3.

If you're like most users, you used a free online converter. You uploaded the file to *cloudconverter.com* or *ilovepdf.com* or *tinypng.com* or one of a hundred near-identical sites. You waited. You downloaded the result. You moved on.

Almost none of those tools needed your file to leave your device. The convenience is real, but the privacy posture is structurally wrong, and [MediaKit](/apps/mediakit/) is the studio's argument that the entire category of conversion tools belongs on your Mac instead.

## What "convert online" actually does

When you use a free online converter, here is what the file does, in sequence:

1. Leaves your machine, encrypted in transit.
2. Lands on the operator's storage, sometimes encrypted at rest, sometimes not.
3. Is processed by their conversion pipeline. The processing typically takes seconds.
4. Is held in storage, often for hours, sometimes for days, depending on the operator's retention policy.
5. Is downloaded back to you.
6. *May or may not* be deleted from the operator's storage according to their stated policy, which you have no way to verify.

The first and last steps are the ones the user notices. The middle ones are the ones with privacy implications. The file you converted contained whatever it contained — a photograph of your kitchen, a screenshot of an email, a PDF of your medical records, a video of your child — and it now lives, briefly or not so briefly, on infrastructure you do not control.

I'm not suggesting any particular online converter is malicious. Most are run by small teams and most try to delete files promptly. I am suggesting that the *architecture* — files leaving your machine for processing tasks that don't require it to leave — is wrong by default, and the user should not have to trust the operator to be the right kind of careful.

## Apple Silicon changed the math

The honest historical reason cloud converters dominated is that local conversion was slow. In 2015, compressing a 4K video on a laptop took twenty minutes. Uploading it to a cloud service that compressed it in thirty seconds was just faster, even with the upload time.

Apple Silicon erased that gap. Modern Macs have hardware video encoders that compress at multiples of real-time speed. ProRes acceleration, HEIC encoding, AV1 decoding, all of it on-die. The local performance is now competitive with — and sometimes faster than — the cloud round-trip.

For images and PDFs, local processing was always faster. The cloud era for those was driven by *deployment* convenience, not performance. A web tool runs in any browser; a desktop tool needs to be installed. That's a real friction. But it's a friction worth paying for the privacy it preserves.

## What MediaKit specifically does

MediaKit is a Mac app with 133 local conversion tools, organised by media type:

- **Video**: compression for YouTube/Instagram/Slack, format conversion (MP4, HEVC, AV1, ProRes), resolution and bitrate adjustment, frame extraction, audio extraction.
- **Image**: HEIC↔JPG↔PNG↔WebP, bulk operations across folders, resize/crop/rotate, EXIF stripping, format-specific optimisation.
- **Audio**: format conversion, bitrate adjustment, channel mixing, silence trimming.
- **PDF**: merge, split, redact, sign, OCR, page reorder, compress.
- **Archive**: ZIP, TAR, GZIP — and crucially, **RAR v5 extraction natively on Apple Silicon**, which has been a long-standing pain point for users who get RAR archives in 2026 (more often than you'd think — academic and design workflows still use it heavily).

Every tool runs entirely on the Mac. No file leaves the device. No upload, no cloud round-trip, no operator retention policy to read.

The tools all support **Shortcuts integration**, which means they can be composed into automated workflows. *"Compress all videos in this Downloads folder, output to ~/Compressed, delete originals over 100MB."* That's a Shortcut, runs on a schedule, never touches the internet.

## The freemium decision

MediaKit's pricing was the most-debated decision internally before launch.

The shape it shipped with: **five tools free forever** (Video Compress, Image Compress, Image Resize, Audio Convert, PDF Compress) — which between them probably cover 70% of casual use cases — and a single Pro tier that unlocks the remaining 128 tools and batch processing across all of them. Pro also includes a free 3-day trial of *all* tools, so users can evaluate before deciding.

The argument for the freemium structure was that the user should have a non-trivial path to actually using the app for free, not a teaser. Five tools is enough that a casual user could go years without paying, and that's fine — the app's job is to be useful first.

The argument for putting the long tail behind Pro is that the long tail is what makes MediaKit valuable to the *power user*, and the power user is who funds the development of the long tail. The two-tier structure aligns the studio's incentives with the user's: power users pay because they get disproportionate value; casual users pay nothing because they get the basic value for free.

## The plain version

If you're reading this and you have a habit of using online converters, [MediaKit](/apps/mediakit/) is the studio's argument that the habit is unnecessary. The Mac in front of you can do the same processing locally, faster than you'd expect, without your files leaving the device.

The free tier covers the common cases. The Pro unlock covers everything else, including the obscure cases (RAR v5 on Apple Silicon, batch HEIC stripping, PDF redaction with verifiable removal) that most online services either don't support or charge a subscription for.

It's the last weekend of March. If you have a stack of media files you've been meaning to process, this is a calmer way to do it.
