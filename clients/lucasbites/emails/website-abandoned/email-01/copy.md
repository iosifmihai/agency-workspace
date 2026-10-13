# Lucas Bites: Website Abandoned, Email 1, copy final

Surse: `strategy.md` (acest folder: unghi, secțiuni S0-S6, limite, categorii, recenzii, USP, UTM, placeholdere; are prioritate), `brief.md`, `../README.md`, `discovery.md` (inclusiv 8b), `../../browse-abandonment/email-01/copy.md` (format, footer, ce nu repetăm), `../../welcome-02/copy.md` (textele categoriilor), `../../welcome-03/copy.md` (recenziile reale și regulile de citare), `../../checkout-started/email-01/copy.md` și `email-02/copy.md` (USP, recenzii, ce nu repetăm), `../../welcome-01/copy.md` (subiecte și închideri deja folosite). Legendă: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [adaptat] = text aprobat ajustat pentru email, [nou] = text nou, de aprobat de client, [din site actual] = recenzie reală de pe lucasbites.ro, citată cuvânt cu cuvânt, ca în `welcome-03/copy.md`, [confirmat] = confirmat de client, [DE CONFIRMAT CU CLIENTUL] = marcaj păstrat din strategie sau adăugat aici.

**Ce cere clientul:** prezentare categorii website + secțiune cu recenzii de la clienți + USP.

**Reguli:** fără prețuri, fără discount, fără urgență falsă, fără promisiuni de sănătate sau nutriționale, fără „cel mai bun”, fără „gata în 5 minute” (valabil doar la Pankees), fără „fără E-uri” (Pizza Crust Mix are emulsificator), fără „făină nealbită” generalizat. Fără nicio referire la vizită: fără „ai fost pe site”, „te-am văzut”, „ai plecat”, „ai uitat”, „coș”. Emailul se citește ca un tur scurt al gamei. Linkurile sunt doar placeholdere, le pune Andreea în theMarketer.

Caracterele sunt numărate cu spații și punctuație; o literă cu diacritice = 1 caracter.

---

## 1. Subiecte și preheadere

| # | Subiect | Car. | Preheader | Car. |
|---|---|---|---|---|
| A **[recomandat]** | Un tur scurt prin mixurile noastre [nou] | 34 | Pancakes, prăjituri, budinci și pizza, plus ce spun cei care le-au încercat. [adaptat din site, categoriile v3] | 76 |
| B | Ce găsești la Lucas Bites [nou] | 25 | Cinci categorii, recenzii reale și transport gratuit de la al 2-lea mix. [nou; transport confirmat] | 72 |
| C | De la micul dejun la movie night [adaptat din site, momentele de consum] | 32 | Pancakes, clătite, prăjituri, budinci și pizza, fiecare cu momentul ei. [adaptat din site] | 71 |

Limite: subiect max ~40 car., preheader max 90 car.

**De ce A:** spune exact ce e emailul (un tur al gamei, nu o reamintire), deci funcționează pentru cineva care nu știe încă ce caută și nu sugerează că știm ceva despre vizită. Preheaderul numește categoriile din S2 și anunță recenziile din S3, deci promisiunea din inbox e plătită în corpul emailului. Nu seamănă cu subiectele folosite („Trei idei pentru pofta de azi”, „Pofta ta e încă în coș”, „Nu ne crede pe cuvânt”, „Ce pui tu și ce am pus noi”, „Le încerci pe toate?”).

**B** e varianta directă, de orientare: se plătește în H2-ul din S2 („CE GĂSEȘTI LA NOI”). **C** e varianta pe momente; se potrivește dacă datele arată că etichetele de moment aduc click-uri.

**Test:** A vs B după primele ~500 de trimiteri pe variantă; câștigătorul se alege pe rata de conversie (comenzi atribuite `utm_campaign=website_01`), nu pe deschideri.

**Fără prenume în subiect:** `{{FIRST_NAME}}` lipsește des; numele apare doar în salutul din S1, cu fallback.

**Expeditor:** Lucas Bites. **Reply-to:** office@lucasbites.ro (sau altă adresă monitorizată).

---

## 2. Copy pe secțiuni (ordinea din `strategy.md`)

### S0-logo

