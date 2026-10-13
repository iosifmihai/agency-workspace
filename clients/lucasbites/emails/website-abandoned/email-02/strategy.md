# Lucas Bites: Website Abandoned, Email 2, strategie și structură

Autor: Email Marketing Strategist, 13.10.2026. Pentru Copywriter (texte) și UI Designer (layout, limite finale).
Surse: `brief.md` (acest folder), `../README.md`, `../email-01/strategy.md` (deciziile de flow), `../email-01/copy.md` (inclusiv răspunsurile clientului din 13.10.2026), `../email-01/design-direction.md`, `discovery.md`, `../../browse-abandonment/email-01/strategy.md` (format, limite, rețete), `../../new-customer-01/copy.md` (blocul de recomandări theMarketer, secțiunea 8), `../../new-customer-02/brief.md` (lista celor 12 rețete de pe propunerea v3) + `copy.md`, `image-prompts.md` din welcome 1-3, new-customer 1-2, checkout-started 1-2, browse 1, website 1.
Legendă: [din site] = text aprobat de pe propunerea v3, [din site actual] = lucasbites.ro actual, [confirmat] = confirmat de client, [propunere] = recomandarea noastră, [neverificat] = funcție theMarketer necitită în documentație, [DE CONFIRMAT CU CLIENTUL].

**Acest document nu conține subiecte și texte finale.** Le scrie Copywriterul, în limitele de mai jos.

**Ce rămâne neschimbat din Email 1 (nu se repetă aici, vezi `../email-01/strategy.md`):** trigger, segment și excluderi (secțiunea 2), frecvență, prioritate între flow-uri, exit conditions, conformitate, structura UTM, regulile din brief (fără prețuri, discount, urgență falsă, promisiuni de sănătate, „cel mai bun”, „gata în 5 minute” generalizat, „fără E-uri”, „făină nealbită” generalizat; fără nicio referire la vizită). Mai jos doar ce e specific sau diferit pentru Email 2.

---

## 1. Strategie

### Unghiul: de la orientare la inspirație și recomandare

Email 1 a răspuns la „ce găsesc la voi?” (categorii, recenzii, USP). Email 2 pleacă la 72 de ore după el, deci ajunge doar la cei care **tot n-au deschis niciun produs** (o vizualizare de produs i-a scos din flow și i-a trecut în Browse). Turul gamei nu i-a mișcat. Următorul pas firesc nu e încă un tur, ci două răspunsuri mai concrete:

1. **„Ce fac, concret, cu un mix?”** → 2 rețete Lucas Bites, fiecare cu produsul ei. Rețeta arată rezultatul, nu ambalajul.
2. **„Și eu ce să încerc?”** → recomandări de produse din theMarketer, singurul element personalizat din tot flow-ul.

Email 1 a fost **despre gamă**; Email 2 e **despre ce iese din ea și despre ce ți s-ar potrivi ție**.

### Ce se schimbă față de Email 1

| | Email 1 | Email 2 |
|---|---|---|
| Întrebarea | Ce găsesc la voi? | Ce fac cu el și ce să încerc? |
| Corpul emailului | 5 carduri de categorie | 2 rețete + bloc de recomandări |
| Personalizare | niciuna | blocul de recomandări theMarketer [neverificat: ce semnale folosește] |
| Dovada socială | secțiune de recenzii (3 citate + 4,9) | fără secțiune de recenzii (vezi secțiunea 7) |
| USP | APROAPE TOT E ÎN MIX / ȘI ÎN MAGAZINE / TRANSPORT GRATUIT | alt set, bandă compactă (secțiunea 7) |
| Rândul Professional | da | nu (vezi S5) |
| Mișcare | fără GIF | un GIF opțional, doar pe rețeta sezonieră (secțiunea 5) |
| Lungime | ~190 de cuvinte, 5-6 ecrane | 160-210 de cuvinte, 4-5 ecrane |

### De ce ordinea asta

| Ordine | Secțiune | Motiv |
|---|---|---|
| S1 | Hero scurt | Face trecerea spre rețete. Fără referire la Email 1 (îl primesc și cei care nu l-au deschis). |
| S2 | 2 rețete | Cererea principală a clientului și cârligul emailului: arată în ce se transformă un mix. |
| S3 | Recomandări theMarketer | După inspirație, alegerea: „încearcă unul dintre acestea”. Click direct pe pagina de produs. |
| S4 | 3 USP, bandă compactă | Obiecțiile de cumpărare, după ce există produse concrete pe ecran. |
| S5 | Închidere + CTA spre gamă | A doua cale de click pentru cine n-a ales nici rețeta, nici un produs. |
| S6 | Footer | Identic structural cu Email 1. |

**De ce rețetele înaintea recomandărilor, nu invers (ca la Browse, unde produsul e primul):** la Browse produsul afișat e unul pe care omul l-a deschis deja, deci semnalul e puternic. Aici recomandările nu au un produs vizualizat în spate (în cel mai bun caz categoria pe care a dat click în Email 1), deci sunt mai slabe ca deschidere decât o rețetă. **Test B după 30 de zile** (recomandările deasupra), doar dacă blocul S3 aduce peste jumătate din click-uri.

