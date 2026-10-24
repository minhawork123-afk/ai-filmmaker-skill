# Craft — Shot Design and Coverage

Choosing shots that tell the beat, and enough of them to give the edit options. Unlabelled content is **[General best practice]**; workflow-proven rules are marked **[Tested]**.

## Every shot has a job

Before writing a shot, name its job: **establish · reveal · react · detail/insert · move the story · pay off**. If a shot has no job, cut it.

## Shot sizes

| Size | Frame | Use it to |
|---|---|---|
| EWS / extreme wide | figure tiny in the environment | isolation, scale, geography |
| WS / wide | full body plus surroundings | establish space, blocking, entrances |
| MS / medium | waist up | behaviour, gesture, conversation |
| MCU / medium close-up | chest up | dialogue, the default for persona talking heads |
| CU / close-up | face fills the frame | reaction, decision, emotion through behaviour |
| ECU / extreme close-up | eyes, lips, a fingertip | tension, a key detail |
| Insert | an object or hands | product, clue, action mechanics |

## Angles and their effect

| Angle | Effect |
|---|---|
| Eye level | neutral, honest |
| Low angle (camera below eyes) | power, threat, monument |
| High angle (camera above) | vulnerability, surveillance |
| Overhead / top shot | pattern, fate, procedure (hands at work) |
| Dutch tilt | unease. Use it sparingly, once per film at most |
| POV | subjectivity. The viewer becomes the character |
| Over-the-shoulder (OTS) | relationship, conversation geography |
| Propped-phone low and wide | UGC authenticity [Tested] |

## Camera first [Tested]

In every shot description: camera position and movement first, then the subject, then the action, then the atmosphere. Early tokens carry more weight.

```text
WEAK    @Image1 sits on the bed reading a letter, shot in close-up with a slow push.
STRONG  Slow push-in, 50mm, close-up from bedside height. @Image1 sits on the bed, reading the letter.
WHY     The model locks framing and movement first, then fills the frame with action.
```

## Coverage patterns

**Classic scene coverage:** establishing WS → MS of the action → CU of the reaction → insert of the key object → a WS or CU payoff.

**Dialogue:** a master WS → singles for each speaker (MCU) → reaction CUs. Each spoken line in its own shot, with the speaker not moving [Tested rule: dialogue and action never overlap].

**Process / product:** overhead WS → hands insert → macro detail → result shot.

**UGC talking head** [Tested]: selfie MCU at arm's length → propped low-wide → hands-only inserts with voiceover → back to the face for the verdict.

## How many shots per block

- Standard beat: 3–4 s per shot. Travel, reveal or collapse: 5–6 s. Fast cut: 2 s. Under 2 s rarely renders cleanly [Tested].
- So a 15 s block holds about 3–5 shots, and a 20 s block about 4–6.
- Fast micro-cuts (under 2 s each) can sit inside one timestamped segment of at least 2 s as a labelled montage ("three quick cuts: …") [Tested exception].

## Geography and the 180-degree line

- Pick a side of the action and keep the camera on it within a scene. "@Image1 is on frame LEFT, @Image2 on frame RIGHT" as a hard fact in every block of the scene.
- Screen direction: if a character exits frame RIGHT, they enter the next shot from frame LEFT. Write it.
- Crossing the line deliberately (to disorient) is a choice; state it.

```text
WEAK    They argue across the table.
STRONG  @Image1 sits frame LEFT facing RIGHT; @Image2 sits frame RIGHT facing LEFT. Camera stays on the window side of the table.
WHY     Fixed geography stops the model flipping characters between shots.
```

## Composition for the format

- **16:9:** use negative space for tension, put the subject on a third, and use depth layers (foreground object, midground subject, background light).
- **9:16:** stack vertically. Faces sit in the top third, hands and product in the lower middle. Full-body shots read small, so favour MS/MCU and vertical movement (stairs, doorways, tilts).
- Keep the important action away from the frame edges, which platforms crop with UI overlays.

## Output format — shot list

```
SHOT LIST — Block [N] ([start]–[end] s)
#  | Time    | Size/angle      | Lens / move            | Subject + action                 | Job
1  | 0–4 s   | WS, eye level   | 24mm, static           | @Image1 enters frame LEFT         | establish
2  | 4–7 s   | MCU             | 50mm, slow push-in     | @Image1 stops, eyes to the door   | react
...
```

## Shot design checks

- [ ] Every shot has a named job.
- [ ] Shot sizes vary (wide, medium, close) unless sameness is the point.
- [ ] Camera is written first in every shot.
- [ ] Geography, screen direction and eyelines are stated as hard facts.
- [ ] Durations follow the 2 s minimum and total the block exactly.
