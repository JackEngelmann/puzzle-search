class PlayerUser:
    def do_move(self, board):
        print("Input: (down, up, left, right) ")
        inp = get_input()
        action = get_action(inp)
        if action == None:
            return self.do_move(board)
        return action


def get_input():
    return input().rstrip("\n")


def get_action(inp):
    # key-choice: vim navigation keys
    if inp in ["right", "l"]:
        return "right"
    if inp in ["left", "h"]:
        return "left"
    if inp in ["down", "j"]:
        return "down"
    if inp in ["up", "k"]:
        return "up"
