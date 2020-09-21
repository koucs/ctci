#! env python
# -*- coding: utf-8 -*-

from tree import create_tree, TreeNode
from typing import Optional, List
import sys, math, unittest


# ctci.4_9
# Date: 2020/09/21
# Filename: 4_9 
# Author: koucs

# 4.9: 各ノードにある値を持ったに分岐が与えられたとき、合計値が与えられた値になる全ての経路を出力するアルゴリズム
# 経路の始まりと終わりは、k他方のノードがもう片方の祖先となっていること

def find_sum(current: TreeNode, sum: int, path: List, result: []):
    if current is None:
        return []
    path.append(current.data)

    i = len(path) - 1
    t = 0
    while i >= 0:
        t += path[i]
        if t == sum:
            result.append(path[i:])
        i -= 1

    find_sum(current.left, sum, path, result)
    find_sum(current.right, sum, path, result)
    path.pop()


def find(root: TreeNode, sum: int) -> List:
    result = []
    find_sum(root, sum, [], result)
    return result


class Test(unittest.TestCase):
    def test_1(self):
        tree = create_tree([1, 2, 3, 4])
        self.assertEqual(find(tree, 3), [[1, 2], [3]])

        tree = create_tree([1, -2, -3, 4, 5, 4])
        self.assertEqual(find(tree, 3), [[1, -2, 4], [-2, 5]])
        return


if __name__ == '__main__':
    unittest.main()
