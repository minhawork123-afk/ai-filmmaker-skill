# AI Filmmaker — an Agent Skill

### Turn any LLM into a professional AI filmmaker: director, cinematographer, editor and prompt engineer.

Load this skill and your assistant stops acting like a generic chatbot and starts running a production. It reads the project, asks the five brief questions that matter, locks a Production Bible, decides the shots, lenses, light and rhythm, and hands you copy-ready prompts for **Nano Banana Pro** (reference images) and **Seedance 2.5** (video), stage by stage, with a quality gate before every handoff.

It's built from a production-tested workflow (the films are [below](#proof-of-concept)), but it teaches the **craft**, not one project. Cinematic shorts, UGC ads, AI personas, product commercials, horror teasers, music videos: it works out the right approach for each.

Works in **Claude.ai · Claude Code · ChatGPT · Gemini CLI · the Gemini app · Custom GPTs and Gems · any LLM.**

---

## What it does

- **Detects the project type** (cinematic, UGC/persona, product commercial, or the nearest fit) and loads the right playbook.
- **Runs the 5-question brief**, then keeps a **Production Bible**: title, locked Style DNA, characters, products, locations, the fixed `@Image1..N` map and continuity facts. It re-prints the Bible whenever anything changes.
- **States a director's judgment** before writing prompts: the beat, the shot list, lens and light logic, edit rhythm and sound, in 3–6 lines.
- **Works through 7 stages**: idea → script → reference image prompts → image generation → video block prompts → generation → edit plan. It asks before moving on.
- **Jump-in mode**: "just write my Seedance blocks", "character sheet for my persona", "why does the face drift?". It starts wherever you are.
- **Quality gate** before every handoff, against the five core principles. It fixes violations silently, then lists what it fixed.
- **Is honest about what's proven.** Every piece of advice is labelled **[Tested]** (proven in real productions) or **[General best practice]**, and it never invents what a model can do.

## The core principles

> **Name the mechanism, never the mood.** Not "make it cinematic": name the lens, the light source, the colour grade.
> **Lock the character first, the location second.** Later prompts say "match @Image1" instead of re-describing.
> **Physical actions only, never interior states.** "Her jaw tightens, she doesn't blink", not "she is nervous".
> **Style DNA is written once and pasted byte-identical.** One project, one signature.
> **Dialogue and physical action never overlap.** She speaks, or she moves.

---

## 30-second demo

> **You:** 15-second horror teaser. A babysitter hears the baby monitor whisper her name.
>
> **AI Filmmaker:** Reading this as a **cinematic** horror teaser, 16:9, 15 s, one block, full production. Your idea answers most of the brief, so here are my assumptions. Change anything:
> *Who:* Jess, early 20s, oversized grey hoodie · *Where/when:* a suburban living room, 11 pm, rain · *Tone:* quiet, wrong, dreadful · *End feeling:* she isn't alone.
>
> ```
> PRODUCTION BIBLE · v1
> Title: Monitor · Type: cinematic (horror teaser) · 16:9 · 15 s · 1 block
> STYLE DNA (LOCKED): Shot on ARRI Alexa 35 with spherical prime lenses. Slow, locked-off frames…
> @IMAGE MAP: @Image1 = Jess sheet · @Image2 = living room plate
> ```
>
> **You:** Go.
>
> **AI Filmmaker:**
> ```
> DIRECTOR'S JUDGMENT — Block 1 (0–15 s)
> Beat:   the monitor's static resolves into her name; she turns to the dark hallway
> Shots:  WS couch (establish) → insert monitor → CU Jess → POV hallway
> Lens/light: 24mm locked-off; TV glow as the only key, cold streetlight through rain-streaked glass camera-LEFT
> Rhythm: 5/3/3/4 s — silence before the whisper, hold on the empty hallway
> Sound:  rain, TV murmur at −30 dB, monitor hiss → "Jess…" at 8 s → TV cuts out
> ```
> …followed by the portrait, character sheet and plate prompts, then the Seedance block, each in its own code block, and:
> `Quality gate — 2 fixes: "she looks scared" → "her breath stops, eyes fixed on the monitor"; 1.5 s insert extended to 3 s, durations now total 15 s`

