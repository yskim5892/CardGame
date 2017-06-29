import MainPlatform

def drawACard(vm, om, log):
    playerIndex = vm.getValue("CurrentPlayerIndex")
    log.insert('insert', "Player " + str(playerIndex) + "'s turn\n")
    
    handName = "P" + str(playerIndex) + "Hand"
    deckName = "P" + str(playerIndex) + "Deck"
    
    vm.setValue("State", "drawACard")
    om.moveCards(deckName, handName, [-1])
    vm.setValue("State", "takeActions")
def takeActions(key, vm, om, log):
    playerIndex = vm.getValue("CurrentPlayerIndex")
    player = om.getPlayer(playerIndex)
    playedCard = player.hands["Hand"].cards[key]
    log.insert('insert', "Player " + str(playerIndex) + " played " + str(key) + '\n')
    
    handName = "P" + str(playerIndex) + "Hand"
    discardName = "P" + str(playerIndex) + "DiscardPile"
    om.moveCards(handName, discardName, [key])