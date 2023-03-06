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
        self.dicehand1.which_players_turn().set_total_score(100)
        
            
            

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
