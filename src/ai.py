from .player import Player


class AI(Player):
    def play(self, game_state):
        print(f"{self.name} (AI) is thinking...")

        # Placeholder for AI logic (minimax / expectiminimax)
        move = self.compute_best_move(game_state)
        return move

    def compute_best_move(self, game_state):
        # TODO: implement AI logic
        return "AI_MOVE"
