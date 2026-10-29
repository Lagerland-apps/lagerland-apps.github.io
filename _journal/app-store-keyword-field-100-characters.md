---
layout: journal
slug: app-store-keyword-field-100-characters
title: "How the App Store keyword field works: 100 characters, commas, and the words Apple already indexes"
date: 2026-05-16
seo:
  title: "App Store Keywords: How the 100-Character Field Works"
  description: "How to write App Store keywords: the 100-character limit, commas without spaces, which words Apple already indexes, plurals, and per-locale fields."
  keywords:
    - "app store keywords 100 characters"
    - "how to write app store keywords"
    - "app store keyword field"
    - "app store keywords commas no spaces"
    - "app store connect keywords"
    - "app store keywords per localization"
    - "appmeta"
lede: "Customers never see the keyword field, yet it decides a lot about who finds your app. Apple's rules for it would fit on an index card, and most of the advice around it is folklore. This post covers what Apple documents, what it leaves out, and how to spend 100 characters without wasting a third of them."
quick_answer: "The App Store keyword field holds 100 characters per localization. Separate terms with commas and no spaces (spaces are fine inside a phrase, as in Real Estate), because every space and comma counts toward the limit. Apple says your app is already searchable by its name, subtitle, and company name, and that its category is indexed, so don't spend keyword characters repeating words from those. Apple also says to skip plurals of words you already have, generic words like app, filler words like the, competitor names, and trademarked terms. Each localization has its own keyword field, and keyword changes go live with your next approved app version."
faq:
  - q: "How many characters can App Store keywords be?"
    a: "100 per localization. Apple's product page and search guides say 100 characters total; the App Store Connect reference page says 100 bytes. Commas and spaces count toward the limit. For English and most Latin-script languages one letter is one unit, but in scripts written with combining vowel signs, such as Hindi, the counter in App Store Connect runs higher than the number of letters you see, so check the count in the form itself."
  - q: "Should App Store keywords have a space after each comma?"
    a: "No. Apple asks for terms separated by commas with no spaces. A space after a comma uses one of your 100 characters and adds nothing. Spaces inside a multi-word term are fine; Apple's own example is Property,House,Real Estate."
  - q: "Do I need to repeat my app name or subtitle in the keyword field?"
    a: "No. Apple's App Store Connect help says your app is searchable by its app name, subtitle, keywords, and company name, and Apple's search guide says the primary and secondary categories are indexed and asks you not to repeat words from your name, subtitle, or category in the keyword field. Repeating them spends characters on words the App Store already has."
  - q: "Should App Store keywords be singular or plural?"
    a: "Use one form, not both. Apple's search guide says plurals of words you've already included, such as climbs and climb, are considered duplicates. Which form to keep, and whether every language and irregular plural is treated the same way, is not something Apple documents; that part is ASO folklore."
  - q: "Can I change my App Store keywords without submitting an update?"
    a: "No. The keyword field belongs to the app version, next to the description, so an edit goes live when your next version is approved. Promotional text is the field you can change at any time, but Apple says promotional text doesn't affect search ranking."
  - q: "Does the App Store description help search ranking?"
    a: "Apple doesn't list it. Its search guide names the app's title, subtitle, keywords, and primary category as the text it matches, and its reference says the description is used for web search engine results once the app is released. Apple also asks you not to add unnecessary keywords to the description to improve search results."
mentioned_apps:
  - appmeta
read_time: "7 min read"
excerpt: "A reference for the App Store keyword field: the 100-character limit, commas without spaces, the words Apple says are already indexed elsewhere, plurals, per-localization fields, a worked example of a wasted field and a fixed one, and the common ASO claims Apple doesn't document."
last_updated: 2026-10-29
---

The keyword field in App Store Connect is a single line of text per localization, and nobody browsing the App Store ever reads it. Apple's search guide says keywords "help determine where your app appears in search results." Below are its rules in one place, each with its source.

## What are the rules for the App Store keyword field?

