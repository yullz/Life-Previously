# Life, Previously: channel kit

> **AI assistants:** read [AGENTS.md](AGENTS.md) first. It has the rules, the owner's preferences and the current status of every episode.

Everything needed to run a faceless illustrated history channel end to end, to a standard where viewers take it for a small studio's hand-made show: identity, look, voice, topics, the research and script workflow, and a pipeline that assembles the finished video.

The format follows Ink Explainer: illustrated stills answering everyday-life questions about the past. Four things make it ours and keep it from looking AI-made:
- **The Visitor**, a modern person dropped into the past who stands in for the viewer. He is drawn once as a fixed pose library and composited, so he never changes between shots.
- **One recognizable narrator voice** from ElevenLabs (Eleven v4), chosen by audition and directed chapter by chapter, with retakes.
- **A named place and year** ("London, 1390") instead of generic "ancient humans".
- **Sources shown on screen**, plus real sound design.

## Start here
1. Do the one-time setup in [channel/setup.md](channel/setup.md): choose the voice, build the character and pose library, and set up the channel.
2. Episodes live in [episodes/](episodes/). Episode 001 (medieval London) is scheduled and episode 002 (Pompeii) is finished; see the status table in [AGENTS.md](AGENTS.md).
3. Publish weekly, on Saturdays at 19:00 Sofia time, with three Shorts per episode (see "Publishing rhythm" in [channel/bible.md](channel/bible.md)).

## Folder map
| Path | What it is |
|---|---|
| [channel/bible.md](channel/bible.md) | Identity, episode structure, writing, title and thumbnail rules |
| [channel/style.md](channel/style.md) | Look, pose library, motion, sound, how we avoid looking AI-made |
| [channel/voice.md](channel/voice.md) | ElevenLabs voice choice, settings, chapter retakes |
| [channel/topics.md](channel/topics.md) | Audience check and the first 40 topics |
| [channel/setup.md](channel/setup.md) | Accounts, assets, channel page, monetization, tax |
| `channel/poses.json`, `channel/assets/` | Pose list, Visitor drawings, style key, paper texture |
| `channel/sfx/` | Sound effects (the names the scripts use are listed in its README) |
| `AGENTS.md` | The guide for any AI assistant: rules, owner preferences, status |
| `CLAUDE.md`, `GEMINI.md`, `.claude/commands/` | Entry points for Claude Code and Gemini (they import AGENTS.md) and the slash commands |
| `templates/` | Claim sheet, script, package and QA checklist |
| `pipeline/lp.py`, `pipeline/config.json` | The pipeline and its settings |
| `episodes/` | One folder per episode |
| `music/` | The channel theme (`life_previously_theme.mp3`), made for the channel |
| `reference/` | The earlier channel research, kept for background |

## Making an episode (9 to 14 hours)
Open Claude Code in this folder, then:

| Step | You run | You get | Time |
|---|---|---|---|
| 1. Topic and research | `/episode-research Egyptian tomb builders' day off` | Audience verdict and a sourced `claims.md` | 2–4 h |
| 2. Script | `/episode-script 003-<slug>` | `script.txt` with poses and sound cues, passing `lp.py check` | 2–3 h |
| 3. Narration | `python pipeline/lp.py voice 003-<slug>`, listen, then `--redo N` any weak chapter | `audio/narration.wav`, exact cut times, `captions.srt`, `chapters.txt` | 30–60 min |
| 4. Pictures | `/episode-images 003-<slug>` (asks before spending credits) | Every background and any new pose made on Nano Banana Pro at 2K, checked automatically and by eye, failures fixed | 15 min of your time |
| 5. Preview | `python pipeline/lp.py render 003-<slug> --preview --music music/life_previously_theme.mp3` | A fast 540p draft. Fix pose placement and timing | 1 min plus watching |
| 6. Final | `python pipeline/lp.py render 003-<slug> --music music/life_previously_theme.mp3` | `output/003-<slug>.mp4` | 2–5 min |
| 7. Package | `/episode-package 003-<slug>` | Three titles, `thumbnail.jpg`, description | 1 h |
| 8. QA and upload | Tick `qa.md`, upload with the settings in setup.md | A published video | 1 h |

You can render at any point: missing backgrounds show as labelled placeholders, missing poses as orange stand-ins, and missing sound effects are skipped with a warning. Anything that spends credits (voice, images) states the cost and asks first.

## Script format
```
TITLE: What Did Egyptian Workers Do on Their Day Off?
## Chapter name
::: A narrow Roman street at night, carts rumbling past, space on the right [pose: cover-nose right] [sfx: cart-wheels]
Narration for this image, 10 to 22 words.
::: A bronze law tablet on a desk [note: Tabula Heracleensis, c. 45 BCE] [zoom-in]
{sighs} Narration for the next image.
```
- **`:::`** starts a new image. The text after it describes the background only; the Visitor is added with `[pose: name position size flip]`.
- **Camera:** `[zoom-in]` `[zoom-out]` `[pan-left]` `[pan-right]` `[still]`.
- **Other tags:** `[reuse S004]` shows an earlier image again, `[same-as: S001]` draws a new shot of the same place as S001 (its image is attached as a reference), `[note: ...]` puts a source label on screen, and `[sfx: name volume +seconds]` plays a sound effect.
- **Voice directions:** in narration lines, `{sighs}`, `{whispers}` and so on are sent to ElevenLabs only. Use them sparingly.
- **Scene IDs:** `lp.py` writes an ID into each scene line (`::: S014 | ...`). Never renumber them by hand.

## Changing things later
- **Prompts, poses, tags or sound cues:** render again. Only changed scenes re-render.
- **Narration text:** run `voice` again. Only chapters whose text changed are regenerated and charged, and the timing realigns automatically.
- **Voice, style, character or model:** don't, mid-season.

## Launch plan and how to judge it
- **Cadence:** weekly, Saturdays at 19:00 Sofia time, plus three Shorts (see "Publishing rhythm" in channel/bible.md).
- **The test is the first 12 episodes.** Don't judge before then; Ink Explainer's big hit was its 14th upload.
- **Per video, check YouTube Studio at 48 hours and at 28 days:** click-through rate against your own average, average percentage viewed, viewers still watching at 0:30, and returning viewers.
- **What to do with the numbers:**
  - Low click-through but good retention: fix titles and thumbnails.
  - Most viewers gone before 0:30: fix the cold open.
  - One era or question type does three times better: make more of it.
- **Stop or rethink** if, after 12 episodes, no video has passed 10K views and average percentage viewed stays under 30%.

## Money and costs
- **No ad income before the Partner Program** (thresholds in setup.md). After that, very roughly $3–10 per 1,000 views in this niche.
- **The tutorial's "$98K/month" is not real.**
- **Monthly:**
  - ElevenLabs Creator: $22, which covers about eight episodes including retakes.
  - Music and sound effects: the channel theme is our own and effects are generated (`lp.py sfx`), so no library subscription is needed unless the owner wants one.
- **Per episode:** about 250-290 Higgsfield credits (about 110 images at 2 credits on Nano Banana Pro 2K, plus fixes and thumbnails; episode 002 used 264 before its fix round). `/episode-images` shows the estimate and asks first.
- **One-time:** illustrator cleanup of the model sheet and pose library. Get quotes.
- **Your time:** 9 to 14 hours per episode.
