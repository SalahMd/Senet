from .cell import Cell


class HorusCell(Cell):
    def __init__(self, pos):
        super().__init__(pos, "horus")

    def on_land(self, piece, board):
        piece.on_horus = True

    def check(self, piece, roll, board, game, is_moved):
        if not is_moved:
            return
        if not piece.on_horus:
            return

        if game.moved_piece is piece:
            piece.on_horus = False
            return

        board.grid[piece.pos].piece = None
        if board.is_rebirth_empty():
            new_pos = 15
        else:
            new_pos = board.get_nearest_empty_cell_before_rebirth()

        if new_pos is not None:
            piece.on_horus = False
            board.grid[new_pos].piece = piece
            piece.pos = new_pos

    def symbol(self):
        return " 🏁"