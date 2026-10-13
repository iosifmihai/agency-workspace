# Lucas Bites: Website Abandoned, Email 2, copy final

Surse: `strategy.md` (acest folder: unghi, secțiuni S0-S6, limite, rețete, recomandări, USP, UTM, placeholdere; are prioritate), inclusiv „Decizie Andreea (13.10.2026): rețete”, `brief.md`, `../README.md`, `../email-01/copy.md` (format, footer, ce nu repetăm), `../../browse-abandonment/email-01/copy.md` (format carduri de rețetă, text în jurul placeholder-ului, rotația Gingerbread propusă acolo), `../../new-customer-01/copy.md` (cum a fost prezentată „Clătite pentru toată familia”), `discovery.md` (inclusiv 8b). Legendă: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [adaptat] = text aprobat ajustat pentru email, [nou] = text nou, de aprobat de client, [confirmat] = confirmat de client, [DE CONFIRMAT CU CLIENTUL] = marcaj păstrat din strategie sau adăugat aici.

**Ce cere clientul:** rețete cu produsele Lucas Bites + recomandări de produse „care s-ar putea să-ți placă și pe care merită să le încerci”.

**Build de bază (decizie Andreea, 13.10.2026):** 2 rețete tot anul, **Clătite pentru toată familia** (card 1, `reteta_1`) + **Cookies cu ciocolată neagră** (card 2, `reteta_2`). **Gingerbread Pancakes** nu intră în build; textul pentru schimbul manual de sezon (1 noiembrie - 31 decembrie) e separat, în secțiunea 3.

**Reguli:** fără prețuri, fără discount, fără urgență falsă, fără promisiuni de sănătate sau nutriționale, fără „cel mai bun”, fără „gata în 5 minute”, fără „fără E-uri”, fără „făină nealbită” generalizat. Fără nicio referire la vizită sau la Email 1: fără „ai fost pe site”, „te-am văzut”, „ai plecat”, „ai uitat”, „coș”, „data trecută”. Pe cardurile de rețetă doar ce publică v3 (titlu, produs, timp, moment): fără ingrediente, pași sau descrieri de gust. Textul din jurul recomandărilor nu numește niciun produs, preț, categorie sau număr de produse. Linkurile sunt doar placeholdere, le pune Andreea în theMarketer.

Caracterele sunt numărate cu spații, ghilimele și punctuație; o literă cu diacritice = 1 caracter. Fiecare număr a fost verificat de două ori.

---

## 1. Subiecte și preheadere

| # | Subiect | Car. | Preheader | Car. |
|---|---|---|---|---|
| A **[recomandat]** | Din mix, direct în farfurie [nou] | 27 | Două rețete de făcut acasă și câteva mixuri care merită încercate. [nou; „merită încercate” din cererea clientului] | 66 |
| B | Cookies sau clătite azi? [nou; numele rețetelor din site] | 24 | Una pentru gustarea de după școală, una pentru duminica fără grabă. [adaptat din site, momentele rețetelor] | 67 |
| C | Mixuri care merită încercate [nou; din cererea clientului] | 28 | Câteva idei de la noi și două rețete de făcut acasă. [nou] | 52 |

Limite: subiect max ~40 car., preheader max 90 car.

**De ce A:** spune ce face emailul (din mix ies rețete) fără să promită nimic despre ce a căutat omul și fără să sugereze că știm de vizită. Merge tot anul, inclusiv în perioada cu Gingerbread, pentru că nu numește rețetele. Preheaderul anunță ambele secțiuni (rețete + recomandări), ca promisiunea din inbox să fie plătită în corp. Nu seamănă cu subiectele din flow-uri („Un tur scurt prin mixurile noastre”, „Ce găsești la Lucas Bites”, „Trei idei pentru pofta de azi”, „Pofta ta e încă în coș”, „Nu ne crede pe cuvânt”).

**B** e varianta concretă, pe rețete. Numește clătitele, deci în perioada cu Gingerbread se schimbă și ea (secțiunea 3). **C** e varianta pe recomandări; se folosește doar dacă fallback-ul de best sellers e mereu activ (strategie, secțiunea 6), altfel subiectul poate promite o secțiune care nu apare.

