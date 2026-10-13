# Lucas Bites: New Customer, Email 3, strategie, structură și copy final

Surse: `brief.md` (acest folder, decizii din 13.10.2026, au prioritate), `discovery.md`, `new-customer-01/copy.md`, `new-customer-02/copy.md` (format, footer, UTM, secțiunea 5), `new-customer-02/index.html` (footer), `refs/ref3.png`, `refs/ref4.png`, `packshots/`. Legendă, aceeași ca la Email 1 și 2: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [adaptat] = text aprobat ajustat pentru email, [nou] = text nou, de aprobat de client, [din site actual] = site-ul WordPress actual (termeni și condiții), [neverificat] = funcție theMarketer negăsită în documentația oficială, [de confirmat] = informație comercială de confirmat la lansare.

**Ce cere clientul:** recomandare de produse cross-sell; USP-uri (transport, livrare, suport); încurajarea clientului să-și posteze rețeta pe social media.

**Ce fel de email e:** al treilea email după prima comandă. Clientul a primit deja rețete (Email 1 și 2) și i s-a cerut o recenzie (Email 2, S3). Email 3 nu mai cere nimic despre comanda trecută: arată trei produse pe care încă nu le-a văzut ca produs principal, îi spune cât de simplu e să comande din nou și îl invită să ne arate ce gătește. Nu e emailul de reaprovizionare (brief: structura clientului are prioritate față de secțiunea 5 din Email 2).

**Fără prețuri, fără coduri de reducere, fără ingrediente sau pași de rețetă inventați.** Toate faptele despre livrare și suport sunt citate din brief.

---

## Ce am adăugat față de structura cerută și de ce

Structura cerută: cross-sell, USP, social. Am adăugat doar:

- **S1-hero scurt.** Fără el, emailul ar începe direct cu un rând de produse, adică ar arăta ca un catalog. Un titlu de 3-4 cuvinte și o frază spun de ce primește emailul.
- **Linia de suport în S3 (nu secțiune separată).** Brief-ul dă contactul verificat (telefon, email, „îți răspundem în zilele lucrătoare”). E cel mai util USP pentru un client nou și ține locul unui bloc „Ai întrebări?”. Pagina /contact/ dă 404, deci linkurile sunt `mailto:` și `tel:`.
- **Ce NU am adăugat:**
  - rețete complete sau perechi rețetă + produs (au fost în Email 2; aici rețeta e doar un rând de inspirație sub produs, fără link separat);
  - recenzii sau stele (cererea de recenzie a fost în Email 2; dovada socială cu recenzii reale vine doar cu acordul autorilor, vezi secțiunea 5);
  - pachetele cu transport gratuit (pe v3 sunt „Propunere · de stabilit de Lucas Bites”);
  - „fără conservanți” (vezi secțiunea 8: e afirmație de compoziție, nu de sănătate, dar nu ajută la cross-sell și Pizza Crust Mix are aditivi, deci formularea pe toată gama cere atenție; o lăsăm deoparte);
  - returul (transportul retur îl plătește clientul, nu e argument de vânzare).

---

## Ce preluăm din ref3 și ref4 (UI Designer decide final)

De evitat (au fost în Email 1 și 2): hero roz cu farfurii la colțuri, carduri albe rotunde, zig-zag farfurie + bandă (NC1); hero portocaliu cu ingrediente zburând, perechi rețetă + produs pe fundaluri alternate (NC2).

| Pattern | Sursă | Potrivit pentru | De ce |
|---|---|---|---|
| Titlu foarte mare, scurt, pe bloc plin, cu o tăietură ondulată jos | ref4, col. 1 | S1-hero | Hero tipografic, fără farfurii, diferit de NC1 și NC2 |
| Packshot mare cu mâncare decupată lângă el, care iese din cadru | ref4, col. 3 | S2, cele 3 produse | Produsul real e vedeta; mâncarea arată ce iese din el |
| Rând de 3 coloane (pe mobil, 1 coloană) | ref3 | S2 | Pattern nou în flux; trei produse egale, un singur ecran pe desktop |
| Bandă cu iconițe simple + text scurt | ref3 („Eat. Recycle. Repeat.”) | S3 USP | Se citește dintr-o privire; iconițele desenate în culorile brandului |
| Grilă de pătrate tip „poză de telefon” + handle foarte mare | ref4 (titluri mari) | S4 social | Arată exact ce cerem: o poză făcută acasă |
| Buton pastilă | ref3, ref4 | toate CTA-urile | Continuitate de familie |

