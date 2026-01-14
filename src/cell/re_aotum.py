from .cell import Cell


class ReAtoumCell(Cell):
    def __init__(self, row):
        super().__init__(row, "re_aotum")
    def can_exit(self, roll):
        return roll == 2
    
    def symbol(self):
        if self.piece:
            return "2️⃣"
        return " 2️⃣"
