# Lucas Bites: New Customer, Email 2, strategie, structură și copy final

Surse: `brief.md` (acest folder, decizii din 12.10.2026, au prioritate), `discovery.md` (inclusiv 8b), `new-customer-01/copy.md` (format, footer, UTM, secțiunea 5), `refs/ref3.png`, `refs/ref4.png`, `packshots/`, paginile propunerii v3 citite la 12.10.2026 (lista din secțiunea 8). Legendă, aceeași ca la Email 1: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [adaptat] = text aprobat ajustat pentru email, [nou] = text nou, de aprobat de client, [din site actual] = site-ul WordPress actual, [neverificat] = funcție theMarketer negăsită în documentația oficială, [de confirmat] = informație comercială de confirmat la lansare.

**Ce cere clientul:** idei de rețete de încercat; produsele potrivite pentru fiecare rețetă (fiecare rețetă cu produsul ei, cu packshot-ul real).

**Ce fel de email e:** al doilea email de marketing după prima comandă, trimis după livrare. Clientul a gustat deja (sau urmează să guste) primul mix. E primul email din flux care vinde, dar blând: rețeta deschide pofta, produsul e doar „cu ce o faci”. Fără prețuri, fără coduri de reducere.

**Rețetele sunt ale brandului**, citite de pe propunerea v3. Pentru cele 3 rețete alese, site-ul publică doar titlu, produs, timp și moment. Nu scriem ingrediente, pași sau descrieri de gust.

---

## Ce am adăugat față de structura cerută și de ce

Structura cerută: rețete + produsul fiecărei rețete. Am adăugat:

- **S3 „Cum au ieșit?”** (cerut în brief, decizia 3). Email 1 a promis „În câteva zile te întrebăm cum au ieșit”; dacă nu întrebăm, promisiunea pică. Blocul are două ieșiri: recenzie (pentru cine e mulțumit) și reply (pentru cine a avut o problemă, ca să ne scrie nouă înainte să scrie o recenzie proastă).
- **S4 „Al doilea produs”**: o bandă de un rând cu transportul gratuit de la al 2-lea produs [de confirmat] și un link spre toată gama. Justificare: site-ul îl afișează în header pe fiecare pagină, iar pentru o a doua comandă e un motiv concret, fără reducere. Dacă nu se confirmă la lansare, banda rămâne doar cu linkul.
- **Ce NU am adăugat:**
  - lista de cumpărături și invitația „Trimite-ne rețeta ta” (au fost în Email 1, aici ar lungi emailul);
  - recenzii sau stele (clientul a cumpărat deja; cifra 1.100 / 4,9 a fost în welcome);
  - grila automată de produse theMarketer (ascunderea prețului din bloc rămâne neverificată, întrebarea 11 din Email 1); folosim 3 produse alese manual;
  - a 4-a rețetă. Email 1 a fost tăiat pentru lungime; 3 perechi rețetă + produs încap în 3-4 ecrane pe mobil. Restul rețetelor stau în rezervă pentru conținut condiționat (S2, tabelul de rezerve).

---

## Ce preluăm din ref3 și ref4 (UI Designer decide final)

Layout-ul, culorile pe secțiuni și pattern-urile le alege UI Designer. Mai jos, doar ce pattern se potrivește cu ce secțiune. Roșul din ref4 devine una dintre cele 4 culori de brand; bleumarinul din ref3 la fel. De evitat, pentru că au fost în Email 1: hero roz cu farfurii la colțuri, carduri albe cu imagine rotundă, zig-zag farfurie + bandă.

| Pattern | Sursă | Potrivit pentru | De ce |
|---|---|---|---|
| Titlu foarte mare, scurt, pe bloc de culoare plin, buton pastilă | ref4, col. 1 | S1-hero | Hero fără farfurii la colțuri, diferit de Email 1 |
| „The Classic”: titlu mare + subtitlu „With ...”, mâncare decupată care iese din bandă | ref4, col. 2 | S2, fiecare pereche (titlu rețetă + „Cu {produs}”) | Exact structura cerută: rețeta și produsul ei, în același bloc |
| Packshot mare cu elemente de mâncare în jur | ref4, col. 3 | S2, partea de produs a fiecărei perechi | Produsul real, mare, lângă rețetă. Elementele din jur sunt decupaje separate (din fotografiile Higgsfield), puse peste fundal, nu peste ambalaj |
| Tăieturi diagonale și ondulate între blocuri | ref4 | separarea celor 3 perechi | Ritm vizual fără carduri; înlocuiește valurile mari din Email 1 cu altă formă |
| Celule de tabel pe fundal închis | ref4, col. 1 (Ingredients) | rândul de info din S2: moment · timp · produs | Nu avem ingrediente; celulele merg pentru cele 3 informații publicate. Pe negru, text doar portocaliu |
| Bloc text centrat, scurt, cu buton | ref3 | S3 „Cum au ieșit?” | Bloc mic, liniștit, după perechi |
| Bandă îngustă de culoare | ref3 („Eat. Recycle. Repeat.”) | S4 transport | Un rând, nu o secțiune întreagă |

**Restricții pentru packshot-uri:** sunt JPG-uri 900 x 900 cu fundal alb (deschis), din site. Nu se decupează, nu se recolorează, nu se pun umbre pe ele. UI le așază pe o zonă albă (panou, cerc sau pastilă albă) peste culoarea de brand. Text alb nicăieri pe portocaliu, roz sau turcoaz; pe negru, doar text portocaliu (deci blocurile negre rămân cu text scurt).

