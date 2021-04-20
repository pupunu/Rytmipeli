import unittest
import rytmipeli

class TestSong(unittest.TestCase):
    def setUp(self):
        pass

    def test_loading_songs_works(self):
        songlist = rytmipeli.load_songs('src/tests/catalog_test_songs/')

        songs = ''

        for song in songlist:
            songs += song +';'

        self.assertEqual(songs, 'testi1;testi2;')
