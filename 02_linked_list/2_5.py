#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest
from linked_list import LinkedList, Node


# ctci.2_4
# Date: 2020/08/15
# Filename: 2_4 
# Author: acto_mini


def add(node1, node2, carry):
    if node1 == None and node2 == None and carry == 0:
        return None

    new_node = Node(0, None, None)

    sum = carry
    if node1 != None: sum += node1.value
    if node2 != None: sum += node2.value

    carry_next = sum // 10
    new_node.value = sum % 10

    if node1 is not None or node2 is not None or carry_next > 0:
        result = add(node1.next if node1 is not None else None,
                     node2.next if node2 is not None else None,
                     carry_next)
        new_node.next = result
    return new_node


class Test(unittest.TestCase):
    TEST_DATA = [
        (
            [
                LinkedList(values=[1, 2]),
                LinkedList(values=[2, 3])
            ],
            [3, 5]
        ),
        (
            [
                LinkedList(values=[5, 2]),
                LinkedList(values=[8, 3])
            ],
            [3, 6]
        ),
        (
            [
                LinkedList(values=[5, 2]),
                LinkedList(values=[8, 7])
            ],
            [3, 0, 1]
        )
    ]

    def test_1(self):
        for in_data, expected in self.TEST_DATA:
            result = add(in_data[0].head, in_data[1].head, 0)
            ans = []
            while result:
                ans.append(result.value)
                result = result.next
            self.assertEqual(expected, ans)


if __name__ == '__main__':
    unittest.main()
