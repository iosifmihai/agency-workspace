# Lucas Bites: Website Abandoned, Email 1, strategie și structură

Autor: Email Marketing Strategist, 13.10.2026. Pentru Copywriter (texte) și UI Designer (layout, limite finale).
Surse: `brief.md` (acest folder), `../README.md`, `discovery.md`, `../../browse-abandonment/README.md` + `email-01/strategy.md`, `copy.md`, `design-direction.md`, `image-prompts.md`, `../../checkout-started/email-01/copy.md` (secțiunea 1 și S4) + `email-02/copy.md` (recenzii, USP), `../../welcome-02/brief.md` + `copy.md` (categoriile de pe propunerea v3), `../../welcome-03/brief.md` + `copy.md` (recenziile reale și regulile de citare), `image-prompts.md` din welcome 1-3, new-customer 1-2 și checkout-started 1-2.
Legendă: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [din site actual] = lucasbites.ro actual, [confirmat] = confirmat de client, [propunere] = recomandarea noastră, [neverificat] = funcție theMarketer necitită în documentație, [DE CONFIRMAT CU CLIENTUL].

**Acest document nu conține subiecte și texte finale.** Le scrie Copywriterul, în limitele de mai jos.

**Reguli care rămân din brief:** fără prețuri, fără discount, fără urgență falsă, fără promisiuni de sănătate sau nutriționale, fără „cel mai bun”, fără „gata în 5 minute” (valabil doar la Pankees, iar emailul prezintă toată gama), fără „fără E-uri” (Pizza Crust Mix are emulsificator), fără „făină nealbită” generalizat (doar pancakes și clătite). Linkuri: doar placeholdere, le pune Andreea în theMarketer.

---

## 1. Strategie

### Unghiul: orientare și încredere, nu reamintire

Website Abandoned are **cea mai mică intenție dintre toate flow-urile de abandon**. Ordinea semnalelor:

| Flow | Ce a făcut omul | Ce știm despre el |
|---|---|---|
| Checkout Started | a ales produse și a ajuns la plată | știe ce vrea |
| Browse Abandonment | a deschis pagina unui produs | știe ce l-a atras |
| **Website Abandoned** | **a intrat pe site, dar n-a deschis niciun produs** | **nu știm ce caută; probabil nici el nu știe încă** |

Omul din acest flow n-a ales nimic și nici n-a găsit ceva care să-l facă să dea click pe un produs. Cele mai probabile motive: n-a înțeles repede ce vinde Lucas Bites (mixuri, nu produse gata făcute), nu s-a orientat în gamă sau nu are încă încredere într-un brand pe care nu-l cunoaște. Emailul răspunde, în ordine, la trei întrebări:

1. **„Ce găsesc la voi?”** → categoriile, fiecare cu o imagine de mâncare și un moment de consum. Aici e click-ul principal.
2. **„Le-a mai încercat cineva?”** → recenzii reale, cu cifra 4,9 din 5.
3. **„De ce de la voi?”** → 3 USP-uri, altele decât în flow-urile cu intenție mai mare.

De aceea:
- **Fără niciun produs personalizat** (nu avem ce reaminti) și **fără referire la vizită**. Copy-ul nu spune „ai fost pe site”, „te-am văzut”, „ai plecat fără să...”. Emailul se citește ca un tur scurt al gamei, nu ca o urmărire. La cea mai mică intenție, senzația de supraveghere costă cel mai mult (dezabonări, plângeri).
- **Categoriile vin primele**, imediat sub un hero scurt. Sunt cererea principală a clientului și singurul loc unde omul își poate alege singur drumul. Fiecare categorie e un click separat, deci click-ul ne spune și ce îl interesează (folosit în Email 2).
- **Recenziile vin după categorii**, nu înainte: întâi omul vede ce e, apoi află că alții l-au încercat. La un public care n-a cumpărat, dovada socială contează mai mult decât la checkout, dar nu poate înlocui orientarea.
- **USP-urile sunt de orientare și încredere** (ce e un mix, unde mă găsești), nu de închidere de comandă. Transportul gratuit rămâne ca singur argument comercial, ultimul.
- **Un singur obiectiv per secțiune:** o categorie (S2), toate recenziile (S3), toată gama (S5). Fără butoane per USP.

### De ce ordinea asta

| Ordine | Secțiune | Motiv |
|---|---|---|
| S1 | Hero scurt | Spune în 3 secunde ce e Lucas Bites, fără ton de reproș. Scurt, ca titlul categoriilor să apară în primul ecran pe mobil. |
| S2 | Categorii (5 carduri) | Corpul emailului. Orientare + click principal + semnal de interes pentru Email 2. |
| S3 | Recenzii (cifra + 3 citate) | Încrederea, după ce omul știe ce e. |
| S4 | 3 USP | Răspunde la „ce e un mix?” și „de ce de la ei?”. |
| S5 | Închidere + CTA spre toată gama + rândul Professional | A doua cale de click pentru cine n-a ales o categorie; ieșire discretă pentru proprietarii de HoReCa. |
| S6 | Footer | Identic structural cu familia. |

Alternativa (recenziile primele) are sens doar dacă datele arată că oamenii nu dau click pe categorii pentru că nu au încredere. O testăm ca variantă B după 30 de zile, doar dacă CTR-ul pe categorii e sub țintă și click-ul pe „toate recenziile” e peste medie (vezi KPI).

---

## 2. Timing, segment, priorități, exit

### Trigger

- Eveniment: **vizită pe site** a unui contact identificat, **fără vizualizare de produs, fără adăugare în coș, fără checkout început și fără comandă** în fereastra de așteptare.
- **[neverificat]** Documentația publică theMarketer citită pentru browse nu descrie o automatizare „vizită fără produs vizualizat”. Trigger-ul și filtrul „fără produs vizualizat” se verifică în editorul theMarketer (întrebarea 1). Același statut ca în `../README.md` ([DE CONFIRMAT]).
- Doar contacte **identificate** (email cunoscut, cookie de identificare de la o înscriere sau o comandă anterioară). Vizitatorii anonimi nu intră.
- **Filtru de calitate a vizitei [propunere, neverificat]:** dacă theMarketer permite, intră doar vizitele cu cel puțin 2 pagini văzute sau cel puțin 30 de secunde pe site. O singură pagină deschisă din greșeală nu e semnal. Dacă filtrul nu există, pornim fără el și urmărim dezabonările.
- **Pagini excluse ca trigger [propunere, neverificat]:** vizite doar pe paginile Professional, contact sau termeni. Doar ACASĂ, PRODUSE (listă / categorie), REȚETE și INGREDIENTE pornesc flow-ul.

