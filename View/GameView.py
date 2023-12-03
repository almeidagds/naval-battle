from abc import ABC, abstractmethod
from Model.Board import Board
from Model.Ship import Ship
import string
import os

class AbstractGameView(ABC):
    def __init__(self):
        pass

    def DisplayBoard(self, board):
        pass

    def DisplayMessage(self, message):
        pass

    def PressEnterToContinue(self):
        pass
    
    def CleanScreen(self):
        pass

class GameView(AbstractGameView):
    def __init__(self):
        super().__init__()

    def DisplayBoard(self, board):
        numberOfLines = len(board.board)
        numberOfColumns = len(board.board[0])
        alphabet = list(string.ascii_uppercase)

        for line in range(numberOfLines + 1):
            for column in range(numberOfColumns + 1):
                if (line == 0):
                    print("{}   ".format(column or " "), end="")
                else:
                    if (column == 0):
                        print(" {} ".format(alphabet[line - 1] or ""), end = "")
                    else:
                        if isinstance(board.board[line-1][column-1], Ship) :
                            value = "A"
                        else:
                            value = board.board[line-1][column-1]
                        print("[{}]".format(value or " "), end = " ")
            print("")

    def DisplayMessage(self, message):
        print("{}".format(message))

    def PressEnterToContinue(self):
        self.DisplayMessage("")
        input("[Aperte ENTER para continuar]\n")
        self.CleanScreen()
    
    def CleanScreen(self):
        os.system("cls")