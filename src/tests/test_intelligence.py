"""This module contains the unit tests for the Intelligence class."""

import unittest
from intelligence import Intelligence
from player import Player
from dice import Dice


class TestIntelligence(unittest.TestCase):
    """This class represents the test intelligence class."""
    def setUp(self):
        """Set up the test intelligence class."""
        self.dice = Dice(6)
        self.player = Player("Computer Player", 0)
        self.intelligence = Intelligence(self.player, self.dice)

    def test_init(self):
        """Test the init method."""
        computer = self.intelligence

        # Test if the computer is an instance of Intelligence, Player, and Dice
        self.assertIsInstance(computer, Intelligence)
        self.assertIsInstance(self.player, Player)
        self.assertIsInstance(self.dice, Dice)

    def test_play(self):
        """Test the play method."""

        # Test that the play method returns either "roll" or "hold"
        self.assertIn(self.intelligence.play(), ["roll", "hold"])

    def test_computer_play(self):
        """Test the computer_play method."""
        # Initialize test objects
        dice = Dice(6)
        player = Player("Computer Player", 0)
        computer = Intelligence(player, dice)

        # Test that the computer_play method ends turn after holding
        self.assertEqual(computer.turn_over, False)
        computer.roll()
        computer.end_turn()
        self.assertEqual(computer.turn_over, True)


if __name__ == '__main__':
    unittest.main()
