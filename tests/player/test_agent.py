import unittest

from puzzlesearch.player.agent import PlayerAgent


class TestUser(unittest.TestCase):
    def test_do_move(self):
        agent = PlayerAgent(lambda state: [1, 2, 3])
        actions = [
            agent.do_move(None),
            agent.do_move(None),
            agent.do_move(None),
        ]
        self.assertEqual(actions, [1, 2, 3])

    def test_do_move_no_actions(self):
        agent = PlayerAgent(lambda state: [])
        self.assertRaises(RuntimeError, agent.do_move, None)

    def test_do_move_planned_actions_none(self):
        agent = PlayerAgent(lambda state: None)
        self.assertRaises(RuntimeError, agent.do_move, None)
