import unittest

from puzzlesearch.games.player_agent import PlayerAgent


class TestPlayerAgent(unittest.TestCase):
    def test_get_action(self):
        agent = PlayerAgent()
        agent.plan_actions = lambda state: [1, 2, 3]
        actions = [
            agent.get_action(None),
            agent.get_action(None),
            agent.get_action(None),
        ]
        self.assertEqual(actions, [1, 2, 3])

    def test_get_action_no_actions(self):
        agent = PlayerAgent()
        agent.plan_actions = lambda state: []
        self.assertRaises(RuntimeError, agent.get_action, None)

    def test_get_action_planned_actions_none(self):
        agent = PlayerAgent()
        agent.plan_actions = lambda state: None
        self.assertRaises(RuntimeError, agent.get_action, None)
