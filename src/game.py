"""This module contains the game class and its methods."""

from dice import Dice
from player import Player
from dicehand import Dicehand


class Game:
    """This class represents a game."""

    POINTS_TO_WIN = 100
    dice1 = Dice(6)
    player1 = Player("p1", 0)
    player2 = Player("p2", 0)
    dicehand1 = Dicehand(player1, dice1)
    dicehand2 = Dicehand(player2, dice1)

    def __init__(self, dicehand1, dicehand2):
        """Initialize the game."""
        self.dicehand1 = dicehand1
        self.dicehand2 = dicehand2
        self.current = dicehand1
        self.is_over = False

    def current_turn(self):
        """Get the current turn."""
        return self.current

    def start_next_turn(self):
        """Start the next turn."""
        if self.current == self.dicehand1:
            self.current = self.dicehand2
            self.current.turn_over = False
        else:
            self.current = self.dicehand1
            self.current.turn_over = False

    def is_over(self):
        """Check if the game is over."""
        return self.is_over

    def cheat_and_endgame(self):
        """Cheat and end the game."""
        if self.current_turn() == self.dicehand1:
            self.dicehand1.which_players_turn().set_total_score(100)
            self.is_over = True
        else:
            self.dicehand2.which_players_turn().set_total_score(100)
            self.is_over = True

    def player_play(self):
        """Player play."""
        target = Game.POINTS_TO_WIN
        while self.current_turn().turn_over is not True:
            p1 = self.current_turn().which_players_turn()
            print(f"\nIt's {p1.get_name()} turn")
            user_inp = input("(help) roll/hold: ").lower()

            inputs = ["roll", "hold", "help"]
            while user_inp not in inputs:  # check if input is valid
                print("Invalid input, try again (help), (roll), (hold)")
                user_inp = input("(help) roll/hold: ").lower()

            if user_inp == "roll":
                print(f"\n{p1.get_name()} rolling dice......")
                print(f"{p1.get_name()} rolled {self.current_turn().roll()}")
                print(
                    f"\n{p1} turn score is: \
{self.current_turn().get_score()}\n"
                )
            elif user_inp == "hold":
                print(f"{p1.get_name()} choose to hold")
                self.current_turn().end_turn()
                print(p1)
                print()
            else:
                cheater = input("Cheat(x) or Change name(n): ").lower()
                valid_cheat = ["x", "n"]
                while cheater not in valid_cheat:
                    print("Invalid input, try again (x), (n)")
                    cheater = input("Cheat(x) or Change name(n): ").lower()

                if cheater == "x":
                    self.cheat_and_endgame()
                    print(p1)
                    self.current_turn().turn_over = True

                elif cheater == "n":
                    new_name = input("Enter your new name: ")
                    self.current_turn().which_players_turn().set_name(new_name)
            contestant = self.current_turn().which_players_turn()
            if contestant.get_total_score() >= target:
                self.current_turn().which_players_turn().has_won = True
                print(
                    f'{self.current_turn().which_players_turn().get_name()} \
is winner'
                    )
                self.is_over = True
                break
