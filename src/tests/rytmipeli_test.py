import unittest
import rytmipeli


class TestRytmipeli(unittest.TestCase):
    def setUp(self):
        pass

    def test_loading_songs_works(self):
        songlist = rytmipeli.load_songs('src/tests/catalog_test_songs/')
        self.assertEqual(list(songlist), ['testi1'])
