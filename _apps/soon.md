---
layout: app
slug: soon
name: "Soon."
tagline: "Countdowns worth waiting for."
quick_answer: "Soon. is a countdown and planner app for iPhone. It turns trips, weddings, birthdays, anniversaries, and milestones into countdowns with full-bleed photo backgrounds, live destination weather, Plan Mode checklists, and widgets for the Home Screen, Lock Screen, and StandBy. It is free, with Premium from {P_MONTHLY}/month or {P_LIFETIME} lifetime, and has no ads, no tracking, and no account."
category: lifestyle
status: live

app_store_url: "https://apps.apple.com/app/id6757280643"

price:
  model: freemium

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Refunds are handled by Apple through the standard App Store refund flow. The lifetime tier is a one-time purchase and does not auto-renew."

# Free / Monthly / Annual / Lifetime shows the full upgrade ladder. The
# lifetime tier costs roughly 8 months of monthly Premium, so readers should
# see the breakeven math at a glance.
plans:
  - name: "Free"
    price: "$0"
    summary: "Five events, one pinned widget, and three themes, with no time limit."
    features:
      - "5 events at a time"
      - "1 pinned widget (Home / Lock / StandBy)"
      - "3 themes (Classic, Soft, Midnight)"
      - "iOS Calendar import"
      - "Memories (anniversaries return automatically)"
      - "Reflection mode"
      - "39 languages"
  - name: "Premium · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "All Premium features, billed monthly. Cancel anytime."
    features:
      - "Unlimited events"
      - "All widget styles (small / medium / large / ring / minimal / timeline)"
      - "10 premium themes"
      - "Live destination weather"
      - "Daily notes that change as the date approaches"
      - "Recurring events"
      - "Event notifications"
      - "7-day free trial · cancel anytime"
  - name: "Premium · Annual"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "The same Premium features, billed once a year. Costs roughly {YEARLY_MONTHS} months of monthly Premium."
    features:
      - "Everything in Premium · Monthly"
      - "~{SAVE_YEARLY}% cheaper than paying monthly all year"
      - "7-day free trial · cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All Premium features for roughly {LIFETIME_MONTHS} months of monthly Premium, paid once."
    features:
      - "Everything in Premium · Annual"
      - "One-time purchase, no renewal"
      - "Restores on every iPhone signed in with the same Apple ID"
      - "Family Sharing supported"

icon: "/assets/icons/soon.png"
og_image: "/assets/og/soon.png"

seo:
  title: "Countdown App for iPhone: Trips, Weddings & More | Soon."
  description: "Countdown & planner app for iPhone for trips, weddings, and birthdays. Photo widgets, destination weather, checklists. Free, Premium {P_MONTHLY}/mo."
  keywords:
    - countdown app iphone
    - event countdown planner
    - trip countdown app
    - wedding countdown app
    - birthday countdown app
    - days until app
    - lock screen countdown widget
    - home screen countdown widget
    - standby countdown widget
    - vacation planner iphone
    - trip checklist app
    - event countdown with weather
    - photo countdown app
    - countdown and planner app
    - pregnancy due date countdown
    - retirement countdown app
    - milestone tracker iphone
    - beautiful countdown widget

hero:
  pre_headline: "Countdown & planner app for iPhone"
  headline: "Some days you can't wait for."
  subheadline: "Soon. is a countdown app for iPhone. Each trip, wedding, birthday, or milestone gets its own countdown with a full-bleed photo, live destination weather, a Plan Mode checklist, and widgets for the Home Screen, Lock Screen, and StandBy. Free, with Premium from {P_MONTHLY}/month. No ads, tracking, or account."
  cta_label: "Download Free"
  alt: "Soon. full-bleed trip countdown on iPhone with photo background and live destination weather"

who_for:
  - "You're planning a trip, wedding, birthday, graduation, or other milestone and want to see it every day"
  - "You like iOS widgets and want countdowns on your Home Screen, Lock Screen, and StandBy"
  - "You want packing lists and timelines that show up on their own as the date gets closer"
  - "You want live weather for your destination as the trip gets closer"
  - "You want your countdowns on your phone without handing location data to advertisers"

who_not_for:
  - "You keep widgets off your Home Screen on principle"
  - "A plain calendar reminder is enough and you don't want photos and daily notes around it"
  - "You want a structured GTD task manager with projects and tags"

