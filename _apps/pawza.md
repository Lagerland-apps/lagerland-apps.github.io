---
layout: app
slug: pawza
name: "Pawza"
tagline: "Your pet's health, doses, and daily care in one calm place."
quick_answer: "Pawza is a pet health record app for iPhone and iPad that keeps vet papers, medications, vaccinations, weight, symptoms, and daily care in one place for dogs, cats, rabbits, birds, reptiles, horses, and other pets. Document scanning and records import run on your device, there is no account, and optional sync goes through your own iCloud. It is free for one pet, with 10 document scans, 50 photos, and your first records import. Pawza Pro adds unlimited pets, Apple Intelligence auto-fill (iOS 26 or later on an eligible device), the Vet Visit PDF, and weight alerts for {P_MONTHLY}/month or {P_YEARLY}/year, each starting with a {TRIAL}, or {P_LIFETIME} once."
category: health
status: live
show_body: true

app_store_url: "https://apps.apple.com/app/id6773507068"

price:
  model: freemium
price_tier: "Pawza Pro"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple handles refunds through the standard App Store refund flow. Monthly and Yearly start with a {TRIAL} for eligible accounts and can be cancelled in Settings before they renew. Lifetime is a one-time purchase and does not auto-renew. Pawza is one universal app for iPhone and iPad."

plans:
  - name: "Free"
    price: "$0"
    summary: "One pet, with no time limit and no account."
    features:
      - "Care log, medications, vaccinations, symptoms, and reminders"
      - "Weight chart, records with attachments, and the Since last vet visit card"
      - "All 8 widgets, the Control Center button, and Siri"
      - "Your first records import, 10 document scans, and 50 photos"
      - "iCloud sync and import from a file"
      - "Emergency Card and Lost Pet Kit"
  - name: "Pro · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Full Pawza Pro, billed monthly. Starts with a {TRIAL}."
    features:
      - "Unlimited pets"
      - "Unlimited scans, with Apple Intelligence auto-fill on iOS 26 or later (eligible devices)"
      - "Unlimited records imports and photos"
      - "Photo auto-sorting and Compare Photos"
      - "Vet Visit PDF and Sitter Pack"
      - "Weight alerts and full data export (JSON, CSV, or PDF)"
      - "Family Sharing included"
  - name: "Pro · Yearly"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "Same Pro features, billed once a year. Starts with a {TRIAL}."
    highlight: true
    features:
      - "Everything in Pro · Monthly"
      - "About {SAVE_YEARLY}% less than paying monthly for a year"
      - "Cancel anytime in Settings"
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All Pro features for one payment."
    features:
      - "Everything in Pro · Yearly"
      - "One-time purchase, no renewal"
      - "Family Sharing included"
    highlight_label: "Pay once"

icon: "/assets/icons/pawza.png"
og_image: "/assets/og/pawza.png"

seo:
  title: "Pet Health Record App for iPhone & iPad | Pawza"
  description: "Pet health record app for iPhone and iPad. Scan vet papers on your device, log care from widgets, share a vet PDF. Free for one pet, no account."
  keywords:
    - pet health record app iphone
    - pet vaccination tracker
    - dog vaccine record app
    - cat health record app
    - pet medication reminder app
    - scan vet records app
    - pet weight tracker app
    - pet vet visit pdf export

hero:
  pre_headline: "For dogs, cats, rabbits, birds, reptiles, horses, and the pets in between"
  headline: "When the vet asks when it started, you'll know."
  secondary: "Vet papers, doses, weight, symptoms, and daily care for every pet, in one record on your iPhone and iPad."
  subheadline: "Scan a vet document and Pawza reads it on your device. With Pawza Pro on iOS 26 and an eligible device, Apple Intelligence fills in the record for you to check. Log a meal or a walk from a widget, Control Center, or Siri. There is no account, and sync runs through your own iCloud."
  cta_label: "Download Pawza on the App Store"
  alt: "Pawza dashboard on iPhone showing a pet profile with upcoming vaccination reminders, recent weight, and quick actions to scan a document or add a record"

