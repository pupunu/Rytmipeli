import unittest
from song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song('karameldanssen', 'karameldanssen.txt', 'audio.mp3')

    def test_correct_name(self):
        self.assertEqual(self.song.name, 'karameldanssen')

    def test_correct_filename(self):
        self.assertEqual(self.song.songfile, "karameldanssen.txt")