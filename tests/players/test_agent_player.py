import unittest

from puzzlesearch.players.agent_player import AgentPlayer


class TestAgentPlayer(unittest.TestCase):
    def test_do_move(self):
        agent = AgentPlayer(lambda state: [1, 2, 3])
        actions = [
            agent.do_move(None),
            agent.do_move(None),
            agent.do_move(None),
        ]
        self.assertEqual(actions, [1, 2, 3])

    def test_do_move_no_actions(self):
        agent = AgentPlayer(lambda state: [])
        self.assertRaises(RuntimeError, agent.do_move, None)

    def test_do_move_planned_actions_none(self):
        agent = AgentPlayer(lambda state: None)
        self.assertRaises(RuntimeError, agent.do_move, None)
