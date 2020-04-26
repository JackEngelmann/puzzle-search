from puzzlesearch.games.game import Game
from puzzlesearch.games.puzzle.puzzle_board import PuzzleBoard
from puzzlesearch.games.puzzle.puzzle_player_agent import PuzzlePlayerAgent
from puzzlesearch.games.puzzle.puzzle_player_manual import PuzzlePlayerManual


class PuzzleGame(Game):
    def __init__(self, size, player, scramble=True):
        super(PuzzleGame, self).__init__(
            self.__take_turn, self.__is_finished, self.__print_turn
        )

        self.board = PuzzleBoard(size)
        self.size = size

        if player == "user":
            self.player = PuzzlePlayerManual()
        else:
            self.player = PuzzlePlayerAgent()

        if scramble:
            self.board.scramble()

    def __print_turn(self):
        print(str(self.board))

    def __take_turn(self):
        action = self.player.get_action(self.board)
        self.board.move(action)

    def __is_finished(self):
        return self.board.is_finished()
