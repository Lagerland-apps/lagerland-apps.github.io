---
layout: app
slug: mediakit
name: "MediaKit"
tagline: "Every media tool. One app for iPhone & Mac."
quick_answer: "MediaKit is a native iPhone and Mac app with 152 local tools for compressing, converting, and editing video, audio, images, PDFs, and archives. Drop in a file and it opens the matching tool. Every operation runs on-device through Apple frameworks, so nothing is uploaded. There is a free 3-day trial, and five core tools stay free after it. Pro costs {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} lifetime. The app has no tracking and needs no account."
category: utilities
status: live

app_store_url: "https://apps.apple.com/app/id6761451361"

price:
  model: freemium
price_lead: "Free trial"
price_tier: "Pro"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. The lifetime tier is a one-time purchase and does not auto-renew."

plans:
  - name: "Free trial"
    price: "$0"
    summary: "All 152 tools unlocked for 3 days. After that, five core tools stay free."
    features:
      - "Full access to all 152 tools for 3 days"
      - "Five tools stay free after the trial: Video Compress, Image Compress, Image Resize, Audio Convert, PDF Compress"
      - "Everything runs on-device, without uploads or an account"
  - name: "Pro · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Full Pro, billed monthly. Cancel anytime."
    features:
      - "All 152 tools across video, audio, image, PDF, archive"
      - "Batch processing"
      - "All 21 export presets (YouTube, Instagram, Discord, broadcast LUFS)"
      - "All six Shortcuts actions"
      - "Menu bar access to every tool"
  - name: "Pro · Annual"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "Same Pro features, billed once a year. ~{SAVE_YEARLY}% cheaper than paying monthly."
    features:
      - "Everything in Pro · Monthly"
      - "~{SAVE_YEARLY}% cheaper than monthly over a year"
      - "Cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All Pro features for the price of roughly {LIFETIME_MONTHS} months of monthly Pro."
    features:
      - "Everything in Pro · Annual"
      - "One-time purchase, no renewal"
      - "Future Pro features included"
      - "Universal Purchase: works on iPhone and every Mac signed in with the same Apple ID"
    highlight_label: "Best long-term value"

icon: "/assets/icons/mediakit.png"
og_image: "/assets/og/mediakit.png"

seo:
  title: "MediaKit: 152 Local Media Tools for iPhone & Mac"
  description: "Compress, convert, and edit video, audio, images, PDFs, and archives on iPhone or Mac with 152 native tools that run fully on-device. Free to start."
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
  device: mac
  headline: "Every media tool. One app for iPhone & Mac."
  subheadline: "152 local tools for video, audio, image, PDF, and archives. Drop a file in and MediaKit opens the right one. Nothing gets uploaded."
  cta_label: "Download Free"
  alt: "MediaKit: drag-and-drop file conversion across 152 native tools on iPhone and Mac"

who_for:
  - "You convert video, audio, images, PDFs, or archives regularly on iPhone or Mac"
  - "You refuse to upload files to cloud conversion tools (CloudConvert, Zamzar) for privacy reasons"
  - "You want one native iPhone & Mac app instead of five single-purpose utilities"
  - "You want sandboxed file processing that works offline on iPhone and Apple Silicon Macs"
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
  - title: "Drop a file in"
    description: "Drag any file onto MediaKit. It recognizes the format and opens the matching tool, so you skip the menus."
  - title: "Six file types in one app"
    description: "Video, audio, image, PDF, archive, and ebook: 152 tools behind a single interface, in place of a dozen separate utilities."
  - title: "Never leaves your device"
    description: "Every operation runs on-device through AVFoundation, CoreImage, PDFKit, Vision, and Speech. There are no servers or accounts, and it works offline."
  - title: "Five tools stay free"
    description: "Full access for 3 days. After that, five core tools stay free. Pro adds the remaining 147 and batch processing."

