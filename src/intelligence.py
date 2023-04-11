import dicehand
import random


class intelligence(dicehand.dicehand):
    def __init__(self, player1, dice1) -> None:
        super().__init__(player1, dice1)

    def play(self):
        mylist = ["roll", "hold", "roll", "roll"]
        chosen = random.choice(mylist)
        return chosen

    def computer_play(self):
        p3 = self.which_players_turn()
        print(f"It's {p3.get_name()} turn")
        while self.turn_over is not True and p3.has_won is False:
            if self.play() == "roll":
                print("Computer Choose to play")
                roll = self.roll()
                print(f"{p3.get_name()} rolled {roll}")
                print(f"{p3} turn score is {self.get_score()}")
            elif self.play() == "hold":
                print("Computer choose to hold")
                self.end_turn()
                print(p3)

    def __str__(self) -> str:
        return super().__str__()
