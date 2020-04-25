from puzzlesearch.game.game import Game
from puzzlesearch.game.puzzle_board import PuzzleBoard


class PuzzleGame(Game):
    def __init__(self, size, player, scramble=True):
        super(PuzzleGame, self).__init__(
            self.__take_turn, self.__is_finished, self.__print_turn
        )

        self.board = PuzzleBoard(size)
        self.size = size
        self.player = player

        if scramble:
            self.board.scramble()

    def __print_turn(self):
        print(str(self.board))

    def __take_turn(self):
        action = self.player.get_action(self.board)
        self.board.move(action)

    def __is_finished(self):
        return self.board.is_finished()