# Founder block: Experience / Authority signal. Soon. is a rebuild of TheWait,
# shipped by one person in Finland. The rebuild story is the strongest narrative
# asset on this page and was previously waived.
founder:
  entity_type: "Organization"
  overline: "Why I built this"
  heading: "Rebuilt from TheWait by the person who shipped it."
  name: "Lagerland Apps"
  role: "Independent Apple developer · Finland · one-person studio since 2025"
  location: "Finland"
  photo: "/assets/icons/lagerland-mark.png"
  bio: "I shipped TheWait years ago as a single-purpose countdown. People kept asking for things its architecture couldn't support: Lock Screen widgets, StandBy, weather forecasts, checklists. Soon. is the full rewrite, with new code, a new icon, and a new name, written by the same person. There is no team. One developer in Finland designs, codes, and answers support email for every Lagerland app, this one included. If something doesn't work, email me directly and I'll fix it."
  support_email: "lagerland.apps@proton.me"
  response_time: "I reply to support emails personally, usually within a day."
  signals:
    - "Original author of TheWait. Soon. is a ground-up rebuild, not a rebrand"
    - "Shipped {APP_COUNT} privacy-first Apple apps under Lagerland since 2025"
    - "Events stay on your iPhone, and weather requests use approximate location only"
    - "Localised into 39 languages, including right-to-left (Arabic, Hebrew) and CJK (Japanese, Korean, Chinese)"

alternatives_to:
  - "Countdowns (Apalon)"
  - "Dreamdays"
  - "Days Matter"
  - "Countdown Star"
  - "Wedding Happy"
  - "TheWait (former name of Soon.)"

value_points:
  - title: "Countdowns with a photo and a forecast"
    description: "Each event gets a full-bleed photo, live weather from the destination, and daily notes that change as the date gets closer."
  - title: "A plan comes with every countdown"
    description: "Each countdown has its own timeline and checklist. Book transport 30 days out, pack three days before, and arrive ready."
  - title: "Widgets for every screen"
    description: "Home Screen, Lock Screen, and StandBy widgets in every iOS size: small, medium, large, ring, minimal, and timeline."
  - title: "Private by default"
    description: "Soon. has no ads, no tracking, and no account. Your events stay on your device for as long as you keep them."

features:
  - title: "Full-bleed photo countdowns"
    description: "Pin a photo to an event and it fills the screen behind the countdown, so you see the place or the people along with the number of days."
  - title: "Smart Plan Mode"
    description: "Each countdown comes with a timeline and checklist for its event type. Trips get packing lists and transport reminders, and weddings get their own schedule. Each task shows up on the day it's due."
  - title: "Live weather"
    description: "See the forecast for your destination as the date approaches, so you know what to pack. Premium only."
  - title: "Natural language search"
    description: "Type \"trips in July,\" \"birthdays this month,\" or \"anniversaries in 2027.\" Soon. finds the matching events in seconds."
  - title: "Memories that return"
    description: "When a countdown ends, it becomes a memory, and Soon. brings it back on every anniversary."
  - title: "Calendar sync"
    description: "Turn any iOS Calendar event into a countdown with one tap."

# Methodology: Plan Mode is the page's strongest information-gain claim and
# was previously stated in a single sentence. Exposing the rule earns the E-E-A-T
# Expertise signal and gives Google something to extract for AI Overviews.
how_it_works:
  intro: "Plan Mode builds the checklist and schedules it. This is what happens between creating an event and the day itself."
  steps:
    - title: "You pick the event type"
      detail: "Add an event and choose a type: Trip, Wedding, Birthday, Pregnancy, Graduation, Move, Concert, Anniversary, or Custom. Each type loads its own checklist template. Custom events start blank."
    - title: "Soon. schedules the checklist backward from the date"
      detail: "Each template is a list of tasks anchored to the event date (T-90, T-30, T-14, T-3, T-1). When you save the event, Soon. places every task on its own calendar day, counted back from the date. You see the checklist, and the schedule runs underneath."
    - title: "Reminders fire on the day each task is due"
      detail: "If you turn on event notifications (Premium), Soon. sends one notification per task on its scheduled day. It never sends a daily nag or a bundle. A trip 30 days away gets a single 'book transport' nudge at T-30, not 30 daily reminders."
    - title: "Weather pulls in as the date approaches"
      detail: "Premium adds destination weather. Soon. fetches the forecast for the location you set through Apple WeatherKit. The request sends only a place name or approximate coordinates, never your precise location. The forecast shows on the countdown card from T-10 onward, when it starts to be useful."
    - title: "Daily notes appear in the final week"
      detail: "Premium adds short daily notes that change between T-7 and T-0. Wedding events get different copy from trips. The notes are written once and shipped with the app, with no AI generation and no surveillance."
    - title: "The countdown becomes a memory"
      detail: "When the date passes, the event turns into a memory. On the same day next year, and every year after, Soon. shows it on your Home Screen again as a recurring anniversary countdown that needs no upkeep."

