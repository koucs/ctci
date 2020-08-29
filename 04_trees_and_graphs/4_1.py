#! env python
# -*- coding: utf-8 -*-

import unittest
from tree import *


# ctci.4_1
# Date: 2020/08/29
# Filename: 4_1 
# Author: acto_mini

def is_balanced(root: TreeNode) -> bool:
    if root is None:
        return True
    diff_height: int = get_height(root.left) - get_height(root.right)
    if abs(diff_height) > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)


def is_balanced2(root: TreeNode) -> bool:
    return False if check_height(root) == -1 else True


class Test(unittest.TestCase):
    def test_1(self):

        t1 = create_tree([1, None, 2, 3])
        self.assertEqual(is_balanced(t1), False)
        self.assertEqual(is_balanced2(t1), False)

        t2 = create_tree([1, 2, 3])
        self.assertEqual(is_balanced(t2), True)
        self.assertEqual(is_balanced2(t2), True)

        t3 = create_tree([1, 2, 3, 4, 5])
        self.assertEqual(is_balanced(t3), True)
        self.assertEqual(is_balanced2(t3), True)


if __name__ == '__main__':
    unittest.main()
