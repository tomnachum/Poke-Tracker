class Type:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self) -> str:
        return f"({self.id},'{self.name}')"

    def __repr__(self) -> str:
        return f"<Type> {self.id} {self.name}"
