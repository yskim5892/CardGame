import MainPlatform

def drawACard(vm, om, log):
    playerIndex = vm.getValue("CurrentPlayerIndex")
    log.insert('insert', "Player " + str(playerIndex) + "'s turn\n")
    
    handName = "P" + str(playerIndex) + "Hand"
    deckName = "P" + str(playerIndex) + "Deck"
    
    vm.setValue("State", "drawACard")
    om.moveCards(deckName, handName, [-1])
    vm.setValue("State", "takeActions")
    
def takeActions(cardName, vm, om, log):
    playerIndex = vm.getValue("CurrentPlayerIndex")
    log.insert('insert', "Player " + str(playerIndex) + " played " + cardName + '\n')
    
    handName = "P" + str(playerIndex) + "Hand"
    discardName = "P" + str(playerIndex) + "DiscardPile"
    om.moveCardsByName(handName, discardName, [cardName])