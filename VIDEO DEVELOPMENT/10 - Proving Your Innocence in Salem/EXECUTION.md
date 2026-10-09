# Execute this episode

Production slug: salem-1692. Run commands from the project root. Do not start while director_to_claude.json says development_in_progress.

1. Copy this folder's script.txt, claims.md, period.txt, package.md, qa.md and all JSON specification files to episodes/salem-1692/; put research.md and sources.json under research/ as well. Create images/, audio/, thumbs/, overlays/, output/ and build/. Do not overwrite an existing production folder; inspect/resume it. Preserve this source folder.
2. Run python pipeline/lp.py check salem-1692. Facts must be checked, not overridden.
3. Quote live costs for 73 episode illustrations,3 thumbnail backgrounds, 8 voice chapters, any dedicated wardrobe artwork in wardrobe_spec.json, and the sound_plan.json assets plus a bounded repair reserve. Obtain one owner allowance.
4. Build the local graphics from visual_assets.json into images/<scene_id>.png. No graphic is a paid image request. Implement sound and pronunciation specifications. Resolve/hash all Visitor source files. Read wardrobe_spec.json and ../WARDROBE_POLICY.md; build and review episode-private outfit variants before main backgrounds or compositing. Declare reviewed derivatives in this episode's poses/poses.json using the original pose names and exact sha256.
5. Generate and actually listen to the narration by chapter; run voice_diff.py. Confirm actual duration before the main image batch.
6. Export the pilot jobs with python pipeline/lp.py jobs salem-1692 --prompts episodes/salem-1692/director_prompt_plan.json --only <the listed paid scene IDs> --name salem-1692-pilot. Submit through Higgsfield only after allowance. Record IDs immediately, fetch to staging, inspect full size, then accept exact reviewed files.
7. Export successive jobs with the same --prompts option. Anchors must be accepted before dependent edits; resolve/upload/hash the accepted parent. Never fall back to default generated prompts. Continue in reviewable batches.
8. Build the three dedicated thumbnail backdrops through the connector using thumbnail_requests in image_prompts.json. Compose the supplied typography and Visitor geometry locally.
9. Run python pipeline/compose_check.py salem-1692 all. Render a preview, then a named candidate with lp.py render and the existing channel theme. Use --out within this episode's build/director_review/ and preserve earlier candidates.
10. Run final_check.py and review_manifest.py against that exact candidate. Inspect images/composites and actually play the complete candidate with audio; fix affected inputs and recheck only impacted plus final playback gates.
11. Resolve shorts_plan.json against actual alignment, write native shorts.json, render the three portrait cuts and inspect/listen to all three. Use pipeline/shorts.py --video <chosen candidate> --out <review folder>.
12. Fill exact chapter times in package.md, refresh packaging checks, and deliver REVIEW salem-1692/ with film,3 thumbnail variants (A lead), captions, upload copy and3 Shorts plus README and hashes. Read ../PRODUCTION_CONTRACT.md for the full acceptance standard. Do not publish.

Routine image defects: identify exact mismatch, replace the offending element with the specified period-correct one, edit only the accepted local version, inspect the entire result before accepting. Shared defects stop the affected batch. Semantic/script changes return to Astra with exact evidence; no silent rewrite.
