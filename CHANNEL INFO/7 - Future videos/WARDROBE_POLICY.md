# Visitor wardrobe — owner instruction, 9 October 2026

The owner authorizes episode-specific traditional/historical clothing and accessories. This is an authorized costume change, not a redesign of the Visitor. His face, skin tone, hair, age, proportions and season drawing style remain recognisable. Never change his ethnicity to match a location.

## Director decisions

Astra chooses one researched outfit for each relevant episode, specifying place, date, occupation/status, garment layers, colors, footwear and any headwear. Clothing must follow museum objects, period images or specialist research with a source locator. “Chinese,” “Japanese,” “Korean,” “Oriental” or “pirate” alone is not an adequate costume prompt. No royal, ceremonial, military or religious clothing unless that is the actual scene's justified role.

China, Japan and Korea each require a distinct researched everyday men's outfit appropriate to the final historical setting. Do not combine their garments or substitute a later dynasty's clothing. The pirate episode requires the already chosen pirate hat. Other episodes use period clothing where it improves immersion; normal orange hoodie and jeans remain appropriate where no specific traditional outfit is selected. Do not invent an Indigenous identity or ceremonial outfit for the Canadian trading episode.

One outfit is locked before the main visual batch. A change within a video must have an explicit scene reason, such as removing a coat indoors; record those scene IDs and continuity. Keep the Visitor recognisable through his unchanged face, hair, shape and acting; use the orange brand color as a small plausible accent only when appropriate, not as a historical claim.

Owner refinement, 9 October: clothing must be understated and fit naturally into the actual scenes. Match ordinary local materials, cut, weather, work and the channel's muted palette. Avoid bright decorative costumes, oversized accessories, conspicuous ornament and ceremonial dress for everyday tasks. The pirate hat is modest, without a theatrical plume or skull decoration. No forced orange accent where it clashes. Judge the outfit beside the local cast and architecture at final shot scale, not only as a standalone character drawing; reduce distracting costume details while preserving historical accuracy and recognisable identity.

## Implementation

Keep clothing separate from Higgsfield backgrounds. Preserve the original library. Prepare episode-private clothed pose derivatives, including every pose used in thumbnails and Shorts, with a full-body reference and a close-up reference showing the same outfit.

For simple accessories, local drawing/compositing is preferred when it produces clean season-matched art. Substantial clothing changes may need dedicated artwork; quote its exact request count/cost in the episode allowance before generation. Never redraw the face casually or accept identity drift. An image model must not generate a new Visitor inside a scene background.

Native support already exists: put private PNGs in episodes/<slug>/poses/<original-pose-name>.png and declare each original pose key with its reviewed sha256 in that folder's poses.json. Record source image hashes and the wardrobe-reference hash as provenance. lp.py find_pose(name, ep) checks and uses these private copies. Keep script pose names stable.

## Acceptance

- Source matches the exact period, locality and ordinary role; no generic national costume.
- Every used pose has the same garment construction, layers, palette and accessories.
- Clothing looks natural beside the local cast, fits the weather and task, and does not compete with the narrated subject.
- Face, hair, age, skin tone and body proportions remain the approved Visitor's.
- Sleeves, hems, hands and feet work in the pose; no old garment edges, extra fingers or transparent holes.
- Footwear meets the ground; headwear fits the head angle and stays inside all crops.
- Full-size source art, final composites and 160/320px thumbnails are inspected.
- Video, thumbnails and all three Shorts use the same accepted wardrobe.
- No paid main batch while the chosen outfit is still unresolved. Resolve routine clothing details within this brief; do not send the owner a new costume-choice round.

Development decisions and references belong in each package's wardrobe_spec.json. Planned clothing is not an inspected asset. Both final slate reviews include these requirements.