---

## 1. Obiectiv, KPI, trimitere

**Obiectiv:** clientul care a încercat primul mix descoperă al doilea produs printr-o rețetă și comandă din nou. Secundar: ține promisiunea din Email 1 și strânge recenzii sau feedback.

**KPI principal:** rata de click unic pe oricare link din S2 (cele 3 rețete și cele 3 produse, plus „Toate rețetele”), raportată la emailurile livrate. Țintă 5%+, alertă sub 2%. Mai jos decât la Email 1 (8%): al doilea email din flux are mai puțină noutate, iar linkurile sunt de cross-sell, nu despre produsul deja cumpărat.

**KPI secundar:** rata de a doua comandă în 14 zile de la trimitere, atribuită pe `utm_campaign=new_customer_02`. Ținta se fixează după prima lună de date (baseline); ca reper de pornire propunem 3% [propunere, nu benchmark verificat]. Dacă theMarketer permite grup de control [neverificat], 10% din segment nu primește emailul și comparăm.

**KPI terțiar:** rata de click unic pe „Lasă o recenzie” (S3), țintă 2%+, alertă sub 0,5%; numărul de recenzii publicate și de reply-uri în 14 zile (raport manual, nu țintă).

**Trigger și timing:**
- **Recomandat:** statusul comenzii „Livrat” + 5 zile, fereastra 09:00-20:00, ora României. Dacă momentul cade în afara ferestrei, emailul așteaptă până la 09:00.
- **De ce 5 zile:** clientul a avut timp să facă mixul cel puțin o dată (inclusiv un weekend, momentul de consum din site: mic dejun, weekend, familie), dar comanda e încă proaspătă în memorie. E și intervalul propus în secțiunea 5 din Email 1 (4-5 zile).
- **Variantă, dacă magazinul nu trimite statusul „Livrat” în theMarketer:** 7 zile după Email 1 (Email 1 pleacă la expediere + 2 ore, livrarea e în 24-48 de ore lucrătoare [din site, produs.html]).
- **Gardă:** minimum 3 zile între Email 1 și Email 2, oricare ar fi trigger-ul. Niciun contact nu primește două emailuri de marketing în 24 de ore (regula din Email 1).
- theMarketer permite declanșarea după statusul comenzii [verificat, vezi secțiunea 8 din Email 1]; numele exact al statusului vine din platforma magazinului (întrebarea 2 din Email 1).

**Segment:**
- Intră: contactele care au intrat în New Customer 1 (prima comandă, gama pentru acasă, temei pentru marketing), cu comanda în statusul „Livrat”.
- Exclus: comenzi anulate sau returnate; comenzi Professional / HoReCa; contacte dezabonate, suprimate sau cu plângere spam.
- **Decis (13.10.2026): cererea automată de recenzie din theMarketer NU se activează.** S3 din acest email e singura cerere de recenzie. Nota inițială, păstrată pentru context: dacă clientul activează și automatizarea de cerere de feedback (modulul de recenzii, declanșat tot după statusul comenzii), clientul ar primi două cereri de recenzie în aceeași săptămână. Recomandare: pentru prima comandă, S3 din acest email ține locul cererii de recenzie; automatizarea separată rulează doar pentru comenzile următoare. Decizia: întrebarea 2.

**Condiții de ieșire din flux:**
1. Dezabonare.
2. Hard bounce.
3. Plângere spam.
4. Comandă anulată sau returnată integral înainte de trimitere.
5. Contactul e deja în flux pentru aceeași comandă (fără dubluri; fluxul rulează o singură dată per contact, doar la prima comandă).

**A doua comandă plasată înainte de Email 2 nu scoate contactul:** emailul rămâne relevant (rețete noi, „Cum au ieșit?”). Opțional [neverificat]: la acești clienți se ascunde banda S4.

**Consimțământ:** același temei ca la Email 1 (întrebarea 6 din Email 1). Fraza din footer o adaugă utilizatorul.

**UTM:** `utm_source=email&utm_medium=postpurchase&utm_campaign=new_customer_02&utm_content=<id>`. Valori `utm_content`: `s1-hero`, `s2-reteta1`, `s2-produs1`, `s2-reteta2`, `s2-produs2`, `s2-reteta3`, `s2-produs3`, `s2-toate`, `s3-recenzie`, `s4-produse`. Reply-ul nu are UTM. Secțiunea „UTM campanie” din automatizarea theMarketer se aliniază la aceste valori [verificat că există, Email 1 secțiunea 8].

**Condiții de lansare (fără ele, emailul nu pornește):**
1. Cele 3 rețete au pagini proprii live. **Azi, pe propunerea v3, toate cardurile de pe pagina de rețete duc la `reteta.html`, adică la rețeta cu banane și nuci** (verificat în codul paginii, 12.10.2026). Un buton „Vezi rețeta” spre altă rețetă decât cea din titlu nu pleacă. Rezervă, dacă paginile nu sunt gata: butonul de rețetă devine „Vezi toate rețetele” spre pagina de rețete, iar produsul rămâne linkul principal al perechii.
2. Fiecare produs are pagina lui. Pe v3, toate produsele duc azi la același `produs.html` (șablonul Classic Pankees).
3. Linkul de recenzie (`{{REVIEW_URL}}`) e stabilit (întrebarea 2).
4. Transportul gratuit de la al 2-lea produs e confirmat; altfel S4 rămâne doar cu linkul spre produse.

