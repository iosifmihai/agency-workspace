# New Customer Email 2: direcția de design (rețete noi + produsul fiecărei rețete)

Autor: UI Designer, 12.10.2026. Bază: `brief.md` (decizii finale, au prioritate), `copy.md` (copy final, folosit cuvânt cu cuvânt), `discovery.md` 5-8, `refs/ref4.png` (BetterBrand), `refs/ref3.png` (Blue Apron), `packshots/` (fotografiile reale de ambalaj), `new-customer-01/` (NC1) și previzualizările W1-W3.
Documentul e o recomandare închisă, nu o listă de variante.

Ideea vizuală: **„blocuri de poftă”**. Emailul e o succesiune de blocuri pline de culoare tăiate în diagonală, ca în ref4. Fiecare rețetă are blocul ei de culoare, titlul uriaș și, dedesubt, o singură compoziție: mâncarea decupată care iese din marginea emailului, lângă ambalajul real, pus pe o plăcuță albă cu contur negru (ca un sticker). Perechea rețetă + produs se citește dintr-o privire, fără carduri și fără grilă.

---

## 1. Ce preluăm din ref4 și ref3 și de ce

Roșul din ref4 devine **portocaliu** (hero și banda finală) și **roz** (perechea 1); negrul din ref4 rămâne negru. Fontul cu serife italic din ref4 („Meet The Better Bagel”, „With Bacon PB&J”) devine Akrobat Bold, fără italic.

| Pattern | Sursă | Unde în NC2 | De ce |
|---|---|---|---|
| Bloc de culoare plin, titlu foarte mare, scurt, buton pastilă, fără fotografie deasupra textului | ref4 col. 1 („Pumpkin Spice”) | S1 hero, portocaliu, H1 92px | Hero-ul NC1 avea farfurii la colțuri; aici titlul e imaginea. Textul e **aliniat la stânga** (NC1 și W1-W3 au hero centrat), ca în ref4 col. 3 („The Cinnamon Has Landed”). |
| Tăietură diagonală între două blocuri, cu mâncare care trece peste ea | ref4 col. 1 (sandvișul peste tăietura roșu/negru), col. 3 | S1 -> S2: `hero-cut.jpg`, ingredientele din IMG0 (ciocolată, pepperoni, înghețată) „zboară” peste diagonala portocaliu -> negru | Anunță cele 3 rețete înainte să înceapă; e momentul „food bursting” din ref4, fără farfurie. |
| Tăieturi diagonale între toate blocurile, cu direcția alternată | ref4 col. 1 și 3 | toate tranzițiile (7 benzi `cut-*.png`, 600 x 48) | Înlocuiesc curbele mari din NC1 și valurile mici din W1-W3. Alternarea pantei dă un ritm de zig-zag pe toată lungimea emailului. |
| „The Classic / With Bacon PB&J”: titlu mare centrat + subtitlu „With ...” | ref4 col. 2 | fiecare pereche: titlul rețetei (H3, 58px) + „Cu {produs}” (Akrobat Bold 26) | Exact structura cerută de client: rețeta și produsul ei, în același bloc. |
| Celule de tabel cu text scurt (tabelul „Ingredients”) | ref4 col. 1 | rândul de info al fiecărei perechi: 2 celule, moment + timp | Nu avem ingrediente (copy.md), dar celulele dau aceeași senzație de „fișă de rețetă”. Pe culoare: celule negre cu text portocaliu; pe negru: celule cu contur portocaliu și text portocaliu (ref4 are celule gri, pe care nu le avem). |
| Packshot mare, cu mâncarea lângă el, pe o tăietură diagonală de culoare | ref4 col. 3 (punga cu bagel + scorțișoară, peste diagonala negru/bej) | compoziția fiecărei perechi: plăcuța cu ambalajul pe o parte, mâncarea decupată pe cealaltă, peste o bandă diagonală de altă culoare de brand | Produsul real e mare (260 x 340 pe desktop) și stă lângă rezultat. Mâncarea acoperă puțin marginea albă a plăcuței, niciodată ambalajul. |
| Mâncare care iese din cadru | ref4 col. 1 și 3 | perechea 1 și 3: farfuria iese prin marginea stângă; perechea 2: mâna cu felia intră din marginea dreaptă | Cadrul emailului devine mai mic decât masa. Diferit de NC1, unde farfuriile erau văzute de sus și tăiate la colțuri. |
| Bloc text centrat, scurt, cu un buton | ref3 („Fresh Ingredients, Quality Guarantee”) | S3 „Cum au ieșit?” | Bloc liniștit după perechi, pe alb, ca pauză între blocurile tari. |
| Bandă îngustă de culoare | ref3 („Eat. Recycle. Repeat.”) | S4, banda portocalie cu transportul și semnătura | Un rând de motiv + semnătura, nu o secțiune întreagă. |

