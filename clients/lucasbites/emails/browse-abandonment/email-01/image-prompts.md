# Prompturi Higgsfield, Browse Abandonment Email 1

**Generate 13.10.2026:** imaginile cu `gpt_image_2_5` (quality high, 2K, background opaque), video-ul cu `seedance_2_5` (omni_reference, start_image = end_image = rec2-pizza, 4 s, 720p, fără audio). GIF-ul se face local cu ffmpeg din `.venv` (`pip install imageio-ffmpeg`), fără instalare pe sistem.

Imagini: model de imagine **GPT Image** (același ca în welcome 2-3 și checkout-started 1-2), calitate **High**, rezoluție **2K**, aspect ratio din tabel. Video: model video ales în Higgsfield (image-to-video, pornind de la imaginea rec2).
Salvează în `clients/lucasbites/emails/browse-abandonment/email-01/images/` cu exact numele de mai jos, apoi rulează `.venv/bin/python build.py --preview`.

**Diferență față de restul seriei:** cele 3 rețete NU sunt decupaje. Sunt fotografii complete, încadrate de `build.py` în arcade. De aceea promptul cere aceeași suprafață și aceeași lumină în toate trei (să arate ca un set) și subiectul centrat, cu aer sus (partea de sus a arcadei e rotundă și taie colțurile). Doar imaginea S5 e decupaj pe fundal alb (NU activa „transparent background” și NU folosi Remove Background: fundalul îl scoatem local).

| Fișier | Aspect ratio | Ce arată | Folosire |
|---|---|---|---|
| rec1-pankees.png | 4:5 | teanc scurt de Pankees de post cu fructe proaspete (kiwi, mango, rodie), fără unt, frișcă sau miere | foto în arcadă 196 x 264 (export 2x), rețeta 01 |
| rec2-pizza.png | 4:5 | pizza de casă cu pepperoni întreagă, abia scoasă, 35 de grade | cadrul 1 al GIF-ului (și imaginea de start pentru video) |
| rec2-pizza.mp4 | 4:5 | video 3-5 s: aburi care urcă, mozzarella care bolborosește ușor, restul nemișcat | GIF animat `assets/rec2-pizza.gif`, max 1 MB |
| rec3-brownie.png | 4:5 | un pătrat înalt de brownie cu zmeură, mure și afine adunate deasupra, 30-45 de grade | foto în arcadă, rețeta 03 |
| s5-clatite.png | 1:1 | teanc plat de clătite subțiri, cea de sus împăturită în jumătate, zahăr pudră | decupaj peste un cerc portocaliu în S5 |

**Diferite de welcome 1-3, checkout-started 1-2 și NC1-2 (verificat în `image-prompts.md` și în strategie):**
- Pankees: nu teanc înalt cu afine și sirop (W1), nu felie scoasă (W3), nu banană și miere (W3, NC1), nu chocolate chips cu căpșuni (C1), nu mini pancakes în cerc cu zmeură (C2). Fructe noi, care nu au fost topping principal: kiwi, mango, semințe de rodie. Fără unt, frișcă, miere (rețetă de post). Fructele exacte sunt [DE CONFIRMAT CU CLIENTUL]; promptul se schimbă când vine răspunsul.
- Pizza: nu margherita întreagă cu felie trasă (W2), nu felii cu legume (W3), nu felie ridicată de mână din lateral (NC2). Aici: pepperoni, pizza întreagă la 35 de grade, aburi, fără mână.
- Brownie: nu brownie simplu de sus (W1), nu stivuit lateral (W3), nu farfurie mică de sus în hero compus (NC1). Aici: un singur pătrat înalt, fructe de pădure deasupra, 30-45 de grade.
- Clătite: nu triunghiuri cu gem (W1), nu sferturi lângă pancakes (W2), nu rulate cu cremă de sus (C1). Aici: teanc plat, văzut din lateral.

Suprafață comună pentru rec1-rec3: **masă mată gri-cărbune închis, fundal la fel, lumină caldă din lateral**. Fundalul închis face aburii pizzei vizibili și mâncarea iese în evidență în arcadele albe cu contur negru.

## rec1-pankees.png (4:5)
Professional food photography, vertical 4:5 frame. A short stack of three fluffy golden vegan pancakes on a small round matte black ceramic plate, centred in the lower two thirds of the frame, with generous empty space above. On top, a colourful heap of fresh fruit: slices of kiwi, cubes of ripe mango and a scatter of pomegranate seeds, a few pieces falling onto the plate. No butter, no cream, no honey, no syrup. Plain dark charcoal matte table and a plain dark charcoal background, no props. Camera at about 30 degrees, warm soft side light from the left, crisp texture of the pancake edges, fresh and bright fruit colours, appetizing. Nothing touching the edges of the frame. No hands, no people, no text, no logos, no labels, no packaging.

