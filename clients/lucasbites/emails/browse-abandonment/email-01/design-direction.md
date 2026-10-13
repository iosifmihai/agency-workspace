# Browse Abandonment, Email 1: direcția de design

Autor: UI Designer, 13.10.2026. Bază: `strategy.md`, `copy.md`, `brief.md`, `../README.md`, referința `refs/e558fb99d55f1dd8c9a47555a498285f.jpg` (emailurile Bello), familia vizuală din welcome 01-03 și checkout-started 01-02.
Textele sunt ale Copywriterului (`copy.md`), preluate exact în `COPY` și `RECIPES` din `build.py`. Aici sunt doar structura, limitele și regulile vizuale.

Ideea vizuală: **„ferestre spre poftă”**. Unghiul emailului e inspirația („ce faci cu mixul ăsta?”), deci rețetele sunt privite prin **arcade**: fiecare rețetă stă într-o fereastră cu partea de sus rotundă, numerotată 01 / 02 / 03, ca un meniu. Arcada se repetă în tot emailul: capul cardului de produs, tranzițiile dintre secțiuni (o boltă largă pe toată lățimea) și cercul din care „iese” teancul de clătite la final.

---

## 1. Ce preluăm din referință (Bello) și ce NU

| Pattern din referință | Unde | De ce |
|---|---|---|
| Rame de foto în formă de arcadă (sus rotund) | S3, cele 3 rețete; S2, imaginea EXEMPLU | Formă nouă în familie (până acum: cercuri, plăci pătrate, decupaje). Dă un ritm de „vitrină” rețetelor. Arcada e arsă în imagine, deci arată la fel și în Outlook. |
| Listă numerotată 01 / 02 / 03, foto în arcadă la stânga, text la dreapta | S3 | Se potrivește exact cu 3 rețete. Numărul e o pastilă rotundă pe colțul arcadei, ca la Bello. Pe mobil foto și text se stivuiesc (titlurile de 25-27 car. nu încap lângă imagine la 375px). |
| Card de produs cu sus în arcadă, fundal de culoare moale și insignă rotundă | S2 | Cardul „PE LISTA DE POFTE” are capul în arcadă roz pe turcoaz și o insignă portocalie rotundă cu steluță. Înăuntru, un panou alb cu contur negru (cum cere strategia) ține blocul theMarketer. |
| Secțiuni puternice, colorate în blocuri | toate | Turcoaz, alb, portocaliu, roz, alb: fiecare secțiune are o singură culoare plină. |
| Hero curat, centrat, titlu mare | S1 | Text live centrat pe turcoaz. Fără buton (copy: cardul din S2 e primul click), deci fără pill în hero. |
| Mâncare care iese dintr-un cerc / dintr-o farfurie | S5 | Teancul de clătite decupat trece peste marginea de sus a unui cerc portocaliu cu contur negru. |

| Nu preluăm | Motiv |
|---|---|
| Fonturile serif (Bello) | Familia Lucas Bites: Akrobat + Arial. |
| Paleta verde / maro / galben-lămâie | Doar #FAA61A, #F7ACB4, #86D2DA, #000000 și alb. |
| Footer-ul închis (gri-maro) cu bandă de categorii | Footer-ul familiei e alb, cu logo stripes; rămâne identic. |
| Tabele de valori nutriționale în card | Fără promisiuni nutriționale (brief); oricum produsul vine din feed. |
| Poze cu oameni și mâini (secțiunea „myth”) | Doar mâncare, nimic care să pară UGC. |
| Insigna „New” cu text | Nu avem copy pentru ea; insigna e doar decorativă (steluță), `alt=""`. |

---

## 2. Culoarea hero-ului și secvența

Hero-urile folosite până acum: W1 portocaliu, W2 negru, W3 turcoaz, Checkout 1 roz, Checkout 2 portocaliu. Strategia cere altă culoare decât roz și portocaliu (cine trece din browse în checkout le vede pe acelea). Rămâneau negru și turcoaz.

