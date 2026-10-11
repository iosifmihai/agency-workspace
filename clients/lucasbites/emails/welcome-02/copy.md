# Lucas Bites: Welcome Email 2, strategie, structură și copy final

Surse: `brief.md` (acest folder), `discovery.md`, `welcome-01/copy.md`, `welcome-01/refs/ref1-4.png`, `refs/ref5-7.png`. Legendă: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [adaptat] = text aprobat ajustat pentru email, [nou] = text nou, de aprobat de client.

**Ce cere clientul:** povestea brandului, cele 4 categorii (Pancakes & Crêpes, Budinci, Prăjituri, Pizza) și USP-ul ingrediente. Acest Email 2 înlocuiește Email 2 planificat în `welcome-01/copy.md` secțiunea 5 (rețeta pas cu pas). Rețeta se mută în Email 3 (vezi secțiunea 5 de mai jos).

**Fără prețuri, fără cod de reducere.** „Făină nealbită” apare doar legat de pancakes și clătite. Povestea (S2) vine din pagina „Povestea noastră” a site-ului actual; nicio afirmație despre an sau loc, care nu apar acolo.

---

## Ce am preluat din referințe și de ce

| Pattern | Din | Unde în Email 2 | De ce |
|---|---|---|---|
| Titlu uriaș condensat pe fundal închis, mâncarea „intră” în tipografie | ref7 (Kings Row, „LEGEND”) | S1-hero | Akrobat condensat bold e făcut pentru asta. Hero-ul negru diferențiază imediat Email 2 de Email 1 (hero portocaliu). |
| Momentul de „dezvăluire” al produsului | ref5 (Beguile, clopotul ridicat) | S1-hero, IMG1 | Tradus în mâncare: lingura care rupe lava cake-ul și lasă ciocolata să curgă. Dramatism fără ambalaj. |
| Secțiune de poveste doar tipografică, text scurt centrat | ref2 (Mori Matcha, „The Story of”) | S2-poveste | Nu avem fapte de fondator, deci povestea stă pe convingere și pe ritm, nu pe fotografie. Un bloc fără imagine dă și pauză vizuală între hero și categorii. |
| Produs: imagine pe o parte, text pe cealaltă, alternat | ref5 (secțiunile „Layer Mystique with”) | S3-categorii | 4 categorii, fiecare cu CTA propriu, scanabil. Zig-zag-ul e alt layout decât cardurile circulare din Email 1 (Blue Apron). |
| Săgeți desenate și etichete scurte care leagă textul de mâncare | ref7 (Boustan, „a hearty shawarma”) | S3-categorii, eticheta de moment de lângă fiecare foto | Leagă fiecare categorie de un moment de consum de pe site. Jucăuș, potrivit tonului. |
| Grid de „note” cu ingrediente ca fotografii decupate | ref5 (Top notes) | S4-ingrediente, IMG6-7 | Face USP-ul vizibil, nu doar o listă. |
| Listă cu bife într-un card cu contur | ref6 (BetterBrand) | S4-ingrediente, cardul „Ce am pus noi” | Cel mai rapid format de citit pentru 3 afirmații verificate. |
| Două coloane față în față „OUR'S vs THEIR'S” | ref7 (Remedy) | S4-ingrediente, „Noi / Tu” | Adaptat: nu ne comparăm cu alții (fără concurenți identificați, fără afirmații nedovedite), ci împărțim munca: ce am pus noi în mix și ce adaugi tu. Plătește subiectul recomandat. |
| Valuri între secțiuni | ref4/ref6 (BetterBrand), deja în Email 1 | toate tranzițiile | Continuitate de serie: aceeași familie vizuală. |

Ce NU preluăm: cardurile de recenzii (ref5) și blocul social negru (deja în Email 1, S4 și S5), bulele cu cifre peste foto (ref6, ar cere text în imagine sau poziționare absolută, nesigură în email), fundalurile foto texturate (ref7 Kings Row, prea grele și în afara paletei).

---

## 1. Obiectiv, KPI, trimitere