---

## 2. Timing, segment, exit: doar ce e specific Email 2

- **Timing:** 72 de ore după Email 1, ore de liniște 22:00-08:00, excluderile și exit-urile verificate din nou chiar înainte de trimitere. Primesc și cei care n-au deschis Email 1 (Apple MPP). Toate deja decise în `../email-01/strategy.md`, secțiunea 2.
- **Cine ajunge la Email 2:** doar contactele care, în 72 de ore, n-au vizualizat un produs, n-au pus în coș, n-au început checkout-ul și n-au comandat. Cine a dat click pe o categorie în Email 1 și a deschis un produs e deja în Browse. Deci publicul Email 2 e cel mai „rece” din flow: a primit un tur al gamei și tot n-a deschis un produs. De aici ținta de click pe produs (S3) ca micro-conversie principală.
- **Click pe o recomandare = vizualizare de produs:** contactul iese din Website (exit 1) și intră în Browse. Regula de 24 de ore din Email 1 se aplică la fel: emailul de browse așteaptă până se împlinesc 24 de ore de la Website Email 2, maximum 48 de ore după vizualizare; peste 48 de ore nu se mai trimite. Altfel omul primește în aceeași zi un email cu recomandări și unul cu produsul pe care tocmai l-a deschis din recomandări.
- **Email 2 e ultimul din flow.** După el, contactul revine în comunicarea obișnuită (newsletter lunar). Frecvența de 30 de zile rămâne.
- **Blocul de recomandări gol** (feed indisponibil, niciun rezultat, nici fallback) nu oprește trimiterea: S3 se ascunde, emailul rămâne S1 → S2 → S4 → S5 (vezi S3).

---

## 3. KPI Email 2 (ținte orientative, de recalibrat după 30 de zile)

| Metrică | Țintă | Alertă |
|---|---|---|
| CTR unic (orice link: rețete, recomandări, gamă) / emailuri livrate | 2,5%+ | sub 1% |
| Rată de conversie: comenzi atribuite `utm_campaign=website_02` (fereastră 72h de la click) / emailuri livrate | 0,4%+ | sub 0,1% |
| Micro-conversie: contacte care deschid o pagină de produs în 72h de la click / emailuri livrate | 1,5%+ | sub 0,5% |
| Dezabonări | sub 0,4% | peste 0,6% |
| Plângeri spam | sub 0,05% | peste 0,10% |
| Hard bounce | sub 0,5% | peste 1% |

Ținte puțin sub Email 1 (3% CTR, 0,5% conversie): al doilea email are mai puțină noutate, iar publicul e filtrat la cei care n-au reacționat la primul. Rata de deschidere doar orientativ (Apple MPP). Dezabonările și plângerile se citesc **cumulat pe flow** (Email 1 + Email 2): dacă Email 2 dublează dezabonările lui Email 1, flow-ul e prea insistent și scurtăm sau oprim Email 2.

**Diagnostic (nu ținte):**
- **Click pe rețete vs click pe recomandări** (`reteta_1`, `reteta_2`, `retete_toate` vs blocul S3 + `cta_rec`). Peste jumătate pe recomandări → testăm S3 deasupra S2.
- **Produsele pe care se dă click în blocul S3** (din raportul theMarketer pe produs, dacă există [neverificat]). Arată ce produse atrag publicul rece; dacă sunt mereu aceleași 2-3, pot deveni rețetele următoarei iterații.
- **Ponderea contactelor care primesc fallback-ul** (best sellers) față de recomandările personalizate [neverificat: dacă theMarketer raportează asta]. Dacă aproape toți primesc fallback, blocul nu e de fapt personalizat și îl tratăm ca „cele mai vândute”.
- **Rețeta sezonieră (Gingerbread) vs rețeta de tot anul** în aceeași perioadă și, dacă se face GIF-ul, **GIF vs foto** (ca la Browse).
- **Contribuția incrementală a Email 2:** comenzi atribuite `website_02` / comenzi atribuite `website_01`. Sub 20% după 60 de zile → Email 2 nu-și justifică trimiterea; îl scurtăm (doar recomandări) sau îl oprim.

---

## 4. Structura pe secțiuni

Limitele pornesc de la sistemul din Email 1 și Browse 1 (validat de UI în `design-direction.md` ale lor). UI Designer le confirmă sau le ajustează după layout.

**Recunoscut ca același flow, layout diferit (cerința din brief) [propunere; decide UI]:**
- **Se păstrează (semnătura flow-ului Website):** tranziția cu margine ruptă și dungă de culoare, fotografiile de mâncare pe fața de masă din in deschisă, decupate „din rețetar”, chip-ul negru cu text portocaliu pentru momentul de consum.
- **Se schimbă:** culoarea hero-ului (Email 1: negru; aici altă culoare, de exemplu roz sau portocaliu, cu text negru), secvența de fundaluri (Email 1: negru, turcoaz, alb, roz, negru, alb), layout-ul secțiunii principale (Email 1: 1 card mare + grilă 2 x 2). Pentru rețete: 2 carduri mari, orizontale, de tip „fișă de rețetă” (imagine pe o parte, text pe cealaltă, alternate), pe mobil stivuite. Layout-uri de rețete deja folosite: cercuri (W1), zig-zag (NC1), perechi rețetă + packshot (NC2), arcade (Browse 1).

