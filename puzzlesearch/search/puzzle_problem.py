class PuzzleProblem:
    def __init__(self, board):
        self.initial_state = board
        self.actions = board.actions

    def result(self, board, action):
        assert board != None
        resulting_board = board.copy()
        resulting_board.move(action)
        return resulting_board

    def is_goal(self, board):
        return board.is_finished()

    def path_cost(self, board, action):
        return 1

    def get_state_hash(self, state):
        return state.get_hash()
