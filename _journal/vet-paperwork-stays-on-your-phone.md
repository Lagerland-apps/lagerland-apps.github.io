---
layout: journal
slug: vet-paperwork-stays-on-your-phone
title: "Your vet paperwork is a household document, and it should never leave the phone"
seo:
  title: "Scan Vet Records on iPhone: Why On-Device Beats Cloud"
  description: "A vet invoice carries your name, address, phone and your pet's microchip number. Why on-device scanning beats cloud OCR, and how to test any pet app."
  keywords:
    - "on-device document scanning"
    - "is my pet data private"
    - "pet health app privacy"
    - "scan vet records iphone"
    - "vet document scanner app"
    - "offline pet records app"
    - "pet app no account"
    - "on-device ocr vs cloud ocr"
date: 2026-07-12
lede: "Nobody would upload a photo of their driving licence to a free web tool. Plenty of people photograph the dog's rabies certificate into a cloud pet app without a second thought, and those two documents carry roughly the same household. Here is what is actually printed on vet paperwork, what changes when the image leaves the device, and a four-test checklist you can run on any health app before you trust it with the drawer."
quick_answer: "Vet paperwork is a household document, not a pet document. A typical invoice or vaccination certificate prints the owner's full name, home address, phone, email, the animal's microchip number, and the clinic and vet who treated it. Scanning it on-device means the image is only ever a file in the app's own container: it works in airplane mode, a company breach cannot expose it, and no later policy change can reach back and re-use it. Cloud extraction is often more accurate on creased or faded scans and improves without an app update, but it makes the upload permanent while the convenience lasts a few seconds."
faq:
  - q: "What personal information is printed on a vet invoice?"
    a: "Usually more than people expect. A standard invoice or vaccination certificate carries the owner's full name, home address, phone number and often email; the animal's name, species, breed, date of birth and microchip transponder code; the treating vet's name and licence number; the clinic's address; the drug names, batch or lot numbers and dosages administered; and sometimes a masked card reference or account number from payment. The animal is one field among a dozen about the household."
  - q: "Is it safe to scan vet records into a pet health app?"
    a: "It depends entirely on where the extraction runs. If the app reads the page on your device, the photo is a file inside the app container and the risk is the same as any photo on your phone. If the app posts the image to a server for OCR, you have handed a third party your name, address, phone and your pet's chip number, plus whatever retention window their policy allows. The feature looks identical from the outside, so you have to check."
  - q: "Does on-device document scanning work offline?"
    a: "Yes, and that is the cleanest test of whether an app is genuinely on-device. Apple's VisionKit capture and Vision text recognition are part of the operating system and need no network. Turn on airplane mode, scan a document, and watch what happens. If the extraction completes and fills in the fields, the reading is local. If you get a spinner, a queued state, or a message about trying again later, the page was going somewhere."
  - q: "Is cloud OCR more accurate than on-device OCR?"
    a: "Often, yes, and it is worth being honest about that. Server-side models are not bound by a phone's memory or thermal budget, they can run larger ensembles, and they improve continuously without you updating anything. On a creased fax of a fax, a faded thermal printout, or unusual handwriting, cloud extraction will usually beat a local model. The question is whether that accuracy gap is worth making a permanent copy of your address on someone else's disk."
  - q: "How do I check whether a pet app uploads my documents?"
    a: "Run four tests. First, scan in airplane mode and see whether it completes. Second, read the App Store privacy nutrition label and check what is declared as collected and whether anything is linked to you. Third, see whether the app forces you to create an account, because an account implies a server that stores something. Fourth, look at the developer's stated Required Reason API disclosure and third-party SDK list. Any single test can be gamed; all four together are hard to fake."
  - q: "Can a pet health app change its privacy policy after I upload documents?"
    a: "Yes, and this is the asymmetry that matters. A privacy policy governs data the company holds, and it can be revised, superseded on acquisition, or reinterpreted under a new owner. You cannot un-upload a scan. Deletion requests apply to the live database and rarely to backups, log lines, or the derived text already extracted. Data that never left the device is not covered by any future version of anyone's terms."
mentioned_apps:
  - pawza
read_time: "12 min read"
excerpt: "A vaccination certificate names the owner, the address, the phone number and the microchip code before it ever names the animal. A field-by-field look at what vet paperwork actually contains, how on-device extraction differs from cloud OCR, and four tests that tell you which one an app is really doing."
---

Ask someone whether they would upload a photo of their driving licence to a free web tool and the answer is instant. No.

Ask the same person to photograph the dog's rabies certificate into a pet app and they will not think about it at all. It is the dog's certificate. The dog does not have a credit rating.

The certificate does not belong to the dog. It is filed mentally under the pet and it is, on paper, a document about a household with an animal named in it. That mismatch between how the document feels and what it contains is the whole subject of this post.

## What is actually printed on a vet invoice or vaccination certificate?

Pull one out of the drawer and read it field by field. The exact layout varies by country and practice-management software, but the contents are remarkably consistent.

