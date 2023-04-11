import unittest
from src import player


class test_dice(unittest.TestCase):
    def setUp(self) -> None:
        self.player1 = player.player("Mercy", 0)
        return self.player1

    # testing whether player instance belongs to player class
    def test_init_(self):
        self.assertIsInstance(self.player1, player.player)

    def test_set_name(self):
        # test case 2
        # The “TypeError: ‘str’ object is not callable”
        # error is raised when you try to call a string as a function.
        # Attribute setter decorator must be used in such a way:
        # objectname.readonlyattribute = newvalue
        # attempting to set attribute using set_name() method
        # will raise type error.
        with self.assertRaises(TypeError):
            self.player1.set_name("Antony")
            # Correct way of using setter to access private attribute
            # p1.name = "Antony"
            # print(p1.name)

    def test_get_name(self):
        # test whether type of object p1 is reference type player
        self.player1.name = "antony"
        self.assertEqual(type(self.player1), player.player)
        # p1.name must be string,
        # test case to check whether p1 is int/float; it is not true
        self.assertNotEqual(type(self.player1.name), int)
        self.assertNotEqual(type(self.player1.name), float)

    def test_get_total_score(self):
        # test case to check whether get_total_score returns
        # score of type int correctly, cross checking whether
        # score in the dictionary's value matches with value method returns.
        # player name is key and its value is their scores in dictionary
        self.assertIn(self.player1.get_total_score(),
                      player.player.player_info.values())

    def test_set_total_score(self):
        # Test case to check whether set method doesn't return anything
        # mutator will not return anything it modifies or sets value
        self.assertIsNone(self.player1.set_total_score(0), None)


if __name__ == '__main__':
    unittest.main()
