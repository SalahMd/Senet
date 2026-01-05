from .cell import Cell


class WaterCell(Cell):
    def __init__(self, row, col):
        super().__init__(row, col, "water")
    def on_land(self, piece, state):
        state.send_to_rebirth(piece)

    def symbol(self):
        if self.piece:
            return "🌊"
        return "🌊"    
