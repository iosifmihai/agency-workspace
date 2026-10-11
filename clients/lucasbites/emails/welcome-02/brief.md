# Welcome series, Email 2: brief comun

**Client:** Lucas Bites. Sursa de adevăr: `clients/lucasbites/discovery.md`.
**Email 1 (gata):** `clients/lucasbites/emails/welcome-01/` (copy.md, index.html, build.py). Email 2 trebuie să arate ca aceeași familie vizuală, dar cu layout propriu, nu o copie.
**ESP:** de confirmat. HTML email-safe (tabele, CSS inline, 600px). Titluri în Akrobat (webfont deja convertit în `welcome-01/assets/fonts/`, licența vine până la trimitere), text Arial.

## Ce cere clientul pentru Email 2
- Povestea brandului
- Categorii de produse: **Pancakes & Crêpes, Budinci, Prăjituri, Pizza**
- USP: ingrediente

## Povestea brandului: ATENȚIE
Nu avem povestea fondatorului (cine e Lucas, anul înființării, de unde a pornit). Nu apare în discovery și nici pe site. **NU inventăm fapte** (nume, ani, locuri, familie, bunici etc.).
Povestea se construiește din ce e confirmat:
- „oricine le poate face, repede” (hero site)
- Mixuri „în care e deja aproape tot. Tu adaugi apă, agiți și gătești.”
- „Ingrediente pe care le recunoști, puse deja la cântar.”
- Slogan oficial: „eat what you love”
- Momente de consum de pe site: „Micul dejun în familie: Toată lumea la masă, fiecare cu topping-ul lui. Un teanc întreg de pancakes iese din aceeași sticlă, fără bol și fără mixer.” / „Duminica fără grabă: Pancakes pufoase cu sirop sau clătite subțiri, cât timp se face cafeaua.” / „Gustarea de după școală: Copiii pot agita singuri sticla. În câteva minute gustarea e pe masă.” / „Pauza de la birou: Un brownie sau un banana bread făcut acasă, adus pentru colegi la cafeaua de la 11.” / „Movie night: Pizza de casă la începutul filmului, lava cake caldă la final.”
- Dovadă: peste 1.100 de recenzii, medie 4,9 din 5 (valabil 10.10.2026); retaileri Kaufland, Carrefour, Dr. Max, Farmacia Tei, Bebe Tei, eMAG, Freshful.
Unde ar ajuta un fapt real (ex. originea numelui), pune un placeholder vizibil `[DE CONFIRMAT CU CLIENTUL: ...]` și listează întrebările pentru client.

## Categorii (din site, date aprobate)
| Categorie | Produse | Link site |
|---|---|---|
| Pancakes & Crêpes | Classic Pankees (Bestseller, 4,9 / 148 recenzii), Buttermilk Pankees, Chocolate Chips Pankees, Blueberry Pankees, Vegan Classic Pankees (vegan, de post), Crêpes Traditional, Crêpes Mix Original | produse.html#pancakes-crepes |
| Budinci | Mix de budincă (NOU) | produse.html#budinci |
| Prăjituri | Brownie Mix (5,0), Lava Cake Mix (5,0), Banana Bread Mix (NOU), Carrot Cake Mix (NOU) | produse.html#prajituri |
| Pizza | Pizza Crust Mix (4,8 / 80 recenzii) | produse.html#pizza |
Prețurile sunt încă în lucru: **nu afișăm prețuri**. URL-urile reale vin la lansarea site-ului: folosește placeholder `{{SHOP_URL}}/produse#<slug>`.
Ce adaugi tu, după produs: apă la pancakes, apă și ulei la pizza, ouă și unt la lava cake.

## USP ingrediente (din site, aprobat, afirmații confirmate de client)
- Făină de grâu nealbită (în mixurile pentru pancakes și clătite)
- Zahăr brun din trestie în loc de zahăr alb
- Ce adaugi tu, scris clar (apă, ulei sau ouă și unt, după produs)
- Fără conservanți (lista scurtă e pe fiecare ambalaj)
- „Lista completă de ingrediente și valorile nutriționale sunt pe pagina fiecărui produs.”
ATENȚIE: făina nealbită e doar la pancakes și clătite. Nu generaliza la toată gama. Fără promisiuni de sănătate.

## Reguli de brand (obligatorii)
- Doar 4 culori: portocaliu #FAA61A, roz #F7ACB4, turcoaz #86D2DA, negru #000000. Alb doar fundal.
- Text negru pe culorile de brand; pe negru doar text portocaliu. Niciodată alb pe portocaliu/roz/turcoaz.
- Ton prietenos, direct, jucăuș, simplu, apetisant. Engleză cât e nevoie. Fără „cel mai bun”, fără corporatist, fără moralizare.
- Fără emoji, fără em-dash.

## Direcția vizuală
Exemple vechi: `clients/lucasbites/emails/welcome-01/refs/ref1-4.png`. Exemple noi: `refs/ref5-7.png` în acest folder:
- ref5 (Beguile): hero dramatic cu produs „dezvăluit”, carduri de recenzii albe pe fundal închis, grid de „note” (ingrediente ca iconițe foto), secțiuni produs cu imagine stânga + text dreapta.
- ref6 (BetterBrand): blocuri roșu/negru/crem cu valuri, liste cu bife în card cu contur, cifre în bule peste foto decupate, carduri produs cu foto pătrat rotunjit + text.
- ref7 (Kings Row / Remedy / Boustan): tipografie foarte mare condensată (se potrivește cu Akrobat), „OUR'S vs THEIR'S”, Boustan cu săgeți desenate și etichete scrise care leagă textul de mâncare („a hearty shawarma”).

## Imagini
Generate cu Higgsfield (GPT Image). Contul e încă în perioada de probă până pe 13.10.2026, deci utilizatorul le generează pe higgsfield.ai din prompturile noastre. Doar mâncare, fără ambalaje inventate, fără text în imagine, fără fețe (mâini OK). Decupajele: cere fundal alb simplu (scoatem noi fundalul local), NU „transparent background” (modelul desenează tabla de șah).
