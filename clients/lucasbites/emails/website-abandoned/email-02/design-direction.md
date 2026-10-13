# Website Abandoned, Email 2: direcția de design

Autor: UI Designer, 13.10.2026. Bază: `strategy.md`, `copy.md` (build de bază: Clătite + Cookies), `brief.md`, `../README.md`, `../email-01/` (`design-direction.md`, `build.py`, `preview.png`), `../../browse-abandonment/email-01/build.py`. Textele sunt preluate exact în `COPY` și `RECIPES` din `build.py`.

Ideea vizuală: **„fișa de rețetă”**. Email 1 era meniul casei (categorii); Email 2 deschide rețetarul: două fișe orizontale, alternate stânga/dreapta, cu fotografia decupată „din rețetar” și marginea ruptă.

## 1. Ce rămâne din Email 1 (același flow) / ce se schimbă

| Rămâne | Detalii |
|---|---|
| Tranziția cu margine ruptă + dungă de culoare | aceeași funcție `torn_divider` (1200 x 56, afișat 600 x 28), seed-uri noi |
| Foto decupaj: colțuri sus rotunjite, jos rupt, pe card alb | aceeași funcție `clipping`, același format 238 px ca în cardul mare din Email 1 |
| Card alb, contur negru 3px, colțuri 20px, chip negru cu text portocaliu | identic |
| Buton contur pe carduri, buton plin portocaliu pe negru în S5 | identic |
| USP: 3 coloane de 193px, Akrobat Bold 18/22, `nowrap` | identic |
| Închidere pe negru, footer alb identic | identic |

| Nou | Detalii |
|---|---|
| **Hero roz, text negru** | Email 1 avea hero negru cu text portocaliu. Logo complet pe roz. |
| **Secvența:** roz, portocaliu, alb, turcoaz, negru, alb | Email 1: negru, turcoaz, alb, roz, negru, alb. |
| **2 fișe orizontale alternate** | card 1 foto stânga, card 2 foto dreapta (`dir="rtl"` pe celula cardului, `dir="ltr"` pe coloane); pe mobil foto mereu deasupra. |
| **Secțiunea de recomandări** | chip centrat „MERITĂ ÎNCERCATE”, H2, intro, blocul feed, buton contur. |
| **Iconițe USP noi** | spatulă (simplu), lupă (le recunoști), două pungi (două mixuri, transport). Nefolosite în serie. |

## 2. Secvența

| # | Secțiune | Fundal | Tranziție (dunga) |
|---|---|---|---|
| S0-S1 | Logo 180px, salut, H1 „HAI ÎN / BUCĂTĂRIE!” 64/60 (mobil 48/46), text | roz | roz -> portocaliu (turcoaz) |
| S2 | Supratitlu, H2, intro, 2 fișe, „Mai multe rețete” | portocaliu | portocaliu -> alb (roz) |
| S3 | Chip, H2, intro, feed, „Vezi și alte mixuri” | alb | alb -> turcoaz (portocaliu) |
| S4 | „PE SCURT” + 3 USP | turcoaz | turcoaz -> negru (roz) |
| S5 | Titlu, rând, „Hai în magazin”, „eat what you love” | negru | negru -> alb (portocaliu) |
| S6 | Footer | alb | - |

Pe mobil (375px) antetul S2 începe la ~390px, în primul ecran (strategie S1).

## 3. Specificații
- 600px, tabele, CSS inline, padding lateral 40px (mobil 20px). Fonturi `Akrobat, "Arial Narrow", Arial` / `Arial, Helvetica`.
- **Fișa de rețetă:** tabel 520px; coloană foto 262px (foto 238 + 12 padding), coloană text 252px. Chip Akrobat Bold 14; titlu Akrobat Bold 28/30 pe 2 rânduri fixe (rupere din copy.md, fiecare jumătate `nowrap`: „CLĂTITE PENTRU / TOATĂ FAMILIA”, „COOKIES CU / CIOCOLATĂ NEAGRĂ”); „Cu {produs}” Arial Bold 16; info Arial 15; buton contur 170 x 44 „Vezi rețeta”. Tot cardul e link (foto, titlu, rânduri, buton). Mobil: coloane stivuite, foto max 100%, buton pe toată lățimea.
- **Recomandări, lățime utilă: 520px pe desktop** (600 - 2 x 40), **335px pe mobil 375**. În `index.html`: 3 carduri EXEMPLU de 175px (169 + rigole), imagine 140 x 140 (`exemplu-produs.jpg`, marcată EXEMPLU), „Nume produs”, stele placeholder (`stele-exemplu.png` 90 x 16), „XX,XX lei”. Pe mobil 2 + 1. Recomandăm blocul theMarketer pe 3 coloane, imagine pătrată.
- **USP:** coloane 193px (181px utili), titluri Akrobat Bold 18/22, `white-space:nowrap`. Măsurat cu Pillow (build.py, `measure_usp`):

