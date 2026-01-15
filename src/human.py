from .player import Player


class Human(Player):
    def play(self, game_state):
        print(f"{self.name} Human Turn:")
        
        while True:
            try:
                row_str = input("Enter the row of the piece you want to move: ")
                col_str = input("Enter the column of the piece you want to move: ")
                row = int(row_str)
                col = int(col_str)
                
                # Convert 2D coordinates to 1D index
                board = game_state["board"]
                move = board.to_1d(row, col)
                
                # A proper implementation should also check if the move is valid
                # (e.g., if the player has a piece at that index)
                return move
            except ValueError:
                print("Invalid input. Please enter a number.")
            except IndexError:
                print("Invalid row or column. Please enter valid coordinates.")
