---
layout: app
slug: aftershift
name: "AfterShift"
tagline: "Sleep and recovery tracking built around your shift roster."
quick_answer: "AfterShift is an iPhone sleep and recovery app for shift workers: nurses, paramedics, firefighters, factory and logistics crews, and anyone on nights, rotating shifts, or on-call. It measures sleep shift to shift instead of midnight to midnight, imports sleep from Apple Health with naps included, fills your roster 8 weeks ahead from a repeating rotation, and times wind-down, caffeine cut-off, and nap reminders to your next shift. All of that is free. Premium ({P_MONTHLY}/mo or {P_YEARLY}/yr, each starting with a {TRIAL}, or {P_LIFETIME} once) adds Readiness, the Sleep Score, the Shift Recovery Score, and trends. There is no account and no ads, and your data is never sent to a server."
category: health
status: live

app_store_url: "https://apps.apple.com/app/id6757163182"

price:
  model: freemium

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew. Monthly, Annual, and Lifetime all support Family Sharing."

plans:
  - name: "Free"
    price: "$0"
    summary: "Your roster, your sleep, and reminders timed to your next shift. Free for good."
    features:
      - "Repeating rotations that fill your roster 8 weeks ahead"
      - "Sleep imported from Apple Health, naps included"
      - "Sleep Timing, Sleep Stages, and the sleep-debt trend"
      - "\"Do this now\" steps and 21 techniques with timers"
      - "Shift-timed reminders, a Lock Screen countdown, and 4 widgets"
      - "Calendar import from 1 calendar, 14 days ahead"
  - name: "Premium · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Full Premium, billed monthly. Cancel anytime."
    features:
      - "Readiness, Sleep Score, and Shift Recovery Score"
      - "Sleep Continuity, nap and caffeine detail, and Trends"
      - "Automatic sync from several calendars, with overtime tracking"
      - "A preview of what a shift change does to your readiness"
      - "Explanations written on-device by Apple Intelligence (iOS 26+ on a supported iPhone)"
      - "A PDF report for your clinician and all 14 color themes"
      - "Cancel anytime"
  - name: "Premium · Annual"
    price: "{P_YEARLY}/yr"
    kind: yearly
    summary: "Same Premium features, billed once a year. ~{SAVE_YEARLY}% cheaper than paying monthly."
    features:
      - "Everything in Premium · Monthly"
      - "~{SAVE_YEARLY}% cheaper than monthly over a year"
      - "Cancel anytime"
    highlight: true
  - name: "Lifetime"
    price: "{P_LIFETIME} once"
    kind: lifetime
    summary: "All Premium features for one payment."
    features:
      - "Everything in Premium · Annual"
      - "One-time purchase, no renewal"
      - "Restores on any iPhone signed in with the same Apple ID"
      - "Family Sharing included"

icon: "/assets/icons/aftershift.png"
og_image: "/assets/og/aftershift.png"

seo:
  title: "AfterShift: Sleep & Recovery App for Shift Workers"
  description: "Sleep and recovery measured shift to shift for nurses, paramedics, and night staff. Your roster fills 8 weeks ahead. Free, with Premium."
  keywords:
    - shift work sleep app
    - sleep tracker for shift workers
    - night shift recovery app
    - nurse sleep app
    - nap tracker shift work
    - rotating schedule sleep app
    - first responder sleep app
    - night shift sleep tracker
    - shift recovery score
    - caffeine timing shift work
    - on-call sleep recovery
    - shift work roster app
    - DuPont schedule sleep
    - 2-2-3 rotation sleep
    - 4 on 4 off sleep app
    - 12 hour shift sleep tracker
    - paramedic sleep tracker
    - firefighter sleep app
    - sleep debt tracker shift work

hero:
  pre_headline: "For nurses, paramedics, firefighters, and anyone on nights, rotations, or on-call"
  headline: "Sleep and recovery, measured from one shift to the next."
  secondary: "Sleep imports itself from Apple Health, naps included, and counts toward the window between your last shift and your next."
  subheadline: "Set your rotation once and AfterShift fills the next 8 weeks of your roster. Wind-down, caffeine cut-off, and nap reminders follow your next shift, and a countdown to it sits on your Lock Screen."
  cta_label: "Download Free"
  alt: "AfterShift Today screen on iPhone showing the countdown to the next shift, Readiness rated Good during an on-call window, and a Sleep Score of 80"