## rec2-pizza.png (4:5), cadrul 1 al GIF-ului
Professional food photography, vertical 4:5 frame. A whole round homemade pepperoni pizza fresh out of the oven on a round dark baking stone, seen from about 35 degrees, centred in the lower two thirds of the frame with generous dark empty space above it. Golden, slightly irregular homemade crust with a few blistered spots, bubbling melted mozzarella, cupped pepperoni slices with crisp edges and small glossy pools of oil. Soft wisps of steam rising from the centre of the pizza into the dark space above, clearly visible against the dark background. Plain dark charcoal matte table and plain dark charcoal background, no props, no board, no cutter. Warm side light from the left, rich and appetizing. Nothing touching the edges of the frame. No hands, no people, no text, no logos, no labels, no packaging.

## rec2-pizza.mp4 (video, 3-5 s, buclă)
Start: imaginea `rec2-pizza.png` aprobată (image-to-video). Model video ales în Higgsfield, durata cea mai scurtă disponibilă (3-5 s), 4:5.

Prompt:
Locked-off static camera, no camera movement, no zoom. Cinemagraph: the pizza stays perfectly still; only soft wisps of steam rise slowly from the centre of the pizza and drift upward into the dark space above, and the melted mozzarella bubbles very gently in two or three small spots. Lighting and colours stay constant. The last frame matches the first frame so the clip loops seamlessly. No hands, no people, no objects entering the frame, no text.

Verifică: camera nu se mișcă (altfel GIF-ul devine mare și pâlpâie), primul cadru e identic cu `rec2-pizza.png`, nicio mână, niciun obiect nou.

### Cum se face GIF-ul (local)
1. **Cu ffmpeg (recomandat):** `brew install ffmpeg` (o singură dată; la 13.10.2026 `ffmpeg` NU e instalat pe acest Mac). Pune `rec2-pizza.mp4` în `images/` și rulează `build.py`: scriptul extrage max 4 s la 12 cadre/s, pune fiecare cadru în arcadă și scrie `assets/rec2-pizza.gif` sub 1 MB (scade scara, culorile și cadrele dacă e nevoie). Raportul afișează mărimea și numărul de cadre.
2. **Fără ffmpeg:** convertește video-ul în GIF cu orice convertor (de exemplu ezgif.com, „Video to GIF”), 4:5, lățime 400-600px, 10-12 cadre/s, max 4 s. Salvează rezultatul ca `images/rec2-pizza.gif` și rulează `build.py`: scriptul citește cadrele cu Pillow și face restul (arcadă, paletă, limită de 1 MB). Fișierul `.gif` are prioritate față de `.mp4`.
3. **Fără video:** dacă există doar `rec2-pizza.png`, GIF-ul are un singur cadru (static). Emailul funcționează la fel.

Primul cadru al GIF-ului e primul cadru al video-ului; trebuie să arate ca o fotografie completă, pentru că Outlook desktop afișează doar cadrul 1.

## rec3-brownie.png (4:5)
Professional food photography, vertical 4:5 frame. One tall, thick square of fudgy chocolate brownie with a shiny crackly top, on a small round matte black ceramic plate, centred in the lower two thirds of the frame with generous empty space above. A generous heap of fresh berries piled on top of the square: raspberries, blackberries and blueberries, a few berries tumbling onto the plate, a light dusting of powdered sugar on the berries. Camera at 30 to 45 degrees, showing both the berry-topped surface and the dense moist side of the brownie. Plain dark charcoal matte table and plain dark charcoal background, no props. Warm soft side light from the left, strong contrast between the dark chocolate and the bright berries, appetizing. Nothing touching the edges of the frame. No hands, no people, no text, no logos, no labels, no packaging.

## s5-clatite.png (1:1, decupaj)
Professional food photography on a plain pure white seamless background, no props, no plate. A neat flat stack of about eight thin golden homemade crepes, slightly irregular lacy edges, the top crepe folded in half and resting on the stack, a light dusting of powdered sugar on top. Side view, camera at about 15 degrees, so the layered edges of the stack are clearly visible. The whole stack fully in frame with white space around it, nothing cut off by the edges. Warm, cozy, homemade feel, soft warm light, appetizing. Only a minimal soft contact shadow. No hands, no people, no text, no logos, no labels, no packaging, no jar.

## Checklist (la fiecare imagine, înainte de salvare)

- [ ] rec1-rec3: aceeași suprafață gri-cărbune și aceeași lumină din stânga; subiectul centrat jos, cu aer sus (partea de sus a arcadei taie colțurile).
- [ ] rec1: fără unt, frișcă, miere, sirop (rețetă de post); fructele din prompt sau cele confirmate de client.
- [ ] rec2: pepperoni vizibil, aburi vizibili pe fundalul închis, pizza întreagă (nu felie trasă), fără mână.
- [ ] rec2.mp4: camera fixă, doar aburi și bule mici, buclă curată, primul cadru = rec2-pizza.png.
- [ ] rec3: un singur pătrat înalt, fructele de pădure deasupra, unghi 30-45 de grade.
- [ ] s5: fundal alb uniform, teancul întreg în cadru.
- [ ] Doar mâncare: fără ambalaje, pungi, borcane, fără text, logo-uri sau etichete inventate. Fără fețe, mâini, oameni.
- [ ] Diferită de pozele din welcome 1-3, checkout-started 1-2 și NC1-2 (lista de sus).
- [ ] Salvată în `images/` cu numele exact, apoi `build.py --preview` și verificat: GIF sub 1 MB (raportul build-ului), cadrul 1 arată bine singur.
