# Reviewer brief: Dutch (nl, Netherlands) Tier 4, batch 3 (journal posts)

Follow `_i18n/nl-tier4-review-brief.md` in full (steps 1 to 5 and «Reply with»). Differences for batch 3:

- The writers followed `_i18n/nl-tier4b3-brief.md` (read it: per-post notes, extended keyword-collision list, comparison links to the Dutch
  page where `nl/alternatives/<slug>.html` exists, local-only front matter).
- Sources are saved under
  `/private/tmp/claude-501/-Users-anttiaittamaa-Downloads-githubcode/b562e572-a501-462e-86d4-d96e70f0914a/scratchpad/nl-t4b3/sources/<slug>/`.
  Re-fetch each one live and check every claim that rests on it, claim by claim. Delete or soften any claim no saved source or
  app fact supports.
- Nine posts are LOCAL-ONLY (no English twin): ontwormen-hond, vlooien-hond, vo2max, remslaap, warming-up-krachttraining,
  foto-verkleinen-iphone, pdf-verkleinen-mac, hoeveel-dagen-tot-kerst, geluid-uit-video-halen-iphone. For these, the «fact diff» is
  against the saved sources and the app facts: every number, threshold, frequency, date and recommendation must be in a source the
  writer saved (or in `_apps/<slug>.md`, the Dutch app page, the glossary or APP_BLUEPRINT.md §10). Compare with the models named in
  the brief to catch a claim the model sourced differently. Health and pet posts keep one plain «geen medisch / diergeneeskundig
  advies» line; no medicine or treatment brand or price.
- hoeveel-dagen-tot-kerst: no typed «nog N dagen»; recompute every weekday with `python3 -c "import datetime; ..."` and check the kerstvakantie dates against the saved
  rijksoverheid.nl page.
- The batch 1 reviewers' must-fix list is the sheet paragraph «From the Tier 4 reviews (2026-11-19)» in `_i18n/nl.md`.
- The sheet paragraphs «From the Tier 4 batch 2 reviews» and its «Wiring (batch 2)» sentence list further must-fix items.
