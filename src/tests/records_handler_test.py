import unittest
import records_handler
from rytmipeli import load_songs
import os

#luo testiksi tulokset oikeaan records-kansioon, en jaksa fiksata atm että olisi erikseen testin records

class TestRecordsHandler(unittest.TestCase):
    def setUp(self):
        self.song = load_songs('src/tests/catalog_test_songs/')['testi1']
        self.path = 'data/records/testi1.txt'
        self.playername = 'testipelaaja'
        self.results = {'brutal': 1, 'hard': 1, 'normal': 1,
              'easy': 1, 'weak': 1, 'total': 186}

    def test_update_records_gives_correct_records(self):
        new_results = records_handler.update_records(self.song, self.playername, self.results)
        new_results = new_results[0]

        os.remove(self.path)
        self.assertEqual(new_results, [('testipelaaja', 186),
        ('---', 0), ('---', 0), ('---', 0), ('---', 0),
        ('---', 0), ('---', 0), ('---', 0), ('---', 0), ('---', 0)])

    def test_update_gives_right_placing_when_better(self):
        new_results = records_handler.update_records(self.song, self.playername, self.results)
        self.results['total'] = 1000
        new_results = records_handler.update_records(self.song, self.playername, self.results)[0]
        print(new_results)
        
        os.remove(self.path)

        self.assertEqual(new_results, [('testipelaaja', 1000), ('testipelaaja', 186),
        ('---', 0), ('---', 0), ('---', 0), ('---', 0),
        ('---', 0), ('---', 0), ('---', 0), ('---', 0)])

    def test_update_gives_right_placing_when_worse(self):
        new_results = records_handler.update_records(self.song, self.playername, self.results)
        self.results['total'] = 1
        new_results = records_handler.update_records(self.song, self.playername, self.results)[0]
        print(new_results)
        
        os.remove(self.path)

        self.assertEqual(new_results, [('testipelaaja', 186), ('testipelaaja', 1),
        ('---', 0), ('---', 0), ('---', 0), ('---', 0),
        ('---', 0), ('---', 0), ('---', 0), ('---', 0)])