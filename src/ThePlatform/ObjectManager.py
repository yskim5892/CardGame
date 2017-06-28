# storage for in-game objects (eg. Cards, Piles ...)
# and functions about them

import Pile

piles = []

def getPileByName(pileName):
    piles = [x for x in piles if x.getName() == pileName]
    if (piles.len(0)):
        print("No pile with the name: " + pileName)
        return None
    return piles[0]

def getPile(tags, values):
    piles = [x for x in piles if x.hasTags(tags) and x.checkValues(tags)]

def makePile(pileName, tags=[], values=dict()):
    piles.append(ThePlatform.Pile.Pile())