**Ce NU preluăm și de ce**

| Nu preluăm | Motiv |
|---|---|
| Text alb pe roșu (ref4 col. 1) și titluri roșii pe negru | Regula de brand: pe culoare doar negru; pe negru doar portocaliu. |
| Fotografie lifestyle pe toată lățimea, cu mâini și blat (ref4 col. 2, sus) | Avem doar decupaje pe alb (brief); o scenă întreagă ar cere fundal generat, care se lovește de culorile de brand. |
| Serif italic („Meet The Better Bagel”) | Plicata nu se folosește; în email avem doar Akrobat și Arial. |
| Bloc „Directions” cu pași | Site-ul nu publică pași pentru cele 3 rețete (copy.md); nu inventăm. |
| Fotografie de cutie de livrare (ref3) și orice ambalaj generat | Ambalajele vin doar din `packshots/` (brief, decizia 1). |
| Recenzii cu stele (ref3) | Excluse în copy.md (clientul a cumpărat deja; cifra 1.100 / 4,9 a fost în welcome). |
| Grila 2 x 2 de carduri (ref3) | Folosită în W3 S2. |
| **Din NC1:** hero roz cu farfurii la colțuri, curbe mari (jumătate de sinus), carduri albe cu imagine rotundă, zig-zag farfurie + bandă colorată, rețeta pe disc turcoaz, listă cu bife, card alb cu pași numerotați | Brief: de evitat. NC2 nu are niciun card alb și nicio imagine rotundă; plăcuța albă e dreptunghi rotunjit, cu contur, iar mâncarea iese prin marginea emailului, nu stă într-o bandă. |
| **Din W1-W3:** valuri scurte, 3 cercuri pe rând, pași 1-2-3 pe turcoaz, poze pe toată lățimea (W1); lava cake rupt pe negru, zig-zag cu săgeți (W2); 4 farfurii negre 2 x 2, recenzii în trepte, grid UGC punctat (W3) | Deja folosite. Lava cake e aici întreg, cu înghețată, pe turcoaz (nu rupt, pe negru, ca în W2). |

---

## 2. Ordinea secțiunilor și culorile

| # | Secțiune | Fundal | Tranziție spre următoarea |
|---|---|---|---|
| S0 | Header: logo (identic NC1, W1-W3) | alb | `cut-white-orange.png` (urcă spre dreapta) |
| S1 | Hero: supratitlu, H1, salut, CTA, apoi IMG0 pe tăietură | **portocaliu #FAA61A** | `hero-cut.jpg` (diagonala coboară spre dreapta, ingredientele trec peste ea) |
| S2a | Antet rețete: H2 + un rând | negru | `cut-black-pink.png` |
| S2-1 | Perechea 1: Pankees cu ciocolată + Chocolate Chips Pankees | roz #F7ACB4 (bandă portocalie în compoziție) | `cut-pink-black.png` |
| S2-2 | Perechea 2: Pizza de casă cu pepperoni + Pizza Crust Mix | negru (bandă turcoaz în compoziție) | `cut-black-turq.png` |
| S2-3 | Perechea 3: Lava cake cu înghețată de vanilie + Lava Cake Mix, apoi „Toate rețetele” | turcoaz #86D2DA (bandă roz în compoziție) | `cut-turq-white.png` |
| S3 | Cum au ieșit? | alb | `cut-white-orange2.png` |
| S4 | Transport gratuit + „Vezi toate produsele” + semnătura | portocaliu | `cut-orange-white.png` |
| S7 | Footer (identic, fără fraza de consimțământ) | alb | - |

