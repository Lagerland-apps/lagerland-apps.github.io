---
layout: app
slug: mediakit
name: "MediaKit"
tagline: "More than 150 on-device tools for video, audio, images, PDFs, and more."
quick_answer: "MediaKit is an iPhone and Mac app with more than 150 tools for compressing, converting, and editing video, audio, images, PDFs, archives, and ebooks. Every tool runs on your device, so your files are never uploaded, and there is no account to create. Five tools stay free for good (Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress), and your first 3 days unlock every other tool for single-file runs with no payment. Pro adds every tool and batch processing for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once, and one purchase covers iPhone and Mac."
category: utilities
status: live

app_store_url: "https://apps.apple.com/app/id6761451361"

price:
  model: freemium
price_lead: "Free"
price_tier: "Pro"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple offers the free trial on Monthly and Annual only to eligible Apple Accounts. The 3 days of full access after you install the app are separate and need no payment. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew."

plans:
  - name: "Free"
    price: "$0"
    summary: "Five tools that stay free for good, and every other tool for your first 3 days."
    features:
      - "Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress, one file at a time"
      - "Every other tool for 3 days after you install, one export per run, with no payment"
      - "Size estimates before you run, and saved space with a side-by-side compare after"
      - "Runs on your device, with no account"
  - name: "Pro · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Every tool and batch processing, billed monthly. Cancel anytime."
    features:
      - "More than 150 tools for video, audio, image, PDF, archive, and ebook files"
      - "Batch processing in the Queue, with unlimited exports"
      - "Recipes that save a chain of tools, and Make It Fit for a target size or platform"
      - "Auto Subtitle, Compare Takes, and the Smart Duplicate Finder"
      - "On Mac: Folder Automation and 3-second Try-It samples"
  - name: "Pro · Annual"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "The same Pro, billed once a year. ~{SAVE_YEARLY}% cheaper than paying monthly."
    features:
      - "Everything in Pro · Monthly"
      - "~{SAVE_YEARLY}% cheaper than monthly over a year"
      - "Cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All of Pro for one payment."
    features:
      - "Everything in Pro · Annual"
      - "One-time purchase, no renewal"
      - "One purchase covers iPhone and Mac"
      - "Restore Purchases sits in Settings under Your Plan"

icon: "/assets/icons/mediakit.png"
og_image: "/assets/og/mediakit.png"

seo:
  title: "MediaKit: Video Compressor & File Converter, iPhone & Mac"
  description: "Compress and convert video, audio, photos, PDFs, and archives on iPhone and Mac. More than 150 tools run on-device, and five stay free."
  keywords:
    - video compressor mac
    - video compressor iphone
    - compress video without uploading
    - convert heic to jpg mac
    - convert heic to jpg iphone
    - offline file converter
    - local file converter no upload
    - compress pdf on mac
    - pdf merge split redact mac
    - batch image converter mac
    - extract rar on mac
    - convert mobi to epub mac
    - ebu r128 loudness normalization app
    - on-device audio transcription
    - strip exif metadata
    - alternative to handbrake mac

hero:
  device: mac
  pre_headline: "For creators, podcasters, and anyone who'd rather not upload personal files to a converter website"
  headline: "More than 150 file tools for iPhone and Mac. None of them upload your files."
  secondary: "Drop in a video, photo, PDF, audio file, archive, or ebook and MediaKit suggests the tools that fit it. Every tool runs on your device."
  subheadline: "Before you press Run, the tool screen estimates the output size. After it, the result shows the space you saved next to a side-by-side compare. Five tools stay free for good, and your first 3 days unlock the rest with no payment."
  cta_label: "Download Free"
  alt: "MediaKit: more than 150 on-device tools for video, audio, images, PDFs, archives, and ebooks on iPhone and Mac"

who_for:
  - "You need a video or photo under a platform's size limit for Discord, Instagram, or YouTube"
  - "You shrink or convert everyday files (video, photos, PDFs, audio) and won't upload them to a website to do it"
  - "You record podcasts, music, or video and want quick clean-up, trimming, and loudness normalization to EBU R128"
  - "You read ebooks and want Kindle (MOBI or AZW3) or FictionBook files as EPUB, PDF, or text"
  - "You repeat the same steps and want them saved as a Recipe, run from Shortcuts, or triggered by a watched folder on your Mac"

