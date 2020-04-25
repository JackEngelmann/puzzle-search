import unittest
import mock
import io

from puzzlesearch.game.game import Game


class BoardMock:
    def __init__(self):
        self.moves_made = 0

    def __str__(self):
        return "BoardMock"

    def is_won(self):
        return self.moves_made == 2

    def move(self, action):
        self.moves_made += 1


class PlayerMock:
    def do_move(self, board):
        return "left"


class TestGame(unittest.TestCase):
    def test_start(self):
        with mock.patch("sys.stdout") as mock_stdout:
            board = BoardMock()
            player = PlayerMock()

            def take_turn():
                action = player.do_move(board)
                board.move(action)

            game = Game(take_turn=take_turn, is_finished=lambda: board.is_won(),)
            game.start()
            self.assertEqual(board.moves_made, 2)
            mock_stdout.assert_has_calls([mock.call.write(Game.congratulation_message)])
