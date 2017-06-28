from ThePlatform import InputManager
from MainPlatform import MainPlatform

class TurnManager:
    def __init__(self):
        pass
    def drawACard(self, sv):
        playerIndex = sv["CurrenPlayerIndex"]
        print("Player " + str(playerIndex) + "'s turn")
        sv.getValue("State") = "drawACard"
        player = MainPlatform.getObjectManager().getPlayers()[playerIndex]
        player.draw("Deck", "Hand", 1)
        sv.getValue("State") = "takeActions"
    def takeActions(self, sv, key):
        playerIndex = sv.getValue("CurrenPlayerIndex")
        player = MainPlatform.getObjectManager().getPlayers()[playerIndex]
        playedCard = player.hands["Hand"].cards[int(key)]
        print("Player " + str(playerIndex) + " played " + str(key))
        
        handPileName = "P" + str(key) + "Hand"
        discardPileName = "P" + str(key) + "DiscardPile"
        MainPlatform.getObjectManager().moveCards(handPileName, discardPileName, [key])
        player.hands["Hand"].cards.remove(playedCard)