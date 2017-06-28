from MainPlatform import MainPlatform

class Initializer:
    @staticmethod
    def initialize(self, sv):
        player0 = MainPlatform.getObjectManager().MakePlayer("p1")
        player1 = MainPlatform.getObjectManager().MakePlayer("p2")
        self.initializePlayer(player0, 0, sv)
        self.initializePlayer(player1, 1, sv)
        sv["CurrentPlayerIndex"] = 1
        self.startGame()
    
    def initializePlayer(self, player, index, dict):
        w = dict["ScreenWidth"]
        h = dict["ScreenHeight"]
        hand = MainPlatform.getObjectManager().MakePile("P" + str(index) + "Hand")
        deck = MainPlatform.getObjectManager().MakePile("P" + str(index) + "Deck")
        for i in range(30): deck.addCard(i)
        deck.shuffle()
        deck.setPos( (w * 2)/3, h/5)
        deck.setValue("ViewType", "overlapped")
        hand.setPos( w/3, h/5)
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