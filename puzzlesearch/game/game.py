import random


class Game:
    def __init__(self, board, player):
        self.board = board
        self.player = player

    def start(self):
        self.board.scramble()
        finished = False
        while not finished:
            finished = self.__play_round()

    def __play_round(self):
        print(self.board)
        if self.board.is_won():
            self.__print_separator()
            print("Congratulations")
            return True
        action = self.player.do_move(self.board)
        self.board.move(action)
        self.__print_separator()
        return False

    def __print_separator(self):
        print(
            "--------------------------------------------------------------------------------------"
        )
