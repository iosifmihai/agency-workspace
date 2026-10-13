# Lucas Bites: Checkout Started, Email 1, strategie și copy final

Surse: `brief.md` (acest folder), `../README.md`, `discovery.md`, `../../welcome-01/brief.md`, `../../welcome-01/copy.md`, `../../welcome-03/copy.md`, referința din `refs/`. Layout-ul și limitele de caractere sunt convenite cu UI Designer (mesaj de feedback primit în aceeași sesiune, 12.10.2026). Legendă: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [adaptat] = text aprobat ajustat pentru email, [nou] = text nou, de aprobat de client.

**Ce cere clientul:** reamintire finalizare comandă + 3 USP.

**Fără prețuri hardcodate, fără discount, fără urgență falsă** („coșul expiră”, „stoc limitat”), fără promisiuni de sănătate, fără „cel mai bun”. Recenziile (1.100 / 4,9) rămân pentru Email 2, care are un bloc dedicat de recenzii.

---

## 1. Strategie, timing, segment

**Unghiul:** primul email din abandon e un serviciu, nu o vânzare. Omul a ales deja produsele și a ajuns la checkout, deci intenția e mare. Cele mai frecvente motive de abandon sunt distragerea și o ezitare mică (cost de transport, „mai mă gândesc”). Emailul face trei lucruri, în ordinea asta: arată exact ce a lăsat în coș, pune un singur buton care îl duce înapoi la checkout și răspunde la ezitare cu 3 fapte confirmate. Transportul gratuit de la al 2-lea produs e primul USP pentru că atacă direct cel mai comun motiv de abandon și poate crește coșul de la 1 la 2 produse. Tonul rămâne jucăuș și fără presiune: un reminder prietenos convertește fără să ardă reputația, iar reducerea, dacă se aprobă vreodată, se păstrează pentru ultimul email din flow, nu pentru primul.

**Timing recomandat:** Email 1 la **30 de minute** după evenimentul Checkout Started (intenția e încă proaspătă, dar omul a avut timp să termine singur). Email 2 la **24 de ore** după Checkout Started. Fără fereastră de livrare la Email 1 (contextul contează mai mult decât ora), cu excepția nopții: dacă momentul trimiterii cade între 22:00 și 08:00 (ora României), emailul așteaptă până la 08:00. [Timing confirmat de client, 12.10.2026: 30 min / 24 h]

**Segment:**
- Intră: contactele cu evenimentul Checkout Started, cu email valid și **consimțământ de marketing**. [Confirmat 12.10.2026: checkout-ul colectează acordul.]
- Exclus: cine a plasat o comandă după evenimentul Checkout Started (verificare înainte de fiecare email), contactele dezabonate, suprimate sau cu hard bounce.
- Frecvență: un singur flow Checkout Started per contact la 7 zile, ca cineva care abandonează de mai multe ori să nu primească emailuri în buclă.
- Dacă contactul e în seria de welcome, emailurile de welcome se pun pe pauză cât timp e în acest flow.

**Exit (ies din flow imediat):** comandă plasată, dezabonare, hard bounce, plângere spam.

**KPI (ținte orientative, de recalibrat după 30 de zile de date):**
| Metrică | Țintă | Alertă |
|---|---|---|
| CTR unic (orice link spre checkout sau magazin) / emailuri livrate | 8%+ | sub 4% |
| Rată de recuperare: comenzi atribuite `utm_campaign=checkout_01` (fereastră 72h de la click) / emailuri livrate | 3%+ | sub 1% |
| Dezabonări | sub 0,3% | peste 0,5% |
| Plângeri spam | sub 0,05% | peste 0,10% |

Rata de deschidere se citește doar orientativ (Apple MPP o umflă).

---

## 2. Subiecte și preheadere

| # | Subiect | Car. | Preheader | Car. |
|---|---|---|---|---|
| A **[recomandat]** | Pofta ta e încă în coș [nou] | 22 | Mixurile alese sunt la un click distanță. Transport gratuit de la al 2-lea produs. [nou] | 82 |
| B | Ai uitat ceva bun în coș [nou] | 24 | Ai ales deja ce-ți face poftă. Termini comanda de unde ai rămas. [nou] | 64 |
| C | Comanda ta e aproape gata [nou] | 25 | Adaugi apă, agiți și gătești. Dar mai întâi, finalizezi comanda. [adaptat] | 64 |