### Timing Email 1: 4 ore după ultima pagină văzută

- **De ce mai târziu decât browse (2 ore):** intenția e mai mică, iar un email venit repede după o vizită în care omul n-a făcut nimic se simte cel mai tare a urmărire. În plus, fereastra mai lungă îi lasă timp să revină și să deschidă un produs; atunci intră în Browse, care are intenție mai mare și prioritate. Cu 2 ore la browse și 4 ore aici, un om care deschide un produs la 1-2 ore după vizită primește doar emailul de browse.
- **De ce nu 24 de ore:** nu există un produs care să-l țină pe om „în minte”; după o zi, emailul devine un newsletter oarecare, iar legătura cu vizita se pierde.
- **Ancora e ultima pagină văzută**, nu prima: dacă omul revine pe site în cele 4 ore, ceasul pornește din nou.
- **Ore de liniște (ca la Checkout Started și Browse):** dacă momentul trimiterii cade între 22:00 și 08:00 (ora României), emailul așteaptă până la 08:00. Condițiile de exit se verifică din nou chiar înainte de trimitere.
- **Test după 30 de zile [propunere]:** 4 ore vs 24 de ore, câștigătorul ales pe rata de conversie (comenzi atribuite / emailuri livrate), nu pe deschideri.
- [DE CONFIRMAT CU CLIENTUL: timing-ul de 4 ore]

### Timing Email 2: 72 de ore după Email 1

- Email 2 (rețete + recomandări de produse) pleacă la **72 de ore după Email 1**, cu aceleași ore de liniște (22:00-08:00).
- Primesc Email 2 și cei care n-au deschis Email 1 (deschiderile sunt umflate de Apple MPP; nu le folosim ca filtru, ca la Checkout 2).
- Toate excluderile și exit-urile se verifică din nou chiar înainte de trimitere.

### Segment

**Intră:**
- Contacte identificate, cu email valid și **consimțământ de marketing** (abonați la newsletter/ghid sau clienți care au bifat acordul la checkout [confirmat pentru checkout, 12.10.2026]).
- Au vizitat site-ul (vezi trigger) fără produs vizualizat, coș, checkout sau comandă.

**Exclus (verificare la intrarea în flow și chiar înainte de fiecare email):**
1. Au vizualizat un produs, au adăugat în coș, au început checkout-ul sau au plasat o comandă după vizită (trec în flow-ul potrivit sau nu mai au nevoie de email).
2. **Sunt în seria Welcome activă** (de la înscriere până la trimiterea Welcome Email 4, aproximativ ziua 12-14) [propunere]. Motiv: Welcome 2 prezintă deja aceleași 4 categorii (Pancakes & Crêpes, Budinci, Prăjituri, Pizza), iar Welcome 3 recenziile. Un abonat nou care intră pe site din emailul de welcome ar primi aceeași prezentare de două ori în aceeași săptămână. Vezi și „Prioritate”.
3. Au plasat o comandă în **ultimele 30 de zile** [propunere]: sunt în flow-urile post-cumpărare (New Customer), iar o vizită pe site după comandă e de obicei pentru instrucțiuni sau status, nu pentru descoperire. [DE CONFIRMAT CU CLIENTUL: excludem doar ultimele 30 de zile sau toți clienții care au cumpărat vreodată]
4. Sunt activi în Checkout Started sau Browse Abandonment, ori au primit un email din aceste flow-uri în ultimele 7 zile.
5. Au primit deja un flow Website Abandoned în ultimele 30 de zile (vezi frecvența).
6. Contacte marcate B2B / Professional, dacă există un astfel de câmp în theMarketer [neverificat]: conținutul e pentru acasă.
7. Dezabonați, suprimați, hard bounce, plângere spam.

### Frecvență

- **Maximum 1 flow Website Abandoned per contact la 30 de zile.** Cine intră des pe site (de exemplu clienți care caută rețete) nu primește aceeași prezentare a gamei la fiecare vizită. Mai strict decât la Browse (7 zile), pentru că emailul nu are nimic personalizat: a doua oară ar fi identic.
- **Maximum 1 email de marketing din flow-uri per contact la 24 de ore** (aceeași regulă ca în `new-customer-01` și Browse; Checkout Started rămâne singura excepție).

### Prioritate între flow-uri

Ordinea, de la cea mai mare prioritate: **Checkout Started > New Customer (post-cumpărare) > Browse Abandonment > Website Abandoned > Welcome**, cu o precizare: **Website Abandoned nu pornește deloc cât timp contactul e în seria Welcome activă** (excluderea 2).

De ce Website stă sub Browse: semnalul e mai slab (n-a deschis niciun produs) și emailul nu are nimic personalizat. De ce stă peste Welcome, dar nu întrerupe seria: după ce seria Welcome s-a terminat, o vizită nouă e un semnal mai proaspăt decât newsletterul lunar, deci Website are prioritate față de comunicarea obișnuită. În timpul seriei însă, Welcome 2 și 3 fac deja exact munca acestui email (categorii, recenzii), deci întreruperea seriei n-ar aduce nimic nou. Asta e diferit de Browse, unde emailul are un produs personalizat și merită să amâne Welcome cu 24 de ore.

| Situație | Ce se întâmplă |
|---|---|
| Vizitează, apoi deschide un produs în cele 4 ore | Iese din Website, intră în Browse. Nu primește Website Email 1. |
| Primește Website Email 1, dă click pe o categorie și deschide un produs | Iese din Website (exit 1), intră în Browse. Regula de 24 de ore: emailul de browse așteaptă până se împlinesc 24 de ore de la Website Email 1, maximum 48 de ore după vizualizarea produsului; peste 48 de ore nu se mai trimite (aceeași regulă ca între Browse și Welcome). |
| Primește Website Email 1, apoi începe checkout-ul | Iese din Website, Checkout Started pornește normal (excepția de la regula de 24 de ore). |
| E în seria Welcome | Nu intră (excluderea 2). |
| A cumpărat în ultimele 30 de zile | Nu intră (excluderea 3). |
| Revine pe site după ce a primit Email 1, fără produs vizualizat | Rămâne în flow, primește Email 2 la timp. Nu repornește flow-ul (frecvența de 30 de zile). |

