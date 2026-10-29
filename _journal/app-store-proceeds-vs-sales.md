---
layout: journal
slug: app-store-proceeds-vs-sales
title: "App Store proceeds vs sales: what each money column in App Store Connect means"
date: 2026-07-20
seo:
  title: "App Store Proceeds vs Sales: What Each Number Means"
  description: "Sales, proceeds, units, customer price, and developer proceeds in App Store Connect, Apple's 15% and 30% rates, taxes, refunds, and why reports differ."
  keywords:
    - "app store proceeds vs sales"
    - "app store connect proceeds"
    - "developer proceeds per unit"
    - "customer price app store connect"
    - "app store commission rates"
    - "sales and trends vs financial reports"
    - "app store small business program"
    - "appmeta pulse"
lede: "Sales and Trends shows two money figures side by side, and only one of them is close to what reaches your bank. This is a reference to what each number in App Store Connect's sales reports counts, how Apple gets from the customer's price to your proceeds, and why neither will match the payment to the cent."
quick_answer: "In App Store Connect, sales is the amount customers were billed, including any tax Apple collects and remits, and proceeds is what you earn after Apple removes that tax and its commission. Under Apple's standard terms the commission is 30%, or 15% for members of the App Store Small Business Program and for auto-renewable subscriptions after a subscriber's first year of paid service. In the downloadable Sales report, Customer Price and Developer Proceeds are both per unit, so multiply each by Units to get a row's total; refunds have negative Units. Sales and Trends figures are next-day estimates; Payments and Financial Reports hold the final proceeds."
faq:
  - q: "What is the difference between sales and proceeds in App Store Connect?"
    a: "Sales is the total billed to customers for your apps, bundles, and In-App Purchases, including any taxes Apple collects and remits. Proceeds is what you earn: Apple defines it as the customer price minus applicable taxes and Apple's commission. Under the standard terms proceeds are 70% of the price without tax, or 85% for Small Business Program members and for subscriptions after a subscriber's first year of paid service."
  - q: "Is Developer Proceeds in the Sales report per unit or per row?"
    a: "Per unit. Apple labels the column Developer Proceeds (per unit), and Customer Price is also the price per unit. A row with 100 units, a Customer Price of 0.99, and Developer Proceeds of 0.70 means 99.00 in sales and 70.00 in proceeds. Multiply both columns by Units before you add rows together."
  - q: "What commission does Apple take on App Store sales?"
    a: "Under the standard App Store terms, 30% of the price without tax. Members of the App Store Small Business Program, open to developers with up to 1 million USD in proceeds in the previous calendar year, pay 15%. Auto-renewable subscriptions also drop to 15% once a subscriber has accumulated one year of paid service. Japan and the European Union have separate Apple business terms with their own rates."
  - q: "Why don't Sales and Trends and Payments and Financial Reports match?"
    a: "Sales and Trends records a transaction when the customer starts it and estimates USD amounts from the previous month's average exchange rates. Financial reports count only settled transactions where Apple collected the customer's payment, group them by Apple's fiscal month, and use the exchange rate applied to your bank's currency. Apple also says proceeds in Sales and Trends aren't final."
  - q: "How do refunds appear in App Store Connect sales reports?"
    a: "In the downloadable Sales report a refund row has negative Units and a negative Customer Price, while Developer Proceeds stays positive, so multiplying proceeds by units gives a negative amount. Sales and Trends includes processed refunds in its daily unit totals, and you can add a filter to see the refund count on its own."
  - q: "Does AppMeta Pulse show proceeds or sales?"
    a: "Both. The Show Amount setting switches every amount between Proceeds, Apple's payout after commission and tax, and Sales, the full customer price. Pulse reads the daily Sales and Trends reports through the App Store Connect API, so its amounts are next-day figures, not the final numbers in Payments and Financial Reports."
mentioned_apps:
  - appmeta-pulse
read_time: "7 min read"
excerpt: "A reference to the money columns in App Store Connect: units, sales, proceeds, customer price, and developer proceeds, the 30% and 15% commission rates, where tax comes out, how refunds appear, and why Sales and Trends never quite matches Payments and Financial Reports."
last_updated: 2026-10-29
---