Logo complet pe fundalul hero-ului (reguli de fundal din discovery 7). Fără text.

### S1-hero (scurt, fără buton)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Salut | **Hei, {{FIRST_NAME}}!** / fallback: **Hei!** [ca în checkout și browse] | 20 (cu placeholder) / 4 | max 25 |
| H1 (Akrobat Black, uppercase) | **CE PUNEM AZI PE MASĂ?** [nou] | 21 | max 28, max 2 rânduri, cuvânt max 12 |
| Text (Arial 16/24) | Mixuri în care e deja aproape tot, de la micul dejun la movie night. Le luăm pe rând. [adaptat din site: „mixuri în care e deja aproape tot”, momentele de consum; ultima frază nouă] | 85 | ideal 70-90, max 110 |

- Despărțire H1 (desktop și mobil): „CE PUNEM AZI” (12) / „PE MASĂ?” (8).
- Fallback nume: salut condiționat, „Hei!” dacă lipsește numele sau dacă are peste 19 caractere.
- „Masa” trimite la povestea brandului („ne strângem toți în jurul mesei” [din site actual]), fără să o citeze. Diferit de „TE AȘTEPTĂM LA MASĂ.” (Checkout 2), care e închidere, nu titlu.
- „Le luăm pe rând” face trecerea spre categorii și nu promite nimic despre ce a căutat omul.

### S2-categorii (secțiunea principală)

| Element | Text | Car. | Limită |
|---|---|---|---|
| Supratitlu | **cinci feluri de poftă** [nou] | 21 | max 25 |
| H2 (Akrobat Black, uppercase) | **CE GĂSEȘTI LA NOI** [nou] | 17 | max 26, max 2 rânduri |
| Intro (Arial 16) | Alege o categorie și vezi toate mixurile din ea. [nou] | 48 | max 70 |

**Cardurile** (fără prețuri, fără ratinguri per categorie; tot cardul e link):

| Element | Card 1 | Car. | Card 2 | Car. | Card 3 | Car. | Card 4 | Car. | Card 5 | Car. | Limită |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Etichetă moment | **micul dejun în familie** [adaptat din site, momente] | 22 | **pauza de la birou** [din site, moment] | 17 | **nou în gamă** [din W2] | 11 | **movie night** [din site, moment] | 11 | **vegan / de post** [din site, filtrul de pe v3] | 15 | max 24 |
| Nume categorie (Akrobat Bold, uppercase) | **PANCAKES & CRÊPES** [din site] | 17 | **PRĂJITURI** [din site] | 9 | **BUDINCI** [din site] | 7 | **PIZZA** [din site] | 5 | **DE POST** [din site actual, „Produse de post”] | 7 | max 18 |
| Rând de conținut | Pancakes pufoase și clătite subțiri. [adaptat din site] | 36 | Patru mixuri, dintre care două noi în gamă. [adaptat din site, `welcome-02`] | 43 | Un desert de lingură, nou la Lucas Bites. [adaptat din W2] | 41 | Blatul îl faci tu, topping-ul îl alegi tot tu. [adaptat din W2: „apoi pui ce topping vrei”] | 46 | Vegan Classic Pankees, pentru zilele de post. [din site, numele produsului; rând nou] | 45 | max 50 |
| CTA (link-buton) | **Vezi categoria** [nou] → `{{CATEGORY_URL_1}}`, `utm_content=cat_pancakes` | 14 | **Vezi categoria** → `{{CATEGORY_URL_2}}`, `utm_content=cat_prajituri` | 14 | **Vezi categoria** → `{{CATEGORY_URL_3}}`, `utm_content=cat_budinci` | 14 | **Vezi categoria** → `{{CATEGORY_URL_4}}`, `utm_content=cat_pizza` | 14 | **Vezi produsul** [nou; De post e produs separat, confirmat 13.10.2026] → `{{CATEGORY_URL_5}}`, `utm_content=cat_post` | 13 | max 16 |

| Element | Text | Car. | Limită |
|---|---|---|---|
| Link sub carduri | **Vezi toate produsele** [nou] → `{{SHOP_URL}}`, `utm_content=cat_toate` | 20 | max 22 |

