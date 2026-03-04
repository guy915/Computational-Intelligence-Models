import re
import traceback
import sys
from Coordinate import Coordinate


# Specification of a path containing a start and end coordinate.
class PathSpecification:

    """
    Constructs a new path specification
    @param start: the starting coordinate of the robot
    @param end: the ending coordinate (goal) of the robot
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end

    """
    Get starting coordinate
    @return the starting coordinate of the robot
    """
    def get_start(self):
        return self.start

    """
    Get ending coordinate
    @return the ending coordinate (goal) of the robot
    """
    def get_end(self):
        return self.end

    """
    Equals method for PathSpecification
    @param other: the PathSpecification that we want to compare
    @return true if the two PathSpecifications are equal
    """
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    """
    String representation of the PathSpecifications
    @return a human-readable representation of the path
    """
    def __str__(self):
        return "Start: " + str(self.start) + " End: " + str(self.end)

    """
    Reads the coordinates file and returns a path specification
    @param file_path: location of the path that should be read from the file
    @return the PathSpecification contained in the file
    """
    @staticmethod
    def read_coordinates(file_path):
        try:
            f = open(file_path, "r")
            lines = f.read().splitlines()

            start = re.compile("[,;]\\s*").split(lines[0])
            start_x = int(start[0])
            start_y = int(start[1])

            end = re.compile("[,;]\\s*").split(lines[1])
            end_x = int(end[0])
            end_y = int(end[1])

            start_coordinate = Coordinate(start_x, start_y)
            end_coordinate = Coordinate(end_x, end_y)
            return PathSpecification(start_coordinate, end_coordinate)
        except FileNotFoundError:
            print("Error reading coordinate file " + file_path)
            traceback.print_exc()
            sys.exit()
