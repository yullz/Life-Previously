# Research: production_stack

Collected 5 Oct 2026 by an independent research agent. Confidence labels are the agent's own.

## Headline
The tutorial stack works but is the slow, generic version: keep Claude and ElevenLabs, keep Higgsfield/OpenArt only as credit-metered image backends, drop TurboScribe, and replace hand assembly in CapCut with a Claude Code-built Remotion or ffmpeg rough cut driven by a scene manifest and TTS timestamps. Tool cost is minor (stills cost $0.01-0.14 each; roughly $10-110 per month for four episodes); labour (about 18-28 hours per 10-minute episode, my unmeasured estimate) and character consistency are the real constraints. The tutorial-era default image model is dated (GPT Image 2.5 now leads the edit leaderboards), image-to-video is poor value on flat 2D art, and Astra's paper-puppet raccoon in textured miniature scenery is the hardest proposed look to keep consistent unless built as a reusable cut-out asset library.

## Findings

### F1 [high] The tutorial-era default (Nano Banana Pro) is dated: OpenAI GPT Image 2.5 (Flare and Sunburst, released 8 Sep 2026) now leads public image-edit and text-to-image leaderboards; Google's image models sit mid-table.
Arena image-edit board (updated 29 Sep 2026): gpt-image-2.5-sunburst 1522, flare 1478, gpt-image-2 medium 1461, seedream-5.0-pro 1394, gemini-3-pro-image-2k 1390, gemini-3.1-flash-image 1387. Artificial Analysis text-to-image: Sunburst 1197, Nano Banana 2 1125, Nano Banana Pro 1102. These boards measure general blind preference, not recurring cartoon-character consistency, so a head-to-head test on the user's own character is still needed.
- source: https://arena.ai/leaderboard/image-edit
- source: https://artificialanalysis.ai/image/leaderboard/text-to-image

### F2 [medium] All leading models accept multiple reference images and cost roughly $0.01-0.14 per still, so per-image price is not the binding constraint; rerolls and review time are.
Google docs: Nano Banana 2 takes 10 object + 4 character + 3 style references, $0.067 (1K) / $0.101 (2K), batch half; Nano Banana Pro 6 object + 5 character, $0.134. GPT Image 2.5: up to 16 references (Higgsfield blog); GPT Image 2 about $0.01 low / $0.05 medium / $0.17 high at 1536x1024 (third-party calculators). Seedream 5.0 Pro $0.045, FLUX.2 pro from $0.03, Ideogram 3.0 $0.03-0.09, Recraft V4 $0.04.
- source: https://ai.google.dev/gemini-api/docs/pricing
- source: https://ai.google.dev/gemini-api/docs/image-generation
- source: https://developers.openai.com/api/docs/pricing
- source: https://higgsfield.ai/blog/gpt-image-2-5-higgsfield
- source: https://www.segmind.com/models/gpt-image-2/pricing

### F3 [medium] Capability split: the GPT Image family is strongest on exact text and reference adherence; Nano Banana 2 is faster and stronger at style adaptation; Midjourney V8.2 cannot be driven by an agent pipeline.
OpenArt's 17 Sep 2026 comparison citing Arena: GPT Image 2 leads Text Accuracy (1,120) and Reference Adherence (1,035 vs 991); Nano Banana 2 leads Style Adaptation (1,065) and renders 1K in 18.1 s vs 44.8 s. An Atlas Cloud test found Seedream 5.0 produced gibberish text. A 22 Sep 2026 Midjourney guide: omni and character reference unsupported on V8.2, Edit Model takes four references, no official API described.
- source: https://openart.ai/blog/gpt-image-2-vs-nano-banana-2/
- source: https://www.atlascloud.ai/blog/tips/2026-ai-image-api-benchmark-gpt-image-2-vs-nano-banana-2-pro-vs-seedream-5-0
- source: https://blakecrosley.com/guides/midjourney

