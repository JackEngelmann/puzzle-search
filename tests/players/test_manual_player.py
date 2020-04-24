import unittest
import mock

from puzzlesearch.players.manual_player import ManualPlayer


class TestManualPlayer(unittest.TestCase):
    def test_do_move_in_direction(self):
        player = ManualPlayer()
        self.__assert_input_does_move("down", "down", player)
        self.__assert_input_does_move("j", "down", player)
        self.__assert_input_does_move("up", "up", player)
        self.__assert_input_does_move("k", "up", player)
        self.__assert_input_does_move("left", "left", player)
        self.__assert_input_does_move("h", "left", player)
        self.__assert_input_does_move("right", "right", player)
        self.__assert_input_does_move("l", "right", player)

    def __assert_input_does_move(self, input_, action, player):
        with mock.patch("builtins.input", lambda: input_):
            self.assertEqual(player.do_move(None), action)

    def test_do_move_repeat_when_unknown_iput(self):
        player = ManualPlayer()

        mock_input = mock.Mock(side_effect=["unknown-input", "down"])

        with mock.patch("builtins.input", mock_input):
            action = player.do_move(None)
            self.assertEqual(mock_input.call_count, 2)
            self.assertEqual(action, "down")
