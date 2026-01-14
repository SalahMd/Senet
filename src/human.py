from .player import Player


class Human(Player):
    def play(self, game_state):
        print(f"{self.name} Human Turn:")
        
        while True:
            try:
                move_str = input("Enter the index of the piece you want to move: ")
                move = int(move_str)
                # A proper implementation should also check if the move is valid
                # (e.g., if the player has a piece at that index)
                return move
            except ValueError:
                print("Invalid input. Please enter a number.")
