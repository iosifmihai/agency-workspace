# Lucas Bites: Request review, strategie, structură și copy final

Surse: `brief.md` (acest folder), `discovery.md` (inclusiv 8b), `new-customer-01/copy.md` (format, footer, verificări theMarketer), `replenishment/copy.md` (timing vecin), `_reference/ref-iqbar-reviews.png`, `_reference/ref-misfits.png`, `_reference/ref-olipop-recess.png`. Legendă: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [adaptat] = text aprobat ajustat pentru email, [nou] = text nou, de aprobat de client, [neverificat] = funcție theMarketer pe care n-am găsit-o în documentația oficială.

**Ce cere clientul:** un email post-achiziție care (1) cere recenzie pentru produsele cumpărate, (2) invită la urmărire pe social media și la postarea creației cu tag Lucas Bites, (3) arată produse recomandate.

**Ce fel de email e:** email post-achiziție, cu scop principal recenzia. Fără reducere, fără cod, fără recompensă pentru recenzie, fără prețuri.

**Ton:** curiozitate sinceră („cum au ieșit?”), nu cerere insistentă. Recenzia e prezentată ca ajutor pentru alți oameni cu poftă, nu ca favoare pentru brand.

---

## Ce am adăugat față de structura cerută și de ce

- **S1 hero „Cum au ieșit?”** înaintea blocului de produse: emailul începe cu experiența clientului, nu cu cererea. Cererea vine în S2, cu un singur click (stelele).
- **S2b „De ce contează” cu cifra reală 1.100+ / 4,9:** arată că recenzia lui intră într-o comunitate existentă. Fără citate: discovery nu conține recenzii text. **Opțional, după aprobare:** 2-3 recenzii reale din modulul de recenzii theMarketer (vezi întrebarea 4), puse în baloanele IQBAR. Până atunci, secțiunea rămâne doar cu cifra.
- **Ce NU am adăugat:** stimulent pentru recenzie (vezi mai jos), rețete complete (emailul are deja 3 scopuri), lista de retaileri.

**De ce fără stimulent:** recenziile oferite în schimbul unei reduceri sau al punctelor de loialitate trebuie declarate ca atare (Directiva Omnibus UE 2019/2161, transpusă în Legea protecției consumatorului; practicile comerciale neloiale privind recenziile). Google interzice recenziile stimulate, iar eMAG și marketplace-urile le pot elimina. Discovery nu menționează un program de recenzii, deci nu introducem unul. Dacă clientul vrea unul, se decide separat, cu mențiune vizibilă „recenzie stimulată”.

---

## 1. Obiectiv, KPI, trimitere

**Obiectiv:** recenzii publicate pe site pentru produsele cumpărate.

**KPI principal:** rata de recenzie (recenzii trimise atribuite emailului / emailuri livrate), fereastră 14 zile. Țintă 3%+, alertă sub 1%. [nou, de calibrat după primele 30 de zile]

**KPI secundar:** click unic pe stele / „Lasă o recenzie” / livrate. Țintă 6%+, alertă sub 2%. CTOR orientativ, țintă 15%+. Click pe social și pe recomandări raportate separat (UTM). Rata de deschidere doar orientativ (Apple MPP).

**Trigger și timing (recomandare):**
- **Status comandă „Livrat” + 7 zile**, fereastră 10:00-20:00 ora României; dacă e sâmbătă sau duminică dimineața, OK (momentul de consum e weekendul, discovery secțiunea 2).
- **De ce 7 zile după livrare:** produsul trebuie folosit întâi. Mixurile sunt de mic dejun / weekend; o săptămână include sigur un weekend, deci majoritatea clienților au gătit cel puțin o dată. Mai devreme (2-3 zile) riscăm „încă n-am încercat”; mult mai târziu (14+ zile) entuziasmul scade și ne lovim de replenishment.
- **Rezervă dacă statusul „Livrat” nu vine din magazin în theMarketer:** comandă plasată + 10 zile (presupunând livrare în 2-3 zile) [neverificat: status de livrare sincronizat].
- **Relația cu replenishment (comandă + 14 zile):** livrat + 7 cade în jurul zilei 9-10 de la comandă, deci minim 3-4 zile între cele două emailuri. Dacă livrarea întârzie și se apropie de ziua 14, replenishment se amână 24 de ore (regula: maximum un email de marketing în 24 de ore).
- **Coliziune cu new-customer Email 2** (care conține deja o cerere de recenzie la Livrat + 4-5 zile): nu trimitem două cereri de recenzie. Recomandare: acest email devine cererea de recenzie unică pentru toți cumpărătorii; din new-customer Email 2 se scoate partea de recenzie (întrebarea 1).

