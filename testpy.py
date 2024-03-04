from Cards_on_board import *
import unittest


class Test_some_methods(unittest.TestCase):
    
    def test_Size_of_board(self):
        self.assertEqual(Size_of_board(10 , 2 ,3), 9)

    def test_Size_of_board(self):
        self.assertEqual(Size_of_board(4 , 1 ,1), 2)


if __name__ == '__main__':
    unittest.main()