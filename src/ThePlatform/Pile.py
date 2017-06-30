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
    
    def removeCard(self, card):
        if(card in self.cards):
            self.cards.remove(card)
            return True
        else:
            return False
    
    def containsCard(self, card):
        return card in self.cards

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