**Segment:**
- Intră: cumpărători pe site-ul propriu, pentru acasă, comandă cu status „Livrat”.
- Exclus: cine a lăsat deja recenzie pentru **toate** produsele din comandă; comenzi anulate sau returnate; comenzi Professional / HoReCa (1 kg și 10 kg; recenzia B2B are alt circuit); dezabonați, suprimați; contacte cu reclamație deschisă la suport [neverificat: dacă există câmp].
- Temei: dacă emailul conține recomandări de produs (S4), e email de marketing și cere consimțământ de marketing. Varianta doar cu S1-S2 ar putea merge pe interes legitim post-achiziție, dar o decide clientul cu juristul (întrebarea 6).

**Condiții de ieșire:** recenzie trimisă pentru toate produsele, dezabonare, hard bounce, plângere spam, comandă anulată sau returnată. O dată per comandă; maximum o dată la 60 de zile per contact [neverificat: limită de frecvență per automatizare].

**Reminder:** nu în această etapă. Dacă rata de recenzie e sub 1% după 30 de zile, testăm un reminder scurt la +5 zile, doar către cei care n-au dat click.

**UTM:** `utm_source=email&utm_medium=postpurchase&utm_campaign=request-review&utm_content=<id>`. Valori: `s1-stele`, `s1-cta`, `s3-social-<retea>`, `s4-produs`, `s4-rezerva`.

**Gărzi de siguranță:** plângeri spam sub 0,10%, dezabonări sub 0,5%, hard bounce sub 1%.

---

## 2. Subiecte și preheadere

| # | Subiect | Caractere | Preheader |
|---|---|---|---|
| A **[recomandat]** | Cum au ieșit pancakes? [nou] | 22 | Spune-ne în 10 secunde: un click pe stele și gata. [nou] |
| B | {{FIRST_NAME}}, cum a fost prima tură? [nou] | 27 fără nume (rezervă: „Cum a fost prima tură?”) | Lasă o recenzie și ajuți pe cineva să-și aleagă pofta. [nou] |
| C | Câte stele merită mixul tău? [nou] | 28 | Un click pe stele e destul. Dacă ai și o poză, cu atât mai bine. [nou] |
| D | Pofta ta are o părere? [nou] | 22 | Recenzia ta ajunge lângă alte peste 1.100. [adaptat din site] |
| E | Ne spui cum a fost? [nou] | 19 | Mixurile tale, notate de tine. Durează câteva secunde. [nou] |

De ce A: întrebare directă și caldă, sună a conversație, nu a formular; „cum au ieșit” vorbește despre rezultatul lui, nu despre noi. Risc: cine a cumpărat doar Pizza, Brownie sau Lava Cake. Pentru ei C sau E (neutre pe produs), dacă theMarketer permite subiect condiționat pe categorie [neverificat]; altfel C ca subiect unic.

**Test A/B:** A contra C, câștigător pe **click pe stele / livrate** (proxy pentru recenzie, volum mai mare), confirmat pe rata de recenzie; minimum ~500 livrări pe variantă; sub 0,5 puncte procentuale diferență, fără câștigător.

**Expeditor:** Lucas Bites. **Reply-to:** aceeași adresă ca la celelalte emailuri. Răspunsurile negative care vin pe reply se tratează de suport în 24 de ore.

---

## 3. Structura, de sus în jos

Lățime 600px, o coloană pe mobil. Titluri: `Akrobat, "Arial Narrow", Arial, sans-serif`, majuscule, Black. Text: `Arial, Helvetica, sans-serif`, 16px. Butoane pastilă bulletproof. Reguli de culoare din brief.

