from . import TurnManager
import MainPlatform

def handleKeyInput(key, vm, om, log):
    if(key == 'e'):
        if(vm.getValue("State") == "takeActions"):
            index = vm.getValue("CurrentPlayerIndex")
            vm.setValue("CurrentPlayerIndex", (index + 1) % 2)
            TurnManager.drawACard(vm, om, log)

def checkCardClickable(cardName, vm, om, log):
    handName = "P" + str(vm.getValue("CurrentPlayerIndex")) + "Hand"
    return om.cardIsInPile(cardName, handName) & (vm.getValue("State") == "takeActions")

def handleCardPress(cardName, vm, om, log):
    pass
    
def handleCardRelease(cardName, vm, om, log):
    TurnManager.takeActions(cardName, vm, om, log)