[DE CONFIRMAT CU CLIENTUL: ordinea de prioritate și excluderea seriei Welcome. În theMarketer: dacă automatizările se pot exclude reciproc sau se folosește un filtru pe „a intrat în automatizarea X” [neverificat], ca la Browse.]

### Exit conditions (ies din flow imediat, inclusiv între Email 1 și Email 2)

1. Vizualizare de produs (trece în Browse Abandonment)
2. Adăugare în coș [DE CONFIRMAT CU CLIENTUL, aceeași întrebare ca la Browse: există un flow pentru „adăugat în coș, fără checkout”? Dacă nu, adăugarea în coș scoate contactul din Website, iar Browse îl preia doar dacă a văzut și pagina produsului.]
3. Checkout început (trece în Checkout Started)
4. Comandă plasată
5. Dezabonare
6. Hard bounce
7. Plângere spam

După Email 2, contactul revine în comunicarea obișnuită (newsletter lunar).

### Conformitate

- Urmărirea vizitelor depinde de scriptul theMarketer de pe site, care trebuie să pornească **doar după acordul pentru cookie-uri** (Legea 506/2004, care transpune Directiva ePrivacy). Fără acord, vizitatorul nu e urmărit și nu intră în flow. [DE CONFIRMAT CU CLIENTUL / dezvoltator, aceeași întrebare ca la Browse]
- Copy-ul nu menționează vizita (vezi S1).
- Dezabonare one-click (`List-Unsubscribe` + `List-Unsubscribe-Post`, RFC 8058), ca în restul flow-urilor.
- Recenziile: citate exact, nume scurtat la prenume + inițială, cu acordul clientului pentru folosirea numelor (vezi secțiunea 6).

---

## 3. KPI (ținte orientative, de recalibrat după 30 de zile de date)

| Metrică | Țintă | Alertă |
|---|---|---|
| CTR unic (orice link: categorii, recenzii, gamă) / emailuri livrate | 3%+ | sub 1,5% |
| Rată de conversie: comenzi atribuite `utm_campaign=website_01` (fereastră 72h de la click) / emailuri livrate | 0,5%+ | sub 0,15% |
| Micro-conversie: contacte care deschid o pagină de produs în 72h de la click / emailuri livrate | 1,5%+ | sub 0,5% |
| Dezabonări | sub 0,4% | peste 0,6% |
| Plângeri spam | sub 0,05% | peste 0,10% |
| Hard bounce | sub 0,5% | peste 1% |

Țintele sunt mai mici decât la Browse (5% CTR, 1% conversie), pentru că intenția e mai mică. Rata de deschidere se citește doar orientativ (Apple MPP o umflă). Pragurile de dezabonare și plângeri rămân la fel de stricte ca la Browse: un email fără produs personalizat nu are scuza relevanței, deci dacă publicul îl simte ca spam, se vede aici primul.

**Diagnostic (nu ținte):**
- **Distribuția click-urilor pe categorii** (`cat_pancakes`, `cat_prajituri`, `cat_budinci`, `cat_pizza`, `cat_post`). Ne spune ce categorie atrage cel mai mult publicul rece; ordinea cardurilor se rearanjează după 30 de zile, iar categoria cu cele mai multe click-uri devine rețeta 1 implicită în Email 2.
- **Click pe „toate recenziile”** față de click-urile pe categorii. Dacă recenziile aduc peste o treime din click-uri, testăm varianta cu recenziile deasupra categoriilor.
- **Click pe rândul Professional** (`professional`). Dacă e semnificativ, propunem un flow separat B2B.
- **Ponderea micro-conversiilor care trec în Browse:** arată câți dintre cei orientați de Email 1 ajung la un produs. Dacă e mare, Email 1 își face treaba chiar fără comenzi atribuite direct.
- **USP „în magazine”:** o parte din efect poate fi o cumpărare la raft, pe care emailul n-o poate măsura. De aceea nu judecăm acest USP pe comenzi online; dacă clientul preferă vânzarea online, îl înlocuim (secțiunea 7).

---

## 4. Structura pe secțiuni

Limitele de caractere pornesc de la sistemul din `../../browse-abandonment/email-01/strategy.md` și `copy.md` (validate de UI în `design-direction.md`: toate textele au încăput), care la rândul lui vine din Checkout 1 (măsurat pe Akrobat și pe fallback Arial Bold). UI Designer le confirmă sau le ajustează după layout. Familia vizuală e aceeași (4 culori, Akrobat + Arial, CTA pill), cu layout propriu.

**Culoarea hero-ului (pentru UI):** hero-uri folosite până acum: W1 portocaliu, W2 negru, W3 turcoaz, NC1 roz, NC2 portocaliu, Checkout 1 roz, Checkout 2 portocaliu, Browse 1 turcoaz. Negrul a apărut o singură dată (W2) și deloc în flow-urile de abandon. Recomandare: **hero negru, text portocaliu** [propunere; decide UI]. Alternativa: alb, cu un element de culoare puternic.
**Tranziții deja folosite:** valuri (W1-W3), curbă mare (NC1), diagonale (NC2), panou rotunjit (Checkout 1), feston (Checkout 2), boltă (Browse 1). Brief-ul cere altă tranziție. O idee din discovery 7: marginea zdrențuită a benzii din logo-ul „stripes” [propunere; decide UI].
**Layout-uri de categorii deja folosite:** cercuri pe un rând (W1), zig-zag foto + text (W2, chiar pentru aceleași categorii), grid 2 x 2 (W3), arcade numerotate (Browse 1). UI alege altceva (de exemplu un card mare + 4 mici, sau o listă orizontală tip „meniu”).

### S0-logo

| Ce | Detalii |
|---|---|
| Scop | Identificarea expeditorului. |
| Conținut | Logo complet pe fundalul hero-ului, conform regulilor de fundal din discovery 7 (pe negru: logo-ul complet, cu conturul alb vizibil, sau varianta „stripes”). |
| Copy | Fără text. |

### S1-hero (scurt)

| Ce | Detalii |
|---|---|
| Scop | Spune ce e Lucas Bites și face trecerea spre categorii. Ton: invitație și tur al gamei, nu reamintire. |
| Conținut | Text live. Opțional o imagine mică de mâncare sau un element decorativ, fără hero foto mare: pe mobil, antetul S2 trebuie să apară în primul ecran (aprox. primii 600-700 px). |
| Copy necesar | Salut cu prenume + fallback; H1; un text scurt. Fără buton (primul click e o categorie). |