**Structură simplificată (feedback client, 14.10.2026):** S0-header, S1-recenzie (portocaliu, balon cu stele, fără poză), (val), S3-social (roz), (val), S4-recomandari (alb, bloc dinamic), S5-footer. Numele secțiunilor din HTML: S1 Review, S2 Social, S3 Recomandări, S4 Footer.

Eliminate: imaginea hero cu mâncare (se repeta între emailuri și era prea mare), blocul dinamic cu produsele din comandă (S2), blocul 4,9 / 1.100 (S2b) și nota de onestitate. Textele lor rămân mai jos, marcate [ELIMINAT], ca alternative.

---

### S0-header

- Identic cu familia (logo `Logo/Logo_LucasBites.png`, centrat, 180px, export 360px).

---

### S1-recenzie (versiunea curentă)

- **Scop:** întrebarea spusă în 2 secunde și primul click, vizibil fără scroll pe mobil.
- **Pattern:** supratitlu mic „script” deasupra unui titlu supradimensionat; hero de mâncare (IQBAR); fundal portocaliu, se încheie cu un **chevron** spre S2 (separator în unghi, ca la IQBAR).
- **Copy:**
  - Supratitlu (mic, minuscule; Plicata ca imagine după licență, până atunci Akrobat Bold): **ei, cum a fost?** [nou]
  - Titlu (H1, 2-3 rânduri, supradimensionat): **CUM AU IEȘIT?** [nou]
  - Text: Ai gătit deja cu mixurile Lucas Bites? Un click și ne spui cum a fost. [nou]
  - **Balon de vorbire** (HTML, negru, text portocaliu, coadă jos-stânga): 5 stele goale (o singură imagine, un singur link spre `{{REVIEW_URL}}` + UTM `s1-stele`; theMarketer nu acceptă nota în URL, deci fără `?rating=`) + text **SPUNE-NE CUM ȚI S-AU PĂRUT** [nou]
  - CTA (pastilă mare): **Lasă o recenzie** → `{{REVIEW_URL}}` + UTM `s1-cta` [nou]
  - Text anterior, mai lung (alternativă): Ai gătit deja cu mixurile Lucas Bites? Spune-ne cum a fost. Un click pe stele e destul, iar părerea ta îi ajută pe alții să-și aleagă pofta.
- **[ELIMINAT] IMG1 (spec):** farfurie cu teanc de pancakes proaspăt făcute, sirop care curge, câteva afine, o furculiță care tocmai a tăiat prima felie. Fără ambalaj, fără text, fără fețe. Fundal alb simplu pentru decupaj.

**Titluri alternative S1:**
1. SPUNE-NE CUM A FOST
2. DĂ-LE O NOTĂ
3. POVESTEȘTE-NE PRIMA TURĂ
4. ARATĂ-NE CÂTE STELE MERITĂ
5. CUM AU IEȘIT? (recomandat; întrebare, nu verb, dar cea mai caldă)

---

### [ELIMINAT] S2-recenzie (BLOC DINAMIC, PLACEHOLDER)

> Scos din email la cererea clientului; păstrat ca alternativă.

> **[PLACEHOLDER: BLOC DINAMIC THEMARKETER, produsele din comanda care a declanșat emailul, cu link de recenzie per produs.]**
> Se inserează din editorul theMarketer (modulul de feedback / recenzii [verificat ca modul, `new-customer-01/copy.md` linia 372]). Sintaxa și numele blocului NU se ghicesc: se iau din editor sau de la suport (întrebarea 2). Câmpurile de mai jos sunt placeholdere generice, nu sintaxă theMarketer.

- **Pattern:** fundal negru (după chevron), fiecare produs într-un **balon de vorbire** (IQBAR), alternat stânga / dreapta, culori portocaliu → roz → turcoaz, text negru. Coada balonului spre imaginea produsului.
- **Copy antet:**
  - Supratitlu mic (portocaliu pe negru): **părerea ta contează** [nou]
  - Titlu (H2, portocaliu pe negru): **NOTEAZĂ-ȚI MIXURILE** [nou]
