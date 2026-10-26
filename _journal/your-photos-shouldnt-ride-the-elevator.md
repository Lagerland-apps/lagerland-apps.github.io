---
layout: journal
slug: your-photos-shouldnt-ride-the-elevator
title: "Your photos shouldn't ride the elevator to a stranger's data centre"
seo:
  title: "Convert Photos Without Uploading Them to a Stranger"
  description: "Online image converters upload your photo to a server you don't control. MediaKit converts HEIC, JPG and PNG locally on your Mac, with no upload."
  keywords:
    - "offline image converter"
    - "convert heic to jpg offline"
    - "image converter privacy"
    - "convert photos without uploading"
    - "local image converter mac"
    - "mediakit"
date: 2026-03-28
last_updated: 2026-10-26
lede: "Almost every online image converter you've used in the last decade uploaded your file to a server you don't control, processed it there, and gave you back a download. That is convenient, and it has real privacy costs. MediaKit is the studio's argument that 133 of those tools should run on your Mac instead."
quick_answer: "Online image, video, audio, and PDF converters upload private files to operator infrastructure that holds them well after the conversion is done. MediaKit is a Mac app that runs 133 equivalent tools locally, including HEIC bulk conversion, video compression, PDF redaction, and RAR v5 extraction on Apple Silicon, with full Shortcuts support. Five tools are permanently free."
faq:
  - q: "Is it safe to upload files to free online converters like CloudConvert or iLovePDF?"
    a: "The file leaves your device, lands on operator storage that may or may not be encrypted at rest, sits in retention for hours or days, and you cannot verify deletion. Most operators are not malicious, but for private files like medical records, photos of children, or screenshots of email, sending the file away at all is the problem."
  - q: "Can my Mac convert HEIC, MP4, PDF, and RAR files locally?"
    a: "Yes. MediaKit runs 133 local conversion tools on Apple Silicon, including HEIC to JPG bulk, video compression, PDF redaction, OCR, and RAR v5 extraction. Apple Silicon's hardware encoders make local conversion competitive with a cloud round trip, and often faster."
  - q: "How many MediaKit tools are free without paying?"
    a: "Five tools are permanently free: Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress. They cover roughly 70% of casual cases. The remaining 128 tools and batch processing are unlocked during a 3-day trial, then require a one-time Pro purchase. There is no subscription."
  - q: "Does MediaKit support Shortcuts automation?"
    a: "Yes. Every tool supports Shortcuts integration, so workflows like 'compress all videos in Downloads, output to ~/Compressed, delete originals over 100MB' can run on a schedule entirely on-device. The workflow never touches the internet."
mentioned_apps:
  - mediakit
read_time: "5 min read"
excerpt: "MediaKit is a Mac app with 133 local conversion tools, among them video compression, HEIC to JPG bulk, PDF tooling, and RAR v5 extraction on Apple Silicon. This post argues for processing media locally, explains the Shortcuts integration, and explains the freemium structure (5 tools permanently free, 128 behind Pro)."
---

Think of the last time this week you needed to convert a media file: a HEIC photo to JPG, a video compressed for Slack, two PDFs merged, a screen recording's audio extracted to MP3.

Most people use a free online converter for that. You upload the file to *cloudconverter.com* or *ilovepdf.com* or *tinypng.com* or one of a hundred near-identical sites, wait, download the result, and move on. The same reflex reaches documents with your home address printed on them, [vet paperwork, for one](/journal/vet-paperwork-stays-on-your-phone/).

Almost none of those tools needed your file to leave your device. Uploading is convenient, but it sends private files somewhere they never needed to go, and [MediaKit](/apps/mediakit/) is the studio's argument that the whole category of conversion tools belongs on your Mac.

## What does "convert online" actually do to your file?

When you use a free online converter, the file goes through these steps:

