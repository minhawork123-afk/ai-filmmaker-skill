# Playbook — UGC / AI Persona

For creator-style content: an AI persona talking to camera, product reviews, testimonials, "day in my life", and AI influencer posts. Usually 9:16, 15–60 s.

**The one truth:** UGC works when it looks like a real person filmed it themselves and didn't try too hard. Every polished choice (smooth camera, perfect light, bright delivery, music) signals "ad" and costs credibility.

## Brief extras (ask only what changes decisions)

- **Platform and length**: TikTok, Reels or Shorts; 15/30/45/60 s. Default: 9:16, 30 s = 2 × 15 s blocks [Tested].
- **Persona source**: four real photos of one person, or a written description [Tested: both routes]. Default: written description of an original person.
- **Persona**: name, age, niche, energy (low and dry / warm and chatty / deadpan / enthusiastic), one distinguishing feature, skin with real texture.
- **Product** (if any): an invented brand name (no real brands) [Tested], what it looks like (colour, shape, packaging, label), what it does, and **one honest caveat**.
- **Environment**: location, time of day, the light feel (warm tungsten against cold window, hard daylight, soft overcast), and one specific lived-in detail.
- **Camera feel**: phone handheld, self-filmed / propped phone / a mix. Never tripod-smooth [Tested].
- **Sound**: voice character; music none (recommended) or subtle; the key sounds (scoop on plastic, zip, lid twist).

## Script structure [Tested]

1. **Skeptical opener.** Not "hey guys". A real opinion or a tension.
2. **One specific, concrete detail.** Name the exact thing, not "omg I love it".
3. **One honest caveat.** Something that isn't perfect.
4. **A verdict that sounds considered.** Understated, specific.

```text
WEAK    "Hey guys! This serum is literally amazing, you NEED it!"
STRONG  "I've returned four serums this year." [beat] "This one I finished."
WHY     A skeptical opener earns attention; a specific claim earns belief.
```

```text
WEAK    "It's perfect, no downsides."
STRONG  "The pump clogs if you don't wipe it." [half beat] "So I wipe it."
WHY     A real caveat makes the praise credible.
```

Endings [Tested]: cut hard, mid-movement (a hand reaching to stop the recording, cut before it arrives). No outro, no sign-off, no logo card, no call to action in-generation. Add any CTA or end card in the edit if the client needs one.

## Performance [Tested]

- Low energy, faintly tired, underselling. She talks to the phone the way she'd talk to a friend.
- No enthusiasm, no smiling at the lens, no influencer energy. The more understated, the more credible.
- Leave real silence between lines.
- On camera, she speaks or she moves, never both. Voiceover may play over hands-only action shots, labelled "Voiceover, no lip sync".

```text
WEAK    She excitedly holds up the jar and talks about it while walking.
STRONG  She sets the jar down and stops. Looks at the lens. "Week three." Beat.
WHY     Stillness before the line keeps lip-sync clean and reads unrehearsed.
```

## Camera [Tested]

- Every frame is filmed on a phone: held at arm's length (selfie), or propped on a counter, shelf, bench or floor.
- Genuine handheld feel: natural hand tremor, small organic drifts, slightly crooked horizons. Propped shots are static but noticeably crooked.
- Autofocus hunts once and resettles in the first two seconds.
- Never a tripod, never a gimbal, never slow motion.
- Hands-only inserts (no face in frame) are good for product action and for voiceover.
- Shots can be "poorly framed" on purpose: uncomfortably close, low and wide from a propped phone.

## Look

Pick one and lock it as the Style DNA (`style-dna-library.md`):
- **Raw phone UGC** [Tested]: smartphone HDR, mild over-sharpening, luminance noise in dim areas, slight rolling shutter, clipped highlights near windows, flat and ungraded, no grain, no halation. Use it for reviews, ads and anything that must feel self-filmed.
- **Polished creator** [Tested]: Sony A7S III + 35mm prime, warm shadows and cool midtones, Kodak Vision3 250D character, subtle grain, halation. Use it for aspirational lifestyle content.

Lighting stays practical [Tested]: a real window, a real lamp, under-cabinet strips. Mismatched colour temperatures (warm tungsten against a cold blue window) read as real rooms. A strong window can act as the key light: "the cinematography is real, it just looks like someone propped their phone well".

One accent colour [Tested]: let one wardrobe item be the only saturated colour in a neutral or charcoal space. It guides the eye without "grading".

## Sound [Tested]

- No music. UGC authenticity lives in silence and room tone, and music signals "ad".
- Real room tone, plus the specific sounds of the action (the scoop against plastic, the shaker lid, the bag zip, distant plates, a fan, footsteps).
- Phone-mic character: slightly hot and a little clipped, as from a phone mic in a reverberant room.
- Voice spec, always included: *natural, warm, human [female/male] voice, casual conversational cadence, real pitch variation, small natural imperfections, one slightly swallowed word. Must sound like an actual person recording themselves — NOT synthetic, NOT robotic, NOT bright, NOT an ad read.*

## References and blocks

- @Image plan [Tested]: persona sheet → product reference(s) → location plate(s) → last frame. Give the product its own reference so close-ups match it instead of reinventing it.
- Multiple locations in one continuous story work [Tested]. Give each its own plate. Two plates of the same space (a wide arrival plate and a tighter filming-corner plate) help when the persona moves within it.
- Wardrobe and condition can progress across blocks, for example jacket on → jacket off, or dry and composed → flushed with sweat at the hairline [Tested]. State the starting state at the top of each block, and say what must NOT appear ("the jacket is already off and must not appear").
- End each block on a described frame ("END ON THIS FRAME — [exact pose, position in frame, wardrobe state, light]") so the last-frame handoff is clean [Tested].
- Use the UGC block header (CAMERA / PACING / PERFORMANCE / VOICE / AUDIO / NEGATIVE + Style DNA) from `translation/video-prompts.md`.

## UGC negatives [Tested]

Add to every block's NEGATIVE line, adapted to the project:

> No identity drift from the persona sheet. No composite, averaged or generic face. No CGI-smooth, waxy or airbrushed skin. No beauty filter. No tripod or gimbal smoothness. No slow motion. No film grain, halation or cinematic grade (phone look). No music. No on-screen text, captions or graphics. No robotic voice. No dialogue overlapping with action. No enthusiasm. No mirror posing, no body-checking, no physique framing, no sexualised angles, no before-and-after comparison. No real-world brand logos. No other people. No watermark.

## Extra quality-gate checks for UGC

- [ ] The opener isn't a greeting, and the script has a concrete detail and a real caveat.
- [ ] Every shot is plausible as phone footage the persona shot themselves.
- [ ] No music, plus a voice spec in every block, identical across blocks.
- [ ] The product is an invented brand, and its label instructions match the product reference.
- [ ] The ending is a hard cut, with no outro or logo card in-generation.
