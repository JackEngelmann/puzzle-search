import sys
import argparse

from puzzlesearch.players.agent_player import AgentPlayer
from puzzlesearch.players.manual_player import ManualPlayer
from puzzlesearch.game.puzzle_game import PuzzleGame
from puzzlesearch.search.puzzle_problem import PuzzleProblem
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
    player = ManualPlayer() if parsed_args.user else AgentPlayer(plan_actions)
    game = PuzzleGame(parsed_args.size, player)
    game.start()
