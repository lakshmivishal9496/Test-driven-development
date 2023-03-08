"""This module contains the intelligence class for the game of pig."""

import random
from dicehand import Dicehand


class Intelligence(Dicehand):
    """This class represents the intelligence of the game."""
    def __init__(self, player1, dice1):
        super().__init__(player1, dice1)

    def play(self):
        """Choose to play or hold."""
        mylist = ["roll", "hold", "roll", "roll"]
        chosen = random.choice(mylist)
        return chosen

    def computer_play(self):
        """Computer play."""
        p3 = self.which_players_turn()
        print(f"It's {p3.get_name()} turn")
        while self.turn_over is not True and p3.has_won is False:
            if self.play() == "roll":
                print("\nComputer rolling dice...")
                roll = self.roll()
                print(f"{p3.get_name()} rolled {roll}")
                print(f"\n{p3} turn score is: {self.get_score()}")
            elif self.play() == "hold":
                print("Computer choose to hold")
                self.end_turn()
                print(p3)
                print()

    def __str__(self):
        """Return the string representation of the intelligence."""
        return super().__str__()
