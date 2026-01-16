from .cell import Cell

class ThreeTruthsCell(Cell):
    def __init__(self, pos):
        super().__init__(pos, "truths")

    def on_land(self, piece, board):
        piece.on_three_truths = True

    def check(self, piece, roll, board, game, is_not_moved):
        # If the piece moved this turn, it just arrived. Do not penalize yet.
        if not is_not_moved:
            return

        if piece.on_three_truths:
            # If roll != 3 OR piece was not moved this turn
            if roll != 3 or is_not_moved:
                if board.is_rebirth_empty():
                    new_pos = 15
                else:
                    new_pos = board.get_nearest_empty_cell_before_rebirth()

                if new_pos is not None:
                    print(f"[{piece.color}] Rolled {roll} on Three Truths. Sent to Rebirth!")
                    board.grid[piece.pos].piece = None
                    board.grid[new_pos].piece = piece
                    piece.pos = new_pos
                    piece.on_three_truths = False
                else:
                    print(f"[{piece.color}] Rolled {roll} but Rebirth is blocked. Piece stays.")
            else:
                # Roll == 3 and piece moved, can exit normally
                piece.on_three_truths = False

    def symbol(self):
        return "3️⃣"
