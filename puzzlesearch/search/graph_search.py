class Node:
    def __init__(self, state, parent=None, path_cost=0, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost


class GraphSearch:
    def search(self, problem):
        frontier = [Node(problem.initial_state)]
        frontier_hash = set([problem.get_state_hash(problem.initial_state)])
        explored_set_hash = set()

        while True:
            if len(frontier) == 0:
                return None
            leaf_node = frontier.pop()
            frontier_hash.remove(problem.get_state_hash(leaf_node.state))
            if problem.is_goal(leaf_node.state):
                return leaf_node
            explored_set_hash.add(problem.get_state_hash(leaf_node.state))

            # expand node
            new_nodes = self.__expand_node(problem, leaf_node)
            for new_node in new_nodes:
                new_node_hash = problem.get_state_hash(new_node.state)
                if (not (new_node_hash in explored_set_hash)) and (
                    not (new_node_hash in frontier_hash)
                ):
                    frontier.append(new_node)
                    frontier_hash.add(new_node_hash)

    def __expand_node(self, problem, node):
        new_nodes = []
        for action in problem.actions:
            resulting_state = problem.result(node.state, action)
            path_cost = node.path_cost + problem.path_cost(node.state, action)
            new_nodes.append(Node(resulting_state, node, path_cost, action))
        return new_nodes


def get_actions(node):
    actions_in_reverse = get_actions_recursive(node, [])
    return list(reversed(actions_in_reverse))


def get_actions_recursive(node, actions=[]):
    if node == None:
        return actions
    if node.parent == None:
        return actions
    new_actions = actions + [node.action]
    return get_actions_recursive(node.parent, new_actions)
