# One-time setup (about a week)

## 1. Accounts and people
| What | Used for | Cost |
|---|---|---|
| YouTube, on a Google brand account | The channel | Free |
| ElevenLabs Creator | The narrator voice ([voice.md](voice.md)) | $22 a month |
| An illustrator (Fiverr Pro, Upwork, ArtStation, Behance) | Cleaning up the Visitor model sheet and pose library, under a written rights assignment | One-time; get quotes |
| Higgsfield (Plus plan) | Backgrounds, poses and thumbnails, generated automatically through the Claude connector | Credits: Nano Banana Pro at 2K is 2 credits an image, so about 250-290 per episode (about 110 images plus fixes and thumbnails). The website's unlimited models are only for manual work. |
| Epidemic Sound or Artlist (or the free YouTube Audio Library) | Optional: the channel uses its own theme (`music/life_previously_theme.mp3`) and generated sound effects (`lp.py sfx`) | Not needed now |
| Claude Code | Research, scripts, prompts, running the pipeline | You already have it |

## 2. This computer
- Python 3.11+, ffmpeg, Pillow and faster-whisper are installed. The speech model used for alignment downloaded on 5 Oct 2026 during testing.
- Copy `.env.example` to `.env` and paste your ElevenLabs API key after `ELEVENLABS_API_KEY=`. Never share or upload `.env`.
- Test: `python pipeline/lp.py check 001-medieval-london-day` should print the pilot's stats with no warnings.

## 3. Voice (about an hour)
Follow "Choosing the voice" in [voice.md](voice.md):
1. Collect four to six candidates from the Voice Library (or Voice Design).
2. Audition them on the pilot's cold open with `voice --audition`.
3. Pick the winner by listening on a phone speaker, and put its ID in `pipeline/config.json`.

## 4. Character, poses and look (3–5 days, plus credits)
Follow [style.md](style.md):
1. Generate the Visitor model sheet and choose one. Have the illustrator clean it up, then save it as `channel/assets/visitor_sheet.png`.
2. Run `python pipeline/lp.py poses` and make the 43 pilot poses from `channel/assets/visitor/to_make.md`. Remove the backgrounds and have the illustrator touch them up. Check them all together with `python pipeline/lp.py sheet --poses`.
3. Generate and approve the style key: `channel/assets/style_key.png`.
4. Run the background model bake-off and write the winner into `images.model` in `pipeline/config.json`.
5. Get the sound effects listed in `channel/sfx/README.md`, including the 2–3 second `sting` sound logo. Pick a music bed for the pilot and put it in `music/`.
6. Make the avatar and banner.

## 5. YouTube channel
1. **Create the channel** on a brand account, named "Life, Previously", with the handle @LifePreviously (or a fallback from bible.md).
2. **Profile:** upload the avatar and banner, paste the About text from bible.md, and add a contact email (a separate Gmail address for the channel).
3. **Verify the phone number** under YouTube Studio > Settings > Channel > Feature eligibility. This unlocks custom thumbnails and longer videos.
4. **Upload defaults:**
   - Category: Education. Language: English.
   - Paste the description template from `templates/package.md`.
5. **Playlists:** Medieval Life, Ancient Rome, Ancient Egypt, Asia, Modern History.
6. **Per upload:**
   - Upload `captions.srt` under Subtitles, and paste the chapters into the description.
   - Add the end screen and the playlist.
   - Assess the current Studio AI-use question for each video, including visuals and audio, using `channel/seo.md`; the owner selected No for the eight uploads scheduled on 9 Oct. Omit optional AI/tool-production notes from public descriptions; keep required credits and accurate internal provenance.

## 6. Monetization and tax
- **YouTube Partner Program (ads):** 1,000 subscribers plus 4,000 public watch hours in the last 12 months, or 10 million Shorts views in 90 days.
  - Researchers reported that from 1 Feb 2027, new applicants will need 8,000 watch hours. This was not double-checked, so confirm it on YouTube's Partner Program help page.
  - Either way, apply the day you qualify.
- **Earlier tier (memberships, Super Thanks):** 500 subscribers, 3 public uploads in 90 days, and 3,000 watch hours in 12 months (or 3 million Shorts views in 90 days).
- **AdSense:** one account per person. Add US tax info (form W-8BEN) and claim the Bulgaria–US treaty rate.
- **Bulgaria:** before your first payout, ask an accountant about registering this income, VAT registration for services to Google Ireland, and income tax.

## 7. Guardrails (why the kit is built this way)
- **Original scripts.** YouTube refuses to monetize mass-produced or interchangeable content and content that copies another format too closely, judged across the channel. Scripts come only from your own research, never from another channel's transcript.
- **Consistent identity.** One auditioned voice, a fixed character, one style and real sound design make the channel recognizably one creator's work.
- **Proof of your process.** Keep each episode's `claims.md`, script drafts, chapter takes and project files. They are your evidence if a monetization review ever questions the channel.
- **Owning your assets.** Get a written rights assignment from the illustrator, and register the show name as a trade mark once the channel shows traction.
