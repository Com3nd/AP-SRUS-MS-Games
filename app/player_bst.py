from __future__ import annotations
from player import Player
from typing import Optional
from player_bnode import PlayerBNode
from python_mermaid.diagram import MermaidDiagram


class NoRootNodeError(Exception):
    def __init__(self, message="The binary search tree has no root node."):
        super().__init__(message)


class PlayerBST:
    def __init__(self, node: Optional[PlayerBNode] = None):
        self._root: Optional[PlayerBNode] = node

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    def traverse(self, player: Player,  # type: ignore
                 current_node: Optional[PlayerBNode] = None) -> tuple[PlayerBNode, str]:
        """A helper method to traverse the tree"""

        if self.root is None:
            self._root = PlayerBNode(player)

        if current_node is None:
            current_node = self.root

        if current_node is not None:  # added this redundant if statement because mypy keeps thinking that
            # current_node is of type "Any | PlayerBNode | None
            if player.name == current_node.player.name:
                return current_node, "equal"

            if player.name >= current_node.player.name:
                if current_node.right:
                    return self.traverse(player, current_node.right)
                else:
                    return current_node, "Right"
            else:
                if current_node.left:
                    return self.traverse(player, current_node.left)
                else:
                    return current_node, "Left"

    def insert(self, player: Player):
        node, result = self.traverse(player)

        if result == "Right":
            node.right = PlayerBNode(player)

        if result == "Left":
            node.left = PlayerBNode(player)

        if result == "equal":
            node.player = player

    def search(self, name: str) -> Optional[PlayerBNode]:
        if self.root is None or self.root.player.name == name:
            return self.root

        node, result = self.traverse(Player("", name))

        if result == "equal":
            return node

        return None

    def to_list(self):
        return self.root.inorder_traversal()

    def balance_tree(self):
        """A method to balance the tree to have as equal amount of left and right nodes"""
        node_list = self.to_list()

        middle_index = len(node_list) // 2
        middle_node = node_list[middle_index]

        self.root = PlayerBNode(middle_node.player)

        step = middle_index - 1
        while step >= 0:
            self.insert(node_list[step].player)
            node_list.pop(step)
            step -= 1

        while len(node_list) > 1:
            self.insert(node_list[1].player)
            node_list.pop(1)

    def write_graph(self):
        node_links = self.root.return_links()

        chart_nodes = []
        for node in self.to_list():
            chart_nodes.append(node.graph_node)

        chart = MermaidDiagram(
            nodes=chart_nodes,
            links=node_links
        )
        start_index = str(chart).find("---")
        end_index = str(chart).find("---", start_index + 1)
        # Remove the "--- title ---" part from the string
        output_string = str(chart)[:start_index] + str(chart)[end_index + 3:]
        mermaid = f"```mermaid\n{output_string}\n```"
        with open("../node_graphs/node_graph.md", "w") as md_file:
            md_file.write(str(mermaid))
        print("\nMermaid diagram written. Check ../node_graphs/node_graph.md " +
              "\n\nIMPORTANT: Make sure to install Markdown plugin with mermaid extension")


if __name__ == "__main__":
    bst = PlayerBST()
    bst.insert(Player("02", "player_2"))
    bst.insert(Player("03", "player_3"))
    bst.insert(Player("04", "player_4"))
    bst.insert(Player("05", "player_5"))
    bst.insert(Player("01", "player_1"))
    bst.insert(Player("08", "player_8"))
    bst.insert(Player("07", "player_7"))
    bst.insert(Player("04", "player_2"))
    bst.insert(Player("04", "player_19"))
    bst.insert(Player("04", "player_199"))
    bst.insert(Player("04", "player_1998"))
    bst.insert(Player("04", "player_15"))
    bst.insert(Player("04", "player_9"))
    bst.write_graph()
