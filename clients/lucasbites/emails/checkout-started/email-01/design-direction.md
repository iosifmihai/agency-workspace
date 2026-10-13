# Checkout Started, Email 1: direcția de design

Autor: UI Designer, 12.10.2026. Bază: `brief.md`, `../README.md`, `discovery.md` (secțiunile 3-7), referința `refs/Email marketing campaigns | Email design klaviyo CPG - Hamed Mohammadi.jpg`, familia vizuală din welcome 01-03.
Textele finale sunt ale Email Marketing Strategist (`copy.md`). Aici sunt doar structura, limitele și regulile vizuale.

Ideea vizuală: **„pofta a rămas în aer”**. Un teanc de pancakes cu chocolate chips plutește înclinat pe roz, cu trei adnotări scrise cu săgeți desenate de mână, ca în referință. Sub el, un panou alb cu colțuri rotunjite urcă peste roz și ține tot ce contează: salutul, titlul, coșul și butonul. Totul se poate termina din primul ecran.

---

## 1. Ce preluăm din referință și de ce

| Pattern din referință | Unde | De ce |
|---|---|---|
| Hero colorat cu produsul decupat, înclinat, „plutind” | S1, IMG1 | Atenția merge întâi pe mâncare. La noi produsul e mâncarea, nu borcanul (nu avem poze de ambalaj). |
| Adnotări scurte cu săgeți scrise de mână în jurul produsului | S1, arse în hero | Spun 3 beneficii fără să ocupe spațiu de text. Font: Akrobat Bold (nu Plicata, licență), săgeți desenate de `build.py`. Informația există și ca text live în S4, deci nu se pierde cu imaginile oprite. |
| Panou deschis cu colțuri rotunjite sus, care intră peste fundalul colorat | trecerea S1 -> S2 | Leagă hero-ul de conținut fără val. E alt tip de tranziție decât valurile din welcome, deci emailul se recunoaște ca alt moment. Colțurile sunt arse în imagine, deci arată la fel și în Outlook. |
| Titlu foarte mare, bold, centrat, imediat sub hero | S2 | La ei e „15% DISCOUNT”; la noi e reamintirea (fără discount, brief). |
| Buton pill plin, sub text | S3 | Același pattern ca în welcome: pastilă neagră cu text portocaliu. |
| Rând de iconițe mici de beneficii | S4 | Mărit la 3 USP cu titlu și un rând, pe turcoaz, ca să fie citibile. |
| Steluțe decorative | S1 (în hero) | Portocalii cu contur negru, ca literele logo-ului. |
| Mâncare decupată care iese din cadru | S1 (pancakes peste marginea panoului) și S5 (farfuria cu clătite tăiată de marginea dreaptă) | Energie și apetit, fără elemente în plus. |

**Ce NU preluăm**

| Nu preluăm | Motiv |
|---|---|
| Cod de reducere, „15% DISCOUNT” | Brief: fără discount, fără urgență falsă. |
| Carduri „Choose your's” cu ambalaje + Buy now | Nu avem ambalaje; produsele relevante sunt deja cele din coș (bloc dinamic). |
| Secțiunea de recenzii | Rămâne pentru Email 2 (README). |
| Poze cu mâini și oameni | Nu generăm imagini care pot părea UGC; nu sunt necesare. |
| Culorile lor (roșu, verde închis, bleu) | Doar cele 4 culori Lucas Bites + alb. |
| Text peste fotografie (în afară de adnotări) | Contrast imprevizibil și se pierde cu imaginile oprite. |

---

## 2. Secțiuni și culori

| # | Secțiune | Fundal | Tranziție |
|---|---|---|---|
| S0 | Logo (pe roz, logo complet, regulă de fundal respectată) | roz #F7ACB4 | continuă în hero |
| S1 | Hero: IMG1 compus (pancakes plutind + 3 adnotări + steluțe), jos începe panoul alb cu colțuri rotunjite | roz | panou alb rotunjit (ars în imagine) |
| S2 | Salut, H1, text scurt, blocul dinamic „În coșul tău” | alb | - |
| S3 | CTA principal „Finalizează comanda” | alb | val alb -> turcoaz |
| S4 | Titlu de secțiune + 3 USP cu iconițe | turcoaz #86D2DA | val turcoaz -> portocaliu |
| S5 | Închidere: titlu + rând + buton outline + „eat what you love”, cu IMG2 (clătite) care iese din marginea dreaptă | portocaliu #FAA61A | val portocaliu -> alb |
| S6 | Footer identic cu welcome (logo stripes, social, contact, dezabonare) | alb | - |

