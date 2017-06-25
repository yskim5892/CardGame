class Taggable:
  def __init__(self):
    self.tags = set()

  def addTag(self, tag):
    self.tags = self.tags | {tag}

  def hasTag(self, tag):
    return (tag in self.tags)

  def removeTag(self, tag):
    self.tags = self.tags - {tag}

