from piece import Piece

class Normal(Piece):

    def __init__(self, val, types):
        super().__init__(types)
        self.val = val
    
    def toString(self):
        return (self.val, self.types.name)