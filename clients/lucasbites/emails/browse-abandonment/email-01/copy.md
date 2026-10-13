# Lucas Bites: Browse Abandonment, Email 1, copy final

Surse: `strategy.md` (acest folder: unghi, secțiuni S0-S6, limite, rețete, USP, UTM; are prioritate), `brief.md`, `../README.md`, `discovery.md` (inclusiv 8b), `../../checkout-started/email-01/copy.md` și `email-02/copy.md` (format, footer, ce nu repetăm), `../../welcome-01/02/03/copy.md` și `../../new-customer-01/02/copy.md` (subiecte, H1-uri și închideri deja folosite). Legendă: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [adaptat] = text aprobat ajustat pentru email, [nou] = text nou, de aprobat de client, [confirmat] = confirmat de client, [DE CONFIRMAT CU CLIENTUL] = marcaj păstrat din strategie sau adăugat aici.

**Ce cere clientul:** reamintire produs vizualizat (placeholder theMarketer) + idei de rețete cu produsele Lucas Bites (2-3 poze / video) + 3 USP.

**Reguli:** fără prețuri hardcodate, fără discount, fără urgență falsă („stoc limitat”, „se termină”), fără promisiuni de sănătate sau nutriționale, fără „cel mai bun”, fără „gata în 5 minute” (produsul vizualizat poate fi oricare), fără „fără E-uri” (Pizza Crust Mix are emulsificator). Fără „ai uitat”, „ți-a rămas”, „te-am văzut”, „am observat”, „coș”. Copy-ul nu numește produsul vizualizat, prețul sau categoria lui.

Caracterele sunt numărate cu spații și punctuație; o literă cu diacritice = 1 caracter.

---

## 1. Subiecte și preheadere

| # | Subiect | Car. | Preheader | Car. |
|---|---|---|---|---|
| A **[recomandat]** | Trei idei pentru pofta de azi [adaptat din site, „Alege-ți pofta de azi”] | 29 | Pankees de post, pizza cu pepperoni sau brownie cu fructe de pădure? [din site, titlurile rețetelor] | 68 |
| B | Ți-a făcut cu ochiul ceva bun? [nou] | 30 | Trei rețete de încercat acasă, de la pancakes la movie night. [nou; „movie night” din site] | 61 |
| C | Seară de film sau pauză de cafea? [adaptat din site, momentele „movie night” și „pauza de la birou”] | 33 | Pizza de casă pentru film, brownie pentru pauza de la birou. Rețetele, mai jos. [adaptat din site] | 79 |

Limite: subiect max ~40 car., preheader max 90 car.

**De ce A:** spune exact ce conține emailul (idei, nu o reamintire), folosește vocabularul site-ului („pofta de azi”) și nu sună a supraveghere: funcționează identic pentru cineva care s-a uitat la pancakes sau la pizza. Preheaderul numește cele trei rețete din S3, deci promisiunea din inbox e plătită în corpul emailului, iar forma de întrebare invită fără presiune. Nu seamănă cu subiectele din checkout („Pofta ta e încă în coș”, „Nu ne crede pe cuvânt”), deci cine primește ambele flow-uri nu vede un duplicat.

**B** e varianta de test pe curiozitate. Atenție: „ți-a făcut cu ochiul” trimite discret la produsul vizualizat; dacă testul arată dezabonări peste alerta din strategie (0,6%), rămânem la A. **C** e varianta pe momente, utilă dacă GIF-ul cu pizza (S3) aduce cele mai multe click-uri.

**Test:** A vs B după primele ~500 de trimiteri pe variantă; câștigătorul se alege pe rata de conversie (comenzi atribuite `utm_campaign=browse_01`), nu pe deschideri.

**Fără prenume în subiect:** `{{FIRST_NAME}}` lipsește des; numele apare doar în salutul din S1, cu fallback.

**Expeditor:** Lucas Bites. **Reply-to:** office@lucasbites.ro (sau altă adresă monitorizată).

---

## 2. Copy pe secțiuni (ordinea din `strategy.md`)

### S0-logo

Logo complet pe fundalul hero-ului (reguli de fundal din discovery 7). Fără text.

### S1-hero (text-led, fără buton)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Salut | **Hei, {{FIRST_NAME}}!** / fallback: **Hei!** [ca în checkout] | 20 (cu placeholder) / 4 | max 25 |
| H1 (Akrobat Black, uppercase) | **CE FACI CU POFTA ASTA?** [nou] | 22 | max 28, max 2 rânduri, cuvânt max 12 |
| Text (Arial 16/24) | Pentru fiecare poftă există un moment. Uite trei idei de pus pe masă, când ai chef. [prima frază din site, restul nou] | 83 | ideal 70-90, max 110 |

