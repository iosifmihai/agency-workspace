# Design notes: Welcome Series, Email 1 (Bun venit + cadou mănuși)

**Fișier:** `email-1.html`, ~25 KB, UTF-8, mult sub limita de 102 KB la care Gmail taie mesajul. Copy-ul final vine din `strategy-and-copy.md` (10.10.2026). Textul vizibil este cel [CLIENT]; propunerile [MODIFICAT] sunt doar în comentarii HTML.

## Layout
- **Template:** DWF, la fel ca newsletterul KometaBio (`2026-10-26-kometabio/newsletter.html`): container de 700 px pe #F4F4F4, Poppins cu fallback Arial/Helvetica (Outlook forțat pe Arial), accent #FF5E08, piersică #FAE1D3, separator 1 px #B3C0CE, footer negru.
- **Ordinea blocurilor:**
  1. preheader ascuns (A);
  2. logo (220 px, fără meniu: atenția rămâne pe cod);
  3. hero 700×400 (placeholder);
  4. titlu „Bun venit în comunitatea Medident Exim!”;
  5. intro (text client);
  6. code-box: piersică, chenar punctat 2 px #FF5E08, cod 28 px bold monospace, linia de valabilitate;
  7. „Cum folosești codul” și rândul opțional despre livrarea gratuită (13 px, gri);
  8. buton principal „Plasează o comandă”;
  9. separator, apoi titlul despre vechime (20 px) și cele două paragrafe;
  10. buton secundar cu contur „Descoperă produsele Medident”;
  11. rândul de contact (telefon și email);
  12. bandă de încredere pe piersică;
  13. semnătura;
  14. footer (social, GDPR verbatim, dezabonare).
- **Butoane:** pastile de 40 px, radius 20 px. În Outlook sunt `v:roundrect` VML (arcsize 50%), în rest `<a>` stilizat. Pe mobil (≤520 px) ocupă toată lățimea.
- **Code box:** codul e text selectabil (`user-select:all`), nu imagine, deci se citește și cu imaginile blocate. Pe mobil scade la 22 px. În Outlook desktop colțurile sunt drepte (radius ignorat), chenarul punctat rămâne.
- **Marcaje în cod:** `<!-- BLOCK: nume -->`, `DE CONFIRMAT`, `TODO-ASSET`, subiectele A/B/C cu preheaderele în comentariul din `<head>`.

## Ce e marcat „DE CONFIRMAT” în HTML
1. **Vechimea** (titlu și paragraful 1): textul vizibil spune „peste 25 de ani”; propunerea „27 de ani” sau „din 1998” e în comentariu.
2. **Pragul de 115 lei** (intro și code-box) vs. comanda minimă de 110 lei. Pragul trebuie setat identic și în voucher.
3. **[COD_UNIC] și [DATA_EXPIRARE]:** placeholdere, nu merge tag-uri theMarketer. Se înlocuiesc după ce aflăm cum generează platforma coduri unice per contact. Fără dată de expirare, se scoate „Valabil până pe…”.
4. **Mănușile:** model, mărime și adăugarea manuală în colet. Nu menționăm model sau valoare până la confirmare.
5. **Destinațiile CTA:** „Plasează o comandă” și hero → homepage; „Descoperă produsele Medident” → /produse/promotii.
6. **Telefonul:** centrala 0268.31.55.44 în locul lui 0732 500 341 în toată seria.
7. **Footer GDPR:** ultimul paragraf vorbește de „relația B2B”; formularea propusă pentru abonați e în comentariu. Textul vizibil rămâne verbatim până la acord.
8. **Hero:** modelul cutiei și sursa fotografiei.
9. Ramificarea pentru abonații care au deja comenzi (setare în automatizare, nu în HTML).

## Asset-uri de înlocuit
| Unde | Acum | Ce trebuie pus |
|---|---|---|
| Hero | placehold.co 1400×800 | Fotografia cutiei de mănuși By Medident pe fundal #FAE1D3, cu fundă sau etichetă #FF5E08, fără text și fără umbre dure. Export 1400×800, urcat în theMarketer. Păstrăm `width="700"`. |
| Logo, iconițe social | URL-uri reale, preluate din template-ul KometaBio | Nu e nevoie de nimic. |

