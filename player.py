from piece import Piece
from constants.calls import call

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
    
    # Command line
    def command(self):
        result = ""
        while not result.isdigit():
            cmd_str = input("Trial: ").lower().split()
            if len(cmd_str) == 1:
                # arrange, call (zhimo and gong), game
                if cmd_str[0] in ["arrange", "sort"]:
                    self.sort_hand()
                    self.print_hand()
                ## Need to think of strategy for calling

                # Call gong
                elif cmd_str[0] == call["gong"] or cmd_str[0] == "gong":
                    print(self.name, "will GONG!")

                    # Select pieces to GONG
                    arr = input("Select pieces (4): ").split()
                    arr = [int(x) for x in arr]
                    checkArr = [self.cards[i] for i in arr]
                    # Make sure all pieces have same type
                    if len({g.getTypes().value for g in checkArr}) == 1:
                        tmpHand = list(self.cards)
                        # if they are normal cards, vals have to be the same too
                        try:
                            if len({n.getVal() for n in checkArr}) == 1:
                                for playInd in arr:
                                    c = tmpHand.pop(playInd)
                                    self.played.append(c)
                        # if they dont have getVal function 
                        except:
                            for playInd in arr:
                                c = tmpHand.pop(playInd)
                                self.played.append(c)
                    result = cmd_str[0]
                    
            elif len(cmd_str) == 2 and cmd_str[1].isdigit() and \
                "throw" in cmd_str[0]:
                # throw (ind number)
                cmd, ind = cmd_str
                print(self.name, cmd, ind)
                result = ind
            else:
                print("Invalid Move. Try again")
        return int(result)
    
    # Draw a card
    def draw(self, cardAdd):
        newCards = list(self.cards)
        newCards.append(cardAdd)
        self.setCards(newCards)
    
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
            print(i.toString(), end=", ")
        print()
    
    # Sorting hand
    def sort_hand(self):
        newHand = sorted(self.cards, key=lambda x: x.getTypes().value)
        valCards = [x for x in newHand if x.getTypes().value < 4]
        valCards = sorted(valCards,key=lambda x : (x.getTypes().value, x.getVal()))
        newHand = valCards + newHand[len(valCards):]
        self.setCards(newHand)



    # Update call should return thrown card
    def update(self, drawnCard):
        print(self.name, "picked up", drawnCard.toString())
        self.draw(drawnCard)
        self.print_hand()
        print(len(self.cards),end="\n")
        tmpInd = self.command()
        # tmpInd = input("Select a card(index): ")
        print(self.name, "threw out", self.cards[tmpInd].toString())
        return self.throwOut(tmpInd)