Limite convenite: subiect max ~40 car., preheader max 90 car.

**De ce A:** e scurt, jucăuș și pe brand („poftă” e cuvântul site-ului), spune exact ce conține emailul și se leagă de titlul din hero, deci promisiunea din inbox e plătită în primul ecran. Preheaderul adaugă singurul beneficiu concret care poate debloca comanda. Testați A vs B după primele ~500 de trimiteri; câștigătorul se alege pe rata de recuperare, nu pe deschideri.

**Fără numele în subiect:** `{{FIRST_NAME}}` lipsește des la checkout-urile abandonate și un subiect cu fallback gol arată rău. Numele apare doar în salutul din hero, unde are fallback.

**Expeditor:** Lucas Bites. **Reply-to:** office@lucasbites.ro (sau altă adresă monitorizată).

---

## 3. Copy pe secțiuni (ordinea din email)

Layout (de la UI Designer): S0 logo complet pe roz, deasupra hero-ului, ca hero-ul să înceapă de sus; S1 hero roz cu stack de pancakes cu chocolate chips decupat, 3 adnotări cu săgeți desenate de mână și steluțe; dedesubt un panou alb cu colțuri rotunjite pe care stau S1 (text), S2 (coș) și S3 (CTA); S4 USP pe turcoaz; S5 închidere pe portocaliu cu clătite decupate care ies din marginea dreaptă; S6 footer ca în welcome. Text negru pe toate culorile de brand.

### S1-hero

| Element | Text | Car. | Limită convenită |
|---|---|---|---|
| Salut | **Hei, {{FIRST_NAME}}!** / fallback: **Hei!** [nou] | 20 (cu placeholder) | max 25 |
| H1 (Akrobat Black, uppercase) | **POFTA TA E ÎNCĂ ÎN COȘ.** [nou] | 23 | max 28, max 2 rânduri, cuvânt max 12 car. |
| Text (Arial 16/24) | Ai ales deja ce-ți face poftă. Mai e un singur pas și mixurile pornesc spre tine. [nou] | 81 | ideal 70-90, max 110 |

- Despărțire H1 pe mobil: „POFTA TA E” (10) / „ÎNCĂ ÎN COȘ.” (12).
- H1 alternativ, pentru test sau dacă subiectul ales e B: **AI UITAT CEVA BUN?** (18) [nou]
- Fallback nume: în ESP, `{{FIRST_NAME}}` cu valoare implicită goală și salutul condiționat (dacă există nume: „Hei, Andreea!”; dacă nu: „Hei!”). Dacă numele depășește 19 caractere, se folosește tot „Hei!”.

**Adnotări hero (arse în imagine, max 2 rânduri x 12 car.):**
| # | Rând 1 | Rând 2 | Sursă |
|---|---|---|---|
| 1 | APROAPE TOT (11) | E ÎN MIX (8) | [adaptat din site: „mixuri în care e deja aproape tot”] |
| 2 | REPEDE (6) | ȘI SIMPLU (9) | [confirmat de client, 12.10.2026] |
| 3 | FĂRĂ (4) | CONSERVANȚI (11) | [din site] |

Toate trei există și ca text live în S4 (cine are imaginile blocate nu pierde informația).

### S2-coș (bloc dinamic `{{CART_ITEMS}}`)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Etichetă secțiune | **ÎN COȘUL TĂU** [nou] | 12 | max 20 |
| Per produs | imagine, nume, cantitate, preț: toate din ESP | | |
| Etichetă cantitate | **Cantitate:** {{qty}} | 10 + valoare | |
| Rând total (opțional, depinde de ESP) | **Total produse:** {{total}} | 14 + valoare | |

