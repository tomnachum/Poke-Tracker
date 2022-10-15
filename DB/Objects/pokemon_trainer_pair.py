from typing import Union


class P_T_Pair:
    def __init__(self, p_id: int, t_id: int) -> None:
        self.p_id = p_id
        self.t_id = t_id

    def __eq__(self, other):
        return self.p_id == other.p_id and self.t_id == other.t_id

    def __hash__(self):
        return hash((self.p_id, self.t_id))

    def __str__(self) -> str:
        return f"({self.p_id},{self.t_id})"

    def __repr__(self) -> str:
        return f"<P_T_Pair> ({self.p_id}, {self.t_id})"
