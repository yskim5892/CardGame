import random
from ThePlatform.Taggable import Taggable
from ThePlatform.Valueable import Valueable
from ThePlatform.Card import Card
from tkinter import *

class Pile(Taggable, Valueable):
    def __init__(self):
        super(Pile, self).__init__()
        self.cards = []
    
    def shuffle(self):
        random.shuffle(self.cards)

    def addCard(self, card):
        self.cards.append(card)

    def drawCard(self):
        return self.cards.pop(-1)

    def setPos(self, x, y):
        self.pos[0] = x
        self.pos[1] = y
    
    def viewCard(self, canvas, i):
        x = self.pos[0]
        y = self.pos[1]
        cardShape = self.cards[i].getShape()
        translatedCardShape = [(p[0] + x, p[1] + y) for p in cardShape]
        canvas.create_polygon(translatedCardShape, outline="#000000", fill="#cccccc")
        
    def view(self, canvas):
        num = len(self.cards)
        if(self.getValue("ViewType") == "overlapped"):
            for i in range(num):
                self.cards[i].setPos(0, 0)
                self.cards[i].angle = 0
        elif(self.getValue("ViewType") == "horizontal"):
            for i in range(num):
                self.cards[i].setPos((i - (num-1)/2) * self.cards[0].width, 0)
                self.cards[i].angle = 0
                
        for i in range(num):
            self.viewCard(canvas, i)

    def getName():
        return self.name

    def setName(name):
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