- „Total produse”, nu „Total”: suma din coș nu include transportul, care se calculează în checkout.
- Fără buton per produs (un singur CTA după listă, convenit cu designerul).
- Dacă ESP-ul nu poate randa `{{CART_ITEMS}}`, blocul se ascunde, iar emailul funcționează doar cu hero + CTA.

### S3-CTA principal

| Element | Text | Car. | Limită |
|---|---|---|---|
| Buton pill (negru, text portocaliu) | **Finalizează comanda** [nou] → `{{CHECKOUT_URL}}` | 19 | max 22 |
| Microcopy sub buton | fără (decis cu designerul: transportul apare doar în S4, ca să nu aglomereze zona butonului) | | |

`{{CHECKOUT_URL}}` trebuie să refacă coșul (cu produsele și cantitățile), nu să ducă într-un coș gol. [DE CONFIRMAT CU CLIENTUL / dezvoltator] UTM: `utm_source=email&utm_medium=flow&utm_campaign=checkout_01&utm_content=cta_main`.

### S4-USP (turcoaz, 3 coloane pe desktop, stivuite pe mobil)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Titlu secțiune | **DE CE O SĂ-ȚI PLACĂ** [nou] | 19 | max 26 |

| # | Titlu (Akrobat Bold 20, uppercase) | Car. | Rând sub titlu (Arial) | Car. | Sursă |
|---|---|---|---|---|---|
| 1 | **TRANSPORT GRATUIT** | 17 | De la al 2-lea produs din coș. | 30 | [adaptat din site] |
| 2 | **REPEDE ȘI SIMPLU** | 16 | Mixul are deja aproape tot în el. | 33 | [confirmat de client, 12.10.2026] |
| 3 | **FĂRĂ CONSERVANȚI** | 16 | Ingrediente pe care le recunoști. | 33 | [din site] |

Limite convenite: titlu max 20 car., max 2 rânduri, cuvânt max 12 car.; rând sub titlu max 50 car.

Note:
- USP 3 a fost reformulat la cererea designerului („Ingrediente pe care le recunoști” are 32 car. și ieșea pe 3-4 rânduri în coloană): claim-ul scurt „fără conservanți” devine titlu, iar formularea aprobată coboară în rândul de sub el. Ambele sunt confirmate în discovery. Nu folosim „fără E-uri” (Pizza Crust Mix conține emulsificator).
- USP 2: clientul a ales varianta generală „Repede și simplu” (12.10.2026), valabilă pentru toată gama. „Gata în 5 minute / adaugi apă” e adevărat doar la Pankees, deci nu se folosește aici.
- USP 1: confirmat de client (12.10.2026): transport gratuit de la al 2-lea produs.
- Iconițe (designer): cutie/livrare, ceas sau tel, spic sau frunză. Fără bife verzi, fără steluțe de rating.

### S5-închidere + CTA secundar (portocaliu)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Titlu (Akrobat uppercase) | **ÎNCĂ TE GÂNDEȘTI?** [nou] | 17 | max 32, max 3 rânduri |
| Rând (Arial 16) | Răsfoiește toată gama: pancakes, clătite, prăjituri și pizza. [adaptat din site] | 61 | max 70 |
| Buton outline (contur negru 2px, text negru) | **Vezi toate mixurile** [nou] → `{{SHOP_URL}}` | 19 | max 22 |
| Semnătură sub buton | **eat what you love** [din site, slogan oficial] | 17 | |

Rând alternativ (dacă preferați să deschideți conversația în loc de a trimite spre gamă): Ai o întrebare? Dă reply la emailul ăsta, îți răspundem noi. (60) [nou]. Îl folosim doar dacă reply-to e monitorizat zilnic. Recomandarea mea e varianta cu gama în Email 1 și subiectul „suport” în Email 2, unde e deja printre USP.

UTM buton: `utm_content=cta_shop`. `{{SHOP_URL}}` = pagina PRODUSE de pe site-ul nou. [DE CONFIRMAT CU CLIENTUL: URL-ul final]

### S6-footer

