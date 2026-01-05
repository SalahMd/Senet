from .cell import Cell


class HappinessCell(Cell):
    def __init__(self, row, col):
        super().__init__(row, col, "happiness")
    def can_land(self, piece, state):
        return True

    def symbol(self):
        if self.piece:
            return "😊"
        return "😊" 
