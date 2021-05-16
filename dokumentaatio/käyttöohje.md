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

## Pelin sulkeminen

- Biisin voi jättää kesken sulkemalla peli-ikkunan.
- Biisinvalinnasta pääsee pois komennolla 'poistu'.
- Nimenvalintatilassa koko ohjelman saa suljettua komennolla 'sulje'.

# Uusien biisien tekeminen

## Biisin tiedoston luonti

Tehdäksesi uuden biisin, luo sitä vastaava tekstitiedosto hakemistoon data/songs/ ja lisää samaan hakemistoon biisin musiikkitiedosto .wav-muodossa. Kopioi tekstitiedostoon seuraavat asiat:

```bash
name:
audiofile:
speed:
offset:
steps:
```
Nyt voit lisätä tekstitiedostoon biisin nimen, musiikkitiedoston nimen, nopeuden beats per minute -muodossa ja offsetin.
**Ole tarkka, ettet lisää ylimääräisiä välilyöntejä kaksoispisteiden lähelle.**

Malliesimerkki biisitiedostosta:

```bash
name:hyvä biisi
audiofile:hyvamusa.wav
speed:90
offset:0.0
steps:
```
## Nuottien lisääminen

Nyt voit alkaa kirjoittaa nuotteja tiedostoon. Rivin "steps:" jälken tulevat rivit ovat nuottien rivejä. Jokainen rivi vastaa yhtä kappaleen iskua ja rivillä on oltava neljä merkkiä, jotka ovat joko 1 tai 0. Jokainen neljästä merkistä vastaa yhtä riviä pelissä. Ensimmäinen vastaa riviä f, toinen riviä g, kolmas riviä h ja neljäs riviä j. 1 tarkoittaa, että rivillä on nuotti tällä iskulla, 0 tarkoittaa että nuottia ei ole.

Esimerkiksi rivi 1111 tarkoittaa että iskulla tulee jokaiselle riville nuotti. Rivi 0000 taas tarkoittaa, että iskulla ei lisätä nuotteja.

Esimerkkitiedostomme voisikin nyt näyttää tältä:

```bash
name:hyvä biisi
audiofile:hyvamusa.wav
speed:90
offset:0.0
steps:
0000
0000
0101
1110
1000
0001
0000
0000
1001
```

## Mikä on offset ja miten käyttää sitä

Offset on kappaleen ajoituksen hienosäätöä varten. Äänitiedostot harvoin alkavat täydellisesti pelin kannalta niin, että ensimmäine rivi osuu ensimmäiselle iskulle. Tätä varten kappaleelle annetaan offset.

Jos nuotit alkavat liian aikaisin, laita offsettiä pienemmäksi, mahdollisesti negatiiviseksi.
Jos nuotit alkavat liian myöhään, aseta offset isommaksi.

Parhaiten sopivan offsetin löytää kokeilemalla :)
