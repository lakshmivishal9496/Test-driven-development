"""This module contains the dice class."""
import random


class Dice:
    """This class represents a dice."""

    def __init__(self, dice):
        """Initialize the dice."""
        self.dice = dice

    def roll_dice(self):
        """Roll the dice."""
        return random.randint(1, self.dice)
