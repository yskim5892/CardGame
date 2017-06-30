from . import TurnManager
import MainPlatform

def handleKeyInput(key, vm, om, log):
    if(key == 'e'):
        if(vm.getValue("State") == "takeActions"):
            index = vm.getValue("CurrentPlayerIndex")
            vm.setValue("CurrentPlayerIndex", (index + 1) % 2)
            TurnManager.drawACard(vm, om, log)
            
def handleCardClick(cardName, vm, om, log):
    if(vm.getValue("State") == "takeActions"):
        index = vm.getValue("CurrentPlayerIndex")
        handName = "P" + str(index) + "Hand"
        if(om.cardIsInPile(cardName, handName)):
            TurnManager.takeActions(cardName, vm, om, log)