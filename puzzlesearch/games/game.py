import random


def noop():
    pass


class Game:
    congratulation_message = "Congratulations, you won! :)"
    separator = "---------------------------------------------------------"

    def __init__(self, take_turn, is_finished, print_turn=noop):
        self.take_turn = take_turn
        self.is_finished = is_finished
        self.print_turn = print_turn

    def start(self):
        finished = False
        while not finished:
            finished = self.__play_round()

    def __play_round(self):
        self.print_turn()

        if self.is_finished():
            print(self.separator)
            print(self.congratulation_message)
            return True

        self.take_turn()
        print(self.separator)
        return False
