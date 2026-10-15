# Lucas Bites: Sunset, strategie, structură și copy final

Surse: `brief.md`, `discovery.md`, `request-review/copy.md` (format, footer). Legendă: [din site] = text aprobat, [nou] = de aprobat de client, [neverificat] = funcție theMarketer negăsită în documentație.

**Ce fel de email e:** ultimul email către un abonat inactiv. Îi cerem o decizie: rămâne sau pleacă. Ambele răspunsuri sunt bune pentru noi; tăcerea înseamnă suprimare.

**Ton:** sincer și ușor, ca un prieten care întreabă „mai ții la grupul ăsta?”. Fără vinovăție, fără dramă.

---

## 1. Segment, trigger, ce urmează

**De ce nu pe deschideri:** Apple MPP deschide automat emailurile, deci „fără deschideri” ratează o mare parte din inactivi reali. Folosim click, vizită pe site și comandă.

**Intră în segment (toate condițiile):**
- Abonat la email (consimțământ de marketing activ).
- Fără **click** pe niciun email în ultimele **90 de zile**.
- Fără **vizită pe site** (tracking theMarketer) în ultimele **90 de zile** [neverificat: condiție de segment pe vizite].
- Fără **comandă** în ultimele **90 de zile** (decizie client: inactiv = 90 de zile fără click, vizită sau comandă).
- Abonat de cel puțin **60 de zile** (nu atingem pe cei încă în welcome / new-customer).

**Exclus:** în orice altă automatizare activă (welcome, new-customer, replenishment, request-review, abandon); clienți Professional / HoReCa; hard bounce, plângere spam, dezabonați.

**Deschiderile:** doar ca semnal secundar. Cine are deschideri dar zero click-uri tot intră; dacă clientul vrea să-i păstreze pe „deschid dar nu dau click”, îi scoatem cu o condiție suplimentară (întrebarea 4).

**Trigger și timing:**
- Automatizare pe intrarea în segment, verificare zilnică. La prima lansare: trimitere în **loturi de 20%** din segment, la 2-3 zile distanță (lista inactivă are risc mai mare de bounce și plângeri).
- Fereastră: **marți sau joi, 10:00-12:00** ora României.
- Maximum o dată la 180 de zile per contact.

**Mecanismul „Da, rămân”:**
- Varianta A (recomandată, cea mai simplă): CTA-ul e un link urmărit (click tracking theMarketer) spre `{{STAY_SUBSCRIBED_URL}}` = o pagină scurtă de mulțumire pe site (sau homepage + UTM). **Click-ul în sine** scoate contactul din segmentul de inactivi (condiția „click în ultimele 90 de zile” devine falsă). Fără altă configurare.
- Varianta B: același click aplică un tag `sunset-ramas` [neverificat: acțiune „tag la click pe link” în automatizarea theMarketer]. Util pentru raportare.
- **De verificat în theMarketer:** (1) dacă click-urile din emailuri sunt condiție de segment, (2) dacă click-urile boților de securitate (scanere de linkuri corporate) sunt filtrate. Dacă nu, un click al unui bot poate „salva” un contact inactiv; acceptabil, efect mic.

**Ce urmează după trimitere:**
- **Ziua 0:** trimitere.
- **Ziua 1-14:** cine dă click pe orice link (nu doar „Da, rămân”) sau comandă = rămâne activ, iese din segment.
- **Ziua 14:** cine n-a dat click și n-a vizitat site-ul = **suprimat** de la emailurile de marketing (nu șters; dezabonat sau mutat într-o listă „sunset-suprimat”, în funcție de ce permite theMarketer [neverificat]). Comenzile și emailurile tranzacționale continuă normal.
- **Fără reminder.** Un singur email, cum a cerut clientul.
- **Retenție:** contactele suprimate fără activitate 24 de luni se anonimizează sau se șterg (politica de retenție a clientului, întrebarea 5).

