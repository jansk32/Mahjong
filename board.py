from constants.valConst import *
from Pieces.dragon import Dragon
from Pieces.wind import Wind
from Pieces.normal import Normal
from Pieces.flower import Flower
from player import Player
import random

class Board:

    def __init__(self):
        self.cards = initialise_pieces()
        self.players = []
        self.discard = []

    # Adds player, returns their index
    def addPlayer(self, name):
        self.players.append(Player(name))
        ind = len(self.players) - 1
        return ind
    
    # Initialise player cards
    def initial_four_player(self, ind):
        tmpPlayer = self.players[ind]
        for i in range(4):
            c = self.drawCard()
            tmpPlayer.draw(c)


    # Update players
    def update(self):
        gvn = self.drawCard()
        t = self.players[0].update(gvn)
        self.discard.append(t)

        #for i in self.players:
        #    gvn = self.drawCard()
        #    i.update(gvn)
            #print_pieces(self.cards)

    # Draw card
    def drawCard(self):
        return self.cards.pop(-1)
    
    # Initial draws
    def initial_drawing(self):
        for round in range(3):
            for i in range(len(self.players)):
                self.initial_four_player(i)
        for last in self.players:
            c = self.drawCard()
            last.draw(c)
    
# Initialise number of cards
def initialise_pieces():
    mahPieces = []

    # Suites BAMBOO, DOTS and HORSE
    for i in range(4):
        for i in valCounts:
            mahPieces.append(Normal(i, Suite.BAMBOO))
            mahPieces.append(Normal(i, Suite.DOTS))
            mahPieces.append(Normal(i, Suite.HORSE))

        for drag in dragon:
                mahPieces.append(Dragon(drag))

        for w in wind:
                mahPieces.append(Wind(w))
        
    for pos in flower:
        mahPieces.append(Flower(pos, Suite.FLOWER))
        mahPieces.append(Flower(pos, Suite.FLOWER))

    #return sorted(mahPieces, key=lambda x: x.getTypes().name)
    random.shuffle(mahPieces)
    return mahPieces


def print_pieces(arr):
    for i in arr:
        print(i.toString(), end=" ")
    print()