Note S2:
- **Ordinea** e cea din strategie: Pancakes & Crêpes, Prăjituri, Budinci, Pizza, De post. Placeholderele `{{CATEGORY_URL_n}}` urmează ordinea cardurilor.
- **Etichetele** nu repetă formularea din W2 („pentru duminica fără grabă”, „pentru pauza de la birou”, „pentru movie night”): fără „pentru”, iar la Pancakes alt moment („micul dejun în familie”).
- **Pancakes & Crêpes:** rândul nu repetă formula W2 („cât timp se face cafeaua”). Fără „gata în 5 minute” și fără „doar apă”.
- **Prăjituri:** „patru mixuri” = Brownie, Lava Cake, Banana Bread (NOU), Carrot Cake (NOU), din tabelul de categorii aprobat. Nu descriem gustul. Cookie Mix nu e numit (întrebarea 6 din strategie).
- **Budinci:** nu scriem aroma și nici ce adaugi (lapte sau apă) până nu confirmă clientul (întrebarea 9 din strategie).
- **De post:** eticheta „vegan / de post” e numele filtrului de pe v3, deci repetă parțial numele categoriei. Dacă UI vrea o etichetă care nu repetă „post”, rezerva e **vegan** (5) [din site, filtrul de pe v3]. Fără afirmații de sănătate, fără trimitere la postul Crăciunului (cardul rămâne tot anul).
- **CTA identic pe toate cardurile:** cardul întreg e link, iar un text scurt și constant ajută scanarea. Variantă jucăușă, dacă UI preferă: „Hai la pancakes” (15), „Hai la prăjituri” (16, la limită), „Hai la budinci” (14), „Hai la pizza” (12); la De post CTA-ul e „Vezi produsul” (13), produs separat (13.10.2026).
- „Vezi toate produsele” e diferit de „Vezi toate mixurile” (W2, W3, Checkout 1).

### S3-recenzii

| Element | Text | Car. | Limită |
|---|---|---|---|
| Titlu secțiune (Akrobat, uppercase) | **ÎNCERCATE ȘI NOTATE** [nou] | 19 | max 24, ideal 1 rând |
| Cifra | **4,9** + **din 5** [din site] | | element vizual (UI) |
| Stele | 5 stele (doar la medie, nu per card) | | |
| Sub cifră | **peste 1.100 de recenzii** [din site] [confirmat, valabil la 10.10.2026] | 23 | max 30 |

**Cardurile** (citatele copiate exact din `welcome-03/copy.md`, fără nicio modificare):

| Card | Citat | Car. | Nume (max 16) | Car. | Produs (max 22) | Car. | Sursă |
|---|---|---|---|---|---|---|---|
| Mare, toată lățimea (max 120) | „Am folosit amestecul pentru blat de pizza, Pizza Crust Mix, 500g și mi-au ieșit două pizza delicioase!” | 104 | **Irina A.** | 8 | Pizza Crust Mix | 15 | [din site actual, diacritice corectate], `welcome-03` S3, card 2; original Irina Anghel, 03.03.2022 |
| Mic (max 90) | „Clătitele ies foarte pufoase și gustoase. O adevărată plăcere să le faci și să le mănânci” | 91 (cu ghilimele; limita de 90 se aplică textului fără ghilimele, 89: UI Designer verifică să încapă) | **Andreea H.** | 10 | Classic Pankees | 15 | [din site actual, diacritice corectate, emoji eliminate], `welcome-03` S3, card 1 |
| Mic (max 90) | „Bun. Rețeta este foarte bună” | 30 | **Liliana F.** | 10 | Brownie Mix | 11 | [din site actual, diacritice corectate], `welcome-03` S2, card 4; original „FLOREA LILIANA”, 26.11.2023 |

| Element | Text | Car. | Limită |
|---|---|---|---|
| Link sub carduri | **Vezi toate recenziile** [nou] → `{{REVIEWS_URL}}`, `utm_content=recenzii_toate` | 21 | max 26 |

