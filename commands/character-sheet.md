---
description: "Write the portrait, three-panel character sheet and skin-pass prompts for one character (Nano Banana Pro)"
argument-hint: "[character description, or 'from photos']"
---

Use the ai-filmmaker skill (jump-in mode, Stage 3).

Write the reference prompts for this character, each in its own code block with a label line:
1. Portrait, 4:5. Generate first and approve the face.
2. Three-panel character sheet, 16:9, headless centre panel, with the approved portrait attached.
3. Skin realism pass, to use only if the sheet looks airbrushed.
If the user has four real photos of the person, use the real-photo identity lock instead.

Ask only for missing essentials (description or photos, wardrobe, the project's look) in one message, and default the rest. Add or update the character in the Production Bible, run the quality gate and list any fixes.

Character: $ARGUMENTS
