#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

from linked_list import LinkedList


# ctci.2_3
# Date: 2020/08/15
# Filename: 2_3 
# Author: acto_mini

def delete_middle_node(node):
    if node == None or node.next == None:
        return
    node.value = node.next.value
    node.next = node.next.next
    return


class Test(unittest.TestCase):
    TEST_DATA = [
        ([LinkedList(values=[5, 4, 3, 2, 1]), 3], [2, 1, 5, 4, 3])
    ]

    def test_1(self):
        for in_data, expected in self.TEST_DATA:
            node = in_data[0].head
            for i in range(in_data[1]):
                node = node.next
            delete_middle_node(node)
            result = [v.value for v in in_data[0]]
            self.assertEqual(expected, result)

        return


if __name__ == '__main__':
    unittest.main()
