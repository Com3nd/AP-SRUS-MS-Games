from player import Player
import unittest


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player("1", "Alice")

    def test_name(self):
        self.assertEqual(self.player.name, "Alice")

    def test_uid(self):
        self.assertEqual(self.player.uid, "1")

    def test_add_password(self):
        self.player.add_password("password")
        self.assertIs(self.player._ph.verify(self.player._hashed_password, "password"), True)

    def test_verify_password(self):
        self.player.add_password("Password to verify")
        self.assertIs(self.player.verify_password("Password to verify"), True)


if __name__ == "__main__":
    unittest.main()
