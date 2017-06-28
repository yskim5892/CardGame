# storage for in-game objects (eg. Cards, Piles ...)
# and functions about them

class ScriptVariableManager:
    def __init__(self):
        self.values = dict()

    def setValue(self, name, value):
        self.values[name] = value

    def getValue(self, name):
        try:
            return self.values[name]
        except KeyError:
            return None

    def removeValue(self, name):
        try:
            del(self.values[name])
        except KeyError:
            return None
    
    def checkValues(self, values):
        return (all(x in self.values.items() for x in values.items()))