**Obiectiv:** abonatul înțelege ce face Lucas Bites (aproape tot e deja în mix, ingrediente pe care le recunoști) și alege o categorie. Click-ul pe categorie ne spune ce poftă are, pentru Email 3 și newsletter.

**KPI principal:** rata de click unic pe oricare dintre cele 5 linkuri de produse (4 categorii + „Vezi mixurile”), raportată la emailurile livrate. Țintă 5%+, alertă sub 2%.

**KPI secundar:** rata de click unic pe linkul de ingrediente din S4. Țintă 1%+, alertă sub 0,3%. Plus distribuția click-urilor pe categorii (raport, nu țintă).

**Acțiune pe click (segmentare):** fiecare click pe o categorie setează un tag/atribut de interes: `INTEREST_PANCAKES`, `INTEREST_BUDINCI`, `INTEREST_PRAJITURI`, `INTEREST_PIZZA` (un contact poate avea mai multe). Fiecare link primește UTM: `utm_source=email&utm_medium=welcome&utm_campaign=welcome_02&utm_content=<id secțiune>-<categorie>`.

**Timing:** la 48 de ore după Email 1 (ziua 2), cu fereastră de livrare 09:00-11:00, ora României. Dacă cele 48 de ore cad în afara ferestrei, emailul așteaptă următoarea fereastră.

**Regula de intrare/ieșire:** Email 2 pleacă tuturor celor care au primit Email 1, **inclusiv celor care nu l-au deschis** (deschiderile sunt umflate de Apple MPP, nu le folosim ca filtru). Singura ramură e blocul ghid din S5, afișat doar celor fără click pe ghid în Email 1. Ies din serie la: dezabonare, hard bounce, plângere spam. Cumpărătorii rămân în Email 2 (povestea și ingredientele sunt utile și după comandă).

**Condiție de lansare:** emailul nu pornește până nu sunt live paginile `{{SHOP_URL}}/produse` cu ancorele pe categorii și pagina de ingrediente. Altfel KPI-ul principal trimite în 404.

Gărzi de siguranță (opresc trimiterea, nu sunt KPI): plângeri spam sub 0,10%, dezabonări sub 0,5%, hard bounce sub 1%. Rata de deschidere se citește doar orientativ.

---

## 2. Subiecte și preheadere

| # | Subiect | Caractere | Preheader |
|---|---|---|---|
| A **[recomandat]** | Ce pui tu și ce am pus noi [nou] | 26 | Ingrediente pe care le recunoști, puse deja la cântar. [din site] |
| B | Pancakes, budinci, prăjituri și pizza [adaptat] | 37 | Alege-ți pofta de azi. Aproape tot e deja în mix. [adaptat] |
| C | Aproape tot e deja în mix [adaptat] | 25 | Tu aduci pofta. Noi am pus restul la cântar. [nou] |

De ce A: e specific (promite exact împărțirea „noi / tu” din S4) și stârnește curiozitate fără clickbait, iar preheaderul aduce mesajul cheie 2 cuvânt cu cuvânt de pe site. B e varianta clară, de catalog: testați A contra B pe primele ~500 de trimiteri, câștigătorul se alege pe **click unic pe linkuri de produs**, nu pe deschideri.

**Expeditor:** Lucas Bites. **Reply-to:** aceeași adresă monitorizată ca la Email 1.

---

## 3. Structura, de sus în jos

Lățime 600px, o coloană pe mobil, zig-zag pe 2 coloane doar pe desktop. Titluri: `Akrobat, "Arial Narrow", Arial, sans-serif`, bold/black, majuscule. Text: `Arial, Helvetica, sans-serif`, 16px, paragrafe de 1-2 rânduri. Text negru #000000 pe orice culoare de brand și pe alb; pe negru, text doar portocaliu #FAA61A. Butoane pill, HTML „bulletproof”, nu imagini.

Ordinea culorilor (diferită de Email 1): alb, **negru**, alb, roz, turcoaz, portocaliu, alb. Tranziții cu valuri PNG de 600px, `alt=""`. Valurile, săgețile desenate, bifele și logo-ul sunt assets UI și nu intră în limita de 7 fotografii.

---

### S0-header

