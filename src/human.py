from player import Player


class Human(Player):
    def play(self, game_state):
        # Example: input-driven move
        print(f"{self.name} (Human) is playing...")
        
        # return a move (depends on your game design)
        move = input("Enter your move: ")
        return move
