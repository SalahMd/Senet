from src.grid import Grid
from src.game import Game
from src.dice import Dice
from src.human import Human
from src.ai import AI

def main():
    grid = Grid()
    dice = Dice()
    player1 = Human("Player 1", color="BLACK")
    player2 = AI("AI Computer", color="WHITE")

    player1.pieces = [cell.piece for cell in grid.grid if cell.piece and cell.piece.color == "BLACK"]
    player2.pieces = [cell.piece for cell in grid.grid if cell.piece and cell.piece.color == "WHITE"]
    players = [player1, player2]
    
    game = Game(players, grid, dice)
    grid.display()
    game.start()

if __name__ == "__main__":
    main()