class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_number(self, value, priority):
        if self.root is None:
            self.root = Node(value, priority)
        else:
            self._add_number(self.root, value, priority)

    def _add_number(self, node, value, priority):
        if priority >= node.priority:
            if node.left is None:
                node.left = Node(value, priority)
            else:
                self._add_number(node.left, value, priority)
        else:
            if node.right is None:
                node.right = Node(value, priority)
            else:
                self._add_number(node.right, value, priority)

    def find_max_priority(self):
        node = self.root
        while node.left:
            node = node.left
        return (node.priority)
            

    def pop_element(self):
        if self.root is None:
            return None
        self.root = self._pop_element(self.root)

    def _pop_element(self, node):
        if node.left is None:
            return node.right
        else:
            node.left = self._pop_element(node.left)
            return node



    def show_in_order(self):
        self._show_in_order(self.root)

    def _show_in_order(self, node):
        if node:
            self._show_in_order(node.left)
            print(f"Priority: {node.priority}")
            self._show_in_order(node.right)
