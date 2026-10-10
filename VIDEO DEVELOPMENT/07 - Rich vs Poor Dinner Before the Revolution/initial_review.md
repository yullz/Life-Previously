# Initial director review — 10 October 2026 (Claude, acting for the director under the owner's delegation)

Read all 96 narration lines, claims, sources, scene instructions, `food_continuity_spec.json`, thumbnails, Shorts, pilot, sound and pronunciation plans against `REVIEW_STANDARD.md`, and re-verified every claim. All six sources were read at the locators on 10 October 2026: Mercier's chapters 67, 362, 383 and 631 on Wikisource, Menon's *Les Soupers de la Cour* volume III (1755) on the archive.org text (title page, the cabbage recipe on p.24, the rissoles on pp.26–27, the roast section and seasonal lists on pp.29–31) and the Wellcome catalogue record. None refused access. Passed with fixes; the full list is `initial_review` in `episode.json` and `review.json`.

Changes:
- The cold open holds a question (what really separates the tables besides quantity?); the payoff chapter opens at S088 (71 seconds), answers it at S090 and cues the next episode at S096.
- Seven third-person lines are second person; fourteen image instructions and the period text no longer name the Visitor; poses added so the Visitor appears in about 55% of scenes.
- Eleven shot runs removed, including six detail shots in a row through the cabbage recipe.
- The kitchen is anchored by a real kitchen scene, not a book insert; the pastry scenes edit the kitchen; the book moves to its own object location.
- Sound plan rebuilt to 20 cues on visible action with 16 specified assets. Pilot resolves to the anchors (modest room, dining room, market, shop, oven, kitchen, second household, TH-A). Thumbnail chips are PARIS • 1783. Menon captions carry 1755 and the page. Pronunciations added. 53 collapsed-space strings fixed.

## Package review passes 1 and 2 — 10 October 2026

Pass 1: one new shot run removed and six added poses taken back; the rissoles source note replaced with the recipe's own words. Slate content check: Paris is also the setting of 01 (1709), and food recurs in 05 and 16, but the format, question and promise differ (see `../SLATE_CHECK.md`).

Pass 2 (execution dry run): read the compiled prompts for the modest-room, market and kitchen anchors (S001, S007, S036), the squeeze medium (S052), the pastry edit (S081) and the closing dining room (S096); checked the food continuity spec against the recipe lines, handoff counts, pilot order, sound assets, pronunciations, Shorts and packaging copy. Nothing further found.

Released as a director package on 10 October 2026 (`package_manifest.json` holds the hashes).