Secvența: **alb, portocaliu, negru, roz, negru, turcoaz, alb, portocaliu, alb**.
NC1: alb, roz, portocaliu, alb, negru, roz, turcoaz, alb. W1: alb, portocaliu, alb, turcoaz, roz, negru, alb. W2: alb, negru, alb, roz, turcoaz, portocaliu, alb. W3: alb, turcoaz, alb, negru, portocaliu, roz, alb.

**Hero:** W1 portocaliu, W2 negru, W3 turcoaz, NC1 roz, **NC2 portocaliu**. Toate 4 culorile au fost deja hero; alegem portocaliul pentru că e cel mai apropiat de roșul din ref4 și cel mai departe în timp (W1), iar emailul imediat anterior (NC1) a fost roz. Hero-ul W1 era un stack decupat pe portocaliu, centrat; aici e doar tipografie, aliniată la stânga, cu ingredientele jos, pe tăietură.
**Secțiunea colorată dinaintea footer-ului:** W1 negru, W2 portocaliu, W3 roz, NC1 turcoaz, **NC2 portocaliu**. E intenționat: portocaliul închide ce a deschis hero-ul (început și sfârșit în aceeași culoare), iar banda e îngustă, nu o secțiune întreagă ca în W2.
**Negrul apare de două ori** (S2a și perechea 2), despărțit de roz. Ref4 alternează roșu și negru exact așa; perechea 2 (pizza, roșu-auriu) e cea care se vede cel mai bine pe negru, iar lava cake (maro închis) ar dispărea pe negru, de aceea stă pe turcoaz.

**Reguli de culoare aplicate:** pe portocaliu, roz, turcoaz și alb tot textul e negru. Pe negru (S2a, perechea 2) textul e doar portocaliu: titluri, eticheta, rândul „Cu ...”, celulele, textul și linkul subliniat. Butoane: pastilă neagră cu text portocaliu pe fundaluri deschise; pe negru, pastilă portocalie cu text negru. „Toate rețetele” e pastilă cu contur negru, text negru, pe turcoaz. Niciun text alb, niciun portocaliu pe alb.

---

## 3. Specificații de layout (600px, tabele, mobile-first)

### Sistem comun
- Container 600px, `bgcolor` pe fiecare `td` de secțiune. Padding lateral 40px desktop, 20px mobil (`.px`).
- Tipografie: titluri `Akrobat, "Arial Narrow", Arial, sans-serif` (webfont copiat din `new-customer-01/assets/fonts/`), text `Arial, Helvetica, sans-serif`.
  - H1: Akrobat Black 92/82, uppercase, aliniat la stânga (mobil 60/54).
  - H2 și titlul rețetei (H3): Akrobat Black 58/54 și 58/52, uppercase, centrat (mobil 40/38).
  - Eticheta (momentul) și supratitlul: Akrobat Bold 22, uppercase, letter-spacing 2px.
  - Rândul „Cu {produs}”: Akrobat Bold 26/30, fără majuscule (ca „With Bacon PB&J”).
  - Celulele de info: Akrobat Bold 22, uppercase, padding 9 x 20, colțuri 12px, 8px între ele (mobil 18px).
  - Text: Arial 16/24 (hero 17/26). Text mic: Arial 14/21. Footer: Arial 13/20.
- **Buton mare:** 260 x 56 (hero, recenzie), **buton de rețetă:** 240 x 52, Arial 18 bold, pastilă; pe mobil 100% (max 335). **Buton contur:** 240 x 48, `border:2px solid #000000`. Toate bulletproof (VML `roundrect` + `<a>`).
- **Tăieturi:** PNG 1200 x 96, afișate 600 x 48, linie dreaptă de la 8px la 88px (la 2x), pantă alternată. Celula are `bgcolor` = culoarea de jos.

### S0 Header (alb)
Logo centrat, 180px (export 360px), link spre lucasbites.ro. Identic cu NC1, padding jos 12px, apoi tăietura alb -> portocaliu.

