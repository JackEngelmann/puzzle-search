import unittest
from puzzlesearch.board.board import Board

board_str = """-----
| |1|
-----
|2|3|
-----"""


class TestBoard(unittest.TestCase):
    def test_initialize(self):
        board = Board(size=2)
        self.assertEqual(board.get_field(0, 0), None)
        self.assertEqual(board.get_field(1, 0), 1)
        self.assertEqual(board.get_field(0, 1), 2)
        self.assertEqual(board.get_field(1, 1), 3)

    def test_move_right(self):
        board = Board(size=2)
        board.move_right()
        self.assertEqual(board.get_field(0, 0), 1)
        self.assertEqual(board.get_field(1, 0), None)

    def test_move_right_already_right(self):
        board = Board(size=2)
        board.move_right()
        board.move_right()
        self.assertEqual(board.get_field(0, 0), 1)
        self.assertEqual(board.get_field(1, 0), None)

    def test_move_left(self):
        board = Board(size=2)
        board.move_right()
        self.assertEqual(board.get_field(0, 0), 1)
        self.assertEqual(board.get_field(1, 0), None)
        board.move_left()
        self.assertEqual(board.get_field(0, 0), None)
        self.assertEqual(board.get_field(1, 0), 1)

    def test_move_left_already_left(self):
        board = Board(size=2)
        board.move_left()
        self.assertEqual(board.get_field(0, 0), None)
        self.assertEqual(board.get_field(1, 0), 1)

    def test_move_down(self):
        board = Board(size=2)
        board.move_down()
        self.assertEqual(board.get_field(0, 0), 2)
        self.assertEqual(board.get_field(0, 1), None)

    def test_move_down_already_down(self):
        board = Board(size=2)
        board.move_down()
        self.assertEqual(board.get_field(0, 0), 2)
        self.assertEqual(board.get_field(0, 1), None)
        board.move_down()
        self.assertEqual(board.get_field(0, 0), 2)
        self.assertEqual(board.get_field(0, 1), None)

    def test_up(self):
        board = Board(size=2)
        board.move_down()
        self.assertEqual(board.get_field(0, 0), 2)
        self.assertEqual(board.get_field(0, 1), None)
        board.move_up()
        self.assertEqual(board.get_field(0, 0), None)
        self.assertEqual(board.get_field(0, 1), 2)

    def test_up_already_up(self):
        board = Board(size=2)
        board.move_up()
        self.assertEqual(board.get_field(0, 0), None)
        self.assertEqual(board.get_field(0, 1), 2)

    def test_board_str(self):
        board = Board(size=2)
        self.assertEqual(board_str, board.__str__())

    def test_is_won_true(self):
        board = Board(size=2)
        self.assertTrue(board.is_won())

    def test_is_won_false(self):
        board = Board(size=2)
        board.move_right()
        self.assertFalse(board.is_won())


"-----\n| |1|\n-----\n|2|3|\n-----"
"-----\n| |1|-----\n|2|3|\n-----"
