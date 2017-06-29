import MainPlatform

def drawACard(vm, om, log):
    playerIndex = vm.getValue("CurrentPlayerIndex")
    log.insert('insert', "Player " + str(playerIndex) + "'s turn\n")
    vm.setValue("State", "drawACard")
    player = om.getPlayer(playerIndex)
    player.draw("Deck", "Hand", 1)
    vm.setValue("State", "takeActions")
def takeActions(key, vm, om, log):
    playerIndex = vm.getValue("CurrentPlayerIndex")
    player = om.getPlayer(playerIndex)
    playedCard = player.hands["Hand"].cards[key]
    log.insert('insert', "Player " + str(playerIndex) + " played " + str(key) + '\n')
    
    handPileName = "P" + str(playerIndex) + "Hand"
    discardPileName = "P" + str(playerIndex) + "DiscardPile"
    om.moveCards(handPileName, discardPileName, [key])
class TurnManager:
    def __init__(self):
        pass