### S1 Hero (portocaliu)
- Text HTML live, aliniat la stânga: supratitlu „idei pentru orice poftă”, H1 pe 2 rânduri („AI POFTĂ / DE ALTCEVA?”), salutul cu `{{FIRST_NAME}}` (lățime maximă 470px, ca să nu fie un rând lung; rezerva fără prenume e în comentariu), butonul „Vezi rețetele”.
- **`hero-cut.jpg`** 1200 x 440 (afișat 600 x 220): diagonala portocaliu -> negru, iar peste ea până la 10 bucăți decupate din IMG0 (cupa de înghețată cea mai mare, în mijloc; bucăți de ciocolată și pepperoni rotite, două ies din cadru stânga-dreapta). Decorativă, `alt=""` (copy.md, secțiunea 6).
- Ordinea pe mobil cerută de copy.md (supratitlu, H1, text, buton, IMG0) e respectată exact. Butonul e deasupra liniei de scroll pe un ecran de 667px.

### S2a Antet rețete (negru)
H2 „ÎNCEARCĂ ȘI ASTA.” și rândul de sub el, portocalii, centrate. E o bandă scurtă: separă hero-ul de perechi și continuă negrul de sub ingrediente.

### S2 Modulul de pereche (de 3 ori, același cod)
De sus în jos, exact ordinea din copy.md:
1. Tăietura din culoarea anterioară.
2. Eticheta (momentul), H3 titlul rețetei, „Cu {produs}”, cele 2 celule de info. Centrat, text live.
3. **Compoziția** `pairN-*.jpg`, 1200 x 880, afișată 600 x 440, pe toată lățimea, cu link spre rețetă:
   - fundal = culoarea blocului; peste el o **bandă diagonală** de altă culoare de brand (perechea 1 portocaliu, 2 turcoaz, 3 roz), paralelă cu ritmul tăieturilor;
   - **plăcuța cu packshot-ul** (520 x 680 la 2x, afișată 260 x 340): dreptunghi alb rotunjit (60px la 2x), contur negru 5px la 2x; perechile 1 și 3 în dreapta, perechea 2 în stânga;
   - **mâncarea decupată** pe partea opusă, cât mai mare: farfuria iese 70px (la 2x) prin marginea stângă (perechile 1 și 3), mâna cu felia intră prin marginea dreaptă (perechea 2). Mâncarea are voie să acopere marginea albă a plăcuței, dar `build.py` oprește decupajul la 14px (la 2x) înainte de ambalaj, deci produsul rămâne mereu întreg.
4. Rândul despre produs, butonul „Vezi rețeta”, linkul subliniat „Vezi {produs}”. Padding jos 44px.

Perechea 3 se continuă cu butonul contur „Toate rețetele”, pe turcoaz.

**Pe mobil (375px):** compoziția se scalează la 375 x 275; plăcuța rămâne ~162px lățime, ambalajul se citește (nume și culoare). Titlurile trec la 40px; „LAVA CAKE CU ÎNGHEȚATĂ DE VANILIE” ocupă 3 rânduri, restul 2.

**Rezerve și rotație sezonieră** (copy.md, S2): același modul; se schimbă textele, URL-urile, culoarea blocului (dacă perechea se mută) și compoziția. `build.py` are lista `PAIRS`: o pereche nouă e un rând nou acolo (fotografie Higgsfield + packshot din `packshots/`).

### S3 Cum au ieșit? (alb)
H2 centrat, textul, butonul „Lasă o recenzie” (pastilă neagră, text portocaliu), textul mic despre reply. Fără imagine (copy.md). Albul vine după trei blocuri pline: e pauza vizuală care face întrebarea să se vadă, iar butonul e singurul element negru plin din secțiune.

### S4 Al doilea produs (bandă portocalie)
Rândul cu transportul (Arial 17 bold), linkul subliniat „Vezi toate produsele”, semnătura „eat what you love” (Akrobat Bold 40) și „Familia Lucas Bites”. Fără buton: un singur motiv, discret. Paragraful cu transportul e marcat în cod `[de confirmat la lansare]`; dacă nu se confirmă, se șterge doar el.

### S7 Footer (alb)
Identic cu NC1 (linie neagră, logo stripes 260px, iconițe 32px, adresă, contact, dezabonare, copyright). **Fraza de consimțământ lipsește** (brief, decizia 5); în cod e comentariul marker `[ADAUGĂ UTILIZATORUL]`, pe aceeași poziție ca în NC1.

---

