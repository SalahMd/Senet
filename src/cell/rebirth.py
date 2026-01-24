from .cell import Cell


class RebirthCell(Cell):
    def __init__(self, pos):
        super().__init__(pos, "rebirth")

    def is_rebirth_empty(self):
            return not self.is_occupied()
    
    def get_nearest_empty_cell_before_rebirth(self,grid):
        for i in range(14, -1, -1):
            if not grid[i].is_occupied():
                return i
        return None

    def symbol(self):
        return "🚹"        
