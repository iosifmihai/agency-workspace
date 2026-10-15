# Sunset: brief

**Client:** Lucas Bites. Sursa de adevăr: `clients/lucasbites/discovery.md`.
**Emailuri înrudite:** welcome, new-customer, replenishment, request-review. Același set vizual (logo, valuri, fonturi, footer).
**ESP:** theMarketer. HTML email-safe (tabele, CSS inline, 600px). Titluri Akrobat, text Arial.

## Ce cere clientul
- **Un singur email** către abonații inactivi, trimis înainte de suprimare / dezabonare.
- **Structură cerută:**
  1. Întrebarea „Vrei să mai primești emailuri?” cu CTA principal „Da, rămân” și o opțiune secundară, discretă, de dezabonare (sau frecvență redusă, dacă theMarketer permite [neverificat]).
  2. Bestsellers: bloc dinamic theMarketer (placeholder), fără prețuri. Discovery nu numește bestsellers, deci rezerva statică folosește categorii din discovery, nu un top.
  3. Stimulent: **neaprobat**. Secțiune marcată [OPȚIONAL / TEST] cu `{{COUPON_CODE}}` și `{{COUPON_VALUE}}`. Emailul funcționează fără ea.
- Clientul preferă simplu: email scurt, 3 secțiuni + footer.

## Context util
- Slogan: „eat what you love”. Promisiune: „Ai poftă? Gata în 5 minute.” (din site).
- Dovadă socială aprobată: „Peste 1.100 de recenzii, cu o medie de 4,9 din 5” (valabil 10.10.2026). Nefolosită aici, ca emailul să rămână scurt.
- Fără prețuri (în lucru). Linkuri `{{SHOP_URL}}/...`.
- Footer identic cu restul familiei.

## Reguli de brand (obligatorii)
- Doar 4 culori: portocaliu #FAA61A, roz #F7ACB4, turcoaz #86D2DA, negru #000000. Albul doar ca fundal.
- Pe culori de brand text negru; pe negru doar portocaliu.
- Ton prietenos, direct, jucăuș. Fără vinovăție („ne-ai uitat”), fără presiune, fără „ultima șansă” agresiv, fără afirmații de sănătate.
- Fără emoji, fără em-dash.

## Imagini
Doar mâncare, fără ambalaje inventate, fără text în imagine, fără fețe. Produsele din blocul dinamic vin din feed-ul theMarketer.
