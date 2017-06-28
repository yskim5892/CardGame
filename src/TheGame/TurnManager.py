from ThePlatform import InputManager
from MainPlatform import MainPlatform

class TurnManager:
    def __init__(self):
        pass
    
    def drawACard(self, sv):
        playerIndex = sv["CurrenPlayerIndex"]
        print("Player " + str(playerIndex) + "'s turn")
        sv["State"] = "drawACard"
        player = MainPlatform.getObjectManager().getPlayers()[playerIndex]
        player.draw("Deck", "Hand", 1)
        sv["State"] = "takeActions"
        #print("Deck : ")
        #print(player.decks["Deck"].cards)
        #print("Hand : ")
        #print(player.hands["Hand"].cards)
        #print("Enter index of the card to use, or 'n' to skip : ")
        #c = InputManager.getInput()
        #if(c != 'n'):
            #playedCard = player.hands["Hand"].cards[int(c)]
            #print(playedCard)
            #player.hands["Hand"].cards.remove(playedCard)
    def takeActions(self, sv, key):
        playerIndex = sv["CurrenPlayerIndex"]
        player = MainPlatform.getObjectManager().getPlayers()[playerIndex]
        playedCard = player.hands["Hand"].cards[int(key)]
        print("Player " + str(playerIndex) + " played " + str(key))
        player.hands["Hand"].cards.remove(playedCard)