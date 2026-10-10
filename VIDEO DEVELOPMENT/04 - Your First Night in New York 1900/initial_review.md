# Initial director review — 10 October 2026 (Claude, acting for the director under the owner's delegation)

Read all 96 narration lines, claims, sources, scene instructions, thumbnails, Shorts, pilot, sound and pronunciation plans against `REVIEW_STANDARD.md`, and re-verified every claim on the sources readable today. Passed with fixes; the full list is `initial_review` in `episode.json` and `review.json`.

Sources: Riis (Gutenberg, 1900 edition), the 1900 census transcription PDF, the Levine family-story PDF and the NYC LGBT Historic Sites page were read at the locators. Three Tenement Museum web pages (the rent article, the virtual tour and the 97 Orchard page) refused automated access (HTTP 403); Astra read them on 9 October. Nothing now rests on them: the rent chapter was rebuilt on the 1903 *Tenement House Problem* volume (the 1900 Commission's block study and a tenant's testimony, both read on archive.org), and the apartment figures follow the National Register form for 97 Orchard Street (four apartments to each upper floor, three small rooms, about 325 square feet). The museum article's floor-specific rent ranges were not found in the Commission volume and are no longer spoken. Readable sources disagree on the building's apartment count (20 or 22), so none is spoken.

Changes:
- The cold open asks what a bed costs and what the price leaves out, and holds the second question for the payoff (S003, S086). Third-person lines about the Visitor are second person.
- Chapter 5 speaks the 1 January 1900 block counts (39 tenements, 605 apartments, 2,781 people; 179 three-room apartments; 264 water-closets and not one bath) and Mrs. Miller's rents ($12, then $10 for three rooms; the $10 flat four flights up). The Levine caveat moves to S089, after the family is introduced.
- Twelve runs of identical shot types removed; seven prompts, the avoid list and thumbnail A no longer name the Visitor; eight unrelated object inserts are independent anchors.
- Sound plan rebuilt to 23 cues on visible action with 15 specified assets; deliberate silence named for the Sabbath workshop and the Mills room.
- Pilot resolves to anchors (street, Mills facade, reception, Mills room, boarding room, front room, kitchen, TH-A). Short 3 starts where the Levines are introduced. Census names added to the pronunciation plan. 79 collapsed-space strings fixed.

## Package review passes 1 and 2 — 10 October 2026

Pass 1: four shot runs created by the re-check removed (S033 and S072 establishing shots, S070 medium, S071 wide, S082 reaction); chapter lengths 76–95 seconds. Slate content check: New York 1900 is distinct from every other package (see `../SLATE_CHECK.md`).

Pass 2 (execution dry run): read the compiled prompts for the independent coin insert (S017), the boarding-room and stairs reaction edits (S038, S048), the street wide with the tenant (S052), the kitchen anchor (S062) and the front-room object insert (S066); checked handoff counts, pilot order, sound assets, pronunciations, Shorts windows and packaging copy. Nothing further found.

Released as a director package on 10 October 2026 (`package_manifest.json` holds the hashes). Note for production: the three Tenement Museum web pages listed as SRC03, SRC05 and SRC07 are kept for the owner's reference only; no narrated line depends on them.
