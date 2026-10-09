---
layout: journal
slug: how-to-calculate-mrr-for-app-store-subscriptions
title: "How to calculate MRR for App Store subscriptions from Apple's Subscription report"
date: 2026-06-27
seo:
  title: "How to Calculate MRR for App Store Subscriptions"
  description: "Calculate MRR for App Store subscriptions from Apple's Subscription report: the formula, the divisor for each plan length, which counts to use, and why."
  keywords:
    - "app store subscription mrr"
    - "how to calculate mrr app store"
    - "app store connect mrr"
    - "app store connect subscription report"
    - "developer proceeds vs customer price"
    - "active standard price subscriptions"
    - "monthly recurring revenue ios app"
    - "appmeta pulse"
lede: "App Store Connect's Analytics dashboard now shows an MRR figure, but Apple doesn't publish how it gets there. The daily Subscription report has every input you need to work it out yourself. The arithmetic is one line. When two dashboards disagree, the cause is almost always one of four decisions around that line."
quick_answer: "MRR (monthly recurring revenue) for App Store subscriptions is what your active paid subscriptions earn you per month once every plan length is put on a monthly footing. From App Store Connect's daily Subscription report, compute it per row as Developer Proceeds × Active Standard Price Subscriptions ÷ the plan's length in months (1 for monthly, 3 for quarterly, 6 for half-yearly, 12 for annual; a 7-day plan is about 0.23 months), then add the rows, converting each proceeds currency to one currency first. Free trials and introductory or promotional offers stay out, because Apple's standard-price count already excludes them. Developer Proceeds already has Apple's commission and applicable taxes removed, and rows marked Rate After One Year carry the higher 85% rate. MRR is a level, not a flow: for a week or a month, average the daily values instead of adding them."
faq:
  - q: "How do you calculate MRR for App Store subscriptions?"
    a: "Use the daily Subscription report from App Store Connect. For each row, multiply Developer Proceeds by Active Standard Price Subscriptions and divide by the plan's length in months: 1 for a monthly plan, 3 for quarterly, 6 for half-yearly, 12 for annual, and about 0.23 (7 ÷ 30.4375) for a 7-day plan. Add the rows per proceeds currency, convert each currency total to one currency, and add those. The result is your MRR for that day."
  - q: "Should MRR use Customer Price or Developer Proceeds?"
    a: "Developer Proceeds, if you want the money you are owed. Customer Price is what the buyer paid, including Apple's commission and, in many storefronts, tax. Under Apple's standard subscription terms you receive 70% of the price minus applicable taxes during a subscriber's first year of paid service and 85% after that; members of the App Store Small Business Program receive 85% from the start. An MRR built on Customer Price overstates your income by the commission and any tax included in the price."
  - q: "Do free trials count toward MRR?"
    a: "No. A subscriber in a free trial hasn't paid anything yet, so a trial is pipeline, not revenue. Apple's Subscription report counts trials in their own column, and its Active Standard Price Subscriptions column already leaves out free trials, introductory offers, subscription offers and marketing opt-ins. Counting only that column gives a conservative MRR made of subscribers paying the standard price."
  - q: "Why doesn't my MRR match last month's proceeds?"
    a: "Because they measure different things. Sales reports record an annual renewal in full on the day it renews, while MRR spreads it across twelve months, so a month with many annual renewals shows proceeds well above MRR and a quiet month shows them below. Proceeds also include one-time purchases, paid-app sales and refunds, which never enter MRR. And Sales and Trends figures are next-day estimates; Apple's Payments and Financial Reports hold the final amounts."
  - q: "Does App Store Connect show MRR?"
    a: "Yes, in Analytics. The Subscriptions dashboard Apple previewed at WWDC25 shows active plans, paid plans and monthly recurring revenue, which Apple defines as revenue from active paid subscriptions normalized to a monthly timeframe. Apple doesn't publish whether that revenue means proceeds or price, which exchange rates apply, or how plan lengths are normalized, so a figure you compute from the Subscription report can differ from it."
  - q: "When is the App Store Connect Subscription report available?"
    a: "Daily Sales and Trends reports, the Subscription report among them, are available the following day, generally by 8 a.m. Pacific Time, and a report day runs from midnight to 11:59 p.m. Pacific Time. Apple lists the Subscription report's availability condition as at least one auto-renewable subscription sold, including introductory prices. Daily reports are kept for one year after they become available."
  - q: "How does AppMeta Pulse calculate MRR?"
    a: "AppMeta Pulse downloads the daily Subscription report through the App Store Connect API with your own key. For each row it multiplies Developer Proceeds by Active Standard Price Subscriptions and divides by the number of months the plan covers (1, 2, 3, 6 or 12), keeps the totals per proceeds currency, and converts them to your display currency with the European Central Bank's monthly average rates only when the number is shown. Trials are counted separately and never enter MRR. Over a period, Pulse shows the average MRR across the days that have a report."
