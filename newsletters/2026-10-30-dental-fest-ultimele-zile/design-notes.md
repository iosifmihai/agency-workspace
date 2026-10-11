# Design notes: newsletter „Ultimele zile Dental Fest”, 30.10.2026

**Fișier:** `newsletter.html`, ~89 KB, UTF-8, sub limita de 102 KB la care Gmail taie mesajul. Copy-ul final vine din `strategy-and-copy.md` (secțiunea 4), fără etichetele [CLIENT]/[MODIFICAT]/[NOU]. Previzualizări: `preview.png` (700 px) și `preview-mobile.png` (375 px).

## Layout
- **Template:** DWF, reluat din `2026-10-26-kometabio/newsletter.html`.
  - Container de 700 px pe fundal #F4F4F4.
  - Poppins din Google Fonts, cu fallback Arial/Helvetica. Outlook este forțat pe Arial prin `<!--[if mso]>`.
  - Accent #FF5E08, piersică #FAE1D3, separatoare de 1 px #B3C0CE, footer negru.
- **Ordinea blocurilor:**
  1. preheader ascuns (General A);
  2. logo;
  3. meniu portocaliu, **comentat** (strategia recomandă fără meniu; se activează scoțând comentariul);
  4. hero placeholder 1400×934, afișat 700×467, link /produse/promotii;
  5. titlu și intro;
  6. bandă cu 2 chip-uri de dată (31 OCT plin, 5 NOV contur);
  7. „DESCOPERĂ TOATE PROMOȚIILE” plus bara de split cabinet / laborator (2 pastile cu contur);
  8. separator „Patru direcții. Două termene.”;
  9. LM Dental: badge de termen, text, 4 sloturi (2 rânduri), „COMANDĂ INSTRUMENTELE LM”;
  10. Solventum: 4 sloturi, „VEZI OFERTELE SOLVENTUM”;
  11. Renfert: eticheta „PENTRU LABORATOR”, 4 sloturi, „VEZI OFERTELE RENFERT” și link text spre promoțiile de laborator;
  12. autoclave Fomos și Melag pe piersică: listă cu 3 bife, 2 sloturi, „SOLICITĂ OFERTA PENTRU AUTOCLAVĂ”;
  13. spațiu alb, apoi blocul de termen portocaliu cu cronologia 31 OCT / 5 NOV și „COMANDĂ ACUM” (buton alb);
  14. consultanță pe piersică: „SUNĂ LA 0268.31.55.44” și link spre contact;
  15. bandă de încredere, disclaimer, semnătură;
  16. footer negru (social, GDPR verbatim, „Trimis cu drag din Brașov.”, dezabonare).
- **Coloane:** hibride, adică `div` inline-block cu tabele-fantomă MSO. Pe mobil (≤520 px) devin o singură coloană chiar și fără media queries.
- **Butoane:** pastile de 40 px, radius 20 px. În Outlook sunt `v:roundrect` VML (arcsize 50%), în rest `<a>` stilizat. Pe mobil ocupă toată lățimea. Pastilele cu contur din bara de split au în VML `strokecolor` portocaliu.
- **Chip-uri de dată:** doar HTML/CSS (tabel de 60 px cu ziua la 28 px și luna la 12 px), fără imagini sau GIF. În Outlook colțurile sunt drepte (border-radius ignorat), restul rămâne identic.
- **Marcaje în cod:**
  - `<!-- BLOCK: nume -->` pe fiecare text;
  - `<!-- TODO-PRODUS: secțiune, slot N -->` pe fiecare card gol (14 în total: LM 4, Solventum 4, Renfert 4, autoclave 2);
  - `<!-- ROW START ... -->` / `<!-- ROW END ... -->` pe fiecare rând de 2 carduri. Pentru a scoate un rând (de exemplu Renfert rândul 2), se șterge tot între cele două comentarii;
  - `TODO-ASSET` pe hero și pe imaginile de produs;
  - `DE CONFIRMAT` lângă fiecare link neconfirmat;
  - subiectele și preheaderele celor 4 variante sunt în comentariul din `<head>`.

## Cum se completează un slot
În fiecare card se înlocuiesc: `src`-ul imaginii (placehold.co → poza produsului, 600×600, fond alb), `alt="[NUME PRODUS]"`, `[NUME PRODUS]`, `[PREȚ VECHI]`, `[PREȚ NOU]` și `[LINK PRODUS]` (apare de **3 ori** pe card: imagine, VML, `<a>`). `?utm_content=...` rămâne după URL. Badge-ul: LM are „-30%”; Solventum și Renfert au `[-X%]`, care se înlocuiește cu procentul real calculat din prețuri (sau se șterge `<tr>`-ul badge-ului). Autoclavele nu au badge și nici valoare de rată.

## Ce e marcat „DE CONFIRMAT” în HTML
Toate au deocamdată rezerva https://medidentexim.ro/produse/promotii în `href`.
1. **PROMOȚII CABINET:** URL-ul subcategoriei „PROMOTII CABINET”.
2. **COMANDĂ INSTRUMENTELE LM:** URL-ul categoriei LM Restaurare în promoții.
3. **VEZI OFERTELE SOLVENTUM:** „Dental Brand Days - Solventum” sau /3m (de verificat că arată prețurile promo).
4. **VEZI OFERTELE RENFERT:** „Dental Brand Days - Renfert” sau /renfert.
5. **SOLICITĂ OFERTA PENTRU AUTOCLAVĂ:** pus pe /contact (logic pentru cerere de ofertă); clientul ceruse /produse/promotii.
6. **Link laborator** (/oferte-speciale/oferte-speciale-laborator): indicat de client pe 21.09, se retestează.
7. **Filtek:** dacă intră în sloturile Solventum, de verificat că oferta -30% mai e activă pe 30.10 (notă în cod).

