import unittest
from src.find_kmp_string import *


class Test_some_methods(unittest.TestCase):

    def test_kmp_match(self):
        self.assertEqual(kmp_match("ababcbcbabcabdcabcabc", "abcabd"), [8])

    def test_kmp_match1(self):
        self.assertEqual(kmp_match("ababcbcbabcabdcabcabc", "abc"), [2, 8, 15, 18])

    def test_kmp_match2(self):
        self.assertEqual(kmp_match("ababcbcbabcabdcabcabc", "abcdeda"), [])

    def test_kmp_match3(self):
        self.assertEqual(kmp_match("ababcbcbabcabdcabcabc", "abca"), [8, 15])


if __name__ == "__main__":
    unittest.main()
