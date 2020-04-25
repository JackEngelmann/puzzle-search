import unittest
from puzzlesearch.game.puzzle_board import PuzzleBoard
from puzzlesearch.game.game import Game
from puzzlesearch.search.puzzle_problem import PuzzleProblem
from puzzlesearch.search.graph_search import GraphSearch


class UnsolvableProblem:
    def __init__(self):
        self.initial_state = 1
        self.actions = ["a", "b"]

    def result(self, state, action):
        if action == "a":
            return 2
        if action == "a":
            return 3

    def is_goal(self, state):
        return state == 4

    def path_cost(self, state, action):
        return 1

    def get_state_hash(self, state):
        return str(state)


class TestGraphSearch(unittest.TestCase):
    def test_search_simple(self):
        board = PuzzleBoard(size=2)
        board.move("right")
        problem = PuzzleProblem(board)
        graph_search = GraphSearch()
        solution = graph_search.search(problem)
        self.__assert_successful_actions(board, solution)

    def test_search_scrambled(self):
        board = PuzzleBoard(size=3)
        board.scramble()
        problem = PuzzleProblem(board)
        graph_search = GraphSearch()
        solution = graph_search.search(problem)
        self.__assert_successful_actions(board, solution)

    def test_search_already_winning(self):
        board = PuzzleBoard(size=2)
        problem = PuzzleProblem(board)
        graph_search = GraphSearch()
        solution = graph_search.search(problem)
        self.__assert_successful_actions(board, solution)

    def test_search_return_none_when_unsolvable(self):
        problem = UnsolvableProblem()
        graph_search = GraphSearch()
        solution = graph_search.search(problem)
        self.assertIsNone(solution)

    def __assert_successful_actions(self, board, solution):
        self.assertIsNotNone(solution)
        for direction in solution:
            board.move(direction)
        self.assertTrue(board.is_finished())
