# Website Abandoned, Email 2: prompturi imagini

Autor: UI Designer, 13.10.2026. **Nu s-au generat încă** (fără apel Higgsfield în acest pas).
Setări pentru toate: Higgsfield, model `gpt_image_2_5`, calitate `high`, rezoluție `2K`, fundal opac.
Fișierele se pun în `images/` cu numele exacte de mai jos; `build.py` le decupează pătrat 476 x 476 (afișat 238 x 238), cu colțuri sus rotunjite și margine ruptă jos (ca în Email 1). Toate sunt **foto completă** (nu decupaj pe alb).

| Fișier | Aspect | Tip | Ce arată | Unde |
|---|---|---|---|---|
| `reteta1-clatite.png` | 1:1 | foto completă | clătite împăturite „plic” (pătrate), 4 pe o farfurie albă, zmeură proaspătă și o linguriță de miere | S2, card 1 (stânga) |
| `reteta2-cookies.png` | 1:1 | foto completă | 5 cookies întregi, ușor suprapuse, bucăți mari de ciocolată neagră, 30-35° | S2, card 2 (dreapta) |
| `sezon-gingerbread.png` | 1:1 | foto completă | teanc scurt de pancakes, zahăr pudră fin, 2 batoane de scorțișoară alături | doar schimbul de sezon, card 1 (1 nov - 31 dec) |

## Verificare față de emailurile anterioare (toate `image-prompts.md` din `emails/`)
- **Clătite** folosite: triunghiuri cu gem (W1), sferturi lângă pancakes (W2), platou cu clătite rulate de sus (NC1 `img5-clatite`), rulate cu cremă de ciocolată pe farfurie neagră (C1), teanc plat cu zahăr pudră (Browse 1), sferturi cu lămâie și zahăr (Website 1). **Nou aici:** pliul „plic” (pătrat), cu zmeură și miere, la 45°. Fără rulouri, fără triunghiuri, fără lămâie.
- **Cookies** folosite: 3 fursecuri pe alb, unul rupt cu ciocolată topită (C2). **Nou aici:** 5 cookies întregi, niciunul rupt, pe față de masă din in, suprapuse (strategie, secțiunea 5).
- **Gingerbread**: nefolosit; minimal, fără sirop, fructe sau biscuiți în formă de om (rețeta e nepublicată).
- Suprafața (in deschis) și lumina sunt cele din Website 1, ca flow-ul să se citească unitar.

## reteta1-clatite.png (1:1)
Professional food photography, square 1:1 frame, camera at 45 degrees. On a light natural linen tablecloth in warm off-white, a round plain white ceramic plate with four thin golden homemade crepes, each folded into a neat square envelope (folded in half, then in half again, into a square pocket shape), overlapping slightly in a row. A small handful of fresh whole raspberries scattered on and next to the crepes, a thin glossy drizzle of honey over the top crepe, a small wooden honey dipper resting on the cloth beside the plate. Soft natural daylight from the left, gentle shadows, shallow depth of field, appetizing, homemade family breakfast feel. Food only: no packaging, no text, no logos, no people, no hands. No rolled crepes, no triangles, no lemon, no pancakes stack.

## reteta2-cookies.png (1:1)
Professional food photography, square 1:1 frame, camera at 30-35 degrees. On a light natural linen tablecloth in warm off-white, five thick homemade cookies with large visible chunks of dark chocolate, golden brown with crisp edges and soft centres, all whole (none broken or bitten), arranged in a loose overlapping stack of three with two more leaning against it. A few loose dark chocolate chunks on the cloth. Soft natural daylight from the left, gentle shadows, shallow depth of field. Food only: no packaging, no plate, no text, no logos, no people, no hands, no milk glass.

## sezon-gingerbread.png (1:1)
Professional food photography, square 1:1 frame, camera at 30 degrees. On a light natural linen tablecloth in warm off-white, a short stack of four fluffy pancakes with a slightly warmer, spiced golden-brown colour, on a plain white ceramic plate, dusted with a fine layer of powdered sugar like light snow. Two cinnamon sticks lying on the cloth next to the plate. Soft natural daylight, gentle shadows, cosy winter feel. Food only: no syrup, no fruit, no gingerbread-man biscuits, no packaging, no text, no logos, no people, no hands.

## Checklist după generare
- [ ] Clătitele sunt pliate pătrat, nu rulate sau în triunghi; zmeura și mierea se văd.
- [ ] Cookies întregi, niciunul rupt; ciocolata neagră se vede clar.
- [ ] Subiectul e centrat (build-ul face crop pătrat central; jos ~5% se pierde în marginea ruptă).
- [ ] Fără text, ambalaje, mâini.
- [ ] Rulat `.venv/bin/python build.py --preview` și verificat alt-ul (copy.md, secțiunea 4) față de ce se vede.
