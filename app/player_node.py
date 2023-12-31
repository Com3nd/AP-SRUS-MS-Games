from player import Player
from typing import Optional


class PlayerNode:
    """A node for the player to occupy or use to traverse"""

    def __init__(self, player: Optional[Player] = None):
        self._player = player
        self._next_node: Optional[PlayerNode] = None
        self._prev_node: Optional[PlayerNode] = None

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        self._next_node = value

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, value):
        self._prev_node = value

    @property
    def key(self):
        return self.player.uid

    def __repr__(self):
        return f"{self.player.name}"

    def __str__(self):
        return f"{self._player.name}"
