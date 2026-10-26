---
layout: app
slug: pawza
name: "Pawza"
tagline: "Your pet's whole life, in one place."
quick_answer: "Pawza is a private pet health record keeper for iPhone and iPad. Photograph any vet document and on-device AI reads it and fills in vaccinations, medications, and visit notes. It tracks shots, meds, weight trends, and photos for every pet, reminds you on the day anything is due, and exports a clean vet-visit PDF in one tap. Free for one pet. Pawza Pro unlocks unlimited pets and scans, AI auto-fill and summaries, the unlimited photo gallery, and the vet PDF, from {P_MONTHLY}/month, {P_YEARLY}/year (7-day free trial), or {P_LIFETIME} once with Family Sharing. No ads, no tracking, no account. Data stays on your device, with optional iCloud sync."
category: health
status: live
show_body: true

app_store_url: "https://apps.apple.com/app/id6773507068"

price:
  model: freemium
price_tier: "Pawza Pro"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. The Lifetime tier is a one-time purchase with no auto-renewal. Monthly and Yearly include a 7-day free trial and can be cancelled anytime in Settings before renewal. Pawza is universal, so one purchase runs on both iPhone and iPad."

plans:
  - name: "Free"
    price: "$0"
    summary: "Everything you need for one pet, with no time limit, no card, and no account."
    features:
      - "One pet profile"
      - "Your first 10 document scans &amp; 50 photos"
      - "Health records, vaccinations &amp; medications"
      - "Reminders for shots, meds &amp; checkups"
      - "Weight tracking with trend charts"
      - "On-device storage, no account required"
  - name: "Pro · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Full Pawza Pro, billed monthly. 7-day free trial."
    features:
      - "Unlimited pets"
      - "Unlimited document scans with AI auto-fill"
      - "AI summaries for every record"
      - "Unlimited searchable photo gallery"
      - "Vet-visit PDF generator"
  - name: "Pro · Yearly"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "Same Pro features, billed once a year, with a 7-day free trial. About {SAVE_YEARLY}% cheaper than monthly."
    highlight: true
    features:
      - "Everything in Pro · Monthly"
      - "About {SAVE_YEARLY}% cheaper than monthly over a year"
      - "7-day free trial, cancel anytime"
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All Pro features for one payment, about the cost of two years of yearly Pro."
    features:
      - "Everything in Pro · Yearly"
      - "One-time purchase, no renewal"
      - "Family Sharing for up to 5 family members at no extra cost"
      - "Future Pro features included"
      - "Restores on every device with the same Apple ID"
    highlight_label: "Best long-term value"

icon: "/assets/icons/pawza.png"
og_image: "/assets/og/pawza.png"

seo:
  title: "Pet Health Record App for iPhone & iPad | Pawza"
  description: "Private pet health record app for iPhone & iPad. Snap a vet document and on-device AI fills in vaccinations, meds, and weight. No account, no ads."
  keywords:
    - pet health record app iphone
    - pet vaccination tracker
    - dog vaccine record app
    - cat health record app
    - pet medication reminder app
    - vet records app iphone
    - pet medical history app
    - ai vet document scanner
    - scan vet records app
    - pet weight tracker app
    - multiple pets health app
    - pet care organizer iphone
    - dog health tracker app
    - cat vaccination reminder
    - pet vet visit pdf export
    - puppy vaccination schedule app
    - kitten vaccine tracker
    - pet photo organizer app
    - pet reminders app iphone
    - deworming reminder app
    - flea tick reminder app
    - pet passport app
    - private pet app no tracking
    - offline pet health app
    - icloud pet records sync
    - pet care app no subscription
    - pet medication schedule tracker
    - dog medical records app
    - pet health app for ipad
    - family pet health organizer

hero:
  headline: "Your pet's whole life, in one place."
  secondary: "Every vaccine, vet visit, and good-boy moment, kept for good."
  subheadline: "Pawza is a private pet health record app for iPhone and iPad. Photograph any vet document and on-device AI reads it and fills in the vaccinations, medications, and notes. The photo never leaves your device, because there's no Pawza server. Track weight trends, get a reminder on the day anything is due, keep every photo searchable, and hand the vet a clean PDF of the whole history in one tap."
  pre_headline: "Free for your first pet, with no card, no account, and your first 10 document scans included. Upgrade to Pro for AI auto-fill, unlimited pets and scans, and the vet PDF."
  cta_label: "Download Pawza on the App Store"
  alt: "Pawza dashboard on iPhone showing a pet profile with upcoming vaccination reminders, recent weight, and quick actions to scan a document or add a record"

