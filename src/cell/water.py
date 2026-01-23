from .cell import Cell


class WaterCell(Cell):
    def __init__(self, pos):
        super().__init__(pos, "water")
    def on_land(self, piece, board):
        if board.is_rebirth_empty():
            new_pos = 15
        else:
            new_pos = board.get_nearest_empty_cell_before_rebirth()

        board.grid[piece.pos].piece = None
        board.grid[new_pos].piece = piece
        piece.pos = new_pos

    def symbol(self):
        return "🌊"    
