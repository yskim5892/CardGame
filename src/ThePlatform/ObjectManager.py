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
        self.viewManager = mainPlatform.viewManager

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
    
    def makeCard(self, pileName, width, height):
        pile = self.getPileByName(pileName)
        card = Card.Card()
        card.width = width
        card.height = height
        
        self.viewManager.clearPile(pile)
        pile.addCard(card)
        self.viewManager.viewPile(pile)
        
        return card
    
    def makePlayer(self, playerName):
        player = Player.Player()
        self.players.append(player)
        return player
    def getPlayer(self, index):
        return self.players[index]
    
    def moveCards(self, fromPileName, toPileName, indices):
        fromPile = self.getPileByName(fromPileName)
        toPile = self.getPileByName(toPileName)
        
        self.viewManager.clearPile(fromPile)
        self.viewManager.clearPile(toPile)
        cards = []
        for i in indices : cards.append(fromPile.drawCard(i))
        for card in cards : toPile.addCard(card)
        self.viewManager.viewPile(fromPile)
        self.viewManager.viewPile(toPile)
        
        self.mainPlatform.triggerWhenCardsMoved(fromPile, toPile, cards)
        
    def shufflePile(self, PileName):
        pile = self.getPileByName(PileName)
        
        self.viewManager.clearPile(pile)
        pile.shuffle()
        self.viewManager.viewPile(pile)
    
    def setPosOfPile(self, PileName, x, y):
        pile = self.getPileByName(PileName)
        
        self.viewManager.clearPile(pile)
        pile.setPos(x, y)
        self.viewManager.viewPile(pile)
        
    def setViewTypeOfPile(self, PileName, viewType):
        pile = self.getPileByName(PileName)
        
        self.viewManager.clearPile(pile)
        pile.viewType = viewType
        self.viewManager.viewPile(pile)