from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        self.pieces = []

    @abstractmethod
    def play(self, game_state):
        pass