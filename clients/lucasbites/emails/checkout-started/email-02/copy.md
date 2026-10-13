# Lucas Bites: Checkout Started, Email 2, strategie și copy final

Surse: `brief.md` (acest folder, inclusiv deciziile confirmate de client la 12.10.2026), `../README.md`, `../email-01/copy.md`, `discovery.md`, `../../welcome-03/copy.md` (recenzii reale verificate și regulile de citare). Layout-ul, culorile și limitele de caractere sunt convenite cu UI Designer (mesaj de feedback primit în aceeași sesiune, 12.10.2026). Legendă: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [adaptat] = text aprobat ajustat pentru email, [nou] = text nou, de aprobat de client, [din site actual] = recenzie reală de pe lucasbites.ro, citată cuvânt cu cuvânt, ca în `welcome-03/copy.md`.

**Ce cere clientul:** reamintire finalizare comandă (al doilea email, la 24 de ore) + recenzii clienți (2-3) + 3 USP: suport, transport, ingrediente.

**Fără prețuri hardcodate, fără discount, fără urgență falsă** („coșul expiră”, „stoc limitat”), fără promisiuni de sănătate, fără „cel mai bun”, fără „gata în 5 minute”. Recenziile sunt doar cele reale, deja verificate în `welcome-03/copy.md`, nemodificate.

---

## 1. Strategie, timing, segment

**Unghiul:** Email 1 a fost un serviciu („pofta ta e încă în coș”, la 30 de minute). Cine n-a finalizat nici după 24 de ore nu mai e distras, ci ezită. Email 2 răspunde ezitării cu ce nu putea spune Email 1: **vocea altor clienți** („nu ne crede pe cuvânt”), apoi închide ultimele obiecții practice cu 3 fapte: pe cine întreb dacă am o problemă (suport), cât mă costă livrarea (transport), ce e în mix (ingrediente). Ordinea în email: coșul și butonul sus (cine s-a hotărât nu trebuie să deruleze), dovada socială imediat sub buton, USP-urile, apoi un al doilea buton spre aceeași comandă. Un singur obiectiv, un singur link principal (`{{CHECKOUT_URL}}`), repetat de două ori.

**Ce NU repetă din Email 1:** subiectul și preheaderul („Pofta ta e încă în coș”), H1-ul, hero-ul (stack cu chocolate chips + adnotări), titlul „DE CE O SĂ-ȚI PLACĂ”, închiderea „ÎNCĂ TE GÂNDEȘTI?” cu trimitere spre gamă. Repetă doar ce trebuie să fie identic: blocul de coș, textul butonului principal, footer-ul și faptul confirmat despre transport (cu altă formulare).

**Timing:** **24 de ore** după evenimentul Checkout Started [confirmat de client, 12.10.2026]. Dacă momentul cade între 22:00 și 08:00 (ora României), emailul așteaptă până la 08:00, ca la Email 1.

**Segment:**
- Intră: contactele din flow care au primit Email 1, **inclusiv cei care nu l-au deschis** (deschiderile sunt umflate de Apple MPP, nu le folosim ca filtru), cu consimțământ de marketing [confirmat: checkout-ul colectează acordul].
- Exclus (verificare chiar înainte de trimitere): cine a plasat comanda după Checkout Started, dezabonați, suprimați, hard bounce, plângere spam.
- Frecvență: un singur flow Checkout Started per contact la 7 zile (ca la Email 1). Seria de welcome rămâne pe pauză cât timp contactul e în flow.

**Exit (ies din flow imediat):** comandă plasată, dezabonare, hard bounce, plângere spam. Email 2 e ultimul din flow (nu e cerut un al treilea); după el contactul revine în comunicarea obișnuită.

**KPI (ținte orientative, de recalibrat după 30 de zile de date):**
| Metrică | Țintă | Alertă |
|---|---|---|
| CTR unic pe linkurile spre checkout (`cta_main` + `cta_final`) / emailuri livrate | 5%+ | sub 2,5% |
| Rată de recuperare: comenzi atribuite `utm_campaign=checkout_02` (fereastră 72h de la click) / emailuri livrate | 2%+ | sub 0,7% |
| Dezabonări | sub 0,4% | peste 0,6% |
| Plângeri spam | sub 0,05% | peste 0,10% |

