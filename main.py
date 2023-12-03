from Model.Board import Board
from Controller.GameController import GameController
import os

def main():
    os.system("cls")
    gameController = GameController()
    gameController.StartGame()

if __name__ == "__main__":
    main()