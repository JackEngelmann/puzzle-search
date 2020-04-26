import unittest
import mock
import io

from puzzlesearch.games.game import Game


class BoardMock:
    def __init__(self):
        self.moves_made = 0

    def __str__(self):
        return "BoardMock"

    def is_finished(self):
        return self.moves_made == 2

    def move(self):
        self.moves_made += 1


class TestPuzzleGame(unittest.TestCase):
    def test_start(self):
        with mock.patch("sys.stdout") as mock_stdout:
            board = BoardMock()
            game = Game(board.move, board.is_finished)
            game.start()
            self.assertEqual(board.moves_made, 2)
            mock_stdout.assert_has_calls([mock.call.write(Game.congratulation_message)])
