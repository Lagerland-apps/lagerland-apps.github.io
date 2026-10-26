---
name: Lagerland Apps
description: One maker in Finland issues his apps the way a post office issues stamps — one sheet, one stamp per app.
colors:
  postal-blue: "#1D3FD6"
  postal-blue-deep: "#1632B4"
  postal-blue-wash: "#E8ECFC"
  selvedge-yellow: "#F4C21B"
  selvedge-yellow-deep: "#E6B30F"
  selvedge-tab: "#FFF6D2"
  selvedge-ink: "#463C16"
  sheet-paper: "#F4F5F1"
  stamp-paper: "#FFFFFF"
  ink: "#15171D"
  ink-2: "#3F4452"
  ink-3: "#5A5F6D"
  rule: "rgba(21, 23, 29, 0.14)"
  rule-2: "rgba(21, 23, 29, 0.28)"
  cut-line: "rgba(21, 23, 29, 0.38)"
  ok-green: "#1E6B45"
  series-health: "#2B7556"
  series-health-tint: "#DCEFE3"
  series-plan: "#A33D22"
  series-plan-tint: "#FBE3D7"
  series-money: "#87610A"
  series-money-tint: "#F6EAC8"
  series-games: "#74357F"
  series-games-tint: "#EEDFF1"
  series-tools: "#1C6380"
  series-tools-tint: "#D8EBF1"
typography:
  display:
    fontFamily: "Jost, Futura, Avenir Next, Century Gothic, Inter, sans-serif"
    fontSize: "clamp(2.4rem, 4.8vw, 4rem)"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "Jost, Futura, Avenir Next, Century Gothic, Inter, sans-serif"
    fontSize: "clamp(1.85rem, 3.2vw, 2.6rem)"
    fontWeight: 650
    lineHeight: 1.06
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Jost, Futura, Avenir Next, Century Gothic, Inter, sans-serif"
    fontSize: "clamp(1.35rem, 2vw, 1.6rem)"
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: "-0.01em"
  denomination:
    fontFamily: "Jost, Futura, Avenir Next, Century Gothic, Inter, sans-serif"
    fontSize: "0.8rem"
    fontWeight: 700
    lineHeight: 1.2
    fontFeature: "\"tnum\""
  body:
    fontFamily: "Inter, -apple-system, SF Pro Text, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
    fontFeature: "\"cv11\", \"ss01\""
  lead:
    fontFamily: "Inter, -apple-system, SF Pro Text, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(1.15rem, 1.4vw, 1.25rem)"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "Inter, -apple-system, SF Pro Text, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 500
    lineHeight: 1.3
  imprint:
    fontFamily: "Inter, -apple-system, SF Pro Text, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "0.72rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.08em"
rounded:
  none: "0"
  sm: "2px"
  md: "3px"
  lg: "4px"
  app-icon: "22.5%"
spacing:
  s-1: "8px"
  s-2: "12px"
  s-3: "16px"
  s-4: "24px"
  s-5: "40px"
  s-6: "64px"
  s-7: "96px"
  s-8: "128px"
components:
  button-primary:
    backgroundColor: "{colors.postal-blue}"
    textColor: "{colors.stamp-paper}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "0 22px"
    height: "50px"
  button-primary-hover:
    backgroundColor: "{colors.postal-blue-deep}"
    textColor: "{colors.stamp-paper}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "0 22px"
    height: "50px"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.stamp-paper}"
  series-tab:
    backgroundColor: "{colors.selvedge-tab}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "10px 12px"
    height: "46px"
  series-tab-pressed:
    backgroundColor: "{colors.postal-blue}"
    textColor: "{colors.stamp-paper}"
  pill:
    backgroundColor: "{colors.stamp-paper}"
    textColor: "{colors.ink-2}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "4px 9px"
  stamp:
    backgroundColor: "{colors.stamp-paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "8px"
  card:
    backgroundColor: "{colors.stamp-paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.s-4}"
  topbar:
    backgroundColor: "{colors.selvedge-yellow}"
    textColor: "{colors.ink}"
    height: "60px"
  cta-band:
    backgroundColor: "{colors.selvedge-yellow}"
    textColor: "{colors.ink}"
    padding: "96px 24px"
