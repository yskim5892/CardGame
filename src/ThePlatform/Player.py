
class Player:
    def __init__(self):
        pass

    def draw(self, deckName, handName, number):
        for i in range(number) : self.hands[handName].addCard(self.decks[deckName].drawCard())
