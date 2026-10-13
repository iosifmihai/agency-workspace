# Checkout Started, Email 2: direcția de design

Autor: UI Designer, 12.10.2026. Bază: `brief.md`, `../email-01/` (design-direction, build.py), referința `../email-01/refs/` (secțiunea „What others say”), regulile de brand din `../../welcome-01/brief.md`.
Textele finale sunt ale Email Marketing Strategist (`copy.md`), preluate exact în `COPY` din `build.py`. Layout-ul și limitele de caractere au fost convenite cu el înainte de copy.

Ideea vizuală: **„nota cinci”**. Unghiul copy-ului e „nu ne crede pe cuvânt”, deci emailul e construit în jurul dovezii: cinci stele negre în arc deasupra unei farfurii cu mini pancakes așezate în cerc (hero), apoi cifra „4,9” uriașă cu stele în secțiunea de recenzii. Motivul de tranziție nou pe tot emailul e **festonul** (margine de biscuit, semicercuri), ca să nu repete panoul rotunjit și valurile din Email 1.

---

## 1. Ce preluăm din referință și de ce

| Pattern din referință | Unde | De ce |
|---|---|---|
| „What others say”: titlu mare + citate scurte cu nume | S4 | Cerința clientului (2-3 recenzii). La noi în carduri albe cu contur, ca blocul de coș, deci aceeași familie. |
| Stele de rating | S4 (doar la media 4,9, nu per card) | Recenzia Luminiței are 4 stele pe site; stelele arată media, nu nota fiecărei recenzii. A 5-a stea e umplută 90% (4,9 din 5). |
| Mâncare decupată care iese din cadru | S1 (farfuria trece peste feston în alb) | Energie și apetit, continuitate cu Email 1. |
| Titlu foarte mare, CTA pill | S1, S3, S6 | Sistemul seriei. |

**Ce NU preluăm:** poze cu mâini și oameni lângă recenzii (ar putea trece drept poze de client; recenziile rămân text), discount/cod, ambalaje, culorile lor.

## 2. Diferențe față de Email 1 (aceeași familie, alt layout)

| | Email 1 | Email 2 |
|---|---|---|
| Ordinea culorilor | roz, alb, turcoaz, portocaliu, alb | **portocaliu, alb, roz, turcoaz, negru, alb** |
| Hero | imagine întâi (stack plutind + adnotări arse), text pe alb dedesubt | **text live pe portocaliu întâi**, apoi imaginea: farfurie de sus + 5 stele, fără text ars |
| Tranziții | panou alb rotunjit + valuri | **feston** (semicercuri) peste tot |
| Închidere | portocaliu, 2 coloane, buton outline spre gamă | **negru, centrat**, buton portocaliu plin spre checkout (text portocaliu pe negru) |
| Secțiune nouă | - | recenzii pe roz |

Identic intenționat: logo, cardul „În coșul tău” (chip negru, placeholder theMarketer), butonul principal, grila USP cu iconițe desenate, footer-ul.

## 3. Secțiuni și culori

| # | Secțiune | Fundal | Tranziție |
|---|---|---|---|
| S0 | Logo 180px (logo complet: litere portocalii cu contur negru, citibil pe portocaliu) | portocaliu #FAA61A | continuă |
| S1 | Salut, H1, rând (text live), apoi IMG1 compus | portocaliu | feston portocaliu -> alb (ars în hero.jpg), farfuria trece peste el |
| S2 | Card „În coșul tău” | alb | - |
| S3 | CTA „Finalizează comanda” | alb | feston alb -> roz |
| S4 | Titlu, „4,9 din 5” + stele + „peste 1.100 de recenzii”, 1 card mare + 2 carduri | roz #F7ACB4 | feston roz -> turcoaz |
| S5 | Titlu + 3 USP (suport, transport, ingrediente) | turcoaz #86D2DA | feston turcoaz -> negru |
| S6 | IMG2 fursecuri, titlu, rând, buton, „eat what you love” | negru #000000 | feston negru -> alb |
| S7 | Footer (identic cu Email 1, rândul SRL / CUI placeholder) | alb | - |

**Text și culori:** negru pe portocaliu, alb, roz și turcoaz. Pe negru tot textul e portocaliu (titlu, rând, semnătură); butonul de pe negru e portocaliu plin cu text negru. Butonul principal (pe alb): pastilă neagră cu text portocaliu. Fără alb ca text.

## 4. Specificații (600px, tabele, CSS inline)

- Container 600px, `bgcolor` pe fiecare `td`, padding lateral 40px desktop, 20px mobil.
- Fonturi: titluri `Akrobat, "Arial Narrow", Arial, sans-serif`, text `Arial, Helvetica, sans-serif` (webfont Akrobat din `welcome-02/assets/fonts/`).
  - H1: Akrobat Black 56/54 uppercase, rupere fixă după „CREDE” (mobil 44/44).
  - H2: Akrobat Black 34/34 uppercase (mobil 30/30), pe negru portocaliu.
  - Cifra „4,9”: Akrobat Black 120/118 (mobil 96), „din 5” 40px (mobil 34). Text live, nu imagine.
  - Salut și „peste 1.100 de recenzii”: Akrobat Bold 22/26 și 20/24, uppercase, letter-spacing 1px.
  - Citat card mare: Arial 18/28 (mobil 17/26); carduri mici: Arial 16/24. Nume: Akrobat Bold 20/22. Produs: Arial 14/20.
  - USP: titlu Akrobat Bold 20/22 uppercase (cuvintele cu cratimă nu se rup: „SCRIE-NE.” stă întreg), rând Arial 14/20.
