class GraphSearch:
    def search(self, problem):
        initial_node = Node(problem.initial_state)
        frontier = Frontier([initial_node], problem.get_state_hash)

        explored_set = ExploredSet(problem.get_state_hash)

        while True:
            if frontier.is_empty():
                return None

            leaf_node = frontier.pop()

            if problem.is_goal(leaf_node.state):
                return self.__get_solution(leaf_node)

            explored_set.add(leaf_node)

            new_nodes = self.__expand_node(problem, leaf_node)

            for new_node in new_nodes:
                if not frontier.includes(new_node) and not explored_set.includes(
                    new_node
                ):
                    frontier.add(new_node)

    def __expand_node(self, problem, node):
        new_nodes = []
        for action in problem.actions:
            resulting_state = problem.result(node.state, action)
            path_cost = node.path_cost + problem.path_cost(node.state, action)
            new_nodes.append(Node(resulting_state, node, path_cost, action))
        return new_nodes

    def __get_solution(self, node):
        assert node != None
        actions = []
        while True:
            if node == None:
                break
            if node.action != None:
                actions.insert(0, node.action)
            node = node.parent
        return actions


class Node:
    next_id = 0

    def __init__(self, state, parent=None, path_cost=0, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.id = Node.next_id
        Node.next_id += 1


class Frontier:
    def __init__(self, node_list, get_hash):
        self.node_list = node_list
        self.hash_set = set([get_hash(n.state) for n in node_list])
        self.get_hash = get_hash

    def add(self, node):
        self.node_list.append(node)
        self.hash_set.add(self.get_hash(node.state))

    def includes(self, node):
        return self.get_hash(node.state) in self.hash_set

    def pop(self):
        popped = self.node_list.pop(0)
        popped_hash = self.get_hash(popped.state)
        self.hash_set.remove(popped_hash)
        return popped

    def is_empty(self):
        return len(self.node_list) == 0


class ExploredSet:
    def __init__(self, get_hash):
        self.hash_set = set()
        self.get_hash = get_hash

    def add(self, node):
        self.hash_set.add(self.get_hash(node.state))

    def includes(self, node):
        return self.get_hash(node.state) in self.hash_set