| Titlu | Akrobat Bold | Arial Narrow Bold | Arial Bold |
|---|---|---|---|
| SIMPLU DE FĂCUT | 121px | 140px | 168px |
| LE RECUNOȘTI | 97px | 114px | 137px |
| TRANSPORT GRATUIT | 145px | 168px | 202px |

Încap toate în Akrobat și Arial Narrow. Outlook desktop: stilul `mso` pune titlurile pe Arial 14px (~157px, încape). Doar în Arial Bold 18 (fără webfont și fără Arial Narrow) „TRANSPORT GRATUIT” depășește cu ~21px; rezerva din copy e „LIVRARE GRATIS”. Acceptat, ca în Email 1.
- Imagini oprite: tot textul e live; alt-uri din copy.md, secțiunea 4; decorative `alt=""`.
- Dark mode, VML, `mso` ca în Email 1. HTML: `index.html` 36,5 KB, `index-esp.html` 33,5 KB (sub 85 KB, marjă pentru codul blocului theMarketer, sub 102 KB).
- UTM: `utm_source=email&utm_medium=flow&utm_campaign=website_02&utm_content=` `reteta_1`, `reteta_2`, `retete_toate`, `cta_rec`, `cta_shop`; feed: `rec_feed` (moștenit). Social, `mailto:`, `tel:`, logo fără UTM.

## 4. index.html vs index-esp.html
- `index.html`: preview, cu 3 carduri EXEMPLU.
- `index-esp.html`: între `<!-- THEMARKETER_FEED START -->` și `<!-- THEMARKETER_FEED END -->` e `[RECOMANDĂRI PRODUSE THEMARKETER]`. Toată secțiunea S3 (chip, H2, intro, feed, buton, comentariul cu fallback) e între `THEMARKETER_SECTION_S3 START/END`, ca Andreea s-o ascundă întreagă când blocul nu are rezultate. Butonul „Vezi și alte mixuri” se șterge dacă blocul are butoane proprii. `ESP-MARKER` în `<head>` cu toate setările manuale.

## 5. Build
```
.venv/bin/python build.py              # assets/, index.html, index-esp.html, index-figma*.html
.venv/bin/python build.py --preview    # + preview.png (600) și preview-mobile.png (375)
.venv/bin/python build.py --sezon      # varianta Gingerbread: index-sezon.html, index-esp-sezon.html
```
Imaginile lipsă devin placeholdere la mărimea finală (476 x 476), cu același nume în `assets/`. Fișierele Figma sunt generate de `../../tools/figma_export.py` la finalul build-ului.

## 6. Schimbul de sezon Gingerbread (manual, Andreea): 1 noiembrie și 1 ianuarie
Doar cardul 1, între `<!-- CARD_RETETA_1 START -->` și `<!-- CARD_RETETA_1 END -->`. Cardul 2 și restul emailului rămân.

**Varianta A (recomandată):** rulează `build.py --sezon`, apoi în theMarketer înlocuiește tot blocul dintre marcajele `CARD_RETETA_1` cu cel din `index-esp-sezon.html`. Imaginea `assets/sezon-gingerbread.jpg` e generată la fiecare build (placeholder până vine `images/sezon-gingerbread.png`).

**Varianta B (direct în editor), în cardul 1:**
| Ce | Clătite (tot anul) | Gingerbread (1 nov - 31 dec) |
|---|---|---|
| Imagine `src` | `reteta1-clatite.jpg` | `sezon-gingerbread.jpg` |
| Alt | Clătite de casă pentru toată familia | Teanc de gingerbread pancakes |
| Chip | duminica fără grabă | Sărbătorile de iarnă |
| Titlu (2 rânduri) | CLĂTITE PENTRU / TOATĂ FAMILIA | GINGERBREAD / PANCAKES |
| Produs | Cu Crêpes Traditional | Cu Classic Pankees |
| Info | Familie · 10 min | Desert · 15 min |
| Link (toate cele 5 linkuri ale cardului + VML) | `{{URL_RETETA_CLATITE}}` | `{{URL_RETETA_GINGERBREAD}}` (fallback `{{RECIPES_URL}}`) |
| `utm_content` | `reteta_1` | `reteta_1` (neschimbat) |
Dacă rulează subiectul B, se schimbă și subiectul/preheaderul (copy.md, secțiunea 3). Pe 1 ianuarie se pune înapoi coloana din stânga.

## 7. Feedback pentru copywriter
- Toate textele au încăput; nicio rupere nedorită pe 600 și 375px. H2 S3 rupe doar „S-AR PUTEA / SĂ-ȚI PLACĂ” pe mobil (`nowrap` pe jumătăți).
- Eticheta „gustarea de după școală” (23) încape în chip pe desktop și mobil.
- Fără imagine în S5 (opțională), ca să rămână 2 fotografii.
