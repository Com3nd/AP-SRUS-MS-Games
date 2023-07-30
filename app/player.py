class Player:
    """To be added"""

    def __init__(self, uid: str, name: str):
        self._uid: str = uid
        self._name: str = name

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Name: {self.name}"


if __name__ == "__main__":
    mustafa = Player("AA", "Mustafa")
    print(mustafa)