who_not_for:
  - "You're on Windows, Linux, Android, or iPad: MediaKit runs on iPhone and Mac only"
  - "You need a video editor with a timeline. MediaKit is a set of single-purpose tools you can chain into Recipes"
  - "Your files are WebM video, DRM-protected Kindle books, or RAR archives you want to create"
  - "You convert one file a year and a free web tool is fine"

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
  - title: "Your files stay on your device"
    description: "Every tool runs on your iPhone or Mac with Apple's own frameworks. The app makes no network requests of its own, so it works offline. You never create an account, and the app has no analytics SDK."
  - title: "See the result before you keep it"
    description: "The tool screen estimates the output size and flags problems before you press Run. Each result shows what you won back, for example \"Saved 1.4 GB · 85% smaller\", next to a side-by-side compare. On Mac, ⌘T renders a 3-second sample of heavy tools first."
  - title: "Six kinds of file, one app"
    description: "More than 150 tools for video, audio, image, PDF, archive, and ebook files. Drop a file in and MediaKit suggests the tools that fit it, or search the grid by name."
  - title: "Five tools free for good"
    description: "Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress stay free after your first 3 days, one file at a time. Pro adds every other tool, batch processing, and unlimited exports."

features:
  - title: "Video"
    description: "Compress to a quality preset, a target size, or a bitrate. Compress never overshoots a target size; it stops with an error instead. Convert, trim, merge with a crossfade, crop, stabilize, color grade with sliders or a .cube LUT, burn in captions, and generate subtitles on the device with Auto Subtitle. MKV files open directly, ProRes is written to .mov, and portrait phone clips keep their orientation. WebM isn't supported."
  - title: "Audio"
    description: "Extract the audio from a video. Convert to M4A (AAC), WAV, AIFF, ALAC, or CAF from formats including MP3 and FLAC. Trim and merge on a waveform, normalize loudness to EBU R128 or a platform preset, reduce noise from a sample you pick, transcribe speech on the device, and make an iPhone ringtone."
  - title: "Photos and images"
    description: "Compress to a quality or a target file size, and convert to HEIC, JPG, PNG, TIFF, GIF, and WebP where your system can write it. Opens camera RAW in 10 formats (CR2, CR3, NEF, ARW, DNG, ORF, RW2, RAF, PEF, and SRW). Remove BG uses Apple Vision on the device; OCR, Smart Crop, Collage, GIF Maker, and Find Duplicates sit in the same grid. Animated GIFs keep every frame through most tools."
  - title: "PDFs"
    description: "Merge, split, reorder, sign, redact, encrypt, and compress with Screen, Ebook, Printer, or Prepress presets. OCR makes scans searchable in the language you choose. Watermarks, page numbers, and headers go on as overlays, so text stays searchable, vectors stay sharp, and bookmarks and links survive. Flatten and Redact rasterize on purpose."
  - title: "Archives and ebooks"
    description: "Create ZIP, TAR, TAR.GZ, GZIP, XZ, or BZIP2 archives, and extract those plus RAR4 and RAR5. You see what's inside before extracting, with limits against path traversal and zip bombs. The ebook Convert tool turns EPUB, FB2, and DRM-free MOBI or AZW3 into EPUB, PDF, plain text, and more, and EPUB Metadata edits the title, author, and cover."
  - title: "Recipes, Make It Fit, and automation"
    description: "With Pro, save any chain of tools as a Recipe and run it on new files, or let Make It Fit choose the steps to hit a target size or platform. On Mac, Folder Automation runs a Recipe on every file that lands in a watched folder, the menu bar reaches any tool, and six Shortcuts actions compress video, convert and compress images, merge PDFs, create a ZIP, and pull text from an image."
  - title: "Strip Metadata before you share"
    description: "Strip Metadata removes location, device, and author tags from videos, audio, photos, and PDFs. On iPhone, send files in from the share sheet and save results to Photos or keep them in the Library tab."

screenshots:
  - src: "/assets/screenshots/mediakit/1.webp"
    alt: "MediaKit on Mac: the tool grid with search and the Video, Audio, Image, PDF, Archive, and Ebook categories"
  - src: "/assets/screenshots/mediakit/2.webp"
    alt: "MediaKit after compressing a video: 55.3 MB before, 42.7 MB after, 22% smaller"
  - src: "/assets/screenshots/mediakit/3.webp"
    alt: "Trimming a MOV video in MediaKit with a timeline and start and end points"
  - src: "/assets/screenshots/mediakit/4.webp"
    alt: "Audio Convert in MediaKit with Podcast, Music, Voice memo, and Hi-fi presets and format, bitrate, sample rate, and channel options"
  - src: "/assets/screenshots/mediakit/5.webp"
    alt: "MediaKit PDF tools, including Compress, Merge, Split, Encrypt, and Watermark"
  - src: "/assets/screenshots/mediakit/6.webp"
    alt: "Compressing six images into a ZIP in MediaKit, with the option to run the batch in the background Queue"
  - src: "/assets/screenshots/mediakit/7.webp"
    alt: "Making a GIF from a video in MediaKit with frame rate, maximum width, and loop settings"
  - src: "/assets/screenshots/mediakit/8.webp"
    alt: "A GIF from an MP4 video in MediaKit at 640 px wide, with the estimated file size shown before export"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "Every tool runs on your iPhone or Mac, and your files are never uploaded"
    - "There is no account, and the app carries no analytics or advertising SDK"
    - "Transcribe and Auto Subtitle use on-device speech recognition"
    - "Recipes, presets, and your recent runs are stored on your device only"
    - "On Mac, the app is sandboxed and opens only the files you choose"

