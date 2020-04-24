import argparse

from puzzlesearch.board.board import Board
from puzzlesearch.player.agent import PlayerAgent
from puzzlesearch.player.user import PlayerUser
from puzzlesearch.game.game import Game


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", action="store_true")
    parser.add_argument("--size", default=2, type=int)
    return parser.parse_args()


def main():
    args = parse_args()
    board = Board(args.size)
    if args.user:
        player = PlayerUser()
    else:
        player = PlayerAgent()
    game = Game(board, player)
    game.start()
