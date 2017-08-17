import MainPlatform
from TheGame import TurnManager

def initialize(vm, om, log):
    player0 = om.makePlayer("P0")
    player1 = om.makePlayer("P1")
    initializePlayer(player0, 0, om)
    initializePlayer(player1, 1, om)
    vm.setValue("CurrentPlayerIndex", 1)
    startGame(vm, om, log)
def initializePlayer(player, index, om):
    handName = "P" + str(index) + "Hand"
    deckName = "P" + str(index) + "Deck"
    discardPileName = "P" + str(index) + "DiscardPile"
    hand = om.makePile(handName)
    deck = om.makePile(deckName)
    om.makePile("P" + str(index) + "DiscardPile")
    for i in range(30): om.makeCard(deckName, "P" + str(index) + "C" + str(i), 60, 90)
    om.shufflePile(deckName)
    om.setPosOfPile(deckName, 850, 160 * (index + 1))
    om.setViewTypeOfPile(deckName, "overlapped")
    om.setPosOfPile(handName, 500, 160 * (index + 1))
    om.setViewTypeOfPile(handName, "horizontal")
    om.setPosOfPile(discardPileName, 150, 160 * (index + 1))
    om.setViewTypeOfPile(discardPileName, "overlapped")
    player.hands = {"Hand" : hand}
    player.decks = {"Deck" : deck}
    
def startGame(vm, om, log):
    for i in range(2):
        handName = "P" + str(i) + "Hand"
        deckName = "P" + str(i) + "Deck"
        om.moveCards(deckName, handName, [-1, -2, -3, -4])
    TurnManager.drawACard(vm, om, log)