**Packshot-uri:** JPG 900 x 900, fundal alb. Nu se decupează, nu se recolorează, nu primesc umbre. Stau pe o zonă albă (panou sau cerc alb) peste culoarea de brand. Pe portocaliu, roz, turcoaz: text negru. Pe negru: text doar portocaliu. Niciodată text alb pe culorile de brand.

---

## 1. Obiectiv, KPI, trimitere

**Obiectiv:** a doua comandă, cu un produs dintr-o categorie nouă (brownie, cookies, clătite). Secundar: clientul postează o poză cu ce a gătit și ne dă tag.

**KPI principal:** rata de click unic pe oricare link din S2 (cele 3 produse + „Vezi toate produsele”), raportată la livrate. Țintă 4%+, alertă sub 1,5%. Sub Email 2 (5%): al treilea email din flux, fără rețete noi ca motiv de click.

**KPI secundar:** rata de a doua comandă în 14 zile de la trimitere, atribuită pe `utm_campaign=new_customer_03`. Reper de pornire 3% [propunere, nu benchmark verificat], se fixează după prima lună.

**KPI terțiar:** click unic pe Instagram + TikTok din S4 (țintă 1%+, alertă sub 0,3%); numărul de postări cu tag @lucas_bites în 30 de zile (raport manual, nu țintă; tag-urile nu se pot atribui emailului).

**Trigger și timing:**
- **Recomandat:** 7 zile după Email 2 (adică „Livrat” + 12 zile), fereastra 09:00-20:00, ora României.
- **De ce 7 zile:** Email 2 a cerut recenzia și reply-ul; reply-urile cu probleme trebuie rezolvate înainte de un email care vinde (secțiunea 5 din Email 2). Pe la 12 zile de la livrare, primul mix e pe terminate la cine l-a folosit în weekend, dar nu e încă momentul reaprovizionării.
- **Gardă:** minimum 5 zile între Email 2 și Email 3; niciun contact nu primește două emailuri de marketing în 24 de ore.

**Segment:**
- Intră: contactele care au primit New Customer 2 (prima comandă, gama pentru acasă, temei pentru marketing).
- Exclus: comenzi anulate sau returnate; Professional / HoReCa; dezabonați, suprimați, plângeri spam; contactele puse pe pauză manual după un reply cu problemă în Email 2 [neverificat: excludere manuală din automatizare].

**Condiții de ieșire din flux:**
1. Dezabonare.
2. Hard bounce.
3. Plângere spam.
4. Comandă anulată sau returnată integral.
5. A doua comandă plasată după Email 2 (secțiunea 5 din Email 2: a doua comandă oprește cross-sell-ul; pornește reaprovizionarea). De confirmat cu clientul, întrebarea 4.
6. Contactul e deja în flux pentru aceeași comandă (fără dubluri).

**Consimțământ:** același temei ca la Email 1. Fraza din footer o adaugă utilizatorul.

**UTM:** `utm_source=email&utm_medium=postpurchase&utm_campaign=new_customer_03&utm_content=<id>`. Valori: `s1-hero`, `s2-brownie`, `s2-cookie`, `s2-crepes`, `s2-toate`, `s4-instagram`, `s4-tiktok`. `mailto:` și `tel:` nu primesc UTM (se citesc ca click în raport).