## Contrast (WCAG 2.1)
- **Butonul principal:** alb pe #FF5E08 are 3,06:1, deci nu trece AA la 15 px. E excepția de brand asumată, ca în newsletter. Varianta conformă: fundal #C74400 (4,94:1) prin find/replace pe `fillcolor="#FF5E08"` și `background-color:#FF5E08` din butonul principal.
- **Butonul secundar:** chenar #FF5E08, text #C74400 pe alb (4,94:1, trece AA). Strategia cerea text portocaliu; #FF5E08 pe alb ar fi avut doar 3,06:1. Dacă se vrea exact #FF5E08, se schimbă `color:#C74400` în cele două locuri (VML și `<a>`).
- **Code box:** negru pe piersică (16,78:1).
- **Text secundar:** #555555 pe alb (7,46:1).
- **Footer:** alb pe negru.
- **În cod:** toate tabelele au `role="presentation"`, toate imaginile au alt text în română, bifele decorative au `aria-hidden`.

## Dark mode
- `color-scheme: light dark`.
- **Apple Mail și Outlook macOS:** fundal #141414/#1E1E1E, piersica (code-box, bandă de încredere) devine #3A2A20, textul #F2F2F2 (12,24:1 pe #3A2A20). Butonul secundar primește text #FF5E08 pe #1E1E1E (5,44:1).
- **Outlook.com:** regulile `[data-ogsc]` / `[data-ogsb]`.
- **Logo:** pe celulă cu fundal alb fix, pentru că PNG-ul e portocaliu.
- **Gmail:** inversare parțială; toate fundalurile sunt setate explicit.

## UTM
- **Toate linkurile medidentexim.ro** au UTM complet, exact ca în tabelul din strategie: `utm_source=themarketer&utm_medium=email&utm_campaign=welcome_email1`, plus `utm_content` = `logo`, `hero`, `cta-comanda`, `cta-produse`.
- **Telefon:** `tel:+40268315544`. **Email:** `mailto:office@medidentexim.ro`. **Social:** fără UTM.
- **Atenție:** în newsletterul KometaBio, source/medium/campaign au fost setate pe campanie și scoase din HTML. Dacă theMarketer face la fel pe automatizare, ștergeți din HTML partea `utm_source=…&utm_campaign=welcome_email1&`, ca să nu se dubleze.

## Import în theMarketer
1. Automatizarea Welcome Series, pasul Email 1, editorul **HTML / Cod sursă**. Lipiți tot fișierul, de la `<!DOCTYPE>` la `</html>`. Nume intern: `[DWF] Welcome 1 - Bun venit + cadou mănuși`.
2. Înlocuiți `[COD_UNIC]` și `[DATA_EXPIRARE]` cu merge tag-urile reale ale codului unic (sau ale blocului de cupon theMarketer). Testați că fiecare contact primește un cod diferit.
3. Verificați `{{unsubscribe_link}}` în editor sau folosiți footerul nativ theMarketer. Activați List-Unsubscribe one-click.
4. Urcați hero-ul în galeria theMarketer și înlocuiți `src`-ul marcat `TODO-ASSET`.
5. Setați subiectul (A recomandat) și preheaderul în câmpurile emailului. Preheaderul A e deja în div-ul ascuns; dacă schimbați subiectul pe B, schimbați și preheaderul.
6. Trigger: abonare nouă (după confirmare, dacă există double opt-in), trimitere imediată. Excludeți suprimații, hard bounce și dezabonații; ramificarea pentru clienții existenți după confirmarea punctului 6.
7. Dacă editorul elimină `<head>`/`<style>`, layout-ul rămâne funcțional prin stilurile inline. Se pierd doar ajustările de mobil și de dark mode.
8. Test în Gmail web și app, Outlook desktop și Apple Mail iOS: butoanele VML (inclusiv cel cu contur), chenarul punctat, codul selectabil, linkul `tel:`.
