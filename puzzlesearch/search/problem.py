class PuzzleProblem:
    def __init__(self, board):
        self.initial_state = board
        self.actions = ["left", "right", "down", "up"]

    def result(self, board, action):
        board = board.copy()
        if action == "right":
            board.move_right()
        if action == "left":
            board.move_left()
        if action == "down":
            board.move_down()
        if action == "up":
            board.move_up()
        return board

    def is_goal(self, board):
        return board.is_won()

    def path_cost(self, board, action):
        return 1

    def get_state_hash(self, state):
        return state.get_hash()
