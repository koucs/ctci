#! env python
# -*- coding: utf-8 -*-

from tree import create_tree, TreeNode
from typing import Optional, List
import sys, math, unittest

# ctci.4_4
# 2分探索木が与えられたとき、同じ深さのノード同士の連結リストをアルゴリズム
# Date: 2020/09/20
# Filename: 4_4 
# Author: acto_mini

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]


def create_depth_list(root: TreeNode, nodes_list: List, depth: int):
    if root is None or root.data is None:
        return
    nodes = list()
    if len(nodes_list) == depth:
        nodes_list.append(nodes)
    else:
        nodes = nodes_list[depth]
    nodes.append(root)
    create_depth_list(root.left, nodes_list, depth + 1)
    create_depth_list(root.right, nodes_list, depth + 1)
    return


class Test(unittest.TestCase):
    def assertNode(self):
        return

    def test_1(self):
        result_list = []
        create_depth_list(create_tree([1, 2, 3, 4, 5, 6, 7, 8]), result_list, 0)
        self.assertEqual(len(result_list), 4)
        self.assertEqual([v.data for v in result_list[0]], [1])
        self.assertEqual([v.data for v in result_list[1]], [2, 3])
        self.assertEqual([v.data for v in result_list[2]], [4, 5, 6, 7])
        self.assertEqual([v.data for v in result_list[3]], [8])
        return


if __name__ == '__main__':
    unittest.main()
