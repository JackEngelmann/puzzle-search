import unittest
from puzzlesearch.games.player_manual import PlayerManual


class TestPlayerManual(unittest.TestCase):
    def test_init(self):
        player = PlayerManual()
        self.assertRaises(NotImplementedError, player.get_input_from_user)
        self.assertRaises(NotImplementedError, player.get_action_from_input, None)
