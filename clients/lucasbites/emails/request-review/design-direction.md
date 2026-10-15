# Request review: direcția de design

Surse: `brief.md`, `copy.md`, `discovery.md`, `_reference/ref-iqbar-reviews.png` (principală), `ref-misfits.png`, `ref-olipop-recess.png`. Tehnic: același sistem ca `replenishment/` (tabele, CSS inline, 600px, header și footer identice, `build.py` generează asset-urile și fișierele Figma).

## Idee (versiunea simplificată, 14.10.2026)
Email scurt, 3 benzi de culoare separate prin valuri: portocaliu (recenzie) > roz (social) > alb (recomandări). Din IQBAR păstrăm doar balonul de vorbire, construit în HTML (tabel negru cu colțuri rotunjite + coadă PNG). Fără poză hero cu mâncare (se repeta între emailuri), fără blocul cu produsele din comandă, fără blocul 4,9.

## Tipografie
- Titluri: Akrobat Black, majuscule. H1 104/92px (60/54 pe mobil), H2 60/56px (38/36 pe mobil).
- Supratitlu „script”: Akrobat Bold 24px, minuscule (Plicata ca imagine după licență).
- Text: Arial 14-17px.
- Diacritice: Akrobat are Ș ș Ț ț cu virgulă (U+0218-021B). Virgula coboară ~0,28 em sub linia de bază: sub un titlu cu Ș/Ț pe ultimul rând lăsăm minimum 30px până la text (S1 34px, S2 padding-bottom 14px + 16px).

## Culori (doar cele 4 + alb)
- Pe portocaliu, roz, alb: text negru. Pe negru (balonul din S1): text doar portocaliu.
- Pastile: negru cu text portocaliu; în S3 turcoaz cu text negru. VML pentru Outlook.
- Stele: 5 stele goale, contur portocaliu pe negru, O SINGURĂ imagine = un link spre `{{REVIEW_URL}}` (theMarketer nu acceptă nota în URL).

## Secțiuni
| Secțiune | Fundal | Conținut |
|---|---|---|
| S0 header | alb | logo 180px, val alb > portocaliu |
| S1 recenzie | portocaliu | „ei, cum a fost?”, H1 „Cum au ieșit?”, o frază, balon negru (stele 260 x 48, 220 pe mobil; „Spune-ne cum ți s-au părut”), coadă jos-stânga, pastilă 280 x 56; ~680px pe desktop; val portocaliu > roz |
| S2 social | roz | H2 „Postează-ți creația”, text cu {{INSTAGRAM_HANDLE}} / {{HASHTAG}}, balon gol cu contur, 3 plăci foto 160 x 160, 3 pastile sociale, notă repost; val roz > alb |
| S3 recomandări | alb | H2 „Încearcă și astea”, BLOC DINAMIC 2 x 2 (1 pe mobil), carduri roz, imagine 200 x 200, pastilă turcoaz; fallback ascuns; „eat what you love” |
| S4 footer | alb | identic cu familia |

## Imagini și forme (build.py)
- `images/social-1..3.png` (800 x 800) > `assets/social-N.jpg` 320 x 320, colțuri rotunjite pe roz, afișate 160.
- `stars-outline-orange.png` (520 x 96 / 260 x 48), `tail-black-down.png` (72 x 60 / 36 x 30), `tail-outline-pink.png`, valuri `wave-white-orange`, `wave-orange-pink`, `wave-pink-white` (1200 x 96 / 600 x 48).
- `images/hero.png` nu mai e folosit. În `assets/` au rămas fișiere vechi nefolosite (hero.jpg, chevron, cozi colorate, star-outline, stars-filled, wave-black-pink); nu sunt referite din HTML și se pot șterge.

## Note
- `{{...}}` sunt placeholdere generice, nu sintaxă theMarketer. `?rating=1..5` pe stele e [neverificat].
- Akrobat necesită licență webfont; la upload, `assets/` se înlocuiește cu URL-uri HTTPS absolute.
