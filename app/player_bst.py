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

    def _insert(self, player: Player,
                current_node: Optional[PlayerBNode] = None) -> tuple[PlayerBNode, str]:
        """A helper method to insert the tree"""

        if current_node is None:
            current_node = self.root

        if current_node is None:
            raise NoRootNodeError

        if player.name > current_node.player.name:
            if current_node.right and player.name > current_node.right.player.name:
                return self._insert(player, current_node.right)
            else:
                return current_node, "Right"
        else:
            if current_node.left and player.name < current_node.left.player.name:
                return self._insert(player, current_node.left)
            else:
                return current_node, "Left"

    def insert(self, player: Player):
        node, direction = self._insert(player)
        post_nodes: Optional[list[PlayerBNode]] = None

        if direction == "Right":
            if node.right is not None:
                post_nodes = node.right.inorder_traversal()
                node.right = PlayerBNode(player)
                for player_node in post_nodes:
                    self.insert(player_node.player)
            else:
                node.right = PlayerBNode(player)

        if direction == "Left":
            if node.left is not None:
                post_nodes = node.right.inorder_traversal()
                node.left = PlayerBNode(player)
                for player_node in post_nodes:
                    self.insert(player_node.player)
            else:
                node.right = PlayerBNode(player)


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
