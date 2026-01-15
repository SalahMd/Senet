from src.player import Player

class Human(Player):
    def play(self, game_state):
        roll = game_state["roll"]
        game_instance = game_state["game_instance"]        
        available_moves = game_instance.get_available_moves(self, roll)
        
        if not available_moves:
            print("No legal moves available")
            return None
        print(f"Your movable pieces are at squares: {[m + 1 for m in sorted(available_moves)]}")
        
        while True:
            try:
                choice_str = input(f"Enter the square number (1-30) of the piece: ")
                choice = int(choice_str) - 1 # Convert to 0-based index
                
                if choice in available_moves:
                    return choice
                else:
                    print(f"Invalid choice Please select from: {[m + 1 for m in sorted(available_moves)]}")
            
            except ValueError:
                print("Invalid input. Please enter a number (1-30)")