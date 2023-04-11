class player:
    player_info = {}

    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score

        self.has_won = False

    def get_name(self):
        return self.name

    def get_winner(self):
        return self.has_won

    def set_name(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"The name of player is {self.name}\
 their total score is {self.score}"

    def set_total_score(self, score):
        self.score = score

    def get_total_score(self):
        return self.score


# name change of player outside the class
# player1 = player("khan", 100)
# player2 = player("Pathan", 80)
# print(player1)
# player1.name = "Tom"
# print(player1.name)
# print(player.player_info.items())
