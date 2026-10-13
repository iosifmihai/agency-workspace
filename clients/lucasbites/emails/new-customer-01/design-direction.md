# New Customer Email 1: direcția de design (mulțumire + produse comandate + rețete)

Autor: UI Designer, 12.10.2026. Bază: `brief.md` (decizii finale), `copy.md` (copy final, folosit ca atare), `discovery.md` 5-7, `refs/ref3.png` (Blue Apron), previzualizările W1-W3.
Documentul e o recomandare închisă, nu o listă de variante. Copy-ul e cel din `copy.md`, preluat cuvânt cu cuvânt.

Ideea vizuală: **„masa ta, în curând”**. Farfurii bej fotografiate de sus care ies din cadrul emailului, ca și cum emailul ar fi o masă văzută de deasupra, mai mare decât ecranul. Curbe mari, nu valuri mici, între secțiuni. Rețetele sunt partea cea mai lungă și stau pe negru, ca farfuriile pe bleumarinul din ref3.

---

## 1. Ce preluăm din ref3 și de ce

Bleumarinul din ref3 devine **negru** (singura culoare închisă din paletă); serif-ul devine **Akrobat**.

| Pattern ref3 | Unde în NC1 | De ce |
|---|---|---|
| Farfurii fotografiate de sus care ies din cadru, pe marginile hero-ului (coloana din mijloc, sus) | S1-hero: banda de sus (pancakes stânga, clătite dreapta, „intră” sub curba albă a header-ului) și banda de jos (brownie, iese din cadru în dreapta) | Spune „masa ta, în curând” fără ambalaj inventat. Niciun email W nu are farfurii tăiate de marginea emailului. |
| Tranziții curbe mari între secțiuni | toate tranzițiile | Familia vizuală rămâne (W1-W3 au valuri), dar aici e o singură curbă amplă pe toată lățimea (jumătate de perioadă, 64px înălțime afișată), nu valul scurt cu 1-1,5 perioade. Se recunoaște ca serie, nu ca același email. |
| Titluri mari centrate | toate secțiunile, H1 76px, H2 46px | Ierarhie clară; e și regula seriei. |
| Butoane pastilă | toate CTA-urile | Bulletproof, la fel ca W3 (VML `roundrect` + `<a>`). |
| Listă de carduri albe cu imagine circulară + titlu + text + buton mic (coloana stângă: „Gluten-Free / Vegetarian...”) | S2-produse comandate | Format natural pentru 1-4 elemente dinamice: fiecare produs e un rând independent, lista crește sau scade fără să rupă grila. W1 a avut cercuri, dar 3 pe un rând, fără carduri și fără buton. |
| Zig-zag farfurie + etichetă-bandă („Chef Favorites”, „Wellness”) | S4: cele 3 carduri de rețetă și eticheta „Rețeta săptămânii” | Banda-etichetă e locul natural pentru numele rețetei. Diferit de zig-zag-ul din W2 prin două lucruri care sunt esența ref3: farfuria e tăiată de marginea emailului, iar banda colorată pleacă din marginea opusă. W2 avea obiecte întregi în coloană și săgeți desenate. |

**Ce NU preluăm și de ce**

| Nu preluăm | Motiv |
|---|---|
| Grid 2 x 2 de carduri („Beyond the Plate”) | Folosit deja în W3 S2. |
| Bloc „Don't just take our word for it” cu stele | Recenziile au fost în W1 și W3; clientul a cumpărat deja (copy.md). |
| Poză lifestyle cu cutia de livrare | Nu avem fotografie de ambalaj; brief-ul interzice ambalaje inventate. |
| Banda „Eat. Recycle. Repeat.” (text în bandă care curge) | Ar fi un al doilea slogan; avem „eat what you love”, folosit ca semnătură în S6. |
| Fundal marmură / textură sub farfurii | În afara paletei, greu în email, contrast imprevizibil cu dark mode. |
| Text pus peste fotografie (titlul din mijlocul farfuriilor) | Dispare cu imaginile oprite și cere VML de fundal în Outlook. Textul hero e HTML live **între** cele două benzi de farfurii. |
| Butoane albastre mici în carduri | Regula de brand: pe alb, pastilă neagră cu text portocaliu; pe negru, pastilă portocalie cu text negru. |

