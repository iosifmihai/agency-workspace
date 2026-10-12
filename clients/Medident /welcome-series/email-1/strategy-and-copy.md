# Welcome Series, Email 1: strategie și copy final
**Automatizare:** Welcome Series (5 emailuri) · **Platformă:** theMarketer · **Client:** Medident Exim
**Nume intern:** [DWF] Welcome 1 - Bun venit + cadou mănuși
**Pregătit:** 10.10.2026

**Surse:** brief.md (copy client verbatim, din „Strategie Automatizări”), discovery.md (secțiunile 6 la 9).

**Legendă:**
- **[CLIENT]**: textul clientului, neschimbat.
- **[MODIFICAT]**: propunere de ajustare a textului clientului. Originalul rămâne versiunea principală până la acordul clientului.
- **[NOU]**: text sau bloc adăugat de agenție.

---

## 1. Rolul emailului în serie

**Obiectiv:** transformăm abonatul nou în client la prima comandă, folosind codul unic pentru cutia de mănuși. Secundar: prezentăm Medident Exim (vechime, branduri, consultanță, cursuri).

**Trigger:** abonare nouă la newsletter. Dacă formularul are dublă confirmare (double opt-in), emailul pleacă după confirmare, nu după completarea formularului.

**Timing:** imediat (în primele minute de la trigger). Emailul 2 vine după intervalul stabilit în „Strategie Automatizări”.

**Segment și excluderi:**
- **Intră:** contacte noi, abonate, cu consimțământ documentat (data, sursa formularului).
- **Exclus din oferta „prima comandă”:** contactele care au deja cel puțin o comandă pe site. Pentru ei oferta nu se aplică și ar genera reclamații. Propunere: o ramificare în automatizare (are comenzi = DA → variantă fără cod sau ies din serie). DE CONFIRMAT (punctul 6).
- **Exclus complet:** adrese suprimate, hard bounce, dezabonați.

**Condiții de ieșire din serie:** dezabonare, hard bounce, reclamație spam. Plasarea primei comenzi oprește mesajele despre cod din emailurile următoare (de aplicat în emailurile 2 la 5).

**KPI (ținte inițiale, recalibrate după 30 de zile de date):**

| KPI | Țintă | Prag de alertă | Notă |
|---|---|---|---|
| Rata de click unic (din livrate) | ≥ 5% | < 2% | Emailurile de bun venit au intenție mare. Media contului la newslettere: 1,67%. |
| CTOR | ≥ 12% | < 6% | Indicator principal de conținut, nu open-ul. |
| Rata de utilizare a codului în 14 zile (comenzi cu cod / livrate) | ≥ 3% | < 1% | KPI-ul de business al emailului. Necesită raportare a codurilor folosite. |
| Rata de deschidere | doar orientativ | < 40% | Umflată de Apple MPP. |
| Dezabonări | ≤ 0,5% | > 1% | |
| Reclamații spam | < 0,1% | > 0,2% | |

**Volum:** nu știm câți abonați noi intră lunar. Fără volum, un test A/B pe subiect nu dă rezultate semnificative în timp util (vezi secțiunea 2).

---

## 2. Subiect și preheader

| # | Subiect | Car. | Preheader | Car. |
|---|---|---|---|---|
| **A (recomandat)** | Îți mulțumim pentru abonare **[CLIENT]** | 27 | Cadoul tău de bun venit: o cutie de mănuși, din partea noastră **[CLIENT]** | 62 |
| B | Bun venit! O cutie de mănuși te așteaptă | 40 | Codul tău unic și o cutie de mănuși gratuită la prima comandă. | 62 |
| C | Bun venit la Medident Exim: cadoul tău e în interior | 52 | Cadoul tău de bun venit: o cutie de mănuși, din partea noastră **[CLIENT]** | 62 |

**De ce A:** este textul clientului, confirmă imediat acțiunea abonatului (emailul e așteptat, deci deschiderea e mare indiferent de subiect), iar preheaderul aduce oferta. Combinația subiect + preheader acoperă și confirmarea, și cadoul.

