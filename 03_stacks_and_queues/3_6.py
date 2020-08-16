#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest


# ctci.3_6
# Date: 2020/08/16
# Filename: 3_6 
# Author: acto_mini

class Stack():
    def __init__(self):
        self.stack = []
        return

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


def sort_desc(s1: Stack):
    s2 = Stack()

    while not s1.is_empty():
        tmp = s1.pop()
        while not s2.is_empty() and s2.peek() < tmp:
            s1.push(s2.pop())
        s2.push(tmp)
    return s2


class Test(unittest.TestCase):
    def test_1(self):
        s = Stack()
        s.push(3)
        s.push(4)
        s.push(1)
        s.push(2)
        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.pop())
        self.assertEqual(4, s.pop())
        self.assertEqual(3, s.pop())

        s = Stack()
        s.push(3)
        s.push(4)
        s.push(1)
        s.push(2)

        # test target
        s = sort_desc(s)

        self.assertEqual(1, s.pop())
        self.assertEqual(2, s.pop())
        self.assertEqual(3, s.pop())
        self.assertEqual(4, s.pop())

        return


if __name__ == '__main__':
    unittest.main()
