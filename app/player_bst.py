from __future__ import annotations
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

    def traverse(self, player: Player,
                 current_node: Optional[PlayerBNode] = None) -> tuple[PlayerBNode, str]:
        """A helper method to traverse the tree"""

        if current_node is None:
            current_node = self.root

        if current_node is None:
            raise NoRootNodeError

        if player.name > current_node.player.name:
            if current_node.right:
                return self.traverse(player, current_node.right)
            else:
                return current_node, "Right"
        else:
            if current_node.left:
                return self.traverse(player, current_node.left)
            else:
                return current_node, "Left"

    def insert(self, player: Player):
        node, direction = self.traverse(player)

        if direction == "Right":
            node.right = PlayerBNode(player)

        if direction == "Left":
            node.left = PlayerBNode(player)


if __name__ == "__main__":
    bst = PlayerBST(PlayerBNode(Player("02", "player_2")))
    bst.insert(Player("03", "player_3"))
    bst.insert(Player("04", "player_4"))
    bst.insert(Player("05", "player_5"))
    bst.insert(Player("01", "player_1"))
    bst.insert(Player("08", "player_8"))
    bst.insert(Player("07", "player_7"))
    print()
    print()
