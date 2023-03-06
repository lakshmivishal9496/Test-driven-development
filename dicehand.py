import dice
import player


class dicehand:
    player1 = player.player("player1", 0)
    player2 = player.player("player2", 0)
    dice1 = dice.dice(6)
    gamechanger = 1
    player_list = []

    def __init__(self, player1, dice1) -> None:
        self.player1 = player1
        self.dice1 = dice1
        self.score = 0
        self.turn_over = False
        dicehand.player_list.append(self)

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def roll(self):
        roll = dicehand.dice1.roll_dice()
        if roll == dicehand.gamechanger:
            self.set_score(0)
            self.turn_over = True
        else:
            self.score += roll
        return roll

    def get_turn_over(self):
        return self.turn_over

    def which_players_turn(self):
        return self.player1

    def __str__(self) -> str:
        return f'{self.player1} and {self.dice1}'

    def end_turn(self):
        # player object's total score is incremented
        # by turn score when he want to hold ie endturn
        # with points he/she scored.
        p = self.player1.get_total_score() + self.get_score()
        self.player1.set_total_score(p)
        self.turn_over = True
        self.set_score(0)
        return p


'''
p1 = player.player("p1", 0)
p2 = player.player("p2", 0)
d1 = dicehand(p1, dice.dice(6))
d2 = dicehand(p2, dice.dice(6))
while d1.turn_over is False and d1.get_score() <= dicehand.TARGET:
    print(d2.which_players_turn())
    print(f"{p1.get_name()} rolled {d1.roll()}")
    print(f"{p1} turn score is {d1.get_score()}")
    print(p1.get_total_score())


while d2.turn_over is False and d2.get_score() <= dicehand.TARGET:
    print(d2.which_players_turn())
    print(f"{p2.get_name()} rolled {d2.roll()}")
    print(f"{p2} turn score is {d2.get_score()}")
    print(p2.get_total_score())
'''
