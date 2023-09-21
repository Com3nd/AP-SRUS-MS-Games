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
            # current_root is of type "Any | PlayerBNode | None
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

    def balance_tree(self, current_root: Optional[PlayerBNode] = None,
                     node_list: Optional[list[PlayerBNode]] = None):
        """A method to balance the binary search tree"""
        if node_list is None:
            node_list = self.to_list()

        if len(node_list) == 0:
            return
        middle_index = len(node_list) // 2
        middle_node = node_list[middle_index]

        if current_root is None:
            self.root = middle_node

        if node_list is None:
            node_list = []

        current_root = node_list.pop(middle_index)
        current_root.right = self.balance_tree(current_root, node_list[middle_index:])
        current_root.left = self.balance_tree(current_root, node_list[:middle_index])

        return current_root

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
    bst.insert(Player("10", "John Smith"))
    bst.insert(Player("11", "Emily Johnson"))
    bst.insert(Player("12", "Michael Davis"))
    bst.insert(Player("13", "Sarah Wilson"))
    bst.insert(Player("14", "David Martinez"))
    bst.insert(Player("15", "Jessica Anderson"))
    bst.insert(Player("16", "Robert Brown"))
    bst.insert(Player("17", "Jennifer Lee"))
    bst.insert(Player("18", "William Jones"))
    bst.insert(Player("19", "Linda Clark"))
    bst.insert(Player("20", "Christopher Wright"))
    bst.insert(Player("21", "Karen Adams"))
    bst.insert(Player("22", "Matthew Taylor"))
    bst.insert(Player("23", "Patricia Hall"))
    bst.insert(Player("24", "Joseph White"))
    bst.balance_tree()
    bst.write_graph()