**Test:** A vs B după primele ~500 de trimiteri pe variantă; câștigătorul se alege pe rata de conversie (comenzi atribuite `utm_campaign=website_02`), nu pe deschideri.

**Fără prenume în subiect:** `{{FIRST_NAME}}` lipsește des; numele apare doar în salutul din S1, cu fallback.

**Expeditor:** Lucas Bites. **Reply-to:** office@lucasbites.ro (sau altă adresă monitorizată).

---

## 2. Copy pe secțiuni (ordinea din `strategy.md`)

### S0-logo

Logo complet pe fundalul hero-ului (reguli de fundal din discovery 7). Fără text.

### S1-hero (scurt, fără buton)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Salut | **Hei, {{FIRST_NAME}}!** / fallback: **Hei!** [ca în Email 1] | 20 (cu placeholder) / 4 | max 25 |
| H1 (Akrobat Black, uppercase) | **HAI ÎN BUCĂTĂRIE!** [nou] | 17 | max 28, max 2 rânduri, cuvânt max 12 |
| Text (Arial 16/24) | Două rețete cu mixurile noastre și câteva sugestii de la noi, pentru când ai poftă. [nou] | 83 | ideal 70-90, max 110 |

- Fallback nume: salut condiționat, „Hei!” dacă lipsește numele sau dacă are peste 19 caractere.
- H1 e o invitație, nu o urmărire. Diferit de „CE PUNEM AZI PE MASĂ?” (Website 1), „CE FACI CU POFTA ASTA?” (Browse), „POFTA TA E ÎNCĂ ÎN COȘ.” și „NU NE CREDE PE CUVÂNT.” (Checkout).
- Textul anunță cele două lucruri din email fără să numească produse și fără „mai jos”. „Sugestii” rămâne general: dacă S3 nu se afișează, fraza nu trimite la un loc gol din pagină.

### S2-rețete (secțiunea principală)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Supratitlu | **din mix, în farfurie** [nou] | 20 | max 25 |
| H2 (Akrobat Black, uppercase) | **PUNE MIXUL LA TREABĂ** [nou] | 20 | max 26, max 2 rânduri |
| Intro (Arial 16) | Fiecare rețetă are mixul ei. Tu alegi cu care începi. [adaptat din site: „Fiecare rețetă îți spune ce produs folosește.”] | 53 | max 70 |

**Cardurile** (doar ce e publicat pe v3: titlu, produs, timp, moment; tot cardul e link):

| Element | Card 1 | Car. | Card 2 | Car. | Limită |
|---|---|---|---|---|---|
| Etichetă moment (chip) | **duminica fără grabă** [din site, moment] | 19 | **gustarea de după școală** [din site, moment] | 23 | max 24 |
| Titlu rețetă (Akrobat Bold, uppercase) | **CLĂTITE PENTRU TOATĂ FAMILIA** [din site] | 28 | **COOKIES CU CIOCOLATĂ NEAGRĂ** [din site] | 27 | max 30, max 2 rânduri, cuvânt max 12 |
| Rând „Cu {produs}” | Cu Crêpes Traditional [din site] | 21 | Cu Cookie Mix [din site actual, categoria „Cookie Mix”, discovery 8b] [DE CONFIRMAT CU CLIENTUL: numele exact] | 13 | max 32 |
| Rând info | Familie · 10 min [din site] | 16 | Desert · 14 min [din site] | 15 | max 22 |
| CTA (link-buton) | **Vezi rețeta** [din site] → `{{URL_RETETA_CLATITE}}`, `utm_content=reteta_1` | 11 | **Vezi rețeta** → `{{URL_RETETA_COOKIES}}`, `utm_content=reteta_2` | 11 | max 16 |

| Element | Text | Car. | Limită |
|---|---|---|---|
| Link sub carduri | **Mai multe rețete** [nou] → `{{RECIPES_URL}}`, `utm_content=retete_toate` | 16 | max 22 |

