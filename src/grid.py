from .cell.empty_cell import EmptyCell
from .cell.piece import Piece
from .cell.happines import HappinessCell
from .cell.horus import HorusCell
from .cell.rebirth import RebirthCell
from .cell.truths import ThreeTruthsCell
from .cell.water import WaterCell
from .cell.re_aotum import ReAtoumCell


class Grid:
    def __init__(self):
        self.rows = 3
        self.cols = 10
        self.grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.snake_path = []
        self.pieces = []
        self._generate_cells()
        self._build_snake_path()
        self._generate_pieces()

    def _generate_cells(self):
        idx = 1
        for r in range(self.rows):
            for c in range(self.cols):

                if idx == 16:
                    cell = RebirthCell(r, c)
                elif idx == 26:
                    cell = HappinessCell(r, c)
                elif idx == 27:
                    cell = WaterCell(r, c)
                elif idx == 28:
                    cell = ThreeTruthsCell(r, c)
                elif idx == 29:
                    cell = ReAtoumCell(r, c)
                elif idx == 30:
                    cell = HorusCell(r, c)
                else:
                    cell = EmptyCell(r, c)

                self.grid[r][c] = cell
                idx += 1


    def _build_snake_path(self):
        self.snake_path = []
        for r in range(self.rows):
            row = self.grid[r]
            if r== 1:      
                self.snake_path.extend(reversed(row))
            else:
                self.snake_path.extend(row)

    def _generate_pieces(self):
        for i in range(14):
            color = "BLACK" if i % 2 == 0 else "WHITE"
            piece = Piece(color, pos=i)
            cell = self.snake_path[i]
            cell.piece = piece
            self.pieces.append(piece)


    def display(self):
        for r in range(self.rows):
            row = self.grid[r]

            print("   ".join(
                cell.piece.symbol() if cell.piece else cell.symbol()
                for cell in row
            ))
            print()

