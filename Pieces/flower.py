from piece import Piece

class Flower(Piece):

    def __init__(self, pos, types):
        super().__init__(types)
        self.pos = pos
    
    def toString(self):
        return (self.pos, self.types.name)