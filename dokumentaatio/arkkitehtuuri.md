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

### Päätoiminnallisuudet ja sekvenssikaaviot
#### Ohjelman perustoiminnallisuus

Kun peli lähtee käyntiin tapahtuu seuraavasti:

![main-sekvenssikaavio](kuvat/pelinmain.png)

#### Mitä tapahtuu, kun pelaaja painaa nappia f

Pelitilan ollessa käynnissä, pelistä saa pisteitä painamalla nappeja f, g, h ja j sopivassa rytmissä. Kun pelaaja painaa esimerkiksi nappia f, GameWindow tarkistaa onko osumaa tapahtunut, ja jos on, se laskee osuman arvosanan ja antaa siitä pisteet. Lisäksi pelinäytölle ilmestyy uusimman osuman arvosanan nimi ja kokonaispistemäärä kasvaa.

![painetaan f](kuvat/pelaajapainaaf.png)

#### Miten pelin tulokset käsitellään biisin loputtua

Kun biisi loppuu, peli palauttaa pelaajan tulokset. Sitten rytmipelin main päivittää records_handlerin tarjoamin metodein uudet tulokset kappaleen ennätysten top 10 -listaan ja näyttää sekä pelaajan omat tulokset, että top 10 -tulokset.

![kun biisi loppuu, mitä tuloksille tapahtuu](kuvat/tulokset.png)
