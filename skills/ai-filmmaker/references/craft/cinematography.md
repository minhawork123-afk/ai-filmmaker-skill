# Craft — Cinematography

Lenses, camera bodies, movement, frame rate and depth: the choices that make an image read as photographed rather than generated. Unlabelled content is **[General best practice]**; workflow-proven rules are marked **[Tested]**.

## Why camera words work

Naming a real camera, lens and movement gives the model a concrete photographic target. "Shot on ARRI Alexa 35, 85mm prime" [Tested] carries more information than "cinematic, high quality".

```text
WEAK    Ultra realistic cinematic shot of a man in a bar.
STRONG  Shot on ARRI Alexa 35, 40mm anamorphic, handheld at shoulder height, shallow depth of field.
WHY     A real camera, lens and move replaces "realistic" with something to reproduce.
```

## Lenses (full-frame / Super 35 equivalents)

| Focal length | What it does | Use for |
|---|---|---|
| 14–18mm | exaggerated depth, distortion near the edges | claustrophobia, POV, cramped interiors, skate/action |
| 24mm | wide but natural; environment dominant | establishing, walking with a character |
| 32–35mm | human-eye width with context | persona selfie feel [Tested: 35mm prime], documentary, handheld drama |
| 40–50mm | neutral perspective | dialogue mediums, honest framing |
| 85mm | flattering compression, soft background | portraits and reference sheets [Tested: 85mm prime], close-ups |
| 100mm macro | texture at the micro scale | product details, skin texture, liquids |
| 135–200mm | heavy compression, stacked background | surveillance, heat-haze roads, isolation in crowds |

- **Anamorphic** [Tested as a Style DNA token]: oval bokeh, horizontal flares, a slight edge falloff. Reads as feature film. Pair it with 16:9.
- **Spherical primes** [Tested as a Style DNA token]: cleaner and more neutral. Good for product, documentary and polished commercial work.
- **Vintage glass** (softer contrast, glow on highlights): nostalgia, dreamlike memory.

## Camera bodies as look tokens

| Body | Read | Status |
|---|---|---|
| ARRI Alexa 35 | high-end cinema: natural skin, rich highlight roll-off | [Tested] for sheets, plates, cinematic Style DNA |
| Sony A7S III | polished creator / indie | [Tested] in the persona Style DNA |
| Recent smartphone | HDR, over-sharpening, noise, rolling shutter | [Tested] for raw UGC |
| Sony Venice 2, RED V-Raptor | high-end commercial and feature | General best practice |
| 16mm film (Arri SR3 / Bolex) | visible grain, gate weave, softer detail | General best practice |
| Super 8 | heavy grain, light leaks, home-movie memory | General best practice |
| VHS / MiniDV camcorder | interlaced softness, chroma noise, date stamps | General best practice. Good for found-footage horror |

Pick **one** body per project, and put it in the Style DNA so it repeats byte-identically.

## Camera movement

| Move | Feeling | Prompt mechanics |
|---|---|---|
| Locked-off / static | control, observation, deadpan | "locked-off on a tripod, no movement" |
| Handheld, subtle micro-shake [Tested] | immediacy, unease | "handheld with subtle micro-shake" |
| Handheld, human tremor (UGC) [Tested] | self-filmed authenticity | "natural hand tremor, small organic drifts, slightly crooked horizon" |
| Slow dolly push-in [Tested as a camera-style option] | realisation, intent, dread | "slow dolly push-in from MS to CU over the full 5 seconds" |
| Dolly pull-out | isolation, reveal of context | "dolly pulls back to reveal…" |
| Tracking / lateral | travel, momentum | "tracks alongside at walking pace, camera LEFT of subject" |
| Crane / jib up | scale, ending, release | "cranes up from ground level to an overhead wide" |
| Orbit / arc | spotlight, product hero | "slow 90-degree arc around the product, LEFT to RIGHT" |
| Whip pan | energy, a transition | "fast whip pan RIGHT, motion blur" |
| Rack focus | shifting attention | "focus racks from the glass in the foreground to @Image1 in the background" |
| Snap zoom | comedy, documentary urgency | "quick snap zoom into her eyes" |
| Gimbal / Steadicam float | dreamlike glide, luxury | Never use for UGC [Tested: no gimbal smoothness in UGC] |

Give every move a **speed**, a **start → end framing** and a **duration**. One move per shot is usually enough.

```text
WEAK    Dynamic camera movement around her.
STRONG  Slow 90-degree arc from her LEFT profile to full front, MS, over 5 seconds.
WHY     Direction, path, size and time are all specified; "dynamic" is not.
```

## Frame rate and shutter

- **24fps, 180-degree shutter** [Tested]: film motion cadence and natural motion blur. The cinematic default.
- **30fps** [Tested]: persona/creator content, and video-native feel.
- **Slow motion** (60–120fps conformed): write it explicitly only when intended. For UGC, write "never slow motion" [Tested], because models sometimes add it.

## Depth of field

- **Shallow**: isolates the subject, soft background. Portraits, emotion, product hero.
- **Deep focus** [Tested for plates]: everything sharp. Establishing shots, geography, location plates.
- State it per shot when it changes ("shallow depth of field on inserts, deep focus on wides" [Tested in the clean industrial Style DNA]).

## Framing principles

- Use thirds for natural framing, and centred symmetry for formality, menace or ritual.
- Headroom shrinks as shots tighten. In CUs, cutting the top of the head is fine; cutting the chin isn't.
- Leave lead room in the direction a subject looks or moves.
- Use foreground layers (a doorframe, a shoulder, a glass) to add depth and voyeurism.

## Cinematography checks

- [ ] One camera body and lens family for the whole project, in the Style DNA.
- [ ] Every shot names its lens or framing, plus a movement with direction and duration.
- [ ] Frame rate and shutter are in the Style DNA.
- [ ] Depth of field is stated where it matters.
- [ ] The movement style matches the playbook (smooth for product, human tremor for UGC).
