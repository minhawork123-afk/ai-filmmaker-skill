"""Tests for skills/ai-filmmaker/scripts/validate_blocks.py (stdlib unittest).

Run: python3 -m unittest discover -s tests
"""

import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "ai-filmmaker" / "scripts" / "validate_blocks.py"
spec = importlib.util.spec_from_file_location("validate_blocks", SCRIPT)
vb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vb)

DNA = """Style DNA:
Shot on ARRI Alexa 35 with spherical prime lenses. Locked-off. Photoreal live-action
cinematography, no stylisation. Single tungsten practical key. 24fps, 180-degree shutter,
fine 35mm grain. Quiet, wrong, dreadful."""

GOOD = """BLOCK 1 — 0:00–0:15 — THE CALL

@Image1 = Ana, grey cardigan
@Image2 = hallway at night

0–4s: Locked-off wide shot, 24mm. Ana @Image1 stands at the phone table.
Audio: fridge hum.

4–7s: Cut. Slow push-in, 50mm, MCU. Ana @Image1 lifts the handset, then stops. Beat. She says, flat: "Hello?"
Audio: dial tone.

7–10s: Cut. Insert, macro. Her thumb presses the cradle twice.
Audio: two clicks.

10–15s: Cut. Close-up, 85mm. Ana @Image1 holds still, eyes on the doorway camera-RIGHT.
Audio: silence.

NEGATIVE: no cinematic grade drift, no slow motion.

{dna}

BLOCK 2 — 0:15–0:27 — THE DOORWAY

@Image1 = Ana
@Image3 = final frame of Block 1

0–5s: Handheld MCU, 35mm. Ana @Image1 walks toward the doorway.
Audio: floorboard creak.

5–8s: Cut. POV wide, 24mm. The dark doorway.
Audio: nothing.

8–12s: Cut. Close-up. Ana @Image1 breathes out.
Audio: one breath.

{dna}
""".format(dna=DNA)


def levels(report, level):
    return [f for f in report.findings if f["level"] == level]


def messages(report, level=None):
    return " | ".join(f["message"] for f in report.findings if level is None or f["level"] == level)


class GoodBlocks(unittest.TestCase):
    def test_clean_blocks_pass(self):
        report, summary = vb.validate(GOOD)
        self.assertEqual(levels(report, "ERROR"), [], messages(report))
        self.assertEqual(levels(report, "WARN"), [], messages(report))
        self.assertEqual(len(summary["blocks"]), 2)
        self.assertTrue(summary["dna_identical"])

    def test_header_duration_parsed(self):
        blocks = vb.split_blocks(GOOD)
        self.assertEqual([b.duration for b in blocks], [15.0, 12.0])

    def test_rewrapped_dna_is_a_note_not_error(self):
        text = GOOD.replace("Locked-off. Photoreal live-action\ncinematography", "Locked-off.\nPhotoreal live-action cinematography", 1)
        report, _ = vb.validate(text)
        self.assertEqual(levels(report, "ERROR"), [], messages(report))
        self.assertIn("line wrapping", messages(report, "NOTE"))


class TimingErrors(unittest.TestCase):
    def test_must_start_at_zero(self):
        text = "BLOCK 1 — 0:00–0:10\n1–5s: Wide shot. x\n5–10s: Close-up. y\n" + DNA
        report, _ = vb.validate(text)
        self.assertIn("restart at 0", messages(report, "ERROR"))

    def test_gap_and_overlap(self):
        text = "BLOCK 1\n0–4s: Wide shot. a\n5–8s: Close-up. b\n7–10s: Insert. c\n" + DNA
        report, _ = vb.validate(text)
        errs = messages(report, "ERROR")
        self.assertIn("gap between shots", errs)
        self.assertIn("overlap between shots", errs)

    def test_total_must_match_header(self):
        text = "BLOCK 1 — 0–15s — X\n0–4s: Wide shot. a\n4–12s: Close-up. b\n" + DNA
        report, _ = vb.validate(text)
        self.assertIn("total 12 s but the block header says 15 s", messages(report, "ERROR"))

    def test_block_over_30s(self):
        text = "BLOCK 1 — 0:00–0:32\n0–16s: Wide shot. a\n16–32s: Close-up. b\n" + DNA
        report, _ = vb.validate(text)
        self.assertIn("maximum is 30 s", messages(report, "ERROR"))

    def test_short_shot_warns_unless_montage(self):
        text = "BLOCK 1 — 0–6s\n0–1.5s: Wide shot. a\n1.5–6s: Close-up. b\n" + DNA
        report, _ = vb.validate(text)
        self.assertIn("under 2 s", messages(report, "WARN"))
        text = "BLOCK 1 — 0–6s\n0–1.5s: MONTAGE, two quick cuts: (a) x (b) y\n1.5–6s: Close-up. b\n" + DNA
        report, _ = vb.validate(text)
        self.assertNotIn("under 2 s", messages(report, "WARN"))
        self.assertIn("MONTAGE", messages(report, "NOTE"))

    def test_timestamp_formats(self):
        for a, b in [("0:00–0:05 ·", "0:05–0:09.5 ·"), ("0-5s:", "5-9.5s:"), ("[0–5s]", "[5–9.5s]")]:
            text = "BLOCK 1 — 0–9.5s\n%s Wide shot. a\n%s Close-up. b\n%s" % (a, b, DNA)
            report, summary = vb.validate(text)
            self.assertEqual(summary["blocks"][0]["shots"], 2, a)
            self.assertEqual(levels(report, "ERROR"), [], (a, messages(report)))


