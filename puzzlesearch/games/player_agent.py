from puzzlesearch.search.graph_search import GraphSearch


class PlayerAgent:
    def __init__(self):
        self.planned_actions = None

    def get_action(self, state):
        if self.planned_actions == None:
            print("starts planning")
            self.planned_actions = self.plan_actions(state)
            print("finished planning")

        if not self.planned_actions:
            raise RuntimeError("agent has no idea what to do")
        action = self.planned_actions.pop(0)
        print(f"player agent acts: {action}")
        return action

    def plan_actions(self, state):
        raise NotImplementedError()