**Condiții de lansare:**
1. Cele 3 linkuri de produs (site actual) răspund 200 și produsele sunt în stoc.
2. Transportul gratuit de la al 2-lea produs e confirmat; altfel rândul respectiv din S3 se scoate (S3 rămâne cu 3 iconițe).
3. Inbox-ul office@lucasbites.ro și telefonul sunt monitorizate în zilele lucrătoare (S3 promite răspuns).

Gărzi de siguranță: plângeri spam sub 0,10%, dezabonări sub 0,5%, hard bounce sub 1%. Rata de deschidere doar orientativ (Apple MPP).

---

## 2. Subiecte și preheadere

| # | Subiect | Caractere | Preheader |
|---|---|---|---|
| A **[recomandat]** | Data viitoare, brownie? [nou] | 22 | Sau cookies, sau clătite. Și o rugăminte: arată-ne ce ai gătit. [nou] |
| B | Arată-ne ce ai gătit [nou] | 20 | Pune poza pe Instagram sau TikTok și dă-ne tag @lucas_bites. [nou] |
| C | {{FIRST_NAME}}, ce încerci după pancakes? [nou] | 31 fără nume (rezervă: „Ce încerci după pancakes?”) | Brownie, cookies, clătite. Comanzi azi până la 15:00, pleacă azi. [nou; fapt din site actual] |

De ce A: scurt, apetisant, numește produsul cross-sell principal și nu repetă tiparul din Email 2 (listă de trei feluri în subiect) sau întrebarea „Ai poftă de altceva?”. Preheaderul acoperă celelalte două produse și blocul social. B duce spre social, nu spre KPI-ul principal. C presupune că primul mix a fost un Pankees; folosiți-l doar dacă theMarketer poate filtra după categoria comandată [neverificat].

**Notă la C:** „pleacă azi” e adaptat din „se procesează în aceeași zi (luni-vineri)”. Procesat nu înseamnă neapărat predat curierului. Dacă clientul nu confirmă că procesare = expediere în aceeași zi, preheaderul C devine „Comenzile de până la 15:00 se procesează în aceeași zi.”

**Test A/B:** A contra B, câștigător pe click unic S2 raportat la livrate; ~500 livrări pe variantă; sub 1 punct procentual, fără câștigător.

**Expeditor:** Lucas Bites. **Reply-to:** aceeași adresă monitorizată ca la Email 1 și 2.

---

## 3. Structura, de sus în jos

Lățime 600px, o coloană pe mobil. Titluri: `Akrobat, "Arial Narrow", Arial, sans-serif`, majuscule. Text: `Arial, Helvetica, sans-serif`, 16px. Butoane pastilă bulletproof. Ordinea culorilor pe secțiuni o decide UI Designer (diferită de NC1 și NC2). Lungime țintă: cam 3,5 ecrane pe mobil.

---

### S0-header

- Identic cu Email 1 și 2 (logo `Logo/Logo_LucasBites.png`, centrat, 180px, export 360px).

---

### S1-hero

- **Scop:** în 3 secunde: trei mixuri noi de încercat. Fără imagine mare (packshot-urile vin imediat dedesubt).
- **Pattern:** ref4 col. 1, titlu foarte mare pe bloc plin, tăietură ondulată spre S2.
- **Copy:**
  - Supratitlu: **alege-ți pofta de azi** [din site]
  - Titlu (H1): **URMĂTOAREA POFTĂ?** [nou]
  - Text: Salut, {{FIRST_NAME}}! Pancakes dimineața, ceva dulce după-amiaza, clătite în weekend. Uite ce mai poți pune pe masă cu Lucas Bites. [nou, revizuit 13.10]
  - Rezervă fără prenume: Salut! Pancakes dimineața, ceva dulce după-amiaza, clătite în weekend. Uite ce mai poți pune pe masă cu Lucas Bites. [nou, revizuit 13.10]
  - CTA: **Vezi mixurile** → ancoră spre S2 nu e sigură în toate clienții de email; butonul duce la `{{SHOP_URL}}/produse` + UTM `s1-hero` [nou]
