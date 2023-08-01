from player_node import PlayerNode
from typing import Optional


class PlayerList:
    """To be added"""

    def __init__(self, node_list: Optional[tuple[str]] = None):
        self._head: Optional[PlayerNode] = None
        self._tail: Optional[PlayerNode] = None
        if node_list:
            [self.add_node(node[0], node[1]) for node in node_list]

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @head.setter
    def head(self, value: Optional[PlayerNode]):
        self._head = value

    @tail.setter
    def tail(self, value: Optional[PlayerNode]):
        self._tail = value

    def is_empty(self):
        return not bool(self.head)

    def add_node(self, uid: str, name: str):
        node = PlayerNode(uid, name)
        if self.head is None:
            self.head = node
            return

        # Assigning 'current_node' to head since it is not None
        current_node = self.head

        while True:
            # The next node is not none, assign 'current_node' to 'next_node'
            if current_node.next_node is not None:
                current_node = current_node.next_node
                continue
            # The next node is none, assign 'next_node' to 'node' and assign the next node's 'prev_node' to the current
            # node
            current_node.next_node = node
            current_node.next_node.prev_node = current_node
            self.tail = node
            return

    def delete_head(self):
        self.head = self.head.next_node
        self.head.prev_node = None

    def delete_tail(self):
        self.tail = self.tail.prev_node
        self.tail.next_node = None

    def to_list(self):
        if self.head is None:
            return []

        node_list = [self.head]
        current_node = self.head

        while current_node.next_node is not None:
            node_list.append(current_node.next_node)
            current_node = current_node.next_node

        return node_list


if __name__ == '__main__':
    player_list = PlayerList()
    player_list.add_node("01", "Mustafa")
    player_list.add_node("02", "Melissa")
    player_list.add_node("03", "Jonghun")
    player_list.add_node("04", "raf")
    print("\n".join(str(player) for player in player_list.to_list()) + "\n")
    player_list.delete_head()
    print("\n".join(str(player) for player in player_list.to_list()) + "\n")
    player_list.delete_tail()
    print("\n".join(str(player) for player in player_list.to_list()) + "\n")