who_for:
  - "You work nights, rotating shifts, or on-call, and generic sleep apps keep measuring you against a 9-to-5"
  - "You're a nurse, paramedic, or firefighter, or you work a factory, warehouse, airport ground crew, or overnight hospitality shift"
  - "Your sleep comes in pieces, a main sleep plus naps, and you want all of it counted between shifts"
  - "You want wind-down and caffeine cut-off reminders that move when your shifts move"
  - "Your roster repeats (4 on / 4 off, Panama 2-2-3, 2 days / 2 nights, or your own cycle up to 28 days) and you'd rather enter it once"
  - "You won't hand your health data to an account, a server, or an analytics SDK"

who_not_for:
  - "You work a steady 9-to-5 and a regular sleep app already fits"
  - "You want diagnosis or treatment for Shift Work Disorder (talk to a sleep specialist)"
  - "Nothing saves your sleep to Apple Health: an iPhone on its own records no sleep, so you need an Apple Watch or a sleep app"
  - "You need the app on iPad, Mac, or Android, or synced across devices"

related_journal:
  slug: "how-to-sleep-after-a-night-shift"
  anchor: "How to sleep after a night shift: the drive home, the dark room, the nap and the days off"
alternatives_to:
  - "OffShift"
  - "Shift Worker"
  - "ShiftSleep"
  - "Timeshifter (Shift Work)"
  - "Sleep Aid for Shift Workers"
  - "SleepSync"
  - "RISE Sleep Tracker"

value_points:
  - title: "Measured shift to shift"
    description: "A shift worker's day runs from the end of one shift to the start of the next, so that is the window AfterShift measures. Readiness and sleep debt look at how much you slept inside it, whether that sleep happened at 10 a.m. or 10 p.m."
  - title: "A roster that fills itself"
    description: "Pick a preset or build your own cycle of 1 to 28 days. AfterShift fills the next 8 weeks and keeps topping them up. Long-press any shift to extend, move, or swap it."
  - title: "What to do with the hours you have"
    description: "\"Do this now\" reads the time before your next shift and gives you three steps from 21 techniques, each with a timer. Wind-down, caffeine cut-off, and nap-window reminders are timed to the same shift."
  - title: "Private by construction"
    description: "You never create an account, and the app makes no network calls of its own, so your shifts and sleep stay on your iPhone. It carries no analytics or third-party SDKs. With Premium, Apple Intelligence writes the explanations on the device (iOS 26+ on a supported iPhone)."

features:
  - title: "Readiness for your next shift"
    description: "A Premium rating of Low, OK, or Good, from the sleep you got since your last shift against the sleep target you set, with the reason in one line. It sits on the Today screen and in a widget, and Siri answers \"Am I ready for my shift?\""
  - title: "Repeating rotations"
    description: "Seven presets: Three-shift rotation, 4 on / 4 off, 4 on / 3 off, 2 days / 2 nights, Panama (2-2-3), Fixed nights, and Fixed days. Or build your own cycle of up to 28 days, long enough for a DuPont. Name as many shift types and rest days as your workplace uses."
  - title: "Sleep from Apple Health, naps included"
    description: "Last night's sleep imports itself, even in the background, and naps are tagged as naps. Log a nap yourself, or start a 25-minute nap timer on the Lock Screen that logs the nap when you end it. Needs an Apple Watch or a sleep app that saves sleep to Apple Health."
  - title: "Sleep Timing, stages, and debt trend"
    description: "Every sleep shows time asleep and efficiency, plus Awake, Core, Deep, and REM when your sleep source records stages. A sleep-debt chart labels each cycle Building, Stable, or Recovering. Premium adds the Sleep Score, the Shift Recovery Score, Sleep Continuity, and Trends."
  - title: "Do this now"
    description: "One of 12 scenarios for your current window, such as a short window between shifts or a night shift coming up, with three steps and their durations. Swap a step you don't like. The 21 techniques come with how-to steps and a timer."
  - title: "Caffeine cut-off that adapts"
    description: "Log a coffee in one tap, or an espresso, energy drink, or tea with a long press. The cut-off reminder adapts to what you drank and the caffeine sensitivity you set, and is timed to your next shift."
  - title: "Calendar import"
    description: "Connect your work calendar and AfterShift detects the shifts in it, with a review list before anything is added. Free reads 1 calendar, 14 days ahead, when you import. Premium syncs several calendars each time you open the app and tracks overtime."
  - title: "Widgets, Lock Screen, and Siri"
    description: "Seven widgets, four of them free: Next Shift, Readiness, Shift Plan, and Roster. A Lock Screen and Dynamic Island countdown to your next shift shows the top \"Do this now\" step. Ask Siri when your next shift is or when to sleep."

