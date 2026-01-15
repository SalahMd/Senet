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
            print(f"\n{current_player.name} Turn")
            print(f"Roll: {roll}")
            piece_idx = current_player.play(self.get_game_state(roll))
            
            if piece_idx is not None:
                self.move_piece(piece_idx, roll)
            else:
                print(f"{current_player.name} has no moves")
            self.board.display() 
            self.current_player_index = (self.current_player_index + 1) % len(self.players)


    def is_valid_move(self, piece, next_idx):
        if next_idx >= 30:
            return getattr(piece, 'passed_happiness', False)

        if piece.pos < 25 and next_idx > 25:
            return False
        next_cell = self.board.grid[next_idx]
        if next_cell.is_occupied() and next_cell.piece.color == piece.color:
            return False
            
        return True

    def move_piece(self, piece_idx, roll):
        current_player = self.players[self.current_player_index]
        piece = self.get_piece_idx(piece_idx, current_player.pieces)
        if not piece: return

        next_idx = piece_idx + roll
        current_cell = self.board.grid[piece_idx]
        if next_idx >= 30:
            print(f"🎉 {current_player.name}'s piece moved off the board")
            current_cell.piece = None
            current_player.pieces.remove(piece)
            return

        next_cell = self.board.grid[next_idx]

        # Handle Swapping or Regular movement
        if next_cell.is_occupied():
            other_piece = next_cell.piece
            if other_piece.color != piece.color:
                other_piece.pos = piece_idx
                piece.pos = next_idx
                current_cell.piece = other_piece
                next_cell.piece = piece
        else:
            current_cell.piece = None
            next_cell.piece = piece
            piece.pos = next_idx

        # Update "Passed Happiness" status
        if next_idx == 25:
            piece.passed_happiness = True

        # Handle House of Water (Square 27 - Index 26)
        if next_idx == 26: 
            self.handle_water_house(piece, next_idx)

    def handle_water_house(self, piece, water_idx):
        rebirth_idx = 14
        water_cell = self.board.grid[water_idx]
        rebirth_cell = self.board.grid[rebirth_idx]

        if not rebirth_cell.is_occupied():
            print("Returning to House of Rebirth")
            water_cell.piece = None
            rebirth_cell.piece = piece
            piece.pos = rebirth_idx
        else:
            print("Piece is in water.")

    def is_game_over(self):
        for player in self.players:
            if not player.pieces:
                print(f"\n🏆 Game Over! Winner: {player.name}")
                return True
        return False

    def get_game_state(self, roll):
        return {
            "board": self.board,
            "roll": roll,
            "players": self.players,
            "game_instance": self
        }

    def get_piece_idx(self, piece_idx, pieces):
        for piece in pieces:
            if piece.pos == piece_idx:
                return piece
        return None

    def get_available_moves(self, player, roll):
        legal_moves = []
        for piece in player.pieces:
            if self.is_valid_move(piece, piece.pos + roll):
                legal_moves.append(piece.pos)
        return sorted(legal_moves)