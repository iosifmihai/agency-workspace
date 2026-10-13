# Website Abandoned, Email 1: direcția de design

Autor: UI Designer, 13.10.2026. Bază: `strategy.md`, `copy.md` (inclusiv răspunsurile clientului din 13.10.2026), `brief.md`, `../README.md`, emailurile construite (welcome 01-03, new-customer 01-02, checkout-started 01-02, browse-abandonment 01: `design-direction.md` + `preview.png`) și referințele lor din `refs/` (welcome-01, welcome-02, checkout-started 01-02, browse 01 / Bello). Nu există referințe noi pentru acest email.
Textele sunt ale Copywriterului, preluate exact în `COPY`, `CATS` și `REVIEWS` din `build.py`.

Ideea vizuală: **„meniul casei, decupat din rețetar”**. H1-ul întreabă „CE PUNEM AZI PE MASĂ?”, iar emailul răspunde ca o pagină de meniu: categoriile sunt tăieturi de foto cu marginea de jos ruptă, prinse în carduri albe cu contur negru, iar secțiunile se despart prin aceeași **margine ruptă**, cu o dungă subțire de culoare între ele. Margine ruptă și dungi vin direct din banda logo-ului „stripes” (discovery 7: „bandă roz cu margine zdrențuită și dungi turcoaz și roz”), deci tranziția e a brandului, nu una împrumutată.

---

## 1. Ce preluăm din emailurile anterioare / ce e nou

| Preluăm | De unde | De ce |
|---|---|---|
| 4 culori pline pe secțiuni, text negru pe culoare, portocaliu doar pe negru | toată familia | Identitatea seriei. |
| Akrobat Black pentru titluri, Akrobat Bold pentru subtitluri, Arial pentru text | toată familia | Aceleași fonturi, același webfont (`welcome-02/assets/fonts/`). |
| Carduri albe cu contur negru gros, colțuri rotunjite | W3 (bestsellers), C1 (coș), Browse (panou) | Semnătura „sticker” a familiei. |
| Chip-ul cu momentul de consum (negru, text portocaliu) | Browse (chip-ul „PE LISTA DE POFTE”), W2 (etichete de moment) | Același limbaj pentru „moment”. |
| Cifra mare 4,9 + stele doar la medie, carduri de citat cu ghilimele desenate | C2, W3 | Dovada socială are deja o formă recunoscută în serie; stelele nu apar pe carduri (strategie, secțiunea 6). |
| 3 USP cu iconițe în cerc alb cu contur negru, titluri pe un singur rând (`nowrap`) | Browse, C1, C2 | Aceeași grilă și aceeași regulă de aliniere ca la Browse. |
| Buton pastilă bulletproof (VML), footer alb cu logo stripes | toată familia | Identic structural. |
| Codul: helperi, footer, preview în iframe, hook Figma | `browse-abandonment/email-01/build.py` | Copiați și adaptați (fișierul nu se poate importa: căile lui țintesc folderul lui). |

| Nou | Detalii |
|---|---|
| **Hero negru, text portocaliu** | Primul hero negru dintr-un flow de abandon (strategia o recomandă). Hero-uri anterioare: W1 portocaliu, W2 negru, W3 turcoaz, NC1 roz, NC2 portocaliu, C1 roz, C2 portocaliu, Browse turcoaz. Față de W2 (singurul negru): fără foto, doar text, iar sub el urmează turcoaz, nu alb. |
| **Tranziția: margine ruptă cu dungă** | Valuri (W1-W3, C1), curbă (NC1), diagonale (NC2), panou rotunjit (C1), feston (C2), boltă (Browse) sunt folosite. Aici: `torn-*.png`, 1200 x 56 (afișat 600 x 28), o margine zdrențuită, o dungă ruptă de a treia culoare, apoi secțiunea următoare. Generată determinist (seed fix), deci aceeași la fiecare build. |
| **Layout de categorii: 1 card mare + grilă 2 x 2** | Folosite: cercuri pe un rând (W1), zig-zag (W2), grilă 2 x 2 de produse cu rating și preț (W3), arcade numerotate (Browse). Aici primul card (Pancakes & Crêpes, cea mai mare categorie) e orizontal, pe toată lățimea; celelalte 4 sunt carduri pătrate de categorie, fără preț, fără rating. Exact varianta propusă de strategie („un card mare + 4 mici”). |
| **Foto ca decupaj de rețetar** | Fotografii complete pe față de masă din in deschisă (nouă; Browse avea cărbune), colțuri de sus rotunjite, jos marginea ruptă, în ecou cu tranzițiile. |
| **Recenzii pe alb, în culori** | C2: carduri albe pe roz; W3: carduri în trepte pe negru. Aici: fundal alb, cardul mare portocaliu, cele mici roz și turcoaz, contur negru. |
| **Închidere pe negru** | Emailul începe și se termină pe negru („masa de seară”); butonul e pastilă portocalie cu text negru (singurul buton plin portocaliu din serie). |
| **Iconițe USP noi** | cană gradată cu mix (aproape tot e în mix), magazin cu copertină (în magazine), casă cu inimă (transport). Nefolosite: camion, cronometru, spic, cască, plic, stea, bol cu tel, colet. |
| **Fără GIF** | Mișcarea rămâne semnătura Browse (strategie, „Lungime totală”). |

