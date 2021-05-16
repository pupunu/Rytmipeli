# Arkkitehtuurikuvaus

## Ohjelman toiminnallinen rakenne

Ohjelman rakenne noudattelee seuraavanlaista arkkitehtuuria. Kuvassa jokanen laatikko tarkoittaa omaa moduuliaan. Ohjelmalla on siis kolmitasoinen kerrosarkkitehtuuri, jossa ylinpänä on rytmipeli, sen jälkeen ui, records_handler, song ja game, joista game käyttää vielä game_logicia ja GameWindowta.

![pakkauskaavio](kuvat/pakkauskaavio.png)

rytmipeli vastaa pelin etenemisestä biisien valinnasta niiden pelaamiseen, ui huolehtii asioiden kirjoittamisen ja lukemisen näytölle pelaajanimeä ja kappaletta valitessa. Song vastaa kappaleiden lataamisesta pelivalmiiksi ja game vastaa itse pelin pelaamisen toiminnallisuuksista.

## Käyttöliittymä
Ohjelmassa on neljä erillistä tilaa.

- Alkutila, jossa annetaan pelaajanimi.
- Kappaleen valitsemistila
- Pelitila
- Tulosten katselutila

Alkutilasta, kappaleen valitsemisesta ja tulosten katselusta vastaa rytmipeli ui:n avulla. Pelitilasta vastaa kokonaan moduuli game, joka hyödyntää game_logicia ja GameWindowta pelin pyörittämisessä. GameWindow vastaa sekä asioiden näyttäisestä ruudulla, että näppäinpainallusten tarkistamisesta.

## Sovelluslogiikka

Sovelluksessa pelin keskiössä ovat Song-oliot, joihin on tallennettu kappaleen musiikin tiedot ja pelin nuotit. Näiden valitsemisesta vastaa rytmipeli ja ui, ja pelissä käsittelyssä niistä vastaa game. Game pitää huolen siitä, että nuotit lisätään pelialueelle oikein ja tippuvat kentän ylälaidasta alalaitaan. Sekä pitää kirjaa pelin aikana pisteistä.

## Tiedostot

Pelissä on valmiiksi kaksi kappaletta ja niitä voi tehdä lisää käyttöohjeen avulla. Nämä tiedostot löytyvät ohjelman data-hakemistosta. Lisäksi data-hakemistosta löytyvät pelin ennätykset. Pelin aloittaessa ensimmäistä kertaa luodaan ennätyksiä varten oma kansionsa, jos sellainen puuttuu. Ennätykset ja biisien tiedot on tallennettu tavallisina tekstitiedostoina.

### Biisien tallennusformaatti
 
 ```bash
name:biisin nimi
audiofile:biisin .wav-muodossa olevan musiikkitiedoston nimi
speed:biisin nopeus bpm-muodossa
offset:biisin offset, eli alkaako biisi heti musiikkitiedoston alusta vai pitääkö alkua hidastaa/aikaistaa 
steps:
0010
1101
.
.
.
 ```
Rivin steps: jälkeen alkavat siis nuotit, joissa yksi rivi vastaa yhtä iskua ja merkit rivillä vasemmalta oikealle pelin nuottirivejä f, g, h ja j. 1 tarkoittaa, että iskussa on kyseisellä rivillä nuotti ja 0 tarkoittaa, että iskussa ei ole kyseisellä rivillä nuottia.

### Tulosten tallennusformaatti

 ```bash
pelaajan nimi:saadut pisteet
pelaajan nimi:saadut pisteet
pelaajan nimi:saadut pisteet
pelaajan nimi:saadut pisteet
pelaajan nimi:saadut pisteet
pelaajan nimi:saadut pisteet
pelaajan nimi:saadut pisteet
pelaajan nimi:saadut pisteet
pelaajan nimi:saadut pisteet
pelaajan nimi:saadut pisteet
 ```
 Ensimmäisellä rivillä oleva on aina saanut parhaat pisteet ja näin mitä alemmas menee rivejä, sitä vähemmän pisteitä on saanut. Rivejä on aina kymmenen.

## Päätoiminnallisuudet ja sekvenssikaaviot
### Ohjelman perustoiminnallisuus

Kun peli lähtee käyntiin tapahtuu seuraavasti:

![main-sekvenssikaavio](kuvat/pelinmain.png)

### Mitä tapahtuu, kun pelaaja painaa nappia f

Pelitilan ollessa käynnissä, pelistä saa pisteitä painamalla nappeja f, g, h ja j sopivassa rytmissä. Kun pelaaja painaa esimerkiksi nappia f, GameWindow tarkistaa onko osumaa tapahtunut, ja jos on, se laskee osuman arvosanan ja antaa siitä pisteet. Lisäksi pelinäytölle ilmestyy uusimman osuman arvosanan nimi ja kokonaispistemäärä kasvaa.

![painetaan f](kuvat/pelaajapainaaf.png)

### Miten pelin tulokset käsitellään biisin loputtua

Kun biisi loppuu, peli palauttaa pelaajan tulokset. Sitten rytmipelin main päivittää records_handlerin tarjoamin metodein uudet tulokset kappaleen ennätysten top 10 -listaan ja näyttää sekä pelaajan omat tulokset, että top 10 -tulokset.

![kun biisi loppuu, mitä tuloksille tapahtuu](kuvat/tulokset.png)
