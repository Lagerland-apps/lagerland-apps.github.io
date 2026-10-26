---
layout: journal
slug: app-store-fields-that-need-a-new-version
title: "Promotional text vs description: which App Store fields you can change without an update"
date: 2026-09-19
seo:
  title: "Promotional Text vs Description: What Needs a New Version"
  description: "Which App Store fields change any time and which ship only with a new version: promotional text vs description, keywords, screenshots, name, subtitle."
  keywords:
    - "promotional text vs description"
    - "change app store description without update"
    - "app store promotional text"
    - "app store fields that need a new version"
    - "update app store screenshots without update"
    - "app information vs version information"
    - "app store connect editable fields"
    - "appmeta"
lede: "Half the App Store product page is frozen until your next update, and the other half you can change on a Tuesday afternoon. Apple documents which is which, but across four or five different help pages. This is all of it in one table, checked against Apple's current pages, with the two places most people get it wrong."
quick_answer: "Promotional text is the only marketing copy on your product page that you can change at any time: Apple says you can update it without submitting a new version, and it shows above the description, up to 170 characters. The description, keywords, What's New, screenshots, app previews, support URL and marketing URL belong to an app version, so changes go live with your next approved version, and the app icon needs a new build. The app name, subtitle, categories, age rating and privacy policy URL sit in App Information, shared across versions, yet they also change only while a new version is being prepared. Pricing and availability, App Privacy data types, App Review information, copyright and the primary language can be edited any time. Custom product pages and product page optimization tests without new icons can be submitted for review without a new version."
faq:
  - q: "What is the difference between promotional text and the description on the App Store?"
    a: "Promotional text is up to 170 characters, appears at the top of the description on the product page, and can be changed at any time without submitting a new version. The description is up to 4,000 characters of plain text and changes only when you submit a new version. Apple says promotional text doesn't affect search ranking and suggests using it for news that changes often, such as limited-time sales or upcoming features."
  - q: "Can I change my App Store description without an update?"
    a: "No. Apple says you can update the description when you submit a new version of your app. For anything that needs to change sooner, Apple points you to promotional text, which you can edit on the live version at any time."
  - q: "Can I update App Store screenshots without a new version?"
    a: "Not on the default product page. Apple accepts screenshot uploads for a version while it is in Prepare for Submission, Invalid Binary, Rejected, Metadata Rejected or Developer Rejected, which means a version you are preparing. Two exceptions run on their own review track: custom product pages, which can have their own screenshots and be submitted with or without an app version once your app is approved, and product page optimization tests, which Apple says can be submitted independently of a new version when they don't include alternate app icons."
  - q: "Do I need a new version to change my app name or subtitle?"
    a: "Yes. The name and subtitle live in App Information, which is shared across versions, but Apple's table of editable properties doesn't mark either as editable at any time, and Apple's product page guide says you can update your subtitle when submitting a new version. Change them while a new version is in Prepare for Submission."
  - q: "Which App Store Connect settings can I change at any time?"
    a: "Per Apple's table of required, localizable and editable properties: promotional text, price, pricing dates and availability, the App Privacy data types, App Review information, copyright, the primary language, the custom license agreement, the routing app coverage file, tax category and accessibility support. A phased release can be paused within its seven-day window."
  - q: "Does a metadata-only update need a new build?"
    a: "Yes, in practice. A new App Store version needs a build attached before you can submit it, and Apple's steps for creating a version include uploading a new build with an incremented build string. App Store Connect copies the current version's metadata into the new version for you, so you only edit what changes."
mentioned_apps:
  - appmeta
read_time: "7 min read"
excerpt: "One table of every App Store product page field and when you can change it: promotional text versus description, keywords, screenshots, name, subtitle, URLs and the any-time settings, plus the difference between App Information and version information, and the review tracks that skip a new version."
last_updated: 2026-10-26
---

App Store Connect splits your product page into things you can change on the live app and things that wait for the next version. Apple's [table of required, localizable and editable properties](https://developer.apple.com/help/app-store-connect/reference/app-information/required-localizable-and-editable-properties) marks the properties that "can be localized and edited at any time without submitting a new version of your app." Everything else changes with a version.

## Which App Store fields need a new version?

| Field | Lives in | Limit | When you can change it |
|---|---|---|---|
| Promotional text | Version | 170 characters | Any time, no new version |
| Description | Version | 4,000 characters | With a new version |
| Keywords | Version | 100 characters | With a new version |
| What's New | Version | 4,000 characters | With a new version (not on the first version) |
| Screenshots | Version | Up to 10 per display size | With a new version |
| App previews | Version | Up to 3 per localization and display size | With a new version |
| Support URL, marketing URL | Version | Full URL | With a new version |
| Copyright | Version | | Any time |
| App Review information | Version | Notes up to 4,000 bytes | Any time |
| App name | App Information | 30 characters | With a new version |
| Subtitle | App Information | 30 characters | With a new version |
| Primary and secondary category | App Information | | With a new version |
| Age rating | App Information | | With a new version |
| Primary language | App Information | | Any time |
| Privacy policy URL | App Privacy | | With a new version |
| App Privacy data types | App Privacy | | Any time |
| Price and availability | Pricing and Availability | | Any time |
| App icon | Your build | | With a new version and a new build |

Sources: the editable-properties table above, Apple's [Platform version information](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information/) reference, its [product page guide](https://developer.apple.com/app-store/product-page/), and the [Add an app icon](https://developer.apple.com/help/app-store-connect/manage-app-information/add-an-app-icon) page, which says changing the icon after publishing means creating and uploading a new version.

## Promotional text vs description: what's the difference?

They sit next to each other on the product page, but Apple treats them differently.