### F4 [medium] Higgsfield through the Claude connector always burns credits; the advertised unlimited image windows apply only to manual use on higgsfield.ai, and Soul ID is designed around photo-trained identities rather than 2D mascots.
Higgsfield's 21 Sep 2026 blog: Starter $15, Plus $49, Ultra $129; Nano Banana 2 is 2 credits (about $0.10) at 1K/2K; unlimited windows exclude MCP, CLI, API and automation. Its GPT Image 2.5 post: 1.5 credits (1K low), 5.5 (2K high), up to 16 references. Krea/Creatify instead list $19/270 credits, $59/1,200, $129/3,000. Soul ID trains on 20+ photos. Kling 3.0: about 10 credits per 5 s.
- source: https://higgsfield.ai/blog/unlimited-nano-banana-2-plans
- source: https://higgsfield.ai/blog/gpt-image-2-5-higgsfield
- source: https://creatify.ai/blog/what-is-higgsfield-mcp-what-it-does-what-it-costs-and-how-to-use-it
- source: https://www.krea.ai/blog/higgsfield-pricing-explained-2026-unlimited-credits-and-real-monthly-costs
- source: https://higgsfield.ai/blog/tools-for-consistent-ai-characters

### F5 [medium] Higgsfield's one-click Explainer app and explainer skill are the wrong tool for a recurring original character and cost far more than stills.
It builds fixed 10-second blocks, one Gemini Omni video clip plus one Seed Audio take each, up to 10 minutes, with presets including Whiteboard Doodle, 2D Illustrator and 3D Papercraft. Higgsfield's blog prices a 20-second video at about 72 credits; linear extrapolation gives roughly 2,160 credits for 10 minutes (my arithmetic). AlphaSignal's review says it is not suited to character-driven content needing a consistent recurring cast.
- source: https://higgsfield.ai/blog/ai-video-from-text-and-url
- source: https://www.typingmind.com/skills/higgsfield-ai-higgsfield-video-explainer
- source: https://alphasignal.ai/news/higgsfield-ai-ships-explainer-to-turn-any-topic-into-a-10-minute-documentary
- source: https://higgsfield.ai/explainer-intro

### F6 [medium] OpenArt is the larger, cheaper credit pool, but its Character feature is not reachable through the Claude connector and per-model credit costs are not on the public pricing page.
openart.ai/pricing: Starter $14 (4,000 credits), Plus $34 (12,000), Pro $56 (24,000), Wonder $240 (106,000), currently shown discounted to $13/$27/$44/$175. openart.ai/mcp: exposes Nano Banana 2, Nano Banana Pro, GPT Image 2, Seedream 4.5, Seedream 5 Lite; external image references work; Character and Smart Shot are listed as roadmap items. A January 2026 third-party post put Nano Banana Pro at 60 credits; credits reportedly do not roll over.
- source: https://openart.ai/pricing
- source: https://openart.ai/mcp/
- source: https://blog.wentuo.ai/en/openart-nano-banana-pro-cost-reduction-api-en.html
- source: https://sloptv.co/guides/openart-pricing

### F7 [medium] Working practice in this niche is narrated stills with cuts and simple camera moves, not image-to-video; I2V on flat 2D art is the weakest and most expensive motion option.
X tutorial captions: about 50 images dropped into CapCut, no zoom or keyframes shown. Other niche guides: subtle zooms added in CapCut; 12-30 images per minute; one illustration per 12-15 words with hard cuts every 2-6 s. Curious Refuge's Kling 3.0 review scored 2D temporal consistency 3.0-6.0 versus 8.0 overall. Kling 3.0 on Higgsfield costs about 10 credits per 5-second 720p clip before rerolls. I did not watch Ink Explainer footage.
- source: https://video.twimg.com/subtitles/amplify_video/2106585145222303744/0/Ee8nMjq7GuozubnB.vtt
- source: https://www.adawatai.dev/blog/article/ancient-human-youtube-channel-prompt.html
- source: https://www.vidau.ai/stick-figure-animation-ai-with-claude-higgsfield/
- source: https://github.com/imishbahu-commits/doodle-explainer-video
- source: https://curiousrefuge.com/blog/kling-3-ai-video-generator-review

