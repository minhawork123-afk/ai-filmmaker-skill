# Self-test log — v1.0.0

Three sessions were walked through using only `skills/ai-filmmaker/SKILL.md` and the reference files it points to. Each followed SKILL.md literally: detect the type → brief → Bible → director's judgment → stage outputs → quality gate. Every block prompt produced was run through `scripts/validate_blocks.py`. The final block prompts are kept as regression fixtures in [`tests/fixtures/`](../tests/fixtures/), and CI fails if they stop validating cleanly.

This was a structured walkthrough by the author's assistant, not a blind test with a fresh model. Re-run it with a fresh model whenever SKILL.md changes, and add anything it trips on to the Gotchas.

| Session | Type | In the source guide? | Blocks | Validator |
|---|---|---|---|---|
| Sleep-gummy UGC ad, 30 s, 9:16 | ugc-persona + product | yes | 2 × 15 s | clean |
| Fisherman and the message in a bottle, 45 s, 16:9 | cinematic | yes | 3 × 15 s | clean |
| Synthwave roller-skate music-video moment, 20 s, 100 BPM | cinematic → music video | **no** | 1 × 20 s | clean |

## What was missing or confusing, and the fix

| # | Found during | Problem | Fix |
|---|---|---|---|
| 1 | UGC | Unclear when to write the Style DNA. Plates in Stage 3 need the look, but SKILL.md said "before the first video prompt" | Draft it in Bible v1 and lock it before Stage 5 (SKILL.md, seven-stages.md) |
| 2 | UGC | Should a phone-look persona get a phone-shot sheet? | Sheets always use the studio format; the look comes from the plates and the Style DNA (image-prompts.md) |
| 3 | UGC | The UGC block format had no END ON THIS FRAME slot | Added to format B (video-prompts.md) |
| 4 | UGC | The same bedroom at night and in the morning; one plate can't play both | One plate per lighting state (image-prompts.md, continuity.md, seven-stages.md) |
| 5 | Cinematic | The byte-identical Style DNA contained the storm, but the film moves to a calm dawn | The DNA holds film-wide constants only; scene light and weather go in each block (style-dna-library.md, SKILL.md, principles.md) |
| 6 | Cinematic | A "handheld" DNA contradicted locked-off shots | The movement slot is written as a rule plus its exception (style-dna-library.md) |
| 7 | Cinematic | At a scene change, the previous block's last frame drags the old set into the new scene | Leave it out, or attach it for identity only; labelled untested (video-prompts.md, continuity.md, seedance-2.5.md) |
| 8 | Cinematic | Format A's example slot numbers read as fixed numbering | Note that the numbers follow the Bible's @Image map (video-prompts.md) |
| 9 | Cinematic | The script used a cabin that had no plate | Stage 3 starts by listing every setting and lighting state; new gate item (seven-stages.md, principles.md) |
| 10 | Music video | Bars at 100 BPM (19.2 s) don't fit whole-second durations | Round the block up, keep the cuts on bar lines, let the last shot absorb the remainder (playbook-cinematic.md, editing-rhythm.md, seedance-2.5.md) |
| 11 | Cold read | No guidance for other models (Veo, Kling, Runway, Sora, Midjourney, Flux) | "Other tools" section: the craft transfers; syntax and limits are tested only on Seedance and Nano Banana (SKILL.md, video-prompts.md) |
| 12 | Cold read | No path for users without reference images | Text-only mode with CHARACTER/LOCATION LOCK lines; labelled untested (video-prompts.md) |
| 13 | Cold read | The validator path was ambiguous inside plugins and uploads | "relative to this SKILL.md" (SKILL.md) |
| 14 | Cold read | No rule on real people or brands | Real people only from their own photos and with consent; no public figures or unlicensed logos (SKILL.md) |
| 15 | Cold read | Re-printing the Bible at every stage start was noisy | Re-print on change, plus once before Stage 5 (SKILL.md) |
