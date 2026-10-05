# Direction sketch ("mock") spec

A mock is a high-fidelity HTML/CSS sketch of ONE style's first viewport, at desktop (1440×900) and mobile (390×844),
plus the start of the section below the fold where it fits. It is decision material for the owner: it must make the
style recognisable at a glance and honest about how the real page would look. It is NOT the build.

Board dir: /tmp/claude-0/-home-user-lagerland-apps-github-io/5553b341-96c8-5ef2-9d5c-b9201c3f3508/scratchpad/board
(below: <board>)

## File format — write exactly one file per style: <board>/mocks/<surface>-<a|b|c>.html
```
<!-- fonts: Display Family:400,700 | Text Family:400,400i,600 -->
<style>
  /* EVERY selector scoped under .s-<surface>-<x>  (e.g. .s-observa-a .hero{...}) — mocks share one page later */
  .s-observa-a{ --ink:#...; ... font-family:'Text Family',system-ui,sans-serif; }
  ...
</style>
<div class="s-observa-a mk mk--desktop"> ...desktop first viewport, exactly 1440×900, overflow hidden... </div>
<div class="s-observa-a mk mk--mobile">  ...mobile first viewport, exactly 390×844, overflow hidden...  </div>
```
- Fonts: the `<!-- fonts: ... -->` line lists Fontsource families with weights (`i` suffix = italic). The renderer
  self-hosts them from npm (@fontsource/<kebab-name>, latin subset). If a family/weight is missing the renderer prints
  MISSING/FONT ERROR — choose another weight/face then. Do not use @import, <link>, or any remote URL.
- Assets: relative paths only — `assets/<slug>/icon.png`, `assets/<slug>/s1.jpg`..`s4.jpg` (screenshots; Mac apps are
  landscape), `assets/qr/<slug>.svg` (QR), `assets/lagerland-mark.png`. Tare has no assets.
- App Store badge: paste the markup in `<board>/assets/appstore-badge.snippet.html` (Apple's official badge as inline SVG).
  Size it (min 120px wide desktop, ~140–170px is typical), frame it, place it in-world — never recolour or redraw it.
  Replace the Liquid `{{ ... }}` with `#` / the app name.
- No JavaScript. No external requests. No <img> of text. Inline SVG is allowed for icons, simple diagrams with countable
  elements, rules, frames, data graphics drawn from REAL numbers in the front matter. No SVG "illustrations" pretending to
  be art.
- Real copy only: use the app's real headline / subheadline / pre_headline / quick_answer / features / price.value /
  platforms from its front matter (you may abridge long subheadlines for the mock and should, if the style's form needs
  less text — note it). No lorem ipsum, no invented numbers, ratings or quotes. Demo data must be labelled "illustrative".
- Show in the desktop viewport: the microsite's own navigation, the offer (headline), the action (badge) and on desktop
  the QR "scan to install" in-world, the price statement, the signature move, and real product evidence (screenshot(s)
  or the world's demonstration of the mechanism). If the style places the quick answer in the first viewport, set it.
  Mobile: nav, offer, badge, price, product evidence, all readable at 390 (body ≥ 15px, no horizontal overflow).
- Craft floor applies (see context.md): no eyebrow kicker labels above headings, no card grids, no gradient text, no
  split-hero template, contrast AA, themed focus not needed in a static mock but text selection colour may be set.

## Render, inspect, fix (bounded: one inspect round + at most one fix round)
1. Make sure the board server is up: `curl -s -o /dev/null -w "%{http_code}" http://localhost:4200/render.mjs` must print
   200; if not: `cd <board> && nohup python3 -m http.server 4200 >/dev/null 2>&1 &` then wait 1s.
2. `cd <board> && node render.mjs mocks/<surface>-<x>.html` → writes `renders/<surface>-<x>-desktop.png` and
   `renders/<surface>-<x>-mobile.png` and prints which fonts loaded.
3. Open BOTH PNGs with the Read tool and judge them as the shipped screen: Does it read as THIS style (cover the name:
   could it be another product)? Is it a template skeleton in costume? A poster with no working parts? Is all text legible,
   nothing clipped or overflowing, the badge unmistakable, the mobile composition real (not a squeezed desktop)? Did
   fonts actually load?
4. Fix everything in one batch, re-render once, look once more. Stop.
