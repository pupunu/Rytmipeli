import unittest
import game_logic


class TestGameLogic(unittest.TestCase):

    def test_gives_right_score_weak(self):
        score = game_logic.get_score(45)
        self.assertEqual(score, 'weak')

    def test_gives_right_score_easy(self):
        score = game_logic.get_score(35)
        self.assertEqual(score, 'easy')

    def test_gives_right_score_normal(self):
        score = game_logic.get_score(25)
        self.assertEqual(score, 'normal')

    def test_gives_right_score_hard(self):
        score = game_logic.get_score(15)
        self.assertEqual(score, 'hard')

    def test_gives_right_score_brutal(self):
        score = game_logic.get_score(5)
        self.assertEqual(score, 'brutal')

    def test_hit_true_if_collision(self):
        self.assertEqual(game_logic.is_hit(30), 20)

    def test_hit_false_if_no_collision(self):
        self.assertEqual(game_logic.is_hit(120), False)