**Ce au folosit deja W1-W3 (de evitat ca layout)**: W1 stack înalt decupat pe portocaliu, 3 cercuri pe un rând, pași 1-2-3 pe turcoaz, poză de tigaie pe toată lățimea, brunch pe toată lățimea, bloc social negru. W2 lava cake pe negru + tipografie uriașă, zig-zag cu săgeți pe roz, boluri + carduri NOI/TU pe turcoaz. W3 4 farfurii negre 2 x 2 pe turcoaz, grid 2 x 2 de carduri cu plăci colorate, recenzii în trepte pe negru, grid UGC punctat pe portocaliu, bilet de transport pe roz.

---

## 2. Ordinea secțiunilor și culorile

| # | Secțiune | Fundal | Tranziție spre următoarea |
|---|---|---|---|
| S0 | Header: logo (identic W1-W3) | alb | curba albă e arsă în banda de sus a hero-ului |
| S1 | Hero: banda de farfurii sus, supratitlu, H1, salut, CTA, banda de farfurii jos | **roz #F7ACB4** | curbă roz -> portocaliu arsă în `hero-bottom.jpg`, cu farfuria de brownie peste ea |
| S2 | Produse comandate (bloc dinamic, 1-4 carduri) | portocaliu #FAA61A | `curve-orange-white.png` |
| S3 | Lista de cumpărături (listă cu bife) | alb | `curve-white-black.png` |
| S4 | Rețete: rețeta săptămânii + 3 carduri zig-zag | negru #000000 | `curve-black-pink.png` |
| S5 | Trimite-ne rețeta ta | roz #F7ACB4 | `curve-pink-turq.png` |
| S6 | Ce urmează + semnătură | **turcoaz #86D2DA** | `curve-turq-white.png` |
| S7 | Footer (identic, cu o frază marcată, vezi secțiunea 3) | alb | - |

Secvența: **alb, roz, portocaliu, alb, negru, roz, turcoaz, alb**.
W1: alb, portocaliu, alb, turcoaz, roz, negru, alb. W2: alb, negru, alb, roz, turcoaz, portocaliu, alb. W3: alb, turcoaz, alb, negru, portocaliu, roz, alb.
**Hero:** W1 portocaliu, W2 negru, W3 turcoaz, NC1 **roz** (singura culoare de brand nefolosită ca hero). **Secțiunea colorată dinaintea footer-ului:** W1 negru, W2 portocaliu, W3 roz, NC1 **turcoaz** (singura nefolosită). Rozul apare de două ori (S1, S5), despărțit de trei secțiuni: e intenționat, ca începutul și invitația personală să aibă aceeași căldură.

**Reguli de culoare aplicate:** pe roz, portocaliu, turcoaz și alb tot textul e negru. Pe negru (S4) textul e doar portocaliu; în cardul alb de rețetă textul e negru; în benzile colorate (roz, turcoaz, portocaliu) textul e negru. Butoane: pastilă neagră cu text portocaliu pe fundaluri deschise și în cardurile albe; pe negru, pastilă portocalie cu text negru, sau contur portocaliu cu text portocaliu pentru linkul secundar („Toate rețetele”). Niciun text alb pe culoare, niciun portocaliu pe alb.

---

## 3. Specificații de layout (600px, tabele, mobile-first)

### Sistem comun
- Container 600px, `bgcolor` pe fiecare `td` de secțiune. Padding lateral 40px desktop, 20px mobil (`.px`).
- Tipografie: titluri `Akrobat, "Arial Narrow", Arial, sans-serif` (webfont copiat din `welcome-03/assets/fonts/`), text `Arial, Helvetica, sans-serif`.
  - H1: Akrobat Black 76/68, uppercase (mobil 52/48).
  - H2: Akrobat Black 46/44, uppercase (mobil 34/34).
  - Titlu rețetă: Akrobat Black 36/36 (mobil 28/28). Titlu card / bandă: Akrobat Black 26/26 (mobil 20/21).
  - Supratitlu: Akrobat Bold 22, uppercase, letter-spacing 1px.
  - Text: Arial 16/24. În carduri: Arial 15/22. Text mic: Arial 13/20.
- **Buton mare:** 280 x 56, Arial 18 bold, `border-radius:28px`; pe mobil 100% (max 335). **Buton mic:** 170 x 40 (S2) sau 150 x 40 (S4), Arial 15 bold. **Buton contur:** 240 x 48, `border:2px solid #FAA61A`.
- **Curbe:** PNG 1200 x 128, afișate 600 x 64, jumătate de perioadă de sinus, amplitudine 40px (la 2x). Celula are `bgcolor` = culoarea de jos.

