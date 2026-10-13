# New Customer, Email 3: brief comun

**Client:** Lucas Bites. Sursa de adevăr: `clients/lucasbites/discovery.md`.
**Emailuri anterioare din flux:** `new-customer-01/` și `new-customer-02/` (brief.md, copy.md, design-direction.md, image-prompts.md, build.py, index.html, preview.png). Email 3 face parte din aceeași familie vizuală (logo, curbe și tăieturi diagonale, fonturi, iconițe sociale, footer), dar are layout propriu. Secțiunea 5 din `new-customer-02/copy.md` („Predarea către Email 3”) e input, dar structura cerută de client mai jos are prioritate (Email 3 NU e emailul de reaprovizionare).
**ESP:** theMarketer. Sintaxa merge tags nu e verificată: placeholdere generice `{{...}}`, doar ca referință; utilizatorul pune sintaxa reală.
HTML email-safe (tabele, CSS inline, 600px, sub 102 KB). Titluri Akrobat (webfont în `new-customer-01/assets/fonts/`), text Arial.

## Ce cere clientul pentru Email 3
- Recomandare produse cross-sell
- USP: transport, livrare, suport etc.
- Încurajare postare rețetă proprie pe Social Media

Agentul Email Marketing Strategist poate adăuga secțiuni dacă sunt necesare, cu justificare.

## Decizii luate cu utilizatorul (13.10.2026)
1. **Cross-sell: produse fixe + marker pentru bloc dinamic.** Trei produse fixe, nefolosite ca produs principal în Email 1 și 2: **Brownie Mix** (450 g), **Cookie Mix Dark Chocolate** (450 g, vegan pe v3), **Crêpes Traditional** (280 g). Packshot-urile reale de pe v3 sunt în `packshots/` (pr-brownie, pr-cookie450, pr-crepes; fundal alb, nu se modifică, nu se generează ambalaje). În HTML se pune un marker `<!-- [OPȚIONAL theMarketer] ... -->` unde utilizatorul poate înlocui blocul fix cu un bloc de recomandări din theMarketer [neverificat dacă există în editor].
2. **Social: doar tag @lucas_bites**, fără hashtag nou. Instagram https://www.instagram.com/lucas_bites/ , TikTok https://www.tiktok.com/@lucas.bites.ro (+ Facebook și YouTube în footer, ca în Email 2).
3. **Fără recompensă pentru postare:** doar invitație. Fără concurs, fără premii, fără promisiune de repostare.
4. **Imaginile de mâncare le generează Claude direct în Higgsfield** (Higgsfield Pro), după `image-prompts.md`, fundal alb simplu pentru decupaj. Utilizatorul NU primește niciodată comenzi de rulat.
5. **Fără prețuri, fără coduri de reducere.** Fără frază de consimțământ în footer (marker `[ADAUGĂ UTILIZATORUL]`, ca la Email 1 și 2).
6. **Linkuri:** URL-urile site-ului actual până la lansarea v3 (ca în Email 2).

## Fapte verificate pentru USP (citite 13.10.2026)
Din v3 (https://lucasbites.ro/propunere-v3/index.html, contact.html):
- „Transport gratuit de la al 2-lea produs pentru acasă” (de confirmat la lansare, ca în Email 2).
- „Toate pachetele au transport gratuit” (pachetele sunt „Propunere · de stabilit de Lucas Bites”, deci NU se folosesc în email).
- Contact: „Întrebări despre o comandă, despre produse [...] Îți răspundem în zilele lucrătoare.” Telefon +40 731 399 399, e-mail office@lucasbites.ro, formular de contact.
- Unde ne găsești: „Pe raft, în farmacie sau cu livrare acasă.”
- „Fără conservanți” apare pe v3 la „Ce e în mix”; ATENȚIE, e afirmație despre compoziție, se folosește doar dacă strategistul o consideră sigură (nu e afirmație de sănătate), altfel se omite.
- Secțiunea UGC de pe v3: „de la voi, pentru voi / Lucas Bites în viața reală / Rețete, momente și idei de la oameni care deja le savurează.”

Din site-ul actual (https://www.lucasbites.ro/termeni-si-conditii/):
- „Comenzile primite pana in ora 15:00 se proceseaza in aceeasi zi (valabil de luni pana vineri).”
- „Livrarea se face prin firme de curierat rapid in 24-48 ore valabil pentru zilele lucratoare.”
- „Nu avem o limită minimă pentru comandă.”
- Plata: card direct pe site, transfer bancar sau ramburs la livrare.
- Retur: în 5 zile de la recepție, anunțat în scris; transportul retur îl plătește clientul (nu se folosește ca USP).

Linkuri produse (site actual):
- Brownie Mix: https://www.lucasbites.ro/produs/brownie-mix-450g-2/
- Cookie Mix: https://www.lucasbites.ro/produs/cookie-mix-amestec-pentru-biscuiti-cu-ciocolata-neagra-450g/
- Crêpes Traditional: https://www.lucasbites.ro/produs/crepes-mix-traditional-280g-clatite-frantuzesti/
- Magazin: `{{SHOP_URL}}`; contact: https://www.lucasbites.ro/contact/ NU există (404); se folosesc mailto:office@lucasbites.ro și tel:+40731399399.

Rețete v3 nefolosite până acum care se potrivesc produselor cross-sell: „Brownie cu fructe de pădure” (Brownie Mix, 35 min, Desert), „Cookies cu ciocolată neagră” (Cookie Mix Dark Chocolate, 14 min, Desert). Crêpes: „Clătite pentru toată familia” a fost folosită în Email 1. Nu inventăm ingrediente sau pași.

## Reguli de brand (obligatorii)
- Doar 4 culori: portocaliu #FAA61A, roz #F7ACB4, turcoaz #86D2DA, negru #000000. Albul doar ca fundal.
- Pe culorile de brand textul e negru; pe negru, textul e doar portocaliu. Niciodată alb pe portocaliu, roz sau turcoaz.
- Ton prietenos, direct, jucăuș, simplu, apetisant. Engleză cât e nevoie. Fără „cel mai bun”, fără ton corporatist, fără moralizare, fără promisiuni de sănătate sau nutriționale.
- Fără emoji, fără em-dash. Plicata nu se folosește.

## Direcția vizuală
Referințele rămân aceleași ca în Email 1 și 2: **`refs/ref3.png`** (Blue Apron) și **`refs/ref4.png`** (BetterBrand: blocuri de culoare puternice, tăieturi diagonale și ondulate, mâncare decupată care iese din cadru, titluri foarte mari, packshot mare cu ingrediente în jur, CTA pill). Roșul din ref devine una din cele 4 culori de brand.
UI Designer păstrează familia vizuală din NC1 și NC2, dar evită să repete exact layout-urile lor (hero roz cu farfurii la colțuri și carduri albe rotunde din NC1; hero portocaliu cu ingrediente zburând și perechile rețetă+produs pe fundaluri alternate din NC2).
Idei de pattern-uri noi potrivite pentru Email 3 (UI decide): rând de 3 produse cu packshot, bandă de USP-uri cu iconițe simple desenate în culorile brandului, bloc social tip grilă de „poze de pe telefon” (mâncare generată, stil foto de client, fără fețe) cu tag @lucas_bites mare.

## Imagini
Mâncare: fără ambalaje inventate, fără text, fără fețe (mâinile sunt OK), fundal alb pentru decupaj (cu excepția pozelor stil „postare de client”, care pot fi fotografii întregi pătrate, nedecupate), diferite de pozele din new-customer-01, new-customer-02 și welcome 1-3. Ambalajele: doar din `packshots/`.