| Rule | What Apple says | Source |
|---|---|---|
| Length | 100 characters total per localization (the reference page says 100 bytes) | [Product page](https://developer.apple.com/app-store/product-page/), [Platform version information](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information/) |
| Separator | Commas, no spaces. Spaces are allowed inside a phrase: Property,House,Real Estate | [App Store search](https://developer.apple.com/app-store/search/) |
| Word length | Each keyword greater than two characters | Platform version information |
| Don't repeat | Words already in your app name, subtitle, or category; the reference adds your company name | App Store search, Platform version information |
| Plurals | Avoid plurals of words already included; "climbs" and "climb" count as duplicates | App Store search |
| Avoid | Generic terms such as "app" or "game", filler words such as "the" and "to", special characters such as # or @ unless they're part of your brand | App Store search |
| Not allowed | Trademarked terms, celebrity names, competing app names, irrelevant or offensive terms | App Store search, product page |
| Scope | One field per localization; part of the app version's metadata | Platform version information |

Apple calls improper keyword use a common reason for App Store rejections, so the last two rows matter for review as well as for ranking.

## How does App Store Connect count the 100 characters?

Everything in the field counts, letters, commas, and spaces alike, which is why the no-spaces rule matters. Write the field the way people write lists, with a space after every comma, and ten terms cost you nine characters for nothing.

Apple's own pages disagree on the unit. The product page and search guides say 100 characters; the App Store Connect reference says 100 bytes. The counter in the App Store Connect form follows neither exactly: it counts the way JavaScript measures text length, in UTF-16 code units. For English, the other Latin-script languages, Cyrillic, Greek, and almost all Chinese, Japanese, and Korean characters, that is one unit per character, so the distinction never comes up. It does come up in scripts that write vowels as combining signs. The Hindi word किराना (grocery) reads as three syllables but is six units. A Hindi keyword field can look two-thirds full and already be at the limit, so trust the counter in App Store Connect over a text editor's.

## Which words are already indexed somewhere else?

Most wasted characters go on words like these, and Apple documents more of this than the folklore suggests.

| Where the word appears | Searchable? | What Apple documents |
|---|---|---|
| App name | Yes | Named as text relevance ("title") in the search guide |
| Subtitle | Yes | Named as text relevance in the search guide |
| Keyword field | Yes | Named as text relevance |
| Company (developer) name | Yes | App Store Connect help: your app is searchable by "app name, app subtitle, keywords, and your company name" |
| Primary and secondary category | Yes | "Your primary category and optional secondary category are indexed" |
| Promotional text | No | Apple says it "doesn't affect your app's search ranking" |
| Description | Not listed | Used for web search engine results after release; Apple asks you not to stuff it with keywords |

The company name line comes from the FAQ on Apple's [view and edit app information](https://developer.apple.com/help/app-store-connect/create-an-app-record/view-and-edit-app-information) page, and the reference page adds that you shouldn't duplicate those values in the keyword list. So if your seller name is "Northwind Labs", "northwind" is already working for you without costing a character.

## A worked example: one wasted field, one fixed

A made-up app: **Kestrel: Habit Tracker**, subtitle **Daily goals and routines**, primary category Productivity. First draft of the English (U.S.) keywords, 94 characters:

`habit tracker, habits, daily goals, routine, routines, app, streaks, reminders, best habit app`

What those characters buy:

| Term | Problem |
|---|---|
| habit tracker | Both words are already in the name |
| habits | Plural of a word already in the name |
| daily goals | Both words are already in the subtitle |
| routine, routines | Already in the subtitle, once as a plural |
| app | Generic word Apple tells you to skip |
| best habit app | Repeats habit and app; "best" is the only new word |
| 8 spaces after commas | 8 characters that do nothing |

Out of 94 characters, the new words are streaks, reminders, and best. The rewrite, 98 characters:

`streak,reminder,checklist,planner,journal,mood,water,sleep,focus,discipline,self care,todo,morning`

That is fourteen words, none of them in the name, subtitle, or category, with no spaces after commas and one form of each word. It only works if the app really does track mood, water, and sleep, because Apple's rule against irrelevant terms applies to the rewrite too.

## What does Apple not document? The ASO folklore

Plenty of keyword advice is reasonable and still unverified. These are the claims I see most, sorted by what Apple has written down.

| Claim | Status |
|---|---|
| Apple combines words from the name, subtitle, and keywords into phrases, so single words beat phrases | Folklore. Widely reported from testing, not in Apple's documentation. Apple's own example keeps "Real Estate" as a phrase. |
| Plural matching works the same in every language, including irregular plurals | Folklore. Apple's example is English (climbs, climb) and it says nothing about other languages. |
| Words in the app name count for more than words in the keyword field | Folklore. Apple lists the fields it matches, not their weights. |
| Some storefronts also search your keywords from other localizations | Folklore. Apple's [localization table](https://developer.apple.com/help/app-store-connect/reference/app-information/app-store-localizations) lists additional supported languages per storefront (the U.S. includes Spanish (Mexico), among others) but says nothing about search. |
| The description is indexed for App Store search | Not documented. Apple doesn't name it as a search factor. |
| Competitor names in keywords work if nobody notices | Against the rules. Apple names competing app names as not allowed, and reviewers do notice. |

Some of the folklore is probably right. Acting on it is still an experiment, so change one thing per version and watch the results.

## How do localizations change the keyword field?

Each localization gets its own 100-character field. App Store Connect accepts metadata in 50 languages and locales now that Apple added [eleven more in March](https://developer.apple.com/help/app-store-connect/release-notes/), including Bangla, Tamil, and Urdu. Write each one for its language. People search with their own words, and a literal translation of the English field often lands on terms nobody types.

The English variants are a good example. English (U.S.), English (U.K.), English (Canada), and English (Australia) are four localizations with four fields, and Apple's table lists a different one as the default language in each of those storefronts. Spelling and vocabulary differ (color and colour, cell phone and mobile), so the U.S. field pasted into the other three still needs a pass for each.

## When do keyword changes go live?

The keyword field sits in the version section of App Store Connect, beside the description, so an edit ships with your next approved version. There's no way to change keywords alone on a live version. So plan a small keyword change for each release; a hurried rewrite has to wait for review like any other version. Apple also notes that metadata updates can take up to 24 hours to appear in every storefront.

## Where AppMeta fits

[AppMeta](/apps/appmeta/), the Mac client for App Store Connect I wrote about [in February](/journal/native-mac-client-for-app-store-connect/), has a Keywords tab built around these rules. Its checks run on the Mac against the metadata you've already entered, with no AI involved. A Health Summary for each locale counts Issues, Wasted Chars, Unique Tokens, and Efficiency, and the tab flags words repeated across your name, subtitle, and keywords, and across locales. Remove Duplicates and Fix Overlaps clean them up. Character counts follow App Store Connect's own count, so the Hindi field from earlier shows the number Apple will. Storefront Coverage maps your localizations to 57 storefronts, which touches the same storefront folklore as the table above, so treat it as a heuristic.

All the localizations sit side by side, so you can see the gaps without opening each one. If you want suggestions, AppMeta can ask an AI provider you choose, with your own key, or Apple Intelligence on the Mac (macOS 26 on a Mac that supports it).