### S0-logo

Ca în Email 1: logo complet pe fundalul hero-ului, reguli de fundal din discovery 7. Fără text.

### S1-hero (scurt, fără buton)

| Ce | Detalii |
|---|---|
| Scop | Face trecerea spre rețete: de la „ce e în gamă” la „ce faci cu ea”. Ton: invitație, idei, nu urmărire. |
| Conținut | Text live. Fără imagine mare: pe mobil, antetul S2 trebuie să apară în primul ecran. |
| Copy necesar | Salut cu prenume + fallback; H1; un text scurt. |

| Element | Limită |
|---|---|
| Salut `Hei, {{FIRST_NAME}}!` / fallback `Hei!` | max 25 car. (fallback și la nume peste 19 car.) |
| H1 (Akrobat Black, uppercase) | max 28 car., max 2 rânduri, cuvânt max 12 car. |
| Text (Arial 16/24) | ideal 70-90, max 110 car. |

**Indicații pentru Copywriter:**
- **Fără referire la Email 1** („data trecută”, „cum îți spuneam”): îl primesc și cei care nu l-au deschis. Fără „ai fost pe site”, „te-am văzut”, „ai plecat”, „coș”.
- Textul anunță cele două lucruri din email (idei de rețete + câteva mixuri de încercat), fără să numească produse (recomandările diferă de la om la om).
- Nu repetați H1-urile anterioare: „CE PUNEM AZI PE MASĂ?” (Website 1), „CE FACI CU POFTA ASTA?” (Browse), „POFTA TA E ÎNCĂ ÎN COȘ.”, „NU NE CREDE PE CUVÂNT.” (Checkout).
- Subiect max ~40 car., preheader max 90 car., fără prenume în subiect. Subiectul nu sugerează că știm de vizită și nu repetă „Un tur scurt prin mixurile noastre” / „Ce găsești la Lucas Bites” (Website 1) sau „Trei idei pentru pofta de azi” (Browse 1).

### S2-rețete (secțiunea principală)

| Ce | Detalii |
|---|---|
| Scop | Inspirație: ce iese dintr-un mix. KPI: click pe rețete. |
| Conținut | Antet + 2 carduri de rețetă + link „toate rețetele”. Fiecare card: imagine, etichetă de moment, titlul rețetei, rândul „Cu {produs}”, rând de info (categorie · timp), CTA. Tot cardul e link. |
| Copy necesar | Supratitlu, H2, intro; pe card doar ce publică site-ul (titlu, produs, timp, moment). **Fără ingrediente, pași sau descrieri de gust** (v3 nu le publică pentru aceste rețete). |

| Element | Limită |
|---|---|
| Supratitlu | max 25 car. |
| H2 (Akrobat Black, uppercase) | max 26 car., max 2 rânduri |
| Intro (Arial 16) | max 70 car. |
| Etichetă moment (chip) | max 24 car. |
| Titlu rețetă (Akrobat Bold, uppercase) | max 30 car., max 2 rânduri, cuvânt max 12 car. |
| Rând „Cu {produs}” | max 32 car. (cel mai lung: „Cu Cookie Mix Dark Chocolate”, 28) |
| Rând info (categorie · timp) | max 22 car. |
| CTA pe card | max 16 car. (tip „Vezi rețeta” [din site]) |
| Link sub carduri | max 22 car. → `{{RECIPES_URL}}`, `utm_content=retete_toate`. Diferit de „Toate rețetele” dacă a fost folosit identic în Browse/NC. |

Detaliile rețetelor sunt în secțiunea 5.

### S3-recomandări de produse (PLACEHOLDER theMarketer)

| Ce | Detalii |
|---|---|
| Scop | Cererea clientului: produse „care s-ar putea să-ți placă și pe care merită să le încerci”. Click direct pe pagina produsului. KPI: micro-conversia (produs vizualizat). |
| Conținut | Antet (chip + H2 + intro) + blocul de recomandări pe care **Andreea îl adaugă manual în theMarketer**. În `index-esp.html`: `[RECOMANDĂRI PRODUSE THEMARKETER]` între comentariile `THEMARKETER_FEED START` / `THEMARKETER_FEED END`. În `index.html` (preview): 3 carduri marcate **EXEMPLU**. Opțional un buton sub bloc. |
| Copy necesar | Chip, H2, intro; buton doar dacă blocul nu are butoane proprii. **Nimic din copy nu numește un produs, o categorie, un preț sau un număr de produse.** |

| Element | Limită |
|---|---|
| Chip (negru, text portocaliu) | max 20 car. |
| H2 (Akrobat Black, uppercase) | max 26 car., max 2 rânduri |
| Intro (Arial 16) | max 70 car. |
| Buton sub bloc (doar dacă blocul nu are buton propriu) | max 22 car. → `{{SHOP_URL}}`, `utm_content=cta_rec` |

