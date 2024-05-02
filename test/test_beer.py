import unittest
from src.beer import *


class Test_some_methods(unittest.TestCase):

    def test_beers(self):
        self.assertEqual(beers(2, 2, "YN NY"), 2)

    def test2_beers(self):
        self.assertEqual(beers(6, 3, "YYY YYY YYY YYY YYY YYY"), 1)

    def test3_beers(self):
        self.assertEqual(beers(6, 3, "YNN YNY YNY NYY NYY NYN"), 2)

    def test4_beers(self):
        self.assertEqual(beers(4, 1, "Y Y Y Y"), 1)

    def test5_beers(self):
        self.assertEqual(beers(4, 1, "YN YYY YN YN"), 1)


if __name__ == "__main__":
    unittest.main()