Secvența: **roz, alb, turcoaz, portocaliu, alb**. Hero-urile din welcome au fost portocaliu, negru, turcoaz; aici roz, deci fiecare email are hero de altă culoare.

**Culori și text**: pe roz, alb, turcoaz și portocaliu tot textul e negru. Portocaliul apare ca text doar pe negru (textul butoanelor pline și rândul de total din coș). Butonul principal: pastilă neagră, text portocaliu. Butonul secundar: contur negru 2px, text negru, fundal transparent.

---

## 3. Specificații (600px, tabele, CSS inline)

### Sistem comun (identic cu welcome-03)
- Container 600px, `bgcolor` pe fiecare `td`. Padding secțiune 40px lateral desktop, 20px mobil (sub 600px).
- Titluri `Akrobat, "Arial Narrow", Arial, sans-serif` (webfont din `welcome-02/assets/fonts/`, copiat de build), text `Arial, Helvetica, sans-serif`.
  - H1: Akrobat Black 52/50 uppercase (mobil 40/40).
  - H2: Akrobat Black 34/34 uppercase (mobil 30/30).
  - Salut/eyebrow: Akrobat Bold 22/26, uppercase, letter-spacing 1px.
  - Nume produs în coș: Akrobat Bold 22/24. Titlu USP: Akrobat Bold 20/22 uppercase.
  - Text: Arial 16/24. Meta (cantitate): Arial 14/20. Text USP: Arial 14/20.
- Butoane bulletproof: VML `v:roundrect` pentru Outlook + `<a>` cu `border-radius`. Principal 280 x 56, Arial 18 bold; pe mobil 100% (max 335). Secundar 260 x 48, contur 2px.

### Limite de caractere (măsurate pe Akrobat și pe fallback Arial Bold, cazul cel mai rău)
| Element | Limită |
|---|---|
| Salut / supratitlu | max 25 car |
| H1 | max 28 car, max 2 rânduri, niciun cuvânt peste 12 car (~14 car/rând pe mobil în Arial) |
| Text sub H1 | ideal 70-90, max 110 car |
| Etichetă bloc coș | max 20 car |
| CTA principal / secundar | max 22 car |
| Titlu secțiune USP | max 26 car |
| Titlu USP | max 20 car, max 2 rânduri |
| Rând USP | ideal 35-45, max 50 car |
| Adnotări hero | 3 x (max 2 rânduri x 12 car) |
| Titlu S5 | max 32 car (coloană ~330px, max 3 rânduri) |
| Rând S5 | max 70 car |
| Preheader | max 90 car |

### S0 + S1 Hero (roz)
- Logo 180px centrat pe roz, padding 24px.
- IMG1 compus de `build.py`: `assets/hero.jpg`, 1200 x 1000, afișat 600 x 500 (100% pe mobil). Straturi: fundal roz; panoul alb cu colțuri de 32px (afișat) care începe la ~84% din înălțime; decupajul pancakes rotit ~-10°, cu baza peste marginea panoului; 3 adnotări Akrobat Bold 50px (afișat 25px desktop, ~16px mobil) cu săgeți curbe desenate; 5 steluțe portocalii cu contur negru.
- Adnotările sunt arse în imagine, deci textul lor trebuie dublat de USP-urile live din S4 (sunt aceleași idei). `alt` descrie mâncarea.

### S2 Salut, H1, coș (alb)
- Centrat: salut, H1, text.
- **Blocul dinamic** `{{CART_ITEMS}}`: card 520px (mobil 100%), `border:2px solid #000000`, `border-radius:20px`, fundal alb.
  - Sus, chip negru cu text portocaliu: eticheta „În coșul tău”.
  - Un rând per produs: imagine 96 x 96 (mobil 72 x 72) | nume (Akrobat Bold 22) + „Cantitate: N” (Arial 14) | preț aliniat dreapta (Arial 16 bold). Între rânduri, linie neagră 1px.
  - Jos, rând de total opțional pe negru: eticheta și `{{CART_TOTAL}}` cu text portocaliu, colțuri de jos rotunjite.
  - Imaginea produsului vine din catalogul ESP (poza din magazin), nu din Higgsfield. Până la conectare: 2 rânduri **EXEMPLU** cu placeholder vizibil („EXEMPLU / imagine din coș”) și preț „XX,XX lei”.
  - Legarea la ESP: vezi secțiunea 6.

