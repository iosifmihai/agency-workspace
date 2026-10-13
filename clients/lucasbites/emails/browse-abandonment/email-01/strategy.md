# Lucas Bites: Browse Abandonment, Email 1, strategie și structură

Autor: Email Marketing Strategist, 13.10.2026. Pentru Copywriter (texte) și UI Designer (layout, limite finale).
Surse: `brief.md` (acest folder), `../README.md`, `discovery.md`, `../../checkout-started/README.md`, `../../checkout-started/email-01/copy.md` + `design-direction.md`, `../../checkout-started/email-02/copy.md`, `../../welcome-01/brief.md`, `image-prompts.md` din welcome 1-3 și checkout-started 1-2, `../../new-customer-01/copy.md` și `../../new-customer-02/copy.md` (lista de rețete de pe propunerea v3, citită acolo la 12-13.10.2026).
Legendă: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [din site actual] = lucasbites.ro actual, [confirmat] = confirmat de client, [propunere] = recomandarea noastră, [neverificat] = funcție theMarketer necitită în documentație, [DE CONFIRMAT CU CLIENTUL].

**Acest document nu conține subiecte și texte finale.** Le scrie Copywriterul, în limitele de mai jos.

**Reguli care rămân din brief:** fără prețuri hardcodate, fără discount, fără urgență falsă („stoc limitat”, „se termină”), fără promisiuni de sănătate sau nutriționale, fără „cel mai bun”, fără „gata în 5 minute” (valabil doar la Pankees, iar produsul vizualizat poate fi oricare), fără „fără E-uri” (Pizza Crust Mix are emulsificator).

---

## 1. Strategie

### Unghiul: inspirație, nu reamintire de coș

Intenția la browse e mult mai mică decât la checkout. Omul nu a ales nimic, doar s-a uitat. Un email de tipul „ai uitat ceva” (tonul din checkout-started) ar fi prea insistent pentru cineva care n-a pus nimic în coș și ar suna ca supraveghere. Emailul de browse răspunde la altă întrebare: **„ce fac, concret, cu mixul ăsta?”**.

De aceea:
- **Reamintirea produsului e scurtă și discretă**: un card, sus, ca omul să-l găsească fără să caute, dar fără să fie tema emailului.
- **Rețetele fac vânzarea.** Ele arată în ce se transformă un mix (o seară de film, o pauză de cafea, un mic dejun de post), ceea ce un card de produs nu poate arăta. Ele acoperă și cazul cel mai des întâlnit la browse: omul nu era sigur că produsul e pentru el. Trei rețete din trei categorii (pancakes, pizza, desert) îi dau trei motive diferite să revină, chiar dacă produsul vizualizat nu l-a convins.
- **USP-urile vin după rețete**, ca răspuns la întrebarea care apare după inspirație: „și de ce de la ei?”. La un public care nu a cumpărat încă, încrederea (recenziile) contează mai mult decât la checkout.
- **Un singur obiectiv de click per secțiune**: produsul (S2), o rețetă (S3), gama (S5). Fără butoane per USP.

### De ce ordinea asta

| Ordine | Secțiune | Motiv |
|---|---|---|
| S1 | Hero scurt, text-led | Spune în 3 secunde de ce primește emailul, fără ton de reproș. Fără imagine mare de hero, ca pe mobil cardul de produs să apară în primul ecran. |
| S2 | Produsul vizualizat (placeholder theMarketer) | Singurul element personalizat. E motivul trimiterii, deci stă sus. Cine s-a hotărât între timp dă click aici și nu mai citește restul. |
| S3 | 3 rețete (1 GIF + 2 foto) | Corpul emailului și partea cea mai lungă. Aici se convinge cine încă ezită. |
| S4 | 3 USP | Închide obiecțiile după ce dorința există. |
| S5 | Închidere + CTA spre gamă | A doua șansă pentru cine nu a dat click pe produs sau pe rețete: toată gama, nu doar ce a vizualizat. |
| S6 | Footer | Identic structural cu familia (welcome, checkout). |

Alternativa (rețetele primele, produsul după ele) e mai „pură” ca inspirație, dar îngroapă singurul element personalizat sub 2-3 ecrane pe mobil. O putem testa ca variantă B după 30 de zile de date, dacă click-urile pe rețete depășesc net click-urile pe produs (vezi KPI).

---

## 2. Timing, segment, priorități, exit

### Trigger

