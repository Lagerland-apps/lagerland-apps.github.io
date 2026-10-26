---
layout: app
slug: aftershift
name: "AfterShift"
tagline: "The shift-worker sleep app where naps count as real recovery."
quick_answer: "AfterShift is a sleep and recovery app for shift workers: nurses, paramedics, firefighters, pilots, and anyone on rotating, night, or on-call schedules. The iPhone app counts naps as recovery, scores how recovered you are before your next shift, and times caffeine to the schedule you actually work instead of a 9-to-5 baseline. It is free, with Premium from {P_MONTHLY}/mo, {P_YEARLY}/yr, or {P_LIFETIME} lifetime. It has no ads, sells no health data, and needs no account."
category: health
status: live

app_store_url: "https://apps.apple.com/app/id6757163182"

price:
  model: freemium

plans_footnote: "Prices in USD; the App Store shows your local currency at checkout. Apple handles refunds through the standard App Store refund flow. Lifetime is a one-time purchase and does not auto-renew."

plans:
  - name: "Free"
    price: "$0"
    summary: "Sleep and nap tracking with basic recovery summaries, free for good."
    features:
      - "Sleep tracking and nap tracking"
      - "Basic recovery summaries"
      - "Calendar shift import"
      - "Shift-timed reminders, including caffeine cut-off"
      - "On-device storage with no account and no cloud sync"
  - name: "Premium · Monthly"
    price: "{P_MONTHLY}/mo"
    kind: monthly
    summary: "Full Premium, billed monthly. Cancel anytime."
    features:
      - "Full Shift Recovery Score"
      - "Fatigue and fragmentation insights"
      - "Automatic calendar sync, multiple calendars & overtime tracking"
      - "Cycle-to-cycle trends and a shareable PDF report"
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
    summary: "All Premium features for one payment, about what {LIFETIME_MONTHS} months of monthly Premium would cost."
    features:
      - "Everything in Premium · Annual"
      - "One-time purchase, no renewal"
      - "Restores on every device signed in with the same Apple ID"
      - "Family Sharing with up to 5 family members at no extra cost"

icon: "/assets/icons/aftershift.png"
og_image: "/assets/og/aftershift.png"

seo:
  title: "AfterShift: Sleep & Recovery App for Shift Workers"
  description: "Shift-aware sleep & recovery for nurses, paramedics, and night staff. Naps count as recovery, caffeine timed to your next shift. Free + Pro."
  keywords:
    - shift work sleep app
    - sleep tracker for shift workers
    - night shift recovery app
    - nurse sleep app
    - shift work fatigue tracker
    - nap tracker shift work
    - rotating schedule sleep app
    - first responder sleep app
    - night shift sleep tracker
    - shift recovery score
    - caffeine timing shift work
    - on-call sleep recovery
    - shift work disorder app
    - DuPont schedule sleep
    - 2-2-3 rotation sleep
    - 4 on 4 off sleep app
    - 12 hour shift sleep tracker
    - paramedic sleep tracker
    - firefighter sleep app
    - pilot fatigue tracker

hero:
  pre_headline: "For nurses, paramedics, firefighters, pilots & shift workers"
  headline: "Sleep & recovery that follows your shifts."
  secondary: "Naps count as recovery here. They are weighted into your Shift Recovery Score alongside core sleep."
  subheadline: "AfterShift scores how recovered you are before your next shift and times caffeine to the schedule you actually work: DuPont, Pitman, 2-2-3, 4-on-4-off, 12-hour, or on-call. It never measures you against a 9-to-5 baseline."
  cta_label: "Download Free"
  alt: "AfterShift Today screen on iPhone showing the countdown to the next shift, Readiness rated Good during an on-call window, and a Sleep Score of 80"

who_for:
  - "You work rotating, night, or on-call shifts and generic sleep apps keep comparing you to a 9-to-5"
  - "You're a nurse, paramedic, firefighter, police officer, pilot, or factory worker tracking recovery"
  - "You rely on naps for recovery and don't want them treated as an afterthought"
  - "You want caffeine timing tied to your next shift, not to a textbook bedtime"
  - "You work a DuPont, Pitman, 2-2-3, 4-on-4-off, or 12-hour rotation and want the app to understand it"
  - "You won't hand your health data to advertisers, analytics SDKs, or wellness brokers"