- Despărțire H1 (desktop și mobil): „CE FACI CU” (10) / „POFTA ASTA?” (11).
- Fallback nume: salut condiționat, „Hei!” dacă lipsește numele sau dacă are peste 19 caractere (ca la checkout).
- Textul nu trimite la „produsul de mai jos”: dacă blocul din S2 nu se încarcă, S1 duce direct în rețete.
- „Pofta asta” rămâne generală: nu spune ce produs, nu spune că l-am văzut.

### S2-produs vizualizat (PLACEHOLDER theMarketer)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Etichetă chip (negru, text portocaliu) | **PE LISTA DE POFTE** [nou] | 17 | max 20 |
| Bloc produs | `[PRODUS VIZUALIZAT THEMARKETER]`: imagine, nume, (preț) și link, generate de blocul adăugat manual de Andreea între comentariile `THEMARKETER_FEED`. În `index.html` (preview): card marcat **EXEMPLU**. | | |
| Buton sub bloc (doar dacă blocul nu are buton propriu) | **Vezi produsul** [nou] → link-ul produsului din bloc, `utm_content=cta_product` | 13 | max 22 |
| Microcopy sub buton | fără | | |

- Eticheta merge la 1 sau la mai multe produse afișate și nu spune „ai văzut” sau „produsul tău”.
- Etichetă alternativă, doar dacă blocul afișează **un singur** produs: **ȚI-A FĂCUT CU OCHIUL** (20, la limită) [nou]. La mai multe produse ar trebui „ți-au”, care depășește limita. Dacă se alege subiectul B, folosim eticheta principală, ca expresia să nu apară de două ori.
- Prețul îl afișează blocul theMarketer; copy-ul nu scrie niciun preț. Ascunderea prețului: [DE CONFIRMAT CU CLIENTUL].

**Fallback (blocul nu se încarcă: feed gol, produs scos din stoc):**
- **Varianta recomandată (din strategie):** cardul și eticheta se ascund complet; emailul merge S1 → S3. Nu e nevoie de text.
- **Doar dacă theMarketer nu poate ascunde containerul** și cardul ar rămâne gol, în card intră:

| Element | Text | Car. | Limită |
|---|---|---|---|
| Rând | Toate mixurile Lucas Bites, într-un singur loc. [nou] | 47 | max 70 |
| Buton | **Răsfoiește gama** [nou] → `{{SHOP_URL}}`, `utm_content=cta_product` | 15 | max 22 |
| Chip | se ascunde (nu are sens fără produs) | | |

### S3-rețete (secțiunea principală)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Supratitlu | **trei momente, trei mixuri** [nou] | 25 | max 25 (la limită) |
| H2 (Akrobat Black, uppercase) | **CE IESE DINTR-UN MIX** [nou] | 20 | max 26, max 2 rânduri |
| Intro (Arial 16) | Una de post, una sărată și una dulce. Tu alegi ordinea. [nou] | 55 | max 70 |

Supratitlu de rezervă, dacă UI vrea mai mult aer: **trei idei, trei mixuri** (22) [nou].

**Cardurile** (doar ce e publicat pe v3: titlu, produs, timp, moment; fără ingrediente, pași sau descrieri de gust):

| Element | Card 1 (foto) | Car. | Card 2 (**GIF**) | Car. | Card 3 (foto) | Car. | Limită |
|---|---|---|---|---|---|---|---|
| Etichetă moment | **vegan / de post** [din site, filtrul de pe retete.html] | 15 | **movie night** [din site, homepage] | 11 | **pauza de la birou** [din site, moment] | 17 | max 24 |
| Titlu rețetă (Akrobat Bold, uppercase) | **PANKEES DE POST CU FRUCTE** [din site] | 25 | **PIZZA DE CASĂ CU PEPPERONI** [din site] | 26 | **BROWNIE CU FRUCTE DE PĂDURE** [din site] | 27 | max 30, max 2 rânduri, cuvânt max 12 |
| Rând „Cu {produs}” | Cu Vegan Classic Pankees [din site] [DE CONFIRMAT CU CLIENTUL: produsul corect pentru rețetă] | 24 | Cu Pizza Crust Mix [din site] | 18 | Cu Brownie Mix [din site] | 14 | max 32 |
| Rând info | De post · 15 min [din site] | 16 | Familie · 30 min [din site] | 16 | Desert · 35 min [din site] | 15 | max 22 |
| Rând de poftă (opțional, vezi nota) | Tu adaugi apă, agiți și gătești. [din site] | 32 | Pizza de casă la începutul filmului. [din site, homepage] | 36 | De adus colegilor, la cafeaua de la 11. [adaptat din site] | 39 | propunere: max 45 |
| CTA (link-buton) | **Vezi rețeta** [din site] → `{{URL_RETETA_POST}}`, `utm_content=reteta_1` | 11 | **Vezi rețeta** → `{{URL_RETETA_PIZZA}}`, `utm_content=reteta_2` | 11 | **Vezi rețeta** → `{{URL_RETETA_BROWNIE}}`, `utm_content=reteta_3` | 11 | max 16 |