- **Card produs (se repetă, maximum 4):**
  - Imagine: `{{ORDER_PRODUCT_IMAGE}}` (din feed), în afara balonului
  - Nume: `{{ORDER_PRODUCT_NAME}}`
  - Rând de 5 stele goale (contur negru), fiecare stea e link: `{{REVIEW_URL}}?rating=1..5` dacă formularul acceptă nota în URL [neverificat]; altfel toate stelele duc la `{{ORDER_PRODUCT_REVIEW_URL}}` + UTM `s2-stele`
  - Text mic sub stele: Atinge o stea [nou]
  - CTA (pastilă mică, neagră cu text portocaliu): **Lasă o recenzie** → `{{ORDER_PRODUCT_REVIEW_URL}}` + UTM `s2-cta` [nou]
  - **Fără preț.**
- **Notă de onestitate (sub carduri, 14px):** Spune-ne sincer, cu bune și cu mai puțin bune. Citim tot. [nou]
- **Rezervă când lipsesc datele de produs:** cardurile dispar, rămâne un singur balon:
  - Text: Cum ți s-au părut mixurile Lucas Bites? Ne-ar ajuta mult o recenzie. [nou]
  - CTA (pastilă): **Scrie o recenzie** → `{{SHOP_URL}}/cont/comenzi` sau pagina de recenzii + UTM `s2-rezerva` [neverificat: pagină]
- **Stelele:** imagini (PNG, 2x), nu caractere Unicode și nu emoji; alt text „1 stea” ... „5 stele”. Fără stele pre-umplute (nu sugerăm nota).

**Titluri alternative S2:**
1. NOTEAZĂ-ȚI MIXURILE (recomandat)
2. DĂ-LE STELE
3. SPUNE-LE PE NUME
4. ALEGE CÂTE STELE MERITĂ
5. LASĂ-NE O VORBĂ

---

### [ELIMINAT] S2b-de-ce-conteaza (cifră mare)

> Scos din email la cererea clientului; păstrat ca alternativă.

- **Scop:** arată că recenzia intră într-o comunitate reală; stil Misfits (cifră uriașă, etichetă scurtă).
- **Copy:**
  - Cifră: **4,9** / etichetă: **DIN 5** [din site]
  - Text: Media a peste 1.100 de recenzii lăsate de oameni care, ca tine, au avut poftă. Următoarea poate fi a ta. [adaptat din site + nou]
- **Opțional (după întrebarea 4):** 2-3 baloane cu recenzii reale din theMarketer (text exact, prenume + inițială, doar cu acordul autorului / termenii modulului). Nu se rescriu și nu se aleg doar cele de 5 stele fără mențiune. Până la aprobare: doar cifra.
- **Notă:** 1.100 / 4,9 valabil la 10.10.2026; se actualizează înainte de lansare.

---

### S3-social (urmărire + postează creația)

- **Scop:** transformă clientul mulțumit în conținut: urmărire pe social și poză cu creația lui.
- **Pattern:** fundal roz între două valuri; un **balon de vorbire gol** mare (contur negru) cu textul „aici apare creația ta”, alături de o grilă de 3 poze de mâncare; iconițe sociale ca pastile.
- **Copy:**
  - Supratitlu mic: **arată-ne farfuria** [nou]
  - Titlu (H2, supradimensionat): **POSTEAZĂ-ȚI CREAȚIA** [nou]
  - Text: Ai pus afine, ciocolată, fructe sau ceva ce nu ne-a trecut prin cap? Fă o poză, postează și dă-ne tag {{INSTAGRAM_HANDLE}}, cu {{HASHTAG}}. Ne uităm la toate și le dăm repost pe cele care ne fac poftă. [nou]
  - Text în balon: aici apare creația ta [nou]
  - Pastile social: **Instagram** → `{{INSTAGRAM_URL}}`, **TikTok** → `{{TIKTOK_URL}}`, **Facebook** → `{{FACEBOOK_URL}}` + UTM `s3-social-<retea>` (aceleași linkuri ca în footer; YouTube rămâne doar în footer)
  - Text mic (14px): Dacă îți dăm repost, te întrebăm înainte și menționăm contul tău. [nou]
