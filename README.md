# Rytmipeli

Sovellus on peli, jossa painellaan nappeja musiikin tahtiin. Mitä paremmin pysyy rytmissä, sitä paremmat pisteet saa. Pelissä parhaat pisteet tallentuvat ja muiden pelaajien top 10 -pisteitä pääsee katsomaan. Pelimekaniikka muistuttaa ポップンミュージック-rytmipeliä.

## Python-versio
Sovellus on suunniteltu toimimaan python 3.6.0:lla. Vanhemmilla versioilla saattaa olla ongelmia suorittaa ohjelmaa.

## Dokumentaatio 
[vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)

[arkkitehtuurikuvaus](/dokumentaatio/arkkitehtuuri.md)

[tuntikirjanpito](/dokumentaatio/tuntikirjanpito.md)

## Uusin julkaisu
[Uusin julkaisu](https://github.com/pupunu/ot-harjoitutyo/releases/tag/viikko5) löytyy täältä.

## Asennus
1. Asenna riippuvuudet komennolla
```bash
poetry install
```

2. Käynnistä ohjelma komennolla
```bash
poetry run invoke start
```

## Ohjelman käynnistys
Käynnistä ohjelma komennolla
```bash
poetry run invoke start
```

## Ohjelman testaus
Suorita testit komennolla
```bash
poetry run invoke test
```
## Testikattavuusraportti
1. Testikattavuusraportin saa suorittamalla komennon
```bash
poetry run invoke coverage-report
```

2. Testikattavuusraportin saa suoraan suoritettua ja näkyviin firefoxissa (jos asennettu) auki komennolla
```bash
poetry run invoke see-coverage-report
```
## Pylint
Suorita koodin laatutarkastus komennolla
```bash
poetry run invoke lint
```

![kuva: betazoid alien pelaa pingistä](/data/graphics/pingis.jpg)
