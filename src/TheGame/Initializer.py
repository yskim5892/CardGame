import MainPlatform

def initialize():
    mainPlatform = MainPlatform.m
    player0 = mainPlatform.getObjectManager().makePlayer("P0")
    player1 = mainPlatform.getObjectManager().makePlayer("P1")
    initializePlayer(player0, 0)
    initializePlayer(player1, 1)
    mainPlatform.getVariableManager().setValue("CurrentPlayerIndex", 1)
    startGame()
def initializePlayer(player, index):
    objectManager = MainPlatform.m.getObjectManager()
    hand = objectManager.makePile("P" + str(index) + "Hand")
    deck = objectManager.makePile("P" + str(index) + "Deck")
    objectManager.makePile("P" + str(index) + "DiscardPile")
    for i in range(30): deck.addCard(objectManager.makeCard(60, 90))
    deck.shuffle()
    deck.setPos(800, 160 * (index + 1))
    deck.setValue("ViewType", "overlapped")
    hand.setPos(400, 160 * (index + 1))
    hand.setValue("ViewType", "horizontal")
    player.hands = {"Hand" : hand}
    player.decks = {"Deck" : deck}
    
def startGame():
    objectManager = MainPlatform.m.getObjectManager()
    objectManager.getPlayer["P0"].draw("Deck", "Hand", 4)
    objectManager.getPlayer["P1"].draw("Deck", "Hand", 4)
    