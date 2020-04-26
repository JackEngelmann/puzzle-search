import random


def noop():
    pass


class Game:
    congratulation_message = "Congratulations, you won! :)"
    separator = "---------------------------------------------------------"

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

    def take_turn(self):
        raise NotImplementedError()

    def is_finished(self):
        raise NotImplementedError()

    def print_turn(self):
        pass
