from .cell import Cell

class ThreeTruthsCell(Cell):
    def __init__(self, pos):
        super().__init__(pos, "truths")

    def on_land(self, piece, board):
        piece.on_three_truths = True

    def check(self, piece, roll, board, game, is_move):
        if is_move:
            return
        if piece.on_three_truths:
            if roll != 3 :
                if board.is_rebirth_empty():
                    new_pos = 15
                else:
                    new_pos = board.get_nearest_empty_cell_before_rebirth()

                if new_pos is not None:
                    board.grid[piece.pos].piece = None
                    board.grid[new_pos].piece = piece
                    piece.pos = new_pos
                    piece.on_three_truths = False
            else:
                piece.on_three_truths = False

    def symbol(self):
        return "3️⃣"