### S0 Header (alb)
Logo centrat, 180px (export 360px), link spre lucasbites.ro. Identic cu W1-W3, doar padding-ul de jos e 4px, pentru că sub el începe direct banda hero.

### S1 Hero (roz)
Trei rânduri, de sus în jos:
1. **`hero-top.jpg`** 1200 x 440 (afișat 600 x 220, 100% pe mobil). Fundal roz; curba albă de sus continuă header-ul. Farfuria A (pancakes cu afine, 210px afișat) iese din cadru în stânga sus, farfuria B (clătite, 200px) în dreapta sus; amândouă „intră” sub curba albă. Decorativ, `alt=""`.
2. **Text HTML live:** supratitlu, H1 pe 2 rânduri, salutul cu `{{FIRST_NAME}}` (rezerva fără prenume e în comentariu), buton mare „Alege prima rețetă”.
3. **`hero-bottom.jpg`** 1200 x 600 (afișat 600 x 300). Curba mare roz -> portocaliu coboară de la dreapta la stânga; farfuria C (brownie, 260px) o traversează și iese din cadru în dreapta. Cu link spre rețete și alt text-ul din copy.md (descrie toate 3 farfuriile).

Ordinea pe mobil cerută de copy.md (supratitlu, H1, text, buton, apoi IMG1) e respectată pentru conținut; deasupra textului stă doar banda decorativă (~137px înălțime la 375px). Butonul rămâne deasupra liniei de scroll pe un ecran de 667px.

### S2 Produse comandate (portocaliu, bloc dinamic)
- H2 + un rând de text centrat.
- **Card produs** (se repetă, max 4): tabel alb, `border-radius:20px`, fără contur (ca ref3: alb pe culoare). Coloana stângă 112px: imaginea din feed `{{ORDER_PRODUCT_IMAGE}}`, 112 x 112 (84 x 84 pe mobil), `border-radius:50%`, `border:2px solid #000000`, `object-fit:cover`. Coloana dreaptă: nume `{{ORDER_PRODUCT_NAME}}` (Akrobat 26), rândul pe categorie (Arial 15, implicit rândul generic; variantele sunt în comentariu), buton mic „Cum se prepară” spre `{{ORDER_PRODUCT_URL}}`. 14px între carduri.
- Pe mobil cardul rămâne pe două coloane (cerc 84px + text); așa arată și în ref3.
- **1 produs:** un singur card, secțiunea e scurtă și echilibrată (H2 + un card). **2-3 produse:** carduri unul sub altul, aceeași înălțime (numele pe 1-2 rânduri). **4 produse:** maximum; peste 4 se afișează primele 4, fără „și încă X”.
- **Starea fără date (fallback):** cardurile dispar; rămâne antetul, iar sub el un singur card alb centrat cu textul de rezervă din copy.md și butonul „Vezi toate mixurile” (220 x 44). În `index.html` blocul e prezent, marcat `ORDER PRODUCTS FALLBACK START/END` și ascuns (`display:none` + `mso-hide:all`), ca preview-ul să arate starea cu produse. La build în theMarketer se leagă de condiția inversă buclei de produse.
- **Placeholderele sunt generice** (`{{ORDER_PRODUCT_NAME}}`, `{{ORDER_PRODUCT_IMAGE}}`, `{{ORDER_PRODUCT_URL}}`), cum cere copy.md: sintaxa theMarketer pentru produsele din comanda declanșatoare nu e verificată (copy.md, întrebarea 1). Marcajele `ORDER PRODUCTS START/END` și `ORDER_PRODUCT_CARD` arată exact ce se repetă.
- Cerința pentru feed: imagine pătrată, minimum 224 x 224, subiectul centrat (cercul taie colțurile).

### S3 Lista de cumpărături (alb)
- H2 pe 2 rânduri + text de intro.
- **Card listă:** `border:2px solid #000000`, `border-radius:20px`, padding 28px. 5 rânduri, fiecare cu o căsuță de bifat (td 16 x 16, contur negru 2px, colțuri 4px; HTML, nu imagine) + numele produsului bold + textul. Linie neagră de 1px între rânduri. Fiecare rând e marcat `S3-ROW: <categorie>` pentru conținut condiționat [neverificat].
- Sub card: „Cantitățile exacte sunt și pe ambalaj.” Arial 13.
- Fără fotografii (copy.md). Căsuța de bifat e singurul element grafic: transformă blocul într-o listă de cumpărături reală, nu într-un paragraf.

