class Game:
    def __init__(self, players, board, dice):
        self.players = players
        self.board = board
        self.dice = dice
        self.current_player_index = 0
        self.moved_piece = None  

    def start(self):
        while not self.is_game_over():
            current_player = self.players[self.current_player_index]
            roll = self.dice.roll()
            print(f"\n{current_player.name} Turn, Roll: {roll}")
            self.moved_piece = None

            piece_idx = current_player.play(self.get_game_state(roll))
            if piece_idx is not None:
                self.move_piece(piece_idx, roll)
            else:
                print(f"{current_player.name} has no moves")
            for piece in current_player.pieces[:]:
                self.check_special_states(piece, roll)   

            self.board.display()
            if self.current_player_index == 0:
                self.current_player_index = 1
            else:
                self.current_player_index = 0

    def check_special_states(self, piece, roll):
        if getattr(piece, "on_three_truths", False):
            if self.board.grid[piece.pos].type == "truths":
                cell = self.board.grid[piece.pos]
                cell.check(piece, roll, self.board, self, piece == self.moved_piece)
            else:
                piece.on_three_truths = False

        if getattr(piece, "on_reatoum", False):
            if self.board.grid[piece.pos].type == "re_aotum":
                cell = self.board.grid[piece.pos]
                cell.check(piece, roll, self.board, self, piece == self.moved_piece)
            else:
                piece.on_reatoum = False
        if getattr(piece, "on_horus", False):
            if self.board.grid[piece.pos].type == "horus":
                cell = self.board.grid[piece.pos]
                cell.check(piece, roll, self.board, self, piece == self.moved_piece)
            else:
                piece.on_horus = False        

    def is_valid_move(self, piece, next_idx):
        happiness_index = 25
        if not piece.passed_happiness and next_idx > happiness_index:
            return False
        if next_idx >= len(self.board.grid):
            return piece.passed_happiness
        if next_idx < len(self.board.grid):
            cell = self.board.grid[next_idx]
            if cell.is_occupied() and cell.piece.color == piece.color:
                return False
        return True


    def move_piece(self, piece_idx, roll):
        current_player = self.players[self.current_player_index]
        piece = self.get_piece_idx(piece_idx, current_player.pieces)

        if not piece:
            return

        next_idx = piece.pos + roll
        if not self.is_valid_move(piece, next_idx):
            return

        current_cell = self.board.grid[piece.pos]

        if next_idx >= len(self.board.grid):
            current_cell.piece = None
            current_player.pieces.remove(piece)
            self.moved_piece = piece
            return

        next_cell = self.board.grid[next_idx]
        if next_cell.is_occupied():
            other_piece = next_cell.piece

            next_cell.piece = piece
            current_cell.piece = other_piece

            other_piece.pos = piece.pos
            piece.pos = next_idx

            if hasattr(current_cell, "on_land"):
                current_cell.on_land(other_piece, self.board)

        else:
            current_cell.piece = None
            next_cell.piece = piece
            piece.pos = next_idx
        if hasattr(next_cell, "on_land"):
            next_cell.on_land(piece, self.board)

        self.moved_piece = piece



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
        current_pieces = [cell.piece for cell in self.board.grid if cell.piece and cell.piece.color == player.color]
        for piece in current_pieces:
            if piece.pos == 27 and roll != 3:
                continue
            if piece.pos == 28 and roll != 2:
                continue
            if self.is_valid_move(piece, piece.pos + roll):
                legal_moves.append(piece.pos)
        return sorted(legal_moves)
