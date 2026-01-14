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
        self.cells = self.rows * self.cols

        self.grid = [None for _ in range(self.cells)]
        self.pieces = []

        self.generate_cells()
        self.generate_pieces()

    # -------------------------
    # Generate cells (1D)
    # -------------------------
    def generate_cells(self):
        for idx in range(self.cells):
            pos = idx + 1  # game numbering (1 → 30)

            if pos == 16:
                cell = RebirthCell(idx)
            elif pos == 26:
                cell = HappinessCell(idx)
            elif pos == 27:
                cell = WaterCell(idx)
            elif pos == 28:
                cell = ThreeTruthsCell(idx)
            elif pos == 29:
                cell = ReAtoumCell(idx)
            elif pos == 30:
                cell = HorusCell(idx)
            else:
                cell = EmptyCell(idx)

            self.grid[idx] = cell

    # -------------------------
    # Pieces
    # -------------------------
    def generate_pieces(self):
        for i in range(14):
            color = "BLACK" if i % 2 == 0 else "WHITE"
            piece = Piece(color, pos=i)
            self.grid[i].piece = piece
            self.pieces.append(piece)

    # ======================================================
    # 1D → 2D (snake layout)
    # ======================================================
    def to_2d(self, idx):
        row = idx // self.cols
        col = idx % self.cols

        if row % 2 == 1:
            col = self.cols - 1 - col

        return row, col

    # ======================================================
    # Print grid as 2D (VIEW ONLY)
    # ======================================================
    def display(self):
        for r in range(self.rows):
            row_cells = []

            for c in range(self.cols):
                idx = self.to_1d(r, c)
                cell = self.grid[idx]

                if cell.piece:
                    row_cells.append(cell.piece.symbol())
                else:
                    row_cells.append(cell.symbol())

            print("   ".join(row_cells))
            print()

    # ======================================================
    # 2D → 1D (snake layout)
    # ======================================================
    def to_1d(self, row, col):
        if row % 2 == 1:
            col = self.cols - 1 - col
        return row * self.cols + col
