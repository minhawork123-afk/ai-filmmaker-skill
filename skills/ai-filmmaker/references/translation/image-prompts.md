# Translation — Image Prompts (Reference Images)

Output formats for the Stage 3 reference images: portraits, character sheets, product references and location plates. **You** fill these in for the user's project and deliver each one in its own code block. Never show them blank.

These images exist to **lock** identity and space before any video [Tested]. Every later video prompt says "match @ImageN" instead of re-describing.

## Filling rules (apply to every format)

- **Specific and ordinary beats beautiful.** The more ordinary and precise a face description is, the more real it looks [Tested].
- **Sides are the character's own LEFT/RIGHT**, in capitals. Add the line "Body sides marked LEFT or RIGHT are the character's own left and right, not the viewer's" whenever a side is mentioned.
- **Light names its source** [Tested]. For plates, the light you write becomes the video's light.
- **Always include a realism clause and a camera** [Tested]: a real body and lens, "visible skin texture and pores, no retouching", "NOT a digital render, NOT a 3D visualisation".
- **Original characters**: add "Original character, not resembling any existing person or public figure" unless the user supplied real photos of a person who has consented.
- Remove every `[bracket]`, and delete optional lines that don't apply.
- **Reference sheets always use the studio format** (mid-grey seamless, ARRI Alexa 35, 85mm, softbox), whatever the project's look. Even a phone-shot UGC persona was built from a studio sheet [Tested]. The look comes from the plates and the Style DNA, not the sheet.

```text
WEAK    A beautiful young woman with perfect skin and nice hair.
STRONG  Light olive skin with a warm undertone, slightly uneven; oval face; dark brown almond eyes; thick, slightly unruly brows; faint flush across the nose.
WHY     Ordinary specifics produce a person; "beautiful" produces the model's average face.
```

---

## 1. Portrait — 4:5 [Tested]

Generate this first and get the face exactly right before making the sheet. Label line: `Nano Banana Pro · 4:5 · portrait for [Name] (attach to the sheet prompt next)`

```
Photorealistic character reference photograph. Chest-up portrait of a [AGE]-year-old [woman/man/person] against a plain mid-grey seamless studio backdrop, facing camera straight on.

FACE: [Skin tone and undertone. Face shape and jaw. Eye colour and shape. Nose. Lips. Brows. Any distinctive features, with the side in capitals.]

HAIR: [Colour. Length. Texture. Style. Condition: dry / wet / tied up / messy.]

BUILD: [Visible from the chest up: neck, shoulders, posture.]

WARDROBE: [Top layer visible from the chest up: garment, fabric, colour, condition.]

EXPRESSION: [What a camera sees, e.g. "relaxed, mouth closed, lips resting together, eyes calm and steady into the lens".]

CONDITION: [Clean / wet / wounded / dirty, and exactly where.]

DISTINGUISHING FEATURE: [Tattoo, scar, glasses, earrings, with location; or "None — no tattoos, jewellery or glasses."]

Background: plain mid-grey seamless studio backdrop, completely empty, evenly lit, no texture, no gradient, no shadow cast on the backdrop.

Shot on ARRI Alexa 35, 85mm prime lens, soft even studio lighting from a large softbox key at 45 degrees with gentle fill, no hard shadows, no rim light, neutral white balance, sharp focus throughout, visible skin texture and pores, no retouching, fine film grain. Original character, not resembling any existing person or public figure.

NEGATIVE: no smooth or airbrushed skin, no beauty filter, no CGI look, no gradient background, no heavy makeup, no resemblance to any real person.
```

## 2. Three-panel character sheet — 16:9, headless centre [Tested, primary method]

Attach the approved portrait as a reference. This image becomes the character's @Image slot. Label line: `Nano Banana Pro · 16:9 · attach approved portrait · becomes @Image[N]`

**Why the headless centre panel:** it leaves exactly one face on the sheet. If two full faces appear, the video model averages them into a blurred, unstable identity. One face, used twice, locks the model onto a single identity that holds across blocks [Tested].

