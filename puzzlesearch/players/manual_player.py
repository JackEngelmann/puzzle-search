from puzzlesearch.game.puzzle_board import PuzzleBoard


class ManualPlayer:
    def get_action(self, board):
        inp = self.__get_input_from_user()
        action = self.__get_action_from_input(inp)
        if action == None:
            return self.get_action(board)
        return action

    def __get_input_from_user(self):
        print(f"Available Actions: ({', '.join(PuzzleBoard.actions)})")
        print("Input:")
        return input().rstrip("\n")

    def __get_action_from_input(self, inp):
        # key-choice: vim navigation keys
        if inp in ["right", "l"]:
            return "right"
        if inp in ["left", "h"]:
            return "left"
        if inp in ["down", "j"]:
            return "down"
        if inp in ["up", "k"]:
            return "up"
