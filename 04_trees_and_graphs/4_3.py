#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from tree import create_tree, TreeNode
from typing import Optional
import math, unittest


# 昇順にソートされた配列が与えられたとき、高さが最小になる二分探索木を作るアルゴリズム
# ctci.4_3
# Date: 2020/09/20
# Filename: 4_3 
# Author: koucs


def create_minimal_BST(arr: list, start: int, end: int) -> Optional[TreeNode]:
    if end < start:
        return None
    mid = math.ceil((start + end) / 2)
    mid_node = TreeNode(arr[mid])
    mid_node.left = create_minimal_BST(arr, start, mid - 1)
    mid_node.right = create_minimal_BST(arr, mid + 1, end)
    return mid_node


class Test(unittest.TestCase):
    def test_1(self):
        arr = [1, 2, 3, 4, 5, 10, 30]
        node = create_minimal_BST(arr, 0, len(arr) - 1)
        self.assertEqual(node.data, 4)
        self.assertEqual(node.left.data, 2)
        self.assertEqual(node.left.left.data, 1)
        self.assertEqual(node.left.right.data, 3)

        self.assertEqual(node.right.data, 10)
        self.assertEqual(node.right.left.data, 5)
        self.assertEqual(node.right.right.data, 30)
        return

    def test_2(self):
        arr = [2, 3, 4, 5, 10, 30]
        node = create_minimal_BST(arr, 0, len(arr) - 1)
        self.assertEqual(node.data, 5)
        self.assertEqual(node.left.data, 3)
        self.assertEqual(node.left.left.data, 2)
        self.assertEqual(node.left.right.data, 4)

        self.assertEqual(node.right.data, 30)
        self.assertEqual(node.right.left.data, 10)
        self.assertEqual(node.right.right, None)

        return

    def test_3(self):
        arr = [10, 30]
        node = create_minimal_BST(arr, 0, len(arr) - 1)
        self.assertEqual(node.data, 30)
        self.assertEqual(node.left.data, 10)
        self.assertEqual(node.right, None)

        return


if __name__ == '__main__':
    unittest.main()
