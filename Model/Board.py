from abc import ABC, abstractmethod
from Model.Ship import Ship

class AbstractBoard(ABC):
    def __init__(self):
        pass
    def PlaceShip(self, ship, row, column, orientation):
        pass
    def ReceiveAttack(self, row, column):
        pass
    def IsGameOver(self):
        pass

class Board(AbstractBoard):
    def __init__(self):
        super().__init__()
        self.size = 10
        self.board = [[" " for columns in range(self.size)] for lines in range(self.size)]
    
    def PlaceShip(self, ship, row, column, orientation):
        if orientation == "horizontal" and row < self.size and (column + 2) < self.size:
            for i in range(ship.size):
                if (self.board[row][column + i] == " "):
                    self.board[row][column + i] = ship
                else:
                    for k in range (i - 1, -1, -1):
                        self.board[row][column + k] = " "
                    return False 
            return True
        elif orientation == "vertical" and (row + 2) < self.size and column < self.size:
            for i in range(ship.size):
                if (self.board[row + i][column] == " "):
                    self.board[row + i][column] = ship
                else:
                    for k in range (i - 1, -1, -1):
                        self.board[row + k][column] = " "
                    return False 

            return True
        else:
            return False
    
    def ReceiveAttack(self, row, column):
        if isinstance(self.board[row][column], Ship):
            self.board[row][column] = "X"
            return True
        self.board[row][column] = "~"
        return False

    def IsGameOver(self):
        for row in self.board:
            for cell in row:
                if isinstance(cell, Ship):
                    return False
        return True

