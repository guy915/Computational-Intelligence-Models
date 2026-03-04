import numpy as np
from matplotlib import pyplot as plt


# Class that provides functionality to visualize the mazes and routes taken by your robot.
class Visualizer:

    def __init__(self):
        pass

    """
    Visualizes an empty maze
    @param maze: the maze (environment) for the robot
    """
    @staticmethod
    def visualize_maze(maze):
        maze_array = np.array(maze.walls)
        maze_array = maze_array.T

        cmap = plt.cm.binary
        cmap.set_bad(cmap(0))

        fig, ax = plt.subplots(figsize=(10, 10))
        ax.imshow(maze_array, cmap=cmap, interpolation='nearest', vmin=0, vmax=1)
        plt.show()
        return

    """
    Helper method for the visualization of maze paths
    @param maze: the Maze object representing the environment for the robot
    @param route_list: the list of routes taken
    @param spec: the PathSpecification describing the problem
    @param list_of_coords: list of coordinates for product locations
    """
    @staticmethod
    def visualize_maze_with_path(maze, route_list, spec, list_of_coords):
        size = 10
        maze_array = np.array(maze.walls)
        maze_array = maze_array.T
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.imshow(maze_array, cmap='binary', interpolation='nearest')

        start_x = spec.start.x
        start_y = spec.start.y

        end_x = spec.end.x
        end_y = spec.end.y

        ant_path = [(start_x, start_y)] # initially with starting position

        x, y = start_x, start_y
        for i in range(len(route_list) - 1):
            for direction in route_list[i].route:
                if direction.value == 0:  # East
                    x += 1
                elif direction.value == 1:  # North
                    y -= 1
                elif direction.value == 2:  # West
                    x -= 1
                elif direction.value == 3:  # South
                    y += 1

                ant_path.append((x, y))

        ant_path_array = np.array(ant_path)

        final_path = [ant_path_array[-1]]

        for direction in route_list[-1].route:
            if direction.value == 0:  # East
                x += 1
            elif direction.value == 1:  # North
                y -= 1
            elif direction.value == 2:  # West
                x -= 1
            elif direction.value == 3:  # South
                y += 1

            final_path.append((x, y))

        final_path_array = np.array(final_path)

        # Plotting the ant's path on top of the maze
        # Since we use a route list, this draws up all the routes except the final route
        ax.plot(ant_path_array[:, 0], ant_path_array[:, 1], color='red', linestyle='-', markerfacecolor='red', markeredgecolor='red', markersize=size*0.8)

        # Plotting the final route on top of the maze (final travel between 2 stipulated points)
        ax.plot(final_path_array[:, 0], final_path_array[:, 1], color='pink', linestyle='-', markerfacecolor='red', markeredgecolor='red', markersize=size*0.8)

        # Blue circle at the starting point
        ax.scatter(start_x, start_y, color='blue', marker='o', s=100, label='Start Point')

        # Green circle at the destination point
        ax.scatter(end_x, end_y, color='green', marker='o', s=100, label='End Point')

        for product_number, coord in enumerate(list_of_coords):
            # For the TSP, this plots purple circles for each of the product locations, with the product number on top of it.
            ax.scatter(coord.x, coord.y, color='purple', marker='o', s=100, label='Product point')
            ax.annotate(product_number, (coord.x, coord.y), textcoords="offset points", xytext=(0,-3), ha='center', size=7, color='white')

        plt.show()

    """
    Method to visualize the path taken for TSP. Plots a series of visualizations, from start to first product, then
    from product to product, and finally from the final product to end. Use this method for Traveling Robot Problem.
    @param maze: the Maze object representing the environment for the robot
    @param product_order: a solution to the TSP problem
    @param tsp_data: the TSPData object for the TSP problem
    """
    @staticmethod
    def visualize_tsp_solution_paths(maze, product_order, tsp_data):
        spec = tsp_data.spec
        route_list = [tsp_data.start_to_product[product_order[0]]]
        product_locations = tsp_data.product_locations

        # Visualizes path from start to the first product recorded in the product_order
        Visualizer.visualize_maze_with_path(maze, route_list, spec, product_locations)

        for i in range(len(product_order) - 1):
            current_route = tsp_data.product_to_product[product_order[i]][product_order[i+1]]
            route_list.append(current_route)

            # Visualizes path between 2 subsequent product_locations
            Visualizer.visualize_maze_with_path(maze, route_list, spec, product_locations)

        route_list.append(tsp_data.product_to_end[product_order[-1]])

        # Visualizes path between the last product location and the end of the maze
        Visualizer.visualize_maze_with_path(maze, route_list, spec, product_locations)

    """
    Method to visualize an individual path from start to end, for the Ant Colony Optimization problem
    @param maze: the Maze object representing the environment for the robot
    @param route: the complete Route from the starting location to the destination
    @param spec: the PathSpecification describing the problem
    """
    @staticmethod
    def visualize_individual_path(maze, route, spec):
        Visualizer.visualize_maze_with_path(maze, [route], spec, [])
