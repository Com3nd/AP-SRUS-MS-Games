import unittest
from player_list import PlayerList


class TestPlayerList(unittest.TestCase):
    def setUp(self) -> None:
        self.player_list = PlayerList()

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
        self.player_list.add_node("03", "Jonghun")

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

    def test_delete_head_by_value(self):
        self.player_list.add_node("01", "Mustafa")
        self.player_list.add_node("02", "Melissa")
        self.player_list.add_node("03", "Jonghun")

        # Delete head using the delete method
        self.player_list.delete("01")

        # Check if the new head has the 'uid' of "02"
        self.assertEqual(self.player_list.head.key, "02")

    def test_delete_tail_by_value(self):
        self.player_list.add_node("01", "Mustafa")
        self.player_list.add_node("02", "Melissa")
        self.player_list.add_node("03", "Jonghun")

        # Delete tail using the delete method
        self.player_list.delete("03")

        # Check if the new tail has the 'uid' of "02"
        self.assertEqual(self.player_list.tail.key, "02")

    def test_delete_node_by_value(self):
        self.player_list.add_node("01", "Mustafa")
        self.player_list.add_node("02", "Melissa")
        self.player_list.add_node("03", "Jonghun")

        # Delete middle node using the delete method
        self.player_list.delete("02")

        # Check if the middle node has been deleted by checking the next node of the head
        self.assertEqual(self.player_list.head.next_node.key, "03")


if __name__ == "__main__":
    unittest.main()
