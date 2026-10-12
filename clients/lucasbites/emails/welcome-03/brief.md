# Welcome series, Email 3: brief comun

**Client:** Lucas Bites. Sursa de adevăr: `clients/lucasbites/discovery.md`.
**Emailurile gata:** `welcome-01/` și `welcome-02/` (copy.md, index.html, build.py). Email 3 face parte din aceeași familie vizuală, dar are layout propriu, nu e o copie.
**ESP:** de confirmat. HTML email-safe (tabele, CSS inline, 600px). Titlurile în Akrobat (webfont-ul e deja convertit în `welcome-02/assets/fonts/`), textul în Arial.

## Ce cere clientul pentru Email 3
- Produse bestseller
- Recenzii clienți
- UGC

## Decizii luate cu utilizatorul (11.10.2026)
1. **Recenziile** sunt extrase de pe site-ul actual (lucasbites.ro, paginile de produs, citite la 11.10.2026). Doar recenzii reale, cu numele exact așa cum apare pe site. Nu inventăm și nu rescriem recenzii. Sunt permise doar corecturi de diacritice și eliminarea emoji-urilor, marcate [din site actual, diacritice corectate].
2. **UGC:** nu avem încă poze reale de la clienți. Layout-ul se construiește cu **placeholdere marcate vizibil** „POZĂ CLIENT, DE ÎNLOCUIT” (casete gri/roz, cu @handle placeholder). Utilizatorul le înlocuiește cu poze reale, cu acordul autorilor, înainte de trimitere. **Nu generăm cu Higgsfield poze prezentate ca venite de la clienți.**
3. **Bestsellers:** aleși de noi după numărul de recenzii (indiciu pentru volumul vânzărilor), marcați [de confirmat cu clientul].
4. **Imaginile Higgsfield** (doar fotografii de produs/mâncare, nu UGC): utilizatorul le generează pe higgsfield.ai din `image-prompts.md`. Folosește aceleași setări ca la Email 2: GPT Image, High, 2K, fundal alb simplu pentru decupaje, niciodată „transparent background”.

