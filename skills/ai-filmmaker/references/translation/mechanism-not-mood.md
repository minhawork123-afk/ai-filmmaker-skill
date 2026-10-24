# Translation — Mechanism, Not Mood

How to turn any craft decision, or any vague word from a user, into words a generation model can act on. The principle is **[Tested]**. The vocabulary below is **[General best practice]** unless marked.

## The conversion procedure

For any adjective, mood or feeling:

1. **Ask what a camera would see and a microphone would hear** if it were true.
2. **Pick the channel**: lens, camera move, light source, colour, physical behaviour, environment, or sound.
3. **Make it specific**: position (LEFT/RIGHT, foreground/background), quantity, speed, and duration in seconds.
4. **Rule out the likely wrong version** if the model tends to get it wrong.

```text
WEAK    Make it feel lonely.
STRONG  Extreme wide, 24mm, locked-off: @Image1 small at frame RIGHT on an empty platform, one buzzing fluorescent tube, no other people.
WHY     Scale, emptiness and a single sound are what loneliness looks like on camera.
```

## Craft decision → prompt wording

| Craft decision | Write it as |
|---|---|
| Story beat | a shot list with timestamps; the beat name in the block header |
| Shot size and angle | "MCU, eye level" / "low angle WS from knee height" at the start of the shot |
| Lens | camera body + focal length + spherical/anamorphic + depth of field |
| Camera move | move + direction + start → end framing + duration ("slow dolly push-in from MS to CU over 5 s") |
| Light | source + position + colour + quality ("hard window daylight from camera-RIGHT, long shadow bars") |
| Colour | the palette sentence: shadows / midtones / highlights / texture |
| Performance | visible behaviour + duration + the wrong version named ("holds for the full 3 s, does not lower the arm") |
| Dialogue | speaker still → `says, [delivery as sound]: "line"`; voiceover labelled "Voiceover, no lip sync" |
| Sound | `Audio:` + named sounds + timing + mic character + music decision |
| Rhythm | shot durations that add up to the block |
| Continuity | @Image slots, "match @ImageN exactly", LEFT/RIGHT facts, wardrobe state, last-frame slot |
| Overall look | the Style DNA, pasted byte-identical |

## Look words → mechanisms

| Instead of | Write (pick what fits) |
|---|---|
| cinematic | "Shot on ARRI Alexa 35 with anamorphic primes, 24fps, 180-degree shutter, fine 35mm grain" [Tested tokens] |
| realistic / lifelike | "Photoreal live-action cinematography, no stylisation. This must read as actual footage shot on a real camera, NOT a digital render, NOT a 3D visualisation, NOT a video game environment" [Tested] |
| high quality / 8k / masterpiece | delete it; describe the camera, lens and light instead |
| epic | an extreme wide, a low angle, a crane up, a long lens compressing scale |
| beautiful (place) | name the light and what it falls on: "low sun through dust, long shadows across the wheat" |
| beautiful (person) | specific ordinary features plus real skin texture; never "flawless" [Tested: no beauty filter] |
| moody / atmospheric | a single practical source, deep shadows, haze or rain in the light, a named colour temperature |
| gritty | handheld micro-shake, desaturated palette, crushed blacks, heavy grain, wet surfaces |
| dreamy | soft vintage glass, halation, slow drift, shallow focus, lifted blacks |
| clean / premium | spherical primes, controlled slider moves, a hard key and soft fill, neutral whites, deep blacks |
| raw / authentic (UGC) | "filmed on a phone held at arm's length, natural hand tremor, slightly crooked horizon, flat and ungraded" [Tested] |

## Interior states → visible behaviour

| Instead of | Show |
|---|---|
| nervous / anxious | thumb works a seam, glances at the door twice, a shallow breath, wipes a palm on the thigh |
| scared / terrified | breath stops, eyes fixed and not blinking, backs up a half-step, a hand finds the wall behind |
| sad / heartbroken | stillness after an action, eyes drop and stay down, a slow exhale through the nose |
| angry | stops moving, jaw tightens, a flat quiet delivery, sets the object down too hard |
| happy / relieved | shoulders drop, a long exhale, a laugh that breaks halfway, eyes close for a beat |
| confident / determined | chin level, eyes locked on the lens without blinking, walks without checking the ground |
| exhausted | eyelids heavy, mouth slightly slack, hands on knees, head down, shoulders heaving [Tested pattern] |
| realises / remembers | stops mid-action, eyes unfocus past the lens, turns slowly toward the object |
| unimpressed (UGC) | flat delivery, a slight shrug, looks off-lens, no smile [Tested pattern] |

```text
WEAK    He is in shock.
STRONG  He stops mid-sentence. His mouth stays slightly open; he doesn't blink for three full seconds.
WHY     An interrupted action plus a timed hold is the image of shock.
```

## Atmosphere → physical elements

| Instead of | Write |
|---|---|
| tense | silence plus one repeating small sound; the camera locked off; a held shot that runs 2 s too long |
| eerie | wrong stillness: a swing moving with no wind, lights on in an empty house, a figure out of focus |
| cozy | warm tungsten practicals, steam from a mug, rain on the window, knitwear texture |
| chaotic | handheld whip pans, overlapping sounds, crowded foreground, fast 2 s cuts |
| oppressive | low ceiling in frame, top light, heavy rain, a long lens compressing the walls inward |

## Sound words → specific sounds

| Instead of | Write |
|---|---|
| ambient sound | the room's actual sources: fridge hum, distant traffic, a fan, wind in the pines |
| scary music | silence, then a low sub-bass swell from 6 s; a single wrong sound (a door downstairs) |
| upbeat | (decide in the edit) in generation: "No music"; specific action sounds |
| crowd noise | "indistinct chatter from a busy café, cups clinking, an espresso grinder at 3 s" |

## Quick self-test for any prompt line

- Could a camera operator set up this shot from this sentence alone?
- Could a sound recordist record it?
- Does it say where (position), how much, and for how long?

If the answer to any of these is no, convert it again.