## 4. Packshot-urile: de ce pe plăcuță albă, nu decupate

Am testat decupajul local pe toate cele 10 packshot-uri (fundal alb 253-255, flood fill de la margine cu prag de alb strict). Rezultatul **nu e acceptabil pentru ambalaj**: sticlele albe translucide au marginea stângă zimțată (corpul sticlei are 235-250, aproape cât fundalul), la baza sticlelor rămân fâșii albe din reflexie, iar pungile Lava Cake și Brownie au marginile argintii mâncate pe alocuri. Un ambalaj cu marginea ciupită arată ca un produs deteriorat; brief-ul cere ca ambalajele să nu fie modificate, iar copy.md cere explicit „nu se decupează, se așază pe o zonă albă”.

**Soluția din `build.py`:**
- fotografia rămâne **întreagă și nemodificată** (fără recolorare, fără umbre, fără retuș); doar se redimensionează;
- se scalează ca să **acopere** plăcuța, iar marginea plăcuței taie doar fundal alb, deci nu există nicio cusătură între poză și plăcuță;
- produsul se centrează pe orizontală în plăcuță (packshot-ul Chocolate Chips are sticla mutată spre stânga în original);
- scriptul calculează conturul produsului și verifică să rămână la cel puțin 14px (la 2x) de marginea plăcuței și de colțurile rotunjite; dacă nu, micșorează poza (punga Lava Cake: 0,70 în loc de 0,76) și umple restul cu albul median al fotografiei (diferență de 1-2 niveluri, invizibilă). Verificat vizual la 2x: fără cusătură;
- conturul negru al plăcuței leagă ambalajul de stilul logo-ului (contur negru gros) și o desprinde de fundal ca un sticker.

---

## 5. Imagini

| Fișier sursă | Ce e | Unghi / tip decupaj | Asset generat | Afișat |
|---|---|---|---|---|
| `images/img0-hero-ingrediente.png` (Higgsfield) | bucăți de ciocolată, pepperoni, o cupă de înghețată, separate | bucăți libere, fără farfurie (niciun set) | `hero-cut.jpg` | 600 x 220 |
| `images/img1-ciocolata.png` (Higgsfield) | teanc scurt de 3 Pankees cu ciocolată | lateral, la nivelul ochilor: `SIDE_PLATES` | `pair1-ciocolata.jpg` | 600 x 440 |
| `images/img2-pizza-felie.png` (Higgsfield) | felie de pizza cu pepperoni ridicată de o mână | lateral 30°, fără farfurie, mâna din dreapta (niciun set) | `pair2-pizza.jpg` | 600 x 440 |
| `images/img3-lava-vanilie.png` (Higgsfield) | lava cake întreg cu înghețată de vanilie | lateral 20°: `SIDE_PLATES` | `pair3-lava.jpg` | 600 x 440 |
| `packshots/pr-choco.jpg`, `pr-pizza.jpg`, `pr-lava.jpg` | ambalajele reale | nedecupate, pe plăcuță albă | în compozițiile de mai sus | 260 x 340 |

`ROUND_PLATES` e gol: nicio farfurie nu e fotografiată de sus în acest email. Pizza nu e în `SIDE_PLATES` pentru că umplerea cu înfășurătoarea convexă ar umple cu alb golul dintre mână și pizza.

**Fără poze:** `build.py` face placeholdere la dimensiunea finală (forme în culorile de brand, cu eticheta IMG0...IMG3), deci `index.html` nu se schimbă când sosesc pozele. Când utilizatorul pune fotografiile în `images/`, Claude rulează build-ul, verifică decupajele și reface previzualizările.

**Asset-uri desenate de `build.py`:** cele 7 tăieturi, plăcuțele cu packshot, compozițiile, logo-urile (aceleași fișiere și același tratament ca NC1), iconițele sociale (același cod ca NC1), webfontul Akrobat copiat din NC1.

---

## 6. Siguranță în email