- **Scop:** recunoaștere imediată.
- **Fundal:** alb.
- **Conținut:** identic cu Email 1, S0-header (logo `Logo/Logo_LucasBites.png`, centrat, 180px, export 360px).
- **Imagine:** nu (doar logo).

---

### S1-hero

- **Scop:** plătește subiectul („ce pui tu, ce am pus noi”) și deschide povestea. Primul click spre produse vizibil fără scroll pe mobil.
- **Fundal:** negru #000000, tot textul portocaliu #FAA61A. Val spre alb la bază; IMG1 trece peste val (compus local, ca IMG1 din Email 1).
- **Copy:**
  - Supratitlu (Akrobat, mic, litere mici): **eat what you love** [din site, slogan oficial]
  - Titlu (Akrobat Black, foarte mare, 2 rânduri): **TU ADUCI POFTA.** [nou]
  - Subtitlu (Akrobat Bold, mediu): **Aproape tot restul e deja în mix.** [adaptat]
  - Text: Azi îți arătăm ce am pus în mixurile Lucas Bites, ce adaugi tu și ce poți face cu ele. [nou]
  - CTA (pill portocaliu, text negru): **Vezi mixurile** → `{{SHOP_URL}}/produse` [nou]
- **Ordinea pe mobil:** supratitlu, titlu, subtitlu, text, buton, apoi IMG1.
- **IMG1 (spec):**
  - Ce arată: un lava cake individual, cald, pe o farfurie mică de ceramică turcoaz. O linguriță tocmai l-a rupt pe o parte, iar ciocolata topită curge lucioasă pe farfurie. Puțin zahăr pudră pe vârf, 2-3 zmeure lângă. Fără mâini.
  - Încadrare: unghi de 30-40 de grade, ușor de jos, ca prăjitura să pară mare. Farfuria întreagă în cadru, cu spațiu liber în jur.
  - Decupaj: **da**, prăjitura împreună cu farfuria, **pe fundal alb simplu** (scoatem noi fundalul). Farfuria turcoaz separă ciocolata închisă de fundalul negru al secțiunii.
  - Raport: 4:5 (export 1200x1500px, afișat la 480px lățime, centrat).
  - Atmosferă: dramatic, „momentul dezvăluirii”, lumină caldă laterală care face ciocolata să lucească.

---

### S2-poveste

- **Scop:** povestea brandului, din pagina „Povestea noastră” a site-ului actual (lucasbites.ro/povestea-noastra/), scurtată pentru email.
- **Fundal:** alb. Fără fotografie (pauză tipografică între hero și categorii).
- **Copy:**
  - Supratitlu: **Povestea noastră, pe scurt** [nou]
  - Titlu (Akrobat Black, mare): **TOTUL A PORNIT DE LA LUCA.** [adaptat din site actual]
  - Text: Suntem o familie tânără, pasionată de bucătărie. Băiețelul nostru, Luca, era pur și simplu îndrăgostit de pancakes: le-ar fi mâncat dimineața, la prânz și seara, cu topping sau fără, numai pufoase să fie. [adaptat din site actual]
  - Text: Așa s-a născut Lucas Bites, după gustările preferate ale lui Luca. Iar Pankees, pentru că așa le alinta el. [adaptat din site actual]
  - Text: Ideea a fost simplă: pancakes pe care oricine le poate face acasă, doar adăugând apă. Am dus-o mai departe la clătite, prăjituri și pizza: aproape tot e deja în mix, tu adaugi ce scrie pe ambalaj. [adaptat]
  - Text: Pentru noi, cel mai frumos moment al zilei e cel în care ne strângem toți în jurul mesei. [adaptat din site actual]
  - Text: Și se pare că nu suntem singurii: peste 1.100 de recenzii, cu o medie de 4,9 din 5. [adaptat]
- **Notă:** cifra 1.100 / 4,9 e valabilă la 10.10.2026; se verifică la fiecare actualizare a fluxului. Fără CTA aici: secțiunea duce cu ochiul în categorii.
- **Imagine:** nu.

---

### S3-categorii