Sales is what customers paid. Proceeds is what you keep. In Apple's own words, proceeds are "the Customer Price minus applicable taxes and Apple's commission" ([Apple](https://developer.apple.com/help/app-store-connect/view-sales-and-trends/view-units-proceeds-sales-and-pre-orders/)). Below: which column holds which figure, which rate applies, and why the totals move from one report to the next.

## What does each number in App Store Connect mean?

Paraphrasing Apple's definitions for [Sales and Trends](https://developer.apple.com/help/app-store-connect/view-sales-and-trends/view-units-proceeds-sales-and-pre-orders/), the [Summary Sales Report](https://developer.apple.com/help/app-store-connect/reference/summary-sales-report), and the [financial reports](https://developer.apple.com/help/app-store-connect/reference/financial-report-fields/):

| Term | Where it appears | What it counts | Tax included | Commission removed |
|---|---|---|---|---|
| Units | Sales and Trends, Sales report | First-time purchases of an app or bundle, plus In-App Purchases. Sales and Trends leaves out updates and redownloads unless you filter them in. Refunds count as negative units | n/a | n/a |
| Sales | Sales and Trends | The total billed to customers for apps, bundles, and In-App Purchases | Yes, taxes Apple collects and remits | No |
| Proceeds | Sales and Trends | What you earn on those sales, as an estimate until the financial reports close | No | Yes |
| Customer Price | Sales report | The price per unit billed to the customer; negative on refund rows | Yes | No |
| Developer Proceeds | Sales report | What you receive per unit; stays positive on refund rows | No | Yes |
| Partner Share | Financial reports | Final proceeds per unit | No | Yes |
| Extended Partner Share | Financial reports | Quantity multiplied by Partner Share | No | Yes |

In the downloadable report, both money columns are per unit, which is easy to miss. Apple's sample row has 100 universal app purchases in the United States, where "Customers paid .99 USD for each unit and you received .70 USD for each" ([Apple](https://developer.apple.com/help/app-store-connect/reference/summary-sales-report)). That row is 99.00 USD of sales and 70.00 USD of proceeds. Add up the Developer Proceeds column without multiplying by Units and a busy app's revenue shrinks to a fraction of itself.

## How does a customer price turn into proceeds?

Per unit, the order of operations is:

**Developer Proceeds = (Customer Price − tax included in it) × your proceeds rate**

Apple's subscription terms spell out the order: you receive 70% of the price "minus applicable taxes", or 85% once the higher rate applies ([Apple](https://developer.apple.com/app-store/subscriptions/)). Tax comes off first, and the rate applies to what is left.

A rough example for a 4.99 EUR price in Germany, where the price includes 19% VAT:

| Step | Standard rate | Small Business Program or subscription year two |
|---|---|---|
| Customer Price | 4.99 | 4.99 |
| Price without 19% VAT | 4.19 | 4.19 |
| Proceeds rate | 70% | 85% |
| Developer Proceeds, about | 2.94 | 3.56 |

That is my arithmetic, not Apple's figure. Apple works out proceeds for each storefront from its own price points and tax rules, so the real figure can be a cent or two off. The same price point earns different proceeds in different countries because the tax inside the price differs, and Apple notes that it "may need to adjust prices or your proceeds due to changes in tax regulations or foreign exchange rates" ([Apple](https://developer.apple.com/news?id=y3w8ck7j)).

## What commission rates does Apple charge?

Under Apple's standard App Store terms:

| Situation | Commission | You keep |
|---|---|---|
| Standard rate on paid apps and In-App Purchases | 30% | 70% |
| App Store Small Business Program member | 15% | 85% |
| Auto-renewable subscription, first year of a subscriber's paid service | 30% | 70% |
| Auto-renewable subscription after one year of paid service | 15% | 85% |
| Any subscription, Small Business Program member | 15% | 85% |