Gărzi de siguranță (opresc trimiterea, nu sunt KPI): plângeri spam sub 0,10%, dezabonări sub 0,5%, hard bounce sub 1%. Rata de deschidere se citește doar orientativ (Apple MPP).

---

## 2. Subiecte și preheadere

| # | Subiect | Caractere | Preheader |
|---|---|---|---|
| A **[recomandat]** | Pizza, lava cake sau Pankees cu ciocolată? [nou] | 43 | Trei rețete noi, fiecare cu mixul ei. Și o întrebare: cum au ieșit? [nou] |
| B | Cum au ieșit? [nou] | 13 | Spune-ne în două rânduri. Plus trei rețete pentru data viitoare. [nou] |
| C | {{FIRST_NAME}}, ai poftă de altceva? [adaptat din site, „Ai poftă?”] | 20 fără nume (rezervă: „Ai poftă de altceva?”) | Trei idei noi de la Lucas Bites, între 12 și 30 de minute. [nou; timpii din site] |

De ce A: numește direct cele trei produse pe care vrem să le vindem, e apetisant și concret, nu seamănă cu subiectele din Email 1 („Mulțumim! Pofta ta e pe drum”, „ce gătești primul?”, „Comanda ta, plus 4 rețete”) și nu depinde de tag-ul de prenume. Preheaderul ține promisiunea din Email 1 fără să o facă subiectul principal. B are probabil rată mare de deschidere și de reply, dar trimite cititorul spre recenzie, nu spre KPI-ul principal.

**Atenție:** dacă se activează conținutul condiționat din S2 (produsul cumpărat e înlocuit), subiectul A poate numi un produs pe care clientul nu-l vede în email. În cazul acela se folosește C.

**Test A/B:** A contra B. Câștigătorul se alege pe **click unic pe S2 + click unic pe recenzie, raportat la livrate**, nu pe deschideri. Volumul e cel al primelor comenzi: testul rulează până la ~500 de livrări pe variantă; sub 1 punct procentual diferență, nu se declară câștigător.

**Expeditor:** Lucas Bites. **Reply-to:** aceeași adresă monitorizată ca la Email 1 (S3 cere reply).

---

## 3. Structura, de sus în jos

Lățime 600px, o coloană pe mobil. Titluri: `Akrobat, "Arial Narrow", Arial, sans-serif`, majuscule. Text: `Arial, Helvetica, sans-serif`, 16px. Pe culorile de brand text negru; pe negru, text doar portocaliu; niciodată alb pe portocaliu, roz sau turcoaz. Butoane pastilă bulletproof. Ordinea culorilor pe secțiuni o decide UI Designer (diferită de Email 1).

Lungime țintă: S1 + 3 perechi + S3 + S4 + footer, cam 4 ecrane pe mobil. Fiecare pereche are un singur paragraf scurt.

---

### S0-header

- Identic cu Email 1 și W1-W3 (logo `Logo/Logo_LucasBites.png`, centrat, 180px, export 360px).

---

### S1-hero

- **Scop:** spune în 3 secunde ce e emailul (rețete noi + produsul lor) și anunță întrebarea promisă.
- **Pattern potrivit:** ref4 col. 1, titlu foarte mare pe bloc de culoare plin, buton pastilă. Imagine opțională (IMG0, secțiunea 7).
- **Copy:**
  - Supratitlu: **idei pentru orice poftă** [din site, retete.html]
  - Titlu (H1): **AI POFTĂ DE ALTCEVA?** [adaptat din site, „Ai poftă?”]
  - Text: Salut, {{FIRST_NAME}}! Sperăm că mixurile tale au ajuns deja pe masă. Ți-am ales trei rețete noi, fiecare cu mixul ei. La final, o întrebare scurtă. [nou]
  - Rezervă fără prenume: Salut! Sperăm că mixurile tale au ajuns deja pe masă. Ți-am ales trei rețete noi, fiecare cu mixul ei. La final, o întrebare scurtă. [nou]
  - CTA (buton mare): **Vezi rețetele** → `{{SHOP_URL}}/retete` + UTM `s1-hero` [nou]
- **Ordinea pe mobil:** supratitlu, H1, text, buton, apoi IMG0 (dacă există).

---

### S2-retete-si-produse (3 perechi)

- **Linkuri (decizie utilizator 13.10.2026):** informațiile se iau din ambele site-uri. Până la lansarea v3, „Vezi rețeta” și „Vezi {produs}” duc la paginile de pe site-ul actual (URL-urile de mai jos). Atenție: paginile de rețete vechi încep cu afirmații de sănătate („100% sigure pentru sănătate”, „E-uri periculoase”); emailul nu le preia, dar cine dă click le vede. Rețeta de lava cake veche e varianta cu mascarpone și fructe, iar pizza veche e cu salam: titlurile din email rămân cele din v3. La lansarea v3, linkurile trec pe paginile noi.

