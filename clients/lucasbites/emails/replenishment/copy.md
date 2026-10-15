# Lucas Bites: Replenishment, strategie, structură și copy final

Surse: `brief.md` (acest folder, decizii din 14.10.2026), `discovery.md` (inclusiv 8b), `new-customer-01/copy.md` (format, footer, verificări theMarketer), `_reference/ref-misfits.png`, `_reference/ref-olipop-recess.png`. Legendă: [din site] = text aprobat de pe lucasbites.ro/propunere-v3/, [adaptat] = text aprobat ajustat pentru email, [nou] = text nou, de aprobat de client, [neverificat] = funcție theMarketer pe care n-am găsit-o în documentația oficială.

**Ce cere clientul:** un singur email la 14 zile după comandă: „mixurile tale sunt aproape pe terminate” + încurajare spre o nouă comandă.

**Ce fel de email e:** email de marketing post-achiziție, de reaprovizionare. Fără reducere, fără cod, fără rețete, fără prețuri. Singura pârghie e comoditatea: produsele lui, deja alese, la un click distanță.

**Ton:** reamintire prietenoasă, nu presiune. Nu știm sigur că mixul s-a terminat, deci copy-ul spune „s-ar putea”, „dacă”, nu „s-a terminat”.

---

## Ce am adăugat față de structura cerută și de ce

- **S4 „De ce revii la ele”: 3 cifre mari, doar din discovery.** Clientul a gustat deja; îi amintim de ce i-a plăcut (5 minute, ingrediente pe care le recunoaște, 4,9 din 5) fără să inventăm beneficii.
- **S5 dovadă socială doar ca cifră.** Discovery nu conține citate de recenzii, deci nu folosim citate. Cifra 1.100+ / 4,9 apare o singură dată (în S4), nu o repetăm într-un bloc separat.
- **Ce NU am adăugat:** rețete (decizia clientului), cod de reducere (decizia clientului), lista de retaileri (ar trimite clientul la raft, iar KPI-ul e comanda pe site; rămâne în footer-ul de contact doar dacă clientul cere).

---

## 1. Obiectiv, KPI, trimitere

**Obiectiv:** a doua comandă pe site-ul propriu.

**KPI principal:** rata de conversie (comenzi atribuite emailului / emailuri livrate), fereastră de atribuire 7 zile. Țintă 2%+, alertă sub 0,5%.

**KPI secundar:** click unic pe oricare link de produs sau CTA / livrate. Țintă 5%+, alertă sub 2%. CTOR orientativ, țintă 15%+. Rata de deschidere doar orientativ (Apple MPP).

**Trigger și timing:**
- Comandă plasată + **14 zile** (decizia clientului), fereastră de livrare 09:00-20:00, ora României.
- theMarketer are template de reaprovizionare în secțiunea „Post Cumpărare”, cu interval setat pe produs [verificat în `new-customer-01/copy.md`, secțiunea 8]. Aici folosim un interval unic de 14 zile pentru toată gama, conform deciziei. Dacă template-ul nativ cere interval per produs, se setează 14 zile la toate produsele.

**Segment:**
- Intră: cumpărători pe site-ul propriu, pentru acasă, cu temei de marketing (ca la new-customer).
- Exclus: cine a plasat **o comandă nouă în cele 14 zile** (nu îi cerem să recomande ce tocmai a recomandat); comenzi anulate sau returnate; comenzi Professional / HoReCa (1 kg și 10 kg); dezabonați, suprimați.
- **Coliziune:** dacă în aceeași zi pleacă un email din seria new-customer sau welcome, replenishment se amână cu 24 de ore. Maximum un email de marketing în 24 de ore per contact.

**Condiții de ieșire:** comandă nouă înainte de trimitere, dezabonare, hard bounce, plângere spam, comandă anulată sau returnată. Se trimite o dată per comandă; maximum o dată la 30 de zile per contact (dacă cineva comandă des, nu primește emailul la fiecare comandă) [neverificat: limită de frecvență per automatizare].

**UTM:** `utm_source=email&utm_medium=postpurchase&utm_campaign=replenishment&utm_content=<id>`. Valori: `s1-hero`, `s3-produs`, `s3-rezerva`, `s5-cta`.

**Gărzi de siguranță:** plângeri spam sub 0,10%, dezabonări sub 0,5%, hard bounce sub 1%.

---

## 2. Subiecte și preheadere

| # | Subiect | Caractere | Preheader |
|---|---|---|---|
| A **[recomandat]** | Mai ai Pankees în cămară? [nou] | 25 | Dacă mixul e pe terminate, îl comanzi din nou în câteva secunde. [nou] |
| B | Pofta ta de weekend are nevoie de un plin [nou] | 43 | Mixurile tale, la un click distanță. Tu adaugi doar apă. [nou, „adaugi apă” adaptat din site] |
| C | {{FIRST_NAME}}, cum stăm cu mixurile? [nou] | 25 fără nume (rezervă: „Cum stăm cu mixurile?”) | Fă plinul înainte să se termine. Gata în 5 minute, ca data trecută. [nou + din site] |
| D | Nu rămâne fără pancakes duminică [nou] | 32 | Comanzi din nou ce ți-a plăcut, din același loc. [nou] |
| E | Încă o rundă? [nou] | 13 | Mixurile Lucas Bites pe care le-ai ales, gata de recomandat. [nou] |