- **Scop:** cele 4 categorii, fiecare legată de un moment de consum de pe site, fiecare cu CTA propriu (KPI principal + tag de interes).
- **Fundal:** roz #F7ACB4, val de intrare din alb.
- **Copy antet:**
  - Titlu: **ALEGE-ȚI POFTA DE AZI.** [din site]
  - Text: 4 categorii, de la micul dejun la movie night. [nou]
- **Layout:** 4 rânduri zig-zag pe desktop (foto 280px pe o parte, text pe cealaltă; foto stânga la rândurile 1 și 3, dreapta la 2 și 4). Pe mobil: foto sus, text dedesubt, la fiecare rând. Eticheta de moment stă deasupra numelui categoriei, cu o săgeată desenată (PNG negru, 80px, `alt=""`) care arată spre fotografie; pe mobil săgeata se ascunde prin media query (unde clientul de email nu suportă, rămâne vizibilă și nu strică nimic). Etichetele sunt text HTML Akrobat; după cumpărarea licenței Plicata le putem trece pe Plicata, ca imagini.

**Rândul 1: Pancakes & Crêpes** (foto stânga)
  - Etichetă: **pentru duminica fără grabă** [adaptat]
  - Nume: **PANCAKES & CRÊPES** [din site]
  - Text: Pancakes pufoase cu sirop sau clătite subțiri, cât timp se face cafeaua. [din site]
  - Text mic: Classic, Buttermilk, Chocolate Chips, Blueberry și Vegan Classic Pankees (de post), plus Crêpes Traditional și Crêpes Mix Original. [adaptat]
  - Text mic: Classic Pankees: 4,9 din 5, din 148 de recenzii. [din site]
  - CTA (pill negru, text portocaliu): **Vezi pancakes & crêpes** → `{{SHOP_URL}}/produse#pancakes-crepes` [nou]
  - **IMG2 (spec):**
    - Ce arată: un teanc scurt de 3 pancakes cu o bucățică de unt și un fir de sirop, iar lângă el 2 clătite subțiri împăturite în sferturi, pe aceeași farfurie rotundă portocalie. Câteva afine.
    - Încadrare: unghi de 45 de grade, farfuria întreagă în cadru.
    - Decupaj: **da**, farfuria cu mâncarea, **pe fundal alb simplu**.
    - Raport: 1:1 (export 560x560px, afișat la 280px).
    - Atmosferă: dimineață liniștită de weekend, lumină caldă, sirop lucios. Diferit de Email 1: aici pancakes și clătite apar împreună.

**Rândul 2: Budinci** (foto dreapta)
  - Etichetă: **nou în gamă** [nou]
  - Nume: **BUDINCI** [din site]
  - Text: Mix de budincă, nou la Lucas Bites. Un desert de lingură, de pus în pahar și de împodobit cum îți place. [nou]
  - CTA (pill negru, text portocaliu): **Vezi budinca** → `{{SHOP_URL}}/produse#budinci` [nou]
  - **Notă:** nu scriem ce adaugi la budincă (lapte sau apă) și nici aroma până nu confirmă clientul (întrebarea 6).
  - **IMG3 (spec):**
    - Ce arată: o porție de budincă cremoasă într-o ceașcă mică de ceramică turcoaz, opacă, cu o lingură înfiptă și câteva fructe de pădure deasupra. Aroma implicită: vanilie; se schimbă după răspunsul clientului.
    - Încadrare: unghi de 30 de grade, ca să se vadă suprafața cremoasă și marginea ceștii.
    - Decupaj: **da**, ceașca cu lingura, **pe fundal alb simplu**. Nu folosiți pahar transparent: sticla nu se decupează curat.
    - Raport: 1:1 (export 560x560px, afișat la 280px).
    - Atmosferă: catifelat, proaspăt, „încă o lingură”.

