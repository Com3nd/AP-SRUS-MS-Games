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

    def test_insert_right_leaf_node(self):
        self.bst.insert(Player("02", "player_2"))
        self.bst.insert(Player("03", "player_3"))
        self.bst.insert(Player("04", "player_4"))
        self.bst.insert(Player("05", "player_5"))

        player_five = self.bst.root.right.right.right.player
        self.assertEqual(player_five.name, Player("05", "player_5").name)

    def test_insert_leaf_node(self):
        self.bst.insert(Player("09", "player_9"))
        self.bst.insert(Player("03", "player_3"))
        self.bst.insert(Player("04", "player_4"))
        self.bst.insert(Player("05", "player_5"))

        player_five = self.bst.root.left.right.right.player
        self.assertEqual(player_five.name, Player("05", "player_5").name)
