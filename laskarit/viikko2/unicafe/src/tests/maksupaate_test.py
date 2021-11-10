import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        

    def test_alussa_oike_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_maksaminen_palauttaa_oikean_summan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_liian_pieni_edullisen_kateismaksu_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_maukkaan_maksaminen_palauttaa_oikean_summan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(460), 60)

    def test_liian_pieni_maukkaan_kateismaksu_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_edullisesti_kortilla_palauttaa_truen(self):
        self.kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)

    def test_edullisesti_kortilla_ei_rahaa_palauttaa_falsen(self):
        self.kortti = Maksukortti(50)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), False)

    def test_maukkaasti_kortilla_palauttaa_truen(self):
        self.kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)

    def test_maukkaasti_kortilla_ei_rahaa_palauttaa_falsen(self):
        self.kortti = Maksukortti(50)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), False)

    def test_kortin_lataus_onnistuu(self):
        self.kortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(self.kortti,1000)
        self.assertEqual(str(self.kortti), "saldo: 15.0")

    def test_kortin_lataus_ei_onnistu_negatiivisella_summalla(self):
        self.kortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1)
        self.assertEqual(str(self.kortti), "saldo: 5.0")