- Carduri recenzii: alb, contur negru 2px, colțuri 20px. Card mare 520px; dedesubt două carduri de 250px cu 20px între ele, în același rând de tabel, deci au aceeași înălțime pe desktop. Ghilimele mari negre desenate (`quote.png`, 44 x 34, `alt=""`).
- Stele: `stars-49.png` 200 x 36, alt „Rating 4,9 din 5”.
- Iconițe USP 64 x 64 (export 128), desenate de build: balon de conversație cu trei puncte (suport), camion, spic. Suport: email pe primul rând, telefon pe al doilea, ambele linkuri (`mailto:`, `tel:`), fără UTM.
- Feston: PNG 1200 x 44 afișat 600 x 22, semicercuri cu raza de 15px afișat.
- Butoane bulletproof (VML + `<a>`), 280 x 56, Arial 18 bold, pe mobil 100% (max 335).

### Limite de caractere (măsurate pe Akrobat și pe fallback Arial Bold, cazul cel mai rău)
| Element | Limită | Folosit în copy.md |
|---|---|---|
| Salut | max 25 | 20 |
| H1 | 2 rânduri x 12 car, cuvânt max 12 | 11 / 10 |
| Rând hero | ideal 80-95, max 110 | 82 |
| Titlu recenzii | ideal 18 (un rând), max 28 pe 2 rânduri | 16 |
| Sub cifră | max 30 | 23 |
| Citat card mare | max 120 | 102 |
| Citat card mic | max 90 | 62, 80 |
| Nume / produs | max 16 / max 22 | ok |
| Titlu USP secțiune | max 24 | 22 |
| Titlu USP | max 20, 2 rânduri | 20, 17, 16 |
| Rând USP | max 50 | 38, 32, 41 |
| Titlu închidere | max 22 | 20 |
| Rând închidere | max 70 | 48 |
| CTA | max 22 | 19 |
| Preheader | max 90 | 87 |

### S1 Hero (IMG1 compus de build.py)
`assets/hero.jpg` 1200 x 900, afișat 600 x 450. Straturi: portocaliu; festonul spre alb la y≈800; 5 stele negre pline în arc (cea din mijloc mai sus, ușor rotite); 4 sclipiri mici cu contur negru; decupajul farfuriei (740 px) cu baza la y=880, deci trece peste feston în alb dar nu atinge marginea de jos. Imaginea e link spre checkout.

### S6 Închidere (IMG2)
`assets/s6-fursecuri.jpg` 720 x 440 pe negru, afișat 360 x 220 centrat (100% pe mobil, max 360).

## 5. Comportament mobil (verificat la 375px, `preview-mobile.png`)
- H1 44/44 pe 2 rânduri, rândul hero pe 2 rânduri.
- Hero și festoanele scalează fluid.
- Cardurile de recenzii trec una sub alta, 16px între ele; cifra 4,9 scade la 96px.
- USP: o coloană, centrat. Butoanele 100% (max 335).
- Coș: imagine 72px, prețul pe coloana din dreapta (ca la Email 1).

## 6. Siguranță în email
- Outlook: VML pentru butoane; `border-radius` ignorat (cardurile devin dreptunghiuri, acceptabil); festonul e imagine; tabel fantomă pentru coloanele USP; `mso-line-height-rule:exactly`.
- Dark mode: `color-scheme: light` + regulile `[data-ogsc]` (`.tb` negru, `.to` portocaliu).
- Imagini oprite: tot textul (H1, cifra 4,9, recenziile, USP, butoane) e live; stelele au alt.
- HTML: ~29 KB (sub pragul de 102 KB al Gmail).

## 7. Legarea la theMarketer
La fel ca Email 1: `index.html` = preview cu 2 rânduri EXEMPLU și rând de total; `index-esp.html` = în card e `[FEED PRODUSE THEMARKETER]` între comentariile `THEMARKETER_FEED`, fără rând de total. Lățime utilă pentru feed: 516px desktop, 100% mobil.
Variabile: `{{CHECKOUT_URL}}` (hero, `cta_main`, `cta_final`), `{{FIRST_NAME}}`, `{{UNSUBSCRIBE_URL}}`. UTM: `utm_campaign=checkout_02`. Fără `{{SHOP_URL}}` (copy: toate linkurile duc la aceeași comandă).

## 8. Build
```
/cale/venv/bin/python build.py              # assets/ + index.html + index-esp.html
/cale/venv/bin/python build.py --preview    # plus preview.png (600px) și preview-mobile.png (375px), Chrome headless
```
Imaginile Higgsfield se pun în `images/` cu numele din `image-prompts.md`; fără ele, build-ul pune placeholdere la dimensiunea finală.