## Strategia utilizatorului + îmbunătățiri aprobate ca direcție
- Recenziile stau lângă produs: fiecare bestseller primește ratingul lui și o recenzie reală, chiar lângă CTA.
- Ordinea bestseller-elor se schimbă după tag-urile din Email 2 (`INTEREST_PANCAKES`, `INTEREST_PRAJITURI`, `INTEREST_PIZZA`, `INTEREST_BUDINCI`); există o ordine implicită pentru restul.
- Motivul să comande acum: **transport gratuit de la al 2-lea produs** (de pe site, de confirmat că e valabil la lansare). Fără cod de reducere, fără prețuri (prețurile sunt încă în lucru).
- UGC are două roluri: dovadă („așa arată la alții”) și invitație („postează cu @lucas_bites și #lucasbites”).
- Excludem cumpărătorii, dacă ESP-ul primește comenzile.
- Recenziile și UGC erau planificate în Email 4. Le mutăm în Email 3, iar Email 4 se replanifică: rețeta pas cu pas plus un rând pentru gama Professional (propunere de inclus în secțiunea de predare).

## Bestsellers și recenzii reale (lucasbites.ro, citit la 11.10.2026)

| Produs | Rating | Nr. recenzii | URL actual |
|---|---|---|---|
| Buttermilk Pankees 290g | 4,90 | 222 | https://www.lucasbites.ro/produs/buttermilk-pankees-290g/ |
| Classic Pankees 290g (marcat Bestseller pe site-ul nou) | 4,91 | 148 | https://www.lucasbites.ro/produs/clasic-pankees-290g/ |
| Pizza Crust Mix 500g | 4,80 | 80 | https://www.lucasbites.ro/produs/pizza-crust-mix-500g/ |
| Brownie Mix 450g | 5,00 | 11 | https://www.lucasbites.ro/produs/brownie-mix-450g-2/ |
| (rezervă) Lava Cake Mix 400g | 5,00 | 5 | https://www.lucasbites.ro/produs/lava-cake-400g/ |

Pe site-ul nou, linkurile devin `{{SHOP_URL}}/produse/<slug>`. Până atunci folosim placeholder.

Recenzii reale disponibile (text original, nume, data):

**Buttermilk Pankees**
- Carmen Nejloveanu (19.07.2021): „Extraordinar de bune, se prepara rapid iar copilul le adora!!!”
- Arabela (02.07.2021): „Clatitele perfecte!”
- Paula cristina Popa (19.06.2021): „Pufoase si delicoase”
- Roxana Hermenean (23.10.2021): „Cele mai delicioase”

**Classic Pankees**
- Andreea Hagiu (19.07.2021): „Clătitele ies foarte pufoase și gustoase. O adevărată plăcere să le faci și sa le mănânci 😅😋”
- Irina Stan (22.07.2021): „Sunt foarte încântată de aceste produse! Sunt minunate! Voi reveni cu comenzi!”
- Gabriela P. (17.07.2022): „Pufoase și delicioase!”
- Kinga Ludescher (deja aprobată, din site-ul nou): „Au ieșit excelent și au fost foarte ușor de preparat. Mi-a plăcut în mod deosebit că nu au fost dulci.” (folosită deja în Email 1; preferăm alta aici)

**Pizza Crust Mix**
- Irina Anghel (03.03.2022): „Am folosit amestecul pentru blat de pizza, Pizza Crust Mix, 500g si mi-au iesit doua pizza delicioase!”
- Luminita Blaga (23.04.2021, 4 stele): „Aleg mereu mixul Pizza Crust pentru o pizza rapida, cu ingrediente din frigider.”
- Paula cristina Popa (19.06.2021): „Blat intradevar pufos”

**Brownie Mix**
- FLOREA LILIANA (26.11.2023): „Bun. Rețeta este foarte buna”
- Valentina (15.11.2025): „Cele mai bune și pufoase mixuri pentru cele mai bune delicatese din lume. Le recomand din tot sufletul.💗💗” (NU o folosim: superlativul „cele mai bune” încalcă regulile de ton, chiar dacă e citat)

Atenție la conformitate: o recenzie e opinia clientului, dar dacă o alegem noi s-o punem în email, devine comunicarea brandului. Evităm citatele cu superlative absolute („cele mai bune din lume”) și cu afirmații de sănătate. Pentru folosirea numelor clienților în email, utilizatorul confirmă cu clientul (termenii site-ului / acordul pentru recenzii).

Dovada generală: „Peste 1.100 de recenzii, cu o medie de 4,9 din 5” (valabil 10.10.2026).

## Reguli de brand (obligatorii)
- Doar 4 culori: portocaliu #FAA61A, roz #F7ACB4, turcoaz #86D2DA, negru #000000. Albul doar ca fundal.
- Pe culorile de brand textul e negru; pe negru, textul e doar portocaliu. Niciodată alb pe portocaliu, roz sau turcoaz.
- Ton prietenos, direct, jucăuș, simplu, apetisant. Engleză cât e nevoie. Fără „cel mai bun”, fără ton corporatist, fără moralizare, fără promisiuni de sănătate.
- Fără emoji, fără em-dash.
- Footer-ul e identic cu Email 1 și Email 2.

## Direcția vizuală
Referințele de la client: `welcome-01/refs/ref1-4.png` și `welcome-02/refs/ref5-7.png` (descrise în `welcome-01/brief.md` și `welcome-02/brief.md`). Agentul UI alege din ele pattern-urile potrivite pentru bestsellers, recenzii și UGC, diferite de ce s-a folosit deja în Email 1 (carduri circulare, bloc social negru) și Email 2 (hero negru, zig-zag, grid de ingrediente). Candidați evidenți: ref5 Beguile (carduri albe de recenzii pe fundal închis), ref1 Botenz (best sellers), ref6 BetterBrand (carduri produs cu foto pătrat rotunjit).

## Imagini
Doar mâncare, fără ambalaje inventate, fără text în imagine, fără fețe (mâinile sunt OK). Decupajele se fac cu fundal alb simplu (fundalul îl scoatem local). Fotografiile trebuie să difere de cele din Email 1 și Email 2 (vezi `image-prompts.md` din ambele). Pozele UGC NU se generează.
