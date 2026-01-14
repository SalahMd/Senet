class Piece:
    def __init__(self, color, pos=None):
        self.color = color
        self.pos = pos

    def update_position(self, pos, snake_path):
        self.pos = pos
        cell = snake_path[pos]

    def opponent(self):
        return "BLACK" if self.color == "WHITE" else "WHITE"
    
    def symbol(self):
        return "⚪" if self.color == "WHITE" else "⚫"
