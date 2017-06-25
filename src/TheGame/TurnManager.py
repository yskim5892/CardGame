
class TurnManager:
    def __init__(self):
        pass
    
    def StartTurn(self, gameData):
        gameData.currentPlayer.draw("Deck", "Hand", 1);