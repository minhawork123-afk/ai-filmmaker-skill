# The 7-Stage Production Method [Tested]

The default way to take any AI film from idea to finished cut. It works the same for cinematic films, UGC/persona content and product commercials; the playbooks change the details, not the order.

```
STAGE 1  IDEA          5 brief questions → Production Bible v1
STAGE 2  SCRIPT        beats + script, physical actions in [brackets]
STAGE 3  REF PROMPTS   portrait → character sheet → skin pass → product refs → location plates
STAGE 4  IMAGES        generate in fixed order, approve, name files, lock the @Image map
STAGE 5  VIDEO PROMPTS director's judgment + block prompts with Style DNA, timestamps, @Image refs
STAGE 6  VIDEO         generate block by block, carry each last frame forward
STAGE 7  EDIT          trim, cut on action, sound, grade, export
```

At the end of every stage: output → quality gate → *"Next: Stage N — ___. Go ahead, or change anything?"*

The output formats below are for **you** to fill in. Show them to the user filled, never blank.

---

## Stage 1 — Idea

**Goal:** a brief clear enough that every later decision can be checked against it.

Ask the five questions (see SKILL.md) plus the playbook's extras that change decisions. Then read the brief back and open the Bible.

```
BRIEF
What happens:     (1–3 sentences, in camera terms)
Who:              (characters / persona / product)
Where & when:     (place, era, time of day, weather)
Tone:             (three words, kept as the Style DNA mood line)
End feeling:      (what the viewer feels at the last frame)
Format:           9:16 | 16:9 · total __ s · platform
Assumptions:      (everything you decided for the user)
```

Then print `PRODUCTION BIBLE · v1`, in the format given in SKILL.md.

**Checks**
- Total length fits whole blocks (12–20 s each, 30 s max) [Tested]. A 30 s piece is usually 2 × 15 s.
- Every character, product and location in the brief has a line in the Bible.

---

## Stage 2 — Script

**Goal:** a script where every line maps onto a piece of video.

Rules [Tested]:
- Write physical actions in [brackets] inline with dialogue, so each line maps directly onto a video segment.
- Never write interior states ("she feels afraid"). Write what a camera sees ("her jaw tightens, she doesn't blink").
- Keep each speaking segment under 8 seconds. That's one shot, not one block.
- No filler, no preamble. Every line earns its place.
- Structure comes from the playbook: persona content uses opener → specific detail → honest caveat → verdict; cinematic uses world and tension in the first 6 s → build through action → end on an image.

First give a beat sheet, then the script.

```
BEAT SHEET — [title] · [total] s · [N] blocks
#  | Time    | Beat        | What the viewer sees                | Line / key sound
1  | 0–4 s   | Hook        | ...                                 | ...
2  | 4–9 s   | ...         | ...                                 | ...
Block split: Block 1 = beats 1–3 (0–15 s) · Block 2 = beats 4–6 (15–30 s)
```

```
SCRIPT
[0–4 s] [Wide. She stands at the bus stop in the rain, hood down, not moving.]
JO (flat, to lens): "Three buses. Full. Every one."
[She looks up the road. Beat.]
[4–9 s] [Insert: her thumb clicks the umbrella release twice. It stays shut.]
...
```

**Checks**
- Splits between blocks fall on story beats, never mid-moment [Tested].
- No line is spoken while the speaker moves. If one is, split it into move → stop → speak.
- The ending is an image, not an explanation (unless the playbook calls for a verdict line).

Load `craft/story-structure.md` for structure by format and length, and `craft/directing-performance.md` for writing behaviour.

---

## Stage 3 — Reference image prompts

**Goal:** lock every identity and every space before any video [Tested]. This is the most important stage.

Order of prompts [Tested]:
1. **Portrait** (4:5), one per character. Get the face right here first.
2. **Character sheet** (16:9), using the approved portrait as a reference. Exactly one full face; the centre panel is headless.
3. **Skin realism pass**, only if the sheet looks airbrushed.
4. **Product reference** (16:9), one per hero product [pattern is General best practice].
5. **Location plate**, one per setting, no people.

Use the output formats in `translation/image-prompts.md`. Each prompt goes in its own code block, with a label line: `Nano Banana Pro · 4:5 · becomes portrait for @Image1 sheet`.

**Checks:** see the image-prompt section of the quality gate in `principles.md`.

---

## Stage 4 — Image generation

**Goal:** approved images in a fixed upload order.

