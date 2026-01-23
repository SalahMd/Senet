from .cell import Cell


class WaterCell(Cell):
    def __init__(self, pos):
        super().__init__(pos, "water")
    def on_land(self, piece, board):
        if board.is_rebirth_empty():
            new_pos = 15
        else:
            new_pos = board.get_nearest_empty_cell_before_rebirth()

        if new_pos is not None:
            board.grid[piece.pos].piece = None
            board.grid[new_pos].piece = piece
            piece.pos = new_pos
            print(f"{piece.color} piece moved to {new_pos} from House of Water")

    def symbol(self):
        return "🌊"    
