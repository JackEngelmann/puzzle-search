import mock
import unittest

from puzzlesearch.bin.play import parse_args, main


class TestPlay(unittest.TestCase):
    def test_parse_args(self):
        self.assertEqual(parse_args(["--player", "user"]).player, "user")
        self.assertEqual(parse_args(["--player", "agent"]).player, "agent")
        self.assertEqual(parse_args(["--puzzle-size", "3"]).puzzle_size, 3)
        self.assertEqual(parse_args([]).puzzle_size, 2)

    def test_main_agent_no_exceptions(self):
        main([])

    def test_main_user_no_exceptions(self):
        """
        The test only checks that main runs with user playing manually.
        The mock_inp raises an error to stop the game after the first user input.
        It is only checked that no other exception is raised before.
        """
        called_errror = "input was called"

        def mock_inp():
            raise RuntimeError(called_errror)

        with mock.patch("builtins.input", mock_inp):
            with self.assertRaises(RuntimeError) as cm:
                main(["--player", "user"])
                self.assertEqual(str(cm.exception), called_errror)
