# Lucas Bites: Welcome Email 3, strategie, structură și copy final

Surse: `brief.md` (acest folder, decizii finale), `design-direction.md` (layout ales de UI Designer), `discovery.md`, `welcome-01/copy.md`, `welcome-02/copy.md`. Legendă: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [adaptat] = text aprobat ajustat pentru email, [nou] = text nou, de aprobat de client, [din site actual] = text de pe site-ul WordPress actual (lucasbites.ro, citit la 11.10.2026), [din site actual, diacritice corectate] = recenzie reală citată cuvânt cu cuvânt, cu diacritice adăugate și emoji eliminate, nimic altceva.

**Ce cere clientul:** produse bestseller, recenzii clienți, UGC.

**Fără prețuri, fără cod de reducere.** Singurul motiv să comande acum: transportul gratuit de la al 2-lea produs. Recenziile sunt doar cele reale din tabelul din `brief.md`. Pozele UGC sunt placeholdere vizibile, nu imagini generate.

---

## Îmbunătățiri față de strategia inițială

Strategia utilizatorului pentru Email 3: bestsellers, recenzii clienți, UGC. Ce am adăugat și de ce:

- **Recenzia stă lângă produs, chiar deasupra butonului.** Fiecare bestseller are ratingul lui și o recenzie reală în card. Dovada ajunge exact în momentul deciziei, nu într-un bloc separat pe care cititorul îl poate sări.
- **Ordinea produselor se schimbă după interesul arătat în Email 2.** Tag-urile `INTEREST_*` setate la click în Email 2 pun primul pe mobil produsul pe care abonatul l-a ales deja. Click-urile din Email 3 actualizează aceleași tag-uri, ca Email 4 să aleagă rețeta potrivită.
- **Un motiv concret să comande acum, fără reducere:** transport gratuit de la al 2-lea produs, prezentat ca bilet. Crește coșul (2+ produse), nu atinge marja și nu depinde de prețurile care sunt încă în lucru.
- **UGC cu două roluri și cu acord:** dovadă („așa arată la alții”) și invitație („postează cu @lucas_bites și #lucasbites”). Nu generăm poze prezentate ca venite de la clienți: o recenzie sau o poză falsă de client e practică comercială interzisă în UE (Directiva Omnibus 2019/2161) și ar strica încrederea pe care o construiește tot emailul.
- **Măsurăm pe click și pe comandă, nu pe deschideri,** și excludem cumpărătorii, dacă ESP-ul primește comenzile. Cine a comandat deja nu primește un email de vânzare pentru ce tocmai a cumpărat.
- **Recenziile și UGC s-au mutat din Email 4 în Email 3**, lângă produse, unde ajută vânzarea. Email 4 devine rețeta pas cu pas din ghid, iar seria rămâne la 4 emailuri, conform promisiunii „o dată pe lună” din formular.

---

## Ce preluăm din referințe și de ce

Rezumat din `design-direction.md` secțiunea 1. Ideea vizuală: „favoritele, puse pe masă”: patru farfurii negre mate pe plăci în culorile brandului, iar dovada stă mereu lângă mâncare.

| Pattern | Din | Unde în Email 3 | De ce |
|---|---|---|---|
| Hero „le încerci pe toate”: toate favoritele într-o singură imagine | ref1 (Botenz, „Try Them All”) | S1-hero, IMG1 | Spune din prima secundă că emailul e despre mai multe favorite. Alt tip de hero decât Email 1 (un stack) și Email 2 (un lava cake + tipografie). |
| Etichetă-pastilă (chip) lângă CTA | ref1 (Botenz) | S1 (transport gratuit), S2 (Bestseller pe Classic) | Mesaj scurt și vizibil, fără să devină al doilea buton. |
| Titlu mare „Best sellers” + buton „vezi toate” sub listă | ref1 (Botenz) | S2-bestsellers | Titlu, 4 produse, un link general pentru cine nu s-a decis. |
| Grid 2 x 2 cu foto pătrat rotunjit pe fundal colorat | ref6 (BetterBrand) + ref3 (Blue Apron) | S2, IMG2-IMG5 | Nu cercuri (Email 1), nu zig-zag (Email 2). |
| Stele + citat + nume în cardul produsului, deasupra CTA | ref5 (Beguile) | S2, în fiecare card | Recenzia lângă butonul de cumpărare. |
| Carduri albe de recenzii pe fundal închis, în trepte | ref5 (Beguile) | S3-recenzii | Ritm de conversație; pe negru cardurile ies în față fără umbre. |
| Cifra mare de dovadă deasupra recenziilor | ref3 (Blue Apron) | S3, „4,9 din 5” | Cifra spune volumul, cardurile spun vocea. |
| Colaj de fotografii reale | ref7 (Kings Row) | S4-UGC | Grid de poze de la clienți, cu placeholdere vizibile până vin pozele reale. |
| Cupon „bilet” cu linie punctată, fără cod | ref6 (BetterBrand) | S5-transport | Dă greutate unui beneficiu care altfel ar fi o propoziție pierdută. |
| Valuri între secțiuni | ref4/ref6, deja în Email 1 și 2 | toate tranzițiile | Continuitate de serie. |

Ce NU preluăm: produse în cercuri (Email 1), zig-zag (Email 2), ambalaje în poze, prețuri pe card, „25% OFF”, cod de reducere, countdown, grafice comparative și cifre nutriționale, text peste fotografie, fundaluri texturate și gradiente, umbre sub carduri, blocul social negru din Email 1.

---

## 1. Obiectiv, KPI, trimitere

**Obiectiv:** prima comandă. Abonatul vede 4 favorite, fiecare cu dovada lângă el, și pune 2 produse în coș pentru transport gratuit.

**KPI principal:** rata de click unic pe oricare dintre linkurile de produs (S1, cele 4 carduri din S2, „Vezi toate mixurile”, CTA-ul final din S5), raportată la emailurile livrate. Țintă 6%+, alertă sub 2,5%.

**KPI secundar (doar dacă ESP-ul primește comenzile):** rata de comandă atribuită `utm_campaign=welcome_03` (fereastră de atribuire 7 zile de la click), raportată la emailurile livrate. Țintă 1%+, alertă sub 0,3%. Plus, ca raport, ponderea comenzilor cu 2+ produse (efectul biletului).

**KPI terțiar:** rata de click unic pe butonul Instagram din S4 (UGC). Țintă 1%+, alertă sub 0,3%. Și numărul de postări noi cu #lucasbites în 14 zile de la lansare (raport manual, nu țintă).

**Timing:** ziua 5-6 după Email 1: la 120 de ore după Email 1, cu fereastră de livrare 09:00-11:00, ora României. Dacă cele 120 de ore cad în afara ferestrei, emailul așteaptă următoarea fereastră (deci pleacă în ziua 5 sau 6). Minimum 72 de ore după Email 2.

**Segment și excluderi:**
- Intră: toți cei care au primit Email 2, **inclusiv cei care nu l-au deschis** (deschiderile sunt umflate de Apple MPP, nu le folosim ca filtru).
- Exclus, dacă ESP-ul primește comenzile din magazin: orice contact cu cel puțin o comandă plasată după înscriere. Aceștia sar peste Email 3 și primesc direct Email 4 (rețeta e utilă și după cumpărare). Dacă ESP-ul nu primește comenzile, emailul pleacă tuturor; integrarea magazin-ESP rămâne recomandarea noastră înainte de lansare.
- Ies din serie la: dezabonare, hard bounce, plângere spam.

**Ordinea bestseller-elor (module independente în S2, schimbate de ESP după tag):**

| Tag din Email 2 | Ordine carduri (1 = primul pe mobil) |
|---|---|
| fără tag (implicit) și `INTEREST_PANCAKES` | Buttermilk, Classic, Pizza, Brownie |
| `INTEREST_PIZZA` | Pizza, Buttermilk, Classic, Brownie |
| `INTEREST_PRAJITURI` | Brownie, Buttermilk, Classic, Pizza |
| `INTEREST_BUDINCI` | Brownie, Buttermilk, Classic, Pizza [propunere: budinca nu e în bestsellers, cel mai apropiat e desertul] |

- Ordinea implicită urmează numărul de recenzii (indiciul nostru pentru volumul vânzărilor): 222, 148, 80, 11.
- Contact cu mai multe tag-uri: precedență `INTEREST_PIZZA` > `INTEREST_PRAJITURI` > `INTEREST_BUDINCI` > `INTEREST_PANCAKES` (interesele mai rare câștigă, pancakes e oricum în față implicit).
- Dacă ESP-ul nu suportă blocuri condiționate: 3 versiuni ale emailului (implicit, pizza, prăjituri), fiecare trimisă segmentului ei, cu excludere reciprocă.
- Culoarea plăcii rămâne cu produsul, indiferent de ordine (Buttermilk roz, Classic portocaliu, Pizza turcoaz, Brownie roz).

**Acțiune pe click (segmentare):** click pe Buttermilk sau Classic setează `INTEREST_PANCAKES`, pe Pizza `INTEREST_PIZZA`, pe Brownie `INTEREST_PRAJITURI`. Email 4 folosește tag-urile la alegerea rețetei.

**UTM:** fiecare link primește `utm_source=email&utm_medium=welcome&utm_campaign=welcome_03&utm_content=<id>`. Valori `utm_content`: `s1-hero`, `s2-buttermilk`, `s2-classic`, `s2-pizza`, `s2-brownie`, `s2-toate`, `s3-recenzii`, `s4-instagram`, `s5-final`. Pentru A/B, adăugați `utm_term=subj-a` / `subj-b`, dacă ESP-ul nu raportează separat pe variantă.

**Condiții de lansare (fără ele, emailul nu pornește):**
1. Paginile de produs de pe site-ul nou sunt live (altfel KPI-ul principal trimite în 404).
2. Transportul gratuit de la al 2-lea produs e confirmat ca valabil la lansare.
3. Clientul a confirmat că putem folosi prenumele și inițiala autorilor recenziilor (vezi întrebarea 4).
4. Gridul UGC are poze reale cu acordul autorilor, **sau** se aplică varianta fără grid din S4. Placeholderele nu pleacă niciodată la abonați.

Gărzi de siguranță (opresc trimiterea, nu sunt KPI): plângeri spam sub 0,10%, dezabonări sub 0,5%, hard bounce sub 1%. Rata de deschidere se citește doar orientativ.

---

## 2. Subiecte și preheadere

| # | Subiect | Caractere | Preheader |
|---|---|---|---|
| A **[recomandat]** | Le încerci pe toate? [nou] | 20 | Patru favorite, recenziile lor și transport gratuit de la al 2-lea produs. [nou] |
| B | 4 favorite, notate de voi [nou] | 25 | Ce spun clienții despre ele, cu numele lor. Plus transport gratuit de la 2 produse. [nou] |
| C | Favoritele, puse pe masă [nou] | 24 | Pancakes, pizza și brownie, așa cum le fac alții acasă. [nou] |

De ce A: e jucăuș, scurt (se citește întreg pe mobil) și plătit direct de titlul din hero, iar preheaderul pune pe masă tot ce oferă emailul, inclusiv beneficiul concret. Nu repetă cifra 4,9, folosită deja în Email 1 (S4) și Email 2 (S2).

**Test A/B:** A (curiozitate) contra B (dovadă socială), pe primele ~1.000 de trimiteri (~500 pe variantă). Câștigătorul se alege pe **click unic pe linkurile de produs raportat la livrate**, nu pe deschideri. Dacă diferența e sub 1 punct procentual, testul continuă pe următoarele ~1.000 înainte de a declara un câștigător.

**Expeditor:** Lucas Bites. **Reply-to:** aceeași adresă monitorizată ca la Email 1 și 2.

---

## 3. Structura, de sus în jos

Lățime 600px, layout și dimensiuni ca în `design-direction.md` secțiunea 3. Titluri: `Akrobat, "Arial Narrow", Arial, sans-serif`, majuscule. Text: `Arial, Helvetica, sans-serif`, 16px. Pe turcoaz, alb, portocaliu și roz, tot textul e negru; pe negru, text doar portocaliu (în cardurile albe din S3, negru). Butoane pastilă bulletproof: negru cu text portocaliu pe fundaluri deschise, portocaliu cu text negru pe negru.

Ordinea culorilor (diferită de Email 1 și 2): alb, **turcoaz**, alb, negru, portocaliu, roz, alb. Valurile, stelele, plăcile colorate și logo-urile sunt assets UI desenate de `build.py` și nu intră în cele 5 fotografii.

---

### S0-header

- **Scop:** recunoaștere imediată.
- **Fundal:** alb, val alb spre turcoaz la bază.
- **Conținut:** identic cu Email 1 și 2 (logo `Logo/Logo_LucasBites.png`, centrat, 180px, export 360px).
- **Imagine:** nu (doar logo).

---

### S1-hero

- **Scop:** plătește subiectul, arată toate favoritele dintr-o privire și pune beneficiul (transport gratuit) lângă primul buton, vizibil fără scroll pe mobil.
- **Fundal:** turcoaz #86D2DA, tot textul negru. IMG1 trece peste valul turcoaz spre alb.
- **Copy:**
  - Supratitlu (eyebrow): **favoritele voastre** [nou]
  - Titlu (H1, 2 rânduri): **LE ÎNCERCI PE TOATE?** [nou]
  - Text: Patru favorite, cu nota și părerea celor care le-au făcut deja acasă. [nou]
  - Chip: **TRANSPORT GRATUIT DE LA AL 2-LEA PRODUS** [adaptat din site actual] [de confirmat la lansare]
  - CTA (buton mare): **Vezi favoritele** → `{{SHOP_URL}}/produse` + UTM `s1-hero` [nou]
- **Ordinea pe mobil:** eyebrow, H1, text, chip, buton, apoi IMG1.
- **IMG1 (spec):**
  - Ce arată: 4 farfurii rotunde negre mate, identice, așezate 2 x 2 și atingându-se: un stack scurt de Buttermilk cu unt, Classic cu felii de banană și miere, 2 felii de pizza, 3 pătrate de brownie.
  - Încadrare: de sus (top-down), toate cele 4 farfurii întregi în cadru.
  - Decupaj: **da**, farfuriile împreună, generate pe fundal alb simplu; fundalul îl scoatem local.
  - Raport: 1:1 la generare; compoziție finală JPG 1200 x 1040 (afișat 600 x 520), decupajul pus pe turcoaz, cu valul turcoaz spre alb trecând prin treimea de jos a farfuriilor.
  - Atmosferă: „masa cu favoritele”, generos, luminos.

---

### S2-bestsellers

- **Scop:** cele 4 produse, fiecare cu dovada lui chiar deasupra butonului (KPI principal + tag de interes).
- **Fundal:** alb, val alb spre negru la bază.
- **Copy antet:**
  - Titlu (H2): **BESTSELLERS** [nou]
  - Text: Fiecare cu nota lui și cu o recenzie reală de pe lucasbites.ro. [nou]
- **Layout:** grid 2 x 2 pe desktop, 1 coloană pe mobil; fiecare card e un modul independent, reordonat după tabelul din secțiunea 1. Ordinea de mai jos e cea implicită.
- **Regulă pentru citate:** maximum 80 de caractere, între ghilimele românești, recenzie reală, numele scurtat la prenume + inițiala numelui. Nicio recenzie din S2 nu se repetă în S3. Kinga Ludescher nu apare (e deja în Email 1).

**Card 1: Buttermilk Pankees** (placă roz)
  - Nume: **BUTTERMILK PANKEES** / 290 g [din site actual]
  - Rating: stele + **4,9 · 222 de recenzii** [din site actual]
  - Citat: „Extraordinar de bune, se prepară rapid iar copilul le adoră!!!” [din site actual, diacritice corectate] (62 caractere)
  - Semnătură: **Carmen N., 19.07.2021**
  - CTA (buton card): **Vezi Buttermilk** → `{{URL_BUTTERMILK}}` + UTM `s2-buttermilk` [nou]
  - **IMG2 (spec):**
    - Ce arată: stack de 5 pancakes pufoase pe farfuria neagră mată, cu o felie triunghiulară scoasă din stack ca să se vadă miezul aerat; unt topit, sirop strâns în baltă pe farfurie, 3-4 zmeure.
    - Încadrare: lateral, aproape la nivelul ochilor (10 grade), farfuria întreagă în cadru.
    - Decupaj: **da**, pe fundal alb simplu; decupajul se pune centrat pe placa roz.
    - Raport: 1:1 (placă finală 492 x 492, afișată 246 x 246, colțuri rotunjite 14px arse în imagine).
    - Atmosferă: textură, „uite cât de pufoase”.

**Card 2: Classic Pankees** (placă portocalie)
  - Chip: **BESTSELLER** [din site] [de confirmat cu clientul]
  - Nume: **CLASSIC PANKEES** / 290 g [din site actual]
  - Rating: stele + **4,9 · 148 de recenzii** [din site actual]
  - Citat: „Pufoase și delicioase!” [din site actual] (22 caractere)
  - Semnătură: **Gabriela P., 17.07.2022**
  - CTA: **Vezi Classic** → `{{URL_CLASSIC}}` + UTM `s2-classic` [nou]
  - **IMG3 (spec):**
    - Ce arată: 3 pancakes așezate în evantai (solzi) pe farfuria neagră mată, felii de banană, un fir de miere, o furculiță cu o bucată tăiată sprijinită pe marginea farfuriei.
    - Încadrare: 45 de grade, farfuria întreagă în cadru.
    - Decupaj: **da**, pe fundal alb simplu; pe placa portocalie.
    - Raport: 1:1 (492 x 492, afișat 246 x 246).
    - Atmosferă: mic dejun liniștit, simplu.

**Card 3: Pizza Crust Mix** (placă turcoaz)
  - Nume: **PIZZA CRUST MIX** / 500 g [din site actual]
  - Rating: stele + **4,8 · 80 de recenzii** [din site actual]
  - Citat: „Aleg mereu mixul Pizza Crust pentru o pizza rapidă, cu ingrediente din frigider.” [din site actual, diacritice corectate] (80 caractere)
  - Semnătură: **Luminița B., 23.04.2021**
  - CTA: **Vezi Pizza Crust** → `{{URL_PIZZA}}` + UTM `s2-pizza` [nou]
  - **Notă:** recenzia are 4 stele pe site; stelele din card arată ratingul produsului (4,8), nu nota recenziei, deci e corect. Recenzia „Blat intradevar pufos” (Paula P.) nu se poate folosi fără a corecta și ortografia („într-adevăr”), ceea ce depășește corectura de diacritice permisă.
  - **IMG4 (spec):**
    - Ce arată: 2 felii de pizza de casă suprapuse ușor pe farfuria neagră mată; felia din față are marginea spre cameră, ca să se vadă blatul înalt și aerat. Ciuperci, ardei, măsline negre, mozzarella.
    - Încadrare: 30 de grade, farfuria întreagă în cadru.
    - Decupaj: **da**, pe fundal alb simplu; pe placa turcoaz.
    - Raport: 1:1 (492 x 492, afișat 246 x 246).
    - Atmosferă: seară relaxată, poftă. Diferit de pizza întreagă de sus din Email 2.

**Card 4: Brownie Mix** (placă roz)
  - Nume: **BROWNIE MIX** / 450 g [din site actual]
  - Rating: stele + **5,0 · 11 recenzii** [din site actual]
  - Citat: „Bun. Rețeta este foarte bună” [din site actual, diacritice corectate] (28 caractere)
  - Semnătură: **Liliana F., 26.11.2023** (pe site: „FLOREA LILIANA”; am presupus că Florea e numele de familie, de confirmat)
  - CTA: **Vezi Brownie** → `{{URL_BROWNIE}}` + UTM `s2-brownie` [nou]
  - **Rezervă:** dacă Brownie Mix nu e pe stoc la lansare, cardul trece pe Lava Cake Mix 400 g (5,0 · 5 recenzii); recenzia pentru Lava Cake trebuie aleasă atunci din site, după aceleași reguli.
  - **IMG5 (spec):**
    - Ce arată: 3 pătrate groase de brownie stivuite pe farfuria neagră mată, crustă lucioasă crăpată, colțul pătratului de sus rupt, cu interiorul umed vizibil, câteva firimituri.
    - Încadrare: lateral, 0-10 grade, farfuria întreagă în cadru.
    - Decupaj: **da**, pe fundal alb simplu; pe placa roz.
    - Raport: 1:1 (492 x 492, afișat 246 x 246).
    - Atmosferă: intens, ciocolatos. Diferit de brownie-ul de sus din Email 1.

- **Sub grid:** link-buton general **Vezi toate mixurile** → `{{SHOP_URL}}/produse` + UTM `s2-toate` [din Email 2]
- **URL-uri de produs:** pe site-ul nou, `{{URL_*}}` devin `{{SHOP_URL}}/produse/<slug>`; slug-urile finale de confirmat. Până atunci, linkurile de pe site-ul actual: Buttermilk https://www.lucasbites.ro/produs/buttermilk-pankees-290g/ , Classic https://www.lucasbites.ro/produs/clasic-pankees-290g/ , Pizza https://www.lucasbites.ro/produs/pizza-crust-mix-500g/ , Brownie https://www.lucasbites.ro/produs/brownie-mix-450g-2/ .
- **Notă:** ratingurile și numărul de recenzii sunt valabile la 11.10.2026; se verifică înainte de lansare și la fiecare actualizare a fluxului.

---

### S3-recenzii

- **Scop:** dovada generală: cifra dă volumul, cele 3 carduri dau vocea clienților.
- **Fundal:** negru #000000, text portocaliu; cardurile sunt albe, cu text negru. Val negru spre portocaliu la bază.
- **Copy:**
  - Titlu (H2, portocaliu): **NU DOAR NOI LE LĂUDĂM.** [nou]
  - Stele portocalii + cifra mare: **4,9 din 5** [din site]
  - Sub cifră: **peste 1.100 de recenzii** [din site]
- **3 carduri în trepte** (stânga, centru, dreapta pe desktop; una sub alta pe mobil). În fiecare: nume + stele negre, produsul, citatul.
  - **Card 1:** **Andreea H.** · Classic Pankees
    „Clătitele ies foarte pufoase și gustoase. O adevărată plăcere să le faci și să le mănânci” [din site actual, diacritice corectate, emoji eliminate]
  - **Card 2:** **Irina A.** · Pizza Crust Mix
    „Am folosit amestecul pentru blat de pizza, Pizza Crust Mix, 500g și mi-au ieșit două pizza delicioase!” [din site actual, diacritice corectate]
  - **Card 3:** **Irina S.** · Classic Pankees
    „Sunt foarte încântată de aceste produse! Sunt minunate! Voi reveni cu comenzi!” [din site actual]
- **Sub carduri:** link text (portocaliu, subliniat): **Citește toate recenziile** → `{{REVIEWS_URL}}` + UTM `s3-recenzii` [nou] (URL de confirmat; până atunci, pagina Classic Pankees de pe site-ul actual).
- **De verificat înainte de lansare:** nota (stelele) fiecăreia dintre cele 3 recenzii pe site. Brief-ul nu o menționează; dacă vreuna are sub 5 stele, cardul ei afișează numărul real de stele sau stelele se scot din card. Cifra 1.100 / 4,9 e valabilă la 10.10.2026.
- **Recenzii excluse intenționat:** Kinga Ludescher (deja în Email 1), Valentina și Roxana H. (superlativ „cele mai bune / cele mai delicioase”), Arabela („perfecte”, absolut), Paula P. (cere corectură de ortografie, nu doar de diacritice).
- **Imagine:** nu (doar stele, asset UI).

---

### S4-ugc

- **Scop:** dovadă vizuală („așa arată la alții”) și invitație să posteze (KPI terțiar + material pentru emailurile viitoare).
- **Fundal:** portocaliu #FAA61A, text negru. Val portocaliu spre roz la bază.
- **Copy:**
  - Titlu (H2): **LA VOI ÎN BUCĂTĂRIE.** [nou]
  - Text: Așa arată Pankees, pizza și brownie făcute de voi. Postează și tu ce gătești cu @lucas_bites și #lucasbites. [adaptat din site]
  - Text mic: Cu acordul tău, poza ta poate apărea într-un email viitor. [nou]
- **Grid 3 x 2 (6 celule, 3 pe rând și pe mobil):**
  - Până vin pozele reale, fiecare celulă e placeholder HTML (roz, contur negru punctat), cu textul **POZĂ CLIENT, / DE ÎNLOCUIT** și sub ea **@handle_client**. În cod: `<!-- UGC-1: POZĂ CLIENT, DE ÎNLOCUIT -->` ... `UGC-6`.
  - La înlocuire: poza reală 352 x 352 (afișată 176 x 176), @handle-ul real sub poză, alt text „Poză de la @handle”. Doar cu acordul scris al autorului (vezi întrebarea 5). Pozele se salvează în `welcome-03/ugc/`.
  - Recomandare de mix: 2 pancakes, 1 clătite, 1 pizza, 1 brownie sau lava cake, 1 masă cu mai multe produse. Fără fețe de copii.
- **CTA (buton mare):** **Vezi @lucas_bites pe Instagram** → https://www.instagram.com/lucas_bites/ + UTM `s4-instagram` [nou]
- **Rând sub buton:** #lucasbites · pe TikTok: @lucas.bites.ro [nou]
- **Varianta fără grid (obligatorie dacă la lansare sunt sub 3 poze reale aprobate):** grid-ul se scoate complet, rămân titlul, un singur text: „Postează ce gătești cu @lucas_bites și #lucasbites. Cu acordul tău, poza ta poate apărea în emailurile noastre.” [nou] și butonul. Cu 3-5 poze reale: un singur rând de 3. Placeholderele nu pleacă niciodată la abonați.
- **Imagine:** nu se generează nimic. Pozele UGC vin doar de la clienți.

---

### S5-transport

- **Scop:** motivul să comande acum și ultimul click spre magazin.
- **Fundal:** roz #F7ACB4, text negru. Val roz spre alb la bază.
- **Copy:**
  - Titlu (H2): **IA-LE ÎN PERECHE.** [nou]
  - **Biletul:**
    - Zona stângă (negru, text portocaliu): **2+** / **produse** [nou]
    - Zona dreaptă: **Transport gratuit** [din site actual] / Pui al 2-lea produs în coș, iar transportul e pe noi. [nou]
  - Text: Pancakes pentru dimineață, pizza pentru seară. Sau brownie pentru oricând. [nou]
  - CTA (buton mare): **Alege-ți favoritele** → `{{SHOP_URL}}/produse` + UTM `s5-final` [nou]
  - Text mic sub buton: Transport gratuit de la al 2-lea produs, la comenzile de pe {{SHOP_URL}}. [adaptat din site actual] [de confirmat la lansare]
  - Semnătură (Akrobat): **eat what you love** [din site, slogan oficial]
- **Notă:** dacă oferta se schimbă la lansare, se modifică doar textul biletului, chip-ul din S1 și preheaderul. Nu scriem „pentru orice comandă” sau „indiferent de produs” până nu confirmă clientul cum se numără produsele (vezi întrebarea 3).
- **Imagine:** nu.

---

## 4. Footer (S6-footer)

Identic cu **Email 1, secțiunea 4 (S7-footer)** și cu Email 2. Nu se modifică nimic.

- **Fundal:** alb, separat de secțiunea de deasupra printr-o linie neagră subțire.
- **Logo:** `Logo/Logo_LucasBites_stripes-nobg.png`, centrat, 200px lățime.
- **Iconițe social** (negre, 32px, assets UI): Instagram, TikTok, Facebook, YouTube, cu aceleași linkuri ca în Email 1.
- **Copy:**

> Lucas Bites · Roșu, Chiajna, Ilfov
> office@lucasbites.ro · +40 731 399 399
>
> Primești acest email pentru că te-ai abonat pe lucasbites.ro la ghidul de rețete și la newsletterul nostru lunar.
>
> Nu mai vrei emailuri de la noi? [Dezabonează-te aici]({{UNSUBSCRIBE_URL}}). Durează un click.
>
> © 2026 Lucas Bites

- **Tehnic:** `{{UNSUBSCRIBE_URL}}` se înlocuiește cu tag-ul de dezabonare al ESP-ului ales. Header-ele `List-Unsubscribe` + `List-Unsubscribe-Post` (one-click, RFC 8058) trebuie să fie active.
- **De confirmat:** denumirea juridică a firmei (SRL) și CUI, dacă vreți identificarea completă a comerciantului în footer.

---

## 5. Predarea către Email 4

Recenziile și UGC, planificate inițial în Email 4, sunt acum în Email 3. Email 4 se replanifică:

- **Email 4 (ziua 12-14, fereastra 09:00-11:00):** rețeta pas cu pas din ghid (fostul „Teancul de duminică”, listă de ingrediente în stil BetterBrand), plus link spre YouTube, plus un singur rând pentru gama Professional: „Ai cafenea, restaurant sau patiserie? Aceeași rețetă, porții constante, preparare rapidă în bucătărie.” [adaptat din site], cu link spre pagina Professional.
- **Alegerea rețetei:** după tag-urile `INTEREST_*` din Email 2 și Email 3 (`INTEREST_PIZZA` primește o rețetă de pizza etc.), cu pancakes ca variantă implicită. Condiție: ghidul conține câte o rețetă pentru fiecare categorie; dacă nu, rămâne doar pancakes.
- **Cumpărătorii primesc Email 4** (rețeta e utilă și după comandă), inclusiv cei care au sărit peste Email 3.
- **UGC în Email 4:** opțional, 1-3 poze reale noi venite după Email 3 (cu acord), ca dovadă că invitația funcționează.
- **După Email 4:** contactul trece în newsletterul lunar. Seria rămâne la 4 emailuri, conform promisiunii „o dată pe lună” din formular și anunțului din Email 1 (S6).
- **Ieșire din serie:** dezabonare, hard bounce, plângere spam.

---

## 6. Alt text

| Imagine | Alt text |
|---|---|
| Logo header | Lucas Bites |
| IMG1 (hero) | Patru farfurii cu pancakes, pizza și brownie, văzute de sus |
| IMG2 | Teanc de pancakes Buttermilk tăiat, cu unt și sirop |
| IMG3 | Pancakes Classic în evantai, cu banană și miere |
| IMG4 | Două felii de pizza de casă cu blat pufos |
| IMG5 | Pătrate de brownie stivuite, cu interior umed |
| Stele card Buttermilk | Rating 4,9 din 5 |
| Stele card Classic | Rating 4,9 din 5 |
| Stele card Pizza | Rating 4,8 din 5 |
| Stele card Brownie | Rating 5 din 5 |
| Stele S3 (mari) | Rating 4,9 din 5 |
| Stele în cardurile S3 | Rating 5 din 5 (sau nota reală, după verificare) |
| Poze UGC (după înlocuire) | Poză de la @handle (handle-ul real) |
| Logo footer | Lucas Bites, eat what you love |
| Iconițe social | Instagram / TikTok / Facebook / YouTube (câte una pe iconiță) |
| Valuri, plăci colorate | `alt=""` (decorativ) |

---

## 7. Întrebări pentru client

1. **Bestsellers:** i-am ales după numărul de recenzii de pe site (Buttermilk 222, Classic 148, Pizza Crust 80, Brownie 11), ca indiciu pentru vânzări. Sunt și produsele cele mai vândute? Dacă alt produs se vinde mai bine decât Brownie, îl punem pe al 4-lea loc. Lava Cake rămâne rezervă.
2. **Eticheta „Bestseller” pe Classic Pankees:** o folosim în email, așa cum apare pe site-ul nou? Se bazează pe date de vânzări?
3. **Transport gratuit de la al 2-lea produs:** e valabil la lansarea emailului? Se aplică la orice combinație de produse, inclusiv 2 bucăți din același produs? Există o valoare minimă a coșului sau excepții (gama Professional, anumite zone)?
4. **Numele din recenzii:** în email am scurtat numele la prenume + inițiala numelui (Carmen N., Gabriela P., Luminița B., Liliana F., Andreea H., Irina A., Irina S.). Avem voie să le folosim în email (termenii site-ului sau acordul dat la publicarea recenziei)? La „FLOREA LILIANA”: prenumele e Liliana? Preferați să afișăm și data recenziei (cele mai multe sunt din 2021) sau doar numele?
5. **Pozele UGC:** aveți poze de la clienți (Instagram, TikTok, mesaje) pe care le putem folosi? Pentru fiecare avem nevoie de acordul scris al autorului (un mesaj de tipul „da, puteți folosi poza mea în emailurile Lucas Bites, cu @handle-ul meu” e suficient), salvat împreună cu poza. Fără poze aprobate, S4 pleacă fără grid.
6. **Comenzile în ESP:** magazinul nou trimite comenzile în platforma de email? Fără ele nu putem exclude cumpărătorii și nu putem măsura comenzile din email.
7. **URL-urile finale:** paginile celor 4 produse pe site-ul nou, pagina cu toate recenziile (dacă există) și pagina Professional (pentru Email 4).
8. **Dovada socială:** rămânem la „peste 1.100 de recenzii, 4,9 din 5” (site-ul nou) sau trecem la cifra de pe site-ul actual (4,83, 3.017 recenzii)?

---

## Reguli pentru toate fotografiile (Higgsfield)

- 5 fotografii, doar mâncare. Fără ambalaje, sticle sau pungi, fără text, logo-uri sau etichete, fără fețe, fără mâini.
- Toate sunt decupaje: promptul cere **fundal alb simplu**, nu „transparent background”, nu Remove Background. Fundalul îl scoatem noi local.
- Recuzită comună: aceeași farfurie rotundă neagră mată în toate cele 5 poze, ca setul să arate unitar pe plăcile colorate. Farfuria neagră dă și contur clar pentru decupaj.
- Lumină naturală caldă, texturi clare (pufos, lucios, crocant), apetisant, nu „de laborator”.
- Fotografiile diferă de cele din Email 1 și Email 2 (vezi tabelul din `design-direction.md` secțiunea 4).
- **Pozele UGC nu se generează.** Vin doar de la clienți, cu acord.
- Exporturi la 2x față de dimensiunea afișată; plăcile produselor PNG/JPG sub 250 KB fiecare, hero JPG sub 300 KB; greutatea totală a imaginilor sub 1,2 MB. HTML sub 102 KB, ca Gmail să nu taie emailul înainte de footer.
- Emailul rămâne lizibil cu imaginile blocate: titluri, nume de produse, ratinguri, recenzii, bilet și butoane sunt text HTML live.
- Placeholder de link: `{{SHOP_URL}}` e rădăcina site-ului, ca în Email 2.
