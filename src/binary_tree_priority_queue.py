class Node:
    def __init__(self, value, priority, right=None, left=None):
        self.value = value
        self.priority = priority
        self.right = right
        self.left = left


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_number(self, value, priority):
        new_node = Node(value, priority)
        if self.root:
            self._add_number(self.root, new_node)
        else:
            self.root = new_node

    def _add_number(self, current_node, new_node):
        if new_node.priority < current_node.priority:
            if current_node.right:
                self._add_number(current_node.right, new_node)
            else:
                current_node.right = new_node
        else:
            if current_node.left:
                self._add_number(current_node.left, new_node)
            else:
                current_node.left = new_node


    def pop_element(self):
        if self.root is None:
            return
        if self.root.left is None:
            value = self.root.value
            self.root = self.root.right
            return value
        parent_node = self.root
        child_node = parent_node.left
        while child_node.left:
            parent_node = child_node
            child_node = parent_node.left
        value = child_node.value
        parent_node.left = child_node.right
        return value

    def show_in_order(self):
        if self.root is None:
            return None
        result = []
        self._show_in_order(result, self.root)
        return result

    def _show_in_order(self,result, node):
        if node.left:
            self._show_in_order(result, node.left)
        result.append((node.value, node.priority))
        if node.right:
            self._show_in_order(result, node.right)
