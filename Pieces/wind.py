from piece import Piece

class Wind(Piece):

    def __init__(self, types):
        super().__init__(types)
    
    def toString(self):
        return (self.types.name)