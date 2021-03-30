import unittest

from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.korttirikas = Maksukortti(1000)
        self.korttikoyha = Maksukortti(200)

    def test_alussa_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_alussa_maukkaita_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_alussa_edullisia_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

#Maukkaasti käteisellä

    def test_kateisella_maukkaasti_kassa_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 400)

    def test_kateisella_maukkaasti_oikea_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1000), 600)

    def test_kateisella_maukkaasti_myytyjen_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisella_maukkaasti_ei_tarpeeksi_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_kateisella_maukkaasti_ei_tarpeeksi_kassan_rahat_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisella_maukkaasti_ei_rahaa_maukkaat_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

#Edullisesti käteisellä

    def test_kateisella_edullisesti_kassa_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 240)

    def test_kateisella_edullisesti_oikea_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(1000), 1000-240)

    def test_kateisella_edullisesti_myytyjen_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisella_edullisesti_ei_tarpeeksi_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_kateisella_edullisesti_ei_tarpeeksi_kassan_rahat_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisella_edullisesti_ei_rahaa_edulliset_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

#Edullisesti maksaminen kortilla, rahaa tarpeeksi

    def test_kortilla_rahaa_osta_edullinen_raha_lahtee(self):
        self.kassapaate.syo_edullisesti_kortilla(self.korttirikas)
        self.assertEqual(self.korttirikas.saldo, 1000-240)

    def test_kortilla_rahaa_osta_edullinen_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.korttirikas), True)

    def test_kortilla_rahaa_osta_edullinen_edulliset_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.korttirikas)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortilla_rahaa_osta_edullinen_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.korttirikas)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

#Maukkaasti maksaminen kortilla, rahaa tarpeeksi

    def test_kortilla_rahaa_osta_maukas_raha_lahtee(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.korttirikas)
        self.assertEqual(self.korttirikas.saldo, 1000-400)

    def test_kortilla_rahaa_osta_maukas_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.korttirikas), True)

    def test_kortilla_rahaa_osta_maukas_maukkaat_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.korttirikas)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_rahaa_osta_maukas_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.korttirikas)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

#Edullisesti kortilla, liian vähän rahaa

    def test_edullisesti_kortilla_ei_rahaa_kortin_raha_ei_muut(self):
        self.kassapaate.syo_edullisesti_kortilla(self.korttikoyha)
        self.assertEqual(self.korttikoyha.saldo, 200)

    def test_edullisesti_kortilla_ei_rahaa_edulliset_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.korttikoyha)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisesti_kortilla_ei_rahaa_palauttaa_false(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.korttikoyha), False)

#Maukkaasti kortilla, liian vähän rahaa

    def test_maukkaasti_kortilla_ei_rahaa_kortin_raha_ei_muut(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.korttikoyha)
        self.assertEqual(self.korttikoyha.saldo, 200)

    def test_maukkaasti_kortilla_ei_rahaa_edulliset_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.korttikoyha)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaasti_kortilla_ei_rahaa_palauttaa_false(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.korttikoyha), False)

#Rahan lataus

    def test_kortille_negatiivinen_lataus_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.korttikoyha, -200)
        self.assertEqual(self.korttikoyha.saldo, 200)

    def test_kortille_negatiivinen_lataus_kassan_raha_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.korttikoyha, -200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_lataus_muuttaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.korttikoyha, 1000)
        self.assertEqual(self.korttikoyha.saldo, 1200)

    def test_kortille_lataus_muuttaa_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.korttikoyha, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 1000)
