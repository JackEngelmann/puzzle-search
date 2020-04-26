from puzzlesearch.games.player_agent import PlayerAgent
import unittest


class TestPlayerAgent(unittest.TestCase):
    def test_init(self):
        player = PlayerAgent()
        self.assertRaises(NotImplementedError, player.plan_actions, None)
