from .cell import Cell


class RebirthCell(Cell):
    def __init__(self, row):
        super().__init__(row, "rebirth")
    def on_land(self, piece, state):
        if self.is_occupied():
            target = state.first_free_before(self.index)
            state.move_piece(self.piece, target)

    def symbol(self):
        if self.piece:
            return "♻️"
        return "🚹"        
