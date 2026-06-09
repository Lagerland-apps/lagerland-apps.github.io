---
layout: app
slug: pawza
name: "Pawza"
tagline: "Your pet's whole life, in one place."
quick_answer: "Pawza is a private pet health record keeper for iPhone and iPad. Snap any vet document and on-device AI reads it and fills in vaccinations, medications, and visit notes automatically. Track shots, meds, weight trends, and photos for every pet, get gentle reminders before anything is due, and export a clean vet-visit PDF in one tap. Free for one pet; Pawza Pro unlocks unlimited pets and scans, AI summaries, the photo gallery, and the vet PDF — from $2.99/month, $19.99/year (7-day free trial), or $39.99 once with Family Sharing. No ads, no tracking, no account. Data stays on your device with optional iCloud sync."
category: health
platforms: ["iOS", "iPadOS"]
status: live
show_body: true

app_store_url: "https://apps.apple.com/app/id6773507068"

price:
  model: freemium
  value: "Free — Pawza Pro from $2.99/mo"
schema_price: "0"
schema_high_price: "39.99"
schema_offer_count: "4"

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple via the standard App Store refund flow. The Lifetime tier is a one-time purchase — no auto-renew. Monthly and Yearly include a 7-day free trial and can be cancelled anytime in Settings before renewal. Pawza is universal — one purchase runs on both iPhone and iPad."

plans:
  - name: "Free"
    price: "$0"
    summary: "Everything you need for one pet — forever. No card, no account."
    features:
      - "One pet profile"
      - "Health records, vaccinations &amp; medications"
      - "Reminders for shots, meds &amp; checkups"
      - "Weight tracking with trend charts"
      - "On-device storage — no account required"
  - name: "Pro · Monthly"
    price: "$2.99/mo"
    summary: "Full Pawza Pro, billed monthly. 7-day free trial."
    features:
      - "Unlimited pets"
      - "Unlimited document scans with AI auto-fill"
      - "AI summaries for every record"
      - "Unlimited searchable photo gallery"
      - "Vet-visit PDF generator"
  - name: "Pro · Yearly"
    price: "$19.99/yr"
    summary: "Same Pro features, billed once a year. 7-day free trial — about 44% cheaper than monthly."
    highlight: true
    features:
      - "Everything in Pro · Monthly"
      - "About 44% cheaper than monthly over a year"
      - "7-day free trial, cancel anytime"
  - name: "Lifetime"
    price: "$39.99 once"
    summary: "All Pro features, one payment. Roughly two years of yearly Pro — then it's yours."
    features:
      - "Everything in Pro · Yearly"
      - "One-time purchase, no renewal"
      - "Family Sharing — up to 5 family members at no extra cost"
      - "Future Pro features included"
      - "Restores on every device with the same Apple ID"
    highlight_label: "Best long-term value"

icon: "/assets/icons/pawza.png"
og_image: "/assets/og/pawza.png"

seo:
  title: "Pet Health Record App for iPhone & iPad — AI Vet Scanner | Pawza"
  description: "Private pet health record app for iPhone & iPad. Snap a vet document and on-device AI fills in vaccinations, meds & weight. Reminders, vet PDF, no account, no ads."
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
  secondary: "Every vaccine, vet visit, and good-boy moment — kept safe, forever."
  subheadline: "Pawza is a private pet health record app for iPhone and iPad. Snap any vet document and on-device AI reads it and fills in the vaccinations, medications, and notes — the photo never leaves your device, because there's no Pawza server. Track weight trends, get gentle reminders before anything is due, keep every photo searchable, and hand the vet a clean PDF of the whole history in one tap."
  pre_headline: "Free for your first pet — no card, no account. Snap one vet document and watch Pawza fill it in. Upgrade to Pro only when you want unlimited pets, scans, and the vet PDF."
  cta_label: "Download Pawza on the App Store"
  alt: "Pawza dashboard on iPhone showing a pet profile with upcoming vaccination reminders, recent weight, and quick actions to scan a document or add a record"

