import sys
import argparse

from puzzlesearch.board.board import Board
from puzzlesearch.player.agent import PlayerAgent
from puzzlesearch.player.user import PlayerUser
from puzzlesearch.game.game import Game
from puzzlesearch.problem.puzzle_problem import PuzzleProblem
from puzzlesearch.search.graph_search import GraphSearch


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", action="store_true")
    parser.add_argument("--size", default=2, type=int)
    return parser.parse_args(args)


def plan_actions(board):
    problem = PuzzleProblem(board)
    return GraphSearch().search(problem)


def main(args=sys.argv[1:]):
    parsed_args = parse_args(args)
    board = Board(parsed_args.size)
    board.scramble()
    if parsed_args.user:
        player = PlayerUser()
    else:
        player = PlayerAgent(plan_actions)
    game = Game(board, player)
    game.start()