who_for:
  - "You have a dog, cat, or any companion and want their whole medical history in one place instead of a drawer of paper"
  - "You juggle vaccinations, medications, and checkups across one or more pets and keep losing track of what's due"
  - "You're tired of retyping vet paperwork and would like to photograph it and let the app file it"
  - "You care about privacy and don't want your pet's health data sold, tracked, or parked on someone else's server"
  - "You want to walk into any vet visit with the full history ready as a PDF"

who_not_for:
  - "You want a social network for pets, public profiles, or a feed"
  - "You're looking for telehealth or a way to message a vet inside the app"
  - "You want a shopping app for pet food, toys, or insurance quotes"
  - "You only ever need a single reminder and don't care about records at all"

alternatives_to:
  - "11pets"
  - "PetDesk"
  - "Pawprint"
  - "Medika"
  - "PetNoter"
  - "VetKeep"

how_it_works:
  intro: "Scanning is where Pawza saves you the most work. Here is what happens between photographing a vet document and your records being filled in, and where that processing happens."
  steps:
    - title: "You snap the document"
      detail: "Point the camera at a vaccination certificate, lab result, prescription label, or discharge note, or pick existing photos of it, up to five pages. Pawza captures it and attaches the original to the pet's file so you always keep the source."
    - title: "Text is read on your device"
      detail: "Pawza extracts the text using Apple's on-device Vision OCR. The image stays on your iPhone or iPad for this step. Nothing is uploaded, because Pawza has no server."
    - title: "AI structures it into records"
      detail: "With Pawza Pro on a device with Apple Intelligence (iOS 26+), Pawza's on-device model turns the raw text into structured fields: vaccine name, date given, due date, medication, dose, vet, and clinic. On other devices, and on the free tier, it falls back to OCR-assisted entry. In both cases the extraction runs locally and documents are never sent to an external service."
    - title: "You review before anything is saved"
      detail: "Pawza shows you what it found and lets you correct or confirm each field. Nothing is written to your records until you approve it, so the AI fills the form and you decide what goes in."
    - title: "Reminders schedule themselves"
      detail: "When a scanned certificate lists a vaccine's next-due date, Pawza offers to add a yearly reminder for that date; log a vaccine by hand and it offers one a year from the date given. For a refill, deworming, or a checkup, add your own reminder with a date and time, repeating never, daily, weekly, monthly, or yearly. Each local notification fires on the due date at the time set (not days ahead), and you can mark it done or snooze it for an hour right from the banner."
    - title: "The whole history exports as a PDF"
      detail: "Before a vet visit, Pawza Pro turns the pet's complete history (vaccinations, medications, weight, visits, and notes) into a clean, printable PDF you can hand over, email, or save, without retyping anything or forgetting details."

value_points:
  - title: "Photograph it and Pawza files it"
    description: "Typing records in is the slowest part of keeping them, and Pawza does it for you: photograph any vet document and on-device AI reads the vaccine, date, medication, and vet, then puts each into the right field for you to confirm. Minutes of data entry become one tap."
  - title: "Never miss a shot, dose, or checkup"
    description: "Boosters, monthly meds, deworming, flea and tick treatments, and annual exams each get a local reminder on the day and at the time they're due, repeating daily, weekly, monthly, or yearly if you want. You get one nudge per due item on the schedule you set, and no alerts you didn't ask for."
  - title: "Private because there is no server"
    description: "There's no Pawza account and no Pawza server. Records live on your device in Apple's SwiftData, scanning and AI run on-device, and optional sync uses your own iCloud, compatible with Advanced Data Protection. No ads, no analytics SDKs, no tracking."
  - title: "For the whole household"
    description: "Add every pet: dogs, cats, and the companions in between. Pro removes the limits, and Family Sharing on the Lifetime tier lets the whole family keep the records together at no extra cost."

