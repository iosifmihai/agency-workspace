# Lucas Bites: Welcome Email 1, strategie, structură și copy final

Surse: `brief.md`, `discovery.md`, `refs/ref1-4.png`. Legendă: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [adaptat] = text aprobat ajustat pentru email, [nou] = text nou, de aprobat de client.

---

## 1. Obiectiv, KPI, trimitere

**Obiectiv:** livrarea ghidului PDF și primul follow pe social. **KPI principal:** rata de click unic pe {{GUIDE_PDF_URL}} raportată la emailurile livrate (țintă 35%+, alertă sub 20%). **KPI secundar:** rata de click unic pe oricare dintre cele 4 linkuri social (țintă 3%+, alertă sub 1%). **Trigger:** imediat după înscriere (sau imediat după confirmare, dacă formularul folosește double opt-in), o singură dată per contact, cu excluderea contactelor dezabonate/suprimate.

Gărzi de siguranță (nu sunt KPI, dar opresc trimiterea dacă sunt depășite): plângeri spam sub 0,10%, dezabonări sub 0,5%, hard bounce sub 1%. Rata de deschidere se citește doar orientativ (Apple MPP o umflă).

---

## 2. Subiecte și preheadere

| # | Subiect | Caractere | Preheader |
|---|---|---|---|
| A **[recomandat]** | Ghidul tău e aici: 10 rețete Jamila | 35 | Pancakes, clătite și deserturi. Alege ce faci primul. |
| B | Ai poftă? Rețetele tale sunt aici | 33 | Descarcă ghidul gratuit și fă primul teanc de pancakes azi. |
| C | Ți-am adus 10 rețete. Enjoy! | 28 | Ghidul cu rețete Jamila te așteaptă, gata de descărcat. |

De ce A: e un email așteptat (abonatul tocmai a cerut ghidul), deci claritatea bate curiozitatea. Subiectul repetă exact promisiunea din formular, se găsește ușor prin căutare în inbox și reduce riscul de „ce e asta?” care duce la plângeri. B este varianta de test A/B după primele ~500 de trimiteri, dacă vreți să testați tonul jucăuș. Măsurați câștigătorul pe click pe ghid, nu pe deschideri.

**Expeditor:** Lucas Bites. **Reply-to:** o adresă monitorizată (ex. office@lucasbites.ro), pentru că S6 invită la reply.

---

## 3. Structura, de sus în jos

Lățime 600px, layout pe o coloană (mobil întâi). Titluri: `Akrobat, "Arial Narrow", Arial, sans-serif`, bold, mari. Text: `Arial, Helvetica, sans-serif`, 16px, paragrafe de 1-2 rânduri. Text negru #000000 pe orice culoare de brand; pe negru, text doar portocaliu #FAA61A. Butoane pill (colțuri complet rotunjite), construite ca butoane HTML „bulletproof”, nu ca imagini.

Tranziții între secțiuni: valuri (stil Blue Apron / BetterBrand), ca benzi PNG decorative de 600px lățime, cu `alt=""`. Ele și logo-ul nu intră în limita de 6 fotografii.

---

### S0-header

- **Scop:** recunoaștere imediată a brandului.
- **Fundal:** alb.
- **Conținut:** logo `Logo/Logo_LucasBites.png` (un rând), centrat, afișat la 180px lățime (export 360px pentru retina). Fără meniu, ca să nu concureze cu CTA-ul principal.
- **Imagine:** nu (doar logo).

---

### S1-hero

- **Scop:** confirmă că ghidul a ajuns și duce la click în primul ecran pe mobil.
- **Fundal:** portocaliu #FAA61A. Trecere cu val spre alb la bază.
- **Copy:**
  - Supratitlu: **Bine ai venit la Lucas Bites!** [nou]
  - Titlu: **Rețetele tale au ajuns.** [nou]
  - Subtitlu: **oricine le poate face, repede** [din site]
  - Text: Mulțumim că te-ai abonat. Ghidul „10 rețete Jamila cu produse Lucas Bites” e la un click distanță. [nou]
  - CTA (pill negru, text portocaliu): **Descarcă ghidul** → `{{GUIDE_PDF_URL}}` [nou]
  - Sub buton, text mic: PDF gratuit, se deschide și pe telefon. [nou]
