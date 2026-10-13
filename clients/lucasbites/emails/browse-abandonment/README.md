# Browse Abandonment (produs vizualizat, fără adăugare în coș)

**Client:** Lucas Bites. Sursa de adevăr: `clients/lucasbites/discovery.md`.
**Trigger:** utilizatorul a vizualizat un produs și nu l-a adăugat în coș / nu a cumpărat.
**ESP:** theMarketer (ca la checkout-started).
**Familie vizuală:** aceeași cu welcome și checkout-started (culori, fonturi, valuri, CTA pill). Layout propriu.

| Email | Conținut |
|---|---|
| `email-01/` | Reamintire produs vizualizat (placeholder, blocul de produs îl adaugă clientul manual în theMarketer) + idei de rețete cu produsele Lucas Bites (2-3 poze / video) + 3 USP |

## Echipa
- Email Marketing Strategist: strategie, timing, segment, structură, KPI
- Copywriter: subiecte, preheadere, texte pe secțiuni
- UI Designer: direcția de design, layout, `build.py`, prompturi Higgsfield

## Status
- [x] Inspirație în `email-01/refs/`
- [x] Strategie și structură (`email-01/strategy.md`)
- [x] Copy (`email-01/copy.md`), de aprobat
- [x] Design direction + prompturi Higgsfield
- [x] Imagini Higgsfield generate 13.10.2026 (GPT Image 2.5 high 2K; video Seedance 2.5, 4 s, 720p -> GIF 48 cadre, 290 KB)
- [x] Build + preview + versiuni Figma (cu placeholdere de imagine)

## De confirmat cu clientul
- [ ] Timing Email 1 după Product Viewed
- [ ] Evenimentul de vizualizare produs e trimis în theMarketer?
- [ ] Prioritate față de checkout-started (cine e în ambele flow-uri)

## Linkuri
Toate linkurile (`{{PRODUCT_URL}}`, rețete, `{{SHOP_URL}}`, dezabonare) le pune Andreea în theMarketer. Agenții lasă doar placeholdere. `{{PRODUCT_URL}}` pentru „Vezi produsul”: aprobat (13.10.2026).
