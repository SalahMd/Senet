class Cell:
    def __init__(self, row, col, type="normal", value=None):
        self.row = row
        self.col = col
        self.type = type 
        self.value = value
        self.piece = None


    def is_occupied(self):
        return self.piece is not None

    def can_land(self, piece, state):
        return True

    def on_land(self, piece, state):
        pass