- **Notă:** textul S1 și titlul S2 au fost refăcute (13.10) ca să nu presupună ce a cumpărat clientul: emailul merge la fel pentru oricine, chiar dacă a comandat deja unul din cele trei produse.

---

### S2-cross-sell (3 produse fixe)

- **Scop:** cererea clientului și KPI-ul principal.
- **Pattern:** rând de 3 coloane pe desktop, 1 coloană pe mobil; packshot pe alb + decupaj de mâncare care iese din cadru (ref4 col. 3).
- **Marker HTML (obligatoriu):** blocul întreg e încadrat de `<!-- [OPȚIONAL theMarketer] Blocul de mai jos poate fi înlocuit cu un bloc de recomandări de produse din theMarketer. De verificat: că blocul nu afișează prețuri și că exclude produsele deja cumpărate. -->` și un comentariu de închidere. Existența blocului de recomandări în editor: [neverificat].
- **Copy antet:**
  - Titlu (H2): **UN MIX PENTRU FIECARE MOMENT** [revizuit 13.10]
  - Text: Desert la birou, gustare după școală sau duminică fără grabă. Alege ce ți se potrivește. [revizuit 13.10: structura pe momente, preluată de pe v3, nu presupune ce a cumpărat clientul]

**Structura unui card (aceeași la toate 3):** etichetă moment → nume produs (H3) → gramaj → packshot + decupaj mâncare → un rând despre ce adaugi / când îl faci → rând „Rețetă de încercat” (doar text) → buton.

| | Card 1 | Card 2 | Card 3 |
|---|---|---|---|
| Etichetă [din site, momente v3] | **pauza de la birou** | **gustarea de după școală** | **duminica fără grabă** |
| Nume (H3) [din site] | BROWNIE MIX | COOKIE MIX DARK CHOCOLATE | CRÊPES TRADITIONAL |
| Gramaj [din brief] | 450 g | 450 g · vegan [din site v3] | 280 g |
| Rând produs | Tu adaugi ouăle, puțină apă și ulei sau unt topit. Restul e deja în mix. [adaptat din site actual: 3 ouă + 50 ml apă + 125 ml ulei sau unt topit] | Tu adaugi doar ce scrie pe ambalaj. Restul e deja în mix. [adaptat din site] | Clătite subțiri, cât timp se face cafeaua. [adaptat din site, „Duminica fără grabă”] |
| Rețetă de încercat [din site, retete.html] | Brownie cu fructe de pădure · 35 min | Cookies cu ciocolată neagră · 14 min | Clătite pentru toată familia · 10 min (singura rețetă Crêpes de pe v3; apare și în Email 1, adăugată la cererea utilizatorului 13.10) |
| Packshot | `packshots/pr-brownie.jpg` | `packshots/pr-cookie450.jpg` | `packshots/pr-crepes.jpg` |
| Decupaj mâncare | IMG1 | IMG2 | IMG3 |
| CTA (buton) | **Vezi Brownie Mix** → `https://www.lucasbites.ro/produs/brownie-mix-450g-2/` + UTM `s2-brownie` | **Vezi Cookie Mix** → `https://www.lucasbites.ro/produs/cookie-mix-amestec-pentru-biscuiti-cu-ciocolata-neagra-450g/` + UTM `s2-cookie` | **Vezi Crêpes** → `https://www.lucasbites.ro/produs/crepes-mix-traditional-280g-clatite-frantuzesti/` + UTM `s2-crepes` |

- **Sub cele 3 carduri:** link-buton secundar **Vezi toate produsele** → `{{SHOP_URL}}/produse` + UTM `s2-toate` [din site, „Toate produsele”]
- **De ce ordinea asta:** Brownie e în subiect, deci e primul. Cookie a doua (desert, tot categorie nouă). Crêpes ultima: e cea mai apropiată de Pankees, deci cel mai puțin „nou”.
- **„vegan” la Cookie Mix:** apare pe v3 ca atribut al produsului (filtrul „Vegan / de post”). E o etichetă de compoziție, nu o promisiune de sănătate. De confirmat că pagina produsului de pe site-ul actual spune la fel (întrebarea 3); dacă nu, se scoate.
- **„Rețetă de încercat”:** doar titlul și timpul din v3, fără link (paginile de rețetă v3 duc toate la aceeași rețetă). Nu scriem ingrediente sau pași.
- **Atenție la linkuri:** paginile de produs de pe site-ul actual pot conține afirmații de sănătate (discovery 8b). Emailul nu le preia; la lansarea v3 linkurile trec pe paginile noi.

