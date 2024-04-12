from src.find_notsorted_subarray import *
import unittest


class Test_some_methods(unittest.TestCase):
    
    def test_Check_if_sorted(self):
        self.assertEqual(Check_if_sorted([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]),False)

    def test_Check_if_sorted(self):
        self.assertEqual(Check_if_sorted([1, 2, 4, 7, 10, 11, 16, 18, 19]),(True))

    def test_max_in_new_arr(self):
        self.assertEqual(max_in_new_arr([7, 12, 6, 7]),(12))

    def test_min_in_new_arr(self):
        self.assertEqual(min_in_new_arr([7, 12, 6, 7]),(6))

if __name__ == '__main__':
    unittest.main()