- **Handle-uri și hashtag:** discovery nu le conține, deci rămân **placeholdere** (`{{INSTAGRAM_HANDLE}}`, `{{HASHTAG}}`). Propunere de hashtag, de confirmat: #eatwhatyoulove (sloganul oficial) [propunere; de verificat dacă nu e deja aglomerat de alte branduri].
- **IMG2-4 (spec):** 3 farfurii diferite, văzute de sus: pancakes cu fructe, clătite rulate, brownie tăiat în pătrate. Fără ambalaj, fără text, fără fețe. Generate sau din shooting, **nu prezentate ca poze de la clienți**.
- **De ce „te întrebăm înainte”:** repostarea pozelor clienților cere acordul lor (drepturi de autor + GDPR, dacă apar persoane).

**Titluri alternative S3:**
1. POSTEAZĂ-ȚI CREAȚIA (recomandat)
2. ARATĂ-NE CE AI GĂTIT
3. FĂ-I O POZĂ ȘI DĂ-NE TAG
4. ÎMPARTE POFTA
5. URMĂREȘTE-NE PENTRU IDEI NOI

---

### S4-recomandari (BLOC DINAMIC, PLACEHOLDER)

> **[PLACEHOLDER: BLOC DINAMIC THEMARKETER DE RECOMANDĂRI, de exemplu „Cumpărate frecvent împreună” [verificat ca tip de recomandare, `new-customer-01/copy.md` linia 299], excluzând produsele din comandă.]**
> Sintaxa NU se ghicește (întrebarea 3). Câmpurile sunt placeholdere generice.

- **Pattern:** fundal alb, grilă 2x2 (o coloană pe mobil), card cu imagine mare, nume, pastilă mică.
- **Copy antet:**
  - Supratitlu mic: **pofta de mâine** [nou]
  - Titlu (H2): **ÎNCEARCĂ ȘI ASTEA** [nou]
- **Card (maximum 4):**
  - Imagine: `{{RECO_PRODUCT_IMAGE}}`; Nume: `{{RECO_PRODUCT_NAME}}`
  - CTA (pastilă mică, turcoaz, text negru): **Vezi mixul** → `{{RECO_PRODUCT_URL}}` + UTM `s4-produs` [nou]
  - **Fără preț** (dacă blocul nu permite ascunderea: întrebarea 3).
- **Rezervă când lipsesc recomandările:**
  - Text: Mai sunt clătite, brownie, lava cake și pizza care așteaptă o tură. [nou, produse din discovery 8b]
  - CTA (pastilă): **Vezi toate mixurile** → `{{SHOP_URL}}/produse` + UTM `s4-rezerva` [din new-customer-01]
- **Sub grilă (14px):** eat what you love [din site, slogan oficial]

**Titluri alternative S4:**
1. ÎNCEARCĂ ȘI ASTEA (recomandat)
2. ALEGE-ȚI POFTA DE AZI [din site, „Alege-ți pofta de azi.”]
3. DESCOPERĂ URMĂTOAREA TURĂ
4. GUSTĂ CEVA NOU
5. PUNE-ȚI ȘI ASTA ÎN COȘ

---

## 4. Footer (S5-footer)

Identic cu W1-W3, new-customer și replenishment (`new-customer-01/copy.md`, secțiunea 4). Nu se modifică nimic fără decizia clientului.

> Lucas Bites · Roșu, Chiajna, Ilfov
> office@lucasbites.ro · +40 731 399 399
>
> Nu mai vrei emailuri de la noi? [Dezabonează-te aici]({{UNSUBSCRIBE_URL}}). Durează un click.
>
> © 2026 Lucas Bites

- Iconițe social (Instagram, TikTok, Facebook, YouTube), aceleași linkuri.
- `{{UNSUBSCRIBE_URL}}` [neverificat: sintaxa]. `List-Unsubscribe` + `List-Unsubscribe-Post` (RFC 8058) active.
- Fraza de consimțământ o adaugă utilizatorul în theMarketer (comentariu marker în HTML).

---

## 5. Etichete CTA (sumar)

