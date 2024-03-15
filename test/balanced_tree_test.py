from balanced_tree import *
import unittest


class Test_some_methods(unittest.TestCase):
    
    def test_is_tree_balanced(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        self.assertEqual(is_tree_balanced(root),True)

    def test2_is_tree_balanced(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        self.assertEqual(is_tree_balanced(root),False)


if __name__ == '__main__':
    unittest.main()
