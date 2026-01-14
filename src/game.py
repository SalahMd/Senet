class Game:
    def __init__(self, players, board, dice):
        self.players = players
        self.board = board
        self.dice = dice
        self.current_player_index = 0

    def start(self):
        while not self.is_game_over():
            current_player = self.players[self.current_player_index]
            roll = self.dice.roll()
            print(f"{current_player.name} rolled a {roll}")
            
            # For simplicity, this assumes the player's `play` method returns the index of the piece to move.
            # A real implementation would need more sophisticated logic for piece selection.
            piece_to_move_idx = current_player.play(self.get_game_state(roll))
            
            if piece_to_move_idx is not None:
                self.move_piece(piece_to_move_idx, roll)
            
            self.board.display() # Display board after each move
            self.current_player_index = (self.current_player_index + 1) % len(self.players)


    def move_piece(self, piece_idx, roll):
        current_player = self.players[self.current_player_index]
        piece = self.get_piece_idx(piece_idx, current_player.pieces)

        if not piece:
            print(f"No piece found at index {piece_idx} for {current_player.name}")
            return

        current_cell = self.board.grid[piece_idx]
        next_idx = piece_idx + roll

        if next_idx >= len(self.board.grid):
            # Piece moves off the board
            print(f"{piece.color} piece moved off the board!")
            current_cell.piece = None
            current_player.pieces.remove(piece)
            return

        next_cell = self.board.grid[next_idx]

        if next_cell.is_occupied():
            other_piece = next_cell.piece
            if other_piece.color != piece.color:
                # Opponent's piece is here, swap them
                print(f"Swapping with opponent's piece at {next_idx}")
                
                # Update positions
                other_piece.pos = piece_idx
                piece.pos = next_idx
                
                # Update cell references
                current_cell.piece = other_piece
                next_cell.piece = piece

                # Find the opponent and update their piece's reference if they are tracked in lists
                for player in self.players:
                    if player.name != current_player.name:
                        for p in player.pieces:
                            if p is other_piece:
                                # This is the piece, its pos is already updated
                                break
                        break
            else:
                # Cannot move to a cell occupied by own piece
                print("Invalid move: cell occupied by own piece.")
                return
        else:
            # Cell is empty, just move the piece
            current_cell.piece = None
            next_cell.piece = piece
            piece.pos = next_idx
        
        # Handle special cell logic
        next_cell.on_land(piece, self.get_game_state(roll))


    def is_game_over(self):
        # Game is over if any player has no pieces left
        for player in self.players:
            if not player.pieces:
                print(f"Game over! {player.name} has no pieces left.")
                return True
        return False

    def get_game_state(self, roll):
        # Return the current game state including the roll
        return {
            "board": self.board,
            "roll": roll,
            "players": self.players,
        }  
    
    def get_piece_idx(self, piece_idx, pieces):
        for piece in pieces:
            if piece.pos == piece_idx:
                return piece
        return None