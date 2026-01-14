class Cell:
    def __init__(self, row, type="normal"):
        self.row = row
        self.type = type 
        self.piece = None


    def is_occupied(self):
        return self.piece is not None

    def can_land(self, piece, state):
        return True

    def on_land(self, piece, state):
        pass

