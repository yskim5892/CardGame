from tkinter import *
from tkinter import filedialog
from math import *
import sys

import importlib.util
import ThePlatform

canvas = 0
gamePkg = 0

class MainPlatform:
    def __init__(self):
        pass

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
    #gamePkg.GameManager.initialize()

def getInput(key):
    print("Key pressed!")

def main():
    global canvas
    global root

    root = Tk()
    root.resizable(width = False, height = False)
    root.bind("<Key>", getInput)

    canvas = Canvas(root, width=1000, height=800)
    canvas.grid(row=0, column=0, sticky="WENS")

    canvas.bind("<B1-Motion>", B1Motion)
    canvas.bind("<ButtonPress-1>", ButtonPress1)
    canvas.bind("<ButtonRelease-1>", ButtonRelease1)

    canvas.focus_set()

    loadGameButton = Button(root, width=50, height=10)
    loadGameButton.grid(row=1, column=0, sticky="WENS")
    loadGameButton.config(text="Load game", command=LoadGameButton)

    root.mainloop()

if __name__ == "__main__":
    main()
