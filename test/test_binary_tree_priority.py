import unittest

from src.binary_tree_priority_queue import *


class TestPriorityQueue(unittest.TestCase):
    def test_add_number(self):
        queue = BinaryTree()
        queue.add_number("SomeTask 1", 5)
        queue.add_number("SomeTask 2", 8)
        queue.add_number("SomeTask 3", 3)
        queue.add_number("SomeTask 4", 10)
        queue.add_number("SomeTask 5", 9)
        queue.add_number("SomeTask 6", 4)
        queue.add_number("SomeTask 7", 1)
        expected_queue = [
            ("SomeTask 4", 10),
            ("SomeTask 5", 9),
            ("SomeTask 2", 8),
            ("SomeTask 1", 5),
            ("SomeTask 6", 4),
            ("SomeTask 3", 3),
            ("SomeTask 7", 1),
        ]
        self.assertEqual(queue.show_in_order(), expected_queue)

    def test_pop(self):
        queue = BinaryTree()
        queue.add_number("SomeTask 1", 5)
        queue.add_number("SomeTask 2", 8)
        queue.add_number("SomeTask 3", 3)
        queue.add_number("SomeTask 4", 10)
        queue.add_number("SomeTask 5", 9)
        queue.add_number("SomeTask 6", 4)
        queue.add_number("SomeTask 7", 1)

        popped_task = queue.pop_element()
        self.assertEqual(popped_task, "SomeTask 4")
        popped_task = queue.pop_element()
        self.assertEqual(popped_task, "SomeTask 5")

        expected_queue = [
            ("SomeTask 2", 8),
            ("SomeTask 1", 5),
            ("SomeTask 6", 4),
            ("SomeTask 3", 3),
            ("SomeTask 7", 1),
        ]
        self.assertEqual(queue.show_in_order(), expected_queue)

    def test_pop_empty_queue(self):
        queue = BinaryTree()
        popped_task = queue.pop_element()
        self.assertIsNone(popped_task)

    def test_pop_single_task(self):
        queue = BinaryTree()
        queue.add_number("SomeTask 1", 5)
        popped_task = queue.pop_element()
        self.assertEqual(popped_task, "SomeTask 1")
        self.assertEqual(queue.show_in_order(), None)


if __name__ == "__main__":
    unittest.main()