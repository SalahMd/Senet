from .cell import Cell

class ReAtoumCell(Cell):
    def __init__(self, pos):
        super().__init__(pos, "re_aotum")

    def on_land(self, piece, board):
        piece.on_reatoum = True

    def check(self, piece, roll, board, game,is_moved):
        print("checking")
        if is_moved:
            return

        if not piece.on_reatoum:
            return

        if roll != 2:
            print("sent")
            self._send_to_rebirth(piece, board)
            return

        if game.moved_piece is piece:
            piece.on_reatoum = False
            return

        self._send_to_rebirth(piece, board)

    def _send_to_rebirth(self, piece, board):
        board.grid[piece.pos].piece = None

        if board.is_rebirth_empty():
            new_pos = 15
        else:
            new_pos = board.get_nearest_empty_cell_before_rebirth()

        if new_pos is not None:
            piece.on_reatoum = False
            board.grid[new_pos].piece = piece
            piece.pos = new_pos
            print(f"{piece.color} piece sent to Rebirth")
        else:
            print(f"No empty cell found for {piece.color} from Re-Atoum")

    def can_exit(self, roll):
        return roll == 2

    def symbol(self):
        return " 2️⃣"
