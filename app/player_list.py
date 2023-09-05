import player_node
from player_node import PlayerNode
from typing import Optional


class PlayerList:
    """A double linked list that contains player nodes"""

    def __init__(self, node_list: Optional[list[tuple[str, str]]] = None):
        self._head: Optional[PlayerNode] = None
        self._tail: Optional[PlayerNode] = None
        if node_list:
            [self.add_node(uid, name) for uid, name in node_list]

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value: Optional[PlayerNode]):
        self._head = value

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, value: Optional[PlayerNode]):
        self._tail = value

    def is_empty(self):
        return not bool(self.head)

    def add_node(self, uid: str, name: str):
        node = PlayerNode(player_node.Player(uid, name))
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
            self._tail = node
            return

    def delete_head(self):
        self.head = self.head.next_node
        self.head.prev_node = None

    def delete_tail(self):
        self._tail = self.tail.prev_node
        self._tail.next_node = None

    def delete(self, key_value: str) -> bool:
        node_to_delete: PlayerNode = self.head

        while True:
            if node_to_delete.key == key_value.strip():
                # Set the next node's pointer of the current node to current node's previous node and vise versa
                # Using if statements to avoid crashing when deleting the head or tail

                # if the node_to_delete is the tail
                if not node_to_delete.next_node:
                    self.delete_tail()
                    return True

                # if the node_to_delete is the head
                if not node_to_delete.prev_node:
                    self.delete_head()
                    return True

                else:  # Runs when the node isn't a head nor a tail node.
                    node_to_delete.next_node.prev_node = node_to_delete.prev_node
                    node_to_delete.prev_node.next_node = node_to_delete.next_node

                return True
            if node_to_delete.next_node:
                node_to_delete = node_to_delete.next_node
                continue

            return False

    def to_list(self, is_forward: bool = True) -> list:
        nodes = []

        current_node = self.head if is_forward else self.tail
        nodes.append(current_node)

        next_node = lambda p: p.next_node if is_forward else p.prev_node

        while next_node(current_node):
            nodes.append(next_node(current_node))
            current_node = next_node(current_node)

        return nodes

    def display(self, is_forward: bool = True):
        print(" --> ".join(node.player.name for node in self.to_list(is_forward)))

    def __str__(self):
        return " --> ".join(node.player.name for node in self.to_list())


if __name__ == '__main__':
    player_list = PlayerList([("01", "Mustafa"), ("02", "Melissa"), ("03", "Jonghun")])
    player_list.display()
    player_list.display(False)
