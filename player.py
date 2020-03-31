from piece import Piece

class Player:

    def __init__(self, name):
        self.name = name
        self.pos = None
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
        cardThrown = self.pop(ind)
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
        for i in self.cards:
            try:
                print(i.toString(), end=", ")
            except:
                print("No pieces")
                break
        print()
    # Update call
    def update(self, drawnCard):
        print(self.name, "picked up", drawnCard.toString())
        self.print_hand()