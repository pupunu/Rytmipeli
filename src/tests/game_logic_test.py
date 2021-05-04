import unittest
import game_logic
from pyglet import sprite, shapes, image


class TestGameLogic(unittest.TestCase):

    def setUp(self):
        noteF_img = image.load('data/graphics/sammakko.png')
        self.note = sprite.Sprite(noteF_img, x=100, y=100)
        self.note.anchor_y = 'center'
        self.points_dict = {'brutal': 0, 'hard': 0, 'normal': 0,
              'easy': 0, 'weak': 0, 'total': 0}
         

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

    def test_check_floor_hit_True(self):
        self.note.y = -100
        self.assertEqual(game_logic.check_floor_hit(self.note), (True, 'Oot huono'))

    def test_check_floor_hit_False(self):
        self.assertEqual(game_logic.check_floor_hit(self.note), (False, ''))

    def test_check_for_hits_gives_score_when_should(self):
        row = [self.note]
        self.note.y = 75
        self.assertEqual(game_logic.check_for_hits(row), 'normal')

    def test_give_points_adds_brutals(self):
        game_logic.give_points(self.points_dict, 'brutal')
        self.assertEqual(self.points_dict, {'brutal': 1, 'hard': 0, 'normal': 0,
              'easy': 0, 'weak': 0, 'total': 100})

    def test_give_points_adds_hards(self):
        game_logic.give_points(self.points_dict, 'hard')
        self.assertEqual(self.points_dict, {'brutal': 0, 'hard': 1, 'normal': 0,
              'easy': 0, 'weak': 0, 'total': 50})

    def test_give_points_adds_normals(self):
        game_logic.give_points(self.points_dict, 'normal')
        self.assertEqual(self.points_dict, {'brutal': 0, 'hard': 0, 'normal': 1,
              'easy': 0, 'weak': 0, 'total': 25})

    def test_give_points_adds_easys(self):
        game_logic.give_points(self.points_dict, 'easy')
        self.assertEqual(self.points_dict, {'brutal': 0, 'hard': 0, 'normal': 0,
              'easy': 1, 'weak': 0, 'total': 10})

    def test_give_points_adds_weaks(self):
        game_logic.give_points(self.points_dict, 'weak')
        self.assertEqual(self.points_dict, {'brutal': 0, 'hard': 0, 'normal': 0,
              'easy': 0, 'weak': 1, 'total': 1})