- **Scop:** cererea clientului și KPI-ul principal. Fiecare pereche: rețeta (fotografie de mâncare) + produsul ei (packshot real).
- **Pattern potrivit:** ref4 col. 2 („The Classic” + „With ...”) pentru titlu; ref4 col. 3 pentru packshot; tăieturi diagonale sau ondulate între perechi; rând de info în celule (ref4, tabelul de ingrediente).
- **Copy antet:**
  - Titlu (H2): **ÎNCEARCĂ ȘI ASTA.** [nou]
  - Text: Fiecare rețetă îți spune ce produs folosește. [din site, retete.html]

**Structura unei perechi (aceeași la toate 3):**
1. Etichetă mică (momentul de pe site)
2. Titlul rețetei (H3, mare)
3. Rând „Cu {produs}” (subtitlul în stil „With ...” din ref4)
4. Rând de info în celule: moment · timp
5. IMG rețetă (Higgsfield) + packshot (din `packshots/`)
6. Un rând despre produs
7. CTA principal: **Vezi rețeta** (buton); CTA secundar: **Vezi {produs}** (link text subliniat)

| | Pereche 1 | Pereche 2 | Pereche 3 |
|---|---|---|---|
| Etichetă | **pentru pofta de dulce** [din site, produs.html, eticheta rețetei] | **movie night** [din site, homepage, „Pentru fiecare poftă există un moment”] | **movie night** [din site, idem] |
| Titlu rețetă [din site, retete.html] | **PANKEES CU CIOCOLATĂ** | **PIZZA DE CASĂ CU PEPPERONI** | **LAVA CAKE CU ÎNGHEȚATĂ DE VANILIE** |
| Rând „Cu ...” [din site] | Cu Chocolate Chips Pankees | Cu Pizza Crust Mix | Cu Lava Cake Mix |
| Celule info [din site, retete.html] | Desert · 15 min | Familie · 30 min | Desert · 12 min |
| Rând produs | Tu adaugi apă, agiți și gătești. Copiii pot agita singuri sticla. [adaptat din site: „Tu adaugi apă, agiți și gătești” + momentul „După școală”, unde Chocolate Chips Pankees e recomandat] | Pizza de casă la începutul filmului. Pentru blat adaugi doar apă și ulei. [din site, momentul „Movie night” + „apă și ulei la pizza”] | Lava cake caldă la final. Tu adaugi ouăle și untul, restul e deja în mix. [adaptat din site: „lava cake caldă la final”, „ouă și unt la lava cake”] |
| Ce-ți trebuie [din site actual, adaptat, decizie utilizator 13.10.2026] | 1 sticlă Chocolate Chips Pankees, apă până la semnul de pe sticlă, cremă de ciocolată, câteva căpșuni. (site actual: rețeta folosește Classic/Buttermilk + Nutella; păstrăm produsul din v3 și scriem generic „cremă de ciocolată”, fără marca altcuiva) | 1 pachet Pizza Crust Mix, 260 g apă călduță, 25 g ulei de măsline, 200 g pastă de roșii, 200 g mozzarella, pepperoni. (site actual: /pizza-salami/, cu salam; titlul v3 cere pepperoni) | 1 pachet Lava Cake Mix, 3 ouă, 250 g unt topit, înghețată de vanilie. (cantitățile de pe pagina produsului; rețeta veche cu mascarpone are 250 g vs 100 g unt, contradictoriu) |
| Packshot | `packshots/pr-choco.jpg` | `packshots/pr-pizza.jpg` | `packshots/pr-lava.jpg` |
| IMG rețetă | IMG1 `img1-ciocolata.png` | IMG2 `img2-pizza-felie.png` | IMG3 `img3-lava-vanilie.png` |
| CTA principal | **Vezi rețeta** → `https://www.lucasbites.ro/reteta-pankees-cu-ciocolata/` + UTM `s2-reteta1` | **Vezi rețeta** → `https://www.lucasbites.ro/pizza-salami/` + UTM `s2-reteta2` | **Vezi rețeta** → `https://www.lucasbites.ro/reteta-de-lava-cake-cu-mascarpone-si-fructe-folosind-lava-cake-mix-de-la-lucas-bites/` + UTM `s2-reteta3` |
| CTA secundar | **Vezi Chocolate Chips Pankees** → `https://www.lucasbites.ro/produs/chocolate-chips-pankees/` + UTM `s2-produs1` | **Vezi Pizza Crust Mix** → `https://www.lucasbites.ro/produs/pizza-crust-mix-500g/` + UTM `s2-produs2` | **Vezi Lava Cake Mix** → `https://www.lucasbites.ro/produs/lava-cake-400g/` + UTM `s2-produs3` |

- **De ce ordinea asta:** primul mix cumpărat e probabil un Pankees (Classic și Buttermilk au cele mai multe recenzii pe site), deci perechea 1 rămâne în categoria cunoscută, cu altă aromă. Perechile 2 și 3 deschid categorii noi (pizza, prăjituri) și sunt legate de același moment de pe site („Movie night: Pizza de casă la începutul filmului, lava cake caldă la final.”), deci se citesc ca o seară întreagă, nu ca două reclame.
- **De ce aceste 3 rețete:** niciuna nu a fost în Email 1 (acolo: banane și nuci, afine și sirop, teancul de duminică, clătite pentru toată familia), acoperă 3 categorii (pancakes, pizza, desert) și au produse diferite de cele din Email 1.
- **Clătitele:** singura rețetă de clătite de pe v3 („Clătite pentru toată familia”) a fost deja card în Email 1. O ținem pe primul loc în rezerve, nu în setul implicit.
- **Rândurile de produs** sunt doar din site sau din discovery; nu descriu gustul și nu promit nimic despre produs. „Lava cake caldă”, „Pizza de casă” sunt formulările momentului de pe homepage.
- **Ce nu scriem:** „rețetă animată” la lava cake (întrebarea 6), descrieri de gust, pași. Ingredientele apar doar ca rând scurt „Ce-ți trebuie”.
- **Sub cele 3 perechi:** link-buton **Toate rețetele** → `{{SHOP_URL}}/retete` + UTM `s2-toate` [din site, „Toate rețetele →”]
- **Pașii nu sunt în email** (doar rândul „Ce-ți trebuie”), deci nimic din S2 nu e text lung; titlurile, rândurile și butoanele sunt text HTML live (lizibile cu imaginile blocate).

