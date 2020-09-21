from typing import List


class BstTreeNode:
    def __init__(self, data, parent):
        self.parent = parent
        self.left = None
        self.right = None
        self.data = data
        return


def create_tree(a: List) -> BstTreeNode:
    """
    input: [1, 2, 3]
       1
      / \
     2   3
    """
    queue = []
    if not a:
        return BstTreeNode(None, None)
    root_data = a.pop(0)
    root = BstTreeNode(root_data, None)
    queue.append(root)

    while queue:
        node = queue.pop(0)
        left_data = a.pop(0) if a else None  # Pop if `a` is not empty
        right_data = a.pop(0) if a else None
        if left_data is not None:
            left = BstTreeNode(left_data, node)
            node.left = left
            queue.append(left)
        if right_data is not None:
            right = BstTreeNode(right_data, node)
            node.right = right
            queue.append(right)

    return root
