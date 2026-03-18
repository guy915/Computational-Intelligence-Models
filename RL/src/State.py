"""
A state is defined by an x and y coordinate which determine its location
in the grid and whether the state is a path (1) or a wall (0).
"""


class State:
    def __init__(self, state_id, x, y, state_type, done=False):
        self.id = state_id
        self.x = x
        self.y = y
        self.type = str(state_type)
        self.done = done

    def __str__(self):
        return f"State(id: {self.id}, x: {self.x} , y: {self.y}, type: {self.type}"

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))
