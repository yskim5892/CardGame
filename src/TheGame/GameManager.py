from TheGame.TurnManager import TurnManager
from ThePlatform.Pile import Pile
from ThePlatform.Player import Player
from TheGame.GameData import GameData

class GameManager:
    def __init__(self):
        self.gameData = GameData()
        self.turnManager = TurnManager()
        player1 = Player()
        player2 = Player()
        self.initializePlayer(player1)
        self.initializePlayer(player2)
        self.gameData.players = [player1, player2]
    
    def initializePlayer(self, player):
        hand = Pile()
        deck = Pile()
        for i in range(30): deck.addCard(i)
        deck.shuffle()
        player.hands = {"Hand" : hand}
        player.decks = {"Deck" : deck}
        
    def startGame(self):
        self.gameData.players[0].draw("Deck", "Hand", 4)
        self.gameData.players[1].draw("Deck", "Hand", 4)
        while(True):
            print("Player " + str(self.gameData.currentPlayerIndex) + "'s turn")
            self.turnManager.executeTurn(self.gameData)
            self.gameData.currentPlayerIndex = (self.gameData.currentPlayerIndex + 1) % 2
            
            
gameManager = GameManager()
gameManager.startGame()