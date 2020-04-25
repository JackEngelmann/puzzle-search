from puzzlesearch.search.graph_search import GraphSearch


class AgentPlayer:
    def __init__(self, plan_actions):
        self.planned_actions = None
        self.plan_actions = plan_actions

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
