from ThePlatform.Taggable import Taggable
from ThePlatform.Valueable import Valueable
from math import *

class Card(Taggable, Valueable):
    def __init__(self):
        super(Card, self).__init__()
        self.pos = [0, 0]
        self.width = 0
        self.height = 0
        self.angle = 0
        self.setValue("Shape", "Rectangle")
    
    def setPos(self, x, y):
        self.pos[0] = x
        self.pos[1] = y
    
    def getShape(self):
        if(self.getValue("Shape") == "Rectangle"):
            x = self.pos[0]
            y = self.pos[1]
            w = self.width
            h = self.height
            angle = self.angle
            baseShape = [(-w/2, -h/2), (-w/2, h/2), (w/2, h/2), (w/2, -h/2)]
            rotate = complex(cos(angle), sin(angle))
            rotatedShapeInComplex = [complex(p[0], p[1]) * rotate for p in baseShape]
            rotatedShape = [(p.real, p.imag) for p in rotatedShapeInComplex]
            rotatedAndTranslatedShape = [(p[0] + x, p[1] + y) for p in rotatedShape]
            return rotatedAndTranslatedShape