| Element | Limită propusă |
|---|---|
| Salut `Hei, {{FIRST_NAME}}!` / fallback `Hei!` | max 25 car. (fallback și la nume peste 19 car.) |
| H1 (Akrobat Black, uppercase) | max 28 car., max 2 rânduri, cuvânt max 12 car. |
| Text (Arial 16/24) | ideal 70-90, max 110 car. |

**Indicații pentru Copywriter:**
- Fără „ai fost pe site”, „te-am văzut”, „ai plecat”, „ai uitat”, „coș”. Emailul nu știe ce a căutat omul și nu pretinde că știe.
- Textul poate spune pe scurt ce e un mix, din vocabularul aprobat: „Pancakes, clătite, prăjituri și deserturi din mixuri în care e deja aproape tot” [din site], „oricine le poate face, repede” [din site], „Alege-ți pofta de azi” [din site]. „Tu adaugi apă, agiți și gătești” e valabil doar la Pankees, deci nu ca afirmație despre toată gama.
- Nu repetați H1-urile anterioare: „CE FACI CU POFTA ASTA?” (Browse), „POFTA TA E ÎNCĂ ÎN COȘ.”, „NU NE CREDE PE CUVÂNT.” (Checkout), „ALEGE-ȚI POFTA DE AZI.” (titlul categoriilor din W2).
- Subiect max ~40 car., preheader max 90 car. Fără prenume în subiect. Subiectul nu sugerează că știm de vizită.

### S2-categorii (secțiunea principală)

| Ce | Detalii |
|---|---|
| Scop | Orientare în gamă. Fiecare categorie e un click separat. KPI: CTR pe categorii. |
| Conținut | Antet + 5 carduri de categorie + link „toate produsele”. Fiecare card: imagine de mâncare, etichetă de moment, numele categoriei (exact ca pe site), un rând de conținut. Tot cardul e link (imagine + nume + rând), plus un CTA scurt. |
| Copy necesar | Supratitlu, H2, intro; pe card etichetă, nume, rând, CTA. **Fără prețuri, fără ratinguri per categorie** (ratingurile per produs au fost în W2/W3; aici dovada e în S3). |

| Element | Limită propusă |
|---|---|
| Supratitlu | max 25 car. |
| H2 (Akrobat Black, uppercase) | max 26 car., max 2 rânduri |
| Intro (Arial 16) | max 70 car. |
| Etichetă moment (pe card) | max 24 car. |
| Nume categorie (Akrobat Bold, uppercase) | max 18 car. (cel mai lung: „PANCAKES & CRÊPES”, 17) |
| Rând de conținut | max 50 car. (cardurile mici au coloane înguste; ca rândul USP) |
| CTA pe card (link-buton) | max 16 car. |
| Link sub carduri | max 22 car. → `{{SHOP_URL}}`, `utm_content=cat_toate` |

Detaliile categoriilor sunt în secțiunea 5.

### S3-recenzii

| Ce | Detalii |
|---|---|
| Scop | Încredere pentru cineva care nu cunoaște brandul: volumul (cifra) și vocea (citatele). |
| Conținut | Titlu, cifra mare 4,9 / din 5 / stele (doar la medie) / peste 1.100 de recenzii, 3 carduri cu citat, nume, produs. Link „toate recenziile”. |
| Copy necesar | Titlul secțiunii și textul linkului. Cifra și citatele sunt fixe (secțiunea 6). |

| Element | Limită propusă |
|---|---|
| Titlu secțiune (Akrobat, uppercase) | max 24 car., ideal 1 rând. Diferit de „CE SPUN CLIENȚII” (Checkout 2) și „NU DOAR NOI LE LĂUDĂM.” (W3) |
| Cifra | **4,9** + **din 5** [din site] |
| Sub cifră | **peste 1.100 de recenzii** [din site], max 30 car. |
| Citat card mare (toată lățimea) | max 120 car. |
| Citat card mic | max 90 car. |
| Nume | max 16 car. |
| Produs | max 22 car. |
| Link sub carduri | max 26 car. → `{{REVIEWS_URL}}`, `utm_content=recenzii_toate` |

Layout recomandat (ca în Checkout 2, validat): 1 card mare + 2 mici. Citatul de 102 car. merge pe cardul mare. UI poate alege alt aranjament (Checkout 2: carduri albe pe roz; W3: carduri în trepte pe negru), dar nu aceleași două.

### S4-USP

| Ce | Detalii |
|---|---|
| Scop | Răspunde la „ce e un mix?” și „de ce de la ei?”. |
| Conținut | Titlu + 3 coloane (desktop) / stivuite (mobil): iconiță, titlu, un rând. Text live. |
| Copy necesar | Titlul secțiunii; 3 x (titlu + rând). |

| Element | Limită propusă |
|---|---|
| Titlu secțiune | max 26 car. Diferit de „DE CE O SĂ-ȚI PLACĂ” (Checkout 1), „CA SĂ COMANZI LINIȘTIT” (Checkout 2), „DE CE LUCAS BITES?” (Browse 1) |
| Titlu USP (Akrobat Bold 20, uppercase) | max 20 car., max 2 rânduri, cuvânt max 12 car. |
| Rând sub titlu (Arial 14) | ideal 35-45, max 50 car. |

Iconițe (UI): altele decât cele folosite (camion, cronometru, spic, cască/plic în Checkout; stea, bol cu tel, colet în Browse). Fără bife verzi. Detaliile USP sunt în secțiunea 7.

### S5-închidere + CTA spre gamă + rândul Professional

| Ce | Detalii |
|---|---|
| Scop | A doua cale de click pentru cine n-a ales o categorie: toată gama. Plus o ieșire discretă pentru proprietarii de cafenele, restaurante, patiserii. |
| Conținut | Titlu, rând, buton, semnătura „eat what you love” [din site, slogan oficial]. Sub ele, separat vizual (linie subțire sau alt fundal), un rând Professional cu link text. Opțional o imagine mică de mâncare (dacă da, alt subiect decât cele 5 categorii). |
| Copy necesar | Titlu, rând, text buton, rândul Professional și textul linkului. |

