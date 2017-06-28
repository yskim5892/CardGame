# storage for in-game objects (eg. Cards, Piles ...)
# and functions about them
from . import Pile
from ThePlatform.Card import Card

class ObjectManager:
    def __init__(self):
        self.piles = []

    def getPileByName(self, pileName):
        piles = [x for x in self.piles if x.getName() == pileName]
        if (piles.len(0)):
            print("No pile with the name: " + pileName)
            return None
        return piles[0]

    def getPile(self, tags, values):
        piles = [x for x in self.piles 
                if x.hasTags(tags) and x.checkValues(tags)]

    def makePile(self, pileName, tags=[], values=dict()):
        self.piles.append(Pile.makePile(pileName, tags, values))
    
    def makeCard(self, width, height):
        card = Card()
        card.width = width
        card.height = height
        return card
    
    def moveCards(self, fromPileName, toPileName, indices):
        fromPile = self.getPileByName(fromPileName)
        toPile = self.getPileByName(toPileName)
        for i in indices : toPile.addcard(fromPile.drawCard(i))