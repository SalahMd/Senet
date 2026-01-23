import copy

from src.player import Player
from src.heuristic import Heuristic

class AI(Player):
    def __init__(self, name, color, allow_print=True):
        super().__init__(name, color)
        self.depth = 2
        self.heuristic = Heuristic(self.color)
        self.probs = {1: 0.25, 2: 0.375, 3: 0.25, 4: 0.0625, 5: 0.0625}
        self.visited_nodes = 0
        self.allow_print = allow_print

    def play(self, game_state):
        move = self.compute_best_move(game_state)
        return move

    def compute_best_move(self, game_state):
        game_instance = game_state["game_instance"]
        roll = game_state["roll"]
        
        self.visited_nodes = 0
        if self.allow_print:
            print(f"\nAI started Roll: {roll}")

        moves = game_instance.get_available_moves(self, roll)
        
        if not moves:
            if self.allow_print:
                print("No valid moves available.")
            return None
        
        best_score = float('-inf')
        best_move = moves[0]
        
        for move in moves:
            temp_game = copy.deepcopy(game_instance)
            piece_to_move = temp_game.get_piece_idx(move, temp_game.players[temp_game.current_player_index].pieces)
            if piece_to_move:
                if self.allow_print:
                    print(f"Evaluating root move from square {move + 1}...")
                temp_game.move_piece(piece_to_move.pos, roll)
                score = self.expectiminimax(temp_game, self.depth - 1, False)
                if self.allow_print:
                    print(f"Move from square {move + 1} score: {score:.2f}")
                
                if score > best_score:
                    best_score = score
                    best_move = move
                    
        if self.allow_print:
            print(f"Computation complete. Total Visited Nodes: {self.visited_nodes}")
            print(f"Best Move: {best_move + 1} with Score: {best_score:.2f}\n")
        return best_move

    def expectiminimax(self, game_instance, depth, is_maximizing, is_chance_node=False, indent=""):
        self.visited_nodes += 1
        indent += "  "

        if game_instance.is_game_over():
            if len(self.pieces) == 0:
                return float('inf') 
            else:
                return float('-inf') 
                
        if depth == 0:
            eval_score = self.heuristic.evaluate(game_instance.get_game_state(None))
            if self.allow_print:
                print(f"{indent}Max depth reached Heuristic Evaluation: {eval_score:.2f}")
            return eval_score
            
        return self.chance_node(game_instance, depth, is_maximizing, indent)
    

    def chance_node(self, game_instance, depth, is_maximizing, indent=""):
        expected_val = 0
        current_player_index = game_instance.current_player_index
        player = game_instance.players[current_player_index]
        
        node_type = "MAX" if is_maximizing else "MIN"
        if self.allow_print:
            print(f"{indent}CHANCE / {node_type} NODE Depth {depth}.")

        for roll, prob in self.probs.items():
            moves = game_instance.get_available_moves(player, roll)
            
            if not moves:
                next_game_state = copy.deepcopy(game_instance)
                next_game_state.current_player_index = (current_player_index + 1) % len(next_game_state.players)
                roll_score = self.expectiminimax(next_game_state, depth - 1, not is_maximizing, False, indent)
            else:
                if is_maximizing:
                    best_roll_score = float('-inf')
                    for move in moves:
                        temp_game = copy.deepcopy(game_instance)
                        piece_to_move = temp_game.get_piece_idx(move, player.pieces)
                        if piece_to_move:
                            temp_game.move_piece(piece_to_move.pos, roll)
                            score = self.expectiminimax(temp_game, depth - 1, not is_maximizing, False, indent)
                            best_roll_score = max(best_roll_score, score)
                    roll_score = best_roll_score
                else:
                    best_roll_score = float('inf')
                    for move in moves:
                        temp_game = copy.deepcopy(game_instance)
                        piece_to_move = temp_game.get_piece_idx(move, player.pieces)
                        if piece_to_move:
                            temp_game.move_piece(piece_to_move.pos, roll)
                            score = self.expectiminimax(temp_game, depth - 1, not is_maximizing, False, indent)
                            best_roll_score = min(best_roll_score, score)
                    roll_score = best_roll_score
            
            if self.allow_print:
                print(f"{indent}  Roll {roll} (Prob {prob}) resulting score: {roll_score:.2f}")
            expected_val += prob * roll_score
            
        if self.allow_print:
            print(f"{indent}CHANCE / {node_type} NODE Expected value returned: {expected_val:.2f}")
        return expected_val