- Eveniment: **vizualizare produs** (pagina unui produs din gama pentru acasă), fără adăugare în coș, fără checkout început și fără comandă în fereastra de așteptare.
- **[neverificat]** Documentația publică theMarketer nu are un articol dedicat pentru o automatizare „produs vizualizat, fără coș”. Are automatizarea de coș abandonat ([knowledge base](https://themarketer.com/resources/knowledge-base/how-to-create-an-automated-cart-abandonment-series)) și tipul de recomandare „Recently viewed” / „Văzute recent” ([product recommendations](https://themarketer.com/features/marketing-automation/product-recommendations/)). Trigger-ul exact și filtrul „fără coș” se verifică în editorul theMarketer (întrebarea 1).
- Se poate trimite doar contactelor **identificate** (email cunoscut, cu cookie de identificare de la o înscriere sau o comandă anterioară). Vizitatorii anonimi nu intră.

### Timing recomandat: 2 ore după ultima vizualizare de produs

- **De ce 2 ore, nu 30 de minute ca la checkout:** la browse intenția e mică, iar un email trimis imediat se simte ca o urmărire. 2 ore lasă timp ca omul să revină singur, să pună în coș sau să înceapă checkout-ul (caz în care intră în checkout-started, care are intenție mai mare și prioritate).
- **De ce nu 24 de ore:** curiozitatea de la browse se stinge repede. După o zi, produsul nu mai e „în cap”, iar emailul devine un newsletter oarecare.
- **Ancora e ultima vizualizare**, nu prima: dacă omul vede 3 produse în 20 de minute, ceasul pornește de la ultimul, iar blocul theMarketer arată produsul (sau produsele) văzute cel mai recent [neverificat: câte produse arată blocul și în ce ordine].
- **Ore de liniște (ca la checkout-started):** dacă momentul trimiterii cade între 22:00 și 08:00 (ora României), emailul așteaptă până la 08:00. Verificarea condițiilor de exit se face din nou chiar înainte de trimitere.
- **Test după 30 de zile [propunere]:** 2 ore vs 24 de ore, câștigătorul ales pe rata de conversie (comenzi atribuite / livrate), nu pe deschideri.
- [DE CONFIRMAT CU CLIENTUL: timing-ul de 2 ore]

### Segment

**Intră:**
- Contacte identificate, cu email valid și **consimțământ de marketing** (abonați la newsletter/ghid sau clienți care au bifat acordul la checkout [confirmat pentru checkout, 12.10.2026]).
- Au vizualizat cel puțin un produs din gama pentru acasă.

**Exclus (verificare la intrarea în flow și chiar înainte de trimitere):**
1. Au adăugat în coș, au început checkout-ul sau au plasat o comandă după vizualizare.
2. Produsul vizualizat e din **gama Professional** (1 kg / 10 kg, HoReCa): tonul și rețetele sunt pentru acasă [DE CONFIRMAT CU CLIENTUL: cum se identifică produsele Professional în feed; aceeași întrebare ca în `new-customer-01`].
3. Au plasat o comandă în **ultimele 7 zile** [propunere]: sunt în flow-ul post-cumpărare și probabil se uită la produs ca să citească instrucțiunile, nu ca să cumpere.
4. Sunt activi în flow-ul Checkout Started.
5. Dezabonați, suprimați, hard bounce, plângere spam.
6. Au primit deja un email Browse Abandonment în ultimele 7 zile (vezi frecvența).

### Frecvență

- **Maximum 1 email Browse Abandonment per contact la 7 zile**, indiferent câte produse vede. Cine navighează des nu primește câte un email după fiecare vizită.
- **Maximum 1 email de marketing din flow-uri per contact la 24 de ore** (aceeași regulă ca în `new-customer-01`).

### Prioritate între flow-uri

Ordinea, de la cea mai mare prioritate: **Checkout Started > New Customer (post-cumpărare) > Browse Abandonment > Welcome**.

| Situație | Ce se întâmplă |
|---|---|
| Vizualizează, apoi începe checkout-ul în cele 2 ore | Iese din Browse, intră în Checkout Started. Nu primește emailul de browse. |
| Primește emailul de browse, apoi începe checkout-ul | Normal: Checkout Started pornește. Regula de 24 de ore nu blochează Checkout Email 1 (30 min), pentru că acolo intenția e cea mai mare [propunere: Checkout Started e singura excepție de la regula de 24 de ore]. |
| E în seria Welcome | Browse are prioritate (semnal de intenție mai proaspăt). Următorul email Welcome se amână cu 24 de ore după trimiterea emailului de browse. Dacă Welcome 1 (ghidul) a plecat în ultimele 24 de ore, emailul de browse așteaptă până se împlinesc 24 de ore, maximum 48 de ore după vizualizare; peste 48 de ore nu se mai trimite. |
| A cumpărat în ultimele 7 zile | Nu intră (excluderea 3). |
| Vizualizează din nou după ce a primit emailul | Nu primește alt email de browse 7 zile (frecvența). |

[DE CONFIRMAT CU CLIENTUL: regulile de prioritate, iar în theMarketer: dacă automatizările se pot exclude reciproc sau se folosește un filtru pe „a intrat în automatizarea X” [neverificat]]

### Exit conditions (ies din flow imediat)

1. Comandă plasată
2. Checkout început (trece în Checkout Started)
3. Adăugare în coș [DE CONFIRMAT CU CLIENTUL: dacă există un flow separat pentru „adăugat în coș, fără checkout”. Dacă nu există, propunem ca adăugarea în coș să NU scoată contactul, ca să nu rămână neacoperit.]
4. Dezabonare
5. Hard bounce
6. Plângere spam

Flow-ul are un singur email; după trimitere, contactul revine în comunicarea obișnuită.

### Conformitate

- Urmărirea vizualizărilor depinde de scriptul theMarketer de pe site. Scriptul trebuie să pornească **doar după acordul pentru cookie-uri** (Legea 506/2004, care transpune Directiva ePrivacy). Fără acord, vizitatorul nu e urmărit și nu intră în flow. [DE CONFIRMAT CU CLIENTUL / dezvoltator: bannerul de cookie-uri blochează scriptul până la acord?]
- Copy-ul nu spune „te-am văzut”, „am observat că...” sau ceva care să sune a supraveghere (vezi S1).
- Dezabonare one-click (`List-Unsubscribe` + `List-Unsubscribe-Post`, RFC 8058), ca în restul flow-urilor.

---

## 3. KPI (ținte orientative, de recalibrat după 30 de zile de date)

| Metrică | Țintă | Alertă |
|---|---|---|
| CTR unic (orice link: produs, rețete, gamă) / emailuri livrate | 5%+ | sub 2% |
| Rată de conversie: comenzi atribuite `utm_campaign=browse_01` (fereastră 72h de la click) / emailuri livrate | 1%+ | sub 0,3% |
| Dezabonări | sub 0,4% | peste 0,6% |
| Plângeri spam | sub 0,05% | peste 0,10% |
| Hard bounce | sub 0,5% | peste 1% |

**Diagnostic (nu ținte):**
- **Ponderea click-urilor pe rețete vs produs** (`reteta_1..3` + `retete_toate` vs `cta_product` / blocul de produs). Dacă rețetele aduc peste jumătate din click-uri, testăm varianta cu rețetele deasupra produsului.
- **GIF vs foto:** CTR pe `reteta_2` (GIF) față de media `reteta_1` și `reteta_3`. Dacă GIF-ul nu aduce mai mult, renunțăm la el la următoarea iterație (costă greutate și timp de încărcare).
- **Comenzi cu alt produs decât cel vizualizat:** dacă sunt multe, rețetele din alte categorii își fac treaba.

Țintele sunt mai mici decât la Checkout Email 1 (8% CTR, 3% recuperare), pentru că intenția e mai mică. Rata de deschidere se citește doar orientativ (Apple MPP o umflă).

---

## 4. Structura pe secțiuni

Limitele de caractere pornesc de la sistemul din `../../checkout-started/email-01/design-direction.md` (măsurate pe Akrobat și pe fallback Arial Bold). UI Designer le confirmă sau le ajustează după layout. Familia vizuală e aceeași (4 culori, Akrobat + Arial, CTA pill, tranziții), cu layout propriu.

**Culoarea hero-ului (pentru UI):** hero-urile folosite până acum: W1 portocaliu, W2 negru, W3 turcoaz, Checkout 1 roz, Checkout 2 portocaliu. Cine trece din browse în checkout le vede pe ultimele două, deci recomandăm altă culoare decât roz și portocaliu pentru S1 [propunere; decide UI].

### S0-logo

| Ce | Detalii |
|---|---|
| Scop | Identificarea expeditorului. |
| Conținut | Logo complet, pe fundalul hero-ului, conform regulilor de fundal din discovery 7. |
| Copy | Fără text. |

### S1-hero (text-led, scurt)

| Ce | Detalii |
|---|---|
| Scop | Spune de ce primește emailul și face trecerea spre produs și rețete. Ton: invitație, nu reamintire. |
| Conținut | Text live pe culoare. Opțional un element decorativ mic (steluțe, o bucată de mâncare decupată), fără imagine mare: cardul de produs trebuie să apară în primul ecran pe mobil (aprox. primii 600-700 px). |
| Copy necesar | Salut cu prenume + fallback; H1; un text scurt. Fără buton (cardul din S2 e primul click). |

| Element | Limită propusă |
|---|---|
| Salut `Hei, {{FIRST_NAME}}!` / fallback `Hei!` | max 25 car. (fallback și la nume peste 19 car., ca la checkout) |
| H1 (Akrobat Black, uppercase) | max 28 car., max 2 rânduri, cuvânt max 12 car. |
| Text (Arial 16/24) | ideal 70-90, max 110 car. |

**Indicații pentru Copywriter:**
- H1 și textul trebuie să meargă pentru **orice produs** din gamă (pancakes, clătite, brownie, lava cake, cookies, pizza). Fără numele produsului, fără „pancakes” în H1.
- Fără „ai uitat”, „ți-a rămas”, „te-am văzut”, „am observat”. Fără „coș”. Unghiul: produsul a stârnit o poftă; uite ce poți face cu ea.
- Textul face legătura spre rețete (promisiunea emailului: idei, nu presiune).
- Vocabular de pe site care se potrivește: „poftă”, „Alege-ți pofta de azi”, „Pentru fiecare poftă există un moment” [din site]. Nu repetați H1-urile din checkout („POFTA TA E ÎNCĂ ÎN COȘ”, „AI UITAT CEVA BUN?”, „NU NE CREDE PE CUVÂNT”).
- Subiect max ~40 car., preheader max 90 car. Fără prenume în subiect (lipsește des). Subiectul nu numește un produs anume.

### S2-produs vizualizat (PLACEHOLDER theMarketer)

| Ce | Detalii |
|---|---|
| Scop | Reamintirea produsului vizualizat. Click direct spre pagina produsului. |
| Conținut | Card alb (contur negru 2px, colțuri rotunjite, ca la cardul de coș din checkout). Înăuntru: blocul de produs pe care **Andreea îl adaugă manual în theMarketer**. În `index-esp.html`: placeholder `[PRODUS VIZUALIZAT THEMARKETER]` între comentariile `THEMARKETER_FEED`. În `index.html` (preview): un card marcat **EXEMPLU**. |
| Copy necesar | Doar eticheta de deasupra blocului (chip) și, condiționat, un buton sub bloc. Nimic din copy nu numește produsul, prețul sau categoria. |

| Element | Limită propusă |
|---|---|
| Etichetă chip (negru, text portocaliu) | max 20 car. |
| Buton sub bloc (doar dacă blocul theMarketer nu are buton propriu) | max 22 car., generic (ex. tip „vezi produsul”), → link-ul produsului din bloc |
| Microcopy sub buton | fără |

**Reguli:**
- Eticheta trebuie să fie neutră și să meargă și la 1, și la mai multe produse afișate (ex. nu „produsul tău”, care sună a cumpărat). Fără „ai văzut”, „te-ai uitat” dacă sună a supraveghere; o formulare de tip „ți-a făcut cu ochiul” sau „pe lista ta de poftă” e mai potrivită tonului [indicație, textul îl decide Copywriterul].
- Prețul îl afișează blocul theMarketer, nu copy-ul. Dacă blocul permite ascunderea prețului, decide clientul [DE CONFIRMAT CU CLIENTUL]. Noi nu scriem niciun preț.
- **Fallback:** dacă blocul nu randează (feed gol, produs scos din stoc), cardul și eticheta se ascund, iar emailul funcționează cu S1 → S3. De aceea textul din S1 nu trimite explicit la „produsul de mai jos”.
- Lățime utilă pentru bloc: aceeași ca la checkout (516 px desktop, 100% mobil), de confirmat de UI.
- UTM: `utm_content=cta_product` pe butonul nostru (dacă există). Pentru link-urile generate de bloc, se verifică dacă moștenesc UTM-ul automatizării din secțiunea „UTM campanie” [verificat în `new-customer-01`: secțiunea există pe fiecare automatizare].

### S3-rețete (secțiunea principală)

| Ce | Detalii |
|---|---|
| Scop | Inspirație. Arată 3 moduri de a folosi gama, din 3 categorii. KPI: click pe rețete. |
| Conținut | Antet + 3 carduri de rețetă (1 GIF + 2 fotografii) + link „Toate rețetele”. Fiecare card: imagine, etichetă de moment, titlul rețetei, rândul „Cu {produs}”, rând de info (moment · timp), CTA. |
| Copy necesar | Supratitlu, H2, un rând de intro; pe card doar ce e publicat pe site (titlu, produs, timp, moment). **Fără ingrediente, pași sau descrieri de gust** (pe v3 nu sunt publicate pentru aceste rețete). |
| Layout | Recomandare: carduri stivuite pe toată lățimea, pe mobil una sub alta (3 coloane fac titlurile prea mici). Pattern-uri deja folosite: cercuri pe un rând (W1), zig-zag (NC1), perechi rețetă + packshot (NC2); UI alege altceva. |

| Element | Limită propusă |
|---|---|
| Supratitlu | max 25 car. |
| H2 (Akrobat Black, uppercase) | max 26 car., max 2 rânduri |
| Intro (Arial 16) | max 70 car. |
| Etichetă moment (pe card) | max 24 car. |
| Titlu rețetă (Akrobat Bold, uppercase) | max 30 car., max 2 rânduri, cuvânt max 12 car. (titlurile de pe site au 25-27 car.) |
| Rând „Cu {produs}” | max 32 car. |
| Rând info (categorie · timp) | max 22 car. |
| CTA pe card (link-buton) | max 16 car. (ex. tip „Vezi rețeta” [din site]) |
| Link sub carduri | max 22 car. (tip „Toate rețetele” [din site]) |

Detaliile rețetelor sunt în secțiunea 5.

### S4-USP

| Ce | Detalii |
|---|---|
| Scop | Răspunde la „de ce de la ei?” după ce pofta există. |
| Conținut | Titlu de secțiune + 3 coloane (desktop) / stivuite (mobil), fiecare cu iconiță, titlu, un rând. Text live. |
| Copy necesar | Titlul secțiunii; 3 x (titlu + rând). |

| Element | Limită propusă |
|---|---|
| Titlu secțiune | max 26 car. (să difere de „DE CE O SĂ-ȚI PLACĂ” din Checkout 1 și „CA SĂ COMANZI LINIȘTIT” din Checkout 2) |
| Titlu USP (Akrobat Bold 20, uppercase) | max 20 car., max 2 rânduri, cuvânt max 12 car. |
| Rând sub titlu (Arial 14) | ideal 35-45, max 50 car. |

Iconițe (UI): altele decât în checkout (acolo: camion, cronometru, spic, cască/plic). Fără bife verzi. Detaliile USP sunt în secțiunea 6.

### S5-închidere + CTA spre gamă

| Ce | Detalii |
|---|---|
| Scop | A doua cale de click pentru cine nu a ales nici produsul, nici o rețetă: toată gama. |
| Conținut | Titlu, un rând, buton, semnătura „eat what you love” [din site, slogan oficial]. Opțional o imagine mică de mâncare (UI decide; dacă da, din altă categorie decât cele 3 rețete sau un detaliu, nu a 4-a rețetă). |
| Copy necesar | Titlu, rând, text buton. |

| Element | Limită propusă |
|---|---|
| Titlu (Akrobat, uppercase) | max 32 car., max 3 rânduri |
| Rând (Arial 16) | max 70 car. |
| Buton | max 22 car. → `{{SHOP_URL}}`, `utm_content=cta_shop` |

Indicații: fără „ÎNCĂ TE GÂNDEȘTI?” (Checkout 1) și „TE AȘTEPTĂM LA MASĂ.” (Checkout 2). Rândul poate numi gama („pancakes, clătite, prăjituri și pizza” [adaptat din site]), dar formularea din Checkout 1 („Răsfoiește toată gama: pancakes, clătite, prăjituri și pizza.”) nu se repetă identic.

### S6-footer

Identic structural cu Checkout 1/2: logo stripes, iconițe social (Instagram, TikTok, Facebook, YouTube, aceleași linkuri ca în `welcome-01/brief.md`), Roșu, Chiajna, Ilfov, office@lucasbites.ro, +40 731 399 399, rândul SRL + CUI ca placeholder [DE PRIMIT DE LA CLIENT], dezabonare `{{UNSUBSCRIBE_URL}}`, © 2026 Lucas Bites.

**Fraza „de ce primești acest email”** nu poate fi cea din checkout („ai început o comandă”). Destinatarii de browse sunt fie abonați, fie clienți cu acord. Propunere: o frază generală de tip „Primești acest email pentru că te-ai abonat la emailurile Lucas Bites” [propunere], sau, ca în `new-customer-01`, fraza o adaugă Andreea separat în theMarketer [DE CONFIRMAT CU ANDREEA].

### Lungime totală

Țintă: aproximativ 150-200 de cuvinte de text live în tot emailul (fără footer), 4-5 ecrane pe mobil. HTML sub 102 KB (Gmail clipping). Greutate imagini totală sub 1,5 MB, din care GIF-ul max 1 MB (vezi secțiunea 5).

---

## 5. Rețetele propuse

### Criterii de selecție

1. Rețeta există pe pagina de rețete a propunerii v3 (lista de 12 rețete citită în `new-customer-01` și `new-customer-02`, cu titlu, produs, timp și moment) [din site].
2. Produsul e confirmat în gamă (`welcome-01/brief.md`, discovery 8b).
3. Nu a fost rețetă sau topping principal în welcome 1-3 și checkout-started 1-2 (verificat în `image-prompts.md` ale lor).
4. Trei categorii diferite, pentru că nu știm ce produs a vizualizat omul.
5. Nicio rețetă cu mențiune nutrițională („Pankees proteice cu iaurt grecesc” rămâne exclusă, ca în `new-customer-02`).

**Ce a fost deja folosit (de evitat):**
- Welcome 1: pancakes cu fructe de pădure și sirop, clătite triunghi cu gem, brownie simplu, tigaia, brunch. Welcome 2: lava cake rupt, pancakes + clătite, budincă, banana bread, pizza întreagă, făină, zahăr. Welcome 3: pancakes buttermilk cu felie scoasă, Classic cu banană și miere, felii de pizza cu legume, brownie stivuit.
- Checkout 1: teanc cu chocolate chips și căpșuni, clătite rulate cu cremă de ciocolată și alune. Checkout 2: mini pancakes în cerc cu zmeură, fursecuri cu ciocolată.
- Post-cumpărare (alt public, dar se poate suprapune): NC1 banane și nuci, afine și sirop, teancul de duminică, clătite pentru toată familia; NC2 Pankees cu ciocolată, pizza cu pepperoni (felie ridicată cu mâna), lava cake cu înghețată de vanilie.

### Setul propus

| # | Rețetă [din site, retete.html] | Produs | Info [din site] | Moment / etichetă | Format |
|---|---|---|---|---|---|
| 1 | **PANKEES DE POST CU FRUCTE** | Vegan Classic Pankees | De post · 15 min | categoria „Vegan / de post” [din site] | Fotografie |
| 2 | **PIZZA DE CASĂ CU PEPPERONI** | Pizza Crust Mix | Familie · 30 min | „movie night” [din site, homepage] | **GIF** (cinemagraph) |
| 3 | **BROWNIE CU FRUCTE DE PĂDURE** | Brownie Mix | Desert · 35 min | „pauza de la birou” [din site, moment] | Fotografie |

**De ce acest set:**
- **Pankees de post cu fructe** aduce un produs care nu a apărut în niciun email (Vegan Classic Pankees a fost doar menționat ca alternativă în NC1) și deschide publicul care ține post (filtrul „Vegan / de post” de pe site). E rețeta de pancakes, deci categoria cea mai vizualizată e acoperită, dar cu un unghi nou. Postul Crăciunului începe pe 15 noiembrie, deci rețeta e relevantă imediat după lansarea flow-ului.
- **Pizza cu pepperoni** e singura rețetă sărată și arată că gama nu e doar dulce. Topping-ul pepperoni nu a apărut în welcome sau checkout (acolo: margherita, legume). E cel mai bun candidat pentru mișcare (mozzarella întinsă, aburi). Imaginea trebuie să difere de NC2 (acolo: felie ridicată de o mână, din lateral).
- **Brownie cu fructe de pădure** acoperă deserturile. Brownie-ul a apărut simplu (W1, W3); varianta cu fructe de pădure deasupra e nouă ca topping principal. În NC1 apare doar ca farfurie mică în hero-ul compus, deci unghiul și compoziția trebuie să difere.

### Formatul vizual (pentru UI Designer și `image-prompts.md`)

| # | Format | Ce arată [propunere, de detaliat de UI] | De ce acest format |
|---|---|---|---|
| 1 | Foto | Teanc scurt de Pankees cu fructe proaspete deasupra, fără unt, frișcă sau miere (rețetă de post). Fructele exacte: [DE CONFIRMAT CU CLIENTUL]. Până la confirmare, fructe care nu au fost topping principal în serie (nu căpșuni, zmeură, afine, banană). | Mișcarea nu adaugă nimic la un teanc; detaliul important e culoarea fructelor. |
| 2 | **GIF / cinemagraph** | Pizza întreagă cu pepperoni, de sus; o felie se desprinde încet cu mozzarella întinsă, sau aburi peste pizza, restul cadrului nemișcat. Fără mână (diferit de NC2). | Mozzarella întinsă e mișcarea care „vinde” singură o pizza. Un cinemagraph (o singură zonă în mișcare) ține GIF-ul mic. |
| 3 | Foto | Un pătrat înalt de brownie, cu fructe de pădure (zmeură, mure, afine) adunate deasupra, 30-45°, alt unghi decât în NC1 (acolo: de sus, în hero compus). | Textura și contrastul ciocolată/fructe se văd bine static. |

**Reguli GIF (pentru UI):**
- Max 1 MB, 2-4 secunde, buclă, max ~15 cadre/secundă, paletă redusă. Export la lățimea de afișare (sau max 1,5x), nu 2x.
- **Primul cadru trebuie să funcționeze singur ca fotografie**: Outlook desktop afișează doar primul cadru.
- Fără text ars în GIF. Fără ambalaje, fără mâini, fără fețe, fără nimic care poate părea UGC.
- Video încorporat nu se folosește (brief). Alternativa e o imagine cu buton play care duce la un video real, doar dacă clientul are un video al acestei rețete (YouTube @lucasbites2267 sau TikTok) [DE CONFIRMAT CU CLIENTUL]. Un video real e preferabil unui video generat.
- Imaginile Higgsfield le generează Andreea/UI după `image-prompts.md`; nu sunt generate în acest pas.

### Linkuri spre rețete

- Pe propunerea v3, toate cardurile de rețetă duc azi la aceeași pagină-șablon (`reteta.html`, banane și nuci) [verificat în `new-customer-02`, 13.10.2026]. Deci linkurile finale depind de lansarea site-ului nou.
- Până atunci, se aplică decizia din `new-customer-02` (13.10.2026): linkurile duc spre paginile de pe site-ul actual. **Atenție:** pe site-ul actual, pizza e „pizza-salami” (nu pepperoni), iar pentru Pankees de post cu fructe și Brownie cu fructe de pădure nu avem URL-uri citite. [DE CONFIRMAT CU CLIENTUL: URL-urile celor 3 rețete; dacă nu există, cardul duce la `{{SHOP_URL}}/retete`.]
- Variabile: `{{URL_RETETA_POST}}`, `{{URL_RETETA_PIZZA}}`, `{{URL_RETETA_BROWNIE}}`.

### Rezerve și variante

| Situație | Înlocuire [din site, retete.html] |
|---|---|
| Clientul nu aprobă rețeta de post sau fructele | **COOKIES CU CIOCOLATĂ NEAGRĂ** · Cu Cookie Mix Dark Chocolate · Desert · 14 min · „gustarea de după școală” (imagine diferită de fursecurile din Checkout 2: de exemplu cookies întregi stivuite, nu rupte) |
| Rotație sezonieră 1 noiembrie - 31 decembrie (opțional) | Rețeta 1 poate deveni **GINGERBREAD PANCAKES** · Cu Classic Pankees · Desert · 15 min · „aroma Sărbătorilor de iarnă” [din site, produs.html] |
| Conținut condiționat după categoria produsului vizualizat [neverificat în theMarketer] | Cardul 1 devine rețeta din categoria vizualizată (fără dubluri cu celelalte două). Fără conținut condiționat, toți primesc setul implicit. Recomandare: pornim cu setul implicit. |

Lava cake (W2, NC2), teancul de duminică, afine și sirop, banane și nuci, clătite pentru toată familia (NC1) și Pankees cu ciocolată (NC2) nu intră în set.

---

## 6. USP-urile propuse

**Ce s-a folosit deja:**
- Checkout 1: TRANSPORT GRATUIT (de la al 2-lea produs) / REPEDE ȘI SIMPLU (mixul are deja aproape tot) / FĂRĂ CONSERVANȚI (ingrediente pe care le recunoști). Transportul pe primul loc.
- Checkout 2: suport (ÎNTREBĂRI? SCRIE-NE.) / TRANSPORT GRATUIT / ȘTII CE E ÎN MIX (fără conservanți, zahăr brun din trestie). Plus secțiune separată de recenzii 4,9 / 1.100.

**Propunerea pentru Browse (în ordinea din email):**

| # | Fapt | Sursă | Formulare de pornire pentru Copywriter | De ce |
|---|---|---|---|---|
| 1 | **4,9 din 5, din peste 1.100 de recenzii** | [din site] [confirmat, valabil la 10.10.2026] | Cifra în titlu, numărul de recenzii în rând. Fără stele per USP dacă UI preferă iconița. | Publicul de browse nu a cumpărat încă: lipsa de încredere e obiecția principală, nu costul livrării. Nu a fost USP în niciun email din abandon (în Checkout 2 e secțiune, nu USP). |
| 2 | **Ingrediente pe care le recunoști, fără conservanți** | [din site] [confirmat] | Unghi nou față de checkout: „ce e în mix” ca titlu scurt; „fără conservanți” poate sta în rând. Nu „fără E-uri”, nu „făină nealbită” (doar pancakes/clătite), nu „zahăr brun” absolut (brownie, Crêpes Original). | Legătură naturală cu rețetele: omul tocmai a văzut ce faci cu mixul, acum află ce e în el. |
| 3 | **Transport gratuit de la al 2-lea produs** | [confirmat, 12.10.2026] | Legat de rețete: două rețete, două mixuri, livrare gratuită. Formulare diferită de „De la al 2-lea produs din coș.” (Checkout 1) și „Când pui al 2-lea produs în coș.” (Checkout 2). Fără „coș” în formulare, ideal. | Rețetele din 3 categorii împing spre 2+ produse; transportul gratuit transformă interesul pentru un al doilea mix într-o decizie ușoară. Ultimul în ordine (în Checkout 1 a fost primul). |

**Diferențierea față de checkout:**
- Față de Checkout 1: alt set (recenzii în loc de „Repede și simplu”), altă ordine (transportul ultimul, nu primul), alte formulări pentru transport și ingrediente, alt titlu de secțiune, alte iconițe.
- Față de Checkout 2: fără suport; recenziile apar ca un singur USP, nu ca secțiune cu citate (citatele din Checkout 2 nu se repetă aici).
- „Repede și simplu” nu e USP aici, pentru că rețetele aleg timpi de 15-35 de minute și ar suna contradictoriu lângă „repede”.

**Alternativă pentru USP 1** (dacă clientul nu vrea cifra de recenzii în emailuri de abandon): **disponibil în magazine**: Kaufland, Carrefour, Dr. Max, Farmacia Tei, Bebe Tei, eMAG, Freshful [din site] [confirmat, listă completă]. Dă încredere (brand prezent la raft), dar poate muta cumpărarea offline, deci o propunem doar ca rezervă [DE CONFIRMAT CU CLIENTUL].

---

## 7. UTM și variabile

**UTM:** `utm_source=email&utm_medium=flow&utm_campaign=browse_01&utm_content=<id>` (aceeași structură ca în checkout-started; se aliniază în secțiunea „UTM campanie” a automatizării theMarketer).

| `utm_content` | Link |
|---|---|
| `cta_product` | Butonul de sub blocul de produs (doar dacă blocul nu are buton propriu); link-urile generate de bloc moștenesc UTM-ul automatizării [de verificat la test] |
| `reteta_1` | Card Pankees de post cu fructe |
| `reteta_2` | Card Pizza de casă cu pepperoni (GIF + titlu + CTA) |
| `reteta_3` | Card Brownie cu fructe de pădure |
| `retete_toate` | Link „Toate rețetele” |
| `cta_shop` | Butonul din S5 |

Link-urile social, `mailto:` și `tel:` nu primesc UTM. Fereastra de atribuire: 72 de ore de la click (ca la checkout).

**Variabile (nume generice, nu sintaxă theMarketer; se înlocuiesc cu tag-urile din editor):**

| Variabilă / placeholder | Unde | Notă |
|---|---|---|
| `{{FIRST_NAME}}` | S1 salut | Fallback „Hei!” dacă lipsește sau are peste 19 car. Nu în subiect. |
| `[PRODUS VIZUALIZAT THEMARKETER]` | S2, între comentariile `THEMARKETER_FEED` | Îl înlocuiește Andreea manual cu blocul theMarketer. Nu e variabilă de copy. |
| `{{URL_RETETA_POST}}`, `{{URL_RETETA_PIZZA}}`, `{{URL_RETETA_BROWNIE}}` | S3 | Fallback: `{{SHOP_URL}}/retete` |
| `{{SHOP_URL}}` | S3 (`/retete`), S5 | URL-ul paginii PRODUSE [DE PRIMIT DE LA CLIENT] |
| `{{UNSUBSCRIBE_URL}}` | S6 | Tag-ul de dezabonare theMarketer [neverificat: sintaxa] |

Copy-ul nu folosește variabile de nume de produs, preț sau categorie.

---

## 8. Întrebări pentru client

1. **Evenimentul de vizualizare:** theMarketer primește evenimentul „produs vizualizat” de pe site? Se poate face o automatizare care pornește la vizualizare și verifică „fără coș / fără checkout / fără comandă”? (Documentația publică nu descrie un flow de browse; de verificat în editor sau cu suportul theMarketer.)
2. **Cookie-uri:** scriptul theMarketer pornește doar după acordul vizitatorului în bannerul de cookie-uri?
3. **Timing:** sunteți de acord cu 2 ore după ultima vizualizare, cu pauză între 22:00 și 08:00?
4. **Blocul de produs:** ce afișează blocul theMarketer (imagine, nume, preț, buton)? Câte produse arată dacă omul a văzut mai multe? Se poate ascunde prețul, și vreți asta?
5. **Adăugat în coș, fără checkout:** există sau va exista un flow separat pentru asta? Dacă nu, cine pune în coș rămâne în Browse (nu iese).
6. **Gama Professional:** cum recunoaștem în feed produsele de 1 kg / 10 kg, ca să le excludem?
7. **Prioritate între flow-uri:** aprobați ordinea Checkout Started > New Customer > Browse > Welcome și regula de maximum un email de marketing din flow-uri la 24 de ore (cu excepția Checkout Started)?
8. **Pankees de post cu fructe:** ce fructe are rețeta? Vegan Classic Pankees e produsul corect pentru ea?
9. **URL-urile rețetelor:** pizza cu pepperoni, brownie cu fructe de pădure și Pankees de post cu fructe vor avea pagini proprii pe site-ul nou? Până atunci, spre ce pagini trimitem (pe site-ul actual pizza e cu salam)?
10. **Video:** aveți un video real cu pizza (sau cu altă rețetă din set) pe YouTube sau TikTok, pe care să-l folosim ca GIF sau ca imagine cu buton play?
11. **USP recenzii:** „peste 1.100 de recenzii, 4,9 din 5” rămâne cifra de folosit la lansare? Sau preferați lista de magazine ca USP?
12. **Transport gratuit:** se aplică și la 2 bucăți din același produs? Există valoare minimă sau excepții? (rămasă deschisă din checkout)
13. **Conținut condiționat:** theMarketer poate schimba o rețetă după categoria produsului vizualizat? (opțional, nu blochează lansarea)
14. **Footer:** fraza „de ce primești acest email” o scriem noi (variantă generală) sau o adăugați din theMarketer, ca la New Customer?
15. **Denumirea SRL, CUI și URL-ul paginii de produse** pentru footer și `{{SHOP_URL}}`.