| What is printed | Whose data is it | Why it matters if it leaves |
|---|---|---|
| Owner full name | Yours | The primary identifier on every other field below |
| Home address | Your household | Physical location, tied to a name and a phone number |
| Phone number, often email | Yours | The two fields that make a record joinable to other databases |
| Animal name, species, breed, DOB, sex | The pet | Common security-question and password-reset material |
| Microchip transponder code | The pet, registered to you | A permanent, unique, lifelong identifier for the animal |
| Clinic name and address | Third party | Places you geographically, often within a few kilometres of home |
| Treating vet's name, sometimes licence number | Third party | Professional identity, not yours to redistribute |
| Drug names, dose, route, batch or lot number | Clinical | Health data about the animal; batch numbers are traceable to supply |
| Diagnosis or presenting complaint | Clinical | The most sensitive line on the page, and often free text |
| Invoice number, date, amount, payment method | Financial | Sometimes a masked card reference or a practice account number |

Two of those deserve a closer look.

The microchip code is not a pet-only number. Transponders sold today generally follow the ISO 11784/11785 standard and carry a 15-digit code, while older chips in the United States may be 9 or 10 digits ([Wikipedia's summary of animal microchip standards](https://en.wikipedia.org/wiki/Microchip_implant_%28animal%29) is a decent overview of the encoding). That code is the key into a registry that holds your name, address and phone. Anyone can type a chip number into the AAHA Universal Pet Microchip Lookup Tool and find out which registry it is enrolled with. The tool returns the registry, not your details, but it is a useful reminder that the number is an index into a database about you, not a serial number on a piece of hardware.

The second is travel paperwork. The EU pet passport model, described on the European Commission's [pet movement pages](https://food.ec.europa.eu/animals/movement-pets_en), binds the transponder code to the owner's name and address in a single booklet, alongside the rabies vaccination record. If you have ever photographed a pet passport, you photographed an identity document with two subjects on it.

## Where does the image go? On-device versus cloud extraction

The user-facing feature is identical. You point the camera at a page, a moment passes, the fields fill in. Underneath, there are two completely different architectures, and they differ on the things you cannot see.

| Dimension | On-device extraction | Cloud extraction |
|---|---|---|
| Where the image goes | Stays in the app's container on the phone | Uploaded to the operator's infrastructure, often via a CDN and a queue |
| Airplane mode | Works. Capture and OCR are OS frameworks | Fails, or queues the scan for later upload |
| Latency | Bounded by the device; no round trip, no rate limit | Network round trip plus queue time; degrades on poor connections |
| What a breach exposes | Nothing. There is no copy to breach | The image, the extracted text, and the account it is attached to |
| What a policy change can do retroactively | Nothing. It cannot reach data it never had | Re-scope, re-use, or transfer everything already held |
| Retention and deletion | You delete the record, the file is gone | Deletion applies to the live store; backups and logs are a separate question |
| Accuracy on hard scans | Bounded by what fits on the device | Usually better on creased, faded or unusual pages |
| Improvement over time | Requires an OS or app update | Improves server-side with no action from you |
| Cost model | Compute is free once the device is bought | Per-page inference cost, which someone has to fund |

Read that last cost row carefully, because it explains the rest of the table. Server-side extraction has a marginal cost per page. That cost has to be recovered — through a subscription, through a clinic partnership, or through the data. Local extraction has no marginal cost at all, which is why a local app can offer scanning without a recurring bill and a cloud app usually cannot.

The two rows where cloud wins are real, and anyone selling on-device processing should say so out loud. A hosted model is not constrained by a phone's memory ceiling or thermal budget, so on a faded thermal printout, a fax of a fax, or a vet's handwriting in the margin, cloud OCR will frequently read a line a local model misses. And it improves while you sleep: the operator ships a new model and every future scan gets better, with no App Store update and no action from you.

## Which Apple frameworks actually do the reading?

Two, and both ship inside iOS.

Capture is [VisionKit's document scanner](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontroller), the same camera sheet you have used in Notes and Files. It finds the page edges, corrects perspective so a photo taken at an angle comes out rectangular, handles multi-page documents, and returns clean images.

Reading is the Vision framework's [text recognition](https://developer.apple.com/documentation/vision/recognizing-text-in-images), which locates and transcribes text in an image. The set of languages it recognises is enumerable at runtime and has grown across framework revisions, so an app should ask the OS rather than hard-code a marketing number.

Here is the part that trips people up. Neither framework tells you anything about privacy on its own. An app can present the VisionKit sheet, get a beautiful deskewed image back, and then POST it straight to a server. The capture UI is not evidence. What matters is what happens to the `UIImage` in the next twenty lines of code, and you cannot see those.

So you test the behaviour instead.

## How can you tell whether an app uploads your documents?

Four tests. None of them requires you to read code, and they work on any health app, not just pet apps.

| Test | How to run it | What a clean answer looks like |
|---|---|---|
| Airplane mode | Enable airplane mode, then scan a document and try to save it | Extraction completes and the record saves, with no spinner and no queue |
| Privacy nutrition label | On the App Store listing, open App Privacy | Nothing under Data Used to Track You; anything collected is Not Linked to You |
| Account requirement | Try to use the core feature on first launch | No sign-up wall. An account implies a server that stores something |
| Required Reason API disclosure | Check the developer's stated privacy manifest and SDK list | A short list of mundane APIs, and few or no third-party SDKs |

The airplane-mode test is the strongest of the four because it is behavioural rather than declarative. A marketing page can say "privacy-first" for free. A scan that completes with the radios off cannot be faked.

The other three are declarations, worth reading rather than skimming. Apple's [app privacy details](https://developer.apple.com/app-store/app-privacy-details/) are self-reported — a genuine weakness — but they are a public commitment with consequences if false, and the "Linked to You" versus "Not Linked to You" distinction is the one that matters most. [Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files) go further: they declare tracking status, tracking domains, and the Required Reason APIs an app calls, each with a category code. A long Required Reason list is not automatically bad, but it is worth reading, and so is the third-party SDK list — an analytics SDK you have never heard of is a data flow you did not choose.

That is why this studio publishes all of it on a single page. Our [transparency page](/transparency/) lists, per app, the declared tracking status, tracking domains, third-party SDKs, network calls and Required Reason API codes. For [Pawza](/apps/pawza/) that comes to two Required Reason APIs — app-specific user defaults and file timestamps within the app's own container — one third-party dependency, an archive library with no network access, and zero tracking domains. You should not take my word for that. You should read the page and then run the airplane-mode test yourself.

## Why the trade is asymmetric

The upload is permanent and the convenience is momentary.

You save a few seconds by having a server read the page instead of the phone. In exchange, a copy of a document containing your name, your address, your phone number and your pet's lifelong identifier exists on infrastructure you have never seen, governed by a document you did not negotiate, for a period you cannot verify.

Everything on the company's side of that trade can change. Policies get revised. Companies get acquired, and the acquirer inherits the database along with the terms, then revises the terms. Retention windows quietly extend when storage gets cheaper. A deletion request usually reaches the live database and rarely reaches the backup snapshots, the log lines, or the extracted text already sitting in a derived table.

Nothing on your side of the trade can change. You cannot un-upload the scan.

The other half of the asymmetry is who pays for a breach. If a pet-records service is compromised, the company writes a blog post, offers credit monitoring, and continues. You are the one whose home address was in the dump, attached to a phone number, a nearby clinic, and a note about which nights you board the dog. That is exactly the shape of data that makes ordinary fraud and ordinary stalking easier. The same argument applies to any file you casually hand to a web service, which is a point I have made before about [image converters](/journal/your-photos-shouldnt-ride-the-elevator/) and about [apps that ask for your bank login](/journal/i-will-not-ask-for-your-bank-login/).

The architectural answer is not to trust harder. It is to arrange things so that trust is not required. A scan that never leaves the device is not covered by any future version of anyone's terms, because there is nothing on the other end to apply them to.

## What on-device processing actually costs you

This is where I have to be straight about the trade-offs in our own app, because a post like this is worthless if it only lists the other side's compromises.

[Pawza](/apps/pawza/) is built to pass its own airplane-mode test. Capture and extraction both run on the device, there is no Pawza account and no Pawza server to upload to, and you confirm every extracted field before it is written. Records stay on iPhone and iPad with optional sync through your own iCloud.

The constraints are real. The best extraction needs Apple Intelligence, which means iOS 26 or later on a supported device; on older hardware Pawza falls back to OCR-assisted entry, and you confirm more by hand. There is no Android app and no web app, because the entire privacy argument rests on Apple's on-device frameworks. And the free tier limits how many documents you can scan, which is a business constraint, not a technical one.

The features we give up are, almost without exception, the ones that need a server. [VetKeep](/alternatives/vetkeep/) answers questions about your records in a conversational AI chat, which is far easier to build when the records already sit on a server; if that is the feature you want, the cloud is the honest way to get it today. [PetDesk](/alternatives/petdesk/)'s clinic booking and [11pets](/alternatives/11pets/)'s Android and web apps are the same story.

What we are not willing to do is quietly route the page through a server and describe it as scanning. For which documents are worth keeping, what each of them costs, and the full category rundown, the companion post on [what to keep in a pet medical record](/journal/pet-medical-records-what-to-keep/) covers the paperwork side.

## TL;DR

- **A vet document is a household document.** Owner name, home address, phone, email, the animal's microchip code, the clinic, the treating vet, the drugs and doses, and sometimes a payment reference. The pet is one field among a dozen about you.
- **The feature looks identical either way.** Point camera, fields fill in. The difference is entirely in where the image goes, which you cannot see from the UI.
- **Airplane mode is the honest test.** VisionKit capture and Vision text recognition are OS frameworks and need no network. If a scan completes with the radios off, the reading is local.
- **Cloud extraction genuinely wins on hard scans.** Bigger models, better on faded and creased pages, and they improve without an app update. That advantage is real and worth naming.
- **The asymmetry is the argument.** The convenience lasts seconds; the copy is permanent, and every term governing it can be rewritten afterwards by someone you never met.
- **Check four things on any health app:** airplane mode, the App Store privacy nutrition label, whether an account is forced, and the declared Required Reason APIs and third-party SDKs.

The drawer of paper in your kitchen has one useful property that no cloud service can match. Nobody can query it from another continent.