Note S2:
- **Clătite, prezentate altfel decât în New Customer 1:** acolo erau al treilea card dintr-o listă, cu titlu și un singur rând compus („Cu Crêpes Traditional · 10 min · Familie”), fără etichetă, cu imaginea platoului cu clătite rulate. Aici sunt primul card, cu etichetă de moment, produsul și info pe rânduri separate, în layout-ul de „fișă de rețetă” și cu imagine nouă (vezi alt text și notele UI).
- **Etichetă card 1:** „duminica fără grabă” e momentul propus de strategie. W2 a folosit „pentru duminica fără grabă” pe un card de categorie; aici e fără „pentru”, ca în regula din Website 1. Dacă Andreea vrea o etichetă care să nu apară deloc în altă parte: **mic dejun de weekend** (20) [adaptat din site, momentele „mic dejun” și „weekend”]. Atunci preheaderul B se ajustează: „Una pentru gustarea de după școală, una pentru micul dejun de weekend.” (69).
- **Fără rând de poftă pe carduri:** strategia nu îl prevede și v3 nu publică ingrediente sau gust pentru aceste rețete. Nu am pus „doar apă” la clătite (cantitatea de 675 ml e de pe site-ul actual, pentru Crêpes Mix Original, nu pentru Crêpes Traditional).
- **Cookie Mix (decizie Andreea, 13.10.2026):** numele exact nu e cunoscut, deci rândul folosește „Cookie Mix”, ca în lista de categorii din discovery 8b [DE CONFIRMAT CU CLIENTUL]. Când se confirmă numele: „Cu Cookie Mix Dark Chocolate” (28) încape; „Cu Cookie Mix Dark Chocolate Chip” (33) depășește limita de 32 cu 1 car.
- **CTA identic pe ambele carduri** („Vezi rețeta”, ca pe site): cardul întreg e link. Variantă jucăușă, dacă UI preferă: **Hai la clătite** (14) / **Hai la cookies** (14) [nou].
- „Mai multe rețete” e diferit de „Toate rețetele” (Browse 1, NC1) și de „Vezi toate produsele” (Website 1).
- Placeholdere: dacă o rețetă nu are pagină proprie, cardul duce la `{{RECIPES_URL}}` (fallback din strategie).

### S3-recomandări de produse (PLACEHOLDER theMarketer)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Chip (negru, text portocaliu) | **MERITĂ ÎNCERCATE** [nou; din cererea clientului] | 16 | max 20 |
| H2 (Akrobat Black, uppercase) | **S-AR PUTEA SĂ-ȚI PLACĂ** [nou; din cererea clientului] | 22 | max 26, max 2 rânduri |
| Intro (Arial 16) | Câteva mixuri din gamă, fiecare cu pofta lui. [nou] | 45 | max 70 |
| Bloc produse | `[RECOMANDĂRI PRODUSE THEMARKETER]` între comentariile `THEMARKETER_FEED START` / `THEMARKETER_FEED END` în `index-esp.html`; în `index.html` (preview): 3 carduri marcate **EXEMPLU**. Imagine, nume, (preț, rating) și link le generează blocul adăugat manual de Andreea. | | |
| Buton sub bloc (doar dacă blocul nu are butoane proprii) | **Vezi și alte mixuri** [nou] → `{{SHOP_URL}}`, `utm_content=cta_rec` | 19 | max 22 |

Note S3:
- **Merge pentru orice produs:** niciun nume, preț, categorie sau număr („câteva” acoperă 2, 3 sau 4 produse). „Mixuri” e corect pentru orice produs din gama pentru acasă (Professional e exclus din grilă, strategie secțiunea 6). Nicio legătură cu rețetele de deasupra și nicio formulare de tip „știm ce ai căutat” („pe baza vizitei”, „alese pentru tine”, „produsele tale”). „S-ar putea să-ți placă” rămâne adevărat și când blocul afișează fallback-ul de best sellers.
- **Prețul și ratingul se afișează în bloc** (decizie Andreea, 13.10.2026, setare de feed). Textul din jur nu le dublează: fără preț, fără stele, fără „bine notate” sau „la prețul de”. Sunt generate de sistem, deci nu încalcă regula „fără prețuri” a copy-ului.

