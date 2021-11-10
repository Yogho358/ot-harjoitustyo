import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_lataaminen_kasvatta_saldoa(self):
        self.maksukortti.lataa_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "saldo: 30.0")

    def test_ottaminen_vahentaa_saldoa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

    def test_liian_suuri_otto_ei_muuta_saldoa(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_ottaminen_palauttaa_truen(self):
        toimiko = self.maksukortti.ota_rahaa(500)
        self.assertEqual(toimiko, True)

    def test_rahan_ottamatta_jattaminen_palauttaa_falsen(self):
        toimiko = self.maksukortti.ota_rahaa(5000)
        self.assertEqual(toimiko, False)