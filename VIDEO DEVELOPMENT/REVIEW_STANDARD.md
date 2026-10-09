# Review standard for the eighteen director packages

This is the bar every package is reviewed against: the initial content review, source verification, and both slate-wide passes. It condenses `AGENTS.md`, `channel/bible.md`, `channel/style.md`, `channel/lessons.md`, `WARDROBE_POLICY.md` and `PRODUCTION_CONTRACT.md` (copies in `CHANNEL INFO/`). When this file and those disagree, the owner's latest instruction and the hard rules in `AGENTS.md` win.

## 1. What is canonical

- `episode.json` is the single source. Every other file in a package folder except `initial_review.md`, `*_spec.json` supplemental specifications and `package_manifest.json` is generated from it by `compile_packages.mjs`. Fix the source, then recompile. Never hand-edit a generated file.
- A scene row is `[narration, claim_ids, location_id, shot_type, visual_instruction, pose|null, note|null, graphic_text|null, meta{}]`. `shot_type` "graphic" means a local parchment graphic (no paid image). `note` becomes an on-screen source caption. `meta` may carry `scope`, `frame`, `parent_scene`, `independent_anchor`.
- Scene IDs are assigned by position at compile time (S001…). Inserting or deleting a row renumbers everything after it, so pilot lists, thumbnail payoffs, Shorts boundaries, sound cues, continuity rules in supplemental specs and `parent_scene` references must be re-checked after any structural edit.
- The compiler derives: the full image prompt (style, scope, period, location design, shot + visual, composition clause, continuity clause, text rule, avoid list); the parent chain (first non-graphic scene of a location is the anchor; later ones are paid edits of it unless `independent_anchor` or `parent_scene` says otherwise); the Visitor placement (standing 0.60 at x 0.80, or offset close-up for `closeup-*` poses); and the camera motion rotation (reactions and graphics are still).

## 2. Validator limits (hard)

1,650–1,900 narration words; no scene over 28 words; every scene mapped to at least one claim; `C0` is the only `F` (fictional framing) row; every factual claim has a source and a passage locator; pose names must exist in `channel/poses.json`; retired `phone-up` and `closeup-phone` are banned; a full-body pose is not allowed on an "object insert"; three thumbnails with headlines of at most four words; three contiguous Shorts (90–175 words is the pacing window); pilot items must be paid scenes or `TH-*`; sound and pronunciation plans must not be "pending". Release mode also needs every claim `checked`, three passed reviews and a manifest.

## 3. Story and script (bible)

- Cold open (first 60–65 seconds, about 160–175 words): drop the Visitor into the named place and year with a concrete problem inside ten seconds; say what is at stake for the viewer; voice the viewer's objection; ask two or three explicit questions and say one will be answered at the end. Package 005-style list episodes label each stop's place and period.
- Six or seven sections of roughly 70–110 seconds (about 190–290 words at 160 wpm). Each section: modern assumption, what actually happened, one concrete detail (number, name or object), a light joke, and a question or turn that leads into the next section.
- At least two evidence moments with a `note` naming the record and its own historical date, paraphrased briefly in narration. At least one myth check with the level of certainty said aloud.
- Payoff (last 90–120 seconds): answer the held question, return to the opening image, one fair comparison with the viewer's life without lecturing, a callback line, and a one-line end-screen cue. Never "smash that like".
- Second person, present tense, short spoken sentences, years as words. Hedges travel with their claims ("probably", "about", "many" not "most"). Time frames are named aloud when the evidence is older or later than the story's year.
- Humour is dry and comes from the situation and the Visitor's failing modern assumptions, at least one joke per section, never mocking people of the past. The Visitor never speaks, never holds a modern device, never has a phone line written for him.
- Sound human: no banned phrases (`pipeline/config.json`), no rule-of-three in every paragraph, no sentence restating the previous one, no stacked methodological disclaimers. Say a limit once, clearly, then get on with the story. If a section is mostly narration about what we cannot know, that is a defect.
- The channel's own avoid list: titles starting "What/How Did Ancient Humans", "nobody tells you" bridges, a you-versus-they sermon, "disturbing/terrifying" clickbait, fake precision, preachy endings.

## 4. Pictures (style, lessons)