- **Ordinea pe mobil:** supratitlu, titlu, subtitlu, text, buton, apoi fotografia. Butonul trebuie să fie vizibil fără scroll.
- **IMG1 (spec):**
  - Ce arată: un teanc înalt de 5-6 pancakes pufoase, aurii, cu sirop care curge pe margini, afine proaspete pe vârf și pe lângă, o bucățică de unt care se topește.
  - Încadrare: unghi de 45 de grade, ușor de jos, ca teancul să pară monumental. Decupat (PNG cu fundal transparent), ca teancul să „iasă” din blocul portocaliu și să treacă peste valul alb (stil BetterBrand).
  - Raport: 4:5 (export 1200x1500px, afișat la 480px lățime, centrat).
  - Atmosferă: răsfăț de weekend, lumină caldă de dimineață, sirop lucios, textură pufoasă vizibilă în secțiune.

---

### S2-ghid

- **Scop:** arată ce e în ghid, ca să crească pofta și click-ul (al doilea punct de click pentru cine a dat scroll peste hero).
- **Fundal:** alb.
- **Copy:**
  - Titlu: **10 rețete. Fără cântar și fără bătaie de cap.** [adaptat]
  - Text: Mixurile noastre au deja aproape tot în ele. Ghidul îți arată ce poți face cu ele, de la micul dejun la desert. [adaptat]
- **3 carduri (imagine circulară sus, text dedesubt, stil Blue Apron), pe mobil unul sub altul, pe desktop 3 pe rând:**
  1. **Mic dejun:** Pancakes pufoase, gata înainte să se răcească cafeaua. [nou]
  2. **Weekend:** Clătite pentru toată familia. [din site]
  3. **Desert:** Brownie și prăjituri, pentru când îți e poftă de ceva dulce. [nou]
- **CTA (pill portocaliu, text negru):** **Vreau rețetele** → `{{GUIDE_PDF_URL}}` [nou]
- **De verificat înainte de trimitere:** cele 3 categorii presupun că ghidul conține pancakes, clătite și un desert. Dacă PDF-ul are alt conținut, înlocuim cardurile cu 3 rețete reale din ghid (nume exact + fotografie potrivită).
- **IMG2 (spec):**
  - Ce arată: o farfurie cu 3 pancakes așezate în evantai, fructe de pădure, un fir de sirop.
  - Încadrare: de sus (overhead), farfuria centrată, umple ~85% din cadru.
  - Raport: 1:1 (export 400x400px, afișat la 200px), livrat deja decupat în cerc (PNG cu colțuri transparente), pentru că Outlook ignoră `border-radius`.
  - Atmosferă: luminos, proaspăt, mic dejun relaxat.
- **IMG3 (spec):**
  - Ce arată: clătite subțiri împăturite în triunghiuri, cu dulceață și puțină zahăr pudră, pe o farfurie.
  - Încadrare: de sus, farfuria centrată.
  - Raport: 1:1, decupat în cerc, ca IMG2.
  - Atmosferă: familiar, de casă, cald.
- **IMG4 (spec):**
  - Ce arată: pătrate de brownie cu crustă lucioasă crăpată și interior umed, o bucată ruptă care arată textura.
  - Încadrare: de sus, ușor înclinat (până la 15 grade) ca să se vadă grosimea.
  - Raport: 1:1, decupat în cerc, ca IMG2.
  - Atmosferă: intens, ciocolatos, „mai iau o bucată”.

---

### S3-pasi

- **Scop:** demonstrează simplitatea (mesajul cheie 1) și justifică descărcarea: „chiar pot face asta”.
- **Fundal:** turcoaz #86D2DA.
- **Copy:**
  - Titlu: **Ai poftă? Gata în 5 minute.** [din site]
  - Text: Pancakes, în 3 pași: [adaptat]
  - **1. Adaugi apă** (în sticlă, până la semn) [din site]
  - **2. Agiți și torni** (4–5 agitări) [din site]
  - **3. Gătești** (când apar bulele, întorci o dată, încă un minut) [din site]
  - **Enjoy!** [din site]
  - Link text (negru, subliniat): Mai multe idei găsești în ghid → `{{GUIDE_PDF_URL}}` [nou]