| Element | Limită propusă |
|---|---|
| Titlu (Akrobat, uppercase) | max 32 car., max 3 rânduri |
| Rând (Arial 16) | max 70 car. |
| Buton | max 22 car. → `{{SHOP_URL}}`, `utm_content=cta_shop` |
| Rând Professional (Arial 14) | max 110 car. Bază aprobată: „Ai cafenea, restaurant sau patiserie? Aceeași rețetă, porții constante, preparare rapidă în bucătărie.” (102 car.) [adaptat din site, formularea din planul W4] |
| Link Professional (text subliniat) | max 24 car. → `{{PROFESSIONAL_URL}}`, `utm_content=professional` |

Indicații: fără „ÎNCĂ TE GÂNDEȘTI?” (Checkout 1), „TE AȘTEPTĂM LA MASĂ.” (Checkout 2), „POFTA NU SE GRĂBEȘTE.” (Browse 1). Butonul nu repetă „Alege-ți pofta” (Browse 1) și nici „Vezi toate mixurile” (W2/W3).

### S6-footer

Identic structural cu Browse 1 / Checkout 1-2: logo stripes, iconițe social (Instagram, TikTok, Facebook, YouTube, aceleași linkuri ca în `welcome-01/brief.md`), Roșu, Chiajna, Ilfov, office@lucasbites.ro, +40 731 399 399, rândul SRL + CUI ca placeholder [DE PRIMIT DE LA CLIENT], dezabonare `{{UNSUBSCRIBE_URL}}`, © 2026 Lucas Bites.

**Fraza „de ce primești acest email”:** aceeași variantă generală ca la Browse (destinatarii sunt abonați sau clienți cu acord), fără nicio referire la vizită. Dacă la Browse Andreea a decis să o adauge din theMarketer, se aplică la fel aici [DE CONFIRMAT CU ANDREEA].

### Lungime totală

Țintă: aproximativ 180-230 de cuvinte de text live în tot emailul (fără footer și fără citate), 5-6 ecrane pe mobil. HTML sub 102 KB (Gmail clipping). **Fără GIF** (mișcarea rămâne semnătura Browse 1); greutate imagini totală sub 1 MB (5 imagini de categorie + eventual una mică în hero sau S5).

---

## 5. Categoriile

### Ce e confirmat

| Sursă | Categorii |
|---|---|
| Propunerea v3, aprobată (`welcome-02/brief.md`, „Categorii (din site, date aprobate)”) | **Pancakes & Crêpes**, **Budinci**, **Prăjituri**, **Pizza** |
| Propunerea v3 (discovery 1-2) | direcția **PROFESIONAL** (gama Professional, HoReCa) + filtrul **„Vegan / de post”** |
| Site-ul actual (discovery 8b) | Pankees - Crêpes, Brownie / Lava Cake, Cookie Mix, Pizza Mix, Produse de post, Produse profesionale, Îndulcitori naturali |

Emailul folosește structura site-ului nou (v3), cu numele exact de acolo. Din site-ul actual preluăm doar „de post”, care există și pe v3 ca filtru.

### Recomandare: 5 carduri pentru acasă + Professional ca un singur rând în S5

| # | Categorie (nume exact) | Produse confirmate [din site, `welcome-02/brief.md`] | Etichetă de moment (pornire pentru Copywriter) | Hint pentru rândul de conținut | Subiect vizual (doar mâncare) |
|---|---|---|---|---|---|
| 1 | **PANCAKES & CRÊPES** | Classic, Buttermilk, Chocolate Chips, Blueberry, Vegan Classic Pankees; Crêpes Traditional, Crêpes Mix Original | „Duminica fără grabă” sau „micul dejun în familie” [din site, momente] | Pancakes pufoase și clătite subțiri din aceeași categorie; formula W2 („cât timp se face cafeaua”) nu se repetă identic. | Clătite subțiri împăturite în sferturi, stropite cu zeamă de lămâie și zahăr, cu jumătăți de lămâie alături; un teanc mic de pancakes în spate, ușor neclar. Lămâia nu a apărut în niciun email. |
| 2 | **PRĂJITURI** | Brownie Mix, Lava Cake Mix, Banana Bread Mix (NOU), Carrot Cake Mix (NOU) | „Pauza de la birou” [din site, moment] | Patru prăjituri, două noi în gamă; fără a descrie gustul sau ce conține fiecare. | **Carrot cake**: o felie tăiată din chec, cu miezul vizibil, morcov ras și câteva nuci alături. Fără glazură până confirmă clientul dacă mixul are glazură (întrebarea 8). Brownie, lava cake, banana bread și fursecurile au fost deja folosite. |
| 3 | **BUDINCI** | Mix de budincă (NOU) | „Nou în gamă” [din W2] sau un moment de desert | Desert de lingură, nou la Lucas Bites. Nu scriem ce adaugi (lapte sau apă) și nici aroma (întrebare deschisă din W2). | Prim-plan pe o lingură plină de budincă, ridicată dintr-un bol mic negru mat; textura cremoasă e subiectul, fără topping. Diferit de W2 (ceașcă turcoaz cu fructe de pădure, decupată). Culoarea de vanilie, ca în W2, până la confirmarea aromei. |
| 4 | **PIZZA** | Pizza Crust Mix | „Movie night” [din site, moment] | Blatul îl faci tu, topping-ul îl alegi tu („adaugi apă și ulei, apoi pui ce topping vrei” [adaptat, W2]). | 3-4 pizza mici, individuale, pe o tavă, de sus, fiecare cu alt topping (ciuperci, ardei, porumb, măsline), legat de „fiecare cu topping-ul lui” [din site, moment familie]. Diferit de: pizza întreagă margherita (W2), 2 felii cu legume (W3), felie cu pepperoni în mână (NC2), pizza întreagă cu pepperoni (Browse 1). |
| 5 | **DE POST** (filtrul „Vegan / de post” [din site]; pe site-ul actual categoria „Produse de post”) | Vegan Classic Pankees (singurul produs vegan confirmat) | „Vegan / de post” [din site] | Pankees de post, pentru postul Crăciunului (începe pe 15 noiembrie) și pentru cine nu mănâncă produse de origine animală. Fără afirmații de sănătate. | Pancakes de post cu felii de pară și puțină scorțișoară, de sus, pe farfurie de culoare deschisă; fără unt, frișcă, miere. Fructe diferite de Browse 1 (kiwi, mango, rodie) și de toppingurile principale anterioare (căpșuni, zmeură, afine, banană). |

