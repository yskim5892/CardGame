from TheGame.TurnManager import TurnManager
from ThePlatform.Player import Player

class GameManager:
    def __init__(self):
        turnManager = TurnManager()
        player1 = Player()
        player2 = Player()
        players = [player1, player2]