De ce A: întrebare directă, scurtă, se citește întreagă pe mobil, numește produsul-vedetă al brandului și spune exact unghiul (stocul de acasă), fără presiune și fără tag de prenume neverificat. Riscul: cine a cumpărat doar Pizza sau Brownie. Dacă theMarketer permite subiect condiționat pe categorie [neverificat], varianta pentru restul gamei e E.

**Test A/B:** A contra C (după verificarea tag-ului de prenume), câștigător pe **conversie / livrate**, nu pe deschideri; minimum ~500 livrări pe variantă; sub 0,5 puncte procentuale diferență, fără câștigător.

**Expeditor:** Lucas Bites. **Reply-to:** aceeași adresă ca la welcome și new-customer.

---

## 3. Structura, de sus în jos

Lățime 600px, o coloană pe mobil. Titluri: `Akrobat, "Arial Narrow", Arial, sans-serif`, majuscule, Black. Text: `Arial, Helvetica, sans-serif`, 16px. Separatoare în val între secțiuni. Butoane pastilă bulletproof. Reguli de culoare din brief.

Secțiuni: S0-header, S1-hero, S2-reamintire, S3-produse (bloc dinamic), S4-de-ce-revii (cifre mari), S5-cta-final, S6-footer.

---

### S0-header

- Identic cu familia (logo `Logo/Logo_LucasBites.png`, centrat, 180px, export 360px).

---

### S1-hero

- **Scop:** unghiul spus în 2 secunde și primul click, vizibil fără scroll pe mobil.
- **Pattern:** supratitlu mic „script” deasupra unui titlu supradimensionat; hero de produs cu ingrediente în zbor (ref Olipop/Recess).
- **Copy:**
  - Supratitlu (mic, minuscule; Plicata ca imagine după licență, până atunci Akrobat Bold): **psst, ia uită-te în cămară** [nou]
  - Titlu (H1, 2-3 rânduri, supradimensionat): **MAI E PENTRU O TURĂ?** [nou]
  - Text: Au trecut două săptămâni de la comanda ta. Dacă pofta a fost mare, s-ar putea ca mixul să fie pe terminate. [nou]
  - CTA (pastilă mare): **Comandă din nou** → `{{SHOP_URL}}/cont/comenzi` sau link de recomandă din theMarketer [neverificat] + UTM `s1-hero` [nou]
- **Rezervă CTA** (dacă nu există link de recomandă / pagină de comenzi): → `{{SHOP_URL}}/produse`.
- **IMG1 (spec):** teanc de pancakes în centru, cu ingrediente în zbor în jur (afine, felii de banană, picături de sirop, un nor fin de făină). Fără ambalaj, fără text. Fundal alb simplu pentru decupaj; culoarea plăcii (portocaliu sau turcoaz) o pune UI.

---

### S2-reamintire

- **Scop:** un rând de context care leagă hero-ul de produse; scurt, fără presiune.
- **Copy:**
  - Text (mare, centrat, 20px): Știi deja cum merge: tu adaugi apă, agiți și gătești. [adaptat din site] Noi ne asigurăm doar că nu rămâi fără. [nou]
  - Notă mică sub text (14px): Pașii diferă puțin de la mix la mix. Scrie pe ambalaj ce adaugi. [adaptat din site]
- **Imagine:** nu.

---

### S3-produse (BLOC DINAMIC, PLACEHOLDER)

> **[PLACEHOLDER: BLOC DINAMIC THEMARKETER, produsele cumpărate în comanda care a declanșat emailul / „recomandă din nou”.]**
> Se inserează din editorul theMarketer. Sintaxa și numele blocului NU se ghicesc: se iau din editor sau de la suport (întrebarea 1). Câmpurile de mai jos sunt placeholdere generice, nu sintaxă theMarketer.

- **Pattern:** carduri pe fundal de brand, imagine de produs mare, nume, buton pastilă mic.
- **Copy antet:**
  - Supratitlu mic: **favoritele tale** [nou]
  - Titlu (H2): **FĂ PLINUL** [nou]
- **Card produs (se repetă, maximum 4):**
  - Imagine: `{{ORDER_PRODUCT_IMAGE}}` (din feed)
  - Nume: `{{ORDER_PRODUCT_NAME}}`
  - CTA (pastilă mică): **Adaugă în coș** → `{{ORDER_PRODUCT_URL}}` + UTM `s3-produs` [nou]
  - **Fără preț afișat** (prețurile sunt în lucru). Dacă blocul theMarketer nu permite ascunderea prețului [neverificat], se decide cu clientul înainte de build (întrebarea 3).
