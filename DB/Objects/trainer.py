class Trainer:
    def __init__(self, id: int, name: str, town: str) -> None:
        self.id = id
        self.name = name
        self.town = town

    def __eq__(self, other):
        return self.name == other.name and self.town == other.town

    def __hash__(self):
        return hash((self.name, self.town))

    def __str__(self) -> str:
        return f"({self.id},'{self.name}','{self.town}')"

    def __repr__(self) -> str:
        return f"<Trainer> {self.id} {self.name}"
