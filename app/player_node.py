from player import Player
from typing import Optional


class PlayerNode:
    """A node for the player to occupy or use to traverse"""
    
    def __init__(self, player: Optional[Player] = None):
        self._player = player
        self._next_node: Optional[PlayerNode] = None
        self._prev_node: Optional[PlayerNode] = None
        self._key: Optional[str] = None

    @property
    def player(self):
        return self._player

    @property
    def next_node(self):
        return self._next_node

    @property
    def prev_node(self):
        return self._prev_node

    @player.setter
    def player(self, value):
        self._player = value
        # Set the value of the 'key' to the player's 'uid'
        # when a player to set for the 'player' property
        if isinstance(value, Player):
            self._key = self._player.uid

    @next_node.setter
    def next_node(self, value):
        self._next_node = value

    @prev_node.setter
    def prev_node(self, value):
        self._prev_node = value

    @property
    def key(self):
        return self.player.uid

    def __str__(self):
        if isinstance(self._player, Player):
            return f"{self._player.name}"

    def __repr__(self):
        if isinstance(self._player, Player):
            return f"{self.player.name}"