**Condiții de ieșire:** click pe orice link, comandă, vizită pe site, dezabonare, hard bounce, plângere spam.

**KPI:**
| Metrică | Țintă | Alertă |
|---|---|---|
| Rată de reactivare (click unic / livrate) | 3%+ | sub 1% |
| Click pe „Da, rămân” / livrate | 2%+ | sub 0,5% |
| Comenzi atribuite (14 zile) | raportat, fără țintă | |
| Plângeri spam | sub 0,10% | peste 0,20% (oprește loturile) |
| Hard bounce | sub 1% | peste 2% (oprește, verifică lista) |
| Dezabonări | de așteptat mai mari; nu e problemă | |
[nou, de calibrat după primul lot]

**UTM:** `utm_source=email&utm_medium=lifecycle&utm_campaign=sunset&utm_content=<id>`. Valori: `s1-raman`, `s1-dezabonare`, `s2-produs`, `s2-rezerva`, `s3-cupon`.

---

## 2. Subiecte și preheadere

| # | Subiect | Caractere | Preheader |
|---|---|---|---|
| A **[recomandat]** | Mai rămânem prieteni? [nou] | 21 | Un click și rămâi pe listă. Dacă nu, nicio supărare. [nou] |
| B | Vrei să mai primești vești de la noi? [nou] | 36 | Spune-ne cu un click. Altfel, ne oprim aici. [nou] |
| C | {{FIRST_NAME}}, rămâi sau pleci? [nou] | 21 fără nume (rezervă: „Rămâi sau pleci?”) | Alegerea e a ta, noi doar întrebăm. [nou] |
| D | Facem curățenie în inbox (al tău) [nou] | 33 | Vrei să mai primești rețete și mixuri noi? [nou] |
| E | Ultimul email, dacă nu ne spui altfel [nou] | 37 | Un click pe „Da, rămân” și ne vedem în continuare. [nou] |

De ce A: scurt, cald, pune întrebarea fără presiune. E e cel mai clar, dar mai rece; bun ca variantă B în test.
**Test A/B:** A contra E, câștigător pe click unic / livrate, minimum ~500 livrări pe variantă (doar dacă segmentul permite; altfel A).

---

## 3. Structura, de sus în jos

Lățime 600px, o coloană pe mobil. Titluri Akrobat, majuscule. Text Arial 16px. Butoane pastilă bulletproof.

**S0-header** · **S1-rămâi (portocaliu)** · (val) · **S2-bestsellers (alb, bloc dinamic)** · (val) · **S3-cupon [OPȚIONAL / TEST] (turcoaz)** · **S4-footer**

---

### S0-header
Identic cu familia (logo centrat, 180px).

---

### S1-rămâi (întrebarea)

- **Scop:** decizia în 3 secunde, vizibilă fără scroll pe mobil.
- **Pattern:** fundal portocaliu, text negru, CTA pastilă neagră cu text portocaliu. Fără imagine mare.
- **Copy:**
  - Supratitlu mic: **o întrebare scurtă** [nou]
  - Titlu (H1): **MAI RĂMÂI CU NOI?** [nou]
  - Text: Nu ne-am mai auzit de ceva vreme, așa că întrebăm direct: vrei să primești în continuare rețete, mixuri noi și idei pentru poftele de weekend? Dacă da, un click e destul. Dacă nu, te scoatem de pe listă și rămânem prieteni. [nou]
  - CTA principal: **Da, rămân** → `{{STAY_SUBSCRIBED_URL}}` + UTM `s1-raman` [nou]
  - Opțiune secundară (link text, 14px, sub buton): **Nu acum, mă dezabonez** → `{{UNSUBSCRIBE_URL}}` + UTM `s1-dezabonare` [nou]
  - Text mic (14px): Dacă nu alegi nimic, după {{SUNSET_DAYS}} zile nu-ți mai trimitem emailuri de marketing. Comenzile tale nu sunt afectate. [nou]
