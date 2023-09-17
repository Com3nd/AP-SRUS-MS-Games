from argon2 import PasswordHasher
from typing import Optional
# import random


class Player:
    """To be added"""

    def __init__(self, uid: str, name: str):
        self._uid: str = uid
        self._name: str = name
        self._hashed_password: Optional[str] = None
        self._ph = PasswordHasher()
        self._score: int = 0

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value: int):
        self._score = value if value >= 0 else 0

    def add_password(self, password: str):
        self._hashed_password = self._ph.hash(password)

    def verify_password(self, password) -> bool:
        return self._ph.verify(self._hashed_password, password)  # type: ignore

    @staticmethod
    def bubble_sort(players: list['Player']):
        for _ in players:
            for index, player in enumerate(players):
                if index != len(players) - 1 and player < players[index + 1]:
                    players[index] = players[index + 1]
                    players[index + 1] = player

        return players

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score

    def __repr__(self):
        return f"Player({self.score})"


if __name__ == "__main__":
    pass
    # count = 0
    # players = []
    # while count < 29:
    #     players.append(Player(f"{count}", f"Player {count}"))
    #     players[count].score = count
    #     count += 1
    #
    # random.shuffle(players)
    #
    # Player.bubble_sort(players)
    # for player in players:
    #     print(player.score)