| | Promotional text | Description |
|---|---|---|
| Length | Up to 170 characters | Up to 4,000 characters, plain text, no HTML |
| Position | At the top of the description | Below the promotional text |
| When it changes | Any time, without a new version | With a new version |
| Search | Apple says it doesn't affect search ranking | Not listed among App Store search factors; used for web search engine results |
| Apple's suggested use | Current news: limited-time sales, upcoming features | What the app does; the first sentence is what people read without tapping more |

The practical rule follows from the third row. Anything that will be out of date in a month (a sale, a seasonal event, a feature that's coming soon) goes in promotional text, because you can take it out again without shipping. Anything that should stay true for the life of a version goes in the description. Apple also says to leave specific prices out of the description, which is easier to follow once you know the promotional text is the place for a sale.

Putting keywords into promotional text doesn't help. Apple says so on both its [search](https://developer.apple.com/app-store/search/) and product page guides, and the [keyword field](/journal/app-store-keyword-field-100-characters/) has its own rules.

## What's the difference between App Information and version information?

App Store Connect has two places for metadata, and the API mirrors them.

**App Information** is shared across all versions and platforms of the app. In the App Store Connect API it's an `appInfoLocalizations` record holding the name, subtitle, privacy policy URL and privacy choices URL, with the categories and age rating on the `appInfo` itself.

**Platform version information** belongs to one version on one platform. Its `appStoreVersionLocalizations` record holds the description, keywords, promotional text, What's New, support URL and marketing URL, and the version also carries the screenshots, app previews, copyright, version number, App Review information and release settings.

That split explains the first trap. App Information isn't tied to a version, so it's easy to assume you can edit it any time, and for most of it you can't. Apple's table marks the name, subtitle, categories, age rating and privacy policy URL as not editable at any time, and the product page guide ties subtitle changes to a new version. In the API, while an update is in preparation the app has two App Info records, one for the live version and one for the update, and the update's record is the one you edit.

The second trap is the promotional text itself. It is a version field, stored right next to the description, yet it's the only marketing copy you can change on a version that's already live. Tools that lock every version field once a version is approved get this one wrong, AppMeta included for now (more on that below).

## When does a version accept edits?

Apple lists the statuses in which you can upload and submit screenshots for a version: Prepare for Submission, Invalid Binary, Rejected, Metadata Rejected and Developer Rejected ([Apple's screenshot upload help](https://developer.apple.com/help/app-store-connect/manage-app-information/upload-app-previews-and-screenshots)). In other words, a version you're preparing or one that came back from review. If you spot a mistake after submitting, Apple's route is to remove the version from review, which sets it back to Developer Rejected; the review starts over when you resubmit ([Remove a submission from review](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/remove-a-submission-from-review)).

To start a new version, the current one has to be Ready for Distribution. App Store Connect copies the live version's metadata into the new one, so a description fix starts from what's already there ([Create a new version](https://developer.apple.com/help/app-store-connect/update-your-app/create-a-new-version)). You still need a build: a version can't be submitted without one, and Apple's steps include uploading a new build with an incremented build string. So a description-only update is still a full release with a new binary.

## What can you change without a new version?

Beyond promotional text, Apple's editable-properties table marks these as editable at any time:

- Price, pricing start and end dates, availability, the pre-order release date, tax category and the last-compatible version setting
- App Privacy data types (the privacy label)
- App Review information and copyright
- Primary language and the custom license agreement
- The routing app coverage file, for navigation apps
- Accessibility support, for the Accessibility Nutrition Labels
- Phased release, which you can pause within its seven-day window

Several review tracks also run without a new app version once your app has an approved one:

| Track | What it changes | Apple's rule |
|---|---|---|
| Custom product pages | Screenshots, app previews, promotional text and keywords on an alternate page, up to 70 per app | Submit with or without an iOS app version; keywords come from your latest approved version |
| Product page optimization | Up to three treatments of icons, screenshots and previews, for up to 90 days | Tests without alternate app icons can be submitted independently of a new version |
| In-App Events | Event cards and details | Submit with or without an iOS app version |
| In-App Purchases | New products and their metadata | Only the first product of each type needs a new app version |

The custom product page rules are on Apple's [submission page](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-a-custom-product-page), the test rules on its [product page optimization page](https://developer.apple.com/app-store/product-page-optimization/), and the In-App Purchase rule was clarified in Apple's [release notes](https://developer.apple.com/help/app-store-connect/release-notes/) on August 19, 2026. A product page optimization test can't change your default page's screenshots by itself, but if a treatment wins, Apple lets you apply it to the original product page.

## How I plan around it

When a version is in Prepare for Submission, I go through every version field and every App Information field in every localization, because that window is the only time most of them open. Between versions, the levers are promotional text and the review tracks above.

Screenshots follow the same window, and the [screenshot guidelines post](/journal/app-store-screenshot-review-guidelines-explained/) covers what App Review checks in them. The keyword field is the one I plan furthest ahead, because a keyword change waits for a version just like a description change does.

## Where AppMeta fits

[AppMeta](/apps/appmeta/) keeps the same split App Store Connect does. App Information fields (name, subtitle, privacy policy URL) and version fields are separate sections, and each push goes to the right API record. When the newest version on a platform is live, in review or waiting for release, AppMeta locks its version fields and says why, and you can create the next version from inside the app, then copy fields over from the previous one. Before anything is pushed, the preview shows the current App Store Connect value next to your change for every field and localization. AppMeta signs in with an API key you create yourself; the [setup guide](/journal/app-store-connect-api-key-setup/) walks through it.

AppMeta has one gap: it applies that version lock to promotional text too. To change promotional text on a live version with no update in progress, use the App Store Connect website for now.
