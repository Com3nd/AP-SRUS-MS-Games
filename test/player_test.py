from player import Player
import unittest


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player("1", "Alice")

    def test_name(self):
        # Test the 'name' property of person
        self.assertEqual(self.player.name, "Alice")

    def test_uid(self):
        # Test the 'uid' property of person
        self.assertEqual(self.player.uid, "1")


if __name__ == "__main__":
    unittest.main()
