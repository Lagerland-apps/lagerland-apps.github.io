---
layout: app
slug: driftlines
name: "Driftlines"
tagline: "Daily prose from a quiet life."
quick_answer: "Driftlines is a quiet daily reading app for iPhone, iPad, Mac, and Apple Vision Pro. Each day, one short piece of first-person prose arrives from a fictional life unfolding in real time. The narrator is a woman in her late thirties living somewhere on the coast; her life drifts forward across months of the calendar. Rare quiet choice moments arrive roughly every ten to fifteen entries and gently bend the texture of what comes next. No feeds, streaks, or notifications. One-time $59.99 — cheaper than a year of one literary Substack. No ads, no trackers, no account."
category: books
platforms: ["iOS"]
status: live

app_store_url: "https://apps.apple.com/app/id6758112876"

price:
  model: one-time
  value: "One-time $59.99"
schema_price: "59.99"

# Plans footnote answers the two biggest pre-purchase objections next to the price:
# why $59.99 makes sense vs subscription literary publications, and the Apple-refund flow.
plans_footnote: "$59.99 once. No subscription, no auto-renew. For context: a year of one literary Substack runs $50–100, a hardcover novel is $25–35, and a New Yorker print subscription is $129. Driftlines unlocks every current and future entry for as long as the story keeps drifting. Refunds via Apple's standard App Store flow if the first entries don't land for you."

icon: "/assets/icons/driftlines.png"
og_image: "/assets/og/driftlines.png"

# CreativeWorkSeries / Book schema — Driftlines is a serialised literary work,
# not only a piece of software. The layout emits an additional Book/Series
# JSON-LD block when this is present so the entity is recognised correctly.
creative_work:
  type: "Book"
  also_type: "CreativeWorkSeries"
  name: "Driftlines"
  genre: "Serialised literary fiction"
  in_language: "en"
  author_credit: "Driftlines (anonymous, written under the work's own name)"
  publisher: "Lagerland Apps"
  date_published: "2026-01-26"
  number_of_episodes: "ongoing"
  abstract: "A serialised first-person narrative delivered as one short prose entry per day. The narrator is a woman in her late thirties living somewhere on the coast; her life unfolds across months of the user's calendar. Rare quiet choice moments — roughly every ten to fifteen entries — gently shift the texture of what comes next without branching the arc. Written week-by-week by a human writer."

seo:
  title: "Driftlines: Daily Literary Fiction, One Entry a Day"
  description: "One short piece of first-person prose each day from a fictional life unfolding in real time. Slow reading for iPhone, iPad, Mac & Vision Pro. $59.99 once."
  keywords:
    - slow reading app
    - daily literary fiction app
    - serialised fiction iPhone
    - calm reading app no notifications
    - anti-doomscroll app
    - sloweb app
    - finite app no engagement loop
    - daily prose app
    - first-person fiction app
    - literary app one-time purchase
    - book app for slow readers
    - The Marginalian app alternative
    - daily reading without streaks
    - private reading app Apple Vision Pro
    - calm fiction app iPhone
    - narrative reading ritual
    - mindful reading app
    - epistolary fiction app
    - diaristic prose app
    - quiet reading habit app

hero:
  pre_headline: "Daily literary prose for iPhone, iPad, Mac & Apple Vision Pro."
  headline: "One life. One entry per day."
  subheadline: "Driftlines is a quiet reading experience. Each day, one short piece of first-person prose arrives from a fictional life unfolding in real time. The narrator is a woman in her late thirties living somewhere on the coast — her life drifts forward across months of your calendar. Memories shift, places change, and a story builds without you noticing."
  cta_label: "Get Driftlines"
  alt: "Driftlines — today's prose entry on iPhone, in a calm full-screen reading view"

who_for:
  - "You miss the feeling of finding a physical notebook and reading a few pages before bed"
  - "You're trying to rebuild a calm reading habit away from feeds, notifications, and streaks"
  - "You love typography-forward design and slow, first-person prose"
  - "You want a daily reading ritual that doesn't demand anything back from you"
  - "You read Robin Sloan, The Marginalian, *Year of the Meteor*, or the slow-web movement"
  - "You're willing to pay once for something quiet that respects your attention"