features:
  - title: "Video"
    description: "Compress, convert, trim, crop, merge, stabilize, and color-adjust MP4, MOV, MKV, AVI, WebM, and M4V with frame-accurate output. ProRes and HEVC are supported. 21 presets for YouTube, Instagram, Discord, and broadcast delivery."
  - title: "Audio"
    description: "Extract audio from any video. Convert MP3, M4A, WAV, FLAC, AIFF, AAC, ALAC. Normalize to EBU R128. Reduce noise with machine learning. Transcribe speech on-device with Apple's Speech framework."
  - title: "Images"
    description: "Compress and convert PNG, JPG, HEIC, WebP, TIFF, GIF, AVIF, and RAW. Upscale with AI. Remove backgrounds with Apple Vision. OCR text. Strip EXIF metadata before you share."
  - title: "PDFs"
    description: "Merge, split, compress, encrypt, redact, sign, and OCR. Add watermarks, page numbers, headers, and footers. Compare two PDFs side by side. Edits keep vectors intact, so quality does not drop."
  - title: "Archives"
    description: "Create ZIP, TAR, TAR.GZ, GZIP, XZ, and BZIP2. Extract RAR v4 and v5. AES-256 encryption through Apple's AppleArchive framework. Path-traversal safe. Batch extraction."
  - title: "Shortcuts and menu bar"
    description: "Six built-in Shortcuts actions: compress video, convert images, merge PDFs, create ZIPs, extract text, and run OCR. Access every tool from the menu bar without opening the main window."

screenshots:
  - "/assets/screenshots/mediakit/1.webp"
  - "/assets/screenshots/mediakit/2.webp"
  - "/assets/screenshots/mediakit/3.webp"
  - "/assets/screenshots/mediakit/4.webp"
  - "/assets/screenshots/mediakit/5.webp"
  - "/assets/screenshots/mediakit/6.webp"
  - "/assets/screenshots/mediakit/7.webp"
  - "/assets/screenshots/mediakit/8.webp"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "Every operation runs 100% on your device"
    - "Uses native Apple frameworks: AVFoundation, CoreImage, PDFKit, Vision, Speech, Compression"
    - "No servers, no uploads, no analytics, no account"
    - "Sandboxed with hardened runtime. Works offline."
    - "Your files never leave your machine"

faq:
  - q: "What is MediaKit?"
    a: "A native iPhone and Mac app with 152 tools for compressing, converting, and editing video, audio, images, PDFs, archives, and ebooks, all running locally on your device. It's a Universal Purchase: buy once, use on both iPhone and Mac."
  - q: "Does MediaKit upload my files?"
    a: "No. Every operation runs 100% on-device using Apple's native frameworks (AVFoundation, CoreImage, PDFKit, Vision, and Speech), so files never leave your device. There are no servers or analytics, and you don't need an account."
  - q: "Which file formats does MediaKit support?"
    a: "Video: MP4, MOV, MKV, AVI, WebM, M4V, ProRes, HEVC. Audio: MP3, M4A, WAV, FLAC, AIFF, AAC, ALAC. Image: PNG, JPG, HEIC, WebP, TIFF, GIF, AVIF, RAW. Documents: PDF, EPUB, CBZ, HTML, RTF. Archives: ZIP, TAR, GZIP, XZ, BZIP2, and RAR v4 and v5."
  - q: "Is MediaKit free?"
    a: "Yes, to start. You get full access to all 152 tools for 3 days. After the trial, five tools stay free: Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress. Pro unlocks the remaining 147 tools and batch processing for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} lifetime. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does MediaKit work offline?"
    a: "Yes. Because everything runs on-device, MediaKit works without an internet connection."
  - q: "Which devices does MediaKit support?"
    a: "iPhone running iOS 17 or later, and any Mac running macOS 14 or later. One Universal Purchase covers both. On Mac it is optimized for Apple Silicon (M1, M2, M3, M4). Some AI features require a newer OS version and degrade gracefully on earlier ones."
  - q: "Can MediaKit be automated?"
    a: "Yes. Six built-in Shortcuts actions cover video compression, image conversion, PDF merging, ZIP creation, text extraction, and OCR, so you can build MediaKit into any Shortcuts workflow."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/mediakit/support/"

release:
  first_release: "2026-04-01"
  last_updated: "2026-04-13"
last_updated: 2026-10-26
---
MediaKit is a native iPhone and Mac app that puts 152 local tools for video, audio, image, PDF, archive, and ebook work into one drag-and-drop interface. It's a Universal Purchase, so one purchase covers iPhone and Mac. Every operation runs on-device using Apple's AVFoundation, CoreImage, PDFKit, Vision, and Speech frameworks, with no uploads, servers, or account. Drop in a file and MediaKit opens the matching tool. It includes 21 built-in presets for YouTube, Instagram, Discord, Podcast, Email, iPhone export, and broadcast LUFS, plus six Shortcuts actions for automation and Mac menu bar access to every tool. The free 3-day trial gives full access. After it, five core tools stay free: Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress. Pro unlocks the remaining 147 tools and batch processing. Published by Lagerland Apps.
