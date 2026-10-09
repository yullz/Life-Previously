---
description: Write the episode script with background prompts, poses and sound cues from its claim sheet
argument-hint: <slug>
---
Episode: episodes/$ARGUMENTS

1. Read `channel/bible.md`, `channel/style.md` (shot vocabulary, poses, sound), `channel/poses.json`, `templates/script.txt` (format), and the episode's `claims.md`. Read `episodes/001-medieval-london-day/script.txt` as the quality bar for structure, pacing, prompts, poses and sound cues, not as text to reuse.
2. Write `script.txt` following the bible's episode structure:
   - Length per `channel/bible.md` (currently 1,650 to 1,900 words), second person, present tense, written to be spoken.
   - One scene per image: 10 to 22 words of narration, never more than 28.
   - Eight or nine `## ` chapters, as in the bible: "Cold open" first, then six or seven sections, then the payoff. Put the channel sting on the first scene after the cold open only if it fits the era (the current `sting` file is a medieval church bell; see channel/style.md).
   - **Background prompts** describe one clear moment: setting, locals, time of day, shot type. **Never mention the Visitor in a prompt.** Put him in with `[pose: name position size flip]` in about half the scenes, with at least one reaction per section, and say where the empty space is ("an empty stool on the right").
   - **Write prompts the image model can't misread:**
     - Say what to draw, not what to avoid. "The only things in it are a bed and a chest", not "no fireplace". The model draws what it reads.
     - One moment per image. Two moments become `Split composition: on the left …; on the right …`.
     - Close-ups of objects start with `Object insert:`.
     - Anything with writing (documents, signs, contracts) shows blank backs, pictures or "illegible script". Shop signs are pictures.
     - Name the material, not just the object: "plain soldered lead pipe", not "pipes", or you get modern plumbing.
   - **Continuity:** when a scene returns to a place already shown (the same room, alehouse or field), add `[same-as: S0xx]` pointing at the first shot of that place. Its image is attached as a reference so the shots match.
   - **Period sheet:** fill in `period.txt` (setting, people, buildings, interiors, light, signs, avoid) from the same sources as claims.md. Each prompt gets only the lines its scene needs.
   - **Poses:** reuse names from `channel/poses.json` wherever possible. If you need a new one, add it to poses.json with a one-line description.
   - **Sound:** 15 to 25 `[sfx: name]` cues where a sound sells the moment. Reuse names from `channel/sfx/README.md`, and add any new names to that table with a description.
   - At least two evidence moments with `[note: Document or object, place, its own date]` (e.g. `[note: Spurriers' ordinance, London, 1345]`; modern books go in the description's sources list, never on screen), and one myth check.
   - `[still]` on punchlines and close-up reactions; otherwise camera moves rotate automatically.
3. **Facts:** only use claims from claims.md whose status is "checked". If a line needs a new fact, add it to claims.md with its source and fact-check it (source passage read, independent refutation attempt) before writing the line. Then check the finished script line by line: every sentence that states a fact (dates, numbers, quantifiers like "most" or "almost nobody", on-screen captions, arithmetic like "fifty years later") must match its checked claim word for word in meaning. The script is not locked until this pass is done.
4. **Check it against `channel/lessons.md`** (no modern devices, the picture does what the line says, one sun, poses whose props fit the spot), then **read it as a listener would.**
   - Cut 10% of the words: filler, throat-clearing, stacked adjectives.
   - No sentence a human narrator would stumble over, no AI-sounding phrasing, and no "rule of three" in every paragraph.
   - Jokes must be specific to this place and time.
   - Write for the voice: punctuation for pauses, years as words, and at most a handful of `{sighs}`-style directions per episode.
5. Run `python pipeline/lp.py check $ARGUMENTS` and fix every warning. Then run `python pipeline/lp.py poses` to list any new poses to make.
6. Report the word count, estimated minutes, scene count, poses (new ones listed), sound cues (new names listed), evidence moments, and confirm that every claim is "checked" and every factual line is covered (`lp.py check` shows no claim warnings). Do not hand over for voice or images otherwise.
