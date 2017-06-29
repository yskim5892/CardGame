import random
from . import Taggable
from . import Valueable
from . import Card
from tkinter import *

class Pile(Taggable.Taggable, Valueable.Valueable):
    def __init__(self):
        super(Pile, self).__init__()
        self.pos = [0, 0]
        self.cards = []
    
    def shuffle(self):
        random.shuffle(self.cards)
        self.updateCardViewObjects()

    def addCard(self, card):
        self.cards.append(card)
        self.updateCardViewObjects()

    def drawCard(self, index = -1):
        return self.cards.pop(index)
        self.updateCardViewObjects()

    def setPos(self, x, y):
        self.pos[0] = x
        self.pos[1] = y
        self.updateCardViewObjects()
    def getCardViewObject(self, i):
        x = self.pos[0]
        y = self.pos[1]
        cardViewObject = self.cards[i].getShape()
        translatedCardViewObject = [(p[0] + x, p[1] + y) for p in cardViewObject]
        return translatedCardViewObject  
    
    '''TODO : gain canvas as a parameter or move this method to ViewManager, 
                and delete old cardViewObjects here'''
    def updateCardViewObjects(self):
        num = len(self.cards)
        for i in range(num):
            card = self.cards[i]
            if(self.getValue("ViewType") == "overlapped"):
                card.setPos(0, 0)
                card.angle = 0
            elif(self.getValue("ViewType") == "horizontal"):
                card.setPos((i - (num-1)/2) * self.cards[0].width, 0)
                card.angle = 0
            card.viewObject = self.getCardViewObject(i)
    def view(self, canvas):
        for card in self.cards:
            canvas.create_polygon(card.viewObject, outline="#000000", fill="#cccccc")
    
    def clear(self, canvas):
        for card in self.cards:
            canvas.delete(card.viewObject)

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

def makePile(pileName, tags=[], values=dict()):
    p = Pile()
    p.setName(pileName)
    for tag in tags:
        p.addTag(tag)
    for (k, v) in values.items():
        p.setValue(k, v)

    return p

#def getInput(event):
#    c = event.char
#    if(c == 'a'):
#
#        a.setPos(480, 200)
#        a.view(canvas)
        
#    elif(c == 'b'):
        
#        a.setPos(480, 400)
#        a.setValue("ViewType", "horizontal")
#        a.view(canvas)

#a = Pile()
#for i in range(10):
#    card = Card()
#    card.width = 50
#    card.height = 90
#    a.addCard(card)
#root = Tk()
#root.resizable(width = False, height = False)

#canvas = Canvas(root, width=960, height=640)
#canvas.grid(row=0, column=0, sticky="WENS")

#canvas.focus_set()
#canvas.bind("<Key>", getInput)
#root.mainloop()