```
Photorealistic character reference sheet. Three panels side by side against a plain mid-grey seamless studio backdrop. One continuous background across all three panels. Match the attached approved portrait exactly — same face, same skin, same hair.

LEFT PANEL — chest-up portrait of a [AGE]-year-old [woman/man/person], facing camera straight on, level chin, calm neutral expression, eyes into the lens.
FACE: [paste the portrait's FACE description]
HAIR: [paste the portrait's HAIR description]
WARDROBE (TOP LAYER ONLY): [top garment]

CENTRE PANEL — full-length front view of the same [woman/man/person], framed from the shoulders down so the head is DELIBERATELY CROPPED OUT OF FRAME. This is an intentional headless costume display — the clothing simply stops at the collar line. The omission is deliberate so the model locks onto one single face from the LEFT panel only.
Standing upright and square to camera, weight evenly on both feet, arms hanging relaxed and straight at the sides, nothing crossing the body, hands open and visible.
BUILD: [height and build, head to toe]
WARDROBE, HEAD TO TOE: [top, bottom, footwear, condition]
DISTINGUISHING FEATURES: [tattoos, jewellery, with the side in capitals]

RIGHT PANEL — full-length rear three-quarter view of the same [woman/man/person], seen mostly from behind, HEAD FULLY VISIBLE AND COMPLETE from the top of the skull down to the feet. Hair, skull shape and nape of the neck all in frame. Head turned very slightly so a sliver of cheek or jaw catches in profile.
HAIR FROM BEHIND: [how the hair sits from behind]
WARDROBE FROM BEHIND: [the same outfit from behind, identical colour, fabric and condition]
Same neutral upright posture, arms at sides.

CRITICAL: Only the CENTRE panel is headless. LEFT and RIGHT panels both include the head. This character has a head and face in every shot of the film.

All three panels identically lit and identically scaled. Plain mid-grey seamless studio backdrop, completely empty, evenly lit, no texture, no gradient.

Shot on ARRI Alexa 35, 85mm prime lens, soft even studio lighting from a large softbox key at 45 degrees with gentle fill, no hard shadows, no rim light, neutral white balance, sharp focus throughout, visible skin texture and pores, no retouching, fine film grain. Original character, not resembling any existing person or public figure.

NEGATIVE: no resemblance to any real person or influencer, no identity drift between panels, no smooth or airbrushed or waxy or CGI-looking skin, no beauty filter, no heavy makeup, no arched back or posed stance, no action poses, no hands raised, no crossed arms, no props, no text, no watermark, no branding.
```

Optional name label [Tested]: replace "no text" with *A small, clean white sans-serif label in the top-left corner of the LEFT panel reads "[NAME]", with "AGE [N]" in smaller type beneath it. No other text anywhere on the sheet.*

**Alternative — turnaround plus separate full-length shots [Tested]:** a chest-up turnaround (front / profile / back, one image), with the headless full-length front and the full-length rear three-quarter view generated as **separate** 16:9 images. Use it when the model won't render the headless centre panel correctly in one image. The trade-off: the profile panel adds a second face angle. Keep the front panel as the clear face source, and say so in every block.

## 3. Real person — four-photo identity lock [Tested]

Use this when the user uploads four photos of the same real person (with their consent). The four photos occupy the reference slots during sheet generation only.

```
CRITICAL IDENTITY LOCK: @Image1, @Image2, @Image3, and @Image4 are all photos of the exact same real person. This is not a composite or blended face. They must be immediately and unmistakably recognizable as the specific individual shown — with their exact face shape, exact eye shape and colour, exact nose, exact lips, exact eyebrow shape, exact jawline, exact skin tone, and exact hair colour, texture, and length as shown. Do not average, generalize, beautify, or drift toward a generic model-like face. If any single reference is clearer than the others, prioritize matching that one exactly rather than blending all four into something new.

A four-panel character reference sheet: front / three-quarter / side / face and texture detail.

Wardrobe: [outfit]

Pure white seamless background across all four panels. Soft texture-revealing side-angle lighting. Real skin texture, never airbrushed.

NEGATIVE: no identity drift from the uploaded references under any circumstances, no generic or composite or averaged face, no beautification, no smooth or airbrushed or CGI-looking skin.
```

Note: this route shows four face angles, which is the opposite of the headless-panel logic. It's documented as tested for real people. If identity averages in video, fall back to generating a headless three-panel sheet from the best front photo.

## 4. Skin realism pass [Tested]

Run this as an edit on the approved sheet, only if the skin looks too perfect. Label line: `Nano Banana Pro · edit on the approved sheet · same aspect ratio`

```
Take this exact image and increase skin and overall realism only. Keep the same identity, pose, outfit, panel layout, background, and lighting exactly as shown.

SKIN REALISM: replace any smooth, airbrushed, or beauty-filter skin with genuinely photographed skin texture — real visible pores across the forehead, cheeks and nose, subtle natural uneven tone, faint texture irregularities. The character should still look [attractive / natural / weathered] but through real photographic texture, not a smoothed surface.

NEGATIVE: no smooth, plastic, waxy, glass-smooth, or CGI-rendered skin. No beauty filter. No change to face shape, identity, pose, wardrobe, or background.
```

## 5. Product reference — 16:9 [General best practice]

The tested part is the principle: a product gets its own reference image so close-ups match it instead of reinventing it. The prompt pattern below is derived, not tested. Label line: `Nano Banana Pro · 16:9 · becomes @Image[N] (product)`

