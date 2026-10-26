---
layout: journal
slug: app-store-connect-api-key-setup
title: "How to create an App Store Connect API key: team or individual, the right role, and a .p8 you only get once"
date: 2026-08-01
seo:
  title: "How to Create an App Store Connect API Key (.p8)"
  description: "Create an App Store Connect API key step by step: team vs individual keys, which role to pick, Issuer ID, Key ID, the one-time .p8 download, revoking."
  keywords:
    - "app store connect api key"
    - "how to create app store connect api key"
    - "app store connect api key p8"
    - "app store connect issuer id"
    - "app store connect team key vs individual key"
    - "app store connect api jwt"
    - "appmeta"
lede: "Every tool that talks to App Store Connect on your behalf, from fastlane to a Mac client like mine, starts with the same three things: an Issuer ID, a Key ID and a .p8 file. Creating them takes two minutes. Choosing the right kind of key and the right role is where people go wrong, and the .p8 download gives you exactly one chance."
quick_answer: "To create an App Store Connect API key, the Account Holder first requests API access once, in Users and Access > Integrations > App Store Connect API. After that, an Account Holder or Admin opens Team Keys, clicks Generate API Key (or + if a key already exists), names the key, picks its role under Access and clicks Generate. Download the .p8 private key straight away: the link works once and Apple keeps no copy. A tool then needs the Issuer ID (shown at the top of that page, the same for every team key), the Key ID (listed next to the key) and the .p8 file. Individual keys are generated from your own profile, carry only your own access, have no Issuer ID, and can't use provisioning, Sales and Finance or notaryTool. You revoke a key on the same page, and a revoked key can't be reinstated."
faq:
  - q: "How do I create an App Store Connect API key?"
    a: "Sign in as the Account Holder or an Admin, go to Users and Access, open Integrations and select App Store Connect API, then Team Keys. Click Generate API Key, or the + button if you already have a key, enter a name, choose a role under Access and click Generate. Then click Download API Key to save the .p8 file, and copy the Issuer ID from the top of the page and the Key ID from the key's row. The very first time, the Account Holder has to click Request Access and accept the terms before any key can be made."
  - q: "What is the difference between a team key and an individual key?"
    a: "A team key covers every app in the account, with the permissions of the role you pick when you create it, and its tokens use the Issuer ID. An individual key carries the access and roles of the user who created it, uses sub: user instead of an Issuer ID in its tokens, and can't use the provisioning endpoints, Sales and Finance, or notaryTool. Each user can have one active individual key at a time."
  - q: "Where do I find my App Store Connect Issuer ID and Key ID?"
    a: "Both are in Users and Access > Integrations > App Store Connect API. The Issuer ID is shown near the top of the page, with a Copy button, and it's the same for all of your team's keys. The Key ID is listed next to each active key; hover over it to see Copy Key ID. Individual keys show their Key ID on your profile, under Individual API Key."
  - q: "What if I lost my .p8 file?"
    a: "Generate a new key and revoke the old one. Apple lets you download the private key once, the download link disappears afterwards, and Apple doesn't keep a copy, so there is no way to download it again."
  - q: "Which role should an App Store Connect API key have?"
    a: "The least that covers the tool's job. You can't change a key's role later, so decide before you click Generate. Per Apple's permissions table, App Manager can create versions, edit App Store details, submit apps and manage TestFlight, In-App Purchases and Game Center, but can't reply to customer reviews or view Sales and Trends. Sales and Finance can read reports but not edit metadata. Admin can do all of it, and Apple notes that a key with the Admin role can also create and delete users."
  - q: "How long does an App Store Connect API token last?"
    a: "For most requests, at most 20 minutes. Apple rejects tokens whose lifetime, exp minus iat, is longer than that, except for a short list of read-only resources that accept scoped tokens for up to six months. Apple also recommends reusing one signed token for many requests until it expires, instead of signing a new token for each request."
mentioned_apps:
  - appmeta
read_time: "7 min read"
excerpt: "A step-by-step reference for App Store Connect API keys: requesting access, team keys versus individual keys, which role to choose, where the Issuer ID and Key ID live, why the .p8 downloads only once, how to store and revoke a key, and what the JWT signed with it contains."
last_updated: 2026-10-26
---

