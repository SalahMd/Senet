class Heuristic:
    def __init__(self, player_color):
        self.player_color = player_color
        self.weights = {
            "piece_progression": 10,
            "pieces_off_board": 800,
            "house_of_happiness": 100,
            "house_of_water": -200,
            "house_of_rebirth": -150,
            "three_truths": 200,
            "re_atoum": 200,
            "horus": 300,
            "piece_safety": 50,
            "blocking": 30
        }

    def evaluate(self, game_state):
        board = game_state['board']
        players = game_state['players']
        current_player = self.get_player(players)
        opponent = self.get_opponent(players)

        score = 0
        score += self._evaluate_piece_progression(board)
        score += self._evaluate_pieces_off_board(current_player)
        score += self._evaluate_special_cells(board)
        score += self._evaluate_piece_safety(board)
        score += self._evaluate_blocking(board, opponent)
        score += self._evaluate_future_risk(board, current_player)
        
        return score

    def get_player(self, players):
        for player in players:
            if player.color == self.player_color:
                return player
        return None

    def get_opponent(self, players):
        for player in players:
            if player.color != self.player_color:
                return player
        return None

    def _evaluate_piece_progression(self, board):
        score = 0
        for cell in board.grid:
            if cell.piece:
                multiplier = 1 if cell.piece.color == self.player_color else -1
                score += cell.piece.pos * self.weights["piece_progression"] * multiplier
        return score

    def _evaluate_pieces_off_board(self, player):

        return (7 - len(player.pieces)) * self.weights["pieces_off_board"]

    def _evaluate_special_cells(self, board):
        score = 0
        special_cells = {
            25: "house_of_happiness",
            26: "house_of_water",
            14: "house_of_rebirth",
            27: "three_truths",
            28: "re_atoum",
            29: "horus"
        }
        for pos, name in special_cells.items():
            cell = board.grid[pos]
            if cell.piece:
                multiplier = 1 if cell.piece.color == self.player_color else -1
                score += self.weights[name] * multiplier
        return score

    def _evaluate_piece_safety(self, board):
        score = 0
        for cell in board.grid:
            if cell.piece and cell.piece.color == self.player_color:
                is_safe = self._is_piece_safe(cell.piece, board)
                if is_safe:
                    score += self.weights["piece_safety"]
        return score

    def _is_piece_safe(self, piece, board):
        if piece.pos in [25, 27, 28, 29]: 
            return True
        for i in range(1, 5):
            if piece.pos - i >= 0:
                prev_cell = board.grid[piece.pos - i]
                if prev_cell.piece and prev_cell.piece.color == piece.color:
                    return True
        return False

    def _evaluate_blocking(self, board, opponent):
        score = 0
        for cell in board.grid:
            if cell.piece and cell.piece.color == opponent.color:
                is_blocked = self._is_piece_blocked(cell.piece, board)
                if is_blocked:
                    score += self.weights["blocking"]
        return score

    def _is_piece_blocked(self, piece, board):
        for i in range(1, 3):
            if piece.pos + i < len(board.grid):
                next_cell = board.grid[piece.pos + i]
                if not next_cell.piece or next_cell.piece.color != self.player_color:
                    return False
            else:
                return False
        return True
    
    def _evaluate_future_risk(self, board, player):
        score = 0
        for cell in board.grid:
            if cell.piece and cell.piece.color == player.color:
                if cell.piece.pos == 25:
                    score -= 50  
                if cell.piece.pos == 24:
                    score -= 30  
        return score
