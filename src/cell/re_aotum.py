from .cell import Cell


class ReAtoumCell(Cell):
    def __init__(self, pos):
        super().__init__(pos, "re_aotum")
    def on_land(self, piece, board):
        piece.on_reatoum = True

    def check(self, piece, roll, board, game):
        if piece.on_reatoum:
            if roll != 2:
                piece.on_reatoum = False
                if board.is_rebirth_empty():
                    new_pos = 15
                else:
                    new_pos = board.get_nearest_empty_cell_before_rebirth()
                
                if new_pos is not None:
                    board.grid[piece.pos].piece = None
                    board.grid[new_pos].piece = piece
                    piece.pos = new_pos
                else:
                    print(f"No empty cell found for {piece.color}")
            else:
                # The roll is 2
                next_idx = piece.pos + roll
                if not game.is_valid_move(piece, next_idx):
                    # The move is not valid
                    piece.on_reatoum = False
                    if board.is_rebirth_empty():
                        new_pos = 15
                    else:
                        new_pos = board.get_nearest_empty_cell_before_rebirth()

                    if new_pos is not None:
                        board.grid[piece.pos].piece = None
                        board.grid[new_pos].piece = piece
                        piece.pos = new_pos
                    else:
                        print(f"No empty cell found for {piece.color} piece from House of Re-Atoum")


    
    def symbol(self):
        return " 2️⃣"