**Indicații pentru eticheta și textul din jur (trebuie să meargă pentru orice produs):**
- Formulări de tip recomandare, nu de tip „știm ce ai căutat”: direcția clientului („s-ar putea să-ți placă”, „merită încercate”) e potrivită. **Interzis:** „pe baza vizitei tale”, „alese după ce ai văzut”, „produsele tale”, „ți-au rămas”.
- Fără număr („3 mixuri”): blocul poate afișa 2, 3 sau 4 produse, după feed.
- Fără categorie („pancakes de încercat”): blocul poate scoate pizza sau brownie.
- Fără legătură explicită cu rețetele de deasupra („mixurile din rețete”): recomandările nu sunt neapărat produsele rețetelor.
- Textul nu trimite la „mai jos” / „de mai jos” în S1 sau S2: dacă blocul nu randează, S3 dispare.

**Fallback:** dacă blocul nu are niciun rezultat (nici personalizat, nici fallback), toată secțiunea S3 (chip, H2, intro, buton) se ascunde [neverificat: dacă theMarketer poate ascunde condiționat o secțiune când grila e goală; altfel, fallback-ul de best sellers din secțiunea 6 trebuie să fie mereu activ, ca grila să nu fie niciodată goală].

Lățime utilă pentru bloc: aceeași ca în Browse (516 px desktop, 100% mobil), de confirmat de UI.

### S4-USP (bandă compactă)

| Ce | Detalii |
|---|---|
| Scop | Obiecțiile de cumpărare, imediat după produse. |
| Conținut | 3 coloane (desktop) / stivuite (mobil): iconiță, titlu, un rând. Fără titlu de secțiune sau cu unul foarte scurt (UI decide; banda e mai compactă decât în Email 1). Text live. |

| Element | Limită |
|---|---|
| Titlu secțiune (opțional) | max 26 car. Diferit de „BINE DE ȘTIUT” (Website 1), „DE CE O SĂ-ȚI PLACĂ”, „CA SĂ COMANZI LINIȘTIT”, „DE CE LUCAS BITES?” |
| Titlu USP (Akrobat Bold 20, uppercase) | max 20 car., **un singur rând** (brief: titluri aliniate pe un rând), cuvânt max 12 car. |
| Rând sub titlu (Arial 14) | ideal 35-45, max 50 car. |

Iconițe (UI): altele decât cele folosite (camion, cronometru, spic, cască, plic, stea, bol cu tel, colet, cană gradată, magazin cu copertină, casă cu inimă). Fără bife verzi. Setul e în secțiunea 7.

### S5-închidere + CTA spre gamă

| Ce | Detalii |
|---|---|
| Scop | A doua cale de click: toată gama. Ultimul email din flow, deci închidere caldă, fără „ultima șansă”. |
| Conținut | Titlu, rând, buton, semnătura „eat what you love” [din site, slogan oficial]. Opțional o imagine mică de mâncare (dacă da, alt subiect decât cele 2 rețete și decât cele 5 categorii din Email 1). |

| Element | Limită |
|---|---|
| Titlu (Akrobat, uppercase) | max 32 car., max 3 rânduri |
| Rând (Arial 16) | max 70 car. |
| Buton | max 22 car. → `{{SHOP_URL}}`, `utm_content=cta_shop` |

Indicații: nu repetați „NU ȘTII DE UNDE SĂ ÎNCEPI?” / „Vezi toată gama” (Website 1), „ÎNCĂ TE GÂNDEȘTI?”, „TE AȘTEPTĂM LA MASĂ.”, „POFTA NU SE GRĂBEȘTE.”, „Alege-ți pofta”, „Vezi toate mixurile”, „Răsfoiește gama”. Fără urgență („ultima zi”, „nu rata”).

**Fără rândul Professional** [propunere]: a fost în Email 1 ca test (`professional`). Un proprietar de HoReCa interesat a avut deja ieșirea lui; în Email 2 ar lungi emailul pentru 25% din public, iar recomandările și rețetele sunt pentru acasă. Îl adăugăm înapoi doar dacă după 30 de zile click-urile `professional` din Email 1 sunt semnificative.

### S6-footer

Identic cu Email 1 (`../email-01/copy.md`, S6), inclusiv fraza „de ce primești acest email” și `{{UNSUBSCRIBE_URL}}`.

### Lungime totală

Țintă: 160-210 de cuvinte de text live (fără footer și fără textul generat de blocul theMarketer), 4-5 ecrane pe mobil. HTML sub 102 KB (Gmail clipping; blocul theMarketer adaugă cod, deci lăsăm marjă: șablonul nostru sub ~85 KB). Imagini: 2 rețete + eventual una mică în S5, sub 1 MB total fără GIF; cu GIF, GIF-ul max 1 MB (reguli GIF din `../../browse-abandonment/email-01/strategy.md`, secțiunea 5). Imaginile produselor vin din feed.

---

## 5. Rețetele

### Ce rămâne nefolosit din lista v3

Pagina de rețete v3 are 12 rețete (titlu, produs, timp, moment), listate în `../../new-customer-02/brief.md`. Situația lor în serie:

| Rețetă [din site] | Produs | Info | Status |
|---|---|---|---|
| Pankees cu banane și nuci caramelizate | Classic Pankees | Mic dejun · 20 min | folosită (NC1) |
| Pancakes cu afine și sirop | Blueberry Pankees | Mic dejun · 10 min | folosită (NC1) |
| Teancul de duminică | Buttermilk Pankees | Familie · 10 min | folosită (NC1) |
| Clătite pentru toată familia | Crêpes Traditional | Familie · 10 min | folosită (NC1) |
| Pankees cu ciocolată | Chocolate Chips Pankees | Desert · 15 min | folosită (NC2) |
| Lava cake cu înghețată de vanilie | Lava Cake Mix | Desert · 12 min | folosită (NC2) |
| Pizza de casă cu pepperoni | Pizza Crust Mix | Familie · 30 min | folosită (NC2, Browse 1) |
| Pankees de post cu fructe | Vegan Classic Pankees | De post · 15 min | folosită (Browse 1) |
| Brownie cu fructe de pădure | Brownie Mix | Desert · 35 min | folosită (Browse 1) |
| Pankees proteice cu iaurt grecesc | Classic Pankees | Mic dejun · 15 min | **exclusă** (mențiune nutrițională, confirmat 13.10.2026 în NC2) |
| **Cookies cu ciocolată neagră** | Cookie Mix Dark Chocolate | Desert · 14 min | **nefolosită** (doar rezervă în NC2 și Browse 1) |
| **Gingerbread Pancakes** | Classic Pankees | Desert · 15 min | **nefolosită** (doar rotație sezonieră propusă în NC2 și Browse 1) |

Rezultat: **doar 2 rețete v3 respectă toate regulile din brief.** De aici decizia de 2 rețete, nu 3. E și lungimea potrivită: emailul are două secțiuni principale (rețete + recomandări), iar 3 rețete + 3 produse ar trece de 5 ecrane pe mobil.

Rețetele de pe site-ul actual cu Muffin Mix și Donut Mix (discovery 8b) nu intră: produsele nu apar în gama confirmată pe v3 (aceeași regulă ca în Email 1, secțiunea 5).

### Setul propus

| # | Rețetă [din site, retete.html] | Rând „Cu ...” | Info [din site] | Etichetă de moment (pornire) | Format | Perioadă |
|---|---|---|---|---|---|---|
| 1 | **GINGERBREAD PANCAKES** (20 car.) | Cu Classic Pankees | Desert · 15 min | „aroma Sărbătorilor de iarnă” [din site, produs.html] (27 car., peste limita de 24: Copywriterul o scurtează, ex. o formulare din aceeași idee) | Foto; **poate fi GIF** | 1 noiembrie - 31 decembrie (aceeași fereastră ca rotația propusă în NC2 și Browse 1) |
| 2 | **COOKIES CU CIOCOLATĂ NEAGRĂ** (27 car.) | Cu Cookie Mix Dark Chocolate | Desert · 14 min | „gustarea de după școală” [din site, moment, ca în rezerva NC2] | Foto | tot anul |

**De ce acest set:**
- **Singurele două rețete v3 nefolosite**, cu produse confirmate în gamă (Classic Pankees; Cookie Mix Dark Chocolate în lista din `welcome-01/brief.md`, cu packshot în `new-customer-02/packshots/`).
- **Două categorii diferite:** pancakes (cea mai mare categorie, bestseller-ul Classic) și prăjituri / deserturi. Pizza și De post au fost deja rețete în Browse 1, pe care publicul de abandon l-a putut primi.
- **Gingerbread se potrivește calendarului de lansare** (flow-ul pornește în toamnă, iar fereastra de sărbători urmează) și aduce un unghi nou pentru cel mai cunoscut produs, Classic Pankees, fără să-l repete ca „mic dejun”.
- **Cookies** aduce un produs care n-a avut încă o rețetă proprie în niciun email (doar imaginea de fursecuri din Checkout 2).

**Atenție la Cookie Mix:** Email 1 (întrebarea 6) a lăsat deschis unde stă Cookie Mix pe site-ul nou, iar răspunsul din 13.10.2026 nu l-a acoperit. Rețeta și produsul sunt însă pe pagina de rețete v3 (text aprobat), deci riscul e mic. Numele exact diferă între surse: „Cookie Mix Dark Chocolate” (rețete v3) vs „Cookie Mix Dark Chocolate Chip” (lista din `welcome-01/brief.md`) [DE CONFIRMAT CU CLIENTUL, întrebarea 3]. Până la răspuns, Copywriterul folosește forma de pe pagina de rețete.

### Slotul 1 în afara ferestrei 1 noiembrie - 31 decembrie