mentioned_apps:
  - appmeta-pulse
read_time: "8 min read"
excerpt: "A reference for computing monthly recurring revenue from App Store Connect's daily Subscription report: the per-row formula, the divisor for each plan length, the columns to use and to ignore, a worked example, and the four decisions that make two MRR numbers disagree. Then how AppMeta Pulse does it."
---

Monthly recurring revenue, for an app that sells subscriptions through the App Store, is what your active paid subscriptions earn you per month once every plan is put on a monthly footing. App Store Connect's daily [Subscription report](https://developer.apple.com/help/app-store-connect/reference/reporting/subscription-report) holds every input. For each row:

**MRR = Developer Proceeds × Active Standard Price Subscriptions ÷ plan length in months**

Add the rows, converting currencies before you add across them, and that is the day's MRR. The rest of this page is about which columns go into that line, and why.

## Which columns in the Subscription report matter?

The report comes in a daily version only, and you can download it from Sales and Trends or through the App Store Connect API's [`salesReports`](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-salesreports) endpoint. One subscription usually fills several rows, broken out by columns such as country, price and proceeds rate. These are the columns that decide MRR, paraphrasing Apple's definitions:

| Column | What it holds | Role in MRR |
|---|---|---|
| Standard Subscription Duration | The plan length: 7 Days, 1 Month, 2 Months, 3 Months, 6 Months or 1 Year | The divisor |
| Developer Proceeds | What you earn per subscription on that row | The amount per subscriber |
| Proceeds Currency | The currency those proceeds are earned in | Add per currency before converting |
| Proceeds Reason | Rate After One Year when a renewal earns 85% of the price instead of 70% | Nothing to do: the proceeds already reflect it |
| Active Standard Price Subscriptions | Paid subscriptions currently active, without free trials, subscription offers, introductory offers or marketing opt-ins | The multiplier |
| Active Free Trial Introductory Offer Subscriptions | Introductory offers currently in a free trial | Left out: a trial earns nothing yet |
| Active Pay Up Front and Pay as You Go Introductory Offer Subscriptions | Introductory offers at a reduced price | Left out of a standard-price MRR |
| Billing Retry, Grace Period | Subscriptions with a billing problem Apple is still trying to fix | Left out |
| Subscribers | People with access, including family members, filled in only when a row covers more than 3 subscriptions | Not a multiplier: it counts people, not paid subscriptions |

## How do you turn each plan length into months?

| Standard Subscription Duration | Divide the row by | Same as |
|---|---|---|
| 7 Days | 0.23 (7 ÷ 30.4375) | multiplying by about 4.35 |
| 1 Month | 1 | the row as it stands |
| 2 Months | 2 | half the row |
| 3 Months | 3 | a third of the row |
| 6 Months | 6 | a sixth of the row |
| 1 Year | 12 | a twelfth of the row |

30.4375 is the length of an average month (365.25 ÷ 12). Treating a month as four weeks instead understates weekly plans by about 8%.

## A worked example

Made-up numbers for an app with a monthly plan and an annual plan, from one day's report:

| Row | Duration | Developer Proceeds | Active Standard Price | Calculation | MRR |
|---|---|---|---|---|---|
| Monthly | 1 Month | 3.49 | 120 | 3.49 × 120 ÷ 1 | 418.80 |
| Annual, first year | 1 Year | 20.99 | 300 | 20.99 × 300 ÷ 12 | 524.75 |
| Annual, Rate After One Year | 1 Year | 25.49 | 80 | 25.49 × 80 ÷ 12 | 169.93 |
| Annual, free trial (45 active) | 1 Year | — | 0 | not counted | 0.00 |
| **Total** | | | | | **1,113.48 USD** |

The 380 annual subscribers contribute more MRR than the 120 monthly ones, yet in a sales report they appear only as lumps on their renewal days. That gap is the reason MRR exists.

## Four decisions that make two MRR numbers disagree

