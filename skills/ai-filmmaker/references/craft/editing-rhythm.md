# Craft — Editing and Rhythm

Rhythm is designed before generation, through shot durations and block splits, and finished in the edit. Unlabelled content is **[General best practice]**; workflow-proven rules are marked **[Tested]**.

## Durations are rhythm [Tested]

- Standard beat: 3–4 s. Travel, reveal or collapse: 5–6 s. Fast cut: 2 s. Under 2 s rarely renders cleanly.
- Shot durations must total the block length exactly.
- Blocks: 12–20 s target, 30 s hard ceiling, split at story beats.

```text
WEAK    0–3s, 3–6s, 6–9s, 9–12s, 12–15s  (all equal)
STRONG  0–5s establish · 5–7s reaction · 7–10s detail · 10–15s hold on the reveal
WHY     Varying lengths create acceleration and a landing; equal lengths drone.
```

## Rhythm patterns

| Pattern | Durations (15 s block) | Feeling |
|---|---|---|
| Slow build → hold | 5 / 3 / 3 / 4 | dread, revelation |
| Accelerate | 5 / 4 / 3 / 3 | rising energy, chase |
| Stutter + release | 3 / 2 / 2 / 8 | shock, then sit with it |
| Even observational | 4 / 4 / 3 / 4 | UGC, documentary |
| Beat-locked (120 BPM) | 4 / 2 / 2 / 4 / 3 | music video, bars of 2 s |

Music videos: at BPM *b*, one bar of 4/4 = 240 ÷ *b* seconds (120 BPM → 2 s, 90 BPM → 2.67 s). Cut on downbeats; save the longest hold for the drop. If the bars don't make a whole number of seconds, round the block up, keep the internal cuts on bar lines, and let the last shot absorb the remainder for trimming.

## Cut on action [Tested]

Cut at the peak of a movement, not after it settles. In generation, overlap the action slightly across shots (the hand starts reaching at the end of shot A, completes the reach in shot B), so the edit has a cut point.

## Trims [Tested]

The first and last 10–15 frames of each generated block often have motion artifacts. Trim them in the edit. That means:
- Don't place key action in the first or last half-second of a block.
- Start each block with the action already settled, and end it with a described final frame (which feeds the next block's last-frame handoff).

## Endings and holds

- Let shots run slightly too long before cutting when you want discomfort or exhaustion [Tested pattern: "let this shot run slightly too long before cutting"].
- Hard cut mid-movement for abrupt UGC endings [Tested pattern: the clip cuts before the hand reaches the lens].
- For an image ending, hold 3–5 s with nothing new entering the frame.

## Dialogue editing [Tested]

- For persona content, sync dialogue cuts to natural breath breaks, not mid-sentence.
- Leave the silences in; don't tighten every pause.

## The edit pass, by tool [Tested]

**CapCut (persona / fast turnaround):** import blocks in order → trim heads and tails → cut on action → native audio on top, music under (usually none for UGC) → minimal or no grade → export.

**After Effects (cinematic):** assemble → a single adjustment-layer grade → subtle vignette → 35mm grain overlay at 10–15% if needed → minimal title cards (clean serif or sans-serif, never default fonts) → export.

**Export:** 1080p minimum, 4K if possible. YouTube: H.264, high bitrate. Instagram/TikTok: 9:16, H.265.

## Transitions

- Straight cuts by default. Every other transition must earn its place.
- Match cuts (shape, motion or colour) connect two blocks or locations elegantly. Plan the matching frames in the prompts.
- Use a sound bridge (J-cut, L-cut) to smooth a location change.
- Avoid generated "transition effects". Make transitions in the edit.

## Output format — edit plan

```
EDIT PLAN — [tool]
Order:   B1 → B2 → …
Trims:   B1 head __f / tail __f · …
Cuts:    [where, and on which action]
Holds:   [which shot runs long, and why]
Sound:   native audio on top · music [none | feel, level] · bridges
Grade:   [one adjustment layer: grade] · vignette · grain __%
Text:    [none | end card / titles, font, duration]
Export:  [aspect] · [resolution] · [codec]
```

## Rhythm checks

- [ ] Shot lengths vary deliberately, and the block lands on its longest or most important shot.
- [ ] No key action in the first or last ~0.5 s of a block.
- [ ] Block splits fall on story beats.
- [ ] The edit plan covers order, trims, cut points, sound, grade, text and export.
