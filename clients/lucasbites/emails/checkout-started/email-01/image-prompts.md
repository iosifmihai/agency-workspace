# Prompturi Higgsfield, Checkout Started Email 1

Pe higgsfield.ai: model **GPT Image**, calitate **High**, rezoluție **2K**, aspect ratio din tabel.
Ambele sunt decupaje: promptul cere **fundal alb simplu**. NU activa „transparent background” și NU folosi Remove Background: fundalul îl scoatem noi local (`build.py`).
Salvează în `clients/lucasbites/emails/checkout-started/email-01/images/` cu exact numele de mai jos (PNG sau JPG).

**Doar 2 imagini.** Imaginile produselor din blocul „În coșul tău” NU se generează: vin din catalogul magazinului, prin ESP. În preview apar ca placeholdere marcate „EXEMPLU”.

| Fișier | Aspect ratio | Ce arată | Folosire |
|---|---|---|---|
| img1-hero.png | 1:1 | teanc de 4 pancakes cu chocolate chips, plutind, cu căpșuni și bucăți de ciocolată în aer | decupaj rotit ~-10° în hero 1200 x 1000 pe roz, peste marginea panoului alb |
| img2-clatite.png | 1:1 | farfurie neagră mată de sus, clătite rulate cu cremă de ciocolată, una tăiată | decupaj tăiat de marginea dreaptă în S5, JPG 440 x 600 pe portocaliu |

Diferite de welcome 1-3: niciun teanc cu afine sau cu sirop curgând (W1), nimic cu banană și miere, nicio felie scoasă din teanc (W3), fără clătite împăturite în triunghi cu gem (W1) sau în sferturi lângă pancakes (W2). Topping-uri noi: chocolate chips, căpșuni, cremă de ciocolată, alune.

## img1-hero.png (1:1)
Professional food photography on a plain pure white seamless background, no props, no plate, no surface. A stack of four fluffy golden homemade pancakes with dark chocolate chips baked into them, levitating in mid-air, the whole stack gently tilted. Melted chocolate chips visible on the golden surface and on the sides of the stack. Around the stack, floating freely in the air: four or five fresh strawberry halves and a few dark chocolate chips and small chocolate chunks, spread out so they do not touch the stack. Camera at a slight low angle, about 20 degrees, so the stack looks generous. The whole stack and all floating pieces fully in frame with wide white space around them, nothing cut off by the edges. Playful, energetic, "craving" mood, bright warm studio light, crisp textures, appetizing. No shadow on the background. No hands, no people, no text, no logos, no labels, no packaging.

## img2-clatite.png (1:1)
Professional food photography on a plain pure white seamless background, no props. Overhead top-down view of a round matte black ceramic plate holding three thin golden homemade crepes rolled into tubes and laid side by side, filled with smooth chocolate cream. One roll is cut in half at an angle, showing the chocolate cream spiral inside. A light dusting of powdered sugar and a sprinkle of chopped toasted hazelnuts on top. The whole plate fully in frame with white space around it, nothing cut off by the edges. Cozy, indulgent, homemade feel, soft warm natural light, appetizing. Only a minimal soft contact shadow under the plate. No hands, no people, no text, no logos, no labels, no packaging, no jar.

## Checklist (la fiecare imagine, înainte de salvare)

- [ ] Fundal alb simplu, uniform (fără tablă de șah, fără gradient, fără textură de masă).
- [ ] img1: fără farfurie, fără umbră pe fundal, bucățile care plutesc nu ating marginea cadrului și nu se lipesc de teanc.
- [ ] img2: farfuria neagră mată întreagă în cadru, cu spațiu alb în jur, văzută de sus.
- [ ] Doar mâncare: fără ambalaje, sticle, pungi, borcane, fără text, logo-uri sau etichete inventate.
- [ ] Fără fețe, fără mâini, fără oameni.
- [ ] Detaliul-cheie vizibil: chocolate chips în pancakes și căpșunile (img1), spirala de cremă din rulada tăiată (img2).
- [ ] Diferită de pozele din welcome 1-3 (vezi lista de deasupra).
- [ ] Salvată în `checkout-started/email-01/images/` cu numele exact din tabel, apoi rulat `build.py`.
