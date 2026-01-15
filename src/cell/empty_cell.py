from .cell import Cell


class EmptyCell(Cell):
    def __init__(self, pos,):
        super().__init__(pos, "empty")

    def symbol(self):
        return "🟫"    