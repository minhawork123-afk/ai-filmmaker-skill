# Translation — Video Prompts (Block Prompts)

How to turn the script, the shot list and the director's judgment into generation-ready block prompts. The rules and formats here are **[Tested]** with Seedance 2.5 (omni_reference mode on OpenArt) unless marked. For other video models, keep the craft and check the model's own limits; never assume they match.

## Hard rules [Tested]

- Every block is 30 seconds or less. Target 12–20 seconds per block.
- Split blocks at story beats, never mid-moment.
- Timestamps restart at 0 inside each block.
- Shot durations: 3–4 s for most beats, 5–6 s for travel or reveals, 2 s for a fast cut. Under 2 s rarely renders.
- Shot durations must total the block length exactly.

**Montage exception** [Tested]: several fast cuts can live inside one timestamped segment of at least 2 s, if labelled: `0–3s: MONTAGE, three quick cuts: (a) … (b) … (c) …`.

**Timestamp format**: write `0–4s:`, `4–7s:`, `7–9.5s:`. Half seconds are fine. Use the same format in every block.

## Craft rules [Tested] — apply without being asked

- **Camera first** in every shot: position and movement, then subject, then action, then atmosphere. Early tokens carry more weight.
- **Physical actions only**, never interior states.
- **Sustained poses need a duration**: "holds the aim for the full three seconds and does not lower the arm".
- **Involuntary motion needs a mechanism**: "his hand goes limp, fingers uncurl, it slips from a slack grip".
- **Name the wrong version inline** when a mistake is likely: "— he does not open his hand, does not throw it".
- **LEFT/RIGHT are hard facts**, capitalised, in every block.
- **Style DNA is written once** and pasted byte-identical as the last section of every block.
- **Write cinematically, never clinically**: full sentences with texture, not keyword lists.
- **Refer to people and products by @Image number.** A name may appear only attached to its tag ("Mara @Image1"), never on its own.

```text
WEAK    Mara walks in, nervous, close-up, rain, cinematic.
STRONG  Handheld close-up, 50mm, tracking backward. Mara @Image1 walks in out of the rain, water running off her hood; her eyes check the room LEFT to RIGHT.
WHY     Camera → subject → action → atmosphere, in sentences, with a tag and a visible behaviour.
```

## @Image binding

- Declare every slot the block uses at the top, in Bible order, each with a one-line description and a "match" instruction.
- Keep the slot numbers fixed for the whole project. Upload the same images in the same order for every block, even if a block doesn't mention every slot [General best practice: keeps numbering stable].
- Character sheets always get the face-source line [Tested]: *"In each character sheet, take the face from the chest-up portrait panel (LEFT). The centre panel omits the head deliberately. [Characters] have a head and face in every shot."*
- Products: *"@Image2 — the [product]. Match exactly: [shape, colour, finish, label]."* [Tested]
- Locations: *"@Image3 — [space]. Match the [light source], palette and contrast exactly."* [Tested]
- Blocks 2+: *"@Image[N] — final frame of Block [N-1]. Continue from it exactly."* [Tested]
- **Scene change** (a new location or a time jump) [General best practice, untested]: the last frame no longer shows the right setting and can drag the old set into the new scene. Either leave it out, or attach it for identity only: *"@Image[N] — final frame of Block [N-1], for @Image1's face and wardrobe only; the setting is now @Image3."* Within a continuous scene, always attach it [Tested].

```text
WEAK    Use the reference images for the characters and the place.
STRONG  @Image1 — character sheet, ODE. Take the face from the LEFT portrait panel; the centre panel omits the head deliberately. Match exactly.
WHY     Slot, role, face source and instruction in one line; nothing left to interpret.
```

## Dialogue, voiceover and audio

- On camera: the speaker is still when speaking. `@Image1 stops at the counter. Beat. She says, flat: "Not tonight."` [Tested rule]
- Voiceover over action: `Voiceover, no lip sync: "…"` [Tested]
- Silence: write it with a duration and say not to fill it [Tested pattern].
- Audio: either one `Audio:` line per shot (standard format) or a global `AUDIO:` section plus synced sounds written into the shot text (UGC format). Both are tested. Never write "ambient sound".
- Voice spec whenever anyone speaks, identical in every block (see `craft/directing-performance.md`).

## Realism clause [Tested]

If the look drifts toward CGI, add to the block: *"This must read as actual footage shot on a real camera, NOT a digital render, NOT a 3D visualization, NOT a video game environment."*

---

## Output format A — standard block (cinematic, product, drama) [Tested]

The slot numbers below are an example. Use the Bible's @Image map: characters → products → locations → last frame, with no gaps.

Label line: `Seedance 2.5 · omni_reference · [9:16 | 16:9] · Block [N] of [T] · upload @Image1–[K] in order`