who_not_for:
  - "You want audiobooks, full-length novels, or to binge-read in one sitting"
  - "You want social reading, book clubs, or shared highlights"
  - "You want daily devotional, Bible verse, or Stoic-quote content specifically"
  - "You want AI-generated text — Driftlines is human-written, week by week"

# Reframed away from "alternative to journaling apps" (the old list was misaligned
# — Stoic, Daily Stoic, Five Minute Journal, Day One are journaling, not reading).
# These are the actual lineage: peer literary products and slow-web traditions.
alternatives_to:
  - "The Marginalian (Maria Popova)"
  - "Daily Science Fiction"
  - "Robin Sloan's *Year of the Meteor*"
  - "Slow-web / sloweb movement"
  - "Literary Substack subscriptions"

value_points:
  - title: "One entry per day, in real time"
    description: "A single piece of first-person prose arrives each morning on the user's day, in the user's time zone. Read it in a few minutes. Let it settle. The next entry waits a full day."
  - title: "A life unfolds slowly"
    description: "The narrator is a woman in her late thirties living somewhere on the coast. Over weeks and months her memories shift, places change, and the writing style itself evolves as the character changes. Nothing is explained — it simply unfolds."
  - title: "Rare quiet choice moments"
    description: "Roughly every ten to fifteen entries, Driftlines offers a small choice. She's on a train and notices someone she might say hello to. Or doesn't. The choice doesn't change the arc — it changes the texture of the next several entries. Reader influence is more like weather than a steering wheel."
  - title: "Nothing demands your attention"
    description: "No push notifications, no streaks, no feeds. Miss a day, a week, a year — the entries wait. There is no fast-forward; the relationship to time is part of the form."

features:
  - title: "Prose that breathes — written by a human, week by week"
    description: "Every entry is written in first person from a single fictional perspective. The voice is intimate, imperfect, human. Entries are written week-by-week — sometimes only a few days ahead of the readers. No LLM is in the pipeline; the imperfection is intentional."
  - title: "A narrative that drifts, not branches"
    description: "Themes return weeks later. Places reappear in different light. The writing style itself shifts as the character changes. Nothing is explained — it simply unfolds. There are no inventory items, skill checks, or game-state. The substrate is prose, not mechanic."
  - title: "Designed for slow reading"
    description: "Typography, spacing, and layout are crafted for long-form text on iPhone, iPad, Mac, and Apple Vision Pro. No UI clutter. No sidebars. Just words on a calm surface, like reading a printed page in a quiet room."
  - title: "Rare moments of influence"
    description: "Roughly every ten to fifteen entries, Driftlines offers a quiet choice. Your intervention shapes the texture of the next several entries — but the effect is delayed and subtle. You're a reader who sometimes leaves a mark. Optional token packs grant additional choice moments for readers who want to shape the narrative more aggressively."
  - title: "No app mechanics. No metrics. No bid for your time."
    description: "No achievement badges, no engagement loops, no social layer, no leaderboard, no public sharing. Driftlines is deliberately the opposite of what apps are supposed to be. It cannot win at engagement because beating engagement isn't the point."

screenshots:
  - "/assets/screenshots/driftlines/1.png"
  - "/assets/screenshots/driftlines/2.png"
  - "/assets/screenshots/driftlines/3.png"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no trackers, no analytics SDKs"
    - "No social features or public sharing"
    - "Entries delivered and stored locally — optional iCloud sync, end-to-end encrypted by Apple"
    - "No account required — no email, no Apple ID, no sign-up flow"

# Link to the editorial backstory journal post — currently the closest thing
# to a free taste of the writing voice that produces Driftlines entries.
related_journal:
  slug: literary-software-in-the-spring
  anchor: "Literary software, in the spring — the studio note on Driftlines"

