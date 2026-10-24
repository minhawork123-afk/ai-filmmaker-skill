# Playbook — Cinematic

For narrative and atmospheric work: short films, scenes, trailers and teasers, horror, thriller, drama, sci-fi, music videos, mood pieces. Usually 16:9 (vertical cinematic is fine for social), 15 s – 3 min.

**The one truth:** cinema is decisions about what the viewer sees, when, and for how long. Every shot needs a job, and the story moves through action and image, not explanation.

## Brief extras (ask only what changes decisions)

- **Title, total length, genre or film type, and how it ends.**
- **Reference films or shows** (optional). Translate them into mechanisms; never paste titles or directors' names into prompts.
- **The look**: setting and era, locations, time of day, weather, colour palette, camera style (handheld and raw / locked-off and still / slow dolly / sweeping), and anything the user does NOT want to see.
- **Characters** (1–3 work best [Tested]): name, age, gender, role, face and hair, build, wardrobe, condition (clean / wet / wounded / dirty, and exactly where), distinguishing feature.
- **Sound**: dialogue yes / no / minimal; music mood or none; key sound moments.
- **Shots**: the user can list them or write "you decide". If they decide, you break the story into shots.

## Structure [Tested]

1. Establish the world and the tension in the first 6 seconds.
2. Build through action, not dialogue.
3. End on an image, not an explanation.

```text
WEAK    He explains to her that the bridge is out and they're trapped.
STRONG  Headlights find the bridge: a gap, black water. He kills the engine. Neither moves.
WHY     The image delivers the information and the dread at once.
```

See `craft/story-structure.md` for beat maps by length.

## Look defaults

- Start from a cinematic Style DNA in `style-dna-library.md`. The baseline [Tested] is ARRI Alexa 35, anamorphic or spherical primes, photoreal live-action cinematography with no stylisation, a named key light, a named palette, 24fps with a 180-degree shutter, fine 35mm grain, and a stated depth of field.
- Camera style follows the tone (`craft/cinematography.md`):
  - Handheld with subtle micro-shake [Tested] for dread, immediacy, survival.
  - Locked-off and still for control, menace, deadpan.
  - Slow dolly push for revelation and intent.
- Use weather and atmosphere as a layer of the Style DNA: rain, mist, dust, water beading on the lens [Tested].

## Performance

Physical actions only, sustained poses with durations, involuntary motion with a mechanism, and the wrong version named inline [Tested]. See `craft/directing-performance.md`. With minimal dialogue, the face and body carry the story, so give them specific behaviour every shot.

## References and blocks

- @Image plan [Tested]: one sheet per character, one plate per location, plus the last frame from the previous block.
- Character conditions (wounds, mud, wet clothes) are stated as LEFT/RIGHT hard facts in every block [Tested]: "the wound is on the LEFT arm".
- 12–20 s blocks [Tested], split at story beats.
- Use the standard block format from `translation/video-prompts.md`.

## Edit [Tested]

After Effects: one adjustment layer for the grade across all clips, a subtle vignette, a 35mm grain overlay at 10–15% if needed, and minimal title cards in a clean serif or sans-serif.

---

## Adapting to cinematic sub-formats [General best practice]

Use the same pipeline and change these levers.

### Horror / thriller teaser (15–30 s)
- **Withhold.** Show the reaction before the threat, or the threat only in negative space (a doorway, a figure out of focus).
- **Use one light source.** A phone screen, torch or single practical, with darkness filling the rest of the frame.
- **Sound leads.** Room tone → a specific wrong sound → silence → the sting. Silence is a beat; give it seconds in the timestamps.
- **Hold longer than comfortable**, then cut hard. End on the reveal, or on the moment just before it.
- Describe the threat by what the camera sees ("a shape stands at the end of the hall, unmoving, backlit, no visible face"), never "scary" or "creepy".

### Music video moment
- **The edit is cut to the track.** Ask for the BPM, or the timestamps of downbeats and drops. Shot durations follow bars: at 120 BPM one bar is 2 s, so 2/4/2/4 s patterns land on the beat.
- **Performance vs narrative.** Lip-syncing to an existing song depends on what the platform supports; this workflow has not tested it. The safe default is non-lip-sync performance (moving, looking, playing an instrument with the hands in frame) and syncing in the edit. If the user's platform accepts an audio reference, suggest a short test first.
- Generate with native audio turned off or ignored, since the song goes on in the edit. Keep `Audio:` lines minimal ("no dialogue, no music") to avoid a competing score.
- A bold single-light or coloured-practical look is common. Keep it physically motivated (a neon sign, stage lights, car headlights).

### Trailer / teaser (30–90 s)
- Structure: world → disturbance → escalation montage → title beat → stinger.
- Many short shots. Each timestamped segment still needs 2 s; group fast flashes into a labelled montage segment.
- Title cards are added in the edit, never generated.

### Drama scene with dialogue
- Coverage: an establishing shot, then singles for each speaker, then a reaction insert. Each speaking line gets its own shot, with the speaker still.
- Shot-reverse-shot needs consistent eyelines and screen direction. State "@Image1 looks camera-RIGHT toward @Image2" as a hard fact.

## Extra quality-gate checks for cinematic

- [ ] The first 6 s establish the world and the tension.
- [ ] Information is delivered by image or action wherever possible, not by dialogue.
- [ ] The final shot is an image with a duration that lets it land.
- [ ] Every character's condition, and every LEFT/RIGHT fact, is repeated in every block they appear in.
