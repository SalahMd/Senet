from .cell import Cell


class HappinessCell(Cell):
    def __init__(self, pos,):
        super().__init__(pos, "happiness")
    def on_land(self, piece, board):
        piece.passed_happiness = True
        piece.stuck_on_happiness = True

    def check(self, piece, roll, board, game):
        next_idx = piece.pos + roll
        if not game.is_valid_move(piece, next_idx):
            piece.stuck_on_happiness = False  # Reset the flag
            if board.is_rebirth_empty():
                new_pos = 15
            else:
                new_pos = board.get_nearest_empty_cell_before_rebirth()

            if new_pos is not None:
                board.grid[piece.pos].piece = None
                board.grid[new_pos].piece = piece
                piece.pos = new_pos
                print(f"{piece.color} piece moved to {new_pos} from House of Happiness")
            else:
                print(f"No empty cell found for {piece.color} piece from House of Happiness")


    def symbol(self):
        if self.piece:
            return "😊"
        return "😊" 