**B și C, opțional:**
- **B** pune cadoul direct în subiect. Util dacă vrem ca oferta să fie vizibilă și la cei care nu afișează preheaderul.
- **C** numește brandul, util când expeditorul apare ca „Medidentexim.ro”.

**Test A/B:** doar dacă volumul lunar de abonați depășește aproximativ 500. Altfel rulăm A și revizuim după 60 de zile. Măsurăm CTOR și utilizarea codului, nu open.

---

## 3. Copy final, pe blocuri (pentru designer)

**Format:** template DWF, 700 px, Poppins, accent #FF5E08, piersică #FAE1D3, butoane pastilă (radius 20 px) portocalii cu text alb. Lungime: aproximativ 200 de cuvinte în corp.

**Adresare:** „tu”, de la început la sfârșit (vezi punctul 5 din lista de confirmat).

### 0. preheader **[CLIENT]**
*Layout: text ascuns, primul element din HTML.*
Cadoul tău de bun venit: o cutie de mănuși, din partea noastră

### 1. logo **[NOU]**
*Layout: fundal alb, logo centrat, aproximativ 220 px lățime, link spre homepage.*
- Fișier: logo_medident_925x240_v9.png (de pe site).
- Link: https://medidentexim.ro/?utm_source=themarketer&utm_medium=email&utm_campaign=welcome_email1&utm_content=logo
- Alt text: „Medident Exim, Your Dentality Partner”
- Fără meniul portocaliu: într-un email de bun venit vrem atenția pe cod.

