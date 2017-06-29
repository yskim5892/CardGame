import MainPlatform

def drawACard(self, sv):
    mainPlatform = MainPlatform.m
    playerIndex = sv["CurrenPlayerIndex"]
    print("Player " + str(playerIndex) + "'s turn")
    sv.setValue("State", "drawACard")
    player = mainPlatform.getObjectManager().getPlayers()[playerIndex]
    player.draw("Deck", "Hand", 1)
    sv.setValue("State", "takeActions")
def takeActions(self, sv, key):
    mainPlatform = MainPlatform.m
    playerIndex = sv.getValue("CurrenPlayerIndex")
    player = mainPlatform.getObjectManager().getPlayers()[playerIndex]
    playedCard = player.hands["Hand"].cards[int(key)]
    print("Player " + str(playerIndex) + " played " + str(key))
    
    handPileName = "P" + str(key) + "Hand"
    discardPileName = "P" + str(key) + "DiscardPile"
    mainPlatform.getObjectManager().moveCards(handPileName, discardPileName, [key])
    player.hands["Hand"].cards.remove(playedCard)
class TurnManager:
    def __init__(self):
        pass
