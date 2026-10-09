# Episode 003 production state (resume point)

Read this first after any context reset. It is the single source of truth for where the end-to-end run stands.
Update it after every batch. Executor: Claude Opus 5.5. Last updated: 2026-10-09 (DELIVERED FOR REVIEW).

## Authority
- Assignment: `handoff/director_to_claude_episode_003_finish_2026-10-09.json` (EP003-FINISH-001). Earlier: version 4 assignment + preflight report.
- Owner approved the spend in chat on 2026-10-09 ("Yes, approve both"): Higgsfield up to 101 results ≈ 202 credits (90 core + 1 thumbnail backdrop + max 10 repairs); ElevenLabs 9 chapters + max 2 retakes, ≤ 13,769 credits. No top-ups, no publishing, no episode 001/002 changes, no agents.
- **Owner raised the paid repair cap from 10 to 25 in chat (2026-10-09): "increase the paid repair cap to 25"**, then: "don't pay for easy and meaningless repairs. If its a small detail you can fix do it instead of spending". New ceiling: 116 results ≈ 232 credits. Small details are fixed locally (free); pay only for faults a local fix cannot solve cleanly.
- Do not ask the owner routine questions. Material blockers go into the completion report for Astra.

## Price checks (actual)
- First Higgsfield charge on Ultra: "Nano Banana Pro" −2 credits (S014, 2026-10-09T01:32Z). Service labels jobs `nano_banana_2` (same label as earlier billed Nano Banana Pro jobs).
- Voice: 9 chapters, 10,825 characters, 1,310 credits (account 7,866 → 9,176 used of 131,000).
- One b03 job (S100, 84a7365a-…) ended `failed` (no image); recorded in `build/jobs/ep003-b03.failed.json`; retried as `ep003-b03-s100`. Check whether the failed job was charged (transactions) before the report.

## Results used (paid)
Core submitted: pilot-s014 1, pilot-1 8, pilot-s050 1, anchors-2 6, b02 12, b03 12 (1 failed, no image), b03-s100 1, b04 12, b05 12, b06 12, b07 12 → 89. Remaining core: S105, S095 (S095 needs S031 from b07).
Repairs: **19 of 25** — S014, S001, S003, S011, S071, S103, S050, S010, S043, S022, S046, S050-2 (not accepted), S100-1 (not accepted), S050-3, S086-1, S094-1, S034-1, S030-1 (not accepted), S030-2.
Left within the owner ceiling (116 = 90 core + 1 thumbnail + 25 repairs): 2 core + 1 thumbnail backdrop + 6 repairs.

## Done
- Free fixes from the finish handoff (pose resolver, cleaned poses, source notes/cards, overlays, 15 graphics, TTS aliases, prompt fixes) — see earlier notes in the completion draft; tests 29 OK; `lp.py check` OK.
- Narration: 663.96 s (11:04), aligned 98%; one item to listen for: S003 "Deir el-Medina" ASR'd as "...Nadina" (0:14). No retakes. Not listened to by a human or by Claude.
- Accepted images (model or repaired): S001 S002 S003 S004 S005 S006 S007 S010 S011 S012 S014 S016 S017 S018 S019 S020 S021 S022 S023 S025 S027 S034 S035 S037 S039 S043 S050 S053 S055 S056 S057 S062 S064 S070 S071 S096 S097 S103 + 15 graphics.
- Local fixes (free, all staged → inspected at full size and in composite → installed with backup + log `accepted_local_fix`): S064, S070 (round 1, `local_fix.py`); round 2 (`build/graphics/local_fix2.py`, sources pinned by hash, per-fix seeds, reproducible): S037 reflect-extend; S064 near-wall edge; S006 panel fill; S017 rebuilt from S014 with the basket on the floor between bench and post (owner asked: not in front of the door); S019 1.33x crop; S023 white strip filled from S014; S055 table+stool removed (owner caught: not in any other view) + hinge plates painted out; S062 tomatoes→onions + added window/light shaft removed (from S014); S056 crop to upper body (legs shared one foot); S035 crop (was same framing as S096).
- Prompt plan revisions (all logged in plan `revisions`, for Astra): people-count/style lock; fully-drawn guard (no blank/white reserved space); no-new-fixtures guard (51 edits); one-camera guard (50 prompts).
- Lessons: `channel/lessons.md` top entries + `channel/learning_register.json` LP-L026 (camera/ground/scale check, owner caught S022) and LP-L027 (blank reserved space; blanket exclusions deleting built-ins).

## Per-image check (write it down for every image before accepting)
People count; period objects (no tomatoes/potatoes/maize/metal hinges/modern stools…); no lettering; no blank/white/framed areas; **one camera height and horizon; one believable ground; doors taller than people; nearer = larger; nothing floating**; continuity with parent (no vanished built-ins, no new furniture/windows); narration fit (the picture must not contradict the line); composite check with `scene_preview.py --bg-dir` for posed/card scenes.

## Status: delivered for review
- All 105 scenes have accepted images. Paid: 111 results submitted, 1 failed (refunded), 110 billed = 220 credits; balance 2,859.78. Repairs 20 of 25.
- Candidate: `build/director_review/render/003_candidate_c2.mp4` (sha256 a9856479...4453f, 11:07, -14.1 LUFS, -1.4 dBTP, final_check PASS). c1 superseded (S062 shelf).
- Thumbnail D v3 on S050 installed (`thumbnail.jpg`, `thumbnail_master.png`, `thumbnail_small.png`); record `build/director_review/thumbnail_D_final/installed.json`.
- Shorts: `build/director_review/render/shorts_c2/` (spec `shorts.json`).
- Review folder: `REVIEW EPISODE 003/` (hashes in `build/director_review/render/review_folder_hashes.json`).
- Report: `handoff/claude_to_director_episode_003_completion_2026-10-09.json` (job IDs: `build/director_review/render/higgsfield_jobs.json`; local fixes: `local_fixes.json`).
- Not done (needs approval): master render to `output/`, upload, scheduling. Not done (no ability): listening pass.
- If the director asks for changes: edit images with `local_fix2.py` or a documented repair, re-render a new candidate name (`--out .../003_candidate_c3.mp4`), re-run final_check, Shorts and the review folder (preserve the old folder in a dated subfolder first).

## How to continue a batch (no duplicate submissions)
1. Never resubmit a job whose `.pending.json` exists without first calling `jobs_wait` on its IDs. A job reported `failed` by the service is known (no image) and may be retried as a new job.
2. Results: `python episodes/003-egyptian-workers/build/graphics/hf_glue.py results <job> '<jobs_wait jobs json>'` (failed ones go to `<job>.failed.json`), then `python pipeline/lp.py fetch <job>`.
3. Inspect every staged image at full size (`build/candidates/<job>/`), then `python pipeline/lp.py accept <job> --only ...`.
4. Ready edits: `python pipeline/lp.py jobs 003-egyptian-workers --prompts episodes/003-egyptian-workers/build/director_prompt_plan.json --only ... --name ep003-bNN` (≤12), print with `hf_glue.py print <job>` (PYTHONIOENCODING=utf-8). Audit the scene line of every prompt before paying.
5. Repairs: hand-written `build/jobs/ep003-repair-*.json` (edit of the candidate's job_id or a better accepted same-place parent; documented failed criteria).
6. Local fixes: add a function to `local_fix2.py` with a hash-pinned source, `stage`, inspect (full size + `scene_preview.py <out> --bg-dir episodes/003-egyptian-workers/build/candidates/localfix2 <ids>`), then `install`.
