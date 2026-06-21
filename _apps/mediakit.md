---
layout: app
slug: mediakit
name: "MediaKit"
tagline: "Every media tool. One app for iPhone & Mac."
quick_answer: "MediaKit is a native iPhone and Mac app with 152 local tools for compressing, converting, and editing video, audio, images, PDFs, and archives. Drop any file and it picks the right tool — every operation runs on-device via Apple frameworks, never uploaded. Free 3-day trial; five core tools stay free forever. Pro from $3.99/month, $22.99/year, or $39.99 lifetime. No tracking, no account."
category: utilities
platforms: ["iOS", "macOS"]
status: live

app_store_url: "https://apps.apple.com/app/id6761451361"

price:
  model: freemium
  value: "Free trial — Pro from $3.99/mo, $22.99/yr, or $39.99 lifetime"
schema_price: "0"
schema_high_price: "39.99"
schema_offer_count: "4"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. The lifetime tier is a one-time purchase — no auto-renew."

plans:
  - name: "Free trial"
    price: "$0"
    summary: "All 152 tools unlocked for 3 days. After that, five core tools stay free forever."
    features:
      - "Full access to all 152 tools for 3 days"
      - "Five tools stay free forever: Video Compress, Image Compress, Image Resize, Audio Convert, PDF Compress"
      - "Everything runs on-device — no upload, no account"
  - name: "Pro · Monthly"
    price: "$3.99/mo"
    summary: "Full Pro, billed monthly. Cancel anytime."
    features:
      - "All 152 tools across video, audio, image, PDF, archive"
      - "Batch processing"
      - "All 21 export presets (YouTube, Instagram, Discord, broadcast LUFS)"
      - "All six Shortcuts actions"
      - "Menu bar access to every tool"
  - name: "Pro · Annual"
    price: "$22.99/yr"
    summary: "Same Pro features, billed once a year. ~52% cheaper than paying monthly."
    features:
      - "Everything in Pro · Monthly"
      - "~52% cheaper than monthly over a year"
      - "Cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "$39.99 once"
    summary: "All Pro features. Roughly 10 months of monthly Pro — then yours."
    features:
      - "Everything in Pro · Annual"
      - "One-time purchase, no renewal"
      - "Future Pro features included"
      - "Universal Purchase — works on iPhone and every Mac signed in with the same Apple ID"
    highlight_label: "Best long-term value"

icon: "/assets/icons/mediakit.png"
og_image: "/assets/og/mediakit.png"

seo:
  title: "MediaKit — 152 Local Media Tools for iPhone & Mac"
  description: "Compress, convert, and edit video, audio, images, PDFs, and archives on your iPhone or Mac. 152 native tools. 100% on-device. No uploads. Free to start."
  keywords:
    - mac media tools
    - video compressor mac
    - convert heic to jpg mac
    - offline pdf editor mac
    - batch image converter mac
    - compress mp4 without uploading
    - extract rar v5 on mac
    - on-device audio transcription mac
    - video compressor iphone
    - convert heic to jpg iphone
    - offline file converter ios
    - ebu r128 loudness normalization app
    - privacy-first file converter for mac
    - all-in-one media converter apple silicon
    - alternative to handbrake mac
    - local file converter no upload
    - pdf merge split redact mac
    - strip exif metadata mac

hero:
  headline: "Every media tool. One app for iPhone & Mac."
  subheadline: "152 local tools for video, audio, image, PDF, and archives. Drop a file — MediaKit picks the right one. Nothing uploaded, ever."
  cta_label: "Download Free"
  alt: "MediaKit — drag-and-drop file conversion across 152 native tools on iPhone and Mac"

who_for:
  - "You convert video, audio, images, PDFs, or archives regularly on iPhone or Mac"
  - "You refuse to upload files to cloud conversion tools (CloudConvert, Zamzar) for privacy reasons"
  - "You want one native iPhone & Mac app instead of five single-purpose utilities"
  - "You care about offline-first, sandboxed file processing on iPhone and Apple Silicon Macs"
  - "You automate via Shortcuts and want conversion actions you can chain"

who_not_for:
  - "You're on Windows or Linux"
  - "You convert one file a year and a free web tool is fine"
  - "You need professional video editing (use Final Cut or Resolve instead)"

alternatives_to:
  - "Handbrake"
  - "Permute"
  - "CloudConvert"
  - "Convertio"
  - "Adapter"
  - "Wondershare UniConverter"
  - "HitPaw Video Converter"
  - "iMazing HEIC Converter"
  - "XnConvert"
  - "ImageOptim"
  - "Keka"
  - "iZip"
  - "Compress Videos & Resize Video"
  - "Image Size"
  - "PDF Expert"
  - "Documents by Readdle"

value_points:
  - title: "Drop. Done."
    description: "Drag any file in. MediaKit recognizes the format and opens the right tool instantly. No menus to hunt through."
  - title: "Every format. One app."
    description: "Video, audio, image, PDF, archive, ebook — 152 tools behind a single interface. Replace a dozen utilities with one."
  - title: "Never leaves your device"
    description: "Every operation runs on-device via AVFoundation, CoreImage, PDFKit, Vision, and Speech. No servers. No account. Works offline."
  - title: "Five tools free forever"
    description: "Full access for 3 days. After that, five core tools stay free forever. Go Pro for the remaining 147 and batch processing."

