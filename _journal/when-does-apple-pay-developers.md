---
layout: journal
slug: when-does-apple-pay-developers
title: "When does Apple pay developers? The App Store fiscal calendar, payment dates and missing months"
date: 2026-10-17
seo:
  title: "When Does Apple Pay Developers? Fiscal Calendar Explained"
  description: "Apple pays App Store proceeds within 45 days of each fiscal month's end. The fiscal calendar, 2026 payment dates, thresholds, currency, and missing months."
  keywords:
    - "when does apple pay developers"
    - "app store payment dates 2026"
    - "apple fiscal calendar app store"
    - "app store connect payments"
    - "minimum payment threshold app store"
    - "balance carried forward app store connect"
    - "payments and financial reports"
    - "appmeta pulse"
lede: "Apple pays App Store developers once per fiscal month, and its fiscal months don't line up with the calendar. That one fact explains most of the confusion: the month with two deposits, the month with none, and the financial report that seems to cover the wrong dates."
quick_answer: "Apple pays App Store proceeds within 45 days of the last day of the fiscal month in which the transactions were completed, as long as you have a Paid Apps Agreement in effect, banking and tax information in App Store Connect, and proceeds above the minimum payment threshold. Apple's fiscal months run Sunday to Saturday, and each quarter has one five-week month followed by two four-week months. In 2026 payments have usually arrived on a Thursday about 33 days after each fiscal month closed, so some calendar months get two payments and others none. Payment details appear in Payments and Financial Reports from the first Wednesday of the following fiscal month."
faq:
  - q: "When does Apple pay App Store developers?"
    a: "Within 45 days of the last day of the fiscal month in which the transactions were completed, according to Apple. In 2026 the payments have usually landed on a Thursday about 33 days after each fiscal month closed: for example, the fiscal month that ended on Saturday, August 29 was paid on Thursday, October 1. Apple's bank sends one payment per fiscal month, combining the proceeds from every currency you sell in."
  - q: "What is Apple's fiscal calendar for App Store payments?"
    a: "Apple's fiscal months are made of whole weeks that run Sunday to Saturday. Each quarter has a five-week month followed by two four-week months, and the fiscal year ends in late September; fiscal 2026 ended on Saturday, September 26, 2026. Apple's help pages link to the official calendar inside App Store Connect, which shows the exact dates for each fiscal month."
  - q: "Why didn't Apple pay me this month?"
    a: "The most common reason is the calendar itself. Payments follow fiscal months, so in 2026 January, April, July and October each had two payments while February, May and August had none. Other reasons are a balance below the minimum payment threshold, which Apple carries forward to the next payment, a payment your bank returned, missing banking or tax information, a Paid Apps Agreement that isn't in effect, or no purchases or refunds in that fiscal month."
  - q: "What is the minimum payment threshold for App Store payments?"
    a: "It depends on the country of your bank and the currency of the account. Apple publishes a table of bank countries and currencies with their own thresholds, and many common pairs, such as a USD account in the United States or a EUR account in the euro area, are listed at 0.02 USD. Bank countries and currencies not in the table must exceed 40 USD. Below the threshold, Payments and Financial Reports shows Balance Carried Forward and the proceeds roll into the next payment period."
  - q: "Why is my Apple payment different from my proceeds?"
    a: "Apple's bank converts proceeds into your bank account's currency at roughly the spot rate on the payment date, so the amount moves with exchange rates after the fiscal month closes. Withholding tax, where it applies, is taken when the payment is made. Your own bank or an intermediary bank can also deduct fees, so the deposit can be smaller than the payment amount shown in App Store Connect."
  - q: "Where do I see my App Store payments?"
    a: "In App Store Connect, under Payments and Financial Reports, which needs the Account Holder, Admin or Finance role. Payment information for the previous fiscal month starts to appear on the first Wednesday of the current fiscal month, and financial reports for all countries and regions are ready by the first Friday. A paid month shows the amount, the date, your bank and a Transaction ID; an unpaid one shows Total Estimated Proceeds."
mentioned_apps:
  - appmeta-pulse
