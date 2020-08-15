#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest
from linked_list import LinkedList

# ctci.2_2
# Date: 2020/08/15
# Filename: 2_2 
# Author: acto_mini


def get_by_bottom(node, n):
    if node == None:
        return 0, None
    cnt, result = get_by_bottom(node.next, n)
    if (cnt + 1) == n:
        print(node.value)
        result = node.value
    return cnt + 1, result


class Test(unittest.TestCase):
    TEST_DATA = [
        ([LinkedList(values=[1, 2, 3, 4, 5]), 2], 4),
        ([LinkedList(values=[1, 2, 3, 4, 5]), 1], 5),
        ([LinkedList(values=[1, 2, 3, 4, 5]), 5], 1)
    ]

    def test_1(self):
        for in_data, expected in self.TEST_DATA:
            _, result = get_by_bottom(in_data[0].head, in_data[1])
            self.assertEqual(expected, result)
        return


if __name__ == '__main__':
    unittest.main()
