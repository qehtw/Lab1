import unittest
from src.shortest_path import *


class TestBFSShortMinesPath(unittest.TestCase):
    def test_normal_case(self):
        find_shortest_safe_path("input.txt", "output.txt")
        cur_path = os.path.dirname(__file__)
        resources_dir = os.path.join(cur_path, "resources")
        output_file_path = os.path.join(resources_dir, "output.txt")
        with open(output_file_path, "r") as file:
            first_line = file.readline()
            numbers = first_line.split()

        self.assertEqual(int(numbers[0]), 12)