who_not_for:
  - "You work a steady 9-to-5 and a generic sleep app already fits"
  - "You want medical diagnosis or treatment for Shift Work Disorder (talk to a sleep specialist)"
  - "You won't use Apple Health or the Apple Sleep tracking on your iPhone or Apple Watch"

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
  - title: "Naps count here"
    description: "For a shift worker a nap is part of the plan. AfterShift is the only shift-worker sleep app that counts naps as full recovery, factored into your Shift Recovery Score alongside core sleep."
  - title: "Your shifts, your recovery"
    description: "Your sleep is analyzed against your actual rotation: DuPont, Pitman, 2-2-3, 4-on-4-off, 12-hour, or on-call. It is never compared to a 9-to-5 benchmark."
  - title: "Caffeine timed to your next shift"
    description: "See when caffeine still helps and when it starts eating into your next sleep window. The timing follows when you actually work, not a textbook 2 p.m. cutoff."
  - title: "Private by default"
    description: "No ads, no account, and no selling of health data. Everything stays on your device, with no analytics SDKs and no resale to wellness brokers."

features:
  - title: "Shift Recovery Score"
    description: "One number built from how much you have slept since your last shift (naps included), how unbroken that sleep was, and your Deep and REM balance. It is capped when the gap before your next shift is too short for a full sleep, or when you are on call. A glance before you clock in tells you whether you're recovered enough."
  - title: "Sleep stages in context"
    description: "Track Awake, Core, Deep, and REM sleep, read against your rotation instead of someone else's Monday morning. Deep sleep at 11 a.m. after a night shift counts as the good result it is."
  - title: "Fatigue & fragmentation insights"
    description: "Spot fragmented-sleep weeks before the fatigue builds up. Pattern-based explanations show why some rotations feel harder and which cycles inside a block left you furthest behind."
  - title: "Smart caffeine timing"
    description: "See when caffeine still helps and when it starts pushing your next sleep window out of reach. It is timed to your actual next shift, not a fixed daily cutoff."
  - title: "Calendar shift import"
    description: "Import shifts straight from your phone calendar. AfterShift detects work blocks and builds recovery insights around them, so you don't enter shifts by hand or rebuild anything when the roster changes."
  - title: "Trends without overwhelm"
    description: "Weekly and monthly patterns in plain, readable charts. Export a summary when you need one for HR, a sleep specialist, or your own diary. The charts stick to what you need and leave out raw data dumps."

screenshots:
  - src: "/assets/screenshots/aftershift/1.png"
    alt: "AfterShift comparing a generic sleep score of 32 with its shift-aware recovery score of 90 for the same night"
  - src: "/assets/screenshots/aftershift/2.png"
    alt: "AfterShift recovery score of 81 on iPhone, timed to when a shift worker clocks out"
  - src: "/assets/screenshots/aftershift/3.png"
    alt: "AfterShift nap guidance showing a recommended nap before a night shift"
  - src: "/assets/screenshots/aftershift/4.png"
    alt: "AfterShift roster import previewing detected shifts from a calendar before adding them"
  - src: "/assets/screenshots/aftershift/5.png"
    alt: "AfterShift coach screen with evening sleep techniques for shift workers"
  - src: "/assets/screenshots/aftershift/6.png"
    alt: "AfterShift sleep debt trend chart with a recovery plan for catching up"
  - src: "/assets/screenshots/aftershift/7.png"
    alt: "AfterShift privacy card: no accounts, data stays on the phone"
  - src: "/assets/screenshots/aftershift/8.png"
    alt: "AfterShift Home Screen widgets showing the next shift, readiness and a week ahead"
  - src: "/assets/screenshots/aftershift/9.png"
    alt: "AfterShift extra-large widget showing a night countdown and sleep heatmap on one page"

privacy:
  data_collection: "none"
  tracking: false
  account_required: false
  notes:
    - "No ads, no health data selling"
    - "No third-party trackers or analytics SDKs"
    - "No account required"
    - "All data stored locally on your device"
    - "Health data never leaves the device unless you choose to export a summary"