---

### S3-usp (bandă cu 4 iconițe)

- **Scop:** elimină frecarea dinaintea celei de-a doua comenzi: cât costă livrarea, cât durează, cum plătesc, pe cine întreb.
- **Pattern:** bandă de culoare cu 4 iconițe simple (2 x 2 pe mobil), fiecare cu titlu scurt (Akrobat) + un rând (Arial).
- **Copy:**
  - Titlu (H2): **SIMPLU DE COMANDAT** [nou]

| Iconiță | Titlu | Rând | Sursă |
|---|---|---|---|
| cutie / pachet | TRANSPORT GRATUIT | De la al 2-lea produs pentru acasă. | [din site] [de confirmat la lansare] |
| ceas | PLEACĂ REPEDE | Comenzile de până la 15:00 se procesează în aceeași zi, de luni până vineri. Livrarea prin curier: 24-48 de ore lucrătoare. | [din site actual, termeni și condiții, adaptat] |
| card | PLĂTEȘTI CUM VREI | Card pe site, transfer bancar sau ramburs la livrare. Fără comandă minimă. | [din site actual, adaptat] |
| balon de chat | SUNTEM AICI | Întrebări despre comandă sau produse? Îți răspundem în zilele lucrătoare. office@lucasbites.ro · +40 731 399 399 | [din site, contact.html, adaptat] |

- **Linkuri:** `mailto:office@lucasbites.ro` și `tel:+40731399399` (fără UTM). Nu se folosește /contact/ (404).
- **Dacă transportul gratuit nu se confirmă:** se scoate prima iconiță; banda rămâne cu 3 (pe mobil, 1 coloană).
- **Ce nu scriem:** „livrare a doua zi”, „livrare gratuită” fără condiție, ore de program la telefon, termen de răspuns în ore. Brief-ul nu le dă.
- **Iconițe:** desenate de UI Designer, line art negru pe culoarea benzii, fără text în imagine; `alt=""` (textul e live alături).

---

### S4-social (invitația de postare)

- **Scop:** cererea clientului; clientul postează și ne dă tag. Doar invitație: fără recompensă, concurs, premii, hashtag sau promisiune de repostare (decizii 2 și 3).
- **Pattern:** grilă de 3 pătrate tip „poză de telefon” (IMG4-IMG6) + handle foarte mare.
- **Copy:**
  - Supratitlu: **de la voi, pentru voi** [din site, secțiunea UGC v3]
  - Titlu (H2, foarte mare): **@LUCAS_BITES** [din site]
  - Text: Ai făcut pancakes, brownie sau clătite cu mixul nostru? Fă-le o poză înainte să dispară și pune-o pe Instagram sau TikTok. Dă-ne tag @lucas_bites, ne bucurăm să vedem cum arată Lucas Bites în viața reală. [nou; „Lucas Bites în viața reală” din site]
  - CTA principal (buton): **Instagram** → `https://www.instagram.com/lucas_bites/` + UTM `s4-instagram`
  - CTA secundar (buton contur): **TikTok** → `https://www.tiktok.com/@lucas.bites.ro` + UTM `s4-tiktok`
  - Semnătură (Akrobat): **eat what you love** [din site, slogan oficial]
  - Sub semnătură: Familia Lucas Bites [ca în Email 1 și 2]
