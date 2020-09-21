#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest


# ctci.2_1
# Date: 2020/08/15
# Filename: 2_1 
# Author: koucs

class Node:

    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        for v in values:
            self.add(v)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def delete_duplicates(self):
        value_list = []
        current = self.head
        previous = None

        while current:
            if current.value in value_list and previous is not None:

                previous.next = current.next
            else:
                value_list.append(current.value)
                previous = current
            current = current.next
        return


class Test(unittest.TestCase):
    TEST_DATA = [
        (LinkedList(values=[1, 2, 3, 4, 4]), [1, 2, 3, 4]),
        (LinkedList(values=[1, 1, 2, 4, 3, 4, 4]), [1, 2, 4, 3]),
        (LinkedList(values=[1, 2, 4, 3, 3, 3, 1]), [1, 2, 4, 3])
    ]

    def test_1(self):
        for list, expected in self.TEST_DATA:
            list.delete_duplicates()
            result = [v.value for v in list]
            self.assertEqual(expected, result)
        return


if __name__ == '__main__':
    unittest.main()
