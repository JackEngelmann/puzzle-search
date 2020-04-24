import unittest
from puzzlesearch.board.board import Board
from puzzlesearch.game.game import Game
from puzzlesearch.player.agent import PuzzleProblem
from puzzlesearch.search.graph_search import GraphSearch


class TestGraphSearch(unittest.TestCase):
    def test_search_simple(self):
        board = Board(size=2)
        board.move("right")
        problem = PuzzleProblem(board)
        graph_search = GraphSearch()
        solution = graph_search.search(problem)
        self.__assert_successful_actions(board, solution)

    def test_search_scrambled(self):
        board = Board(size=3)
        board.scramble()
        problem = PuzzleProblem(board)
        graph_search = GraphSearch()
        solution = graph_search.search(problem)
        self.__assert_successful_actions(board, solution)

    def test_search_already_winning(self):
        board = Board(size=2)
        problem = PuzzleProblem(board)
        graph_search = GraphSearch()
        solution = graph_search.search(problem)
        self.__assert_successful_actions(board, solution)

    def __assert_successful_actions(self, board, solution):
        self.assertIsNotNone(solution)
        for direction in solution:
            board.move(direction)
        self.assertTrue(board.is_won())
