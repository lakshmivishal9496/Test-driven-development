import unittest
from src import dice


class test_dice(unittest.TestCase):
    # testing whether dice instance belongs to dice class
    def test_init_(self):
        dice_testing = dice.dice(6)
        self.assertIsInstance(dice_testing, dice.dice)
        # test case to check whether int parameter is passed to instance
        with self.assertRaises(TypeError):
            dice.dice("six").roll_dice()

    def test_roll_dice(self):
        # As we are playing with single six sided dice
        # probability of throwing dice may result in 1,2,3,4,5,6
        # roll_dice can never result value less than 1 or greater than 6
        dice_testing = dice.dice(6)
        if dice_testing.roll_dice() > 6 | dice_testing.roll_dice() < 1:
            self.assertRaises(ValueError)


if __name__ == '__main__':
    unittest.main()
