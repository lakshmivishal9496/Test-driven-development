import game
import dice
import dicehand
import player
import intelligence


def main():
    game_type1 = input("Press p for player vs player:/ press c for player vs computer: ")
    if game_type1 == "p" or game_type1 == "P":
        p_vs_p()
    elif game_type1 == "c" or game_type1 == "C":
        p_vs_c()


def p_vs_c():
    choose_name = input("Enter Your name: ")
    player1 = player.player("", 0)
    player1.set_name(choose_name)
    player3 = player.player("computer", 0)
    dice1 = dice.dice(6)
    dicehand1 = dicehand.dicehand(player1, dice1)
    dicehand3 = intelligence.intelligence(player3, dice1)
    game1 = game.game(dicehand1, dicehand3)
    while game1.is_over is not True:
        p3 = dicehand3.which_players_turn()
        while dicehand1.turn_over is not True:
            p1 = dicehand1.which_players_turn()
            print(f"It's {p1.get_name()} turn")
            user_inp = input("(help) roll/hold: ")
            if user_inp == "roll":
                print("You choose to play")
                print(f"{p1.get_name()} rolled {dicehand1.roll()}")
                print(f"{p1} turn score is {dicehand1.get_score()}")
            elif user_inp == "hold":
                print("You choose to hold")
                dicehand1.end_turn()
                print(p1)
            else:
                cheater = input("Cheat(x) or Change name(n): ").lower()
                if cheater == "x":
                    game1.cheat()

                elif cheater == "n":
                    new_name = input("Enter your new name: ")
                    p1.set_name(new_name)
            if dicehand1.turn_over is True and p1.has_won is False:
                game1.start_next_turn()
            if p1.get_total_score() >= 100:
                p1.has_won = True
                print(f'{p1.get_name()} is winner')
                game1.is_over = True
                break
        
        while dicehand3.turn_over is not True and p1.has_won is False:
            # print(f"It's {p3.get_name()} turn")
            if dicehand3.play() == "roll":
                print("Computer Choose to play")
                roll = dicehand3.roll()
                print(f"{p3.get_name()} rolled {roll}")
                print(f"{p3} turn score is {dicehand3.get_score()}")
            elif dicehand3.play() == "hold":
                print("Computer choose to hold")
                dicehand3.end_turn()
                print(p3)
            if dicehand3.turn_over is True:
                game1.start_next_turn()
            if p3.get_total_score() >= 10 and p1.has_won is False:
                p3.has_won = True
                print(f'{p3.get_name()} is winner')
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
            p1 = dicehand1.which_players_turn()
            print(f"It's {p1.get_name()} turn")
            user_inp = input("(help) roll/hold: ")
            if user_inp == "roll":
                print("You choose to play")
                print(f"{p1.get_name()} rolled {dicehand1.roll()}")
                print(f"{p1} turn score is {dicehand1.get_score()}")
            elif user_inp == "hold":
                print("You choose to hold")
                dicehand1.end_turn()
                print(p1)
            else:
                cheater = input("Cheat(x) or Change name(n): ").lower()
                if cheater == "x":
                    game1.cheat()

                elif cheater == "n":
                    new_name = input("Enter your new name: ")
                    p1.set_name(new_name)
            if dicehand1.turn_over is True and p1.has_won is False:
                game1.start_next_turn()
            if p1.get_total_score() >= 100:
                p1.has_won = True
                print(f'{p1.get_name()} is winner')
                game1.is_over = True
                break

        while dicehand2.turn_over is not True and p1.has_won is False:
            p2 = dicehand2.which_players_turn()
            print(f"It's {p2.get_name()} turn")
            user_inp = input("(help) roll/hold: ")
            if user_inp == "roll":
                roll = game1.current_turn().roll()
                print(f"{p2.get_name()} rolled {roll}")
                print(f"{p2} turn score is \
{game1.current_turn().get_score()}")
            elif user_inp == "hold":
                print("You choose to hold")
                game1.current_turn().end_turn()
                game1.start_next_turn()
                print(p2)
            else:
                cheater = input("Cheat(x) or Change name(n): ").lower()
                if cheater == "x":
                    game1.cheat()

                elif cheater == "n":
                    new_name = input("Enter your new name: ")
                    p2.set_name(new_name)
            if game1.current_turn().turn_over is True:
                game1.start_next_turn()
            if p2.get_total_score() >= 10:
                p2.has_won = True
                print(f'{p2.get_name()} is winner')
                game1.is_over = True
                break


main()