Gingerbread e etichetată pe site ca rețetă de sărbători, deci nu rulează tot anul. Pentru restul anului:
1. **Preferat:** o rețetă nouă de la client pentru un produs fără rețetă în serie (Banana Bread Mix, Carrot Cake Mix, Mix de budincă sau Crêpes Mix Original) [DE CONFIRMAT CU CLIENTUL, întrebarea 1]. Ar acoperi și produsele noi din gamă.
2. **Rezervă până atunci:** **CLĂTITE PENTRU TOATĂ FAMILIA** · Cu Crêpes Traditional · Familie · 10 min · „duminica fără grabă” [din site], cu **imagine nouă** (alta decât platoul de clătite rulate din NC1 și clătitele cu lămâie din Website 1). E o excepție de la brief și trebuie aprobată de Andreea: rețeta a fost card în NC1, dar NC1 merge doar la cumpărători, iar Website exclude cumpărătorii din ultimele 30 de zile, deci suprapunerea reală de public e cea mai mică dintre toate rețetele folosite (față de Browse 1, care are exact același public de abandon).
3. Dacă theMarketer nu poate programa conținut pe date [neverificat], schimbarea se face manual de Andreea în automatizare, pe 1 noiembrie și pe 1 ianuarie.

**Fără rețete condiționate după click-ul din Email 1** [propunere]: cu doar 2 rețete eligibile, o rețetă „din categoria pe care ai dat click” ar cere reluarea rețetelor deja folosite. Personalizarea stă în blocul de recomandări (secțiunea 6), unde feed-ul are toată gama.

### Formatul vizual (pentru UI Designer și `image-prompts.md`)

| # | Format | Ce arată [propunere; detaliază UI] | De ce |
|---|---|---|---|
| 1 Gingerbread | Foto; **GIF opțional** (cinemagraph) | Teanc scurt de pancakes, de culoare ceva mai caldă, cu un strat fin de zahăr pudră și 1-2 batoane de scorțișoară alături. Pentru GIF: zahăr pudră care cade încet peste teanc, restul cadrului nemișcat; primul cadru funcționează singur ca fotografie (Outlook). **Ce conține rețeta nu e publicat pe v3**: condimentele și topping-ul din imagine sunt [DE CONFIRMAT CU CLIENTUL, întrebarea 2]; până la răspuns, imaginea rămâne minimală (fără sirop, fără fructe, fără biscuiți în formă de om). | Mișcarea „ninsorii” de zahăr pudră spune „sărbători” fără text și fără recuzită inventată. GIF-ul are sens doar pe rețeta sezonieră; Email 1 n-a avut GIF, deci flow-ul nu devine „al doilea Browse”. Dacă GIF-ul nu se face, foto e suficient. |
| 2 Cookies | Foto | 4-5 cookies întregi cu bucăți mari de ciocolată neagră, stivuite sau ușor suprapuse, pe aceeași față de masă din in ca în Website 1, 30-35°. **Niciun cookie rupt** (Checkout 2: 3 fursecuri, unul rupt cu ciocolata topită; NC1 img9, negenerat: de sus, unul rupt). | Textura bucăților de ciocolată se vede bine static. |
| Clătite (doar rezerva de tot anul) | Foto | De stabilit de UI, diferit de: clătite rulate cu cremă (Checkout 1), platou cu clătite rulate (NC1), clătite în sferturi cu lămâie (Website 1), clătite triunghi cu gem (W1), teanc cu zahăr pudră (Browse 1 S5). | |

Reguli comune (din brief și Email 1): Higgsfield, doar mâncare, fără ambalaje inventate, fără oameni sau mâini, fără text ars; aceeași suprafață (in deschis) și lumină ca în Website 1, ca flow-ul să se citească unitar. Imaginile nu se generează în acest pas.

### Linkuri spre rețete

Pe v3, toate cardurile de rețetă duc azi la aceeași pagină-șablon (verificat în NC2, 13.10.2026). Andreea pune linkurile finale; până la lansarea site-ului nou se aplică decizia din NC2 (paginile de pe site-ul actual, unde există). Dacă o rețetă nu are pagină, cardul duce la `{{RECIPES_URL}}`.

---

## 6. Blocul de recomandări: logica recomandată (de setat de Andreea în theMarketer)

**Ce știm:** theMarketer are blocul „Grilă de produse personalizată”, utilizabil și în automatizări, cu tipuri ca „Recomandate pentru tine”, „Cumpărate frecvent împreună”, „Altele care ți-ar putea plăcea”, plus rezultate de rezervă (fallback) configurabile; setările permit ascunderea titlului, brandului, numelui, ratingului sau reducerii, **dar ascunderea prețului nu e menționată** [verificat în documentație, `../../new-customer-01/copy.md`, secțiunea 8]. Ce semnale folosește „Recomandate pentru tine” pentru un contact fără produs vizualizat și fără comandă, nu știm [neverificat].

**Recomandarea [propunere]:**

| Nivel | Logică | Când se aplică | Status |
|---|---|---|---|
| 1. Implicit (de la lansare) | **„Recomandate pentru tine”** | pentru toți; theMarketer folosește ce istoric are contactul (navigare, emailuri) | tipul [verificat]; semnalele [neverificat] |
| 2. Fallback (obligatoriu) | **Cele mai vândute** din gama pentru acasă (sau, dacă theMarketer nu oferă best sellers ca fallback, o selecție manuală fixă de 3 produse aleasă de client) | când „Recomandate pentru tine” nu are destule rezultate, cazul cel mai probabil la acest public | fallback-ul [verificat că se poate configura]; opțiunea „best sellers” [neverificat] |
| 3. Opțional, faza 2 | **Grilă filtrată pe categoria din click-ul din Email 1**: cine a dat click pe `cat_pancakes` vede produse din Pancakes & Crêpes etc., prin tag-urile `INTEREST_*` propuse în Email 1 și conținut condiționat | doar dacă tag-ul la click și conținutul condiționat funcționează; altfel nivelul 1 + 2 | [neverificat] |