who_for:
  - "You have a drawer of vet paperwork and want it as one searchable record"
  - "Your pet takes daily medication and you have asked yourself whether today's dose was given"
  - "You keep several pets, foster, or care for a senior pet with more than one vet"
  - "You have had your pet for years and want the old records in without typing them"
  - "You'd rather your pet's records stayed on your devices than in an account on someone else's server"
  - "You leave your pet with a sitter now and then, or want a plan ready if they ever slip out"

who_not_for:
  - "You want a social network for pets, public profiles, or a feed"
  - "You want to message a vet or book appointments inside the app"
  - "You need a GPS tracker; the Lost Pet Kit is a poster, a QR collar tag, and a checklist"
  - "Several people need to edit the same pet's records; sync covers your own devices only"
  - "You use Android, a Mac, or an Apple Watch; Pawza runs on iPhone and iPad"

alternatives_to:
  - "11pets"
  - "PetDesk"
  - "Pawprint"
  - "Medika"
  - "PetNoter"
  - "VetKeep"

how_it_works:
  intro: "Scanning is where Pawza saves the most typing. Here is what happens between photographing a vet document and a saved record, and where each step runs."
  steps:
    - title: "You snap the document"
      detail: "Scan a vaccination certificate, lab result, prescription, invoice, or discharge notes with the camera, or pick up to five photos of it. If a page is too blurry to read, Pawza asks for a retake."
    - title: "The text is read on your device"
      detail: "Apple Vision reads the text on your iPhone or iPad, and nothing is uploaded. This works on every device Pawza supports. The free plan includes 10 scans; Pro has no limit."
    - title: "Apple Intelligence fills in the fields (Pro)"
      detail: "With Pawza Pro on iOS 26 or later and a device that supports Apple Intelligence, the on-device model picks out the document type, visit date, vet and clinic, vaccinations, medications, diagnoses, weight, next-due date, and a short summary. A course written as \"for 10 days\" gets an end date. Without Apple Intelligence, the review form opens with the recognized text and you fill in the fields."
    - title: "You check everything before it is saved"
      detail: "Every scan ends on an editable Review screen with the original text beside it. Extraction can be wrong, so nothing goes into the record until you confirm it."
    - title: "Reminders come from the document"
      detail: "Pawza can turn a booster date or a \"next visit due\" line into a reminder. Reminders can be one-time or repeat daily, weekly, monthly, or yearly, and you can mark one done or snooze it for an hour from the notification."
    - title: "The history goes to the vet as a PDF (Pro)"
      detail: "Before an appointment, the Vet Visit PDF gathers what changed since the last visit, current medications and diet, vaccination status, recent weight, symptoms, and the last 7 days of care, plus your own \"What to discuss\" notes. Pick 30 days, 90 days, a year, or all time, and share it as a PDF or an image."

value_points:
  - title: "Ready for the vet's questions"
    description: "The Since last vet visit card counts what changed since the last appointment: weight, symptoms logged, medications started and finished, vaccines given, and diet changes. With Pro, the Vet Visit PDF puts it on one page with the questions you meant to ask."
  - title: "Paperwork in without the typing"
    description: "Scan a single document, or import one records PDF with years of visits. Pawza splits it into visits by date, you check each one, and you save once. Your first import is free and never uses up a scan."
  - title: "Care logged from where you already are"
    description: "Log food, water, a walk, a bathroom break, or mood in one tap from the dashboard, eight free widgets, a Control Center button (iOS 18), or Siri. Tap Given on a dose notification and the dose is recorded; tap Fed and the meal is logged."
  - title: "Your records stay on your devices"
    description: "Pawza runs without an account, ads, or analytics. Your records live on your device and, if you turn on iCloud, sync through your own private iCloud. Photos are stripped of location and EXIF data when you import them."

