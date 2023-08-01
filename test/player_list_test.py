import unittest
from player_list import PlayerList


class TestPlayerList(unittest.TestCase):
    def setUp(self) -> None:
        self.player_list = PlayerList()
        # player_list.add_node("01", "Mustafa")
        # player_list.add_node("02", "Melissa")
        # player_list.add_node("03", "Jonghun")
        # player_list.add_node("04", "raf")

    def test_empty_player_list(self):
        self.assertIs(self.player_list.is_empty(), True)

    def test_adding_node_to_list(self):
        self.player_list.add_node("01", "Mustafa")
        self.assertIs(self.player_list.is_empty(), False)

    def test_previous_node_variable(self):
        self.player_list.add_node("01", "Mustafa")
        self.player_list.add_node("02", "Melissa")
        self.player_list.add_node("03", "Jonghun")
        self.assertEqual(self.player_list.tail.prev_node.key, "02")

    def test_delete_head(self):
        self.player_list.add_node("01", "Mustafa")
        self.player_list.add_node("02", "Melissa")

        # Delete head
        self.player_list.delete_head()

        # Check if the new head has the 'uid' of "02"
        self.assertEqual(self.player_list.head.key, "02")

    def test_delete_tail(self):
        self.player_list.add_node("01", "Mustafa")
        self.player_list.add_node("02", "Melissa")
        self.player_list.add_node("03", "Jonghun")

        # Delete tail
        self.player_list.delete_tail()

        # Check if the new tail has the 'uid' of "02"
        self.assertEqual(self.player_list.tail.key, "02")


if __name__ == "__main__":
    unittest.main()
