#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest


# ctci.3_5
# Date: 2020/08/16
# Filename: 3_5 
# Author: koucs

class Stack():
    def __init__(self):
        self.stack = []
        return

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)


class MyQueue():
    def __init__(self):
        self._in_stack = Stack()
        self._out_stack = Stack()

    def enqueue(self, val):
        self._in_stack.push(val)

    def dequeue(self):
        self._shift()
        return self._out_stack.pop()

    def _shift(self):
        while self._in_stack.size() > 0:
            self._out_stack.push(self._in_stack.pop())


class Test(unittest.TestCase):
    def test_1(self):
        queue = MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(3, queue.dequeue())
        self.assertEqual(4, queue.dequeue())
        return


if __name__ == '__main__':
    unittest.main()
