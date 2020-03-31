from board import Board

def main():
    board = Board()
    p1 = board.addPlayer("John")
    p2 = board.addPlayer("Kevin")
    board.initial_drawing()
    board.update()



if __name__ == "__main__":
    main()