## Asset-uri de înlocuit
| Unde | Acum | Ce trebuie pus |
|---|---|---|
| Hero | placehold.co 1400×934 PNG, „HERO DENTAL FEST · 1400x934” | Bannerul făcut de utilizator, 1400×934 (3:2), urcat în theMarketer. Păstrăm `width="700" height="467"` și alt text-ul nou. Fără umbre în spatele produselor. |
| 14 sloturi de produs | placehold.co 600×600 PNG gri, „LM · PRODUS 1” etc. | Pozele produselor (fond alb, pătrate), afișate la 200 px. |
| Logo, iconițe social | URL-uri reale (aceleași ca la KometaBio) | Nu e nevoie de nimic. |

Placeholder-ele folosesc `/png` în URL: fără el, placehold.co servește SVG, pe care Gmail și Outlook nu îl afișează.

## Contrast (WCAG 2.1)
Aceleași decizii ca la KometaBio, plus un token nou pentru textul mic portocaliu.
- **Butoanele pline (alb pe #FF5E08, 3,06:1)** rămân excepția de brand asumată; varianta conformă e #C74400 pe fundal (4,94:1).
- **Text mic portocaliu → #B03C00** (6,0:1 pe alb, 4,8:1 pe piersică): etichetele „PENTRU LABORATOR” / „PENTRU CABINET · STERILIZARE”, ziua săptămânii de lângă chip-uri, textul pastilelor cu contur din bara de split și textul butonului alb din blocul de termen. #FF5E08 la 12–15 px pe alb ar avea doar 3,06:1. Dacă se vrea portocaliul de brand, find/replace `#B03C00` → `#FF5E08`.
- **Text mare portocaliu (#FF5E08):** „pe 5 noiembrie” din titlu, „Două termene.”, prețul nou (20 px bold), ziua din chip-ul cu contur (28 px bold). Toate sunt ≥18,66 px bold, deci trec la 3:1.
- **Chip-uri:** ziua albă pe portocaliu e text mare (OK); luna e neagră pe portocaliu (6,86:1), nu albă, pentru că 12 px alb nu trece.
- **Badge-ul LM** („SE ÎNCHEIE SÂMBĂTĂ, 31 OCTOMBRIE”): text negru pe portocaliu (6,86:1), ca eticheta „ARTICOL TEHNIC” de la KometaBio.
- **Blocul de termen:** titlul alb (24 px bold, text mare, OK), corpul și cronologia negre pe portocaliu (6,86:1). Designerul cerea text alb; la 15 px albul nu trece AA.
- **Meniu** (dacă se activează): negru pe portocaliu (6,86:1).
- **Corpul textului:** negru pe alb sau piersică (16,8:1); griurile #555555 / #6B6B6B pe alb (≥5,3:1); alb pe negru în footer.
- **Accesibilitate în cod:** `role="presentation"` pe toate tabelele, alt text în română, bifele decorative au `aria-hidden`. Data, procentul și oferta LM există ca text live (intro, chip-uri, badge), nu doar în banner.

## Dark mode
- Ca la KometaBio: fundaluri #141414/#1E1E1E, piersica devine #3A2A20, textul #F2F2F2, accentul rămâne.
- `.accent-dark` (#B03C00) devine #FF8A4C în dark mode, pentru lizibilitate pe fundal închis.
- Badge-urile de procent devin portocalii cu text negru (negrul pe card închis nu se vedea).
- Blocul de termen și chip-urile au culori fixe și nu se inversează.

## UTM
- În HTML e doar `?utm_content=<element>` (hero, cta-toate, split-cabinet, split-laborator, lm-produs-1…4, cta-lm, solventum-produs-1…4, cta-solventum, renfert-produs-1…4, cta-renfert, renfert-laborator, autoclav-fomos, autoclav-melag, cta-autoclav, cta-termen, contact, logo, meniu-*).
- `utm_source=themarketer`, `utm_medium=email`, `utm_campaign=dental-fest-ultimele-zile_2026-10-30` se setează pe campanie în theMarketer, ca la KometaBio. Așa am economisit ~7 KB.
- **Dacă theMarketer nu le adaugă:** find/replace `?utm_content=` cu `?utm_source=themarketer&amp;utm_medium=email&amp;utm_campaign=dental-fest-ultimele-zile_2026-10-30&amp;utm_content=`. Fișierul ajunge la ~97 KB, tot sub 102 KB.
- **`utm_term` pe segment** (cos, promotii-vazute, clienti-activi, general): se setează pe fiecare variantă sau prin find/replace în copia HTML a variantei (instrucțiuni în `<head>`).
- `tel:+40268315544` nu are UTM.

## Import în theMarketer
1. Patru campanii (Cos, Promotii vazute, Clienti activi, General), același HTML. Editorul **HTML / Cod sursă**: lipiți tot fișierul.
2. Pe fiecare variantă: subiectul și preheaderul din comentariul din `<head>`. Înlocuiți și textul din div-ul de preheader ascuns (acum are General A).
3. Completați cele 14 sloturi (sau ștergeți rândurile nefolosite), urcați bannerul și pozele, înlocuiți `src`-urile `TODO-ASSET`.
4. `{{unsubscribe_link}}`: verificați merge tag-ul exact sau folosiți footerul nativ theMarketer. Textul GDPR rămâne verbatim.
5. Test în Gmail web și app, Outlook desktop, Apple Mail iOS: grila 2×2 → 1 coloană, chip-urile de dată nu se rup, pastilele rămân rotunjite (VML), linkul `tel:`.

## Fișier sursă
Generatorul (Python, opțional) e în scratchpad-ul sesiunii (`dentalfest/build.py`). HTML-ul e sursa de adevăr; se editează direct.
