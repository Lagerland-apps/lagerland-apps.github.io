# Back-translation brief: Dutch (nl) Tier 1 pages

For the blind back-translation agents (TRANSLATION.md 9, step 4). Never published.

You translate finished Dutch pages back into English so a reviewer can compare claims with the English original.

- Read ONLY the Dutch file(s) you are given, under `/Users/anttiaittamaa/Downloads/githubcode/lagerland-apps.github.io-main/nl/`.
  Do NOT open the English source pages (`_apps/`, `index.html`, `apps/`, `lagerland-apps/` at the repo root), the
  Italian or other language twins, the glossary or the keyword files. You must not know what the English says.
- Translate literally and completely, claim by claim: every front-matter text field (title, tagline, quick_answer,
  seo.title, seo.description, hero, who_for, who_not_for, value_points, features, how_it_works, plans text, comparison
  labels, faq, captions, alt texts, about body, enrichment) and the body. Keep the field names as headings so the
  reviewer can match them. Keep tokens like `{P_MONTHLY}` and Liquid as they are.
- Keep every hedge exactly as the Dutch says it ("kan", "ongeveer", "alleen", "optioneel", "op je apparaat"). Do not
  smooth or improve anything. Where a Dutch word is ambiguous, give both readings in [brackets].
- Write the result to `/private/tmp/claude-501/-Users-anttiaittamaa--claude-spares-spare-sfRxDf/a0f20936-3297-4b44-a744-abd8a39f3d0e/scratchpad/nl/bt/<slug>.md`
  (home → `home.md`, about → `about.md`). Touch nothing in the repo.
- Reply with the path(s) written and any Dutch sentence you found unclear or ungrammatical (quote it).
