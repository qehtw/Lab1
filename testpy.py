from py import *
import unittest


class Test_some_methods(unittest.TestCase):
    
    def test_find_start_pos(self):
        self.assertEqual(find_start_pos([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]),3)

    def test_find_last_pos(self):
         self.assertEqual(find_last_pos([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]),9)
    
    def test_Check_if_sorted(self):
        self.assertEqual(Check_if_sorted([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]),False )

    def test_Check_if_sorted(self):
        self.assertEqual(Check_if_sorted([1, 2, 4, 7, 10, 11, 16, 18, 19]),True)

    def test_finder(self):
        self.assertEqual(finder([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]),(3 , 9))
    
    def test_finder(self):
        self.assertEqual(finder([2,1,5,6,7,7,1,9,2]) , "not sorted at all")


if __name__ == '__main__':
    unittest.main()