**„Pankees proteice cu iaurt grecesc”: nu o folosim (confirmat 13.10.2026).** Titlul spune „proteice”, iar pe pagina de produs v3 (`produs.html`) rețeta e etichetată „Mic dejun bogat în proteine”. „Bogat în proteine” e o mențiune nutrițională reglementată (Regulamentul CE 1924/2006, anexa: cel puțin 20% din valoarea energetică din proteine). Pentru mixul Classic Pankees, tabelul de pe aceeași pagină dă 12,7 g proteine și 345 kcal la 100 g, adică aproximativ 15% din energie din proteine (calcul orientativ, pe mix uscat, fără iaurt). Chiar și cu o formulare neutră, titlul rețetei ar rămâne pe link. Discovery 8 interzice promisiunile nutriționale; o lăsăm deoparte și semnalăm eticheta de pe site clientului (întrebarea 7).

**Rezerve (conținut condiționat, opțional) [neverificat]:** dacă theMarketer permite ascunderea unui bloc după produsele din comanda care a declanșat fluxul, perechea cu produsul deja cumpărat se înlocuiește cu prima rezervă disponibilă din lista de mai jos (fără dubluri). Fără conținut condiționat, toți primesc setul implicit; cine a cumpărat deja unul dintre cele 3 produse vede o rețetă nouă pentru el, ceea ce rămâne util.

| Ordine | Titlu rețetă [din site] | Rând „Cu ...” | Celule info | Etichetă | Rând produs | Packshot |
|---|---|---|---|---|---|---|
| R1 | CLĂTITE PENTRU TOATĂ FAMILIA | Cu Crêpes Traditional | Familie · 10 min | **duminica fără grabă** [din site, moment] | Clătite subțiri, cât timp se face cafeaua. [adaptat din site, „Duminica fără grabă”] | `pr-crepes.jpg` |
| R2 | BROWNIE CU FRUCTE DE PĂDURE | Cu Brownie Mix | Desert · 35 min | **pauza de la birou** [din site, moment] | Un brownie făcut acasă, adus pentru colegi la cafeaua de la 11. [adaptat din site] | `pr-brownie.jpg` |
| R3 | COOKIES CU CIOCOLATĂ NEAGRĂ | Cu Cookie Mix Dark Chocolate | Desert · 14 min | **gustarea de după școală** [din site, moment] | Tu adaugi doar ce scrie pe ambalaj. Restul e deja în mix. [adaptat din site] | `pr-cookie450.jpg` |

- R1 a fost card în Email 1; folosim altă fotografie și altă etichetă.
- **Rotație sezonieră (opțional, întrebarea 8):** 1 noiembrie-31 decembrie, perechea 1 poate deveni **GINGERBREAD PANCAKES** · Cu Classic Pankees · Desert · 15 min · etichetă **aroma Sărbătorilor de iarnă** [din site, produs.html] · `pr-classic-front.jpg`. În perioadele de post (de exemplu postul Crăciunului, din 15 noiembrie), o pereche poate deveni **PANKEES DE POST CU FRUCTE** · Cu Vegan Classic Pankees · De post · 15 min · `pr-vegan.jpg`. Ambele au tot doar titlu, produs, timp, moment pe v3.
- **Ramificare după Email 1 (opțional) [neverificat: tag la click]:** cine a dat click pe o rețetă de pizza sau prăjituri în Email 1 vede perechea din aceeași categorie pe primul loc.

---

### S3-cum-au-iesit

- **Scop:** ține promisiunea din Email 1; recenzie de la cine e mulțumit, reply de la cine a avut o problemă.
- **Pattern potrivit:** ref3, bloc text centrat, scurt, cu buton. Fără fotografie.
- **Copy:**
  - Titlu (H2): **CUM AU IEȘIT?** [nou; promis în Email 1, S6]
  - Text: Ți-am promis că te întrebăm. Le-ai încercat deja? Spune-ne cum ți-au ieșit și adaugă o poză. [prima frază nou; restul din site, homepage]
  - CTA (buton): **Lasă o recenzie** → `{{REVIEW_URL}}` + UTM `s3-recenzie` [din site, „Lasă o recenzie →”]
  - Text mic: Ceva n-a ieșit cum voiai? Dă reply la emailul ăsta și te ajutăm. [nou]
