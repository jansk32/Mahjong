from constants.valConst import *
from piece import Piece

def main():
    print("Hello")
    pArr = initialise_pieces()
    print_pieces(pArr)

def initialise_pieces():
    mahPieces = []

    # Suites BAMBOO, DOTS and HORSE
    for i in range(4):
        for i in valCounts:
            mahPieces.append(Piece(i, Suite.HORSE, False))
            mahPieces.append(Piece(i, Suite.BAMBOO, False))
            mahPieces.append(Piece(i, Suite.DOTS, False))

    return sorted(mahPieces, key=lambda x: x.getSuite().name)

def print_pieces(arr):
    for i in arr:
        print(i.toString(), end=" ")
        print()


if __name__ == "__main__":
    main()