### F8 [high] The current ElevenLabs flagship is Eleven v4 (released 28 Sep 2026); narration for four 10-minute episodes fits the $22 Creator plan, which also unlocks a Professional Voice Clone of the user's own voice.
ElevenLabs docs: v4 is the flagship, 10,000 characters per request; v3 5,000; Multilingual v2 is described as the most stable for long-form. API list price $0.08 per 1,000 characters for v4 and v3 (v4 promo $0.022 until 12 Oct). Creator: 121,000 credits, PVC included; PVC wants 30+ minutes of clean audio. Ink Explainer's 11:12 All Day transcript is 2,516 words, about 15,000 characters, about 225 words per minute.
- source: https://elevenlabs.io/docs/overview/models
- source: https://elevenlabs.io/pricing/api
- source: https://elevenlabs.io/pricing
- source: https://techcrunch.com/2026/09/28/elevenlabs-new-v4-speech-model-supports-more-expression-control-and-90-languages/
- source: https://prepublish.ai/youtube-transcript/49_Ph2q6uIM

### F9 [medium] Evidence that audiences prefer human over AI narration is weak and generic; the firmer risks are policy and sameness, which favour the user's own voice (recorded or cloned) over a stock library voice.
Surveys: Animoto (about 460 US consumers) 78% trust real-person video more; Audacy (1,120 adults) 55% vs 23% trust human vs AI voice; TechSmith found voice quality mattered more than AI-versus-human for learning. None measures YouTube watch behaviour. YouTube's policy bans no AI voice but names "Image slideshows, templated storylines, or scrolling text with minimal or no narrative" and templated AI content. The tutorial uses stock voice Roger.
- source: https://support.google.com/youtube/answer/1311392?hl=en
- source: https://craftomorrow.com/ai-voice-vs-your-own-voice/
- source: https://www.techsmith.com/blog/ai-voices-avatars-in-training-videos/
- source: https://video.twimg.com/subtitles/amplify_video/2106585145222303744/0/Ee8nMjq7GuozubnB.vtt

### F10 [medium] A coding agent can realistically automate the rough cut from a scene manifest; TurboScribe and hand-placing images in CapCut are the tutorial's avoidable bottlenecks.
Remotion documents Claude Code support with installable agent skills and is free for individuals and companies of up to three people. ElevenLabs' with-timestamps endpoint returns audio plus character-level timings, so TTS needs no transcription step; WhisperX or Scribe v2 ($0.22/hour) covers self-recorded audio. Public repos already do manifest-to-ffmpeg doodle explainers and Whisper-to-FCPXML timelines importable into free DaVinci Resolve. TurboScribe costs $10-20/month; CapCut Pro $19.99.
- source: https://www.remotion.dev/docs/ai/coding-agents
- source: https://www.remotion.dev/docs/license/faq
- source: https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps
- source: https://github.com/imishbahu-commits/doodle-explainer-video
- source: https://github.com/Bouliw/fcpxml-roughcut
- source: https://github.com/emircbngl/davinci-resolve-mcp-free

### F11 [low] Planning estimate per 10-minute episode: 90-140 unique stills (120-180 generations with rerolls) and roughly 18-28 working hours once the system exists; four episodes a month cost about $60-110 on the recommended stack or $10-35 on the cheap one, excluding the Claude subscription.
My arithmetic, not measured: 2,000-2,250 words, a new visual every 4-6 s. Recommended: one image subscription sized for about 600 generations a month (Higgsfield Plus $49-59 at roughly 2 credits each, or OpenArt Plus $27-34 if per-image credits allow) + ElevenLabs Creator $22 + $10-30 music or hero clips; Remotion, WhisperX, Resolve free. Cheap: own recorded voice plus Gemini or OpenAI API stills at $0.01-0.05 each ($10-30). Labour dominates.
- source: https://ai.google.dev/gemini-api/docs/pricing
- source: https://higgsfield.ai/blog/unlimited-nano-banana-2-plans
- source: https://openart.ai/pricing
- source: https://elevenlabs.io/pricing

