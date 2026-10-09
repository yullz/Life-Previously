# Channel bible

## Identity
- **Name:** Life, Previously.
- **Handle:** @LifePreviously. Confirm it when you create the channel; fallbacks are @LifePreviouslyTV and @LifePreviouslyHistory. The name passed a quick US-only check on 5 Oct 2026. That is not legal clearance.
- **Tagline:** How ordinary people actually lived.
- **Promise**, as a viewer would put it to a friend: "It drops you into a real place and year and walks you through a normal day: the work, the food, the rules, the gross bits. And it's actually researched."
- **Audience:** curious adults aged 18 to 45, watching on phone or TV, who like history when it is about people rather than dates. No prior knowledge is assumed.

## Why we differ from Ink Explainer
- **The prehistoric stick-figure format is saturated.** At least 35 look-alike "ancient humans" channels have launched since April 2026, and the ones started since July mostly get under 2K views per video.
- **YouTube won't pay for interchangeable content.** It does not monetize content that copies an existing format until videos feel interchangeable, and it judges the whole channel. With AI-assisted images, the script, the narrator, the character and the research are what make the channel ours.
- **So every video must show three things:** the Visitor, a named place and year, and on-screen sources. For comparative/list formats explored at the owner's request on 9 October 2026, label the place and period of each segment rather than pretending all examples belong to one setting.

## The Visitor
- A modern young man in an orange hoodie, jeans and white sneakers. He is "you": the narration speaks in the second person, and he acts it out.
- **Owner-directed pirate episode accessory (9 October 2026):** the Visitor wears a pirate hat in the approved pirate-life episode. Keep his face, hoodie and established style; use consistent episode-specific accessory copies of approved poses and preserve the originals. The hat has not yet been produced or visually approved.
- He arrives with modern assumptions, tries them, and they fail in a way you can see. That failure is the joke and sets up the explanation.
- He never speaks on screen: no lip-sync, no speech bubbles. He reacts with confusion, disgust, delight or panic.
- He appears in roughly half the scenes. Locals carry the other half.

## Every episode answers two questions
1. **History:** what did ordinary people in this place and year actually do?
2. **Behavior:** why did they behave that way? Name the reason in one sentence: rules, incentives, fear, status or comfort. Pilot example: the city banned night work, so everyone's day matched the sun.

## Episode structure (10 to 12 minutes; the owner's minimum is 10 minutes, decided 2026-10-07)

**Owner-approved exception, 2026-10-08:** episode 001 is allowed to remain at 9:24. Do not add padding or new narration just to lengthen the pilot. All future episodes still have the ten-minute minimum.

| When | Beat | Rules |
|---|---|---|
| 0:00–1:05 | Cold open | Drop the Visitor into the place and year with a concrete problem within 10 seconds. State what is at stake for the viewer's own life. Voice the viewer's objection. Ask two or three explicit questions, and say that one will be answered at the end. |
| 1:05–about 10:30 | Six or seven sections of 70 to 110 seconds | Follow the day, or a chain of problems. Each section runs: modern assumption, then what actually happened, then one concrete detail (a number, name or object), then a light joke, then a question that leads into the next section. |
| At least twice | Evidence moment | Show a named record, document or find with a `[note: source]` label, and paraphrase it briefly. |
| At least once | Myth check | Correct something viewers "know" (beer instead of water) with evidence, and say how sure we are. |
| Last 90–120 seconds | Payoff | Answer the held question. Return to the opening image. Make one fair comparison with the viewer's life, without lecturing. End on a callback line and a one-line end-screen cue. Never "smash that like". |

## Writing rules
- **Length:** 1,650 to 1,900 words, so the finished video runs 10 to 12 minutes. Measured rates including pauses and holds: episode 1, 170 words per minute (1,601 words, 9:24); episode 2, 160 (1,945 words, 12:12). `lp.py check` uses 160 and warns outside 10 to 12.5 minutes. Add real content from the claim sheet to reach length, never padding.
- **Apply exceptions to the named episode only.** The owner's acceptance of the 9:24 pilot does not lower the minimum for episode 003 or later. Measure the actual narration duration before the main image batch; estimated words per minute alone did not predict the pilot's final length.
- **Voice:** second person, present tense, short spoken sentences. Read every line aloud.
- **Pacing:** one image per 10 to 22 words, never more than 28.
- **Humor:** dry, coming from the situation and the Visitor's reactions. At least one joke per section. Never mock the people of the past.
- **Sound human, not generated:**
  - Cut 10% after the first draft.
  - No AI-sounding phrases; `lp.py check` flags the list in `banned_phrases` in config.json, and you should add any new one you notice.
  - No "rule of three" in every paragraph, no sentences that restate the previous one, and no generic adjectives where a concrete detail would do.
