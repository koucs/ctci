#! env python
# -*- coding: utf-8 -*-

from binary_search_tree import create_tree, BstTreeNode
from typing import Optional, List
import sys, math, unittest


# ctci.4_6
# In order successor of a BST
# Date: 2020/09/20
# Filename: 4_6 
# Author: acto_mini


def inorder_successor_bst(current: BstTreeNode) -> Optional[BstTreeNode]:
    # 次のノードとは、該当のノード(current)の
    # 右側に部分木がある場合: 右側の部分木の一番左のノード
    # 右側に部分木がない場合 (currentが親ノードのleftであった場合): 親ノード
    # 右側に部分木がない場合 (currentが親ノードのrightであった場合): 親ノードからさらに親ノードを探索し、left/right判定

    if current.right is not None:
        next_node = current.right
        while next_node.left is not None:
            next_node = next_node.left
        return next_node
    elif current.parent == None:
        return None
    else:
        if current.parent.left == current:
            return current.parent
        elif current.parent.right == current:
            c = current
            p = current.parent
            while p is not None and p.left is not c:
                c = p
                p = p.parent
            return p


class Test(unittest.TestCase):
    def test_1(self):
        root = create_tree([3, 2, 4])
        self.assertEqual(inorder_successor_bst(root).data, 4)
        self.assertEqual(inorder_successor_bst(root.left).data, 3)
        self.assertEqual(inorder_successor_bst(root.right), None)
        return

    def test_2(self):
        root = create_tree([20, 10, 30, 5, 15, None, None, 3, 7, None, 17])
        self.assertEqual(inorder_successor_bst(root.left.left.right).data, 10)
        self.assertEqual(inorder_successor_bst(root.left.right.right).data, 20)
        return


if __name__ == '__main__':
    unittest.main()