| Element | Text | Car. | Limită |
|---|---|---|---|
| Link sub carduri | **Toate rețetele** [din site] → `{{SHOP_URL}}/retete`, `utm_content=retete_toate` | 14 | max 22 |

Note S3:
- **Rândul de poftă e opțional.** Strategia nu îl prevede în card și interzice descrierile de gust. Cele trei rânduri de mai sus nu descriu gustul: sunt momentele de pe site (homepage și categoria Prăjituri) și pasul de preparare Pankees din discovery 8b („gama Pankees”: apă până la semn, agiți). Dacă UI nu are loc sau strategul preferă cardul curat, rândul se scoate fără să lipsească nimic.
- „Tu adaugi apă, agiți și gătești.” apare doar pe cardul Pankees, deci nu încalcă regula „fără gata în 5 minute” pentru gama întreagă. Nu am pus timpul de 5 minute.
- **Card 1:** fructele exacte și produsul (Vegan Classic Pankees): [DE CONFIRMAT CU CLIENTUL]. Copy-ul spune doar „cu fructe”, ca pe site.
- **Card 2:** pe site-ul actual pizza e „pizza-salami”; titlul rămâne cel din v3 (pepperoni). URL: [DE CONFIRMAT CU CLIENTUL].
- **URL-uri:** `{{URL_RETETA_POST}}`, `{{URL_RETETA_PIZZA}}`, `{{URL_RETETA_BROWNIE}}` [DE CONFIRMAT CU CLIENTUL: URL-urile celor 3 rețete]; fallback pentru oricare: `{{SHOP_URL}}/retete`. Un buton „Vezi rețeta” care duce la altă rețetă decât cea din titlu nu pleacă.
- **Rezervă card 1** (dacă clientul nu aprobă rețeta de post): **COOKIES CU CIOCOLATĂ NEAGRĂ** (27) · Cu Cookie Mix Dark Chocolate (28) · Desert · 14 min (15) · etichetă **gustarea de după școală** (23) [din site]. Rând de poftă opțional: Tu adaugi doar ce scrie pe ambalaj. (35) [adaptat din site]. Atunci intro devine: Una dulce, una sărată și încă una dulce. Tu alegi ordinea. (58) [nou].
- **Rotație sezonieră opțională (1 noiembrie - 31 decembrie):** card 1 devine **GINGERBREAD PANCAKES** (20) · Cu Classic Pankees (18) · Desert · 15 min (15) · etichetă **aroma Sărbătorilor de iarnă** (27, peste limita de 24: pe card folosim **aroma de Sărbători** (18) [adaptat din site]). Intro: Una de Sărbători, una sărată și una dulce. Tu alegi ordinea. (60) [nou].

### S4-USP

| Element | Text | Car. | Limită |
|---|---|---|---|
| Titlu secțiune | **DE CE LUCAS BITES?** [nou] | 18 | max 26 |

| # | Titlu (Akrobat Bold 20, uppercase) | Car. | Rând sub titlu (Arial 14) | Car. | Sursă |
|---|---|---|---|---|---|
| 1 Recenzii | **4,9 DIN 5** | 9 | Din peste 1.100 de recenzii ale clienților. | 43 | [din site] [confirmat, valabil la 10.10.2026] |
| 2 Ingrediente | **CE E ÎN MIX** | 11 | Ingrediente pe care le recunoști, puse la cântar. | 49 | titlu [din site, homepage „Ce e în mix”]; rând [adaptat din site: „Ingrediente pe care le recunoști, puse deja la cântar.”] |
| 3 Transport | **TRANSPORT GRATUIT** | 17 | De la al 2-lea mix, ca să încerci două rețete. | 46 | [confirmat, 12.10.2026]; rând [nou] |

