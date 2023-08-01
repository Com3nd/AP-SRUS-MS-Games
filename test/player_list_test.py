import unittest
from player_list import PlayerList


class TestPlayerList(unittest.TestCase):
    def setUp(self) -> None:
        self.player_list = PlayerList()
        # player_list.add_node("01", "Mustafa")
        # player_list.add_node("02", "Melissa")
        # player_list.add_node("03", "Jonghun")
        # player_list.add_node("04", "raf")

    def test_empty_player_list(self):
        self.assertIs(self.player_list.is_empty(), True)

    def test_adding_node_to_list(self):
        self.player_list.add_node("01", "Mustafa")
        self.assertIs(self.player_list.is_empty(), False)


if __name__ == "__main__":
    unittest.main()