Țintele sunt mai mici decât la Email 1: al doilea email ajunge doar la cei care n-au răspuns la primul, deci la un public mai rece. Rata de deschidere se citește doar orientativ. Merită urmărit separat câte click-uri vin pe `cta_final` (cel de după recenzii și USP): dacă e o pondere mare, dovada socială face treaba și poate urca mai sus în layout la o iterație viitoare.

**UTM:** `utm_source=email&utm_medium=flow&utm_campaign=checkout_02&utm_content=<id>`. Valori `utm_content`: `cta_main` (S3), `cta_final` (S6). Linkurile de suport (mailto, tel) nu primesc UTM.

---

## 2. Subiecte și preheadere

| # | Subiect | Car. | Preheader | Car. |
|---|---|---|---|---|
| A **[recomandat]** | Nu ne crede pe cuvânt [nou] | 21 | Peste 1.100 de recenzii, media 4,9 din 5. Plus transport gratuit de la al 2-lea produs. [adaptat din site] | 87 |
| B | Ce spun cei care le-au făcut deja [nou] | 33 | Trei păreri reale, cuvânt cu cuvânt. Comanda ta e la un click de final. [nou] | 71 |
| C | Întrebări înainte de comandă? [nou] | 29 | Ne scrii la office@lucasbites.ro sau ne suni. Și vezi ce spun clienții. [nou] | 71 |

Limite convenite: subiect max ~40 car., preheader max 90 car.

**De ce A:** e scurt, are o voce (jucăuș, puțin obraznic, pe tonul brandului) și se plătește direct în H1 și în blocul de recenzii, deci promisiunea din inbox e onorată în primul ecran. Preheaderul pune cifra de dovadă și singurul beneficiu concret care poate debloca o comandă de un produs. Nu seamănă cu subiectul Email 1, deci în inbox nu arată ca un duplicat. **C** e varianta de test pentru ipoteza „oamenii se opresc din cauza unei întrebări”: dacă bate A pe rata de recuperare, suportul urcă mai sus în email.

**Test:** A vs B după primele ~500 de trimiteri, câștigătorul ales pe rata de recuperare (comenzi atribuite), nu pe deschideri. Fără numele în subiect (ca la Email 1: `{{FIRST_NAME}}` lipsește des la checkout).

**Expeditor:** Lucas Bites. **Reply-to:** office@lucasbites.ro (sau altă adresă monitorizată).

---

## 3. Copy pe secțiuni (ordinea din email)

Layout (de la UI Designer): culori portocaliu (S0 + S1) -> alb (S2 + S3) -> roz (S4) -> turcoaz (S5) -> negru (S6, text portocaliu) -> alb (S7). Tranziție nouă între secțiuni: margine festonată (semicercuri, ca un biscuit), nu valuri și nu panou ca în Email 1. Text negru pe portocaliu, alb, roz și turcoaz; pe negru, tot textul e portocaliu.

### S0-logo

Logo complet pe portocaliu, ca în Email 1. Fără text.

### S1-hero (portocaliu, text live, apoi IMG1)

| Element | Text | Car. | Limită convenită |
|---|---|---|---|
| Salut | **Hei, {{FIRST_NAME}}!** / fallback: **Hei!** [nou] | 20 (cu placeholder) | max 25 |
| H1 (Akrobat Black, uppercase) | **NU NE CREDE PE CUVÂNT.** [nou] | 22 | max 2 rânduri x 12 car., cuvânt max 12 |
| Text (Arial 16/24) | Ai ales deja. Înainte să termini comanda, uite ce spun cei care le-au făcut acasă. [nou] | 82 | ideal 80-95, max 110 |

- Rupere fixă a H1 (desktop și mobil): „NU NE CREDE” (11) / „PE CUVÂNT.” (10).
- Fallback nume: ca la Email 1 (salut condiționat; „Hei!” dacă lipsește numele sau dacă depășește 19 caractere).
- IMG1 (designer): farfurie neagră văzută de sus, mini pancakes așezate în cerc, zmeură, 5 steluțe negre desenate în arc deasupra. Fără text ars în imagine.
- „Le-au făcut” e intenționat general: coșul poate conține orice produs din gamă.