**Outlook (Windows, motorul Word)**
- Butoane VML `v:roundrect` cu fallback `<a>`; butonul contur folosește `strokecolor`.
- `border-radius` e ignorat: celulele de info devin dreptunghiuri negre (rămân lizibile). Plăcuțele, tăieturile și benzile diagonale sunt arse în imagini, deci identitatea rămâne.
- Container cu tabel fantomă MSO de 600px; toate imaginile au `width`/`height` ca atribute; `mso-line-height-rule:exactly` pe titluri.
- Akrobat nu se încarcă în Outlook: fallback „Arial Narrow”, apoi Arial. H1 92px pe 2 rânduri („AI POFTĂ / DE ALTCEVA?”) în Akrobat (verificat în preview); în fallback literele sunt mai late, deci „DE ALTCEVA?” poate trece pe încă un rând, fără să rupă layout-ul.

**Dark mode**
- `color-scheme: light`, `supported-color-schemes: light` și regulile Outlook.com `[data-ogsc] .tb / .to`, ca să rămână perechile negru pe culoare și portocaliu pe negru.
- Fundalurile de secțiune sunt pe `bgcolor`; tăieturile și compozițiile sunt PNG/JPG opace cu culorile arse, deci nu se inversează și nu apar dungi între secțiuni.
- În Gmail iOS/Android (inversare totală), blocurile negre se schimbă cel mai puțin; plăcuțele albe din compoziții rămân albe (sunt în imagine), deci ambalajele se văd corect.

**Imagini oprite**
- Tot ce contează e text live: titlurile rețetelor, „Cu {produs}”, celulele, rândurile despre produs, toate butoanele și linkurile.
- Alt text pe compoziții: textele din copy.md, secțiunea 6, unite pentru rețetă și packshot (o singură imagine), de exemplu „Pankees cu ciocolată și sticla Chocolate Chips Pankees”. `alt=""` pe tăieturi și pe `hero-cut.jpg`.

**Mărime**
- HTML: **~32 KB** (limita Gmail: 102 KB). Rezervă mare pentru sintaxa reală theMarketer și pentru URL-urile absolute ale imaginilor.
- Imagini: compozițiile au limită de 190 KB fiecare, `hero-cut.jpg` 170 KB (copy.md: fiecare imagine sub 200 KB). Cu placeholdere, `assets/` fără fonturi are ~510 KB; cu fotografiile reale, estimat ~650 KB (ținta din copy.md: sub 1,2 MB).

**La upload în theMarketer**
- `assets/` se urcă în biblioteca de imagini, iar căile relative se înlocuiesc cu URL-uri absolute HTTPS (inclusiv `assets/fonts/`).
- Placeholderele generice (`{{FIRST_NAME}}`, `{{SHOP_URL}}`, `{{URL_RETETA_*}}`, `{{URL_PRODUS_*}}`, `{{REVIEW_URL}}`, `{{UNSUBSCRIBE_URL}}`) se înlocuiesc cu tag-urile și URL-urile reale (copy.md, secțiunile 1 și 8). UTM-ul e deja pus după `?`; dacă un URL real are deja `?`, UTM-ul se leagă cu `&`.
- Compoziția fiecărei perechi are linkul rețetei; dacă paginile de rețetă nu sunt gata (copy.md, condiția de lansare 1), linkul imaginii și butonul trec pe pagina de rețete, iar produsul rămâne linkul text.

---

## 7. Abateri de la copy.md (de știut)

1. **IMG1, ciocolata „căzută lângă farfurie”:** o cerem doar **pe farfurie**. Bucățile de pe fundal, pe aceleași rânduri cu farfuria, ar fi înghițite de umplerea `SIDE_PLATES` și ar lăsa pete albe în decupaj. Detaliile din copy.md (teanc de 3, bucăți vizibile în aluat, fir de sos) rămân.
2. **IMG2, direcția mâinii:** copy.md nu o fixează; o cerem **din marginea dreaptă**, ca încheietura să iasă prin marginea emailului (altfel ar apărea tăiată în mijlocul blocului negru). Pizza fără farfurie și fără blat, direct pe alb.
3. **IMG0 e folosit** (copy.md îl lasă opțional): e singura imagine din hero, pe tăietură.
4. **Alt text:** compoziția unește rețeta și packshot-ul într-o singură imagine, deci alt text-urile din copy.md pentru IMG și packshot sunt unite într-o frază.
5. **Logo footer:** copy.md spune 200px; păstrăm 260px, ca în NC1 (copy.md cere și „identic cu Email 1”).
