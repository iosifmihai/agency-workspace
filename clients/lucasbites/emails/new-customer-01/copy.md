# Lucas Bites: New Customer, Email 1, strategie, structură și copy final

Surse: `brief.md` (acest folder, decizii finale din 12.10.2026), `discovery.md` (inclusiv 8b), `welcome-01/copy.md`, `welcome-03/copy.md`, `refs/ref3.png`, paginile de site citite la 12.10.2026 (lista din secțiunea 8). Legendă: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [adaptat] = text aprobat ajustat pentru email, [nou] = text nou, de aprobat de client, [din site actual] = text de pe site-ul WordPress actual (lucasbites.ro), [neverificat] = funcție theMarketer pe care n-am găsit-o în documentația oficială.

**Ce cere clientul:** mulțumire pentru comandă, rețete, entuziasm pentru produsele comandate.

**Ce fel de email e:** primul email de marketing după **prima** comandă. Nu e confirmarea comenzii (aceea e tranzacțională și o trimite magazinul). Fără prețuri, fără coduri de reducere, fără vânzare agresivă: clientul tocmai a plătit.

**Rețetele sunt ale brandului**, citite de pe site, nu trimise de clienți. Rețetele clienților vin abia de acum înainte, prin invitația din S5.

---

## Ce am adăugat față de structura cerută și de ce

Structura cerută: mulțumire, rețete, entuziasm pentru produse. Am adăugat:

- **S3 „Pe lista de cumpărături”: ce adaugi tu la fiecare mix.** Clientul are coletul pe drum; dacă știe dinainte că la lava cake îi trebuie 3 ouă și unt, îl face în seara în care ajunge, nu „cândva”. Primul produs folosit repede e cel mai sigur drum spre a doua comandă.
- **S5 „Trimite-ne rețeta ta”.** Cerința din brief (rețetele clienților în viitor) are nevoie de un canal: reply, Instagram, hashtag. Aici pornește materialul pentru emailurile următoare.
- **S6 „Ce urmează”, cu contact pentru comandă.** Anunță Email 2 („te întrebăm cum au ieșit”), pune la îndemână telefonul și emailul pentru orice problemă cu comanda și are un singur link discret spre toată gama. Atât cross-sell, nu mai mult: vânzarea propriu-zisă vine în Email 2, după ce clientul a gustat.
- **Ce NU am adăugat:** grila de produse recomandate. theMarketer o are (vezi secțiunea 8), dar documentația nu confirmă că prețul se poate ascunde din bloc, iar regula din brief e „fără prețuri”. O mutăm în Email 2.

---

## Ce preluăm din ref3 și unde (UI Designer decide final)

Layout-ul, culorile pe secțiuni și pattern-urile le alege UI Designer. Mai jos, doar ce pattern din ref3 se potrivește cu fiecare secțiune, ca punct de plecare. Bleumarinul din ref3 devine una dintre cele 4 culori de brand, serif-ul devine Akrobat.

| Pattern din ref3 | Potrivit pentru | De ce | Deja folosit în welcome? |
|---|---|---|---|
| Farfurii fotografiate de sus care ies din cadru, pe marginile hero-ului | S1-hero | Spune „masa ta, în curând” fără ambalaj inventat | Nu (W1 stack decupat, W2 lava cake, W3 grid 2 x 2 de farfurii întregi) |
| Tranziții curbe mari între secțiuni | toate | Continuitate cu familia vizuală (valurile din W1-W3) | Da, ca familie; UI poate varia amplitudinea |
| Listă de carduri albe cu imagine circulară + titlu + text + buton mic | S2-produse comandate sau S4-carduri rețete | Format clar pentru 1-4 elemente dinamice | Cercuri în W1 (3 carduri pe un rând), nu ca listă verticală |
| Zig-zag farfurie + etichetă-bandă („Chef Favorites”) | S4-rețete (eticheta = numele produsului sau „Rețeta săptămânii”) | Eticheta-bandă e locul natural pentru „Cu Blueberry Pankees” | Zig-zag în W2 (categorii); UI decide dacă e prea aproape |
| Grid 2 x 2 de carduri | variante pe categorie în S4 | Doar dacă UI nu-l consideră prea aproape de W3 | Da, W3 S2 |
| Bloc „Don't just take our word for it” cu stele | nu îl folosim aici | Recenziile au fost în W1 și W3; clientul a cumpărat deja | - |
| Poză lifestyle cu cutia de livrare | nu o folosim | Nu avem fotografie de ambalaj; brief-ul interzice ambalaje inventate | - |

---

## 1. Obiectiv, KPI, trimitere

**Obiectiv:** clientul folosește mixul repede după livrare și se simte bine cu alegerea făcută. Concret: dă click pe o rețetă (o deschide ca s-o facă) și, pe termen mai lung, revine la a doua comandă.

**KPI principal:** rata de click unic pe oricare link de rețetă (S1 CTA, rețeta din S4, cele 3 carduri din S4), raportată la emailurile livrate. Țintă 8%+, alertă sub 3%. Emailurile post-achiziție au de obicei atenție mai mare decât un newsletter, de aici ținta mai sus decât la W3 (6%).

**KPI secundar:** rata de a doua comandă în 60 de zile de la prima, la contactele care au primit emailul. Dacă theMarketer permite un grup de control (5-10% din cumpărători care nu primesc emailul), comparăm cu el; dacă nu, raportăm doar tendința lunară [neverificat: grup de control în automatizări].

**KPI terțiar:** rata de click unic pe „Trimite-ne rețeta” + Instagram din S5 (țintă 1%+, alertă sub 0,3%) și numărul de rețete primite pe reply sau cu #lucasbites în 30 de zile (raport manual, nu țintă).

