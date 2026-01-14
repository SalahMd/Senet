from .cell import Cell


class EmptyCell(Cell):
    def __init__(self, row,):
        super().__init__(row, "empty")

    def symbol(self):
        return "🟫"    