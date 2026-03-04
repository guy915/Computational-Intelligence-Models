from Direction import Direction


# Class representing a route.
class Route:

    """
    Route takes a starting coordinate to initialize
    @param start: the starting coordinate of the robot
    """
    def __init__(self, start):
        self.route = []
        self.start = start

    """
    After taking a step we add the direction we moved
    @param dir: the direction where the robot moved
    """
    def add(self, dir):
        self.route.append(dir)
        return

    """
    Returns the length of the route
    @return length of the route
    """
    def size(self):
        return len(self.route)

    """
    Getter for the list of directions
    @return the complete list of directions
    """
    def get_route(self):
        return self.route

    """
    Getter for the starting coordinate
    @return the starting coordinate of the robot
    """
    def get_start(self):
        return self.start

    """
    Function that checks whether a route is shoter than another route
    @param other: the route that we want to compare
    @return true if the current route is shorter
    """
    def shorter_than(self, other):
        return self.size() < other.size()

    """
    Take a step back in the route and return the last direction
    @return the last direction that was taken
    """
    def remove_last(self):
        return self.route.pop()

    """
    Build a string representing the route as the format specified in the assignment
    @return representation of the route in the correct format
    """
    def __str__(self):
        string = ""
        for dir in self.route:
            string += str(Direction.dir_to_int(dir))
            string += ";\n"
        return string

    """
    Equals method for route
    @param other: the route that we want to compare
    @return true if the two routes are equal
    """
    def __eq__(self, other):
        return self.start == other.start and self.route == other.route

    """
    Method that implements the specified format for writing a route to a file
    @param file_path: location where the route file should be stored
    """
    def write_to_file(self, file_path):
        f = open(file_path, "w")
        string = ""
        string += str(len(self.route))
        string += ";\n"
        string += str(self.start)
        string += ";\n"
        string += str(self)
        f.write(string)
