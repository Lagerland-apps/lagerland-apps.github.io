# Reviewer brief: Dutch (nl, Netherlands) Tier 4, batch 2 (journal posts)

Follow `_i18n/nl-tier4-review-brief.md` in full (steps 1 to 5 and «Reply with»). Differences for batch 2:

- The writers followed `_i18n/nl-tier4b2-brief.md` (read it: per-post notes, extended keyword-collision list, the rule that comparison
  links stay English, local-only front matter).
- Sources are saved under
  `/private/tmp/claude-501/-Users-anttiaittamaa-Downloads-githubcode/b562e572-a501-462e-86d4-d96e70f0914a/scratchpad/nl-t4b2/sources/<slug>/`.
  Re-fetch each one live and check every claim that rests on it, claim by claim. Delete or soften any claim no saved source or
  app fact supports.
- Six posts are LOCAL-ONLY (no English twin): hoeveel-diepe-slaap, hartslag-in-rust, slaaptekort-inhalen, progressive-overload,
  sets-per-spiergroep-per-week, feestdagen-2027. For these, the «fact diff» is against the saved sources and the app facts:
  every number, study, threshold, date and recommendation must be in a source the writer saved (or in `_apps/<slug>.md`, the
  Dutch app page, the glossary or APP_BLUEPRINT.md §10). Compare with the French/German/Spanish/Italian model named in the brief
  to catch a claim the model sourced differently. Health posts keep a plain «geen medisch advies» line.
- feestdagen-2027: recompute every weekday with `python3 -c "import datetime; ..."` and check every date against the saved
  rijksoverheid.nl page.
- The batch 1 reviewers' must-fix list is the sheet paragraph «From the Tier 4 reviews (2026-11-19)» in `_i18n/nl.md`.