screenshots:
  - src: "/assets/screenshots/aftershift/1.webp"
    alt: "AfterShift comparing a generic sleep score of 32 with its shift-aware recovery score of 90 for the same night"
  - src: "/assets/screenshots/aftershift/2.webp"
    alt: "AfterShift recovery score of 81 on iPhone, timed to when a shift worker clocks out"
  - src: "/assets/screenshots/aftershift/3.webp"
    alt: "AfterShift nap guidance showing a recommended nap before a night shift"
  - src: "/assets/screenshots/aftershift/4.webp"
    alt: "AfterShift roster import previewing detected shifts from a calendar before adding them"
  - src: "/assets/screenshots/aftershift/5.webp"
    alt: "AfterShift coach screen with evening sleep techniques for shift workers"
  - src: "/assets/screenshots/aftershift/6.webp"
    alt: "AfterShift sleep debt trend chart with a recovery plan for catching up"
  - src: "/assets/screenshots/aftershift/7.webp"
    alt: "AfterShift privacy card: no accounts, data stays on the phone"
  - src: "/assets/screenshots/aftershift/8.webp"
    alt: "AfterShift Home Screen widgets showing the next shift, readiness and a week ahead"
  - src: "/assets/screenshots/aftershift/9.webp"
    alt: "AfterShift extra-large widget showing a night countdown and sleep heatmap on one page"


privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No account, no ads, and no analytics or third-party SDKs"
    - "Sleep is read from Apple Health, read-only, and never written back"
    - "Shifts, sleep, and calendar data stay on your iPhone and are never sent to a server"
    - "Premium explanations come from Apple Intelligence on the device"
    - "Data leaves your iPhone only when you export or share a report yourself"

