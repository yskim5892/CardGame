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
    
    def getCardByName(self, cardName):
        cards = []
        for pile in self.piles:
            cardsToAppend = [x for x in pile.cards if x.getName() == cardName]
            for card in cardsToAppend:
                cards.append(card)
        if (len(cards) == 0):
            print("No pile with the name: " + cardName)
            return None
        return cards[0]

    def getPile(self, tags, values):
        piles = [x for x in self.piles 
                if x.hasTags(tags) and x.checkValues(tags)]
        
    def cardIsInPile(self, cardName, pileName):
        card = self.getCardByName(cardName)
        pile = self.getPileByName(pileName)
        return card.pile == pile

    def makePile(self, pileName, tags=[], values=dict()):
        pile = Pile.makePile(pileName, tags, values)
        self.piles.append(pile)
        return pile
    
    def makeCard(self, pileName, cardName, width, height, tags=[], values=dict()):
        pile = self.getPileByName(pileName)
        card = Card.makeCard(cardName, tags, values)
        card.width = width
        card.height = height
        card.pile = pile
        
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
        
        cards = []
        for i in indices : 
            cards.append(fromPile.cards[i])
            fromPile.cards.remove(fromPile.cards[i])
        for card in cards : 
            toPile.addCard(card)
            card.pile = toPile
        self.viewManager.viewPile(fromPile)
        self.viewManager.viewPile(toPile)
        
        self.mainPlatform.triggerWhenCardsMoved(fromPile, toPile, cards)
        
    def moveCardsByName(self, fromPileName, toPileName, cardNames):
        fromPile = self.getPileByName(fromPileName)
        toPile = self.getPileByName(toPileName)
        
        cards = []
        for cardName in cardNames : cards.append(self.getCardByName(cardName))
        for card in cards : 
            if(fromPile.removeCard(card)):
                toPile.addCard(card)
                card.pile = toPile
        
        self.viewManager.viewPile(fromPile)
        self.viewManager.viewPile(toPile)
        
        self.mainPlatform.triggerWhenCardsMoved(fromPile, toPile, cards)
        
    def shufflePile(self, PileName):
        pile = self.getPileByName(PileName)
        
        pile.shuffle()
        self.viewManager.viewPile(pile)
    
    def setPosOfPile(self, PileName, x, y):
        pile = self.getPileByName(PileName)
        
        pile.setPos(x, y)
        self.viewManager.viewPile(pile)
        
    def setViewTypeOfPile(self, PileName, viewType):
        pile = self.getPileByName(PileName)
        
        pile.viewType = viewType
        self.viewManager.viewPile(pile)