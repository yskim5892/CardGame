from MainPlatform import MainPlatform

class Initializer:
    @staticmethod
    def initialize(self, sv):
        player0 = MainPlatform.getObjectManager().MakePlayer("p1")
        player1 = MainPlatform.getObjectManager().MakePlayer("p2")
        self.initializePlayer(player0, 0)
        self.initializePlayer(player1, 1)
        sv.setValue("CurrentPlayerIndex", 1)
        self.startGame()
    
    def initializePlayer(self, player, index):
        objectManager = MainPlatform.getObjectManager()
        hand = objectManager.MakePile("P" + str(index) + "Hand")
        deck = objectManager.MakePile("P" + str(index) + "Deck")
        objectManager.MakePile("P" + str(index) + "DiscardPile")
        for i in range(30): deck.addCard(objectManager.makeCard(60, 90))
        deck.shuffle()
        deck.setPos(800, 160 * (index + 1))
        deck.setValue("ViewType", "overlapped")
        hand.setPos(400, 160 * (index + 1))
        hand.setValue("ViewType", "horizontal")
        player.hands = {"Hand" : hand}
        player.decks = {"Deck" : deck}
        
    def startGame(self):
        self.gameData.players[0].draw("Deck", "Hand", 4)
        self.gameData.players[1].draw("Deck", "Hand", 4)
        while(True):
            print("Player " + str(self.gameData.currentPlayerIndex) + "'s turn")
            self.turnManager.executeTurn(self.gameData)
            self.gameData.currentPlayerIndex = (self.gameData.currentPlayerIndex + 1) % 2