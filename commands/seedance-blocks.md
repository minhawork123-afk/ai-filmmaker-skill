---
description: "Write generation-ready Seedance 2.5 block prompts from a script or beats and your reference images"
argument-hint: "[script or beats, images in upload order, aspect ratio, length]"
---

Use the ai-filmmaker skill (jump-in mode, Stage 5).

Turn the material below into Seedance 2.5 block prompts:
1. Ask in one message only for what's missing: what happens (script or beats), the images in upload order (this becomes the @Image map, so keep the user's order), aspect ratio, total length, and their Style DNA (if they have none, write one and lock it). Build a minimal Production Bible.
2. Split into 12–20 s blocks (30 s max) at story beats.
3. For each block, state the director's judgment in 3–6 lines, then write the block in its own code block: camera first, physical actions only, timestamps from 0 that total the block exactly, LEFT/RIGHT facts, the last-frame slot from block 2 on, and the Style DNA byte-identical at the end.
4. Run the quality gate. If you can run code, save the blocks to a file and run scripts/validate_blocks.py; otherwise check by hand. List the fixes.

Material: $ARGUMENTS
