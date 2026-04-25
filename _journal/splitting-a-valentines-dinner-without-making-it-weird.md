---
layout: journal
slug: splitting-a-valentines-dinner-without-making-it-weird
title: "How to split a Valentine's dinner without making it weird"
date: 2026-02-14
lede: "It's the 14th. Somewhere right now, a group of four friends is staring at a $312 dinner bill, three of them ordered the steak, one ordered the salad, and someone is doing math on a napkin. RightSplit was built for that exact moment."
read_time: "4 min read"
excerpt: "A short Valentine's-adjacent post on RightSplit's design philosophy: scan the receipt, split items fairly, send shares via iMessage or WhatsApp, no shared Splitwise account required. Why item-level splitting beats equal-split for groups of more than two."
---

It is February the 14th. Somewhere in the world right now, a table of four friends is staring at a $312 receipt at the end of a dinner. Three of them had the steak. One had the salad and a glass of wine. Someone is doing math on a napkin.

This is a small post about that exact moment, and the app I built for it.

## Why "split equally" is unfair

The default in most splitting tools is to divide the bill into equal shares. This works when the table ordered roughly the same things. It is unfair the moment the orders diverge.

Equal-splitting punishes the lighter eater. The salad-and-wine person at our hypothetical table pays $78, when their actual order was closer to $32. They will not say anything because the maths is awkward and the social cost of asking exceeds the $46 in question. They will quietly resent it, the next dinner will feel slightly different, and over a year of small inequalities the friendship loses a little bit of trust without anyone being able to point at the moment it happened.

The fix is item-level splitting. It takes thirty seconds with the right tool. Without one, it takes ten minutes and a calculator.

## The Splitwise problem

The dominant solution to this problem in the early 2020s was Splitwise. It works, with one structural friction: every participant has to have an account. The four friends at the table are now signing up for an app that will email them about IOUs for the next eight months because one of them couldn't be bothered to settle.

For a recurring group — roommates, a partnership, a regular travel circle — that overhead is fine, even valuable. For a one-off Valentine's dinner with friends, it's a tax on the relationship that nobody asked for.

[RightSplit](/apps/rightsplit/) is built around the opposite premise: **the group should not need to download anything**. Only the person doing the math has the app.

## The flow

The version that lives in my head when I think about RightSplit's job:

1. The receipt arrives. One person picks up the phone.
2. They take a picture of the receipt. The app reads the items, prices, and tax.
3. They drag each item onto a person's avatar. Bottle of wine? Drag it onto two people, the app splits it 50/50. Round of beers shared by three? Same. Steak? Drag onto the person who ordered it.
4. Tip is calculated and distributed proportionally.
5. The app produces four small messages — one per person — with the exact amount and a payment app deeplink (Venmo, PayPal, iMessage Cash). The owner sends them in iMessage or WhatsApp.
6. Done. The app remembers the split for future reference if the owner cares to look.

That's the whole product. There's no shared account, no notification storm, no IOU ledger that follows you around for nine months. The group never has to install RightSplit. The friction lives entirely with the person who's already holding the phone.

## What item-level splitting buys at scale

The interesting thing about this design is what happens when groups get bigger.

For two people, item-level vs. equal split rarely matters. The amounts are small.

For four people, item-level splitting recovers an average of $20-40 per dinner over equal-split, in the favour of whoever ordered modestly. That's small, but it's the kind of small that compounds across a year of group meals.

For ten people — bachelor parties, family dinners, work outings — item-level vs. equal-split can be a $80-150 swing per person. At that point, equal-splitting isn't just unfair; it's the thing that turns a fun dinner into an awkward Venmo argument the next morning.

[RightSplit](/apps/rightsplit/) Pro adds item-level splitting, uneven splits (the person with the bigger appetite explicitly takes a 1.5× share), per-person tip breakdowns, and split history. $1.99 a year, or $7.99 lifetime. The free tier covers equal-split and tip calculator, which is enough for most two-person scenarios.

## A note on small kindnesses

There's a category of software that exists specifically to remove a tiny amount of friction from human relationships, and I'd argue this category is undervalued. The financial impact of any individual split is small. The relational impact of *not* having the awkward conversation about the bill is non-trivial. Friends remember small kindnesses; they remember small inequalities even more.

If you went out to dinner tonight and someone is staring at a receipt right now, consider this the offhand suggestion that there's a calmer way to handle the math.

Happy 14th.