who_for:
  - "You have a dog, cat, or any companion and want their whole medical history in one place instead of a drawer of paper"
  - "You juggle vaccinations, medications, and checkups across one or more pets and keep losing track of what's due"
  - "You want to stop retyping vet paperwork — snap it and let the app file it"
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
  intro: "Scanning is the part of Pawza that does the work. Here's exactly what happens between photographing a vet document and your records being filled in — and where that processing happens."
  steps:
    - title: "You snap the document"
      detail: "Point the camera at a vaccination certificate, lab result, prescription label, or discharge note — or pick an existing photo or PDF. Pawza captures it and attaches the original to the pet's file so you always keep the source."
    - title: "Text is read on your device"
      detail: "Pawza extracts the text using Apple's on-device Vision OCR. The image never leaves your iPhone or iPad for this step — there is no upload to a Pawza server, because Pawza has no server."
    - title: "AI structures it into records"
      detail: "On devices with Apple Intelligence (iOS 26+), Pawza's on-device model turns the raw text into structured fields — vaccine name, date given, due date, medication, dose, vet, and clinic. On earlier devices it falls back to OCR-assisted entry. Either way, the extraction runs locally; documents are never sent to an external service."
    - title: "You review before anything is saved"
      detail: "Pawza shows you what it found and lets you correct or confirm each field. Nothing is written to your records until you approve it — the AI fills the form, you stay in control."
    - title: "Reminders schedule themselves"
      detail: "When a record has a due date — a booster, a refill, an annual checkup — Pawza offers to set a local notification ahead of time. One gentle nudge before it's due, never a daily nag."
    - title: "The whole history exports as a PDF"
      detail: "When it's time for a vet visit, Pawza Pro turns the pet's complete history — vaccinations, medications, weight, visits, and notes — into a clean, printable PDF you can hand over, email, or save. No re-typing, no forgotten details."

value_points:
  - title: "Snap it. Pawza files it."
    description: "The slowest part of keeping pet records is typing them in. Pawza removes it: photograph any vet document and on-device AI reads the vaccine, date, medication, and vet, then drops it into the right fields for you to confirm. Minutes of data entry become one tap."
  - title: "Never miss a shot, dose, or checkup"
    description: "Boosters, monthly meds, deworming, flea and tick treatments, annual exams — Pawza schedules a gentle reminder before each one is due. One nudge at the right time, not a stream of daily alerts."
  - title: "Private by design, not by promise"
    description: "There's no Pawza account and no Pawza server. Records live on your device in Apple's SwiftData, scanning and AI run on-device, and optional sync uses your own iCloud — compatible with Advanced Data Protection. No ads, no analytics SDKs, no tracking."
  - title: "Built for the whole household"
    description: "Add every pet — dogs, cats, and the companions in between. Pro removes the limits, and Family Sharing on the Lifetime tier means the whole family can keep the records together at no extra cost."

features:
  - title: "AI vet-document scanning"
    description: "Snap a vaccination certificate, lab result, or prescription and Pawza reads it on-device, then fills in the vaccine, date given, due date, medication, dose, and clinic. You review and confirm — the AI does the typing, you keep control. The original document is saved alongside the record."
  - title: "Vaccinations &amp; medications, tracked properly"
    description: "Log every vaccination — rabies, DHPP/DAPP (distemper, hepatitis, parvovirus), Bordetella, leptospirosis, parainfluenza and Lyme for dogs; FVRCP and FeLV for cats — with its given and due dates, and track medication courses, deworming, and flea/tick treatments with dose, schedule, and start/end dates. Pawza knows what's active, what's overdue, and what's coming up — across every pet."
  - title: "Reminders that respect your attention"
    description: "Local notifications for shots, refills, deworming, flea/tick treatments, and checkups — scheduled ahead of the due date. One gentle nudge per item, on time. No account, no push server, no daily nagging."
  - title: "Weight tracking with trend charts"
    description: "Record weight over time and see it as a clean Swift Charts trend line. Spotting a slow gain or loss early is often the difference between a quick fix and a vet bill — Pawza makes the trend obvious at a glance."
  - title: "A complete, searchable health record"
    description: "Diagnoses, lab results, prescriptions, vet visits, grooming, and free-text notes — every part of your pet's medical story in one timeline, per pet, ready when you need it. Keep the practical details alongside it too: microchip number, pet insurance policy, and the travel and pet-passport records you need for boarding, daycare, or crossing a border."
  - title: "Searchable photo gallery"
    description: "Keep every photo of your pet in one place, tagged and searchable — not lost in a camera roll of thousands. Pro removes the gallery limit so the whole album lives with the records."
  - title: "One-tap vet-visit PDF"
    description: "Pawza Pro turns a pet's full history into a clean, printable PDF — vaccinations, medications, weight, visits, and notes — to hand the vet, email ahead, or keep for boarding, travel, or a new clinic."
  - title: "Private &amp; on-device, with optional iCloud sync"
    description: "Records are stored locally with SwiftData; scanning and AI extraction run on-device. Turn on iCloud and your data syncs across your own devices through your Apple ID — Lagerland Apps never sees or stores it. Compatible with Advanced Data Protection."