# Plan Mode template gallery: the page's strongest information-gain asset.
# Shows specific T-anchored checklist examples for the most common event
# types, exactly as they appear inside the app.
example_insights:
  anchor: "templates"
  overline: "Inside Plan Mode"
  heading: "Sample Plan Mode checklists."
  intro: "A sample of the timelines that ship with Soon. Each template is anchored to your event date, and tasks appear on their scheduled day, not all at once."
  cards:
    - tag: "Trip · 30-day template"
      headline: "Trip to Lisbon, 28 days out"
      body: "T-30: Book flights · T-21: Reserve accommodation · T-14: Buy travel adapter, check passport expiry · T-10: Destination weather appears on widget · T-7: Refill any prescriptions · T-3: Pack (with weather-aware suggestions) · T-1: Charge devices, check-in opens."
    - tag: "Wedding · 90-day template"
      headline: "Wedding, 12 weeks out"
      body: "T-90: Confirm vendor list · T-60: Send save-the-dates · T-45: Final dress / suit fitting · T-30: Wedding band rehearsal · T-21: Confirm headcount with caterer · T-14: Pack ceremony kit (rings, vows, emergency sewing kit) · T-7: Final venue walkthrough · T-1: Day-of timeline finalised."
    - tag: "Pregnancy · 40-week template"
      headline: "Pregnancy due date, week 36"
      body: "Week 28: Glucose screening reminder · Week 32: Pack hospital bag prompt · Week 35: Install car seat · Week 36: Confirm birth plan, pack snacks · Week 38: Finalize contact list · Week 39: Last full-day prep · Week 40: Daily check-in notes. Trimester summary returns each year as a memory."
    - tag: "Birthday · 14-day template"
      headline: "Birthday party, 14 days out"
      body: "T-14: Set guest list · T-10: Send invites · T-7: Book venue or confirm at home · T-5: Order cake · T-3: Buy decorations · T-1: Charge speakers, prep playlist · T-0: Photo backdrop ready. Returns as an anniversary memory next year."
    - tag: "Graduation · 21-day template"
      headline: "Graduation day, 3 weeks out"
      body: "T-21: Confirm ceremony seating · T-14: Reserve restaurant · T-10: Book accommodation for family · T-7: Order gown / cap if not provided · T-3: Frame for diploma · T-1: Charge camera, plan the photo spots."
    - tag: "Move · 45-day template"
      headline: "Moving day, 6 weeks out"
      body: "T-45: Compare movers · T-30: Book mover · T-21: Begin packing non-essentials · T-14: File change-of-address · T-7: Pack essentials box · T-3: Confirm parking at both ends · T-1: Defrost freezer, pack overnight bag."

# Side-by-side comparison: replaces the templated 'Branded comparisons' card grid
# with actual feature deltas. Where a row is genuinely uncertain about a competitor
# (apps change their stack), the cell reads 'Not stated' rather than guessing.
comparison_table:
  intro: "Each row is something people check before choosing a countdown app. Days Matter and Countdowns (Apalon) are the largest competitors on the App Store, and Wedding Happy is the dedicated wedding planner most likely to show up in the same searches. Checked against each app's public App Store listing and landing page on 2026-05-13."
  competitors: ["Soon.", "Days Matter", "Countdowns (Apalon)", "Wedding Happy"]
  rows:
    - feature: "Event-type-aware checklist templates (Plan Mode)"
      values: ["Yes: Trip, Wedding, Birthday, Pregnancy, Graduation, Move, Concert", "No, generic events only", "No, generic events only", "Yes, wedding only"]
    - feature: "Live destination weather on the countdown"
      values: ["Yes (Premium, via Apple WeatherKit)", "No", "No", "No"]
    - feature: "StandBy widgets (iOS 17+)"
      values: ["Yes", "Not stated", "Not stated", "No"]
    - feature: "Lock Screen widgets"
      values: ["Yes", "Yes", "Yes", "Limited"]
    - feature: "No ads, ever"
      values: ["None on any tier", "Ads in free tier", "Ads in free tier", "Free with banners"]
    - feature: "No account required"
      values: ["No account ever", "Optional account", "Optional account", "Account required"]
    - feature: "Data storage"
      values: ["On-device only", "Cloud sync available", "Cloud sync available", "Cloud-based"]
    - feature: "One-time lifetime price"
      values: ["{P_LIFETIME} lifetime", "No (subscription only)", "No (subscription only)", "No"]
    - feature: "Localised languages"
      values: ["39", "~30", "~20", "1 (English)"]
    - feature: "Memories return on anniversaries"
      values: ["Yes, automatically", "No", "Manual recurring event", "N/A"]
  footnote: "Competitor positioning summarised from each app's public App Store listing and landing page on 2026-05-13. Prices and features change often, so check them before switching."

