---
description: Generate an episode's backgrounds (and any missing Visitor poses) through the Higgsfield connector, check them and fix failures
argument-hint: <slug>
---
Episode: episodes/$ARGUMENTS. This is the paid route: every image costs credits (Nano Banana Pro at 2K = 2 credits, set in `images` in pipeline/config.json). Follow these steps exactly. Never edit the prompts or params inside a job file; change the script or config and rebuild the job instead.

1. **References.** Run `python pipeline/lp.py refs`. For anything marked NEEDS UPLOAD:
   - call `media_upload` with its filename;
   - PUT the file to the returned `upload_url` with curl (`-H "Content-Type: image/png"`; if the reply isn't 200, retry adding `-H "If-None-Match: *"`);
   - call `media_confirm` (type image), then `python pipeline/lp.py refs --set <style_key|visitor_sheet> <media_id>`.
2. **Prompt audit (required, before any credits).** Check every prompt against `channel/lessons.md` first; each lesson there is a mistake this channel already made once.
   - Run `python pipeline/lp.py prompts $ARGUMENTS` and read `images/prompts.md` in full, next to the narration.
   - Every scene must say what to draw (no "no X" in the scene text), describe one moment, and match its narration line.
   - Writing appears only as blank backs or squiggles, and signs are pictures.
   - Places shown twice carry `[same-as: S0xx]`, and `period.txt` is filled in.
   - Fix the script and re-run until every prompt passes. Only then build jobs.
3. **Jobs.** Run `python pipeline/lp.py jobs --poses` (only if poses are missing) and `python pipeline/lp.py jobs $ARGUMENTS`. Each prints the image count and estimated credits. Scenes whose `same-as` anchor doesn't exist yet are held back; build them after the anchor is fetched.
4. **Budget (required).** Call `balance`. Tell the user the images per job, the estimate plus 30% for retries, and the balance. Wait for an explicit OK. Stop if the balance is below the estimate. Fixes that stay inside that 30% need no new OK; anything beyond needs one.
5. **Generate**, for each job file `build/jobs/<name>.json`:
   - Copy the job file to a frozen name first (for example `bg2.json`) and submit from that. Rebuilding a job drops fetched images and shifts every index, so never rebuild while its batches are in flight.
   - Submit one batch of 12 and review it before sending the rest. Cheap prompt bugs show up in the first batch.
   - Send its `requests` to `generate_image_batch` in groups of 12, exactly as written. Keep every returned job ID with its index.
   - Wait with `jobs_wait` (groups of up to 12) until every job is finished, polling again after `poll_after_seconds`.
   - Never resubmit a request whose outcome is unknown; resolve it with `jobs_wait` first.
   - Write `build/jobs/<name>.results.json` as a list of `{"index", "job_id", "status", "url"}`, with the result image URL for each index.
   - Run `python pipeline/lp.py fetch <name>`. It stages every image in `episodes/$ARGUMENTS/build/candidates/<name>/` and logs it with its hash; nothing in `images/` changes yet.
   - After the inspection in step 7, install the good ones with `python pipeline/lp.py accept <name> [--only ID ...]` (each replaced file is kept in `build/prefix_backup/`).
6. **Automatic checks.** Run `python pipeline/lp.py qa $ARGUMENTS` (and `python pipeline/lp.py qa --poses` if poses were made), then `powershell -File pipeline/ocr_scan.ps1 episodes/$ARGUMENTS/images` to find readable lettering. Run both again after every round of fixes.
7. **Independent full-size inspection (required before any composite or render).** Contact sheets are not enough: in episode 002 they hid about 80 faults. Run inspectors over every new or changed image at full size (1280 px or more) with the checklist in `channel/lessons.md` (anachronism, physics, text, continuity, what the line says), each batch re-checked by an independent skeptic. Compare every [same-as] pair side by side (gates, arches, people, furniture). Fix and re-inspect until nothing major remains. Then the **visual review** (against `channel/lessons.md` as well as the style review list). Look at every contact sheet (`episodes/$ARGUMENTS/build/sheets/`, `channel/assets/pose_sheets/`) against the image review list in channel/style.md, together with the qa flags. List each failure with its reason. Then run `python pipeline/compose_check.py $ARGUMENTS all` and check every Visitor composite: he has a real place in the set (never on top of people or props), the object his pose uses is beside him, his scale matches the people around him, and the same people stay the same people across shots of one place.
8. **Fix**, at most two attempts per image:
   - Small defect (stray text, a modern-dressed person, one wrong object): `python pipeline/lp.py jobs $ARGUMENTS --only S014 --edit "remove the sign above the door"`. Submit it as in step 5 (the job is named `backgrounds-$ARGUMENTS-edit`), fetch, inspect and accept. The edit starts from the exact accepted file; if that file was corrected locally, `lp.py jobs` stops and asks for it to be uploaded and recorded with `lp.py refs --file <path> <media_id>` first.
   - Wrong composition or style: `python pipeline/lp.py jobs $ARGUMENTS --only S014 S020`, then submit and fetch.
   - Poses: the same, with `--poses` instead of the slug.
   - List anything still failing after two attempts for the user.
9. **Placement.** Run `python pipeline/lp.py poses` (removes any green left), then `python pipeline/lp.py render $ARGUMENTS --preview`. Check each pose's size and position in its scene and adjust the `[pose: ...]` numbers in script.txt. This costs no credits.
10. **Report:** images made, fixed and still flagged, and credits used (`balance` before and after).

## Website route (by hand)
This route is free only if Higgsfield's Generate button shows 'Unlimited' for Nano Banana Pro at 2K on the owner's plan; if it shows a credit cost, it spends the same credits as the connector and needs the owner's OK first. If the owner prefers to generate on higgsfield.ai: `python pipeline/lp.py brief $ARGUMENTS` writes a helper page in `handoff/` (see `handoff/README.md`), then `python pipeline/lp.py import $ARGUMENTS inbox`.
