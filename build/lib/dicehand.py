"""This module contains the dicehand class and its methods."""

from dice import Dice
from player import Player


class Dicehand:
    """This class represents a dicehand."""

    player1 = Player("player1", 0)
    player2 = Player("player2", 0)
    dice1 = Dice(6)
    gamechanger = 1

    def __init__(self, player1, dice1):
        """Initialize the dicehand."""
        self.player1 = player1
        self.dice1 = dice1
        self.score = 0
        self.turn_over = False

    def set_score(self, score):
        """Set the score."""
        self.score = score

    def get_score(self):
        """Get the score."""
        return self.score

    def roll(self):
        """Roll the dice."""
        roll = Dicehand.dice1.roll_dice()
        if roll == Dicehand.gamechanger:
            self.set_score(0)
            self.turn_over = True
        else:
            self.score += roll
        return roll

    def get_turn_over(self):
        """Get the turn_over."""
        return self.turn_over

    def which_players_turn(self):
        """Get the player."""
        return self.player1

    def __str__(self):
        """Return the string representation of the dicehand."""
        return f"{self.player1} and {self.dice1}"

    def end_turn(self):
        """End the turn."""
        # player object's total score is incremented
        # by turn score when he want to hold ie endturn
        # with points he/she scored.
        p = self.player1.get_total_score() + self.get_score()
        self.player1.set_total_score(p)
        self.turn_over = True
        self.set_score(0)
        return p
