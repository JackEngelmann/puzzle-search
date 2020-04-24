class Node:
    def __init__(self, state, parent=None, path_cost=1, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost


class SearchTree:
    def __init__(self, board):
        self.board = board
        self.nodes = [Node(board)]

    def explore(self, node):
        right_board = node.state.copy()
        right_board.move_right()
        right_node = Node(right_board, node, node.path_cost + 1, "right")
        left_board = node.state.copy()
        left_board.move_left()
        left_node = Node(left_board, node, node.path_cost + 1, "left")
        down_board = node.state.copy()
        down_board.move_down()
        down_node = Node(down_board, node, node.path_cost + 1, "down")
        up_board = node.state.copy()
        up_board.move_up()
        up_node = Node(up_board, node, node.path_cost + 1, "up")
        return [right_node, left_node, up_node, down_node]
