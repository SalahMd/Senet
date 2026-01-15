from .cell import Cell


class ReAtoumCell(Cell):
    def __init__(self, pos):
        super().__init__(pos, "re_aotum")
    def on_land(self, piece, board):
        piece.on_reatoum = True

    def check(self, piece, roll, board, game):
        if piece.on_reatoum:
            if roll != 2:
                # If the roll is not 2, the piece must be moved back
                piece.on_reatoum = False
                if board.is_rebirth_empty():
                    new_pos = 15
                else:
                    new_pos = board.get_nearest_empty_cell_before_rebirth()
                
                if new_pos is not None:
                    board.grid[piece.pos].piece = None
                    board.grid[new_pos].piece = piece
                    piece.pos = new_pos
                    print(f"{piece.color} piece moved to {new_pos} from House of Re-Atoum")
                else:
                    print(f"No empty cell found for {piece.color} piece from House of Re-Atoum")
            else:
                # The roll is 2, check if the move is valid
                next_idx = piece.pos + roll
                if not game.is_valid_move(piece, next_idx):
                    # The move is not valid, so the piece must be moved back
                    piece.on_reatoum = False
                    if board.is_rebirth_empty():
                        new_pos = 15
                    else:
                        new_pos = board.get_nearest_empty_cell_before_rebirth()

                    if new_pos is not None:
                        board.grid[piece.pos].piece = None
                        board.grid[new_pos].piece = piece
                        piece.pos = new_pos
                        print(f"{piece.color} piece moved to {new_pos} from House of Re-Atoum")
                    else:
                        print(f"No empty cell found for {piece.color} piece from House of Re-Atoum")

    def can_exit(self, roll):
        return roll == 2
    
    def symbol(self):
        if self.piece:
            return "2️⃣"
        return " 2️⃣"