**Rândul 3: Prăjituri** (foto stânga)
  - Etichetă: **pentru pauza de la birou** [adaptat]
  - Nume: **PRĂJITURI** [din site]
  - Text: Un brownie sau un banana bread făcut acasă, adus pentru colegi la cafeaua de la 11. [din site]
  - Text mic: Brownie și Lava Cake, plus noile Banana Bread și Carrot Cake. [adaptat]
  - CTA (pill negru, text portocaliu): **Vezi prăjiturile** → `{{SHOP_URL}}/produse#prajituri` [nou]
  - **IMG4 (spec):**
    - Ce arată: un banana bread copt, cu o jumătate de banană caramelizată pe vârf, din care sunt tăiate 2 felii groase sprijinite de chec, cu miezul umed vizibil.
    - Încadrare: unghi de 45 de grade, checul în diagonală.
    - Decupaj: **da**, doar checul și feliile (fără tocător), **pe fundal alb simplu**.
    - Raport: 1:1 (export 560x560px, afișat la 280px).
    - Atmosferă: de casă, cald, „am adus ceva pentru toată lumea”. Diferit de brownie-ul din Email 1.

**Rândul 4: Pizza** (foto dreapta)
  - Etichetă: **pentru movie night** [adaptat]
  - Nume: **PIZZA** [din site]
  - Text: Pizza de casă la începutul filmului, lava cake caldă la final. [din site]
  - Text mic: Pizza Crust Mix: adaugi apă și ulei, apoi pui ce topping vrei. [adaptat] 4,8 din 5, din 80 de recenzii. [din site]
  - CTA (pill negru, text portocaliu): **Vezi pizza** → `{{SHOP_URL}}/produse#pizza` [nou]
  - **IMG5 (spec):**
    - Ce arată: o pizza de casă rotundă, cu sos de roșii, mozzarella topită și frunze de busuioc, o felie ușor trasă în afară cu fire de brânză întinse. Margine aurie, ușor neregulată, „făcută acasă”.
    - Încadrare: de sus (overhead), pizza întreagă în cadru.
    - Decupaj: **da**, doar pizza (fără planșetă), **pe fundal alb simplu**.
    - Raport: 1:1 (export 560x560px, afișat la 280px).
    - Atmosferă: seară relaxată, poftă, brânză care se întinde.

- **Notă:** cifrele de recenzii (148 / 4,9 și 80 / 4,8) sunt valabile la 10.10.2026; se verifică înainte de fiecare actualizare a fluxului sau se scot, dacă site-ul nou le schimbă.

---

### S4-ingrediente

- **Scop:** USP ingrediente, în formatul „noi / tu” care plătește subiectul. KPI secundar (linkul de ingrediente).
- **Fundal:** turcoaz #86D2DA, val de intrare din roz. Cardurile au fundal alb și contur negru de 2px, colțuri rotunjite 16px.
- **Copy:**
  - Titlu: **CE AM PUS NOI. CE PUI TU.** [nou]
  - Text: Ingrediente pe care le recunoști, puse deja la cântar. [din site]
- **Grid de note (2 fotografii decupate una lângă alta, și pe mobil, câte 50%):**
  - Sub IMG6: **Făină de grâu nealbită** [din site] / în mixurile pentru pancakes și clătite [adaptat]
  - Sub IMG7: **Zahăr brun din trestie** [din site] / în loc de zahăr alb [din site]
- **Două carduri (față în față pe desktop, unul sub altul pe mobil):**
  - Card 1, titlu: **NOI** [nou]
    - (bifă) Făină de grâu nealbită, în mixurile pentru pancakes și clătite. [adaptat]
    - (bifă) Zahăr brun din trestie în loc de zahăr alb. [din site]
    - (bifă) Fără conservanți. Lista scurtă de ingrediente e pe fiecare ambalaj. [adaptat]
  - Card 2, titlu: **TU** [nou]
    - (bifă) Apă, la pancakes. [adaptat]
    - (bifă) Apă și ulei, la pizza. [adaptat]
    - (bifă) Ouă și unt, la lava cake. [adaptat]
    - Text mic: La fiecare mix, ce adaugi tu e scris clar pe ambalaj. [adaptat]
- **Sub carduri:**
  - Text: Lista completă de ingrediente și valorile nutriționale sunt pe pagina fiecărui produs. [din site]
  - Link text (negru, subliniat): **Vezi ingredientele** → `{{SHOP_URL}}/ingrediente` [nou] (URL de confirmat la lansare; site-ul are secțiunea INGREDIENTE în meniu)
