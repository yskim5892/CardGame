class Taggable:
    def __init__(self):
        super(Taggable, self).__init__()
        self.tags = set()

    def addTag(self, tag):
        self.tags = self.tags | {tag}

    def hasTag(self, tag):
        return (tag in self.tags)

    def removeTag(self, tag):
        self.tags = self.tags - {tag}

    def hasTags(self, tags):
        if (set(tags) <= self.tags):
            return True
        else:
            return False