features:
  - title: "AI vet-document scanning"
    description: "Photograph a vaccination certificate, lab result, or prescription and Pawza reads it on-device; with Pawza Pro, it then fills in the vaccine, date given, due date, medication, dose, and clinic. The AI does the typing and you review and confirm each field. The original document is saved alongside the record."
  - title: "Vaccinations &amp; medications with dates and dosing"
    description: "Log every vaccination with its given and due dates: rabies, DHPP/DAPP (distemper, hepatitis, parvovirus), Bordetella, leptospirosis, parainfluenza and Lyme for dogs; FVRCP and FeLV for cats. Track medication courses, deworming, and flea/tick treatments with dose, schedule, and start/end dates. Pawza shows what's active, what's overdue, and what's coming up across every pet."
  - title: "Reminders on the day, at your time"
    description: "Local notifications for shots, refills, deworming, flea/tick treatments, and checkups arrive on the due date at the time you set, repeating daily, weekly, monthly, or yearly if you choose. Mark a dose done or snooze it for an hour from the notification; switch on Time-sensitive and it breaks through Focus. No account and no push server are involved."
  - title: "Weight tracking with trend charts"
    description: "Record weight over time and see it as a Swift Charts trend line. Catching a slow gain or loss early is often the difference between a quick fix and a vet bill, and the chart makes the trend easy to see."
  - title: "A complete, searchable health record"
    description: "Diagnoses, lab results, prescriptions, vet visits, grooming, and free-text notes sit in one timeline per pet. Keep the practical details alongside them too: microchip number, pet insurance policy, and the travel and pet-passport records you need for boarding, daycare, or crossing a border."
  - title: "Searchable photo gallery"
    description: "Keep every photo of your pet in one place, tagged and searchable, instead of lost among thousands in a camera roll. Pro removes the gallery limit so the whole album lives with the records."
  - title: "One-tap vet-visit PDF"
    description: "Pawza Pro turns a pet's full history (vaccinations, medications, weight, visits, and notes) into a clean, printable PDF to hand the vet, email ahead, or keep for boarding, travel, or a new clinic."
  - title: "Private &amp; on-device, with optional iCloud sync"
    description: "Records are stored locally with SwiftData, and scanning and AI extraction run on-device. Turn on iCloud and your data syncs across your own devices through your Apple ID; Lagerland Apps never sees or stores it. Compatible with Advanced Data Protection."

screenshots:
  - src: "/assets/screenshots/pawza/1.png"
    alt: "Pawza pet dashboard showing a dog profile, next medication, care log and weight"
  - src: "/assets/screenshots/pawza/2.png"
    alt: "Pawza AI document scan of a vaccination certificate with extracted details to confirm"
  - src: "/assets/screenshots/pawza/3.png"
    alt: "Pawza reminders grouped by this week and later for medication, grooming and vaccines"
  - src: "/assets/screenshots/pawza/4.png"
    alt: "Pawza health records timeline with vaccinations, lab results and diagnoses"
  - src: "/assets/screenshots/pawza/5.png"
    alt: "Pawza weight tracking with a trend chart and history"
  - src: "/assets/screenshots/pawza/6.png"
    alt: "Pawza searchable photo gallery of a pet"
  - src: "/assets/screenshots/pawza/7.png"
    alt: "Pawza printable vet visit PDF with medications, vaccinations and weight"
  - src: "/assets/screenshots/pawza/8.png"
    alt: "Pawza My Pets screen with a profile for each pet and an add-pet button"
  - src: "/assets/screenshots/pawza/9.png"
    alt: "Pawza care log with walk, water, food and toilet entries and a shareable vet summary"
  - src: "/assets/screenshots/pawza/10.png"
    alt: "Pawza Home Screen widgets showing care logs and a heatmap of care over time"

comparison_table:
  intro: "Pawza compared with the most-searched pet-health apps on cost, whether your pet's data stays private, and how much typing you have to do."
  competitors:
    - "Pawza"
    - "11pets"
    - "PetDesk"
    - "Pawprint"
  rows:
    - feature: "Pricing model"
      values:
        - "Free for 1 pet; Pro {P_MONTHLY}/mo to {P_LIFETIME} lifetime"
        - "Free + subscription"
        - "Free (clinic-tied)"
        - "Free + in-app purchases"
    - feature: "AI scans vet documents &amp; auto-fills records"
      values:
        - "✓ On-device AI (Pro)"
        - "Manual entry"
        - "Pulls from partner clinics"
        - "Requests records by fax/clinic"
    - feature: "Works without an account"
      values:
        - "✓ No account"
        - "Account required"
        - "Account required"
        - "Account required"
    - feature: "Data stays on your device"
      values:
        - "✓ On-device + your iCloud"
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
        - "✓ {P_LIFETIME} + Family Sharing"
        - "Subscription only"
        - "N/A"
        - "N/A"
    - feature: "iPhone + iPad universal"
      values:
        - "✓ One purchase"
        - "Varies"
        - "Yes"
        - "Yes"
  footnote: "Competitor details reflect publicly documented features as of 2026 and vary by region and clinic partnerships. The App Store is the canonical source for current pricing. Pawza is independent and not affiliated with any veterinary clinic network."

