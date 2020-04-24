from puzzlesearch.board.board import Board
from puzzlesearch.game.game import Game


def main():
    board = Board(2)
    game = Game(board)
    game.scramble()
    while True:
        print(board)
        print("Input: ")
        inp = get_input()
        if is_exit(inp):
            break
        execute_command(board, inp)

        if game.is_won():
            print("Congratulations")
            break


def get_input():
    return input().rstrip("\n")


def execute_command(board, inp):
    if inp == "r":
        board.move_right()
    if inp == "l":
        board.move_left()
    if inp == "u":
        board.move_up()
    if inp == "d":
        board.move_down()


def is_exit(inp):
    return inp == "e"
