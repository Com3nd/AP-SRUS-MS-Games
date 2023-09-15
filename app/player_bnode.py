from player import Player
from player_bst import PlayerBST


class PlayerBNode:

    def __init__(self, player: Player):
        self._player: Player = player
        self._right: int = None  # Right is less than
        self._left: int = None  # Left is greater

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