- **Etichetă obligatorie pe grilă (text mic, live):** „Fotografii cu titlu de exemplu.” [nou] Pozele sunt generate, deci nu le prezentăm ca postări reale ale clienților: fără nume de utilizator, fără like-uri, fără interfață de Instagram desenată peste ele.
- **Notă de ton:** „ne bucurăm să vedem” nu promite repostare sau răspuns. Nu scriem „cele mai frumoase poze ajung pe pagina noastră”.
- **Dacă vor exista poze reale de la clienți (cu acord scris):** pot înlocui IMG4-IMG6, cu numele autorului, iar eticheta „de exemplu” se scoate.

---

## 4. Footer (S5-footer)

Identic cu Email 2 (`new-customer-02/index.html`). Nu se modifică nimic fără decizia clientului.

- **Fundal:** alb, separat de S4 printr-o linie neagră subțire.
- **Logo:** `Logo/Logo_LucasBites_stripes-nobg.png`, centrat, 200px.
- **Iconițe social** (negre, 32px, aceleași assets ca în Email 2):
  - Instagram → https://www.instagram.com/lucas_bites/
  - TikTok → https://www.tiktok.com/@lucas.bites.ro
  - Facebook → https://www.facebook.com/Lucas-Bites-101759484548844
  - YouTube → https://www.youtube.com/@lucasbites2267
- **Copy:**

> Lucas Bites · Roșu, Chiajna, Ilfov
> office@lucasbites.ro · +40 731 399 399
>
> [ADAUGĂ UTILIZATORUL]
>
> Nu mai vrei emailuri de la noi? [Dezabonează-te aici]({{UNSUBSCRIBE_URL}}). Durează un click.
>
> © 2026 Lucas Bites

- **Fraza de consimțământ:** nu e scrisă. În HTML rămâne comentariul `<!-- [ADAUGĂ UTILIZATORUL] Fraza de consimțământ se pune separat, în theMarketer (brief, decizia 5). -->`, pe aceeași poziție ca în Email 2 (după contact, înainte de dezabonare).
- **Tehnic:** `{{UNSUBSCRIBE_URL}}` se înlocuiește cu tag-ul theMarketer [neverificat: sintaxa]. `List-Unsubscribe` + `List-Unsubscribe-Post` (one-click, RFC 8058) active.
- **De confirmat:** denumirea juridică (SRL) și CUI.

---

## 5. Predarea către Email 4

- **Email 4 (reaprovizionare):** template-ul theMarketer „Post Cumpărare” cu interval de recurență pe produs [verificat în Email 1, secțiunea 8]. Pornește după intervalul dat de client pentru produsul din prima comandă; conținut: produsul cumpărat + o rețetă nefolosită cu același produs (Gingerbread Pancakes, Pankees de post cu fructe).
- **Ce ia Email 4 din Email 3:**
  - produsul pe care s-a dat click în S2 (tag la click [neverificat]) poate fi recomandat din nou în Email 4, ca a doua sugestie;
  - cine a cumpărat după Email 3 iese din cross-sell și intră pe reaprovizionare pentru noul produs;
  - postările cu tag @lucas_bites găsite manual: cu acordul scris al autorului, pot deveni pozele reale din emailurile următoare (înlocuiesc pozele generate).
- **Ce NU repetăm în Email 4:** subiectele, titlurile, cardurile și fotografiile din Email 1-3; banda USP din S3 (în Email 4 doar un rând de transport, dacă e confirmat).

---

## 6. Alt text

| Imagine | Alt text |
|---|---|
| Logo header | Lucas Bites |
| Packshot `pr-brownie.jpg` + IMG1 (dacă UI le combină într-un singur JPG) | Brownie cu fructe de pădure și punga Brownie Mix |
| Packshot `pr-cookie450.jpg` + IMG2 | Cookies cu ciocolată neagră și punga Cookie Mix Dark Chocolate |
| Packshot `pr-crepes.jpg` + IMG3 | Clătite subțiri și flaconul Crêpes Traditional |
| Packshot-uri separate (dacă nu se combină) | Brownie Mix / Cookie Mix Dark Chocolate / Crêpes Traditional |
| IMG1-IMG3 separate | Brownie cu fructe de pădure / Cookies cu ciocolată neagră / Clătite subțiri împăturite |
| IMG4 | Pancakes făcute acasă, fotografiate pe blatul din bucătărie |
| IMG5 | Brownie tăiat în tavă, poză făcută acasă |
| IMG6 | Clătite rulate pe o farfurie, poză făcută acasă |
| Iconițe USP, tăieturi, forme | `alt=""` |
| Logo footer | Lucas Bites, eat what you love |
| Iconițe social | Instagram / TikTok / Facebook / YouTube |

