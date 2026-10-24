#!/usr/bin/env python3
"""Validate AI-video block prompts (Seedance-style) against the ai-filmmaker rules.

Checks, per block:
  ERROR  timestamps do not restart at 0, have gaps/overlaps, or run backwards
  ERROR  shot durations do not total the block length given in the header
  ERROR  block longer than the maximum (default 30 s)
  ERROR  Style DNA missing, or not identical across blocks
  WARN   timestamped segment shorter than the minimum (default 2 s), unless labelled MONTAGE
  WARN   mood / interior-state words in shot lines (Style DNA, NEGATIVE and MOOD lines are exempt)
  WARN   on-camera dialogue and physical action in the same shot with no sequencing
  WARN   @ImageN used in a shot but not declared in the block
  NOTE   block outside the 12-20 s target, camera not named first, sequenced dialogue+action

Usage:
  python3 validate_blocks.py blocks.md            # human-readable report
  python3 validate_blocks.py blocks.md --json     # machine-readable
  cat blocks.md | python3 validate_blocks.py -     # read stdin

Exit code: 1 if any ERROR (or any WARN with --strict), else 0.
Standard library only; Python 3.8+.
"""

import argparse
import json
import re
import sys

# --- vocab -------------------------------------------------------------------

MOOD_WORDS = [
    # look words
    "cinematic", "epic", "beautiful", "stunning", "gorgeous", "breathtaking", "amazing",
    "moody", "atmospheric", "dramatic", "aesthetic", "vibe", "vibes", "high quality",
    "masterpiece", "award-winning", "8k", "4k", "hyper-realistic", "ultra-realistic",
    "realistic", "lifelike",
    # light words
    "good lighting", "nice lighting", "perfect lighting",
    # interior states
    "nervous", "scared", "afraid", "terrified", "sad", "happy", "angry", "anxious",
    "excited", "confident", "determined", "in love", "feels", "feeling", "thinks",
    "realises", "realizes", "remembers", "wants", "decides",
    # sound words
    "ambient sound", "background noise", "epic music", "sound effects",
]

ACTION_VERBS = [
    # verb forms only - base forms ("walk", "open", "rack") are too often nouns or adjectives
    "walks", "walking", "runs", "running", "turns", "turning", "lifts", "lifting",
    "picks up", "grabs", "reaches", "reaching", "pours", "pouring", "opens", "closes",
    "throws", "shakes", "shaking", "scoops", "pulls", "pulling", "pushes", "climbs",
    "jumps", "crosses", "steps forward", "steps back", "steps in", "steps out", "dances",
    "dancing", "spins", "drives", "carries", "twists", "wipes", "zips", "sits down",
    "stands up", "gets up", "kneels down", "leans in", "unracks", "swings", "hands it",
    "hands over", "nods", "shrugs",
]  # static postures ("sits", "stands") are deliberately excluded
SEQUENCE_CUES = [
    "then", "after", "before", "once", "only after", "stops", "stopped", "pauses", "pause",
    "beat", "still", "settles", "has stopped", "not walking", "not moving", "stands still",
    "standing still", "until",
]
CAMERA_TERMS = [
    "handheld", "wide", "close-up", "close up", "closeup", "ecu", "mcu", "cu", "ws", "ms",
    "medium", "insert", "dolly", "push", "pull", "tracking", "track", "static", "locked",
    "overhead", "top shot", "pov", "selfie", "propped", "phone", "crane", "pan", "tilt",
    "mm", "lens", "shot", "angle", "camera", "aerial", "drone", "orbit", "arc", "macro",
    "montage", "same setup", "over-the-shoulder", "ots", "low", "high", "eye level",
    "establishing", "rack focus", "whip", "steadicam", "gimbal", "slider", "frame",
]

TIME = r"\d+:\d{2}(?:\.\d+)?|\d+(?:\.\d+)?"
DASH = r"\s*[–—\-]\s*"
SHOT_RE = re.compile(
    r"^\s*(?:[-*]\s+)?[\[(]?\s*(?P<a>" + TIME + r")\s*s?" + DASH + r"(?P<b>" + TIME + r")\s*s?"
    r"(?:\s*[\])]\s*[:·|.,]?|\s*[:·|.,]|\s*$)"
)
RANGE_RE = re.compile(r"(?P<a>" + TIME + r")\s*s?" + DASH + r"(?P<b>" + TIME + r")\s*s?\b")
BLOCK_RE = re.compile(r"^\s*(?:#+\s*)?BLOCK\s+(?P<id>[0-9]+|[A-Za-z])\s*(?:[—–\-·:|(]|$)(?P<rest>.*)$", re.IGNORECASE)
DNA_RE = re.compile(r"^\s*(?:\*\*)?style\s+dna(?:\*\*)?\s*:", re.IGNORECASE)
SECTION_RE = re.compile(
    r"^\s*(VOICE|AUDIO|NEGATIVE|LOOK|CAMERA|PACING|PERFORMANCE|CONTINUITY|END ON THIS FRAME)\b"
)
EXEMPT_LINE_RE = re.compile(r"^\s*(NEGATIVE|MOOD)\b", re.IGNORECASE)
FENCE_RE = re.compile(r"^\s*(```|~~~)")
IMAGE_DECL_RE = re.compile(r"^\s*@Image(\d+)\b")
IMAGE_USE_RE = re.compile(r"@Image(\d+)\b")
QUOTE_RE = re.compile(r"“[^”]*”|\"[^\"]*\"")
VO_RE = re.compile(r"voice-?over|\bV\.?O\.?\b|no\s+lip[\s-]?sync", re.IGNORECASE)


