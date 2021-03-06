
class ViewManager:
    def __init__(self, mainPlatform):
        self.mainPlatform = mainPlatform
        self.canvas = mainPlatform.canvas
        self.cardDict = {}
    def viewAllPile(self, om):
        for pile in om.piles:
            self.viewPile(pile)
            
    def getCardPolygon(self, pile, i):
        x = pile.pos[0]
        y = pile.pos[1]
        cardPolygon = pile.cards[i].getPolygon()
        translatedCardPolygon = [(p[0] + x, p[1] + y) for p in cardPolygon]
        return translatedCardPolygon
    
    def getCardPolygons(self, pile):
        cardPolygons = []
        num = len(pile.cards)
        for i in range(num):
            card = pile.cards[i]
            if(card != self.mainPlatform.selectedCard):
                try:
                    if(pile.viewType == "overlapped"):
                        card.setPos(0, 0)
                    elif(pile.viewType == "horizontal"):
                        card.setPos((i - (num-1)/2) * pile.cards[0].width, 0)
                except AttributeError:
                    card.setPos(0, 0)
            card.angle = 0
            cardPolygons.append(self.getCardPolygon(pile, i))
        return cardPolygons
    
    def viewPile(self, pile):
        cardPolygons = self.getCardPolygons(pile)
        for i in range(len(pile.cards)):
            card = pile.cards[i]
            try:
                viewObject = card.viewObject
                cardCoords = []
                for coord in cardPolygons[i]:
                    cardCoords.append(coord[0])
                    cardCoords.append(coord[1])
                self.canvas.coords(viewObject, *cardCoords)
            except AttributeError:    
                viewObject = self.canvas.create_polygon(cardPolygons[i], outline="#000000", fill="#cccccc")
                self.cardDict[viewObject] = pile.cards[i]
                self.canvas.tag_bind(viewObject, '<ButtonPress-1>', self.mainPlatform.onCardPressed)
                self.canvas.tag_bind(viewObject, '<B1-Motion>', self.mainPlatform.onCardMoved)
                self.canvas.tag_bind(viewObject, '<ButtonRelease-1>', self.mainPlatform.onCardReleased)
                pile.cards[i].viewObject = viewObject
    
    def clearPile(self, pile):
        for card in pile.cards:
            try:
                self.canvas.delete(card.viewObject)
            except AttributeError:
                pass