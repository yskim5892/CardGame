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
    hand = om.makePile("P" + str(index) + "Hand")
    deck = om.makePile("P" + str(index) + "Deck")
    om.makePile("P" + str(index) + "DiscardPile")
    for i in range(30): deck.addCard(om.makeCard(60, 90))
    deck.shuffle()
    deck.setPos(800, 160 * (index + 1))
    deck.setValue("ViewType", "overlapped")
    hand.setPos(400, 160 * (index + 1))
    hand.setValue("ViewType", "horizontal")
    player.hands = {"Hand" : hand}
    player.decks = {"Deck" : deck}
    
def startGame(vm, om, log):
    om.getPlayer(0).draw("Deck", "Hand", 4)
    om.getPlayer(1).draw("Deck", "Hand", 4)
    TurnManager.drawACard(vm, om, log)