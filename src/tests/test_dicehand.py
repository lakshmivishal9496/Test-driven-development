"""Test the dicehand class."""

import unittest
from unittest.mock import patch
from dice import Dice
from player import Player
from dicehand import Dicehand


class TestDicehand(unittest.TestCase):
    """This class represents the test dicehand class."""
    def setUp(self):
        """Set up the test dicehand class."""
        self.player1 = Player("player1", 0)
        self.dice1 = Dice(6)
        self.dicehand = Dicehand(self.player1, self.dice1)

    def test_init(self):
        """Test the init method."""
        self.assertEqual(self.dicehand.player1, self.player1)
        self.assertEqual(self.dicehand.dice1, self.dice1)
        self.assertEqual(self.dicehand.score, 0)
        self.assertFalse(self.dicehand.turn_over)

    def test_set_score(self):
        """Test the set score method."""
        self.dicehand.set_score(100)
        self.assertEqual(self.dicehand.score, 100)

    def test_get_score(self):
        """Test the get score method."""
        self.dicehand.set_score(5)
        result = self.dicehand.get_score()
        self.assertEqual(result, 5)

    def test_roll_gamechanger(self):
        """Test the roll method."""
        with patch('random.randint', return_value=1):
            result = self.dicehand.roll()
        self.assertEqual(result, 1)
        self.assertEqual(self.dicehand.score, 0)
        self.assertTrue(self.dicehand.turn_over)

    def test_roll_non_gamechanger(self):
        """Test the roll method."""
        with patch('random.randint', return_value=4):
            result = self.dicehand.roll()
        self.assertEqual(result, 4)
        self.assertEqual(self.dicehand.score, 4)
        self.assertFalse(self.dicehand.turn_over)

    def test_get_turn_over(self):
        """Test the get turn over method."""
        result = self.dicehand.get_turn_over()
        self.assertEqual(result, False)

    def test_which_players_turn(self):
        """Test the which players turn method."""
        result = self.dicehand.which_players_turn()
        self.assertEqual(result, self.player1)

    def test_end_turn(self):
        """Test the end turn method."""
        self.dicehand.set_score(5)
        self.player1.set_total_score(10)
        result = self.dicehand.end_turn()
        self.assertEqual(result, 15)
        self.assertTrue(self.dicehand.turn_over)
        self.assertEqual(self.dicehand.score, 0)


if __name__ == '__main__':
    unittest.main()
