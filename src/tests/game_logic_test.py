import unittest
import game_logic

class TestGameLogic(unittest.TestCase):

    def test_gives_right_score_weak(self):
        score = game_logic.score(45)
        self.assertEqual(score, 'Heikko')

    def test_gives_right_score_easy(self):
        score = game_logic.score(35)
        self.assertEqual(score, 'Helppo')

    def test_gives_right_score_normal(self):
        score = game_logic.score(25)
        self.assertEqual(score, 'Normaali')

    def test_gives_right_score_hard(self):
        score = game_logic.score(15)
        self.assertEqual(score, 'Vaikea')

    def test_gives_right_score_brutal(self):
        score = game_logic.score(5)
        self.assertEqual(score, 'Brutaali')

    def test_hit_true_if_collision(self):
        self.assertEqual(game_logic.is_hit(30), 20)

    def test_hit_false_if_no_collision(self):
        self.assertEqual(game_logic.is_hit(120), False)
