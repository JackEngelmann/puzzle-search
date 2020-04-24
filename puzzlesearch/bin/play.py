from puzzlesearch.board.board import Board


def main():
    board = Board(3)
    while True:
        print(board)
        print("Input: ")
        inp = input().rstrip("\n")
        if inp == "e":
            break
        if inp == "r":
            board.move_right()
        if inp == "l":
            board.move_left()
        if inp == "u":
            board.move_up()
        if inp == "d":
            board.move_down()
