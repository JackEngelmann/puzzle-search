import random


class Game:
    def __init__(self, board):
        self.board = board

    def scramble(self):
        no_moves = random.randint(3, 100)
        for _ in range(no_moves):
            rand_move = random.randint(0, 3)
            if rand_move == 0:
                self.board.move_right()
            if rand_move == 1:
                self.board.move_left()
            if rand_move == 2:
                self.board.move_down()
            if rand_move == 3:
                self.board.move_up()

    def is_won(self):
        return self.board.is_won()
