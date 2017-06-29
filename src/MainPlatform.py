from tkinter import *
from tkinter import filedialog
import sys
import importlib

import ThePlatform

m = 0
gamePkg = 0

class MainPlatform:
    def __init__(self):
        pass

    def getVariableManager(self):
        return self.scriptVariableManager

    def getObjectManager(self):
        return self.objectManager
    def start(self):
        self.scriptVariableManager = ThePlatform.ScriptVariableManager.ScriptVariableManager()
        self.objectManager = ThePlatform.ObjectManager.ObjectManager()
        
        self.root = Tk()
        self.root.resizable(width = False, height = False)
        self.root.bind("<Key>", getInput)

        self.canvas = Canvas(self.root, width=500, height=400)
        self.canvas.grid(row=0, column=0, sticky="WENS")

        self.canvas.bind("<B1-Motion>", B1Motion)
        self.canvas.bind("<ButtonPress-1>", ButtonPress1)
        self.canvas.bind("<ButtonRelease-1>", ButtonRelease1)

        self.canvas.focus_set()
        
        self.log = Text(self.root, width=30, height = 20)
        self.log.grid(row=0, column=1, sticky="WENS")
        self.log.focus_set()
        
        loadGameButton = Button(self.root, width=50, height=10)
        loadGameButton.grid(row=1, column=0, sticky="WENS")
        loadGameButton.config(text="Load game", command=LoadGameButton)

        self.root.mainloop()

def B1Motion(event):
    global canvas
    global root
    print("Mouse moved!")

def ButtonPress1(event):
    global canvas
    global root
    print("Mouse pressed!")

def ButtonRelease1(event):
    print("Mouse released!")

def LoadGameButton():
    global gamePkg

    gameDirectory = filedialog.askdirectory()
    sys.path.append(gameDirectory)
    gameName = gameDirectory.split("/")[-1]
    m.log.insert(INSERT, gameName)
    gamePkg = importlib.import_module(gameName)
    gamePkg.Initializer.initialize()

def getInput(key):
    if(gamePkg != 0):
        gamePkg.InputHandler.handleKeyInput(key)
    m.log.insert(INSERT, "Key pressed!\n")

if(m ==0):
    m = MainPlatform()
    m.start()

#if __name__ == "__main__":
    #main()
