from src.grid import Grid
from src.game import Game
from src.dice import Dice
from src.human import Human

def main():
    # 1. Initialize game components
    grid = Grid()
    dice = Dice()
    
    # 2. Create players
    player1 = Human("Player 1 (Black)")
    player2 = Human("Player 2 (White)")
    
    # 3. Assign pieces to players
    player1.pieces = [piece for piece in grid.pieces if piece.color == "BLACK"]
    player2.pieces = [piece for piece in grid.pieces if piece.color == "WHITE"]
    
    players = [player1, player2]
    
    # 4. Create and start the game
    game = Game(players, grid, dice)
    
    print("Initial board layout:")
    grid.display()
    
    game.start()

if __name__ == "__main__":
    main()