- **Notă:** bifele sunt iconițe PNG negre (asset UI), nu caractere Unicode. Fără promisiuni de sănătate, fără „cel mai”. Nu extindem „nealbită” la alte categorii.
- **IMG6 (spec):**
  - Ce arată: un mic morman de făină albă, fină, într-un bol mic de ceramică neagră, cu o lingură de lemn în el; câteva urme de făină pe marginea bolului.
  - Încadrare: unghi de 30 de grade, bolul întreg în cadru, centrat.
  - Decupaj: **da**, bolul cu făina, **pe fundal alb simplu**. Bolul negru e obligatoriu: făina albă pe fundal alb nu se poate decupa.
  - Raport: 1:1 (export 400x400px, afișat la 200px).
  - Atmosferă: simplu, curat, „de cămară”, lumină naturală moale.
- **IMG7 (spec):**
  - Ce arată: zahăr brun din trestie, cristale mari aurii, într-un bol identic cu cel din IMG6 (ceramică neagră), cu o linguriță de lemn.
  - Încadrare: identică cu IMG6 (aceeași înălțime a camerei, aceeași lumină), ca cele două să arate ca o pereche.
  - Decupaj: **da**, **pe fundal alb simplu**.
  - Raport: 1:1 (export 400x400px, afișat la 200px).
  - Atmosferă: cald, cristale care prind lumina.

---

### S5-final

- **Scop:** ultimul click spre produse și, pentru cine nu a luat ghidul, a doua șansă.
- **Fundal:** portocaliu #FAA61A, val de intrare din turcoaz.
- **Copy:**
  - Titlu (Akrobat Black, foarte mare): **EAT WHAT YOU LOVE.** [din site, slogan oficial]
  - Text: Mixurile Lucas Bites le găsești online și în magazinele de lângă tine. [adaptat]
  - CTA (pill negru, text portocaliu): **Vezi toate mixurile** → `{{SHOP_URL}}/produse` [nou]
  - **Bloc condiționat** (doar contactele fără click pe `{{GUIDE_PDF_URL}}` în Email 1):
    - Text: Încă n-ai deschis ghidul cu 10 rețete Jamila? [nou]
    - Link text (negru, subliniat): **Descarcă ghidul** → `{{GUIDE_PDF_URL}}` [din Email 1]
  - **Varianta fără conținut condiționat** (dacă ESP-ul nu suportă): Text: Ghidul cu 10 rețete Jamila e tot aici, dacă vrei să-l mai deschizi o dată. [nou] + același link.
- **Imagine:** nu.

---

## 4. Footer (S6-footer)

Identic cu **Email 1, secțiunea 4 (S7-footer)**: același fundal, logo stripes, iconițe social, adresă, motivul abonării, `{{UNSUBSCRIBE_URL}}`, header-ele `List-Unsubscribe` + `List-Unsubscribe-Post` (one-click, RFC 8058) și aceeași notă „De confirmat” pentru denumirea juridică și CUI. Nu se modifică nimic, ca footerul să rămână consecvent în toată seria.

---

## 5. Predarea către Email 3

Email 3 din planul inițial (gama + ingrediente) e acum acoperit de Email 2, deci propunem:

