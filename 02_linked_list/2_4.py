#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest
from linked_list import LinkedList


# ctci.2_4
# Date: 2020/08/15
# Filename: 2_4 
# Author: koucs

def partition(linked_list, n):
    before_list = LinkedList()
    after_list = LinkedList()
    node = linked_list.head
    while node:
        if node.value < n:
            before_list.add(node.value)
        else:
            after_list.add(node.value)
        node = node.next

    before_list.tail.next = after_list.head
    return before_list


class Test(unittest.TestCase):
    TEST_DATA = [
        ([LinkedList(values=[3, 4, 5, 1, 2]), 2], [1, 3, 4, 5, 2]),
        ([LinkedList(values=[3, 4, 5, 1, 2]), 5], [3, 4, 1, 2, 5])
    ]

    def test_1(self):
        for list, expected in self.TEST_DATA:
            actual = partition(list[0], list[1])
            result = [v.value for v in actual]
            self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