**Fallback (blocul nu are niciun rezultat):**
- **Varianta recomandată (din strategie):** toată secțiunea S3 (chip, H2, intro, buton) se ascunde; emailul merge S1 → S2 → S4 → S5. Nu e nevoie de text.
- **Doar dacă theMarketer nu poate ascunde secțiunea** și grila ar rămâne goală, în locul blocului intră:

| Element | Text | Car. | Limită |
|---|---|---|---|
| Chip și H2 | rămân (generale, nu promit produse anume) | | |
| Rând (în locul intro-ului și al grilei) | Toată gama e aici, fiecare mix cu pagina lui. [nou] | 45 | max 70 |
| Buton | **Vezi gama completă** [nou] → `{{SHOP_URL}}`, `utm_content=cta_rec` | 18 | max 22 |

### S4-USP (bandă compactă)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Titlu secțiune (opțional; UI decide) | **PE SCURT** [nou] | 8 | max 26 |

| # | Titlu (Akrobat Bold 18, uppercase) | Car. | Rând sub titlu (Arial 14) | Car. | Sursă |
|---|---|---|---|---|---|
| 1 Simplu | **SIMPLU DE FĂCUT** | 15 | Oricine le poate face, fără bătaie de cap. | 42 | titlu [adaptat din „Repede și simplu”, confirmat 12.10.2026; alternativa nefolosită din Website 1]; rând [adaptat din site: „oricine le poate face, repede”; „fără bătaie de cap” din tonul aprobat, discovery 3] |
| 2 Ingrediente | **LE RECUNOȘTI** | 12 | Ingredientele din mix, fără conservanți. | 40 | [adaptat din site: „Ingrediente pe care le recunoști”; „fără conservanți” din site, confirmat] |
| 3 Transport | **TRANSPORT GRATUIT** | 17 | Alegi două mixuri? Livrarea nu costă nimic. | 43 | [confirmat, 12.10.2026: transport gratuit de la al 2-lea produs]; rând [nou] |

**Limita titlurilor USP: max 18 car., un singur rând.** Coloana are ~180 px pe desktop, iar titlurile sunt la Akrobat Bold 18px, uppercase (cerința din brief: titluri aliniate pe un rând). Strategia permitea 20 car. la 20px; aici limita e mai strictă. Cel mai lung titlu: „TRANSPORT GRATUIT” (17 din 18). Rânduri: ideal 35-45, max 50; toate trei sunt în ideal.

Note S4:
- **Ordinea și setul sunt cele din strategie:** simplu, ingrediente, transport (ultimul, singurul argument comercial).
- **USP 1:** accent pe simplitate, nu pe viteză: fără „repede”, fără „gata în 5 minute”, fără „doar apă” (nu e valabil la toată gama). Diferit de „REPEDE ȘI SIMPLU” (Checkout 1).
- **USP 2:** formulare nouă față de „FĂRĂ CONSERVANȚI” (Checkout 1), „ȘTII CE E ÎN MIX” (Checkout 2), „CE E ÎN MIX” (Browse 1). „Fără conservanți” e valabil pe toată gama (discovery 8b); fără „fără E-uri”, „făină nealbită”, „zahăr brun”. Alternativa din strategie, dacă clientul nu vrea încă un USP de ingrediente: **4,9 DIN 5 STELE** (16) / Media din peste 1.100 de recenzii. (36) [din site] [confirmat], altă formulare decât Browse 1.
- **USP 3:** fără „coș”, diferit de Checkout 1, Checkout 2, Browse 1 („De la al 2-lea mix, ca să încerci două rețete.”) și Website 1 („Când combini două mixuri, livrarea e pe noi.”). Forma de întrebare se leagă de recomandările de deasupra fără să le numească. Dacă transportul e gratuit și la 2 bucăți din același mix rămâne [DE CONFIRMAT CU CLIENTUL]; „două mixuri” nu promite nici una, nici alta.
- Titlul secțiunii diferă de „BINE DE ȘTIUT”, „DE CE O SĂ-ȚI PLACĂ”, „CA SĂ COMANZI LINIȘTIT”, „DE CE LUCAS BITES?”. Fără butoane pe USP.