screenshots:
  - src: "/assets/screenshots/soon/1.webp"
    alt: "Soon home screen showing a large countdown card for a summer vacation"
  - src: "/assets/screenshots/soon/2.webp"
    alt: "Soon moments list of countdowns for trips, exams, birthdays and weddings"
  - src: "/assets/screenshots/soon/3.webp"
    alt: "Soon Plan tab listing events happening soon"
  - src: "/assets/screenshots/soon/4.webp"
    alt: "Soon event detail for a trip with days until and plan actions"
  - src: "/assets/screenshots/soon/5.webp"
    alt: "Soon trip plan with a timeline and a packing checklist"
  - src: "/assets/screenshots/soon/6.webp"
    alt: "Soon wedding countdown card with a plan"
  - src: "/assets/screenshots/soon/7.webp"
    alt: "Soon vacation countdown card with a plan"
  - src: "/assets/screenshots/soon/8.webp"
    alt: "Soon birthday countdown card with a plan"
  - src: "/assets/screenshots/soon/9.webp"
    alt: "Soon memory card showing a year since a past event"
  - src: "/assets/screenshots/soon/10.webp"
    alt: "Soon widget gallery with countdown widgets in several sizes"
  - src: "/assets/screenshots/soon/11.webp"
    alt: "Soon color themes picker"
  - src: "/assets/screenshots/soon/12.webp"
    alt: "Soon information widgets with a calendar and event list"
  - src: "/assets/screenshots/soon/13.webp"
    alt: "Soon extra-large countdown widget"

privacy:
  data_collection: "minimal"
  tracking: false
  account_required: false
  notes:
    - "No ads, no trackers, no account"
    - "Event data stored locally on your device"
    - "Photos accessed only through Apple's system picker, and only the ones you pick"
    - "Weather requests use approximate location or a place name only"
    - "39 languages supported"

faq:
  - q: "What is Soon.?"
    a: "Soon. is a countdown and planner app for iPhone. It turns trips, weddings, birthdays, anniversaries, and milestones into countdowns with photo backgrounds, live weather, checklists, and widgets for every screen."
  - q: "What can I count down to?"
    a: "Anything with a date: trips, weddings, birthdays, anniversaries, graduations, due dates, retirement, moves, concerts, holidays. There's no limit on event types, and the checklist changes with the kind of event."
  - q: "How is Soon. different from TheWait?"
    a: "Soon. is the complete rebuild of TheWait, with a new name, icon, and home. It adds Plan Mode with timelines and checklists, natural language search, StandBy widgets, calendar sync, memories that return on anniversaries, and 39 languages. If you used TheWait, everything carries over."
  - q: "Is Soon. free?"
    a: "Yes. The free tier includes 5 events, one pinned widget, three themes, calendar import, memories, and reflection mode. Premium unlocks unlimited events, all widget styles, ten premium themes, live weather, daily notes, recurring events, and event notifications."
  - q: "What does Premium cost?"
    a: "{P_MONTHLY} per month, {P_YEARLY} per year, or {P_LIFETIME} once for lifetime access. Premium comes with a seven-day free trial and you can cancel anytime. Prices in USD; the App Store shows your local currency at checkout."
  - q: "Which widgets does Soon. support?"
    a: "Home Screen, Lock Screen, and StandBy widgets in every iOS size, in small, medium, large, ring, minimal, and timeline styles. Your main countdown can sit on every screen you already use."
  - q: "Does Soon. track me or collect data?"
    a: "No. Soon. has no ads, no trackers, and no account requirement. Your events stay on your device. Weather requests send only an approximate location or a place name, never your precise location."
  - q: "What languages does Soon. support?"
    a: "39 languages, including Japanese, Chinese, Arabic, Hebrew, Korean, and all major European languages. Arabic and Hebrew get a native right-to-left layout."
  - q: "What happens to my events if I switch iPhones?"
    a: "Restore from iCloud Backup. Soon. stores events locally, and that data is included in your standard iPhone iCloud Backup, so a new iPhone set up from the backup gets your countdowns, photos, and Plan Mode progress. There is no Soon. account, so there's no separate login to recover."
  - q: "Does Soon. support Apple Watch, iPad, or Mac?"
    a: "Soon. is iPhone-only today. There is no Apple Watch, iPad, or Mac version. If you need cross-device sync now, Apple's own Calendar app works with Soon. through the calendar import feature."
  - q: "Can I count up from a past date too?"
    a: "Yes. An event whose date has passed turns into a memory automatically. Soon. counts the days, weeks, or years since it happened and brings it back on every anniversary. The widgets that showed the countdown switch to a count-up after the date."
  - q: "How do event notifications work?"
    a: "Premium adds one notification per Plan Mode task, sent on the day that task is scheduled (not the day you created the event). For a trip 30 days out, you get a single 'book transport' reminder at T-30 instead of 30 daily nags. You can turn notifications off per event or globally in Settings. The free tier never sends notifications."
  - q: "Where does the destination weather forecast come from?"
    a: "Apple's WeatherKit, the same data source the iOS Weather app uses. Soon. sends the destination's place name or approximate coordinates (never your precise location) and shows the forecast from roughly T-10 onward, when a 10-day forecast covers the date. Weather is Premium-only."
  - q: "Can I share an event with someone else?"
    a: "Not inside Soon. Events live only on your iPhone, by design. You can share a screenshot of any countdown with the standard iOS share sheet, but live shared countdowns are out of scope. If two people want the same wedding countdown, each installs Soon. and creates the event."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/soon/support/"

