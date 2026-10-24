# Craft — Continuity

Across blocks, AI video forgets everything you don't restate. Continuity is a system of locks, hard facts and handoffs. Unlabelled content is **[General best practice]**; workflow-proven rules are marked **[Tested]**.

## The locks [Tested]

1. **Identity lock**: a character sheet per person and a reference per product, generated before any video.
2. **Space lock**: a location plate per setting, with no people.
3. **Look lock**: the Style DNA, pasted byte-identical into every block.
4. **Slot lock**: the @Image upload order, fixed for the whole project (characters → products → locations → last frame). The prompt binds to slots, not file names.
5. **Motion lock**: the final frame of block N, attached to block N+1.

```text
WEAK    Block 2: Mara continues walking down the same street as before.
STRONG  Block 2: @Image4 is the final frame of Block 1 — continue from it exactly. @Image1 walks on through @Image3.
WHY     "Same as before" means nothing to a model with no memory; the last frame does.
```

## Hard facts, restated in every block [Tested]

- **Sides**, in capitals: "the bandage is on his RIGHT hand", "the bag hangs from her LEFT shoulder". Models mirror references constantly.
- **Wardrobe state**: what is on, what is off, and what must NOT appear ("the jacket is already off and must not appear").
- **Condition**: wet, muddy, wounded, sweating, and exactly where.
- **Props**: who holds what, in which hand.
- **Time and weather**: these persist unless the script changes them.
- **Face source**: "In each character sheet, take the face from the chest-up portrait panel. The centre panel omits the head deliberately." [Tested]

## Progression across blocks [Tested pattern]

When something changes over time (sweat building, rain soaking clothes, light fading), write the start state, the end state and the direction:

```text
STRONG  Over this block @Image1 goes from dry to soaked: rain darkens the coat shoulders first, then the hair flattens against the forehead.
WHY     Start, end and location of the change; the model interpolates instead of inventing.
```

Then the next block starts from that end state.

## The last-frame handoff [Tested]

1. End each block on a described, stable frame: "END ON THIS FRAME — [pose, position in frame, wardrobe state, light]".
2. After generating, save that frame as a still.
3. Attach it as the last slot of the next block, and open that block with: "This clip picks up seconds after the previous one."
4. At a **scene change** (a new location or a time jump), the last frame shows the wrong setting. Leave it out, or attach it for the character's face and wardrobe only and name the new plate as the setting [General best practice, untested].

## Same place, different light

If a location changes time of day or lighting state (lamp on → lamp off, night → morning), generate a **separate plate for each lighting state** and give each its own @Image slot [General best practice]. The plate's light becomes the video's light, so one night plate can't be asked to play morning.

## Screen direction and geography

- Keep characters on consistent sides of the frame within a scene, and state it in every block.
- Exits and entrances match: out frame RIGHT, in from frame LEFT.
- Direction of travel is a hard fact for vehicles and walks.

## Continuity ledger (keep it in the Bible)

```
CONTINUITY
@Image1: bandage RIGHT hand · grey hoodie ON (Block 1) → OFF (Block 2+) · hair wet from Block 2
@Image2 (product): label always faces camera, cap ON until 0:22
Time: dusk → full dark by Block 3 · rain: continuous
Screen: @Image1 frame LEFT, @Image3 frame RIGHT in the kitchen scene
```

## Common breaks and fixes

| Break | Fix |
|---|---|
| Face changes between blocks | Never change the upload order; attach the last frame from block 2 onward [Tested] |
| Location looks different | The same plate in every block, plus "match @ImageN" [Tested] |
| Prop jumps hands | State the hand in every block, in capitals |
| Wardrobe reappears | Say what must not appear, and add it to NEGATIVE |
| Light or colour shifts | Byte-identical Style DNA [Tested]; one grade layer in the edit [Tested] |

## Continuity checks

- [ ] Every block declares the full @Image set in Bible order, and blocks 2+ include the last frame.
- [ ] The sides, wardrobe, condition and props in each block match the ledger.
- [ ] Every block except the last ends on a described frame.
- [ ] Each progression has a start state, an end state and a location.
