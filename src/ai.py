import copy

from src.player import Player
from src.heuristic import Heuristic

class AI(Player):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.depth = 2
        self.heuristic = Heuristic(self.color)
        # Probabilities of rolling 1, 2, 3, 4, or 5
        self.probs = {1: 0.25, 2: 0.375, 3: 0.25, 4: 0.0625, 5: 0.0625}

    def play(self, game_state):
        """
        Computes and returns the best move for the AI based on the expectiminimax algorithm.
        """
        move = self.compute_best_move(game_state)
        return move

    def compute_best_move(self, game_state):
        """
        Calculates the best move to make for a given dice roll.
        """
        game_instance = game_state["game_instance"]
        roll = game_state["roll"]
        moves = game_instance.get_available_moves(self, roll)
        
        if not moves:
            return None
        
        best_score = float('-inf')
        best_move = moves[0]
        
        for move in moves:
            temp_game = copy.deepcopy(game_instance)
            # Find the piece to move based on its position `move`
            piece_to_move = temp_game.get_piece_idx(move, temp_game.players[temp_game.current_player_index].pieces)
            if piece_to_move:
                temp_game.move_piece(piece_to_move.pos, roll)
                # After our move, it's the opponent's turn (minimizing player)
                score = self.expectiminimax(temp_game, self.depth - 1, False)
                if score > best_score:
                    best_score = score
                    best_move = move
        return best_move

    def expectiminimax(self, game_instance, depth, is_maximizing):
        """
        The main expectiminimax recursive function.
        """
        if depth == 0 or game_instance.is_game_over():
            return self.heuristic.evaluate(game_instance.get_game_state(0))
        
        # The next node is a chance node, representing the dice roll for the current player
        return self.chance_node(game_instance, depth, is_maximizing)

    def chance_node(self, game_instance, depth, is_maximizing):
        """
        Calculates the expected value from a chance node (dice roll).
        """
        expected_val = 0
        current_player_index = game_instance.current_player_index
        player = game_instance.players[current_player_index]

        for roll, prob in self.probs.items():
            moves = game_instance.get_available_moves(player, roll)
            
            if not moves:
                # If no moves are possible, the turn passes to the next player
                next_game_state = copy.deepcopy(game_instance)
                next_game_state.current_player_index = (current_player_index + 1) % len(next_game_state.players)
                roll_score = self.expectiminimax(next_game_state, depth - 1, not is_maximizing)
            else:
                # Find the best move for this roll (max for us, min for opponent)
                if is_maximizing:
                    best_roll_score = float('-inf')
                    for move in moves:
                        temp_game = copy.deepcopy(game_instance)
                        piece_to_move = temp_game.get_piece_idx(move, player.pieces)
                        if piece_to_move:
                            temp_game.move_piece(piece_to_move.pos, roll)
                            score = self.expectiminimax(temp_game, depth - 1, not is_maximizing)
                            best_roll_score = max(best_roll_score, score)
                    roll_score = best_roll_score
                else: # Minimizing player
                    best_roll_score = float('inf')
                    for move in moves:
                        temp_game = copy.deepcopy(game_instance)
                        piece_to_move = temp_game.get_piece_idx(move, player.pieces)
                        if piece_to_move:
                            temp_game.move_piece(piece_to_move.pos, roll)
                            score = self.expectiminimax(temp_game, depth - 1, not is_maximizing)
                            best_roll_score = min(best_roll_score, score)
                    roll_score = best_roll_score
            
            expected_val += prob * roll_score
            
        return expected_val