---

# Design System: Lagerland Apps

## Overview

**Creative North Star: "The Issue"**

The studio publishes its apps the way a post office issues stamps: one printed sheet, one perforated stamp per app, one maker. Every surface is printed matter on light paper. The postal-yellow selvedge (the sheet's printed margin) carries the chrome: the top bar, the homepage masthead column, the screenshot band, the closing band and the footer. Cool sheet paper is the ground; white stamp paper carries anything that is "issued". Ink does the talking. A single postal blue is held back for the one thing a visitor should do and for keyboard focus.

Density is that of a stamp sheet and its leaflet: the homepage is a tight 5×4 grid of stamps with release date, denomination, icon, name and devices; an app page is the stamp's leaflet, a big stamp beside its headline, then printed columns separated by perforation rules. Structure comes from rules, dashed cut lines and series-coloured frames, never from boxed cards nested in cards. Motion has one gesture: a stamp lifts off the sheet (rotate, rise, deeper shadow) on an exponential ease-out.

Confirmed rejections (PRODUCT.md, owner 2026-10-26): not playful or toy-like, not corporate SaaS, not dark-first, not so minimal the apps get lost. The direction contract also refuses the dark SaaS hero with floating device mockups, gradient headlines and a stat bar.

**Key Characteristics:**
- Light only; printed paper, no dark theme.
- Postal-yellow selvedge for chrome and loud bands; cool paper ground; white stamp paper.
- Five stamp series, each a frame colour plus a pale tint, assigned from the app's category.
- Perforated edges, postmarks with wavy cancellation lines, dashed cut lines, tabular numerals.
- One postal blue: primary action, pressed filter, focus. Body links are ink.
- Jost (geometric postal sans) for display and denominations; Inter for reading.

## Colors

A printed-matter palette: one loud warm margin, cool paper, ink, five series inks, and one blue held in reserve.

### Primary
- **Postal Blue** (#1D3FD6): the primary action (App Store button under the sheet, primary buttons), the pressed series filter ("Whole sheet"), and every `:focus-visible` outline (3px). Hover deepens to **Postal Blue Deep** (#1632B4). Link text turns blue only on hover and focus. **Postal Blue Wash** (#E8ECFC) is its only tint.

### Secondary
- **Selvedge Yellow** (#F4C21B): the sheet's printed margin. Top bar, mobile nav drawer, homepage masthead column, se-tenant screenshot band, sticky download bar, closing band, footer, and text selection. **Selvedge Yellow Deep** (#E6B30F) is its pressed edge; **Selvedge Tab** (#FFF6D2) is a paper tab sitting on the margin (series filter tabs, highlighted plan). Secondary text on yellow is **Selvedge Ink** (#463C16, 6.6:1).

### Tertiary — the five series
Each series is a frame colour (`--s`) and a field tint (`--t`), set together by one series class. Frame colours also set the stamp's date and denomination text on its tint (all ≥4.6:1).
- **Health Green** (#2B7556 on #DCEFE3): health, fitness.
- **Planning Vermilion** (#A33D22 on #FBE3D7): productivity, lifestyle, education, books, and the default for any unmapped category.
- **Money Ochre** (#87610A on #F6EAC8): finance.
- **Games Plum** (#74357F on #EEDFF1): games.
- **Tools Teal** (#1C6380 on #D8EBF1): developer tools, business, graphics, utilities.

### Neutral
- **Sheet Paper** (#F4F5F1): page ground, the sheet behind the stamps.
- **Stamp Paper** (#FFFFFF): stamp paper, cards, tables, quotes, covers.
- **Ink** (#15171D): text, headings, body links, postmarks (at 78% opacity), heavy 2px top rules.
- **Ink 2** (#3F4452, 9:1): secondary text on paper.
- **Ink 3** (#5A5F6D, 5.8:1): tertiary text, meta, captions.
- **Rule** / **Rule 2** (ink at 14% / 28%): hairlines and pill borders.
- **Cut Line** (ink at 38%): dashed cut lines between sheet parts.
- **OK Green** (#1E6B45): positive status only.

### Named Rules
**The One Blue Rule.** Postal blue appears only on the primary action, the pressed series filter, link hover/focus, and focus outlines. Body links are ink with a 35% ink underline. If blue shows up anywhere at rest that isn't the thing to press, it is wrong.

**The Series From Category Rule.** A stamp's colour is never chosen by hand: it comes from the app's `category` through the series mapping, and frame and tint always travel together. A new category needs a mapping line, not a new colour.

**The Printed Paper Rule.** Light only. There is no dark theme; the world is paper and ink.

## Typography

**Display Font:** Jost (self-hosted variable, OFL; fallback Futura, Avenir Next, Century Gothic)
**Body Font:** Inter (self-hosted variable; fallback -apple-system, SF Pro Text, system-ui)

**Character:** Jost is the geometric postal sans of stamp lettering and denominations; Inter carries reading at a comfortable 17px. Both are self-hosted; no third-party font host.

### Hierarchy
- **Display** (Jost 700, clamp(2.4rem, 4.8vw, 4rem), 1, −0.025em): page H1. On the homepage selvedge it tightens to clamp(2.5rem, 4.1vw, 3.75rem) at 0.97 and an 11ch measure; on phones H1 drops to clamp(2.15rem, 10vw, 2.7rem).
- **Headline** (Jost 650, clamp(1.85rem, 3.2vw, 2.6rem), 1.06, −0.02em): section H2s, series headings.
- **Title** (Jost 600, clamp(1.35rem, 2vw, 1.6rem), 1.18): H3, app names on cards, pair and cover titles.
- **Denomination** (Jost 700, 0.8rem, tabular numerals): the price on a stamp, scaled up on the leaflet stamp (1.15rem) and plan stamps (clamp(1.5rem, 2.4vw, 2rem)).
- **Body** (Inter 400, 17px, 1.6, `cv11` `ss01`): running text; lead paragraphs at clamp(1.15rem, 1.4vw, 1.25rem) / 1.55 in Ink 2, max 60ch.
- **Label** (Inter 500, 13px): pills, meta, captions, crumbs.
- **Imprint** (Inter 500, 0.66–0.72rem, 0.06–0.22em tracking, uppercase): the printer's marginal text on the selvedge only (top-bar imprint, the rotated margin note, the sheet imprint line, footer meta).

### Named Rules
**The Tabular Numerals Rule.** Dates, denominations, tables, `time` and spec values set `tabular-nums`. A sheet is a record; its numbers line up.

**The Heading Stands Alone Rule.** No label line above a heading. The heading carries its own weight.

## Layout

A centred container of 1180px (narrow 800px, prose 720px) with 24px gutters, under a fixed 60px yellow top bar. The spacing scale is 8, 12, 16, 24, 40, 64, 96, 128px; sections breathe at 96px (64px under 720px), large sections at 128px. Full-bleed bands (screenshot strip, closing band) break out to 100vw.

The homepage "Issue" is a two-column spread: a yellow selvedge column at minmax(340px, 31%) with a dashed cut line on its right, and the sheet on the remaining width, filling the first viewport (clamp(660px, 100svh − 60px, 960px)). The sheet is a 5-column grid in first-release order with 8–12px gaps, closed by a sheet bar (screen preview, name, tagline, blue App Store button) above a dashed rule. Below 1180px the selvedge stacks on top and stamps take a 5:5.6 ratio; 4 columns under 860px; a two-column booklet under 640px.

App pages open with the leaflet: big stamp at minmax(260px, 0.8fr) beside the headline column at 1.2fr; single column under 980px. The leaflet body sets content as printed columns (auto-fit minmax(220px, 1fr)) under 2px ink top rules, with a perforation rule (a row of 2.6px holes) between sections and series-coloured 3px underlines on section heads, left-aligned.

Breakpoints observed: 1180, 980, 880, 860, 760, 720, 640, 560, 480px.

## Elevation & Depth

Mostly flat printed paper. Depth exists only where paper physically sits on paper: stamps on the sheet, and a lifted stamp in the hand. Stamp shadows are `drop-shadow` filters on the parent link, because the perforation mask on the paper would clip a box-shadow. Boxed cards outside the leaflet carry a 1px hairline shadow and lift to a soft long shadow on hover. Inside the leaflet body nothing is boxed and nothing casts a shadow.

### Shadow Vocabulary
- **Stamp at rest** (`filter: drop-shadow(0 1px 1.5px rgba(21,23,29,0.16))`): every stamp, shot and plan stamp lying on the sheet.
- **Stamp lifted** (`filter: drop-shadow(0 16px 16px rgba(21,23,29,0.26))`): hover, focus or selected stamp, with `translateY(-8px) rotate(-2deg) scale(1.05)`.
- **Elev 1** (`0 1px 1px rgba(21,23,29,0.08)`): cards at rest.
- **Elev 2** (`0 2px 4px rgba(21,23,29,0.08), 0 1px 1px rgba(21,23,29,0.06)`): app icons in lists and bars.
- **Elev 3** (`0 12px 22px -10px rgba(21,23,29,0.28)`): card and cover hover.
- **Elev 4** (`0 24px 44px -18px rgba(21,23,29,0.34)`): legacy hero screenshots.
- **App icon on stamp** (`0 3px 8px -2px rgba(21,23,29,0.35)`): the printed icon sitting on the stamp field.

### Named Rules
**The Lift Rule.** Shadows answer state, never decorate. A stamp lies flat until hovered, focused or selected, then lifts in one exponential ease-out (cubic-bezier(0.16, 1, 0.3, 1), 0.35s). Reduced motion removes the lift.

## Shapes

Stamps are square-cornered (0) with perforated edges cut by a radial-gradient mask (4px holes on the sheet, 6px on the leaflet stamp, 3px on mini stamps, 5px on screenshot stamps). Inside the perforation is a thick series frame: 3px on sheet stamps, plan stamps and screenshots, 5px on the leaflet stamp, 2px on mini stamps. App icons keep Apple's squircle (22.5%). Everything else is nearly square: 2px on buttons, pills, tabs, cards and inputs, never above 4px. The App Store badge keeps its own 10px. Lines do the structural work: 2px solid ink top rules open lists and columns, 1px dashed cut lines separate sheet parts and rows, 1px hairlines divide tables. Postmarks are two ink rings with a date plus four wavy cancellation lines.

## Components

### Buttons
Printed, square, quiet; one blue.
- **Shape:** near-square (2px), 50px tall, 22px side padding, Inter 600 at 15px.
- **Primary:** Postal Blue with white text, no shadow; hover deepens to Postal Blue Deep; `:active` presses down 1px.
- **Secondary:** transparent with a 1.5px ink border and ink text; hover fills with ink and turns the text white.
- **Focus:** 3px postal-blue outline, 2px offset.

### Chips (pills)
- **Style:** white stamp paper, 1px Rule 2 border, Ink 2 text at 13px, 2px corners. The price pill takes an ink border and ink text at 600. The privacy badge is ink-bordered uppercase.

### Series filter tabs
- **Style:** a two-column grid of paper tabs on the selvedge (Selvedge Tab ground, ink-20% border, 46px tall), each with a 12px series swatch and a tabular count.
- **State:** hover darkens the border to ink; pressed fills Postal Blue with white text and a white swatch. "Whole sheet" is server-rendered pressed. Filtering dims non-matching stamps to 22% greyscale without reload.

### Cards / Containers
- **Corner Style:** 2px.
- **Background:** Stamp Paper, 1px Rule border, 24px padding.
- **Shadow Strategy:** Elev 1 at rest, Elev 3 and −3px rise on hover (see Elevation).
- **Leaflet body:** cards dissolve into printed columns: no background, no border, no shadow, a 2px ink top rule and 16px top padding.
- **App card:** a mini stamp (84px, 64px on phones) beside the name and tagline, 4px series-colour top border.

### Navigation
- **Style:** fixed 60px yellow top bar with a dashed cut line beneath, a soft shadow once scrolled. Brand in Jost 700 at 1.3rem beside the 30px studio mark. Links are Inter 600 ink with a 2px underline bar: cut-line on hover, ink for the current page. A small uppercase imprint sits at the right on wide screens.
- **Mobile:** under 720px a yellow drawer slides in from the right (min(300px, 84vw)), links in Jost 1.4rem divided by dashed cut lines.

### The Stamp (signature)
Perforated white paper around a tinted field with a thick series frame. Top row: release date (Jost 500, tracked) and denomination (Jost 700), both in the series colour; centred app icon; name in Jost 700; devices in Ink 2 (up to two lines). Denomination and devices come from the catalogue, never typed. The newest app on the sheet alone carries a postmark over its top-right corner. On keyboard focus a 3px blue outline is drawn inside the frame.

### Leaflet stamp and postmark
The app page's large stamp (max 420px, 5:6, 6px perforation, 5px frame) does not lift on hover; a first-day postmark sits over its lower right.

### Se-tenant screenshot strip
Screenshots printed as a row of joined stamps on a full-bleed yellow band: each 270px wide, 10px perforated white paper, 3px series frame, horizontal scroll-snap.

### Denomination stamps (pricing)
Each plan is a stamp: series tint field, 3px series frame, 8px white outline and a ring of 4px paper-coloured holes; plan name in the series colour, price in Jost 700 tabular. Feature lists start on one shared line via subgrid.

### Pairs and covers
Comparisons are paired mini stamps (the competitor as a dashed blank stamp) with a Jost title; journal entries are white covers with a rotated postmark. Hover turns the title blue and tilts the mini stamp −3°.

### Quotes
A still row of printed quotes under 2px series-coloured rules, quote text in Jost 500. No auto-scrolling ticker.

### Closing band
Full-bleed Selvedge Yellow with dashed cut lines, centred text, 96px vertical padding, running straight into the yellow footer.

## Do's and Don'ts

### Do:
- **Do** take every colour from the `:root` tokens; components set series colour only through the series class (`--s` frame, `--t` tint).
- **Do** map a new app's category to a series in the series mapping before it ships; unmapped categories fall to Planning Vermilion.
- **Do** read prices, devices and app counts from the catalogue; never type them into a stamp, card or headline.
- **Do** give every stamp its small icon at `assets/icons/sm/<slug>.webp` (256px, generated by the icon script); a missing file prints a broken stamp.
- **Do** keep content visible without JavaScript: reveal and deal-in states apply only under `html.js`, with a force-visible fallback.
- **Do** separate sheet parts with 1px dashed cut lines and open lists and columns with a 2px ink top rule.
- **Do** set dates, denominations and tables in tabular numerals.
- **Do** keep app icons at Apple's 22.5% squircle and everything else at 2–4px or square.
- **Do** attribute everything to "Lagerland Apps".

### Don't:
- **Don't** use postal blue at rest for anything but the primary action, the pressed filter and focus; body links stay ink.
- **Don't** add a dark theme or dark sections; the world is printed paper.
- **Don't** put a label or kicker line above a heading; an overline directly above a heading is hidden by the stylesheet.
- **Don't** nest cards in cards, or box content inside the leaflet body.
- **Don't** use gradient fills, washes or gradient text; gradients only draw perforation holes, the FAQ plus sign and edge fades.
- **Don't** postmark more than the newest app on the sheet.
- **Don't** load fonts from a third-party host.
- **Don't** put the owner's personal name anywhere.