**Trigger și timing:**
- **Recomandat:** la schimbarea statusului comenzii în „Expediată” (sau termenul echivalent din platforma magazinului), cu întârziere de 2 ore și fereastră de livrare 09:00-20:00, ora României. Dacă cele 2 ore cad în afara ferestrei, emailul așteaptă până la 09:00.
- **De ce așa:** confirmarea tranzacțională pleacă la plasarea comenzii; un email de marketing în același minut concurează cu ea și pare spam. După expediere, clientul așteaptă coletul: e momentul de entuziasm cerut de client, iar rețetele și lista de cumpărături (S3) ajung înainte de colet sau în aceeași zi.
- **Variantă, dacă magazinul nu trimite statusul „Expediată” în theMarketer:** 24 de ore după plasarea comenzii, aceeași fereastră 09:00-20:00.
- theMarketer permite declanșarea unei automatizări după statusul comenzii (exemplul din documentație e statusul „Livrat”) [verificat, vezi secțiunea 8]. Numele exact al statusurilor vine din platforma magazinului (întrebarea 2).
- **Copy-ul e scris neutru față de livrare** („pofta e pe drum”, „când ajunge”), ca să rămână corect și dacă livrarea e foarte rapidă.

**Segment:**
- Intră: contacte cu **prima comandă** plasată pe site-ul propriu, pentru acasă, care au temei pentru emailuri de marketing (vezi „Consimțământ” mai jos). Filtrul „prima comandă” [neverificat] ca filtru direct în theMarketer; documentația confirmă doar filtrul „Statut cumpărător” > „Cumpărător în ultimele X zile” (vezi secțiunea 8). Întrebarea 3.
- Exclus: comenzile anulate sau returnate înainte de trimitere; comenzile din gama Professional / HoReCa (1 kg și 10 kg: rețetele și tonul sunt pentru acasă) [de confirmat cum se identifică, întrebarea 9]; contacte dezabonate sau suprimate.
- **Coliziune cu seria welcome:** cine e în seria welcome și comandă sare peste W3 (regula din `welcome-03/copy.md`). New Customer 1 are prioritate; dacă un email welcome ar pleca în aceeași zi, se amână cu 24 de ore. Niciun contact nu primește două emailuri de marketing în 24 de ore.

**Condiții de ieșire din flux:** dezabonare, hard bounce, plângere spam, comandă anulată sau returnată. Fluxul rulează o singură dată per contact (doar la prima comandă).

**Consimțământ:** emailul e de marketing, deci pleacă doar la cumpărătorii care s-au abonat (bifă la checkout sau înscriere anterioară) sau, dacă clientul vrea să folosească excepția pentru clienți existenți din Directiva ePrivacy, art. 13(2) (transpusă în legea română), doar dacă la comandă clientul a avut ocazia clară să refuze. Decizia o ia clientul, cu avizul juristului lui (întrebarea 6).

**UTM:** `utm_source=email&utm_medium=postpurchase&utm_campaign=new_customer_01&utm_content=<id>`. Valori `utm_content`: `s1-hero`, `s2-produs`, `s3-produse`, `s4-reteta-saptamanii`, `s4-card1`, `s4-card2`, `s4-card3`, `s4-toate`, `s5-reteta`, `s5-instagram`, `s6-gama`. theMarketer are o secțiune „UTM campanie” cu structură implicită pe fiecare automatizare, care se poate personaliza [verificat]; o aliniem la valorile de mai sus.

**Condiții de lansare (fără ele, emailul nu pornește):**
1. Paginile de rețetă din S4 sunt live pe site-ul nou, cu ingrediente și pași (azi, cele 3 rețete din brief au pe propunerea v3 doar nume, produs și timp; vezi secțiunea 8).
2. Blocul de produse comandate e verificat în editorul theMarketer, cu un test pe o comandă reală (inclusiv varianta fără date).
3. Temeiul de consimțământ e clarificat (întrebarea 6) și textul din footer e corect pentru cumpărători.
4. Cantitățile din S3 sunt verificate pe ambalajele actuale.

Gărzi de siguranță (opresc trimiterea, nu sunt KPI): plângeri spam sub 0,10%, dezabonări sub 0,5%, hard bounce sub 1%. Rata de deschidere se citește doar orientativ (Apple MPP).

---

## 2. Subiecte și preheadere

| # | Subiect | Caractere | Preheader |
|---|---|---|---|
| A **[recomandat]** | Mulțumim! Pofta ta e pe drum [nou] | 28 | Până ajunge comanda, alege-ți prima rețetă. Enjoy! [nou] |
| B | {{FIRST_NAME}}, ce gătești primul? [nou] | 18 fără nume (rezervă: „Ce gătești primul?”) | Rețete Lucas Bites pentru mixurile din comanda ta. [nou] |
| C | Comanda ta, plus 4 rețete de încercat [nou] | 37 | Ce adaugi tu, ce faci primul și cum ne arăți rezultatul. [nou] |

De ce A: face exact ce a cerut clientul în primele cuvinte (mulțumire + entuziasm), e scurt, se citește întreg pe mobil și se distinge clar de subiectul confirmării de comandă, deci nu pare un duplicat tranzacțional. Nu depinde de tag-ul de prenume, a cărui sintaxă n-am putut-o verifica.

**Test A/B:** A contra B, doar după ce tag-ul de prenume și rezerva lui sunt verificate în theMarketer. Câștigătorul se alege pe **click unic pe linkurile de rețetă raportat la livrate**, nu pe deschideri. Volumul de prime comenzi e mai mic decât lista de abonați: testul rulează până strânge ~500 de livrări pe variantă, oricât ar dura; sub 1 punct procentual diferență, nu se declară câștigător.

**Expeditor:** Lucas Bites. **Reply-to:** aceeași adresă monitorizată ca la seria welcome (S5 cere reply cu rețete).

---

## 3. Structura, de sus în jos

