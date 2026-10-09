# Voice: ElevenLabs, directed like a real read

## Decision
- **One ElevenLabs voice for the whole channel,** chosen by audition and never changed mid-season.
- **Narration is directed, not just generated:** it is made one chapter at a time, you listen to every chapter, and any chapter that sounds off is redone.
- **The limits, honestly:** the best AI voices now win blind tests on short clips (ElevenLabs reports that [Eleven v4](https://elevenlabs.io/blog/eleven-v4), released 28 September 2026, ranked #1 on the [Artificial Analysis leaderboard](https://artificialanalysis.ai/text-to-speech/leaderboard) in September), but over ten minutes listeners can notice repeated intonation or a flat joke. The audition and the chapter retakes are where you remove those moments.

## Channel voice (locked 6 October 2026)
- **Amir – Calm, Natural Storyteller:** young American male, a Voice Library professional clone of a real voice actor. Voice ID `YPRmL2oHPibcUwJtQnPM`, saved in My Voices as "Amir - Life, Previously narrator".
- **Why him:** used by only about 576 accounts (versus about 294,000 for the first candidate, Jarnathan), so the voice can become recognizably ours. His delivery is natural and unhurried, with enough pitch movement for dry jokes. The owner must give two years' notice before withdrawing it.
- **Model: `eleven_v4`, chosen after the audition on 6 October 2026.** On the pilot's cold open, v4 matched the pitch variety of Amir's own preview (3.2 semitones, against 1.9 on Multilingual v2), read at a natural 177 words a minute, and got 98% of the words right. The clips are in `episodes/001-medieval-london-day/audio/audition/`.
  - **Tuning:** his clone isn't fine-tuned for v4 yet (that support is rolling out), so the `voice` command warns until it is. When it is, re-run the audition to confirm he still sounds the same.
  - **Fallback:** if you ever switch to `eleven_multilingual_v2`, `{sighs}`-style directions are dropped automatically, because that model would read them aloud.

## Plan and cost
- **Creator plan, [$22 a month](https://bigvu.tv/blog/elevenlabs-pricing-2026-plans-credits-commercial-rights-api-costs/):** about 100 minutes of audio (around 100,000 credits), commercial use, and Professional Voice Cloning (only needed for the upgrade path at the end).
- **Per episode:** the pilot is about 8,600 characters. Allow 20–30% extra for retakes, so roughly 11,000 credits per episode. Creator covers about eight episodes a month. Starter is too small once you count retakes.
- **Launch offer:** ElevenLabs is including 3x credits on Creator and higher plans until 12 October 2026 ([source](https://elevenlabs.io/blog/eleven-v4)). Subscribing before then makes the auditions and the pilot almost free.
- **Commercial use requires a paid plan.** Check ElevenLabs' terms on what happens to your rights if you cancel, and until then keep the plan active while you publish.
- **API key:** copy `.env.example` to `.env` and paste your key (ElevenLabs > Developers > API keys) after `ELEVENLABS_API_KEY=`.

## Choosing the voice (once, about an hour)
1. **Collect candidates** in the ElevenLabs Voice Library: filter for English and the narrative or storytelling use case, or search "documentary storyteller".
   - **Prefer voices cloned from real voice actors** (the library's professional voices). They have a real human timbre.
   - **Avoid the trending voices.** The fewer channels already use a voice, the more it can become recognizably ours.
   - **Check the notice period.** A library voice's owner can withdraw it after a notice period, so prefer voices with a long one.
   - **Or use Voice Design.** Describe the narrator and get a voice that exists only in your account. Starting prompt: "Warm, dry-humoured male narrator in his late thirties with a neutral, lightly British accent. Medium-low pitch, relaxed conversational pace, a slight smile in the voice, very clear diction, close-microphone documentary storyteller." (Swap the first part for "female narrator in her thirties" if you prefer.)
2. **Add four to six candidates** to My Voices and copy their voice IDs.
3. **Audition them all on the pilot's cold open, on both models:**
   `python pipeline/lp.py voice 001-medieval-london-day --audition ID1 ID2 ID3 ID4 --models eleven_v4 eleven_v3`
   - The same voice can sound quite different on v4 and v3, so compare both before deciding.
   - This costs about 965 characters per voice per model; the command shows the total and asks before spending.
   - The files land in `episodes/001-medieval-london-day/audio/audition/`.
4. **Listen on a phone speaker, without looking at names.**
   - Would you listen to this voice for ten minutes?
   - Do the jokes land without being pushed?
   - Could you recognize this voice again?
5. **Lock it:** put the winner's ID in `voice.voice_id` in `pipeline/config.json`. Never change it mid-season; a new voice regenerates every chapter.

## Settings (`voice` in pipeline/config.json)
- **Model:** `model_id` is `eleven_v4`, ElevenLabs' newest model ([docs](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)). It suits long-form narration and keeps the voice consistent across regenerated lines, which is exactly what chapter retakes need. It also takes up to 10,000 characters per request, against 5,000 for v3.
  - **It is one week old.** ElevenLabs says its direction tags are "not perfect yet", and Professional Voice Clone support is still rolling out.
  - **Fallbacks:** if a voice sounds better on v3 in the audition, set `eleven_v3`. If v4 misbehaves, use `eleven_multilingual_v2`, which is steadier, and remove the `{...}` tags.
  - **Endpoint:** if the regular Text to Speech API refuses v4, the pipeline automatically retries through ElevenLabs' Text to Dialogue API with a single speaker.
- **Settings:** v4 only uses Stability and Similarity. It has no Style or Speed, and no SSML.
  - **Stability 0.5** sounds natural. Lower is more expressive but riskier; higher is steadier but flatter.
  - **Similarity 0.75.**
- **Chapter gap:** `chapter_gap` is the pause between chapters, 0.6 seconds by default.

## Writing for the voice
- **Punctuation is direction.** Commas and full stops make pauses, "..." makes a longer beat, and a question mark lifts the line.
- **Years as words** ("thirteen-ninety"). Add any name the voice mispronounces to `voice.pronunciations`.
- **Direction tags** go in curly braces in the narration, sparingly, a handful per episode at most.
  - Short ones work: `{sighs}`, `{whispers}`, `{laughs}`. v4 also follows plain-English directions, such as `{said drily}` or `{trying not to laugh}`.
  - They reach ElevenLabs as `[sighs]` and so on, and never appear in captions.
  - Too many sound fake.
- **Short sentences, one idea each.**

## Workflow per episode
1. **Generate.** Run `python pipeline/lp.py voice <slug>`. It shows the character count and asks, then generates each chapter, joins them with a short pause, and aligns the result to the script. Images then cut exactly on the words, and captions are word-timed.
2. **Listen to every chapter** in `audio/chapters/` (`01_take1.mp3` onward). Listen for:
   - a stress on the wrong word, or a rushed joke;
   - an odd pronunciation, a strange breath or a glitch;
   - a jump in energy between chapters.
3. **Fix:**
   - **A weak chapter:** `voice <slug> --redo 4` makes a new take and charges only that chapter.
   - **The earlier take was better:** `voice <slug> --use 4:1`. Free.
   - **A word mispronounced everywhere:** add it to `pronunciations` and run `voice` again. Only chapters whose text changed regenerate.
   - **A line that never sounds right:** rewrite it in script.txt (and claims.md if a fact changes). Only that chapter regenerates.
4. When every chapter sounds right, render.

**Budget habit:** redo at most two or three chapters per episode. If a chapter fails twice, rewrite the line instead of paying for more takes.

**Any recording works with `align`.** If you ever generate on the ElevenLabs website instead, run `python pipeline/lp.py narration <slug> --tts` for paste-ready text, then `python pipeline/lp.py align <slug> narration.mp3`.

## Disclosure
YouTube's altered-or-synthetic label is for realistic content, so an animated video with a synthetic narrator who isn't a real person doesn't need it. Say it plainly in the description instead: "Illustrations and narration are made with AI tools from our own scripts and character designs."

## Sound identity
- The same voice, the same 2–3 second sound logo (`[sfx: sting]` after the cold open), and the same sign-off rhythm in every episode.
- Music only ever sits under the voice. The pipeline ducks it automatically whenever the narrator speaks.

## Upgrade path, once the channel earns
- **Licensed clone of a real narrator:** hire a marketplace narrator for a one-time licence fee. They record 30–60 minutes of training audio and pass ElevenLabs' [voice verification](https://elevenlabs.io/docs/eleven-api/guides/how-to/voices/professional-voice-cloning) on your account. You get an exclusive voice on the same $22 plan, and the workflow stays the same.
- **Or the narrator reads each episode** (about $40–100 per episode on Fiverr or Voice123), and you run `align` on their recording.
- **Either way,** switch at a season boundary. Get a written licence that covers perpetual worldwide online use, credit, and (for a clone) use on this channel only.