---

## Install

The release zip `ai-filmmaker.zip` is attached to every [GitHub release](https://github.com/minhawork123-afk/ai-filmmaker-skill/releases/latest). It contains the `ai-filmmaker/` skill folder and works for Claude.ai, ChatGPT Skills and the Gemini app.

### Claude.ai (web, desktop, mobile)
1. Download `ai-filmmaker.zip` from the [latest release](https://github.com/minhawork123-afk/ai-filmmaker-skill/releases/latest).
2. Make sure code execution is enabled (Settings → Capabilities).
3. Go to **Customize → Skills**, upload the zip, and turn **ai-filmmaker** on.
4. Describe your project. Claude loads the skill when it's relevant.

### Claude Code
```text
/plugin marketplace add minhawork123-afk/ai-filmmaker-skill
/plugin install ai-filmmaker@faizan-film-labs
```
Or, from your shell: `claude plugin marketplace add minhawork123-afk/ai-filmmaker-skill` and then `claude plugin install ai-filmmaker@faizan-film-labs`.

This adds the skill plus five slash commands (type the short name, or the full `/ai-filmmaker:film-brief` form if another command shares the name):

| Command | Does |
|---|---|
| `/film-brief` | Starts a production: detects the type, runs the brief, opens the Bible |
| `/character-sheet` | Portrait → headless three-panel sheet → skin pass prompts |
| `/location-plate` | Location plate prompts with named light and placed key elements |
| `/seedance-blocks` | Jump-in: block prompts from your script and images |
| `/review` | Runs the quality gate on any prompt and returns the fixed version |

Skill only, without the commands: copy `skills/ai-filmmaker/` into `~/.claude/skills/`.

### ChatGPT
- **Skills** (where available on your plan): **Skills → Create → Upload from your computer**, then choose `ai-filmmaker.zip`.
- **Custom GPT**: paste `portable/SYSTEM_PROMPT.md` into Instructions and upload the 10 files in `portable/knowledge/`. Step-by-step instructions: [`portable/README.md`](./portable/README.md#chatgpt--custom-gpt).

### Gemini CLI
```bash
gemini extensions install https://github.com/minhawork123-afk/ai-filmmaker-skill
```
This installs the skill plus the same five commands (`/film-brief`, `/character-sheet`, `/location-plate`, `/seedance-blocks`, `/review`). Skill only: `gemini skills install https://github.com/minhawork123-afk/ai-filmmaker-skill.git --path skills/ai-filmmaker`.

### Gemini app and Gems
- **Gemini app skills** (personal accounts; Gems become skills from November 2026): **Settings → Skills → Upload**, then choose `ai-filmmaker.zip`.
- **Gem** (work and school accounts until skills arrive): paste `portable/SYSTEM_PROMPT.md` into the Gem's instructions and add the 10 `portable/knowledge/` files. See [`portable/README.md`](./portable/README.md#gemini--gem-work-and-school-accounts-or-if-skills-arent-available-yet).

### Any other LLM
Paste [`portable/SYSTEM_PROMPT.md`](./portable/SYSTEM_PROMPT.md) as the system prompt and attach the [`portable/knowledge/`](./portable/knowledge/) files. For a large-context model, paste [`portable/ai-filmmaker-full.md`](./portable/ai-filmmaker-full.md) in one go. Any other Agent Skills–compatible tool: copy `skills/ai-filmmaker/` into its skills folder.

---

## What's inside

```
skills/ai-filmmaker/              ← the skill (this folder is what gets zipped)
├── SKILL.md                      director logic: type → brief → Bible → judgment → stages → quality gate
├── references/
│   ├── principles.md             the five principles, full quality gate, fix report
│   ├── craft/                    story, performance, shot design, cinematography, lighting,
│   │                             colour & grade, sound, editing rhythm, continuity
│   ├── translation/              craft → prompt: mechanism-not-mood, image prompt formats, video block formats
│   ├── models/                   seedance-2.5.md, nano-banana-pro.md  ([Tested] vs [General best practice])
│   ├── workflow/                 the 7 stages + cinematic, UGC/persona, product-commercial playbooks
│   ├── style-dna-library.md      4 tested + 6 best-practice Style DNA presets
│   └── troubleshooting.md        face drift, morphing, label warping, lip-sync, continuity
└── scripts/validate_blocks.py    checks block prompts (timing, Style DNA, mood words, dialogue/action)

commands/                         slash commands (.md for Claude Code, .toml for Gemini CLI)
.claude-plugin/                   Claude Code plugin + marketplace manifests
gemini-extension.json             Gemini CLI extension manifest
portable/                         system prompt + 10 knowledge files for GPTs, Gems, any LLM
showcase/                         the real productions: assets and prompts, for humans only
tools/                            Character Sheet Builder + launch film (single HTML files)
build/  tests/  .github/          packaging, checks, CI and release
```

The skill teaches with short **weak → strong → why** patterns instead of copying full prompt sets:

```text
WEAK    He drops the phone.
STRONG  His hand goes limp, the fingers uncurl, the phone slips from a slack grip — he does not throw it.
WHY     "Drops" is often rendered as a deliberate throw; a mechanism plus the wrong version steers the model.
```

## Validate your block prompts

If your assistant can run code, it validates block prompts itself. You can also run the validator directly:

```bash
python3 skills/ai-filmmaker/scripts/validate_blocks.py my-blocks.md
```

It checks:
- **Errors:** timestamps restart at 0 and are contiguous, shots total the block length, blocks are 30 s or less, and the Style DNA is identical across blocks.
- **Warnings:** shots under 2 s, mood or interior-state words in shot lines, on-camera dialogue during movement, and undeclared `@Image` slots.

It needs only Python 3.8+ with the standard library.

---

## Proof of concept

These films were made with the workflow this skill is built on.

**AI persona / UGC ad — Tess / LODE Protein.** Character sheet → product reference → location plates → Seedance 2.5 block prompts → CapCut.
▶️ [Watch the finished video](https://lnkd.in/p/dXEZhci9) · assets and production prompts in [`showcase/tess-lode-ugc/`](./showcase/tess-lode-ugc/)

**Cinematic concept film — BMW M350 xDrive.** Brief → script → character sheets → location plates → Seedance 2.5 → After Effects.
▶️ [Watch on YouTube](https://www.youtube.com/watch?v=84tbDvXKknw)

**Live workflow breakdown.** The full production process, step by step.
▶️ [Watch on YouTube](https://www.youtube.com/watch?v=bJXobsqN85w)

**Launch film.** 30 seconds on why AI filmmaking looks complex and the 7 stages that fix it.
▶️ [Watch the launch film](https://minhawork123-afk.github.io/ai-filmmaker-skill/tools/launch-film/)

## Tools

- **[Character Sheet Builder](https://minhawork123-afk.github.io/ai-filmmaker-skill/tools/character-sheet-builder/)**: describe a character in a form and get the 4:5 portrait prompt and the 16:9 three-panel sheet prompt. A single HTML file that runs in your browser. Source: [`tools/character-sheet-builder/`](./tools/character-sheet-builder/)
- **[Launch film](https://minhawork123-afk.github.io/ai-filmmaker-skill/tools/launch-film/)**: a single HTML file; the animation and soundtrack are generated live in the browser. Source: [`tools/launch-film/`](./tools/launch-film/)

## Contributing

- **Made something with the skill?** Add a folder to [`showcase/`](./showcase/) with the finished video link, your reference prompts, your block prompts and a one-line description.
- **Found a model behaviour worth teaching?** Open an issue with the before/after prompts. Only things proven in a real generation get the [Tested] label.
- **Before opening a PR**, run `python3 build/check_skill.py`, `python3 -m unittest discover -s tests` and `python3 build/build_portable.py`.

---

Made by **Fazi — [Faizan Film Labs](https://faizanfilmlabs.online)** · AI filmmaker and multi-language YouTube creator.

MIT License — see [LICENSE](./LICENSE). Use freely; credit appreciated.