### S5-închidere + CTA spre gamă

| Element | Text | Car. | Limită |
|---|---|---|---|
| Titlu (Akrobat, uppercase) | **CÂND AI CHEF, NOI SUNTEM AICI.** [nou] | 30 | max 32, max 3 rânduri |
| Rând (Arial 16) | De la pancakes la pizza, alege ce-ți face poftă azi. [adaptat din site, „Alege-ți pofta de azi”] | 52 | max 70 |
| Buton | **Hai în magazin** [nou] → `{{SHOP_URL}}`, `utm_content=cta_shop` | 14 | max 22 |
| Semnătură | **eat what you love** [din site, slogan oficial] | 17 | |

- Ultimul email din flow: închidere caldă, fără termen și fără „ultima șansă”. Titlul diferă de „NU ȘTII DE UNDE SĂ ÎNCEPI?”, „ÎNCĂ TE GÂNDEȘTI?”, „TE AȘTEPTĂM LA MASĂ.”, „POFTA NU SE GRĂBEȘTE.”.
- Butonul diferă de „Vezi toată gama”, „Alege-ți pofta”, „Vezi toate mixurile”, „Răsfoiește gama” și de butoanele din S3.
- Fără rândul Professional (decizia din strategie).
- Dacă UI pune o imagine mică aici, alt text-ul se scrie după ce se alege imaginea (alt subiect decât clătite, cookies și cele 5 categorii din Email 1).

### S6-footer

Identic cu Email 1 (`../email-01/copy.md`, S6):

> Lucas Bites · Roșu, Chiajna, Ilfov
> [DE PRIMIT DE LA CLIENT: denumire juridică SRL] · CUI [DE PRIMIT DE LA CLIENT]
> office@lucasbites.ro · +40 731 399 399
>
> Primești acest email pentru că ai acceptat să primești emailuri de la Lucas Bites. [identic cu Browse 1 și Website 1] [DE CONFIRMAT CU ANDREEA]
>
> Nu mai vrei emailuri de la noi? [Dezabonează-te aici]({{UNSUBSCRIBE_URL}}). Durează un click.
>
> © 2026 Lucas Bites

- Dacă la Browse/Website 1 Andreea adaugă fraza „de ce primești” din theMarketer, se aplică la fel aici, cu markerul `[ADAUGĂ UTILIZATORUL]` pe aceeași poziție.
- Logo stripes, iconițe social: Instagram, TikTok, Facebook, YouTube. Linkurile social, `mailto:` și `tel:` nu primesc UTM.
- `{{UNSUBSCRIBE_URL}}` = tag-ul de dezabonare theMarketer [neverificat: sintaxa]; `List-Unsubscribe` + `List-Unsubscribe-Post` active.

---

## 3. SCHIMB DE SEZON (manual, Andreea): Gingerbread Pancakes, 1 noiembrie - 31 decembrie

**Nu face parte din build-ul de bază.** Andreea înlocuiește manual **cardul 1 (Clătite)** pe 1 noiembrie și pune Clătite înapoi pe 1 ianuarie. Cardul 2 (Cookies) rămâne. Id-ul UTM rămâne `reteta_1` (perioada se citește din data click-ului).

**Ce știm sigur (din strategie, secțiunea 5):** titlul, produsul (Classic Pankees), info (Desert · 15 min) și eticheta „aroma Sărbătorilor de iarnă” [din site, pagina de produs]. **Ce nu știm (confirmat de Andreea, 13.10.2026):** ingredientele, condimentele, topping-ul și gustul [DE CONFIRMAT CU CLIENTUL]. De aceea textul e generic: nu descrie gustul, nu numește ingrediente sau condimente și nu are rând de poftă.

