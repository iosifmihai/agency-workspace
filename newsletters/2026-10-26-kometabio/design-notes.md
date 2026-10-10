# Design notes: newsletter KometaBio, 26.10.2026

**Fișier:** `newsletter.html`, ~57 KB, UTF-8, sub limita de 102 KB la care Gmail taie mesajul. Copy-ul final vine din `strategy-and-copy.md`.

## Layout
- **Template:** DWF.
  - Container de 700 px pe fundal #F4F4F4.
  - Poppins din Google Fonts, cu fallback Arial/Helvetica. Outlook este forțat pe Arial prin `<!--[if mso]>`.
  - Accent #FF5E08 și piersică #FAE1D3.
  - Separatoare de 1 px #B3C0CE.
  - Footer negru.
- **Ordinea blocurilor:**
  1. preheader ascuns (A);
  2. link „versiune web”;
  3. logo;
  4. meniu portocaliu;
  5. hero, cu link către Starter Kit;
  6. titlu și intro (text client);
  7. 4 beneficii pe piersică;
  8. „Cum funcționează, în 3 pași” pe piersică, cu nota „o cameră per pacient”;
  9. articol tehnic: imagine plus text, buton „CITEȘTE ARTICOLUL” și link text opțional spre video;
  10. grilă de produse 2×2;
  11. „DESCOPERĂ GAMA KOMETABIO”;
  12. bloc de consultanță cu „SOLICITĂ O OFERTĂ PERSONALIZATĂ” și telefonul;
  13. bandă de încredere;
  14. disclaimer și semnătură;
  15. footer.
- **Coloane:** sunt hibride, adică `div` inline-block cu tabele-fantomă MSO. Pe mobil (≤520 px) devin o singură coloană chiar și fără media queries, de exemplu în Gmail cu conturi non-Google. Media query-ul ajustează doar padding-ul și lățimea imaginilor.
- **Butoane:** sunt pastile de 40 px înălțime, cu radius 20 px.
  - În Outlook se randează ca `v:roundrect` VML, cu arcsize 50%. În celelalte clienți se folosește un `<a>` stilizat.
  - Pe mobil, butoanele ocupă toată lățimea.
- **Marcaje în cod:**
  - fiecare text are `<!-- BLOCK: nume -->`;
  - afirmațiile neconfirmate au `DE CONFIRMAT`;
  - imaginile de înlocuit au `TODO-ASSET`;
  - subiectele A/B/C și preheaderele lor sunt într-un comentariu în `<head>`.

## Ce e marcat „DE CONFIRMAT” în HTML
1. **Pasul 3, „5 minute în Dentin Cleanser”:** PDF-ul spune 5 minute și marchează pasul ca opțional, iar blogul spune ~10 minute. Dacă nu se confirmă, ajustăm textul și trecem pe subiectul B.
2. **Fraza de sub cardul Starter Kit, „cu 79,82 lei mai mult decât aparatul…”:** depinde de ce include exact KB-07.
3. **Descrierea pentru Dentin Graft Accelerator Kit (KB-06):** cardul afișează doar codul. Dacă nu se confirmă, trecem pe KB-02, care e pregătit într-un comentariu sub grilă, cu date și URL.
4. **Rândul despre finanțare:** e comentat în blocul de consultanță. Îl activăm doar dacă clientul confirmă că finanțarea se aplică la KometaBio.
5. **Prețuri, reduceri și stoc:** le reverificăm pe 25.10. Vizualul hero îl alege clientul.

## Asset-uri de înlocuit
| Unde | Acum | Ce trebuie pus |
|---|---|---|
| Hero | placehold.co 1400×630 | KometaBio_1410x630.png, sau 1200×628 ca rezervă, urcat în theMarketer. Păstrăm `width="700"`. |
| Articol | og:image de pe static.wixstatic.com (kometabio.com) | Aceeași imagine, descărcată și urcată în theMarketer, pentru ca linkul să nu depindă de Wix. |
| 4 produse | placehold.co 600×600 cu codul produsului | Pozele de pe paginile produselor de pe medidentexim.ro sau din blocul de produse theMarketer. Fond alb, afișate la 220 px. |
| Logo, iconițe social | URL-uri reale (verificate, HTTP 200) | Nu e nevoie de nimic. |

## Contrast (WCAG 2.1)
- **Alb pe #FF5E08 are 3,06:1.** Asta **nu trece AA pentru text normal** (cerința e 4,5:1). Trece doar pentru text mare, adică ≥18,66 px bold.
  - **Butoanele** (15 px, bold, alb) sunt păstrate așa pentru consecvență cu template-ul existent, deci sunt o excepție de brand asumată.
  - **Varianta conformă:** fundal #C74400 pe butoane (4,94:1, find/replace pe `fillcolor="#FF5E08"` și pe `background-color:#FF5E08` din `.btn-a`), sau text negru pe portocaliu (6,86:1).
