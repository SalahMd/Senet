class Piece:
    def __init__(self, color, pos=None):
        self.color = color
        self.pos = pos
        self.passed_happiness = False
        self.on_three_truths = False
        self.on_reatoum = False
        self.on_horus = False

    def update_position(self, pos):
        self.pos = pos

    def opponent(self):
        return "BLACK" if self.color == "WHITE" else "WHITE"
    
    def symbol(self):
        return "⚪" if self.color == "WHITE" else "⚫"
