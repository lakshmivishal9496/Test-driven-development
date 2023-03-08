"""This module contains the test dice class."""

import unittest
from unittest.mock import patch
from dice import Dice


class TestDice(unittest.TestCase):
    """This class represents the test dice class."""
    def setUp(self):
        """Set up the test dice class."""
        self.dice = Dice(6)

    def test_init(self):
        """Test the init method."""
        self.assertIsInstance(self.dice, Dice)

    def test_roll_dice_(self):
        """Test the roll dice method."""
        dice = Dice(6)
        self.assertTrue(dice.roll_dice() in range(1, 7))
        self.assertIsInstance(dice.roll_dice(), int)
        self.assertNotEqual(dice.roll_dice(), 0)

    def test_roll_dice_1(self):
        """Test the roll dice method."""
        dice = Dice(6)
        with patch('random.randint', return_value=1):
            result = dice.roll_dice()
        self.assertEqual(result, 1)

    def test_roll_dice_2(self):
        with patch('random.randint', return_value=2):
            result = self.dice.roll_dice()
        self.assertEqual(result, 2)

    def test_roll_dice_3(self):
        with patch('random.randint', return_value=3):
            result = self.dice.roll_dice()
        self.assertEqual(result, 3)

    def test_roll_dice_4(self):
        """Test the roll dice method."""
        dice = Dice(6)
        with patch('random.randint', return_value=4):
            result = dice.roll_dice()
        self.assertEqual(result, 4)

    def test_roll_dice_5(self):
        with patch('random.randint', return_value=5):
            result = self.dice.roll_dice()
        self.assertEqual(result, 5)

    def test_roll_dice_6(self):
        with patch('random.randint', return_value=6):
            result = self.dice.roll_dice()
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
