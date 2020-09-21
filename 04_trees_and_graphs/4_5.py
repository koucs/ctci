#! env python
# -*- coding: utf-8 -*-

from tree import create_tree, TreeNode
from typing import Optional, List
import sys, math, unittest


# ctci.4_5
# To see if a binary tree is a binary search tree,
# Date: 2020/09/20
# Filename: 4_5 
# Author: koucs

def check_BST(current: Optional[TreeNode], min: int, max: int) -> bool:
    if current is None:
        return True
    if current.data < min or current.data >= max:
        return False
    if not check_BST(current.left, min, current.data) or not check_BST(current.right, current.data, max):
        return False
    return True


def check(root: TreeNode) -> bool:
    MAX = sys.maxsize
    MIN = MAX * -1
    return check_BST(root, MIN, MAX)


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(check(create_tree([2, 1, 3])), True)
        self.assertEqual(check(create_tree([1, 3, 2, 4, 5])), False)
        self.assertEqual(check(create_tree([20, 10, 30, None, 25])), False)
        self.assertEqual(check(create_tree([20, 10, 30, 5, 15, None, None, 3, 7, None, 17])), True)
        return


if __name__ == '__main__':
    unittest.main()
