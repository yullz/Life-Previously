# Channel info — copies of the key documents

Copied on **2026-10-09** from the project folder, so everything about the channel and how it is made is in one place.

**These are copies.** The assistants keep updating the originals, so a copy can go out of date. Each entry below says where the original lives. Ask Claude to refresh this folder at any time. Edits made here are not seen by the assistants; change the originals instead.

Not copied on purpose: the private keys file (`.env`), videos, audio, episode pictures and program code.


## 1 - Start here

| File | What it is | Original |
|---|---|---|
| AGENTS.md | The main guide: how the owner wants the work done, the hard rules, where every episode stands, money and credits, how an episode is made | `AGENTS.md` |
| UPLOAD SCHEDULE.md | What goes live when (episodes and Shorts, Sofia time) | `UPLOAD SCHEDULE.md` |
| Project README.md | Overview of the production kit and the script format | `README.md` |
| CLAUDE.md | Entry note for Claude (points to AGENTS.md) | `CLAUDE.md` |
| GEMINI.md | Entry note for Gemini (points to AGENTS.md) | `GEMINI.md` |

## 2 - Channel identity and style

| File | What it is | Original |
|---|---|---|
| bible.md | The channel's identity: what an episode is, structure, length, writing rules, titles, publishing rhythm | `channel/bible.md` |
| style.md | The look: drawing style, the Visitor and his poses, camera motion, sound | `channel/style.md` |
| voice.md | The narrator voice and its settings | `channel/voice.md` |
| thumbnails.md | Thumbnail rules and the research behind them | `channel/thumbnails.md` |
| seo.md | Titles, descriptions, tags, AI-disclosure notes, the title clone check | `channel/seo.md` |
| topics.md | Topic research, audience demand and the topic list | `channel/topics.md` |
| setup.md | Accounts, subscriptions and one-time channel setup | `channel/setup.md` |
| poses.json | The list of approved Visitor poses | `channel/poses.json` |
| sound effects README.md | What each sound effect is and where it may be used | `channel/sfx/README.md` |
| sound effects list.json | Sound effect catalogue (machine-readable) | `channel/sfx/sfx.json` |

## 3 - Lessons learned

| File | What it is | Original |
|---|---|---|
| lessons.md | Every past mistake, written as a check to do next time | `channel/lessons.md` |
| learning_register.json | Structured record of each issue: cause, fix, prevention, status | `channel/learning_register.json` |
| learning_loop.json | How lessons are applied before, during and after each job | `channel/learning_loop.json` |

## 4 - How production works

| File | What it is | Original |
|---|---|---|
| production_workflow.json | Who does what (Astra directs, Claude produces, owner approves spend and publication) | `channel/production_workflow.json` |
| quality gates (qa template).md | The quality gates every episode must pass | `templates/qa.md` |
| package template.md | Template for an episode's titles, thumbnail, description, tags | `templates/package.md` |
| claims template.md | Template for the fact-check sheet (every claim with its source) | `templates/claims.md` |
| period template.txt | Template for the period look notes | `templates/period.txt` |
| script template.txt | Template for a script | `templates/script.txt` |
| learning review template.json | Template for the end-of-job lessons review | `templates/learning_review.json` |
| step guide - 1 research.md | Step-by-step: research and fact-check | `.claude/commands/episode-research.md` |
| step guide - 2 script.md | Step-by-step: write the script | `.claude/commands/episode-script.md` |
| step guide - 3 images.md | Step-by-step: make and check the images | `.claude/commands/episode-images.md` |
| step guide - 4 package.md | Step-by-step: titles, thumbnails, description, Shorts | `.claude/commands/episode-package.md` |
| pipeline settings.json | Production settings: voice, image model, banned phrases, thumbnail fonts (no passwords or keys) | `pipeline/config.json` |
| making images on the website.md | How to make the images yourself on higgsfield.ai | `handoff/README.md` |

## 5 - YouTube publishing