Note S3:
- **Caracterele citatelor** sunt numărate fără ghilimele. Ghilimelele românești („ ”) se păstrează, ca în W3 și Checkout 2.
- **Fără stele și fără date pe carduri**, conform strategiei: stelele apar doar la media 4,9 (nota fiecărei recenzii nu e verificată). Datele rămân doar în coloana „Sursă”, ca referință. Formatul nume / produs pe rânduri separate e cel din Checkout 2.
- **Titlul** diferă de „CE SPUN CLIENȚII” (Checkout 2) și „NU DOAR NOI LE LĂUDĂM.” (W3) și se leagă de preheaderul A („cei care le-au încercat”) și de cifra de dedesubt.
- **Rezervă pentru Liliana F.** (dacă numele nu se confirmă): **Irina S.** · Classic Pankees · „Sunt foarte încântată de aceste produse! Sunt minunate! Voi reveni cu comenzi!” (78) [din site actual], `welcome-03` S3, card 3. A doua rezervă: **Gabriela P.** · Classic Pankees · „Pufoase și delicioase!” (22) [din site actual], `welcome-03` S2.
- „Vezi toate recenziile” e diferit de „Citește toate recenziile” (W3).

### S4-USP

| Element | Text | Car. | Limită |
|---|---|---|---|
| Titlu secțiune | **BINE DE ȘTIUT** [nou] | 13 | max 26 |

| # | Titlu (Akrobat Bold 20, uppercase) | Car. | Rând sub titlu (Arial 14) | Car. | Sursă |
|---|---|---|---|---|---|
| 1 Ce e un mix | **APROAPE TOT E ÎN MIX** | 20 | Tu adaugi doar ce scrie pe ambalaj. | 35 | titlu [adaptat din site: „mixuri în care e deja aproape tot”]; rând [adaptat din site, ca în NC1] |
| 2 În magazine | **ȘI ÎN MAGAZINE** | 14 | Kaufland, Carrefour, Dr. Max, eMAG și altele. | 45 | [din site] [confirmat, lista completă]; titlu [nou] |
| 3 Transport | **TRANSPORT GRATUIT** | 17 | Când combini două mixuri, livrarea e pe noi. | 44 | [confirmat, 12.10.2026]; rând [nou] |

Limite: titlu max 20 car., max 2 rânduri, cuvânt max 12; rând ideal 35-45, max 50.

Note S4:
- **Ordinea și setul sunt cele din strategie:** ce e un mix, unde mă găsești, transport (ultimul, singurul argument comercial).
- **USP 1:** rândul nu spune „doar apă” (valabil doar la Pankees) și nu enumeră ce adaugi la fiecare produs (la budincă nu știm încă). „Aproape tot e în mix” a apărut până acum doar ca adnotare arsă în hero-ul Checkout 1, nu ca USP. Titlul are 20 car., la limită (vezi notele UI).
- **USP 2:** „ȘI ÎN MAGAZINE” / patru retaileri + „și altele”, diferit de rezerva Browse („ÎN MAGAZINE” / „Kaufland, Carrefour, eMAG, Freshful și altele.”). Dacă clientul nu vrea retailerii într-un email care măsoară vânzarea online (întrebarea 11 din strategie), alternativa din strategie: **SIMPLU DE FĂCUT** (15) [adaptat din „Repede și simplu”, confirmat 12.10.2026] / Oricine le poate face, repede. (30) [din site]. Diferit de „REPEDE ȘI SIMPLU” (Checkout 1). „ORICINE LE POATE FACE” (21) nu încape în limita de 20.
- **USP 3:** fără „coș”, diferit de „De la al 2-lea produs din coș.” (Checkout 1), „Când pui al 2-lea produs în coș.” (Checkout 2) și „De la al 2-lea mix, ca să încerci două rețete.” (Browse 1). „Combini două mixuri” se leagă de categoriile de mai sus și nu promite nimic despre 2 bucăți din același produs [DE CONFIRMAT CU CLIENTUL, întrebarea 13 din strategie].
- Ingredientele lipsesc intenționat (au fost în toate cele trei emailuri de abandon și în W2). Fără butoane pe USP. Titlul secțiunii diferă de „DE CE O SĂ-ȚI PLACĂ”, „CA SĂ COMANZI LINIȘTIT” și „DE CE LUCAS BITES?”.

### S5-închidere + CTA spre gamă + rândul Professional