```
BLOCK [N] — [start]–[end] — [BEAT NAME]

@Image1 = [character 1 — one line: name, key physical detail, wardrobe]
@Image2 = [character 2 / product — one line]
@Image3 = [location — one line: space, time of day, key light]
@Image4 = [final frame of Block N-1 — blocks 2+ only]

In each character sheet, take the face from the LEFT chest-up portrait panel. The centre panel omits the head deliberately. [Name(s)] [has/have] a head and face in every shot of this film.

Continuous scene. [No dialogue / Voiceover only / Dialogue on camera]. [Weather]. [Time of day].
[LEFT/RIGHT facts: "The wound is on the LEFT arm. The torch is in the RIGHT hand."]
[Blocks 2+: "This clip picks up seconds after the previous one. Continue from @Image4 exactly."]

0–[X]s: [Camera position, lens, movement]. [@ImageN subject] [exact physical action]. [Atmosphere detail].
Audio: [specific sounds with timing]

[X]–[Y]s: Cut. [Camera]. [@ImageN subject]. [Action]. [Atmosphere].
Audio: [specific sounds]

[... until the durations total the block length]

[Not the final block: "END ON THIS FRAME — [pose, frame position, wardrobe state, light]."]

NEGATIVE: [likely failures for this block: identity drift, CGI look, slow motion, text, extra people, the wrong version of key actions]

Style DNA:
[paste byte-identical from the Bible]
```

## Output format B — UGC / persona block [Tested pattern]

The same rules, with performance and capture direction up front. Label line as above.

```
BLOCK [N] — [start]–[end] — [BEAT NAME]

@Image1 — character sheet, [NAME]. Take the face from the LEFT chest-up portrait panel. The centre panel omits the head deliberately. [Name] has a head and face in every shot. [Name] matches the sheet 100% — exact face, exact skin texture, exact hair, exact build, exact wardrobe. One specific real person, not a composite. Do not beautify, smooth, or drift toward a generic face.
@Image2 — the [product]. Match exactly: [shape, colour, label].
@Image3 — [location]. Match the [light] exactly.
[@Image4 — final frame of Block N-1 — blocks 2+ only]

[Blocks 2+: CONTINUITY — CRITICAL. This clip picks up seconds after the previous one. Wardrobe now: [state]; [item] is already off and must not appear. Over this clip [Name] progresses from [start state] to [end state].]

CAMERA: every frame filmed on a phone, held at arm's length by [Name] or propped on a surface. Genuine handheld feel — real hand tremor, small organic drifts, slightly crooked horizons. Never a tripod, never a gimbal, never slow motion.
PACING: dialogue and physical action never overlap. [Name] speaks, or moves — never both. Leave real silence between lines.
PERFORMANCE: [energy as behaviour — e.g. low energy, underselling, talking to the phone like to a friend, no smiling at the lens].

0–[X]s · [BEAT]. [Camera setup]. [Name] @Image1 [action]. [She/He] says, [delivery]: "[line]". [Pause or beat.]
[X]–[Y]s · [BEAT]. Cut. [Camera]. [Hands-only insert / action]. Voiceover, no lip sync: "[line]". [Sounds of the action.]
[...]
[Not the final block: END ON THIS FRAME — [pose, frame position, wardrobe state, light].]

VOICE: [voice spec — identical in every block].
AUDIO: [room tone, action sounds, mic character]. No music.
NEGATIVE: [identity drift, airbrushed skin, tripod or gimbal smoothness, slow motion, film grain or cinematic grade if phone look, music, on-screen text, robotic voice, dialogue overlapping action, enthusiasm, other people, real brand logos, watermark].

Style DNA:
[paste byte-identical from the Bible]
```

---

## Text-only mode — no reference images [General best practice, untested]

Use this when the user can't or won't make reference images. Warn once that identity and location will drift more than with references.
- Write a **CHARACTER LOCK** line per person (age, face specifics, hair, build, wardrobe, one distinguishing mark with its side) and a **LOCATION LOCK** line per setting. Keep them in the Bible and paste them byte-identical into every block, exactly like the Style DNA.
- Drop the @Image declarations and the face-source line. Refer to people by a short fixed label ("the woman in the yellow raincoat") used identically everywhere.
- Fewer cuts per block and simpler actions help a model with no reference hold identity.

## Other video models [General best practice]

The craft, the shot logic and the quality gate transfer to any model. The `@ImageN` syntax, omni_reference mode, the 30 s ceiling and the 2 s minimum are tested on Seedance 2.5 only. Ask the user how their tool references images and how long one generation can be, keep the same block structure, and adapt only the syntax and limits.

## From script to blocks: procedure

1. Mark the beats in the script, and group them into blocks of 12–20 s at beat boundaries.
2. For each block, write the director's judgment (beat, shots, lens/light logic, rhythm, sound).
3. Assign durations so they total the block exactly. Vary them for rhythm (`craft/editing-rhythm.md`).
4. Write each shot camera-first, using the visible behaviour from the script's [brackets].
5. Move dialogue so it never overlaps movement. Convert lines over action to labelled voiceover, or split the shot.
6. Add LEFT/RIGHT facts, continuity lines and the END ON THIS FRAME line.
7. Add NEGATIVE, then paste the Style DNA last.
8. Run the quality gate, and `scripts/validate_blocks.py` if you can run code.

## Video-prompt checks

- [ ] Header with number, time range and beat.
- [ ] All slots declared in Bible order, with the face-source line and match instructions.
- [ ] Durations: starting at 0, contiguous, totalling the block length, ≥2 s per segment, block ≤30 s.
- [ ] Camera first in every shot, physical actions only, and holds with durations.
- [ ] No on-camera dialogue during movement, and voiceover labelled.
- [ ] Audio named and timed, and a voice spec where anyone speaks.
- [ ] END ON THIS FRAME in every block but the last.
- [ ] Style DNA last and byte-identical.
