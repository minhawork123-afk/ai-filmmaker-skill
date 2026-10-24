# Playbook — Product Commercial

For spots where the product is the hero: car films, tech, beauty, food and drink, fashion accessories, packaged goods. 6–60 s, any aspect ratio.

**The one truth:** the product must look exactly like itself in every frame. Identity lock matters as much for a bottle or a car as for a face, and labels and logos are where AI video breaks first.

What is tested here: the pipeline (brief → script → character sheets → location plates → Seedance 2.5 → After Effects, used on a car concept film), the product reference image as its own @Image slot with "Match exactly", and the clean industrial Style DNA. Everything else in this file is **[General best practice]**.

## Brief extras (ask only what changes decisions)

- **The product**: name, shape, colour, material and finish (matte, gloss, brushed metal, glass), label and logo text (exact wording), size cue. Real product photos if available.
- **The single message**: what the viewer should believe after watching (fast, premium, refreshing, durable). Express it as a visual proof, not a slogan.
- **People?** None, hands only, or a talent with a character sheet.
- **Where it lives**: a studio void, a lifestyle setting, or an environment that demonstrates the claim (a road, a kitchen, the rain).
- **Deliverables**: aspect ratios, length, and whether there's an end card or packshot (added in the edit).

## Structure [General best practice]

| Length | Beats |
|---|---|
| 6 s | Hero reveal → payoff detail (one block) |
| 15 s | Desire/problem → product enters → proof detail → hero shot |
| 30 s | World → tension or need → product in use → 2–3 proof details → hero → (end card in edit) |

```text
WEAK    The bottle looks refreshing and premium.
STRONG  Macro: condensation beads run down the glass shoulder; the cap twists, a fine mist escapes into the backlight.
WHY     "Refreshing" becomes cold, wet, released: things a lens can see.
```

## Product identity and labels

- Give each product its own reference image: a clean product reference generated first (pattern in `translation/image-prompts.md`), or the user's real photos [Tested: product as its own @Image].
- In every block: `@Image2 — the [product]. Match exactly: [shape, colour, finish, label wording].` [Tested]
- **Label strategy** [General best practice]: keep label text short and simple on the reference. In motion, frame labels facing camera and steady, or slightly soft in the background. Avoid fast rotation, extreme angles and hands covering or bending the label, because those are the moments text warps. Put legible brand text, prices and claims in the edit as graphics, not in generation.
- An unbranded or invented brand is the default. Never generate real brand logos unless the user owns or is authorised to use them.

## Look and light [General best practice unless labelled]

- Start from **Clean industrial** [Tested] in `style-dna-library.md` for cars, tech and anything metal. Adapt to **Luxury product macro** for beauty and jewellery, or **Sunlit lifestyle** for food and drink.
- Light by material (`craft/lighting.md`):
  - **Metal and paint**: large soft sources and long highlights, with dark flags for definition and reflection control.
  - **Glass and liquid**: backlight or edge light so the liquid glows; rim to separate it from the background.
  - **Matte packaging**: a soft key at 45° and a gentle fill, keeping texture visible.
  - **Skin and cosmetics**: soft frontal key, specular highlights kept small.
- Camera language: slow dolly and slider moves, orbit, macro inserts, low tracking shots for vehicles, locked-off hero frames. Product films usually want smooth, deliberate movement (the opposite of UGC).

## Cars specifically

- Lock the car with its own reference sheet (front three-quarter, side, rear three-quarter) and treat it as a character.
- Plates: one per road or location, without the car, with the light direction stated.
- Motion: low tracking alongside, a rolling shot from a car ahead, a static wide as it passes, detail inserts (wheel, light signature, badge kept soft). State the direction of travel as a hard fact: "the car travels LEFT to RIGHT across frame".
- Reflections reveal environment errors, so match the plate's sky and light in the reflection description.

## People with products

- Hands-only inserts need hand continuity: same skin tone, nails, rings, sleeve. State it in each block.
- Talent follows `craft/directing-performance.md`, and the product handling is described as physical mechanics ("thumb slides the cap off, it clicks once").

## Edit

Packshots, end cards, legal lines and logos go in the edit [General best practice]. Use one grade layer [Tested], keep sound designed around the product (cap click, engine note, pour), and only use music if the brand calls for it.

## Extra quality-gate checks for product work

- [ ] The product reference exists and is declared in every block where the product appears, with "Match exactly".
- [ ] No shot asks for readable label text in fast motion, at extreme angles or partly covered.
- [ ] The claim is proven visually (texture, behaviour, result), not stated in words.
- [ ] Direction of travel or orientation is stated as a hard fact.
- [ ] No real brand logos unless the user confirmed they have the rights.
