from board import Board

def main():
    board = Board()
    p1 = board.addPlayer("John")
    p2 = board.addPlayer("Kevin")
    #a,b = input("trial: ").split()
    board.initial_drawing()
    board.update()
    print("Number of cards in pile:",len(board.cards))
    print("Number of cards in discard:", len(board.discard))

if __name__ == "__main__":
    main()