### S4 Rețete (negru)
- Supratitlu + H2 + text, toate portocalii, centrate.
- **Banda „Rețeta săptămânii”:** td portocaliu de 300px lipit de marginea stângă a emailului (padding stânga 40px), Akrobat 24 negru. Echivalentul benzilor din ref3.
- **`rotw.jpg`** 1200 x 800 (afișat 600 x 400): teancul (IMG2, lateral) pe negru, peste un disc turcoaz (350px afișat), ușor deplasat spre dreapta. Link spre rețetă.
- Titlul rețetei (Akrobat 36, portocaliu, aliniat stânga), descrierea, rândul info „3 porții · 12 pancakes · 20 min · Ușor” (Arial 15 bold).
- **Cardul alb de rețetă** (`border-radius:20px`, padding 28px): „Ingrediente” pe două coloane (4 + 4, se stivuiesc pe mobil, `.stack`), linie neagră de 2px, „Cum le faci” cu cele 3 grupe (Pancakes / Nuci caramelizate / Servire) și pașii 1-10 numerotați în cercuri portocalii de 28px cu cifră neagră (td cu `bgcolor`, nu imagine), apoi caseta „Sfat” pe roz (`border-radius:14px`). Tot textul e HTML live.
- Buton mare portocaliu cu text negru „Vezi rețeta animată”.
- **3 carduri zig-zag** (ref3): rând de 600px, celula imagine 280 x 260 + celula text 320px. Cardurile 1 și 3: farfuria iese din cadru pe stânga, banda pleacă spre marginea dreaptă; cardul 2 invers. Banda: roz (afine), turcoaz (teanc), portocaliu (clătite), Akrobat 26 negru, uppercase. Sub bandă: rândul info portocaliu Arial 15 bold și buton mic portocaliu „Vezi rețeta”. Pe mobil rămâne pe două coloane (44% / 56%), banda scade la 20px.
- Sub carduri: buton contur portocaliu „Toate rețetele”.
- Variantele pe categorie (img6-img9) folosesc același modul; se schimbă doar fișierul `assets/cardX-*.jpg`, banda și textele.

### S5 Trimite-ne rețeta ta (roz)
H2 pe 2 rânduri, textul de invitație cu @lucas_bites și #lucasbites în bold, nota despre acord (Arial 13), buton mare negru „Trimite-ne rețeta” (`mailto:`, fără UTM), link subliniat spre Instagram (UTM `s5-instagram`), rândul cu hashtag și TikTok. Fără fotografii: nu generăm nimic ce ar putea trece drept poză de client.

### S6 Ce urmează (turcoaz)
H2, textul cu emailul și telefonul ca linkuri subliniate (`mailto:`, `tel:`), lista de magazine, link subliniat „Vezi toată gama”, semnătura „eat what you love” (Akrobat Bold 32) și „Familia Lucas Bites”. Aici nu e niciun buton: e o secțiune de încheiere, iar copy.md vrea cross-sell discret.

### S7 Footer (alb)
Identic cu W1-W3 (linie neagră, logo stripes 260px, iconițe 32px, adresă, contact, dezabonare, copyright), copiat din `welcome-03/index.html`. **Fraza de consimțământ lipsește** (decizie 12.10.2026): o adaugă utilizatorul separat, în theMarketer; în cod e marcată cu `[ADAUGĂ UTILIZATORUL]`.

---

## 4. Imagini

| Fișier sursă (Higgsfield) | Asset generat de `build.py` | Afișat | Notă |
|---|---|---|---|
| img1-hero | `hero-top.jpg`, `hero-bottom.jpg` | 600 x 220, 600 x 300 | farfuriile se separează automat (regiuni opace distincte); A = cea mai din stânga, B = de sus din rest, C = de jos |
| img2-banane-nuci | `rotw.jpg` | 600 x 400 | pe negru, disc turcoaz |
| img3-afine | `card1-afine.jpg` | 280 x 260 | iese din cadru pe stânga |
| img4-teanc | `card2-teanc.jpg` | 280 x 260 | iese din cadru pe dreapta |
| img5-clatite | `card3-clatite.jpg` | 280 x 260 | iese din cadru pe stânga |
| (feed theMarketer) | `{{ORDER_PRODUCT_IMAGE}}` | 112 x 112 | nu se generează |

