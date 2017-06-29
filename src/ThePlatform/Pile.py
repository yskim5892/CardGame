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

    def addCard(self, card):
        self.cards.append(card)

    def drawCard(self, index = -1):
        return self.cards.pop(index)

    def setPos(self, x, y):
        self.pos[0] = x
        self.pos[1] = y
        
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
