import game
import dice
import dicehand
import player
import intelligence


def main():
    game_type1 = input("Press p for player vs \
player:/ press c for player vs computer: ")
    if game_type1 == "p" or game_type1 == "P":
        p_vs_p()
    elif game_type1 == "c" or game_type1 == "C":
        p_vs_c()


def p_vs_c():
    target = game.game.POINTS_TO_WIN
    choose_name = input("Enter Your name: ")
    player1 = player.player("", 0)
    player1.set_name(choose_name)
    player3 = player.player("computer", 0)
    dice1 = dice.dice(6)
    dicehand1 = dicehand.dicehand(player1, dice1)
    dicehand3 = intelligence.intelligence(player3, dice1)
    game1 = game.game(dicehand1, dicehand3)
    while game1.is_over is not True:
        while dicehand1.turn_over is not True:
            game1.player_play()
            if dicehand1.turn_over is True:
                game1.start_next_turn()
        while dicehand3.turn_over is not True and dicehand1.which_players_turn().has_won is False:
            dicehand3.computer_play()
            if dicehand3.turn_over is True:
                game1.start_next_turn()
            if dicehand3.which_players_turn().get_total_score() >= target:
                dicehand3.which_players_turn().has_won = True
                print(f'{dicehand3.which_players_turn().get_name()} is winner')
                game1.is_over = True
                break


def p_vs_p():
    choose_name_p1 = input("Enter name (player_1): ")
    player1 = player.player("", 0)
    player1.set_name(choose_name_p1)
    choose_name_p2 = input("Enter name (player_2): ")
    player2 = player.player("", 0)
    player2.set_name(choose_name_p2)
    dice1 = dice.dice(6)
    dicehand1 = dicehand.dicehand(player1, dice1)
    dicehand2 = intelligence.intelligence(player2, dice1)
    game1 = game.game(dicehand1, dicehand2)
    while game1.is_over is not True:
        while dicehand1.turn_over is not True:
            game1.player_play()
            if dicehand1.turn_over is True and dicehand2.which_players_turn().has_won is False:
                game1.start_next_turn()

        while dicehand2.turn_over is not True and dicehand1.which_players_turn().has_won is False:
            game1.player_play()
            if game1.current_turn().turn_over is True:
                game1.start_next_turn()


main()
