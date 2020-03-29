from constants.valConst import Suite

class Piece:

    def __init__(self, number, suite, isNorm):
        self.number = number # value or points
        self.suite = suite
        self.isNorm = isNorm

    def getNumber(self):
        return self.number
    
    def getSuite(self):
        return self.suite
    
    def getNorm(self):
        return self.isNorm

    def toString(self):
        return (self.number, self.suite.name)