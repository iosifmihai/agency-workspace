# Hambar: Welcome Email 1, strategie, structură și copy final

Surse: `brief.md`, `clients/hambar/discovery.md`, `refs/site-hero-bunvenit.png`, textele site-ului hambar.ro (citite pe 2026-10-15). Legendă: [din site] = text preluat ca atare de pe hambar.ro, [adaptat] = text de pe site ajustat pentru email, [nou] = text nou, de aprobat de client.

---

## 1. Obiectiv, KPI, trimitere

**Obiectiv:** cont creat pe hambar.ro, ca pas spre prima comandă cu codul BUNVENIT. **KPI principal:** rata de click unic pe `{{SIGNUP_URL}}` raportată la emailurile livrate (țintă 8%+, alertă sub 3%). **KPI secundar:** rata de click unic pe oricare dintre cele 6 categorii sau pe "Toate categoriile" (țintă 4%+, alertă sub 1,5%). **KPI de business (urmărit la nivel de serie):** prima comandă cu codul BUNVENIT în 14 zile de la abonare.

**Trigger:** abonare la newsletter din pop-up, wait 1 minut, o singură dată per contact (fără re-entry). **Excluderi:** contacte dezabonate/suprimate; contacte care au deja o comandă (acestea intră în Post-purchase). **Ieșire din serie:** prima comandă, dezabonare, hard bounce, plângere spam, final de secvență (trece în newsletter).

Gărzi de siguranță (opresc trimiterea dacă sunt depășite): plângeri spam sub 0,10%, dezabonări sub 0,5%, hard bounce sub 1%. Rata de deschidere se citește doar orientativ (Apple MPP o umflă).

---

## 2. Subiecte și preheadere

| # | Subiect | Caractere | Preheader |
|---|---|---|---|
| A **[recomandat]** | Bun venit în Hambar. Ai 50 de lei pentru prima comandă | 54 | Codul BUNVENIT, la prima comandă de minimum 250 de lei. |
| B | Mulțumim că ai intrat în Hambar | 31 | Îți lăsăm aici codul BUNVENIT și ce găsești la noi. |
| C | Codul tău BUNVENIT te așteaptă | 30 | 50 de lei la prima comandă, de la producători verificați. |

De ce A: e un email așteptat (abonatul tocmai a văzut oferta în pop-up), deci claritatea bate curiozitatea. Subiectul repetă exact titlul și oferta de pe site ("Bun venit în Hambar", "50 de lei discount la prima comandă"), se găsește ușor prin căutare în inbox, iar preheaderul pune condiția (minimum 250 de lei) din prima, ca să nu apară surpriza în coș. Pe mobil, primele ~35 de caractere ("Bun venit în Hambar. Ai 50 de lei") duc deja mesajul. B este varianta de test A/B (ton mai cald, oferta mutată în preheader) după primele ~500 de trimiteri. Câștigătorul se măsoară pe click pe `{{SIGNUP_URL}}`, nu pe deschideri.

**Expeditor:** Hambar. **Reply-to:** contact@hambar.ro (adresă monitorizată).

---

## 3. Structura, de sus în jos

Lățime 600px, o coloană (mobil întâi). Fundal corp #f7f6f5, text #241e1e. Titluri: `"Louize Display", Georgia, "Times New Roman", serif`. Text: `"GT America", Helvetica, Arial, sans-serif`, 16px, paragrafe scurte. Butoane: pastilă #c93f13 cu text alb (5.0:1), construite ca butoane HTML "bulletproof" cu VML pentru Outlook, nu ca imagini. Textul secundar #877b71 nu se folosește (eșuează contrastul); verde, mov și galben accent doar decorativ.

Șapte secțiuni: S0 header, S1 hero, S2 brand, S3 cont + cod, S4 categorii, S5 încredere, S6 footer.

---

### S0-header

- **Scop:** recunoaștere imediată a brandului.
- **Fundal:** #f7f6f5.
- **Conținut:** logo `clients/hambar/logos/hambar-logotype.svg` exportat PNG (2x), culoare originală #241e1e, centrat, afișat la 160px lățime. Fără meniu, ca să nu concureze cu CTA-ul principal.
- **Imagine:** nu (doar logo).

---

### S1-hero