**Ales: turcoaz.** Negru ar fi cerut text portocaliu pe tot hero-ul și un ton de „seară” prea apăsat pentru un email de inspirație. Turcoazul e proaspăt și luminos, iar față de W3 (tot turcoaz) diferă clar: W3 avea compoziție foto mare și val, aici hero-ul e doar text, urmat de cardul roz în arcadă. Între W3 și acest email trec de obicei zile sau săptămâni, iar secvența completă nu seamănă cu niciun alt email.

| # | Secțiune | Fundal | Tranziție spre următoarea |
|---|---|---|---|
| S0 | Logo 180px (logo complet, ca în W3 pe turcoaz) | turcoaz #86D2DA | continuă |
| S1 | Steluțe decorative, salut, H1, text | turcoaz | continuă |
| S2 | Card produs vizualizat: cap în arcadă roz + corp roz cu panou alb | turcoaz (card roz) | boltă turcoaz -> alb |
| S3 | Supratitlu, H2, intro, 3 rețete numerotate, „Toate rețetele” | alb | boltă alb -> portocaliu |
| S4 | Titlu + 3 USP cu iconițe | portocaliu #FAA61A | boltă portocaliu -> roz |
| S5 | Titlu, rând, buton, „eat what you love”, clătite în cerc | roz #F7ACB4 | boltă roz -> alb |
| S6 | Footer (identic structural cu checkout) | alb | - |

**Secvența: turcoaz, alb, portocaliu, roz, alb.** Checkout 1: roz, alb, turcoaz, portocaliu, alb. Checkout 2: portocaliu, alb, roz, turcoaz, negru, alb. W3: turcoaz, alb, ... cu valuri.

**Tranziția nouă: bolta.** Valurile (welcome, Checkout 1), panoul cu colțuri rotunjite (Checkout 1) și festonul (Checkout 2) sunt deja folosite. Aici secțiunea următoare urcă într-o singură arcadă largă, pe toată lățimea (`dome-*.png`, 1200 x 80, afișat 600 x 40), ecoul ramelor din S3.

**Text și culori:** negru pe turcoaz, roz, alb și portocaliu. Portocaliul apare ca text doar pe negru (chip-ul din S2 și textul butoanelor pline). Buton plin: pastilă neagră, text portocaliu. Buton secundar (rețete): contur negru 2px, text negru.

---

## 3. Specificații (600px, tabele, CSS inline)

- Container 600px, `bgcolor` pe fiecare `td`, padding lateral 40px desktop, 20px mobil.
- Fonturi: titluri `Akrobat, "Arial Narrow", Arial, sans-serif` (webfont din `welcome-02/assets/fonts/`, copiat de build), text `Arial, Helvetica, sans-serif`.
  - H1: Akrobat Black 60/56 uppercase, rupere fixă „CE FACI CU” / „POFTA ASTA?” (mobil 46/44).
  - H2 S3 și S5: Akrobat Black 40/40 (mobil 32/32). H2 S4: 34/34. „DINTR-UN” e în `white-space:nowrap`, nu se rupe la cratimă.
  - Salut și supratitlu S3: Akrobat Bold 22/26, letter-spacing 1px (supratitlul rămâne cu litere mici, ca în copy).
  - Titlu rețetă: Akrobat Bold 24/26 uppercase, ruperile fixe din copy.md (secțiunea 4). Măsurat: cel mai lung rând, „BROWNIE CU FRUCTE”, are 205px în Akrobat și 262px în fallback Arial Bold la 24px, deci încape în coloana de 276px și în Outlook.
  - Etichetă moment: chip cu contur negru 2px, Akrobat Bold 16. Rând „Cu {produs}”: Arial 15 bold. Rând info: Arial 14. Rând de poftă: Arial 15.
  - USP: titlu Akrobat Bold 20/22 uppercase, rând Arial 14/20.
- Butoane bulletproof (VML `v:roundrect` + `<a>`): principal 280 x 56 (S5), „Vezi produsul” 260 x 52, „Vezi rețeta” outline 150 x 40. Pe mobil butoanele pline devin 100% (max 335).

### S1 Hero
Text live centrat, fără imagine mare: `sparkles.png` (140 x 40, `alt=""`) deasupra salutului. Pe mobil (375px) cardul de produs începe la ~370px și se termină la ~710px, deci e în primul ecran, cum cere strategia.

