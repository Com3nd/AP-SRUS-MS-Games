from player import Player
from typing import Optional
from python_mermaid.diagram import Node, Link


class PlayerBNode:

    def __init__(self, player: Player):
        self._player: Player = player
        self.graph_node = Node(self.player.name, shape="circle")
        self._right: Optional[PlayerBNode] = None  # Right is greater than
        self._left: Optional[PlayerBNode] = None  # Left is greater than

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = value

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

    def inorder_traversal(self, input_list: Optional[list['PlayerBNode']] = None) -> Optional[list['PlayerBNode']]:
        if input_list is None:
            input_list = []

        if self.left:
            self.left.inorder_traversal(input_list=input_list)

        input_list.append(self)

        if self.right:
            self.right.inorder_traversal(input_list=input_list)

        return input_list

    def return_links(self, links: list[Link] = None):
        if links is None:
            links = []

        if self.left:
            links.append(Link(self.graph_node, self.left.graph_node))
            self.left.return_links(links)

        if self.right:
            links.append(Link(self.graph_node, self.right.graph_node))
            self.right.return_links(links)

        return links

    def __str__(self):
        return f"{self.player.name}"

    def __repr__(self):
        return f"{self.player.name}"