An App Store Connect API key is a key pair. Apple keeps the public half; you download the private half as a `.p8` file and use it to sign the short-lived tokens that every API request carries. A tool will ask you for four things, listed below with where each one lives.

## What does a tool need from you?

| Item | What it is | Where to find it |
|---|---|---|
| Issuer ID | A UUID that identifies your team, the same for every team key | Top of Users and Access > Integrations > App Store Connect API, with a Copy button |
| Key ID | A short ID for one key, such as `2X9R4HXF34` | Next to each key in the Active list; hover to Copy Key ID |
| Private key (.p8) | The private half of the key pair, a small text file | Download API Key link, available a single time |
| Role | What the key is allowed to do | Chosen under Access when you generate the key, fixed after that |

The `.p8` file is a PEM text file that begins with `-----BEGIN PRIVATE KEY-----`. If a tool complains that your key is the wrong format and the file says `BEGIN EC PRIVATE KEY`, you probably have a key made with OpenSSL, not one downloaded from App Store Connect.

## Team key or individual key?

Apple offers two kinds, and picking the wrong one causes more trouble than any of the setup steps.

| | Team key | Individual key |
|---|---|---|
| Who can create it | Account Holder or Admin | Most users, from their own profile (Account Holder, Admin, App Manager, Customer Support, Developer or Marketing), unless an Admin removed that permission |
| Access | All apps in the account, with the role you pick; app access can't be limited | The apps and roles of the user who made it |
| Can't use | Only what its role rules out | Provisioning endpoints, Sales and Finance, notaryTool |
| How many | Several; Apple lets you generate multiple | One active key per user |
| In the token | `iss` set to the Issuer ID | `sub` set to `user`, no `iss` |

Sources: Apple's [Creating API Keys for App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi/creating-api-keys-for-app-store-connect-api) and the [App Store Connect API help page](https://developer.apple.com/help/app-store-connect/get-started/app-store-connect-api).

Use a team key for anything that works for the whole account: CI, a metadata tool, a sales dashboard. Use an individual key when a script should only ever see what one person sees. Since individual keys can't read Sales and Finance, they're no use for revenue tools at all.

## How do you create a team key, step by step?

1. **Request access, once.** The Account Holder goes to Users and Access > Integrations, clicks Request Access, agrees to the terms and submits. Apple says requests are reviewed case by case.
2. **Open Team Keys.** In Users and Access > Integrations, with App Store Connect API selected in the left column, choose the Team Keys tab.
3. **Generate.** Click Generate API Key, or the + button if you already have an active key.
4. **Name it.** The name is only for you. Name it after the tool or the machine that will use it, so you know what breaks when you revoke it later.
5. **Pick the role.** Under Access, choose the role. Apple says you can't edit a key's name or access level afterwards; to change either, you revoke the key and make a new one.
6. **Click Generate**, then **Download API Key** next to the new key. Save the `.p8` before you leave the page.
7. **Copy the Issuer ID and Key ID** into the tool, along with the file.

An individual key is shorter: click your name at the top right, Edit Profile, then Generate Key under Individual API Key, and Download.

## Which role should the key have?

The roles for keys are the same ones you give people on your team. The rows below are from Apple's [role permissions table](https://developer.apple.com/help/account/access/roles), narrowed to what API tools usually do:

| Role | Edit App Store details | Create versions, submit apps | Reply to reviews | Sales and Trends reports |
|---|---|---|---|---|
| Admin | Yes | Yes | Yes | Yes |
| App Manager | Yes | Yes | No | No |
| Marketing | Yes | Create versions only | No | No |
| Customer Support | Yes | No | Yes | No |
| Developer | No | No | No | No |
| Sales | No | No | No | Yes |
| Finance | No | No | No | Yes |

Pick the smallest role that covers the job. A screenshot or metadata tool fits App Manager. A revenue dashboard fits Sales or Finance. A tool that edits metadata, replies to reviews and reads sales needs Admin, and Apple's docs single that role out: an Admin key can create and delete users. Keep that file somewhere better than your Downloads folder.

## Where should the .p8 file live?