### S2 Produs vizualizat (PLACEHOLDER theMarketer)
- `card-cap.png` 520 x 96 (export 1040 x 192): arcadă roz pe turcoaz, insignă portocalie cu steluță albă, `alt=""`. Sub ea, corp roz (`td` cu colțuri de jos 24px).
- Chip negru cu text portocaliu „PE LISTA DE POFTE”, centrat.
- Panou alb, contur negru 2px, colțuri 16px. **Lățimea utilă pentru blocul theMarketer: 476px pe desktop** (card 520, padding 20 + 20, bordura 2 + 2), 100% pe mobil (aprox. 307px la un ecran de 375). Dacă blocul are imagini fixe mai late de 476px, trebuie setate la 100%.
- `index.html`: exemplu marcat EXEMPLU: imagine 160 x 160 cu arcadă turcoaz „EXEMPLU / produs vizualizat”, „Nume produs”, „XX,XX lei”.
- `index-esp.html`: `[PRODUS VIZUALIZAT THEMARKETER]` între `<!-- THEMARKETER_FEED START -->` și `<!-- THEMARKETER_FEED END -->`, același principiu ca `[FEED PRODUSE THEMARKETER]` din Checkout 1.
- Butonul „Vezi produsul” e sub panou, cu comentariul să fie șters dacă blocul are buton propriu. Linkul e `{{PRODUCT_URL}}` (placeholder nou, se înlocuiește cu linkul produsului din bloc), `utm_content=cta_product`.
- Tot S2 e între comentariile `VIEWED_PRODUCT START` / `VIEWED_PRODUCT END`, ca Andreea să-l poată ascunde dacă blocul nu randează (fallback-ul recomandat în copy.md). Varianta „Toate mixurile Lucas Bites, într-un singur loc.” + „Răsfoiește gama” e în `COPY` (`fallback_line`, `fallback_cta`), dar nu e în HTML: se folosește doar dacă theMarketer nu poate ascunde containerul.

### S3 Rețete (secțiunea principală)
- Antet centrat: supratitlu, H2, intro.
- 3 rânduri, fiecare: imagine 220 x 290 la stânga (arcadă 196 x 264 cu contur negru 3px, pastilă rotundă cu numărul în colțul din dreapta sus: 01 portocaliu, 02 roz, 03 turcoaz) și text 300px la dreapta (chip moment, titlu, „Cu {produs}”, info, rând de poftă, buton „Vezi rețeta”). Coloane fluid-hybrid (`inline-block` + tabel fantomă MSO).
- Imaginea, titlul și butonul duc la aceeași rețetă (`utm_content=reteta_1..3`).
- Mobil: imaginea centrată deasupra, textul centrat dedesubt.
- **Rețeta 2 = GIF animat** (`assets/rec2-pizza.gif`). Export la 1,5x (330 x 435), max 1 MB: `build.py` scade scara (1,5 / 1,25 / 1x), numărul de culori (160 -> 64) și cadrele (fiecare al doilea) până intră sub 1 MB. Paleta e luată din primul cadru, iar zonele care nu se mișcă rămân identice cu primul cadru (cinemagraph: GIF mic, fără pâlpâire). Outlook desktop arată doar cadrul 1, deci cadrul 1 trebuie să fie o fotografie completă (vezi `image-prompts.md`).
- Rândul de poftă e opțional (copy.md, întrebarea 2): `SHOW_CRAVING_LINE = False` în `build.py` îl scoate.
- „Toate rețetele”: link subliniat, Akrobat Bold 22, spre `{{SHOP_URL}}/retete`, `utm_content=retete_toate`.

### S4 USP (portocaliu)
3 coloane de 173px (mobil: una sub alta, max 300px). Iconițe noi, 64 x 64 (export 128), desenate de build, `alt=""`: **stea** (4,9 din 5), **bol cu tel** (ce e în mix), **colet** (transport; camionul e folosit în checkout). Cerc alb, contur negru 3px, pictogramă neagră, ca restul familiei.

