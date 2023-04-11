import dice
import player
import dicehand


class game:
    POINTS_TO_WIN = 10
    dice1 = dice.dice(6)
    player1 = player.player("p1", 0)
    player2 = player.player("p2", 0)
    dicehand1 = dicehand.dicehand(player1, dice1)
    dicehand2 = dicehand.dicehand(player2, dice1)

    def __init__(self, dicehand1, dicehand2) -> None:
        self.dicehand1 = dicehand1
        self.dicehand2 = dicehand2
        self.current = dicehand1
        self.is_over = False

    def current_turn(self):
        return self.current

    def start_next_turn(self):
        if self.current == self.dicehand1:
            self.current = self.dicehand2
            self.current.turn_over = False
        else:
            self.current = self.dicehand1
            self.current.turn_over = False

    def is_over(self):
        return self.is_over

    def cheat(self):
        # self.dicehand1.which_players_turn().set_total_score(100)
        highest_turn_score = 5
        if self.dicehand1.get_score() >= highest_turn_score:
            print("I want to hold this turn points...")
            self.dicehand1.end_turn()
            print(self.dicehand1.which_players_turn())
        elif self.dicehand2.get_score() >= highest_turn_score:
            print("I want to hold this turn points...")
            self.dicehand2.end_turn()
            print(self.dicehand2.which_players_turn())

    def player_play(self):
        while self.current_turn().turn_over is not True:
            p1 = self.current_turn().which_players_turn()
            print(f"It's {p1.get_name()} turn")
            user_inp = input("(help) roll/hold: ")
            if user_inp == "roll":
                print("You choose to play")
                print(f"{p1.get_name()} rolled {self.current_turn().roll()}")
                print(f"{p1} turn score is {self.current_turn().get_score()}")
            elif user_inp == "hold":
                print("You choose to hold")
                self.current_turn().end_turn()
                print(p1)
            else:
                cheater = input("Cheat(x) or Change name(n): ").lower()
                if cheater == "x":
                    self.cheat()
                    self.is_over = True
                    break

                elif cheater == "n":
                    new_name = input("Enter your new name: ")
                    self.current_turn().which_players_turn().set_name(new_name)
            if self.current_turn().which_players_turn().get_total_score() >= game.POINTS_TO_WIN:
                self.current_turn().which_players_turn().has_won = True
                print(f'{self.current_turn().which_players_turn().get_name()} \
is winner')
                self.is_over = True
                break

    def __str__(self) -> str:
        return f'{self.player1} has scored {game.POINTS_TO_WIN}'


'''
dice1 = dice.dice(6)
player1 = player.player("Samy", 0)
player2 = player.player("tomy", 0)
game1 = game(player1, player2)
print(game1.current_player())
game1.start_next_turn()
print(game1.current_player())
game1.start_next_turn()
'''
