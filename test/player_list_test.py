import unittest
from player_list import PlayerList
from player import Player
from player_node import PlayerNode


class TestPlayerList(unittest.TestCase):
    def setUp(self) -> None:
        self.player_list = PlayerList()
        self.mustafa = Player("01", "Mustafa")

    def test_empty_player_list(self):
        self.assertIs(self.player_list.is_empty(), True)

    def test_add_node_to_list(self):
        self.player_list.add_node(PlayerNode())
        self.assertIs(self.player_list.is_empty(), False)

    def test_add_tail_to_list(self):



if __name__ == "__main__":
    unittest.main()
