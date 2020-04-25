import unittest

from puzzlesearch.players.agent_player import AgentPlayer


class TestAgentPlayer(unittest.TestCase):
    def test_get_action(self):
        agent = AgentPlayer(lambda state: [1, 2, 3])
        actions = [
            agent.get_action(None),
            agent.get_action(None),
            agent.get_action(None),
        ]
        self.assertEqual(actions, [1, 2, 3])

    def test_get_action_no_actions(self):
        agent = AgentPlayer(lambda state: [])
        self.assertRaises(RuntimeError, agent.get_action, None)

    def test_get_action_planned_actions_none(self):
        agent = AgentPlayer(lambda state: None)
        self.assertRaises(RuntimeError, agent.get_action, None)
