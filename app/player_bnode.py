from player import Player
from typing import Optional


class PlayerBNode:

    def __init__(self, player: Player):
        self._player: Player = player
        self._right: Optional['PlayerBST'] = None  # type: ignore # Right is greater than
        self._left: Optional['PlayerBST'] = None  # type: ignore # Left is greater than

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