| File | What it is | Original |
|---|---|---|
| youtube_publication_2026-10-09.json | Receipts for the uploads: video IDs, schedule, captions, thumbnails, playlists | `handoff/youtube_publication_2026-10-09.json` |
| youtube_saved_metadata_2026-10-09.json | Titles, descriptions and settings as saved in YouTube Studio | `handoff/youtube_saved_metadata_2026-10-09.json` |
| youtube_shorts_metadata_2026-10-09.json | Shorts titles, descriptions and schedule | `handoff/youtube_shorts_metadata_2026-10-09.json` |
| youtube_tag_coverage_2026-10-09.json | Tags used per upload | `handoff/youtube_tag_coverage_2026-10-09.json` |
| owner_publication_authorization_2026-10-09.json | Your go-ahead to publish episodes 001 and 002 | `handoff/owner_publication_authorization_2026-10-09.json` |
| ai_disclosure_decision_2026-10-09.json | The AI-disclosure decision and its reasoning | `handoff/ai_disclosure_decision_2026-10-09.json` |
| public_copy_update_2026-10-09.json | Changes to public text (descriptions, About) | `handoff/public_copy_update_2026-10-09.json` |
| astra_youtube_release_plan_2026-10-08.json | The release plan for the first two episodes | `handoff/astra_youtube_release_plan_2026-10-08.json` |
| youtube_setup (episode 001).md | How the first upload was set up in YouTube Studio | `episodes/001-medieval-london-day/youtube_setup.md` |

## 6 - Episodes

| File | What it is | Original |
|---|---|---|
| 001 - London 1390 / package.md | Title, thumbnail, description, tags, chapters | `episodes/001-medieval-london-day/package.md` |
| 001 - London 1390 / narration script.md | The narration as spoken | `episodes/001-medieval-london-day/narration_script.md` |
| 001 - London 1390 / claims (fact-check).md | Every fact with its source and check date | `episodes/001-medieval-london-day/claims.md` |
| 001 - London 1390 / qa (quality gates).md | Quality gates for this episode | `episodes/001-medieval-london-day/qa.md` |
| 001 - London 1390 / chapters.txt | Chapter list | `episodes/001-medieval-london-day/chapters.txt` |
| 002 - Pompeii AD 79 / package.md | Title, thumbnail, description, tags, chapters | `episodes/002-pompeii-life/package.md` |
| 002 - Pompeii AD 79 / script.txt | The script (narration with picture notes) | `episodes/002-pompeii-life/script.txt` |
| 002 - Pompeii AD 79 / claims (fact-check).md | Every fact with its source and check date | `episodes/002-pompeii-life/claims.md` |
| 002 - Pompeii AD 79 / qa (quality gates).md | Quality gates for this episode | `episodes/002-pompeii-life/qa.md` |
| 002 - Pompeii AD 79 / chapters.txt | Chapter list | `episodes/002-pompeii-life/chapters.txt` |
| 003 - Egyptian workers / package.md | Title, thumbnail, description, measured chapters, tags, Shorts | `episodes/003-egyptian-workers/package.md` |
| 003 - Egyptian workers / narration script.md | The narration as spoken | `episodes/003-egyptian-workers/narration_script.md` |
| 003 - Egyptian workers / claims (fact-check).md | Every fact with its source and check date | `episodes/003-egyptian-workers/claims.md` |
| 003 - Egyptian workers / qa (quality gates).md | Quality gates for this episode | `episodes/003-egyptian-workers/qa.md` |
| 003 - Egyptian workers / director brief.md | Astra's brief for this episode | `episodes/003-egyptian-workers/director_brief.md` |
| 003 - Egyptian workers / visual direction.md | Shot plan and visual rules | `episodes/003-egyptian-workers/visual_direction_v4.md` |
| 003 - Egyptian workers / production state.md | Where production stands: spend, repairs, fixes, next steps | `episodes/003-egyptian-workers/build/PRODUCTION_STATE.md` |
| 003 - Egyptian workers / completion report.json | The delivery report for Astra (files, checks, costs, limits) | `handoff/claude_to_director_episode_003_completion_2026-10-09.json` |
| 003 - Egyptian workers / director assignment (finish).json | Astra's assignment for finishing episode 003 | `handoff/director_to_claude_episode_003_finish_2026-10-09.json` |

