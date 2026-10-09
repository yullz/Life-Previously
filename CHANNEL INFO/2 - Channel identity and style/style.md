# Style guide: look, character, motion, sound

The standard: a viewer should take it for a small studio's hand-made show. Everything below exists to remove the tells that make videos read as AI-generated.

## The look
Flat 2D cartoon illustration. Simple round-headed people with dot eyes and expressive eyebrows, clean dark-brown outlines (never black), flat colors with soft shading. A muted earthy period palette, so the Visitor's orange hoodie is the only saturated color in most frames. Simple shapes are deliberate: image models make their worst mistakes in detailed hands, faces and text, and a simple style leaves less room for them. The exact wording lives in `pipeline/config.json` (`images.style`, `images.suffix`).

| Role | Color |
|---|---|
| Visitor orange (hoodie, place chip) | #FF7A1A |
| Outlines and text stroke | #2B1D14 |
| Parchment (source labels) | #F2E6CF |
| Ochre | #C9A24B |
| Olive | #7A8450 |
| Brick | #A4473A |
| Slate | #4F6272 |
| Night blue | #1F2A3A |

## The Visitor: one pose library, never redrawn
A character that changes slightly from shot to shot is the most obvious AI tell. So the image model never draws the Visitor inside a scene. He comes from a fixed library of approved drawings, and the pipeline places one into each scene.

1. **Model sheet (once).** Generate candidates with the prompt below and pick one. Then have an illustrator redraw or clean it, under a written rights assignment. That removes AI artifacts and makes the character legally yours, because a prompt-only character cannot be copyrighted. Save it as `channel/assets/visitor_sheet.png`.
2. **Poses (once each).**
   - `channel/poses.json` names and describes every pose; the pilot uses 43.
   - `python pipeline/lp.py poses` lists the poses your scripts use that don't exist yet, with a ready prompt for each, in `channel/assets/visitor/to_make.md`.
   - Generate each pose from the model sheet on flat chroma-key green; `python pipeline/lp.py brief --poses` writes a helper page with every pose prompt (see `handoff/README.md`). The pipeline removes the green automatically (`lp.py poses`). Check every pose against the sheet; ideally the illustrator touches up each one.
   - Save each as a transparent PNG, `channel/assets/visitor/<name>.png`.
3. **Pose drawing rules:**
   - Three-quarter view facing the viewer's left. Mirror with `flip` when he stands on the left side of a frame.
   - Full body, unless the name starts with `closeup-`.
   - No shadow (the pipeline adds a soft contact shadow), on flat green (the pipeline cuts it out).
4. **Review the library** on one contact sheet with `python pipeline/lp.py sheet --poses`. Every pose must look like the same person.
5. **In scripts:** `[pose: name position size flip]`.
   - Position is `left`, `center` or `right`, or exact `x,y` (the point under his feet, as fractions of the frame).
   - Size is his height as a fraction of the frame height: about 0.6–0.75 standing, 0.95 for close-ups.
   - The scene's prompt then describes only the background, leaving room where he will stand.
6. **Growing the library:** each new episode adds a few poses. Reuse existing ones wherever you can.

Locals are drawn inside the backgrounds by the image model. Keep them medium or small, and simple.

## Backgrounds
- **Every generation:** use the full prompt from `lp.py prompts`, with `channel/assets/style_key.png` attached as the style reference.
- **Style key (once):** an approved background you love, saved as `channel/assets/style_key.png`.
- **Production model:** Nano Banana Pro at 2K, through the Claude connector (`/episode-images`), at 2 credits an image. The style key came from Nano Banana, its free sibling, so the look carries over. The website's unlimited models are only for manual work (`lp.py brief`).
- **Model bake-off (once, free on the website):**
  - Generate the same five pilot backgrounds (S004 wide city, S017 interior detail, S034 market street, S058 busy cookshop, S080 crowd action) with the style key attached.
  - **Candidates, in order:**
    1. **Seedream 4.5:** up to 4K, strong at following reference images, good at flat illustration.
    2. **Seedream 5.0 Lite:** follows editing instructions well; also good for fixing an image ("remove the man on the left").
    3. **GPT Image:** very literal prompt-following, but watch for its warm, over-polished house look.
    4. **Nano Banana:** excellent with references, but lower resolution.
  - **Weaker fits:** FLUX.2 Pro at 1K, which goes soft at full screen, and Kling O1, which leans photoreal.
  - **Pick** the model whose five images all look like the style key, with no text and no modern people. Write its name into `images.model`.
  - Never switch models mid-season.
- **Resolution:** pick 2K or higher where the model offers it. The pipeline zooms in slightly, and 1K images look soft at 1080p.
- **Finish:** the pipeline lays the same paper texture over every frame (`channel/assets/paper.png`, strength set in `finish.paper_strength`), so images from different generations read as one hand-made set.

