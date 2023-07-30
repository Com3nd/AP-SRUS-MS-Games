from player_node import PlayerNode


class PlayerList:
    """To be added"""

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return bool(self.head)

    def add_node(self, node: PlayerNode):
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
            # The next node is none, assign 'next_node' to 'node'
            current_node.next_node = node
            current_node.next_node.prev_node = current_node
            self.tail = node
            return

    def to_list(self):
        if self.head is None:
            return []

        node_list = [self.head]
        current_node = self.head
        while True:
            if current_node.next_node is None:
                return node_list

            node_list.append(current_node.next_node)
            current_node = current_node.next_node


if __name__ == '__main__':
    player_list = PlayerList()
    mustafa = PlayerNode("01", "Mustafa")
    player_list.add_node(mustafa)
    melissa = PlayerNode("02", "Melissa")
    player_list.add_node(melissa)
    jonghun = PlayerNode("03", "Jonghun")
    player_list.add_node(jonghun)
    raf = PlayerNode("04", "raf")
    player_list.add_node(raf)
    print("\n".join(str(player) for player in player_list.to_list()))