### S2-coș (alb, bloc dinamic)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Etichetă (chip) | **ÎN COȘUL TĂU** [nou, identic cu Email 1] | 12 | max 20 |
| Produse | `[FEED PRODUSE THEMARKETER]`: imagine, nume, cantitate, preț, din feed-ul adăugat de client | | |
| Etichetă cantitate | **Cantitate:** {{qty}} | 10 + valoare | |
| Rând total (opțional) | **Total produse:** {{total}} | 14 + valoare | |

Aceleași reguli ca la Email 1: „Total produse”, nu „Total” (transportul se calculează în checkout); fără buton per produs; dacă feed-ul nu randează, blocul se ascunde și emailul funcționează cu hero + CTA.

### S3-CTA principal (alb)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Buton pill (negru, text portocaliu) | **Finalizează comanda** [nou, identic cu Email 1] → `{{CHECKOUT_URL}}` | 19 | max 22 |
| Microcopy | fără | | |

UTM: `utm_content=cta_main`. `{{CHECKOUT_URL}}` trebuie să refacă coșul (vezi întrebările deschise).

### S4-recenzii (roz)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Titlu secțiune (Akrobat, uppercase) | **CE SPUN CLIENȚII** [nou] | 16 | ideal max 18 (1 rând) |
| Cifra mare | **4,9** [din site] | | element vizual (designer) |
| Lângă cifră | **din 5** [din site] | 5 | |
| Stele | 5 stele negre (doar la medie, nu per card) | | |
| Sub cifră | **peste 1.100 de recenzii** [din site] | 23 | max 30 |

Variantă de titlu mai lungă, dacă preferați să lege direct de H1: **CE SPUN CEI CARE LE-AU FĂCUT** (28, pe 2 rânduri) [nou].

**Cardurile** (albe, contur negru 2px, ghilimele mari desenate; nume și produs pe rânduri separate):

| Card | Citat | Car. | Nume (max 16) | Produs (max 22) | Sursă |
|---|---|---|---|---|---|
| Mare, toată lățimea (max 120) | „Au ieșit excelent și au fost foarte ușor de preparat. Mi-a plăcut în mod deosebit că nu au fost dulci.” | 102 | **Kinga L.** | Classic Pankees | [din site actual], confirmată în `brief.md` și `welcome-01` |
| Mic, coloana 1 (max 90) | „Extraordinar de bune, se prepară rapid iar copilul le adoră!!!” | 62 | **Carmen N.** | Buttermilk Pankees | [din site actual, diacritice corectate], `welcome-03` S2, 19.07.2021 |
| Mic, coloana 2 (max 90) | „Aleg mereu mixul Pizza Crust pentru o pizza rapidă, cu ingrediente din frigider.” | 80 | **Luminița B.** | Pizza Crust Mix | [din site actual, diacritice corectate], `welcome-03` S2, 23.04.2021 |

**De ce acestea trei:**
- Fiecare răspunde unei ezitări de la checkout: „e greu de făcut?” (Kinga: „foarte ușor de preparat”), „merită pentru familie?” (Carmen: „copilul le adoră”), „o să-l mai folosesc?” (Luminița: „aleg mereu”, adică revine la produs).
- Acoperă trei produse diferite (Classic, Buttermilk, Pizza Crust), pentru că nu știm ce e în coș.
- „Rapid” apare în cuvintele clienților, nu ca promisiune a noastră; nu înlocuiește regula „fără gata în 5 minute”.

**Reguli de citare (aceleași ca în `welcome-03/copy.md`):** citat cuvânt cu cuvânt, între ghilimele românești, doar diacritice corectate și emoji eliminate; prenume + inițiala numelui (de aceea „Kinga L.” în loc de „Kinga Ludescher”, pentru consecvență cu restul recenziilor); fără stele per card (recenzia Luminiței are 4 stele pe site, stelele din email arată doar media 4,9).

**Rezervă** (dacă un client cere scoaterea unei recenzii): „Clătitele ies foarte pufoase și gustoase. O adevărată plăcere să le faci și să le mănânci” (89 car., intră pe card mic sau mare) **Andreea H.** · Classic Pankees [din site actual, diacritice corectate, emoji eliminate].

**Excluse intenționat** (ca în `welcome-03`): Valentina și Roxana H. (superlative „cele mai bune / cele mai delicioase”), Arabela („perfecte”), Paula P. (ar cere corectură de ortografie).

