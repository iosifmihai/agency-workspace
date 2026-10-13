# Prompturi Higgsfield, New Customer Email 1

Pe higgsfield.ai: model **GPT Image**, calitate **High**, rezoluție **2K**, aspect ratio din tabel.
Toate 5 sunt decupaje: promptul cere **fundal alb simplu**. NU activa „transparent background” și NU folosi Remove Background: fundalul îl scoatem noi local cu `build.py`.
Salvează în `clients/lucasbites/emails/new-customer-01/images/` cu exact numele de mai jos (PNG sau JPG), apoi rulează `python3 build.py`.

**Nu se generează:** imaginile produselor comandate (S2). Vin din feed-ul de produse theMarketer (`{{ORDER_PRODUCT_IMAGE}}`).
**Nu se generează acum:** img6-img9 (variantele de rețetă pe categorie din copy.md). Le scriem doar dacă se confirmă conținutul condiționat în theMarketer (copy.md, întrebarea 4).

**Recuzită comună: aceeași farfurie rotundă din gresie mată bej deschis (culoarea fulgilor de ovăz)**, cu margine puțin mai închisă, în toate cele 5 poze. Bej, nu alb și nu gri: o farfurie albă sau gri deschis se pierde la decupare (are aceeași culoare cu fundalul) și ar semăna cu W1. Nu e farfuria neagră din W3. Dacă prima generare iese bine, folosește-o ca imagine de referință pentru celelalte 4.

| Fișier | Aspect ratio | Ce arată | Folosire în email |
|---|---|---|---|
| img1-hero.png | 1:1 | 3 farfurii separate, de sus: pancakes cu afine, clătite rulate, brownie cu fructe de pădure | separate automat de `build.py`: A și B ies din cadru sus, în banda roz; C traversează curba roz -> portocaliu |
| img2-banane-nuci.png | 1:1 | teanc de 4 pancakes cu nuci și banane caramelizate, lateral 20-30° | rețeta săptămânii, pe negru, peste un disc turcoaz (600 x 400) |
| img3-afine.png | 1:1 | pancakes cu afine și sirop de afine, de sus | cardul 1, farfuria iese din cadru pe stânga (280 x 260) |
| img4-teanc.png | 1:1 | vârful unui teanc, cub de unt care se topește, sirop în spirală, strict de sus | cardul 2, farfuria iese din cadru pe dreapta |
| img5-clatite.png | 1:1 | platou cu clătite rulate + 2 boluri mici, de sus | cardul 3, farfuria iese din cadru pe stânga |

**Două abateri voite de la tabelul din copy.md, secțiunea 7** (copy.md lasă compoziția în seama UI):
1. **img1:** copy.md cere farfuriile deja tăiate de marginile cadrului. Le cerem **întregi și separate**, iar `build.py` le taie la marginea emailului. Așa decupajul e curat, iar poziția fiecărei farfurii se poate regla din cod fără o generare nouă.
2. **img3:** copy.md cere 45°. Îl cerem **de sus**, ca cele 3 farfurii din zig-zag să se citească drept un set (ca în ref3). img4 și img5 erau deja de sus.

---

## img1-hero.png (1:1)
Professional food photography on a plain pure white seamless background, no props, no surface texture. Overhead top-down view of three identical round matte stoneware plates in a warm light oatmeal beige color with a slightly darker rim, clearly separated from each other with white space between them, the plates not touching. Left plate, centered vertically: three golden American pancakes with blueberries baked into the batter and a few fresh blueberries on top, a thin glossy drizzle of syrup. Top right plate: thin golden crepes rolled into neat logs, lined up side by side, lightly dusted with powdered sugar. Bottom right plate: two thick fudgy chocolate brownie squares topped with fresh raspberries, blueberries and blackberries. All three plates fully in frame, nothing cut off by the edges, generous white space around each plate. Bright, fresh, inviting "your table, soon" feel, soft natural daylight, crisp textures, appetizing. Only a minimal soft contact shadow under each plate. No hands, no people, no text, no logos, no labels, no packaging, no bottles.

