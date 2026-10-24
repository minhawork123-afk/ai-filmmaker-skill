# Model — Nano Banana Pro (images)

Google's image model (Gemini 3 Pro Image), used in this workflow for every reference image: portraits, character sheets, product references and location plates. **[Tested]** marks what real productions proved; **[General best practice]** marks public information or general experience.

## Order of operations — never skip a step [Tested]

1. **Portrait** (4:5). Review and fix the face. Don't move on until the face is right.
2. **Three-panel character sheet** (16:9), generated with the approved portrait attached as a reference. Review identity consistency across the panels.
3. **Skin realism pass** (an edit on the approved sheet), only if the skin looks smooth, waxy or airbrushed.
4. **Product reference(s)** (16:9) and **location plates** (16:9). Review the lighting and key elements.
5. **Save** every approved image with a clear name: `portrait-[name].png`, `sheet-[name].png`, `product-[name].png`, `plate-[place].png`.

## Aspect ratios [Tested]

| Image | Ratio |
|---|---|
| Portrait | 4:5 |
| Character sheet | 16:9 |
| Location plate | 16:9 (also used for vertical 9:16 projects) |
| Product reference | 16:9 |

## What works [Tested]

- Real camera language in image prompts: "Shot on ARRI Alexa 35, 85mm prime lens, soft even studio lighting from a large softbox key at 45 degrees with gentle fill".
- A plain mid-grey seamless backdrop for invented characters, and pure white seamless for real-photo identity sheets.
- "Visible skin texture and pores, no retouching, fine film grain" plus a NEGATIVE line against airbrushed, beauty-filter or CGI skin.
- Attaching the approved portrait when generating the sheet, so the face carries over.
- Follow-up edits on an approved image ("Take this exact image and … keep the same identity, pose, outfit, panel layout, background, and lighting exactly as shown").
- A short name label on the sheet, when requested, as one clean sans-serif line plus a smaller age line.
- Location plates with every key object placed by frame position, and named, physically motivated light.

## Watch for [Tested]

- **Too-perfect skin**: run the skin realism pass.
- **A second face sneaking into the sheet**, or the headless centre panel getting a head: regenerate, or switch to the alternative (generate the full-length panels as separate images).
- **Identity drift between panels**: re-attach the portrait and repeat "match the attached approved portrait exactly".

## Public information, not tested here [General best practice]

- Public reports say Nano Banana Pro accepts up to 14 reference images and outputs at 1K, 2K or 4K. Lists of supported aspect ratios vary by platform.
- **Nano Banana 2** (Gemini 3.1 Flash Image, released February 2026) is a newer, faster sibling. This workflow hasn't tested it. If the user prefers it, use the same prompts and review the results with the same checklist.
- Text rendering is generally strong for image models of this class, but keep label text short and check the spelling on every product reference.

## Never claim

- A specific reference-image limit or resolution on the user's platform. Ask, or label it as a public report.
- That an image prompt guarantees identity. Always tell the user what to check before approving.