faq:
  - q: "What is AfterShift?"
    a: "AfterShift is a sleep and recovery app for shift workers. It tracks sleep, naps, and fatigue against your actual work schedule, with a Shift Recovery Score, caffeine timing, and fragmentation insights. Generic sleep apps compare you to a 9-to-5 baseline; AfterShift does not."

  - q: "Who is AfterShift for?"
    a: "Nurses, paramedics, firefighters, police officers, pilots, factory workers, control-room operators, and anyone working night shifts, rotating schedules, early starts, or on-call hours. If your week follows a DuPont, Pitman, 2-2-3, 4-on-4-off, 12-hour, or swing rotation, AfterShift is meant for you."

  - q: "How is AfterShift different from OffShift, ShiftSleep, Timeshifter, or generic sleep apps?"
    a: "Generic sleep apps assume a regular schedule and compare you to a 9-to-5 benchmark. Most other shift-work apps score core night sleep and treat naps as a footnote. AfterShift differs in two ways: (1) naps count fully toward recovery and are factored into the Shift Recovery Score, and (2) caffeine timing follows your actual next shift instead of a textbook 2 p.m. cutoff. It is also private by default, with no account, no tracking, and no resale of health data."

  - q: "What is the Shift Recovery Score, and how is it calculated?"
    a: "The Shift Recovery Score is a single number from 0 to 100 that estimates how recovered you are before your next shift, measured over the window between your last shift and your next one. It combines three inputs: how much you slept in that window against your sleep target, naps included (50%); sleep continuity, meaning your longest unbroken stretch and how many times you woke (30%); and stage balance, the share of Deep and REM sleep (20%). If the gap before your next shift is shorter than your sleep target, the score is capped at 79; an on-call window is capped at 75. The score is informational. It is not a medical assessment or a diagnosis of Shift Work Disorder. See <a href=\"/apps/aftershift/methodology/\">the full Shift Recovery Score methodology page</a> for the weightings, the caps, and what the literature does and does not support."

  - q: "Why do naps count toward recovery in AfterShift?"
    a: "For shift workers, naps are a recovery strategy. A 20-minute pre-shift nap reduces sleep inertia on a long block; a 90-minute mid-shift nap protects REM and Deep sleep when the main sleep window is short. Sleep researchers studying rotating and on-call work consistently treat naps as legitimate recovery, especially prophylactic naps before night shifts. AfterShift counts the sleep from every nap between your shifts toward the Shift Recovery Score, so a nap moves the number, and Premium shows your nap timing and grogginess patterns."

  - q: "Does AfterShift help with Shift Work Disorder (SWSD)?"
    a: "AfterShift is an informational recovery tracker, not a treatment for Shift Work Disorder. SWSD is a circadian rhythm sleep-wake disorder classified in the <a href=\"https://aasm.org/clinical-resources/international-classification-sleep-disorders/\" rel=\"noopener\">ICSD-3</a>, and a sleep specialist should diagnose and treat it. AfterShift can help you see your own patterns (fragmented weeks, caffeine timing, how much naps contribute), but if your schedule is badly affecting your sleep, talk to a clinician. The U.S. <a href=\"https://www.cdc.gov/niosh/work-hour-training-for-nurses/longhours/mod7/06.html\" rel=\"noopener\">NIOSH shift work resources</a> are a reasonable starting point."

  - q: "Which shift patterns does AfterShift support?"
    a: "Any pattern you can put in your calendar or set up as a repeating rotation. The built-in rotation presets cover a forward-rotating three-shift pattern (day → evening → night, the direction sleep science generally favors over backward rotation), 4-on-4-off, 4-on-3-off, 2 days / 2 nights, Panama/Pitman (2-2-3), fixed nights, and fixed days. You can also build your own cycle of up to 28 days, which is long enough for a full DuPont (4 nights / 3 off / 3 days / 1 off / 3 nights / 3 off / 4 days / 7 off). Day, evening, night, and on-call shift types take your own times, so 12-hour days/nights and swing shifts fit too. Calendar shift import detects work blocks automatically, and the Shift Recovery Score is measured over whatever window sits between the shifts you actually work."

  - q: "Does AfterShift give caffeine timing recommendations?"
    a: "Yes, and they are not a fixed daily cutoff. AfterShift looks at your next scheduled shift and your current sleep window, then shows when caffeine still helps and when it starts pushing your next sleep out of reach. For a worker rotating to nights, the right cutoff is hours later than a 9-to-5 textbook would suggest; on the recovery day after a night block, it may be hours earlier."

  - q: "Does AfterShift give medical advice?"
    a: "No. AfterShift is a tool for tracking and planning recovery. It gives plain insights, not medical diagnoses or treatment recommendations. If you suspect Shift Work Disorder, chronic insomnia, sleep apnea, or any other clinical sleep condition, see a sleep specialist."

  - q: "Is AfterShift free?"
    a: "Yes. The core features are free: sleep tracking, nap tracking, basic recovery summaries, calendar shift import, repeating rotations, next-shift widgets and Live Activity, and shift-timed reminders (wind-down, caffeine cut-off, nap window). Premium unlocks the full Shift Recovery Score, fatigue and fragmentation insights, cycle-to-cycle trends, automatic calendar sync across multiple calendars with overtime tracking, a shareable PDF report, and explanations written on-device by Apple Intelligence on supported iPhones. It costs {P_MONTHLY}/month, {P_YEARLY}/year, or {P_LIFETIME} lifetime. Lifetime supports Family Sharing, so one purchase covers up to 5 family members at no extra cost. Prices in USD; the App Store shows your local currency at checkout."

  - q: "Does AfterShift sell my health data?"
    a: "No. AfterShift has no ads, no third-party trackers, no analytics SDKs, and no data resale. Your sleep, nap, and shift data stay on your device, since there is no account and no cloud sync. Health data leaves the device only if you export a summary yourself."

  - q: "Do I need an Apple Watch?"
    a: "No. AfterShift has no Apple Watch app and does not need one. You can log naps in the app and sleep through Siri or Shortcuts, and it imports sleep from any app or device that saves it to Apple Health. An Apple Watch (or another tracker that records sleep stages) adds the stage and continuity detail behind part of the Shift Recovery Score; without one, those parts use neutral defaults."

  - q: "Should I get morning light after a night shift, or block it?"
    a: "Both, at different times and for different goals. If you are staying on a night-shift schedule, block bright morning light on the commute home (sunglasses help) and sleep in a dark room, because bright light tells your circadian clock it is daytime and makes it harder to fall asleep. If you are switching back to day life, do the opposite and get bright light in the morning to phase-advance your clock. AfterShift uses your scheduled shifts to show which mode you are in. For the circadian science in full, sleep specialists and the U.S. <a href=\"https://www.cdc.gov/niosh/work-hour-training-for-nurses/longhours/mod7/06.html\" rel=\"noopener\">NIOSH shift work resources</a> cover light exposure timing in detail."

  - q: "What does sleep inertia have to do with shift work?"
    a: "Sleep inertia is the groggy, slowed-reaction state in the first 15 to 30 minutes after waking. For shift workers it matters in two places. (1) Waking from a deep mid-shift nap can leave inertia bad enough that the nap costs more than it gives, so AfterShift's nap guidance favors lengths that avoid this. (2) The start of a night shift after daytime sleep often comes with leftover inertia that feels like fatigue. Telling the two apart helps when you are deciding whether you need caffeine or just fifteen minutes."

  - q: "Does it matter if I'm a morning person or a night owl for shift work?"
    a: "Yes. Your chronotype is one of the biggest predictors of how hard rotating and night shifts will hit you. Strong morning types (larks) struggle more with permanent night shifts because their circadian system resists the phase shift; strong evening types (owls) usually adapt better to nights but pay for it on early-morning rotations. Most people sit in the middle. AfterShift does not ask you to label yourself, because your actual sleep timing and recovery pattern across rotations say more than any chronotype questionnaire. If you want a formal read on yours, sleep researchers use two validated tools: the MEQ (Horne-Östberg Morningness-Eveningness Questionnaire) and the MCTQ (Munich ChronoType Questionnaire)."

  - q: "Should I take melatonin for shift work? Does AfterShift recommend supplements?"
    a: "AfterShift does not give supplement recommendations; that conversation belongs with a clinician or pharmacist. What we can fairly say from the literature: low-dose melatonin (0.3 to 3 mg) taken at the start of your intended sleep window is the use sleep researchers most often discuss for shift workers. It works as a circadian phase-shifter as much as a sedative, so when you take it matters more than how much. Higher doses are not better and increase next-day grogginess in some people. Melatonin sold in the U.S. is unregulated and its doses are labelled inconsistently. The U.S. <a href=\"https://www.cdc.gov/niosh/work-hour-training-for-nurses/longhours/mod7/06.html\" rel=\"noopener\">NIOSH shift work module</a> and the AASM's clinical guidance both cover melatonin timing for shift workers in more depth. Talk to your clinician before starting any supplement."

  - q: "What are sleep latency and sleep efficiency, and does AfterShift track them?"
    a: "Sleep latency is how long it takes you to fall asleep after lights-out; sleep efficiency is the percentage of time in bed actually spent asleep. Both are standard metrics in sleep science. For shift workers, both usually get worse with daytime sleep: bright daylight, noise, and a circadian system still saying \"this is the wrong time\" push latency up and efficiency down. AfterShift does not measure sleep latency. When Apple Health has separate in-bed and asleep data, sleep efficiency feeds the Sleep Score (the \"how well did I sleep\" number); the Shift Recovery Score itself is built from sleep length, continuity, and stage balance. Either way, a chronically low sleep efficiency on daytime sleep usually points to a problem with your sleep environment (light, noise, a partner's schedule) more than a number to chase."

  - q: "What is social jet lag, and does it matter for shift workers?"
    a: "Social jet lag is the term sleep researchers use for the gap between your biologically preferred sleep timing and the schedule your work or social life imposes. Most people feel some of it on Monday mornings after a freer weekend. For shift workers the mechanism is the same but much larger: a permanent night-shift nurse who spends days off with a family that sleeps at night is in effect flying across time zones every weekend, and the recovery cost is real. AfterShift does not label social jet lag separately, but it shows up in the fragmentation and recovery-score patterns around rotation changes. The day after a forced realignment is almost always your weakest recovery day in the block, and the score reflects that. Researchers use the MCTQ (Munich ChronoType Questionnaire) to quantify social jet lag if you want a formal read."