Limite: titlu max 20 car., max 2 rânduri, cuvânt max 12; rând ideal 35-45, max 50.

Note S4:
- **Ordinea și setul sunt cele din strategie:** recenzii, ingrediente, transport (transportul ultimul, invers față de Checkout 1).
- **USP 2:** „fără conservanți” nu încape în același rând cu formularea aprobată (ar avea 51 car.). Rând de rezervă, dacă clientul preferă „fără conservanți” în locul „puse la cântar”: **Ingrediente cunoscute, fără conservanți.** (40) [adaptat din site]. Fără „fără E-uri”, fără „făină nealbită”, fără „zahăr brun”.
- **USP 3:** „mix” în loc de „produs”: un al doilea mix e întotdeauna un al doilea produs, deci afirmația rămâne în interiorul faptului confirmat. Fără „coș”, diferit de „De la al 2-lea produs din coș.” (Checkout 1) și „Când pui al 2-lea produs în coș.” (Checkout 2). Dacă se aplică și la 2 bucăți din același mix: [DE CONFIRMAT CU CLIENTUL] (întrebarea 12 din strategie); formularea actuală nu promite nici una, nici alta.
- **USP 1:** cifra se verifică în ziua lansării. Alternativa din strategie (dacă clientul nu vrea cifra în emailuri de abandon): **ÎN MAGAZINE** (11) / Kaufland, Carrefour, eMAG, Freshful și altele. (46) [adaptat din site] [DE CONFIRMAT CU CLIENTUL].
- Fără butoane pe USP. Titlul secțiunii diferă de „DE CE O SĂ-ȚI PLACĂ” și „CA SĂ COMANZI LINIȘTIT”.

### S5-închidere + CTA spre gamă

| Element | Text | Car. | Limită |
|---|---|---|---|
| Titlu (Akrobat, uppercase) | **POFTA NU SE GRĂBEȘTE.** [nou] | 21 | max 32, max 3 rânduri |
| Rând (Arial 16) | Când ești gata: pancakes, clătite, prăjituri și pizza, toate aici. [adaptat din site] | 66 | max 70 |
| Buton | **Alege-ți pofta** [adaptat din site, „Alege-ți pofta de azi”] → `{{SHOP_URL}}`, `utm_content=cta_shop` | 14 | max 22 |
| Semnătură | **eat what you love** [din site, slogan oficial] | 17 | |

- Titlul ține tonul de „slow marketing”: fără grabă, fără termen. Diferit de „ÎNCĂ TE GÂNDEȘTI?” și „TE AȘTEPTĂM LA MASĂ.”.
- Rândul numește gama altfel decât Checkout 1 („Răsfoiește toată gama: ...”).
- Dacă UI pune o imagine mică aici, alt text-ul se scrie după ce se alege imaginea (vezi secțiunea 3).

### S6-footer

> Lucas Bites · Roșu, Chiajna, Ilfov
> [DE PRIMIT DE LA CLIENT: denumire juridică SRL] · CUI [DE PRIMIT DE LA CLIENT]
> office@lucasbites.ro · +40 731 399 399
>
> Primești acest email pentru că ai acceptat să primești emailuri de la Lucas Bites. [nou] [DE CONFIRMAT CU ANDREEA]
>
> Nu mai vrei emailuri de la noi? [Dezabonează-te aici]({{UNSUBSCRIBE_URL}}). Durează un click.
>
> © 2026 Lucas Bites

- **Fraza „de ce primești”:** destinatarii de browse sunt abonați (newsletter/ghid) sau clienți care au bifat acordul la checkout, nu oameni care au început o comandă. Formularea de mai sus e generală și acoperă ambele surse de acord, fără să afirme o înscriere anume. [DE CONFIRMAT CU ANDREEA: o păstrăm noi sau, ca la New Customer, o adaugă Andreea în theMarketer; în al doilea caz, în HTML rămâne markerul `[ADAUGĂ UTILIZATORUL]` pe aceeași poziție.]
- Logo stripes, iconițe social: Instagram, TikTok, Facebook, YouTube (aceleași linkuri ca în `welcome-01/brief.md`). Linkurile social, `mailto:` și `tel:` nu primesc UTM.
- `{{UNSUBSCRIBE_URL}}` = tag-ul de dezabonare theMarketer [neverificat: sintaxa]; `List-Unsubscribe` + `List-Unsubscribe-Post` (one-click, RFC 8058) active.

