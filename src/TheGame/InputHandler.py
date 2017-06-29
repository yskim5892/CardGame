from . import TurnManager
import MainPlatform

def handleKeyInput(key, vm, om, log):
    if(key == 'e'):
        if(vm.getValue("State") == "takeActions"):
            index = vm.getValue("CurrentPlayerIndex")
            vm.setValue("CurrentPlayerIndex", (index + 1) % 2)
            TurnManager.drawACard(vm, om, log)
    if('0' <= key and key <= '9'):
        if(vm.getValue("State") == "takeActions"):
            TurnManager.takeActions(int(key), vm, om, log)