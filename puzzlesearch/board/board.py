from itertools import product

"""
TODO:
- size < 2: throw error
"""


class Board:
    def __init__(self, size):
        self.size = size
        self.__initialize_state()

    def copy(self):
        board = Board(self.size)
        board.state = [row.copy() for row in self.state]
        board.none_position = (self.none_position[0], self.none_position[1])
        return board

    def __initialize_state(self,):
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

    def get_field(self, col_idx, row_idx):
        return self.state[row_idx][col_idx]

    def move_right(self):
        none_pos = self.none_position
        if none_pos[0] == self.size - 1:
            return
        new_none_pos = (none_pos[0] + 1, none_pos[1])
        self.__swap(none_pos, new_none_pos)
        self.none_position = new_none_pos

    def move_left(self):
        none_pos = self.none_position
        if none_pos[0] == 0:
            return
        new_none_pos = (none_pos[0] - 1, none_pos[1])
        self.__swap(none_pos, new_none_pos)
        self.none_position = new_none_pos

    def move_down(self):
        none_pos = self.none_position
        if none_pos[1] == self.size - 1:
            return
        new_none_pos = (none_pos[0], none_pos[1] + 1)
        self.__swap(none_pos, new_none_pos)
        self.none_position = new_none_pos

    def move_up(self):
        none_pos = self.none_position
        if none_pos[1] == 0:
            return
        new_none_pos = (none_pos[0], none_pos[1] - 1)
        self.__swap(none_pos, new_none_pos)
        self.none_position = new_none_pos

    def __str__(self):
        b_str = ""
        for row in self.state:
            b_str += "-" * (self.size * 2 + 1)
            b_str += "\n"
            b_str += "|"
            for cell in row:
                b_str += str(cell) if cell != None else " "
                b_str += "|"
            b_str += "\n"
        b_str += "-" * (self.size * 2 + 1)
        return b_str

    def get_hash(self):
        return str(self.state)

    def __swap(self, pos_1, pos_2):
        self.state[pos_1[1]][pos_1[0]], self.state[pos_2[1]][pos_2[0]] = (
            self.state[pos_2[1]][pos_2[0]],
            self.state[pos_1[1]][pos_1[0]],
        )

    def is_won(self):
        positions = product(range(self.size), repeat=2)
        return all([self.__field_is_won(*p) for p in positions])

    def __field_is_won(self, col_idx, row_idx):
        field = self.get_field(col_idx, row_idx)
        if col_idx == 0 and row_idx == 0:
            return field == None
        target = row_idx * self.size + col_idx
        return field == target
