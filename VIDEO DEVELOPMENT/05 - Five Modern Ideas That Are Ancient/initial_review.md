# Initial director review — 10 October 2026 (Claude, acting for the director under the owner's delegation)

Read all 100 narration lines, claims, sources, scene instructions, `mechanism_spec.json`, thumbnails, Shorts, pilot, sound and pronunciation plans against `REVIEW_STANDARD.md`, and re-verified every claim. All eight sources were read at the locators on 10 October 2026: the Pompeii Archaeological Park press release, the Ostia Antica panel, the two Roman Baths pages, Vitruvius V.10 and Hero's Pneumatics sections 21, 37 and 38 (both on Gutenberg), MacTutor and the Linda Hall essay. None refused access. Passed with fixes; the full list is `initial_review` in `episode.json` and `review.json`.

Changes:
- Cold open now asks which idea you would keep and what the catch is, and holds the catch; chapters re-cut without renumbering (the temple intro opens chapter 6; S087–S100 form the payoff "Every convenience has a catch", which answers the held question, returns to the temple doors and cues the next episode). Chapters run 60–112 seconds.
- The seven coin diagrams and five door diagrams in a row are interleaved with the chest and temple exteriors showing the visible result (coin dropped, water flowing, doors opening and closing); the hypocaust gets an illustrated cutaway, a detail of the preserved tile stacks and a reaction. `mechanism_spec.json` scene lists updated to the remaining diagram scenes; geometry unchanged.
- Sixteen image instructions no longer name the Visitor; three third-person lines are second person; Visitor in about half the scenes.
- Thumbnail chips are place-and-year (Alexandria, 1st century AD; Aquae Sulis, c. AD 350). Pilot resolves to the anchors (temple model, counter, Ostia block, room, warm room, furnace, chest, TH-A).
- Sound plan rebuilt to 21 cues on visible action with 12 specified assets. Pronunciations added for thermopolium, Regio, medianum, Vitruvius and Alexandria.
- The press release's "about eighty thermopolia" and the nymph-and-animals decoration are now used within the existing claims.

## Package review passes 1 and 2 — 10 October 2026

Pass 1: one new shot run and two instructions still naming the Visitor fixed; chapter 4 at 112 seconds accepted. Slate content check: Pompeii AD 79 is also the setting of published episode 002 and heated floors recur in 18, but the format, question and promise differ and each episode keeps its own full explanation (see `../SLATE_CHECK.md`).

Pass 2 (execution dry run): read the compiled prompts for the hypocaust cutaway (S042), the coin insert (S060), the coin-drop reaction (S062), the doors-opening wide (S082) and the closing temple wide (S100); checked the spec scene lists, handoff counts, pilot order, sound assets, pronunciations, Shorts and packaging copy. Nothing further found.

Released as a director package on 10 October 2026 (`package_manifest.json` holds the hashes).
