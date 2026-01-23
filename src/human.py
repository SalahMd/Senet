from src.player import Player

class Human(Player):
    def play(self, game_state):
        roll = game_state["roll"]
        game_instance = game_state["game_instance"]        
        
        available_moves = game_instance.get_available_moves(self, roll)
        if len(available_moves) == 0:
            print("No legal moves")
            return None
        
        human_moves = []
        for move in available_moves:
            human_moves.append(move + 1)
        human_moves.sort()
        print("Your moves are at squares:", human_moves)

        while True:
            choice_str = input("Enter the square number (1-30) of the piece: ")
            
            if choice_str.isdigit():
                human_choice = int(choice_str)
                choice = human_choice - 1 
                
                if choice in available_moves:
                    return choice
                else:
                    print("Invalid choice. Please select from:", human_moves)
            else:
                print("Invalid input. Please enter a number (1-30).")