## 7 - Future videos

| File | What it is | Original |
|---|---|---|
| README.md | The eighteen-video development library: what it is and its state | `VIDEO DEVELOPMENT/README.md` |
| GOAL.md | What was commissioned (eighteen episodes) | `VIDEO DEVELOPMENT/GOAL.md` |
| STATUS.json | Progress tracker for each future video | `VIDEO DEVELOPMENT/STATUS.json` |
| PRODUCTION_CONTRACT.md | What a finished development package must contain | `VIDEO DEVELOPMENT/PRODUCTION_CONTRACT.md` |
| ADDITIONAL_FIVE.md | The five extra topics chosen for UK/US/Canada/Australia | `VIDEO DEVELOPMENT/ADDITIONAL_FIVE.md` |
| EAST_ASIA_SELECTIONS.md | The China, Japan and Korea episodes | `VIDEO DEVELOPMENT/EAST_ASIA_SELECTIONS.md` |
| WARDROBE_POLICY.md | Visitor costume rules (for example the pirate hat) | `VIDEO DEVELOPMENT/WARDROBE_POLICY.md` |
| DEVELOPMENT_CHECKPOINT.md | Latest development checkpoint | `VIDEO DEVELOPMENT/DEVELOPMENT_CHECKPOINT.md` |
| next 10 video ideas.md | The ten video ideas proposed | `handoff/next_10_video_ideas_2026-10-09.md` |
| next 10 video ideas - selected.md | The ten ideas you selected | `handoff/next_10_video_ideas_selected_2026-10-09.md` |
| episode 003 topic options.md | How the episode 003 topic was chosen | `handoff/episode_003_topic_options_2026-10-09.md` |

## 8 - Background research

| File | What it is | Original |
|---|---|---|
| channel research report.md | The original channel research report | `reference/astra6-report.md` |
| catalog_forensics.md | What similar history channels publish | `reference/research/catalog_forensics.md` |
| demand_behavior.md | How audiences behave and what they watch | `reference/research/demand_behavior.md` |
| demand_history_and_systems.md | Demand for history topics | `reference/research/demand_history_and_systems.md` |
| money_claims_and_economics.md | Monetisation and earnings claims, checked | `reference/research/money_claims_and_economics.md` |
| names_and_distinctiveness.md | Channel naming and standing out | `reference/research/names_and_distinctiveness.md` |
| platform_policy_risk.md | YouTube policy risks (AI content, reuse) | `reference/research/platform_policy_risk.md` |
| production_stack.md | Tools and production stack | `reference/research/production_stack.md` |
| saturation_and_clones.md | Saturation and copycat channels | `reference/research/saturation_and_clones.md` |
| script_forensics.md | What makes scripts work | `reference/research/script_forensics.md` |

## 9 - Brand images

| File | What it is | Original |
|---|---|---|
| channel avatar (800px).png | Profile picture | `channel/brand/avatar_800.png` |
| channel banner (2560x1440).png | Channel banner | `channel/brand/banner_2560x1440.png` |
| logo (2048px).png | Logo | `channel/brand/logo_2048.png` |
| logo transparent (1024px).png | Logo on a transparent background | `channel/brand/logo_transparent_1024.png` |
| logo.svg | Logo as a scalable vector file | `channel/brand/logo.svg` |
| video watermark (150px).png | The small watermark used on videos | `channel/brand/watermark_150.png` |

## Also worth knowing
- `REVIEW EPISODE 003/` (project root): the finished episode 003 for review.
- `VIDEO DEVELOPMENT/` (project root): the full folders for the eighteen future videos.
- `handoff/`: the complete history of assignments and reports between Astra and Claude.