### 2. hero **[NOU]** (placeholder, asset-ul lipsește)
*Layout: imagine full-width, afișată 700×400, export 1400×800 (retina).*
- **Concept:** cutia de mănuși nitril By Medident, fotografiată pe fundal piersică (#FAE1D3), cu o fundă sau o etichetă de cadou portocalie (#FF5E08). Lumină curată, fără umbre dure (clientul a semnalat umbre pe vizualuri anterioare). Fără text în imagine: oferta stă în HTML, ca să fie citită și cu imaginile blocate.
- **Atenție:** imaginea trebuie să arate exact produsul oferit. Până la confirmarea modelului (punctul 4), folosim o cutie generică By Medident.
- Link: același cu cta-primary, `utm_content=hero`.
- Alt text: „Cutie de mănuși By Medident, cadou la prima comandă pe medidentexim.ro”

### 3. headline **[CLIENT]**
*Layout: bold, 24 px, centrat, negru.*
Bun venit în comunitatea Medident Exim!

### 4. intro **[CLIENT]**
*Layout: 15 px, centrat sau aliniat stânga, max 3 rânduri pe desktop.*
Mănușile sunt printre produsele pe care le folosești zilnic în cabinet, așa că ne-am gândit să începem cu ceva cu adevărat util. La prima ta comandă de minimum 115 lei, primești cadou o cutie de mănuși. Introdu codul de mai jos la finalizarea comenzii și o adăugăm direct în colet.

> Pragul „115 lei” rămâne așa până la confirmare (punctul 2). Comanda minimă pe site este 110 lei.

### 5. code-box **[NOU]**
*Layout: casetă pe fundal piersică, chenar punctat portocaliu de 2 px, cod mare (28 px, bold, litere spațiate), selectabil ca text, nu imagine.*

CODUL TĂU DE BUN VENIT
**[COD_UNIC]**
Valabil până pe [DATA_EXPIRARE], la prima comandă de minimum 115 lei.

*Rând mic sub casetă (13 px):* Cum folosești codul: adaugi produsele în coș, introduci codul la finalizarea comenzii, iar cutia de mănuși ajunge în același colet cu comanda ta.

*Rând opțional (13 px), fapt verificat pe site [W3]:* Livrare gratuită la comenzile de peste 290 lei.

- `[COD_UNIC]` și `[DATA_EXPIRARE]` sunt placeholdere. Se înlocuiesc cu merge tag-urile reale din theMarketer, după ce verificăm cum generează platforma coduri unice per contact.
- Dacă nu avem dată de expirare, scoatem fraza „Valabil până pe…” și păstrăm doar pragul.

### 6. cta-primary **[CLIENT]**
*Layout: buton pastilă portocaliu, centrat, lățime aproximativ 260 px.*
**Plasează o comandă**
→ https://medidentexim.ro/?utm_source=themarketer&utm_medium=email&utm_campaign=welcome_email1&utm_content=cta-comanda **DE CONFIRMAT**
- Propunere: homepage, pentru că oferta e valabilă pe orice produs. Dacă clientul are o pagină de categorie pentru consumabilele uzuale (sau pagina mănușilor), aceea ar fi o destinație mai bună.

### 7. about-headline **[CLIENT]**
*Layout: separator subțire, apoi titlu bold 20 px, aliniat stânga.*
Împreună de peste 25 de ani, alături de profesioniștii din stomatologie

> **[MODIFICAT] propus:** Împreună de 27 de ani, alături de profesioniștii din stomatologie
> Motiv: regula din discovery („27 de ani”, 10.10.2026). Vezi punctul 1 pentru alternativa „din 1998”.

### 8. about-body **[CLIENT]**
*Layout: 15 px, aliniat stânga, două paragrafe.*
De peste 25 de ani, Medident Exim este partenerul cabinetelor stomatologice și laboratoarelor de tehnică dentară din România. Aducem produse de la branduri de referință, precum KaVo, Ivoclar, GC, Solventum sau Renfert, și te ajutăm să alegi soluția potrivită pentru activitatea ta.

Pentru noi, o comandă nu se încheie la livrare. Îți oferim consultanță înainte de achiziție, suport tehnic după, și cursuri susținute de lectori cu experiență academică și clinică, ca să crești profesional alături de noi.

> **[MODIFICAT] propus pentru paragraful 1:** „De 27 de ani, Medident Exim este partenerul…” (restul neschimbat).
> Brandurile numite apar toate în lista de parteneri de pe site [W1]. Afirmațiile despre consultanță, suport tehnic și lectori sunt susținute de discovery (secțiunile 2 și 4).

### 9. cta-secondary **[CLIENT]**
*Layout: buton pastilă cu contur portocaliu și text portocaliu (secundar vizual față de cta-primary), centrat.*
**Descoperă produsele Medident**
→ https://medidentexim.ro/produse/promotii?utm_source=themarketer&utm_medium=email&utm_campaign=welcome_email1&utm_content=cta-produse **DE CONFIRMAT**
- Propunere: pagina de promoții (peste 1.100 de produse reduse), ca abonatul să ajungă ușor la pragul ofertei. Alternativă: homepage.

### 10. contact-line **[NOU]**
*Layout: rând de 14 px, centrat, sub cta-secondary.*
Ai nevoie de ajutor la prima comandă? Sună-ne la **0268.31.55.44** sau scrie-ne la office@medidentexim.ro.
- Telefon ca link `tel:+40268315544`, email ca `mailto:office@medidentexim.ro`.

### 11. trust-strip **[NOU]**
*Layout: bandă pe fundal piersică, 3 iconițe portocalii, din template-ul standard.*
Precizie garantată · Suport tehnic și service · Livrare rapidă din stoc

### 12. signature **[NOU]**
*Layout: 15 px, aliniat stânga sau centrat, înainte de footer.*
Echipa Medident Exim

### 13. footer **[NOU]**, standard DWF
*Layout: fundal negru, text alb 12 px.*
- Iconițe Facebook, YouTube, Instagram (linkurile din discovery, secțiunea 10).
- Text GDPR din template (vezi punctul 8: formularea actuală vorbește de „relația B2B”, nu de abonare).
- „Trimis cu drag din Brașov.”
- Merge tag-urile theMarketer pentru dezabonare și versiune web. Header List-Unsubscribe (one-click) activ.

### Rezumat linkuri și UTM
Bază: `utm_source=themarketer&utm_medium=email&utm_campaign=welcome_email1`. Verificăm dacă theMarketer adaugă UTM automat, ca să nu se dubleze.

| Bloc | Text | URL | utm_content | Status |
|---|---|---|---|---|
| logo | (imagine) | https://medidentexim.ro/ | logo | OK |
| hero | (imagine) | ca cta-primary | hero | DE CONFIRMAT |
| cta-primary | Plasează o comandă | https://medidentexim.ro/ | cta-comanda | DE CONFIRMAT |
| cta-secondary | Descoperă produsele Medident | https://medidentexim.ro/produse/promotii | cta-produse | DE CONFIRMAT |
| contact-line | 0268.31.55.44 | tel:+40268315544 | – | OK |

---

## 4. DE CONFIRMAT cu clientul

1. **Vechime: „peste 25 de ani” vs. „27 de ani”.** Regula din 10.10 este „27 de ani”. **Recomandare:** „27 de ani” în ambele locuri (titlu și paragraf). Fiind automatizare permanentă, cifra trebuie actualizată în octombrie 2027; alternativ, formularea „din 1998” nu expiră. Clientul alege.
2. **Pragul ofertei: 115 lei vs. comanda minimă de 110 lei.** Este un prag separat, intenționat? **Recomandare:** dacă oferta se aplică la orice primă comandă, scoatem pragul („La prima ta comandă, primești cadou…”), pentru că diferența de 5 lei creează confuzie. Pragul trebuie setat identic și în voucher (filtrul „valoare minimă”).
3. **Codul unic.** Copy-ul spune „codul de mai jos”, dar nu exista bloc pentru cod; am adăugat code-box [NOU]. De confirmat: cum se generează codul unic per contact în theMarketer și care sunt merge tag-urile reale pentru [COD_UNIC] și [DATA_EXPIRARE]; care este valabilitatea (Emailul 2 menționează o dată de expirare); dacă codul e de utilizare unică și exclude vreo categorie (echipamente, implanturi).
4. **Mănușile.** Model (nitril By Medident, 100 buc.?), mărime, cine alege mărimea și cum (câmp la comandă, telefon, mărime standard). „O adăugăm direct în colet” presupune adăugare manuală de către depozit: confirmăm că așa funcționează și că nu trebuie pusă cutia în coș. Fără confirmare nu menționăm model, mărime sau valoare.
5. **Adresare: „tu” vs. „dumneavoastră”.** Regula din discovery nu acoperă explicit emailul de bun venit. **Recomandare:** „tu”, pentru că emailul conține o ofertă (tipul „promoție”), iar seria și newsletterele care urmează folosesc „tu”. Copy-ul clientului este deja consecvent pe „tu”.
6. **Abonați care sunt deja clienți.** Oferta e pentru prima comandă. Excludem din Email 1 contactele cu comenzi anterioare sau le dăm o variantă fără cod?
7. **Telefonul.** Folosim centrala 0268.31.55.44 (regula din 10.10). Documentul clientului folosește 0732 500 341 în alte emailuri ale seriei. Confirmăm că înlocuim peste tot cu centrala.
8. **Consimțământ și footer GDPR.** Textul actual („în urma interacțiunii profesionale… relației de tip B2B”) nu descrie un abonat nou prin formular. Propunem o variantă pentru automatizare: „Primești acest email pentru că te-ai abonat la newsletterul Medident Exim pe medidentexim.ro.” Confirmăm și dacă formularul are double opt-in și ce se salvează (dată, sursă).
9. **Destinațiile CTA-urilor.** „Plasează o comandă” → homepage și „Descoperă produsele Medident” → /produse/promotii sunt propuneri. Există o pagină mai potrivită (consumabile uzuale, pagina mănușilor)?
10. **Vizualul hero.** Poate clientul trimite o fotografie a cutiei de mănuși oferite (fără umbre), sau o producem noi pe baza produsului confirmat?
11. **Volumul de abonați noi pe lună.** Necesar pentru decizia de test A/B și pentru calibrarea KPI.
