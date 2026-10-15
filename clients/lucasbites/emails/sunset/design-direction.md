# Sunset: direcția de design

Surse: `brief.md`, `copy.md`, `discovery.md`. Tehnic: același sistem ca `request-review/` (tabele, CSS inline, 600px exact, header și footer identice, pastile cu VML pentru Outlook, `build.py` generează asset-urile și fișierele Figma). Fără referințe externe.

## Idee
Email scurt și simplu: o întrebare, un buton. 3 benzi separate prin valuri: portocaliu (decizia) > alb (bestsellers) > turcoaz (cupon, opțional). Fără hero mare cu mâncare: o singură ilustrație compactă (clătită-inimă pe farfurie), 320px, întreagă, pe portocaliu.

## Tipografie
- Titluri Akrobat Black, majuscule. H1 104/92px (60/54 mobil). H2 60/68px (38/46 mobil).
- Supratitluri Akrobat Bold 24px, minuscule. Text Arial 14-17px.
- Diacritice: virgula din Ș/Ț coboară ~0,28 em. Ambele H2 au Ț pe primul rând („ALEGE-ȚI”, „IA-ȚI”), deci line-height mărit (68px desktop, 46px mobil) ca virgula să nu atingă rândul următor; sub titluri minimum 30px.

## Culori (doar cele 4 + alb)
Pe portocaliu, alb, turcoaz, roz: text negru. Pe negru (pastile, cupon): doar portocaliu.

## Secțiuni
| Secțiune | Fundal | Conținut |
|---|---|---|
| S0 header | alb | logo 180px, val alb > portocaliu |
| S1 rămâi | portocaliu | ilustrație 320px (260 mobil), „o întrebare scurtă”, H1 „Mai rămâi cu noi?”, text, pastilă neagră „Da, rămân” 280 x 56, link text subliniat 14px „Nu acum, mă dezabonez”, notă 14px cu {{SUNSET_DAYS}}; val portocaliu > alb |
| S2 bestsellers | alb | „dacă tot ești aici”, H2 „Alege-ți pofta de azi”, „Ai poftă? Gata în 5 minute.”, BLOC DINAMIC (chenar întrerupt, etichetat [Placeholder]) cu 3 carduri roz, imagine 140 x 140, pastilă turcoaz „Vezi mixul”, fără preț; rezervă ascunsă (Pankees / Brownie și Lava Cake / Pizza Mix); „eat what you love” |
| S3 cupon [OPȚIONAL / TEST] | turcoaz | etichetă vizibilă „Opțional / test”, H2 „Ia-ți {{COUPON_VALUE}} reducere”, text, cupon: chenar negru cu margine întreruptă portocalie și cod portocaliu, pastilă „Folosește codul”, termeni 14px. Încadrat de comentariile `[OPȚIONAL / TEST] S3 CUPON START/END`, valurile incluse: se șterge blocul întreg și emailul trece curat în footer |
| S4 footer | alb | identic cu familia |

## Imagini și forme (build.py)
- `images/s1-visual.png` > `assets/s1-visual.jpg`: întreagă, fără crop, fără card, fundal adus exact la #FAA61A, margini goale tăiate, 640 lățime (afișată 320), înălțimea scrisă automat în index.html.
- Valuri 1200 x 96 (afișate 600 x 48): alb>portocaliu, portocaliu>alb, alb>turcoaz, turcoaz>alb.
- Logo, iconițe sociale, font Akrobat: copiate din `request-review/assets/`.

## Note
- `{{...}}` sunt placeholdere generice, nu sintaxă theMarketer. UTM: utm_medium=lifecycle, utm_campaign=sunset, utm_content per copy.md.
- Akrobat necesită licență webfont; la upload, `assets/` se înlocuiește cu URL-uri HTTPS absolute.