def parse_time(token):
    token = token.strip()
    if ":" in token:
        m, s = token.split(":", 1)
        return int(m) * 60 + float(s)
    return float(token)


def fmt(t):
    return ("%.2f" % t).rstrip("0").rstrip(".")


def word_pattern(phrase):
    return re.compile(r"(?<![\w-])" + re.escape(phrase) + r"(?![\w-])", re.IGNORECASE)


MOOD_PATTERNS = [(w, word_pattern(w)) for w in MOOD_WORDS]
ACTION_PATTERNS = [word_pattern(w) for w in ACTION_VERBS]
CUE_PATTERNS = [word_pattern(w) for w in SEQUENCE_CUES]
CAMERA_PATTERNS = [word_pattern(w) for w in CAMERA_TERMS]


# --- parsing -----------------------------------------------------------------

class Block:
    def __init__(self, name, header, line_no):
        self.name = name
        self.header = header
        self.line_no = line_no
        self.lines = []  # (line_no, text)
        self.duration = None
        m = RANGE_RE.search(header or "")
        if m:
            self.duration = parse_time(m.group("b")) - parse_time(m.group("a"))
        else:
            m = re.search(r"\(?\b(\d+(?:\.\d+)?)\s*s(?:ec(?:onds)?)?\b\)?", header or "")
            if m:
                self.duration = float(m.group(1))


def split_blocks(text):
    """Split on BLOCK headers. Text before the first header is a preamble and is
    ignored when headers exist; with no headers the whole text is one block."""
    blocks = []
    preamble = Block("1", "", 1)
    current = None
    for i, raw in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(raw):
            continue
        m = BLOCK_RE.match(raw)
        if m:
            current = Block(m.group("id").upper(), m.group("rest"), i)
            blocks.append(current)
            continue
        (current or preamble).lines.append((i, raw))
    if not blocks and any(t.strip() for _, t in preamble.lines):
        blocks.append(preamble)
    return blocks


def analyse_block(block):
    """Classify block lines into shots, the Style DNA section, and other tagged lines.

    Returns (shots, dna_text, other) where other is a list of (line_no, text, section).
    Continuation lines inherit the section of the line above until a blank line.
    """
    shots = []  # dict(a, b, line, text)
    dna_lines = []
    other = []
    in_dna = False
    current = None   # current shot
    section = None   # current non-shot section name
    for line_no, raw in block.lines:
        if DNA_RE.match(raw):
            in_dna = True
            rest = DNA_RE.sub("", raw).strip()
            if rest:
                dna_lines.append(rest)
            continue
        if in_dna:
            dna_lines.append(raw.strip())
            continue
        if not raw.strip():
            current, section = None, None
            continue
        m = SHOT_RE.match(raw)
        if m:
            current, section = {
                "a": parse_time(m.group("a")),
                "b": parse_time(m.group("b")),
                "line": line_no,
                "text": [(line_no, raw)],
            }, None
            shots.append(current)
            continue
        sm = SECTION_RE.match(raw)
        if sm:
            current, section = None, sm.group(1)
        elif EXEMPT_LINE_RE.match(raw):
            current, section = None, raw.strip().split(":")[0].split()[0].upper()
        elif IMAGE_DECL_RE.match(raw):
            current, section = None, "DECL"
        elif current is not None:
            current["text"].append((line_no, raw))
            continue
        other.append((line_no, raw, section or "TEXT"))
    dna = "\n".join(dna_lines).strip()
    return shots, dna, other


# --- checks ------------------------------------------------------------------

class Report:
    def __init__(self):
        self.findings = []

    def add(self, level, block, line, message):
        self.findings.append({"level": level, "block": block, "line": line, "message": message})

    def count(self, level):
        return sum(1 for f in self.findings if f["level"] == level)


def strip_quotes(text):
    return QUOTE_RE.sub(" ", text)