**De ce nu celelalte tipuri:** „Văzute recent” e gol prin definiție (omul n-a deschis un produs). „Cumpărate frecvent împreună” și „Altele care ți-ar putea plăcea” pornesc de la o comandă, pe care acest public nu o are.

**Setări recomandate pentru grilă:**
- **3 produse** (o linie pe desktop; pe mobil stivuite sau 1 + 2). Patru dacă layout-ul UI e grilă 2 x 2.
- **Exclus:** gama Professional (1 kg / 10 kg), produse fără stoc [neverificat: filtre disponibile; întrebarea despre identificarea Professional e deja deschisă în Browse].
- **Opțional:** excluderea produselor din cele 2 rețete (Classic Pankees, Cookie Mix), ca să nu apară de două ori [neverificat]; dacă nu se poate, dublura e acceptabilă.
- **Preț:** decizia clientului (întrebarea 16 din Email 1, încă deschisă). Dacă prețul nu se poate ascunde, regula „fără prețuri” se aplică doar copy-ului nostru; prețul din feed vine din sistem și e actualizat automat.
- **Rating per produs:** ascuns, dacă ratingul din feed nu vine din aceleași recenzii verificate ca cifra 4,9 / 1.100; afișat, dacă vine (întrebarea 4).
- **Linkuri:** verificat la test că linkurile generate de bloc moștenesc UTM-ul automatizării (`utm_campaign=website_02`) din secțiunea „UTM campanie” [secțiunea există, verificat în NC1; moștenirea de verificat la test].

---

## 7. USP sau recenzii: decizia

**Fără secțiune de recenzii.** Email 1 a avut-o deja (3 citate + 4,9), iar toate recenziile aprobate rămase sunt deja folosite în Welcome 3, Checkout 2 sau Website 1. O a doua secțiune de recenzii la 72 de ore ar repeta fie citatele, fie mesajul. Acordul pentru prenume + inițială (13.10.2026) rămâne valabil pentru recenzii noi, dacă clientul alege altele de pe site (întrebarea 5); atunci le putem testa în locul benzii USP.

**Cu o bandă compactă de 3 USP**, pentru că S3 pune produse concrete pe ecran, iar obiecțiile de cumpărare apar acum, nu la turul gamei:

| # | Fapt | Sursă | Formulare de pornire pentru Copywriter | De ce aici |
|---|---|---|---|---|
| 1 | **Simplu de făcut, oricine le poate face** | „oricine le poate face, repede” [din site]; „Repede și simplu” confirmat pentru toată gama [confirmat, 12.10.2026] | Accent pe simplitate, nu pe viteză. Diferit de „REPEDE ȘI SIMPLU” (Checkout 1) și de alternativa „SIMPLU DE FĂCUT” scrisă în Website 1 (nefolosită acolo, deci se poate prelua). Fără „gata în 5 minute”. | Se leagă direct de rețete: omul tocmai a văzut ce iese; obiecția firească e „îmi iese și mie?”. Timpii rețetelor (14-15 min) nu contrazic „simplu” (Browse a evitat „repede” din cauza brownie-ului de 35 min). |
| 2 | **Ingrediente pe care le recunoști, fără conservanți** | [din site] [confirmat] | Formulare nouă față de „FĂRĂ CONSERVANȚI” (Checkout 1), „ȘTII CE E ÎN MIX” (Checkout 2), „CE E ÎN MIX” (Browse 1). Nu „fără E-uri”, nu „făină nealbită”, nu „zahăr brun” absolut (Cookie Mix are ciocolată, ca brownie). | Email 1 l-a lăsat intenționat deoparte; pentru cineva care decide acum între produse, „ce e în mix” e argumentul care lipsea din flow. |
| 3 | **Transport gratuit de la al 2-lea produs** | [confirmat, 12.10.2026] | Legat de recomandări (alegi două, livrarea e gratuită). Altă formulare decât Checkout 1, Checkout 2, Browse 1 și Website 1 („Când combini două mixuri, livrarea e pe noi.”). Fără „coș”. | Singurul argument comercial; recomandările afișează mai multe produse, deci împinge spre 2+. Ultimul, ca în Browse și Website 1. |

**Față de Email 1:** se repetă doar transportul (inevitabil, e singurul argument comercial), cu altă formulare. Nu se repetă „APROAPE TOT E ÎN MIX” și nici „ȘI ÎN MAGAZINE”: lista de retaileri a fost aprobată ca USP (13.10.2026), dar a fost deja în Email 1 și, la un email care împinge spre pagina de produs, ar trimite omul spre raft.

**Alternativă pentru USP 2** (dacă clientul vrea să evite încă un USP de ingrediente în seria de abandon): **4,9 din 5, din peste 1.100 de recenzii** [din site] [confirmat], ca USP (nu ca secțiune), cu altă formulare decât Browse 1.