screenshots:
  - src: "/assets/screenshots/pawza/1.png"
    alt: "Pawza pet dashboard on iPhone showing a pet profile with upcoming vaccination and medication reminders, recent weight, and quick actions"
  - src: "/assets/screenshots/pawza/2.png"
    alt: "Pawza AI document scanning — a vet vaccination certificate photographed and the extracted vaccine, date, and clinic ready to confirm"
  - src: "/assets/screenshots/pawza/3.png"
    alt: "Pawza reminders screen listing upcoming shots, medication doses, and a checkup, each scheduled ahead of its due date"
  - src: "/assets/screenshots/pawza/4.png"
    alt: "Pawza health records timeline with vaccinations, medications, lab results, and vet visit notes for a pet"
  - src: "/assets/screenshots/pawza/5.png"
    alt: "Pawza weight tracking screen with a trend chart showing a pet's weight history over time"
  - src: "/assets/screenshots/pawza/6.png"
    alt: "Pawza searchable photo gallery with tagged photos of a pet in one organized place"
  - src: "/assets/screenshots/pawza/7.png"
    alt: "Pawza vet-visit PDF export — a clean printable summary of vaccinations, medications, weight, and visits ready to share with the vet"
  - src: "/assets/screenshots/pawza/8.png"
    alt: "Pawza multi-pet view showing several dog and cat profiles managed together in one app"

comparison_table:
  intro: "Pawza versus the most-searched pet-health apps on the things owners actually care about: what it costs, whether your pet's data is private, and how much typing you have to do."
  competitors:
    - "Pawza"
    - "11pets"
    - "PetDesk"
    - "Pawprint"
  rows:
    - feature: "Pricing model"
      values:
        - "Free for 1 pet; Pro $2.99/mo–$39.99 lifetime"
        - "Free + subscription"
        - "Free (clinic-tied)"
        - "Free + in-app purchases"
    - feature: "AI scans vet documents &amp; auto-fills records"
      values:
        - "✓ On-device AI"
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
        - "✓ $39.99 + Family Sharing"
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
  data_collection: "On-device only — no analytics, no advertising, no account"
  tracking: false
  account_required: false
  app_privacy_label: "Pawza requests no tracking (no IDFA), ships zero advertising or analytics SDKs, and stores your pet's records on-device in Apple's SwiftData, with optional sync through your own iCloud private database."
  notes:
    - "No ads, no analytics SDKs, no tracking — Pawza requests no App Tracking Transparency permission"
    - "No account required — open the app and start with your first pet"
    - "Document scanning and AI extraction run on-device; documents are never uploaded to a Pawza server (there isn't one)"
    - "All records stay on your device by default; optional iCloud sync uses your own Apple ID and is compatible with Advanced Data Protection"
    - "Health-type data (vaccinations, medications) and your photos and notes are stored only to make the app work — never sold or shared"

