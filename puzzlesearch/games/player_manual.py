class PlayerManual:
    def get_action(self, board):
        inp = self.get_input_from_user()
        action = self.get_action_from_input(inp)
        if action == None:
            return self.get_action(board)
        return action

    def get_input_from_user(self):
        raise NotImplementedError()

    def get_action_from_input(self, input):
        raise NotImplementedError()
