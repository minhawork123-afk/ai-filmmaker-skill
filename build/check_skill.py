#!/usr/bin/env python3
"""Static checks for the ai-filmmaker skill and its packaging. Standard library only.

- SKILL.md frontmatter uses only Agent Skills spec fields (Claude.ai rejects other keys)
- name matches the folder and the spec's character rules; description <= 1024 chars, no < or >
- SKILL.md body under 500 lines
- every references/... path mentioned in SKILL.md exists
- plugin.json, marketplace.json and gemini-extension.json are valid and agree on name/version
- every commands/*.md has a matching commands/*.toml
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ai-filmmaker"
ALLOWED = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}

errors = []


def frontmatter(text):
    if not text.startswith("---\n"):
        errors.append("SKILL.md: no YAML frontmatter")
        return {}, text
    end = text.index("\n---\n", 4)
    raw, body = text[4:end], text[end + 5:]
    data, key = {}, None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):
            if key:
                data.setdefault(key + ".children", []).append(line.strip())
            continue
        k, _, v = line.partition(":")
        key = k.strip()
        data[key] = v.strip().strip('"')
    return data, body


skill_text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
fm, body = frontmatter(skill_text)
top_keys = {k for k in fm if not k.endswith(".children")}
if top_keys - ALLOWED:
    errors.append("SKILL.md: frontmatter keys not allowed by the Agent Skills spec: %s" % sorted(top_keys - ALLOWED))
name = fm.get("name", "")
if name != SKILL_DIR.name:
    errors.append("SKILL.md: name %r must match folder %r" % (name, SKILL_DIR.name))
if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
    errors.append("SKILL.md: invalid name %r" % name)
desc = fm.get("description", "")
if not desc or len(desc) > 1024:
    errors.append("SKILL.md: description must be 1-1024 chars (is %d)" % len(desc))
if "<" in desc or ">" in desc:
    errors.append("SKILL.md: description must not contain < or >")
if len(fm.get("compatibility", "")) > 500:
    errors.append("SKILL.md: compatibility over 500 chars")
lines = body.count("\n") + 1
if lines >= 500:
    errors.append("SKILL.md: body is %d lines (keep under 500)" % lines)

for ref in sorted(set(re.findall(r"`(references/[^`*<>]+\.md)`", skill_text))):
    if not (SKILL_DIR / ref).exists():
        errors.append("SKILL.md references missing file: %s" % ref)
for sub in ("craft", "translation"):
    for ref in re.findall(r"`(%s/[a-z0-9.-]+\.md)`" % sub, skill_text):
        if not (SKILL_DIR / "references" / ref).exists():
            errors.append("SKILL.md references missing file: references/%s" % ref)

plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
gemini = json.loads((ROOT / "gemini-extension.json").read_text(encoding="utf-8"))
version = fm.get("metadata.children") and next(
    (c.split(":", 1)[1].strip().strip('"') for c in fm["metadata.children"] if c.startswith("version:")), None)
if not (plugin["name"] == gemini["name"] == name == market["plugins"][0]["name"]):
    errors.append("plugin/marketplace/gemini/skill names disagree")
if not (plugin["version"] == gemini["version"] == version):
    errors.append("versions disagree: plugin %s, gemini %s, SKILL.md metadata %s"
                  % (plugin["version"], gemini["version"], version))

md = {p.stem for p in (ROOT / "commands").glob("*.md")}
toml = {p.stem for p in (ROOT / "commands").glob("*.toml")}
if md != toml:
    errors.append("commands: .md and .toml sets differ: %s" % sorted(md ^ toml))

for e in errors:
    print("ERROR: " + e)
print("check_skill: %s" % ("OK" if not errors else "%d problem(s)" % len(errors)))
sys.exit(1 if errors else 0)
