import unittest
from rytmipeli import load_songs


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = load_songs('src/tests/catalog_test_songs/')['testi1']

    def test_correct_name(self):
        self.assertEqual(self.song.name, 'testi1')

    def test_correct_filename(self):
        self.assertEqual(self.song.filename,
                         "src/tests/catalog_test_songs/testibiisi.txt")

    def test_correct_audiofile(self):
        self.assertEqual(self.song.audiofile,
                         "src/tests/catalog_test_songs/testibiisi1.wav")

    def test_str_returns_name(self):
        self.assertEqual('testi1', str(self.song))

    def test_load_steps_works(self):
        self.song.load_steps()
        self.assertEqual(self.song.steps, ['0001', '1000'])

    def test_get_next_beat_works_in_the_middle(self):
        self.song.load_steps()
        beat = self.song.get_next_beat()
        self.assertEqual(beat, '0001')
