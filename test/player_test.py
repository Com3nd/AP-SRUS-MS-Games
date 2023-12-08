import player
from player import Player
import unittest
import random

class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        count = 0
        self.players = []
        while count < 10:
            count += 1
            self.players.append(Player(f"{count}", f"Player {count}"))
            self.players[count - 1].score = count

    def test_name(self):
        self.assertEqual(self.players[0].name, "Player 1")

    def test_uid(self):
        self.assertEqual(self.players[0].uid, "1")

    def test_add_password(self):
        self.players[0].add_password("password")
        self.assertIs(self.players[0]._ph.verify(self.players[0]._hashed_password, "password"), True)

    def test_verify_correct_password(self):
        self.players[0].add_password("Password to verify")
        self.assertIs(self.players[0].verify_password("Password to verify"), True)

    def test_verify_incorrect_password(self):
        self.players[0].add_password("Password to verify")
        self.assertIs(self.players[0].verify_password("Password"), False)

    def test_comparison_operators(self):
        self.players[0].score = 46
        self.players[1].score = 10
        self.players[2].score = 10

        self.assertLess(self.players[1], self.players[0])
        self.assertEqual(self.players[1], self.players[2])
        self.assertGreater(self.players[0], self.players[2])

    def test_bubble_sort(self):
        random.shuffle(self.players)

        unsort_list = self.players
        Player.bubble_sort(self.players)

        self.assertEqual(sorted(unsort_list, reverse=True), self.players)


if __name__ == "__main__":
    unittest.main()