features:
  - title: "Broadcast-grade video"
    description: "Compress, convert, trim, crop, merge, stabilize, and color-adjust MP4, MOV, MKV, AVI, WebM, and M4V. Frame-accurate output. ProRes and HEVC supported. 21 presets for YouTube, Instagram, Discord, and broadcast delivery."
  - title: "Studio-quality audio"
    description: "Extract audio from any video. Convert MP3, M4A, WAV, FLAC, AIFF, AAC, ALAC. Normalize to EBU R128. Reduce noise with machine learning. Transcribe speech on-device via Apple's Speech framework."
  - title: "Pixel-perfect images"
    description: "Compress and convert PNG, JPG, HEIC, WebP, TIFF, GIF, AVIF, and RAW. AI upscale. Remove backgrounds with Apple Vision. OCR text. Strip EXIF metadata before you share."
  - title: "PDFs without compromise"
    description: "Merge, split, compress, encrypt, redact, sign, and OCR. Add watermarks, page numbers, headers, and footers. Compare two PDFs side by side. Vector-preserving edits — no quality loss."
  - title: "Archives that just work"
    description: "Create ZIP, TAR, TAR.GZ, GZIP, XZ, and BZIP2. Extract RAR v4 and v5. AES-256 encryption via Apple's AppleArchive framework. Path-traversal safe. Batch extraction."
  - title: "Shortcuts and menu bar"
    description: "Six built-in Shortcuts actions — compress video, convert images, merge PDFs, create ZIPs, extract text, run OCR. Access every tool from the menu bar without opening the main window."

screenshots:
  - "/assets/screenshots/mediakit/1.png"
  - "/assets/screenshots/mediakit/2.png"
  - "/assets/screenshots/mediakit/3.png"
  - "/assets/screenshots/mediakit/4.png"
  - "/assets/screenshots/mediakit/5.png"
  - "/assets/screenshots/mediakit/6.png"
  - "/assets/screenshots/mediakit/7.png"
  - "/assets/screenshots/mediakit/8.png"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "Every operation runs 100% on your device"
    - "Uses native Apple frameworks — AVFoundation, CoreImage, PDFKit, Vision, Speech, Compression"
    - "No servers, no uploads, no analytics, no account"
    - "Sandboxed with hardened runtime. Works offline."
    - "Your files never leave your machine"

faq:
  - q: "What is MediaKit?"
    a: "A native iPhone and Mac app with 152 tools for compressing, converting, and editing video, audio, images, PDFs, archives, and ebooks — all running locally on your device. It's a Universal Purchase: buy once, use on both iPhone and Mac."
  - q: "Does MediaKit upload my files?"
    a: "No. Every operation runs 100% on-device using Apple's native frameworks — AVFoundation, CoreImage, PDFKit, Vision, and Speech. Files never leave your device. No servers, no analytics, no account required."
  - q: "Which file formats does MediaKit support?"
    a: "Video: MP4, MOV, MKV, AVI, WebM, M4V, ProRes, HEVC. Audio: MP3, M4A, WAV, FLAC, AIFF, AAC, ALAC. Image: PNG, JPG, HEIC, WebP, TIFF, GIF, AVIF, RAW. Documents: PDF, EPUB, CBZ, HTML, RTF. Archives: ZIP, TAR, GZIP, XZ, BZIP2, and RAR v4 and v5."
  - q: "Is MediaKit free?"
    a: "Yes, to start. You get full access to all 152 tools for 3 days. After the trial, five tools stay free forever: Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress. Pro unlocks the remaining 147 tools and batch processing — $3.99/month, $22.99/year, or $39.99 lifetime. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does MediaKit work offline?"
    a: "Yes. Because everything runs on-device, MediaKit works without an internet connection."
  - q: "Which devices does MediaKit support?"
    a: "iPhone running iOS 17 or later, and any Mac running macOS 14 or later — one Universal Purchase covers both. On Mac it is optimized for Apple Silicon (M1, M2, M3, M4). Some AI features require a newer OS version and degrade gracefully on earlier ones."
  - q: "Can MediaKit be automated?"
    a: "Yes. Six built-in Shortcuts actions cover video compression, image conversion, PDF merging, ZIP creation, text extraction, and OCR — so you can build MediaKit into any Shortcuts workflow."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/mediakit/support/"

release:
  first_release: "2026-04-01"
  last_updated: "2026-04-13"
---
MediaKit is a native iPhone and Mac app that consolidates 152 local tools for video, audio, image, PDF, archive, and ebook work into a single drag-and-drop interface. It's a Universal Purchase — buy once, use on both iPhone and Mac. Every operation runs on-device using Apple's AVFoundation, CoreImage, PDFKit, Vision, and Speech frameworks — no uploads, no servers, no account. Drop any file and MediaKit picks the right tool instantly. Includes 21 built-in presets for YouTube, Instagram, Discord, Podcast, Email, iPhone export, and broadcast LUFS, plus six Shortcuts actions for automation and Mac menu bar access to every tool. Free 3-day trial with full access. Five core tools — Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress — stay free forever. Pro unlocks the remaining 147 tools and batch processing. Published by Lagerland Apps.
