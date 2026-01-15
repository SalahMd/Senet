from .cell import Cell


class RebirthCell(Cell):
    def __init__(self, pos):
        super().__init__(pos, "rebirth")
    def on_land(self, piece, board):
        pass

    def symbol(self):
        if self.piece:
            return "♻️"
        return "🚹"        
