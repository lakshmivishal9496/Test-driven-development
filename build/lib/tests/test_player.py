"""This module contains the player class and its methods."""

import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    """This class represents the test player class."""
    def setUp(self):
        """Set up the test player class."""
        self.player = Player("Abshir", 0)

    def test_init(self):
        """Test the init method."""
        player = self.player

        # Test if the player is an instance of Player
        self.assertIsInstance(player, Player)

    def test_get_name(self):
        """Test the get_name method."""
        # Test that the get_name method returns the correct name
        self.assertEqual(self.player.get_name(), "Abshir")

    def test_get_winner(self):
        """Test the get_winner method."""
        # Test that the get_winner method returns the correct winner
        self.assertEqual(self.player.get_winner(), False)

    def test_set_name(self):
        """Test the set_name method."""
        # Test that the set_name method sets the correct name
        self.player.set_name("Lakshmi")
        self.assertEqual(self.player.get_name(), "Lakshmi")


if __name__ == '__main__':
    unittest.main()