Prompturile și checklist-ul: `image-prompts.md`. Recuzita comună e o farfurie bej mată, diferită de farfuria neagră din W3 și de farfuriile albe din W1.

**Fără poze:** `build.py` face placeholdere la dimensiunea finală (farfurii stilizate cu eticheta IMG1 A/B/C, IMG2...IMG5), deci `index.html` nu se schimbă când sosesc pozele: se pun în `images/` și se rulează din nou scriptul. Dacă cele 3 farfurii din img1 se ating și nu pot fi separate, scriptul afișează un avertisment și pune toată poza în banda de jos.

**Asset-uri desenate de `build.py` (nu Higgsfield):** cele 5 curbe, benzile hero, compozițiile, logo-urile (aceleași fișiere și același tratament ca W1-W3), iconițele sociale (același cod ca W3), webfontul Akrobat copiat din W3.

---

## 5. Siguranță în email

**Outlook (Windows, motorul Word)**
- Butoane VML `v:roundrect` cu fallback `<a>`, ca în W3; butonul contur folosește `strokecolor`.
- `border-radius` e ignorat: cardurile, cercurile cu pași și imaginea produsului din feed devin dreptunghiuri sau pătrate (cu contur negru). Acceptabil; farfuriile și curbele sunt arse în imagini, deci identitatea rămâne.
- `object-fit` nu e suportat în Outlook, Gmail web parțial: de aici cerința ca imaginea din feed să fie pătrată.
- Containerul are tabel fantomă MSO de 600px; toate imaginile au `width`/`height` ca atribute; `mso-line-height-rule:exactly` pe titluri.
- Akrobat nu se încarcă în Outlook: fallback „Arial Narrow”, apoi Arial. Titlul cel mai lung („Pankees cu banane și nuci caramelizate”) încape pe 2 rânduri la 600px în Akrobat (verificat în preview); în fallback e mai lat, deci poate trece pe 3 rânduri, fără să rupă layout-ul.

**Dark mode**
- `color-scheme: light`, `supported-color-schemes: light` și regulile Outlook.com `[data-ogsc] .tb / .to` din W3, ca să rămână perechile negru pe culoare și portocaliu pe negru.
- Fundalurile de secțiune sunt pe `bgcolor`; hero-ul, curbele, rețeta săptămânii și farfuriile din zig-zag sunt JPG/PNG opace cu culorile arse, deci nu se inversează.
- S4 e deja negru: în Gmail iOS/Android (inversare totală) se schimbă cel mai puțin. Cardul alb de rețetă poate deveni închis la culoare, cu text deschis; cercurile portocalii cu pași rămân lizibile.

**Imagini oprite**
- Tot ce contează e text live: titlurile, numele produselor comandate, lista de cumpărături, ingredientele, pașii, numele rețetelor (în benzi) și toate butoanele.
- Alt text din copy.md, secțiunea 6, pe fiecare imagine cu conținut; `alt=""` pe benzile decorative și pe curbe.

**Mărime**
- HTML: **~61 KB** (limita Gmail: 102 KB). Rezervă suficientă pentru sintaxa reală theMarketer a buclei de produse și pentru URL-urile absolute ale imaginilor la upload.
- Imagini: compozițiile se salvează cu limită de greutate în `build.py` (benzi hero max 200 KB fiecare, rețeta săptămânii max 260 KB, carduri max 120 KB). Cu placeholdere, tot `assets/` (fără fonturi) are ~330 KB; cu poze reale, estimat sub 1,2 MB (ținta din copy.md).

**La upload în theMarketer**
- `assets/` se urcă în biblioteca de imagini, iar căile relative se înlocuiesc cu URL-uri absolute HTTPS (inclusiv `assets/fonts/`).
- Placeholderele generice (`{{FIRST_NAME}}`, `{{ORDER_PRODUCT_*}}`, `{{UNSUBSCRIBE_URL}}`, `{{SHOP_URL}}`, `{{URL_RETETA_*}}`) se înlocuiesc cu tag-urile reale din editorul theMarketer, după ce sunt verificate (copy.md, secțiunea 9).
- Testul de lansare (copy.md, condiția 2): o comandă reală cu 1, 2 și 4 produse și o comandă fără date în feed, ca să se vadă și starea fallback.
