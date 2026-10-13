# Prompturi Higgsfield, Checkout Started Email 2

Pe higgsfield.ai: model **GPT Image**, calitate **High**, rezoluție **2K**, aspect ratio din tabel.
Ambele sunt decupaje: promptul cere **fundal alb simplu**. NU activa „transparent background” și NU folosi Remove Background: fundalul îl scoatem noi local (`build.py`).
Salvează în `clients/lucasbites/emails/checkout-started/email-02/images/` cu exact numele de mai jos (PNG sau JPG).

**Doar 2 imagini.** Imaginile produselor din blocul „În coșul tău” NU se generează: vin din feed-ul theMarketer. În preview apar ca placeholdere marcate „EXEMPLU”. Recenziile sunt text: nu generăm nicio imagine care ar putea trece drept poză de client (fără mâini, fără telefon, fără unghi de Instagram, fără bucătărie de acasă în fundal).

| Fișier | Aspect ratio | Ce arată | Folosire |
|---|---|---|---|
| img1-hero.png | 1:1 | farfurie neagră mată văzută de sus, 9-10 mini pancakes așezate în cerc, zmeură între ele și o grămăjoară de zmeură cu mentă în centru | decupaj 740 px în hero 1200 x 900 pe portocaliu, sub 5 stele desenate, trece peste festonul spre alb |
| img2-fursecuri.png | 3:2 | 3 fursecuri cu bucăți mari de ciocolată neagră, unul rupt în două cu ciocolata topită vizibilă | decupaj centrat în S6, JPG 720 x 440 pe negru |

Diferite de welcome 1-3 și de Email 1: niciun teanc (W1, W3, E1), nicio felie scoasă, fără sirop curgând, fără clătite (W1, W2, E1), fără brownie, lava cake, budincă, banana bread, pizza. Noi: aranjamentul în cerc de sus cu mini pancakes, zmeura ca topping principal (în welcome a fost doar accent lateral), fursecurile (prima apariție în serie).

## img1-hero.png (1:1)
Professional food photography on a plain pure white seamless background, no props. Overhead top-down view, camera exactly 90 degrees above, of a round matte black ceramic plate. On the plate, nine or ten small fluffy golden homemade mini pancakes, each about the size of a cookie, arranged evenly in a ring along the rim, slightly overlapping like a wreath. Fresh whole raspberries tucked between the mini pancakes, and a small heap of fresh raspberries with two or three mint leaves in the centre of the ring. The golden pancake surface shows the typical fine bubbles and a soft brown even colour. The whole plate fully in frame with generous white space around it, nothing cut off by the edges. Fresh, generous, cheerful mood, bright soft daylight, crisp textures, appetizing. Only a minimal soft contact shadow under the plate. No hands, no people, no cutlery, no napkin, no table surface, no text, no logos, no labels, no packaging.

## img2-fursecuri.png (3:2)
Professional food photography on a plain pure white seamless background, no props, no plate. Three thick homemade cookies with large chunks of dark chocolate, golden brown with crisp edges and a soft centre, arranged in a loose overlapping group. The front cookie is broken into two halves pulled slightly apart, with glossy melted dark chocolate stretching between them. A few small dark chocolate chunks and crumbs scattered around. Camera at about 30 degrees, close and appetizing. The whole group fully in frame with white space around it, nothing cut off by the edges. Warm, indulgent, homemade feel, soft warm studio light. Only a minimal soft contact shadow. No hands, no people, no text, no logos, no labels, no packaging, no jar, no glass of milk.

## Checklist (la fiecare imagine, înainte de salvare)

- [ ] Fundal alb simplu, uniform (fără tablă de șah, fără gradient, fără textură de masă).
- [ ] img1: văzută strict de sus, farfuria neagră întreagă în cadru, mini pancakes în cerc (nu în teanc), zmeura vizibilă între ele și în centru.
- [ ] img2: fursecurile întregi în cadru, unul rupt cu ciocolata topită vizibilă, fără farfurie.
- [ ] Doar mâncare: fără ambalaje, sticle, pungi, borcane, fără text, logo-uri sau etichete inventate.
- [ ] Fără fețe, fără mâini, fără oameni, fără telefon, nimic care să arate ca o poză trimisă de un client.
- [ ] Diferită de pozele din welcome 1-3 și Email 1 (vezi lista de deasupra).
- [ ] Salvată în `checkout-started/email-02/images/` cu numele exact din tabel, apoi rulat `build.py --preview` și verificat hero-ul (farfuria trece peste feston, nu e tăiată de marginea de jos a imaginii).
