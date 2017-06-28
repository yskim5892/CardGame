from TheGame.TurnManager import TurnManager

class InputHandler(object):
    def __init__(self, params):
        pass
    def handleKeyInput(self, key):
        sv = ScripitVariableManager.getScriptVariable()
        if(key == 'e'):
            if(sv.getValue("State") == "takeActions"):
                sv.setValue("CurrentPlayerIndex", (sv.getValue("CurrentPlayerIndex") + 1) % 2)
                TurnManager.drawACard(sv)
        if('0' <= key & key <= '9'):
            if(sv.getValue("State") == "takeActions"):
                TurnManager.takeActions(sv, key)
                