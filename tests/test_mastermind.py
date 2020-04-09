from unittest import TestCase
from pyarcade.games.mastermind import Mastermind, total_history


class MastermindTestCase(TestCase):
    def setUp(self):
        pass

    def test_exact_match(self):
        game1 = Mastermind()
        game1.set_hidden_sequence([1, 2, 3, 4])
        self.assertEqual({1: 1, 2: 1, 3: 1, 4: 1}, game1.evaluate([1, 2, 3, 4]))
        self.assertEqual({1: {(1, 2, 3, 4): {1: 1, 2: 1, 3: 1, 4: 1}}}, total_history)
        game2 = Mastermind()
        game2.set_hidden_sequence([5, 6, 7, 8])
        self.assertEqual({5: 1, 6: 1, 7: 1, 8: 1}, game2.evaluate([5, 6, 7, 8]))
        self.assertEqual({1: {(1, 2, 3, 4): {1: 1, 2: 1, 3: 1, 4: 1}}, 2: {(5, 6, 7, 8): {5: 1, 6: 1, 7: 1, 8: 1}}},
                         total_history)
        game1.clear()
        self.assertEqual({}, total_history)

    def test_some_correct_digits(self):
        game = Mastermind()
        game.set_hidden_sequence([1, 2, 3, 4])
        self.assertEqual({1: 1, 8: -1, 6: -1, 2: 0}, game.evaluate([1, 8, 6, 2]))
        self.assertEqual({(1, 8, 6, 2): {1: 1, 8: -1, 6: -1, 2: 0}}, game.current_history)
        self.assertEqual({}, total_history)
        self.assertEqual({1: 1, 2: 1, 6: -1, 3: 0}, game.evaluate([1, 2, 6, 3]))
        self.assertEqual({(1, 8, 6, 2): {1: 1, 8: -1, 6: -1, 2: 0}, (1, 2, 6, 3): {1: 1, 2: 1, 6: -1, 3: 0}}, game.current_history)
        game.reset()
        self.assertEqual({}, game.current_history)
        game.clear()

    def test_all_wrong_digits(self):
        game = Mastermind()
        game.set_hidden_sequence([1, 2, 3, 4])
        self.assertEqual({5: -1, 6: -1, 7: -1, 8: -1}, game.evaluate([5, 6, 7, 8]))
        self.assertEqual({(5, 6, 7, 8): {5: -1, 6: -1, 7: -1, 8: -1}}, game.current_history)
        self.assertEqual({}, total_history)
        game.clear()

    def tearDown(self):
        pass