| Element | Text | Car. | Limită |
|---|---|---|---|
| Etichetă moment (chip) | **Sărbătorile de iarnă** [adaptat din site: „aroma Sărbătorilor de iarnă”, 27 car., peste limită] | 20 | max 24 |
| Titlu rețetă (Akrobat Bold, uppercase) | **GINGERBREAD PANCAKES** [din site] | 20 | max 30, max 2 rânduri, cuvânt max 12 |
| Rând „Cu {produs}” | Cu Classic Pankees [din site] | 18 | max 32 |
| Rând info | Desert · 15 min [din site] | 15 | max 22 |
| CTA (link-buton) | **Vezi rețeta** [din site] → `{{URL_RETETA_GINGERBREAD}}` (fallback `{{RECIPES_URL}}`), `utm_content=reteta_1` | 11 | max 16 |
| Alt text imagine (foto sau primul cadru al GIF-ului) | Teanc de gingerbread pancakes [DE CONFIRMAT CU CLIENTUL: se detaliază doar după confirmarea rețetei] | 29 | |

- **Eticheta de rezervă:** **aroma de Sărbători** (18) [adaptat din site]. Atenție: e eticheta propusă pentru rotația sezonieră din Browse 1; dacă acea rotație e activă în aceeași perioadă, aici rămâne „Sărbătorile de iarnă”, ca omul care primește ambele emailuri să nu vadă aceeași etichetă.
- **Varianta jucăușă de CTA** (doar dacă s-a ales și pentru cardul Cookies): **Hai la pancakes** (15) [nou].
- **Restul emailului rămâne neschimbat:** H1, text hero, supratitlu, H2 și intro S2 nu numesc rețetele, deci funcționează și cu Gingerbread.
- **Doar dacă rulează subiectul B**, în aceeași perioadă se schimbă și subiectul și preheaderul:

| Element | Text | Car. | Limită |
|---|---|---|---|
| Subiect B (sezon) | Cookies sau gingerbread azi? [nou] | 28 | max ~40 |
| Preheader B (sezon) | Una pentru gustarea de după școală, una pentru Sărbătorile de iarnă. [adaptat din site] | 68 | max 90 |

Subiectele A și C nu se schimbă.

- **Alt text:** generic, fără ingrediente sau topping, pentru că rețeta nu e confirmată. Se completează cu ce se vede în imagine doar după confirmarea clientului.

---

## 4. Alt text (build de bază)

| Imagine | Alt text | Car. |
|---|---|---|
| Logo header | Lucas Bites | 11 |
| Hero | fără imagine mare; element decorativ mic, dacă există: `alt=""` | |
| Card 1, Clătite pentru toată familia | Clătite de casă pentru toată familia | 36 |
| Card 2, Cookies cu ciocolată neagră | Cookies întregi cu bucăți mari de ciocolată neagră | 50 |
| Carduri produse S3 (`index-esp.html`) | le pune blocul theMarketer (numele produsului din feed) [neverificat]; nu scriem noi | |
| Carduri produse S3 (`index.html`, EXEMPLU) | numele produsului din exemplu (doar preview) | |
| Iconițe USP | `alt=""` (decorative, textul e live alături) | |
| Imagine mică S5 (doar dacă UI o folosește) | de scris după ce se alege imaginea | |
| Logo footer | Lucas Bites, eat what you love | 30 |
| Iconițe social | Instagram / TikTok / Facebook / YouTube (câte una pe iconiță) | |
| Tranziții, forme decorative | `alt=""` | |

- Alt-ul clătitelor e general pentru că imaginea nouă o alege UI (diferită de cele din Checkout 1, NC1, Website 1, W1, Browse 1). După ce se alege, alt-ul se ajustează la ce se vede (de exemplu forma și topping-ul).
- Alt-ul cookies urmează direcția din strategie (cookies întregi, niciunul rupt).
- Toate textele (H1, titluri de rețete, chip, H2, USP, butoane) sunt HTML live, deci emailul rămâne complet cu imaginile blocate.

---

## 5. Note pentru UI Designer