def check_mood(report, block, lines):
    """lines: (line_no, text, section). NEGATIVE, MOOD and LOOK sections are exempt."""
    for line_no, raw, section in lines:
        if section in ("NEGATIVE", "MOOD", "LOOK"):
            continue
        text = strip_quotes(raw)
        for word, pat in MOOD_PATTERNS:
            if pat.search(text):
                report.add("WARN", block.name, line_no,
                           'mood/interior word "%s" in a shot line - name the visible mechanism instead' % word)


def check_dialogue_action(report, block, shot):
    full = " ".join(t for _, t in shot["text"])
    quotes = QUOTE_RE.findall(full)
    if not quotes or VO_RE.search(full):
        return
    rest = strip_quotes(full)
    has_action = any(p.search(rest) for p in ACTION_PATTERNS)
    if not has_action:
        return
    if any(p.search(rest) for p in CUE_PATTERNS):
        report.add("NOTE", block.name, shot["line"],
                   "on-camera dialogue and action in one shot (sequenced) - confirm the line is spoken while still")
    else:
        report.add("WARN", block.name, shot["line"],
                   "on-camera dialogue and physical action in the same shot - sequence them (move, stop, speak) "
                   'or label the line "Voiceover, no lip sync"')


def check_camera_first(report, block, shot):
    first = SHOT_RE.sub("", shot["text"][0][1], count=1)
    first = re.sub(r"^\s*[A-Z][A-Z &'/-]{2,}\.\s*", "", first)  # beat label like "HOOK."
    first = re.sub(r"^\s*Cut\.\s*", "", first, flags=re.IGNORECASE)
    words = " ".join(first.split()[:14])
    if words and not any(p.search(words) for p in CAMERA_PATTERNS):
        report.add("NOTE", block.name, shot["line"],
                   "camera first? the shot's opening words don't name a camera setup or move")


def first_difference(a, b):
    wa, wb = a.split(), b.split()
    for i, (x, y) in enumerate(zip(wa, wb)):
        if x != y:
            return i, x, y
    if len(wa) != len(wb):
        i = min(len(wa), len(wb))
        return i, (wa[i] if i < len(wa) else "<end>"), (wb[i] if i < len(wb) else "<end>")
    return None


