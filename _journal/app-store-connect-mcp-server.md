---
layout: journal
slug: app-store-connect-mcp-server
title: "An App Store Connect MCP server that never sees your API key"
date: 2026-11-13
last_updated: 2026-11-13
seo:
  title: "App Store Connect MCP Server: Ask Claude About Your Sales"
  description: "Ask Claude, Cursor, or another AI app about your App Store sales. AppMeta Pulse for Mac serves your reports over MCP without ever seeing your API key."
  keywords:
    - "app store connect mcp server"
    - "app store connect mcp"
    - "ask claude about app store sales"
    - "app store sales ai assistant"
    - "mcp server for app store reports"
    - "claude desktop app store connect"
    - "cursor mcp app store connect"
    - "appmeta pulse"
lede: "AppMeta Pulse now runs on the Mac, and the Mac app includes an MCP server. Turn it on, and Claude, Cursor, or another AI app that supports MCP can answer questions from your own App Store Connect reports. The helper that serves those reports has no network access and never sees your API key. This post covers how it works, what the assistant can and can't read, and how it compares with the other ways to connect App Store Connect to an AI app."
quick_answer: "An App Store Connect MCP server lets an AI app such as Claude or Cursor read your App Store data and answer questions about it. AppMeta Pulse for Mac (macOS 14 or later) includes one. Turn on Settings › AI Assistants, and the app keeps a read-only SQLite copy of the reports it has downloaded from App Store Connect, which a bundled helper serves to the AI apps you connect. The helper has no network access, can't change anything, and never sees your API key. The feature is off until you turn it on and comes with AppMeta Pulse's full access (a subscription or Lifetime)."
faq:
  - q: "Is there an MCP server for App Store Connect?"
    a: "Yes, several. Open-source servers such as JoshuaRileyDev's App Store Connect MCP server and asc-mcp run on your computer and call Apple's API with your key. Appfigures offers an MCP server for the data in your Appfigures account. AppMeta Pulse for Mac includes one that serves a read-only copy of the reports Pulse has downloaded, through a sandboxed helper with no network access that never sees your API key."
  - q: "Can Claude read my App Store Connect sales?"
    a: "Yes, through an MCP server. With AppMeta Pulse for Mac, turn on Settings › AI Assistants, then add the helper to Claude Desktop or Claude Code with the setup the settings page copies for you. Claude can then query your sales, subscription, and review data and answer in plain words."
  - q: "Does the AI app get my App Store Connect API key?"
    a: "No. The .p8 key stays in AppMeta Pulse's Keychain, and the helper that serves your reports has no Keychain access. The AI app's configuration holds only the helper's path on your Mac, with no key, token, or vendor number in it."
  - q: "Can the assistant change my apps, prices, or listing?"
    a: "No. The helper accepts one read-only SQLite statement per query, works on a copy of your reports, and has no network access, so it can't reach App Store Connect at all."
  - q: "Does my data leave my Mac?"
    a: "AppMeta Pulse sends nothing to the AI app or its provider. What the AI app reads through the helper to answer you goes to that app and, for a cloud model, to its provider, under their terms, the same as anything you paste into a chat."
  - q: "Does the MCP server work on iPhone?"
    a: "No. It's part of AppMeta Pulse for Mac. The same purchase covers the iPhone and Mac apps, and the iPhone app points to the Mac feature in its Help & FAQ."
mentioned_apps:
  - appmeta-pulse
read_time: "7 min read"
excerpt: "AppMeta Pulse for Mac includes an MCP server for Claude, Cursor, and other AI apps. How it serves a read-only copy of Apple's own reports through a sandboxed helper with no network access and no API key, what the assistant can read, and how it compares with other App Store Connect MCP servers."
---

If you sell apps on the App Store, you've probably wanted to ask a plain question about your numbers and get a plain answer. Which countries grew this quarter? How many refunds last month? Did the price change hurt trials? App Store Connect has the data, spread across report files that need downloading, unzipping, and joining before they answer anything.

[AppMeta Pulse](/apps/appmeta-pulse/) now runs on the Mac, and the Mac app includes an MCP server, so an AI app can do that work for you. The assistant reads the same report files you could download yourself, and the part of Pulse that serves them can't reach the internet or your API key.

## What is an MCP server?