- **H1:** „HAI ÎN BUCĂTĂRIE!” (17) încape pe un rând; dacă trece pe două: „HAI ÎN” (6) / „BUCĂTĂRIE!” (10). Cel mai lung cuvânt: „BUCĂTĂRIE” (9).
- **H2 S2:** „PUNE MIXUL LA TREABĂ” (20); rupere: „PUNE MIXUL” (10) / „LA TREABĂ” (9).
- **Titluri de rețete (pe 2 rânduri):** „CLĂTITE PENTRU” (14) / „TOATĂ FAMILIA” (13); „COOKIES CU” (10) / „CIOCOLATĂ NEAGRĂ” (16); sezon: „GINGERBREAD” (11) / „PANCAKES” (8). Cel mai lung cuvânt: „GINGERBREAD” (11 din 12).
- **H2 S3:** „S-AR PUTEA SĂ-ȚI PLACĂ” (22); rupere: „S-AR PUTEA” (10) / „SĂ-ȚI PLACĂ” (11). Nu rupeți în cratimă.
- **Titlul S5:** „CÂND AI CHEF,” (13) / „NOI SUNTEM AICI.” (16).
- **Titluri USP: max 18 car., un singur rând** în coloana de ~180 px, Akrobat Bold 18px. Setul are 15, 12 și 17 car. Verificați „TRANSPORT GRATUIT” (17) și în fallback-ul de font (`"Arial Narrow"`, apoi Arial, mai lat): dacă pe desktop trece pe două rânduri în Arial, rezerva e **LIVRARE GRATIS** (14) [adaptat, același fapt confirmat]. Pe mobil coloanele se stivuiesc, deci lățimea nu e o problemă acolo.
- **La limită sau aproape:** eticheta „gustarea de după școală” (23 din 24), titlul Clătite (28 din 30), titlul S5 (30 din 32).
- **Cardurile de rețetă** au doar chip, titlu, „Cu {produs}”, info, CTA; fără rând de poftă. Card 1 și card 2 au aceeași structură, ca schimbul de sezon să fie doar înlocuire de text și imagine.
- **Schimbul Gingerbread** (secțiunea 3) e doar pe cardul 1; dacă se face GIF-ul, primul cadru trebuie să funcționeze ca fotografie (Outlook), iar alt-ul descrie acel cadru.
- **S3:** butonul „Vezi și alte mixuri” apare doar dacă blocul theMarketer nu are butoane proprii. Rândul și butonul de fallback („Toată gama e aici...” / „Vezi gama completă”) se folosesc doar dacă secțiunea nu se poate ascunde.
- **Lungime:** aproximativ 140 de cuvinte de text live fără footer și fără textul blocului theMarketer, sub ținta din strategie (160-210). Am preferat cardurile curate (fără rând de poftă, fără descrieri pe care v3 nu le publică); cu grila de recomandări, emailul are oricum 4-5 ecrane pe mobil. Dacă strategul vrea mai mult text, locul potrivit e rândul din S5 (are 18 car. liberi).

---

## 6. Întrebări deschise

1. **Eticheta cardului Clătite:** „duminica fără grabă” (momentul de pe site, folosit deja cu „pentru” în W2) sau „mic dejun de weekend”?
2. **Subiectul C:** se folosește doar dacă fallback-ul de best sellers din blocul theMarketer e mereu activ. Se confirmă la setarea blocului?
3. **Cele mai vândute:** care sunt cele 3 produse pentru acasă pe care le-ați recomanda unui client nou (rezerva blocului de recomandări)?
4. **Rămân din strategie:** numele exact al Cookie Mix; ce conține rețeta Gingerbread Pancakes (ingrediente, condimente, topping); dacă transportul e gratuit și la 2 bucăți din același mix; fraza „de ce primești” din footer, denumirea SRL și CUI.
5. **Produsul clătitelor:** pe v3 e „Crêpes Traditional”, pe site-ul actual „Crêpes Mix Original” (întrebarea deschisă din NC1). Cardul folosește forma de pe v3 până la răspuns.
