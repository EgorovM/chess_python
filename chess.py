from typing import Dict, Tuple, List
coord = Tuple[int, int]

class Figure:
    def __init__(self, start_pos: coord) -> None:
        self._position = start_pos
    
    def step(self, new_position: coord) -> None:
        self._position = new_position

    def possible_step(self):
        raise NotImplementedError


class Pawn(Figure):
    def __init__(self, start_pos: coord) -> None:
        super().__init__(start_pos)

    def possible_step(self) -> List[coord]:
        x, y = self._position
        return [(x, y + i) for i in range(1, 3) if x < 8 and y < 8]


class ChessDesk:
    def __init__(self, size: Tuple[int, int]=(8, 8)) -> None:
        self._figures = []

        self._figures.append(Pawn((0, 0)))
        self._figures.append(Pawn((1, 0)))
        self._figures.append(Pawn((2, 0)))
        