"""
This file loads the maze, visualizes it, allows to set rewards and terminal states,
and get information about states e.g., whether the state is a wall or if it is within bounds.
"""

from State import State

import matplotlib.pyplot as plt
import numpy as np
from typing import List


class Maze:
    def __init__(self, file_path: str) -> None:
        """
        Initialize the maze from a file. The file should be a text file
        where the first line contains the width and height of the maze.
        """
        try:
            f = open(file_path, "r")
            lines = f.readlines()
            width, height = lines[0].split(" ")

            self.width = int(width)
            self.height = int(height)
            # initialize states with None: height x width. 
            self.states = {i: {j: None for j in range(self.width)} for i in range(self.height)}
            # initialize rewards with zero: height x width.
            self.rewards = {i: {j: 0 for j in range(self.width)} for i in range(self.height)}

            for row_idx, row in enumerate(lines[1:]):
                vals = row.split(" ")[:-1]
                for col_idx, val in enumerate(vals):
                    state_type = "wall" if val == "0" else "path"
                    state_id = row_idx * self.width + col_idx
                    state = State(state_id=state_id, x=col_idx, y=row_idx, state_type=state_type, done=False)
                    self.states[row_idx][col_idx] = state

        except FileNotFoundError:
            print(f"Error reading maze file {file_path}")

    def get_state(self, x: int, y: int) -> State:
        """
        Returns the state at the given coordinates.
        """
        return self.states[y][x]

    def get_all_states(self) -> List[State]:
        """
        Returns a list of all states in the maze.
        """
        states = []
        for row in self.states.values():
            for state in row.values():
                states.append(state)
        return states

    def set_reward(self, x: int, y: int, reward: int):
        """
        Set a reward for the given state.
        """
        self.rewards[y][x] = reward

    def get_reward(self, x: int, y: int) -> int:
        """
        Get the reward for the given state.
        """
        return self.rewards[y][x]

    def set_terminal(self, x: int, y: int):
        """
        Mark the given state as a terminal state.
        """
        state = self.get_state(x, y)
        state.done = True

    def is_walkable(self, x: int, y: int) -> bool:
        """
        Check if the given coordinates is a walkable state or a wall.
        """
        state = self.get_state(x, y)
        return state.type == "path"

    def check_bounds(self, x: int, y: int) -> bool:
        """
        Check if the given coordinates are within the bounds of the maze.
        """
        return x in range(0, self.width) and y in range(0, self.height)

    def visualize(self, path):
        """
        Visualize the maze and the given path. A path is a list of (y, x) tuples,
        where each tuple represents a state that was visited by the agent during exploration.
        """

        img = np.zeros((self.height, self.width, 3))

        # plot maze.
        for state in self.get_all_states():
            img[state.y][state.x] = [1.0] * 3 if self.is_walkable(state.x, state.y) else [0.0] * 3

        # plot given path.
        for pt in path:
            y, x = pt
            img[y][x] = [.5, .5, .75]

        # plot terminal states.
        _, ax = plt.subplots()

        terminal_states = [s for s in self.get_all_states() if s.done]
        for terminal in terminal_states:
            x, y = terminal.x, terminal.y
            img[y][x] = [1., 0., 0.]
            ax.text(x=x, y=y, s='x', color='white', fontsize=12, ha='center', va='center')

        ax.imshow(img)
        plt.show()
