# Direcție vizuală, New Customer Email 3

Familie comună cu NC1 și NC2: logo, Akrobat (titluri, majuscule) + Arial (text), butoane pastilă bulletproof (VML în Outlook), packshot-uri reale pe plăcuță albă cu contur negru subțire, footer identic cu NC2. Doar #FAA61A, #F7ACB4, #86D2DA, #000000 + alb ca fundal. Text negru pe culori; pe negru, doar portocaliu.

## Ce e nou față de NC1 și NC2
| | NC1 | NC2 | NC3 |
|---|---|---|---|
| Tăieturi | diagonale | diagonale, zig-zag | **ondulate** (wave, 600 x 40), toate secțiunile |
| Hero | roz, farfurii la colțuri | portocaliu, ingrediente zburând | **turcoaz, pur tipografic, centrat**, fără imagine |
| Produse | carduri albe rotunde, zig-zag | perechi rețetă + produs pe fundaluri alternate, 600px | **rând de 3 coloane** (1 coloană pe mobil), un singur fundal roz |
| USP | rând text | un paragraf | **bandă portocalie cu 4 iconițe line art** (2 x 2 pe mobil) |
| Social | doar footer | doar footer | **bloc negru: handle @LUCAS_BITES foarte mare + grilă 3 pătrate „poză de telefon”** |

## Secțiuni, de sus în jos
| Secțiune | Fundal | Text | Pattern |
|---|---|---|---|
| S0 header | alb | negru | logo 180px |
| S1 hero | turcoaz | negru | supratitlu, H1 96px (64px mobil), text, buton negru/portocaliu „Vezi mixurile” |
| S2 cross-sell | roz | negru | H2 + 3 carduri: etichetă, H3, gramaj, imagine card 180 x 250 (packshot + decupaj mâncare care iese din colțul dreapta-jos al plăcuței și din marginea cardului, ref4 col. 3), rând, „Rețetă de încercat”, buton negru; dedesubt buton contur „Vezi toate produsele”. Încadrat de marker `[OPȚIONAL theMarketer]` |
| S3 USP | portocaliu | negru | H2 + 4 coloane (iconiță 56px, titlu Akrobat, rând Arial); mailto/tel subliniate |
| S4 social | negru | portocaliu | supratitlu, handle 80px, 3 pătrate 172px cu colțuri rotunjite, eticheta „Fotografii cu titlu de exemplu.”, text, buton portocaliu Instagram + buton contur TikTok, semnătură |
| S5 footer | alb | negru | copiat din NC2, cu `[ADAUGĂ UTILIZATORUL]` |

Ordinea culorilor (alb, turcoaz, roz, portocaliu, negru, alb) nu repetă NC1 sau NC2.

## Imagini și build
- `assets/card1-brownie.jpg`, `card2-cookies.jpg`, `card3-crepes.jpg` (360 x 500, afișat 180 x 250): plăcuță albă cu packshot nemodificat sus; decupajul IMG1-3 jos-dreapta, poate acoperi doar marginea plăcuței și ultimii 15% din produs.
- `assets/ugc1..3-*.jpg` (352 x 352, afișat 172): IMG4-6, crop central 1:1, nedecupate.
- `assets/usp-*.png`: iconițe desenate în build.py (negru pe transparent).
- `assets/wave-*.png`: 5 tăieturi ondulate.
- Mobil: cardurile S2 pe 1 coloană (imagine 240px, buton 240px), USP 2 x 2, grila UGC rămâne 3 x 1.
- Alt: card = mâncare + ambalaj (punga Brownie / Cookie, flaconul Crêpes); iconițe, tăieturi `alt=""`.
