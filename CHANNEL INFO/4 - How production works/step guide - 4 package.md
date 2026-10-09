---
description: Titles, thumbnails, description and upload checklist for a finished episode
argument-hint: <slug>
---
Episode: episodes/$ARGUMENTS

1. Make sure `timeline.json` and `chapters.txt` exist (they come from `python pipeline/lp.py voice`; if narration was recorded elsewhere, run `python pipeline/lp.py align <slug> <audio>` first). Read the script, claims.md, chapters.txt and the bible's title and thumbnail rules.
2. **Titles.** Write three options from different formulas, keeping the question type that passed the audience check. Each is 40 to 65 characters with no banned phrase. Run the title clone check in channel/seo.md (and again on upload day).
3. **Thumbnails.** Sketch 10-15 concepts first as code composites from existing images and poses (channel/thumbnails.md rule 14), then pick three structurally different ones. For each: a background prompt (a period scene with one problem object, calm space on the Visitor's side), a Visitor pose from the library, one to four words of text (bible rule), and the place-and-year chip.
   - State the image cost and wait for an OK, then generate the backgrounds with the episode's provider, model and style key (never draw the Visitor in them).
   - Save them as `thumb_a.png` and so on, then run for each: `python pipeline/lp.py thumb $ARGUMENTS thumb_a.png "TEXT" "PLACE YEAR" --side right --text-pos top --accent --pose <pose>`. The command overwrites `thumbnail.jpg`, `thumbnail_master.png` and `thumbnail_small.png`, so copy each result into `thumbs/` before the next one (see episode 002).
   - Check `thumbnail_small.png` and reject any you can't read.
4. **Description.** Fill in the template in package.md:
   - hook line and short summary;
   - chapters from chapters.txt;
   - sources from claims.md, as "Author, Title (Year)";
   - the "How we make this" line and the music credit.
5. Add 5 to 8 tags, the playlist and the end screen plan. Write everything into `package.md`.
6. Go through `qa.md` with the user and report which items are still unticked.
