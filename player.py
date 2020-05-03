from piece import Piece
from Pieces.flower import Flower
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
    def command(self, drawPile, discardCard, flowerPile):
        isThrow = False
        """
        1. Prompt user of action (during turn)
            a. Draw (1) v
                b. Gong (2)
                c. throw (3) v
                d. Flower (4)
            b. Zhi Mo (2)
            c. arrange(3) v
        2. Prompt user of action (outside turn)
            a. Pong (5)
            b. Gong (6)
        3. Prompt user of game (7)
        Each move should return an updated (drawPile, discardCard, flowerPile, thrownInd)
        """

        ## Actions during turn
        action = int(input("Draw or Zhimo or arrange: "))
        while isThrow == False:
            # if action != game or arrange or sort, do the following
            if action == 1:
                c, drawPile_updated = self.draw(drawPile)
                print("You drew", c.toString())
                self.print_hand()
                action = int(input("gong, zhimo or throw: "))
                if action == 2:
                    # Gong
                    lst = input("Which cards to Gong? ")
                    lst = [int(x) for x in lst.split() if x.digit()]
                    if len(lst) == 4:
                        isGong = gong(flowerPile)

                    # if gong is correctly done, draw flower
                    if isGong == True:
                        isThrow = True
                        while type(flowerPile[0]) == Flower:

                            # flowerDraw already adds it to the hand
                            flowerPile = self.flowerDraw(flowerPile)

                        # if no more flowers
                        flowerPile = self.flowerDraw(flowerPile)
                        ind = int(input("Throw out which card?" ))
                        return ind     
                    

                elif action == 3:
                    # Throw out a card
                    isThrow = True
                    ind = int(input("Which card to throw? "))
                    return ind

            elif action == 2:
                # Zhimo
                self.card.append(discardCard)

                # should have check in place

                zhiMoPiece = input("Which pieces do you want to zhimo? ")
                zhiMoPiece = zhiMoPiece.split()

                # Assuming pieces are in one line, separated by one space
                for card in zhiMoPiece:
                    self.played.append(self.cards.pop(card))
                return
            
            elif action == 8:
                # Arrange cards
                self.sort_hand()
                self.print_hand()
                action = int(input("Draw or Zhi mo? "))

    
    # Draw a card
    def draw(self, drawPile):
        newCards = list(self.cards)
        tmp = drawPile.pop(0)
        newCards.append(tmp)
        self.setCards(newCards)
        return (tmp, drawPile)


    # Throw out a card
    def throwOut(self, ind):
        cardThrown = self.cards.pop(ind)
        return cardThrown
    
    # Check if playable pong/gong
    def checkGongPong(self, playing):
        sample = self.cards[playing[0]]
        for card in playing:
            tmpCard = self.cards[card]

            # Need to check if all cards are the same type
            if tmpCard.types != sample.types:
                return False
            # Check if cards have same value too where possible
            try:
                if tmpCard.val != sample.val:
                    return False
            except:
                continue
        return True

    # Check if zhimo is playable
    def checkZhiMo(self, playing):
        sample = self.cards[playing[0]]
        correctNumbers = []
        for card in playing:
            tmpCard = self.cards[card]

            # Need to check if all cards are the same type
            if tmpCard.types != sample.types:
                return False
            correctNumbers.append(tmpCard.val)
            
        # Check if in order
        if sorted(correctNumbers) == \
            range(min(correctNumbers), max(correctNumbers) + 1):
                        return True
        return False

    # To make a call
    def gong(self,playing, flowerPile):
        # Takes an array of ind 

        # Selects first card in line as sample
        if self.checkGongPong(playing) == False:
            return False

        # Play cards and take from flower pile    
        for add in playing:
            self.played.append(self.cards.pop(add))

        self.flowerDraw(flowerPile)  
        return True

           

    def flowerDraw(self, flowPile):
        tmp = flowPile.copy()
        for i in self.cards:
            if type(i) == Flower:
                self.played.append(i)
                self.cards.remove(i)
                self.cards.append(tmp[0])
                tmp = tmp[1:]
        # Returns the flower pile
        return tmp

    # Print hand
    def print_hand(self):
        for i in self.getCards():
            print(i.toString(), end=", ")
        print()
    
    # Sorting hand
    def sort_hand(self):
        newHand = sortCards(self.cards)
        self.setCards(newHand)


    # Update call should return thrown card
    def update(self, drawPile,discardPile,flowerPile):
        # print(self.name, "picked up", drawnCard.toString())
        # self.draw(drawnCard)
        self.print_hand()
        print(len(self.cards),end="\n")
        if len(discardPile) < 1:
            tmpInd = self.command(drawPile, [], flowerPile)
        else:    
            tmpInd = self.command(drawPile, discardPile[0], flowerPile)
        # tmpInd = input("Select a card(index): ")
        #print(self.name, "threw out", self.cards[tmpInd].toString())
        return self.throwOut(tmpInd)

# Sorts card algorithm
def sortCards(tiles):
    newHand = sorted(tiles, key=lambda x: x.getTypes().value)
    valCards = [x for x in newHand if x.getTypes().value < 4]
    valCards = sorted(valCards,key=lambda x : (x.getTypes().value, x.getVal()))
    newHand = valCards + newHand[len(valCards):]
    return newHand