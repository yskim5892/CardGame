class Valueable:
  def __init__(self):
    self.values = dict()

  def setValue(self, name, value):
    self.values[name] = value

  def getValue(self, name):
    try:
      return self.values[name]
    except KeyError:
      return 0

  def removeValue(self, name):
    try:
      del(self.values[name])
    except KeyError:
      return 0 
