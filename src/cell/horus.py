from .cell import Cell


class HorusCell(Cell):
    def __init__(self, row):
        super().__init__(row, "horus")
    def can_exit(self, roll):
        return True
    
    def symbol(self):
        if self.piece:
            return "🦅"
        return " 🏁"
