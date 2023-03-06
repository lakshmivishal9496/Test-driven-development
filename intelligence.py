import dicehand
import random


class intelligence(dicehand.dicehand):
    def __init__(self, player1, dice1) -> None:
        super().__init__(player1, dice1)

    def play(self):
        mylist = ["roll", "hold", "roll", "roll"]
        chosen = random.choice(mylist)
        return chosen