## img2-banane-nuci.png (1:1)
Professional food photography on a plain pure white seamless background, no props. A round matte stoneware plate in a warm light oatmeal beige color holding a neat stack of four fluffy golden American pancakes, topped with glossy caramelized chopped walnuts and caramelized banana slices, maple syrup running down the sides of the stack and pooling on the plate. Side view, camera at 20 to 30 degrees, the whole plate fully in frame with white space around it, nothing cut off by the edges. Focus on the shiny caramel on the walnuts. Warm side light, cozy weekend breakfast, appetizing. Only a minimal soft contact shadow under the plate. No honey, no fan arrangement, no hands, no people, no text, no logos, no labels, no packaging.

## img3-afine.png (1:1)
Professional food photography on a plain pure white seamless background, no props. Overhead top-down view of a round matte stoneware plate in a warm light oatmeal beige color with two overlapping golden pancakes, one cut in half so the blueberries baked inside show on the cut edge, a pool of deep purple blueberry syrup on the plate and a small handful of fresh blueberries. The whole plate fully in frame with white space around it, nothing cut off by the edges. Fresh morning breakfast, soft natural light, appetizing. Only a minimal soft contact shadow under the plate. No strawberries, no raspberries, no hands, no people, no text, no logos, no labels, no packaging.

## img4-teanc.png (1:1)
Professional food photography on a plain pure white seamless background, no props. Strict overhead top-down view of a round matte stoneware plate in a warm light oatmeal beige color holding a tall stack of golden pancakes, seen from directly above so only the top pancake shows, a cube of butter melting in the center and a glossy spiral of syrup drawn over the top. The whole plate fully in frame with white space around it, nothing cut off by the edges. Relaxed Sunday family breakfast, warm natural light, appetizing. Only a minimal soft contact shadow under the plate. No fruit, no hands, no people, no text, no logos, no labels, no packaging.

## img5-clatite.png (1:1)
Professional food photography on a plain pure white seamless background, no board. Overhead top-down view of a large round matte stoneware serving plate in a warm light oatmeal beige color with six to eight thin golden crepes rolled into logs and lined up, with two small matching beige bowls on the plate rim: one with red berry jam, one with chocolate spread. The whole plate fully in frame with white space around it, nothing cut off by the edges. Generous family table feel, soft natural light, appetizing. Only a minimal soft contact shadow under the plate. No triangles, no folded crepes, no hands, no people, no text, no logos, no labels, no packaging.

---

## Checklist (la fiecare imagine, înainte de salvare)

- [ ] Fundal alb simplu, uniform (fără tablă de șah, fără gradient, fără textură de masă).
- [ ] Farfuria întreagă în cadru, cu spațiu alb în jur, nimic tăiat de margine.
- [ ] img1: cele 3 farfurii **nu se ating** (altfel `build.py` nu le poate separa și afișează un avertisment).
- [ ] img1: pancakes în stânga, clătitele sus-dreapta, brownie jos-dreapta (`build.py` le recunoaște după poziție).
- [ ] Aceeași farfurie bej mată în toate cele 5 poze; nu albă, nu gri, nu neagră.
- [ ] Doar mâncare: fără ambalaje, sticle, pungi, cutii de livrare, fără text, logo-uri sau etichete inventate.
- [ ] Fără fețe, fără mâini, fără oameni.
- [ ] Unghiul cerut: img2 lateral 20-30°, toate celelalte de sus.
- [ ] Detaliul-cheie vizibil: nucile lucioase (img2), afinele în aluat pe tăietură (img3), untul și spirala de sirop (img4), clătitele rulate aliniate (img5).
- [ ] Diferită de pozele din W1-W3: fără stack înalt cu afine la 45° și fără evantai cu fructe de pădure (W1), fără clătite triunghiuri (W1), fără lava cake rupt și pizza întreagă (W2), fără farfurii negre, stack cu felie scoasă sau evantai cu banană și miere (W3).
- [ ] Salvată în `new-customer-01/images/` cu numele exact din tabel, apoi `python3 build.py` și verificare în `index.html`.
