class Pokemon:
    def __init__(self, id: int, name: str, height: int, weight: int) -> None:
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.height == other.height
            and self.weight == other.weight
        )

    def __hash__(self):
        return hash((self.name, self.height, self.weight))

    def __str__(self) -> str:
        return f"({self.id},'{self.name}',{self.height},{self.weight})"

    def __repr__(self) -> str:
        return f"<Pokemon> {self.id} {self.name}"