The [Small Business Program](https://developer.apple.com/app-store/small-business-program/) is for developers who, together with any associated developer accounts, earned no more than 1 million USD in proceeds in the previous calendar year and stay under it in the current one. You have to enrol; it isn't automatic. Apple adjusts proceeds fifteen days after the end of the fiscal month in which it approves you. Cross the threshold during a year and the standard rate applies to future sales.

For subscriptions, the 85% rate follows days of paid service, counted per subscription group ([Apple](https://developer.apple.com/app-store/subscriptions/)). Free trials don't count toward the year; paid introductory offers do. If a subscription lapses and the customer comes back within 60 days, the count resumes. After 60 days it starts again. In the Sales report, rows earning the higher rate carry Rate After One Year in the Proceeds Reason column.

These are the standard terms. Storefronts in [Japan](https://developer.apple.com/support/app-distribution-in-japan/) and the [European Union](https://developer.apple.com/support/dma-and-apps-in-the-eu/) run under separate Apple business terms with their own rate tables, and Apple has changed both since 2024. If a large share of your sales comes from either, check those pages before modelling proceeds with the percentages above.

## Where does tax come out?

Apple's definition of Customer Price says it is "inclusive of any applicable taxes we collect and remit" ([Apple](https://developer.apple.com/help/app-store-connect/reference/summary-sales-report)). So sales, built from Customer Price, includes that tax, and proceeds never do. When you compare two storefronts at the same price, the one with the higher VAT or GST pays you less.

Income tax and withholding are a separate layer. They don't appear in Sales and Trends at all. Financial reports carry a Taxes and Adjustments field, and Apple applies any withholding tax when it makes a payment ([Apple](https://developer.apple.com/help/app-store-connect/getting-paid/view-payments-and-proceeds)).

## How do refunds show up?

In the Sales report, a refund row has negative Units and a negative Customer Price, while Developer Proceeds stays positive ([Apple](https://developer.apple.com/help/app-store-connect/reference/summary-sales-report)). Multiply proceeds by units, as you do for every row, and the refund subtracts itself. A Units value of 0 can mean a partial refund.

Sales and Trends folds processed refunds into its daily unit totals and shows them as negative units; to see the refund count on its own, add a filter. A refund appears on the day Apple processes it, which is rarely the day of the original purchase, so a quiet day can show negative proceeds.

## Why doesn't Sales and Trends match Payments and Financial Reports?

Apple's short answer is that Sales and Trends provides next-day data, while Payments and Financial Reports provide final proceeds ([Apple](https://developer.apple.com/help/app-store-connect/view-sales-and-trends/download-and-view-reports)). The reasons underneath, from Apple's page on [differences in reporting tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/differences-in-reporting-tools):

- Sales and Trends records a transaction when the customer starts it. Financial reports include only settled transactions where Apple collected the payment, so a purchase late in one month can land in the next fiscal month, and a payment Apple never collects never appears.
- Financial reports follow Apple's fiscal calendar, whose months run Sunday to Saturday and don't line up with calendar months. Sales and Trends reports use Pacific Time days.
- Sales and Trends estimates USD amounts from a rolling average of the previous month's exchange rates. Financial reports use the rate that converts each currency to your bank account's currency.
- Taxes, adjustments, and withholding appear only on the financial side.

Use Sales and Trends to see direction: which app sold, in which country, this week against last. Use the financial reports when the number has to match a bank statement.

## Where AppMeta Pulse fits

[AppMeta Pulse](/apps/appmeta-pulse/) is the iPhone dashboard I built for the daily look at these numbers. It downloads the daily Sales report and the subscription reports through the App Store Connect API with a key you create, keeps every day it fetches on the iPhone, and keeps Apple's names for things. The Show Amount setting switches every amount between Proceeds, Apple's payout after commission and tax, and Sales, the full customer price. Units count first-time downloads net of refunds. Each row is converted from its own currency into the display currency you pick, using the European Central Bank's monthly average rates, so converted amounts are estimates.

Pulse reads Sales and Trends, not Payments and Financial Reports. Its figures are next-day numbers with the same caveats as the Sales and Trends page itself. For subscription revenue on a monthly footing, the earlier post on [calculating MRR from the Subscription report](/journal/how-to-calculate-mrr-for-app-store-subscriptions/) covers the formula, and [this post](/journal/read-only-revenue-on-the-iphone/) explains why a quick revenue check belongs on the phone.
