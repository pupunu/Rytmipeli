import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_alussa_oikea_maara_rahaa(self):
        self.assertEqual(str(self.maksukortti),"saldo: 10.0")

    def test_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "saldo: 12.0")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(400)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")

    def test_saldo_ei_muutu_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_metodi_palauttaa_true_jos_on_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(300), True)

    def test_metodi_palauttaa_false_jos_ei_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1200), False)