MCP, the [Model Context Protocol](https://modelcontextprotocol.io/), is an open standard Anthropic published in November 2024 for connecting AI apps to tools and data. An MCP server offers a few named tools. The AI app decides when to call them and reads what comes back. Claude Desktop, Claude Code, Cursor, and VS Code all support MCP servers.

For App Store Connect, it means you ask a question in plain words and the assistant fetches the rows it needs, instead of you exporting reports and pasting them into a chat.

## How does the AppMeta Pulse MCP server work?

1. In AppMeta Pulse for Mac, open Settings › AI Assistants and turn on "Let AI assistants read your reports". An alert explains what that allows before anything happens.
2. The Mac builds a SQLite copy of the reports Pulse has downloaded: Apple's rows and columns as they arrived, with nothing converted or summed. Pulse refreshes the copy after new reports come in.
3. The copy sits in a folder that only the app and its helper share. The helper is a small sandboxed app inside AppMeta Pulse. It can read that folder and nothing else: it has no network access, no Keychain access, and no access to the app's own data.
4. You add the helper to your AI app. The settings page has rows that copy the setup for you: a command for Claude Code, a JSON configuration for Claude Desktop, Cursor, and VS Code, or the helper's path.
5. The AI app starts the helper on your Mac and talks to it over standard input and output.

The configuration your AI app stores holds the helper's path and nothing more. There's no API key, token, or vendor number in it, because the helper never needs one.

The helper offers four tools:

| Tool | What it does |
|---|---|
| `describe_data` | A guide to the copy: how the tables are laid out, the mistakes to avoid, and each table's columns under Apple's own header names |
| `data_coverage` | Which reports are in the copy and which dates they cover, so the assistant can tell a missing day from a day with no sales |
| `query` | Runs one read-only SQLite statement, up to 5,000 rows, 60 KB, and about 10 seconds per call |
| `list_accounts` | The App Store Connect teams whose reports are shared on this Mac |

## What can the assistant read?

By default, the copy holds:

- Sales reports (daily, weekly, monthly, and yearly)
- Subscription reports and subscription events
- Customer reviews
- The lists of your apps and in-app products

Turn on Collect more reports (Settings › Data) and Pulse also keeps finance reports; Subscriber, offer code, and win-back reports; App Store analytics reports such as downloads, engagement, sessions, and installs and deletions; and your store setup: prices, availability, versions, and listing text. App Store Connect keeps no history of the store setup, so Pulse saves a new copy of a page each time it changes.

The assistant gets Apple's reports as delivered. It doesn't get anything Pulse calculates, such as MRR, and it doesn't get your API key or your settings. The guide in `describe_data` tells it how to read Apple's files correctly: filter by report frequency so a sale isn't counted four times, never add different currencies together, treat refunds as rows with negative units, and say which table and dates each number came from.

While the feature is on, Pulse also fills gaps in the copy. It downloads again every daily sales, subscription, and subscription event report Apple still serves (about the last year) and every yearly report from the last ten years that it doesn't already hold as Apple's original file. Settings shows what's still missing. Pulse keeps every file once it has it, so from the day you start, the copy keeps growing after Apple stops serving the older days.

## What can't it do?

- **Change anything.** The query tool takes one read-only statement against a copy. The helper can't write to that copy and can't reach App Store Connect.
- **See your API key.** The .p8 key stays in AppMeta Pulse's Keychain, and the helper has no Keychain access.
- **Run without you.** It's off until you turn it on. Turning it off, or the end of your full access, deletes the copy. The copy isn't synced to iCloud and isn't included in backups.

AppMeta Pulse sends nothing to your AI app or its provider. The rows the assistant reads to answer you do go to that AI app and, for a cloud model, to its provider, under their terms. That's the same path a report takes when you paste it into a chat yourself.

## How does it compare with other App Store Connect MCP servers?

Pulse isn't the only way to connect App Store Connect to an AI app, and the others suit different jobs:

- **Open-source servers**, such as [JoshuaRileyDev's App Store Connect MCP server](https://mcpservers.org/servers/JoshuaRileyDev/app-store-connect-mcp-server) and [asc-mcp](https://pypi.org/project/asc-mcp/), run on your computer and call Apple's API live with your key. Some go well beyond reports, managing TestFlight or app metadata, and the key they hold can do the same.
- **[Appfigures](https://appfigures.com/products/cli-ai)** offers an MCP server for the data in your Appfigures account, which adds store intelligence such as rankings and competitor data.
- **Hosted connectors**, such as [Truto's](https://truto.one/blog/connect-app-store-connect-to-claude-analyze-sales-user-reviews/), give you an MCP endpoint that calls App Store Connect from their servers.

AppMeta Pulse's server does less on purpose. It's read-only, it works from Apple's own report files, and it runs on your Mac with a helper that can't reach the network. If you want an assistant that can also edit your listing or ship builds, an open-source server is the better fit.

## Questions worth asking

The copy holds raw report rows, so questions like these work:

- Which territories grew most in proceeds this quarter compared with the same quarter last year?
- What share of last month's new subscriptions started with a free trial, per app?
- How many refunds did each app have in the last 90 days?
- What do this month's 1-star and 2-star reviews complain about most?
- What did my listing say in March? (Only if Collect more reports was on by then.)

The assistant does the arithmetic. Ask it to show the SQL it ran and which report and dates each figure came from. A year-over-year question only works once the copy holds both years.

## What do you need?

- A Mac with macOS 14 or later and AppMeta Pulse for Mac. One purchase covers the iPhone and Mac apps.
- Full access: a subscription or Lifetime ({P_MONTHLY@appmeta-pulse}/month, {P_YEARLY@appmeta-pulse}/year, or {P_LIFETIME@appmeta-pulse} once).
- Reports on the Mac, either through its own App Store Connect API key with the Admin role or through iCloud Sync from a device that has one.
- An AI app that supports MCP servers, such as Claude Desktop, Claude Code, Cursor, or VS Code.

If you already use AppMeta Pulse on the iPhone, install it on your Mac, turn on AI Assistants, and paste the setup into your AI app. The [AppMeta Pulse page](/apps/appmeta-pulse/) has the rest of what the app does, and [How to calculate MRR for App Store subscriptions](/journal/how-to-calculate-mrr-for-app-store-subscriptions/) is a good check on any MRR figure an assistant gives you.