**Notă:** cifra 1.100 / 4,9 e valabilă la 10.10.2026; se verifică înainte de lansare. Recenziile de mai sus s-au folosit deja în welcome (Kinga în Email 1, Carmen și Luminița în Email 3); publicul se suprapune doar parțial, iar `brief.md` permite refolosirea.

### S5-USP (turcoaz, 3 coloane cu iconițe pe desktop, stivuite pe mobil)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Titlu secțiune | **CA SĂ COMANZI LINIȘTIT** [nou] | 22 | max 24 |

| # | Titlu (Akrobat Bold, uppercase) | Car. | Rând sub titlu (Arial) | Car. | Sursă |
|---|---|---|---|---|---|
| 1 Suport | **ÎNTREBĂRI? SCRIE-NE.** | 20 | office@lucasbites.ro / +40 731 399 399 (două rânduri, ambele linkuri: `mailto:` și `tel:+40731399399`) | 38 | [confirmat: datele de contact]; titlu [nou] |
| 2 Transport | **TRANSPORT GRATUIT** | 17 | Când pui al 2-lea produs în coș. | 32 | [confirmat de client, 12.10.2026]; rând [adaptat] |
| 3 Ingrediente | **ȘTII CE E ÎN MIX** | 16 | Fără conservanți. Zahăr brun din trestie. | 41 | [din site], afirmații [confirmat] |

Limite convenite: titlu max 20 car., max 2 rânduri (coloana are 157px); rând max 50 car.

Note:
- **Suport:** nu promitem program, timp de răspuns sau canale (WhatsApp, chat), pentru că nu sunt confirmate. Dacă clientul confirmă, rândul poate deveni, de exemplu, „Îți răspundem [DE CONFIRMAT CU CLIENTUL: zilele și intervalul orar].”, cu datele de contact păstrate.
- **Transport:** alt rând decât în Email 1 („De la al 2-lea produs din coș.”), același fapt. Nu scriem „orice combinație” sau „fără valoare minimă” până nu confirmă clientul.
- **Ingrediente:** „făină nealbită” NU apare, pentru că e valabil doar la pancakes și clătite, iar coșul poate conține altceva. „Zahăr brun din trestie” e scris fără „în loc de zahăr alb” (brownie-ul conține ciocolată, care are zahăr; Crêpes Original nu are zahăr adăugat). Dacă clientul preferă fără nicio nuanță, rândul de rezervă e **Ingrediente pe care le recunoști.** (33) [din site], cu „Fără conservanți” mutat în titlu: **FĂRĂ CONSERVANȚI** (16). Nu folosim „fără E-uri” (Pizza Crust Mix are emulsificator).
- Iconițe (designer): cască sau plic, camion, spic. Fără bife, fără stele.

### S6-închidere + CTA final (negru, text portocaliu, centrat)

| Element | Text | Car. | Limită |
|---|---|---|---|
| IMG2 (deasupra) | fursecuri cu bucăți de ciocolată, unul rupt (designer) | | |
| Titlu (Akrobat, uppercase, portocaliu) | **TE AȘTEPTĂM LA MASĂ.** [nou] | 20 | max 22 |
| Rând (Arial, portocaliu) | Finalizezi comanda, iar partea bună abia începe. [nou] | 48 | max 70 |
| Buton pill (portocaliu plin, text negru) | **Finalizează comanda** → `{{CHECKOUT_URL}}` | 19 | max 22 |
| Semnătură | **eat what you love** [din site, slogan oficial] | 17 | |

- Titlul trimite la povestea brandului („cel mai important moment al zilei este acela când ne strângem toți, în jurul mesei”, [din site actual]), fără să o citeze.
- UTM buton: `utm_content=cta_final`.
- Fără al doilea link spre gamă (`{{SHOP_URL}}`): în Email 2 tot ce e clickabil duce spre aceeași comandă, plus contactul de suport. `{{SHOP_URL}}` rămâne în footer doar dacă e deja în șablonul Email 1.

### S7-footer (alb, identic cu Email 1)

> Lucas Bites · Roșu, Chiajna, Ilfov
> [DE CONFIRMAT: denumire juridică SRL] · CUI [DE CONFIRMAT]
> office@lucasbites.ro · +40 731 399 399
>
> Primești acest email pentru că ai început o comandă pe lucasbites.ro și ai acceptat să primești emailuri de la noi.
>
> Nu mai vrei emailuri de la noi? [Dezabonează-te aici]({{UNSUBSCRIBE_URL}}). Durează un click.
>
> © 2026 Lucas Bites

