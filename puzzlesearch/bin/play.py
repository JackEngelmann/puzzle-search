import sys
import argparse

from puzzlesearch.games.puzzle.puzzle_game import PuzzleGame
from puzzlesearch.games.puzzle.puzzle_problem import PuzzleProblem
from puzzlesearch.search.graph_search import GraphSearch


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--player", default="agent", type=str)
    parser.add_argument("--puzzle-size", dest="puzzle_size", default=2, type=int)
    return parser.parse_args(args)


def main(args=sys.argv[1:]):
    parsed_args = parse_args(args)
    game = PuzzleGame(parsed_args.puzzle_size, parsed_args.player)
    game.start()
