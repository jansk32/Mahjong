from piece import Piece

class Flower(Piece):

    def __init__(self, val, types):
        super().__init__(types)
        self.val = val
    
    def getVal(self):
        return self.val

    def toString(self):
        return (self.val, self.types.name)