Lățime 600px, o coloană pe mobil. Titluri: `Akrobat, "Arial Narrow", Arial, sans-serif`, majuscule. Text: `Arial, Helvetica, sans-serif`, 16px. Reguli de culoare din brief: pe culorile de brand text negru; pe negru, text doar portocaliu; niciodată alb pe portocaliu, roz sau turcoaz. Butoane pastilă bulletproof. Culorile pe secțiuni și ordinea lor le decide UI Designer (diferite de W1-W3).

---

### S0-header

- **Scop:** recunoaștere imediată.
- **Conținut:** identic cu W1-W3 (logo `Logo/Logo_LucasBites.png`, centrat, 180px, export 360px).
- **Imagine:** nu (doar logo).

---

### S1-hero

- **Scop:** mulțumirea, entuziasmul și un prim click spre rețete, vizibil fără scroll pe mobil.
- **Pattern ref3 potrivit:** farfurii de sus care ies din cadru pe margini, titlu mare centrat, buton pastilă.
- **Copy:**
  - Supratitlu: **mulțumim pentru comandă** [nou]
  - Titlu (H1, 2 rânduri): **POFTA E PE DRUM.** [nou]
  - Text: Salut, {{FIRST_NAME}}! Mulțumim că ai ales Lucas Bites. Mai jos găsești ce ai comandat, ce adaugi tu și primele rețete de încercat. [nou]
  - Rezervă fără prenume: Salut! Mulțumim că ai ales Lucas Bites. Mai jos găsești ce ai comandat, ce adaugi tu și primele rețete de încercat. [nou]
  - CTA (buton mare): **Alege prima rețetă** → `{{SHOP_URL}}/retete` + UTM `s1-hero` [nou]
- **Notă:** nu folosim ancoră spre S4 (ancorele nu funcționează sigur în Gmail pe mobil); butonul duce pe pagina de rețete.
- **Ordinea pe mobil:** supratitlu, H1, text, buton, apoi IMG1.
- **IMG1 (spec):** vezi secțiunea 7.

---

### S2-produse (bloc dinamic din comandă)

- **Scop:** produsele comandate, arătate apetisant, fiecare cu un rând despre cum se face. Asta e „entuziasmul pentru produsele comandate”.
- **Pattern ref3 potrivit:** lista de carduri albe cu imagine circulară + titlu + text + buton mic.
- **Copy antet:**
  - Titlu (H2): **ÎN CURÂND, PE MASA TA.** [nou]
  - Text: Ce ai pus în coș și cât de repede ajunge pe farfurie. [nou]
- **Card produs (se repetă pentru fiecare produs din comandă, maximum 4):**
  - Imagine: `{{ORDER_PRODUCT_IMAGE}}` (din feed-ul de produse theMarketer, nu se generează)
  - Nume: `{{ORDER_PRODUCT_NAME}}`
  - Rând pe categorie (conținut condiționat [neverificat], vezi tabelul de mai jos)
  - CTA (buton mic): **Cum se prepară** → `{{ORDER_PRODUCT_URL}}` + UTM `s2-produs` [nou]
- **Toate placeholderele de mai sus sunt generice, nu sintaxă theMarketer.** N-am găsit în documentația publică theMarketer variabilele pentru produsele dintr-o comandă și nici un bloc „produse comandate” (vezi secțiunea 8). Sintaxa reală se ia din editorul theMarketer sau de la suportul lor înainte de build (întrebarea 1).
- **Peste 4 produse:** se afișează primele 4; nu scriem „și încă X”, pentru că nu știm dacă numărul e disponibil ca variabilă.

**Rândul pe categorie (dacă theMarketer permite conținut condiționat după categoria produsului) [neverificat]:**

| Categoria produsului | Rând în card |
|---|---|
| Pankees (pancakes) | Adaugi apă, agiți și gătești. Gata în 5 minute. [din site] |
| Clătite (Crêpes) | Adaugi apă, amesteci cu telul și torni în tigaie. [adaptat din site actual] |
| Prăjituri (Lava Cake, Brownie) | Adaugi ouăle și untul (sau uleiul). Restul e deja în mix. [adaptat din site actual] |
| Pizza | Apă călduță și ulei de măsline. Blatul e gata de topping. [adaptat din site actual] |
| Altă categorie sau categorie lipsă | Tu adaugi doar ce scrie pe ambalaj. Restul e deja în mix. [adaptat din site] |

- **Dacă nu există conținut condiționat:** toate cardurile primesc rândul generic din ultimul rând al tabelului.
- **Rezervă când lipsesc datele de produs** (blocul gol, comandă fără produse în feed, eroare de sincronizare): cardurile dispar complet și rămâne doar antetul, cu textul înlocuit de:
  - Text: Mixurile tale sunt pe drum. Până ajung, uite ce adaugi tu și ce poți face cu ele. [nou]
  - CTA (buton mic): **Vezi toate mixurile** → `{{SHOP_URL}}/produse` + UTM `s2-produs` [din Email 2]
- **Mapare categorii:** feed-ul theMarketer trebuie să aibă categoria produsului completată la fel pe toată gama (Pankees, Clătite, Prăjituri, Pizza). De confirmat cum apar categoriile în feed (întrebarea 5).

---

### S3-lista-de-cumparaturi

- **Scop:** clientul are în casă ce îi trebuie când ajunge coletul, deci gătește imediat.
- **Pattern ref3 potrivit:** bloc simplu cu titlu centrat; rânduri text, fără fotografii (iconițele, dacă există, sunt assets UI).
- **Copy:**
  - Titlu (H2): **PE LISTA DE CUMPĂRĂTURI.** [nou]
  - Text: Ca să le faci în ziua în care ajung, verifică dacă ai în casă: [nou]
  - **Pankees:** apă, până la semnul de pe sticlă, și puțin ulei sau unt pentru tigaie. Lapte și ouă nu-ți trebuie, sunt deja în mix. [adaptat din site și din site actual]
  - **Clătite (Crêpes):** 675 ml apă și un tel. [din site actual]
  - **Pizza Crust Mix:** 260 g apă călduță și 25 g ulei de măsline. Ajunge pentru 3 pizza. [din site actual]
  - **Lava Cake Mix:** 3 ouă și 250 g unt topit. Ies 8 porții, la cuptor, la 210°C, 7-8 minute. [din site actual]
  - **Brownie Mix:** 3 ouă, 50 ml apă și 125 ml ulei sau unt topit. [din site actual]
  - Text mic: Cantitățile exacte sunt și pe ambalaj. [nou]
