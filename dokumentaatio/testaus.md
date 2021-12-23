# Testausdokumentti

Ohjelmaa on testattu automatisoiduin testein sekä manuaalisesti.

Suurin osa automatisoiduista testeistä on service-luokkien testejä, mutta koska ne käyttävät oikeita repositorioluokkia ja testitietokantaa (joka on identtinen oikean kanssa), toimivat ne myös intgraatiotesteinä. Testeissä on pyritty ennenkaikkea simuloimaan käyttöliittymältä tulevia realistisia syötteitä, ja katsottu, että koko järjestelmä reagoi niihin oikein. Käyttöliittyää, ja varsinkin battle ui:ta, joka on toteutettu Pygletillä ja siten vaikeampaa testata automaattisesti, on testattu manuaalisesti kattavasti.

### Testikattavuus

Käyttöliittymää lukuunottamatta testien haaratumakattavuus on 88 %. Testamaatta on jokseenkin triviaaleja asioita, jotka pääsääntöisesti vain siirtävät dataa suoraan repositoriasta käyttöliittymälle. Lähinnä skillrepositoryssa on valmisteluja ominaisuuksille, joiden lisäys olisi seuraavana vuorossa, niin niitä ei ole testattu.

Kaikki määrittelydokumentissa ja käyttöohjeessa olevat ominaisuudet on testattu Linux-ympäristössä.