| Loc | Etichetă | Destinație |
|---|---|---|
| S1 stele (un link) | Notează cu 1-5 stele (alt) | `{{REVIEW_URL}}` |
| S1 | Lasă o recenzie | `{{REVIEW_URL}}` |
| S3 | Instagram / TikTok / Facebook | `{{INSTAGRAM_URL}}`, `{{TIKTOK_URL}}`, `{{FACEBOOK_URL}}` |
| S4 card | Vezi mixul | `{{RECO_PRODUCT_URL}}` |
| S4 rezervă | Vezi toate mixurile | `{{SHOP_URL}}/produse` |

---

## 6. Alt text

| Imagine | Alt text |
|---|---|
| Logo header | Lucas Bites |
| Stele (S1, o imagine) | Notează cu 1-5 stele |
| IMG2-4 (S3) | Pancakes cu fructe / Clătite rulate / Brownie tăiat în pătrate |
| Balon gol (S3) | `alt=""` (textul e HTML) |
| Produse (S4) | `{{RECO_PRODUCT_NAME}}` |
| Logo footer | Lucas Bites, eat what you love |
| Chevron, valuri, forme decorative | `alt=""` |

---

## 7. Ce am verificat și ce nu

- Toate afirmațiile și cifrele vin din `discovery.md` (secțiunile 1, 3, 4, 8b). Fără citate de recenzii, nume sau handle-uri (nu există în discovery).
- Modulul de feedback / recenzii theMarketer și automatizarea pe status comandă, tipul de recomandare „Cumpărate frecvent împreună”: verificate în `new-customer-01/copy.md` (liniile 299, 372).
- **Neverificat:** blocul cu produsele din comandă + link de recenzie per produs, nota transmisă prin URL, ascunderea prețului, sincronizarea statusului „Livrat”, excluderea celor care au lăsat deja recenzie, subiect condiționat, sintaxa prenumelui și a dezabonării, limita de frecvență.

**Placeholdere generice (nu sunt sintaxă theMarketer):** `{{FIRST_NAME}}`, `{{ORDER_PRODUCT_NAME}}`, `{{ORDER_PRODUCT_IMAGE}}`, `{{ORDER_PRODUCT_REVIEW_URL}}`, `{{REVIEW_URL}}`, `{{RECO_PRODUCT_NAME}}`, `{{RECO_PRODUCT_IMAGE}}`, `{{RECO_PRODUCT_URL}}`, `{{INSTAGRAM_HANDLE}}`, `{{HASHTAG}}`, `{{INSTAGRAM_URL}}`, `{{TIKTOK_URL}}`, `{{FACEBOOK_URL}}`, `{{UNSUBSCRIBE_URL}}`, `{{SHOP_URL}}`.

---

## 8. Întrebări pentru client (și de verificat în theMarketer)

1. **Coliziune cu new-customer Email 2** (cerere de recenzie la Livrat + 4-5 zile): păstrăm acest email ca cerere unică și scoatem recenzia din Email 2?
2. **Blocul de recenzie:** ce bloc / variabile oferă modulul de feedback theMarketer (produse din comandă, link de recenzie per produs, notă preselectată prin URL)? Statusul „Livrat” ajunge din magazin în theMarketer?
3. **Recomandări:** ce tip de bloc folosim („Cumpărate frecvent împreună” sau altul), poate exclude produsele din comandă și poate ascunde prețul?
4. **Recenzii reale în email:** putem afișa 2-3 recenzii existente (text exact, prenume + inițială)? Termenii modulului de recenzii permit asta?
5. **Social:** handle-urile exacte (Instagram, TikTok, Facebook) și un hashtag oficial? Propunerea noastră: #eatwhatyoulove. Faceți repost la creațiile clienților?
6. **Temei legal:** emailul cu recomandări se trimite doar celor cu consimțământ de marketing (recomandarea noastră), sau varianta fără S4 și pe interes legitim?
7. **Program de recenzii:** confirmați că nu oferiți nicio recompensă pentru recenzii (de exemplu puncte de loialitate în theMarketer)? Dacă da, trebuie mențiune „recenzie stimulată”.
