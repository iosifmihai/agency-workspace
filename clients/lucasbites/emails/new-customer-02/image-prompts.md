# Prompturi Higgsfield, New Customer Email 2

Pe higgsfield.ai: model **GPT Image**, calitate **High**, rezoluție **2K**, aspect ratio din tabel.
Toate 4 sunt decupaje: promptul cere **fundal alb simplu**. NU activa „transparent background” și NU folosi Remove Background: fundalul îl scoatem noi local.
Salvează în `clients/lucasbites/emails/new-customer-02/images/` cu exact numele de mai jos (PNG sau JPG). După aceea, Claude rulează build-ul, verifică decupajele și reface previzualizările.

**Nu se generează:** ambalajele. Vin doar din `packshots/` (pr-choco, pr-pizza, pr-lava), fotografii reale, nemodificate. Niciun prompt nu cere sticle, pungi, cutii sau etichete.
**Nu se generează acum:** rezervele și rotația sezonieră (img4-clatite-v2, img5-brownie, img6-cookies, img7-gingerbread, img8-post-fructe). Le scriem doar dacă se confirmă conținutul condiționat în theMarketer (copy.md, întrebările 5 și 8).

**Recuzită comună:** aceeași farfurie rotundă din gresie mată bej deschis (culoarea fulgilor de ovăz), cu margine puțin mai închisă, ca în Email 1 (continuitate de familie, copy.md secțiunea 7). Doar la img1 și img3; img2 și img0 nu au farfurie. Bej, nu alb și nu gri: o farfurie albă se pierde la decupare. Dacă prima generare iese bine, folosește-o ca imagine de referință pentru img3.

| Fișier | Aspect ratio | Ce arată | Unghi | Tip decupaj | Folosire în email |
|---|---|---|---|---|---|
| img1-ciocolata.png | 1:1 | teanc scurt de 3 pancakes cu bucăți de ciocolată, fir de sos de ciocolată, pe farfuria bej | frontal, la nivelul ochilor | farfurie laterală (`SIDE_PLATES`) | perechea 1, pe roz: farfuria iese prin marginea stângă, lângă sticla Chocolate Chips |
| img2-pizza-felie.png | 4:5 | felie de pizza cu pepperoni ridicată de o mână, mozzarella întinsă, fără farfurie | lateral 30°, mâna intră din dreapta | fără farfurie (niciun set) | perechea 2, pe negru: mâna iese prin marginea dreaptă, lângă cutia Pizza Crust Mix |
| img3-lava-vanilie.png | 1:1 | lava cake întreg, cupă de înghețată de vanilie deasupra, puțină pudră de cacao, pe farfuria bej | lateral 20° | farfurie laterală (`SIDE_PLATES`) | perechea 3, pe turcoaz: farfuria iese prin marginea stângă, lângă punga Lava Cake Mix |
| img0-hero-ingrediente.png | 1:1 | bucăți separate: ciocolată, pepperoni, o cupă de înghețată | ușor de sus, „în zbor” | bucăți libere (niciun set) | hero: bucățile se separă automat și „zboară” peste tăietura portocaliu -> negru |

**Două abateri voite de la copy.md, secțiunea 7** (copy.md lasă compoziția în seama UI):
1. **img1:** copy.md cere bucăți de ciocolată „căzute lângă farfurie”. Le cerem **doar pe farfurie**: bucățile de pe fundal, pe aceleași rânduri cu farfuria, ar strica decupajul farfuriei laterale (ar apărea pete albe între ele și farfurie).
2. **img2:** copy.md nu fixează direcția mâinii. O cerem **din marginea dreaptă a cadrului**: în email, încheietura iese prin marginea dreaptă a emailului. O mână care intră de sus ar apărea tăiată în mijlocul blocului negru.

---

## img1-ciocolata.png (1:1)
Professional food photography on a plain pure white seamless background, no props, no surface texture. Eye-level frontal view, camera at plate height, of a round matte stoneware plate in a warm light oatmeal beige color with a slightly darker rim, centered in the frame. On the plate, a short stack of three fluffy golden American pancakes with dark chocolate chips clearly visible in the batter and on the edges of each pancake, a thin glossy drizzle of chocolate sauce running from the top down one side of the stack, and a few loose chocolate chips fallen on the plate around the stack, all of them on the plate, none on the background. The whole plate fully in frame, generous white space around it, nothing cut off by the edges. Warm soft side light, after-school treat feel, appetizing. Only a minimal soft contact shadow under the plate. No syrup, no butter, no fruit, no cream, no fork, no hands, no people, no text, no logos, no labels, no packaging, no bottles.

