from .cell import Cell


class HappinessCell(Cell):
    def __init__(self, row,):
        super().__init__(row, "happiness")
    def can_land(self, piece, state):
        return True

    def symbol(self):
        if self.piece:
            return "😊"
        return "😊" 