### F12 [low] Astra's paper-puppet raccoon in textured miniature scenery is materially harder to keep consistent than a flat doodle human if every frame is generated whole; it becomes practical only as a reusable cut-out asset library, and neither look is distinctive by itself.
Inference, no benchmark found: a textured non-human puppet adds identity features (ears, mask, tail, satchel, paper grain) plus scene lighting and depth that can drift, and human-history scenes still need a second, human cast. A flat doodle human has few features but is the look of Ink Explainer and its clones. Papercraft and Whiteboard Doodle are both stock Higgsfield Explainer presets, so style alone will not differentiate the channel.
- source: https://higgsfield.ai/blog/ai-video-from-text-and-url
- source: https://curiousrefuge.com/blog/kling-3-ai-video-generator-review

## Implications
1. Tutorial stack verdict: keep Claude (research, script, scene manifest, orchestration) and ElevenLabs; keep Higgsfield or OpenArt only as the image backend already paid for; drop TurboScribe; demote CapCut to optional final polish. Add what the tutorial lacks: a sourced claim sheet, 90+ visuals per episode instead of about 50, music and SFX, and a human timing pass.
2. Assembly: have Claude Code build one reusable Remotion (or ffmpeg) project that reads a scene manifest plus character-level TTS timestamps and renders the rough cut with cuts, push-ins, pans and pop-in overlays; finish in free DaVinci Resolve. This removes the most repetitive hours and makes re-timing after script edits nearly free.
3. Image model: do not default to Nano Banana Pro. Before committing, run a 20-image consistency bake-off of GPT Image 2.5 Flare versus Nano Banana 2 (optionally Seedream 5 Pro) with the same character sheet and style-key image attached to every call, and pick on usable-image rate per dollar. Use the GPT Image family for thumbnails and any in-image text.
4. Budget the connectors correctly: generations through the Claude connector always spend credits (about 600 a month is roughly 1,200 Higgsfield credits). Check exact per-model costs with the connectors' free listing and cost tools first; if credits run short, bulk stills straight from the Gemini or OpenAI API via Claude Code are $0.01-0.10 each.
5. Motion: skip Higgsfield's one-click Explainer and skip image-to-video for the body of the episode. Use cuts every 4-6 seconds, programmatic camera moves and layered character or prop pop-ins; reserve I2V for zero to five hero shots per episode, and only after launch.
6. Voice: use the user's own voice, either recorded for the pilots or as a Professional Voice Clone on the $22 Creator plan; A/B Eleven v4, v3 and Multilingual v2 on one 90-second passage because v4 is one week old. Avoid stock library voices such as the tutorial's Roger: the upside is a unique, rights-clean voice and distance from the mass-produced pattern YouTube's policy targets.
7. Concept choice from a production standpoint: B (one reusable office set, simple geometric envelope character) is the cheapest to produce consistently; A and C as written (miniature cutaways, model city, paper-puppet textures) are the most expensive looks. If C wins editorially, restyle Mox as flat cut-paper shapes on plain backdrops and build a pose library (about 20-30 poses and expressions on clean backgrounds) that is composited, not regenerated, each episode.
8. Cadence: plan two to three episodes a month at first. Four a month at 18-28 hours each is roughly 72-112 hours of solo work; Ink Explainer's own median upload gap is about 10 days and its last eight uploads average about 12 minutes, so the reference channel itself does not sustain weekly output at that length.
9. Risk: the literal tutorial recipe (about 50 stills, stock voice, script derived from a competitor's transcript) is the closest match to what YouTube's inauthentic-content policy describes. Original research with linked sources, a distinct character, the user's own voice and denser, purposeful visuals are the practical mitigations.

## Checks of Astra 6 claims
- [confirmed] The tutorial narration says Claude Code but shows chat with custom connectors; a terminal workflow is not demonstrated. -- The public caption file describes adding Higgsfield as a custom connector inside Claude. I read captions only, not the screen recording.
- [confirmed] No exact image model or measured generation duration is established; the presenter estimates an image count and skips forward. -- Captions name only Higgsfield, no model. The presenter mentions roughly fifty images around 08:22 and gives no measured time.
- [confirmed] Tutorial steps: ElevenLabs narration, TurboScribe timestamps, Higgsfield illustrations via Claude with a placement table, manual CapCut assembly. -- Matches the captions. Extra detail: the voice is the stock ElevenLabs voice Roger, and the CapCut step shows image placement only, with no zooms or keyframes.
- [unverifiable] The $98,000/month headline is unverified and not established as Ink Explainer's income. -- The captions I parsed contain other figures ($18,000 from one video, about $15,000, $8,000 in a month, $9,000 in 90 days) but I did not find the $98,000 figure there; it may be on screen or in the post text. Nothing I saw ties any figure to Ink Explainer.
- [confirmed] Catalog runs roughly 4 to 15 minutes, averaging about 9:20, with a historical median gap around 10 days. -- From the orchestrator's snapshot the 16 older videos average 9:21; the channel RSS feed gives a median gap of 10 days across 14 gaps. Missing nuance: the last eight uploads average about 12:02 and recent gaps were 7 to 23 days, so the format is getting longer and slower.
- [partly] A provisional 6-9 minute target for the pilot. -- Fine for a first pilot, but the reference channel's biggest videos are 8-12 minutes (All Day 11:13, Rain 11:37) and its recent average is about 12 minutes. The user's 8-12 minute target fits the evidence better; workload should be estimated for that length.
- [partly] Narration, illustration and editing tools can follow the roles shown in the tutorial; choose specific tools after a small visual and voice test. -- Testing first is right. But two tutorial roles should be replaced outright (TurboScribe, hand assembly in CapCut), a stock voice should not be used, and the image-model choice should be re-tested because GPT Image 2.5 now leads the edit leaderboards.
- [confirmed] A scene manifest can organize generation, revisions and editing; lock narration before finalizing illustration timing. -- Both are sound, and the manifest can go further than Astra says: with TTS character timestamps it can drive an automated Remotion or ffmpeg rough cut.
- [partly] Concept C look: compact paper-puppet forms, textured miniature scenery and a recurring model city, with the stated tradeoff being editorial focus only. -- Astra omits production cost. This is the hardest of the three looks to keep consistent when frames are generated whole, and Papercraft is a stock Higgsfield Explainer preset, so the texture itself is not a differentiator. Feasible if simplified and built as a composited asset library. This is my inference, not a measured result.
- [confirmed] The channel's toolchain is unknown and the tutorial's tools should not be attributed to it as fact. -- The feed descriptions credit only animation by Ink Explainer and list sources; no tools are named. An agency site (ytwealthmedia.com) presents Ink Explainer as its case study with a full production pipeline, which, if true, means it may not be a solo operation; I could not verify that.

## Gaps
- I did not watch Ink Explainer footage (browser tools were off-limits), so its real cut rate, visuals per minute and whether any shots are animated clips are unmeasured; the visuals-per-minute figures come from tutorials and pipelines for the niche.
- The Higgsfield pricing page did not render; plan figures conflict between Higgsfield's own blog ($15, $49, $129) and third parties ($19 for 270 credits, $59 for 1,200, $129 for 3,000). The user's actual plan and balance were not checked because connector calls were excluded.
- OpenArt per-model credit costs are not on its public pricing page; the only figure found (Nano Banana Pro at 60 credits) is third-party and from January 2026. Whether OpenArt or the Higgsfield connector exposes GPT Image 2.5 specifically is unconfirmed.
- No benchmark exists that I could find for recurring 2D mascot consistency, or for papercraft versus flat doodle styles; the verdict on the raccoon look is reasoning, to be settled by a cheap 20-image test of each look.
- No YouTube-specific controlled data on AI versus human narration was found; the surveys are small or generic, several circulating statistics trace to vendor blogs, and Ink Explainer's narrator (AI or human) is unidentified.
- Hours per episode and images per episode are my estimates, not measurements; Remotion render time and WhisperX speed on the user's Windows 11 machine are untested.
- Eleven v4 is one week old: long-form stability, Professional Voice Clone behaviour on v4, whether subscription credits are one per character for v4, and whether the with-timestamps endpoint supports v4 or v3 were not confirmed.
- OpenAI's own GPT Image 2.5 announcement returned 403; per-image prices by quality tier for 2.5 were not obtained, and the GPT Image 2 per-image figures are from third-party calculators.
- Music and sound-effect licensing costs were not researched; the $10-30 allowance is a placeholder.