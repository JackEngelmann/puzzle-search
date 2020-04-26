from puzzlesearch.games.player_manual import PlayerManual
from puzzlesearch.games.puzzle.puzzle_board import PuzzleBoard


class PuzzlePlayerManual(PlayerManual):
    def get_input_from_user(self):
        print(f"Available Actions: ({', '.join(PuzzleBoard.actions)})")
        print("Input:")
        return input().rstrip("\n")

    def get_action_from_input(self, inp):
        # key-choice: vim navigation keys
        if inp in ["right", "l"]:
            return "right"
        if inp in ["left", "h"]:
            return "left"
        if inp in ["down", "j"]:
            return "down"
        if inp in ["up", "k"]:
            return "up"