- **Scop:** mulțumire, bun venit și oferta în primul ecran pe mobil.
- **Fundal:** fotografie IMG1 pe toată lățimea, cu text alb peste zona întunecată a imaginii (fallback: culoare de fundal #413535 sub imagine, ca textul alb să rămână lizibil dacă imaginea e blocată). În Outlook, fundalul se pune cu VML.
- **Copy:**
  - Titlu: **Bun venit în Hambar** [din site]
  - Text: Mulțumim că te-ai abonat. Ai 50 de lei discount la prima comandă cu codul BUNVENIT. [adaptat]
  - CTA (pastilă #c93f13, text alb): **Creează-ți contul** → `{{SIGNUP_URL}}` [nou]
  - Sub buton, text mic alb: Ofertă valabilă la prima comandă, de min. 250 de lei. [din site]
- **Ordinea pe mobil:** titlu, text, buton, text mic. Butonul trebuie să fie vizibil fără scroll.
- **IMG1 (descriere):** interior rustic cald, lumină de după-amiază prin fereastră cu umbre pe perete, o masă de lemn cu ulcior de lut, borcan de zacuscă, o pâine rotundă și un fagure de miere, tonuri maro-miere, cu spațiu liber întunecat în stânga-sus pentru text (fără etichete, fără text în imagine). Raport 4:5, export 1200x1500px.

---

### S2-brand

- **Scop:** spune în 3-4 rânduri ce este Hambar (mâncare românească de la producători mici), ca abonatul să știe de ce merită contul.
- **Fundal:** #f7f6f5.
- **Copy:**
  - Titlu: **Produse locale de la producători din România, livrate acasă** [din site]
  - Text: Ai luat o brânză extraordinară la un târg și n-ai mai găsit-o niciodată. Ai comandat miere dintr-un grup și ai primit un borcan fără etichetă. [din site]
  - Text: În Hambar găsești producători din toată țara, într-un singur loc. Nu vezi "vânzător", vezi un om cu nume și cu loc. Fiecare îți trimite direct ce ai comandat de la el, fără depozit la mijloc. [adaptat]
- **Imagine:** nu (secțiune de text, scurtă).

---

### S3-cont-si-cod

- **Scop:** motivul concret pentru care contul merită (KPI principal) și codul afișat clar, ușor de copiat.
- **Fundal:** #efedea (bloc distinct față de restul corpului).
- **Copy:**
  - Titlu: **Contul tău, primul pas spre cei 50 de lei** [nou]
  - Text: Ca să comanzi pe Hambar ai nevoie de un cont. Durează un minut și te ajută și după prima comandă: [adaptat]
  - Listă (3 rânduri, cu bife desenate ca text, nu ca emoji):
    - Îți vezi comenzile vechi. [din site]
    - Urmărești coletele. [din site]
    - Îți salvezi adresele și poți comanda din nou ce ți-a plăcut. [adaptat]
  - Casetă cod (chenar #241e1e, 2px, fundal #f7f6f5, text live, selectabil):
    - Etichetă mică: Codul tău [nou]
    - Cod, mare, Louize Display: **BUNVENIT**
    - Text: 50 de lei discount la prima comandă, de min. 250 de lei. [adaptat]
  - CTA (pastilă #c93f13, text alb): **Creează-ți contul** → `{{SIGNUP_URL}}` [nou]
  - Text mic sub buton: Comanda minimă este de 50 de lei per producător, iar livrarea se calculează pentru fiecare producător din coș. Costul exact îl vezi în coș, înainte de plată. [adaptat]
- **Notă:** textul mic previne surpriza din coș (obiecție principală din discovery 2). Nu promite livrare gratuită. Nu se adaugă termen de valabilitate pentru cod.
- **Imagine:** nu.

---

### S4-categorii

- **Scop:** arată ce poți cumpăra (KPI secundar) și dă al doilea punct de click pentru cine a trecut de CTA.
- **Fundal:** #f7f6f5.
- **Copy:**
  - Titlu: **Din cămara Hambar** [din site]
  - Text: Șase categorii de unde să începi. [nou]
- **Grilă 2x3 pe desktop, o coloană pe mobil (sau 2 coloane cu imagini mai mici).** Fiecare card: imagine 1:1 (export 560x560px, afișat la 280px), nume categorie ca link, descriere de un rând. Imaginea și numele duc la același URL.
  1. **Zacuscă & Murături** → https://hambar.ro/categorie/zacusca-si-muraturi
     - Text: Zacuscă de vinete, de ciuperci sau de fasole, legume în borcan și murături în saramură sau în oțet. [din site]
     - IMG2: borcan deschis de zacuscă de vinete lângă un castron de murături în saramură (castraveți, gogoșari), pe masă de lemn, lumină caldă laterală.
  2. **Brânzeturi & Lactate** → https://hambar.ro/categorie/branzeturi-si-lactate
     - Text: Brânzeturi și lactate de la ferme și stâne din toată țara. [adaptat]
     - IMG3: roată de brânză maturată tăiată, câteva felii și o bucată de telemea pe o planșetă de lemn, fără etichete.
  3. **Carne, Mezeluri & Pește** → https://hambar.ro/categorie/carne-si-mezeluri
     - Text: Carne și mezeluri din porc, mangaliță, vită, pui și vânat, plus pește. [adaptat]
     - IMG4: platou de lemn cu cârnați afumați, slănină și felii de mușchi țigănesc, câteva fire de cimbru.
  4. **Miere & Dulcețuri** → https://hambar.ro/categorie/miere-si-dulceturi
     - Text: Miere, dulcețuri și magiun, pentru cămară și pentru micul dejun. [adaptat]
     - IMG5: borcan de miere cu linguriță de lemn din care curge mierea, lângă un borcan de dulceață de cireșe, lumină de după-amiază.
  5. **Pâine și Patiserie** → https://hambar.ro/categorie/paine-si-patiserie
     - Text: Pâine, cozonac și patiserie de la brutării locale. [adaptat]
     - IMG6: pâine rotundă cu coajă crocantă, ruptă, și câteva felii de cozonac cu nucă pe un ștergar țesut.
  6. **Coșuri și Cadouri** → https://hambar.ro/categorie/cosuri-si-cadouri
     - Text: Pachete care combină mai multe produse, pentru ocazii speciale. [din site]
     - IMG7: coș de nuiele cu borcane fără etichete, o sticlă de vin fără etichetă, brânză și un ștergar, pe masă rustică.
- **Link sub grilă (text #241e1e, subliniat):** **Vezi toate categoriile** → https://hambar.ro [nou]
- **Notă:** descrierile 2-6 sunt construite din FAQ-ul site-ului ("Ce fel de produse găsesc pe Hambar?") și din paginile Cum livrăm / Misiunea Hambar; doar Zacuscă & Murături are descriere proprie de categorie în textele citite. Dacă paginile de categorie au descrieri proprii, le înlocuim cu ele.

---

### S5-incredere

- **Scop:** răspunde la "de ce să am încredere?" înainte de prima comandă, cu diferențiatorul principal (verificare la fața locului).
- **Fundal:** #efedea.
- **Copy:**
  - Supratitlu mic: Producător verificat [din site]
  - Titlu: **Până acum, verificarea o făceai tu** [din site]
  - Text: Un om din echipa noastră merge la fiecare producător, la locul unde se face produsul. Se uită, întreabă, gustă. Badge-ul "Producător verificat" nu se cumpără și nu se dă la distanță. [adaptat]
  - Link text (#241e1e, subliniat): **Cum selectăm producătorii** → https://hambar.ro/cum-selectam-producatorii [din site]
- **IMG8 (descriere):** mâini care țin o roată de brânză sau un borcan de miere într-un atelier rural cu lumină naturală, fără fețe, fără etichete, tonuri calde maro-miere; ilustrează "mergem la sursă". Raport 3:2, export 1200x800px, afișat la 600px.
- **Notă:** nu se enumeră criteriile, nu se dau cifre de producători și nu se prezintă badge-ul drept certificare oficială (discovery 9).

---

## 4. Footer (S6-footer)

- **Fundal:** #413535, text #efedea.
- **Logo:** `hambar-logotype-white.svg` exportat PNG (2x), centrat, 140px lățime.
- **Tagline:** Gust adevărat, de la oameni buni livrat [din site, tagline oficial]
- **Aplicație (rând de text-linkuri, nu badge-uri imagine):** Descarcă aplicația: **App Store** → https://apps.apple.com/ro/app/hambar/id6794062859 · **Google Play** → https://play.google.com/store/apps/details?id=ro.hambar.client
- **Iconițe social** (albe, 28px, assets UI): Facebook → https://www.facebook.com/hambar.romania · Instagram → https://www.instagram.com/hambar_ro/ · TikTok → https://www.tiktok.com/@hambar.ro · YouTube → https://www.youtube.com/@Hambar_ro
- **Linkuri utile:** Cum livrăm → https://hambar.ro/cum-livram · Cum selectăm producătorii → https://hambar.ro/cum-selectam-producatorii
- **Copy:**

> Hambar Marketplace SRL · CUI 54747901
> contact@hambar.ro
>
> Primești acest email pentru că te-ai abonat la newsletterul Hambar pe hambar.ro.
>
> Nu mai vrei emailuri de la noi? [Dezabonează-te aici]({{UNSUBSCRIBE_URL}}). Durează un click.
>
> © 2026 Hambar

- **Tehnic:** `{{UNSUBSCRIBE_URL}}` se înlocuiește cu tag-ul de dezabonare din theMarketer. Header-ele `List-Unsubscribe` + `List-Unsubscribe-Post` (one-click, RFC 8058) trebuie să fie active. Domeniul hambar.ro trebuie adăugat și autentificat (SPF, DKIM, DMARC) în theMarketer înainte de lansare (discovery 10).

---

## 5. Linkuri (rezumat)

| Element | URL |
|---|---|
| CTA hero, CTA S3 | `{{SIGNUP_URL}}` [de confirmat: URL-ul paginii de înregistrare] |
| 6 categorii | URL-urile din S4 |
| Vezi toate categoriile | https://hambar.ro |
| Cum selectăm producătorii | https://hambar.ro/cum-selectam-producatorii |
| Cum livrăm | https://hambar.ro/cum-livram |
| Aplicație, social | vezi S6 |

Toate linkurile spre hambar.ro primesc UTM: `utm_source=themarketer&utm_medium=email&utm_campaign=welcome&utm_content=w1-<secțiune>` (ex. `w1-hero`, `w1-cont`, `w1-cat-zacusca`), ca să vedem ce bloc aduce conturi.

---

## 6. Alt text

| Imagine | Alt text |
|---|---|
| Logo header | Hambar |
| IMG1 (hero) | Masă rustică cu zacuscă, pâine, miere și un ulcior de lut, în lumina de după-amiază |
| IMG2 | Zacuscă de vinete și murături în saramură |
| IMG3 | Brânză maturată și telemea pe o planșetă de lemn |
| IMG4 | Platou cu cârnați afumați, slănină și mușchi țigănesc |
| IMG5 | Miere curgând dintr-o linguriță, lângă un borcan de dulceață |
| IMG6 | Pâine rotundă și felii de cozonac cu nucă |
| IMG7 | Coș cadou cu borcane, brânză și vin |
| IMG8 | Mâini care țin o roată de brânză într-un atelier |
| Logo footer | Hambar, gust adevărat, de la oameni buni livrat |
| Iconițe social | Facebook / Instagram / TikTok / YouTube (câte una pe iconiță) |

---

## 7. Note

- **Ce nu apare în email (intenționat):** ramburs, livrare gratuită, termen de valabilitate pentru cod, cifre (număr de producători/produse), nume de producători, "BIO"/"ECO", retur. Nu sunt necesare aici și unele au reguli stricte (discovery 9-10).
- **Dublarea CTA-ului:** "Creează-ți contul" apare de două ori (hero și S3), cu aceeași destinație. Categoriile sunt CTA secundar; dacă un abonat dă click pe o categorie fără cont, site-ul îi va cere contul la checkout.
- **Lizibilitate cu imagini blocate:** toate titlurile, textele, codul și butoanele sunt text HTML live. Hero-ul are culoare de fundal #413535 ca rezervă.
- **Webfonturi:** Louize Display și GT America se încarcă doar în Apple Mail / iOS; restul clienților văd Georgia și Helvetica/Arial. Opțional, titlul hero poate fi imagine randată cu Louize Display, cu titlul complet în alt.
- **Imagini (Higgsfield):** stilul referinței `refs/site-hero-bunvenit.png` (lumină caldă de după-amiază, lemn, lut, tonuri maro-miere). Doar mâncare românească reală, fără ambalaje sau etichete inventate, fără text, fără fețe (mâinile sunt OK). Export 2x, JPG optimizat sub 200 KB. Imaginile de categorie (IMG2-7) trebuie să aibă aceeași lumină și același unghi (45 de grade), ca grila să arate unitar. Alternativ, dacă clientul preferă, IMG2-7 pot fi fotografii reale de produs de pe site (Hambar deține drepturile, discovery 7).
- **De confirmat înainte de construire:** `{{SIGNUP_URL}}`; dacă codul BUNVENIT se aplică automat sau se introduce manual în coș (dacă e automat, textul "cu codul BUNVENIT" rămâne, dar adăugăm "se aplică la checkout").
