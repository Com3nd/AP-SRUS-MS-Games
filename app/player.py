from argon2 import PasswordHasher
from typing import Optional


class Player:
    """To be added"""

    def __init__(self, uid: str, name: str):
        self._uid: str = uid
        self._name: str = name
        self._hashed_password: Optional[str] = None
        self._ph = PasswordHasher()

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    def add_password(self, password: str):
        self._hashed_password = self._ph.hash(password)

    def verify_password(self, password) -> bool:
        # Note: I don't know if Assessment Task 2 asks us to use the verify method.

        # return self._hashed_password == self._ph.hash(password)
        return self._ph.verify(self._hashed_password, password)  # type: ignore

    def __str__(self):
        return f"Name: {self.name}"


if __name__ == "__main__":
    mustafa = Player("AA", "Mustafa")
    print(mustafa)