- **Afișare:** dacă theMarketer permite conținut condiționat după categorie [neverificat], se afișează doar rândurile categoriilor din comandă. Altfel, toate 5 rândurile (sunt scurte, merge și așa).
- **Surse:** `discovery.md` 8b, „Ce adaugi la preparare” (paginile de produs de pe site-ul actual, citite la 11.10.2026); Pankees confirmat și de propunerea v3 (rețeta de mai jos: „Toarnă 300 ml de apă în sticlă, până la semnul marcat”) și de pagina https://www.lucasbites.ro/pankees-clasice/ (citită la 12.10.2026). Mențiunea „Lapte și ouă nu-ți trebuie” vine din 8b („Nu e nevoie de lapte sau ouă: mixul conține lapte praf și praf de ou”).
- **De verificat înainte de lansare:** cantitățile pe ambalajele actuale; numele produsului de clătite (pe propunerea v3 e „Crêpes Traditional”, pe site-ul actual „Crêpes Mix Original”; cantitatea de 675 ml e de pe site-ul actual) (întrebarea 8).
- **Imagine:** nu.

---

### S4-retete

- **Scop:** rețetele brandului (cererea clientului) și KPI-ul principal.
- **Pattern ref3 potrivit:** zig-zag farfurie + etichetă-bandă pentru rețeta săptămânii; lista de carduri cu imagine circulară pentru celelalte 3.
- **Copy antet:**
  - Supratitlu: **idei de servire** [din site]
  - Titlu (H2): **CU CE LE MĂNÂNCI AZI?** [din site]
  - Text: Toppinguri, combinații și deserturi pornite dintr-un mix Lucas Bites. Fiecare rețetă îți spune ce produs folosește. [din site]

**Rețeta săptămânii (rețeta completă, singura cu ingrediente și pași publicați pe propunerea v3)**

- Etichetă-bandă: **Rețeta săptămânii** [din site]
- Titlu: **PANKEES CU BANANE ȘI NUCI CARAMELIZATE** [din site]
- Text: O porție de pancakes americane pufoase, cu banane și nuci caramelizate. Baza vine din sticla de Classic Pankees; tu adaugi doar toppingul. [din site]
- Rând info: **3 porții · 12 pancakes · 20 min · Ușor** [din site] (20 min apare pe pagina de rețete; pe pagina rețetei câmpul de timp e încă gol, „[timp]”)
- **Ingrediente** [din site]:
  - 1 sticlă Classic Pankees (sau Vegan Classic Pankees)
  - 300 ml apă
  - 2 linguri ulei vegetal
  - 50 g nuci
  - 20 g zahăr brun
  - 5 ml apă, pentru caramel
  - 0,5 banană
  - sirop de arțar, după gust
