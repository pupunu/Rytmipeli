# Käyttöohje

Projektin viimeisimmän version saa ladattua [uusimman julkaisun](https://github.com/pupunu/ot-harjoitutyo/releases/tag/viikko6) lähdekoodin.

## Miten pelin saa käyntiin

Kun ohjelman koodi on ladattu, tulee asentaa riippuvuudet komennolla:

```bash
poetry install
```

Nyt ohjelman voi käynnistää komennolla

```bash
poetry run invoke start
```

## Pelaajanimen antaminen

Pelin alkaessa kysytään pelaajanimeä. Tämä tapahtuu komentorivillä. Kirjoita komentoriville käyttäjänimesi ja paina enter.

## Biisin valinta

Pelaajanimen annettuasi pelin biisit listataan ja voit valita niistä haluamasi. Kirjoita biisin nimi komentoriville ja paina enter.

## Pelin pelaaminen

Kun olet valinnut biisin, pelinäkymä avautuu ja pääset pelaamaan. Pelissä ylhäältä tippuu sammakon näköisiä nuotteja neljässä rivissä. Rivien alapäässä on pallurat F, G, H ja J. Kun sammakon pää on palluran kohdalla, paina riviä vastaavaa kirjainta. Yritän osua mahdollisimman tarkasti, niin saat parhaimmat pisteet!
(tällä hetkellä biisin loppuessa ikkuna ei vielä sulkeudu, joten nuottien loppuessa sulje ikkuna)

Pelin jälkeen näet omat pisteesi ja voit verrata niitä muiden pisteisiin. Pisteet ovat laitekohtaisia. Sitten voit valita uuden biisin.