### S5 Închidere (roz, centrat)
Titlu „POFTA NU” / „SE GRĂBEȘTE.”, rând, buton „Alege-ți pofta” spre `{{SHOP_URL}}` (`cta_shop`), semnătura. Dedesubt `s5-clatite.jpg` 360 x 280 (export 720 x 560): cerc portocaliu cu contur negru, teancul de clătite decupat trece peste marginea de sus a cercului, 3 steluțe. Imaginea e link spre gamă (același `cta_shop`). Clătitele sunt singura categorie din rândul S5 care nu e în cele 3 rețete (strategia: „din altă categorie, nu a 4-a rețetă”).

### S6 Footer
Identic structural cu checkout: logo stripes, social, adresă, rândul SRL / CUI placeholder, fraza „de ce primești” din copy.md (cu comentariu [DE CONFIRMAT CU ANDREEA]), dezabonare, ©.

---

## 4. Siguranță în email

- Outlook: VML pentru butoane, tabele fantomă pentru coloane (rețete, USP), `mso-line-height-rule:exactly`. `border-radius` ignorat: corpul cardului roz și panoul alb devin dreptunghiuri, acceptabil, pentru că arcada de sus e imagine. GIF-ul arată doar cadrul 1.
- Dark mode: `color-scheme: light` + regulile `[data-ogsc]` (`.tb` negru, `.to` portocaliu). Fundalurile sunt `bgcolor`; arcadele, bolțile și S5 sunt imagini cu culorile arse.
- Imagini oprite: H1, chip, titlurile rețetelor, USP, butoanele sunt text live. Alt texte din copy.md (rețete), `alt=""` pe decorative.
- HTML: ~35 KB (`index.html` și `index-esp.html`), sub pragul de 102 KB. Imagini totale fără GIF: ~250 KB; GIF-ul real max 1 MB.
- UTM: `utm_source=email&utm_medium=flow&utm_campaign=browse_01&utm_content=<id>` pe toate linkurile, în afară de social, `mailto:`, `tel:` și logo.

## 5. Variabile (nume generice, se înlocuiesc cu tag-urile theMarketer)
`{{FIRST_NAME}}` (fallback „Hei!”), `{{PRODUCT_URL}}` (nou: linkul produsului din bloc, doar pentru butonul „Vezi produsul”), `{{URL_RETETA_POST}}`, `{{URL_RETETA_PIZZA}}`, `{{URL_RETETA_BROWNIE}}` (fallback `{{SHOP_URL}}/retete`), `{{SHOP_URL}}`, `{{UNSUBSCRIBE_URL}}`.

## 6. Build
```
python3 -m venv .venv && .venv/bin/pip install Pillow     # o singură dată (venv-ul există deja în folder)
.venv/bin/python build.py              # assets/, index.html, index-esp.html, index-figma.html, index-figma-mobile.html
.venv/bin/python build.py --preview    # plus preview.png (600px) și preview-mobile.png (375px), Chrome headless
```
Imaginile Higgsfield se pun în `images/` cu numele din `image-prompts.md`; fără ele, build-ul pune placeholdere la dimensiunea finală. Pentru GIF: vezi `image-prompts.md`, secțiunea „Cum se face GIF-ul”. `ffmpeg` nu e instalat pe acest Mac (verificat cu `which ffmpeg`, 13.10.2026).
Fișierele Figma (`index-figma*.html`) sunt generate de `../../tools/figma_export.py` la finalul fiecărui build, din `index.html` (preview cu EXEMPLU).

## 7. Feedback pentru copywriter

- Toate textele au încăput în limite; nu e nevoie de rezervele de lungime (supratitlul S3 de 25 car. stă pe un rând și pe mobil, rândul USP 2 trece pe 2 rânduri pe desktop și pe mobil).
- **Alt text S5:** copy.md spune că se scrie după alegerea imaginii. Propunerea mea, folosită acum în `COPY["alt_s5"]`: „Teanc de clătite subțiri, aurii, cu zahăr pudră” (47 car.). De aprobat sau înlocuit.
- **Alt text rețeta 2:** am folosit varianta „aburi” („Pizza de casă cu pepperoni, abia scoasă, din care ies aburi”), pentru că GIF-ul propus e cu aburi, fără felie trasă (fără mână, diferit de NC2).
- Pastilele 01 / 02 / 03 sunt decorative (arse în imagine), nu text nou.
