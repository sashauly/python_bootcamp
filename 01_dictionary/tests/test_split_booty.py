import unittest

from golden_fewer.split_booty import split_booty


class TestSplitBooty(unittest.TestCase):
    def test_split_booty_default(self):
        purse1 = {"gold_ingots": 3}
        purse2 = {"gold_ingots": 2}
        purse3 = {"apples": 10}

        new_purses = split_booty(purse1, purse2, purse3)
        result = [{"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 1}]
        self.assertEqual(result, new_purses)

    def test_split_booty_none_given(self):
        new_purses = split_booty()
        result = [{}, {}, {}]
        self.assertEqual(result, new_purses)

    def test_split_booty_one_given(self):
        purse1 = {"gold_ingots": 3}

        new_purses = split_booty(purse1)
        result = [{"gold_ingots": 1}, {"gold_ingots": 1}, {"gold_ingots": 1}]
        self.assertEqual(result, new_purses)

    def test_split_booty_two_given(self):
        purse1 = {"gold_ingots": 2}
        purse2 = {"gold_ingots": 1}

        new_purses = split_booty(purse1, purse2)
        result = [{"gold_ingots": 1}, {"gold_ingots": 1}, {"gold_ingots": 1}]
        self.assertEqual(result, new_purses)

    def test_split_booty_four_given(self):
        purse1 = {"gold_ingots": 2}
        purse2 = {"gold_ingots": 1}
        purse3 = {"apples": 10}
        purse4 = {"gold_ingots": 1}

        new_purses = split_booty(purse1, purse2, purse3, purse4)
        result = [{"gold_ingots": 2}, {"gold_ingots": 1}, {"gold_ingots": 1}]
        self.assertEqual(result, new_purses)

    def test_split_booty_five_given(self):
        purse1 = {"gold_ingots": 2}
        purse2 = {"gold_ingots": 1}
        purse3 = {"apples": 10}
        purse4 = {"gold_ingots": 1}
        purse5 = {"gold_ingots": 2}

        new_purses = split_booty(purse1, purse2, purse3, purse4, purse5)
        result = [{"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 2}]
        self.assertEqual(result, new_purses)

    def test_split_booty_negative_ingots(self):
        purse1 = {"gold_ingots": -3}
        purse2 = {"gold_ingots": 2}
        purse3 = {"apples": 10}

        with self.assertRaises(ValueError):
            split_booty(purse1, purse2, purse3)

    def test_split_booty_less(self):
        purse1 = {"gold_ingots": 1}
        purse2 = {"gold_ingots": 0}
        purse3 = {"apples": 10}

        new_purses = split_booty(purse1, purse2, purse3)
        result = [{"gold_ingots": 1}, {}, {}]
        self.assertEqual(result, new_purses)


if __name__ == "__main__":
    unittest.main()