1. It leaves your machine, encrypted in transit.
2. It lands on the operator's storage, sometimes encrypted at rest, sometimes not.
3. Their conversion pipeline processes it, which typically takes seconds.
4. It is held in storage, often for hours, sometimes for days, depending on the operator's retention policy.
5. You download it.
6. It *may or may not* be deleted from the operator's storage according to their stated policy, which you have no way to verify.

You notice the first and last steps. The privacy questions sit in the middle ones. The file you converted contained whatever it contained (a photograph of your kitchen, a screenshot of an email, a PDF of your medical records, a video of your child), and it now lives, briefly or not so briefly, on infrastructure you do not control.

Most online converters are run by small teams, and most try to delete files promptly. The problem is the design: files leave your machine for processing that doesn't require it, and you have to trust the operator to be careful in the right way.

## Apple Silicon changed the math

Cloud converters dominated because local conversion used to be slow. In 2015, compressing a 4K video on a laptop took twenty minutes. Uploading it to a cloud service that compressed it in thirty seconds was simply faster, even counting the upload.

Apple Silicon closed that gap. Modern Macs have hardware video encoders that compress at multiples of real-time speed, with ProRes acceleration, HEIC encoding, and AV1 decoding all on the chip. Local performance is now competitive with the cloud round trip, and sometimes faster.

For images and PDFs, local processing was always faster. Those moved to the cloud because web tools are easier to ship: one runs in any browser, while a desktop tool has to be installed. That is real friction, and we think the privacy you keep is worth it.

## What MediaKit specifically does

MediaKit is a Mac app with 133 local conversion tools, organised by media type:

- **Video**: compression for YouTube/Instagram/Slack, format conversion (MP4, HEVC, AV1, ProRes), resolution and bitrate adjustment, frame extraction, audio extraction.
- **Image**: HEIC↔JPG↔PNG↔WebP, bulk operations across folders, resize/crop/rotate, EXIF stripping, format-specific optimisation.
- **Audio**: format conversion, bitrate adjustment, channel mixing, silence trimming.
- **PDF**: merge, split, redact, sign, OCR, page reorder, compress.
- **Archive**: ZIP, TAR, GZIP, and **RAR v5 extraction natively on Apple Silicon**. That has long been a pain point for people who still get RAR archives in 2026, which happens more often than you'd think, since academic and design workflows use the format heavily.

Every tool runs entirely on the Mac, so nothing is uploaded and there is no operator retention policy to read. For the most common video job, getting a clip under an email attachment limit, the limits and the bitrate arithmetic are in [a separate guide](/journal/compress-a-video-for-email/).

All the tools support **Shortcuts integration**, so you can chain them into automated workflows. *"Compress all videos in this Downloads folder, output to ~/Compressed, delete originals over 100MB"* is one Shortcut; it runs on a schedule and never touches the internet.

## The freemium decision

Pricing was the decision we argued about most before launch.

MediaKit shipped with **five permanently free tools** (Video Compress, Image Compress, Image Resize, Audio Convert, PDF Compress), which between them probably cover 70% of casual use cases, and a single Pro tier that unlocks the remaining 128 tools and batch processing across all of them. There is also a free 3-day trial of *all* tools, so you can try everything before deciding.

We wanted a free path that people would actually use. Five tools is enough that a casual user could go years without paying, and that's fine; the app should be useful first.

The long tail of tools is what makes MediaKit worth paying for to a *power user*, and power users are the ones who fund building it. So power users pay because they get a lot out of the app, and casual users pay nothing for the basics.

## In short

If you habitually use online converters, [MediaKit](/apps/mediakit/) is our case that you don't need to. The Mac in front of you can do the same processing locally, faster than you'd expect, and your files stay on it.

The free tier covers the common cases. The Pro unlock covers everything else, including the obscure jobs (RAR v5 on Apple Silicon, batch HEIC stripping, PDF redaction with verifiable removal) that most online services either don't support or charge a subscription for.

It's the last weekend of March. If you have a stack of media files you've been meaning to process, this is a way to do it without uploading any of them.