- **`{{REVIEW_URL}}`:** fie formularul modulului de recenzii theMarketer (dacă clientul îl folosește), fie pagina produsului cumpărat, secțiunea de recenzii (pe v3, „Lasă o recenzie” duce la `produs.html#recenzii`). Decizia: întrebarea 2. Dacă linkul e per produs, are nevoie de variabila produsului din comandă [neverificat, întrebarea 1 din Email 1]; rezerva e pagina generală de produse.
- **Opțional [neverificat]:** cine a lăsat deja o recenzie după prima comandă nu vede butonul; vede doar textul mic.
- **Imagine:** nu.

---

### S4-al-doilea-produs (bandă îngustă)

- **Scop:** un motiv concret pentru a doua comandă, fără reducere.
- **Pattern potrivit:** bandă de culoare de un rând (ref3).
- **Copy:**
  - Text: **Transport gratuit de la al 2-lea produs pentru acasă.** [din site] [de confirmat la lansare]
  - Link text (subliniat): **Vezi toate produsele** → `{{SHOP_URL}}/produse` + UTM `s4-produse` [din site, „Toate produsele”]
  - Semnătură (Akrobat): **eat what you love** [din site, slogan oficial]
  - Sub semnătură: Familia Lucas Bites [ca în Email 1]
- **Dacă transportul gratuit nu se confirmă:** rămân doar linkul, semnătura și rândul de sub ea.
- **Imagine:** nu.

---

## 4. Footer (S7-footer)

Identic cu Email 1, secțiunea 4 (și cu W1-W3). Nu se modifică nimic fără decizia clientului.

- **Fundal:** alb, separat de secțiunea de deasupra printr-o linie neagră subțire.
- **Logo:** `Logo/Logo_LucasBites_stripes-nobg.png`, centrat, 200px lățime.
- **Iconițe social** (negre, 32px, assets UI): Instagram, TikTok, Facebook, YouTube, cu aceleași linkuri ca în Email 1.
- **Copy:**

> [ADAUGĂ UTILIZATORUL]
>
> Lucas Bites · Roșu, Chiajna, Ilfov
> office@lucasbites.ro · +40 731 399 399
>
> Nu mai vrei emailuri de la noi? [Dezabonează-te aici]({{UNSUBSCRIBE_URL}}). Durează un click.
>
> © 2026 Lucas Bites

- **Fraza de consimțământ:** NU e scrisă aici. O adaugă utilizatorul în theMarketer (decizia 5 din brief). În HTML rămâne un comentariu marker `[ADAUGĂ UTILIZATORUL]`, pe aceeași poziție ca în Email 1.
- **Tehnic:** `{{UNSUBSCRIBE_URL}}` se înlocuiește cu tag-ul de dezabonare din theMarketer [neverificat: sintaxa]. Header-ele `List-Unsubscribe` + `List-Unsubscribe-Post` (one-click, RFC 8058) trebuie să fie active.
- **De confirmat (ca la Email 1):** denumirea juridică a firmei (SRL) și CUI.

---

## 5. Predarea către Email 3 (și mai departe)

- **Email 3 (reaprovizionare):** template-ul theMarketer „Reamintește clienților să recomande” din secțiunea „Post Cumpărare”, cu interval de recurență pe fiecare produs [verificat în Email 1, secțiunea 8]. Intervalul îl dă clientul (întrebarea 12 din Email 1). Conținut: produsul cumpărat, înapoi pe masă, plus o rețetă nouă cu același produs (din cele nefolosite: Gingerbread Pancakes, Pankees de post cu fructe, Brownie, Cookies).
- **Ce ia Email 3 din Email 2:**
  - categoria pe care s-a dat click în S2 (tag la click [neverificat]) decide rețeta și produsul din Email 3;
  - reply-urile din S3 cu probleme se rezolvă manual înainte de Email 3; acele contacte pot fi puse pe pauză [neverificat: excludere manuală din automatizare];
  - recenziile cu poză primite (doar cu acordul autorului, ca în Email 1 S5) pot deveni dovada socială din Email 3.
- **Ieșire din fluxul de vânzare:** a doua comandă oprește emailurile de cross-sell rămase; reaprovizionarea pornește după produsul cumpărat.
- **Ce NU repetăm în Email 3:** titlurile, subiectele, perechile și fotografiile din Email 1 și Email 2.

---

## 6. Alt text

| Imagine | Alt text |
|---|---|
| Logo header | Lucas Bites |
| IMG0 (hero, opțional) | `alt=""` (decorativ, bucăți de ingrediente) |
| IMG1 | Pankees cu ciocolată |
| Packshot pereche 1 (`pr-choco.jpg`) | Sticlă Chocolate Chips Pankees |
| IMG2 | Felie de pizza de casă cu pepperoni |
| Packshot pereche 2 (`pr-pizza.jpg`) | Cutie Pizza Crust Mix |
| IMG3 | Lava cake cu înghețată de vanilie |
| Packshot pereche 3 (`pr-lava.jpg`) | Pungă Lava Cake Mix |
| Rezerve R1-R3 (doar dacă se folosesc) | Clătite pentru toată familia / Brownie cu fructe de pădure / Cookies cu ciocolată neagră; packshot: Sticlă Crêpes Traditional / Brownie Mix / Cookie Mix Dark Chocolate |
| Logo footer | Lucas Bites, eat what you love |
| Iconițe social | Instagram / TikTok / Facebook / YouTube (câte una pe iconiță) |
| Tăieturi diagonale, valuri, forme decorative | `alt=""` |

---

## 7. Imagini: ce se generează (Higgsfield) și ce vine din `packshots/`