---

## 8. UTM și placeholdere

**UTM:** `utm_source=email&utm_medium=flow&utm_campaign=website_02&utm_content=<id>` (structura din Email 1).

| `utm_content` | Link |
|---|---|
| `reteta_1` | Card rețetă 1 (Gingerbread; în afara ferestrei, rețeta de tot anul) |
| `reteta_2` | Card Cookies cu ciocolată neagră |
| `retete_toate` | Link spre pagina de rețete (S2) |
| `rec_feed` | Linkurile generate de blocul theMarketer (moștenite din „UTM campanie”, de verificat la test) |
| `cta_rec` | Butonul de sub bloc (doar dacă blocul nu are butoane proprii) |
| `cta_shop` | Butonul din S5 |

`reteta_1` rămâne același id și când rețeta din slot se schimbă; perioada se citește din data click-ului. Linkurile social, `mailto:`, `tel:` și logo-ul nu primesc UTM. Fereastra de atribuire: 72 de ore de la click.

**Placeholdere (nume generice, nu sintaxă theMarketer; Andreea pune linkurile reale):**

| Placeholder | Unde | Notă |
|---|---|---|
| `{{FIRST_NAME}}` | S1 salut | Fallback „Hei!” dacă lipsește sau are peste 19 car. Nu în subiect. |
| `{{URL_RETETA_GINGERBREAD}}` | S2, card 1 (noiembrie-decembrie) | Fallback `{{RECIPES_URL}}` |
| `{{URL_RETETA_CLATITE}}` | S2, card 1 (restul anului, doar dacă se aprobă rezerva) | Fallback `{{RECIPES_URL}}` |
| `{{URL_RETETA_COOKIES}}` | S2, card 2 | Fallback `{{RECIPES_URL}}` |
| `{{RECIPES_URL}}` | S2, link sub carduri | Pagina REȚETE (în Browse 1 notată `{{SHOP_URL}}/retete`) |
| `[RECOMANDĂRI PRODUSE THEMARKETER]` | S3, între `THEMARKETER_FEED START` / `END` | Îl înlocuiește Andreea cu blocul theMarketer. Nu e variabilă de copy. |
| `{{SHOP_URL}}` | S3 (buton opțional), S5 | |
| `{{UNSUBSCRIBE_URL}}` | S6 | |

Copy-ul nu folosește variabile de nume de produs, preț sau categorie.

---

## 9. Întrebări pentru client (fără URL-uri; linkurile le pune Andreea)

1. **Rețete pentru tot anul:** pe site-ul nou vor exista și alte rețete decât cele 12 de pe pagina de rețete, de exemplu cu Banana Bread Mix, Carrot Cake Mix, Mix de budincă sau Crêpes Mix Original? Avem nevoie de una pentru perioada ianuarie-octombrie. Până atunci, sunteți de acord să folosim „Clătite pentru toată familia” (deja trimisă clienților noi, în primul email după comandă)?
2. **Gingerbread Pancakes:** ce conține rețeta (condimente, topping)? E gândită doar pentru sărbătorile de iarnă (noiembrie-decembrie)?
3. **Cookie Mix:** numele exact e „Cookie Mix Dark Chocolate” sau „Cookie Mix Dark Chocolate Chip”? În ce categorie apare pe site-ul nou?
4. **Recomandări de produse:** blocul afișează prețul și ratingul fiecărui produs. Vreți prețul vizibil sau ascuns (dacă theMarketer permite)? Ratingul din magazin vine din aceleași recenzii ca cifra 4,9 din 5?
5. **Recenzii noi:** vreți să alegem câteva recenzii noi de pe site (cu prenume + inițială), ca să le testăm în emailurile următoare fără să repetăm cele deja folosite?
6. **Cele mai vândute:** care sunt cele 3 produse pentru acasă pe care le-ați recomanda unui client nou? Le folosim ca rezervă dacă recomandările automate nu au destule rezultate.

---

## Decizie Andreea (13.10.2026): rețete
Secțiunea de rețete rulează tot anul cu **2 rețete: Cookies cu ciocolată neagră (Cookie Mix Dark Chocolate) + Clătite pentru toată familia** (cu imagine nouă, diferită de New Customer 1). **Gingerbread Pancakes** rămâne doar ca variantă de sezon (1 nov - 31 dec), de schimbat manual de Andreea; nu intră în build-ul de bază.

## Răspunsuri Andreea (13.10.2026)
1. Ce conține Gingerbread Pancakes: **nu se știe**. Varianta de sezon rămâne generică (fără ingrediente/arome nespecificate în discovery) și marcată [DE CONFIRMAT CU CLIENTUL].
2. Numele exact al Cookie Mix-ului: **nu se știe**. Folosim denumirea din discovery / lista REȚETE, marcată [DE CONFIRMAT CU CLIENTUL].
3. Preț și rating în blocul de recomandări: **da** (se setează în feed-ul theMarketer).
4. Top 3 bestselleri pentru fallback: **nu se știe**. Fallback-ul se setează în theMarketer după datele de vânzări; rămâne întrebare pentru client.
