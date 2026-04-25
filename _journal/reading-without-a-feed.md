---
layout: journal
slug: reading-without-a-feed
title: "Reading without a feed: a quiet year with Wikipedia"
date: 2026-02-07
lede: "I deleted my last social-feed app in late 2024. The hardest part wasn't withdrawal. It was rebuilding a habit of reading something, anything, in the small windows that used to be filled by scrolling. WanderWiki was, more than anything else, the tool I built to give that habit somewhere to live."
read_time: "5 min read"
excerpt: "An essay about replacing feed-based reading with a calmer Wikipedia client. Why ‘For-You without behavioral tracking’ is technically possible, what offline reading enables, and why a Today-in-History feed is the one piece of editorial scaffolding the app does keep."
---

Sometime in late 2024 I deleted the last social feed off my phone. I want to say it was clean and freeing, but the honest version is that I spent the next few weeks reaching for the phone, swiping to where the app used to be, finding empty space, and not knowing what to do with the hand or the attention.

The hard part wasn't withdrawal. The hard part was that there was nothing else trained to fit the same hole. The five-minute window between meetings, the queue at the coffee shop, the two minutes waiting for the tea kettle. These had been algorithmic-feed time for a decade. Without the feed, they were just silence — which is fine, except the brain that's been on dopamine for ten years doesn't know what to do with silence yet.

[WanderWiki](/apps/wanderwiki/) is, more than anything else in this catalogue, the app I built for that hand and that hole.

## What I wanted

The brief I wrote for myself was small. I wanted an app that:

- Loaded fast enough to fill a thirty-second window without a loading spinner.
- Showed me something interesting on first launch without asking what I liked.
- Got *more* interesting if I told it what I liked, *without* tracking what I tapped.
- Worked on a flight without an "offline mode" hidden behind three menus.
- Didn't have a feed. Specifically: didn't try to be infinite.

The substrate was obvious. Wikipedia is the largest collection of well-written, fact-checked, structurally consistent prose in human history, and it's available under a Creative Commons license. If I couldn't make a calm reading habit out of Wikipedia, the problem wasn't the substrate.

## "For You" without surveillance

The unsolved problem in non-feed reading apps is that pure randomness gets boring quickly. Wikipedia has six and a half million English articles. A truly random tap will give you *Italian municipality of 800 people*, *American politician (1820-1888)*, and *insect taxonomy* in a row, and the user will close the app.

Most apps solve this by tracking what you read, building a profile, and using that profile to weight the recommendations. This works, and it's also exactly the thing I deleted off my phone.

The interesting question is whether you can have *For-You-style relevance* without behavioural tracking. The WanderWiki answer is: yes, if you ask the user what they like instead of inferring it. The app has a one-screen onboarding where the user taps interest tags — *natural history, architecture, modernist literature, geology, chess, jazz, cycling, whatever* — and the For-You feed weighs articles against those declared preferences.

The user can change the tags any time. The app does not log which articles got read versus skipped. There is no behavioural model, because there's no behavioural data. This is *less personalised* than a feed-based reader. It is also accountable to the user in a way the feed-based version cannot be — there's no hidden state to "fix" if the recommendations go off, because there isn't any hidden state.

## Today in History

The one piece of editorial scaffolding I did keep is the **Today in History** view. Every day, on launch, WanderWiki surfaces three or four notable events that happened on the current calendar date. A treaty in 1648. A first ascent in 1953. A scientific paper in 1979. A peaceful transition of power in 1994.

This works for the same reason it has always worked in newspapers: time-anchored content gives the brain a small handhold. *Today*, specifically. *This day*, in another year. The same calendar slot, occupied by a different version of the world. It's a small thing, but it's the feature I get the most direct user feedback on, and it's why I kept it.

## Offline as a first-class state

The other constraint I held to was that the app should be useful on a plane.

This sounds trivial. It is not. Most reader apps treat "offline" as a degraded mode — articles you've explicitly saved, with a clunky download flow. WanderWiki's offline mode is the same UI as online mode. Articles open instantly because they were prefetched on Wi-Fi the last time you used the app. Today-in-History works offline. The interest-based feed works offline.

The technical work for this is not glamorous — caching layers, eviction policies, content-budget management — but it's the thing that makes the app *fit the hole* on a 13-hour flight, which is the moment the value of a feed-replacement is highest.

## What it gives up

A reading app that doesn't have a feed and doesn't track behaviour is not going to outcompete Twitter for attention, and it shouldn't try. WanderWiki sessions are short. Two articles, sometimes three. The session ends when the user is satisfied, not when the app runs out of things to show. This is intentional and it is the metric I most want to be lower than the competitors' metric.

Daily active users is a noisy number for an app like this anyway. The right number is *did I just read something the algorithm would not have shown me, and did I close the app before I lost ten minutes I didn't mean to lose?* That's the bar.

## Where this fits in a privacy-first catalogue

[WanderWiki](/apps/wanderwiki/) sits next to [Driftlines](/apps/driftlines/) (literary fiction at one entry per day), [Calm 2048](/apps/calm-2048/) (a no-ads puzzle), and a small handful of other apps in this catalogue that all share a posture: the *replacement for the feed* doesn't have to be productive, but it should be calm, finite, and yours.

It's a Saturday in early February. The internet is doing whatever the internet does. If you've been looking for something to fill the small windows that used to be filled by something worse, you could do worse than three Wikipedia articles and a quiet kitchen.
