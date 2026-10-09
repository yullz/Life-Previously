# Production gates: Did Ancient Egyptian Workers Have Better Jobs Than Us?

The standard is top-tier by default: the owner should never find a mistake, and should never have to ask for quality. Every gate below exists because a real mistake reached the owner once (see `channel/lessons.md`). Tick a gate only when it was actually run and passed, and write how next to it, naming the exact file versions checked (the render manifest gives their hashes). A finished tool run or a ticked box is not a review; a check that could not be done stays unticked with the reason.

## 1. Facts (before any voice, image or render)
- [x] Every claims.md row is "checked YYYY-MM-DD": passage read, separate critical review by Astra, disputes resolved; self-review is not described as independent-model verification
- [x] Line-by-line pass done: every narrated sentence matches its claim in meaning (hedges, ranges, numbers, quotes, arithmetic); `lp.py check` shows no claim warnings
- [x] Every evidence [note:] names its ancient object/place and date or honestly unknown reign, never a modern publication year; diagrams are labelled as interpretation/framing and state nothing unchecked
- [x] The held question is answered in the payoff, and the title's promise is delivered
- [x] At least 2 evidence moments and 1 myth check, with how sure we are said aloud
- [x] No sentence, structure or title borrowed from another channel

## 2. Script and prompts (before spending credits)
- [ ] Independent prompt audit against lessons.md: the picture does what the line says, no readable text anywhere, no modern objects, one sun or moon, period traps from period.txt avoided
- [ ] Classifier flags read for every scene (`lp.py prompts`: people / buildings / interiors / dark / shops)
- [ ] Every pose makes physical sense where it stands, with its object beside it and its props fitting the spot; repeated places carry [same-as]
- [ ] Listener read: no stumbles, no AI-sounding phrases, a joke per section that belongs to this place and time
- [ ] Length 10:00 to 12:30 (owner's minimum is 10 minutes; aim for 10-12; `lp.py check` warns outside 10-12.5)
- [ ] Credit count and cost stated to the owner and approved

## 3. Images and composites (before the owner sees anything)
- [ ] Independent full-size inspection of every image (inspectors + skeptic, checklist from lessons.md) passed BEFORE compositing or rendering; every [same-as] pair compared side by side
- [ ] Every background reviewed by eye; `pipeline/ocr_scan.ps1` run after every round, every sign and document checked
- [ ] Evidence the narration quotes or names (inscriptions, price lists, documents, artefacts) is shown accurately and readably: a checked text card (`[card: ...]`, `pipeline/cards.py`) or an accurate, labelled diagram, never blank plaster or invented lettering; a named artefact keeps its documented forms and arrangement
- [ ] No modern-dressed person, extra limbs, duplicated props or gibberish text; repeated places and people stay the same
- [ ] `python pipeline/compose_check.py <slug> all`: every Visitor scene checked for position, scale, contact with the set and light
- [ ] Would a stranger guess this was AI-generated? Find the shot that gives it away and fix it

## 4. Sound
- [ ] Every new sound effect checked by analysis that it sounds like what the picture shows, and levelled by its kind
- [ ] Every chapter of narration listened to; `python pipeline/voice_diff.py <slug>` run and every real misread fixed; weak chapters redone (`voice --redo N`). Every difference in meaning (names, numbers, negations, quotations) is resolved by listening and recorded, not dismissed as a transcription error
- [ ] `python pipeline/final_check.py <slug> [--video <candidate>]` says PASS: no cue louder than the narration nearby, nothing unmeasured, master at -14 LUFS and true peak at or below -1 dBTP

## 5. Whole-video inspection (before hand-over)
- [ ] Independent frame-by-frame inspection of every scene against its line, its neighbours and lessons.md, with adversarial verification of each finding; everything found is fixed and re-checked
- [ ] The final render ran without refusals (no missing or placeholder background, pose, sound, card or narration) and wrote its manifest of input and output hashes
- [ ] Captions: `python pipeline/captions.py <file.srt>` shows no problems (no zero-length, flashing or overlapping cues, at most two 42-character lines); names, quotations and numbers checked against the audio
- [ ] A complete playback review (not only sampled frames) was done, or its absence is stated
- [ ] Exactly one deliverable: `output/<slug>.mp4`, with audio, and a fade at the end

## 6. Packaging
- [ ] Title 40-65 characters, search-tested per channel/seo.md, no banned words
- [ ] Three thumbnails per channel/thumbnails.md; the Visitor is the brightest thing, measured (`lp.py thumb` prints it); readable at small size on white and dark feeds
- [ ] Description, tags, chapters and captions per channel/seo.md; every word of the description held to the claims; no promise of a link that isn't clickable
- [ ] Shorts cut from the approved master and checked like the episode (captions, cards, end card, description); full-quality `_master.mp4` files kept beside the upload copies
- [ ] Any new mistake found at any stage is added to lessons.md the same day and wired into a tool or command

## Director evidence — 9 October 2026

Facts gates above were checked by Astra against the unchanged 1,790-word narration, now staged across 105 shots; see research/fact_checks.json, research/director_script_review.json and build/director_preflight_report.json for findings, source limits and reviewed file hashes. The owner assigned the separate critical script review to Astra. This is self-review, not separate-model validation. Native script check returned OK with no warnings. Version 4 updates scene mapping and visual specifications without changing narration. Only the factual/script-content gates are checked; graphic readability, paid work, actual timing, audio, composites, continuous playback and release remain open. A change to a reviewed input reopens affected gates.
