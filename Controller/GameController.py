from abc import ABC, abstractmethod
from Model.Player import Player, Computer
from View.GameView import GameView
import os

class AbstractGameController(ABC):
    def __init__(self):
        pass
    def StartGame(self):
        pass
    def TakePlayerTurn(self):
        pass
    def TakeComputerTurn(self):
        pass

class GameController(AbstractGameController):
    def __init__(self):
        super().__init__()
    
    def StartGame(self):
        view = GameView()
        self.view = view

        self.view.DisplayMessage("* BATALHA NAVAL *")
        self.view.DisplayMessage("")
        self.view.DisplayMessage("Regras:")
        self.view.DisplayMessage("- O jogo é dividido em turnos: um do jogador e um do computador;")
        self.view.DisplayMessage("- Cada jogador tem 3 navios (3x1 unidades de tamanho);")
        self.view.DisplayMessage("- Cada jogador tem 1 tiro por turno;")
        self.view.DisplayMessage("- Quando os 3 navios de um jogador foram completamente alvejados, o jogo acabará.")
        self.view.PressEnterToContinue()

        playerName = input("Entre com seu nome de jogador: ")
        player = Player(playerName)
        computer = Computer("Computador")
        self.view.DisplayMessage("Boa sorte, {}!".format(playerName))
        self.view.PressEnterToContinue()

        self.player = player
        self.computer = computer
        self.player.PlaceShips()
        self.computer.PlaceShips()

        while not self.player.board.IsGameOver() and not self.computer.board.IsGameOver():
            self.TakePlayerTurn()
            if not self.computer.board.IsGameOver():
                self.TakeComputerTurn()
        winner = self.player.name
        if (self.player.board.IsGameOver()):
            winner = self.computer.name
        view.DisplayMessage("FIM DE JOGO!")
        view.DisplayMessage("E o vencedor é...")
        view.DisplayMessage(winner.upper())
        view.PressEnterToContinue()

    def TakePlayerTurn(self):
        self.view.CleanScreen()
        self.view.DisplayMessage(f"TURNO DE {self.player.name.upper()}")
        self.view.DisplayMessage("")
        self.view.DisplayBoard(self.computer.board)
        self.view.DisplayMessage("")
        result = self.player.MakeMove(self.computer.board)
        if result:
            self.view.DisplayMessage("Ataque bem-sucedido!")
        else:
            self.view.DisplayMessage("Tiro na água...")
        self.view.PressEnterToContinue()
    
    def TakeComputerTurn(self):
        self.view.CleanScreen()
        self.view.DisplayMessage(f"TURNO DE {self.computer.name.upper()}")
        self.view.DisplayMessage("")
        self.view.DisplayBoard(self.player.board)
        self.view.DisplayMessage("")
        result = self.computer.MakeMove(self.player.board)
        if result:
            self.view.DisplayMessage("Ataque bem-sucedido!")
        else:
            self.view.DisplayMessage("Tiro na água...")
        self.view.PressEnterToContinue()