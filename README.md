# Harjoitustyö

Vuoropohjainen roolipeli, jossa hahmoa kehitetään taistelemalla yksittäisiä vihollisia vastaan erilaisilla areenoilla. Ajatuksena on testata, voiko eri aseita tasapainottaa niin, että isompi on yleensä parempi, mutta sitä on vaikeampaa käyttää kuin kuin pienempää jos areenalla ei ole tarpeeksi tilaa. Tavoitteena on, että erilaisia tasapainotuksia on suhteellisen helppoa testata muuttamalla muutamaa muuttujaa.


* [Vaatimusmäärittely](https://github.com/Yogho358/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](https://github.com/Yogho358/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
* [Arkkitehtuuri](https://github.com/Yogho358/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.MD)
* [Release](https://github.com/Yogho358/ot-harjoitustyo/releases/tag/viikko5)
* [Release 2](https://github.com/Yogho358/ot-harjoitustyo/releases/tag/viikko6)
* [Release 3, final](https://github.com/Yogho358/ot-harjoitustyo/releases/tag/lopullinen)
* [Käyttöohje](https://github.com/Yogho358/ot-harjoitustyo/blob/master/dokumentaatio/manual.md)
* [Testausdokumentti](https://github.com/Yogho358/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

## Käyttöohje

Asenna ensin riippuvuudet komennolla poetry install, sitten asenna peli komennolla poetry run invoke build.

Peli käynnistetään komennolla poetry run invoke start

Testit ajetaan komennolla poetry run invoke test, testikattavuusraportin saa komennolla poetry run invoke coverage-report, ja lint-raportin komennolla poetry run invoke lint

