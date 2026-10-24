# Principles and Quality Gate

The non-negotiables behind every prompt, the full quality-gate checklist, and how to report fixes.

## Labels used across all references

- **[Tested]**: proven in the productions this workflow comes from (a UGC persona ad and a cinematic car film, both made with Nano Banana Pro + Seedance 2.5 on OpenArt).
- **[General best practice]**: established film craft or public information that this workflow has not tested.
- In `craft/` files, anything without a label is general film craft (**[General best practice]**). Model-specific claims are always labelled.
- When you advise the user, keep the label. Never upgrade [General best practice] to [Tested].

## Teaching snippet format

Patterns throughout the references are written like this:

```text
WEAK    She looks terrified.
STRONG  Her breath stops; her eyes slide to the door and hold there.
WHY     A camera can film breath and eyelines. It cannot film "terrified".
```

These patterns teach the move. Never paste them into a user's project; write fresh lines for every project.

---

## The five core principles [Tested]

### 1. Name the mechanism, never the mood

Not "make it cinematic": name the lens, the light source and the colour grade. Not "make it realistic": say it was shot on a real camera and is not a 3D render. Not "she looks scared": describe what a camera would actually see.

```text
WEAK    Cinematic, moody lighting.
STRONG  Single tungsten practical lamp camera-LEFT as the key, soft falloff into deep shadow, cold blue spill from a window behind.
WHY     The model can place a lamp and a window. It can't place "moody".
```

Mood words are allowed in exactly two places: the closing mood line of the Style DNA, and a location plate's `MOOD:` line, which is a coherence check for you rather than an instruction to the model. Anywhere else, convert them with `translation/mechanism-not-mood.md`.

### 2. Lock the character first, the location second

Generate character sheets, product references and location plates **before** any video. Every later prompt then says "match @Image1" instead of re-describing from scratch. A model inventing a location and its lighting while also delivering a performance will fail at both.

```text
WEAK    A woman with dark curly hair in a red coat walks through a rainy neon street...
STRONG  @Image1 walks through @Image3 toward camera. Match @Image1 exactly; match @Image3's wet asphalt and neon spill.
WHY     Re-describing invites a re-invention. A reference slot holds the identity steady.
```

### 3. Physical actions only, never interior states

A video model renders what a camera sees, so give it something to see.

```text
WEAK    He is nervous about the interview.
STRONG  He wipes his palm down his thigh, checks the door, wipes it again.
WHY     Behaviour is visible; nerves are not. Repetition reads as anxiety.
```

### 4. Style DNA is written once and pasted byte-identical

Never reword it between blocks. One project, one signature. Even a synonym swap ("grain" → "texture") is a different instruction and can shift the look.

### 5. Dialogue and physical action never overlap

On camera, a character speaks or moves, not both at once. Sequence it: move → settle → speak, or speak → stop → move.

```text
WEAK    She walks to the window while saying, "I never wanted this."
STRONG  She walks to the window and stops. Beat. She says, "I never wanted this."
WHY     Lip-sync and full-body motion compete; separating them keeps both clean.
```

Voiceover with no lip sync **may** run over action [Tested], but mark it explicitly in the shot: `Voiceover, no lip sync: "…"`.

---

## Quality gate checklist

Run this before every handoff. Fix silently, then report (see the end of this file).

### Direction
- [ ] A director's judgment (3–6 lines) was stated before the prompts, and the prompts carry it out.
- [ ] Every shot has a job: it establishes, reveals, reacts, shows a detail or pays off. Cut any shot that has none.
- [ ] The block ends on an image or a turn, not on an explanation.

### Image prompts (portraits, sheets, products, plates)
- [ ] The aspect ratio is stated (portrait 4:5, character sheet 16:9, plate matches the project unless the playbook says otherwise).
- [ ] Faces are described as specific, ordinary features, not as "beautiful".
- [ ] A character sheet shows exactly one full face (headless centre panel), and says explicitly that only the centre panel is headless.
- [ ] Location plates contain **no people**, and every key object has a frame position (foreground/mid/background, LEFT/centre/RIGHT).
- [ ] Lighting names the physical source. "Good lighting" and "cinematic lighting" never appear.
- [ ] A realism clause is present ("an actual photograph… NOT a digital render, NOT a 3D visualisation"), plus a camera body and lens.
- [ ] A NEGATIVE line covers the likely failures (airbrushed skin, CGI look, text, logos, people in plates).

### Video blocks
- [ ] The block header shows its number, time range and beat name.
- [ ] Every @Image slot used is declared at the top of the block, in Bible order. Blocks 2+ attach the previous block's last frame.
- [ ] Character sheets carry the instruction to take the face from the portrait panel; the centre panel omits the head deliberately.
- [ ] Persistent conditions are stated: dialogue/no dialogue, weather, time of day.
- [ ] LEFT/RIGHT facts are stated in capitals.
- [ ] Every shot reads in this order: camera (position, lens, movement) → subject (@ImageN) → physical action → atmosphere. Audio is an `Audio:` line per shot (standard format) or a global `AUDIO:` section with synced sounds written into the shots (UGC format).
- [ ] Timestamps start at 0, are contiguous, and total the block length exactly.
- [ ] The block is 30 s or less (12–20 s target), split at a story beat and never mid-moment.
- [ ] No timestamped segment is under 2 s. Fast micro-cuts inside a segment are labelled as a montage.
- [ ] Sustained poses have a duration; involuntary motion has a mechanism; likely mistakes are named inline ("does not throw it").
- [ ] No on-camera line overlaps movement, and voiceover is labelled "Voiceover, no lip sync".
- [ ] Audio lines name specific sounds with timing, never "ambient sound".
- [ ] The Style DNA is the last section, byte-identical to the Bible.
- [ ] No interior states and no mood words in shot lines.

### Output
- [ ] One prompt per code block, with no placeholders left and no commentary inside.
- [ ] A one-line label above each block: tool · aspect ratio · @Image slot.
- [ ] The Bible is re-printed if anything changed.
- [ ] Any model-behaviour claim made to the user carries its label.

---

## Mood and filler words to remove from shot lines

Replace these with a mechanism (see `translation/mechanism-not-mood.md`). The validator flags the same list.

- **Look words**: cinematic, epic, beautiful, stunning, gorgeous, breathtaking, amazing, moody, atmospheric, dramatic, aesthetic, vibe, high quality, masterpiece, award-winning, 8k, 4k, hyper-realistic, ultra-realistic, realistic, lifelike
- **Light words**: good lighting, nice lighting, cinematic lighting, dramatic lighting, perfect lighting
- **Interior states**: nervous, scared, afraid, terrified, sad, happy, angry, anxious, excited, confident, determined, in love, feels, feeling, thinks, realises, remembers, wants, decides
- **Sound words**: ambient sound, background noise, epic music, sound effects

"Photoreal" and "photorealistic" are fine; they're realism instructions, not moods. Words inside a NEGATIVE line ("no cinematic grade") are fine.

## Fix report

After the deliverable, list every change you made silently:

```
Quality gate — N fixes
- [where]: [what was wrong] → [what it is now]
```

- One line per fix, saying where it was (block and timestamp, or prompt name).
- If a fix changed a creative decision (for example, merging shots changed the rhythm), say so in the line.
- If something can't be fixed without the user (for example, a missing reference image), don't guess. List it under `Needs you:`.
- If nothing was wrong: `Quality gate — passed, no fixes.`

## When the user asks for something that breaks a principle

Do it if the user insists or has marked it `LOCKED`. Warn once, in one line, about the likely failure and how to avoid it, then move on. Never lecture.
