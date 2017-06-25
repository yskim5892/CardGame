from ThePlatform import InputManager

class TurnManager:
    def __init__(self):
        pass
    
    def executeTurn(self, gameData):
        player = gameData.players[gameData.currentPlayerIndex]
        player.draw("Deck", "Hand", 1)
        print("Deck : ")
        print(player.decks["Deck"].cards)
        print("Hand : ")
        print(player.hands["Hand"].cards)
        print("Enter index of the card to use, or 'n' to skip : ")
        c = InputManager.getInput()
        if(c != 'n'):
            playedCard = player.hands["Hand"].cards[int(c)]
            print(playedCard)
            player.hands["Hand"].cards.remove(playedCard)