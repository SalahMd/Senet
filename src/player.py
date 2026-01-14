from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name: str):
        self.name = name
        self.pieces = [] 
    @abstractmethod
    def play(self, game_state):
        """
        Perform a move.
        Must be implemented by subclasses.
        """
        pass
