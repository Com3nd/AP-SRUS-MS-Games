from __future__ import annotations
from player import Player
from player import Player
from typing import Optional
from player_bnode import PlayerBNode


class NoRootNodeError(Exception):
    def __init__(self, message="The binary search tree has no root node."):
        super().__init__(message)


class PlayerBST:
    def __init__(self, node: Optional[PlayerBNode] = None):
        self._root: Optional[PlayerBNode] = node

    @property
    def root(self):
        return self._root

    def _insert(self, player: Player,
                current_node: Optional[PlayerBNode] = None) -> tuple[PlayerBNode, str]:
        """A helper method to traverse the tree"""

        if self.root is None:
            self._root = PlayerBNode(player)

        if current_node is None:
            current_node = self.root

        if player.name == current_node.player.name:
            return current_node, "equal"

        if player.name >= current_node.player.name:
            if current_node.right:
                return self._insert(player, current_node.right)
            else:
                return current_node, "Right"
        else:
            if current_node.left:
                return self._insert(player, current_node.left)
            else:
                return current_node, "Left"

    def insert(self, player: Player):
        node, result = self._insert(player)

        if result == "Right":
            node.right = PlayerBNode(player)

        if result == "Left":
            node.left = PlayerBNode(player)

        if result == "equal":
            node.player = player


if __name__ == "__main__":
    bst = PlayerBST()
    bst.insert(Player("02", "player_2"))
    print(bst.root.player.uid)
    bst.insert(Player("03", "player_3"))
    bst.insert(Player("04", "player_4"))
    bst.insert(Player("05", "player_5"))
    bst.insert(Player("01", "player_1"))
    bst.insert(Player("08", "player_8"))
    bst.insert(Player("07", "player_7"))
    bst.insert(Player("04", "player_2"))
    print(bst.root.player.uid)
