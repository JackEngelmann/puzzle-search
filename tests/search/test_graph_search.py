import unittest
from puzzlesearch.board.board import Board
from puzzlesearch.game.game import Game
from puzzlesearch.search.problem import PuzzleProblem
from puzzlesearch.search.graph_search import GraphSearch
from puzzlesearch.search.search_tree import SearchTree


class TestSearchStrategy(unittest.TestCase):
    def test_search_simple(self):
        board = Board(size=2)
        board.move_right()
        problem = PuzzleProblem(board)
        graph_search = GraphSearch()
        winning_node = graph_search.search(problem)
        self.assertTrue(winning_node != None)
        self.assertTrue(winning_node.state.is_won())

    def test_search_scrambled(self):
        for _ in range(1):
            board = Board(size=3)
            game = Game(board)
            game.scramble()
            problem = PuzzleProblem(board)
            graph_search = GraphSearch()
            winning_node = graph_search.search(problem)
            self.assertTrue(winning_node != None)
            self.assertTrue(winning_node.state.is_won())

    def test_search_already_winning(self):
        board = Board(size=2)
        problem = PuzzleProblem(board)
        graph_search = GraphSearch()
        winning_node = graph_search.search(problem)
        self.assertTrue(winning_node != None)
        self.assertTrue(winning_node.state.is_won())
