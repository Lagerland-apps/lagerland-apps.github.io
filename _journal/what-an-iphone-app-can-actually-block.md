---
layout: journal
slug: what-an-iphone-app-can-actually-block
title: "What an iPhone app can actually block, and what it structurally cannot"
seo:
  title: "How App Blockers Work on iPhone: What Can Be Blocked"
  description: "How iPhone app blockers really work: the three Apple frameworks, why the app picker hands back opaque tokens, and why no on-device blocker is unbypassable."
  keywords:
    - "how app blockers work iphone"
    - "screen time vs app blocker"
    - "family controls api"
    - "can an app block instagram iphone"
    - "app blocker that cannot be bypassed"
    - "iphone app blocker bypass"
    - "managedsettings shield"
    - "deviceactivity framework"
date: 2026-07-29
lede: "No third-party iPhone app blocks anything by itself. It asks iOS to do the blocking, through three Apple frameworks with sharp, published limits. Those limits explain why your blocker cannot name the apps you blocked, why notifications still arrive, and why every honest answer to 'can this be bypassed' is yes."
quick_answer: "On iPhone, no third-party app blocks anything itself. It asks iOS to, through three Apple frameworks: FamilyControls (authorisation plus the system app picker), ManagedSettings (which draws the shield over your chosen apps), and DeviceActivity (schedules and usage thresholds). The picker returns opaque tokens, so the blocker never learns which apps you chose. It can shield apps, whole categories, and Safari domains. It cannot silence notifications, reach your other devices, or survive you revoking its authorisation in Settings. Every on-device blocker is friction, and the only honest measure is how long the way out takes."
faq:
  - q: "Can an app block Instagram on iPhone?"
    a: "Yes. Using Apple's ManagedSettings framework, a third-party app can shield the Instagram app so that tapping it shows a blocking screen instead of launching it, and can shield instagram.com in Safari if you include web content in the selection. What it cannot do is stop Instagram notifications from arriving, block Instagram on your iPad or laptop, or stop you from revoking the blocker's authorisation in Settings, which drops every shield at once."
  - q: "Is there an app blocker that cannot be bypassed?"
    a: "Not on your own iPhone. Apple deliberately keeps revocation in the user's hands: you can always withdraw Family Controls authorisation in Settings, which voids the blocker's tokens and removes every shield. A blocker can prevent its own deletion and add friction such as a math problem or a delay, but it cannot make itself permanent. The only genuinely hard case is a device where somebody else holds the Screen Time passcode, which is parental control, not self-restriction."
  - q: "What is the Family Controls API?"
    a: "FamilyControls is the Apple framework that gates the whole Screen Time API. It does two things: it asks the user for authorisation, in either individual mode (self-restriction) or child mode (a Family Sharing parent managing a minor), and it presents FamilyActivityPicker, the system UI where the user selects apps, categories, and web domains. It hands back a FamilyActivitySelection of opaque tokens. Shipping it on the App Store needs a restricted entitlement that Apple grants on request."
  - q: "Do app blockers work without an internet connection?"
    a: "Family Controls blockers do. The shield state lives in a local ManagedSettingsStore and is enforced by iOS itself, so airplane mode changes nothing. DNS and VPN content filters are the opposite case: they only ever see network traffic, so they do nothing about an app that works offline or content already cached on the device, and toggling the profile off in Settings removes them outright. Offline resilience is one of the clearest dividing lines between the two approaches."
  - q: "Can an app blocker see which apps I blocked?"
    a: "No, and this is enforced by iOS rather than promised by the developer. Apple's picker returns tokens, which Apple's own documentation describes as representations that do not reveal an activity's identity. The blocker stores a token, passes it back to ManagedSettings to apply a shield, and never receives a bundle identifier or a display name. It cannot log your selection, sell it, or leak it, because it never had it."
  - q: "Screen Time or a third-party app blocker?"
    a: "Built-in Screen Time is free, covers every device signed into the same Apple Account when Share Across Devices is on, and can be locked with a passcode someone else holds. Its weakness is the escape: your own passcode, or the Ignore Limit button. A third-party blocker uses the same enforcement machinery but can change what the unlock costs and can paint a far more useful shield. Many people are best served running both."
mentioned_apps:
  - earnlock
read_time: "13 min read"
excerpt: "A third-party iPhone app cannot see what you open, run continuously in the background, or draw over another app. Here is what the Screen Time API actually permits, what the opaque-token design means for privacy and for product, and an honest ladder of every way out of a shield."
---

Ask most people how an app blocker works on iPhone and you get some version of this: the blocker sits in the background, watches what you open, and slams a door when it spots Instagram.

