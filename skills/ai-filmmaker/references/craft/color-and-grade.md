# Craft — Colour and Grade

Colour is decided twice: in generation, through the Style DNA and the plates, and in the edit, through the grade. Unlabelled content is **[General best practice]**; workflow-proven rules are marked **[Tested]**.

## Name it specifically [Tested]

Not "dark and moody". Name the values: where warm and cold sit (shadows, midtones, highlights), the saturation, the black level, the highlight behaviour, the grain and halation.

```text
WEAK    Dark, moody colour grade.
STRONG  Desaturated teal-green and grey, deep crushed blacks, cold blue-grey ambience.
WHY     Hue, saturation and black level are instructions; "moody" is an adjective.
```

## The palette sentence

Write the grade as one sentence covering four slots:

1. **Shadows**: crushed black · lifted milky black · cold blue shadows · warm amber shadows
2. **Midtones / skin**: natural skin · cool blue-grey midtones · warm golden midtones
3. **Highlights**: controlled highlights that never blow out · clipped highlights near windows (phone) · soft halation around practicals
4. **Saturation and texture**: desaturated · one saturated accent · fine 35mm grain · no grain

Example [Tested, persona Style DNA]: *warm amber shadows, cool blue-grey midtones, controlled highlights that never blow out, Kodak Vision3 250D character, subtle 35mm grain, soft halation around the practical light source.*

## Film stocks as colour tokens

| Token | Read | Status |
|---|---|---|
| Kodak Vision3 250D | daylight stock, balanced, gentle warmth | [Tested] in the persona Style DNA |
| Kodak Vision3 500T | tungsten stock, night, warm practicals, cooler ambient | General best practice |
| Kodak Vision3 50D | fine grain, saturated daylight | General best practice |
| Kodak Portra 400 (stills) | soft pastel skin, warm highlights | General best practice |
| Fuji Eterna (cine) | muted, slightly green-cyan, low contrast | General best practice |
| Kodak Ektachrome | punchy, saturated, slide-film contrast | General best practice |

## Recognisable looks and their mechanics

| Look | Mechanics |
|---|---|
| Bleak naturalism | desaturated teal-green and grey, crushed blacks, cold blue-grey ambience [Tested] |
| Phone-native realism | flat and ungraded, HDR, mild over-sharpening, luminance noise in shadows, clipped highlights [Tested] |
| Steel and graphite (product/car) | desaturated steel and graphite palette, deep blacks, cool blue-grey fill, hard key [Tested] |
| Near-monochrome with a warm pocket | charcoal and graphite with cool highlights on steel, one pocket of warm daylight [Tested, location plate pattern] |
| Warm nostalgia | lifted blacks, golden midtones, soft halation, 16mm grain |
| Night city | sodium-vapour orange against cyan shadows, saturated neon, wet reflections |
| Bleach bypass | low saturation, high contrast, silvery highlights. Grit, war, sci-fi |
| Clean commercial | neutral whites, accurate product colour, gentle contrast, no tint |

Avoid the generic teal-and-orange blockbuster grade unless it's asked for. It's the most "AI default" look, and naming it in a NEGATIVE line can help [Tested: "no cinematic or teal-and-orange grade" for phone looks].

## The one-accent rule [Tested pattern]

Keep the frame neutral or near-monochrome and let one element carry the only real colour, usually a wardrobe item or the product: *"the yellow raincoat is the only real colour in frame"*. It guides the eye and survives across blocks better than a global grade instruction.

## Grain, halation and texture

- Fine 35mm grain [Tested] is the cinematic default; 16mm grain is heavier and more nostalgic.
- Halation (a red-orange glow around bright practicals) reads as film [Tested in the persona Style DNA].
- Phone looks: **no** grain, no halation [Tested]. Put that in the NEGATIVE line, because models add film texture by default.

## Colour in plates vs blocks

- The location plate sets the colour reality. Write the palette into its `COLOUR GRADE:` line [Tested].
- Blocks repeat the palette through the Style DNA, byte-identical [Tested], and can add "Match @Image3's palette exactly" [Tested pattern].

## Grade in the edit [Tested]

- After Effects: apply the grade as a single adjustment layer across all clips.
- Add a subtle lens vignette.
- Add a 35mm grain overlay at 10–15% opacity if the generated grain feels insufficient.
- In CapCut for persona content, keep the grade minimal or flat.

## Colour checks

- [ ] The palette sentence names the shadows, midtones, highlights and texture.
- [ ] The plate's colour line and the Style DNA agree.
- [ ] Phone looks explicitly exclude grain, halation and cinematic grades.
- [ ] There's at most one saturated accent, if the look calls for one.
