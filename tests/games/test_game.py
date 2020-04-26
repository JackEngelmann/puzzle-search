import unittest
import mock
import io

from puzzlesearch.games.game import Game


class MockGame(Game):
    def __init__(self):
        self.moves_made = 0

    def is_finished(self):
        return self.moves_made == 2

    def take_turn(self):
        self.moves_made += 1


class TestPuzzleGame(unittest.TestCase):
    def test_start(self):
        with mock.patch("sys.stdout") as mock_stdout:
            game = MockGame()
            game.start()
            self.assertEqual(game.moves_made, 2)
            mock_stdout.assert_has_calls([mock.call.write(Game.congratulation_message)])
