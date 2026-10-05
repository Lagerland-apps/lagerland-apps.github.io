# Lagerland redesign — shape round (proposal only)

Status: **proposal, not implemented.** Nothing here is part of the site: Jekyll skips dot-folders, and
GitHub Pages builds only `main`. No site file was changed in this round.

Decisions the owner made:
- The owner picks one of three styles per page; only the winner ships.
- Every app page becomes a standalone microsite (own nav, type and structure). Only a thin footer strip links back to Lagerland.
- Code in every build phase is written by Sonnet subagents. The lead model owns design decisions and reviews.
- Nothing goes live without the owner's approval.

## What's here

| Path | What it is |
|---|---|
| `brief.md` | Shared brief every agent worked from: binding contract (permalinks, seo/schema/quick_answer, App Store elements), calibration rules, the dice protocol, the style-card anatomy |
| `cards/<page>.json` | 21 pages × 3 style cards. Each file holds the dossier, 7 grounded candidates, the dice seed, 3 styles (palette, faces, first viewport, page sequence, signature interaction, risks), a `specimen` and the `fixes` queued per style |
| `cards-before-enrich/` | The same cards as first composed, before specimens and fixes were attached |
| `issues/issues-*.json` | Cross-catalogue critique, 3 lenses (distinctness, truth/contract, feasibility): 175 issues |
| `issues/per-page/` | The same issues split per page. **Not yet applied to the cards** |
| `issues/_face-census.txt` | Typefaces shared across pages |
| `plan.json` | Rollout plan: 23 phases, one branch + one PR each (P0 foundation, P1 Observa pilot, P2 studio, P3–P20 one app each, P21 Tare, P22 hardening/docs) |
| `plan.before-renumber.json` | The plan as written, before it was renumbered to one PR per phase |
| `sketches/html/` and `sketches/png/` | Layout sketches drawn by Sonnet: studio A/B/C and Observa A/B/C, desktop 1440×1800 and phone 390×1688 |
| `previews/lagerland-redesign-board.html` | Self-contained board: every page's three styles (type/colour specimens), queued fixes, today's page, and the plan |
| `previews/lagerland-layouts-studio-observa.html` | Self-contained page showing the six layout sketches |
| `today/` | Screenshots of the current first viewports, for comparison |
| `tools/` | Render harness and build scripts. They contain absolute paths from the original cloud session, so adjust them before reuse |

## Not done (stopped to save session credits)
- The critique fixes are listed per style but not yet written into the cards.
- Layout sketches exist only for studio and Observa. The other 19 pages have cards and specimens only.
- The dice ran without the roll service's challenger catalogue (blocked by the network policy).

## Next step (awaiting owner)
1. The owner picks one style per page (at least studio + Observa).
2. P0, the no-visual-change foundation: contract includes, world dispatcher, SEO parity guard.
3. P1, the Observa pilot.

Each phase goes on its own branch and PR, and is merged only with the owner's approval.