faq:
  - q: "What is Pawza?"
    a: "Pawza is a private pet health record keeper for iPhone and iPad. It stores every pet's vaccinations, medications, weight, vet visits, notes, and photos in one place — and its standout feature is AI document scanning: photograph any vet document and on-device AI reads it and fills in the records for you. It's free for your first pet, with Pawza Pro unlocking unlimited pets, unlimited scans, AI summaries, the photo gallery, and one-tap vet-visit PDF export."
  - q: "How does the AI document scanning work?"
    a: "Snap a vaccination certificate, lab result, prescription, or discharge note. Pawza extracts the text with Apple's on-device Vision OCR, then — on devices with Apple Intelligence (iOS 26 and later) — uses an on-device model to structure it into fields like vaccine name, date given, due date, medication, dose, and clinic. You review and confirm before anything is saved. All of this runs locally; documents are never sent to an external server."
  - q: "Is Pawza free?"
    a: "Yes — Pawza is free for one pet, with full health records, vaccinations, medications, reminders, and weight tracking, no card and no account required. Pawza Pro adds unlimited pets and document scans, AI summaries for every record, the unlimited photo gallery, and the vet-visit PDF generator. Pro is $2.99/month or $19.99/year (each with a 7-day free trial), or $39.99 once as a Lifetime purchase with Family Sharing."
  - q: "What does Pawza Pro unlock?"
    a: "Pro removes the one-pet limit (add as many pets as you like), gives you unlimited document scans with AI auto-fill, AI summaries for every record, an unlimited searchable photo gallery, and the one-tap vet-visit PDF export. The free tier is fully usable for a single pet — Pro is for multi-pet households and anyone who wants the scanning and PDF power features."
  - q: "Is my pet's data private?"
    a: "Yes. Pawza has no account and no server of its own. Records are stored on your device in Apple's SwiftData, and document scanning and AI extraction run on-device. If you turn on iCloud sync, your data goes into your own private iCloud database through your Apple ID — Lagerland Apps never sees or stores it, and it's compatible with Apple's Advanced Data Protection. There are no ads, no analytics SDKs, and no tracking."
  - q: "Does Pawza work without an internet connection?"
    a: "Yes. Pawza works fully offline — adding records, scanning documents, setting reminders, and tracking weight all work with no connection. An internet connection is only used for optional iCloud sync across your own devices."
  - q: "Can I track more than one pet?"
    a: "The free tier covers one pet. Pawza Pro removes the limit so you can track every dog, cat, and companion in the household. The Lifetime tier includes Family Sharing, so up to five family members can keep the records together at no extra cost."
  - q: "Does Pawza work on iPad?"
    a: "Yes — Pawza is a universal app that runs on both iPhone and iPad, with an adaptive iPad layout. One purchase covers both, and your records sync between them through your own iCloud."
  - q: "Which vaccinations and treatments can I track in Pawza?"
    a: "Any of them. Pawza tracks core and non-core vaccines — rabies, DHPP/DAPP (distemper, adenovirus/hepatitis, parvovirus), Bordetella, leptospirosis, parainfluenza and Lyme for dogs, and FVRCP and FeLV for cats — plus deworming, flea and tick treatments, and any custom medication course, each with its own given and due dates. You type the dates in or scan them straight from your vet's certificate, and Pawza reminds you before each booster, refill, or treatment is due. Because dates come from your own records, Pawza works with any country's vaccination schedule, not just one region's."
  - q: "Will I get reminders for vaccinations and medications?"
    a: "Yes. When a record has a due date — a booster, a medication refill, deworming, a flea or tick treatment, or an annual checkup — Pawza can schedule a local notification ahead of time. You get one gentle reminder before each item is due, not a daily stream of alerts. Reminders work without an account or push server."
  - q: "Can I share my pet's history with a vet?"
    a: "Yes. Pawza Pro generates a clean, printable PDF of a pet's full history — vaccinations, medications, weight, visits, and notes — that you can hand to the vet, email ahead of an appointment, or keep for boarding, travel, or a new clinic."
  - q: "Do I need Apple Intelligence to use Pawza?"
    a: "No. The full AI auto-fill experience uses Apple Intelligence, which is available on iOS 26 and later on supported devices. On earlier devices, Pawza still reads documents with on-device OCR and helps you fill records in quickly — you just confirm a little more by hand. Pawza requires iOS 17.6 or later."
  - q: "How do I cancel a Pawza Pro subscription?"
    a: "Monthly and Yearly include a 7-day free trial and renew automatically unless cancelled. You can cancel anytime from Settings → your Apple ID → Subscriptions before the renewal date; you keep Pro until the period ends. The Lifetime tier is a one-time purchase with nothing to cancel. Refunds are handled by Apple through the standard App Store refund flow."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/pawza/support/"

release:
  first_release: "2026-06-06"
  last_updated: "2026-06-06"
---
Pawza is a private pet health record keeper for iPhone and iPad that keeps every pet's medical life in one place — vaccinations, medications, weight, vet visits, notes, and photos — and removes the most tedious part of doing so. Its defining feature is AI document scanning: photograph any vet document — a vaccination certificate, a lab result, a prescription label, a discharge note — and Pawza reads it on-device and fills in the structured records for you. Text is extracted with Apple's Vision OCR, and on devices with Apple Intelligence (iOS 26 and later) an on-device model turns that text into fields like vaccine name, date given, due date, medication, dose, and clinic; on earlier devices Pawza falls back to OCR-assisted entry. Either way the processing is local — documents are never uploaded to a Pawza server, because Pawza has no server. You always review and confirm before anything is written to your records. Around that, Pawza tracks vaccinations and medication courses with proper given/due dates, schedules gentle local reminders before each shot, refill, deworming, flea/tick treatment, or checkup is due, charts weight trends with Swift Charts so a slow gain or loss is obvious early, keeps a searchable photo gallery, and — with Pawza Pro — exports a pet's entire history as a clean, printable vet-visit PDF in one tap. Pawza is free for one pet with full records, reminders, and weight tracking and no account required; Pawza Pro unlocks unlimited pets and scans, AI summaries for every record, the unlimited photo gallery, and the vet PDF for $2.99/month or $19.99/year (each with a 7-day free trial) or $39.99 once as a Lifetime purchase that includes Family Sharing for up to five people. Privacy is structural rather than promised: there is no Pawza account and no Pawza server, records live on-device in Apple's SwiftData, optional sync uses your own private iCloud database through your Apple ID and is compatible with Advanced Data Protection, and there are no ads, no analytics SDKs, and no tracking. Pawza is a universal app — one purchase runs on both iPhone and iPad with an adaptive iPad layout — and requires iOS 17.6 or later.