- **Rezervă când lipsesc datele de produs:** cardurile dispar, rămâne antetul cu:
  - Text: Mixurile Lucas Bites te așteaptă, toate într-un singur loc. [nou]
  - CTA (pastilă): **Vezi toate mixurile** → `{{SHOP_URL}}/produse` + UTM `s3-rezerva` [din new-customer-01]

---

### S4-de-ce-revii (cifre mari)

- **Scop:** amintește de ce i-a plăcut, fără afirmații noi. Stil Misfits „15G protein”: cifră uriașă, etichetă scurtă dedesubt.
- **Copy:**
  - Titlu (H2): **DE CE REVII LA ELE** [nou]
  - Coloana 1: cifră **5** / etichetă **MINUTE** / text: Ai poftă? Gata în 5 minute. [din site]
  - Coloana 2: cifră **4,9** / etichetă **DIN 5** / text: Media a peste 1.100 de recenzii. [adaptat din site]
  - Coloana 3: iconiță (cântar, asset UI) / etichetă **DEJA LA CÂNTAR** / text: Ingrediente pe care le recunoști, fără conservanți. [adaptat din site]
- **Pe mobil:** cele 3 coloane se stivuiesc.
- **De ce nu „zahăr brun”:** nu e valabil absolut la Brownie (discovery 8b), iar blocul se vede indiferent de produsele cumpărate.
- **Notă:** cifra 1.100 / 4,9 e valabilă la 10.10.2026; se actualizează înainte de lansare, dacă s-a schimbat pe site.

---

### S5-cta-final

- **Scop:** ultimul click, pentru cine a citit până jos.
- **Copy:**
  - Supratitlu mic: **eat what you love** [din site, slogan oficial]
  - Titlu (H2, supradimensionat): **NU LĂSA POFTA SĂ AȘTEPTE.** [nou]
  - CTA (pastilă mare): **Comandă din nou** → același link ca S1 + UTM `s5-cta` [nou]
  - Text sub buton (14px): Ai o întrebare? Scrie-ne la office@lucasbites.ro. [nou]

---

## 4. Footer (S6-footer)

Identic cu W1-W3 și new-customer (`new-customer-01/copy.md`, secțiunea 4). Nu se modifică nimic fără decizia clientului.

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
| S1 | Comandă din nou | link recomandă / `{{SHOP_URL}}/cont/comenzi`, rezervă `{{SHOP_URL}}/produse` |
| S3 card | Adaugă în coș | `{{ORDER_PRODUCT_URL}}` |
| S3 rezervă | Vezi toate mixurile | `{{SHOP_URL}}/produse` |
| S5 | Comandă din nou | ca S1 |

---

## 6. Alt text

| Imagine | Alt text |
|---|---|
| Logo header | Lucas Bites |
| IMG1 (hero) | Teanc de pancakes cu afine, banană și sirop în jur |
| Produse (S3) | `{{ORDER_PRODUCT_NAME}}`; rezervă: „Mix Lucas Bites” |
| Iconiță cântar (S4) | `alt=""` (decorativ, textul e alături) |
| Logo footer | Lucas Bites, eat what you love |
| Valuri, forme decorative | `alt=""` |

---

## 7. Ce am verificat și ce nu

- Toate afirmațiile și cifrele vin din `discovery.md` (secțiunile 1, 3, 4, 8b). Fără citate de recenzii (nu există în discovery).
- Template-ul de reaprovizionare theMarketer („Post Cumpărare”, interval pe produs): verificat în `new-customer-01/copy.md`, secțiunea 8.
- **Neverificat:** blocul cu produsele din comanda declanșatoare / link de recomandă, ascunderea prețului în bloc, sintaxa prenumelui și a dezabonării, subiect condiționat, limita de frecvență per automatizare, excluderea pe „comandă nouă în ultimele 14 zile”.

**Placeholdere generice (nu sunt sintaxă theMarketer):** `{{FIRST_NAME}}`, `{{ORDER_PRODUCT_NAME}}`, `{{ORDER_PRODUCT_IMAGE}}`, `{{ORDER_PRODUCT_URL}}`, `{{UNSUBSCRIBE_URL}}`, `{{SHOP_URL}}`.

---

## 8. Întrebări pentru client (și de verificat în theMarketer)

1. **Blocul dinamic:** ce bloc / variabile oferă theMarketer pentru produsele din comanda care declanșează emailul de reaprovizionare (nume, imagine, link, „recomandă”)? Există link direct de reorder sau pagină „comenzile mele”?
2. **Excludere:** se pot exclude din automatizare cei care au comandat din nou în cele 14 zile?
3. **Prețul în bloc:** se poate ascunde? Dacă nu, acceptați prețul vizibil aici?
4. **14 zile pentru toată gama:** rămâne un interval unic, sau vreți ulterior intervale per produs (de exemplu Pizza vs Pankees)?
5. **Subiectul A** numește Pankees: OK pentru cumpărătorii care au luat doar alte mixuri, sau folosim E pentru ei (dacă se poate condiționa)?
