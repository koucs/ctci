#! env python
# -*- coding: utf-8 -*-

from tree import create_tree, TreeNode
from typing import Optional, List
import sys, math, unittest


# ctci.4_7
# Find common parent node between 2 tree nodes.
# Date: 2020/09/21
# Filename: 4_7 
# Author: acto_mini


def scan(root: TreeNode, target: TreeNode) -> bool:
    if root is None: return False
    if root == target: return True
    return scan(root.left, target) or scan(root.right, target)


def search_common_ancestor(root: TreeNode, node_a: TreeNode, node_b: TreeNode) -> Optional[TreeNode]:
    if root is None:
        return None
    if root == node_a or root == node_b:
        return root

    a_on_left = scan(root.left, node_a)
    b_on_right = scan(root.left, node_b)

    if a_on_left != b_on_right:
        return root

    next_child = root.left if a_on_left else root.right
    return search_common_ancestor(next_child, node_a, node_b)


def search(root: TreeNode, node_a: TreeNode, node_b: TreeNode) -> Optional[TreeNode]:
    if not scan(root, node_a) or not scan(root, node_b):
        return None
    return search_common_ancestor(root, node_a, node_b)


class Test(unittest.TestCase):
    def test_1(self):
        tree = create_tree([1, 2, 3, 4, 5, 6])
        node_a = tree.left.left
        node_b = tree.left.right
        expected = tree.left
        self.assertEqual(search(tree, node_a, node_b), expected)

        node_a = tree.right.left
        node_b = tree.right
        expected = tree.right
        self.assertEqual(search(tree, node_a, node_b), expected)

        node_a = tree.left.left
        node_b = tree.right
        expected = tree
        self.assertEqual(search(tree, node_a, node_b), expected)

        node_a = tree.left
        node_b = TreeNode(100)
        expected = None
        self.assertEqual(search(tree, node_a, node_b), expected)
        return


if __name__ == '__main__':
    unittest.main()