- **Email 3 (ziua 5-6):** rețeta pas cu pas din ghid (fostul Email 2: „Teancul de duminică”, listă de ingrediente în stil BetterBrand) plus link spre YouTube, și transportul gratuit de la al 2-lea produs, dacă e încă valabil la lansare. Blocul de rețetă se alege după tag-ul de interes setat în Email 2 (`INTEREST_PIZZA` primește o rețetă de pizza etc.), cu pancakes ca variantă implicită pentru cine nu a dat click. Condiție: ghidul trebuie să conțină câte o rețetă pentru fiecare categorie; dacă nu, păstrăm doar pancakes.
- **Email 4 (ziua 12-14):** neschimbat față de planul din Email 1 (comunitate, recenzii, #lucasbites, un rând pentru Professional), apoi trecere în newsletterul lunar.
- Seria rămâne la 4 emailuri, conform promisiunii „o dată pe lună” făcute în formular.

---

## 6. Alt text

| Imagine | Alt text |
|---|---|
| Logo header | Lucas Bites |
| IMG1 (hero) | Lava cake rupt cu lingurița, cu ciocolată topită care curge pe farfurie |
| IMG2 | Pancakes cu sirop și clătite împăturite pe o farfurie portocalie |
| IMG3 | Budincă cremoasă într-o ceașcă, cu fructe de pădure |
| IMG4 | Banana bread cu două felii tăiate |
| IMG5 | Pizza de casă cu mozzarella și busuioc, cu o felie trasă |
| IMG6 | Bol cu făină de grâu |
| IMG7 | Bol cu zahăr brun din trestie |
| Logo footer | Lucas Bites, eat what you love |
| Iconițe social | Instagram / TikTok / Facebook / YouTube (câte una pe iconiță) |
| Valuri, săgeți desenate, bife | `alt=""` (decorativ) |

---

## 7. Întrebări pentru client

Povestea brandului: S2 folosește acum povestea de pe lucasbites.ro/povestea-noastra/ (Luca, Pankees, familia la masă). Întrebările 1 și 3 au primit răspuns de pe site. Rămân opționale:

1. ~~Cine este Lucas?~~ Răspuns pe site: Luca, copilul familiei fondatoare. De confirmat doar că povestea se poate folosi în continuare pe email, așa cum e pe site.
2. În ce an a pornit Lucas Bites și unde (oraș)?
3. ~~Ce v-a făcut să începeți?~~ Răspuns pe site.
4. Unde se produc mixurile (de exemplu, în România) și putem menționa asta în email?
5. Putem semna emailul cu prenumele părinților (de exemplu „[prenume] și [prenume], părinții lui Luca”)?

Confirmări de produs, necesare pentru copy și fotografii:

6. Mixul de budincă: ce arome are și ce se adaugă la preparare (lapte, apă sau altceva)?
7. „Fără conservanți” și „zahăr brun din trestie în loc de zahăr alb” sunt valabile pentru toate mixurile, inclusiv cele noi (Budinci, Banana Bread, Carrot Cake) și Pizza Crust Mix?
8. Ce se adaugă la Brownie, Banana Bread, Carrot Cake și la cele două mixuri de clătite? (Opțional, ca să completăm cardul „TU”.)
9. URL-urile finale la lansare: pagina de produse cu ancorele pe categorii și pagina INGREDIENTE.

---

## Reguli pentru toate fotografiile (Higgsfield)

- Doar mâncare. Fără ambalaje, sticle sau pungi, fără text, logo-uri sau etichete în imagine, fără fețe (mâinile sunt OK, dar în Email 2 nu le folosim).
- Toate cele 7 fotografii sunt decupaje: cereți **fundal alb simplu** în prompt, nu „transparent background” (modelul desenează tabla de șah). Fundalul îl scoatem noi local și exportăm PNG.
- Pentru decupaj curat: obiecte cu contur clar (farfurie, ceașcă, bol), nimic alb pe alb (de aceea făina e în bol negru), nimic transparent (fără pahare de sticlă).
- Lumină naturală caldă, texturi clare (pufos, lucios, cremos, crocant), apetisant, nu „de laborator”.
- Recuzita (farfurii, căni) poate fi portocalie, roz sau turcoaz, plus negru la bolurile de ingrediente; fără alte culori dominante puternice.
- Exporturi la 2x față de dimensiunea afișată; PNG optimizat, sub 250 KB per decupaj. Greutatea totală a emailului (imagini) sub 1,2 MB.
- Emailul trebuie să rămână lizibil cu imaginile blocate: toate titlurile, etichetele, textele și butoanele sunt text HTML live.
- Placeholder de link: `{{SHOP_URL}}` e aici rădăcina site-ului (paginile sunt `{{SHOP_URL}}/produse...`). În Email 1, `{{SHOP_URL}}` a fost folosit direct ca pagina PRODUSE: la build, aliniați cele două înainte de lansare.
