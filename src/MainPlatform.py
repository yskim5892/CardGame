from tkinter import *
from tkinter import filedialog
import sys
import importlib

import ThePlatform

class MainPlatform:
    def __init__(self):
        self.scriptVariableManager = ThePlatform.ScriptVariableManager.ScriptVariableManager()
        self.root = Tk()
        self.canvas = Canvas(self.root, width=1000, height=400)
        self.viewManager = ThePlatform.ViewManager.ViewManager(self)
        self.objectManager = ThePlatform.ObjectManager.ObjectManager(self)
        
        self.root.resizable(width = False, height = False)
        self.root.bind("<Key>", self.getInput)

        self.canvas.grid(row=0, column=0, sticky="WENS")

        self.canvas.focus_set()
        
        self.log = Text(self.root, width=30, height = 20)
        self.log.grid(row=0, column=1, sticky="WENS")
        self.log.focus_set()
        
        loadGameButton = Button(self.root, width=50, height=10)
        loadGameButton.grid(row=1, column=0, sticky="WENS")
        loadGameButton.config(text="Load game", command=self.LoadGameButton)
        
        self.selectedCard = 0
        pass
    def getInput(self, event):
        vm = self.scriptVariableManager
        om = self.objectManager
        if(self.gamePkg != 0):
            self.gamePkg.InputHandler.handleKeyInput(event.char, vm, om, self.log)
            self.viewManager.viewAllPile(om)
    def LoadGameButton(self):
        gameDirectory = filedialog.askdirectory()
        sys.path.append(gameDirectory)
        gameName = gameDirectory.split("/")[-1]
        self.gamePkg = importlib.import_module(gameName)
        self.gamePkg.Initializer.initialize(self.scriptVariableManager, self.objectManager, self.log)
        self.viewManager.viewAllPile(self.objectManager)
    def onCardPressed(self, event):
        vm = self.scriptVariableManager
        om = self.objectManager
        cardViewObject = event.widget.find_closest(event.x, event.y)
        card = self.viewManager.cardDict[cardViewObject[0]]
        cardName = card.getName()
        
        if(self.gamePkg.InputHandler.checkCardClickable(cardName, vm, om, self.log)):
            self.selectedCard = card
            self.mousePrevX = event.x
            self.mousePrevY = event.y
            self.gamePkg.InputHandler.handleCardPress(cardName, vm, om, self.log)
            
    def onCardMoved(self, event):
        card = self.selectedCard
        if(card != 0):
            dx =  event.x - self.mousePrevX
            dy =  event.y - self.mousePrevY
            self.canvas.move(card.viewObject, dx, dy)
            self.mousePrevX = event.x
            self.mousePrevY = event.y
            
    def onCardReleased(self, event):
        vm = self.scriptVariableManager
        om = self.objectManager
        card = self.selectedCard
        if(card != 0):
            cardName = card.getName()
            self.selectedCard = 0
            self.gamePkg.InputHandler.handleCardRelease(cardName, vm, om, self.log)
            
          
    def start(self):
        self.root.mainloop()
    def triggerWhenCardsMoved(self, fromPile, toPile, cards):
        pass

def main():
    m = MainPlatform()
    m.start()

if __name__ == "__main__":
    main()