privacy:
  data_collection: "On-device only: no analytics, no advertising, no account"
  tracking: false
  account_required: false
  app_privacy_label: "Pawza requests no tracking (no IDFA), ships zero advertising or analytics SDKs, and stores your pet's records on-device in Apple's SwiftData, with optional sync through your own iCloud private database."
  notes:
    - "No ads, no analytics SDKs, no tracking; Pawza requests no App Tracking Transparency permission"
    - "No account required: open the app and start with your first pet"
    - "Document scanning and AI extraction run on-device; documents are never uploaded to a Pawza server (there isn't one)"
    - "All records are stored on your device; when you're signed in to iCloud they also sync through your own Apple ID's private iCloud database, compatible with Advanced Data Protection"
    - "Health-type data (vaccinations, medications) and your photos and notes are stored only to make the app work and are never sold or shared"

faq:
  - q: "What is Pawza?"
    a: "Pawza is a private pet health record keeper for iPhone and iPad. It stores every pet's vaccinations, medications, weight, vet visits, notes, and photos in one place. Its main feature is AI document scanning: photograph any vet document and on-device AI reads it and fills in the records for you. It's free for your first pet, and Pawza Pro unlocks unlimited pets, unlimited scans, AI auto-fill and summaries, the unlimited photo gallery, and one-tap vet-visit PDF export."
  - q: "How does the AI document scanning work?"
    a: "Photograph a vaccination certificate, lab result, prescription, or discharge note. Pawza extracts the text with Apple's on-device Vision OCR. With Pawza Pro on devices with Apple Intelligence (iOS 26 and later), an on-device model then sorts it into fields like vaccine name, date given, due date, medication, dose, and clinic. You review and confirm before anything is saved. All of this runs locally; documents are never sent to an external server."
  - q: "Is Pawza free?"
    a: "Yes. Pawza is free for one pet, with full health records, vaccinations, medications, reminders, and weight tracking, plus your first 10 document scans and 50 photos, and no card or account required. Pawza Pro adds unlimited pets and document scans, AI auto-fill and summaries for scanned records, the unlimited photo gallery, and the vet-visit PDF generator. Pro is {P_MONTHLY}/month or {P_YEARLY}/year (each with a 7-day free trial), or {P_LIFETIME} once as a Lifetime purchase with Family Sharing."
  - q: "What does Pawza Pro unlock?"
    a: "Pro removes the one-pet limit (add as many pets as you like) and gives you unlimited document scans with AI auto-fill, AI summaries for every record, an unlimited searchable photo gallery, and the one-tap vet-visit PDF export. The free tier is fully usable for a single pet; Pro is for multi-pet households and anyone who wants the scanning and PDF features."
  - q: "Is my pet's data private?"
    a: "Yes. Pawza has no account and no server of its own. Records are stored on your device in Apple's SwiftData, and document scanning and AI extraction run on-device. If you turn on iCloud sync, your data goes into your own private iCloud database through your Apple ID. Lagerland Apps never sees or stores it, and it's compatible with Apple's Advanced Data Protection. There are no ads, no analytics SDKs, and no tracking."
  - q: "Does Pawza work without an internet connection?"
    a: "Yes. Adding records, scanning documents, setting reminders, and tracking weight all work with no connection. Pawza only uses the internet for optional iCloud sync across your own devices."
  - q: "Can I track more than one pet?"
    a: "The free tier covers one pet. Pawza Pro removes the limit so you can track every dog, cat, and companion in the household. The Lifetime tier includes Family Sharing, so up to five family members can keep the records together at no extra cost."
  - q: "Does Pawza work on iPad?"
    a: "Yes. Pawza is a universal app that runs on both iPhone and iPad, with an adaptive iPad layout. One purchase covers both, and your records sync between them through your own iCloud."
  - q: "Which vaccinations and treatments can I track in Pawza?"
    a: "Any of them. Pawza tracks core and non-core vaccines, plus deworming, flea and tick treatments, and any custom medication course, each with its own given and due dates. For dogs that includes rabies, DHPP/DAPP (distemper, adenovirus/hepatitis, parvovirus), Bordetella, leptospirosis, parainfluenza and Lyme; for cats, FVRCP and FeLV. You type the dates in or scan them straight from your vet's certificate, and Pawza can remind you on the day each booster, refill, or treatment is due. Because the dates come from your own records, Pawza works with any country's vaccination schedule."
  - q: "Will I get reminders for vaccinations and medications?"
    a: "Yes. Reminders are local notifications that fire on the due date, at the time you set. There's no days-ahead warning, so if you want a head start, date the reminder earlier. When a scanned vaccination certificate lists a next-due date, Pawza offers to add a yearly reminder for that date; for a medication refill, deworming, a flea or tick treatment, or an annual checkup, you add a reminder and choose whether it repeats daily, weekly, monthly, or yearly. Turn on Time-sensitive for a dose that must break through Focus: a one-off Time-sensitive reminder re-alerts after 5, 15, and 30 minutes until you mark it done or snooze it. Reminders work without an account or push server."
  - q: "Can I share my pet's history with a vet?"
    a: "Yes. Pawza Pro generates a clean, printable PDF of a pet's full history (vaccinations, medications, weight, visits, and notes) that you can hand to the vet, email ahead of an appointment, or keep for boarding, travel, or a new clinic."
  - q: "Do I need Apple Intelligence to use Pawza?"
    a: "No. AI auto-fill is a Pawza Pro feature that uses Apple Intelligence, which is available on iOS 26 and later on supported devices. On other devices, Pawza still reads documents with on-device OCR and helps you fill records in quickly; you just confirm a little more by hand. Pawza requires iOS 17.6 or later."
  - q: "How do I cancel a Pawza Pro subscription?"
    a: "Monthly and Yearly include a 7-day free trial and renew automatically unless cancelled. You can cancel anytime from Settings → your Apple ID → Subscriptions before the renewal date; you keep Pro until the period ends. The Lifetime tier is a one-time purchase with nothing to cancel. Refunds are handled by Apple through the standard App Store refund flow."

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
last_updated: 2026-10-26
---
Pawza is a private pet health record keeper for iPhone and iPad. It keeps every pet's medical history in one place (vaccinations, medications, weight, vet visits, notes, and photos) and takes over the most tedious part of keeping it, which is data entry. Photograph any vet document, such as a vaccination certificate, a lab result, a prescription label, or a discharge note, and Pawza reads it on-device and fills in the structured records for you. Text is extracted with Apple's Vision OCR. With Pawza Pro on devices with Apple Intelligence (iOS 26 and later), an on-device model turns that text into fields like vaccine name, date given, due date, medication, dose, and clinic; otherwise Pawza falls back to OCR-assisted entry. The processing is local in both cases, and documents are never uploaded to a Pawza server, because Pawza has no server. You review and confirm before anything is written to your records. Pawza also tracks vaccinations and medication courses with given and due dates, sends a local reminder on the day each shot, refill, deworming, flea/tick treatment, or checkup is due, charts weight with Swift Charts so a slow gain or loss shows up early, keeps a searchable photo gallery, and with Pawza Pro exports a pet's entire history as a printable vet-visit PDF in one tap. Pawza is free for one pet with full records, reminders, and weight tracking and no account required. Pawza Pro unlocks unlimited pets and scans, AI auto-fill and summaries for scanned records, the unlimited photo gallery, and the vet PDF for {P_MONTHLY}/month or {P_YEARLY}/year (each with a 7-day free trial), or {P_LIFETIME} once as a Lifetime purchase that includes Family Sharing for up to five family members. On privacy, there is no Pawza account and no Pawza server; records live on-device in Apple's SwiftData, optional sync uses your own private iCloud database through your Apple ID and is compatible with Advanced Data Protection, and there are no ads, no analytics SDKs, and no tracking. Pawza is a universal app, so one purchase runs on both iPhone and iPad with an adaptive iPad layout. It requires iOS 17.6 or later.