faq:
  - q: "What is AfterShift?"
    a: "AfterShift is an iPhone sleep and recovery app for shift workers. It measures your sleep over the window between shifts instead of midnight to midnight, builds your roster from a repeating rotation, imports sleep from Apple Health with naps included, and times wind-down, caffeine cut-off, and nap reminders to your next shift. Premium adds Readiness for your next shift, the Sleep Score, the Shift Recovery Score, and trends."

  - q: "Who is AfterShift for?"
    a: "Nurses and hospital staff, paramedics, firefighters, factory, logistics, and airport ground crews, hospitality and overnight staff, on-call workers, and anyone whose sleep window moves from week to week. If your roster repeats, from 4 on / 4 off to a DuPont-length 28-day cycle, AfterShift can hold it. Setup asks whether you work rotating shifts, a fixed schedule, or irregular and on-call hours."

  - q: "How is AfterShift different from OffShift, ShiftSleep, Timeshifter, or generic sleep apps?"
    a: "Generic sleep apps measure you against a night that starts at 11 p.m. AfterShift measures recovery shift to shift, fills your roster from a repeating rotation, and times its reminders and its \"Do this now\" steps to your next shift. There is no account, and your data stays on your iPhone. The comparison pages go app by app: <a href=\"/alternatives/offshift/\">OffShift</a>, <a href=\"/alternatives/shiftsleep/\">ShiftSleep</a>, and <a href=\"/alternatives/timeshifter/\">Timeshifter</a>."

  - q: "What is the Shift Recovery Score, and how is it calculated?"
    a: "The Shift Recovery Score is a 0 to 100 score for one sleep, shown in Recovery details with Premium. It weighs sleep duration (50%), continuity, meaning how unbroken the sleep was (30%), and the balance of sleep stages (20%). Readiness is the separate rating for your next shift: Low, OK, or Good, from the sleep you got between shifts against your sleep target. Both are custom heuristics, not medical assessments and not a diagnosis of Shift Work Disorder. <a href=\"/apps/aftershift/methodology/\">The methodology page</a> lists every input and weight."

  - q: "Why do naps count toward recovery in AfterShift?"
    a: "For shift workers, naps are part of the plan. A short nap before a night shift is one of the most common strategies in shift-work sleep guidance, because the main sleep window is often too short on its own. AfterShift imports naps from Apple Health and tags them as naps, and naps you log yourself, or time with the 25-minute nap timer, land in the same list. Readiness counts the sleep you got inside the window between shifts, naps included. Premium adds a Naps card to Recovery details."

  - q: "Does AfterShift help with Shift Work Disorder (SWSD)?"
    a: "AfterShift is an informational recovery tracker, not a treatment for Shift Work Disorder. SWSD is a circadian rhythm sleep-wake disorder classified in the <a href=\"https://aasm.org/clinical-resources/international-classification-sleep-disorders/\" rel=\"noopener\">ICSD-3</a>, and a sleep specialist should diagnose and treat it. AfterShift can help you see your own patterns, such as sleep debt building across cycles or caffeine late in the day, but if your schedule is badly affecting your sleep, talk to a clinician. The U.S. <a href=\"https://www.cdc.gov/niosh/work-hour-training-for-nurses/longhours/mod7/06.html\" rel=\"noopener\">NIOSH shift work resources</a> are a reasonable starting point."

  - q: "Which shift patterns does AfterShift support?"
    a: "Any pattern you can set up as a repeating rotation or add by hand. The presets are Three-shift rotation, 4 on / 4 off, 4 on / 3 off, 2 days / 2 nights, Panama (2-2-3), Fixed nights, and Fixed days. You can also build your own cycle of 1 to 28 days, which is long enough for a full DuPont (4 nights / 3 off / 3 days / 1 off / 3 nights / 3 off / 4 days / 7 off). AfterShift fills the next 8 weeks and keeps topping them up. Shift types take your own names and times, so 12-hour days and nights and swing shifts fit too. Calendar import can also detect shifts from your work calendar: free reads 1 calendar, 14 days ahead; Premium syncs several calendars automatically when you open the app."

  - q: "Does AfterShift give caffeine timing recommendations?"
    a: "It gives you a caffeine cut-off reminder timed to your next shift, so the cut-off moves when your shifts move. Log a coffee in one tap, or long-press for an espresso, an energy drink, tea, or something else, and the reminder adapts to how much caffeine you had and the caffeine sensitivity you set. Premium adds caffeine detail to each sleep in Recovery details."

  - q: "Does AfterShift give medical advice?"
    a: "No. AfterShift is a tool for tracking and planning recovery. It gives plain insights, not medical diagnoses or treatment recommendations, and its suggestions are labelled as suggestions, not prescriptions. If you suspect Shift Work Disorder, chronic insomnia, sleep apnea, or any other clinical sleep condition, see a sleep specialist."

  - q: "Is AfterShift free?"
    a: "Yes. Free covers repeating rotations and the roster, sleep import from Apple Health with naps included, Sleep Timing and Sleep Stages, the sleep-debt trend, the recovery plan, \"Do this now\" steps and 21 techniques, shift-timed reminders, the Lock Screen countdown and nap timer, Siri, four of the seven widgets, and calendar import from 1 calendar, 14 days ahead. Premium adds Readiness, the Sleep Score and Shift Recovery Score, Sleep Continuity, Trends, automatic sync from several calendars with overtime tracking, a preview of what a shift change does to your readiness, a PDF report, and explanations written on-device by Apple Intelligence (iOS 26 or later on a supported iPhone). It costs {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} once, and the subscriptions start with a {TRIAL}. All three plans support Family Sharing. Prices in USD; the App Store shows your local currency at checkout."

  - q: "Does AfterShift sell my health data?"
    a: "No. AfterShift has no ads, no third-party trackers, no analytics SDKs, and no servers to send data to. Your sleep, nap, and shift data stay on your iPhone, because there is no account and no cloud sync. Data leaves the device only if you export or share a report yourself."

  - q: "Does AfterShift sync between devices or work on iPad?"
    a: "No. AfterShift runs on iPhone only, and there is no account and no iCloud sync, so your data lives on one iPhone. Deleting the app deletes that data. A Premium purchase restores on any iPhone signed in with the same Apple ID."

  - q: "Do I need an Apple Watch?"
    a: "No. AfterShift has no Apple Watch app and does not need one, but it does need sleep in Apple Health, and an iPhone on its own records none. An Apple Watch or any sleep app that saves to Apple Health will do. You can also log naps in the app and log sleep by asking Siri. A source that records sleep stages adds the stage detail; without it, the stage part of the scores uses neutral defaults."

  - q: "Should I get morning light after a night shift, or block it?"
    a: "Both, at different times and for different goals. If you are staying on a night-shift schedule, block bright morning light on the commute home (sunglasses help) and sleep in a dark room, because bright light tells your circadian clock it is daytime and makes it harder to fall asleep. If you are switching back to day life, do the opposite and get bright light in the morning to phase-advance your clock. AfterShift's Coach tab has a short \"Light exposure basics\" reading. For the circadian science in full, sleep specialists and the U.S. <a href=\"https://www.cdc.gov/niosh/work-hour-training-for-nurses/longhours/mod7/06.html\" rel=\"noopener\">NIOSH shift work resources</a> cover light exposure timing in detail."

  - q: "What does sleep inertia have to do with shift work?"
    a: "Sleep inertia is the groggy, slowed-reaction state in the first 15 to 30 minutes after waking. For shift workers it matters in two places. (1) Waking from a long, deep nap mid-shift can leave inertia bad enough that the nap costs more than it gives; AfterShift's Lock Screen nap timer runs for 25 minutes. (2) The start of a night shift after daytime sleep often comes with leftover inertia that feels like fatigue. Telling the two apart helps when you are deciding whether you need caffeine or just fifteen minutes."

  - q: "Does it matter if I'm a morning person or a night owl for shift work?"
    a: "Yes. Your chronotype is one of the biggest predictors of how hard rotating and night shifts will hit you. Strong morning types (larks) struggle more with permanent night shifts because their circadian system resists the phase shift; strong evening types (owls) usually adapt better to nights but pay for it on early-morning rotations. Most people sit in the middle. AfterShift does not ask you to label yourself; it works from the sleep you actually get around your shifts. If you want a formal read on yours, sleep researchers use two validated tools: the MEQ (Horne-Östberg Morningness-Eveningness Questionnaire) and the MCTQ (Munich ChronoType Questionnaire)."

  - q: "Should I take melatonin for shift work? Does AfterShift recommend supplements?"
    a: "AfterShift does not give supplement recommendations; that conversation belongs with a clinician or pharmacist. What we can fairly say from the literature: low-dose melatonin (0.3 to 3 mg) taken at the start of your intended sleep window is the use sleep researchers most often discuss for shift workers. It works as a circadian phase-shifter as much as a sedative, so when you take it matters more than how much. Higher doses are not better and increase next-day grogginess in some people. Melatonin sold in the U.S. is unregulated and its doses are labelled inconsistently. The U.S. <a href=\"https://www.cdc.gov/niosh/work-hour-training-for-nurses/longhours/mod7/06.html\" rel=\"noopener\">NIOSH shift work module</a> and the AASM's clinical guidance both cover melatonin timing for shift workers in more depth. Talk to your clinician before starting any supplement."

  - q: "What are sleep latency and sleep efficiency, and does AfterShift track them?"
    a: "Sleep latency is how long it takes you to fall asleep after lights-out; sleep efficiency is the percentage of time in bed actually spent asleep. Both are standard metrics in sleep science. For shift workers, both usually get worse with daytime sleep: bright daylight, noise, and a circadian system still saying \"this is the wrong time\" push latency up and efficiency down. AfterShift does not measure sleep latency. When Apple Health has separate in-bed and asleep data, AfterShift shows sleep efficiency in Sleep Timing, and with Premium it feeds the Sleep Score. A chronically low efficiency on daytime sleep usually points to the sleep environment (light, noise, a partner's schedule) more than a number to chase."

  - q: "What is social jet lag, and does it matter for shift workers?"
    a: "Social jet lag is the term sleep researchers use for the gap between your biologically preferred sleep timing and the schedule your work or social life imposes. Most people feel some of it on Monday mornings after a freer weekend. For shift workers the mechanism is the same but much larger: a permanent night-shift nurse who spends days off with a family that sleeps at night is in effect flying across time zones every weekend. AfterShift does not measure social jet lag. Its sleep-debt trend shows, cycle by cycle, whether your debt is building, stable, or recovering. Researchers use the MCTQ (Munich ChronoType Questionnaire) to quantify social jet lag if you want a formal read."

