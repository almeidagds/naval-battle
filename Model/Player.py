from abc import ABC, abstractmethod
import random
from Model.Board import Board
from Model.Ship import Ship
import string

class AbstractPlayer(ABC):
    def __init__(self):
        pass
    def PlaceShips(self):
        pass
    def MakeMove(self, opponentBoard):
        pass

class Player(AbstractPlayer):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.board = Board()

    def PlaceShips(self):
        for index in range(3):
            shipWasSuccessfullyPositioned = False
            while (not shipWasSuccessfullyPositioned):
                size = 3
                position = input("Entre com a linha e coluna que deseja posicionar o {}º navio (Ex.: B3): ".format(index + 1))
                row = list(string.ascii_uppercase).index(position[0].upper())
                column = int(position[1:]) - 1
                orientation = input("Entre com a orientação do {}º navio ('vertical' ou 'horizontal'): ".format(index + 1))
                ship = Ship(size)
                shipWasSuccessfullyPositioned = self.board.PlaceShip(ship, row, column, orientation)
                if not shipWasSuccessfullyPositioned:
                    print("* ERRO *")
                    print("Coordenadas incorretas, navio fora do tabuleiro ou já existe um navio posicionado em uma das células. Tente novamente.\n")
                else:
                    print("Navio posicionado com sucesso!\n")

    def MakeMove(self, opponentBoard):
        while True:
            try:
                position = input("Entre com a linha e coluna que deseja realizar o ataque (Ex.: B3): ")
                row = list(string.ascii_uppercase).index(position[0].upper())
                column = int(position[1:]) - 1
                isCoordinateInRange = 0 <= row < opponentBoard.size and 0 <= column < opponentBoard.size
                isCellAlreadyAttacked = opponentBoard.board[row][column] == "X" or opponentBoard.board[row][column] == "~"
                if not isCoordinateInRange:
                    print("Coordenadas fora do alcance! Tente novamente!")
                elif isCellAlreadyAttacked:
                    print("A célula escolhida já foi atacada! Tente novamente!")
                else:
                    return opponentBoard.ReceiveAttack(row, column)
            except Exception as exception:
                print("Entrada inválida: ")
                print(exception)

class Computer(AbstractPlayer):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.board = Board()

    def PlaceShips(self):
        for ship in range(3):
            shipWasSuccessfullyPositioned = False
            while (shipWasSuccessfullyPositioned == False):
                size = 3
                row = random.randint(0, self.board.size)
                column = random.randint(0, self.board.size)
                if (random.randint(0,2)):
                    orientation = "horizontal"
                else:
                    orientation = "vertical"
                ship = Ship(size)
                shipWasSuccessfullyPositioned = self.board.PlaceShip(ship, row, column, orientation)

    def MakeMove(self, opponentBoard):
        while True:
            try:
                row = random.randint(0, opponentBoard.size - 1)
                column = random.randint(0, opponentBoard.size - 1)
                print("O {} atacou a célula {}{}...".format(self.name, list(string.ascii_uppercase)[row], column + 1))
                if 0 <= row < opponentBoard.size and 0 <= column < opponentBoard.size:
                    return opponentBoard.ReceiveAttack(row, column)
                else:
                    print("Coordenadas fora do alcance! Tente novamente!")
            except:
                print("Entrada inválida! Tente novamente!")