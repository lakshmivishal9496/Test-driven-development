import random


class dice:
    def __init__(self, dice):
        self.__dice = dice

    def roll_dice(self):
        return random.randint(1, self.__dice)
