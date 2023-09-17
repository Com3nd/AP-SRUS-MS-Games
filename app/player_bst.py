from __future__ import annotations
from player import Player
from typing import Optional
from player_bnode import PlayerBNode


class NoRootNodeError(Exception):
    def __init__(self, message="The binary search tree has no root node."):
        super().__init__(message)


class PlayerBST:
    def __init__(self, node: Optional[PlayerBNode] = None):
        self.root: Optional[PlayerBST] = node
        self.node: Optional[PlayerBNode] = None

    # @property
    # def root(self):
    #     return self.root

    def traverse(self, player: Player, tree: Optional[PlayerBST] = None) -> tuple[PlayerBST, str]:
        if tree is None:
            tree = self

        root: PlayerBNode = tree.root  # type: ignore

        if root is None:
            raise NoRootNodeError

        if player.name > root.player.name:
            if root.right:
                return self.traverse(player, root.right)
            else:
                return tree, "Right"
        else:
            if root.left:
                return self.traverse(player, root.left)
            else:
                return tree, "Left"

    def insert(self, player: Player):
        tree: PlayerBST = self.traverse(player)[0]
        direction: str = self.traverse(player)[1]
        if direction == "Right":
            tree.root.right = PlayerBST(PlayerBNode(player))

        if direction == "Left":
            tree.root.left = PlayerBST(PlayerBNode(player))
