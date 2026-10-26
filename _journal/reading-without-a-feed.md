---
layout: journal
slug: reading-without-a-feed
title: "Reading without a feed: a quiet year with Wikipedia"
seo:
  title: "Reading Without a Feed: A Calm Wikipedia App"
  description: "WanderWiki turns Wikipedia into calm reading without a feed, for the small windows of the day you used to fill by scrolling an infinite feed."
  keywords:
    - "wikipedia reading app"
    - "calm reading app"
    - "read without a feed"
    - "encyclopedia app iphone"
    - "anti-doomscroll app"
    - "wanderwiki"
date: 2026-02-07
last_updated: 2026-10-26
lede: "I deleted my last social-feed app in late 2024. The hardest part was rebuilding a habit of reading something, anything, in the small windows I used to fill by scrolling. I built WanderWiki mostly to give that habit somewhere to live."
quick_answer: "WanderWiki is a calm Wikipedia client built as a feed replacement. It picks For-You-style articles from interest topics the user chooses, never from behavioural tracking of taps or read time. A Today-in-History view gives each day a small editorial anchor. Articles you save stay on the phone for when there is no connection. There is no account and there are no ads."
faq:
  - q: "What is a good app to replace social media feeds?"
    a: "WanderWiki is a calm Wikipedia client built specifically to fill the small windows that used to be social-feed time. Sessions tend to be short and end when you have read enough. There is no engagement algorithm and no behavioural tracking."
  - q: "How does WanderWiki personalise without tracking me?"
    a: "During a one-screen onboarding, WanderWiki asks the user to tap interest topics (Science, History, Space, Architecture, Music, Food, and ten more), and draws For You articles from the Wikipedia categories behind those topics. What you read or skip does not decide what comes next, and nothing about your reading leaves the phone, because there is no behavioural model."
  - q: "Does WanderWiki work offline on a plane?"
    a: "Partly. Articles you save are kept on the phone, so a reading list saved before take-off is there when the Wi-Fi is not. The swipe feed and Today in History load live from Wikipedia and need a connection. For the whole encyclopedia offline, Kiwix is the right tool."
  - q: "Does WanderWiki require a Wikipedia account?"
    a: "No. WanderWiki has no account, no signup, and no Wikipedia login. It reads public Creative Commons content from Wikipedia directly, and there is no profile attached to your reading."
mentioned_apps:
  - wanderwiki
read_time: "5 min read"
excerpt: "An essay about replacing feed-based reading with a calmer Wikipedia client. How ‘For-You without behavioral tracking’ works, what saved articles give you offline, and why a Today-in-History feed is the one piece of editorial scaffolding the app keeps."
---

Sometime in late 2024 I deleted the last social feed off my phone. I'd like to say it felt clean and freeing, but I spent the next few weeks reaching for the phone, swiping to where the app used to be, finding empty space, and not knowing what to do with the hand or the attention.

Withdrawal was the easy part. The hard part was that nothing else had been trained to fit the same hole. The five-minute window between meetings, the queue at the coffee shop and the two minutes waiting for the kettle had been algorithmic-feed time for a decade. Without the feed they were just silence. Silence is fine, but a brain that's been on dopamine for ten years doesn't yet know what to do with it.

[WanderWiki](/apps/wanderwiki/) is the app in this catalogue I built most directly for that hand and that hole.

## What did I want from a reading app?

The brief I wrote for myself was small. I wanted an app that:

- Loaded fast enough to fill a thirty-second window without a loading spinner.
- Showed me something interesting on first launch without asking what I liked.
- Got *more* interesting if I told it what I liked, *without* tracking what I tapped.
- Worked on a flight without an "offline mode" hidden behind three menus.
- Didn't have a feed, or at least didn't try to be infinite.

Wikipedia was the obvious source. It is the largest collection of well-written, fact-checked, structurally consistent prose in human history, and it's available under a Creative Commons license. If I couldn't build a calm reading habit on Wikipedia, the fault would be mine.

## "For You" without tracking

Reading apps without a feed run into one problem: pure randomness gets boring quickly. Wikipedia has around seven million English articles, and [every language edition is a different encyclopedia](/journal/wikipedia-is-different-in-every-language/). A truly random tap will give you *Italian municipality of 800 people*, *American politician (1820-1888)*, and *insect taxonomy* in a row, and the user will close the app.

Most apps solve this by tracking what you read, building a profile, and using it to weight the recommendations. That works, and it's exactly what I deleted off my phone.

So can you have *For-You-style relevance* without behavioural tracking? WanderWiki's answer is yes, if you ask the user what they like instead of inferring it. In a one-screen onboarding the user taps interest topics (*Science, History, Space, Architecture, Music, Food,* sixteen in all), and the For-You feed draws its articles from the Wikipedia categories behind those declared preferences.

The user can change the topics any time. What you read or skip doesn't feed back into what For You picks, and none of it leaves the phone. There is no behavioural model. That makes it *less personalised* than a feed-based reader, but easier for the user to correct: if the recommendations go off, the only thing to fix is the list of topics you can see on screen.

## Today in History

The one piece of editorial scaffolding I did keep is the **Today in History** view. Switch to it and WanderWiki deals out the notable events that happened on the current calendar date. A treaty in 1648. A first ascent in 1953. A scientific paper in 1979. A peaceful transition of power in 1994.

It works for the same reason it always has in newspapers: content tied to a date gives the brain a small handhold. It's *this day*, in another year, the same calendar slot occupied by a different version of the world. It's the feature I get the most direct user feedback on, which is why I kept it.

## Reading offline

The other constraint I held to was that the app should be some use on a plane.

Here WanderWiki only partly delivers. A discovery deck is live by nature: Random, For You and Today in History all ask Wikipedia for something new, and on a plane there is no Wikipedia to ask. What WanderWiki does is keep what you save. Save an article on the ground and it is on the phone at cruising altitude, in the same list you use online, with no separate offline mode and no download screen.

If you want the whole encyclopedia offline, that is a different engineering problem, and [Kiwix](/alternatives/kiwix/) solves it. WanderWiki handles the small reading list you build while wandering, which is still there on a 13-hour flight, when a feed replacement is most welcome.

## What it gives up

A reading app with no feed and no behaviour tracking is not going to outcompete Twitter for attention, and it shouldn't try. WanderWiki sessions are short, two articles or sometimes three, and they end when the user has had enough. That is intentional, and session length is the one metric where I want WanderWiki to come in below the competition.

Daily active users is a noisy number for an app like this anyway. The better test is *did I just read something the algorithm would not have shown me, and did I close the app before I lost ten minutes I didn't mean to lose?*

## Where this fits in the catalogue

[WanderWiki](/apps/wanderwiki/) sits alongside a handful of other apps in this privacy-first catalogue that share one idea: the *replacement for the feed* doesn't have to be productive, but it should be calm, finite, and yours.

It's a Saturday in early February, and the internet is doing whatever the internet does. If you've been looking for something to fill the small windows that used to be filled by something worse, you could do worse than three Wikipedia articles and a quiet kitchen.

*Update, 25 October 2026:* WanderWiki has grown since this was written. It now keeps a reading streak, shown on the Profile tab and in a widget, and if you allow notifications it sends one daily reminder, which you can retime or turn off in Settings. The free tier stops at 20 articles a day; WanderWiki Plus swipes without a limit. For You still works from the topics you pick and nothing else.