def validate(text, max_block=30.0, min_shot=2.0, target=(12.0, 20.0), require_dna=True):
    report = Report()
    blocks = split_blocks(text)
    summary = {"blocks": [], "dna_identical": None}
    if not blocks:
        report.add("ERROR", "-", 0, "no content found")
        return report, summary

    dnas = []
    for block in blocks:
        shots, dna, other = analyse_block(block)
        info = {"name": block.name, "line": block.line_no, "shots": len(shots),
                "declared_length": block.duration}

        # timestamps
        if not shots:
            report.add("WARN", block.name, block.line_no, "no timestamped shots found (expected lines like '0-4s:')")
        else:
            if abs(shots[0]["a"]) > 1e-6:
                report.add("ERROR", block.name, shots[0]["line"],
                           "timestamps must restart at 0 inside each block (first shot starts at %s s)" % fmt(shots[0]["a"]))
            for prev, cur in zip(shots, shots[1:]):
                if abs(cur["a"] - prev["b"]) > 1e-6:
                    kind = "gap" if cur["a"] > prev["b"] else "overlap"
                    report.add("ERROR", block.name, cur["line"],
                               "%s between shots: previous ends at %s s, this starts at %s s"
                               % (kind, fmt(prev["b"]), fmt(cur["a"])))
            for shot in shots:
                length = shot["b"] - shot["a"]
                if length <= 0:
                    report.add("ERROR", block.name, shot["line"], "shot ends before it starts")
                    continue
                if length < min_shot - 1e-6:
                    label = " ".join(t for _, t in shot["text"])
                    if re.search(r"montage", label, re.IGNORECASE):
                        report.add("NOTE", block.name, shot["line"],
                                   "%s s segment labelled MONTAGE - allowed, keep each cut readable" % fmt(length))
                    else:
                        report.add("WARN", block.name, shot["line"],
                                   "shot is %s s - under %s s rarely renders cleanly; merge or extend"
                                   % (fmt(length), fmt(min_shot)))
                check_dialogue_action(report, block, shot)
                check_camera_first(report, block, shot)

            total = shots[-1]["b"] - shots[0]["a"]
            summed = sum(max(0.0, s["b"] - s["a"]) for s in shots)
            info["shot_total"] = summed
            length = block.duration if block.duration is not None else total
            if block.duration is not None and abs(summed - block.duration) > 1e-6:
                report.add("ERROR", block.name, block.line_no,
                           "shot durations total %s s but the block header says %s s"
                           % (fmt(summed), fmt(block.duration)))
            if length > max_block + 1e-6:
                report.add("ERROR", block.name, block.line_no,
                           "block is %s s - maximum is %s s; split at a story beat" % (fmt(length), fmt(max_block)))
            elif not (target[0] - 1e-6 <= length <= target[1] + 1e-6):
                report.add("NOTE", block.name, block.line_no,
                           "block is %s s - target is %s-%s s" % (fmt(length), fmt(target[0]), fmt(target[1])))

        # mood words in shot lines and persistent lines (not Style DNA / NEGATIVE / MOOD)
        shot_lines = [l for s in shots for l in s["text"]]
        check_mood(report, block, [(n, t, "SHOT") for n, t in shot_lines] + other)

        # @Image declarations vs use
        declared = {int(m.group(1)) for _, t, _ in other for m in [IMAGE_DECL_RE.match(t)] if m}
        used = {}
        for line_no, t in shot_lines:
            for m in IMAGE_USE_RE.finditer(t):
                used.setdefault(int(m.group(1)), line_no)
        if used and not declared:
            report.add("WARN", block.name, min(used.values()),
                       "@Image slots are used but none are declared at the top of the block")
        elif declared:
            for n, line_no in sorted(used.items()):
                if n not in declared:
                    report.add("WARN", block.name, line_no,
                               "@Image%d is used in a shot but not declared at the top of the block" % n)

        # Style DNA
        if not dna:
            if require_dna:
                report.add("ERROR", block.name, block.line_no, 'Style DNA missing (expected a "Style DNA:" section at the end)')
        else:
            dnas.append((block, dna))
        summary["blocks"].append(info)

    if len(dnas) >= 2:
        base_block, base = dnas[0]
        base_norm = " ".join(base.split())
        identical = True
        for block, dna in dnas[1:]:
            norm = " ".join(dna.split())
            if norm != base_norm:
                identical = False
                diff = first_difference(base_norm, norm)
                where = ""
                if diff:
                    i, x, y = diff
                    where = ' (first difference at word %d: "%s" vs "%s")' % (i + 1, x, y)
                report.add("ERROR", block.name, block.line_no,
                           "Style DNA differs from Block %s%s - paste it byte-identical" % (base_block.name, where))
            elif dna != base:
                report.add("NOTE", block.name, block.line_no,
                           "Style DNA matches Block %s except line wrapping/whitespace" % base_block.name)
        summary["dna_identical"] = identical
    elif len(dnas) == 1:
        summary["dna_identical"] = True
    return report, summary


# --- output ------------------------------------------------------------------

def render(report, summary):
    out = []
    nb = len(summary["blocks"])
    ns = sum(b["shots"] for b in summary["blocks"])
    out.append("validate_blocks: %d block(s), %d shot(s)" % (nb, ns))
    for b in summary["blocks"]:
        length = b.get("declared_length")
        head = "Block %s" % b["name"]
        if length is not None:
            head += " (%s s)" % fmt(length)
        head += ": %d shots" % b["shots"]
        if "shot_total" in b:
            head += ", shots total %s s" % fmt(b["shot_total"])
        out.append(head)
        for f in sorted((f for f in report.findings if f["block"] == b["name"]), key=lambda f: f["line"]):
            if True:
                out.append("  %-5s line %s: %s" % (f["level"], f["line"], f["message"]))
    if summary["dna_identical"] is True and nb > 1:
        out.append("Style DNA: identical across blocks - OK")
    out.append("Result: %d error(s), %d warning(s), %d note(s)"
               % (report.count("ERROR"), report.count("WARN"), report.count("NOTE")))
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Validate AI-video block prompts.")
    ap.add_argument("file", help="file with block prompts, or - for stdin")
    ap.add_argument("--max-block", type=float, default=30.0, help="maximum block length in seconds (default 30)")
    ap.add_argument("--min-shot", type=float, default=2.0, help="minimum segment length in seconds (default 2)")
    ap.add_argument("--no-dna", action="store_true", help="do not require a Style DNA section")
    ap.add_argument("--json", action="store_true", help="print JSON instead of text")
    ap.add_argument("--strict", action="store_true", help="exit 1 on warnings too")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")  # never crash on a console that can't print a character

    if args.file == "-":
        text = sys.stdin.read()
    else:
        with open(args.file, encoding="utf-8") as fh:
            text = fh.read()

    report, summary = validate(text, max_block=args.max_block, min_shot=args.min_shot,
                               require_dna=not args.no_dna)
    if args.json:
        print(json.dumps({"summary": summary, "findings": report.findings}, indent=2))
    else:
        print(render(report, summary))
    failed = report.count("ERROR") > 0 or (args.strict and report.count("WARN") > 0)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
