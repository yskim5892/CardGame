from . import TurnManager
import MainPlatform

def handleKeyInput(key, vm, om):
    if(key == 'e'):
        if(vm.getValue("State") == "takeActions"):
            vm.setValue("CurrentPlayerIndex", (vm.getValue("CurrentPlayerIndex") + 1) % 2)
            TurnManager.drawACard(vm, om)
    if('0' <= key & key <= '9'):
        if(vm.getValue("State") == "takeActions"):
            TurnManager.takeActions(key, vm, om)
    if(key == 'h'):
        print("Hi")
class InputHandler(object):
    def __init__(self, params):
        pass