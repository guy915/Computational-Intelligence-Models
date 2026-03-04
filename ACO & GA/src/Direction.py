import enum


# Enum representing the directions an ant can take.
class Direction(enum.Enum):
    east = 0
    north = 1
    west = 2
    south = 3

    """
    Convert direction to an integer representation.
    @param dir: the direction of interest
    @return the corresponding integer from 0 to 3
    """
    @classmethod
    def dir_to_int(cls, dir):
        return dir.value
