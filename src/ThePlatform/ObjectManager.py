# storage for in-game objects (eg. Cards, Piles ...)
# and functions about them
from . import Pile
from . import Card
from . import Player
class ObjectManager:
    def __init__(self, mainPlatform):
        self.piles = []
        self.players = []
        self.mainPlatform = mainPlatform

    def getPileByName(self, pileName):
        piles = [x for x in self.piles if x.getName() == pileName]
        if (len(piles) == 0):
            print("No pile with the name: " + pileName)
            return None
        return piles[0]

    def getPile(self, tags, values):
        piles = [x for x in self.piles 
                if x.hasTags(tags) and x.checkValues(tags)]

    def makePile(self, pileName, tags=[], values=dict()):
        pile = Pile.makePile(pileName, tags, values)
        self.piles.append(pile)
        return pile
    
    def makeCard(self, width, height):
        card = Card.Card()
        card.width = width
        card.height = height
        return card
    
    def makePlayer(self, playerName):
        player = Player.Player()
        self.players.append(player)
        return player
    def getPlayer(self, index):
        return self.players[index]
    
    def moveCards(self, fromPileName, toPileName, indices):
        viewManager = self.mainPlatform.viewManager
        fromPile = self.getPileByName(fromPileName)
        toPile = self.getPileByName(toPileName)
        viewManager.clearPile(fromPile)
        viewManager.clearPile(toPile)
        cards = []
        for i in indices : cards.append(fromPile.drawCard(i))
        for card in cards : toPile.addCard(card)
        viewManager.viewPile(fromPile)
        viewManager.viewPile(toPile)
        self.mainPlatform.triggerWhenCardsMoved(fromPile, toPile, cards)