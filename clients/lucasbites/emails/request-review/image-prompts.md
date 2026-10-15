# Prompturi Higgsfield, Request review

Model: **GPT Image 2.5** (`gpt_image_2_5`). Generate direct prin Higgsfield MCP, 14.10.2026. Cost total: 1,25 credite (494,75 -> 493,5), 5 joburi.
Fără ambalaje în nicio imagine, deci nu s-a folosit packshot ca referință.

| Fișier | Job | Aspect | Final |
|---|---|---|---|
| images/hero.png | 9927b20b-c4fb-4636-851d-3b76638cbed6 (v2) | 4:3 (1168x880) | fundal recolorat la #FAA61A exact, recentrat pe 1200x900, margini min. ~9% |
| images/_alt-hero-v1-hand.png | 630a93e7-9751-4462-8420-092d0fb6d6cf (v1, respinsă) | 4:3 | mâna/brațul tăiate de marginea de sus |
| images/social-1.png | f5f8ab6c-8a6b-4711-8289-052312d91fec | 1:1 | 800x800 |
| images/social-2.png | 21b229c1-5b4a-4d52-90bc-7af4d637f1bf | 1:1 | 800x800 |
| images/social-3.png | 99f8cd2e-61f8-4406-9535-cb3703b595fc | 1:1 | 800x800 |

Originalele sunt în `images/_raw/`.

**Post-procesare hero:** modelul a dat fundal #FB9E0E (nu #FAA61A). Pixelii de fundal au fost mutați pe #FAA61A cu tranziție moale (distanță de culoare), apoi subiectul (cu umbra) a fost recentrat pe pânză 1200x900 #FAA61A. Colțurile verificate: 250/166/26.

**Abateri de la cerere:** v1 cu mâna care toarnă a fost respinsă (brațul iese din cadru; o mână vine mereu dintr-o margine). V2: carafa plutește, fără mână. S3: copy.md cere „clătite rulate”, nu waffles (Lucas Bites are mix de clătite, nu de waffles), deci social-2 = clătite.

## hero.png, v2
Vivid appetising commercial food photography, studio cutout style, playful levitation. A round white ceramic plate with a stack of four fluffy golden homemade pancakes, a few fresh blueberries on top and around, a pat of melting butter. A fork rests in the stack having just cut out the first wedge, showing the soft airy crumb. A small glass syrup jug floats in mid-air just above and to the right of the stack, tilted, pouring a glossy ribbon of maple syrup onto the pancakes, syrup dripping down the sides. No hands, no people. Three-quarter view from 30 degrees above. The whole group (plate, fork, floating jug) is compact and centered, occupying only the middle 70 percent of the frame, with an empty margin of at least 14 percent on every side including the top; the jug is fully visible and well below the top edge; nothing touches or is cut off by the image edges. Solid flat seamless background in bright saffron orange exactly #FAA61A filling the entire image edge to edge, no table, no floor, no horizon line, no surface, no gradient, no vignette, only a faint soft contact shadow directly under the plate. Warm soft studio key light from upper left, crisp details, saturated colors. No text, no logos, no packaging.

## hero v1 (respinsă)
Ca v2, dar cu „From upper right, a hand (only the hand and wrist, no face, no person) tilts a small glass jug pouring...” și margine cerută 12%.

## social-1.png (pancakes cu fructe)
Casual smartphone photo shot from directly above, looking like a real home Instagram post: a stack of homemade pancakes on a simple mismatched plate on a light wooden kitchen table, topped with sliced strawberries, blueberries, banana slices and a messy drizzle of honey, a few crumbs and a used fork beside it, a mug of coffee partly in frame at the corner. Natural soft window daylight from the side, slightly imperfect framing, mild phone-camera look, realistic not styled. No people, no faces, no text, no packaging, no logos.

## social-2.png (clătite rulate)
Casual smartphone photo from a slight angle above, looking like a real home Instagram post: thin homemade crepes rolled up on a plain white plate, filled with chocolate hazelnut spread, dusted with powdered sugar, a few raspberries, on a kitchen counter with a light tiled backsplash slightly out of focus. Natural morning daylight from a nearby window, gentle shadows, slightly imperfect composition, authentic phone-camera look. No people, no faces, no text, no packaging, no logos.

## social-3.png (brownie)
Casual smartphone photo shot from directly above, looking like a real home Instagram post: a homemade fudgy chocolate brownie cut into squares in a slightly worn metal baking tray lined with baking paper, crackly shiny top, one square lifted out and placed on a small plate with a scoop of vanilla ice cream, crumbs around, on a light kitchen table with a folded linen towel. Natural soft daylight, realistic home feel, slightly imperfect framing. No people, no faces, no text, no packaging, no logos.
