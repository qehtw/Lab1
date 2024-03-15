class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def _is_tree_balanced(node: BinaryTree) -> bool:
    if node is None:
        return True, 0 , 0
    
    node_left_balance , node_left_height_left , node_left_height_right = _is_tree_balanced(node.left)
    node_right_balance , node_right_height_left , node_right_height_right = _is_tree_balanced(node.right)


    if abs(node_right_height_right - node_right_height_left) <= 1 and  abs(node_left_height_right - node_left_height_left) <= 1 and node_left_balance and node_right_balance and abs(max(node_left_height_left , node_left_height_right) - max(node_right_height_left , node_right_height_right)) <= 1:
         return True ,max(node_left_height_left , node_left_height_right) + 1 , max(node_right_height_left , node_right_height_right) + 1
    
    return False , max(node_left_height_left , node_left_height_right) + 1 , max(node_right_height_left , node_right_height_right) + 1
    

def is_tree_balanced(node: BinaryTree) -> bool:
    result, *_ = _is_tree_balanced(node)
    return result



root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)

print(is_tree_balanced(root))