faq:
  - q: "What is Driftlines?"
    a: "Driftlines is a piece of literary software for iPhone, iPad, Mac, and Apple Vision Pro — a serialised first-person narrative delivered as one short prose entry per day. The narrator is a woman in her late thirties living somewhere on the coast; her life unfolds across months of the reader's calendar. Rare quiet choice moments — roughly every ten to fifteen entries — gently shift the texture of what comes next."
  - q: "Is Driftlines AI-generated?"
    a: "No. Driftlines is written by a human writer, week by week — sometimes only a few days ahead of the readers. There is no LLM in the pipeline and no AI generation step. The voice is intentionally imperfect because that is what real diaristic prose sounds like."
  - q: "Who writes Driftlines?"
    a: "Driftlines is published anonymously, under the work's own name. The author is human, writes in real time week by week, and chose not to attach a personal byline to the work — the voice in the entries is the only signature the writer wants. The narrator is a fictional character; the writer is real."
  - q: "Do I write anything in Driftlines?"
    a: "No. Driftlines is a reading experience. Each entry is written for you. Your role is to read, reflect, and occasionally — once every ten or fifteen entries — make a small subtle choice that shifts the texture of the next several entries."
  - q: "How does the story influence mechanic work?"
    a: "Roughly every ten to fifteen entries, Driftlines offers a small quiet choice. She's on a train and notices someone she might say hello to. Or doesn't. The choice doesn't branch the arc — it changes the texture of the next several entries. Optional token packs grant additional choice moments for readers who want more influence."
  - q: "Is Driftlines a subscription?"
    a: "No. Driftlines is a one-time $59.99 purchase that unlocks every current and future entry. Optional token packs grant additional influence moments. For context: a year of one literary Substack runs $50–100, a hardcover novel is $25–35, and a New Yorker print subscription is $129. Driftlines is priced like a book, not like software."
  - q: "Can I binge-read all the entries at once?"
    a: "No. Entries arrive at the rate of one per day in the user's time zone and are structurally tied to the calendar. If you skip a week, a month, or a year, the entries wait for you. There is no fast-forward — the relationship to time is part of the form."
  - q: "Does Driftlines have notifications or streaks?"
    a: "No. There are no push notifications, no engagement streaks, no read-count badges, no daily nag. Open the app when you want to read. Skip when you don't. The app makes no bid for your time beyond the few minutes the entry takes to read."
  - q: "What platforms does Driftlines support?"
    a: "Driftlines runs natively on iPhone, iPad, Mac (Apple Silicon), and Apple Vision Pro. Typography, spacing, and layout are crafted for each platform's reading surface."
  - q: "Does Driftlines collect any data?"
    a: "No. Driftlines collects no data, has no trackers, has no analytics SDKs, and requires no account. Your reading stays completely private. Optional iCloud sync between your own Apple devices is end-to-end encrypted by Apple."
  - q: "How is Driftlines different from The Marginalian, Daily Science Fiction, or a literary Substack?"
    a: "The Marginalian is curated essays about other people's work; Driftlines is original serial fiction. Daily Science Fiction is a free newsletter with one-shot stories from different authors; Driftlines is one continuous serial from one narrator. Literary Substacks are subscription email newsletters; Driftlines is a one-time-purchase app with no email, no inbox clutter, and a contemplative reading surface designed for the platform."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/driftlines/support/"

release:
  first_release: "2026-01-26"
  last_updated: "2026-02-25"

ratings:
  value: "5.0"
  count: 2
  last_synced: "2026-04-15"
  display_label: "Early access"
---
Driftlines is a quiet daily reading experience for iPhone, iPad, Mac, and Apple Vision Pro — a serialised first-person narrative delivered as one short prose entry per day. The narrator is a woman in her late thirties living somewhere on the coast; her life drifts forward across months of the reader's calendar as memories shift, places change, and the writing style itself evolves. Rare quiet choice moments — roughly every ten to fifteen entries — let the reader gently shape the texture of what comes next without branching the arc. Driftlines is written by a human writer, week by week, sometimes only a few days ahead of readers; no LLM is in the pipeline. There are no notifications, no streaks, no feeds, no read-count badges, and no bid for the reader's time beyond the few minutes each entry takes. One-time $59.99 unlocks every current and future entry — priced like a book, not like software. No ads, no trackers, no account.
