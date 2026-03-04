from Direction import Direction


# Class representing a coordinate.
class Coordinate:

    """
    Constructs a new coordinate object.
    @param x: the x coordinate
    @param y: the y coordinate
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """
    Add a coordinate to this coordinate
    @param other: the new coordinate to be added
    @return the resulting coordinate (a new instance)
    """
    def add_coordinate(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    """
    Move in a direction from this coordinate
    @param dir: direction of unit move
    @return the new coordinate
    """
    def add_direction(self, dir):
        return self.add_coordinate(self.dir_to_coordinate_delta(dir))

    """
    Substract a coordinate from the current coordinate
    @param other: the coordinate to be subtracted
    @return the new coordinate
    """
    def subtract_coordinate(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    """
    Move in a inverted direction from this coordinate
    @param dir: the direction of unit move
    @return the new coordinate
    """
    def subtract_direction(self, dir):
        return self.subtract_coordinate(self.dir_to_coordinate_delta(dir))

    """
    String representation of coordinate
    @return the representation of coordinate
    """
    def __str__(self):
        return str(self.x) + ", " + str(self.y)

    """
    Equals method for Coordinate
    @param other: the other coordinate to check for equality
    @return true if two coordinates are equal
    """
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    """
    Check whether a point lies between a x range with [low,up)
    @param low: lower bound of the range
    @param up: upper bound of the range (non-inclusive)
    @return true if the point lies between the two coordinates
    """
    def x_between(self, low, up):
        return low <= self.x and self.x < up

    """
    Check whether a point lies between a y range with [low,up)
    @param low: lower bound of the range
    @param up: upper bound of the range (non-inclusive)
    @return true if the point lies between the two coordinates
    """
    def y_between(self, low, up):
        return low <= self.y and self.y < up

    """
    Returns x position
    @return x
    """
    def get_x(self):
        return self.x

    """
    Returns y position
    @return y
    """
    def get_y(self):
        return self.y

    """
    Get vector (coordinate) of a certain direction.
    @param dir: the direction of interest
    @return the coordinate in the specified direction
    """
    def dir_to_coordinate_delta(self, dir):
        # all directions in a vector
        # Creates a map with a direction linked to its (direction) vector.
        map = {}
        map[Direction.east] = Coordinate(1, 0)
        map[Direction.west] = Coordinate(-1, 0)
        map[Direction.north] = Coordinate(0, -1)
        map[Direction.south] = Coordinate(0, 1)
        return map[dir]