read_time: "7 min read"
excerpt: "How Apple pays App Store developers: the 45-day rule, the 5-4-4 fiscal calendar with 2026 dates, minimum payment thresholds, currency conversion and bank fees, where Payments and Financial Reports shows each payment, and the usual reasons a month looks missing."
---

Apple's rule is one sentence long: payments are made "within 45 days of the last day of the fiscal month in which the transaction was completed," to the bank account and currency you entered in App Store Connect ([Apple](https://developer.apple.com/help/app-store-connect/getting-paid/overview-of-receiving-payments/)). The fiscal month is the part that needs explaining, because it decides when a sale gets paid and which report it appears in.

## When will Apple pay me?

To be paid at all, Apple lists four conditions ([Apple](https://developer.apple.com/help/app-store-connect/getting-paid/overview-of-receiving-payments/)):

1. A Paid Apps Agreement in effect.
2. Banking information in App Store Connect. Apple pays the primary account on file and doesn't split payments across accounts.
3. Proceeds above the minimum payment threshold for each country or region where you sell.
4. Any monthly invoicing your country or region requires.

Tax forms belong on that list in practice: Apple's tax pages say you need to submit them, alongside banking information, to receive payments ([Apple](https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information/)).

Once those are in place, Apple's bank combines the proceeds from every currency you sell in and sends "a single payment to your bank per fiscal month."

## How does Apple's fiscal calendar work?

Fiscal months are built from whole weeks that run Sunday to Saturday. Each quarter has a five-week month followed by two four-week months, and the year ends in late September. Fiscal 2026 ended on Saturday, September 26. In 2026 the App Store's fiscal quarters have closed on the same days as Apple's company quarters; Apple's third quarter of fiscal 2026 ended on June 27 ([Apple](https://www.apple.com/newsroom/2026/07/apple-reports-third-quarter-results/)), the same day as fiscal June.

Apple's help pages link to the official calendar inside App Store Connect, which needs a sign-in. These are the fiscal months behind this year's payments, with the payment dates that RevenueCat and ASO.dev both list in their published calendars ([RevenueCat](https://www.revenuecat.com/blog/app-store-fiscal-calendar-and-payment-dates), [ASO.dev](https://aso.dev/app-store-connect/apple-fiscal-calendar/)):

| Fiscal month | Sales period | Payment |
|---|---|---|
| November 2025 | Nov 2 – Nov 29, 2025 | Fri, Jan 2, 2026 |
| December 2025 | Nov 30 – Dec 27, 2025 | Thu, Jan 29 |
| January 2026 (5 weeks) | Dec 28, 2025 – Jan 31 | Thu, Mar 5 |
| February 2026 | Feb 1 – Feb 28 | Thu, Apr 2 |
| March 2026 | Mar 1 – Mar 28 | Thu, Apr 30 |
| April 2026 (5 weeks) | Mar 29 – May 2 | Thu, Jun 4 |
| May 2026 | May 3 – May 30 | Thu, Jul 2 |
| June 2026 | May 31 – Jun 27 | Thu, Jul 30 |
| July 2026 (5 weeks) | Jun 28 – Aug 1 | Thu, Sep 3 |
| August 2026 | Aug 2 – Aug 29 | Thu, Oct 1 |
| September 2026 | Aug 30 – Sep 26 | Thu, Oct 29 (expected) |
| October 2026 (5 weeks) | Sep 27 – Oct 31 | Thu, Dec 3 (expected) |

The pattern is 33 days from the Saturday a fiscal month ends to a Thursday payment, with New Year's Day pushing one payment to a Friday. That sits inside Apple's 45-day promise, but the promise is the 45 days, not the Thursday. Treat the last two rows as estimates until Payments and Financial Reports shows an expected payment date.

A fiscal month can also carry a calendar month's name while starting in the previous one. Fiscal January 2026 began on December 28, 2025, so a purchase on December 30 sits in a January financial report. Sales and Trends, which uses calendar days in Pacific Time, files the same purchase under December.

## Why is a month missing?

Most of the time, nothing is wrong. Because every quarter starts with a five-week month, payments drift against the calendar. In 2026, January, April, July and October each had two payments, and February, May and August had none. If your bookkeeping runs by calendar month, those months will look empty even though every fiscal month was paid.

When a fiscal month really wasn't paid, Payments and Financial Reports says why ([Apple](https://developer.apple.com/help/app-store-connect/getting-paid/view-payments-and-proceeds)):

- Expected Payment Date: the payment date hasn't come yet.
- Balance Carried Forward: proceeds haven't reached the minimum payment threshold and "will carry over to the next payment period."
- Payment Returned: your bank sent the payment back. App Store Connect shows the reason and a Transaction ID. Once you fix the banking details, Apple says returned earnings can take up to two regular payment cycles to resend.

There are two quieter cases. A fiscal month with no purchases or refunds produces no financial report at all ([Apple](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports/)), and an expired agreement or missing tax form stops payments until it is fixed.

## What is the minimum payment threshold?

Apple publishes a [table of thresholds](https://developer.apple.com/help/app-store-connect/reference/reporting/minimum-payment-threshold) by bank country and account currency. Many common pairs, such as a USD account in the United States, a EUR account in the euro area or a GBP account in the United Kingdom, are listed at 0.02 USD. Any bank country or currency not in the table must exceed 40 USD. A small app paid into an unlisted currency can carry its balance forward for months before a payment goes out.

## What currency are you paid in, and who takes the fees?

You are paid in your bank account's currency. Apple's bank does the conversion, typically at the spot rate on the payment date and no more than three business days before the money reaches your account ([Apple](https://developer.apple.com/help/app-store-connect/getting-paid/overview-of-receiving-payments/)). Apple sends low-value transfers instead of wires where it can, but your bank or an intermediary bank may still deduct fees, and the deposit can be smaller than the amount App Store Connect shows.

That is why the estimate and the payment differ. Before a month is paid, App Store Connect shows Total Estimated Proceeds, and Apple says the actual amount can differ mainly because of exchange-rate movement and withholding tax, which is applied when the payment is made ([Apple](https://developer.apple.com/help/app-store-connect/getting-paid/view-payments-and-proceeds)).

## Where do you see payments in App Store Connect?

Payments and Financial Reports, which needs the Account Holder, Admin or Finance role. Payment information for the previous fiscal month starts to appear on the first Wednesday of the current fiscal month, and the financial reports for every country and region are ready by the first Friday ([Apple](https://developer.apple.com/help/app-store-connect/getting-paid/view-payments-and-proceeds)). You can ask for an email when they arrive.

A paid month shows the amount in your bank currency, the bank name with the last four digits of the account, the issue date and a seven-digit Transaction ID, also called a Consolidated Credit Identifier. Have that ID ready if you need to ask Apple or your bank about a deposit. For any country or region you can open units, amounts in the local currency, taxes and adjustments, and the exchange rate applied.

The downloadable financial reports come as a single file for all countries and regions, as separate files for each location, or as a detailed version with transaction and settlement dates, and Apple keeps them for ten years. They can also be fetched through the App Store Connect API.

## Why doesn't the payment match Sales and Trends?

Sales and Trends counts a purchase when the customer starts it and estimates USD amounts with last month's average exchange rates. The financial reports count settled transactions in fiscal months and use the rate applied to your bank's currency. My [July post on proceeds and sales](/journal/app-store-proceeds-vs-sales/) goes through every column and the reasons the two sets of numbers drift apart.

## Where AppMeta Pulse fits

[AppMeta Pulse](/apps/appmeta-pulse/) reads the daily Sales and Trends reports through the App Store Connect API. It doesn't read Payments and Financial Reports, so it can't tell you when a payment will land or what it will be after conversion and fees. For that, the Payments page above is the source.

Payments and Financial Reports is still the first place Pulse sends you: the Vendor Number it needs to download sales reports is shown there, under your legal entity name. After that, Pulse covers the daily side, with proceeds by app, refunds, and subscription figures such as the [MRR worked out from Apple's Subscription report](/journal/how-to-calculate-mrr-for-app-store-subscriptions/). It also keeps its own copy of the daily reports after Apple's one-year window for them closes.
