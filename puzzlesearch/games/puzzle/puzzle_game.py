from puzzlesearch.games.game import Game
from puzzlesearch.games.puzzle.puzzle_board import PuzzleBoard
from puzzlesearch.games.puzzle.puzzle_player_agent import PuzzlePlayerAgent
from puzzlesearch.games.puzzle.puzzle_player_manual import PuzzlePlayerManual


class PuzzleGame(Game):
    def __init__(self, size, player, scramble=True):
        self.board = PuzzleBoard(size)
        self.size = size

        if player == "user":
            self.player = PuzzlePlayerManual()
        else:
            self.player = PuzzlePlayerAgent()

        if scramble:
            self.board.scramble()

    def print_turn(self):
        print(str(self.board))

    def take_turn(self):
        action = self.player.get_action(self.board)
        self.board.move(action)

    def is_finished(self):
        return self.board.is_finished()