Order of operations, never skipping a step [Tested]:
1. Generate the portrait (4:5). Review and fix the face.
2. Generate the three-panel character sheet (16:9) with the approved portrait attached. Review identity consistency.
3. Run the skin realism pass if needed.
4. Generate product references and location plates. Review lighting and key elements.
5. Save every approved image with a clear name.

```
GENERATION ORDER — Nano Banana Pro
1. portrait-jo.png       4:5   approve: specific face, real pores, no beauty filter
2. sheet-jo.png          16:9  attach portrait-jo.png · approve: one face, centre headless, wardrobe matches
3. sheet-jo-v2.png       16:9  skin pass on sheet-jo.png (only if skin reads smooth/waxy)
4. product-flask.png     16:9  approve: shape, label, colour exact
5. plate-busstop.png     16:9  approve: no people, light source visible, key objects in place

@IMAGE MAP — upload in this order for EVERY block, never reorder
@Image1 = sheet-jo-v2.png
@Image2 = product-flask.png
@Image3 = plate-busstop.png
@Image4 = last frame of previous block (blocks 2+ only)
```

**Checks**
- The @Image map follows characters → products → locations → last frame, with no gaps [Tested rule].
- Bible statuses are updated to `approved`, and the Bible is re-printed.

---

## Stage 5 — Video prompt engineering

**Goal:** generation-ready block prompts.

Procedure:
1. Split the script into blocks of 12–20 s (30 s max) at story beats [Tested].
2. For each block, write the **director's judgment** (3–6 lines): beat, shot list, lens and light logic, rhythm, sound.
3. Write the block in the format from `translation/video-prompts.md`, in this order: header → @Image declarations → persistent conditions → LEFT/RIGHT facts → timestamped shots (camera → subject → action → atmosphere → Audio) → Style DNA.
4. Run the quality gate, and the validator if code execution is available.

One block per code block, labelled `Seedance 2.5 · omni_reference · 9:16 · Block 1 of 2 · upload @Image1–3`.

---

## Stage 6 — Video generation

**Goal:** clean blocks with continuity between them.

Generation order [Tested]:
1. Generate Block 1. Review identity consistency, lighting match and motion quality.
2. Save the **final frame** of Block 1 as a still. It becomes the last-frame slot for Block 2.
3. Generate Block 2 with that frame attached.
4. Repeat for every block.

```
GENERATION PLAN — Seedance 2.5 · OpenArt · omni_reference
Settings: 9:16 · 1080p · duration = block length · bitrate Standard · native audio ON
Block 1 (15 s): upload @Image1–3 → generate → review → save lastframe-b1.png
Block 2 (15 s): upload @Image1–3 + lastframe-b1.png as @Image4 → generate → review
Review each block for: face matches sheet · light matches plate · actions in the right order · no slow motion · audio as written
```

If a generation fails or drifts [Tested]: check the @Image upload order is exactly right; add specificity at the problem point by naming the mechanism; check no shot is under 2 s and no block exceeds 30 s. For anything else, see `troubleshooting.md`.

---

## Stage 7 — Editing

**Goal:** turn the blocks into a film.

CapCut, for fast turnaround and persona content [Tested]:
- Import the blocks in order.
- Trim the head and tail of each block (the first and last 10–15 frames often have motion artifacts).
- Cut on action, at the peak of a movement, not after it settles.
- Lay music under the native audio and keep Seedance's native audio on top (persona content usually has no music).
- For persona content, sync dialogue cuts to natural breath breaks, not mid-sentence.

After Effects, for cinematic work [Tested]:
- Apply the colour grade as a single adjustment layer across all clips for consistency.
- Add a subtle lens vignette.
- Add a 35mm grain overlay at 10–15% opacity if Seedance's grain feels insufficient.
- Keep title cards minimal, in a clean serif or sans-serif; never default fonts.

Export [Tested]: 1080p minimum, 4K if the machine allows. For YouTube, H.264 at high bitrate. For Instagram and TikTok, 9:16 in H.265.

```
EDIT PLAN — [CapCut | After Effects]
Order:   B1 → B2
Trims:   B1 head 12 f / tail 15 f · B2 head 12 f / tail 10 f
Cuts:    B1→B2 on the bag lift (peak of motion) · inside B2 hold the last shot 1 s longer than feels comfortable
Sound:   native audio on top · music: none | [track feel] at −18 dB under dialogue · room tone bridges the cut
Grade:   one adjustment layer: [grade from Style DNA] · vignette subtle · grain 10–15% only if needed
Text:    none | end card [content] in [font], 2 s
Export:  9:16 · 1080p · H.265
```

Load `craft/editing-rhythm.md`, `craft/sound-design.md` and `craft/color-and-grade.md` for the craft behind these choices.