**Notă (verificat vizual de UI Designer):** Brownie Mix și Cookie Mix sunt pungi (doypack); Crêpes Traditional e un flacon de plastic cu mâner, deci „flaconul”, nu „sticla”.

---

## 7. Imagini: ce se generează (Higgsfield) și ce vine din `packshots/`

**Packshot-uri (nu se generează, nu se modifică):**

| Unde | Fișier |
|---|---|
| S2 card 1 | `packshots/pr-brownie.jpg` |
| S2 card 2 | `packshots/pr-cookie450.jpg` |
| S2 card 3 | `packshots/pr-crepes.jpg` |

**Fotografii de mâncare (Higgsfield, generate de Claude, în `new-customer-03/images/`):** doar mâncare, fără ambalaje, sticle, pungi, cutii, fără text, fără logo, fără fețe; mâinile sunt permise. Total 6 imagini.

| Fișier | Raport | Folosire | Ce arată | Fundal |
|---|---|---|---|---|
| img1-brownie.png | 1:1 | S2 card 1, decupaj lângă packshot | Trei pătrate de brownie stivuite ușor decalat, crustă lucioasă crăpată sus, interior dens și umed vizibil pe latura tăiată; câteva mure, zmeură și afine pe și lângă teanc. Unghi 30°, fără farfurie. | alb simplu, pentru decupaj |
| img2-cookies.png | 1:1 | S2 card 2, decupaj | Patru cookies cu bucăți mari de ciocolată neagră topită la suprafață, unul rupt în două cu interiorul moale vizibil, câteva fărâme și bucăți de ciocolată în jur. Unghi frontal-jos, ușor de sus. | alb simplu, pentru decupaj |
| img3-crepes.png | 1:1 | S2 card 3, decupaj | Trei clătite subțiri împăturite în triunghi, suprapuse în evantai, margini aurii dantelate, puțină pudră de zahăr. Fără topping-uri grele. Diferit de platoul cu clătite din Email 1. | alb simplu, pentru decupaj |
| img4-ugc-pancakes.png | 1:1 | S4 grilă, pătrat 1 | Stil poză de telefon, de sus: farfurie cu teanc mic de pancakes și fructe, pe un blat de bucătărie obișnuit, o cană de cafea tăiată de cadru, o mână care ține furculița intrând din colț. Lumină naturală de fereastră, ușor imperfectă, încadrare neglijentă. | foto întreagă, nedecupată |
| img5-ugc-brownie.png | 1:1 | S4 grilă, pătrat 2 | Stil poză de telefon: tavă de copt cu brownie tăiat în pătrate, hârtie de copt la margini, un pătrat lipsă, o mână care ridică o bucată cu spatula. Lumină caldă de seară. | foto întreagă, nedecupată |
| img6-ugc-crepes.png | 1:1 | S4 grilă, pătrat 3 | Stil poză de telefon: clătite rulate pe o farfurie, pe o masă de lemn cu o față de masă în carouri la margine, borcan de gem deschis fără etichetă. Lumină de dimineață. | foto întreagă, nedecupată |

