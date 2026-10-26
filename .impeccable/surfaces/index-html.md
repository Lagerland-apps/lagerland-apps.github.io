---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: ["_layouts/app.html"]
---

# Surface brief: homepage + app page template (site redesign v4 "The Issue")

Scope: homepage (`index.html`) in Persuade mode; app pages (`_layouts/app.html`) Persuade; comparison, journal, guides inherit the world in Read mode.
Audience: app shoppers on iPhone or desktop arriving from search, AI answers or App Store links. Job: find an app worth installing, get to its App Store page.
Proof on hand: 20 live apps, real icons and screenshots, catalogue prices, App Privacy labels, real testimonials. Never invent claims.
Constraints: SEO/AEO gate in repo CLAUDE.md, content visible without JS, self-hosted fonts, prices from catalog tokens, no owner name.

## Direction contract

THESIS: Lagerland Apps issues its apps the way a post office issues stamps: one sheet, twenty stamps, one designer. Refuses the dark SaaS hero with floating device mockups, gradient headline and stat bar.

OWN-WORLD: Postal-yellow printed sheet margin (selvedge) carrying masthead, headline and filters; cool white stamp paper ground; perforated stamps with a thick series-colour frame and pale tint field (five series: health green, planning vermilion-orange, money ochre, games plum, dev teal); postmark rings and wavy cancellation lines in ink; one postal blue reserved for the primary action and focus. Geometric postal sans (Jost) for display and denominations, Inter for body. Dashed cut lines, tabular numerals, no cards-in-cards, no gradients.

STORY: The visitor sees in one look that one maker in Finland makes twenty apps, all free of tracking; scans the sheet or filters by series; lifts the stamp they like and goes to the App Store.

FIRST VIEWPORT: Desktop: yellow selvedge column (~31%) left with headline "Twenty apps. One maker. No tracking in any of them.", one-paragraph lede and series filter tabs (Whole sheet in postal blue); right ~69% the perforated 5x4 sheet of all live apps in release order, each stamp with release date, denomination, icon, name, devices; newest app postmarked. Primary action: each stamp links to its app page, plus the blue App Store button under the sheet. Phone: selvedge on top, sheet as a two-column booklet.

FORM: Postage stamp sheet and stamp leaflet, candidate 3 of 7 on the ordered list. seed:0fefea83d39b6911. Raises kept: release order as record (clay tower), one hot colour for focus only (Polish poster), every stamp addressable (HyperCard), screen preview before opening (darkroom), only newest app postmarked (night city). Signature interaction: hovering/focusing a stamp lifts it off the sheet (rotate + shadow) and the sheet filters by series without reload; motion is one exponential ease-out lift.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