**Packshot-uri (nu se generează, nu se modifică):**

| Unde | Fișier | Ce e |
|---|---|---|
| S2 pereche 1 | `packshots/pr-choco.jpg` | sticla Pankees Chocolate Chips |
| S2 pereche 2 | `packshots/pr-pizza.jpg` | cutia Pizza Crust Mix 500 g |
| S2 pereche 3 | `packshots/pr-lava.jpg` | punga Lava Cake Mix |
| Rezerve / sezon | `pr-crepes.jpg`, `pr-brownie.jpg`, `pr-cookie450.jpg`, `pr-classic-front.jpg`, `pr-vegan.jpg` | doar dacă se activează rezervele sau rotația |
| Nefolosite aici | `pr-blueberry.jpg`, `pr-buttermilk.jpg` | produsele din rețetele Email 1 |

**Fotografii de mâncare (Higgsfield):** le generează utilizatorul pe higgsfield.ai din `image-prompts.md` (GPT Image, High, 2K, **fundal alb simplu**, niciodată „transparent background”), în `new-customer-02/images/`. Doar mâncare: fără ambalaje, sticle, pungi sau cutii, fără text, fără fețe; mâinile sunt permise. Imaginile arată rezultatul după titlul rețetei, nu pași.

| Fișier | Raport | Folosire | Ce arată |
|---|---|---|---|
| img1-ciocolata.png | 1:1 | S2 pereche 1, decupaj care iese din bandă | La nivelul ochilor (eye-level, frontal): teanc scurt de 3 pancakes cu bucăți de ciocolată vizibile în aluat și pe margine, câteva bucăți de ciocolată căzute lângă farfurie, un fir subțire de sos de ciocolată. Fundal alb simplu. |
| img2-pizza-felie.png | 4:5 | S2 pereche 2, decupaj vertical | O felie de pizza cu pepperoni ridicată de o mână din pizza (doar mâna și încheietura), mozzarella întinsă între felie și restul pizzei, margine aurie. Fundal alb simplu. |
| img3-lava-vanilie.png | 1:1 | S2 pereche 3, decupaj | Lateral, 20°: lava cake întreg (nerupt) pe farfurie, o cupă de înghețată de vanilie pusă deasupra care începe să se topească pe laterale, puțină pudră de cacao. Fundal alb simplu. |
| img0-hero-ingrediente.png | 1:1 | S1, opțional, „ingrediente care zboară” (ref4 col. 3) | Elemente separate, fără farfurie, cu spațiu între ele pentru decupaj: 6-8 bucăți de ciocolată, 3 felii de pepperoni, o cupă mică de înghețată de vanilie. Fundal alb simplu. |

- **Diferențe obligatorii** față de Email 1 (farfurii de sus la colțuri, banane și nuci, afine, teanc de sus cu unt, platou de clătite) și W1-W3 (lava cake rupt și pizza întreagă margherita de sus în W2; felii de pizza cu legume, stack cu felie scoasă și farfurii negre în W3; stack înalt cu afine la 45° în W1). De aici: pizza ca felie ridicată, lava cake întreg cu înghețata deasupra, pancakes frontal, teanc scurt.
- **Recuzită:** aceeași farfurie rotundă din ceramică deschisă la culoare ca în Email 1 (continuitate de familie), unde e farfurie.
- **Rezerve (doar dacă se confirmă conținutul condiționat):** img4-clatite-v2 (altă compoziție decât platoul din Email 1), img5-brownie, img6-cookies; sezon: img7-gingerbread, img8-post-fructe. Nu se generează acum.
- **Minim pentru lansare:** img1-img3. IMG0 doar dacă UI îl folosește.
- **Greutate:** exporturi la 2x față de afișare; fiecare imagine sub 200 KB, packshot-urile redimensionate la lățimea de afișare x2; total imagini sub 1,2 MB; HTML sub 102 KB.

---

## 8. Ce am verificat și ce nu

**Site Lucas Bites, propunerea v3 (citit la 12.10.2026, din codul paginilor):**

| Ce | URL | Rezultat |
|---|---|---|
| Lista de rețete | https://lucasbites.ro/propunere-v3/retete.html | Aceleași 12 rețete ca în brief, cu titlu, produs, timp, moment. Marcate „animată”: banane și nuci, afine și sirop, lava cake. **Toate cardurile au `href="reteta.html"`.** Fără ingrediente sau pași pentru cele 11 rețete în afară de banane și nuci. |
| Rețeta completă | https://lucasbites.ro/propunere-v3/reteta.html | Neschimbată față de Email 1 (banane și nuci, „[timp]” încă gol). Are blocul „Folosit în rețetă: Classic Pankees · Adaugă în coș”. Nu o folosim în Email 2. |
| Pagina de produs | https://lucasbites.ro/propunere-v3/produs.html | Șablon Classic Pankees. Etichetele rețetelor: „Pentru pofta de dulce” (Pankees cu ciocolată), „Mic dejun bogat în proteine” (Pankees proteice), „Aroma Sărbătorilor de iarnă” (Gingerbread). Valori nutriționale Classic Pankees: 345 kcal, 12,7 g proteine la 100 g. Livrare în 24-48 de ore lucrătoare. |
| Lista de produse | https://lucasbites.ro/propunere-v3/produse.html | Numele exacte folosite: Chocolate Chips Pankees, Pizza Crust Mix, Lava Cake Mix, Crêpes Traditional, Brownie Mix, Cookie Mix Dark Chocolate, Classic Pankees, Vegan Classic Pankees. Toate produsele duc la același `produs.html`. Pe v3 există și „Crêpes Traditional” (280 g) și „Crêpes Mix Original” (450 g) ca produse separate. |
| Homepage | https://lucasbites.ro/propunere-v3/ | Momentele „Movie night” („Pizza de casă la începutul filmului, lava cake caldă la final.”), „Gustarea de după școală”, „Duminica fără grabă”, „Pauza de la birou”; „Ce e în mix” (apă la pancakes, apă și ulei la pizza, ouă și unt la lava cake); blocul „Le-ai încercat deja? Spune-ne cum ți-au ieșit și adaugă o poză. Lasă o recenzie →” cu link `produs.html#recenzii`. |
| Transport gratuit | header-ul tuturor paginilor v3 | „Transport gratuit de la al 2-lea produs pentru acasă”. Valabilitatea la lansare: [de confirmat]. |
| Packshot-uri | `new-customer-02/packshots/` | 10 fișiere JPG 900 x 900, fundal alb. Verificate vizual: pr-choco (sticlă Chocolate Chips), pr-lava (pungă Lava Cake Mix), pr-pizza (cutie Pizza Crust Mix 500 g), pr-crepes (sticlă Crêpes Traditional). |

