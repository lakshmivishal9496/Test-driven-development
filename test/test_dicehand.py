import unittest
from src import dice, dicehand, player
import sys
sys.path.append(r'C:\Users\laksh\Dice_Game')


class test_dicehand(unittest.TestCase):
    def setUp(self) -> None:
        self.d = dicehand.dicehand(player.player("abc", 0), dice.dice(6))
        self.p = player.player("abc", 0)
        return self.d

    # testing whether dicehand instance belongs to dicehand class
    def test_init_(self):
        self.assertIsInstance(self.d, dicehand.dicehand)

    def test_set_score(self):
        # set_score will not return anything
        self.assertIs(self.d.set_score(0), None)

    def test_get_score(self):
        # rolling a dice adds the dice side value to score
        # calling get_score method and checking whether its working as intended
        # whether it's returning an int value (Condition is true)
        self.d.start_rolling()
        self.assertIsInstance(self.d.get_score(), int)

    def test_get_turn_over(self):
        # this method is intended to return boolean
        self.assertIsInstance(self.d.get_turn_over(), bool)

    def test_which_players_turn(self):
        # this method is supposed to return
        # player object whose turn is to roll a dice
        self.assertIsInstance(self.d.which_players_turn(), player.player)

    def test_end_turn(self):
        # indent of method add turn score to total score
        # testing whether it's working as indented
        # get_score() returns default value zero before endturn() is called
        # end turn sets the total score + turn score using set_score
        # next time when we try to access get_score()
        # value will be value set by mutator of dicehand class
        # that value must be returned
        self.assertEqual(self.d.end_turn(), self.d.get_score())

    def test_start_rolling(self):
        # roll = self.d.start_rolling()
        # this method returns random integer between 1 to 6
        # if a player throws 1(game changer) he lost the game
        # manually setting roll_expected to 1 to check whether test passes
        roll_expected = 1
        expected_score = 0
        if self.assertEqual(dicehand.dicehand.gamechanger, roll_expected):
            self.assertEquals(self.d.score, expected_score)


if __name__ == '__main__':
    unittest.main()
