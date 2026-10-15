# Welcome Email 1: direcția de design (bun venit + cont + BUNVENIT + categorii)

Autor: UI Designer, 15.10.2026. Bază: `brief.md`, `copy.md` (copy final, preluat cuvânt cu cuvânt), `discovery.md` 5-7, `refs/site-hero-bunvenit.png`.
Documentul e o recomandare închisă, nu o listă de variante. Orice text din email vine din `copy.md`; aici se decide doar cum arată.

Ideea vizuală: **„cămara de după-amiază”**. Emailul continuă exact hero-ul de pe site (interior rustic, lumină caldă prin fereastră, serif mare alb, pastilă cărămizie), apoi coboară în pagini liniștite, deschise la culoare, ca o cămară așezată: mult aer, chenare subțiri, fotografii cu aceeași lumină. Abonatul tocmai a văzut pop-up-ul; emailul trebuie să pară aceeași casă, nu o campanie nouă.

---

## 1. Ce preluăm din referința de pe site și de ce

| Element din `site-hero-bunvenit.png` | Unde în W1 | De ce |
|---|---|---|
| Fotografie caldă pe toată lățimea, text alb serif aliniat stânga, sus | S1-hero | Continuitate directă pop-up -> site -> email; recunoaștere în prima secundă. |
| Titlu serif foarte mare („Bun venit în Hambar”), subtitlu serif mai mic | S1 H1 + text | Același ritm ierarhic: titlu, ofertă, buton, condiție. |
| Pastilă #c93f13 cu text alb | toate CTA-urile | E butonul de brand. Pe site e mai rotunjit; în email păstrăm pastila completă (raza = jumătate din înălțime). |
| Rândul mic „Ofertă valabilă la prima comandă...” sub buton | S1, sub CTA | Condiția stă lângă ofertă, ca pe site. |

**Ce NU preluăm**

| Nu preluăm | Motiv |
|---|---|
| Textul „BUNVENIT” ca parte din titlu, în hero | Codul primește o casetă proprie în S3, unde e ușor de citit și de copiat. În hero apare doar în fraza din copy. |
| CTA-ul „Descoperă produsele” | Obiectivul emailului e contul; CTA-ul este „Creează-ți contul” (copy.md). |
| Gradient întunecat peste fotografie (overlay CSS) | Gradientele CSS peste imagini de fundal nu sunt suportate uniform (Outlook, unele versiuni Gmail). Întunecarea se obține din fotografie (vezi 4.2). |
| Verde, mov, galben accent, #877b71 | Nu trec contrastul pentru text (discovery 5); nu sunt necesare aici. Emailul rămâne în 5 culori. |

---

## 2. Ordinea secțiunilor și culorile

Doar culori din paleta oficială (discovery 5): #241e1e, #f7f6f5, #efedea, #413535, #c93f13, #c5bfb7 (chenare, doar decorativ), plus #ffffff pentru textul pe fotografie și pe buton.

| # | Secțiune | Fundal | Text | Separare față de următoarea |
|---|---|---|---|---|
| S0 | Header: logotip | #f7f6f5 | - | direct în fotografie |
| S1 | Hero: IMG1 cu text live peste | IMG1, fallback #413535 | #ffffff | margine dreaptă a fotografiei |
| S2 | Brand | #f7f6f5 | #241e1e | schimbare de fundal |
| S3 | Cont + cod BUNVENIT | #efedea | #241e1e | schimbare de fundal |
| S4 | Categorii (grilă 6 carduri) | #f7f6f5 | #241e1e | schimbare de fundal |
| S5 | Încredere (IMG8 + text) | #efedea | #241e1e | schimbare de fundal |
| S6 | Footer | #413535 | #efedea | - |

Secvența: **deschis, foto caldă, deschis, crem, deschis, crem, maro**. Alternanța #f7f6f5 / #efedea e discretă (aceeași familie); delimitarea vine din fundal, nu din linii. Singurul element saturat din tot emailul e #c93f13 pe butoane, deci ochiul ajunge mereu la CTA. Fundalul exterior (în jurul containerului de 600px) e #efedea.

