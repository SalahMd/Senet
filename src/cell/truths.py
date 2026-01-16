from .cell import Cell

class ThreeTruthsCell(Cell):
    def __init__(self, pos):
        super().__init__(pos, "truths")

    def on_land(self, piece):
        piece.on_three_truths = True

    def check(self, piece, roll, board, game):
        # We only run logic if the piece is currently marked as being on Three Truths
        if piece.on_three_truths:
            
            # The Golden Rule of Three Truths:
            # You can ONLY exit with a roll of 3.
            # If you roll anything else (1, 2, 4, 5), you are sent to Rebirth.
            if roll != 3:
                # 1. Logic to determine where the piece lands (Rebirth or nearest empty)
                if board.is_rebirth_empty():
                    new_pos = 15 # House of Rebirth (Square 16 is index 15)
                else:
                    new_pos = board.get_nearest_empty_cell_before_rebirth()
                
                # 2. Move the piece if a valid spot was found
                if new_pos is not None:
                    print(f"[{piece.color}] Rolled {roll} on Three Truths. Sent to Rebirth!")
                    
                    # Clear current cell
                    board.grid[piece.pos].piece = None
                    
                    # Move to new cell
                    board.grid[new_pos].piece = piece
                    piece.pos = new_pos
                    
                    # Reset the flag since it's no longer on Three Truths
                    piece.on_three_truths = False
                else:
                    print(f"[{piece.color}] Rolled {roll} but Rebirth is blocked. Piece stays.")
            
            # If the roll IS 3, the piece is allowed to exit normally via the 
            # standard move function (handled by your main game loop/move logic).
            # We don't need to move it here, just ensure we don't send it to Rebirth.

    def symbol(self):
        return "3️⃣"