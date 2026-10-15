# Replenishment: direcția de design

Surse: `brief.md`, `copy.md`, `discovery.md`, `_reference/ref-misfits.png`, `_reference/ref-olipop-recess.png`. Tehnic: același sistem ca `new-customer-01/` (tabele, CSS inline, 600px, header și footer identice, `build.py` care generează asset-urile).

## Idee
Un email scurt și apetisant, construit din benzi de culoare plină separate prin valuri (ref Misfits): fiecare secțiune are o singură culoare de brand și o singură idee. Ritmul de culoare: alb (header) > portocaliu (hero) > alb (reamintire) > roz (produse) > negru (cifre) > turcoaz (CTA final) > alb (footer).

## Tipografie
- Titluri: Akrobat Black, majuscule, supradimensionate. H1 88/78px (52/48 pe mobil), H2 56-64px (34 pe mobil).
- Supratitlu „script”: Akrobat Bold 24px, minuscule, deasupra titlului. Plicata nu e licențiată: când se cumpără, supratitlurile se înlocuiesc cu imagini PNG Plicata, la aceeași poziție (ca în emailurile anterioare).
- Text: Arial 15-20px. Fallback titluri: „Arial Narrow”, Arial.

## Culori (doar cele 4 + alb)
- Pe portocaliu, roz, turcoaz, alb: text negru. Pe negru: text doar portocaliu.
- Butoane pastilă: negru cu text portocaliu (pe culori deschise). Bulletproof VML pentru Outlook.

## Secțiuni
| Secțiune | Fundal | Conținut |
|---|---|---|
| S0 header | alb | logo 180px, val alb > portocaliu |
| S1 hero | portocaliu | supratitlu, H1 „Mai e pentru o tură?”, hero 600 x 440 cu ingrediente în zbor, text, CTA 280 x 56 |
| S2 reamintire | alb | text mare 20px bold + notă 14px |
| S3 produse | roz | supratitlu, H2 „Fă plinul”, BLOC DINAMIC theMarketer (placeholder cu contur punctat, 2 carduri pe rând, 1 pe mobil, imagine 200 x 200, fără preț, pastilă 170 x 40), fallback ascuns |
| S4 de ce revii | negru | 3 coloane stil Misfits: „5” MINUTE, „4,9” DIN 5, iconiță 96 x 96 DEJA LA CÂNTAR; se stivuiesc pe mobil |
| S5 CTA final | turcoaz | supratitlu „eat what you love”, H2, imagine pe toată lățimea, fără crop, CTA 300 x 60, contact |
| S6 footer | alb | identic cu familia |

## Imagini (build.py le compune pe culoarea secțiunii)
| Sursă (`images/`) | Ieșire (`assets/`) | Export / afișat |
|---|---|---|
| hero.png | hero.jpg (pe portocaliu; PNG transparent = centrat jos, opac = crop) | 1200 x 880 / 600 x 440 |
| s4-icon-clean.png | s4-icon.png (pe negru) | 192 x 192 / 96 x 96 |
| s5-cta.png | s5-cta.jpg (întreagă, fără crop, fundal adus pe turcoaz) | 1200 lățime / 600 lățime, înălțime proporțională |
Lipsă imagine = placeholder la dimensiunea finală; se rulează din nou build-ul după ce apare.
Produsele din S3 vin din feed-ul theMarketer, nu se generează.

## Valuri
6 PNG 1200 x 96 (afișate 600 x 48), 1,5 perioade, amplitudine mică (ref Misfits), față de curba mare din new-customer-01.

## Note
- `{{...}}` sunt placeholdere generice, nu sintaxă theMarketer (copy.md, secțiunea 7).
- Akrobat necesită licență webfont înainte de trimitere; la upload, `assets/` se înlocuiește cu URL-uri HTTPS absolute.
