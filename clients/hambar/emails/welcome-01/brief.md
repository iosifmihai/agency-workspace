# Welcome series, Email 1: brief comun

**Client:** Hambar (hambar.ro). Sursa de adevăr: `clients/hambar/discovery.md` (citește-l integral, mai ales 1-7, 9, 10, 11). Scop proiect: doar email marketing.
**ESP:** theMarketer. HTML email-safe (tabele, CSS inline, 600px, bulletproof buttons, Outlook VML). Placeholders în stil `{{NUME}}`, ca la Lucas Bites.

## Flow (de la client)
WELCOME SERIES. Trigger: abonare la newsletter (pop-up). Re-entry: nu. Obiectiv: cont creat, apoi prima comandă. Ieșire: prima comandă (trece în Post-purchase) / dezabonare / final secvență (trece în newsletter). Wait: 1 minut.

## Email 1: ce cere clientul
- Mulțumire pentru abonare + bun venit.
- Câteva propoziții despre brand: mâncare românească de la producători mici.
- Beneficiul creării contului + oferta de bun venit.
- Prezentarea categoriilor (vezi lista de mai jos).
- CTA principal: **creează cont**.

## Oferta de bun venit (confirmată, de pe site: `refs/site-hero-bunvenit.png`)
- "Bun venit în Hambar" / "Ai 50 de lei discount la prima comandă cu codul BUNVENIT" / CTA pe site "Descoperă produsele" / "Ofertă valabilă la prima comandă, de min. 250 de lei".
- Cod: **BUNVENIT**. 50 lei, prima comandă, minim 250 lei. Nu inventa termen de valabilitate.
- Atenție: comanda minimă este 50 Lei per producător, iar livrarea se plătește per producător [din site]. Nu promite livrare gratuită.

## Beneficiile contului (doar ce scrie pe site)
Contul e obligatoriu pentru comandă [FAQ]. Avantaje [FAQ]: îți vezi comenzile vechi, urmărești coletele, îți salvezi adresele. Plus: "Comandă din nou" pe homepage. Codul BUNVENIT se folosește la prima comandă, deci contul e pasul spre ofertă.

## Categorii (nume exacte de pe site, cu URL)
- Zacuscă & Murături: https://hambar.ro/categorie/zacusca-si-muraturi
- Brânzeturi & Lactate: https://hambar.ro/categorie/branzeturi-si-lactate
- Carne, Mezeluri & Pește: https://hambar.ro/categorie/carne-si-mezeluri
- Miere & Dulcețuri: https://hambar.ro/categorie/miere-si-dulceturi
- Pâine și Patiserie: https://hambar.ro/categorie/paine-si-patiserie
- Coșuri și Cadouri: https://hambar.ro/categorie/cosuri-si-cadouri
- (disponibile și: Vinuri & Băuturi, Băcănie, Fructe & Legume, Îngrijire Personală; link "Toate categoriile": https://hambar.ro)
Clientul a cerut primele 6. Recomandare: grilă de 6 + link către toate.

## Linkuri
- Creare cont: `{{SIGNUP_URL}}` (URL-ul exact al paginii de înregistrare nu e vizibil în HTML-ul site-ului; /cont dă 404) [de confirmat].
- Site: https://hambar.ro · Cum selectăm producătorii: https://hambar.ro/cum-selectam-producatorii · Cum livrăm: https://hambar.ro/cum-livram
- Aplicație: App Store https://apps.apple.com/ro/app/hambar/id6794062859 · Google Play https://play.google.com/store/apps/details?id=ro.hambar.client
- Social: https://www.facebook.com/hambar.romania · https://www.instagram.com/hambar_ro/ · https://www.tiktok.com/@hambar.ro · https://www.youtube.com/@Hambar_ro
- Footer: contact@hambar.ro · Hambar Marketplace SRL · CUI 54747901 · © 2026 Hambar · `{{UNSUBSCRIBE_URL}}`.

## Reguli de brand (discovery, obligatorii)
- Ton: Direct, Cald, Onest. Nu corporatist, nu glumeț. Adresare cu "tu". Fără emoji, fără em-dash.
- Plată: doar card (nu menționa ramburs). Retur: doar "14 zile". Criteriile de verificare: lista de pe "Cum selectăm producătorii".
- Nu inventa produse, prețuri, cifre, certificări, producători. Se pot folosi doar poveștile din discovery 11.6.
- Paletă (discovery 5): ink #241e1e, fundal #f7f6f5, pre-footer #efedea, footer #413535 cu text #efedea, accent #c93f13 (CTA, text alb pe el 5.0:1). Culorile care nu trec contrastul nu se folosesc pentru text.
- Fonturi: titluri Louize Display (fallback Georgia, serif); text GT America (fallback Helvetica, Arial). Fișiere: `clients/hambar/fonts/`. Licențe deținute de Hambar.
- Logo: `clients/hambar/logos/` (SVG; în email se folosește PNG exportat). Variante -white și -black.

## Direcție vizuală
Referința de pe site (`refs/site-hero-bunvenit.png`): interior rustic cald, lumină de după-amiază prin fereastră, umbre de fereastră pe perete, ulcior de lut, tonuri maro-miere, titluri serif mari albe, CTA pastilă #c93f13 (pe site e mai rotunjit).

## Imagini
Generate cu Higgsfield, în stilul referinței. Mâncare românească reală (zacuscă, murături, brânzeturi, mezeluri, miere, pâine, coș cadou), fără etichete, branduri sau ambalaje inventate, fără text.