class StyleDNA(unittest.TestCase):
    def test_missing_dna(self):
        report, _ = vb.validate("BLOCK 1 — 0–4s\n0–4s: Wide shot. a\n")
        self.assertIn("Style DNA missing", messages(report, "ERROR"))

    def test_no_dna_flag(self):
        report, _ = vb.validate("BLOCK 1 — 0–4s\n0–4s: Wide shot. a\n", require_dna=False)
        self.assertNotIn("Style DNA missing", messages(report))

    def test_reworded_dna_is_error(self):
        second = DNA.replace("fine 35mm grain", "fine 35mm texture")
        text = GOOD.rsplit(DNA, 1)[0] + second + "\n"
        report, summary = vb.validate(text)
        self.assertIn('"grain." vs "texture."', messages(report, "ERROR"))
        self.assertFalse(summary["dna_identical"])


class LanguageChecks(unittest.TestCase):
    def test_mood_words_flagged_in_shots_only(self):
        text = ("BLOCK 1 — 0–8s\n0–4s: Wide shot. She looks nervous in a cinematic room.\n"
                "Audio: ambient sound.\n4–8s: Close-up. Her jaw tightens.\n"
                "NEGATIVE: no cinematic grade, nothing epic.\n" + DNA.replace("dreadful", "moody"))
        report, _ = vb.validate(text)
        warns = messages(report, "WARN")
        for word in ("nervous", "cinematic", "ambient sound"):
            self.assertIn('"%s"' % word, warns)
        self.assertNotIn('"epic"', warns)   # NEGATIVE line exempt
        self.assertNotIn('"moody"', warns)  # Style DNA exempt

    def test_mood_word_inside_dialogue_is_ignored(self):
        text = 'BLOCK 1 — 0–4s\n0–4s: Close-up, static. She says, flat: "I am not happy."\n' + DNA
        report, _ = vb.validate(text)
        self.assertNotIn('"happy"', messages(report))

    def test_photoreal_is_not_flagged(self):
        text = "BLOCK 1 — 0–4s\n0–4s: Wide shot, photorealistic. A street.\n" + DNA
        report, _ = vb.validate(text)
        self.assertNotIn("realistic", messages(report, "WARN"))

    def test_dialogue_during_action_warns(self):
        text = 'BLOCK 1 — 0–4s\n0–4s: Close-up. She walks to the window saying, "I never wanted this."\n' + DNA
        report, _ = vb.validate(text)
        self.assertIn("same shot", messages(report, "WARN"))

    def test_voiceover_over_action_is_allowed(self):
        text = ('BLOCK 1 — 0–4s\n0–4s: Insert, hands only. She scoops powder into the shaker. '
                'Voiceover, no lip sync: "Thirty grams."\n' + DNA)
        report, _ = vb.validate(text)
        self.assertNotIn("same shot", messages(report))

    def test_sequenced_dialogue_is_note(self):
        text = 'BLOCK 1 — 0–4s\n0–4s: MCU. She walks to the window and stops. Beat. She says: "No."\n' + DNA
        report, _ = vb.validate(text)
        self.assertNotIn("same shot", messages(report, "WARN"))
        self.assertIn("sequenced", messages(report, "NOTE"))

    def test_undeclared_image_slot(self):
        text = "BLOCK 1 — 0–4s\n@Image1 = Ana\n0–4s: Wide shot. @Image1 and @Image2 stand.\n" + DNA
        report, _ = vb.validate(text)
        self.assertIn("@Image2 is used", messages(report, "WARN"))


class Cli(unittest.TestCase):
    def test_exit_codes(self):
        import tempfile, os
        with tempfile.TemporaryDirectory() as d:
            good = os.path.join(d, "good.md")
            bad = os.path.join(d, "bad.md")
            with open(good, "w", encoding="utf-8") as fh:
                fh.write(GOOD)
            with open(bad, "w", encoding="utf-8") as fh:
                fh.write("BLOCK 1 — 0–10s\n0–4s: Wide shot. a\n")
            self.assertEqual(vb.main([good]), 0)
            self.assertEqual(vb.main([bad]), 1)
            self.assertEqual(vb.main([good, "--json"]), 0)



class SelfTestFixtures(unittest.TestCase):
    """Block prompts produced while self-testing the skill (UGC, cinematic, music video)
    must stay clean: they are what the skill's own formats should produce."""

    def test_fixtures_are_clean(self):
        fixtures = sorted((ROOT / "tests" / "fixtures").glob("selftest-*.md"))
        self.assertGreaterEqual(len(fixtures), 3)
        for path in fixtures:
            report, summary = vb.validate(path.read_text(encoding="utf-8"))
            bad = [f for f in report.findings if f["level"] in ("ERROR", "WARN")]
            self.assertEqual(bad, [], "%s: %s" % (path.name, bad))
            self.assertTrue(summary["dna_identical"], path.name)


if __name__ == "__main__":
    unittest.main()
