from tkinter import *
from tkinter import filedialog
from math import *
import sys

import importlib.util
import ThePlatform


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

    def getVariableManager():
        return self.scriptVariableManager

    def getObjectManager():
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
    gameDirectory = filedialog.askdirectory()
    sys.path.append(gameDirectory)
    gameName = gameDirectory.split("/")[-1]
    #gamePkg = importlib.import_module(gameName)
    #gamePkg.GameManager.initialize()

def getInput(key):
    print("Key pressed!")

def main():
    m = MainPlatform()

if __name__ == "__main__":
    main()