**1. Proceeds or price.** Customer Price is what the buyer paid, including Apple's commission and, in many storefronts, tax. Developer Proceeds is what you are owed. Under Apple's [subscription terms](https://developer.apple.com/app-store/subscriptions/) you receive 70% of the price minus applicable taxes during a subscriber's first year of paid service and 85% after that. Members of the [Small Business Program](https://developer.apple.com/app-store/small-business-program/) receive 85% from the start. An MRR built on price overstates your income by the commission and any included tax.

**2. Who counts as paying.** Free trials are pipeline, not revenue. Introductory and promotional offers are the judgment call: they bring in money, but at a temporary price. Using only Active Standard Price Subscriptions gives the conservative figure, made of subscribers paying the standard price. Including discounted offers raises the number and makes it less stable.

**3. Currency.** Rows arrive in many proceeds currencies. Add per currency first, then convert. Apple's [availability notes](https://developer.apple.com/help/app-store-connect/reference/reporting/sales-and-trends-reports-availability/) say Sales and Trends estimates USD amounts from a rolling average of the previous month's exchange rates. Other tools use other rates, so cross-currency totals can differ slightly even from identical inputs.

**4. Time.** MRR is a level, like a balance, not a flow like sales. For a week or a month, average the daily values; adding thirty days of MRR produces a number thirty times too large. Apple's availability table also lists the Subscription report's condition as at least one auto-renewable subscription sold, introductory prices included. When a day's report isn't there, treat that day as missing, not as zero.

## Why doesn't MRR match last month's proceeds?

Sales reports record an annual renewal in full on the day it renews; MRR spreads it over twelve months. A month heavy with annual renewals shows proceeds well above MRR, and the quiet month after it shows them below. One-time purchases, paid-app sales and refunds land in proceeds and never in MRR.

The two sources also differ in finality. Apple describes Sales and Trends as next-day data and points to Payments and Financial Reports for final proceeds ([Apple](https://developer.apple.com/help/app-store-connect/view-sales-and-trends/download-and-view-reports)). Use MRR to read the direction of your subscriber base, and the financial reports to reconcile money.

## Doesn't App Store Connect show MRR now?

It does, in Analytics. The Subscriptions dashboard that Apple previewed at [WWDC25](https://developer.apple.com/videos/play/wwdc2025/252/) shows active plans, paid plans and monthly recurring revenue. Apple's [metric definitions](https://developer.apple.com/help/app-store-connect-analytics/reference/metrics-definitions/) describe MRR as "revenue earned from active paid subscriptions, normalized to a monthly timeframe." The definition doesn't say whether revenue means proceeds or price, which exchange rates apply, or how each plan length is normalized. If your own figure and Apple's differ, the four decisions above are where to look.

In the same session Apple said two new subscription reports in the Analytics Reports API, a subscription state report and a subscription event report, will replace the older Sales and Trends subscription reports. The Sales and Trends Subscription report is still available through the API, and the formula doesn't depend on which file the numbers arrive in.

## When does each day's report arrive?

Daily Sales and Trends reports are available the following day, generally by 8 a.m. Pacific Time ([Apple](https://developer.apple.com/help/app-store-connect/reference/reporting/sales-and-trends-reports-availability/)), and a report day runs from midnight to 11:59 p.m. Pacific Time ([Apple](https://developer.apple.com/help/app-store-connect/view-sales-and-trends/download-and-view-reports)). Daily reports are kept for one year after they become available, so anyone building a long MRR history has to store the files as they arrive.

## How AppMeta Pulse calculates it

[AppMeta Pulse](/apps/appmeta-pulse/) downloads the daily Subscription report through the App Store Connect API, using a key you create that stays in your Keychain. The [API access page](/apps/appmeta-pulse/api-access/) lists the endpoints it calls and the role the key needs. For each row, Pulse multiplies Developer Proceeds by Active Standard Price Subscriptions and divides by the number of months the plan covers: 1, 2, 3, 6 or 12. Trials are counted and shown on their own; they never enter MRR. Introductory and promotional offers stay out too, because the standard-price column already excludes them.

The totals are kept per proceeds currency. Conversion happens only when a number is shown, into the display currency you choose in Settings, using the European Central Bank's monthly average rates.

Where the number appears:

- **Subscriptions screen.** MRR for the newest day Apple has published, next to active subscriptions and trials, plus a By Product list with one row per subscription and plan length, showing its MRR, active subscriptions and trials.
- **Trends and the per-app view.** MRR over a period is shown as an average (Avg MRR) across the days that have a report, compared with the previous period. Days without a report are skipped, not counted as zero.
- **Widgets.** The Subscriptions widget on the Home Screen and its Lock Screen counterpart show trials, active subscribers and MRR.

Pulse doesn't forecast MRR or make Apple's data arrive sooner. The newest day in the app is the newest day Apple has published, usually yesterday in Pacific Time. For why a quick revenue check belongs on the phone at all, see [the earlier post on AppMeta Pulse](/journal/read-only-revenue-on-the-iphone/); for how it differs from [AppStats](/alternatives/appstats/), [App Sales](/alternatives/app-sales-store-reports/) and [Appfigures](/alternatives/appfigures/), the comparison pages cover each one.

Whichever tool you use, write down its four decisions before comparing its MRR with anyone else's. Two MRR figures rarely part ways over the formula.