## Prompts for one-time assets
- **Visitor sheet:** "Character model sheet. [images.style] [Visitor description from config]. Front view, three-quarter view, side view and back view, plus six facial expressions: neutral, confused, disgusted, delighted, panicked, smug. Plain parchment background, evenly spaced, no text."
- **Style key:** "[images.style] Scene: a muddy medieval London street at mid-morning, merchants at open shopfronts, a church spire behind, empty space on the right of the street. [images.suffix]"
- **Avatar (800×800):** use the `closeup-smile` or `count-fingers` pose on a solid parchment background with an orange circle behind him. Check it at 48×48 pixels.
- **Banner (2560×1440):** "Wide flat 2D cartoon panorama of five historical streets blending left to right: a Roman street, medieval London, Edo Japan, Victorian London, a 1920s city, parchment sky, no people in the centre, no text." Place a walking pose in the centre, then add the name and tagline inside the central 1546×423 safe area.
- **Thumbnail base:** "[images.style] Scene: [period scene with one problem object], the important object on the [text side], the other side calm for a character. [images.suffix]" Then: `python pipeline/lp.py thumb <slug> base.png "TEXT" "PLACE YEAR" --side right --pose <pose>`.

## Shot vocabulary
| Shot | Use |
|---|---|
| Establishing wide | Place and time of day, small figures. Opens each section. |
| Visitor reaction | A pose at size 0.6–0.75 in the setting, or a `closeup-` pose at 0.95 on a calm backdrop. |
| Action medium | A local doing one task. |
| Object insert | One object filling the frame: a loaf, a candle, a privy. |
| Map | A simple illustrated map with no labels; the narration names places. |
| Evidence card | A document or find on a desk, with a `[note: source]` label. |
| Comparison split | Left and right halves: then versus now, summer versus winter. |
| Street or crowd | Many locals, the Visitor small and orange. |

Rules: never two identical shot types in a row, at least one Visitor reaction per section, and one focal point per image.

## Motion
- **Camera moves:** slow and eased. They start and stop gently instead of drifting at a mechanical constant speed. The default strength is 8%, and moves rotate automatically.
- **Hold still on jokes:** `[still]` for punchlines and close-up reactions. A held frame lands a joke; a moving one smothers it.
- **Cut on the word:** images cut 0.08 seconds before the first word of their line, which the alignment makes exact.
- **Hard cuts only.** No wipes, spins, glitch transitions or zoom-punches: they read as template output.

## Sound
- **Narration:** one recognizable narrator voice (see [voice.md](voice.md)), levelled automatically.
- **Music:**
  - One calm instrumental bed per episode from a licensed library (Epidemic Sound or Artlist, or the free YouTube Audio Library).
  - The pipeline ducks it under the voice automatically; the level is `music.volume`.
  - No music stings under every joke.
- **Sound effects:**
  - 15 to 25 per episode, on scenes where a sound sells the moment: bells, crowds, splashes, a gate.
  - Script syntax: `[sfx: name volume +seconds]`. Files go in `channel/sfx/`; the list of names is in [sfx/README.md](sfx/README.md).
  - Sound design is the cheapest professional upgrade there is. Low-effort AI channels almost never have it.
- **Sound logo:** the same 2–3 second `sting` after every cold open. The current `sting` file is a medieval church bell, so it only fits medieval Christian settings; episode 002 (Pompeii) ran without it. An era-neutral channel sting is still to be made (an ElevenLabs sound effect; state the cost and ask the owner first).

## Signs of AI-made video, and how we avoid them
| Sign | Our fix |
|---|---|
| Character changes between shots | Fixed pose library, composited by the pipeline |
| Glossy, over-detailed "AI look" | Flat simple style, limited palette, one paper texture over every frame |
| Gibberish letters in images | The prompt suffix bans text; review rejects any; real text is added by the pipeline |
| Wrong hands, limbs or faces | Simple shapes, contact-sheet review, regenerate |
| The same composition over and over | Shot vocabulary rotation; no two identical shot types in a row |
| Slideshow feel | Eased moves, held frames for jokes, cuts exactly on words, varied scene lengths |
| Flat, generic AI voice | An auditioned voice few channels use, generated chapter by chapter, weak chapters redone, sparing direction tags |
| Wall-to-wall music, no effects | Ducked music bed plus 15 to 25 sound effects |
| Filler script, AI phrases | `lp.py check` flags banned phrases; every fact comes from claims.md; read-aloud edit |
| Factual errors | Claims checked against the sources before upload |
| Mass-produced rhythm | Two or three episodes a month, a different era each time |

## Image review (contact sheets from `lp.py sheet <slug>`)
First run `powershell -File pipeline/ocr_scan.ps1 episodes/<slug>/images`: Windows' own OCR lists any image with readable words. It catches printed lettering on signs, not cursive, so still look at every document and sign.

Regenerate or edit a background if any of these is true:
- It contains a modern-dressed person. The Visitor is added later, never generated.
- There is readable or gibberish text, a logo or a watermark. Edits can add text too, so re-check every fixed image.
- It doesn't match the narration line it sits under (read them together, not the prompt alone).
- A `[same-as]` scene doesn't look like the same place, or people vanish between shots of one moment.
- The picture doesn't fill the frame (white page, border or margin).
- An unrequested person stands where the pose will go.
- It has extra fingers or limbs, merged bodies or melted faces.
- It shows modern objects, or clothing and buildings from the wrong era.
- There is no empty space where the scene's pose will stand.
- The key action sits at the frame edge, where camera moves will crop it.
- The style has drifted: a 3D look, photorealism, black outlines, or blank white faces (Ink Explainer's look).

Then watch the full preview render: each pose's size and position should look natural in its scene. Adjust the `[pose: ...]` numbers and render again; only changed scenes re-render.
