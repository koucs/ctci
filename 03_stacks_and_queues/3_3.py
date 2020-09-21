#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest


# ctci.3_3
# Date: 2020/08/16
# Filename: 3_3 
# Author: koucs

class SetStack():
    def __init__(self, size):
        self.size = size
        self.stacks = []
        self.stacks.append([])

    def push(self, val):
        stack = self.stacks[-1]

        if len(stack) >= self.size:
            self.stacks.append([val])
        else:
            stack.append(val)

    def pop(self):
        if len(self.stacks[-1]) > 0:
            return self.stacks[-1].pop()
        else:
            self.stacks.pop()
            return self.stacks[-1].pop()


class Test(unittest.TestCase):
    def test_1(self):
        stack = SetStack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(6)
        stack.push(7)

        self.assertEqual(7, stack.pop())
        self.assertEqual(6, stack.pop())
        self.assertEqual(5, stack.pop())
        self.assertEqual(4, stack.pop())
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())
        return


if __name__ == '__main__':
    unittest.main()