Apple's guidance is short. Treat the private key like a password; don't share it, store it in a code repository or ship it in client-side code; and revoke it at once if it's lost or exposed. Apple keeps no copy, so the file you downloaded is the only one.

In practice that means a password manager, the macOS Keychain, or your CI provider's secret store, and then deleting the stray copy in Downloads. One key per tool helps too. Apple lets you generate multiple team keys, and if each tool has its own, revoking one doesn't take the others down with it.

## How do you revoke a key?

Revoking is immediate and permanent. Apple's [Revoking API Keys](https://developer.apple.com/documentation/appstoreconnectapi/revoking-api-keys) page says a revoked key can't be reinstated; revoked keys stay listed for 30 days under Revoked.

- For a team key, an Account Holder or Admin opens Users and Access > Integrations > App Store Connect API, chooses Team Keys, clicks Edit, selects the key, clicks Revoke Key and confirms.
- For someone else's individual key, it's the same place under the Individual Keys tab, again as an Account Holder or Admin.
- For your own individual key, open Edit Profile, find Individual API Key and click Revoke.

Revoke a key when a laptop holding the file is lost, when someone who had a copy leaves, and when you retire the tool that used it.

## What is a JWT, in one paragraph?

The API never sees your `.p8` file. Each request carries a JSON Web Token ([RFC 7519](https://tools.ietf.org/html/rfc7519)) that the tool builds and signs on your machine: a header saying it's signed with ES256 and naming your Key ID (`kid`), and a payload with your Issuer ID (`iss`), the time it was issued (`iat`), its expiry (`exp`) and the audience `appstoreconnect-v1`, optionally narrowed with a `scope` list of allowed requests. Apple checks the signature against the public half it kept, so a valid signature proves the request came from whoever holds the private key. Tokens with a lifetime over 20 minutes are rejected for most requests, and Apple suggests reusing one token across requests until it expires ([Generating Tokens for API Requests](https://developer.apple.com/documentation/appstoreconnectapi/generating-tokens-for-api-requests)).

```
Header:  { "alg": "ES256", "kid": "2X9R4HXF34", "typ": "JWT" }
Payload: { "iss": "57246542-96fe-1a63-e053-0824d011072a",
           "iat": 1528407600, "exp": 1528408800,
           "aud": "appstoreconnect-v1" }
```

Those are Apple's own example values: an exp 1,200 seconds after iat is exactly the 20-minute ceiling.

## What do the common errors mean?

A token App Store Connect won't accept usually comes back as 401 with the code `NOT_AUTHORIZED`. The usual causes are an Issuer ID and Key ID that don't belong together, a token signed with a different key than the one its `kid` names, a lifetime over 20 minutes, or a computer clock that's off. Apple's [status code table](https://developer.apple.com/documentation/appstoreconnectapi/about-the-http-status-code) lists 403 Forbidden for a revoked key, a badly formatted token, or an operation the key isn't allowed to do. If the token works for some requests and not others, it's the role. 429 means you've hit the rate limit for that key.

## How AppMeta uses your key

[AppMeta](/apps/appmeta/), the Mac client for App Store Connect I [wrote about in February](/journal/native-mac-client-for-app-store-connect/), takes a team key: it asks for the Issuer ID, the Key ID and the `.p8` file, so individual keys, which have no Issuer ID, don't fit it. Before it saves anything it signs a token and asks App Store Connect for your app list, so a mismatched ID or a revoked key shows up as an error on the setup screen, before you've saved anything.

The three values go into the macOS Keychain as items that stay on that Mac and don't sync through iCloud. AppMeta signs 20-minute ES256 tokens locally and reuses each one until it's about two minutes from expiring, and the only server it sends them to is `api.appstoreconnect.apple.com`. Removing the account in AppMeta deletes the Keychain items.

For the role: App Manager covers editing metadata in every localization, the [keyword field](/journal/app-store-keyword-field-100-characters/) included, plus creating and submitting versions. Replying to reviews and the sales views need a role that allows them, and for a single key that means Admin. If you'd rather keep revenue on a separate key, the [AppMeta Pulse API access page](/apps/appmeta-pulse/api-access/) lists the endpoints Pulse calls and the role it asks for.