```
Photorealistic product reference photograph, 16:9. [PRODUCT] [and ACCESSORY] standing side by side on a pure white seamless background, centred, straight-on front view at product height, label facing camera.

PRODUCT: [exact shape and proportions, size cue, material and finish (matte / gloss / brushed metal / clear plastic), precise colour names, cap or lid, transparent parts and what is visible through them]

LABEL: [exact wording — keep it short], [clean sans-serif wordmark / other style], [colour], [position on the pack]. Lettering crisp, correctly spelled, perfectly flat to the surface.

ACCESSORY: [optional: shaker, case, box, with the same level of detail]

Lighting: large soft overhead and frontal softboxes, even and shadowless except a soft contact shadow beneath each object, true-to-life colour, controlled reflections that never cross the label.

Shot on a medium-format stills camera, 100mm macro lens at f/8, deep focus, everything sharp. This must read as an actual product photograph — NOT a 3D render, NOT a CGI packshot.

NEGATIVE: no extra text, no misspelled or warped lettering, no other logos, no real-world brand marks, no props, no hands, no gradient background, no reflections over the label.
```

Optional extra views [General best practice]: generate the three-quarter view, the back, and a label/texture macro as **separate** images, keeping the front view as the product's main @Image slot. Separate images avoid several tiny labels on one sheet, which is where text warps.

```text
WEAK    A sleek premium protein tub with a cool logo.
STRONG  Matte black cylindrical tub, ribbed black screw lid, single white wordmark "KORE" centred low on the front, nothing else printed.
WHY     Shape, finish, colour and exact text give the model one product to hold.
```

## 6. Location plate — no people [Tested]

One plate per setting. Lock the location before the video so the video model only has to handle performance, not invent a location and its lighting at the same time. Default aspect ratio: 16:9 [Tested, including for 9:16 projects]. Matching the project's aspect ratio is a [General best practice] alternative when exact vertical framing matters. Label line: `Nano Banana Pro · 16:9 · becomes @Image[N] (location)`

```
[Photorealistic cinematic establishing plate / Photorealistic interior photograph / Real phone photo], [wide shot / three-quarter angle]. No people. Empty of people entirely.

SETTING: [type of space, with specific materials and wear]
ERA / STYLE: [contemporary / 1970s / brutalist / cluttered and lived-in]
TIME OF DAY: [pre-dawn / golden hour / overcast noon / late dusk / night]
WEATHER (exterior only): [heavy rain / fog / dry / clear]

KEY ELEMENTS: [every object that must appear, with its frame position — foreground / mid-ground / background, LEFT / centre / RIGHT of frame]

LIGHTING: [the actual physical light source(s): position, colour temperature, quality, and whether the sources disagree in colour]

COLOUR GRADE: [the palette sentence: shadows, midtones, highlights, texture]

CAMERA POSITION: [height and angle, and what it looks at — e.g. "low at hip height, three-quarter angle looking down the length of the floor"]

MOOD: [one line — a coherence check for you; it doesn't instruct the model]

This must read as an actual photograph taken [on a phone in a real space / on a real camera] — NOT a digital render, NOT a 3D visualisation, NOT a video-game environment, NOT an AI-generated look.

Shot on [ARRI Alexa 35 / Sony A7S III / a recent smartphone], [focal length], [deep focus / shallow], [35mm grain / no grain for phone looks], [natural light only / mixed practical sources].

NEGATIVE: no people, no text, no logos, no CGI or 3D render look, no flat or shadowless lighting, [no plants / no clutter unless specified], [anything specific to avoid].
```

```text
WEAK    A gritty laundromat at night with nice lighting.
STRONG  Row of steel washers mid-ground LEFT; orange plastic chairs foreground RIGHT; one flickering fluorescent tube overhead as the only key; wet night street through the window behind.
WHY     Objects with frame positions and a named light become a set the video can return to.
```

**Phone-look plates** [Tested]: say "real phone photo", ask for an under-lit room, mild noise in the shadows and mismatched practical light, and put "no film grain, no halation, no cinematic colour grade, no even or flattering lighting" in the NEGATIVE.

**Two plates for one space** [Tested pattern]: a wide establishing plate for arrivals, and a tighter plate of the exact corner where the action happens.

**One plate per lighting state** [General best practice]: if the same place appears at night and in the morning, or with the lamp on and off, generate a plate for each. Match their camera position and key elements so only the light changes.

## Image-prompt checks

- [ ] Aspect ratio and label line above every code block.
- [ ] The sheet has exactly one full face and states that only the centre panel is headless.
- [ ] Every side is in capitals, with the "character's own left and right" line.
- [ ] Plates contain no people, and every key element has a frame position.
- [ ] A realism clause, a camera body and lens, and a NEGATIVE line in every prompt.
- [ ] No brackets left unfilled.
