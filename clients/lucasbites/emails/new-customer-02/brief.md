# New Customer, Email 2: brief comun

**Client:** Lucas Bites. Sursa de adevăr: `clients/lucasbites/discovery.md`.
**Email anterior din flux:** `new-customer-01/` (brief.md, copy.md, design-direction.md, image-prompts.md, build.py, index.html). Email 2 face parte din aceeași familie vizuală (logo, curbe mari, fonturi, footer), dar are layout propriu. Secțiunea 5 din `new-customer-01/copy.md` („Predarea către Email 2”) e input, dar structura cerută de client mai jos are prioritate.
**ESP:** theMarketer. Sintaxa merge tags nu e verificată: placeholdere generice `{{...}}`, doar ca referință; utilizatorul pune sintaxa reală.
HTML email-safe (tabele, CSS inline, 600px). Titluri Akrobat (webfont în `new-customer-01/assets/fonts/`), text Arial.

## Ce cere clientul pentru Email 2
- Idei de rețete pe care să le încerci
- Produsele potrivite pentru rețetele puse (fiecare rețetă cu produsul ei)

Agentul Email Marketing Strategist poate adăuga secțiuni dacă sunt necesare, cu justificare.

## Decizii luate cu utilizatorul (12.10.2026)
1. **Pozele produselor** sunt fotografiile reale de ambalaj de pe site-ul aprobat v3, descărcate în `packshots/` (fundal alb): pr-blueberry, pr-brownie, pr-buttermilk, pr-choco (Chocolate Chips), pr-classic-front (Classic), pr-cookie450, pr-crepes (Crêpes Traditional), pr-lava, pr-pizza, pr-vegan (Classic Vegan). Nu se modifică, nu se recolorează, nu se generează ambalaje.
2. **Higgsfield** doar pentru fotografiile de mâncare ale rețetelor. Le generează utilizatorul pe higgsfield.ai din `image-prompts.md` (GPT Image, High, 2K, fundal alb simplu, niciodată „transparent background”), în `new-customer-02/images/`. Apoi Claude rulează build-ul, verifică decupajele și refacerea previzualizărilor. Utilizatorul NU primește niciodată comenzi de rulat.
3. **Promisiunea din Email 1** („În câteva zile te întrebăm cum au ieșit”): Email 2 conține un bloc scurt „Cum au ieșit?” (link spre recenzie/răspuns). Restul emailului rămâne pe rețete + produse.
4. **Fără prețuri, fără coduri de reducere.** Transport gratuit de la al 2-lea produs doar ca motiv, marcat de confirmat la lansare.
5. **Fără frază de consimțământ în footer**: o adaugă utilizatorul separat (ca la Email 1, marker `[ADAUGĂ UTILIZATORUL]`).

## Rețete disponibile (https://lucasbites.ro/propunere-v3/retete.html, citit 12.10.2026)
Site-ul publică pentru fiecare doar titlu, produs, timp, moment. Singura rețetă completă (ingrediente + pași) e „Pankees cu banane și nuci caramelizate” (reteta.html), folosită deja în Email 1. Nu inventăm ingrediente sau pași.

| Rețetă | Produs | Timp | Moment | Folosită în Email 1? |
|---|---|---|---|---|
| Pankees cu banane și nuci caramelizate | Classic Pankees | 20 min | Mic dejun | da (rețeta săptămânii) |
| Gingerbread Pancakes | Classic Pankees | 15 min | Desert | nu |
| Pankees proteice cu iaurt grecesc | Classic Pankees | 15 min | Mic dejun | nu (atenție: „proteice” poate fi afirmație nutrițională) |
| Pankees cu ciocolată | Chocolate Chips Pankees | 15 min | Desert | nu |
| Pancakes cu afine și sirop | Blueberry Pankees | 10 min | Mic dejun | da |
| Teancul de duminică | Buttermilk Pankees | 10 min | Familie | da |
| Lava cake cu înghețată de vanilie | Lava Cake Mix | 12 min | Desert | nu |
| Brownie cu fructe de pădure | Brownie Mix | 35 min | Desert | nu |
| Pizza de casă cu pepperoni | Pizza Crust Mix | 30 min | Familie | nu |
| Cookies cu ciocolată neagră | Cookie Mix Dark Chocolate | 14 min | Desert | nu |
| Clătite pentru toată familia | Crêpes Traditional | 10 min | Familie | da |
| Pankees de post cu fructe | Vegan Classic Pankees | 15 min | De post | nu |

Preferăm rețete nefolosite în Email 1, cu produse diferite de ce a cumpărat probabil clientul (cross-sell). Dacă theMarketer permite conținut condiționat după produsele cumpărate [neverificat], se notează ca opțiune.

## Reguli de brand (obligatorii)
- Doar 4 culori: portocaliu #FAA61A, roz #F7ACB4, turcoaz #86D2DA, negru #000000. Albul doar ca fundal.
- Pe culorile de brand textul e negru; pe negru, textul e doar portocaliu. Niciodată alb pe portocaliu, roz sau turcoaz.
- Ton prietenos, direct, jucăuș, simplu, apetisant. Engleză cât e nevoie. Fără „cel mai bun”, fără ton corporatist, fără moralizare, fără promisiuni de sănătate sau nutriționale.
- Fără emoji, fără em-dash. Plicata nu se folosește.

## Direcția vizuală
Referințele clientului: **`refs/ref3.png`** (Blue Apron) și **`refs/ref4.png`** (BetterBrand: blocuri de culoare puternice roșu/negru, tăieturi diagonale și ondulate, mâncare decupată care „iese” din cadru, titluri foarte mari, tabel de ingrediente în celule pe fundal închis, rețetă „The Classic” cu produsul, packshot mare al produsului cu ingrediente zburând în jur, CTA pill).
Traducere în brandul nostru: roșul devine una din cele 4 culori de brand. UI Designer alege pattern-urile și evită ce s-a folosit deja în new-customer-01 (hero roz cu farfurii la colțuri, carduri albe cu imagine rotundă, zig-zag farfurie + bandă) și în welcome 1-3.

## Imagini
Mâncare: fără ambalaje inventate, fără text, fără fețe (mâinile sunt OK), fundal alb pentru decupaj, diferite de pozele din new-customer-01 și welcome 1-3. Ambalajele: doar din `packshots/`.