**De ce 5 și de ce acestea:**
- **Cele 4 categorii v3 acoperă toată gama pentru acasă**, iar omul din acest flow nu știe încă ce caută. Toate 4 sunt confirmate și aprobate.
- **„De post” e al 5-lea card** pentru că are un public distinct (cine ține post nu se uită la o gamă cu lapte și ouă dacă nu vede imediat varianta lui), există ca filtru pe site-ul nou și ca categorie pe cel actual, iar flow-ul se lansează aproape de postul Crăciunului. Dacă theMarketer nu poate rula conținut sezonier, cardul rămâne tot anul (postul există și în alte perioade).
- **Ordinea:** Pancakes & Crêpes primul (cea mai mare categorie, cu bestseller-ul Classic), Prăjituri și Budinci (dulce), Pizza (singura sărată, arată că gama nu e doar dulce), De post ultimul (nișă). Se rearanjează după 30 de zile, pe date (KPI).
- **Diferit de W2**, care a arătat aceleași 4 categorii: alt layout, alte imagini (de mai sus), alte etichete și rânduri, plus cardul „De post”. Cei care au văzut W2 sunt oricum excluși cât timp seria Welcome e activă.

**Professional: nu ca card, ci ca un rând în S5.**
- Publicul principal al flow-ului e cel de acasă (75% din vânzări, 20-35 de ani, urban) [confirmat]. Un card Professional (1 kg / 10 kg) între Pancakes și Pizza ar încurca un vizitator de acasă și ar lua locul unei categorii care îl poate converti.
- Totuși, B2B e aproximativ 25% din vânzări [confirmat], iar un proprietar de cafenea care a intrat pe site și n-a găsit pagina potrivită e exact un „website abandoned”. Un rând discret, cu mesajul aprobat („Aceeași rețetă, porții constante, preparare rapidă în bucătărie.” [din site]), costă puțin și îi dă o ieșire. Click-ul (`professional`) ne spune dacă merită un flow B2B separat.

**Nu intră:**
- **Îndulcitori naturali** (site actual): nu apare în gama confirmată pe v3, nu avem produse numite și categoria e aproape de afirmații de sănătate. [DE CONFIRMAT CU CLIENTUL: mai există în gamă?]
- **Cookie Mix** (categorie pe site-ul actual, produs în lista din `welcome-01/brief.md`): în tabelul de categorii v3 nu apare la Prăjituri. Nu îl numim până nu știm unde stă pe site-ul nou (întrebarea 6).
- **Mix de muffins, Mix de gogoși** (în lista de produse din `welcome-01/brief.md`, dar nu în tabelul de categorii v3): nu îi numim (întrebarea 6).

**Reguli pentru imagini (pentru UI și `image-prompts.md`):** Higgsfield, doar mâncare, fără ambalaje, fără text ars, fără fețe, fără nimic care să pară UGC. Toate 5 în același format și aceeași lumină, ca să se citească drept „meniu”. Nu se generează în acest pas. Lista completă a subiectelor deja folosite e în `../../browse-abandonment/email-01/strategy.md` secțiunea 5, plus Browse 1: Pankees de post cu kiwi, mango, rodie; pizza cu pepperoni întreagă (GIF cu aburi); brownie cu fructe de pădure; teanc de clătite subțiri cu zahăr pudră.

---

## 6. Recenziile

### Ce e disponibil (recenzii reale, deja verificate)

Toate recenziile aprobate până acum vin din `welcome-01/brief.md` (Kinga) și `welcome-03/brief.md` (site-ul actual), cu regulile de citare din `welcome-03/copy.md`: citat cuvânt cu cuvânt, doar diacritice corectate și emoji eliminate, prenume + inițiala numelui, fără superlative absolute.

| Autor | Produs | Folosită în |
|---|---|---|
| Kinga L. | Classic Pankees | W1, Checkout 2 |
| Carmen N. | Buttermilk Pankees | W3 (S2), Checkout 2 |
| Luminița B. | Pizza Crust Mix | W3 (S2), Checkout 2 |
| Andreea H. | Classic Pankees | W3 (S3), rezervă în Checkout 2 |
| Irina A. | Pizza Crust Mix | W3 (S3) |
| Irina S. | Classic Pankees | W3 (S3) |
| Gabriela P. | Classic Pankees | W3 (S2) |
| Liliana F. | Brownie Mix | W3 (S2) |

Excluse intenționat (ca în W3 și Checkout 2): Valentina și Roxana H. (superlative), Arabela („perfecte”), Paula P. (ar cere corectură de ortografie).

### Setul propus (zero suprapunere cu Checkout 2)

| Card | Citat (exact, de copiat ca atare) | Car. | Nume | Produs | Sursa în proiect |
|---|---|---|---|---|---|
| Mare (max 120) | „Am folosit amestecul pentru blat de pizza, Pizza Crust Mix, 500g și mi-au ieșit două pizza delicioase!” | 102 | **Irina A.** | Pizza Crust Mix | `welcome-03/copy.md` S3, card 2 [din site actual, diacritice corectate]; original în `welcome-03/brief.md` (Irina Anghel, 03.03.2022) |
| Mic (max 90) | „Clătitele ies foarte pufoase și gustoase. O adevărată plăcere să le faci și să le mănânci” | 89 | **Andreea H.** | Classic Pankees | `welcome-03/copy.md` S3, card 1 [din site actual, diacritice corectate, emoji eliminate]; rezervă în `checkout-started/email-02/copy.md` |
| Mic (max 90) | „Bun. Rețeta este foarte bună” | 28 | **Liliana F.** | Brownie Mix | `welcome-03/copy.md` S2, card 4 [din site actual, diacritice corectate]; original „FLOREA LILIANA”, 26.11.2023 |

**De ce acestea trei:**
- **Se potrivesc cu categoriile din S2:** pizza, pancakes, prăjituri. Pentru cineva care tocmai a văzut gama, citatele confirmă trei categorii diferite, nu de trei ori pancakes.
- **Nicio recenzie din Checkout 2** (Kinga, Carmen, Luminița). Cine trece din Website în Checkout nu vede aceleași citate de două ori.
- **Irina A. pe cardul mare:** e cea mai concretă (produs, gramaj, rezultat: „două pizza”), deci cea mai credibilă pentru un public rece, și singura care cere cardul mare (102 car.).
- Liliana F. e scurtă; UI poate echilibra cardurile mici (citat mai mare ca font, sau carduri de înălțimi diferite).

