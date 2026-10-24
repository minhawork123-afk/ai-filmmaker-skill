# Craft — Sound Design

Sound sells reality more than image does. Generated native audio follows what you write, so write it like a sound designer. Unlabelled content is **[General best practice]**; workflow-proven rules are marked **[Tested]**.

## The rule [Tested]

Name specific sounds with their timing. Not "ambient sound", but *"rain on leaf litter, a low roll of thunder at 4 s, boots dragging through wet mud"*.

```text
WEAK    Audio: ambient office sounds.
STRONG  Audio: HVAC hum, a printer starting at 2 s, keys clattering two desks away, her chair creak at 5 s.
WHY     Named, located, timed sounds build a space; "ambient" builds nothing.
```

## Four layers of a soundtrack

1. **Room tone / ambience**: the space itself (fridge hum, distant traffic, fan, wind in pines). Always present; it glues the cuts.
2. **Hard effects / foley**: sounds of the action, synced (a scoop against plastic, a shaker lid, a bag zip, a barbell clang) [Tested examples of naming].
3. **Voice**: dialogue or voiceover, with a voice spec (see `directing-performance.md`).
4. **Music**: score or source music. Often added in the edit, not generated.

Write layers 1–3 in each shot's `Audio:` line. Decide layer 4 in the Bible and the edit plan.

## Native audio [Tested]

- Generate with native audio ON (Seedance 2.5) and keep it on top in the edit; lay music underneath.
- Every shot ends with an `Audio:` line.
- Microphone character is part of the realism. For phone content: *"slightly hot and a little clipped, like a phone mic in a reverberant room"* [Tested].

## Silence is a beat

- Write silence with a duration: *"no dialogue at all from 3 to 6 s — only breathing and equipment sound. That silence is deliberate; do not fill it."* [Tested pattern]
- Silence before a line or a reveal makes it land. A sudden absence of room tone is a horror tool.

## Music decisions

| Format | Default |
|---|---|
| UGC / persona | **No music** [Tested]. Room tone and silence carry authenticity; music signals "ad". |
| Cinematic | Score added in the edit, under native audio [Tested: music under the native audio track]. |
| Music video | The track goes on in the edit. Generated audio stays minimal or is replaced. |
| Product | Designed product sounds first (a click, a pour, an engine note), then music if the brand needs it. |

In generation, write "No music" explicitly when you don't want any [Tested], because models often add a score.

## Sound as storytelling

- **Off-screen sound** expands the world and creates dread: a door downstairs, a dog stopping barking.
- **Sound bridges / J-cuts**: the next shot's sound starts before the cut. Plan it in the edit, and write the sound early in the outgoing shot if needed.
- **Perspective**: distant vs close ("muffled through the wall", "right at the mic").
- **Sync points**: a clang, a slam or a click on a cut gives the edit snap.

## Voice in generation [Tested]

Always include a voice spec when someone speaks, identical across blocks:

> A natural, warm, human [female/male] voice, casual conversational cadence, real pitch variation, small natural imperfections. Must sound like an actual person, NOT synthetic or robotic.

For voiceover, write `Voiceover, no lip sync:` before the line.

## Output format — audio line

```
Audio: [room tone] · [synced effect at time] · [voice: "line" or none] · [music: none | as specified]
```

## Sound checks

- [ ] Every shot has an `Audio:` line with named sounds and timings.
- [ ] Music is decided (often "No music" in generation).
- [ ] Silence is written as a beat where it matters.
- [ ] A voice spec is present and identical, and voiceover is labelled.
