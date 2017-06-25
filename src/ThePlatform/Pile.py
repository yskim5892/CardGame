import random

class Pile(Taggable, Valueable):
    def __init__(self):
        pass

    def shuffle(self):
        try:
            random.shuffle(self.cards)
        except AttributeError:
            return

    def addCard(self, card):
        try:
            self.cards.append(card)
        except AttributeError:
            self.cards = [card]


    def drawCard(self):
        try:
            return self.cards.pop(-1)
        except AttributeError:
            return

a = Pile()

a.addCard(3)
a.addCard(7)
a.addCard(23)
a.addCard(25)

print(a.cards)

a.shuffle()

print(a.cards)

print(a.drawCard())
print(a.drawCard())
print(a.cards)
