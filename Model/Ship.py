from abc import ABC, abstractmethod

class AbstractShip(ABC):
    def __init__(self):
        pass
    def IsSunk(self, hits):
        pass

class Ship(AbstractShip):
    def __init__(self, size):
        super().__init__()
        self.size = size
