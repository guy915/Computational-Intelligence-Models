"""
This file shows all valid actions for an agent, makes the agent
take a step in its environment and reset its location to its starting point.
"""

from Maze import Maze
from Action import Action
from State import State


class Agent:
    def __init__(self, start_x: int, start_y: int):
        self.start_x = start_x
        self.start_y = start_y
        self.x = start_x
        self.y = start_y
        self.nr_of_actions_since_reset = 0

    def get_state(self, maze: Maze) -> State:
        """
        Returns the current state of the agent.
        """
        return maze.get_state(self.x, self.y)

    def get_valid_actions(self, maze: Maze):
        """
        Returns a list of all valid actions for the agent.
        """
        actions = []
        if self.y > 0 and maze.is_walkable(self.x, self.y - 1):
            actions.append(Action("up"))
        if self.y < maze.height - 1 and maze.is_walkable(self.x, self.y + 1):
            actions.append(Action("down"))
        if self.x > 0 and maze.is_walkable(self.x - 1, self.y):
            actions.append(Action("left"))
        if self.x < maze.width - 1 and maze.is_walkable(self.x + 1, self.y):
            actions.append(Action("right"))
        return actions

    def step(self, action: Action, maze: Maze):
        """
        Take a step in the environment according to the action.
        """
        if action.id == "up":
            self.y -= 1
        if action.id == "down":
            self.y += 1
        if action.id == "left":
            self.x -= 1
        if action.id == "right":
            self.x += 1
        self.nr_of_actions_since_reset += 1

        # get next state, reward for transitioning to next state and
        # whether next state is terminal or not.
        next_state = self.get_state(maze)
        reward = maze.get_reward(next_state.x, next_state.y)
        done = next_state.done
        return next_state, reward, done

    def reset(self):
        """
        Reset the agent to its starting location.
        """
        self.x = self.start_x
        self.y = self.start_y
        self.nr_of_actions_since_reset = 0