---

## 2. Secvența

| # | Secțiune | Fundal | Tranziție spre următoarea (dunga) |
|---|---|---|---|
| S0 | Logo complet 180px (contur alb vizibil pe negru, discovery 7) | negru | continuă |
| S1 | Salut, H1 „CE PUNEM AZI / PE MASĂ?”, text. Fără buton, fără imagine | negru | ruptă negru -> turcoaz (dungă roz) |
| S2 | Supratitlu, H2, intro, card mare, grilă 2 x 2, „Vezi toate produsele” | turcoaz | ruptă turcoaz -> alb (dungă portocalie) |
| S3 | Titlu, 4,9 din 5, stele, „peste 1.100 de recenzii”, card mare + 2 mici, „Vezi toate recenziile” | alb | ruptă alb -> roz (dungă turcoaz) |
| S4 | „BINE DE ȘTIUT” + 3 USP | roz | ruptă roz -> negru (dungă portocalie) |
| S5 | Titlu, rând, buton „Vezi toată gama”, „eat what you love”, linie albă, rândul Professional + link | negru | ruptă negru -> alb (dungă turcoaz) |
| S6 | Footer (identic structural cu Browse) | alb | - |

**Secvența: negru, turcoaz, alb, roz, negru, alb.** Nu se repetă în nicio altă secvență din serie (Browse: turcoaz, alb, portocaliu, roz, alb; C1: roz, alb, turcoaz, portocaliu, alb; C2: portocaliu, alb, roz, turcoaz, negru, alb; W2: negru, alb, roz, turcoaz, portocaliu, alb).

**Primul ecran pe mobil (375px):** H2 „CE GĂSEȘTI LA NOI” e la ~410px, iar cardul mare începe la ~490px, deci categoriile se văd în primul ecran (cerința din strategie, S1).

---

## 3. Specificații (600px, tabele, CSS inline)

- Container 600px, `bgcolor` pe fiecare `td`, padding lateral 40px desktop, 20px mobil.
- Fonturi: titluri `Akrobat, "Arial Narrow", Arial, sans-serif`, text `Arial, Helvetica, sans-serif`.
  - H1: Akrobat Black 64/60 portocaliu, rupere fixă „CE PUNEM AZI” / „PE MASĂ?” (mobil 48/46). Măsurat: „CE PUNEM AZI” 324px la 60px.
  - Salut: Akrobat Bold 22/26, portocaliu, uppercase. Text hero: Arial 16/24 alb (pe negru).
  - H2: S2 42/42, S3 40/40, S4 36/36, S5 42/42 portocaliu (mobil 32/32).
  - Supratitlu S2: Akrobat Bold 22, litere mici, ca în copy.
- Butoane bulletproof (VML `v:roundrect` + `<a>`): S5 plin portocaliu 280 x 56, text negru; carduri: contur negru 2px pe alb, 180 x 44 (card mare), 160 x 40 (carduri mici); pe mobil butoanele cardurilor devin pe toată lățimea cardului.