- The Visitor appears in roughly half the scenes, at least one reaction per section, and he is the brightest thing in a thumbnail. He is only ever a composited library pose; no prompt may describe him, his hoodie or a sleeve (the compiler replaces the word "Visitor" in prompts, but write visuals so the background is complete without him).
- The picture does what the line says. Narration and visual describe the same arrangement (next to, not on top of; the basin is beside the splashing pose; "darkness" is dark).
- Shot vocabulary rotates: establishing wide, Visitor reaction, action medium, object insert, map, evidence card, comparison split, street or crowd. Never two identical shot types in a row, and never long runs of graphics; interleave an illustrated shot or a reaction.
- One sky, one sun, one camera height, one ground. A standing pose needs a floor and plausible scale beside the locals. A `closeup-*` pose must sit beside the subject, not cover it; object inserts take close-up poses only.
- Poses carry their props: `drink-cup` (medieval tankard), `parcel-overhead`/`overwhelmed` (wrapped parcel), `eat-pie-hot`, `hold-hammer`, `hold-candle`, `bow-wrong`, `sit-cup`, `sit-eat`, `cushion-overhead`, `closeup-horrified-contract`, `hide-embarrassed`, `empty-bowl`. Use them only where the prop makes sense in that era and scene.
- Returning places are edits of the accepted anchor (same room, same people, same furniture). A generic object-study location must not make an unrelated object inherit the first object's image: give unrelated objects `independent_anchor` or an explicit `parent_scene`. "Same view, different state" (empty, night, riot) is an edit of the anchor.
- Recurring props (fountains, water towers, notices) in roughly one street shot in five, chosen scene by scene.
- No text from the image model, ever. Documents, signs and coins are blank; checked words are composited later. Named artefacts are drawn from their source or shown as a labelled schematic.
- Graphics: at most four labelled elements, every icon recognisable at a glance or labelled with its own noun, a schematic says it is a schematic, no facsimile of an archival scan.
- Source captions name the historical record and its own date ("Spurriers' ordinance, London, 1345"), never a modern book's year. Modern scholarship goes in the description.
- `period.txt` content (the `period` and `avoid` fields and each location design) names the era's own forms positively and lists the drift the model reaches for (Tudor framing, church spires, modern taps, glass bottles, striped awnings, paper posters, Victorian top hats, modern vegetables).

## 5. Sound and voice

- 15 to 25 sound cues per episode on moments a sound sells (a bell, a gate, a splash, a crowd), each tied to visible action in a still image, below the narration, era-correct ambience only where the source is in view. Fewer than about twelve cues is a thin plan unless the episode's subject justifies deliberate silence, and then the plan says so per section. New assets carry a generation prompt, a `kind` (spot, ambience, accent), a path under `channel/sfx/`, `paid: true` and `quote_at_launch: true`; the medieval bell sting is only for medieval Christian settings.
- Every foreign or unusual name in the narration has a pronunciation entry; captions keep the historical spelling.

## 6. Packaging

- Title: a real question or promise with the place or era, 40–65 characters, no banned title words, built on the episode's own angle. Clone check is refreshed at upload, not here.
- Thumbnails: one to four words, white with the last line orange and a dark-brown stroke, orange place-and-year chip, the Visitor large with one emotion, one problem object, the promised moment paid off inside the cut (payoff scene IDs must be the scenes that deliver it, preferably set up by the cold open). No yellow text, no myth stated as fact, no claim the video does not keep.
- Description: every sentence held to the claims; sources listed; three topic hashtags; tags are real searched phrases the video answers.
- Shorts: three self-contained contiguous cuts of 90–175 words that keep their dates and hedges, each with a title that is a promise the clip keeps.

## 7. Facts

- Every narrated fact traces to a claim row whose source passage was actually read; the narrated wording keeps the claim's limits. Numbers are rounded and sourced; ranges where historians disagree; "we don't really know" said aloud when it matters.
- A claim is `checked` only after the source passage was read, the spoken wording compared, and a separate attempt to refute it was made and recorded. An inaccessible source leaves the claim open and visible; it is not marked checked.
- Reconstructions are identified as such once, clearly, in the narration and in `C0`.

## 8. Wardrobe

- Normal outfit unless the package selects a researched, understated period outfit (China, Japan, Korea distinct; pirate hat mandatory in 02). `wardrobe_spec.json` names sources, garments, colours and the identity lock; `pose_plan.json` lists every pose used anywhere, including thumbnails, and those poses must agree with the spec.

## 9. Execution readiness (the "point the folder at Claude" test)

- Nothing in the package asks Claude to research, choose wording, pick a lead thumbnail or invent a missing specification. Pilot lists resolve to paid anchors in dependency order and include the hardest setting, a character interaction scene and the lead thumbnail. Supplemental specs are listed in `extra_specs`. Continuity rules named in a spec (for example 09: S048 edits S004) are bound in the scene rows, not only described.
- No placeholder text, no "TBD", no collapsed-space strings (for example "MarcoPolo atworkingquay"), no stale counts.

## 10. Review record

Each pass writes its findings and fixes into `episode.json` (`initial_review`, `slate_reviews[]`) so `review.json` shows the real state. A finding without a fix is recorded as open, never silently dropped. Reviews are self-reviews by the assistant acting for the director under the owner's 9 October 2026 instruction; they are not independent human review, and they approve no media.
