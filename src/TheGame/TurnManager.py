import MainPlatform

def drawACard(self, vm, om):
    playerIndex = vm["CurrenPlayerIndex"]
    print("Player " + str(playerIndex) + "'s turn")
    vm.setValue("State", "drawACard")
    player = om.getPlayers()[playerIndex]
    player.draw("Deck", "Hand", 1)
    vm.setValue("State", "takeActions")
def takeActions(self, key, vm, om):
    playerIndex = vm.getValue("CurrenPlayerIndex")
    player = om.getPlayers()[playerIndex]
    playedCard = player.hands["Hand"].cards[int(key)]
    print("Player " + str(playerIndex) + " played " + str(key))
    
    handPileName = "P" + str(key) + "Hand"
    discardPileName = "P" + str(key) + "DiscardPile"
    om.moveCards(handPileName, discardPileName, [key])
    player.hands["Hand"].cards.remove(playedCard)
class TurnManager:
    def __init__(self):
        pass