---

## 3. Sistem comun (600px, tabele, CSS inline, mobil sub 600px)

- Container `table` 600px, `role="presentation"`, `bgcolor` pe fiecare `td` de secțiune (și `background-color` inline). Media query `@media only screen and (max-width:599px)`: container `width:100% !important`.
- Padding lateral: **40px desktop, 20px mobil** (clasa `.px`). Padding vertical de secțiune: **56px desktop, 40px mobil** (clasa `.py`), excepții notate la fiecare secțiune.
- Fonturi:
  - Titluri: `font-family:"Louize Display", Georgia, "Times New Roman", serif; font-weight:400;` (Louize e Regular; nu se pune bold, altfel Georgia apare faux-bold diferit de site).
  - Text, butoane, etichete: `font-family:"GT America", Helvetica, Arial, sans-serif;`
  - `@font-face` cu `louize-display-regular.woff2` și `gt-america-standard-regular.woff2` din `clients/hambar/fonts/`, găzduite pe CDN-ul imaginilor, în `<style>` din `<head>`. Funcționează în Apple Mail / iOS; restul văd Georgia și Helvetica/Arial, iar dimensiunile de mai jos sunt alese să arate corect și în fallback.
- Scara tipografică (desktop / mobil, mărime/line-height în px):

| Rol | Font | Desktop | Mobil | Culoare |
|---|---|---|---|---|
| H1 hero | Louize | 52/56 | 38/42 | #ffffff |
| Text hero | Louize | 24/32 | 20/28 | #ffffff |
| H2 secțiune | Louize | 36/42 | 28/34 | #241e1e |
| Cod BUNVENIT | Louize | 44/48, letter-spacing 4px | 34/40, letter-spacing 3px | #241e1e |
| Nume categorie | Louize | 22/28 | 18/24 | #241e1e |
| Supratitlu / etichetă | GT America, uppercase, letter-spacing 1.5px | 13/18 | 12/16 | #241e1e |
| Text curent | GT America | 17/27 | 16/25 | #241e1e |
| Descriere card | GT America | 15/22 | 14/20 | #241e1e |
| Text mic (condiții, footer) | GT America | 13/20 | 13/20 | #241e1e sau #efedea / #ffffff |
| Buton | GT America, 600 (fallback bold) | 17/56 | 17/52 | #ffffff |

