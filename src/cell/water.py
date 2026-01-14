from .cell import Cell


class WaterCell(Cell):
    def __init__(self, row):
        super().__init__(row, "water")
    def on_land(self, piece, state):
        state.send_to_rebirth(piece)

    def symbol(self):
        if self.piece:
            return "🌊"
        return "🌊"    