support:
  email: "lagerland.apps@proton.me"
  url: "/apps/aftershift/support/"

release:
  first_release: "2026-01-01"
  last_updated: "2026-04-03"

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
  bio: "AfterShift exists because every consumer sleep app we tried assumed an 11 p.m. bedtime and a 7 a.m. alarm, then quietly marked down the nurses, paramedics, pilots, and factory workers among our family and friends for not living that way. Naps counted as failures. Daytime sleep was scored as a poor night. Caffeine cutoffs sat at 2 p.m. whenever the next shift actually started. Those apps were built around a person who wasn't the one using them. Lagerland has no team, investors, or advertisers behind it. It is a small Apple studio in Finland making the apps we wanted to use."
  support_email: "lagerland.apps@proton.me"
  response_time: "Support emails are answered personally, usually within a day."
  signals:
    - "GDPR-first architecture: on-device storage, no cloud sync, zero analytics SDKs"
    - "Lagerland's other App Store apps follow the same data rules: no advertising SDKs, no required accounts, no health-data resale"
    - "Paid for by people buying the software, with no ads or investors"
    - "The methodology is public and citable: the Shift Recovery Score page lists the inputs, the weights, and what the literature does and does not support"
  external_link:
    href: "/apps/aftershift/methodology/"
    label: "Read the Shift Recovery Score methodology →"
