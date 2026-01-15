from .cell import Cell


class ThreeTruthsCell(Cell):
    def __init__(self, pos):
        super().__init__(pos, "truths")
    def on_land(self, piece, board):
        piece.on_three_truths = True

    def check(self, piece, roll, board, game):
        if piece.on_three_truths:
            next_idx = piece.pos + roll
            if not game.is_valid_move(piece, next_idx):
                piece.on_three_truths = False
                if board.is_rebirth_empty():
                    new_pos = 15
                else:
                    new_pos = board.get_nearest_empty_cell_before_rebirth()
                
                if new_pos is not None:
                    board.grid[piece.pos].piece = None
                    board.grid[new_pos].piece = piece
                    piece.pos = new_pos
                    print(f"{piece.color} piece moved to {new_pos} from House of Three Truths")
                else:
                    print(f"No empty cell found for {piece.color} piece from House of Three Truths")
            else:
                piece.on_three_truths = False # Reset the flag if a valid move is possible

    def can_exit(self, roll):
        return True
    
    def symbol(self):
        if self.piece:
            return "3️⃣"
        return "3️⃣"