faq:
  - q: "What is MediaKit?"
    a: "MediaKit is an iPhone and Mac app with more than 150 tools for compressing, converting, and editing video, audio, images, PDFs, archives, and ebooks. You drop in a file, MediaKit suggests the tools that fit it, and every tool runs on your device. Five tools are free for good, and Pro unlocks the rest, with one purchase covering iPhone and Mac."
  - q: "Does MediaKit upload my files?"
    a: "No. Every tool runs on your iPhone or Mac, and the app makes no network requests of its own; only Apple's App Store handles purchases. There is no account, and the app has no analytics SDK. Transcription and auto subtitles use on-device speech recognition."
  - q: "How do I compress a video to fit a size limit?"
    a: "Drop the video into MediaKit and choose Compress. Set a target size and MediaKit works out the bitrate; it never goes over the target, and if the target can't be reached it stops with an error instead. The tool screen shows the estimated size before you run it, and the result shows the space you saved. Video Compress is one of the five free tools. With Pro, Make It Fit can also enhance a clip, turn it into 9:16, and bring it under 25 MB for social posts in one step."
  - q: "Which file formats does MediaKit support?"
    a: "Video: MKV opens directly, because MediaKit unpacks it itself (DTS, E-AC-3, and MP3 audio inside an MKV is dropped, with a notice); ProRes is written to .mov. Audio: reads formats including MP3 and FLAC and writes M4A (AAC), WAV, AIFF, ALAC, and CAF. Images: HEIC, JPG, PNG, TIFF, GIF, WebP (where your system can write it), BMP, and JPEG 2000, plus camera RAW, AVIF, PSD, and EXR as input. Ebooks: EPUB, FB2, MOBI and AZW3 (read-only), PDF, TXT, HTML, CBZ, and RTF. Archives: ZIP, TAR, TAR.GZ, GZIP, XZ, and BZIP2, plus RAR4 and RAR5 for extracting. WebM, RAR creation, encrypted RAR, and DRM-protected Kindle books are not supported."
  - q: "Is MediaKit free?"
    a: "Yes, to start. For your first 3 days every tool works, one export per run, with no payment. After that, five tools stay free for good, one file at a time: Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress. Pro unlocks every other tool, batch processing, and unlimited exports for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Does MediaKit work offline?"
    a: "Yes. Every tool runs on your device, so MediaKit works without an internet connection. The one exception is subtitle translation, which uses Apple's Translation language packs; macOS downloads them the first time (macOS 15 or later)."
  - q: "Which devices does MediaKit support?"
    a: "iPhone with iOS 17 or later, and Mac with macOS 14.6 (Sonoma) or later. One purchase covers both. There is no iPad version. Some extras are Mac-only: Folder Automation, the menu bar item, Open With from Finder, and Try-It samples with ⌘T. The share sheet extension, the Library tab, and saving to Photos are on iPhone."
  - q: "Can MediaKit be automated?"
    a: "Yes. With Pro, save any chain of tools as a Recipe and run it on new files. On Mac, Folder Automation runs a Recipe on every file that lands in a folder you choose, and six actions in the Shortcuts app cover Compress Video, Convert Image, Compress Image, Merge PDFs, Create ZIP, and Extract Text from Image."
  - q: "How is MediaKit different from online converters?"
    a: "Online converters upload your file to a server, process it there, and send it back. MediaKit does the same jobs on your iPhone or Mac, so a contract, a scan, or a family video never leaves the device, and there is no upload to wait for. It also covers six kinds of file in one app, shows the estimated size before you run a tool, and lets you compare the result with the original."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/mediakit/support/"

release:
  first_release: "2026-04-01"
  last_updated: "2026-04-13"
last_updated: 2026-10-29
---
MediaKit is an iPhone and Mac app with more than 150 tools for video, audio, image, PDF, archive, and ebook files, and every one of them runs on the device. Drop in a file and MediaKit suggests the tools that fit it. The tool screen estimates the output size before you press Run, and each result shows the space you saved next to a side-by-side compare. Five tools stay free for good: Video Compress, Image Compress, Image Resize, Audio Convert, and PDF Compress. Your first 3 days unlock every other tool for single-file runs with no payment, and Pro adds every tool, batch processing, Recipes, and Make It Fit, with one purchase covering iPhone and Mac. On Mac, Folder Automation, the menu bar, and six Shortcuts actions put the same tools into your routine. There is no account, and your files are never uploaded. Published by Lagerland Apps.