- **Frecvență redusă [neverificat]:** theMarketer pare să nu aibă un centru de preferințe cu frecvență în documentația găsită. Dacă există (întrebarea 2), linkul secundar devine: **Vreau mai puține emailuri** → `{{PREFERENCES_URL}}`, iar dezabonarea rămâne în footer.
- **De ce dezabonarea e vizibilă aici:** cine vrea să plece pleacă prin link, nu prin butonul de spam. Plângerile sunt riscul principal pe o listă inactivă.

**Titluri alternative S1:**
1. MAI RĂMÂI CU NOI? (recomandat; întrebare, nu verb)
2. SPUNE-NE DACĂ RĂMÂI
3. ALEGE: RĂMÂI SAU PLECI
4. RĂMÂI PE LISTA POFTELOR
5. HAI SĂ NE AUZIM ÎN CONTINUARE

---

### S2-bestsellers (BLOC DINAMIC, PLACEHOLDER)

> **[PLACEHOLDER: BLOC DINAMIC THEMARKETER, produse „cele mai vândute” / „populare”, maximum 3, fără preț.]**
> Sintaxa și tipul exact al blocului nu se ghicesc: se iau din editor (întrebarea 3). Câmpurile sunt placeholdere generice.

- **Scop:** amintește ce e bun la Lucas Bites, pentru cei care decid din poftă, nu din principiu.
- **Pattern:** fundal alb, 3 carduri pe rând (o coloană pe mobil), imagine, nume, pastilă turcoaz cu text negru.
- **Copy antet:**
  - Supratitlu mic: **dacă tot ești aici** [nou]
  - Titlu (H2): **ALEGE-ȚI POFTA DE AZI** [din site]
  - Text (opțional, o linie): Ai poftă? Gata în 5 minute. [din site]
- **Card (maximum 3):** `{{BEST_PRODUCT_IMAGE}}`, `{{BEST_PRODUCT_NAME}}`, CTA **Vezi mixul** → `{{BEST_PRODUCT_URL}}` + UTM `s2-produs`. **Fără preț.**
- **Rezervă (blocul nu e disponibil):** discovery nu numește bestsellers, deci nu inventăm un top. 3 carduri statice pe categorii din discovery: **Pankees** (clătite americane), **Brownie / Lava Cake**, **Pizza Mix**, fiecare cu **Vezi mixurile** → `{{SHOP_URL}}/produse` + UTM `s2-rezerva`. Clientul confirmă cele 3 produse reale cele mai vândute (întrebarea 3).
- **Sub carduri (14px):** eat what you love [din site]

**Titluri alternative S2:**
1. ALEGE-ȚI POFTA DE AZI (recomandat) [din site]
2. ÎNCEARCĂ PREFERATELE
3. GUSTĂ CE SE CERE ACUM
4. REVINO LA CLASICE
5. PUNE-ȚI CEVA BUN ÎN COȘ

---

### S3-cupon [OPȚIONAL / TEST]

> **Neaprobat de client.** Secțiunea se scoate integral fără să afecteze restul emailului. Se activează doar ca test A/B: jumătate din lot cu S3, jumătate fără; câștigător pe **comenzi / livrate** în 14 zile, nu pe click.

- **Pattern:** fundal turcoaz, text negru, codul într-un chenar negru cu text portocaliu.
- **Copy:**
  - Supratitlu mic: **un mic motiv în plus** [nou]
  - Titlu (H2): **IA-ȚI {{COUPON_VALUE}} REDUCERE** [nou]
  - Text: Dacă rămâi, rămâi cu ceva bun pe masă. Folosește codul la următoarea comandă, până la {{COUPON_EXPIRY}}. [nou]
  - Cod: **{{COUPON_CODE}}**
  - CTA: **Folosește codul** → `{{SHOP_URL}}` + UTM `s3-cupon` [nou]
  - Text mic (14px): Cod valabil o singură dată, pe lucasbites.ro. {{COUPON_TERMS}} [nou]