- **Notă:** cifrele 1-2-3 ca text mare Akrobat (negru), nu ca iconițe-imagine.
- **IMG5 (spec):**
  - Ce arată: o tigaie cu 3 pancakes rotunde în timp ce se gătesc, cu bule vizibile la suprafață; o mână ține o spatulă gata să întoarcă unul. Fără sticlă, fără ambalaj în cadru.
  - Încadrare: macro, la 45 de grade, profunzime mică de câmp (bulele clare, marginea tigăii estompată).
  - Raport: 3:2 (export 1200x800px, afișat la 600px, full width).
  - Atmosferă: acțiune, bucătărie acasă, lumină caldă naturală, ușor de reprodus.

---

### S4-recenzii

- **Scop:** dovadă socială scurtă, care confirmă că rețetele „chiar ies”.
- **Fundal:** roz #F7ACB4.
- **Copy:**
  - Titlu: **Peste 1.100 de recenzii, cu o medie de 4,9 din 5** [din site]
  - Citat: „Au ieșit excelent și au fost foarte ușor de preparat. Mi-a plăcut în mod deosebit că nu au fost dulci.” [din site]
  - Semnătură: Kinga Ludescher, Classic Pankees [din site]
- **Imagine:** nu. Fără stele-emoji; dacă vreți stele, sunt iconițe PNG negre (asset UI, nu fotografie).
- **Notă:** cifra 1.100 / 4,9 e valabilă la 10.10.2026. Se verifică la fiecare actualizare a fluxului.

---

### S5-social

- **Scop:** follow pe social (KPI secundar). Instagram și TikTok primele, pentru publicul de 20-35 de ani.
- **Fundal:** negru #000000, cu val de intrare din roz. Tot textul în portocaliu #FAA61A (singura combinație permisă pe negru).
- **Ordine:** fotografia sus, apoi textul și butoanele.
- **Copy:**
  - Titlu: **Ce gătești, arată-ne.** [nou]
  - Text: Etichetează-ne. Postează ce ai pregătit cu @lucas_bites și #lucasbites. [din site, trunchiat]
  - Text: Între două newslettere, găsești idei noi pe paginile noastre. [nou]
  - Buton 1 (pill portocaliu, text negru): **Urmărește-ne pe Instagram** → https://www.instagram.com/lucas_bites/
  - Buton 2 (pill portocaliu, text negru): **Urmărește-ne pe TikTok** → https://www.tiktok.com/@lucas.bites.ro
  - Linkuri text (portocaliu, subliniat), pe un rând: **Facebook** → https://www.facebook.com/Lucas-Bites-101759484548844 · **YouTube** → https://www.youtube.com/@lucasbites2267
- **IMG6 (spec):**
  - Ce arată: o masă plină, văzută de sus: pancakes cu fructe, clătite rulate, brownie, câteva brioșe, cești de cafea; 2-3 mâini (fără fețe) se întind spre farfurii.
  - Încadrare: de sus (overhead), compoziție aglomerată, „de feed”.
  - Raport: 1:1 (export 1200x1200px, afișat la 600px, full width).
  - Atmosferă: social, vesel, „brunch cu prietenii”. Fundal de masă închis la culoare (lemn închis sau ardezie) ca să se lege de secțiunea neagră; accente de recuzită în portocaliu, roz și turcoaz (șervețele, farfurii), fără niciun text.

---

### S6-ce-urmeaza

- **Scop:** respectă promisiunea din formular (lunar, fără spam), anunță transparent următoarele emailuri din serie și cere un reply (semnal bun de livrabilitate).
- **Fundal:** alb.
- **Copy:**
  - Titlu: **Ce urmează** [nou]
  - Text: În zilele următoare îți mai trimitem câteva idei, ca să începi cu dreptul. Apoi ne auzim o dată pe lună, cu idei noi și noutăți. Fără spam. [adaptat]
  - Text: Până atunci, spune-ne: ce faci primul din ghid? Dă reply la emailul ăsta. [nou]
  - Text: Mixurile Lucas Bites le găsești în Kaufland, Carrefour, Dr. Max, Farmacia Tei, Bebe Tei, eMAG, Freshful și online. [adaptat]
  - Link text (negru, subliniat): **Vezi toate mixurile** → `{{SHOP_URL}}` [nou] (URL-ul paginii PRODUSE, de confirmat la lansarea site-ului)
  - Semnătură: **eat what you love** [din site, slogan oficial]