| Element | Text | Car. | Limită |
|---|---|---|---|
| Titlu (Akrobat, uppercase) | **NU ȘTII DE UNDE SĂ ÎNCEPI?** [nou] | 26 | max 32, max 3 rânduri |
| Rând (Arial 16) | Începe cu pancakes. Sau cu pizza. Sau cu amândouă. [nou] | 50 | max 70 |
| Buton | **Vezi toată gama** [nou] → `{{SHOP_URL}}`, `utm_content=cta_shop` | 15 | max 22 |
| Semnătură | **eat what you love** [din site, slogan oficial] | 17 | |

Separat vizual (linie subțire sau alt fundal):

| Element | Text | Car. | Limită |
|---|---|---|---|
| Rând Professional (Arial 14) | Ai cafenea, restaurant sau patiserie? Aceeași rețetă, porții constante, preparare rapidă în bucătărie. [adaptat din site, formularea din planul W4] | 102 | max 110 |
| Link Professional (text subliniat) | **Vezi gama Professional** [nou] → `{{PROFESSIONAL_URL}}`, `utm_content=professional` | 22 | max 24 |

- Titlul e o întrebare generală, fără reproș și fără trimitere la vizită; diferit de „ÎNCĂ TE GÂNDEȘTI?”, „TE AȘTEPTĂM LA MASĂ.”, „POFTA NU SE GRĂBEȘTE.”, „EAT WHAT YOU LOVE.”, „IA-LE ÎN PERECHE.”.
- „Sau cu amândouă” trimite discret la transportul gratuit de la al 2-lea produs, fără să-l repete.
- Butonul diferă de „Alege-ți pofta” (Browse 1), „Vezi toate mixurile” (W2, W3, Checkout 1) și „Răsfoiește gama” (fallback Browse 1).
- Dacă UI pune o imagine mică aici, alt text-ul se scrie după ce se alege imaginea (vezi secțiunea 3).

### S6-footer

> Lucas Bites · Roșu, Chiajna, Ilfov
> [DE PRIMIT DE LA CLIENT: denumire juridică SRL] · CUI [DE PRIMIT DE LA CLIENT]
> office@lucasbites.ro · +40 731 399 399
>
> Primești acest email pentru că ai acceptat să primești emailuri de la Lucas Bites. [nou, identic cu Browse 1] [DE CONFIRMAT CU ANDREEA]
>
> Nu mai vrei emailuri de la noi? [Dezabonează-te aici]({{UNSUBSCRIBE_URL}}). Durează un click.
>
> © 2026 Lucas Bites

- **Fraza „de ce primești”:** varianta generală de la Browse, fără nicio referire la vizită; acoperă ambele surse de acord (abonați, clienți cu acord la checkout). Dacă la Browse Andreea a decis să o adauge din theMarketer, se aplică la fel aici, iar în HTML rămâne markerul `[ADAUGĂ UTILIZATORUL]` pe aceeași poziție.
- Logo stripes, iconițe social: Instagram, TikTok, Facebook, YouTube (aceleași linkuri ca în `welcome-01/brief.md`). Linkurile social, `mailto:` și `tel:` nu primesc UTM.
- `{{UNSUBSCRIBE_URL}}` = tag-ul de dezabonare theMarketer [neverificat: sintaxa]; `List-Unsubscribe` + `List-Unsubscribe-Post` (one-click, RFC 8058) active.

---

## 3. Alt text

| Imagine | Alt text | Car. |
|---|---|---|
| Logo header | Lucas Bites | 11 |
| Hero | fără imagine mare; element decorativ mic sau imagine mică de mâncare, dacă există: `alt=""` pentru decorativ, altfel de scris după ce se alege imaginea | |
| Card 1, Pancakes & Crêpes | Clătite împăturite cu lămâie și zahăr, cu pancakes în spate | 59 |
| Card 2, Prăjituri | Felie de carrot cake cu morcov ras și nuci | 42 |
| Card 3, Budinci | Lingură plină cu budincă cremoasă, dintr-un bol negru | 53 |
| Card 4, Pizza | Pizza mici de casă, fiecare cu alt topping | 42 |
| Card 5, De post | Pancakes de post cu felii de pară și scorțișoară | 48 |
| Stele S3 | Rating 4,9 din 5 | 16 |
| Ghilimele desenate (carduri), dacă există | `alt=""` (decorativ) | |
| Iconițe USP | `alt=""` (decorative, textul e live alături) | |
| Imagine mică S5 (doar dacă UI o folosește) | de scris după ce se alege imaginea | |
| Logo footer | Lucas Bites, eat what you love | 30 |
| Iconițe social | Instagram / TikTok / Facebook / YouTube (câte una pe iconiță) | |
| Tranziții, forme decorative | `alt=""` | |