**Suprapunerea cu Welcome 3 nu se poate evita:** toate cele 5 recenzii aprobate care nu sunt în Checkout 2 au fost folosite în W3. Riscul e mic: cine e în seria Welcome activă e exclus din acest flow, iar între W3 și o vizită ulterioară trec de obicei săptămâni. Pentru recenzii noi, clientul trebuie să aleagă altele de pe site (întrebarea 10).

**Rezervă:**
- Dacă numele „Liliana F.” nu se confirmă (pe site apare „FLOREA LILIANA”, iar ordinea prenume/nume e presupusă în W3): cardul trece pe **Irina S.** · Classic Pankees · „Sunt foarte încântată de aceste produse! Sunt minunate! Voi reveni cu comenzi!” (78 car.) [din site actual], `welcome-03/copy.md` S3, card 3. Se pierde acoperirea categoriei Prăjituri, dar citatul vorbește despre brand în general, ceea ce se potrivește bine unui public care nu cunoaște gama.
- A doua rezervă: **Gabriela P.** · Classic Pankees · „Pufoase și delicioase!” (22 car.), `welcome-03/copy.md` S2.

**Reguli:**
- Fără stele per card (nota fiecărei recenzii nu e verificată; Luminița are 4 stele). Stelele apar doar la media 4,9.
- Cifra 1.100 / 4,9 e valabilă la 10.10.2026 [confirmat]; se verifică în ziua lansării.
- Folosirea numelor (prenume + inițială) depinde de acordul clientului (întrebarea deschisă în W3 și Checkout 2).

---

## 7. USP-urile propuse

**Ce s-a folosit deja în flow-urile de abandon:**
- Checkout 1: TRANSPORT GRATUIT / REPEDE ȘI SIMPLU / FĂRĂ CONSERVANȚI (transportul primul).
- Checkout 2: ÎNTREBĂRI? SCRIE-NE. / TRANSPORT GRATUIT / ȘTII CE E ÎN MIX (+ secțiune de recenzii).
- Browse 1: 4,9 DIN 5 / CE E ÎN MIX / TRANSPORT GRATUIT (transportul ultimul).
- Ingredientele (fără conservanți, ingrediente pe care le recunoști) apar în toate trei, plus W2.

**Propunerea pentru Website (în ordinea din email):**

| # | Fapt | Sursă | Formulare de pornire pentru Copywriter | De ce aici |
|---|---|---|---|---|
| 1 | **Aproape tot e deja în mix; tu adaugi doar ce scrie pe ambalaj** (apă, ulei sau ouă și unt, după produs) | „mixuri în care e deja aproape tot” [din site]; „Ce adaugi tu, scris clar (apă, ulei sau ouă și unt, după produs)” [din site, `welcome-02/brief.md`]; „Tu adaugi doar ce scrie pe ambalaj. Restul e deja în mix.” [adaptat din site, NC1] | Titlu scurt despre „aproape tot e în mix”; rândul spune ce adaugi tu, general. Nu „doar apă” (valabil doar la Pankees), nu „gata în 5 minute”. | E răspunsul la prima neclaritate a unui vizitator care n-a deschis niciun produs: ce e, de fapt, un mix Lucas Bites. În abandon a apărut doar ca adnotare în hero-ul Checkout 1, niciodată ca USP. |
| 2 | **Ne găsești și în magazine:** Kaufland, Carrefour, Dr. Max, Farmacia Tei, Bebe Tei, eMAG, Freshful | [din site] [confirmat, listă completă] | Titlu despre prezența la raft; rândul numește 3-4 magazine + „și altele” (lista completă nu încape în 50 car.). Formularea din rezerva Browse („ÎN MAGAZINE” / „Kaufland, Carrefour, eMAG, Freshful și altele.”) nu se repetă identic. | Pentru un brand necunoscut, „îl vând Kaufland și Carrefour” e o dovadă de încredere diferită de recenzii (instituțională, nu socială), deci completează S3 fără să-l repete. Nefolosit în niciun email. Risc: poate muta cumpărarea la raft (vezi KPI și întrebarea 11). |
| 3 | **Transport gratuit de la al 2-lea produs** | [confirmat, 12.10.2026] | Legat de categorii: două categorii, două mixuri, livrare gratuită. Formulare diferită de „De la al 2-lea produs din coș.” (Checkout 1), „Când pui al 2-lea produs în coș.” (Checkout 2) și „De la al 2-lea mix, ca să încerci două rețete.” (Browse 1). Fără „coș”. | Singurul argument comercial; ultimul, ca la Browse. Un vizitator care tocmai a văzut 5 categorii are un motiv să combine două. |

**Diferențierea:**
- **Față de Checkout 1:** doar transportul se repetă (alt rând, altă poziție: ultimul, nu primul). Fără „Repede și simplu” și fără „Fără conservanți”.
- **Față de Checkout 2:** fără suport, fără ingrediente; recenziile apar ca secțiune proprie cu alte citate.
- **Față de Browse 1:** fără „4,9 din 5” ca USP (aici e în S3, ca secțiune) și fără „Ce e în mix”. USP 1 de aici e despre **ce adaugi tu**, nu despre ce ingrediente conține mixul.
- **Ingredientele lipsesc intenționat:** au fost în toate cele trei emailuri de abandon și în W2. Dacă clientul vrea totuși ingredientele, înlocuiesc USP 2, nu USP 1.

**Alternativă pentru USP 2** (dacă clientul nu vrea să trimită oamenii spre raft dintr-un email care măsoară vânzări online): **Repede și simplu / oricine le poate face** („oricine le poate face, repede” [din site], „Repede și simplu” confirmat pentru toată gama [confirmat, 12.10.2026]), cu altă formulare decât Checkout 1 („REPEDE ȘI SIMPLU”).

---

## 8. UTM și placeholdere

**UTM:** `utm_source=email&utm_medium=flow&utm_campaign=website_01&utm_content=<id>` (aceeași structură ca la Browse și Checkout; se aliniază în secțiunea „UTM campanie” a automatizării theMarketer). Email 2: `utm_campaign=website_02`.

| `utm_content` | Link |
|---|---|
| `cat_pancakes` | Card Pancakes & Crêpes (imagine + nume + CTA) |
| `cat_prajituri` | Card Prăjituri |
| `cat_budinci` | Card Budinci |
| `cat_pizza` | Card Pizza |
| `cat_post` | Card De post |
| `cat_toate` | Link „toate produsele” sub carduri |
| `recenzii_toate` | Link „toate recenziile” (S3) |
| `cta_shop` | Butonul din S5 |
| `professional` | Linkul Professional din S5 |