- **Meniu:** am pus text negru pe portocaliu (6,86:1), pentru că 13 px alb nu trece. Dacă vrem înapoi albul din template, schimbăm `color:#000000` în cele 4 linkuri din meniu.
- **Etichete:**
  - „ARTICOL TEHNIC” are text negru pe portocaliu (6,86:1).
  - Cifrele pașilor sunt albe la 20 px bold, deci text mare (3,06:1), ceea ce e OK.
- **Corpul textului:**
  - negru pe alb sau pe piersică (16,8:1);
  - griul secundar #555555 sau #6B6B6B pe alb (≥5,3:1);
  - alb pe negru în footer.
- **Accesibilitate în cod:**
  - toate tabelele au `role="presentation"`;
  - imaginile au alt text descriptiv în română;
  - iconițele ✓ decorative au `aria-hidden`.

## Dark mode
- **Meta tag-uri:** `color-scheme: light dark`.
- **Apple Mail și Outlook macOS:** prin `prefers-color-scheme` primesc fundal #141414/#1E1E1E, blocurile piersică devin #3A2A20, iar textul devine #F2F2F2. Accentul portocaliu rămâne.
- **Outlook.com:** folosește regulile `[data-ogsc]`.
- **Logo:** stă pe o celulă cu fundal alb, pentru că PNG-ul e portocaliu.
- **Gmail:** inversează parțial culorile. Toate fundalurile sunt setate explicit, așa că rezultatul rămâne lizibil.

## UTM
- **Toate linkurile medidentexim.ro** au `utm_source=themarketer&utm_medium=email&utm_campaign=kometabio_2026-10-26`, plus `utm_content` pe fiecare: hero, produs-starterkit / produs-aparat / produs-consumabile / produs-accelerator, cta-gama, cta-oferta, meniu-*, logo.
- **Linkurile externe** (kometabio.com, YouTube) nu au UTM.
- **Atenție la `utm_campaign`:** în strategie apare `kometabio_2026-10-26`, iar în HTML am păstrat `kometabio_26oct2026`, ca în specificația inițială. Alegeți unul. Valoarea e într-o singură constantă, deci se poate înlocui ușor cu find/replace.
- **Verificați** dacă theMarketer adaugă automat UTM, ca să nu apară dublat.
- **Niciun link nu duce pe /kometabio** (pagina are produse din afara gamei). Dacă clientul curăță pagina, schimbăm CTA-ul gamă în `/kometabio?...&utm_content=cta-gama`.

## Import în theMarketer
1. Campanie nouă, apoi editorul **HTML / Cod sursă**. Lipiți tot fișierul, de la `<!DOCTYPE>` la `</html>`.
2. Înlocuiți `{{unsubscribe_link}}` și `{{web_version_url}}` cu merge tag-urile exacte din editor. Alternativ, ștergeți footerul nostru de dezabonare și folosiți blocul de footer nativ theMarketer. Textul GDPR trebuie să rămână verbatim.
3. Urcați hero-ul, imaginea articolului și cele 4 poze de produs în galeria theMarketer, apoi înlocuiți `src`-urile marcate `TODO-ASSET`.
4. Setați subiectul (A recomandat) și preheaderul în câmpurile campaniei. Preheaderul A e deja în div-ul ascuns; dacă schimbați subiectul, schimbați-l și pe el.
5. Dacă editorul elimină `<head>`/`<style>`, layout-ul rămâne funcțional: stilurile inline și coloanele hibride se așază singure pe o coloană. Se pierd doar ajustările de mobil și de dark mode.
6. Trimiteți un test în Gmail web și app, Outlook desktop și Apple Mail iOS. Verificați butoanele VML, grila 2×2 → 1 coloană și linkul `tel:`.

## Fișier sursă
Generatorul (Python, opțional) este în scratchpad-ul sesiunii. HTML-ul e sursa de adevăr; se editează direct.

## Draft în theMarketer (10.10.2026)
- **ID:** 6aca094a0aefa5084b032f74
- **Link:** https://app.themarketer.com/campaign/email/6aca094a0aefa5084b032f74
- **Stare:** draft, deci nimic nu se trimite până nu e programat manual din aplicație.
- **Ora prestabilită:** 26.10, 07:30 UTC.
- **Subiect și preheader:** varianta A.
- **Segmente:** Utilizatori Versah (558) + Utilizatori MDI și implanturi (226).
- **Exclus:** segmentul „[DWF] Voucher 5% - cumparatori 2026 AOV peste 500 lei”.
- **UTM:** sunt setate pe campanie (themarketer / email / kometabio_2026-10-26). În HTML a rămas doar `utm_content`.
- **Link versiune web:** l-am scos din HTML, pentru că theMarketer nu are merge tag pentru el. Se adaugă cu componenta nativă de footer, dacă e nevoie.
