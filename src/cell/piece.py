class Piece:
    def __init__(self, color, pos=None, row=None, col=None):
        self.color = color
        self.pos = pos
        self.row = row
        self.col = col

    def update_position(self, pos, snake_path):
        self.pos = pos
        cell = snake_path[pos]
        self.row = cell.row
        self.col = cell.col

    def opponent(self):
        return "BLACK" if self.color == "WHITE" else "WHITE"
    
    def symbol(self):
        return "⚪" if self.color == "WHITE" else "⚫"