Linkurile social, `mailto:`, `tel:` și logo-ul nu primesc UTM. Fereastra de atribuire: 72 de ore de la click (ca la Browse și Checkout).

**Tag de interes la click [propunere, neverificat în theMarketer]:** click pe o categorie setează același tag ca în welcome (`INTEREST_PANCAKES`, `INTEREST_PRAJITURI`, `INTEREST_PIZZA`), plus `INTEREST_BUDINCI` și `INTEREST_POST` noi. Email 2 le folosește la alegerea rețetei.

**Placeholdere (nume generice, nu sintaxă theMarketer; Andreea pune linkurile și tag-urile reale):**

| Placeholder | Unde | Notă |
|---|---|---|
| `{{FIRST_NAME}}` | S1 salut | Fallback „Hei!” dacă lipsește sau are peste 19 car. Nu în subiect. |
| `{{CATEGORY_URL_1}}` | S2, Pancakes & Crêpes | |
| `{{CATEGORY_URL_2}}` | S2, Prăjituri | |
| `{{CATEGORY_URL_3}}` | S2, Budinci | |
| `{{CATEGORY_URL_4}}` | S2, Pizza | |
| `{{CATEGORY_URL_5}}` | S2, De post | |
| `{{SHOP_URL}}` | S2 (link sub carduri), S5 (buton) | |
| `{{REVIEWS_URL}}` | S3 | |
| `{{PROFESSIONAL_URL}}` | S5, rândul Professional | |
| `{{UNSUBSCRIBE_URL}}` | S6 | |

Numerotarea `{{CATEGORY_URL_n}}` urmează ordinea cardurilor de mai sus; dacă ordinea se schimbă după 30 de zile, se mută și placeholderele.

---

## 9. Email 2 (de construit ulterior): cum se leagă

- **Timing:** 72 de ore după Email 1, ore de liniște 22:00-08:00, aceleași excluderi și exit-uri (o vizualizare de produs îl scoate și îl trece în Browse).
- **Unghi:** Email 1 a arătat **ce** e în gamă; Email 2 arată **ce faci** cu ea. Pentru cineva care tot n-a deschis un produs după un tur al gamei, o rețetă concretă e următorul pas firesc.
- **Conținut cerut de client:** (1) 2-3 rețete cu produse Lucas Bites, din lista de rețete de pe v3 (ca la Browse și NC), fără cele deja folosite în NC1, NC2 și Browse 1 (de exemplu „Cookies cu ciocolată neagră”, rezervă nefolosită din Browse, sau „Gingerbread pancakes” în sezonul de iarnă); (2) recomandări de produse „care s-ar putea să-ți placă”: blocul theMarketer de tip „Recomandate pentru tine” / „Altele care ți-ar putea plăcea” [verificat ca tip de recomandare în `new-customer-01`], placeholder pe care îl adaugă Andreea.
- **Personalizare [neverificat]:** dacă tag-urile de interes din Email 1 funcționează, rețeta 1 vine din categoria pe care a dat click; fără click, rețeta 1 vine din categoria cu cele mai multe click-uri în flow (vezi KPI).
- **Fără recenzii și USP repetate** din Email 1. Dacă e nevoie de un argument, transportul gratuit, într-un singur rând.
- **Prețurile din blocul de recomandări:** decizia clientului (aceeași întrebare ca la Browse și NC).

---

## 10. Întrebări pentru client (fără URL-uri; linkurile le pune Andreea)

1. **Evenimentul de vizită:** theMarketer poate porni o automatizare la „vizită pe site” pentru un contact identificat și poate verifica „fără produs vizualizat / fără coș / fără checkout / fără comandă”? Se pot filtra vizitele scurte (o singură pagină, sub 30 de secunde) și vizitele doar pe paginile Professional sau contact?
2. **Cookie-uri:** scriptul theMarketer pornește doar după acordul vizitatorului în bannerul de cookie-uri? (aceeași întrebare ca la Browse)
3. **Timing:** sunteți de acord cu 4 ore după ultima pagină văzută pentru Email 1 și 72 de ore după Email 1 pentru Email 2, cu pauză între 22:00 și 08:00?
4. **Prioritate:** aprobați ordinea Checkout Started > New Customer > Browse > Website > Welcome și excluderea din acest flow a contactelor aflate în seria Welcome (pentru că Welcome 2 și 3 au deja categoriile și recenziile)?
5. **Clienții existenți:** excludem doar contactele cu o comandă în ultimele 30 de zile, sau pe toți cei care au cumpărat vreodată?
6. **Categoriile pe site-ul nou:** rămân Pancakes & Crêpes, Budinci, Prăjituri, Pizza (plus Professional)? Unde apar Cookie Mix, Mix de muffins și Mix de gogoși? „Îndulcitori naturali” mai există în gamă?
7. **„De post”:** pe site-ul nou e doar un filtru sau și o pagină proprie? Vegan Classic Pankees e singurul produs de post?
8. **Carrot Cake Mix:** mixul include și glazură? (de asta depinde imaginea categoriei Prăjituri)
9. **Budinci:** ce aromă are mixul de budincă și ce se adaugă la preparare? (rămasă deschisă din W2; până atunci nu le scriem)
10. **Recenzii:** confirmați că putem folosi prenumele + inițiala (Irina A., Andreea H., Liliana F.) și că „Liliana” e prenumele autoarei „FLOREA LILIANA”? Vreți să alegem și recenzii noi de pe site, ca să nu repetăm Welcome 3?
11. **USP „în magazine”:** sunteți de acord să menționăm retailerii într-un email care urmărește vânzarea online? Dacă nu, folosim „Repede și simplu / oricine le poate face”.
12. **Rândul Professional:** e în regulă un rând discret pentru cafenele, restaurante și patiserii în acest email pentru acasă?
13. **Transport gratuit:** se aplică și la 2 bucăți din același produs? Există valoare minimă sau excepții? (rămasă deschisă din Checkout)
14. **Dovada socială:** „peste 1.100 de recenzii, 4,9 din 5” rămâne cifra de folosit la lansare?
15. **Footer:** fraza „de ce primești acest email” o scriem noi (variantă generală) sau o adăugați din theMarketer, ca la Browse / New Customer? Denumirea SRL și CUI.
16. **Email 2, recomandări:** blocul theMarketer afișează prețul? Se poate ascunde, și vreți asta?
