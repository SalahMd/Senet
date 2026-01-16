from .cell import Cell


class RebirthCell(Cell):
    def __init__(self, pos):
        super().__init__(pos, "rebirth")


    def symbol(self):
        return "🚹"        