last_updated: 2026-10-26
---

Most sleep apps were designed for someone who goes to bed at 11 p.m. and wakes at 7 a.m. Go through the onboarding of any major one and the questions assume a fixed bedtime, a steady wake time, and free weekends. The people who keep hospitals, fire stations, factories, and cockpits running through the night have to use those same apps. A nurse logs five hours of daytime sleep after a string of night shifts, and the app politely tells her she had a *poor night* and should go to bed earlier. The app was built around someone who isn't her.

AfterShift comes from an independent Apple studio that watched too many friends in scrubs and uniforms get that same patronising notification. In AfterShift, naps count as recovery. Daytime sleep before a night shift is a good result. The right caffeine cutoff depends on the shift you are walking into, whatever the clock says. None of this is radical; sleep researchers who study shift work have framed the problem this way for two decades. AfterShift makes it the default.

The Shift Recovery Score is the metric we are proudest of. It is a forward-looking estimate, unlike a consumer sleep score: given the sleep and naps you have had since your last shift, how long you have until the next one, and how fragmented that sleep was, how recovered are you for the next block? Seven hours of daytime sleep before a night shift counts exactly as much as seven hours at night, because the score looks at how much you slept between shifts and ignores the time on the clock. Generic sleep apps penalise daytime sleep. AfterShift does not.
