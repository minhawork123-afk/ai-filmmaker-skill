---
description: "Review and fix AI image or video prompts against the ai-filmmaker quality gate"
argument-hint: "[paste prompt(s), or leave empty to review the latest ones]"
---

Use the ai-filmmaker skill and run its quality gate (references/principles.md) on the prompt(s) below. If nothing is pasted, review the most recent prompts in this conversation.

1. Identify the target model and the prompt type (portrait, sheet, plate, product reference, video block).
2. Fix every violation: name the mechanism not the mood, physical actions only, camera first, Style DNA byte-identical, no on-camera dialogue during action, timing rules, @Image binding, LEFT/RIGHT facts, realism clause, NEGATIVE line.
3. For video blocks, if you can run code, run scripts/validate_blocks.py on them; otherwise check by hand.
4. Return the corrected prompt(s), each in its own code block, then the 'Quality gate — N fixes' list. Label any advice about model behaviour [Tested] or [General best practice].

Prompt(s): $ARGUMENTS