features:
  - title: "Scan a vet document"
    description: "Photograph a certificate, lab result, prescription, invoice, or discharge note, up to five pages at a time. Apple Vision reads it on the device. With Pro on iOS 26 and an eligible device, Apple Intelligence fills in dates, vet, vaccines, medications, diagnoses, and the next-due date, and you review every field before saving. Free includes 10 scans with manual fill."
  - title: "Import past records"
    description: "Pick one records PDF of up to 100 MB. Pawza reads every page, splits it into visits by date and, with Apple Intelligence, pulls out the vet, vaccines, medications, and weights for each. Merge, split, or discard visits, then save once. On iOS 26, long files keep going in the background."
  - title: "Care log, widgets, and Siri"
    description: "One-tap chips log food, water, walks, toilet trips, and mood on five levels. Eight free widgets put a care streak, a quick-log button, upcoming reminders, and every pet's last meal and walk on your Home Screen and Lock Screen. A Control Center button on iOS 18 and phrases such as \"Log walk in Pawza\" work without opening the app."
  - title: "Medications, vaccines, and reminders you can answer"
    description: "Add a medication course with its dose and a repeating reminder, and tap Given on the notification to record each dose. Turn on Track supply and Pawza counts the doses left and adds a refill reminder. Vaccines keep the date given, next due date, and lot number. A reminder marked Time-sensitive breaks through Focus, and a one-time one re-alerts after 5, 15, and 30 minutes until you act."
  - title: "Weight chart and weight alerts"
    description: "Log weigh-ins in kg or lb, down to two decimals for kittens, rabbits, and toy breeds, and see the trend over the range you choose. With Pro, Pawza alerts you when weight changes quickly, for example a loss of 8% or more in 30 days. The alerts compare change over time; they are not a healthy-weight range."
  - title: "Symptoms, records, and photos"
    description: "Log a symptom with its area, severity, a note, and up to three photos, so \"when did it start?\" has a date. Records hold up to 10 photos or PDFs each, and you can search them or filter by vet or clinic. The photo gallery filters by vet visit, symptom, and milestone; Pro adds auto-sorting (correct any it gets wrong) and side-by-side Compare Photos."
  - title: "Vet Visit PDF and Since last vet visit"
    description: "The free dashboard card shows what changed since the last visit. With Pro, one tap builds a PDF with medications, diet, vaccinations, weight, symptoms, the last week of care, contacts, and insurance, on Letter or A4 paper. Where Apple Intelligence is available it writes the summary paragraph; otherwise a template does."
  - title: "Emergency Card, Lost Pet Kit, and Sitter Pack"
    description: "The Emergency Card holds allergies, current medications, insurance, microchip details, and a call button for the vet, the emergency clinic, and your backup contact, even offline. The free Lost Pet Kit has a printable poster, a QR collar tag any phone can scan, and a first-hours checklist. With Pro, the Sitter Pack prints feeding times, doses, a day-by-day checklist, and who to call for stays of up to 31 days."
  - title: "Import from a file, export with Pro"
    description: "Bring records over from a Pawza backup (JSON) or a CSV file, with a preview before anything is added. Importing is always free. With Pro, export everything as a JSON backup, a ZIP of spreadsheets, or a PDF for each pet."