## img2-pizza-felie.png (4:5)
Professional food photography on a plain pure white seamless background, no plate, no board, no table texture. Three-quarter side view, camera at about 30 degrees. A whole homemade pepperoni pizza with a puffy golden crust resting directly on the white background in the lower left part of the frame. A hand and wrist enter from the right edge of the frame and lift one slice up and to the right, long strings of melted mozzarella stretching between the lifted slice and the rest of the pizza. Crispy slightly curled pepperoni, golden blistered crust edge. Only one bare hand and wrist are visible, coming in from the right edge, no sleeve, no jewelry, no nail polish. The pizza fully in frame with white space on the left, top and bottom; only the wrist touches the right edge of the image. Movie night at home feel, warm light, appetizing. Only a minimal soft contact shadow under the pizza. No face, no other people, no text, no logos, no labels, no packaging, no pizza box.

## img3-lava-vanilie.png (1:1)
Professional food photography on a plain pure white seamless background, no props, no surface texture. Side view, camera at about 20 degrees, of a round matte stoneware plate in a warm light oatmeal beige color with a slightly darker rim, centered in the frame. On the plate, one whole individual chocolate lava cake, intact, not cut and not broken, with a scoop of creamy pale yellow vanilla ice cream with visible vanilla bean specks on top, just starting to melt and run down the sides of the cake, and a light dusting of cocoa powder on the cake and on the plate. The whole plate fully in frame, generous white space around it, nothing cut off by the edges. Cozy evening dessert feel, warm soft light, appetizing. Only a minimal soft contact shadow under the plate. No molten chocolate pouring out, no berries, no mint leaf, no spoon, no hands, no people, no text, no logos, no labels, no packaging.

## img0-hero-ingrediente.png (1:1)
Professional food photography on a plain pure white seamless background, no plate, no bowl, no surface texture. Separate loose ingredients spread across the frame with clear white space between every piece, no two pieces touching: one round scoop of creamy pale yellow vanilla ice cream with visible vanilla bean specks, seven chunky pieces of dark chocolate broken from a bar in different sizes, and three slices of pepperoni. Seen slightly from above, as if the pieces were floating, every piece sharp with crisp edges. Soft natural light, each piece with only its own tiny soft shadow, no shadows connecting pieces. All pieces fully in frame, nothing cut off by the edges. No hands, no people, no text, no logos, no labels, no packaging.

---

## Checklist (la fiecare imagine, înainte de salvare)

- [ ] Fundal alb simplu, uniform (fără tablă de șah, fără gradient, fără textură de masă, fără blat de lemn).
- [ ] Nimic tăiat de margine. Singura excepție: la img2, încheietura atinge **doar marginea dreaptă**.
- [ ] img1 și img3: aceeași farfurie bej mată ca în Email 1; nu albă, nu gri, nu neagră. img2 și img0: fără farfurie, fără bol, fără blat.
- [ ] img1: bucățile de ciocolată sunt toate **pe farfurie**, niciuna pe fundal.
- [ ] img0: bucățile **nu se ating** între ele (altfel nu pot fi separate și așezate pe tăietură).
- [ ] Înghețata (img3, img0) e galben pal cremos, cu puncte de vanilie, nu albă ca fundalul (altfel se pierde la decupare).
- [ ] Doar mâncare: fără ambalaje, sticle, pungi, cutii (nici cutie de pizza), fără text, logo-uri sau etichete inventate.
- [ ] Fără fețe și fără alți oameni; la img2 doar o mână și încheietura, fără mânecă și fără bijuterii.
- [ ] Unghiul cerut: img1 frontal la nivelul ochilor, img2 lateral 30°, img3 lateral 20°, img0 ușor de sus.
- [ ] Detaliul-cheie vizibil: ciocolata în aluat și firul de sos (img1), mozzarella întinsă între felie și pizza (img2), lava cake întreg cu înghețata care începe să se topească (img3).
- [ ] Diferită de pozele din Email 1 și W1-W3: fără farfurii de sus (Email 1), fără banane și nuci, afine, teanc de sus cu unt, platou de clătite (Email 1); fără lava cake rupt și pizza întreagă de sus cu felie trasă (W2); fără felii de pizza cu legume, farfurii negre, stack cu felie scoasă (W3); fără stack înalt cu afine la 45° (W1).
- [ ] Salvată în `new-customer-02/images/` cu numele exact din tabel.
