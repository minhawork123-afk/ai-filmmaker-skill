# Model — Seedance 2.5 (video)

ByteDance's video model, used in this workflow on **OpenArt** in **omni_reference** mode. Everything marked **[Tested]** comes from real productions with this setup. Everything marked **[General best practice]** comes from public reports or general experience and has not been tested here. Pass these labels on to the user.

## Settings — use these every time [Tested]

| Setting | Value |
|---|---|
| Platform | OpenArt |
| Model | Seedance 2.5 |
| Mode | omni_reference |
| Aspect ratio | 9:16 (vertical) or 16:9 (cinematic) |
| Resolution | 1080p |
| Duration | the block length, 30 seconds max per block |
| Bitrate | Standard |
| Native audio | ON |

Setting names and options can differ on other platforms that host Seedance. Ask the user what their interface shows rather than assuming.

[General best practice] For a 2.39:1 "scope" look, generate 16:9 and letterbox in the edit; frame important action inside the central band. If the duration setting only takes whole seconds, make the block a whole number of seconds and let the final shot absorb any remainder.

## Limits and timing [Tested]

- 30 s maximum per block; target 12–20 s.
- Shots under 2 s rarely render cleanly. Standard beats are 3–4 s, travel and reveals 5–6 s, fast cuts 2 s.
- Timestamps restart at 0 inside each block, and shot durations must total the block length exactly.
- Early tokens carry more weight, so camera position and movement come first in every shot.
- The first and last 10–15 frames of a block often have motion artifacts, which get trimmed in the edit.

## Reference images [Tested]

- Prompts refer to uploaded images as `@Image1`, `@Image2`, … in upload order. **The prompt binds to slots, not to file names.**
- Never change the upload order across generations. If the order changes, the wrong reference gets the wrong role.
- Order rule: characters → products → locations → the final frame of the previous block (blocks 2+). Numbered without gaps and fixed for the project.
- Character sheets with a headless centre panel give the model exactly one face to lock onto. Two full faces get averaged into a blurred identity.
- Attaching the previous block's final frame from Block 2 onward is the main defence against face and location drift, within a continuous scene. At a scene change (new location or time jump), see `translation/video-prompts.md` [General best practice].

Public reports say Seedance 2.5 accepts up to about 30 reference images in one generation, plus video and audio references [General best practice: public spec, not tested here]. In this workflow, projects used up to 6 image slots.

## Generation order [Tested]

1. Generate Block 1. Review identity consistency, lighting match and motion quality.
2. Save the final frame of Block 1 as a still.
3. Generate Block 2 with that still attached in the last-frame slot.
4. Repeat for every block.

## What the model responds to [Tested]

- Camera bodies, lenses, frame rates and named grades in a byte-identical Style DNA.
- Explicit realism clauses ("actual footage shot on a real camera, NOT a digital render, NOT a 3D visualization").
- Physical action described as mechanics, with durations for held poses.
- Explicit negatives for common drift: slow motion, gimbal smoothness, beauty filters, film grain on phone looks, music.
- Specific, timed sounds in `Audio:` lines. Native audio follows them.
- A voice spec ("natural, warm, human… NOT synthetic or robotic") to avoid robotic voices.

## Known failure modes and fixes [Tested]

| Symptom | Fix |
|---|---|
| Face changes between blocks | Check the upload order; attach the last frame from block 2 onward |
| Looks like a 3D render | Add the realism clause |
| Character does two things at once | Separate the actions into separate shots; dialogue and action never overlap |
| "Drops it" renders as a throw | Describe the mechanism and name the wrong version |
| Plastic skin | Run the skin realism pass on the sheet before generating video |
| Block too long or too short | Count the shot durations; they must total the block exactly |
| Location differs between blocks | Attach the same plate in every block and reference it |
| Robotic voice | Add the voice spec |
| Glitchy very short shot | Merge it with the adjacent shot or extend it to 3 s |

For anything else, see `troubleshooting.md`.

## Public information, not tested here [General best practice]

- Public reports put Seedance 2.5's release around mid-2026, with single generations of up to about 30 s and a maximum output of 1080p. Claims of native 4K output did not ship, according to reviews.
- Availability varies by region and platform.
- Some platforms expose editing and extension features. This workflow hasn't tested them, so suggest a short test before relying on them.

## Never claim

- That Seedance will lip-sync to an uploaded song, accept a specific number of references on the user's platform, render readable small text, or keep identity without reference images. None of these is tested here.
- Any setting the user's interface doesn't show.