support:
  email: "support@lagerland.app"
  url: "/apps/aftershift/support/"

release:
  first_release: "2026-01-01"
  last_updated: "2026-10-24"

ratings:
  value: "3.6"
  count: 5
  last_synced: "2026-07-31"

show_body: true
about_heading: "Why AfterShift exists."

# Studio identity (Organization-mode founder block, no personal name).
founder:
  overline: "Who built this"
  heading: "An independent Apple studio making apps for people who don't work 9 to 5."
  entity_type: "Organization"
  name: "Lagerland Apps"
  role: "Independent Apple studio · Finland"
  photo: "/assets/icons/lagerland-mark.png"
  bio: "AfterShift exists because every consumer sleep app we tried assumed an 11 p.m. bedtime and a 7 a.m. alarm, then quietly marked down the nurses, paramedics, and factory workers among our family and friends for not living that way. Naps counted as failures. Daytime sleep was scored as a poor night. Caffeine cutoffs sat at 2 p.m. whenever the next shift actually started. Those apps were built around a person who wasn't the one using them. Lagerland has no team, investors, or advertisers behind it. It is a small Apple studio in Finland making the apps we wanted to use."
  support_email: "support@lagerland.app"
  response_time: "Support emails are answered personally, usually within a day."
  signals:
    - "GDPR-first architecture: on-device storage, no cloud sync, zero analytics SDKs"
    - "Lagerland's other App Store apps follow the same data rules: no advertising SDKs, no required accounts, no health-data resale"
    - "Paid for by people buying the software, with no ads or investors"
    - "The methodology is public: the inputs and weights behind Readiness and the scores are on one page"
  external_link:
    href: "/apps/aftershift/methodology/"
    label: "Read the AfterShift methodology →"
last_updated: 2026-10-30
---

Most sleep apps were designed for someone who goes to bed at 11 p.m. and wakes at 7 a.m. Go through the onboarding of any major one and the questions assume a fixed bedtime, a steady wake time, and free weekends. The people who keep hospitals, fire stations, factories, and warehouses running through the night have to use those same apps. A nurse logs five hours of daytime sleep after a string of night shifts, and the app politely tells her she had a *poor night* and should go to bed earlier. The app was built around someone who isn't her.

AfterShift comes from an independent Apple studio that watched too many friends in scrubs and uniforms get that same notification. It starts the day where a shift worker's day starts: when the last shift ends. Sleep at 10 a.m. counts toward the window before your next shift, and so does the nap you take before a night. Your rotation goes in once and fills eight weeks of roster. The caffeine cut-off and the wind-down reminder move when your shifts move.

Readiness is the part we are proudest of. Before you leave for work it answers one question: given the sleep you got since your last shift, against the target you set, are you ready for the next one? Low, OK, or Good, with the reason in a line. The Sleep Score and the Shift Recovery Score go deeper on a single sleep, and [the methodology page](/apps/aftershift/methodology/) shows how each one is built. All three are part of Premium, and none of them is a medical measure. They are there to help you plan the hours you have.
