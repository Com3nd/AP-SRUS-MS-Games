import unittest
from player_bst import PlayerBST
from player import Player


class TestPlayerBST(unittest.TestCase):

    def setUp(self) -> None:
        self.bst = PlayerBST()

    def test_insert_root(self):
        self.bst.insert(Player("02", "player_2"))
        self.bst.insert(Player("03", "player_3"))

        self.assertEqual(self.bst.root.player, Player("02", "player_2"))