- **Imagine:** nu.

---

## 4. Footer (S7-footer)

- **Fundal:** alb, separat de S6 printr-o linie neagră subțire.
- **Logo:** `Logo/Logo_LucasBites_stripes-nobg.png`, centrat, 200px lățime.
- **Iconițe social** (negre, 32px, assets UI): Instagram, TikTok, Facebook, YouTube, cu aceleași linkuri ca în S5.
- **Copy:**

> Lucas Bites · Roșu, Chiajna, Ilfov
> office@lucasbites.ro · +40 731 399 399
>
> Primești acest email pentru că te-ai abonat pe lucasbites.ro la ghidul de rețete și la newsletterul nostru lunar.
>
> Nu mai vrei emailuri de la noi? [Dezabonează-te aici]({{UNSUBSCRIBE_URL}}). Durează un click.
>
> © 2026 Lucas Bites

- **Tehnic:** `{{UNSUBSCRIBE_URL}}` se înlocuiește cu tag-ul de dezabonare al ESP-ului ales. Header-ele `List-Unsubscribe` + `List-Unsubscribe-Post` (one-click, RFC 8058) trebuie să fie active.
- **De confirmat:** denumirea juridică a firmei (SRL) și CUI, dacă vreți identificarea completă a comerciantului în footer.

---

## 5. Seria de welcome: ce urmează după Email 1

Spațiere recomandată: 4 emailuri în ~14 zile, apoi contactul trece în newsletterul lunar. Toate emailurile ies din serie la: dezabonare, hard bounce, plângere spam. Emailurile 3-4 exclud cumpărătorii, dacă ESP-ul primește date de comandă.

- **Email 2 (ziua 2):** o rețetă din ghid pas cu pas („Teancul de duminică”, stil BetterBrand cu listă de ingrediente) plus link spre YouTube; ramură: cine nu a dat click pe ghid în Email 1 primește linkul ghidului ca CTA principal.
- **Email 3 (ziua 6):** „Alege-ți pofta de azi”: gama de mixuri, ingredientele pe care le recunoști, unde le găsești și transport gratuit de la al 2-lea produs; dacă se aprobă un cod de reducere, aici e primul loc unde are sens, doar pentru necumpărători.
- **Email 4 (ziua 12-14):** comunitate: recenzii, poze de la abonați cu #lucasbites, invitație repetată la follow și tag; un rând discret pentru cine are cafenea sau restaurant (gama Professional), apoi trecere în newsletterul lunar.

Notă: formularul promite „o dată pe lună”. Email 1 anunță explicit cele câteva emailuri de început (S6), ca seria să nu pară spam. Nu prelungiți seria peste 4 emailuri.

---

## 6. Alt text

| Imagine | Alt text |
|---|---|
| Logo header | Lucas Bites |
| IMG1 (hero) | Teanc înalt de pancakes pufoase cu sirop și afine |
| IMG2 | Pancakes cu fructe de pădure și sirop, pe farfurie |
| IMG3 | Clătite împăturite cu dulceață și zahăr pudră |
| IMG4 | Pătrate de brownie cu crustă lucioasă |
| IMG5 | Pancakes cu bule în tigaie, gata de întors |
| IMG6 | Masă de brunch cu pancakes, clătite, brownie și brioșe |
| Logo footer | Lucas Bites, eat what you love |
| Iconițe social | Instagram / TikTok / Facebook / YouTube (câte una pe iconiță) |
| Valuri decorative | `alt=""` (decorativ) |

---

## Reguli pentru toate fotografiile (Higgsfield)

- Doar mâncare. Fără ambalaje, sticle sau pungi, fără text, logo-uri sau etichete în imagine, fără fețe (mâinile sunt OK).
- Lumină naturală caldă, texturi clare (pufos, lucios, crocant), apetisant, nu „de laborator”.
- Recuzita poate avea accente în portocaliu, roz și turcoaz; fără alte culori dominante puternice.
- Exporturi la 2x față de dimensiunea afișată; JPG optimizat sub 200 KB pentru fotografii, PNG doar pentru decupaje (IMG1 și cercurile IMG2-4).
- Emailul trebuie să rămână lizibil cu imaginile blocate: toate titlurile, textele și butoanele sunt text HTML live.
