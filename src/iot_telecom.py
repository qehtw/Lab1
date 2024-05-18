import os


def read_input(file_name):
    """
    This function reads info from a CSV file.
    """
    input_info = []
    cur_path = os.path.dirname(__file__)
    resources_dir = os.path.join(cur_path, "..", "test", "resources")
    file_path = os.path.join(resources_dir, file_name)

    with open(file_path, "r") as file:
        for line in file:
            values = line.strip().split(",")
            input_info.append(values)

    return input_info


class DisjointSet:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            return x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x

def is_connected(disjoint_set):
    """
    Checks if all wells connected
    Returns True if all connected and False if doesn`t
    """
    num_roots = len(set(disjoint_set.find(node) for node in disjoint_set.parent))
    
    return num_roots == 1


def min_length_connection(connections):
    """
    This function calculates the minimal length of fiber
    """
    connections.sort(key=lambda x: int(x[2]))
    disjoint_set = DisjointSet()
    length = 0

    for edge in connections:
        well1, well2, distance = edge
        if disjoint_set.find(well1) != disjoint_set.find(well2):
            disjoint_set.union(well1, well2)
            length += int(distance)

    if not is_connected(disjoint_set):
        return -1

    return length


def calculate_minimal_length(file_name):
    """
    This function activates all code
    """
    connections = read_input(file_name)
    result = min_length_connection(connections)

    return result
