import unittest
import mock

from puzzlesearch.players.manual_player import ManualPlayer


class TestManualPlayer(unittest.TestCase):
    def test_do_move_in_direction(self):
        player = ManualPlayer()

        # down
        with mock.patch("builtins.input", lambda: "down"):
            self.assertEqual(player.do_move(None), "down")
        with mock.patch("builtins.input", lambda: "j"):
            self.assertEqual(player.do_move(None), "down")

        # up
        with mock.patch("builtins.input", lambda: "up"):
            self.assertEqual(player.do_move(None), "up")
        with mock.patch("builtins.input", lambda: "k"):
            self.assertEqual(player.do_move(None), "up")

        # left
        with mock.patch("builtins.input", lambda: "left"):
            self.assertEqual(player.do_move(None), "left")
        with mock.patch("builtins.input", lambda: "h"):
            self.assertEqual(player.do_move(None), "left")

        # right
        with mock.patch("builtins.input", lambda: "right"):
            self.assertEqual(player.do_move(None), "right")
        with mock.patch("builtins.input", lambda: "l"):
            self.assertEqual(player.do_move(None), "right")

    def test_do_move_repeat_when_unknown_iput(self):
        player = ManualPlayer()

        mock_input = mock.Mock(side_effect=["unknown-input", "down"])

        with mock.patch("builtins.input", mock_input):
            action = player.do_move(None)
            self.assertEqual(mock_input.call_count, 2)
            self.assertEqual(action, "down")