- Iconițe social ca în Email 1: Instagram, TikTok, Facebook, YouTube (aceleași linkuri).
- `{{UNSUBSCRIBE_URL}}` = tag-ul de dezabonare theMarketer; header-ele `List-Unsubscribe` + `List-Unsubscribe-Post` (one-click, RFC 8058) active.
- Rândul SRL + CUI e placeholder, ca în `../email-01/index-esp.html`. [DE PRIMIT DE LA CLIENT: denumirea SRL și CUI-ul]

---

## 4. Alt text

| Imagine | Alt text | Car. |
|---|---|---|
| Logo header | Lucas Bites | 11 |
| IMG1 (hero) | Mini pancakes așezate în cerc pe o farfurie neagră, cu zmeură, sub cinci steluțe desenate | 89 |
| Stele S4 | Rating 4,9 din 5 | 16 |
| Ghilimele desenate (carduri) | `alt=""` (decorativ) | |
| Iconițe USP | `alt=""` (decorative, textul e live alături) | |
| IMG2 (închidere) | Fursecuri cu bucăți de ciocolată, unul rupt în două | 51 |
| Feston, forme decorative | `alt=""` | |
| Logo footer | Lucas Bites, eat what you love | 30 |
| Iconițe social | Instagram / TikTok / Facebook / YouTube | |

Toate textele (H1, recenzii, cifra 4,9, USP, butoane) sunt HTML live, deci emailul rămâne complet cu imaginile blocate.

---

## 5. Comunicare cu UI Designer

- Structura pe secțiuni (ordine, mesaj, lungimi, recenziile alese cu rezervă) a fost trimisă înainte de copy; feedback-ul a venit în aceeași sesiune (12.10.2026).
- Integrat din feedback: culori pe secțiuni (portocaliu, alb, roz, turcoaz, negru, alb) și festonul ca tranziție nouă; text live pe portocaliu în hero și IMG1 fără adnotări; „4,9 / din 5 / stele / peste 1.100 de recenzii” ca element vizual cu textul exact de mai sus; 1 card mare (Kinga, 102 din max 120) + 2 carduri mici (Carmen 62, Luminița 80, din max 90), nume și produs pe rânduri separate; titlul recenziilor scurtat la 16 car. („CE SPUN CLIENȚII”) pentru un singur rând; titlu de secțiune USP adăugat (22 din max 24); suport pe două rânduri (email / telefon), ambele linkuri; închiderea pe negru cu buton portocaliu plin spre checkout; alt text pentru IMG1 și IMG2.
- Nu au fost cerute variante mai scurte: toate textele intră în limitele convenite.
- Designerul construiește doar cu textele exacte din acest fișier și semnalează dacă ceva nu încape.

---

## 6. Întrebări deschise pentru client

1. **Suport:** care e programul și pe ce canale răspundeți (email, telefon, WhatsApp)? Putem promite un interval de răspuns? Până la confirmare, emailul dă doar adresa și telefonul.
2. **„Zahăr brun din trestie” pe USP-ul de ingrediente:** e în regulă formularea generală pentru toată gama (inclusiv pizza, unde nu știm dacă mixul conține zahăr)? Dacă nu, folosim „Fără conservanți” + „Ingrediente pe care le recunoști.”
3. **Numele din recenzii:** avem voie să afișăm prenumele + inițiala autorilor (Kinga L., Carmen N., Luminița B.) într-un email comercial? (aceeași întrebare ca în `welcome-03`, întrebarea 4)
4. **Link de checkout:** `{{CHECKOUT_URL}}` din theMarketer reface coșul cu produsele și cantitățile, sau duce într-un coș gol? (rămasă deschisă din Email 1)
5. **Comandă plasată în timp real:** theMarketer primește evenimentul de comandă înainte de trimiterea Email 2, ca să nu scrie cuiva care tocmai a cumpărat? (rămasă deschisă din Email 1)
6. **Transport gratuit:** se aplică și la 2 bucăți din același produs? Există valoare minimă sau excepții (gama Professional, zone)?
7. **Dovada socială:** rămânem la „peste 1.100 de recenzii, 4,9 din 5” (site-ul nou) până la lansare? Cifra se verifică în ziua lansării.
8. **Denumirea SRL și CUI** pentru footer.
