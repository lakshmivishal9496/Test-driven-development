"""This module contains the player class and its methods."""


class Player:
    """This class represents a player."""

    def __init__(self, name, score):
        """Initialize the player."""
        self.name = name
        self.score = score

        self.has_won = False

    def get_name(self):
        """Get the name."""
        return self.name

    def get_winner(self):
        """Get the winner."""
        return self.has_won

    def set_name(self, name):
        """Set the name."""
        self.name = name

    def __str__(self):
        """Return the string representation of the player."""
        return f"The player is {self.name}\n\
Total score is: {self.score}"

    def set_total_score(self, score):
        """Set the total score."""
        self.score = score

    def get_total_score(self):
        """Get the total score."""
        return self.score
