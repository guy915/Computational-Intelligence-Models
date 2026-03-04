import pickle
import re
import sys
import traceback
from Coordinate import Coordinate
from PathSpecification import PathSpecification


# Class containing the product distances. Can be either build from a maze,
# a list of product locations and a PathSpecification or be loaded from a file.
class TSPData:

    """
    Constructs a new TSPData object
    @param product_locations: the locations of all products in the maze
    @param spec: the path specification for the maze
    """
    def __init__(self, product_locations, spec):
        self.product_locations = product_locations
        self.spec = spec

        self.distances = None
        self.start_distances = None
        self.end_distances = None
        self.product_to_product = None
        self.start_to_product = None
        self.product_to_end = None

    """
    Calculate the routes from the product locations to each other, the start, and the end
    Additionally generate arrays that contain the length of all the routes
    @param aco: the AntColonyOptimization object that can be used to generate routes
    """
    def calculate_routes(self, aco):
        self.product_to_product = self.build_distance_matrix(aco)
        self.start_to_product = self.build_start_to_products(aco)
        self.product_to_end = self.build_products_to_end(aco)
        self.build_distance_lists()
        return

    """
    Build a list of integer distances of all the product-product routes.
    """
    def build_distance_lists(self):
        number_of_products = len(self.product_locations)
        self.distances = []
        self.start_distances = []
        self.end_distances = []

        for i in range(number_of_products):
            self.distances.append([])
            for j in range(number_of_products):
                self.distances[i].append(self.product_to_product[i][j].size())
            self.start_distances.append(self.start_to_product[i].size())
            self.end_distances.append(self.product_to_end[i].size())
        return

    """
    Getter for the distance between each pair of products
    @return the list of distances between products
    """
    def get_distances(self):
        return self.distances

    """
    Getter for the distance between the starting location and each product
    @return the list of distances to products
    """
    def get_start_distances(self):
        return self.start_distances

    """
    Getter for the distance between each product and the ending location
    @return the list of distances to the end
    """
    def get_end_distances(self):
        return self.end_distances

    """
    Equals method for the class
    @param other: the TSPData that we want to evaluate for equality
    @return true if the two objects are equal
    """
    def __eq__(self, other):
        return self.distances == other.distances \
               and self.product_to_product == other.product_to_product \
               and self.product_to_end == other.product_to_end \
               and self.start_to_product == other.start_to_product \
               and self.spec == other.spec \
               and self.product_locations == other.product_locations

    """
    Persist object to file so that it can be reused later
    @param file_path: path to the location where the object should be stored
    """
    def write_to_file(self, file_path):
        pickle.dump(self, open(file_path, "wb"))

    """
    Write the action file based on a solution for the TSP problem
    @param product_order: a solution found for the TSP problem
    @param file_path: path to the location where the object should be stored
    """
    def write_action_file(self, product_order, file_path):
        total_length = self.start_distances[product_order[0]]
        for i in range(len(product_order) - 1):
            frm = product_order[i]
            to = product_order[i + 1]
            total_length += self.distances[frm][to]

        total_length += self.end_distances[product_order[len(product_order) - 1]] + len(product_order)

        string = ""
        string += str(total_length)
        string += ";\n"
        string += str(self.spec.get_start())
        string += ";\n"
        string += str(self.start_to_product[product_order[0]])
        string += "take product #"
        string += str(product_order[0] + 1)
        string += ";\n"

        for i in range(len(product_order) - 1):
            frm = product_order[i]
            to = product_order[i + 1]
            string += str(self.product_to_product[frm][to])
            string += "take product #"
            string += str(to + 1)
            string += ";\n"
        string += str(self.product_to_end[product_order[len(product_order) - 1]])

        f = open(file_path, "w")
        f.write(string)

    """
    Calculate the optimal routes between all of the individual products
    @param maze: the maze where we want to calculate "optimal" routes
    @return the "optimal" routes between all products in the form of a 2d array
    """
    def build_distance_matrix(self, aco):
        number_of_product = len(self.product_locations)
        product_to_product = []
        for i in range(number_of_product):
            product_to_product.append([])
            for j in range(number_of_product):
                start = self.product_locations[i]
                end = self.product_locations[j]
                product_to_product[i].append(
                    aco.find_shortest_route(PathSpecification(start, end))
                )
        return product_to_product

    """
    Calculate optimal route between the starting location and all products
    @param maze: the maze where we want to calculate "optimal" routes
    @return the optimal route from the starting location to products
    """
    def build_start_to_products(self, aco):
        start = self.spec.get_start()
        start_to_products = []
        for i in range(len(self.product_locations)):
            start_to_products.append(
                aco.find_shortest_route(PathSpecification(start, self.product_locations[i]))
            )
        return start_to_products

    """
    Calculate optimal route between all products and the ending location
    @param maze: the maze where we want to calculate "optimal" routes
    @return the optimal route from the products to the ending location
    """
    def build_products_to_end(self, aco):
        end = self.spec.get_end()
        products_to_end = []
        for i in range(len(self.product_locations)):
            products_to_end.append(
                aco.find_shortest_route(PathSpecification(self.product_locations[i], end))
            )
        return products_to_end

    """
    Load a TSPData object from a file
    @param file_path: the location of the file with a TSPData object
    @return the TSPData object from the file
    """
    @staticmethod
    def read_from_file(file_path):
        return pickle.load(open(file_path, "rb"))

    """
    Read a TSP problem specification based on a coordinate file and a product file
    @param coordinates: the path to the coordinate file
    @param product_file: the path to the product file
    @return the TSPData object with uninitiatilized routes
    """
    @staticmethod
    def read_specification(coordinates, product_file):
        try:
            f = open(product_file, "r")
            lines = f.read().splitlines()

            firstline = re.compile("[:,;]\\s*").split(lines[0])
            product_locations = []
            number_of_products = int(firstline[0])
            for i in range(number_of_products):
                line = re.compile("[:,;]\\s*").split(lines[i + 1])
                x = int(line[1])
                y = int(line[2])
                product_locations.append(Coordinate(x, y))
            spec = PathSpecification.read_coordinates(coordinates)
            return TSPData(product_locations, spec)
        except FileNotFoundError:
            print("Error reading file " + product_file)
            traceback.print_exc()
            sys.exit()