- **Note:** cod unic per contact recomandat (modulul de cupoane theMarketer [neverificat: generare automată per contact]); valoarea, expirarea și termenii vin de la client. Click pe CTA = reactivare (iese din segment), ca orice click.

**Titluri alternative S3:**
1. IA-ȚI {{COUPON_VALUE}} REDUCERE (recomandat)
2. FOLOSEȘTE CODUL ÎN WEEKEND
3. RĂSFAȚĂ-ȚI POFTA CU {{COUPON_VALUE}} MAI PUȚIN
4. PRIMEȘTE UN MOTIV ÎN PLUS
5. ÎNCEARCĂ DIN NOU, CU REDUCERE

---

## 4. Footer (S4-footer)

Identic cu familia (`request-review/copy.md`, secțiunea 4): adresă, contact, link dezabonare `{{UNSUBSCRIBE_URL}}` [neverificat: sintaxa], iconițe social, © 2026. `List-Unsubscribe` + `List-Unsubscribe-Post` (RFC 8058) active.

---

## 5. Etichete CTA (sumar)

| Loc | Etichetă | Destinație |
|---|---|---|
| S1 principal | Da, rămân | `{{STAY_SUBSCRIBED_URL}}` |
| S1 secundar | Nu acum, mă dezabonez (sau: Vreau mai puține emailuri) | `{{UNSUBSCRIBE_URL}}` / `{{PREFERENCES_URL}}` |
| S2 card | Vezi mixul | `{{BEST_PRODUCT_URL}}` |
| S2 rezervă | Vezi mixurile | `{{SHOP_URL}}/produse` |
| S3 [OPȚIONAL] | Folosește codul | `{{SHOP_URL}}` |

**Alternative „Da, rămân”:** Rămân pe listă · Da, vreau în continuare · Rămân cu voi.

---

## 6. Alt text

| Imagine | Alt text |
|---|---|
| Logo header | Lucas Bites |
| Produse (S2) | `{{BEST_PRODUCT_NAME}}` |
| Rezervă S2 | Pankees / Brownie și Lava Cake / Pizza Mix |
| Valuri, forme decorative | `alt=""` |

---

## 7. Placeholdere (generice, nu sintaxă theMarketer)

`{{FIRST_NAME}}`, `{{STAY_SUBSCRIBED_URL}}`, `{{UNSUBSCRIBE_URL}}`, `{{PREFERENCES_URL}}`, `{{SUNSET_DAYS}}` (recomandat 14), `{{BEST_PRODUCT_NAME}}`, `{{BEST_PRODUCT_IMAGE}}`, `{{BEST_PRODUCT_URL}}`, `{{COUPON_CODE}}`, `{{COUPON_VALUE}}`, `{{COUPON_EXPIRY}}`, `{{COUPON_TERMS}}`, `{{SHOP_URL}}`.

---

## 8. Întrebări pentru client (și de verificat în theMarketer)

1. **Praguri:** stabilit de client, 90 de zile fără click, vizită sau comandă. Rămâne de aflat cât de mare e segmentul azi.
2. **Frecvență redusă:** theMarketer are centru de preferințe cu frecvență? Dacă nu, rămâne doar dezabonarea.
3. **Bestsellers:** ce bloc dinamic oferă theMarketer (populare / cele mai vândute), poate ascunde prețul? Care sunt cele 3 produse cele mai vândute, pentru rezervă?
4. **Deschideri:** îi păstrăm pe cei care deschid dar nu dau click, sau intră și ei în sunset (recomandarea noastră, din cauza MPP)?
5. **După 14 zile:** suprimare (listă separată) sau dezabonare? Politica de retenție pentru contactele suprimate (recomandare: anonimizare după 24 de luni)?
6. **Cupon:** se testează? Valoare, expirare, cod unic sau general, termeni.
7. **Mecanism:** click-ul pe link e condiție de segment în theMarketer? Se poate aplica un tag la click? Click-urile boților sunt filtrate?