### S3 CTA (alb)
- Buton principal spre `{{CHECKOUT_URL}}`, fără microcopy dedesubt (transportul apare în USP, nu se repetă). Apoi val alb -> turcoaz.

### S4 USP (turcoaz)
- H2 centrat, apoi 3 coloane de 160px (fluid hybrid: `inline-block` + tabel fantomă MSO). Pe mobil, coloanele trec una sub alta, centrate, max 300px.
- Fiecare: iconiță 64 x 64 (export 128, desenată de `build.py`: cerc alb cu contur negru 3px și pictogramă neagră: camion, cronometru cu „5”, spic de grâu), titlu, un rând.

### S5 Închidere (portocaliu)
- Două coloane pe desktop: text 340px stânga (titlu H2, rând Arial 16, buton outline spre `{{SHOP_URL}}`, „eat what you love” Akrobat Bold 30) și IMG2 220 x 300 la dreapta, lipit de marginea emailului (farfuria e tăiată de marginea dreaptă, arsă pe portocaliu în JPG).
- Mobil: textul centrat, apoi IMG2 aliniat dreapta, tot lipit de margine.

### S6 Footer (alb)
- Identic structural cu welcome-03 (linie, logo stripes, social, contact, dezabonare). Rândul „de ce primești acest email” e al strategistului (pentru coș abandonat nu se potrivește textul cu ghidul de rețete).

---

## 4. Comportament mobil (sub 600px)
- Container 100%, padding lateral 20px. H1 40/40, H2 30/30.
- Hero și valurile scalează fluid (`width:100%;height:auto`), adnotările rămân lizibile (~17px).
- Coș: imaginea scade la 72px, prețul rămâne pe coloana din dreapta (lățime 80px).
- Butoanele principale devin 100% (max 335px).
- USP: o coloană, centrat. S5: coloanele se stivuiesc.

## 5. Siguranță în email
- Outlook: VML pentru butoane, `border-radius` ignorat (cardul coșului devine dreptunghi, acceptabil), colțurile panoului din hero sunt arse în imagine, tabele fantomă pentru coloane, `mso-line-height-rule:exactly` pe titluri.
- Dark mode: `color-scheme: light` + regulile `[data-ogsc]` din welcome. Fundalurile de secțiune sunt `bgcolor`, hero și IMG2 sunt JPG cu culorile arse.
- Imagini oprite: salutul, titlul, coșul, butoanele și USP-urile sunt text live. Adnotările din hero sunt dublate de USP.
- Mărime HTML sub 102 KB (Gmail clipping).

## 6. Legarea blocului dinamic la ESP
ESP: **theMarketer** (confirmat 12.10.2026). `build.py` scrie două fișiere: `index.html` (preview, 2 rânduri marcate EXEMPLU cu preț „XX,XX lei”) și `index-esp.html` (versiunea pentru theMarketer: în cardul „În coșul tău” e un placeholder `[FEED PRODUSE THEMARKETER]`, între comentariile `THEMARKETER_FEED`, pe care clientul îl înlocuiește cu blocul de produse din coș din editor; rândul de total lipsește, îl afișează feed-ul dacă e cazul). Blocul e marcat între `CART_ITEMS START` și `CART_ITEMS END`.
Variabile rămase (nume generice, se înlocuiesc cu tag-urile theMarketer): `{{CHECKOUT_URL}}`, `{{SHOP_URL}}`, `{{FIRST_NAME}}`, `{{UNSUBSCRIBE_URL}}`.
Lățimea utilă a cardului pentru feed: 516px desktop (card 520px cu bordură 2px), 100% pe mobil.

## 7. Build
```
python3 -m venv .venv && .venv/bin/pip install Pillow     # o singură dată, dacă Pillow lipsește
.venv/bin/python build.py              # assets/ + index.html + index-esp.html
.venv/bin/python build.py --preview    # plus preview.png (600px) și preview-mobile.png (375px), cu Google Chrome headless
```
Imaginile Higgsfield se pun în `images/` cu numele din `image-prompts.md`; fără ele, build-ul pune placeholdere la dimensiunea finală. Textele stau în `COPY` din `build.py`, copiate exact din `copy.md`.
