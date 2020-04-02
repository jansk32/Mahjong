from piece import Piece

class Player:

    def __init__(self, name):
        self.name = name
        self.pos = None
        self.played = []
        self.cards = []
        self.currCard = None

    def getName(self):
        return self.name
    
    def getPos(self):
        return self.pos
    
    def getCards(self):
        return self.cards

    def setCards(self,arrOfCards):
        self.cards = arrOfCards
    
    def setPos(self,pos):
        self.pos = pos
    
    # Choose a card
    def chooseCard(self, ind):
        self.currCard = self.cards[ind]
        return ind

    # Draw a card
    def draw(self, cardAdd):
        self.cards.append(cardAdd)
    
    # Throw out a card
    def throwOut(self, ind):
        cardThrown = self.cards.pop(ind)
        return cardThrown
    
    # To make a call
    def call():
        # 1 = pong, 2 = zhimo, 3 = gong
        calling = input("Type your call (1,2,3): ")
        if calling.isdigit():
            return calling
        else:
            return None

    # Print hand
    def print_hand(self):
        for i in self.getCards():
            try:
                print(i.toString(), end=", ")
            except:
                print("No pieces")
                break
        print()
    # Update call should return thrown card
    def update(self, drawnCard):
        print(self.name, "picked up", drawnCard.toString())
        self.draw(drawnCard)
        self.print_hand()
        print(len(self.cards),end="\n")
        tmpInd = len(self.cards) -1 ## FIX THIS
        print(self.name, "threw out", self.cards[tmpInd].toString())
        return self.throwOut(tmpInd)