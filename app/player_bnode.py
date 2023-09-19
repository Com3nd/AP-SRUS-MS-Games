from player import Player
from typing import Optional


class PlayerBNode:

    def __init__(self, player: Player):
        self._player: Player = player
        self._right: Optional[PlayerBNode] = None  # Right is greater than
        self._left: Optional[PlayerBNode] = None  # Left is greater than

    @property
    def player(self):
        return self._player

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    def inorder_traversal(self, result: Optional[list['PlayerBNode']] = None) -> list['PlayerBNode']:
        if result is None:
            result = []

        if self.left:
            self.left.inorder_traversal()

        result.append(self)

        if self.right:
            self.right.inorder_traversal()

        return result

    def __str__(self):
        return f"{self.player.name}"