### S2 Categorii
- **Card mare** (Pancakes & Crêpes): tabel 520px, contur negru 3px, colțuri 20px. Foto 238 x 238 (export 476) la stânga, text 252px la dreapta (fluid-hybrid: `inline-block` + tabel fantomă MSO). Nume: Akrobat Bold 28, „PANCAKES &” / „CRÊPES” se poate rupe doar după „&” (`nowrap` pe cele două jumătăți); pe desktop stă pe un rând (225px în 232px disponibili). Mobil: foto deasupra (max 309px), text dedesubt.
- **Grila 2 x 2** (Prăjituri, Budinci / Pizza, De post): două rânduri, fiecare un tabel 520px cu 2 celule-card de 254px (232 conținut + 8 + 8 padding + 3 + 3 contur) și o rigolă de 12px. Celulele din același rând au automat aceeași înălțime. Foto 232 x 232 (export 464).
- **Pe mobil grila rămâne pe 2 coloane** (aprox. 162px per card la 375px): numele de categorie sunt scurte (max „PRĂJITURI”, 9 car., Akrobat 21px pe mobil), rândurile de conținut intră pe 2 rânduri la Arial 13/18, iar butoanele trec pe toată lățimea cardului. Am ales 2 coloane și nu stivuire ca S2 să nu devină 5 ecrane de carduri, iar cardul mare de sus păstrează ierarhia. Rândul de conținut are înălțime fixă (44px desktop, 38px mobil) ca butoanele din același rând să fie aliniate.
- Tot cardul e link: foto, nume și rând trimit la același URL ca butonul (`{{CATEGORY_URL_n}}`, `utm_content=cat_*`).
- **Cardul 5 (De post) e produs, nu categorie** (răspuns client 13.10.2026): CTA „Vezi produsul”, placeholder `{{CATEGORY_URL_5}}`, `utm_content=cat_post`.
- Eticheta de moment: chip negru, Akrobat Bold 14, portocaliu, `nowrap` (mobil 12).

### S3 Recenzii
- „4,9” Akrobat Black 96/88 (mobil 84) + „din 5” Akrobat Bold 32, ambele text live. `stars.png` 200 x 36 (export 400 x 72), `alt="Rating 4,9 din 5"`. „peste 1.100 de recenzii” Akrobat Bold 20 uppercase.
- Card mare portocaliu (Irina A., 102 car.): Arial 19/28. Carduri mici: roz (Andreea H., Arial 16/24) și turcoaz (Liliana F., citat scurt, Arial Bold 24/32 ca să echilibreze înălțimea). Nume Akrobat Bold 22, produs Arial 14, pe rânduri separate. Fără stele și fără date pe carduri.
- `quote.png` 44 x 34, PNG transparent, `alt=""`.
- Mobil: cardurile mici se stivuiesc (`.stack`).

### S4 USP: verificarea „APROAPE TOT E ÎN MIX”
Măsurat cu Pillow pe fonturile reale, cu letter-spacing inclus:

| Font | 20px (ca la Browse) | 18px (ales) |
|---|---|---|
| Akrobat Bold (webfont) | 179px | 158px |
| Arial Narrow Bold (fallback 1) | ~196px | 176px |
| Arial Bold (fallback 2) | 240px | 213px |

La Browse coloanele au 173px (157px utili): titlul NU încăpea la 20px. Ajustare, aceeași pentru toate trei coloanele: rândul USP are padding lateral 10px (nu 40px), deci coloanele au **193px**, cu **181px utili**; titlurile sunt **Akrobat Bold 18/22, letter-spacing 0,3px**, `white-space:nowrap`. Încap Akrobat (158) și Arial Narrow (176). În Outlook desktop (fără webfont) un stil `mso` le pune pe Arial 14px (167px). Rămâne un risc doar pentru un client fără webfont și fără Arial Narrow (Arial Bold 213px): titlul ar depăși coloana cu ~30px; acceptat, documentat.
Iconițe 64 x 64 (export 128), desenate de build: `usp-mix.png`, `usp-magazin.png`, `usp-acasa.png`, `alt=""`. Mobil: coloane stivuite, max 300px.

### S5 Închidere (negru)
Titlu portocaliu „NU ȘTII DE UNDE” / „SĂ ÎNCEPI?”, rând alb, buton portocaliu „Vezi toată gama” (`{{SHOP_URL}}`, `cta_shop`), „eat what you love” Akrobat Bold 30 portocaliu. Linie albă 1px, apoi rândul Professional (Arial 14 alb) și linkul subliniat „Vezi gama Professional” (`{{PROFESSIONAL_URL}}`, `professional`). Fără imagine în S5 (opțională în strategie; păstrăm 5 imagini și greutate mică).

### S6 Footer
Identic structural cu Browse: logo stripes, social, adresă, rândul SRL / CUI placeholder, fraza „de ce primești” (comentariu [DE CONFIRMAT CU ANDREEA]), dezabonare, ©.

