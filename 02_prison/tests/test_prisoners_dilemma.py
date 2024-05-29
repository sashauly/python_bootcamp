import unittest

from prison.prisoners_dilemma import Game, Cheater, Cooperator, Copycat, Grudger, Detective


class TestCooperator(unittest.TestCase):
    def test_cooperator_cheater(self):
        cooperator = Cooperator()
        cheater = Cheater()
        game = Game()
        game.play(cooperator, cheater)
        result = [('Cheater', 30), ('Cooperator', -10)]
        self.assertEqual(result, game.top3())

    def test_cooperator_copycat(self):
        cooperator = Cooperator()
        copycat = Copycat()
        game = Game()
        game.play(cooperator, copycat)
        result = [('Cooperator', 20), ('Copycat', 20)]
        self.assertEqual(result, game.top3())

    def test_cooperator_grudger(self):
        cooperator = Cooperator()
        grudger = Grudger()
        game = Game()
        game.play(cooperator, grudger)
        result = [('Cooperator', 20), ('Grudger', 20)]
        self.assertEqual(result, game.top3())

    def test_cooperator_detective(self):
        cooperator = Cooperator()
        detective = Detective()
        game = Game()
        game.play(cooperator, detective)
        result = [('Detective', 27), ('Cooperator', -1)]
        self.assertEqual(result, game.top3())


class TestCheater(unittest.TestCase):
    def test_cheater_copycat(self):
        cheater = Cheater()
        copycat = Copycat()
        game = Game()
        game.play(cheater, copycat)
        result = [('Cheater', 3), ('Copycat', -1)]
        self.assertEqual(result, game.top3())

    def test_cheater_grudger(self):
        cheater = Cheater()
        grudger = Grudger()
        game = Game()
        game.play(cheater, grudger)
        result = [('Cheater', 3), ('Grudger', -1)]
        self.assertEqual(result, game.top3())

    def test_cheater_detective(self):
        cheater = Cheater()
        detective = Detective()
        game = Game()
        game.play(cheater, detective)
        result = [('Cheater', 9), ('Detective', -3)]
        self.assertEqual(result, game.top3())


class TestCopycat(unittest.TestCase):
    def test_copycat_grudger(self):
        copycat = Copycat()
        grudger = Grudger()
        game = Game()
        game.play(copycat, grudger)
        result = [('Copycat', 20), ('Grudger', 20)]
        self.assertEqual(result, game.top3())

    def test_copycat_detective(self):
        copycat = Copycat()
        detective = Detective()
        game = Game()
        game.play(copycat, detective)
        result = [('Detective', 19), ('Copycat', 15)]
        self.assertEqual(result, game.top3())


class TestDetective(unittest.TestCase):
    def test_detective_grudger(self):
        detective = Detective()
        grudger = Grudger()
        game = Game()
        game.play(detective, grudger)
        result = [('Grudger', 7), ('Detective', 3)]
        self.assertEqual(result, game.top3())


class TestAll(unittest.TestCase):
    def test_all_pairs(self):
        cheater = Cheater()
        cooperator = Cooperator()
        copycat = Copycat()
        grudger = Grudger()
        detective = Detective()

        game = Game()

        players = [cheater, cooperator, copycat, grudger, detective]
        for player1 in players:
            for player2 in players:
                if player1 != player2:
                    game.play(player1, player2)
        result = [('Cheater', 78), ('Grudger', 65), ('Copycat', 62)]
        self.assertEqual(result, game.top3())


if __name__ == '__main__':
    unittest.main()