release:
  first_release: "2026-01-01"
  last_updated: "2026-04-13"

ratings:
  value: "5.0"
  count: 3
  last_synced: "2026-08-01"
# Surface the Plan Mode methodology post directly on the app page:
# information-gain content tied back to the page's strongest feature claim.
related_journal:
  slug: how-plan-mode-builds-a-checklist
  anchor: "How Plan Mode builds a wedding (or trip, or pregnancy) checklist"

# Render the markdown body as a visible "About Soon." section. The body
# contains contextual in-body internal links to the methodology,
# templates, comparison, and privacy sections. SearchPilot data:
# in-body contextual links return 5 to 25% organic uplift.
show_body: true
about_heading: "What Soon. does: countdowns, planning, widgets, weather"
last_updated: 2026-10-26
---
Soon. is a [countdown and planner app for iPhone](#features) and the complete rebuild of TheWait. Trips, weddings, birthdays, anniversaries, graduations, due dates, and personal milestones each get a full-bleed countdown with a photo you pin yourself, live weather for the destination, and daily notes that change as the date approaches.

Every countdown comes with [Plan Mode](#how-it-works), a timeline and checklist made for the event type. A trip gets packing, transport, and check-in reminders, a wedding gets vendor and rehearsal milestones, and a pregnancy gets prompts anchored to each trimester. Tasks appear on the day each one is due, scheduled backward from the event date, so you don't get the whole list at once. [The Plan Mode templates](#templates) show what a trip, wedding, birthday, or pregnancy timeline looks like inside the app.

Soon. has [widgets](#features) for the Home Screen, Lock Screen, and StandBy in every size: small, medium, large, ring, minimal, and timeline. Natural language search lets you type "trips in July," "birthdays this month," or "anniversaries in 2027" and get the matching events. iOS Calendar sync turns any existing calendar event into a countdown with one tap, and memories come back on every anniversary automatically. The app is localised into 39 languages, including right-to-left (Arabic, Hebrew) and CJK (Japanese, Korean, Chinese).

Soon. has [no ads, no tracking, and no account](/apps/soon/privacy/). Events stay on your iPhone instead of on a server behind a login, and weather requests use only an approximate location or a place name. It is a [privacy-first alternative to](/alternatives/) Countdowns (Apalon), Dreamdays, Days Matter, and Wedding Happy; [the side-by-side comparison](#compare-heading-soon) lists the feature differences.

The free tier has 5 events, one pinned widget, three themes, calendar import, memories, and reflection mode. Premium adds unlimited events, all widget styles, ten premium themes, live weather, daily notes, recurring events, and event notifications for {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} lifetime, with a seven-day free trial and no auto-renew surprises. Soon. is published by Lagerland Apps, an independent Apple developer in Finland.