None of that is possible. A third-party iOS app cannot see which apps you launch, cannot run continuously in the background to watch for one, and cannot draw a single pixel over another app. Every blocker on the App Store works by asking iOS to do the blocking on its behalf, through three frameworks Apple shipped in 2021 and has extended in small increments since.

That distinction is not pedantry. It decides what your blocker can do, what it will never do no matter how much you pay, and — the part nobody puts in the App Store screenshots — exactly how you get out.

## What actually blocks an app on an iPhone?

Three frameworks, collectively the Screen Time API, introduced in the WWDC21 session [Meet the Screen Time API](https://developer.apple.com/videos/play/wwdc2021/10123/). A fourth, ManagedSettingsUI, only controls how the blocking screen looks.

| Framework | Its one job | The types you actually touch | What it cannot do |
|---|---|---|---|
| [FamilyControls](https://developer.apple.com/documentation/familycontrols) | Get permission, and let the user choose apps | `AuthorizationCenter`, [`FamilyActivityPicker`](https://developer.apple.com/documentation/familycontrols/familyactivitypicker), [`FamilyActivitySelection`](https://developer.apple.com/documentation/familycontrols/familyactivityselection) | Tell your code which apps were chosen |
| [ManagedSettings](https://developer.apple.com/documentation/managedsettings) | Apply the restriction | `ManagedSettingsStore`, [`ShieldSettings`](https://developer.apple.com/documentation/managedsettings/shieldsettings) (`.applications`, `.applicationCategories`, `.webDomains`), [`ApplicationSettings`](https://developer.apple.com/documentation/managedsettings/applicationsettings) (`denyAppRemoval`) | Outlive the authorisation that created it |
| [DeviceActivity](https://developer.apple.com/documentation/deviceactivity) | Anything to do with time | `DeviceActivityCenter`, `DeviceActivitySchedule`, [`DeviceActivityEvent`](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent), `DeviceActivityMonitor` | Run your code continuously — the extension wakes on events only |
| [ManagedSettingsUI](https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration) | Style the shield | `ShieldConfigurationDataSource`, `ShieldActionDelegate` | Anything except draw a title, subtitle, icon and up to two buttons |

The sequence in a real app is short. Ask for authorisation through `AuthorizationCenter.shared`, in `.individual` mode for self-restriction or `.child` mode for a Family Sharing parent. Present the picker. Put whatever came back into a `ManagedSettingsStore` as `store.shield.applications`. Register a schedule with `DeviceActivityCenter`, and let your `DeviceActivityMonitor` extension get woken at interval boundaries and usage thresholds to change the store.

Two practical gates are worth knowing before you assume the category is bigger than it is. The Family Controls capability adds the [`com.apple.developer.family-controls`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.family-controls) entitlement, and distributing it on the App Store requires asking Apple for it. And the `DeviceActivityMonitor` extension is not a daemon: iOS wakes it, gives it a short slice of time, and suspends it. Anything a blocker claims to do "continuously" is really doing it at Apple's chosen moments.

## Why the blocker never learns which apps you picked

This is the single most consequential design decision in the whole API.

The app-selection UI is `FamilyActivityPicker`, and it is Apple's, not the developer's. It renders out of process, it lists your installed apps, and what it returns is a `FamilyActivitySelection` containing sets of tokens: `ApplicationToken`, `ActivityCategoryToken`, `WebDomainToken`. Apple's documentation for [`Token`](https://developer.apple.com/documentation/managedsettings/token) describes it as a representation of an app or website "that doesn't reveal its identity," and the `ApplicationToken` page says the point is to restrict and filter apps without access to personal user data.

So a blocker holds an opaque blob. It hands that blob back to ManagedSettings to raise a shield. It never receives a bundle identifier or a display name. There is no way to reverse it. A token is also only meaningful to the app that received it, and it stops working the moment you revoke authorisation in Settings, because revocation invalidates the app's tokens along with its permission.

The privacy consequence is real and worth saying plainly: a screen-time app physically cannot log that you blocked Grindr, or Robinhood, or your ex's favourite app. Not "promises not to" — cannot. That is privacy by construction, and the strongest such guarantee in any category I have shipped into.

The product consequence is a genuine tax, and every developer in this category pays it:

- You cannot offer a one-tap "block the usual suspects" onboarding, because you cannot name the suspects.
- You cannot tell the user, in your own copy, which apps are currently shielded.
- You cannot verify from your own data that a user selected anything at all, which makes support ("it isn't blocking anything") an exercise in guided screenshots.

That trade is Apple's to make, not the developer's. I think it is the right one.

## Which approach blocks what?

Five approaches get sold as "app blocking", and they intercept at completely different layers. The column that matters is not price, it is where each one sits in the stack.

| Approach | What it blocks | What it cannot block | How it is bypassed | Works offline | Who it actually suits |
|---|---|---|---|---|---|
| **Built-in Screen Time** ([Apple's setup guide](https://support.apple.com/guide/iphone/set-up-screen-time-iphbdf9d5495/ios)) | App and category time limits, Downtime, content ratings, web content; syncs across your devices with Share Across Devices | Nothing beyond Apple's own categories; no custom unlock condition | Your own passcode, or the Ignore Limit button | Yes | Anyone who has not tried it — free, and it covers the Mac and iPad too |
| **Family Controls shield app** (Opal, one sec, ScreenZen, Jomo, EarnLock) | Any app or Apple category you select, plus Safari web domains, on this iPhone | Notifications, other devices, and anything after you revoke authorisation | Whatever escape hatch the app ships, then revoking authorisation in Settings | Yes — state is local and enforced by iOS | People who want a different unlock condition than "wait" or "type your passcode" |
| **DNS or VPN content filter** ([NetworkExtension](https://developer.apple.com/documentation/networkextension)) | Domains and traffic patterns, system-wide, including apps you did not select | Anything on cellular when the profile is off, encrypted DNS inside an app, or a service sharing a CDN with something you need | Toggle the VPN off in Settings, roughly three taps | No — it is a network mechanism by definition | Blocking whole classes of content (ads, adult sites) rather than a named app |
| **Separate device or lockbox** (dumbphone, timer safe, Brick's NFC tag) | Everything on the device you left behind | Every other screen in the building | Physically retrieving the object | Yes | People whose problem is one hour, one place — writing sessions, dinners, sleep |
| **Grayscale and friction** (Color Filters, Focus modes, apps off the Home Screen) | Nothing — it just makes the phone duller and slower to reach | Anything, if you actually want it | Three taps in Settings, or Spotlight | Yes | Drift rather than compulsion — the person who opens an app for no reason and stays for 40 minutes |

Two honest notes on that table. A DNS filter is the only row that touches apps you did not enumerate, which is why it is the right tool for adult-content blocking and the wrong tool for "keep me off X between 9 and 5." And Apple's own review rules constrain the VPN row: [App Store Review Guideline 5.4](https://developer.apple.com/app-store/review/guidelines/) requires VPN apps to use `NEVPNManager` and to come from a developer enrolled as an organisation, and the content-filter entitlement is granted case by case, which is why so few of these exist.

## Can an app block Instagram on iPhone?

Yes. Then three caveats that matter more than the yes.

**The app, properly.** Select Instagram in the picker, put the token in `store.shield.applications`, and tapping the icon shows a shield instead of launching the app. The app does not open in the background, does not refresh, does not get its five seconds.

**The website, mostly.** `ShieldSettings.webDomains` covers Safari. Selecting web content in the picker is what makes instagram.com in Safari behave the same way as the app. Coverage inside third-party browsers and in-app web views is less predictable, and I would not build a plan around it.

**Not the notifications.** A shield stops a launch. It does not stop delivery. If a badge and a banner are what pull you in, the shield is fixing the wrong half of the loop, and a Focus mode is the better tool — or both together.

**Not your other screens.** The store is local to the device. Your iPad, your Mac, and the work laptop are all untouched. Family Controls does not ship on macOS in a form that supports this mechanic, so any shield app that does cover the Mac is doing it with a different mechanism.

## Is there an app blocker that cannot be bypassed?

No. Not on a device you own and control, and the reason is deliberate: if a third-party app could permanently restrict your phone, the first malicious app to ship would brick a lot of phones. Apple keeps the exit in your hands on purpose.

So the useful question is not whether there is a way out — there always is. It is how long the way out takes, and whether the effort lands somewhere useful. Here is the actual ladder, cheapest first.

| Way out | Roughly how long | What it costs you | Can the app tell? |
|---|---|---|---|
| Tap-through or "I really need this" button, if the app ships one | 1–2 taps, under 5 seconds | Nothing | Yes — it fired the action |
| Wait out a timer or a breathing pause | 5–60 seconds | Attention, the currency you were defending | Yes |
| Solve a gate — a math problem, a long typed phrase | 20–60 seconds | Concentration, which is the point | Yes |
| Delete the blocker | ~10 seconds, unless `denyAppRemoval` is set | Your settings, history, streak | No — it is gone |
| Revoke Family Controls in Settings | ~15 seconds if you know the path | Every shield drops at once; tokens are voided | Yes — [`authorizationStatus`](https://developer.apple.com/documentation/familycontrols/authorizationcenter/authorizationstatus) is observable |
| Turn off Screen Time entirely | ~20 seconds | Your limits and your usage history | Yes |
| Erase and restore the device | 30+ minutes | Everything | No |
| Someone else holds the Screen Time passcode | Not available to you | Autonomy — a real cost, sometimes worth paying | N/A |

Two rows deserve comment. `ApplicationSettings.denyAppRemoval` is real: a blocker can prevent app deletion device-wide, which closes the cheapest exit. And revocation is observable — an app can watch its own authorisation status and know the moment you walked out. Whether it should do anything with that, beyond quietly recording it for you, is a design question with an obvious wrong answer.

Read down that ladder and "unbypassable" collapses. The only real variable is how many seconds sit between the impulse and the app, and whether those seconds buy you anything.

## What the API reality means for design

I wrote a while ago that [the unlock cost has to live outside the app](/journal/unlock-cost-outside-the-app/) — that a cost you set yourself, inside the software, is a cost your craving can renegotiate from inside the moment of craving. The API reality above is the structural version of the same argument. Since revocation is always about fifteen seconds away, the wall is not the product. The price is.

And the price should be paid somewhere your future self benefits. Time-of-wait fails that test: you pay in attention, which is exactly what you were trying to protect, and you get nothing back. Body movement passes it, because the cost lands in the rest of your life.

That is not the same as saying the other designs are wrong. Several are good for problems mine does not solve:

**[one sec](/alternatives/one-sec/)** interrupts *before* the app opens — a breath, a pause, a question. If your problem is that your thumb arrives before your intention does, that is a better-shaped intervention than a hard gate, because the reflex is what it targets. A gate you have already earned past does nothing about a reflex. one sec also runs on Android, which nothing of ours does.

**[Brick](/alternatives/brick/)** puts a physical NFC tag in the loop, around $59 one time. Leaving the tag at home is a commitment you cannot undo from the couch, and it is the only design in the category where the friction is made of atoms rather than software you authorised. The cost is that you have an object to buy, carry, and lose. [Unpluq](/alternatives/unpluq/) works on the same physical principle, paired with a subscription.

**[ScreenZen](/alternatives/screenzen/)** is free, with escalating pauses, and free is a real advantage that a $19.99 tier does not erase. **[Opal](/alternatives/opal/)** and **[Jomo](/alternatives/jomo/)** are more polished than we are, and Jomo covers iPhone, iPad, and Mac.

[EarnLock](/apps/earnlock/) uses exactly the same three frameworks as all of them. It is not doing anything Apple does not publish. What it changes is the price: your selected apps stay shielded until you hit a daily activity goal read from Apple Health — steps in the free tier, active minutes or active energy in Premium — and the shield is a `ShieldConfiguration` extension that paints a live progress ring with the number remaining instead of Apple's generic restriction screen. *3,412 steps until unlock* is a destination. *This app has been restricted* is a wall. The Apple Watch app reads HealthKit on the wrist, so the count keeps running on a walk without the phone. $1.99/month, $9.99/year, or $19.99 once, each price checked in August 2026.

The honest constraints are the same ones on this page. EarnLock cannot see which apps you blocked either. It does not stop notifications. It is iPhone and Apple Watch only, and there is no iPad or Mac version because the framework does not support the mechanic there. It ships one math-gated emergency unlock per day, on purpose, because a tool with no exit is a tool people delete. And if you open Settings and revoke its authorisation, every shield drops and there is nothing it can do about that — which is true of every Family Controls app named on this page, and worth knowing before you pay any of us. (The data discipline behind that, and every other Lagerland app, is on the [transparency page](/transparency/).)

## TL;DR

- **No third-party iPhone app blocks anything itself.** It asks iOS to, via FamilyControls (permission and the picker), ManagedSettings (the shield), and DeviceActivity (schedules and thresholds).
- **The picker returns opaque tokens, not app names.** Your blocker cannot log, sell, or leak which apps you chose, because iOS never gives it the names — and it also cannot pre-fill a recommended list for you.
- **A shield blocks launching, not notifying.** It covers the app and, via web domains, Safari. It does not cover your iPad, your Mac, or the banner that pulled you in.
- **Nothing is unbypassable, by Apple's design.** Revoking Family Controls in Settings takes about fifteen seconds and voids every shield at once. `denyAppRemoval` closes the cheapest exit; nothing closes the last one.
- **So compare the price, not the wall.** The only real variable is what stands between the impulse and the app — a tap, a wait, a physical tag, or a step count — and whether paying it leaves you better off.