screenshots:
  - src: "/assets/screenshots/pawza/1.webp"
    alt: "Pawza pet dashboard showing a dog profile, next medication, care log and weight"
  - src: "/assets/screenshots/pawza/2.webp"
    alt: "Pawza document scan of a vaccination certificate with extracted details to confirm"
  - src: "/assets/screenshots/pawza/3.webp"
    alt: "Pawza reminders grouped by this week and later for medication, grooming and vaccines"
  - src: "/assets/screenshots/pawza/4.webp"
    alt: "Pawza health records with vaccinations, lab results and diagnoses"
  - src: "/assets/screenshots/pawza/5.webp"
    alt: "Pawza weight tracking with a trend chart and history"
  - src: "/assets/screenshots/pawza/6.webp"
    alt: "Pawza photo gallery of a pet"
  - src: "/assets/screenshots/pawza/7.webp"
    alt: "Pawza printable vet visit PDF with medications, vaccinations and weight"
  - src: "/assets/screenshots/pawza/8.webp"
    alt: "Pawza My Pets screen with a profile for each pet and an add-pet button"
  - src: "/assets/screenshots/pawza/9.webp"
    alt: "Pawza care log with walk, water, food and toilet entries and a shareable vet summary"
  - src: "/assets/screenshots/pawza/10.webp"
    alt: "Pawza Home Screen widgets showing care logs and a heatmap of care over time"

comparison_table:
  intro: "Pawza compared with the most-searched pet health apps on cost, where your pet's data lives, and how much typing you have to do."
  competitors:
    - "Pawza"
    - "11pets"
    - "PetDesk"
    - "Pawprint"
  rows:
    - feature: "Pricing model"
      values:
        - "Free for 1 pet; Pro monthly, yearly, or lifetime"
        - "Free + subscription"
        - "Free (clinic-tied)"
        - "Free + in-app purchases"
    - feature: "Reads vet documents into records"
      values:
        - "✓ On-device text recognition; Apple Intelligence auto-fill with Pro"
        - "Manual entry"
        - "Pulls from partner clinics"
        - "Requests records by fax/clinic"
    - feature: "Works without an account"
      values:
        - "✓ No account"
        - "Account required"
        - "Account required"
        - "Account required"
    - feature: "Where your data lives"
      values:
        - "✓ Your device + your own iCloud"
        - "Cloud servers"
        - "Cloud servers"
        - "Cloud servers"
    - feature: "Third-party tracking / ads"
      values:
        - "None"
        - "Standard analytics"
        - "Standard analytics"
        - "Standard analytics"
    - feature: "One-tap vet-visit PDF export"
      values:
        - "✓ Pro"
        - "Limited"
        - "Via clinic portal"
        - "Limited"
    - feature: "Lifetime one-time purchase"
      values:
        - "✓ {P_LIFETIME}, with Family Sharing"
        - "Subscription only"
        - "N/A"
        - "N/A"
    - feature: "iPhone + iPad universal"
      values:
        - "✓ One app"
        - "Varies"
        - "Yes"
        - "Yes"
  footnote: "Competitor details reflect publicly documented features as of 2026 and vary by region and clinic partnerships. The App Store is the canonical source for current pricing. Pawza is independent and not affiliated with any veterinary clinic network."

privacy:
  data_collection: "Nothing sent to the developer; data stays on your devices and your own iCloud"
  tracking: false
  account_required: false
  app_privacy_label: "Pawza does not track you and carries no advertising or analytics SDKs. Your pet's records stay on your device and, if you turn on sync, in your own private iCloud."
  notes:
    - "No account: open the app and add your first pet"
    - "Pawza carries no ad, analytics, or crash-reporting SDKs and does not track you"
    - "Document scanning, records import, and Apple Intelligence extraction run on your device; documents are not uploaded"
    - "Optional sync uses your own private iCloud across your iPhone and iPad; Lagerland Apps has no server of its own and cannot read your data"
    - "Photos are stripped of location and EXIF data when you import them"

