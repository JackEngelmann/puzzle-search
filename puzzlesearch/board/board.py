import random
from itertools import product

"""
TODO:
- size < 2: throw error
"""

actions = ["right", "down", "up", "left"]


class Board:
    def __init__(self, size):
        self.size = size
        self.__initialize_state()

    def get_field(self, col_idx, row_idx):
        return self.state[row_idx][col_idx]

    def get_hash(self):
        return str(self.state)

    def is_won(self):
        positions = product(range(self.size), repeat=2)
        return all([self.__field_is_won(*p) for p in positions])

    def move(self, action):
        assert action in actions
        new_none_position = get_new_position(self.none_position, action)
        if is_valid_position(new_none_position, self.size):
            self.__swap(self.none_position, new_none_position)
            self.none_position = new_none_position

    def scramble(self):
        no_moves = random.randint(3, 100)
        for _ in range(no_moves):
            action = random.choice(actions)
            self.move(action)

    def copy(self):
        board = Board(self.size)
        board.state = [row.copy() for row in self.state]
        board.none_position = (self.none_position[0], self.none_position[1])
        return board

    def __initialize_state(self):
        size = self.size
        state = []

        for row_idx in range(size):
            state.append([])
            for col_idx in range(size):
                if col_idx == 0 and row_idx == 0:
                    state[row_idx].append(None)
                else:
                    state[row_idx].append(row_idx * size + col_idx)

        self.state = state
        self.none_position = (0, 0)

    def __field_is_won(self, col_idx, row_idx):
        field = self.get_field(col_idx, row_idx)
        if col_idx == 0 and row_idx == 0:
            return field == None
        target = row_idx * self.size + col_idx
        return field == target

    def __swap(self, pos_1, pos_2):
        self.state[pos_1[1]][pos_1[0]], self.state[pos_2[1]][pos_2[0]] = (
            self.state[pos_2[1]][pos_2[0]],
            self.state[pos_1[1]][pos_1[0]],
        )

    def __str__(self):
        separator = "-" * (self.size * 2 + 1)
        b_str = ""
        for row in self.state:
            b_str += f"{separator}\n|"
            for cell in row:
                b_str += f"{cell or ' '}|"
            b_str += "\n"
        b_str += separator
        return b_str


def get_new_position(pos, direction):
    assert direction in ["right", "left", "down", "up"]
    if direction == "right":
        return (pos[0] + 1, pos[1])
    if direction == "left":
        return (pos[0] - 1, pos[1])
    if direction == "down":
        return (pos[0], pos[1] + 1)
    if direction == "up":
        return (pos[0], pos[1] - 1)


def is_valid_position(pos, size):
    return pos[0] >= 0 and pos[0] < size and pos[1] >= 0 and pos[1] < size
