from puzzlesearch.search.graph_search import GraphSearch


class PlayerAgent:
    def __init__(self):
        self.planned_actions = None

    def do_move(self, board):
        if self.planned_actions == None:
            print("starts planning", end=" ... ")
            puzzle_problem = PuzzleProblem(board)
            graph_search = GraphSearch()
            solution = graph_search.search(puzzle_problem)
            print(solution)
            self.planned_actions = solution
        action = self.planned_actions.pop(0)
        print(f"Puzzle player logs in: {action}")
        return action


class PuzzleProblem:
    def __init__(self, board):
        self.initial_state = board
        self.actions = ["left", "right", "down", "up"]

    def result(self, board, action):
        assert board != None
        resulting_board = board.copy()
        resulting_board.move(action)
        return resulting_board

    def is_goal(self, board):
        return board.is_won()

    def path_cost(self, board, action):
        return 1

    def get_state_hash(self, state):
        return state.get_hash()
