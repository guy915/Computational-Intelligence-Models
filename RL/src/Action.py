"""
Each action has an id that determines the type of action:
up, down, left, right.
"""


class Action:
    def __init__(self, action_id):
        self.id = str(action_id)

    def __str__(self):
        return str(self.id)

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))