---

## 4. Siguranță în email

- Outlook: VML pentru butoane, tabele fantomă pentru cardul mare și USP, `mso-line-height-rule:exactly`. `border-radius` ignorat: cardurile devin dreptunghiuri cu contur negru, acceptabil; colțurile foto sunt arse în imagine.
- Dark mode: `color-scheme: light` + `[data-ogsc]` (`.tb` negru, `.to` portocaliu, `.tw` alb). Fundalurile sunt `bgcolor`; tranzițiile și fotografiile au culorile arse.
- Imagini oprite: H1, numele categoriilor, cifra 4,9, citatele, USP-urile și butoanele sunt text live; alt texte din copy.md, `alt=""` pe decorative.
- HTML: `index.html` 44,4 KB, `index-esp.html` 45,1 KB (sub 102 KB). Imagini: 5 foto ~25-110 KB fiecare (limită 110 KB în build), restul sub 20 KB; total sub 1 MB.
- UTM pe toate linkurile, în afară de social, `mailto:`, `tel:` și logo: `utm_source=email&utm_medium=flow&utm_campaign=website_01&utm_content=<id>` (`cat_pancakes`, `cat_prajituri`, `cat_budinci`, `cat_pizza`, `cat_post`, `cat_toate`, `recenzii_toate`, `cta_shop`, `professional`).

## 5. index.html vs index-esp.html
Emailul nu are feed dinamic de produse, deci cele două sunt identice ca layout. `index-esp.html` are în plus:
- un comentariu `ESP-MARKER` în `<head>` cu tot ce pune Andreea manual în theMarketer (tag-ul și condiția pentru `{{FIRST_NAME}}`, linkurile reale pentru `{{CATEGORY_URL_1..5}}`, `{{SHOP_URL}}`, `{{REVIEWS_URL}}`, `{{PROFESSIONAL_URL}}`, tag-ul `{{UNSUBSCRIBE_URL}}`, fraza din footer, SRL/CUI, URL-uri absolute pentru `assets/`);
- un `ESP-MARKER` chiar deasupra salutului (fallback „Hei!” sub 1 sau peste 19 caractere).
Placeholderele `{{...}}` sunt nume generice, nu sintaxă theMarketer.

## 6. Build
```
python3 -m venv .venv && .venv/bin/pip install Pillow     # o singură dată (venv-ul există deja)
.venv/bin/python build.py              # assets/, index.html, index-esp.html, index-figma.html, index-figma-mobile.html
.venv/bin/python build.py --preview    # plus preview.png (600px) și preview-mobile.png (375px), Chrome headless
```
Imaginile Higgsfield se pun în `images/` cu numele din `image-prompts.md` (`cat1-pancakes` ... `cat5-post`, `.png/.jpg/.jpeg`); fără ele build-ul pune placeholdere la dimensiunea finală, cu același nume de fișier în `assets/`. Testat cu o fotografie reală (copie temporară a `rec3-brownie.png` din Browse ca `cat2-prajituri.png`, apoi ștearsă): încadrarea și marginea ruptă funcționează.
Fișierele Figma (`index-figma*.html`) sunt generate de `../../tools/figma_export.py` la finalul fiecărui build, din `index.html`.

## 7. Feedback pentru copywriter

- Toate textele au încăput în limite pe desktop și pe mobil 375px; nicio rupere nedorită.
- **USP 1 „APROAPE TOT E ÎN MIX”** (20/20) a cerut micșorarea titlurilor USP de la 20 la 18px (toate trei, consecvent) și coloane mai late (vezi S4). Dacă se vrea 20px ca în restul seriei, titlul ar trebui să aibă max ~17 car.; nu propun o formulare, doar semnalez.
- **„PANCAKES & CRÊPES”** încape pe un rând în cardul mare la 28px; pe mobil (o coloană) la fel.
- **Citatul Andreei H.** (89 car. fără ghilimele) încape în cardul mic: 4 rânduri desktop, 3 pe mobil (stivuit).
- **Card 5:** am aplicat răspunsul clientului (CTA „Vezi produsul”). Eticheta „vegan / de post” rămâne; nota din copy despre rezerva „vegan” nu a fost necesară (chip-ul încape).
- **Nota din copy.md, S2:** „la De post rămâne «Vezi categoria»” (varianta jucăușă) e depășită de răspunsul clientului; de actualizat în copy.md de Copywriter.