---

## 3. Alt text

| Imagine | Alt text | Car. |
|---|---|---|
| Logo header | Lucas Bites | 11 |
| Hero | nu are imagine mare; element decorativ mic (steluțe, bucată de mâncare decupată), dacă există: `alt=""` | |
| Card produs S2 (`index-esp.html`) | îl pune blocul theMarketer (numele produsului din feed) [neverificat]; nu scriem noi | |
| Card produs S2 (`index.html`, EXEMPLU) | numele produsului din exemplu (doar preview) | |
| Rețeta 1, foto | Teanc scurt de Pankees de post cu fructe proaspete | 50 |
| Rețeta 2, GIF (descrie și primul cadru, singurul vizibil în Outlook) | varianta felie: Pizza de casă cu pepperoni, cu mozzarella care se întinde / varianta aburi: Pizza de casă cu pepperoni, abia scoasă, din care ies aburi | 57 / 59 |
| Rețeta 3, foto | Brownie cu fructe de pădure deasupra | 36 |
| Iconițe USP | `alt=""` (decorative, textul e live alături) | |
| Imagine mică S5 (doar dacă UI o folosește) | de scris după ce se alege imaginea | |
| Logo footer | Lucas Bites, eat what you love | 30 |
| Iconițe social | Instagram / TikTok / Facebook / YouTube (câte una pe iconiță) | |
| Tranziții, forme decorative | `alt=""` | |

Alt-ul rețetei 1 spune doar „fructe proaspete” până se confirmă fructele. Toate textele (H1, chip, titluri de rețete, USP, butoane) sunt HTML live, deci emailul rămâne complet cu imaginile blocate.

---

## 4. Note pentru UI Designer

- **H1:** rupere fixă „CE FACI CU” (10) / „POFTA ASTA?” (11).
- **H2 S3:** „CE IESE” (7) / „DINTR-UN MIX” (12) dacă nu încape pe un rând; nu rupeți „DINTR-UN”.
- **Titluri de rețete (25-27 car., pe 2 rânduri):** „PANKEES DE POST” (15) / „CU FRUCTE” (9); „PIZZA DE CASĂ” (13) / „CU PEPPERONI” (12); „BROWNIE CU FRUCTE” (17) / „DE PĂDURE” (9). Cel mai lung cuvânt: „PEPPERONI” (9).
- **Titlul S5:** „POFTA NU” (8) / „SE GRĂBEȘTE.” (12).
- **La limită sau aproape:** supratitlul S3 (25 din 25), chip-ul alternativ „ȚI-A FĂCUT CU OCHIUL” (20 din 20), rândul USP 2 (49 din 50), rândul USP 3 (46, peste idealul de 45). Dacă rândul USP 2 trece pe 3 rânduri în coloana de mobil, folosiți rezerva „Ingrediente cunoscute, fără conservanți.” (40). Supratitlul are rezervă de 22 car.
- **Rândul „Cu Vegan Classic Pankees”** (24) e cel mai lung rând de produs; încape în 32.
- **Rândul de poftă din carduri** e opțional (vezi nota S3); dacă îl păstrați, max 39 car. în setul actual.
- **Butonul S2** apare doar dacă blocul theMarketer nu are buton propriu. Fallback-ul cu „Răsfoiește gama” se folosește doar dacă containerul nu se poate ascunde.
- Lungime: aproximativ 150 de cuvinte de text live fără footer, în ținta din strategie (150-200).

---

## 5. Întrebări deschise

1. **Eticheta S2:** „PE LISTA DE POFTE” (merge la 1 sau mai multe produse) sau „ȚI-A FĂCUT CU OCHIUL” (doar dacă blocul arată un singur produs)? Depinde de câte produse afișează blocul theMarketer (întrebarea 4 din strategie).
2. **Rândul de poftă din carduri:** îl păstrăm (moment de pe site, fără descrieri de gust) sau cardurile rămân strict cu titlu, produs, info, CTA, ca în strategie?
3. **Footer:** fraza generală de mai sus o scriem noi sau o adaugă Andreea în theMarketer?
4. **Rămân din strategie:** fructele și produsul pentru Pankees de post cu fructe; URL-urile celor 3 rețete; transportul gratuit la 2 bucăți din același produs; cifra de recenzii la lansare; denumirea SRL, CUI și `{{SHOP_URL}}`.