faq:
  - q: "What is Pawza?"
    a: "Pawza is a pet health record app for iPhone and iPad. Each pet gets one dashboard with medications, vaccinations, diet, weight, symptoms, records, photos, reminders, and a daily care log. You can scan vet documents or import a records PDF, and both run on your device. It is free for one pet. Pawza Pro adds unlimited pets, unlimited scans with Apple Intelligence auto-fill, the Vet Visit PDF, the Sitter Pack, weight alerts, and data export."
  - q: "How does the AI document scanning work?"
    a: "Scan a vaccination certificate, lab result, prescription, invoice, or discharge note with the camera, or pick up to five photos. Apple Vision reads the text on your device. With Pawza Pro on iOS 26 or later and a device that supports Apple Intelligence, the on-device model fills in the document type, visit date, vet and clinic, vaccinations, medications, diagnoses, weight, and next-due date. Without it, the review form opens with the recognized text and you complete the fields. Either way you review every field before anything is saved, because extraction can be wrong."
  - q: "Can I import years of old vet records at once?"
    a: "Yes. Import past records takes one PDF of up to 100 MB, reads every page, and splits it into visits by date. With Apple Intelligence it also pulls out the vet, vaccines, medications, and weights per visit; without it, you fill in the details. You merge, split, or discard visits and save once. Your first import is free and does not use up a scan; later imports need Pro. On iOS 26, long files continue in the background."
  - q: "Is Pawza free?"
    a: "Yes, for one pet and with no time limit. Free includes the care log, medications, vaccinations, symptoms, records, the weight chart, reminders, the Emergency Card, the Lost Pet Kit, all 8 widgets, the Control Center button, Siri, iCloud sync, your first records import, 10 document scans, and 50 photos in total. Pawza Pro costs {P_MONTHLY}/month or {P_YEARLY}/year, each starting with a {TRIAL}, or {P_LIFETIME} once, and every Pro plan includes Family Sharing. Prices in USD; the App Store shows your local currency."
  - q: "What does Pawza Pro unlock?"
    a: "Unlimited pets, unlimited document scans with Apple Intelligence auto-fill (iOS 26 or later on an eligible device), unlimited records imports and photos, photo auto-sorting and Compare Photos, the Vet Visit PDF, the Sitter Pack, weight alerts, and full data export as JSON, CSV, or PDF."
  - q: "Is my pet's data private?"
    a: "Yes. Pawza needs no account, has no server of its own, and carries no ads or analytics. Records are stored on your device. If you sign in to iCloud, they sync through your own private iCloud between your iPhone and iPad, and Lagerland Apps cannot read them. Scanning and records import run on the device, and imported photos are stripped of location and EXIF data."
  - q: "Does Pawza work without an internet connection?"
    a: "Yes. Logging, records, scanning, reminders, widgets, and PDFs all work offline. Pawza needs a connection only for iCloud sync and for purchases."
  - q: "Can I track more than one pet?"
    a: "The free plan covers one pet; Pawza Pro removes the limit. Each pet gets its own dashboard, and the Up next and The pack widgets show reminders and the last meal and walk for all of them. Archived pets keep their history."
  - q: "Can my family share my pet's records?"
    a: "No. iCloud sync covers your own devices, so a partner or sitter on their own Apple Account sees a separate record. For a sitter, the Sitter Pack (Pro) prints everything they need. Every Pro plan includes Family Sharing, which shares the Pro purchase with your family group; each person keeps their own records."
  - q: "Does Pawza work on iPad?"
    a: "Yes. Pawza is one universal app for iPhone and iPad, and on iPad the Pets tab becomes a two-column view with the list beside the dashboard. Your records sync between the two through your own iCloud. Pawza requires iOS 17.6 or later and has no Mac, Apple Watch, or Android version."
  - q: "Which vaccinations and treatments can I track in Pawza?"
    a: "Whatever your vet gives. Each vaccine keeps the date given, the next due date, the lot number, and notes, and can remind you on the due day. Medication courses keep the dose, a repeating dose reminder, and the dose history. Because you enter the names your vet uses, or scan them from the certificate, Pawza works with any country's schedule: rabies, DHPP, Bordetella, and leptospirosis for dogs, FVRCP and FeLV for cats, or a rabbit's or horse's own vaccines."
  - q: "Will I get reminders for vaccinations and medications?"
    a: "Yes. Reminders are local notifications in six categories: vaccine, medication, feeding, grooming, vet visit, and custom. They can be one-time or repeat daily, weekly, monthly, or yearly. A dose notification has a Given button that records the dose, a feeding one has Fed, and the others have Mark Done and Snooze 1 hour. Mark a reminder Time-sensitive to break through Focus; a one-time Time-sensitive reminder re-alerts after 5, 15, and 30 minutes until you act. Reminders need notification permission."
  - q: "Can I share my pet's history with a vet?"
    a: "Yes, with Pawza Pro. The Vet Visit PDF covers the time range you pick and can include what changed since the last visit, current medications and diet, vaccination status, recent weight and visits, symptoms, the last 7 days of care, contacts, insurance, and your own \"What to discuss\" notes. Share it as a PDF or an image, on Letter or A4 paper."
  - q: "Do I need Apple Intelligence to use Pawza?"
    a: "No. Apple Intelligence auto-fill is a Pawza Pro feature that needs iOS 26 or later on an eligible device (the app names iPhone 15 Pro or newer). On every other device, Pawza reads documents with on-device text recognition and you fill in the fields yourself. Everything else in the app works the same."
  - q: "Does Pawza diagnose health problems?"
    a: "No. Pawza keeps records; it is not a medical device and does not give veterinary advice. Weight alerts flag a quick change over time, and symptom logs and summaries help you describe what happened. The diagnosis stays with your vet."
  - q: "Can I log care from my Home Screen or with Siri?"
    a: "Yes, and it is all free. Eight widgets cover the Home Screen and Lock Screen, including a one-tap Quick log button and an Up next list with a Mark Done button. On iOS 18 a Log care button goes in Control Center. Siri understands phrases such as \"Log walk in Pawza\" and \"Log care for Bella in Pawza\". Widgets update from the app, so open Pawza once after adding a pet or a reminder."
  - q: "Can I move my records from another pet app?"
    a: "Through a file. Pawza imports Pawza backups (JSON) and CSV files, shows a preview, and importing is always free. It has no direct connection to other apps. If your old app can export a PDF of your records, Import past records can read that too."
  - q: "How do I cancel a Pawza Pro subscription?"
    a: "Open Settings, tap your name, then Subscriptions, and cancel before the renewal date; you keep Pro until the period ends. Monthly and Yearly start with a {TRIAL} for eligible accounts and renew automatically unless cancelled. Lifetime is a one-time purchase with nothing to cancel. Apple handles refunds through the standard App Store refund flow."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/pawza/support/"

