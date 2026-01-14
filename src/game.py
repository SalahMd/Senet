class Game:
    def __init__(self, players, board, dice):
        self.players = players
        self.board = board
        self.dice = dice
        self.current_player_index = 0

    def start(self):
        while not self.is_game_over():
            current_player = self.players[self.current_player_index]
            roll = self.dice.roll()
            idx = current_player.play(self.get_game_state(roll))
            self.current_player_index = (self.current_player_index + 1) % len(self.players)


    def move_piece(self, piece_idx, roll):
        piece_object = self.get_piece_idx(piece_idx, self.players[self.current_player_index].pieces)

        next_idx = piece_idx + roll 

        # check if the cell is empty 


        # check if there is another player in this cell, if so swap it

        # check 
    def is_game_over(self):
        # Implement game over logic
        return False

    def get_game_state(self, roll):
        # Return the current game state including the roll
        return {
            "board": self.board,
            "roll": roll,
            "players": self.players,
        }  
    
    def get_piece_idx(self, piece_idx, pieces):
        for piece in pieces:
            if piece.pos == piece_idx:
                return piece
        return None