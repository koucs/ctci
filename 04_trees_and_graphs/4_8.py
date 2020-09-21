#! env python
# -*- coding: utf-8 -*-

from tree import create_tree, TreeNode
from typing import Optional, List
import sys, math, unittest

# 2つの部分木T1, T2のうち、T2がT1の部分木であるかの判定を行うアルゴリズム
# ctci.4_8
# Date: 2020/09/21
# Filename: 4_8 
# Author: koucs

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]


# T1のノードを順々に調べ、T2のルートと一致するノードが発見された場合に部分木判定を行う

def match(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
    if n1 == n2 == None:
        return True
    if n1 == None or n2 == None:
        return False
    if n1.data != n2.data:
        return False
    return match(n1.left, n2.left) and match(n1.right, n2.right)


def scan(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
    if n1 == None:
        return False

    if n1.data == n2.data and match(n1, n2):
        return True

    return scan(n1.left, n2) or scan(n1.right, n2)


def is_partial_tree(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
    if t2 == None:
        return True
    return scan(t1, t2)


class Test(unittest.TestCase):
    def test_1(self):
        t1 = create_tree([1, 2, 3, 4, 5, 6])
        t2 = create_tree([2, 4, 5])
        self.assertEqual(is_partial_tree(t1, t2), True)

        t2 = create_tree([2, 4])
        self.assertEqual(is_partial_tree(t1, t2), False)

        t2 = create_tree([4])
        self.assertEqual(is_partial_tree(t1, t2), True)

        self.assertEqual(is_partial_tree(None, t2), False)
        self.assertEqual(is_partial_tree(t1, None), True)

        return


if __name__ == '__main__':
    unittest.main()
