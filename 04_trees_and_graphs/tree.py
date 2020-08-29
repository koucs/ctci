from typing import List


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        return


def get_height(root: TreeNode) -> int:
    if (root is None):
        return 0
    return max(get_height(root.left),
               get_height(root.right)) + 1


def check_height(root: TreeNode) -> int:
    if root is None:
        return 0
    left_height: int = check_height(root.left)
    if left_height == -1:
        return -1
    right_height: int = check_height(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1
    else:
        return max(left_height, right_height) + 1


def create_tree(a: List) -> TreeNode:
    """
    input: [1, 2, 3]
       1
      / \
     2   3
    """
    queue = []
    if not a:
        return TreeNode(None)
    root_data = a.pop(0)
    root = TreeNode(root_data)
    queue.append(root)

    while queue:
        node = queue.pop(0)
        left_data = a.pop(0) if a else None  # Pop if `a` is not empty
        right_data = a.pop(0) if a else None
        if left_data is not None:
            left = TreeNode(left_data)
            node.left = left
            queue.append(left)
        if right_data is not None:
            right = TreeNode(right_data)
            node.right = right
            queue.append(right)

    return root
