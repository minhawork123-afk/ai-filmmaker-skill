# Portable setup — ChatGPT, Gemini, and any LLM

Use this folder where Agent Skills aren't available, or where you'd rather configure an assistant by hand.

| File | What it is |
|---|---|
| `SYSTEM_PROMPT.md` | The director logic, condensed to about 6,100 characters (under the 8,000-character Custom GPT limit) |
| `knowledge/` | 10 files, 00–09, covering the whole skill. Upload all of them |
| `ai-filmmaker-full.md` | Everything in one file, for pasting into a large-context LLM |

The knowledge files are generated from `skills/ai-filmmaker/` by `build/build_portable.py`, so they always match the skill. Download them from this folder, or get `ai-filmmaker-portable.zip` from the [latest release](https://github.com/minhawork123-afk/ai-filmmaker-skill/releases/latest).

> **Prefer real skills where you can.** ChatGPT and the Gemini app both accept the same `SKILL.md` skill format now. Uploading `ai-filmmaker.zip` (from the latest release) gives you progressive loading and the full skill. Use the manual setups below when skills aren't available on your plan.

---

## ChatGPT — Skills (recommended where available)

1. Download `ai-filmmaker.zip` from the [latest release](https://github.com/minhawork123-afk/ai-filmmaker-skill/releases/latest).
2. In ChatGPT, open **Skills → Create → Upload from your computer** and choose the zip, or the unzipped `ai-filmmaker` folder.
3. Wait for the scan to finish, then make sure the skill is turned on.
4. Start a chat with something like *"I want to make a 30-second UGC ad for a coffee brand"*, or call the skill with `@ai-filmmaker`.

Availability varies by plan and is still rolling out. If you don't see **Skills**, use a Custom GPT.

## ChatGPT — Custom GPT

1. Go to **Explore GPTs → Create**, then open the **Configure** tab.
2. **Name:** AI Filmmaker. **Description:** *Director, cinematographer, editor and prompt engineer for realistic AI video.*
3. **Instructions:** paste the entire contents of `SYSTEM_PROMPT.md`.
4. **Knowledge:** upload all 10 files from `knowledge/` (00–09).
5. **Capabilities:** turn on **Code Interpreter** if you want block prompts validated automatically. Then also upload `skills/ai-filmmaker/scripts/validate_blocks.py` as an 11th knowledge file. Skip this if your plan caps knowledge at 10 files.
6. **Conversation starters** (suggested):
   - Start a new AI film with me
   - Write my Seedance blocks — I already have my images
   - Build a character sheet for my AI persona
   - Review and fix this video prompt
7. Save the GPT, choosing whichever sharing setting you want.

Note: there are reports that OpenAI is moving some workspaces from GPTs to plugins and skills. If GPT creation isn't available to you, use Skills.

## Gemini app — Skills (recommended for personal accounts)

Google is replacing Gems with skills: from November 2026 for personal accounts, and in 2027 for work and school accounts.

1. Download `ai-filmmaker.zip` from the [latest release](https://github.com/minhawork123-afk/ai-filmmaker-skill/releases/latest).
2. In the Gemini web app or the Mac app, open **Settings → Skills → Upload**, choose the zip, review it, and click **Create**.
3. Make sure the skill is active, then describe your project in a chat.

## Gemini — Gem (work and school accounts, or if skills aren't available yet)

1. Open the **Gem manager → New Gem**.
2. **Name:** AI Filmmaker.
3. **Instructions:** paste the entire contents of `SYSTEM_PROMPT.md`.
4. **Knowledge:** add all 10 files from `knowledge/`. Gems take up to 10 files, which is why the set is exactly 10.
5. Save, and start with a project description.

## Any other LLM

**Option A — system prompt plus files** (best quality):
1. Paste `SYSTEM_PROMPT.md` as the system prompt, custom instructions, or the first message.
2. Attach the `knowledge/` files, or paste the ones the current stage needs. The prompt tells the model which file covers what.

**Option B — one file** (for large-context models, about 40k tokens):
1. Paste the whole `ai-filmmaker-full.md` as the first message.
2. Then describe your project.

In both cases the assistant can't run the validator unless your tool can execute code. Without it, the assistant checks the blocks by hand, and it's told never to claim it ran the script.

---

## Keeping it up to date

The portable files are rebuilt from the skill whenever it changes:

```bash
python3 build/build_portable.py          # regenerate knowledge/ and ai-filmmaker-full.md
python3 build/build_portable.py --check  # CI: fail if they are stale
```

`SYSTEM_PROMPT.md` is written by hand. CI checks that it stays under 7,500 characters.
