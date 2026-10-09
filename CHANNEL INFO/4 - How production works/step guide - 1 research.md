---
description: Demand-check a topic and build the episode's sourced claim sheet
argument-hint: <topic or working title>
---
Topic: $ARGUMENTS

1. Read `channel/bible.md` (titles, episode structure) and `channel/topics.md` (demand gate).
2. **Demand gate.** Search YouTube for the question type over the past year, sorted by views (URL pattern in topics.md), using WebSearch or WebFetch. Record up to eight comparable videos: title, channel, subscribers if shown, views and age.
   - PASS if at least two unrelated channels under about 200K subscribers reached 100K+ views with this question type in the past year.
   - If a near-identical title appeared in the last 60 days, propose a different angle.
   - If it FAILS, propose two reframes that would pass, and stop for the user to choose.
3. Choose the slug `NNN-short-name` (next number in `episodes/`) and a working title that follows the bible's formulas. Run `python pipeline/lp.py new <slug> "<title>"`.
4. **Research.** Find 8 to 15 sources. Prefer historians' books, academic articles, primary-source editions (British History Online, museum and university pages) and archaeology reports. Never use YouTube videos, transcripts, content farms or other AI summaries as sources.
5. Fill in `episodes/<slug>/claims.md`:
   - Every claim the script might use, phrased as it would be said, with its tag (E/R/I), source with page or URL, confidence, and status "verify".
   - **Fact-check before anything else is made.** Check every claim against its source passage (primary edition or scholarship, never another channel), then have an independent reviewer try to refute each verdict. Only then set the status to "checked YYYY-MM-DD". Fix or cut anything wrong or unsupported. Nothing downstream (script lock, voice, images, render) may start with an unchecked claim; `lp.py` enforces this.
   - Three to five vivid concrete details, two evidence moments the script can show, one common myth to correct, and the contested points.
   - The hook: stakes for the viewer, the viewer's objection, and three cold-open questions with the held one marked.
6. Report: the gate verdict with comparables, the number of claims (all must be checked; list any cut or reworded), the proposed six or seven sections, and any claims you could not source.
