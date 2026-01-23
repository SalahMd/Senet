from .cell import Cell


class HappinessCell(Cell):
    def __init__(self, pos,):
        super().__init__(pos, "happiness")

    def on_land(self, piece,board):
        piece.passed_happiness = True

    def check(self, piece, roll, board, game, is_not_moved):
        next_idx = piece.pos + roll
        if not game.is_valid_move(piece, next_idx):
            if board.is_rebirth_empty():
                new_pos = 15
            else:
                new_pos = board.get_nearest_empty_cell_before_rebirth()

            board.grid[piece.pos].piece = None
            board.grid[new_pos].piece = piece
            piece.pos = new_pos


    def symbol(self):
        return "😊" 
