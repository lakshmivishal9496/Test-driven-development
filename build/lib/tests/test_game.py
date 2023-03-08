"""Test the game class."""

import unittest
from dice import Dice
from dicehand import Dicehand
from player import Player
from game import Game


class TestGame(unittest.TestCase):
    """Test the game class."""

    def setUp(self):
        """Set up the game class."""
        self.dice = Dice(6)
        self.player1 = Player("p1", 0)
        self.player2 = Player("p2", 0)
        self.dicehand1 = Dicehand(self.player1, self.dice)
        self.dicehand2 = Dicehand(self.player2, self.dice)
        self.game = Game(self.dicehand1, self.dicehand2)

    def test__init__(self):
        self.assertIsInstance(self.game, Game)
        dicehand_one = Dicehand(self.player1, self.dice)
        self.assertTrue(self.dicehand1, dicehand_one)
        dicehand_two = Dicehand(self.player1, self.dice)
        self.assertTrue(self.dicehand1, dicehand_two)

    def test_current_turn(self):
        """Test the current turn."""
        self.assertEqual(self.game.current_turn(), self.dicehand1)

    def test_start_next_turn(self):
        """Test the start next turn."""
        self.game.start_next_turn()
        self.assertEqual(self.game.current_turn(), self.dicehand2)
        self.game.start_next_turn()
        self.assertEqual(self.game.current_turn(), self.dicehand1)

    def test_is_over(self):
        """Test the is over method."""
        self.assertEqual(self.game.is_over, False)

    def test_cheat_end_game(self):
        self.assertEqual(self.game.is_over, False)
        self.dicehand1.which_players_turn().set_total_score(100)
        self.game.is_over = True
        self.assertEqual(self.game.is_over, True)


if __name__ == '__main__':
    unittest.main()
