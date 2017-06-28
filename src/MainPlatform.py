from tkinter import *
from tkinter import filedialog
import sys
import importlib

import ThePlatform

m = 0
gamePkg = 0

class MainPlatform:
    def __init__(self):
        self.scriptVariableManager = ThePlatform.ScriptVariableManager.ScriptVariableManager()
        self.objectManager = ThePlatform.ObjectManager.ObjectManager()
        
        self.root = Tk()
        self.root.resizable(width = False, height = False)
        self.root.bind("<Key>", getInput)

        self.canvas = Canvas(self.root, width=1000, height=800)
        self.canvas.grid(row=0, column=0, sticky="WENS")

        self.canvas.bind("<B1-Motion>", B1Motion)
        self.canvas.bind("<ButtonPress-1>", ButtonPress1)
        self.canvas.bind("<ButtonRelease-1>", ButtonRelease1)

        self.canvas.focus_set()

        loadGameButton = Button(self.root, width=50, height=10)
        loadGameButton.grid(row=1, column=0, sticky="WENS")
        loadGameButton.config(text="Load game", command=LoadGameButton)

        self.root.mainloop()

    def getVariableManager(self):
        return self.scriptVariableManager

    def getObjectManager(self):
        return self.objectManager

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
    gamePkg = importlib.import_module(gameName)
    gamePkg.Initializer.initialize()

def getInput(key):
    gamePkg.InputHandler.handleKeyInput(key)
    print("Key pressed!")

def main():
    global m
    m = MainPlatform()

if __name__ == "__main__":
    main()
