# New Customer, Email 1: brief comun

**Client:** Lucas Bites. Sursa de adevăr: `clients/lucasbites/discovery.md` (citește-l integral).
**Emailurile gata:** `welcome-01/`, `welcome-02/`, `welcome-03/` (brief.md, copy.md, design-direction.md la Email 3, image-prompts.md, build.py, index.html). Acest email face parte din aceeași familie vizuală (logo, valuri, fonturi, footer), dar are layout propriu și NU e parte din seria welcome: e primul email după prima comandă.
**ESP:** theMarketer (confirmat de utilizator, 12.10.2026). HTML email-safe (tabele, CSS inline, 600px). Titluri în Akrobat (webfont deja convertit în `welcome-03/assets/fonts/`), text în Arial.

## Ce cere clientul pentru Email 1 (new customer)
- Mulțumire pentru comandă
- Rețete (clientul a scris „rețete de la clienți”)
- Creare de entuziasm pentru produsele comandate

Agentul Email Marketing Strategist poate adăuga secțiuni dacă sunt necesare (ex: ce urmează cu livrarea, cum se prepară, invitație socială, cross-sell ușor), cu justificare. Nu e email tranzacțional (confirmarea comenzii o trimite magazinul); e email de marketing post-achiziție.

## Decizii luate cu utilizatorul (12.10.2026)
1. **Rețetele** sunt rețetele brandului de pe site (lucasbites.ro, secțiunea REȚETE și rețetele animate de pe propunere-v3: „Pancakes cu afine și sirop”, „Teancul de duminică”, „Clătite pentru toată familia”). Le prezentăm ca rețete Lucas Bites, NU ca rețete trimise de clienți. Nu inventăm rețete, cantități sau pași: tot ce apare se citește de pe site (citește paginile, notează URL-ul și data). Adăugăm o invitație „trimite-ne rețeta ta / etichetează-ne cu @lucas_bites și #lucasbites”, ca rețetele clienților să poată veni în viitor.
2. **Produsele comandate** apar într-un **bloc dinamic din comandă** (date din theMarketer). Layout-ul se construiește cu placeholdere pentru produs (imagine, nume, link) și cu un conținut de rezervă generic, dacă datele lipsesc. **Sintaxa de merge tags / blocuri dinamice theMarketer NU se ghicește**: se verifică în documentația oficială theMarketer. Dacă nu se poate confirma, se folosesc placeholdere generice clar marcate `{{ORDER_PRODUCT_NAME}}` etc. și se notează la „Întrebări / de verificat”.
3. **Imaginile** le generează utilizatorul pe higgsfield.ai din `image-prompts.md`, cu aceleași setări ca la Email 2 și 3: GPT Image, High, 2K, fundal alb simplu pentru decupaje, niciodată „transparent background”. Salvate în `new-customer-01/images/`.

## Context util
- Promisiune de preparare (site): „Ai poftă? Gata în 5 minute.” 3 pași pancakes: 1 Adaugi apă (în sticlă, până la semn) / 2 Agiți și torni (4–5 agitări) / 3 Gătești (când apar bulele, întorci o dată, încă un minut). „Enjoy!”
- Povestea brandului (discovery 8b): numit după Luca, copilul fondatorilor; „Pankees” era cuvântul lui.
- Dovadă: „Peste 1.100 de recenzii, cu o medie de 4,9 din 5” (valabil 10.10.2026). Transport gratuit de la al 2-lea produs (de confirmat la lansare). Fără prețuri, fără coduri de reducere (prețurile sunt în lucru), dacă clientul nu decide altfel.
- Social: Instagram https://www.instagram.com/lucas_bites/ · TikTok https://www.tiktok.com/@lucas.bites.ro · Facebook https://www.facebook.com/Lucas-Bites-101759484548844 · YouTube https://www.youtube.com/@lucasbites2267
- Footer identic cu emailurile welcome.
- Linkurile site-ului nou: `{{SHOP_URL}}/...` (placeholder până la lansare).

## Reguli de brand (obligatorii)
- Doar 4 culori: portocaliu #FAA61A, roz #F7ACB4, turcoaz #86D2DA, negru #000000. Albul doar ca fundal.
- Pe culorile de brand textul e negru; pe negru, textul e doar portocaliu. Niciodată alb pe portocaliu, roz sau turcoaz.
- Ton prietenos, direct, jucăuș, simplu, apetisant. Engleză cât e nevoie. Fără „cel mai bun”, fără ton corporatist, fără moralizare, fără promisiuni de sănătate (vezi afirmațiile interzise din discovery 8b).
- Fără emoji, fără em-dash.
- Plicata doar ca imagine și doar după licență (deci NU în acest draft).

## Direcția vizuală
Referința clientului pentru acest email: **`refs/ref3.png`** (Blue Apron, 3 variante de layout pe o singură imagine). Pattern-uri vizibile: farfurii fotografiate de sus care ies din cadru, tranziții curbe mari între secțiuni (alb / bleumarin), titluri serif mari centrate, butoane pastilă, listă de carduri albe cu imagine circulară + titlu + text + buton mic („Gluten-Free / Vegetarian...”), grid 2 x 2 de carduri, zig-zag farfurie + etichetă-bandă („Chef Favorites”, „Wellness”), bloc „Don't just take our word for it” cu stele, poză lifestyle cu cutia de livrare.
Traducere în brandul nostru: bleumarinul devine una din cele 4 culori de brand (fără culori noi), serif-ul devine Akrobat. UI Designer alege pattern-urile și notează ce s-a folosit deja în welcome 1-3, ca emailul să nu fie o copie.

## Imagini
Doar mâncare, fără ambalaje inventate (nu avem fotografii de ambalaj, deci și „cutia de livrare” din ref3 nu se generează cu ambalaj Lucas Bites inventat), fără text în imagine, fără fețe (mâinile sunt OK). Decupaje cu fundal alb simplu. Fotografiile trebuie să difere de cele din welcome 1-3 (vezi `image-prompts.md` din toate trei). Imaginile produselor comandate vin din feed-ul theMarketer, nu se generează.
