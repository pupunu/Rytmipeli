import unittest
from catalog import Catalog

class TestCatalog(unittest.TestCase):
    def setUp(self):
        self.catalog = Catalog()
        self.catalog.load_songs('src/tests/catalog_test_songs/')
    
    def test_song_loading_works(self):

        return self.assertEqual(self.catalog.list_songs(), ['testi1', 'testi2'])