- Linkuri text: culoarea textului din jur (#241e1e pe deschis, #efedea în footer), `text-decoration:underline`. Niciun link în #c93f13 pe text mic (4.63:1 e la limită; rezervăm accentul pentru butoane).

### 3.1 Buton (bulletproof pastilă)

- Desktop: **280 x 56px**, `background-color:#c93f13`, `border-radius:28px`, text `#ffffff` 17px, centrat, fără chenar. Mobil: `width:100%`, max 335px, înălțime 52px, `border-radius:26px`.
- Construcție: `<a>` stilizat ca bloc (`display:inline-block; line-height:56px; padding:0 32px; mso-hide:all` pe varianta HTML) + VML pentru Outlook desktop:
  `<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="{{SIGNUP_URL}}" style="height:56px;v-text-anchor:middle;width:280px;" arcsize="50%" stroke="f" fillcolor="#c93f13"><center style="color:#ffffff;font-family:Helvetica,Arial,sans-serif;font-size:17px;">Creează-ți contul</center></v:roundrect><![endif]-->`
- Zonă de atingere minim 44px pe toate CTA-urile. Text buton: exact „Creează-ți contul”.

---

## 4. Specificații pe secțiuni

### S0 Header (#f7f6f5)
- Padding 28px sus, 24px jos, centrat.
- `hambar-logotype.png` (640 x 104, fill #241e1e), afișat **160 x 26px** (`width="160"`, fără `height` forțat diferit de raport: 160 / 640 x 104 = 26). Exportul 640px acoperă 4x; e suficient și pentru retina. Link spre https://hambar.ro cu UTM `w1-header`, `alt="Hambar"`.
- Fără meniu, fără simbol.

### S1 Hero (IMG1 cu text live)

**Decizie: text HTML live peste imagine de fundal, cu VML pentru Outlook și culoare de rezervă solidă.** Nu coacem textul în imagine.
De ce: (1) cu imaginile blocate (Outlook implicit, unele conturi Gmail corporate) mesajul „Bun venit în Hambar / 50 de lei / BUNVENIT” și butonul trebuie să rămână vizibile, iar culoarea de rezervă #413535 le face lizibile; (2) textul live e accesibil pentru cititoare de ecran și se poate căuta; (3) hero-ul reproduce site-ul unde textul e tot live; (4) dark mode nu poate inversa un text copt într-o imagine, dar poate respecta un text alb pe fundal închis. Costul (VML, test în Outlook) e acceptat.

- **Celula:** `td` cu `background="IMG1.jpg"`, `bgcolor="#413535"`, `style="background-image:url(IMG1.jpg); background-color:#413535; background-size:cover; background-position:center top;"`, `width=600`, `height=750` (4:5), `valign="top"`.
- **Outlook (VML):** `<!--[if gte mso 9]><v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width:600px;height:750px;"><v:fill type="frame" src="IMG1.jpg" color="#413535"/><v:textbox inset="0,0,0,0"><![endif]-->` ... conținut ... `<!--[if gte mso 9]></v:textbox></v:rect><![endif]-->`.
- **Conținut (aliniat stânga, ca pe site):** padding 56px sus, 40px lateral (mobil 36px sus, 20px lateral). Ordinea din copy: H1 „Bun venit în Hambar”, 16px spațiu, text hero (Louize 24/32, max 440px lățime ca să cadă pe 2-3 rânduri), 28px spațiu, buton, 12px spațiu, text mic „Ofertă valabilă la prima comandă, de min. 250 de lei.” (GT America 13/20, #ffffff).
- Conținutul ocupă ~330px din cei 750px pe desktop; restul fotografiei (masa cu ulcior, zacuscă, pâine, miere) se vede dedesubt. Text-shadow `0 1px 12px rgba(36,30,30,0.45)` pe H1 și textul hero (ignorat unde nu e suportat; contrastul nu depinde de el).
- **Mobil (sub 600px):** celula devine `width:100%; height:auto; min-height:540px` (clasa `.hero`), `background-position:center top`. La 375px, H1 38/42 pe 2 rânduri + text pe 3-4 rânduri + buton intră în ~330px, deci butonul e vizibil fără scroll pe un ecran de 667px (cu header 78px și preheader-ul clientului).
- **IMG1 (fix, 4:5):** export 1200 x 1500, afișat **600 x 750**. Crop: fotografia completă, fără tăiere pe desktop. Pe mobil (raport ~375 x 540, adică aprox. 0.69) `background-size:cover` taie ~6% din fiecare lateral; obiectele importante trebuie să stea în treimea de jos și în centrul orizontal. Cerință pentru imaginea generată: **treimea de sus (aprox. 0-500px din 1500) trebuie să fie zonă calmă și întunecată** (perete maro în umbră, fără pete de lumină puternice sub text). Fără dimensiunea asta, contrastul textului alb nu e garantat; dacă imaginea livrată are luminozitate mare sus, o întunecăm în export (curbă de tonuri pe zona de sus, nu overlay în cod).
- Alt text: imaginea e fundal, deci nu are `alt`; descrierea din copy.md („Masă rustică cu zacuscă, pâine, miere și un ulcior de lut, în lumina de după-amiază”) se pune ca `<span>` ascuns vizual (`.sr-only`) la sfârșitul celulei, pentru cititoare de ecran.

### S2 Brand (#f7f6f5)
- Padding 56/40 (mobil 40/20). Aliniere: **stânga**, ca hero-ul; coloană de text max 520px.
- H2 (Louize 36/42), 20px spațiu, două paragrafe GT America 17/27 cu 16px între ele, în ordinea din copy.
- Fără imagine, fără buton. Secțiunea e o pauză scurtă de citit între hero și ofertă.

### S3 Cont + cod (#efedea)
- Padding 56/40 (mobil 40/20). Aliniere stânga pentru titlu, text și listă; caseta, butonul și textul mic sunt centrate.
- H2, 16px, text introductiv GT America 17/27, 16px, listă.
- **Lista cu bife:** tabel cu 3 rânduri, coloana stângă 28px cu bifa „✓” ca text (caracter U+2713, nu emoji; `font-family:Arial; color:#241e1e; font-size:17px`), coloana dreaptă textul GT America 17/27. 8px între rânduri. Nu folosim `<ul>` (indentare inconsistentă între clienți).
- **Caseta cod BUNVENIT:** 28px sub listă. Tabel centrat, **400px** desktop (mobil 100%), `background-color:#f7f6f5`, `border:2px solid #241e1e`, `border-radius:12px` (Outlook o arată dreaptă, acceptabil), padding 24px sus/jos, 24px lateral. Conținut centrat:
  - Eticheta „Codul tău”: GT America 13/18, uppercase, letter-spacing 1.5px, #241e1e.
  - 8px, apoi „BUNVENIT”: Louize 44/48, letter-spacing 4px, #241e1e, text live selectabil (`user-select:all` pentru clienții care îl suportă). Nu e link (evită ca iOS să îl transforme în link albastru; dacă apare, se forțează culoarea cu `a[x-apple-data-detectors]`).
  - 8px, apoi textul „50 de lei discount la prima comandă, de min. 250 de lei.”: GT America 15/22.
- 28px, apoi butonul (spec 3.1), apoi 16px și textul mic despre comanda minimă per producător: GT America 13/20, #241e1e, centrat, max 440px.

### S4 Categorii (#f7f6f5)
- Padding 56px sus, 48px jos; lateral **20px** (excepție, ca grila să aibă loc). Titlul și textul introductiv au padding lateral intern 20px în plus (deci tot 40px, aliniate cu restul).
- H2 „Din cămara Hambar” + text, aliniat stânga, 32px până la grilă.
- **Grilă desktop: 2 coloane x 3 rânduri.** 560px utili = card 270px + gutter 20px + card 270px. Între rânduri 32px. Ordinea din copy: rândul 1 Zacuscă & Murături / Brânzeturi & Lactate; rândul 2 Carne, Mezeluri & Pește / Miere & Dulcețuri; rândul 3 Pâine și Patiserie / Coșuri și Cadouri.
- **Card:** fără fundal și fără chenar (fotografia e cardul). De sus în jos: imagine 270 x 270, `border-radius:8px`, link; 14px; nume categorie Louize 22/28, link #241e1e fără subliniere (subliniere doar la hover unde e suportat); 6px; descriere GT America 15/22. Alinierea textului: stânga. Textele cele mai lungi (Zacuscă, Carne) ajung la 3-4 rânduri; celulele din același rând au `valign="top"`, deci diferența de înălțime nu strică grila.
- Construcție: fiecare rând e un tabel cu două `td` de 270px și un `td` de 20px; pe mobil coloanele devin `display:block` doar sub 340px (vezi mai jos).
- **Mobil:**
  - **340-599px (majoritatea telefoanelor):** rămân **2 coloane**, fiecare `width:48%`, gutter 4%, imaginile `width:100%; height:auto` (aprox. 160px fiecare la 375px), nume 18/24, descriere 14/20. Ales în locul stivuirii pe o coloană: 6 carduri stivuite ar însemna ~6 x 420px = peste 2500px de scroll pentru un CTA secundar; în 2 coloane grila are ~1050px și se citește ca un raft. Descrierile rămân integral (copy final).
  - **Sub 340px (ecrane foarte mici, iPhone SE 1):** cardurile trec pe **o coloană**, imagine 100%, prin clasa `.stack` (`display:block !important; width:100% !important`).
- **Link „Vezi toate categoriile”:** 36px sub grilă, centrat, GT America 16/24, #241e1e, subliniat, urmat de săgeată text „→” (U+2192). Nu e buton, ca să nu concureze cu „Creează-ți contul”.
- **IMG2-IMG7 (fix, 1:1):** export 1024 x 1024 sau mai mare, livrat la **560 x 560** (2x), afișat **270 x 270** desktop, ~160 x 160 mobil. Crop: centrat, fără tăiere (1:1 pe 1:1). Subiectul trebuie să ocupe zona centrală ~70%, pentru că la 160px detaliile mici dispar. Toate 6 cu aceeași lumină laterală caldă și același unghi, ca grila să arate unitar. Alt text exact din copy.md, secțiunea 6.

### S5 Încredere (#efedea)
- Fără padding sus; imaginea începe direct la marginea secțiunii, pe toată lățimea.
- **IMG8 (fix, 3:2):** export 1200 x 800, afișat **600 x 400** desktop, `width:100%; height:auto` pe mobil (375 x 250). Crop: complet, fără tăiere. Subiect (mâinile cu brânza / borcanul) în treimea din mijloc; marginile pot fi ușor neclare. Alt text din copy.md.
- Sub imagine, padding 44px sus, 40 lateral, 56 jos (mobil 32/20/40), aliniat stânga:
  - Supratitlu „Producător verificat”: GT America 13/18, uppercase, letter-spacing 1.5px, #241e1e. Nu folosim verdele badge-ului #26974a (3.47:1, eșuează).
  - 10px, H2 „Până acum, verificarea o făceai tu”.
  - 16px, paragraf GT America 17/27.
  - 20px, link „Cum selectăm producătorii” GT America 16/24, #241e1e, subliniat, cu „→”.

### S6 Footer (#413535)
- Padding 48px sus, 40 lateral, 40 jos (mobil 40/20/32). Totul centrat, textul în #efedea.
- `hambar-logotype-white.png` (640 x 104), afișat **140 x 23px**, link spre https://hambar.ro, alt din copy.md („Hambar, gust adevărat, de la oameni buni livrat”). 14px sub logo: tagline-ul, Louize 18/26, #efedea.
- 28px, rândul aplicației: „Descarcă aplicația: App Store · Google Play”, GT America 14/22, linkurile subliniate, #efedea.
- 20px, iconițele social: 4 iconițe albe 28 x 28 (export 56 x 56 PNG), spațiate la 16px, ordinea Facebook, Instagram, TikTok, YouTube, alt pe fiecare.
- 20px, linkuri utile „Cum livrăm · Cum selectăm producătorii”, GT America 14/22.
- 24px, linie separatoare 1px #c5bfb7, lățime 80px, centrată, decorativă (fără opacitate, nesigură în email).
- 24px, blocul legal din copy.md, GT America 13/20, #efedea, cu 12px între paragrafe; „Dezabonează-te aici” subliniat, link `{{UNSUBSCRIBE_URL}}`.
- `hambar-symbol-white.png` (188 x 112) **nu se folosește** în W1: un singur semn de brand per zonă; simbolul rămâne rezervat pentru eventualul avatar BIMI / pentru emailuri mai scurte din serie.

---

## 5. Logo: rezumat utilizare

| Fișier | Dimensiune sursă | Unde | Afișat | Fundal |
|---|---|---|---|---|
| `hambar-logotype.png` | 640 x 104 | S0 header | 160 x 26 | #f7f6f5 (15.21:1) |
| `hambar-logotype-white.png` | 640 x 104 | S6 footer | 140 x 23 | #413535 |
| `hambar-symbol.png`, `-white.png` | 188 x 112 | nu se folosesc în W1 | - | - |

Logo-ul nu stă pe fotografie (regulă discovery 7: fără plasare pe fotografii aglomerate). Fără umbre, fără recolorare, fără deformare (doar `width` setat; `height` calculat proporțional și scris explicit pentru Outlook).

---

## 6. Dark mode

- `<meta name="color-scheme" content="light dark">` și `<meta name="supported-color-schemes" content="light dark">`.
- **Apple Mail / iOS (respectă media query):** `@media (prefers-color-scheme: dark)` cu: fundal secțiuni #f7f6f5 și #efedea -> #241e1e și #413535 (alternanța se păstrează), text #241e1e -> #efedea, chenarul casetei de cod #241e1e -> #efedea, fundalul casetei -> #241e1e. Butonul #c93f13 și textul alb rămân neschimbate. Hero și footer rămân neschimbate (sunt deja închise). Logo-ul din header se schimbă pe `hambar-logotype-white.png` prin două imagini (`.logo-light` / `.logo-dark` cu `display:none` comutat).
- **Gmail app (inversare forțată parțială) și Outlook.com:** fundalurile deschise se închid automat; textul #241e1e devine deschis. Riscul e logotipul negru pe fundal închis. Soluția: pentru header, logotipul PNG se exportă **pe fundal solid #f7f6f5** (nu transparent), cu `border-radius` 0, ca logo-ul să rămână vizibil chiar dacă fundalul secțiunii se închide. Diferența de nuanță e acceptabilă și rară.
- Outlook.com: atribute `[data-ogsc]` / `[data-ogsb]` pentru aceleași schimbări ca la Apple, unde e cazul.
- Textul alb din hero și din footer nu se inversează (fundalurile sunt deja închise). Butonul: pastila e `bgcolor` pe `td` + `background-color` pe `<a>`, ca să nu dispară la inversare.

---

## 7. Contrast (WCAG AA, 4.5:1 text normal, 3:1 text mare)

| Combinație | Unde | Raport | Verdict |
|---|---|---|---|
| #241e1e pe #f7f6f5 | S2, S4, header | 15.21 | Trece |
| #241e1e pe #efedea | S3, S5 | ~14.0 | Trece |
| #241e1e pe #f7f6f5 (caseta cod) | S3 | 15.21 | Trece |
| #ffffff pe #c93f13 | butoane | 5.0 | Trece (text 17px) |
| #efedea pe #413535 | footer | 10.07 | Trece |
| #ffffff pe #413535 | hero cu imaginile oprite | ~11.5 | Trece |
| #ffffff pe IMG1 (zona de text) | hero | țintă minimă 4.5 | Se verifică la livrarea imaginii: luminanța medie în zona de text trebuie să fie sub cea a culorii #767676 (alb pe #767676 = 4.54). Dacă nu, se întunecă zona în export. |
| #c5bfb7 | linie footer | 1.69 | Doar decor, nu text |
| #c93f13 pe #f7f6f5 | nefolosit pentru text | 4.63 | Evitat intenționat |

Text minim în email: 13px (doar condiții și footer); textul de citit e 15-17px.

---

## 8. Imagini: rezumat sloturi (fixe)

| Slot | Raport | Export livrat | Afișat desktop | Afișat mobil | Crop | Greutate |
|---|---|---|---|---|---|---|
| IMG1 hero | 4:5 | 1200 x 1500 | 600 x 750 (fundal) | 100% x min. 540, cover, top | fără tăiere desktop; ~6% lateral pe mobil; treimea de sus calmă și întunecată | sub 250 KB |
| IMG2-IMG7 categorii | 1:1 | 560 x 560 | 270 x 270 | ~160 x 160 | fără tăiere; subiect în centrul de 70% | sub 80 KB fiecare |
| IMG8 încredere | 3:2 | 1200 x 800 | 600 x 400 | 100% (375 x 250) | fără tăiere; subiect în treimea din mijloc | sub 180 KB |

JPG progresiv, sRGB. Greutate totală a emailului (imagini) sub ~1 MB. Codul HTML sub 100 KB, ca Gmail să nu taie mesajul.

---

## 9. Checklist QA înainte de trimitere

- Outlook 2016/365 Windows: hero VML afișează imaginea și textul; butoanele VML au raza pastilei.
- Imagini oprite (Outlook, Gmail): hero pe #413535 cu text alb lizibil; codul BUNVENIT, butoanele și numele categoriilor sunt text.
- iPhone 375px: butonul hero vizibil fără scroll; grila 2 x 3 fără depășire orizontală.
- Dark mode în Apple Mail, Gmail iOS, Outlook.com: logo vizibil, caseta de cod lizibilă.
- Toate linkurile au UTM `w1-<secțiune>` (copy.md, secțiunea 5); `{{SIGNUP_URL}}` și `{{UNSUBSCRIBE_URL}}` înlocuite cu valorile din theMarketer.