> Lucas Bites · Roșu, Chiajna, Ilfov
> office@lucasbites.ro · +40 731 399 399
>
> Primești acest email pentru că ai început o comandă pe lucasbites.ro și ai acceptat să primești emailuri de la noi.
>
> Nu mai vrei emailuri de la noi? [Dezabonează-te aici]({{UNSUBSCRIBE_URL}}). Durează un click.
>
> © 2026 Lucas Bites

- Iconițe social ca în welcome: Instagram, TikTok, Facebook, YouTube (aceleași linkuri ca în `welcome-01/brief.md`).
- `{{UNSUBSCRIBE_URL}}` = tag-ul de dezabonare al ESP-ului; header-ele `List-Unsubscribe` + `List-Unsubscribe-Post` (one-click, RFC 8058) active.
- Fraza „ai acceptat să primești emailuri” rămâne: checkout-ul colectează acordul de marketing (confirmat 12.10.2026).
- Denumirea juridică și CUI intră în footer (confirmat 12.10.2026). [DE PRIMIT DE LA CLIENT: denumirea SRL și CUI-ul]

---

## 4. Alt text

| Imagine | Alt text |
|---|---|
| Logo header | Lucas Bites |
| Hero | Teanc de pancakes pufoase cu bucăți de ciocolată. Repede și simplu, fără conservanți. |
| Clătite S5 | Clătite rulate cu cremă de ciocolată, alune și zahăr pudră |
| Iconițe USP | `alt=""` (decorative, textul e live alături) |
| Logo footer | Lucas Bites, eat what you love |
| Iconițe social | Instagram / TikTok / Facebook / YouTube |

Alt-ul hero include adnotările, pentru că sunt arse în imagine.

---

## 5. Comunicare cu UI Designer

- Structura a fost trimisă înainte de copy, iar feedback-ul a venit în aceeași sesiune. Integrat: limitele de caractere de mai sus, H1 de 23 car., USP 3 reformulat sub 20 car., transportul doar în S4 (fără microcopy sub CTA), titlul S5 sub 32 car. cu rând separat, CTA secundar ca buton outline, eticheta „Total produse” pentru rândul de total opțional, 3 adnotări hero.
- Designerul construiește cu textele exacte și semnalează dacă ceva nu încape.

---

## 6. Întrebări pentru client

1. **Transport gratuit de la al 2-lea produs:** e valabil la lansare? Se aplică și la 2 bucăți din același produs? Există valoare minimă a coșului sau excepții (gama Professional, zone)?
2. **ESP și date de coș:** ce platformă folosim și poate trimite produsele din coș (nume, imagine, cantitate, preț, total) plus un link de checkout care reface coșul?
3. **Consimțământ:** checkout-ul are bifă de acord pentru emailuri de marketing? Emailul de abandon se trimite doar contactelor cu acord.
4. **Comenzi în ESP:** magazinul trimite evenimentul de comandă plasată în timp real? Fără el nu putem scoate din flow cine a cumpărat între timp.
5. **Timing:** sunteți de acord cu 1 oră (Email 1) și 24 de ore (Email 2) după Checkout Started?
6. **USP 2:** acceptați „Gata în 5 minute / Adaugi apă, agiți și gătești” și pentru coșurile care conțin doar Brownie sau Lava Cake, sau folosim varianta generală „Repede și simplu”?
7. **URL-ul paginii de produse** pe site-ul nou (pentru `{{SHOP_URL}}`).

### Răspunsuri client (12.10.2026)
1. Transport gratuit de la al 2-lea produs: confirmat.
2. ESP: **theMarketer**. Poate afișa produsele din coș; feed-ul de produse îl adaugă clientul în editor. În `index-esp.html` blocul de coș are placeholder-ul `[FEED PRODUSE THEMARKETER]`.
3. Consimțământ marketing la checkout: da.
4. Timing: Email 1 la 30 de minute, Email 2 la 24 de ore după Checkout Started.
5. USP 2: „Repede și simplu”.
6. URL produse și denumire juridică / CUI în footer: da. [DE PRIMIT DE LA CLIENT: URL-ul exact, denumirea SRL, CUI-ul]
Rămân deschise: întrebarea 4 (evenimentul de comandă plasată în timp real în theMarketer) și link-ul de checkout care reface coșul.
