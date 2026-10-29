---
layout: journal
slug: your-photos-shouldnt-ride-the-elevator
title: "Your photos shouldn't ride the elevator to a stranger's data centre"
seo:
  title: "Convert Photos Without Uploading Them to a Stranger"
  description: "Online image converters upload your photo to a server you don't control. MediaKit converts HEIC, JPG and PNG locally on your Mac or iPhone, with no upload."
  keywords:
    - "offline image converter"
    - "convert heic to jpg offline"
    - "image converter privacy"
    - "convert photos without uploading"
    - "local image converter mac"
    - "mediakit"
date: 2026-03-28
last_updated: 2026-10-29
lede: "Almost every online image converter you've used in the last decade uploaded your file to a server you don't control, processed it there, and gave you back a download. That is convenient, and it has real privacy costs. MediaKit is the studio's argument that more than 150 of those tools should run on your Mac or iPhone instead."
quick_answer: "Online image, video, audio, and PDF converters upload private files to operator infrastructure that can hold them well after the conversion is done. MediaKit is a Mac and iPhone app that runs more than 150 equivalent tools locally, including HEIC conversion, video compression, PDF redaction, and RAR5 extraction, and nothing is uploaded. Five tools stay free for good."
faq:
  - q: "Is it safe to upload files to free online converters like CloudConvert or iLovePDF?"
    a: "The file leaves your device, lands on operator storage that may or may not be encrypted at rest, sits in retention for hours or days, and you cannot verify deletion. Most operators are not malicious, but for private files like medical records, photos of children, or screenshots of email, sending the file away at all is the problem."
  - q: "Can my Mac convert HEIC, MP4, PDF, and RAR files locally?"
    a: "Yes. MediaKit runs more than 150 local tools on Mac and iPhone, including HEIC to JPG, video compression, PDF redaction, OCR, and RAR4 and RAR5 extraction. Converting a batch of files at once needs Pro. The hardware video encoders in Apple Silicon Macs make local conversion competitive with a cloud round trip."
  - q: "How many MediaKit tools are free without paying?"
    a: "Five tools stay free for good, one file at a time: Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress. For your first 3 days every other tool works too, one export per run. After that, the other tools and batch processing require Pro: a monthly or yearly plan, or a one-time lifetime purchase."
  - q: "Does MediaKit support Shortcuts automation?"
    a: "Yes, on Mac. MediaKit has six Shortcuts actions: Compress Video, Convert Image, Compress Image, Merge PDFs, Create ZIP, and Extract Text from Image. With Pro, Folder Automation also runs a saved Recipe on every file that lands in a folder you choose. Both run on the device and never touch the internet."
mentioned_apps:
  - mediakit
read_time: "5 min read"
excerpt: "MediaKit is a Mac and iPhone app with more than 150 local tools, among them video compression, HEIC to JPG, PDF tooling, and RAR5 extraction. This post argues for processing media locally, covers the Shortcuts and Folder Automation options on Mac, and explains the freemium structure (five tools free for good, the rest with Pro)."
---

Think of the last time this week you needed to convert a media file: a HEIC photo to JPG, a video compressed for Slack, two PDFs merged, a screen recording's audio pulled out into its own file.

Most people use a free online converter for that. You upload the file to *cloudconvert.com* or *ilovepdf.com* or *tinypng.com* or one of a hundred near-identical sites, wait, download the result, and move on. The same reflex reaches documents with your home address printed on them, [vet paperwork, for one](/journal/vet-paperwork-stays-on-your-phone/).

Almost none of those tools needed your file to leave your device. Uploading is convenient, but it sends private files somewhere they never needed to go, and [MediaKit](/apps/mediakit/) is the studio's argument that the whole category of conversion tools belongs on your Mac and iPhone.

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

Cloud converters dominated because local conversion used to be slow. Ten years ago, compressing a 4K video on a laptop could take longer than uploading it to a cloud service and waiting for the result.

Apple Silicon closed that gap. Modern Macs have hardware video encoders on the chip, with ProRes acceleration and HEVC encoding built in. Local performance is now competitive with the cloud round trip.

For images and PDFs, local processing was always faster. Those moved to the cloud because web tools are easier to ship: one runs in any browser, while a desktop tool has to be installed. That is real friction, and we think the privacy you keep is worth it.

## What MediaKit specifically does

MediaKit is a Mac and iPhone app with more than 150 local tools, organised by kind of file:

- **Video**: compression to a quality, a target size, or a bitrate, conversion with H.264 or HEVC and ProRes written to .mov, resolution changes, frame extraction, and audio extraction.
- **Image**: conversion between HEIC, JPG, PNG, and WebP (where your system can write it), batches with Pro, resize, crop, and rotate, and metadata stripping.
- **Audio**: conversion to M4A (AAC), WAV, AIFF, ALAC, or CAF, sample rate and channel changes, and silence removal.
- **PDF**: merge, split, redact, sign, OCR, page reorder, compress.
- **Archive**: create ZIP, TAR, GZIP, XZ, and BZIP2 archives, and extract those plus **RAR4 and RAR5**. RAR archives still turn up in 2026, and MediaKit opens them on the device.

Every tool runs entirely on your Mac or iPhone, so nothing is uploaded and there is no operator retention policy to read. For the most common video job, getting a clip under an email attachment limit, the limits and the bitrate arithmetic are in [a separate guide](/journal/compress-a-video-for-email/).

On Mac, six MediaKit actions appear in **Shortcuts** (Compress Video, Convert Image, Compress Image, Merge PDFs, Create ZIP, and Extract Text from Image), so you can chain them into your own workflows. With Pro, **Folder Automation** goes one step further: *"compress every video that lands in this folder"* becomes a saved Recipe that runs on its own, and it never touches the internet.

## The freemium decision

Pricing was the decision we argued about most before launch.

MediaKit shipped with **five tools that stay free for good** (Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress), which between them cover most casual use, and a single Pro tier that unlocks every other tool and batch processing across all of them. For the first 3 days *every* tool works, one export per run, so you can try everything before deciding.

We wanted a free path that people would actually use. Five tools is enough that a casual user could go years without paying, and that's fine; the app should be useful first.

The long tail of tools is what makes MediaKit worth paying for to a *power user*, and power users are the ones who fund building it. So power users pay because they get a lot out of the app, and casual users pay nothing for the basics.

## In short

If you habitually use online converters, [MediaKit](/apps/mediakit/) is our case that you don't need to. The Mac or iPhone in front of you can do the same processing locally, and your files stay on it.

The free tier covers the common cases. The Pro unlock covers everything else, including the less common jobs (RAR5 extraction, stripping metadata from a batch of photos, PDF redaction) that online services handle by taking your file away first.

It's the last weekend of March. If you have a stack of media files you've been meaning to process, this is a way to do it without uploading any of them.