- **Diferențe față de NC1, NC2, W1-W3:** fără teancuri înalte, fără farfurii de sus la colțuri, fără lava cake, pizza, banane cu nuci sau afine cu sirop ca subiect principal.
- **UGC (IMG4-IMG6):** trebuie să arate ca poze reale de acasă (fără styling de studio), dar nu pretind că sunt ale unor clienți: fără interfață de social media, fără nume de utilizator (vezi S4, eticheta „de exemplu”). Niciun ambalaj, deci nici packshot în ele.
- **Recuzită:** unde e farfurie în IMG1-IMG3 nu e (decupaje libere); în UGC, veselă obișnuită, nu ceramica din NC1.
- **Greutate:** exporturi la 2x față de afișare, fiecare sub 200 KB; total imagini sub 1,2 MB; HTML sub 102 KB.

---

## 8. Ce am verificat și ce nu

**Verificat (din brief, citit 13.10.2026 de utilizator / agentul anterior; nu am redeschis paginile):**
- Transport gratuit de la al 2-lea produs (v3, header) [de confirmat la lansare].
- Procesare în aceeași zi pentru comenzile până la 15:00, L-V; livrare prin curier în 24-48 de ore lucrătoare; fără comandă minimă; plata card / transfer / ramburs (site actual, termeni și condiții).
- Contact: răspuns în zilele lucrătoare, +40 731 399 399, office@lucasbites.ro; /contact/ = 404.
- Linkurile celor 3 produse, gramajele, „vegan” la Cookie Mix (v3), titlurile și timpii rețetelor Brownie și Cookies (v3), textele UGC de pe v3.
- Footer și linkuri social: citite din `new-customer-02/index.html`.
- „Ce adaugi” la Brownie Mix: discovery (site actual, pagina produsului).

**Neverificat:**
- Blocul de recomandări de produse din editorul theMarketer și dacă poate ascunde prețul și exclude produsele cumpărate.
- Conținut condiționat după produsele comandate (textul din S1, subiectul C).
- Tag la click, excludere manuală din automatizare, sintaxa prenumelui și a dezabonării.
- Ce adaugi la Cookie Mix și la Crêpes Traditional 280 g (de aceea rândurile lor nu dau cantități).
- Dacă „procesat în aceeași zi” înseamnă „predat curierului în aceeași zi” (nu folosim „pleacă azi” în copy-ul principal; titlul iconiței „PLEACĂ REPEDE” e generic).

**„Fără conservanți”:** discovery îl marchează confirmat, iar brief-ul îl lasă la decizia strategistului. Nu e o afirmație de sănătate, dar e o mențiune de compoziție pe toată gama, iar emailul nu are nevoie de ea pentru cross-sell. Omis.

**Placeholdere generice (nu sunt sintaxă theMarketer):** `{{FIRST_NAME}}`, `{{SHOP_URL}}`, `{{UNSUBSCRIBE_URL}}`.

---

## 9. Întrebări pentru client (și de verificat în theMarketer)

1. **Transport gratuit de la al 2-lea produs:** valabil la lansare? Se aplică și la două bucăți din același produs?
2. **Procesare și expediere:** o comandă procesată până la 15:00 pleacă la curier în aceeași zi? Dacă da, putem scrie „pleacă azi”.
3. **Cookie Mix Dark Chocolate:** e vegan și pe produsul vândut acum (ambalaj, pagina din site-ul actual)? Ce se adaugă la preparare, la el și la Crêpes Traditional 280 g?
4. **A doua comandă înainte de Email 3:** o scoatem din flux (recomandarea noastră) sau primește totuși emailul?
5. **Bloc de recomandări theMarketer:** există în editorul de automatizări, poate ascunde prețul și poate exclude produsele deja cumpărate? Dacă da, înlocuiește cardurile fixe din S2.
6. **Postări cu tag:** cine urmărește tag-urile @lucas_bites pe Instagram și TikTok și cere acordul autorilor înainte ca o poză să apară în emailuri sau pe site?
7. **Suport:** telefonul are un program anume? Dacă da, îl adăugăm în S3; altfel rămâne „în zilele lucrătoare”.
8. **Pozele generate în S4:** sunteți de acord cu pozele de exemplu, etichetate „Fotografii cu titlu de exemplu”, până strângem poze reale?