- **Numbers:** round them, and source every one in claims.md. Give a range when historians disagree ("forty to fifty thousand people").
- **Uncertainty:** say it aloud when it matters: "historians think", "the records show", "we don't really know".
- **Years:** write them as words ("thirteen-ninety"), or add them to `voice.pronunciations` in config.json.
- **Banned:**
  - "Ancient Humans" titles, "nobody tells you" and "disturbing" or "terrifying" clickbait.
  - Fake precision and preachy endings.
  - Any phrase lifted from another channel, and any claim that isn't in claims.md.

## Titles
- **Shape:** a clear curiosity hook with a named place or era, usually in 40 to 65 characters. Questions remain useful; the owner's 9 October request also permits proposing countdown, comparison and viewer-choice titles when their exact promise is supported.
- **Formulas** (rotate them):
  1. What Did People in [Place/Era] Actually Do All [Day/Night/Winter]?
  2. How Did [People] in [Era] Survive [Heat/Cold/the Dark]?
  3. What Did [Era] People Do When [relatable situation]?
  4. The Worst Jobs in [Place, Era]
  5. How Did [Era] People [Sleep/Wash/Commute]?
  6. You Wake Up in [Place, Year]. [Three to five words.]
- **Demand gate:** every title passes the gate in topics.md before scripting.
- **Never** reuse, word for word, a title another channel published in the last 60 days.

## Thumbnails
- **SEO:** follow `channel/seo.md` (search-demand tags, description opening, chapters, hashtags) for every upload.
- **Playbook:** read `channel/thumbnails.md` (researched rules and evidence) before designing any thumbnail.
- **Composition:** the Visitor large on one side with one clear emotion (a library pose, placed by `lp.py thumb --pose`), in a period scene, with one problem object.
- **Text:** one to four words (owner-approved 2026-10-07; research found 4-6 words carry no penalty) in white (#FFFFFF) with the last line in the Visitor's orange (`lp.py thumb --accent`, as shipped on episodes 001 and 002) and a dark-brown stroke, on the side opposite the Visitor.
- **Signature:** an orange place-and-year chip above the text ("LONDON 1390"). Every episode has one.
- **Never** use yellow text (Ink Explainer's), white round stick-figure faces, more than four words, or tiny details.
- **Testing:** make three versions, and use YouTube Studio's Test & Compare when your channel has it.
- **Legibility:** check `thumbnail_small.png`. If you can't read it at that size, it fails.

## Variety across the channel
- **Eras:** never the same era twice in a row, and at most one episode in six set in the Stone Age.
- **Scope (owner expansion, 9 October 2026):** ordinary people and lived experience remain the centre. The owner explicitly encouraged exploring different concepts, including list/comparison ideas, so do not reject a proposal solely for using a countdown, contrasting cases or viewer choices. A story episode has one named place and time; comparative episodes label each setting separately. Keep claims sourced, reconstructions identified and comparisons specific. This permits proposing formats; it does not approve every proposed topic or change the style.

## Publishing rhythm (decided 2026-10-07)
- **Long-form:** weekly, Saturdays at 19:00 Sofia time. Episode 001 on 10 Oct 2026, episode 002 targeted for 17 Oct.
- **Shorts:** three per episode, cut from it, on the Sunday, Tuesday and Thursday after it at 19:00.
- **Quality beats the date.** If any gate (all claims checked, compose_check, the owner's review of the preview, final_check) isn't passed by the Thursday before, the episode moves back one week. Never ship a known mistake to keep the slot.
- **Get ahead.** Research and fact-checking for the next episode start while the current one is in images and render, so one finished episode can build up in reserve.
- The About text keeps "New episode every other week" until four weekly episodes have shipped on time; promise less than we deliver.

## Channel page copy
- **About:** How did ordinary people actually live? Each episode drops you into a real place and year, from medieval London and ancient Rome to Edo Japan, and walks you through a normal day: the work, the food, the rules, and the strange parts that never make it into textbooks. Every video is researched from historians' books and primary sources, listed in the description. New episode every other week.
- **Banner text:** "How ordinary people actually lived." Small line: "New episode every other week."