Alt-urile cardurilor urmează subiectele vizuale din strategie (secțiunea 5). Dacă imaginea finală diferă (de exemplu carrot cake cu glazură, după întrebarea 8, sau altă aromă de budincă, după întrebarea 9), alt-ul se ajustează la ce se vede. Toate textele (H1, nume de categorii, cifra 4,9, recenzii, USP, butoane) sunt HTML live, deci emailul rămâne complet cu imaginile blocate.

---

## 4. Note pentru UI Designer

- **H1:** rupere fixă „CE PUNEM AZI” (12) / „PE MASĂ?” (8). Cel mai lung cuvânt: „PUNEM” (5).
- **H2 S2:** „CE GĂSEȘTI LA NOI” (17) încape pe un rând; dacă trece pe două: „CE GĂSEȘTI” (10) / „LA NOI” (6).
- **Nume de categorii:** cel mai lung „PANCAKES & CRÊPES” (17 din 18); dacă trece pe două rânduri pe cardurile mici: „PANCAKES &” (10) / „CRÊPES” (6). Nu rupeți „&” pe rândul de jos.
- **Titlul S3:** „ÎNCERCATE ȘI NOTATE” (19), gândit pe un rând; dacă nu încape: „ÎNCERCATE” (9) / „ȘI NOTATE” (9).
- **USP 1:** „APROAPE TOT E ÎN MIX” (20 din 20, la limită); rupere „APROAPE TOT” (11) / „E ÎN MIX” (8).
- **Titlul S5:** „NU ȘTII DE UNDE” (15) / „SĂ ÎNCEPI?” (10).
- **La limită sau aproape:** titlul USP 1 (20 din 20), rândul Pizza (46 din 50) și rândul De post (45 din 50) pe cardurile înguste, rândul USP 2 (45, la capătul idealului), rândul Professional (102 din 110), linkul Professional (22 din 24), linkul „Vezi toate produsele” (20 din 22). Varianta jucăușă de CTA „Hai la prăjituri” are 16 din 16.
- **Recenzii:** citatul Irinei A. (102) doar pe cardul mare; cardurile mici au 89 și 28 car., deci UI echilibrează înălțimea (de exemplu font mai mare pentru citatul scurt). Fără stele per card.
- **Fără GIF**, fără prețuri, fără ratinguri per categorie.
- Lungime: aproximativ 190 de cuvinte de text live fără footer și fără citate, în ținta din strategie (180-230).

---

## 5. Întrebări deschise

1. **Recenzii:** acordul pentru prenume + inițială (Irina A., Andreea H., Liliana F.) și confirmarea că „Liliana” e prenumele autoarei „FLOREA LILIANA”. Dacă nu, cardul trece pe Irina S.
2. **USP 2 „ȘI ÎN MAGAZINE”:** aprobat de client sau trecem pe „SIMPLU DE FĂCUT / Oricine le poate face, repede.”?
3. **De post:** e pagină proprie sau doar filtru pe site-ul nou, și Vegan Classic Pankees e singurul produs de post? (de asta depind rândul și eticheta cardului 5)
4. **Rămân din strategie:** aroma și prepararea budincii, glazura la Carrot Cake (alt text card 2), transportul gratuit la 2 bucăți din același mix, cifra 1.100 / 4,9 la lansare, fraza „de ce primești” din footer, denumirea SRL și CUI.

### Răspunsuri client (13.10.2026)
1. Recenzii cu prenume + inițială: **da**. „Liliana” e prenumele, cardul Liliana F. rămâne.
2. USP 2 „ȘI ÎN MAGAZINE” cu lista de retaileri: **da**.
3. De post: **produs separat** (Vegan Classic Pankees), nu filtru. Cardul 5 duce la produs: CTA **Vezi produsul** (13), placeholder-ul rămâne `{{CATEGORY_URL_5}}` (linkul îl pune Andreea).