**theMarketer:** nicio verificare nouă față de Email 1 (secțiunea 8 de acolo). Rămân **neverificate**: variabilele produselor din comanda care a declanșat fluxul, conținutul condiționat (ascunderea perechii cu produsul cumpărat, ascunderea butonului de recenzie), tag la click, grupul de control, sintaxa prenumelui și a linkului de dezabonare. Verificat (din Email 1): trigger după statusul comenzii, modulul de recenzii cu automatizare de cerere de feedback, secțiunea „UTM campanie”, template-ul de reaprovizionare.

**Placeholdere generice folosite (nu sunt sintaxă theMarketer):** `{{FIRST_NAME}}`, `{{SHOP_URL}}`, `https://www.lucasbites.ro/reteta-pankees-cu-ciocolata/`, `https://www.lucasbites.ro/pizza-salami/`, `https://www.lucasbites.ro/reteta-de-lava-cake-cu-mascarpone-si-fructe-folosind-lava-cake-mix-de-la-lucas-bites/`, `https://www.lucasbites.ro/produs/chocolate-chips-pankees/`, `https://www.lucasbites.ro/produs/pizza-crust-mix-500g/`, `https://www.lucasbites.ro/produs/lava-cake-400g/`, `{{REVIEW_URL}}`, `{{UNSUBSCRIBE_URL}}` (plus URL-urile rezervelor, dacă se folosesc).

---

## 9. Întrebări pentru client (și de verificat în theMarketer)

1. **Paginile de rețetă și de produs:** la lansare, „Pankees cu ciocolată”, „Pizza de casă cu pepperoni” și „Lava cake cu înghețată de vanilie” au pagini proprii, cu ingrediente și pași? Dar Chocolate Chips Pankees, Pizza Crust Mix și Lava Cake Mix au pagini de produs proprii? Care sunt URL-urile? Azi, pe v3, toate rețetele duc la rețeta cu banane și nuci, iar toate produsele la Classic Pankees.
2. **Recenzii:** folosiți modulul de recenzii theMarketer cu automatizarea lui de cerere de feedback? Dacă da, propunem ca pentru prima comandă S3 din acest email să țină locul cererii automate (ca să nu primească clientul două cereri într-o săptămână). Unde duce „Lasă o recenzie”: formularul theMarketer sau secțiunea de recenzii de pe pagina produsului?
3. **Transport gratuit de la al 2-lea produs:** rămâne valabil la lansare? Se aplică la două bucăți din același produs sau doar la produse diferite?
4. **Statusul „Livrat”:** magazinul îl trimite în theMarketer? (aceeași întrebare ca 2 din Email 1; fără el, Email 2 pleacă la 7 zile după Email 1).
5. **Conținut condiționat:** se poate ascunde un bloc după produsele din comanda care a declanșat fluxul? De asta depind rezervele din S2 și subiectul recomandat.
6. **Lava cake animată:** pe pagina de rețete lava cake e marcată „animată”. Animația există la lansare? Dacă da, o putem spune în email („rețetă animată”), e un motiv în plus de click.
7. **„Pankees proteice cu iaurt grecesc”:** pe pagina de produs v3 e etichetată „Mic dejun bogat în proteine”. „Bogat în proteine” e mențiune nutrițională reglementată (Reg. CE 1924/2006) și, după calculul nostru orientativ pe valorile Classic Pankees, mixul nu pare să îndeplinească pragul. Recomandăm verificarea cu juristul și schimbarea etichetei și a titlului (de exemplu, după ingredientul principal). Până atunci, nu o folosim în emailuri.
8. **Rotație sezonieră:** vreți ca, în noiembrie-decembrie, perechea 1 să devină Gingerbread Pancakes, iar în perioadele de post să apară Pankees de post cu fructe (Vegan Classic Pankees)?
9. **Reply-uri:** cine răspunde la reply-urile din S3 și în cât timp? Textul promite „te ajutăm”; un răspuns în 1-2 zile lucrătoare e minimul ca promisiunea să fie adevărată.
