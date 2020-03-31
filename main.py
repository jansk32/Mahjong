from constants.valConst import *
from Pieces.dragon import Dragon
from Pieces.wind import Wind
from Pieces.normal import Normal
from Pieces.flower import Flower

def main():
    pArr = initialise_pieces()
    print_pieces(pArr)
    print(len(pArr))

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

    return sorted(mahPieces, key=lambda x: x.getTypes().name)

def print_pieces(arr):
    for i in arr:
        print(i.toString(), end=" ")
    print()


if __name__ == "__main__":
    main()