release:
  first_release: "2026-06-06"
  last_updated: "2026-06-06"

related_journal:
  slug: "pet-medical-records-what-to-keep"
  anchor: "What actually belongs in your pet's medical record, and who asks for it"

ratings:
  value: "5.0"
  count: 1
  last_synced: "2026-08-13"
last_updated: 2026-10-29
---
Most of a pet's health history arrives on paper: a vaccination certificate from the shelter, a printout after a late-night visit, an invoice with a dose written on it. Then the vet asks when the limping started, or you stand in the kitchen unsure whether this morning's pill went in. Pawza keeps those answers in one record per pet, on the iPhone or iPad you already carry.

We don't think a pet's medical file needs an account on someone else's server, so Pawza has none. Text recognition runs on your device, and so does Apple Intelligence extraction (with Pawza Pro, on iOS 26 and an eligible device). Imported photos lose their location data. If you sign in to iCloud, records sync between your own devices through your private iCloud. Lagerland Apps has no server to receive them and cannot read them.

A one-tap care log for food, water, walks, bathroom breaks, and mood, eight free widgets, a Control Center button on iOS 18, and Siri phrases such as "Log walk in Pawza" add up to the pattern the vet asks about. The Since last vet visit card counts what changed since the last appointment, and with Pro the Vet Visit PDF puts it on one page. Pawza keeps the record and leaves the diagnosis to your vet: weight alerts and symptom logs help you describe what happened.
