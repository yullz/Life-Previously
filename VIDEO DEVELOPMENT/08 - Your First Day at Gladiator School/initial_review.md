# Initial director review — 10 October 2026 (Claude, acting for the director under the owner's delegation)

Read all 96 narration lines, claims, sources, scene instructions, `equipment_spec.json`, thumbnails, Shorts, pilot, sound and pronunciation plans against `REVIEW_STANDARD.md`, and re-verified every claim. Read on 10 October 2026: the Antiquity 2014 paper in full (PDF parsed), the Carnuntum site page, the VIAS interpretation page, Seneca's Letter 37, Archaeology Magazine's gladiator-weapons article and glossary, Vegetius I.11 (Latin Library) and the Britannia 2024 Colchester Vase article. The Met essay and object page could not be rendered (script-driven pages, rate-limited) and the British Museum blog refused access; no row relies on them any more: the training-post evidence moved to Vegetius and the Carnuntum post foundation, the kit to Archaeology Magazine, the Colchester fighters to the peer-reviewed article. Passed with fixes; the full list is `initial_review` in `episode.json` and `review.json`.

Changes:
- The cold open asks the three questions and holds "who controls you?"; chapters re-cut without renumbering (chapter 3 ends at the post, chapter 6 opens at the baths, chapter 7 at the amphitheatre, chapter 8 at S085, now 90 seconds); S092 answers the held question; S096 cues the next episode.
- The lamp cards became a Vegetius source card and a courtyard medium; S013 follows the glossary on who became gladiators; S083 names Memnon and Valentinus from the Britannia article.
- Nine shot runs removed; nine image instructions and two lines no longer name the Visitor; poses added so he appears in about half the scenes; the retiarius kit is its own anchor.
- Sound plan rebuilt to 21 cues on visible action with 10 specified assets. Pilot resolves to the anchors (courtyard, gate, bath, bench, kit, cell, hall, amphitheatre, TH-A). Thumbnail chips are CARNUNTUM • c. AD 200; captions carry the sources' own dates. Pronunciations added. 21 collapsed-space strings fixed.

## Package review passes 1 and 2 — 10 October 2026

Pass 1: one new shot run removed; the retiarius kit made an independent anchor. Slate content check: the Roman era is shared with 05, but the setting, question and promise differ (see `../SLATE_CHECK.md`).

Pass 2 (execution dry run): read the compiled prompts for the courtyard, gate, kit, cell and amphitheatre anchors and the Vegetius medium; checked the equipment spec against the kit lines, handoff counts, pilot order, sound assets, pronunciations, Shorts and packaging copy. Nothing further found.

Released as a director package on 10 October 2026 (`package_manifest.json` holds the hashes). Note for production: the Met lamp image is optional and may be added only if the museum page confirms a fighter at a post.
