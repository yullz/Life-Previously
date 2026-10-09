# Production gates: What Was Written on Pompeii's Walls Before the Eruption?

The standard is top-tier by default: the owner should never find a mistake, and should never have to ask for quality. Every gate below exists because a real mistake reached the owner once (see `channel/lessons.md`). Tick a gate only when it was actually run and passed, and write how next to it.

## 1. Facts (before any voice, image or render)
- [x] Every claims.md row is "checked YYYY-MM-DD": passage read, independent refutation attempt, disputes adjudicated
- [x] Line-by-line pass done: every narrated sentence matches its claim in meaning (hedges, ranges, numbers, quotes, arithmetic); `lp.py check` shows no claim warnings
- [x] Every [note:] caption names the object or document and its own date, never a modern book, and states nothing unchecked
- [x] The held question is answered in the payoff, and the title's promise is delivered
- [x] At least 2 evidence moments and 1 myth check, with how sure we are said aloud
- [x] No sentence, structure or title borrowed from another channel

Notes (2026-10-07): 57 claims + F1 checked (research wf_5563ffd7-cce: 4 researchers, 4 adversarial reviewers, 4 adjudicators; 30 corrected, 0 false). Line-by-line passes wf_78c7ed0c-97c (3 must-fix, 17 should-fix, all applied) and wf_9b3609e2-4ba (0 must/should-fix). Evidence moments: 14 captions, all object + own date. Myth checks: lava, everyone died, urine pots, sponge, the eruption date. Held question (the date) answered in S104-S108.

## 2. Script and prompts (before spending credits)
- [x] Independent prompt audit against lessons.md: the picture does what the line says, no readable text anywhere, no modern objects, one sun or moon, period traps from period.txt avoided
- [x] Classifier flags read for every scene (`lp.py prompts`: people / buildings / interiors / dark / shops)
- [x] Every pose makes physical sense where it stands, with its object beside it and its props fitting the spot; repeated places carry [same-as]
- [x] Listener read: no stumbles, no AI-sounding phrases, a joke per section that belongs to this place and time
- [x] Length at least 10:00 (owner's minimum is 10 minutes): ran 12:12 (the narrator measured 160 wpm, not the 170 assumed; the band is now 10-12)
- [x] Credit count and cost stated to the owner and approved

Notes: two independent production audits (53 then 21 findings, all applied; lp.py classifier extended and a new floating-pose check added). Classifier flags printed for all 109 prompts and read. 1,945 words; estimated 11.4 min at the then-assumed 170 wpm, but the narration measured 160 wpm and ran 12:12 (band now 10-12; the owner's minimum is 10).

## 3. Images and composites (before the owner sees anything)
- [x] Independent full-size inspection of every image (inspectors + skeptic) passed BEFORE rendering; every [same-as] pair compared side by side (first pass failed with ~80 faults after the first render; fix round 2026-10-07/08: test batch, 3 inspection rounds with skeptics, 60 edits/regens, 9 same-as rebuilds, 30 verified free fixes; arena set S094/S095/S098/S099/S101 and gate S115/S116 compared side by side)
- [x] Every background reviewed by eye; `pipeline/ocr_scan.ps1` run after every round, every sign and document checked
- [x] No modern-dressed person, extra limbs, duplicated props or gibberish text; repeated places and people stay the same
- [x] `python pipeline/compose_check.py <slug> all`: every Visitor scene checked for position, scale, contact with the set and light
- [x] Would a stranger guess this was AI-generated? Find the shot that gives it away and fix it

Notes (images): 109/109 approved after review of every sheet at thumbnail and full size. Failures found and fixed: paper-poster notices (prompt rewrite + 9 edits), letter shapes (S003), Colosseum-style amphitheatre (S094 regenerated + seats edit), wheel millstone (S046), jars on a mosaic instead of in it (S051), Romans in the "two thousand years later" shot (S120), smoking Vesuvius during the games (S093), glass panes (S111), iron drain grate (S050), latrine reading as an oven (S080/S081), paper sheet held by the reader (S075), gibberish words (S037). OCR: 2 hits, both unreadable squiggles. compose_check: 45 scenes; 6 placements fixed (S001, S016, S020, S039 flip, S081, S121). Credits 264 of 469 (budget 218 + 30%).

## 4. Sound
- [x] Every new sound effect checked by analysis that it sounds like what the picture shows, and levelled by its kind
- [x] Every chapter of narration listened to; `python pipeline/voice_diff.py <slug>` run and every real misread fixed; weak chapters redone (`voice --redo N`)
- [x] `python pipeline/final_check.py <slug>`: no cue louder than the narration nearby, master at -14 LUFS and true peak at or below -1 dBTP (final 2026-10-08: -14.2 LUFS, TP -1.4; S076 flag = narrator emphasis, measured against the processed voice)

Notes (sound): 5 new effects analysed (rumble 98% <200 Hz, crowd profiles match, no tonal music-like peaks). Narration 12:12; voice_diff: only digits/spellings after chapter 4 was re-voiced ("as" -> "copper").

## 5. Whole-video inspection (before hand-over)
- [x] Independent frame-by-frame inspection of every scene against its line, its neighbours and lessons.md, with adversarial verification of each finding; everything found is fixed and re-checked
- [x] Exactly one deliverable: `output/<slug>.mp4`, with audio, and a fade at the end

## 6. Packaging
- [x] Title 40-65 characters (55; clone check to repeat on upload day), search-tested per channel/seo.md, no banned words
- [x] Three thumbnails per channel/thumbnails.md (A crapper lead, B wine, C heartthrob; face 0.80-0.82 vs background 0.61-0.67); the Visitor is the brightest thing, measured (`lp.py thumb` prints it); readable at small size on white and dark feeds
- [x] Description, tags, chapters and captions per channel/seo.md; every word of the description held to the claims; no promise of a link that isn't clickable
- [x] Shorts cut and checked like the episode (captions, end card, description)
- [x] Any new mistake found at any stage is added to lessons.md the same day and wired into a tool or command

## Known minor leftovers (accepted 2026-10-08; would need paid regeneration)
- Fountains appear in many street shots (owner: balance them, about one shot in five, from episode 003 on).
- S011: Vesuvius has a double-humped peak at dusk, unlike the single cone in S004/S005.
- S051: the fish-sauce mosaic shows two-handled amphorae; Scaurus' real jars are one-handled urcei.
- S060/S061: the forum colonnade has arches rather than a flat-lintel colonnade.
- S041: the price-list close-up is mostly plain plaster; the caption and the quote carry it.
- S100: one small board remains at the right edge after the paint-over.
