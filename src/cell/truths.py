from .cell import Cell


class ThreeTruthsCell(Cell):
    def __init__(self, row, col):
        super().__init__(row, col, "truths")
    def can_exit(self, roll):
        return roll == 3
    
    def symbol(self):
        if self.piece:
            return "3️⃣"
        return "3️⃣"

