import unittest
import mock
from puzzlesearch.game.puzzle_board import PuzzleBoard, get_random_no_moves

board_str = """-----
| |1|
-----
|2|3|
-----"""


class TestPuzzleBoard(unittest.TestCase):
    def test_initialize(self):
        board = PuzzleBoard(size=2)
        self.assertEqual(board.get_field(0, 0), None)
        self.assertEqual(board.get_field(1, 0), 1)
        self.assertEqual(board.get_field(0, 1), 2)
        self.assertEqual(board.get_field(1, 1), 3)

    def test_initialize_size_to_small(self):
        self.assertRaises(AssertionError, PuzzleBoard, size=1)

    def test_move_right(self):
        board = PuzzleBoard(size=2)
        board.move("right")
        self.assertEqual(board.get_field(0, 0), 1)
        self.assertEqual(board.get_field(1, 0), None)

    def test_move_right_already_right(self):
        board = PuzzleBoard(size=2)
        board.move("right")
        board.move("right")
        self.assertEqual(board.get_field(0, 0), 1)
        self.assertEqual(board.get_field(1, 0), None)

    def test_move_left(self):
        board = PuzzleBoard(size=2)
        board.move("right")
        self.assertEqual(board.get_field(0, 0), 1)
        self.assertEqual(board.get_field(1, 0), None)
        board.move("left")
        self.assertEqual(board.get_field(0, 0), None)
        self.assertEqual(board.get_field(1, 0), 1)

    def test_move_left_already_left(self):
        board = PuzzleBoard(size=2)
        board.move("left")
        self.assertEqual(board.get_field(0, 0), None)
        self.assertEqual(board.get_field(1, 0), 1)

    def test_move_down(self):
        board = PuzzleBoard(size=2)
        board.move("down")
        self.assertEqual(board.get_field(0, 0), 2)
        self.assertEqual(board.get_field(0, 1), None)

    def test_move_down_already_down(self):
        board = PuzzleBoard(size=2)
        board.move("down")
        self.assertEqual(board.get_field(0, 0), 2)
        self.assertEqual(board.get_field(0, 1), None)
        board.move("down")
        self.assertEqual(board.get_field(0, 0), 2)
        self.assertEqual(board.get_field(0, 1), None)

    def test_up(self):
        board = PuzzleBoard(size=2)
        board.move("down")
        self.assertEqual(board.get_field(0, 0), 2)
        self.assertEqual(board.get_field(0, 1), None)
        board.move("up")
        self.assertEqual(board.get_field(0, 0), None)
        self.assertEqual(board.get_field(0, 1), 2)

    def test_up_already_up(self):
        board = PuzzleBoard(size=2)
        board.move("up")
        self.assertEqual(board.get_field(0, 0), None)
        self.assertEqual(board.get_field(0, 1), 2)

    def test_board_str(self):
        board = PuzzleBoard(size=2)
        self.assertEqual(board_str, board.__str__())

    def test_get_none_position_1(self):
        board = PuzzleBoard(size=2, state=[[None, 1], [2, 3]])
        none_position = board.get_none_position()
        self.assertEqual(none_position, (0, 0))

    def test_get_none_position_2(self):
        board = PuzzleBoard(size=2, state=[[1, 1], [None, 3]])
        none_position = board.get_none_position()
        self.assertEqual(none_position, (0, 1))

    def test_get_none_position_3(self):
        board = PuzzleBoard(size=2, state=[[1, None], [2, 3]])
        none_position = board.get_none_position()
        self.assertEqual(none_position, (1, 0))

    def test_is_finished_true(self):
        board = PuzzleBoard(size=2, state=[[None, 1], [2, 3]])
        self.assertTrue(board.is_finished())

    def test_is_finished_false(self):
        board = PuzzleBoard(size=2, state=[[1, None], [2, 3]])
        self.assertFalse(board.is_finished())

    def test_scramble(self):
        board = PuzzleBoard(size=2)
        board.scramble()
        self.assertFalse(board.is_finished())

    def test_scramble_called_twice_when_first_is_finished(self):
        board = PuzzleBoard(size=2)
        mock_is_finished = mock.Mock(side_effect=[True, False])
        board.is_finished = mock_is_finished
        board.scramble()
        self.assertEqual(mock_is_finished.call_count, 2)
