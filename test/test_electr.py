import unittest
from src.elecrt import *


class Test_some_methods(unittest.TestCase):

    def test_electr(self):
        self.assertEqual(start_code('electr_input.txt'), 5.66)

    def test_electr1(self):
        self.assertEqual(start_code('electr_input1.txt'), 300.0)

    def test_electr2(self):
        self.assertEqual(start_code('electr_input2.txt'), 396.32)


if __name__ == "__main__":
    unittest.main()
