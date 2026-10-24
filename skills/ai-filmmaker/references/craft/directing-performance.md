# Craft — Directing Performance

AI actors can't take notes, so every performance choice has to be written as visible, physical behaviour with a duration. Unlabelled content is **[General best practice]**; workflow-proven rules are marked **[Tested]**.

## The core rule [Tested]

Physical actions only, never interior states. A video model renders what a camera sees, so give it something to see.

```text
WEAK    She is heartbroken.
STRONG  She reads the text, lowers the phone to her lap, and keeps staring at the dark screen.
WHY     Stillness after an action reads as impact; "heartbroken" is not a pixel.
```

## A vocabulary of visible behaviour

Build emotions from these physical channels instead of naming them.

| Channel | Examples a camera can see |
|---|---|
| Eyes | holds still without blinking · slides LEFT to the door · drops to the floor · unfocused just past the lens · squints against the light |
| Jaw / mouth | tightens · pushes slightly forward · lips press into a line · mouth falls slightly open · swallows |
| Breath | stops · shallow and fast, shoulders rising · one long exhale through the nose · catches |
| Hands | thumb rubs a seam · fingers tap twice then stop · grip whitens on the strap · hand hovers, doesn't touch |
| Posture | shoulders drop · weight shifts to the back foot · leans in an inch · goes completely still |
| Tempo | moves a half-beat slower than normal · stops mid-step · turns too fast |

Combine two channels for a clear read: *"jaw tightens; she doesn't blink"* [Tested phrasing].

## Mechanics that stop the model improvising [Tested]

**Sustained poses need a duration.**
```text
WEAK    He aims the gun at the door.
STRONG  He holds the aim on the door for the full three seconds and does not lower the arm.
WHY     Without a duration the model resolves the pose early.
```

**Involuntary motion needs a mechanism.**
```text
WEAK    He drops the phone.
STRONG  His hand goes limp, the fingers uncurl, the phone slips from a slack grip.
WHY     "Drops" is often rendered as a deliberate throw or toss.
```

**Name the wrong version inline when a mistake is likely.**
```text
STRONG  The glass slips free — she does not open her hand, does not throw it.
WHY     Explicitly ruling out the likely error steers the model away from it.
```

**State sides as hard facts, in capitals** [Tested]: "the cut is above her RIGHT eye", "the bag is on his LEFT shoulder". Models mirror references.

**One action per shot, in sequence.** If a character must do two things, split them across two shots, or chain them with "then" and a beat.

## Dialogue on camera [Tested]

- Dialogue and physical action never overlap. She speaks, or she moves. Sequence it as move → settle → speak.
- Voiceover with no lip sync may play over action shots (hands, inserts, wides with no visible mouth). Label it: `Voiceover, no lip sync: "…"`.
- Leave real silence between lines; write the pause ("she pauses for a full half-second, looking slightly off-lens").
- Give delivery as sound, not emotion: *flat, unhurried, slightly out of breath, half-swallowed last word.*

```text
WEAK    She angrily says, "Get out."
STRONG  She stops wiping the counter. Doesn't look up. Flat and quiet: "Get out."
WHY     Stillness + a delivery note is a performance; "angrily" is a guess.
```

## Voice specification [Tested]

Robotic, synthetic voices are the most common persona failure. Include a voice spec whenever someone speaks, and keep it identical across blocks:

> A natural, warm, human [female/male] voice, casual conversational cadence, real pitch variation, small natural imperfections. Must sound like an actual person, NOT synthetic or robotic.

Adapt the delivery words per character (low energy and dry; clipped and precise; breathless), but never drop the "actual person, NOT synthetic" clause.

## Energy and register

- **UGC / persona** [Tested]: low energy, underselling, talking to the phone like a friend, no smiling at the lens. Understatement reads as credible.
- **Drama:** fewer, smaller movements, longer holds. Stillness is a choice; write it with a duration.
- **Action:** big, clear, single-direction movements; one beat per shot; land each move before the cut.
- **Comedy:** timing is the performance. Write the pause length and the exact reaction shot.

## Blocking and eyelines

- Say where the character is in frame and where they move: "enters frame LEFT, crosses to the window at frame RIGHT, stops".
- Eyelines are hard facts: "@Image1 looks off-camera LEFT toward @Image2". Keep them consistent across shots in a conversation.
- Looking into the lens is a deliberate choice (UGC, confession, horror). Otherwise state "does not look at the camera".

## Performance checks

- [ ] No emotion words; every feeling is a visible behaviour.
- [ ] Every held pose has a duration, and every involuntary motion has a mechanism.
- [ ] No on-camera line overlaps movement, and voiceover is labelled.
- [ ] A voice spec is present and identical across blocks.
- [ ] Sides, eyelines and frame positions are stated.