- **Pe scurt** (4 pași, condensați din cei 10 de pe https://lucasbites.ro/propunere-v3/reteta.html; varianta scurtă aprobată de utilizator la 12.10.2026, ca emailul să nu fie prea lung):
  - 1. Toarnă 300 ml de apă în sticla de Classic Pankees, până la semn, și agită bine.
  - 2. Gătește pancakes-urile în tigaia încinsă: când apar bulele, întoarce-le și mai lasă-le un minut.
  - 3. Caramelizează nucile cu zahărul brun și apa, la foc mediu, apoi adaugă banana feliată pentru încă 30 de secunde.
  - 4. Pune toppingul peste pancakes și servește.
- Sub pași: „Toți pașii, cu timpi și sfaturi, plus varianta animată, te așteaptă pe pagina rețetei.”
- CTA (buton): **Vezi rețeta completă** → `{{URL_RETETA_BANANE_NUCI}}` + UTM `s4-reteta-saptamanii`
- Ingredientele și pașii sunt text HTML live, nu imagine (lizibile cu imaginile blocate).
- **Sursă:** https://lucasbites.ro/propunere-v3/reteta.html (ingrediente, pași, sfat, porții, dificultate) și https://lucasbites.ro/propunere-v3/retete.html (eticheta „Rețeta săptămânii”, „Classic Pankees · 3 porții · rețetă animată”, 20 min). Citite la 12.10.2026. Fără afirmații de sănătate în textul preluat.
- **Imagine:** IMG2 (secțiunea 7).

**3 carduri de rețete (implicit, cele din brief)**

Pe propunerea v3, aceste 3 rețete au doar nume, produs, timp și moment. Ingredientele și pașii nu sunt publicați (toate cardurile de pe homepage duc la aceeași pagină-șablon, cea cu banane și nuci). Deci în carduri scriem **doar** ce e publicat, fără descrieri inventate.

| Card | Titlu [din site] | Rând info [din site] | CTA |
|---|---|---|---|
| 1 | **PANCAKES CU AFINE ȘI SIROP** | Cu Blueberry Pankees · 10 min · Mic dejun | **Vezi rețeta** → `{{URL_RETETA_AFINE}}` + UTM `s4-card1` |
| 2 | **TEANCUL DE DUMINICĂ** | Cu Buttermilk Pankees · 10 min · Familie | **Vezi rețeta** → `{{URL_RETETA_TEANC}}` + UTM `s4-card2` |
| 3 | **CLĂTITE PENTRU TOATĂ FAMILIA** | Cu Crêpes Traditional · 10 min · Familie | **Vezi rețeta** → `{{URL_RETETA_CLATITE}}` + UTM `s4-card3` |

- **Contradicție pe propunerea v3, de lămurit (întrebarea 7):** pe homepage, „Pancakes cu afine și sirop” e etichetată „Rețetă animată · Classic Pankees”, pe pagina de rețete produsul e „Blueberry Pankees”. La fel, „Teancul de duminică” e „Rețetă animată” pe homepage, dar nu e marcată animată pe pagina de rețete. Am folosit pagina de rețete (are produsul, timpul și momentul) și n-am scris „animată” pe niciun card.
- **Sursă:** https://lucasbites.ro/propunere-v3/retete.html (titlu, produs, timp, moment) și https://lucasbites.ro/propunere-v3/ (secțiunea „idei de servire”). Citite la 12.10.2026.

**Variante pe categorie (dacă theMarketer permite conținut condiționat după categoria produselor din comandă) [neverificat]:** cardul 1 se înlocuiește cu o rețetă din categoria primului produs comandat; cardurile 2-3 rămân din setul implicit (fără dubluri).

| Categoria comandată | Cardul 1 devine [din site] | Rând info [din site] |
|---|---|---|
| Pankees (orice) | rămâne setul implicit | - |
| Clătite | **CLĂTITE PENTRU TOATĂ FAMILIA** urcă pe primul loc; cardul 3 devine Pancakes cu afine și sirop | Cu Crêpes Traditional · 10 min · Familie |
| Pizza | **PIZZA DE CASĂ CU PEPPERONI** | Cu Pizza Crust Mix · 30 min · Familie |
| Lava Cake | **LAVA CAKE CU ÎNGHEȚATĂ DE VANILIE** | Cu Lava Cake Mix · 12 min · Desert |
| Brownie | **BROWNIE CU FRUCTE DE PĂDURE** | Cu Brownie Mix · 35 min · Desert |
| Cookie Mix | **COOKIES CU CIOCOLATĂ NEAGRĂ** | Cu Cookie Mix Dark Chocolate · 14 min · Desert |

- Aceleași reguli: doar titlu + rând info, aceeași sursă (https://lucasbites.ro/propunere-v3/retete.html, 12.10.2026). Și aceste rețete au doar nume/produs/timp/moment pe v3.
- Dacă nu există conținut condiționat: alternativa e câte o versiune a emailului pe categorie (pancakes implicit, pizza, prăjituri), fiecare cu filtrul ei de produs în automatizare [neverificat: filtru pe categoria produsului comandat]. Recomandarea noastră: pornim cu setul implicit și adăugăm variantele după ce se confirmă funcția.

- **Sub carduri:** link-buton **Toate rețetele** → `{{SHOP_URL}}/retete` + UTM `s4-toate` [din site, „Toate rețetele →”]

**De ce nu folosim rețetele de pe site-ul actual (lucasbites.ro/retete-pancakes-brownies-wafe-naturale/):** toate paginile de rețetă citite la 12.10.2026 încep cu același paragraf care conține afirmații de sănătate („100% sigure pentru sănătatea dumneavoastră și a copiilor”, „E-uri periculoase”), unele și „pufoasă și sănătoasă” (vezi lista din secțiunea 8). Conform discovery 8b și regulii din această sarcină, nu preluăm copy din ele și **nu trimitem linkuri spre ele** din email. Rețeta cu banane și nuci există și acolo (aceleași cantități), dar folosim versiunea aprobată de pe v3.

---

### S5-reteta-ta

- **Scop:** primul pas spre rețetele clienților (cerința din brief) și spre UGC pentru emailurile viitoare.
- **Pattern ref3 potrivit:** bloc text centrat cu buton pastilă; fără fotografii (nu generăm nimic ce ar putea trece drept poză de client).
- **Copy:**
  - Titlu (H2): **TRIMITE-NE REȚETA TA.** [nou]
  - Text: Ai o combinație a ta? Un topping pe care nu l-am încercat noi? Dă reply la emailul ăsta cu rețeta și o poză, sau postează-o cu @lucas_bites și #lucasbites. [nou]
  - Text mic: Cu acordul tău, rețeta ta poate apărea într-un email viitor, cu numele tău. [nou]
  - CTA (buton mare): **Trimite-ne rețeta** → `mailto:office@lucasbites.ro?subject=Rețeta%20mea%20Lucas%20Bites` + (UTM nu se aplică la mailto; se măsoară ca click pe link `s5-reteta` în raportul theMarketer) [nou]
  - Link text: **Vezi @lucas_bites pe Instagram** → https://www.instagram.com/lucas_bites/ + UTM `s5-instagram` [nou]
  - Rând sub link: #lucasbites · pe TikTok: @lucas.bites.ro [din W3]
- **Notă de proces:** rețetele primite se salvează cu acordul scris al autorului (un reply de tipul „da, puteți publica rețeta și poza mea în emailurile Lucas Bites, cu numele meu” e suficient). Fără acord, nu apar nicăieri. Cine răspunde la inbox: întrebarea 10.
- **Imagine:** nu.

---

### S6-ce-urmeaza

- **Scop:** anunță Email 2, dă contactul pentru orice problemă cu comanda și lasă un singur link discret spre gamă (cross-sell ușor).
- **Copy:**
  - Titlu (H2): **CE URMEAZĂ** [nou]
  - Text: În câteva zile te întrebăm cum au ieșit. Până atunci, dacă ai o întrebare despre comandă, scrie-ne la office@lucasbites.ro sau sună-ne la +40 731 399 399. [nou]
  - Text: Când ai poftă de altceva, mixurile Lucas Bites le găsești și în Kaufland, Carrefour, Dr. Max, Farmacia Tei, Bebe Tei, pe eMAG și Freshful. [adaptat din site]
  - Link text (subliniat): **Vezi toată gama** → `{{SHOP_URL}}/produse` + UTM `s6-gama` [nou]
  - Semnătură (Akrobat): **eat what you love** [din site, slogan oficial]
  - Sub semnătură: Familia Lucas Bites [adaptat din site actual: „Noi suntem o familie tânără...”]
- **Imagine:** nu.

---

## 4. Footer (S7-footer)

Identic cu **W1, secțiunea 4 (S7-footer)**, W2 și W3. Nu se modifică nimic fără decizia clientului.

- **Fundal:** alb, separat de secțiunea de deasupra printr-o linie neagră subțire.
- **Logo:** `Logo/Logo_LucasBites_stripes-nobg.png`, centrat, 200px lățime.
- **Iconițe social** (negre, 32px, assets UI): Instagram, TikTok, Facebook, YouTube, cu aceleași linkuri ca în W1.
- **Copy:**

> Lucas Bites · Roșu, Chiajna, Ilfov
> office@lucasbites.ro · +40 731 399 399
>
> Nu mai vrei emailuri de la noi? [Dezabonează-te aici]({{UNSUBSCRIBE_URL}}). Durează un click.
>
> © 2026 Lucas Bites

- **Tehnic:** `{{UNSUBSCRIBE_URL}}` se înlocuiește cu tag-ul de dezabonare din theMarketer [neverificat: sintaxa]. Header-ele `List-Unsubscribe` + `List-Unsubscribe-Post` (one-click, RFC 8058) trebuie să fie active.
- **Fraza de consimțământ:** NU apare în acest email. O adaugă utilizatorul separat, în theMarketer (decizie 12.10.2026). În HTML e un comentariu marker.
- **De confirmat (ca la W1-W3):** denumirea juridică a firmei (SRL) și CUI, dacă vreți identificarea completă a comerciantului.

---

## 5. Predarea către Email 2 (și mai departe)

- **Email 2 (după livrare):** trigger pe statusul „Livrat” + 4-5 zile, fereastra 09:00-20:00. Conținut: „Cum au ieșit?”, cererea de recenzie (theMarketer are modul de feedback și o automatizare de cerere de feedback declanșată după statusul comenzii [verificat]), repetarea invitației de la S5 cu 1-3 rețete sau poze reale primite (doar cu acord), apoi cross-sell: grila „Cumpărate frecvent împreună” din theMarketer [verificat ca tip de recomandare], doar dacă prețul se poate ascunde; altfel 2-3 produse alese manual, fără preț. Aici intră și transportul gratuit de la al 2-lea produs, dacă e valabil.
- **Ramificare Email 2:** cine a dat click pe o rețetă de pizza sau prăjituri în Email 1 primește în Email 2 o rețetă din aceeași categorie (tag la click, ca în W2/W3, dacă theMarketer permite tag pe click [neverificat]).
- **Email 3 (reaprovizionare):** theMarketer are template-ul „Reamintește clienților să recomande” în secțiunea „Post Cumpărare”, cu interval de recurență setat pe fiecare produs [verificat]. Intervalul (de exemplu, câte zile ține o sticlă de Pankees într-o familie) îl dă clientul.
- **Ieșire din flux la toate:** dezabonare, hard bounce, plângere spam, a doua comandă (pentru emailurile de vânzare din flux; Email 2 rămâne).
- **Ce NU repetăm în Email 2:** titlurile, subiectele și fotografiile din Email 1.

---

## 6. Alt text

| Imagine | Alt text |
|---|---|
| Logo header | Lucas Bites |
| IMG1 (hero) | Farfurii cu pancakes cu afine, clătite rulate și brownie cu fructe de pădure, văzute de sus |
| Imagini produse comandate (S2) | `{{ORDER_PRODUCT_NAME}}` (numele produsului din feed); rezervă: „Mix Lucas Bites” |
| IMG2 (rețeta săptămânii) | Pancakes cu banane și nuci caramelizate |
| IMG3 (card 1) | Pancakes cu afine și sirop |
| IMG4 (card 2) | Teanc de pancakes cu unt și sirop, văzut de sus |
| IMG5 (card 3) | Platou cu clătite rulate pentru toată familia |
| IMG6 (variantă pizza) | Pizza de casă cu pepperoni |
| IMG7 (variantă lava cake) | Lava cake cu înghețată de vanilie |
| IMG8 (variantă brownie) | Brownie cu fructe de pădure |
| IMG9 (variantă cookies) | Cookies cu ciocolată neagră |
| Logo footer | Lucas Bites, eat what you love |
| Iconițe social | Instagram / TikTok / Facebook / YouTube (câte una pe iconiță) |
| Valuri, forme decorative | `alt=""` (decorativ) |

---

## 7. Imagini: ce trebuie generat (Higgsfield) și ce vine din feed

Setări (din brief): GPT Image, High, 2K, **fundal alb simplu** pentru decupaje, niciodată „transparent background”. Salvate în `new-customer-01/images/`. Doar mâncare, fără ambalaje, sticle sau pungi, fără text sau logo-uri, fără fețe (mâinile sunt permise, dar nu le cerem aici). Prompturile finale le scrie `image-prompts.md` (nu face parte din acest document).

**Din feed, nu se generează:** imaginile produselor comandate (S2).

**Diferențe obligatorii față de W1-W3** (din `image-prompts.md` ale lor): nu repetăm stack-ul înalt cu afine la 45° (W1), pancakes în evantai cu fructe de pădure de sus (W1), clătite triunghiuri cu dulceață (W1), brownie simplu (W1, W3), tigaia cu bule (W1), masa de brunch pe ardezie (W1), lava cake rupt (W2), pizza întreagă margherita de sus (W2), cele 4 farfurii negre 2 x 2 (W3), stack cu felie scoasă (W3), evantai cu banană și miere (W3), felii de pizza cu legume (W3). Nici farfuria neagră mată din W3 nu o folosim ca recuzită comună, ca setul să arate diferit.

| Fișier | Raport | Folosire | Ce arată |
|---|---|---|---|
| img1-hero.png | 1:1 | S1, compus de UI cu farfurii care ies din cadru | De sus (top-down), 3 farfurii rotunde din ceramică deschisă la culoare, tăiate de marginile cadrului (stânga, dreapta sus, dreapta jos), centrul cadrului liber pentru text: pancakes cu afine coapte în aluat, cu un fir de sirop; clătite rulate, aliniate, cu puțin zahăr pudră; 2 pătrate de brownie acoperite cu fructe de pădure. Fundal alb simplu. |
| img2-banane-nuci.png | 1:1 | S4, rețeta săptămânii (decupaj) | Lateral, 20-30°: teanc de 4 pancakes acoperit cu nuci caramelizate lucioase și felii de banană caramelizate, sirop de arțar care curge pe margini. Farfurie din ceramică deschisă la culoare. Fundal alb simplu. Diferit de W3 (fără miere, fără evantai, accent pe nucile lucioase). |
| img3-afine.png | 1:1 | S4 card 1, decupat în cerc de UI | Aproape (close-up), 45°: 3 pancakes cu afinele vizibile în aluat pe marginea tăiată, sirop de afine pe farfurie. Fundal alb simplu. |
| img4-teanc.png | 1:1 | S4 card 2, cerc | Strict de sus: vârful unui teanc de pancakes, un cub de unt care se topește în centru, sirop în spirală. Fundal alb simplu. |
| img5-clatite.png | 1:1 | S4 card 3, cerc | De sus: platou mare cu clătite rulate, 2 boluri mici cu dulceață și cremă de ciocolată lângă. Fundal alb simplu. |
| img6-pizza-pepperoni.png | 1:1 | S4 variantă pizza, cerc | 45°: jumătate de pizza de casă cu pepperoni, mozzarella topită, margine aurie. Fundal alb simplu. |
| img7-lava-inghetata.png | 1:1 | S4 variantă lava cake, cerc | Lateral: lava cake întreg (nerupt) cu o cupă de înghețată de vanilie lângă, zahăr pudră. Fundal alb simplu. |
| img8-brownie-fructe.png | 1:1 | S4 variantă brownie, cerc | De sus: pătrat de brownie acoperit cu zmeură, afine și mure. Fundal alb simplu. |
| img9-cookies.png | 1:1 | S4 variantă cookies, cerc | De sus: 5-6 cookies cu bucăți de ciocolată neagră, unul rupt în două. Fundal alb simplu. |

- **Minim pentru lansare:** img1-img5 (5 imagini). img6-img9 doar dacă se confirmă conținutul condiționat pe categorie.
- **Recuzită comună:** aceeași farfurie rotundă din ceramică deschisă la culoare (crem sau gri foarte deschis, mată) în toate pozele cu farfurie, ca setul să fie unitar și diferit de farfuria neagră din W3. Culorile plăcilor de fundal le pune UI.
- **Imaginile nu ilustrează pași de rețetă** pe care nu-i avem; arată doar rezultatul, după titlul rețetei.
- **Greutate:** exporturi la 2x față de afișare; cercuri sub 150 KB fiecare, hero și rețeta săptămânii sub 300 KB; total imagini sub 1,2 MB. HTML sub 102 KB (Gmail taie emailul peste această limită, iar rețeta completă din S4 adaugă text).
- Emailul rămâne lizibil cu imaginile blocate: titluri, carduri de produs (nume), listă de cumpărături, ingrediente, pași și butoane sunt text HTML live.

---

## 8. Ce am verificat și ce nu

**Site Lucas Bites (citit la 12.10.2026):**

| Ce | URL | Rezultat |
|---|---|---|
| Rețeta completă „Pankees cu banane și nuci caramelizate” | https://lucasbites.ro/propunere-v3/reteta.html | Ingrediente, 10 pași, sfat, 3 porții · 12 pancakes, „Ușor”. Câmpul de timp e gol („[timp]”). Fără afirmații de sănătate. Folosită în S4. |
| Lista de rețete v3 | https://lucasbites.ro/propunere-v3/retete.html | 12 rețete cu titlu, produs, timp, moment; „Rețeta săptămânii” = banane și nuci (20 min). Fără ingrediente sau pași pentru celelalte 11. |
| Homepage v3, „idei de servire” | https://lucasbites.ro/propunere-v3/ | „Cu ce le mănânci azi?”, cele 3 rețete din brief, „Toate rețetele →”. Toate cele 3 carduri duc la aceeași pagină-șablon. |
| Pagina de rețete, site actual | https://www.lucasbites.ro/retete-pancakes-brownies-wafe-naturale/ (3 pagini) | Găsită din meniul homepage-ului https://www.lucasbites.ro/ ; ~29 de rețete. |
| Rețete site actual citite | https://www.lucasbites.ro/pankees-clasice/ , https://www.lucasbites.ro/reteta-pancakes_banane_si_nuci/ , https://www.lucasbites.ro/reteta-blueberry-pankees-cu-sirop-de-artar/ , https://www.lucasbites.ro/reteta-de-clatite-americane-cu-sirop-de-ciocolata-si-frisca/ , https://www.lucasbites.ro/pizza-salami/ | Toate încep cu paragraful cu afirmații de sănătate („100% sigure pentru sănătatea dumneavoastră și a copiilor”, „E-uri periculoase”; la Pankees Clasice și „pufoasă și sănătoasă”). Nu preluăm copy și nu trimitem linkuri spre ele. Le-am folosit doar ca verificare încrucișată (cantitățile de la Pankees și Pizza coincid cu 8b și v3). |

**theMarketer (documentație oficială, themarketer.com, citită la 12.10.2026; paginile se servesc în română):**

| Ce | URL | Status |
|---|---|---|
| Automatizare declanșată după statusul comenzii (ex. „Livrat”), template-uri în secțiunea „Post Cumpărare” | https://themarketer.com/resources/knowledge-base/how-to-set-up-automated-replenishment-emails și https://themarketer.com/resources/knowledge-base/how-to-set-up-the-feedback-reviews-module | Verificat |
| Etichete de personalizare (nume complet / prenume / nume de familie, link site) inserate printr-o iconiță în subiect și preheader | aceleași 2 articole + https://themarketer.com/resources/knowledge-base/how-to-create-an-automated-cart-abandonment-series | Verificat că există; **sintaxa nu e afișată** în documentație. |
| Filtru „Date E-commerce” > „Statut cumpărător” > „Cumpărător în ultimele X zile” | https://themarketer.com/resources/knowledge-base/how-to-create-an-automated-cart-abandonment-series | Verificat |
| Secțiunea „UTM campanie” cu structură implicită editabilă | aceleași articole | Verificat |
| Blocul „Grilă de produse personalizată” în editorul drag-and-drop, și în emailuri din automatizări; tipuri: „Recomandate pentru tine”, „Cumpărate frecvent împreună”, „Altele care ți-ar putea plăcea” (aceeași categorie ca ultima comandă) etc. | https://themarketer.com/resources/knowledge-base/how-to-add-custom-products-to-your-emails , https://themarketer.com/resources/knowledge-base/personalized-product-grid-recommendation , https://themarketer.com/resources/knowledge-base/determine-fallback-results-personalized-product-grid | Verificat. Setările permit ascunderea titlului, brandului, numelui, ratingului sau reducerii; **ascunderea prețului nu e menționată**. |
| Variabile / bloc pentru **produsele din comanda care a declanșat automatizarea** (nume, imagine, URL) | căutat în sitemap-ul https://themarketer.com/sitemap.xml (cele 99 de articole din knowledge base) și pe web | **Neverificat.** Niciun articol nu le descrie. Folosim placeholdere generice. |
| Conținut condiționat (afișare pe categoria produsului comandat) | idem | **Neverificat.** |
| Filtru „prima comandă” / număr de comenzi, filtru pe categoria produsului comandat, tag la click, grup de control | idem | **Neverificat.** |
| Sintaxa linkului de dezabonare | idem | **Neverificat.** |

**Placeholdere generice folosite (nu sunt sintaxă theMarketer):** `{{FIRST_NAME}}`, `{{ORDER_PRODUCT_NAME}}`, `{{ORDER_PRODUCT_IMAGE}}`, `{{ORDER_PRODUCT_URL}}`, `{{UNSUBSCRIBE_URL}}`, `{{SHOP_URL}}`, `{{URL_RETETA_BANANE_NUCI}}`, `{{URL_RETETA_AFINE}}`, `{{URL_RETETA_TEANC}}`, `{{URL_RETETA_CLATITE}}` (și URL-urile rețetelor-variantă).

---

## 9. Întrebări pentru client (și de verificat în theMarketer)

1. **Produsele comandate în email:** ce variabile sau ce bloc oferă theMarketer pentru produsele din comanda care declanșează automatizarea (nume, imagine, link)? Și ce sintaxă au prenumele și linkul de dezabonare în corpul emailului? Documentația publică nu le arată; răspunsul vine din editorul theMarketer (iconița de personalizare) sau de la suportul lor. Fără asta, S2 nu se poate construi.
2. **Statusurile comenzii:** magazinul trimite în theMarketer statusurile „Expediată” și „Livrată”? Cum se numesc exact? (Pentru trigger-ul Email 1 și Email 2.)
3. **Prima comandă:** se poate filtra în theMarketer „prima comandă” (sau „număr de comenzi = 1”)? Dacă nu, cine a mai cumpărat înainte (inclusiv pe site-ul vechi) ar primi și el emailul.
4. **Conținut condiționat:** theMarketer permite afișarea unui bloc după categoria produsului comandat? De asta depind rândurile din S2 și S3 și variantele de rețete din S4.
5. **Categoriile din feed:** cum apar categoriile produselor în feed-ul theMarketer (Pankees, Clătite, Prăjituri, Pizza, Professional)? Sunt completate la toate produsele?
6. **Consimțământ și footer:** cumpărătorii intră în lista de marketing doar dacă bifează la checkout, sau vreți să folosiți excepția pentru clienți existenți (cu posibilitate clară de refuz la comandă)? În funcție de răspuns, fraza din footer „te-ai abonat... la ghidul de rețete” se schimbă doar în acest flux (propunerea e în secțiunea 4).
7. **Rețetele din brief pe site-ul nou:** „Pancakes cu afine și sirop”, „Teancul de duminică” și „Clătite pentru toată familia” vor avea pagini proprii cu ingrediente și pași la lansare? Care sunt URL-urile? „Pancakes cu afine și sirop” se face cu Classic sau cu Blueberry Pankees (v3 spune ambele)? „Teancul de duminică” e rețetă animată sau nu?
8. **Lista de cumpărături (S3):** cantitățile din site-ul actual sunt valabile pe ambalajele de acum? Produsul de clătite se numește „Crêpes Traditional” (v3) sau „Crêpes Mix Original” (site actual), și rămâne 675 ml apă?
9. **Comenzile Professional:** cum le deosebim în theMarketer de cele pentru acasă, ca să le excludem din acest flux?
10. **Rețetele clienților:** cine citește reply-urile la office@lucasbites.ro și salvează acordul autorilor? Vreți un premiu sau o mențiune pentru rețetele publicate (fără reducere, dacă rămâne regula)?
11. **Grila de produse recomandate (pentru Email 2):** se poate ascunde prețul din blocul „Grilă de produse personalizată”? Dacă nu, pentru Email 2 alegem produsele manual.
12. **Reaprovizionare (Email 3):** în câte zile se termină, în medie, o sticlă de Pankees, un Pizza Crust Mix, un Brownie Mix într-o familie? Valorile se setează pe fiecare produs în theMarketer.
