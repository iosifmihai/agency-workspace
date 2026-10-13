# Checkout Started, Email 2: brief

**Client:** Lucas Bites. Reguli de brand, fonturi, culori și contact: vezi `../../welcome-01/brief.md`.
**Email 1:** `../email-01/`. Email 2 rămâne în aceeași familie vizuală, cu layout propriu.
**ESP:** de confirmat. HTML email-safe (tabele, CSS inline, 600px).

## Ce cere clientul
- Reamintire finalizare comandă
- Recenzii clienți (2-3)
- 3 USP: suport, transport, ingrediente

## Structură propusă
1. Logo
2. Hero: a doua reamintire, alt unghi decât Email 1
3. Bloc dinamic produse din coș: `{{CART_ITEMS}}`
4. CTA pill: „Finalizează comanda” -> `{{CHECKOUT_URL}}`
5. Recenzii (2-3) + „Peste 1.100 de recenzii, cu o medie de 4,9 din 5”
6. 3 USP
7. CTA secundar
8. Footer

## Recenzii
Confirmată (de pe site): „Au ieșit excelent și au fost foarte ușor de preparat. Mi-a plăcut în mod deosebit că nu au fost dulci.” (Kinga Ludescher, Classic Pankees)
Restul: `[DE CONFIRMAT CU CLIENTUL: încă 1-2 recenzii reale, cu nume și produs]`. NU inventăm recenzii.

## USP
- **Suport:** office@lucasbites.ro · +40 731 399 399 (`[DE CONFIRMAT: program / canale suport]`)
- **Transport:** transport gratuit de la al 2-lea produs
- **Ingrediente:** ingrediente pe care le recunoști, fără conservanți; zahăr brun din trestie; făină nealbită doar la pancakes și clătite (nu generaliza)

## Reguli
- Fără discount (nu e cerut), fără urgență falsă, fără promisiuni de sănătate.

## Decizii confirmate de client (12.10.2026)
- ESP: **theMarketer**. Feed-ul cu produsele din coș îl adaugă clientul; în HTML punem placeholder `[FEED PRODUSE THEMARKETER]` (ca în `../email-01/index-esp.html`).
- Timing: Email 2 la **24 de ore** după Checkout Started (Email 1 la 30 de minute).
- Transport gratuit de la al 2-lea produs: confirmat.
- Acord marketing la checkout: da.
- „Repede și simplu” în loc de „Gata în 5 minute” (valabil pentru toată gama).
- Footer: denumire juridică + CUI (placeholder până le primim), URL pagină produse = `{{SHOP_URL}}`.

## Recenzii disponibile
Recenzii reale de pe site-ul actual, deja selectate și verificate în `../../welcome-03/copy.md` (vezi regulile de citare și excluderile de acolo). Kinga Ludescher e folosită în welcome-01. Se pot refolosi, cu aceleași reguli.
